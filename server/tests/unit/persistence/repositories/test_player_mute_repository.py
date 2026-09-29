"""Unit tests for PlayerMuteRepository (#681): row mapping, bound params, commit, error wrapping.

The procedures themselves run against PostgreSQL in
server/tests/integration/test_player_aliases_and_mutes_db.py.
"""

import uuid
from datetime import UTC, datetime, timedelta
from types import SimpleNamespace

import pytest
from sqlalchemy import TextClause
from sqlalchemy.exc import OperationalError

from server.exceptions import DatabaseError
from server.persistence.repositories.player_mute_repository import PlayerMute, PlayerMuteRepository


class _Result:
    def __init__(self, rows: list[object], scalar: object) -> None:
        self._rows: list[object] = rows
        self._scalar: object = scalar

    def all(self) -> list[object]:
        return self._rows

    def scalar(self) -> object:
        return self._scalar


class _Session:
    """Just enough AsyncSession for the repository: execute, commit, async context manager."""

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
    monkeypatch.setattr(
        "server.persistence.repositories.player_mute_repository.get_session_maker",
        lambda: lambda: session,
    )


def _broken_session_maker() -> object:
    raise OperationalError("SELECT 1", {}, Exception("db down"))


@pytest.mark.asyncio
async def test_load_active_maps_rows(monkeypatch: pytest.MonkeyPatch) -> None:
    muter, target = uuid.uuid4(), uuid.uuid4()
    now = datetime.now(UTC)
    session = _Session(
        rows=[
            SimpleNamespace(
                mute_type="global",
                muter_id=str(muter),  # asyncpg may hand back str; mapped to UUID
                muter_name="Admin",
                target_id=target,
                target_name="Noisy",
                channel=None,
                reason="spam",
                muted_at=now,
                expires_at=None,
            ),
            SimpleNamespace(
                mute_type="channel",
                muter_id=muter,
                muter_name="Admin",
                target_id=None,
                target_name=None,
                channel="ooc",
                reason="",
                muted_at=now,
                expires_at=now + timedelta(minutes=5),
            ),
        ]
    )
    _use_session(monkeypatch, session)

    mutes = await PlayerMuteRepository().load_active()

    assert mutes == [
        PlayerMute("global", muter, "Admin", target, "Noisy", None, "spam", now, None),
        PlayerMute("channel", muter, "Admin", None, None, "ooc", "", now, now + timedelta(minutes=5)),
    ]
    assert "FROM get_active_player_mutes()" in session.executed[0][0]


@pytest.mark.asyncio
async def test_upsert_binds_stringified_ids_and_commits(monkeypatch: pytest.MonkeyPatch) -> None:
    session = _Session()
    _use_session(monkeypatch, session)
    muter = uuid.uuid4()
    now = datetime.now(UTC)
    mute = PlayerMute("channel", muter, "Admin", None, None, "ooc", "quiet", now, None)

    await PlayerMuteRepository().upsert(mute)

    [(sql, params)] = session.executed
    assert "upsert_player_mute(" in sql
    assert params == {
        "mute_type": "channel",
        "muter_id": str(muter),
        "muter_name": "Admin",
        "target_id": None,
        "target_name": None,
        "channel": "ooc",
        "reason": "quiet",
        "muted_at": now,
        "expires_at": None,
    }
    assert session.commits == 1


@pytest.mark.asyncio
@pytest.mark.parametrize(("scalar", "expected"), [(True, True), (False, False), (None, False)])
async def test_delete_reports_whether_a_row_was_removed(
    monkeypatch: pytest.MonkeyPatch, scalar: object, expected: bool
) -> None:
    session = _Session(scalar=scalar)
    _use_session(monkeypatch, session)
    target = uuid.uuid4()

    assert await PlayerMuteRepository().delete("global", None, target, None) is expected

    [(_sql, params)] = session.executed
    assert params == {"mute_type": "global", "muter_id": None, "target_id": str(target), "channel": None}
    assert session.commits == 1


@pytest.mark.asyncio
async def test_database_errors_raise_database_error(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "server.persistence.repositories.player_mute_repository.get_session_maker", _broken_session_maker
    )
    repo = PlayerMuteRepository()
    mute = PlayerMute("player", uuid.uuid4(), "A", uuid.uuid4(), "B", None, "", datetime.now(UTC), None)

    with pytest.raises(DatabaseError):
        _ = await repo.load_active()
    with pytest.raises(DatabaseError):
        await repo.upsert(mute)
    with pytest.raises(DatabaseError):
        _ = await repo.delete("player", mute.muter_id, mute.target_id, None)
