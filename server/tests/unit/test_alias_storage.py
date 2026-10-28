"""Unit tests for AliasStorage (#680): validation, row mapping, and DB-failure fallbacks.

The procedures themselves are exercised against PostgreSQL in
server/tests/integration/test_player_aliases_and_mutes_db.py.
"""

# pyright: reportPrivateUsage=false

from datetime import UTC, datetime, timedelta, timezone
from types import SimpleNamespace

import pytest
from sqlalchemy import TextClause
from sqlalchemy.exc import OperationalError

from server.alias_storage import MAX_ALIASES_PER_PLAYER, AliasStorage, _row_to_alias


@pytest.mark.parametrize(
    ("name", "valid"),
    [
        ("sit", True),
        ("go_north2", True),
        ("", False),
        ("2go", False),
        ("has space", False),
        ("x" * 21, False),
        ("ALIAS", False),
        ("help", False),
    ],
)
def test_validate_alias_name(name: str, valid: bool) -> None:
    assert AliasStorage().validate_alias_name(name) is valid


@pytest.mark.parametrize(
    ("command", "valid"),
    [("look", True), ("say hi there", True), ("", False), ("x" * 201, False), ("unalias x", False)],
)
def test_validate_alias_command(command: str, valid: bool) -> None:
    assert AliasStorage().validate_alias_command(command) is valid


def test_row_to_alias_stores_naive_utc() -> None:
    aware = datetime(2026, 9, 28, 12, 0, tzinfo=timezone(timedelta(hours=-7)))
    alias = _row_to_alias(SimpleNamespace(id="abc", name="sit", command="/sit", created_at=aware, updated_at=aware))
    assert alias.id == "abc"
    assert alias.created_at == datetime(2026, 9, 28, 19, 0)
    assert alias.created_at.tzinfo is None
    assert alias.updated_at == aware.astimezone(UTC).replace(tzinfo=None)


def _broken_session_maker() -> object:
    raise OperationalError("SELECT 1", {}, Exception("db down"))


@pytest.mark.asyncio
async def test_database_errors_degrade_to_no_alias(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("server.alias_storage.get_session_maker", _broken_session_maker)
    storage = AliasStorage()

    assert await storage.get_player_aliases("Someone") == []
    assert await storage.get_alias("Someone", "sit") is None
    assert await storage.create_alias("Someone", "sit", "/sit") is None
    assert await storage.remove_alias("Someone", "sit") is False
    assert await storage.delete_player_aliases_by_id("00000000-0000-0000-0000-000000000000") is False


@pytest.mark.asyncio
async def test_create_alias_rejects_invalid_input_without_touching_db(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("server.alias_storage.get_session_maker", _broken_session_maker)
    storage = AliasStorage()

    assert await storage.create_alias("Someone", "help", "look") is None
    assert await storage.create_alias("Someone", "ok", "") is None


class _Result:
    def __init__(self, rows: list[object], scalar: object) -> None:
        self._rows: list[object] = rows
        self._scalar: object = scalar

    def all(self) -> list[object]:
        return self._rows

    def scalar(self) -> object:
        return self._scalar


class _Session:
    """Just enough AsyncSession for AliasStorage: execute, commit, async context manager."""

    def __init__(self, rows: list[object] | None = None, scalar: object = None) -> None:
        self.result: _Result = _Result(rows or [], scalar)
        self.executed: list[tuple[str, dict[str, object]]] = []
        self.commits: int = 0

    async def execute(self, stmt: TextClause, params: dict[str, object] | None = None) -> _Result:
        self.executed.append((str(stmt), params or {}))
        return self.result

    async def commit(self) -> None:
        self.commits += 1

    async def __aenter__(self) -> "_Session":
        return self

    async def __aexit__(self, *_exc: object) -> None:
        return None


def _use_session(monkeypatch: pytest.MonkeyPatch, session: _Session) -> None:
    monkeypatch.setattr("server.alias_storage.get_session_maker", lambda: lambda: session)


def _alias_row(name: str, command: str) -> SimpleNamespace:
    now = datetime(2026, 9, 28, 12, 0, tzinfo=UTC)
    return SimpleNamespace(
        id="11111111-1111-1111-1111-111111111111", name=name, command=command, created_at=now, updated_at=now
    )


@pytest.mark.asyncio
async def test_get_alias_calls_procedure_and_maps_row(monkeypatch: pytest.MonkeyPatch) -> None:
    session = _Session(rows=[_alias_row("sit", "/sit")])
    _use_session(monkeypatch, session)

    alias = await AliasStorage().get_alias("Armitage", "SIT")

    assert alias is not None
    assert (alias.name, alias.command) == ("sit", "/sit")
    [(sql, params)] = session.executed
    assert "FROM get_player_alias(:player_name, :alias_name)" in sql
    assert params == {"player_name": "Armitage", "alias_name": "SIT"}


@pytest.mark.asyncio
async def test_create_alias_upserts_and_commits(monkeypatch: pytest.MonkeyPatch) -> None:
    session = _Session(rows=[_alias_row("sit", "/sit")])
    _use_session(monkeypatch, session)

    created = await AliasStorage().create_alias("Armitage", "sit", "/sit")

    assert created is not None
    assert created.command == "/sit"
    # first the limit check (list), then the upsert
    assert "get_player_aliases(" in session.executed[0][0]
    assert "upsert_player_alias(" in session.executed[1][0]
    assert session.executed[1][1] == {"player_name": "Armitage", "alias_name": "sit", "command": "/sit"}
    assert session.commits == 2


@pytest.mark.asyncio
async def test_create_alias_refused_at_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    session = _Session(rows=[_alias_row(f"a{i}", "look") for i in range(MAX_ALIASES_PER_PLAYER)])
    _use_session(monkeypatch, session)

    assert await AliasStorage().create_alias("Armitage", "one_more", "look") is None
    assert len(session.executed) == 1  # never reached the upsert


@pytest.mark.asyncio
@pytest.mark.parametrize(("scalar", "expected"), [(True, True), (False, False)])
async def test_remove_alias_returns_procedure_result(
    monkeypatch: pytest.MonkeyPatch, scalar: object, expected: bool
) -> None:
    session = _Session(scalar=scalar)
    _use_session(monkeypatch, session)

    assert await AliasStorage().remove_alias("Armitage", "sit") is expected
    assert "delete_player_alias(" in session.executed[0][0]


@pytest.mark.asyncio
async def test_delete_player_aliases_by_id_binds_player_id(monkeypatch: pytest.MonkeyPatch) -> None:
    session = _Session(scalar=3)
    _use_session(monkeypatch, session)

    assert await AliasStorage().delete_player_aliases_by_id("abc") is True
    assert session.executed == [("SELECT delete_player_aliases_by_id(:player_id)", {"player_id": "abc"})]
