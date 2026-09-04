"""
Unit tests for DEFAULT_LOG_CATEGORIES.

Regression coverage for #687: the "infrastructure" category was removed after
server/infrastructure/ (its only possible logger source) was deleted as dead code.
Without this entry gone, _setup_category_handlers would keep creating an empty
infrastructure.log on every server startup.
"""

import logging

from server.structured_logging.logging_file_categories import DEFAULT_LOG_CATEGORIES, LoggerNameFilter


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
