"""
Unit tests for DEFAULT_LOG_CATEGORIES.

Regression coverage for #687: the "infrastructure" category was removed after
server/infrastructure/ (its only possible logger source) was deleted as dead code.
Without this entry gone, _setup_category_handlers would keep creating an empty
infrastructure.log on every server startup.
"""

import logging

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
