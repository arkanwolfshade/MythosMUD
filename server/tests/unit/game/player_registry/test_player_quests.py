"""Unit tests for the quests part: loading, synchronous changes, ordering, rollback, and its write of every instance."""

from __future__ import annotations

import json
import re
import uuid
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime, timedelta

import pytest

from server.game.player_registry import PlayerQuestsPart, QuestInstanceData, load_player_aggregate
from server.game.player_registry.player_quests import LIST_QUEST_INSTANCES_SQL, UPSERT_QUEST_INSTANCE_SQL

from .fakes import FakeDatabase, raw_row

T0 = datetime(2026, 10, 30, 12, 0, tzinfo=UTC)


def _instance(
    quest_id: str, state: str = "active", minutes: int = 0, progress: Mapping[str, object] | None = None
) -> QuestInstanceData:
    accepted = T0 + timedelta(minutes=minutes)
    completed = accepted if state == "completed" else None
    return QuestInstanceData(uuid.uuid4(), quest_id, state, dict(progress or {}), accepted, completed)


def test_from_rows_reads_every_column_and_keys_by_quest_id() -> None:
    instance_id = uuid.uuid4()
    rows = [
        {
            "id": str(instance_id),
            "quest_id": "leave_the_tutorial",
            "state": "active",
            "progress": '{"0": 1}',
            "accepted_at": T0,
            "completed_at": None,
        }
    ]

    part = PlayerQuestsPart.from_rows(uuid.uuid4(), rows)

    assert part.get("leave_the_tutorial") == QuestInstanceData(
        instance_id, "leave_the_tutorial", "active", {"0": 1}, T0, None
    )
    assert part.get("unknown") is None


def test_active_is_oldest_first_and_completed_is_newest_first() -> None:
    part = PlayerQuestsPart(
        uuid.uuid4(),
        [
            _instance("b", minutes=2),
            _instance("a", minutes=1),
            _instance("done_early", "completed", minutes=3),
            _instance("done_late", "completed", minutes=4),
            _instance("dropped", "abandoned"),
        ],
    )

    assert [instance.quest_id for instance in part.active()] == ["a", "b"]
    assert [instance.quest_id for instance in part.completed()] == ["done_late", "done_early"]


def test_set_creates_an_instance_accepted_now_and_every_change_is_synchronous() -> None:
    part = PlayerQuestsPart(uuid.uuid4())

    created = part.set("q", state="active", progress={})

    assert part.get("q") == created and created.state == "active" and created.accepted_at is not None
    assert part.dirty and part.sync_required


def test_set_changes_only_the_fields_given_and_keeps_the_instance_id() -> None:
    original = _instance("q", progress={"0": 2})
    part = PlayerQuestsPart(uuid.uuid4(), [original])

    updated = part.set("q", state="completed", completed_at=T0)

    assert updated.instance_id == original.instance_id
    assert (updated.state, dict(updated.progress), updated.completed_at) == ("completed", {"0": 2}, T0)


def test_an_unchanged_set_is_not_dirty() -> None:
    part = PlayerQuestsPart(uuid.uuid4(), [_instance("q")])

    _ = part.set("q", state="active")

    assert not part.dirty


def test_a_new_instance_needs_a_state() -> None:
    with pytest.raises(ValueError, match="needs a state"):
        _ = PlayerQuestsPart(uuid.uuid4()).set("q", progress={"0": 1})


def test_rollback_restores_the_instances_and_flags() -> None:
    part = PlayerQuestsPart(uuid.uuid4(), [_instance("q")])
    part.begin()
    _ = part.set("q", state="abandoned")
    _ = part.set("new", state="active")
    part.rollback()

    restored = part.get("q")
    assert restored is not None and restored.state == "active"
    assert part.get("new") is None
    assert not part.dirty and not part.sync_required


def test_write_params_cover_every_procedure_argument_for_every_instance() -> None:
    player_id = uuid.uuid4()
    part = PlayerQuestsPart(player_id, [_instance("a", progress={"0": 1}), _instance("b", "completed")])

    params = part.write_params()

    assert [row["quest_id"] for row in params] == ["a", "b"]
    for row in params:
        assert set(row) == set(re.findall(r":(\w+)", str(UPSERT_QUEST_INSTANCE_SQL)))
        assert row["player_id"] == str(player_id)
    assert json.loads(str(params[0]["progress"])) == {"0": 1}


async def test_captured_write_upserts_every_instance_and_clears_the_flags() -> None:
    part = PlayerQuestsPart(uuid.uuid4(), [_instance("a")])
    _ = part.set("b", state="active")
    write = part.take_write()
    assert write is not None and not part.dirty and not part.sync_required

    db = FakeDatabase()
    async with db.session() as session:
        await write(session)

    assert [params["quest_id"] for params in db.executed if params is not None] == ["a", "b"]


class _QuestRowsSession:
    """Answers the player-row query with ``row`` and the quest query with ``quest_rows``."""

    def __init__(self, row: Mapping[str, object], quest_rows: Sequence[Mapping[str, object]]) -> None:
        self.row: Mapping[str, object] = row
        self.quest_rows: Sequence[Mapping[str, object]] = quest_rows
        self.quest_queries: list[Mapping[str, object] | None] = []
        self._answer: Sequence[Mapping[str, object]] = []

    async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> _QuestRowsSession:
        if statement is LIST_QUEST_INSTANCES_SQL:
            self.quest_queries.append(params)
            self._answer = self.quest_rows
        else:
            self._answer = [self.row]
        return self

    def mappings(self) -> _QuestRowsSession:
        return self

    def first(self) -> Mapping[str, object] | None:
        return self._answer[0] if self._answer else None

    def all(self) -> Sequence[Mapping[str, object]]:
        return self._answer

    async def commit(self) -> None:
        return None

    async def rollback(self) -> None:
        return None


async def test_the_default_loader_reads_the_players_quests_with_the_row() -> None:
    player_id = uuid.uuid4()
    quest_row: dict[str, object] = {
        "id": str(uuid.uuid4()),
        "quest_id": "q",
        "state": "active",
        "progress": {},
        "accepted_at": T0,
        "completed_at": None,
    }
    session = _QuestRowsSession(raw_row(player_id), [quest_row])

    loaded = await load_player_aggregate(session, player_id)

    assert loaded is not None and [instance.quest_id for instance in loaded.quests.active()] == ["q"]
    assert session.quest_queries == [{"id": str(player_id)}]
