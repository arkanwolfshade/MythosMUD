"""
Unit tests for QuestService collect_n sync, auto-complete, and turn-in consumption.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.quest.quest_service import QuestService

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters
# pylint: disable=protected-access  # Reason: Tests may access protected members for verification


@pytest.fixture
def mock_def_repo():
    """Mock QuestDefinitionRepository."""
    repo = MagicMock()
    repo.get_by_id = AsyncMock(return_value=None)
    repo.get_by_name = AsyncMock(return_value=None)
    repo.list_quest_ids_offered_by = AsyncMock(return_value=[])
    return repo


@pytest.fixture
def mock_instance_repo():
    """Mock QuestInstanceRepository."""
    repo = MagicMock()
    repo.create = AsyncMock()
    repo.get_by_player_and_quest = AsyncMock(return_value=None)
    repo.list_active_by_player = AsyncMock(return_value=[])
    repo.list_completed_by_player = AsyncMock(return_value=[])
    repo.update_state_and_progress = AsyncMock()
    return repo


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
        "goals": [
            {
                "type": "collect_n",
                "target": "misc.herb.sanitarium_daisy",
                "config": {"count": count},
            }
        ],
        "rewards": [{"type": "xp", "config": {"amount": 5}}],
        "triggers": [{"type": "npc", "entity_id": "54"}],
        "requires_all": [],
        "requires_any": [],
        "auto_complete": auto_complete,
        "turn_in_entities": turn_in_entities if turn_in_entities is not None else (["54"] if not auto_complete else []),
    }
    return row


def _make_inventory_player(inventory: list[dict], equipped: dict | None = None) -> MagicMock:
    """Mock player with inventory getters/setters."""
    player = MagicMock()
    player.get_inventory = MagicMock(return_value=inventory)
    player.get_equipped_items = MagicMock(return_value=equipped or {})
    player.set_inventory = MagicMock()
    player.set_equipped_items = MagicMock()
    return player


def _quest_service_with_persistence(mock_def_repo, mock_instance_repo, player: MagicMock) -> QuestService:
    """QuestService wired with async_persistence returning player."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_id = AsyncMock(return_value=player)
    mock_persistence.save_player = AsyncMock()
    return QuestService(
        quest_definition_repository=mock_def_repo,
        quest_instance_repository=mock_instance_repo,
        async_persistence=mock_persistence,
    )


@pytest.mark.asyncio
async def test_start_quest_collect_n_seeds_progress_from_holdings(mock_def_repo, mock_instance_repo):
    """start_quest syncs collect_n progress from current inventory."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=False, turn_in_entities=["54"])
    player = _make_inventory_player([{"prototype_id": "misc.herb.sanitarium_daisy", "quantity": 2}])
    svc = _quest_service_with_persistence(mock_def_repo, mock_instance_repo, player)
    active_instance = MagicMock()
    active_instance.id = uuid.uuid4()
    active_instance.quest_id = "gather_daisies"
    active_instance.progress = {}
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)
    mock_instance_repo.create = AsyncMock()
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[active_instance])

    result = await svc.start_quest(player_id, "gather_daisies")

    assert result["success"] is True
    mock_instance_repo.create.assert_awaited_once_with(player_id, "gather_daisies", state="active", progress={})
    progress_call = mock_instance_repo.update_state_and_progress.call_args[1]
    assert progress_call.get("progress") == {"0": 2}


@pytest.mark.asyncio
async def test_sync_collect_progress_updates_on_inventory_change(mock_def_repo, mock_instance_repo):
    """sync_collect_progress reflects increased and decreased holdings."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=True, turn_in_entities=[])
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "gather_daisies"
    instance.progress = {"0": 1}
    player = _make_inventory_player([{"prototype_id": "misc.herb.sanitarium_daisy", "quantity": 3}])
    svc = _quest_service_with_persistence(mock_def_repo, mock_instance_repo, player)
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    await svc.sync_collect_progress(player_id)

    assert mock_instance_repo.update_state_and_progress.await_count >= 1
    progress_call = mock_instance_repo.update_state_and_progress.call_args_list[0][1]
    assert progress_call.get("progress") == {"0": 3}


@pytest.mark.asyncio
async def test_sync_collect_progress_nested_container(mock_def_repo, mock_instance_repo):
    """Nested inner_container items count toward collect_n progress."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=False, turn_in_entities=["54"])
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "gather_daisies"
    instance.progress = {}
    inventory = [
        {
            "prototype_id": "wearable.pouch",
            "quantity": 1,
            "inner_container": {
                "items": [{"prototype_id": "misc.herb.sanitarium_daisy", "quantity": 2}],
            },
        }
    ]
    player = _make_inventory_player(inventory)
    svc = _quest_service_with_persistence(mock_def_repo, mock_instance_repo, player)
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    await svc.sync_collect_progress(player_id)

    progress_call = mock_instance_repo.update_state_and_progress.call_args[1]
    assert progress_call.get("progress") == {"0": 2}


@pytest.mark.asyncio
async def test_collect_n_auto_complete_keeps_items(mock_def_repo, mock_instance_repo):
    """Auto-complete collect_n quest does not consume inventory."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=True, turn_in_entities=[], count=2)
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "gather_daisies"
    instance.progress = {}
    inventory = [{"prototype_id": "misc.herb.sanitarium_daisy", "quantity": 2}]
    player = _make_inventory_player(inventory)
    svc = _quest_service_with_persistence(mock_def_repo, mock_instance_repo, player)
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    await svc.sync_collect_progress(player_id)

    player.set_inventory.assert_not_called()
    completed = any(
        c[1].get("state") == "completed" for c in mock_instance_repo.update_state_and_progress.call_args_list
    )
    assert completed


@pytest.mark.asyncio
async def test_turn_in_collect_n_consumes_items(mock_def_repo, mock_instance_repo):
    """Turn-in consumes required collect_n items before completion."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=False, turn_in_entities=["54"], count=3)
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "gather_daisies"
    instance.state = "active"
    instance.progress = {"0": 3}
    inventory = [{"prototype_id": "misc.herb.sanitarium_daisy", "quantity": 5}]
    player = _make_inventory_player(inventory)
    svc = _quest_service_with_persistence(mock_def_repo, mock_instance_repo, player)
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=instance)
    mock_instance_repo.update_state_and_progress = AsyncMock()
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])

    result = await svc.turn_in(player_id, "gather_daisies", "npc", "54")

    assert result["success"] is True
    player.set_inventory.assert_called_once()
    saved = player.set_inventory.call_args[0][0]
    assert saved[0]["quantity"] == 2


@pytest.mark.asyncio
async def test_start_quest_rejects_auto_complete_with_turn_in(mock_def_repo, mock_instance_repo):
    """Validation rejects auto_complete true combined with turn_in_entities."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=True, turn_in_entities=["54"])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)

    result = await QuestService(mock_def_repo, mock_instance_repo).start_quest(player_id, "gather_daisies")

    assert result["success"] is False
    assert "auto_complete" in result["message"].lower()


@pytest.mark.asyncio
async def test_start_quest_rejects_turn_in_without_entities(mock_def_repo, mock_instance_repo):
    """Validation rejects non-auto-complete quest without turn_in_entities."""
    player_id = uuid.uuid4()
    row = _make_collect_quest_row(auto_complete=False, turn_in_entities=[])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)

    svc = QuestService(mock_def_repo, mock_instance_repo)
    result = await svc.start_quest(player_id, "gather_daisies")

    assert result["success"] is False
    assert "turn_in_entities" in result["message"].lower()
