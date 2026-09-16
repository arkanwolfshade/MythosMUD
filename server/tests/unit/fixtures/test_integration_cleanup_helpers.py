"""Regression tests for `_should_preserve_table_on_cleanup` (#811).

The migration ledger table changed name when the project adopted dbmate: `alembic_version`
(Alembic, never actually wired up) became `schema_migrations` (dbmate). This pure helper is what
`_delete_mutable_integration_test_rows` consults to decide what `db_cleanup` may truncate between
integration tests, so a wrong table name here is a silent behavior change, not a crash.
"""

from __future__ import annotations

import pytest

from server.tests.fixtures.integration import (
    _REFERENCE_SEED_TABLES,  # pyright: ignore[reportPrivateUsage]
    _should_preserve_table_on_cleanup,  # pyright: ignore[reportPrivateUsage]
)


def test_preserves_the_dbmate_migration_ledger() -> None:
    """schema_migrations (dbmate, #811) must survive db_cleanup."""
    assert _should_preserve_table_on_cleanup("schema_migrations") is True


def test_no_longer_special_cases_the_unused_alembic_table_name() -> None:
    """Alembic was scaffolded but never wired up (no alembic.ini/env.py, not a dependency) and
    was removed in #811 -- alembic_version never existed in any MythosMUD database, so it must
    not be preserved (nor, more importantly, silently created an expectation of)."""
    assert _should_preserve_table_on_cleanup("alembic_version") is False


@pytest.mark.parametrize("table_name", sorted(_REFERENCE_SEED_TABLES))
def test_preserves_every_reference_seed_table(table_name: str) -> None:
    """World topology and professions must survive cleanup so procedure/E2E tests keep seed data."""
    assert _should_preserve_table_on_cleanup(table_name) is True


@pytest.mark.parametrize("table_name", ["players", "users", "player_effects", "quest_instances"])
def test_does_not_preserve_mutable_player_tables(table_name: str) -> None:
    """Player-generated rows are exactly what db_cleanup exists to truncate."""
    assert _should_preserve_table_on_cleanup(table_name) is False
