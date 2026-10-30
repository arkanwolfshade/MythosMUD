"""
Unit tests for QuestService collect_n sync, auto-complete, and turn-in consumption.

The player's stacks and quest instances live in a real PlayerRegistry over an in-memory database (ADR-029 steps 4c-i
and 5a): collect progress is counted from the live stacks, and a turn-in's consumption and completion commit in one
unit.
"""

import json
import uuid
from collections.abc import Mapping
from datetime import UTC, datetime
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.player_registry import DbSession, PlayerAggregate, PlayerRegistry, QuestInstanceData
from server.game.quest.quest_service import QuestService
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters
# pylint: disable=protected-access  # Reason: Tests may access protected members for verification

DAISY = "misc.herb.sanitarium_daisy"


class _MockDefRepo:
    """Typed stub for QuestDefinitionRepository (avoids MagicMock Any attributes)."""

    get_by_id: AsyncMock
    get_by_name: AsyncMock
    list_quest_ids_offered_by: AsyncMock

    def __init__(self) -> None:
        self.get_by_id = AsyncMock(return_value=None)
        self.get_by_name = AsyncMock(return_value=None)
        self.list_quest_ids_offered_by = AsyncMock(return_value=[])


@pytest.fixture
def mock_def_repo() -> _MockDefRepo:
    """Mock QuestDefinitionRepository."""
    return _MockDefRepo()


def _make_collect_quest_row(
    quest_id: str = "gather_daisies",
    *,
    auto_complete: bool = False,
    turn_in_entities: list[str] | None = None,
    count: int = 3,
):
    """Definition with collect_n goal."""
    row = MagicMock()
    row.id = quest_id
    row.definition = {
        "name": quest_id,
        "title": "Gather Daisies",
        "description": "Collect daisies.",
        "goals": [{"type": "collect_n", "target": DAISY, "config": {"count": count}}],
        "rewards": [{"type": "xp", "config": {"amount": 5}}],
        "triggers": [{"type": "npc", "entity_id": "54"}],
        "requires_all": [],
        "requires_any": [],
        "auto_complete": auto_complete,
        "turn_in_entities": turn_in_entities if turn_in_entities is not None else (["54"] if not auto_complete else []),
    }
    return row


def _daisies(quantity: int) -> dict[str, object]:
    return {
        "item_id": DAISY,
        "prototype_id": DAISY,
        "item_name": "Sanitarium Daisy",
        "slot_type": "inventory",
        "quantity": quantity,
    }


class _Player:
    """One player (carried stacks and quest instances) behind a real PlayerRegistry."""

    def __init__(self, carried: list[dict[str, object]], quests: Mapping[str, Mapping[str, object]] | None = None):
        self.player_id: uuid.UUID = uuid.uuid4()
        self.db: FakeDatabase = FakeDatabase()
        self._carried: list[dict[str, object]] = carried
        self._quests: list[QuestInstanceData] = [
            QuestInstanceData(uuid.uuid4(), quest_id, "active", dict(progress), datetime.now(UTC))
            for quest_id, progress in (quests or {}).items()
        ]
        self.registry: PlayerRegistry = PlayerRegistry(self.db.session, loader=self._load)

    async def _load(self, _session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        row = raw_row(player_id, inventory=json.dumps(self._carried))
        return aggregate(row, self._quests) if player_id == self.player_id else None

    def quest(self, quest_id: str) -> QuestInstanceData:
        view = self.registry.peek(self.player_id)
        instance = view.quests.get(quest_id) if view is not None else None
        assert instance is not None
        return instance

    def carried(self) -> list[dict[str, object]]:
        view = self.registry.peek(self.player_id)
        assert view is not None
        return [dict(stack) for stack in view.inventory.carried]

    def service(self, def_repo: _MockDefRepo) -> QuestService:
        return QuestService(quest_definition_repository=def_repo, player_registry=self.registry)


@pytest.mark.asyncio
async def test_start_quest_collect_n_seeds_progress_from_holdings(mock_def_repo: _MockDefRepo):
    """start_quest syncs collect_n progress from current inventory, in the same unit."""
    player = _Player([_daisies(2)])
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(turn_in_entities=["54"]))

    result = await player.service(mock_def_repo).start_quest(player.player_id, "gather_daisies")

    assert result["success"] is True
    assert (player.quest("gather_daisies").state, dict(player.quest("gather_daisies").progress)) == ("active", {"0": 2})
    assert player.db.commits == 1


@pytest.mark.asyncio
async def test_sync_collect_progress_updates_on_inventory_change(mock_def_repo: _MockDefRepo):
    """sync_collect_progress reflects increased holdings."""
    player = _Player([_daisies(3)], {"gather_daisies": {"0": 1}})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(auto_complete=False, count=5))

    await player.service(mock_def_repo).sync_collect_progress(player.player_id)

    assert dict(player.quest("gather_daisies").progress) == {"0": 3}


@pytest.mark.asyncio
async def test_sync_collect_progress_nested_container(mock_def_repo: _MockDefRepo):
    """Nested inner_container items count toward collect_n progress."""
    pouch: dict[str, object] = {
        "item_id": "wearable.pouch",
        "prototype_id": "wearable.pouch",
        "item_name": "Pouch",
        "slot_type": "inventory",
        "quantity": 1,
        "inner_container": {"items": [_daisies(2)]},
    }
    player = _Player([pouch], {"gather_daisies": {}})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(turn_in_entities=["54"]))

    await player.service(mock_def_repo).sync_collect_progress(player.player_id)

    assert dict(player.quest("gather_daisies").progress) == {"0": 2}


@pytest.mark.asyncio
async def test_sync_collect_progress_skips_an_unknown_player(mock_def_repo: _MockDefRepo):
    player = _Player([_daisies(1)])

    await player.service(mock_def_repo).sync_collect_progress(uuid.uuid4())  # no such player: logged, not raised

    assert player.db.commits == 0


@pytest.mark.asyncio
async def test_collect_n_auto_complete_keeps_items(mock_def_repo: _MockDefRepo):
    """Auto-complete collect_n quest does not consume inventory."""
    player = _Player([_daisies(2)], {"gather_daisies": {}})
    mock_def_repo.get_by_id = AsyncMock(
        return_value=_make_collect_quest_row(auto_complete=True, turn_in_entities=[], count=2)
    )

    await player.service(mock_def_repo).sync_collect_progress(player.player_id)

    assert player.quest("gather_daisies").state == "completed"
    assert player.carried()[0]["quantity"] == 2
    assert player.db.last_inventory_write() is None


@pytest.mark.asyncio
async def test_turn_in_collect_n_consumes_items(mock_def_repo: _MockDefRepo):
    """Turn-in consumes the required items and completes the quest, in one commit."""
    player = _Player([_daisies(5)], {"gather_daisies": {"0": 3}})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(turn_in_entities=["54"], count=3))

    result = await player.service(mock_def_repo).turn_in(player.player_id, "gather_daisies", "npc", "54")

    assert result["success"] is True
    write = player.db.last_inventory_write()
    assert write is not None
    committed = cast(list[dict[str, object]], json.loads(str(write["inventory_json"])))
    assert committed[0]["quantity"] == 2
    assert player.quest("gather_daisies").state == "completed"
    assert player.db.commits == 1


@pytest.mark.asyncio
async def test_a_failed_turn_in_commit_keeps_the_items_and_the_quest_active(mock_def_repo: _MockDefRepo):
    """Consumption and completion are one unit: a failed commit rolls both back, so nothing is lost or half-done."""
    player = _Player([_daisies(5)], {"gather_daisies": {"0": 3}})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(turn_in_entities=["54"], count=3))
    player.db.fail_commits = 1

    with pytest.raises(RuntimeError, match="database unavailable"):
        _ = await player.service(mock_def_repo).turn_in(player.player_id, "gather_daisies", "npc", "54")

    assert player.carried()[0]["quantity"] == 5
    assert player.quest("gather_daisies").state == "active"


@pytest.mark.asyncio
async def test_turn_in_short_of_items_consumes_nothing(mock_def_repo: _MockDefRepo):
    player = _Player([_daisies(1)], {"gather_daisies": {"0": 1}})
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(turn_in_entities=["54"], count=3))

    result = await player.service(mock_def_repo).turn_in(player.player_id, "gather_daisies", "npc", "54")

    assert result["success"] is False
    assert player.db.last_inventory_write() is None
    assert player.quest("gather_daisies").state == "active"


@pytest.mark.asyncio
async def test_start_quest_rejects_auto_complete_with_turn_in(mock_def_repo: _MockDefRepo):
    """Validation rejects auto_complete true combined with turn_in_entities."""
    player = _Player([])
    mock_def_repo.get_by_id = AsyncMock(
        return_value=_make_collect_quest_row(auto_complete=True, turn_in_entities=["54"])
    )

    result = await player.service(mock_def_repo).start_quest(player.player_id, "gather_daisies")

    assert result["success"] is False
    assert "auto_complete" in result["message"].lower()


@pytest.mark.asyncio
async def test_start_quest_rejects_turn_in_without_entities(mock_def_repo: _MockDefRepo):
    """Validation rejects non-auto-complete quest without turn_in_entities."""
    player = _Player([])
    mock_def_repo.get_by_id = AsyncMock(return_value=_make_collect_quest_row(auto_complete=False, turn_in_entities=[]))

    result = await player.service(mock_def_repo).start_quest(player.player_id, "gather_daisies")

    assert result["success"] is False
    assert "turn_in_entities" in result["message"].lower()
