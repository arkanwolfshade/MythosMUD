"""
Unit tests for DEFAULT_LOG_CATEGORIES.

Regression coverage for #687: the "infrastructure" category was removed after
server/infrastructure/ (its only possible logger source) was deleted as dead code.
Without this entry gone, _setup_category_handlers would keep creating an empty
infrastructure.log on every server startup.
"""

import logging
from pathlib import Path

import server
from server.structured_logging.logging_file_categories import (
    DEFAULT_LOG_CATEGORIES,
    LoggerNameFilter,
    add_handler_to_loggers,
)


def test_infrastructure_category_removed() -> None:
    """No "infrastructure" category: server/infrastructure/ (its only logger source) is gone (#687)."""
    assert "infrastructure" not in DEFAULT_LOG_CATEGORIES


def test_no_category_still_references_infrastructure_module() -> None:
    """No surviving category's logger-name list should point at the deleted server.infrastructure package."""
    for category, logger_names in DEFAULT_LOG_CATEGORIES.items():
        assert not any(name.startswith("server.infrastructure") for name in logger_names), (
            f"category {category!r} still references the deleted server.infrastructure package"
        )


def test_persistence_category_does_not_reference_deleted_persistence_layer_class() -> None:
    """#60 audit: the sync `PersistenceLayer` class was deleted 2025-12-08 (32839025b); all
    code uses AsyncPersistenceLayer now. The "persistence" category's logger-name list must not
    carry a bare "PersistenceLayer" entry -- that name matches no logger emitted by the current
    codebase, so it was dead routing left behind by the class removal."""
    assert "PersistenceLayer" not in DEFAULT_LOG_CATEGORIES["persistence"]


def test_realtime_module_loggers_match_communications_category() -> None:
    """#297: get_logger(__name__) in server/realtime/*.py produces "server.realtime.<module>",
    not bare "realtime.<module>" -- the "communications" category's prefix list must include
    "server.realtime", or every server/realtime/ log line (e.g. disconnect_grace_period.py's
    "Starting grace period for player") silently reaches no log file at all."""
    logger_filter = LoggerNameFilter(DEFAULT_LOG_CATEGORIES["communications"])
    record = logging.LogRecord(
        name="server.realtime.disconnect_grace_period",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="Starting grace period for player",
        args=(),
        exc_info=None,
    )
    assert logger_filter.filter(record) is True


def test_inventory_category_covers_every_container_and_inventory_service_module() -> None:
    """#688: DEFAULT_LOG_CATEGORIES["inventory"] must list every server/services/ module whose
    logs belong in inventory.log, by prefix (container*, inventory*, wearable_container*,
    equipment*). LoggerNameFilter only matches a listed prefix or "<prefix>.", so a module that
    get_logger(__name__)s under a name absent from this list silently reaches no inventory log
    file (the container_service_* split modules regressed exactly this way -- see #688 PR). This
    globs the actual files instead of hardcoding names so the next split is caught automatically."""
    services_dir = Path(server.__file__).parent / "services"
    patterns = ("container*.py", "inventory*.py", "wearable_container*.py", "equipment*.py")
    module_names = sorted(
        {f"server.services.{path.stem}" for pattern in patterns for path in services_dir.glob(pattern)}
    )
    assert module_names, "expected to find inventory-related modules under server/services/"

    logger_filter = LoggerNameFilter(DEFAULT_LOG_CATEGORIES["inventory"])
    for module_name in module_names:
        record = logging.LogRecord(
            name=module_name,
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg="probe",
            args=(),
            exc_info=None,
        )
        assert logger_filter.filter(record) is True, (
            f"{module_name!r} is not covered by DEFAULT_LOG_CATEGORIES['inventory'] -- "
            "its logs would silently miss inventory.log"
        )


def test_inventory_category_also_catches_equip_unequip_command_logs() -> None:
    """#688: server/commands/inventory_equip_command.py and inventory_unequip_command.py already
    log "Item equipped"/"Item unequipped" at INFO with full player/slot/item context -- their
    logger name only matched the "commands" category, so that visibility never reached
    inventory.log. Listing these two modules in the "inventory" category too dual-routes that
    existing logging into inventory.log alongside commands.log, without duplicating log calls."""
    logger_filter = LoggerNameFilter(DEFAULT_LOG_CATEGORIES["inventory"])
    for module_name, event in (
        ("server.commands.inventory_equip_command", "Item equipped"),
        ("server.commands.inventory_unequip_command", "Item unequipped"),
    ):
        record = logging.LogRecord(
            name=module_name,
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg=event,
            args=(),
            exc_info=None,
        )
        assert logger_filter.filter(record) is True, (
            f"{module_name!r} is not covered by DEFAULT_LOG_CATEGORIES['inventory']"
        )


def _reset_logger(prefix: str) -> None:
    """Undo add_handler_to_loggers' effects on both loggers it touches for a given prefix."""
    for name in (prefix, f"server.{prefix}"):
        target = logging.getLogger(name)
        target.handlers.clear()
        target.setLevel(logging.NOTSET)


def test_npc_loggers_suppressed_to_info_in_e2e_test_regardless_of_debug_level() -> None:
    """#297/#610: NPC behavior-engine/threading debug lines fire continuously enough in a
    long-running e2e session to rotate connection-lifecycle events out of the retained logs
    within minutes (the investigation this guards against lost real time to exactly that). NPC
    loggers must be forced to INFO in e2e_test even though LOGGING_LEVEL=DEBUG there."""
    prefix = "test_npc_e2e_suppression"
    handler = logging.NullHandler()
    try:
        add_handler_to_loggers(handler, [prefix], "npc", environment="e2e_test", log_level="DEBUG")
        assert logging.getLogger(prefix).level == logging.INFO
    finally:
        _reset_logger(prefix)


def test_npc_loggers_keep_debug_level_in_local_environment() -> None:
    """The e2e-only suppression must not leak into local development, where full NPC debug
    detail is exactly what LOGGING_LEVEL=DEBUG is asking for."""
    prefix = "test_npc_local_debug"
    handler = logging.NullHandler()
    try:
        add_handler_to_loggers(handler, [prefix], "npc", environment="local", log_level="DEBUG")
        assert logging.getLogger(prefix).level == logging.DEBUG
    finally:
        _reset_logger(prefix)


def test_combat_loggers_still_get_debug_level_in_e2e_test() -> None:
    """Regression guard: the new npc-specific e2e branch must not shadow the existing
    combat-in-DEBUG-environments special case it sits next to."""
    prefix = "test_combat_e2e_debug"
    handler = logging.NullHandler()
    try:
        add_handler_to_loggers(handler, [prefix], "combat", environment="e2e_test", log_level="DEBUG")
        assert logging.getLogger(prefix).level == logging.DEBUG
    finally:
        _reset_logger(prefix)
