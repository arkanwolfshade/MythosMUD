"""
Unit tests for QuestService.

Covers: resolve_name_to_quest_id, start_quest, progress, completion, turn-in, abandon, reset and get_quest_log. The
quest instances live in a real PlayerRegistry over an in-memory database (ADR-029 step 5a), so each test runs the real
unit of work: it seeds the player's instances, calls the service, and reads back what the unit committed.
"""

# pyright: reportAny=false, reportExplicitAny=false, reportUnknownArgumentType=false
# Reason: unittest.mock.AsyncMock inherits Any in typeshed (NonCallableMock(Base, Any)); mock
# attribute access and JSONB dict[str, Any] payloads cannot be reportAny-clean without cast noise.

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, cast
from unittest.mock import AsyncMock, patch

import pytest

from server.events.event_types import BaseEvent
from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry, QuestInstanceData
from server.game.quest.quest_service import QuestService
from server.models.player import Player
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which triggers this warning but is the standard pytest pattern
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior


class _MockDefRepo:
    """Typed stub for QuestDefinitionRepository (avoids MagicMock Any attributes)."""

    get_by_id: AsyncMock
    get_by_name: AsyncMock
    list_quest_ids_offered_by: AsyncMock

    def __init__(self) -> None:
        self.get_by_id = AsyncMock(return_value=None)
        self.get_by_name = AsyncMock(return_value=None)
        self.list_quest_ids_offered_by = AsyncMock(return_value=[])


class _Quests:
    """One player's quest instances behind a real PlayerRegistry, and the events it published after each commit."""

    def __init__(self) -> None:
        self.player_id: uuid.UUID = uuid.uuid4()
        self.db: FakeDatabase = FakeDatabase()
        self.events: list[BaseEvent] = []
        self._seeded: list[QuestInstanceData] = []
        self.registry: PlayerRegistry = PlayerRegistry(self.db.session, loader=self._load, publish=self.events.append)

    async def _load(self, _session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        return aggregate(raw_row(player_id), self._seeded) if player_id == self.player_id else None

    def seed(self, quest_id: str, state: str = "active", progress: Mapping[str, object] | None = None) -> None:
        """Give the player an instance before it is loaded."""
        self._seeded.append(QuestInstanceData(uuid.uuid4(), quest_id, state, dict(progress or {}), datetime.now(UTC)))

    def get(self, quest_id: str) -> QuestInstanceData | None:
        """The player's instance of ``quest_id`` as the registry holds it now (the seed if nothing loaded it)."""
        view = self.registry.peek(self.player_id)
        if view is None:
            return next((instance for instance in self._seeded if instance.quest_id == quest_id), None)
        return view.quests.get(quest_id)

    def names(self) -> list[str]:
        """The type names of the published events."""
        return [type(event).__name__ for event in self.events]


@dataclass
class _DefinitionRow:
    """Typed quest definition row with JSONB definition payload."""

    id: str
    definition: dict[str, Any]


class _FullInventory:
    """ItemGiver stub that always reports no free slot (and must never be asked to grant)."""

    async def has_free_slot(self, player_id: uuid.UUID) -> bool:
        _ = player_id
        return False

    async def grant(
        self, player_id: uuid.UUID, prototype_id: str, quantity: int = 1, *, origin: Mapping[str, object]
    ) -> None:
        raise AssertionError(f"granted {quantity}x {prototype_id} to {player_id} ({origin}) with no free slot")


def _message(result: dict[str, Any]) -> str:
    """Narrow service result message for assertions (dict values are Any)."""
    return str(result["message"])


@pytest.fixture
def mock_def_repo() -> _MockDefRepo:
    """Mock QuestDefinitionRepository."""
    return _MockDefRepo()


@pytest.fixture
def quests() -> _Quests:
    """The test player's quest instances."""
    return _Quests()


def _make_definition_row(quest_id: str = "leave_the_tutorial", name: str = "leave_the_tutorial") -> _DefinitionRow:
    """Build a definition row with definition JSONB."""
    return _DefinitionRow(
        id=quest_id,
        definition={
            "name": name,
            "title": "Leave the Tutorial",
            "description": "Find your way out.",
            "goals": [{"type": "complete_activity", "target": "exit_tutorial_room", "config": {}}],
            "rewards": [{"type": "xp", "config": {"amount": 10}}],
            "triggers": [],
            "requires_all": [],
            "requires_any": [],
            "auto_complete": True,
            "turn_in_entities": [],
        },
    )


def _make_kill_definition_row(quest_id: str = "kill_quest") -> _DefinitionRow:
    """Definition with kill_n goal."""
    return _DefinitionRow(
        id=quest_id,
        definition={
            "name": quest_id,
            "title": "Kill 3 Rats",
            "description": "Kill rats.",
            "goals": [{"type": "kill_n", "target": "npc_rat", "config": {"count": 3}}],
            "rewards": [],
            "triggers": [],
            "requires_all": [],
            "requires_any": [],
            "auto_complete": True,
            "turn_in_entities": [],
        },
    )


def _definition_named(quest_id: str) -> _DefinitionRow:
    """A definition whose id and name are both ``quest_id``."""
    return _make_definition_row(quest_id, quest_id)


@pytest.fixture
def quest_service(mock_def_repo: _MockDefRepo, quests: _Quests) -> QuestService:
    """QuestService over the mocked definitions and the test player's registry."""
    return QuestService(quest_definition_repository=mock_def_repo, player_registry=quests.registry)


# ---- the Journal is told about every change to the quest log, after the commit ----
@pytest.mark.asyncio
async def test_starting_a_quest_announces_a_quest_log_change(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())

    with patch("server.game.quest.quest_service.notify_quest_started"):
        _ = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert quests.names() == ["QuestLogChanged"]
    assert quests.db.commits == 1


@pytest.mark.asyncio
async def test_progress_that_does_not_complete_announces_a_quest_log_change(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """Regression: only completion refreshed the Journal, so cmd_look stayed 0/1 after `look`."""
    row = _make_definition_row()
    row.definition["auto_complete"] = False
    quests.seed("leave_the_tutorial")
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    with patch("server.game.quest.quest_service.notify_quest_progress"):
        await quest_service.record_complete_activity(quests.player_id, "exit_tutorial_room")

    assert quests.names() == ["QuestLogChanged"]


@pytest.mark.asyncio
async def test_completing_a_quest_announces_the_log_exactly_once(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    quests.seed("leave_the_tutorial")
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())  # auto_complete

    with (
        patch("server.game.quest.quest_service.notify_quest_completed"),
        patch.object(QuestService, "_apply_rewards", new=AsyncMock()),
    ):
        await quest_service.record_complete_activity(quests.player_id, "exit_tutorial_room")

    assert quests.names() == ["QuestCompleted", "QuestLogChanged"]


@pytest.mark.asyncio
async def test_abandoning_a_quest_announces_a_quest_log_change(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    row = _make_definition_row()
    mock_def_repo.get_by_name = AsyncMock(return_value=row)
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    quests.seed("leave_the_tutorial")

    with patch("server.game.quest.quest_service.notify_quest_abandoned"):
        _ = await quest_service.abandon(quests.player_id, "leave_the_tutorial")

    assert quests.names() == ["QuestLogChanged"]


@pytest.mark.asyncio
async def test_a_failed_commit_publishes_nothing_and_leaves_the_quest_unchanged(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """The unit rolls back: no QuestLogChanged for a change the database never got, and memory matches it."""
    row = _make_definition_row()
    mock_def_repo.get_by_name = AsyncMock(return_value=row)
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    quests.seed("leave_the_tutorial")
    quests.db.fail_commits = 1

    with pytest.raises(RuntimeError, match="database unavailable"):
        _ = await quest_service.abandon(quests.player_id, "leave_the_tutorial")

    assert quests.events == []
    instance = quests.get("leave_the_tutorial")
    assert instance is not None and instance.state == "active"


@pytest.mark.asyncio
async def test_two_kills_at_once_both_count(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """Each kill is one unit under the player's lock, so concurrent kills cannot overwrite each other's progress."""
    quests.seed("kill_quest", progress={"0": 0})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_kill_definition_row())

    _ = await asyncio.gather(
        quest_service.record_kill(quests.player_id, "npc_rat"), quest_service.record_kill(quests.player_id, "npc_rat")
    )

    instance = quests.get("kill_quest")
    assert instance is not None and dict(instance.progress) == {"0": 2}


# ---- reset_offered_quests (a fresh instance restarts the run) ----
def _offers(by_entity: dict[tuple[str, str], list[str]]) -> AsyncMock:
    """list_quest_ids_offered_by answering from a (entity_type, entity_id) table."""

    async def lookup(entity_type: str, entity_id: str) -> list[str]:
        return by_entity.get((entity_type, entity_id), [])

    return AsyncMock(side_effect=lookup)


@pytest.mark.asyncio
async def test_reset_offered_quests_resets_the_room_chain_but_not_unoffered_quests(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    mock_def_repo.list_quest_ids_offered_by = _offers(
        {("room", "square"): ["act1"], ("quest", "act1"): ["act2"], ("quest", "act2"): ["act3"]}
    )
    quests.seed("act1", "completed", {"0": 1})
    quests.seed("act2", "active", {"0": 1})
    quests.seed("epilogue", "completed")  # offered by no room or quest; act3 was never started

    reset = await quest_service.reset_offered_quests(quests.player_id, ["square", "elsewhere"])

    assert sorted(reset) == ["act1", "act2"]
    for quest_id in ("act1", "act2"):
        instance = quests.get(quest_id)
        assert instance is not None and (instance.state, dict(instance.progress)) == ("abandoned", {})
    epilogue = quests.get("epilogue")
    assert epilogue is not None and epilogue.state == "completed"
    assert quests.get("act3") is None
    assert quests.names() == ["QuestLogChanged"]  # announced once for the whole reset


@pytest.mark.asyncio
async def test_reset_offered_quests_leaves_already_abandoned_quests_and_stays_quiet(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    mock_def_repo.list_quest_ids_offered_by = _offers({("room", "square"): ["act1"]})
    quests.seed("act1", "abandoned")

    assert await quest_service.reset_offered_quests(quests.player_id, ["square"]) == []

    assert quests.db.commits == 0
    assert not quests.events


# ---- resolve_name_to_quest_id ----
@pytest.mark.asyncio
async def test_resolve_name_to_quest_id_found(quest_service: QuestService, mock_def_repo: _MockDefRepo):
    """resolve_name_to_quest_id returns quest_id when definition exists."""
    row = _make_definition_row()
    mock_def_repo.get_by_name = AsyncMock(return_value=row)

    result = await quest_service.resolve_name_to_quest_id("leave_the_tutorial")

    assert result == "leave_the_tutorial"
    mock_def_repo.get_by_name.assert_awaited_once_with("leave_the_tutorial")


@pytest.mark.asyncio
async def test_resolve_name_to_quest_id_not_found(quest_service: QuestService, mock_def_repo: _MockDefRepo):
    """resolve_name_to_quest_id returns None when definition missing."""
    mock_def_repo.get_by_name = AsyncMock(return_value=None)

    result = await quest_service.resolve_name_to_quest_id("unknown_quest")

    assert result is None


# ---- start_quest ----
@pytest.mark.asyncio
async def test_start_quest_success(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """start_quest creates an active instance, commits it, and returns success when prereqs met."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())

    with patch("server.game.quest.quest_service.notify_quest_started") as notify:
        result = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert result["success"] is True
    assert "started" in _message(result).lower()
    assert result.get("title") == "Leave the Tutorial"
    instance = quests.get("leave_the_tutorial")
    assert instance is not None and (instance.state, dict(instance.progress)) == ("active", {})
    assert [params["quest_id"] for params in quests.db.executed if params] == ["leave_the_tutorial"]
    notify.assert_called_once_with(quests.player_id, "Leave the Tutorial")


@pytest.mark.asyncio
async def test_start_quest_not_found(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """start_quest returns error when quest id not found."""
    mock_def_repo.get_by_id = AsyncMock(return_value=None)

    result = await quest_service.start_quest(quests.player_id, "unknown_quest")

    assert result["success"] is False
    assert "not found" in _message(result).lower()


@pytest.mark.asyncio
async def test_start_quest_already_active(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """start_quest returns error when player already has active instance."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())
    quests.seed("leave_the_tutorial", "active")

    result = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "already have" in _message(result).lower()
    assert quests.db.commits == 0


@pytest.mark.asyncio
async def test_start_quest_already_completed(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """start_quest returns error when player already completed quest."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())
    quests.seed("leave_the_tutorial", "completed")

    result = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "already completed" in _message(result).lower()


@pytest.mark.asyncio
async def test_start_quest_reaccept_after_abandon(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """start_quest re-activates the abandoned instance in place (same id), with its progress cleared."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())
    quests.seed("leave_the_tutorial", "abandoned", {"0": 1})
    seeded = quests.get("leave_the_tutorial")

    result = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert result["success"] is True
    assert "started" in _message(result).lower()
    instance = quests.get("leave_the_tutorial")
    assert seeded is not None and instance is not None
    assert (instance.instance_id, instance.state, dict(instance.progress)) == (seeded.instance_id, "active", {})


@pytest.mark.asyncio
async def test_start_quest_prereq_not_met(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """start_quest returns error when requires_all not satisfied."""
    row = _make_definition_row()
    row.definition["requires_all"] = ["other_quest"]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    result = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "prerequisite" in _message(result).lower()
    assert quests.get("leave_the_tutorial") is None


@pytest.mark.asyncio
async def test_start_quest_requires_any_satisfied(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """start_quest succeeds when requires_any has at least one completed."""
    row = _make_definition_row()
    row.definition["requires_any"] = ["quest_a", "quest_b"]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    quests.seed("quest_a", "completed")

    result = await quest_service.start_quest(quests.player_id, "leave_the_tutorial")

    assert result["success"] is True
    instance = quests.get("leave_the_tutorial")
    assert instance is not None and instance.state == "active"


# ---- start_quest_by_trigger ----
@pytest.mark.asyncio
async def test_start_quest_by_trigger_starts_matching_quest(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """start_quest_by_trigger returns result from start_quest when offer and trigger match."""
    mock_def_repo.list_quest_ids_offered_by = AsyncMock(return_value=["leave_the_tutorial"])
    row = _make_definition_row()
    row.definition["triggers"] = [{"type": "room", "entity_id": "tutorial_room_001"}]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    results = await quest_service.start_quest_by_trigger(quests.player_id, "room", "tutorial_room_001")

    assert len(results) == 1
    assert results[0]["success"] is True
    assert quests.get("leave_the_tutorial") is not None


@pytest.mark.asyncio
async def test_start_quest_by_trigger_skips_when_no_offer(quest_service: QuestService, mock_def_repo: _MockDefRepo):
    """start_quest_by_trigger returns empty list when entity offers no quests."""
    mock_def_repo.list_quest_ids_offered_by = AsyncMock(return_value=[])

    results = await quest_service.start_quest_by_trigger(uuid.uuid4(), "room", "unknown_room")

    assert results == []


# ---- record_complete_activity ----
@pytest.mark.asyncio
async def test_record_complete_activity_updates_progress(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """record_complete_activity updates instance progress for matching complete_activity goal."""
    quests.seed("leave_the_tutorial")
    row = _make_definition_row()
    row.definition["goals"] = [{"type": "complete_activity", "target": "exit_tutorial_room", "config": {}}]
    row.definition["auto_complete"] = False
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    with patch("server.game.quest.quest_service.notify_quest_progress") as notify:
        await quest_service.record_complete_activity(quests.player_id, "exit_tutorial_room")

    instance = quests.get("leave_the_tutorial")
    assert instance is not None and (instance.state, dict(instance.progress)) == ("active", {"0": 1})
    assert quests.db.commits == 1
    notify.assert_called_once_with(quests.player_id, "Leave the Tutorial")


@pytest.mark.asyncio
async def test_record_complete_activity_auto_completes_when_goals_met(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """When all goals met and auto_complete true, record_complete_activity completes the instance."""
    quests.seed("leave_the_tutorial")
    row = _make_definition_row()
    row.definition["goals"] = [{"type": "complete_activity", "target": "exit_tutorial_room", "config": {}}]
    row.definition["auto_complete"] = True
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    with (
        patch("server.game.quest.quest_service.notify_quest_progress") as notify_progress,
        patch("server.game.quest.quest_service.notify_quest_completed") as notify_completed,
    ):
        await quest_service.record_complete_activity(quests.player_id, "exit_tutorial_room")

    instance = quests.get("leave_the_tutorial")
    assert instance is not None and instance.state == "completed" and instance.completed_at is not None
    assert dict(instance.progress) == {"0": 1}
    assert quests.db.commits == 1  # the progress and the completion commit together
    # Completing tick: only completed notify (no duplicate progress line) — #583
    notify_progress.assert_not_called()
    notify_completed.assert_called_once_with(quests.player_id, "Leave the Tutorial")


# ---- record_kill ----
@pytest.mark.asyncio
async def test_record_kill_updates_progress(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """record_kill updates instance progress for matching kill_n goal."""
    quests.seed("kill_quest", progress={"0": 0})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_kill_definition_row())

    await quest_service.record_kill(quests.player_id, "npc_rat")

    instance = quests.get("kill_quest")
    assert instance is not None and dict(instance.progress) == {"0": 1}


@pytest.mark.asyncio
async def test_record_kill_suppresses_intermediate_progress_notify(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """Intermediate kill ticks do not emit progress chat (#583 milestones)."""
    quests.seed("kill_quest", progress={"0": 1})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_kill_definition_row())

    with patch("server.game.quest.quest_service.notify_quest_progress") as notify:
        await quest_service.record_kill(quests.player_id, "npc_rat")

    notify.assert_not_called()
    instance = quests.get("kill_quest")
    assert instance is not None and dict(instance.progress) == {"0": 2}


@pytest.mark.asyncio
async def test_record_kill_without_a_matching_quest_writes_nothing(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    quests.seed("kill_quest", progress={"0": 0})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_kill_definition_row())

    await quest_service.record_kill(quests.player_id, "npc_bat")

    assert quests.db.commits == 0 and not quests.events


# ---- abandon ----
@pytest.mark.asyncio
async def test_abandon_success(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """abandon updates instance to abandoned and returns success."""
    row = _make_definition_row()
    mock_def_repo.get_by_name = AsyncMock(return_value=row)
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    quests.seed("leave_the_tutorial", "active", {"0": 1})

    with patch("server.game.quest.quest_service.notify_quest_abandoned") as notify:
        result = await quest_service.abandon(quests.player_id, "leave_the_tutorial")

    assert result["success"] is True
    assert "abandoned" in _message(result).lower()
    instance = quests.get("leave_the_tutorial")
    assert instance is not None and (instance.state, dict(instance.progress)) == ("abandoned", {"0": 1})
    notify.assert_called_once_with(quests.player_id, "Leave the Tutorial")


@pytest.mark.asyncio
async def test_abandon_unknown_quest(quest_service: QuestService, mock_def_repo: _MockDefRepo):
    """abandon returns error when quest name not found."""
    mock_def_repo.get_by_name = AsyncMock(return_value=None)

    result = await quest_service.abandon(uuid.uuid4(), "unknown_quest")

    assert result["success"] is False
    message = _message(result)
    assert "unknown" in message.lower() or "Unknown" in message


@pytest.mark.asyncio
async def test_abandon_no_instance(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """abandon returns error when player has no instance."""
    mock_def_repo.get_by_name = AsyncMock(return_value=_make_definition_row())

    result = await quest_service.abandon(quests.player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "do not have" in _message(result).lower()
    assert quests.db.commits == 0


@pytest.mark.asyncio
async def test_abandon_not_active(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """abandon returns error when instance is not active."""
    mock_def_repo.get_by_name = AsyncMock(return_value=_make_definition_row())
    quests.seed("leave_the_tutorial", "completed")

    result = await quest_service.abandon(quests.player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "only abandon an active" in _message(result).lower()
    assert quests.db.commits == 0


# ---- get_quest_log ----
@pytest.mark.asyncio
async def test_get_quest_log_empty(quest_service: QuestService, quests: _Quests):
    """get_quest_log returns empty list when no active or completed."""
    result = await quest_service.get_quest_log(quests.player_id, include_completed=True)

    assert result == []


@pytest.mark.asyncio
async def test_get_quest_log_of_an_unknown_player_is_empty(quest_service: QuestService):
    assert await quest_service.get_quest_log(uuid.uuid4(), include_completed=True) == []


@pytest.mark.asyncio
async def test_get_quest_log_excludes_completed_when_requested(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """get_quest_log with include_completed=False lists only the active quests."""
    mock_def_repo.get_by_id = AsyncMock(side_effect=_definition_named)
    quests.seed("still_going", "active")
    quests.seed("done", "completed")
    quests.seed("dropped", "abandoned")

    active_only = await quest_service.get_quest_log(quests.player_id, include_completed=False)
    everything = await quest_service.get_quest_log(quests.player_id, include_completed=True)

    assert [entry["quest_id"] for entry in active_only] == ["still_going"]
    assert [entry["quest_id"] for entry in everything] == ["still_going", "done"]  # abandoned stays hidden


@pytest.mark.asyncio
async def test_get_quest_log_returns_entries(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """get_quest_log returns formatted entries for active/completed instances."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_definition_row())
    quests.seed("leave_the_tutorial", "active", {"0": 0})

    result = await quest_service.get_quest_log(quests.player_id, include_completed=True)

    assert len(result) == 1
    assert result[0]["quest_id"] == "leave_the_tutorial"
    assert result[0]["name"] == "leave_the_tutorial"
    assert result[0]["title"] == "Leave the Tutorial"
    assert result[0]["state"] == "active"
    goals = result[0]["goals_with_progress"]
    assert isinstance(goals, list)
    assert len(goals) == 1
    assert goals[0]["goal_type"] == "complete_activity"
    assert goals[0]["done"] is False


# ---- turn_in ----
def _make_turn_in_definition_row(quest_id: str = "turn_in_quest") -> _DefinitionRow:
    """Definition with auto_complete false and turn_in_entities."""
    return _DefinitionRow(
        id=quest_id,
        definition={
            "name": quest_id,
            "title": "Turn-in Quest",
            "description": "Complete and turn in.",
            "goals": [{"type": "complete_activity", "target": "do_thing", "config": {}}],
            "rewards": [{"type": "xp", "config": {"amount": 5}}],
            "triggers": [],
            "requires_all": [],
            "requires_any": [],
            "auto_complete": False,
            "turn_in_entities": ["npc_quest_giver_001"],
        },
    )


@pytest.mark.asyncio
async def test_turn_in_auto_complete_returns_error(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """turn_in returns error when quest has auto_complete true."""
    row = _make_definition_row()
    row.definition["auto_complete"] = True
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    result = await quest_service.turn_in(quests.player_id, "leave_the_tutorial", "room", "any_room")

    assert result["success"] is False
    assert "automatically" in _message(result).lower()


@pytest.mark.asyncio
async def test_turn_in_success(quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests):
    """turn_in applies rewards and sets instance completed when goals met and at valid entity."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_turn_in_definition_row())
    quests.seed("turn_in_quest", "active", {"0": 1})

    with patch("server.game.quest.quest_service.notify_quest_completed") as notify:
        result = await quest_service.turn_in(quests.player_id, "turn_in_quest", "npc", "npc_quest_giver_001")

    assert result["success"] is True
    assert result.get("title")
    instance = quests.get("turn_in_quest")
    assert instance is not None and instance.state == "completed" and instance.completed_at is not None
    assert quests.db.commits == 1
    notify.assert_called_once()


@pytest.mark.asyncio
async def test_turn_in_wrong_entity_returns_error(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """turn_in returns error when at_entity_id not in turn_in_entities."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_turn_in_definition_row())

    result = await quest_service.turn_in(quests.player_id, "turn_in_quest", "npc", "wrong_npc")

    assert result["success"] is False
    message = _message(result)
    assert "cannot turn in" in message.lower() or "here" in message.lower()


@pytest.mark.asyncio
async def test_turn_in_no_active_instance_returns_error(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """turn_in returns error when player has no active instance."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_turn_in_definition_row())

    result = await quest_service.turn_in(quests.player_id, "turn_in_quest", "npc", "npc_quest_giver_001")

    assert result["success"] is False
    message = _message(result)
    assert "do not have" in message.lower() or "active" in message.lower()


@pytest.mark.asyncio
async def test_turn_in_inventory_full_blocks_item_reward(mock_def_repo: _MockDefRepo, quests: _Quests):
    """When reward is item and inventory full, turn_in returns error (block turn-in)."""
    row = _make_turn_in_definition_row()
    row.definition["rewards"] = [{"type": "item", "config": {"item_id": "quest_item_1"}}]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    quests.seed("turn_in_quest", "active", {"0": 1})
    svc = QuestService(
        quest_definition_repository=mock_def_repo, player_registry=quests.registry, item_granter=_FullInventory()
    )

    result = await svc.turn_in(quests.player_id, "turn_in_quest", "npc", "npc_quest_giver_001")

    assert result["success"] is False
    message = _message(result)
    assert "inventory" in message.lower() or "full" in message.lower()
    instance = quests.get("turn_in_quest")
    assert instance is not None and instance.state == "active"


@pytest.mark.asyncio
async def test_turn_in_at_entity_turns_in_every_quest_listing_it(mock_def_repo: _MockDefRepo, quests: _Quests):
    rows = {quest_id: _make_turn_in_definition_row(quest_id) for quest_id in ("first", "second", "elsewhere")}
    rows["elsewhere"].definition["turn_in_entities"] = ["npc_other"]
    mock_def_repo.get_by_id = AsyncMock(side_effect=rows.__getitem__)
    for quest_id in rows:
        quests.seed(quest_id, "active", {"0": 1})
    service = QuestService(quest_definition_repository=mock_def_repo, player_registry=quests.registry)

    with patch("server.game.quest.quest_service.notify_quest_completed"):
        results = await service.turn_in_at_entity(quests.player_id, "npc", "npc_quest_giver_001")

    assert [result["success"] for result in results] == [True, True]
    states = {quest_id: getattr(quests.get(quest_id), "state", None) for quest_id in rows}
    assert states == {"first": "completed", "second": "completed", "elsewhere": "active"}
    assert quests.db.commits == 1  # every turn-in joined one unit


class _RespawnPersistence:
    """Typed async_persistence stand-in for reward application."""

    def __init__(self, player: Player) -> None:
        self.player: Player = player
        self.saved: list[Player] = []

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player:
        _ = player_id
        return self.player

    async def save_player(self, player: Player) -> None:
        self.saved.append(player)


async def _complete_tutorial_with_rewards(rewards: list[dict[str, object]], persistence: _RespawnPersistence) -> None:
    def_repo = _MockDefRepo()
    quests = _Quests()
    row = _make_definition_row()
    row.definition["rewards"] = rewards
    quests.seed("leave_the_tutorial")
    def_repo.get_by_id = AsyncMock(return_value=row)
    service = QuestService(
        quest_definition_repository=def_repo, player_registry=quests.registry, async_persistence=persistence
    )
    with (
        patch("server.game.quest.quest_service.notify_quest_progress"),
        patch("server.game.quest.quest_service.notify_quest_completed"),
    ):
        await service.record_complete_activity(quests.player_id, "exit_tutorial_room")


async def test_respawn_room_reward_moves_the_players_respawn():
    """Completing leave_the_tutorial points respawn at the Sanitarium Main Foyer."""
    foyer = "earth_arkhamcity_sanitarium_room_foyer_001"
    player = Player(name="Newbie", respawn_room_id="earth_arkhamcity_sanitarium_room_tutorial_bedroom_001")
    persistence = _RespawnPersistence(player)

    await _complete_tutorial_with_rewards([{"type": "respawn_room", "config": {"room_id": foyer}}], persistence)

    assert player.respawn_room_id == foyer
    assert persistence.saved == [player]


async def test_respawn_room_reward_without_room_id_changes_nothing():
    bedroom = "earth_arkhamcity_sanitarium_room_tutorial_bedroom_001"
    player = Player(name="Newbie", respawn_room_id=bedroom)
    persistence = _RespawnPersistence(player)

    await _complete_tutorial_with_rewards([{"type": "respawn_room", "config": {}}], persistence)

    assert player.respawn_room_id == bedroom
    assert persistence.saved == []


@pytest.mark.asyncio
async def test_get_quest_log_carries_the_goals_authored_description(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """#1102: the journal shows the authored text instead of the raw target; a goal without one reports None."""
    row = _make_definition_row()
    row.definition["goals"] = [
        {"type": "complete_activity", "target": "cmd_look", "description": "Look around (`look`)"},
        {"type": "complete_activity", "target": "cmd_talk"},
    ]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    quests.seed("leave_the_tutorial", "active", {"0": 1})

    result = await quest_service.get_quest_log(quests.player_id, include_completed=False)

    goals = cast(list[dict[str, object]], result[0]["goals_with_progress"])
    assert [g["description"] for g in goals] == ["Look around (`look`)", None]
    assert [g["target"] for g in goals] == ["cmd_look", "cmd_talk"]


# ---- has_completed_activity (exits a quest unlocks, #1111) ----
def _activity_row(*goals: dict[str, object], quest_id: str = "walk") -> _DefinitionRow:
    row = _make_definition_row(quest_id=quest_id, name=quest_id)
    row.definition["goals"] = list(goals)
    return row


@pytest.mark.asyncio
async def test_has_completed_activity_is_true_when_a_goal_with_that_target_is_done(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    mock_def_repo.get_by_id = AsyncMock(
        return_value=_activity_row(
            {"type": "complete_activity", "target": "cmd_look"},
            {"type": "complete_activity", "target": "cmd_read"},
        )
    )
    quests.seed("walk", "active", {"0": 1})

    assert await quest_service.has_completed_activity(quests.player_id, "cmd_look") is True
    assert await quest_service.has_completed_activity(quests.player_id, "cmd_read") is False  # not done yet
    assert await quest_service.has_completed_activity(quests.player_id, "cmd_elsewhere") is False  # no such goal


@pytest.mark.asyncio
async def test_has_completed_activity_counts_a_completed_quest(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    """The path stays open behind the player: finishing Act I must not re-lock the lane they already walked."""
    mock_def_repo.get_by_id = AsyncMock(return_value=_activity_row({"type": "complete_activity", "target": "cmd_look"}))
    quests.seed("walk", "completed", {"0": 1})

    assert await quest_service.has_completed_activity(quests.player_id, "cmd_look") is True


@pytest.mark.asyncio
async def test_has_completed_activity_ignores_other_goal_types_and_missing_definitions(
    quest_service: QuestService, mock_def_repo: _MockDefRepo, quests: _Quests
):
    rows = {"gone": None, "walk": _activity_row({"type": "kill_n", "target": "cmd_look", "config": {"count": 1}})}
    mock_def_repo.get_by_id = AsyncMock(side_effect=rows.__getitem__)
    quests.seed("gone", "active", {"0": 1})
    quests.seed("walk", "active", {"0": 1})

    assert await quest_service.has_completed_activity(quests.player_id, "cmd_look") is False
