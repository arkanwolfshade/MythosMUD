"""#1006: player.py server defaults are typed func.* calls, and still render the same Postgres DDL as the old text()."""

import pytest
from sqlalchemy import Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable

from server.models.player import PlayerChannelPreferences, PlayerExploration, PlayerInventory


def _default_of(table: Table, column: str) -> str:
    ddl = str(CreateTable(table).compile(dialect=postgresql.dialect()))
    line = next(line for line in ddl.splitlines() if line.strip().startswith(f"{column} "))
    return line.split("DEFAULT ", 1)[1].split(" NOT NULL")[0].strip().rstrip(",")


@pytest.mark.parametrize(
    ("table", "column", "expected"),
    [
        (PlayerChannelPreferences.__table__, "created_at", "CURRENT_TIMESTAMP"),
        (PlayerChannelPreferences.__table__, "updated_at", "CURRENT_TIMESTAMP"),
        (PlayerInventory.__table__, "created_at", "CURRENT_TIMESTAMP"),
        (PlayerExploration.__table__, "id", "gen_random_uuid()"),
        (PlayerExploration.__table__, "explored_at", "now()"),
    ],
)
def test_server_default_renders_the_same_ddl(table: Table, column: str, expected: str) -> None:
    assert _default_of(table, column) == expected
