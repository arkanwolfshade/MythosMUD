"""
Unit tests for DEFAULT_LOG_CATEGORIES.

Regression coverage for #687: the "infrastructure" category was removed after
server/infrastructure/ (its only possible logger source) was deleted as dead code.
Without this entry gone, _setup_category_handlers would keep creating an empty
infrastructure.log on every server startup.
"""

from server.structured_logging.logging_file_categories import DEFAULT_LOG_CATEGORIES


def test_infrastructure_category_removed() -> None:
    """No "infrastructure" category: server/infrastructure/ (its only logger source) is gone (#687)."""
    assert "infrastructure" not in DEFAULT_LOG_CATEGORIES


def test_no_category_still_references_infrastructure_module() -> None:
    """No surviving category's logger-name list should point at the deleted server.infrastructure package."""
    for category, logger_names in DEFAULT_LOG_CATEGORIES.items():
        assert not any(name.startswith("server.infrastructure") for name in logger_names), (
            f"category {category!r} still references the deleted server.infrastructure package"
        )
