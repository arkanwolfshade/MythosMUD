"""
Unit tests for QuestService.

Covers: resolve_name_to_quest_id, start_quest, abandon, get_quest_log with mocked repos.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.quest.quest_service import QuestService

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which triggers this warning but is the standard pytest pattern
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior


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


def _make_definition_row(quest_id: str = "leave_the_tutorial", name: str = "leave_the_tutorial"):
    """Build a mock definition row with definition JSONB."""
    row = MagicMock()
    row.id = quest_id
    row.definition = {
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
    }
    return row


@pytest.fixture
def quest_service(request):
    """QuestService with mocked repos."""
    def_repo = request.getfixturevalue("mock_def_repo")
    instance_repo = request.getfixturevalue("mock_instance_repo")
    return QuestService(
        quest_definition_repository=def_repo,
        quest_instance_repository=instance_repo,
    )


# ---- resolve_name_to_quest_id ----
@pytest.mark.asyncio
async def test_resolve_name_to_quest_id_found(quest_service, mock_def_repo):
    """resolve_name_to_quest_id returns quest_id when definition exists."""
    row = _make_definition_row()
    mock_def_repo.get_by_name = AsyncMock(return_value=row)

    result = await quest_service.resolve_name_to_quest_id("leave_the_tutorial")

    assert result == "leave_the_tutorial"
    mock_def_repo.get_by_name.assert_awaited_once_with("leave_the_tutorial")


@pytest.mark.asyncio
async def test_resolve_name_to_quest_id_not_found(quest_service, mock_def_repo):
    """resolve_name_to_quest_id returns None when definition missing."""
    mock_def_repo.get_by_name = AsyncMock(return_value=None)

    result = await quest_service.resolve_name_to_quest_id("unknown_quest")

    assert result is None


# ---- start_quest ----
@pytest.mark.asyncio
async def test_start_quest_success(quest_service, mock_def_repo, mock_instance_repo):
    """start_quest creates instance and returns success when prereqs met."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)
    mock_instance_repo.create = AsyncMock()

    result = await quest_service.start_quest(player_id, "leave_the_tutorial")

    assert result["success"] is True
    assert "started" in result["message"].lower()
    mock_instance_repo.create.assert_awaited_once_with(player_id, "leave_the_tutorial", state="active", progress={})


@pytest.mark.asyncio
async def test_start_quest_not_found(quest_service, mock_def_repo):
    """start_quest returns error when quest id not found."""
    mock_def_repo.get_by_id = AsyncMock(return_value=None)

    result = await quest_service.start_quest(uuid.uuid4(), "unknown_quest")

    assert result["success"] is False
    assert "not found" in result["message"].lower()


@pytest.mark.asyncio
async def test_start_quest_already_active(quest_service, mock_def_repo, mock_instance_repo):
    """start_quest returns error when player already has active instance."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    existing = MagicMock()
    existing.state = "active"
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=existing)

    result = await quest_service.start_quest(player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "already have" in result["message"].lower()
    mock_instance_repo.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_start_quest_already_completed(quest_service, mock_def_repo, mock_instance_repo):
    """start_quest returns error when player already completed quest."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    existing = MagicMock()
    existing.state = "completed"
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=existing)

    result = await quest_service.start_quest(player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "already completed" in result["message"].lower()


@pytest.mark.asyncio
async def test_start_quest_prereq_not_met(quest_service, mock_def_repo, mock_instance_repo):
    """start_quest returns error when requires_all not satisfied."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    row.definition["requires_all"] = ["other_quest"]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)

    result = await quest_service.start_quest(player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "prerequisite" in result["message"].lower()
    mock_instance_repo.create.assert_not_awaited()


@pytest.mark.asyncio
async def test_start_quest_requires_any_satisfied(quest_service, mock_def_repo, mock_instance_repo):
    """start_quest succeeds when requires_any has at least one completed."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    row.definition["requires_any"] = ["quest_a", "quest_b"]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    completed_a = MagicMock()
    completed_a.state = "completed"
    # First call: existing instance for leave_the_tutorial (None); then requires_any quest_a, quest_b
    mock_instance_repo.get_by_player_and_quest = AsyncMock(side_effect=[None, completed_a, None])
    mock_instance_repo.create = AsyncMock()

    result = await quest_service.start_quest(player_id, "leave_the_tutorial")

    assert result["success"] is True
    mock_instance_repo.create.assert_awaited_once_with(player_id, "leave_the_tutorial", state="active", progress={})


# ---- start_quest_by_trigger ----
@pytest.mark.asyncio
async def test_start_quest_by_trigger_starts_matching_quest(quest_service, mock_def_repo, mock_instance_repo):
    """start_quest_by_trigger returns result from start_quest when offer and trigger match."""
    player_id = uuid.uuid4()
    mock_def_repo.list_quest_ids_offered_by = AsyncMock(return_value=["leave_the_tutorial"])
    row = _make_definition_row()
    row.definition["triggers"] = [{"type": "room", "entity_id": "tutorial_room_001"}]
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)
    mock_instance_repo.create = AsyncMock()

    results = await quest_service.start_quest_by_trigger(player_id, "room", "tutorial_room_001")

    assert len(results) == 1
    assert results[0]["success"] is True
    mock_instance_repo.create.assert_awaited_once()


@pytest.mark.asyncio
async def test_start_quest_by_trigger_skips_when_no_offer(quest_service, mock_def_repo):
    """start_quest_by_trigger returns empty list when entity offers no quests."""
    mock_def_repo.list_quest_ids_offered_by = AsyncMock(return_value=[])

    results = await quest_service.start_quest_by_trigger(uuid.uuid4(), "room", "unknown_room")

    assert results == []


# ---- record_complete_activity ----
@pytest.mark.asyncio
async def test_record_complete_activity_updates_progress(quest_service, mock_def_repo, mock_instance_repo):
    """record_complete_activity updates instance progress for matching complete_activity goal."""
    player_id = uuid.uuid4()
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "leave_the_tutorial"
    instance.progress = {}
    row = _make_definition_row()
    row.definition["goals"] = [{"type": "complete_activity", "target": "exit_tutorial_room", "config": {}}]
    row.definition["auto_complete"] = False
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    await quest_service.record_complete_activity(player_id, "exit_tutorial_room")

    mock_instance_repo.update_state_and_progress.assert_awaited_once()
    call_kw = mock_instance_repo.update_state_and_progress.call_args[1]
    assert call_kw.get("progress") == {"0": 1}


@pytest.mark.asyncio
async def test_record_complete_activity_auto_completes_when_goals_met(quest_service, mock_def_repo, mock_instance_repo):
    """When all goals met and auto_complete true, record_complete_activity completes the instance."""
    player_id = uuid.uuid4()
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "leave_the_tutorial"
    instance.progress = {}
    row = _make_definition_row()
    row.definition["goals"] = [{"type": "complete_activity", "target": "exit_tutorial_room", "config": {}}]
    row.definition["auto_complete"] = True
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    await quest_service.record_complete_activity(player_id, "exit_tutorial_room")

    assert mock_instance_repo.update_state_and_progress.await_count >= 2
    calls = [c[1] for c in mock_instance_repo.update_state_and_progress.call_args_list]
    completed_call = next((c for c in calls if c.get("state") == "completed"), None)
    assert completed_call is not None


# ---- record_kill ----
@pytest.mark.asyncio
async def test_record_kill_updates_progress(quest_service, mock_def_repo, mock_instance_repo):
    """record_kill updates instance progress for matching kill_n goal."""
    player_id = uuid.uuid4()
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "kill_quest"
    instance.progress = {"0": 0}
    row = MagicMock()
    row.id = "kill_quest"
    row.definition = {
        "name": "kill_quest",
        "title": "Kill 3 Rats",
        "description": "Kill rats.",
        "goals": [{"type": "kill_n", "target": "npc_rat", "config": {"count": 3}}],
        "rewards": [],
        "triggers": [],
        "requires_all": [],
        "requires_any": [],
        "auto_complete": True,
        "turn_in_entities": [],
    }
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    await quest_service.record_kill(player_id, "npc_rat")

    mock_instance_repo.update_state_and_progress.assert_awaited_once()
    call_kw = mock_instance_repo.update_state_and_progress.call_args[1]
    assert call_kw.get("progress") == {"0": 1}


# ---- abandon ----
@pytest.mark.asyncio
async def test_abandon_success(quest_service, mock_def_repo, mock_instance_repo):
    """abandon updates instance to abandoned and returns success."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.state = "active"
    mock_def_repo.get_by_name = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=instance)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    result = await quest_service.abandon(player_id, "leave_the_tutorial")

    assert result["success"] is True
    assert "abandoned" in result["message"].lower()
    mock_instance_repo.update_state_and_progress.assert_awaited_once_with(instance.id, state="abandoned")


@pytest.mark.asyncio
async def test_abandon_unknown_quest(quest_service, mock_def_repo):
    """abandon returns error when quest name not found."""
    mock_def_repo.get_by_name = AsyncMock(return_value=None)

    result = await quest_service.abandon(uuid.uuid4(), "unknown_quest")

    assert result["success"] is False
    assert "unknown" in result["message"].lower() or "Unknown" in result["message"]


@pytest.mark.asyncio
async def test_abandon_no_instance(quest_service, mock_def_repo, mock_instance_repo):
    """abandon returns error when player has no instance."""
    row = _make_definition_row()
    mock_def_repo.get_by_name = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)

    result = await quest_service.abandon(uuid.uuid4(), "leave_the_tutorial")

    assert result["success"] is False
    assert "do not have" in result["message"].lower()
    mock_instance_repo.update_state_and_progress.assert_not_awaited()


@pytest.mark.asyncio
async def test_abandon_not_active(quest_service, mock_def_repo, mock_instance_repo):
    """abandon returns error when instance is not active."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.state = "completed"
    mock_def_repo.get_by_name = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=instance)

    result = await quest_service.abandon(player_id, "leave_the_tutorial")

    assert result["success"] is False
    assert "only abandon an active" in result["message"].lower()
    mock_instance_repo.update_state_and_progress.assert_not_awaited()


# ---- get_quest_log ----
@pytest.mark.asyncio
async def test_get_quest_log_empty(quest_service, mock_instance_repo):
    """get_quest_log returns empty list when no active or completed."""
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[])
    mock_instance_repo.list_completed_by_player = AsyncMock(return_value=[])

    result = await quest_service.get_quest_log(uuid.uuid4(), include_completed=True)

    assert result == []


@pytest.mark.asyncio
async def test_get_quest_log_excludes_completed_when_requested(quest_service, mock_instance_repo):
    """get_quest_log with include_completed=False does not call list_completed_by_player."""
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[])
    mock_instance_repo.list_completed_by_player = AsyncMock(return_value=[])

    await quest_service.get_quest_log(uuid.uuid4(), include_completed=False)

    mock_instance_repo.list_completed_by_player.assert_not_awaited()


@pytest.mark.asyncio
async def test_get_quest_log_returns_entries(quest_service, mock_def_repo, mock_instance_repo):
    """get_quest_log returns formatted entries for active/completed instances."""
    player_id = uuid.uuid4()
    row = _make_definition_row()
    instance = MagicMock()
    instance.quest_id = "leave_the_tutorial"
    instance.state = "active"
    instance.progress = {"0": 0}
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.list_active_by_player = AsyncMock(return_value=[instance])
    mock_instance_repo.list_completed_by_player = AsyncMock(return_value=[])

    result = await quest_service.get_quest_log(player_id, include_completed=True)

    assert len(result) == 1
    assert result[0]["quest_id"] == "leave_the_tutorial"
    assert result[0]["name"] == "leave_the_tutorial"
    assert result[0]["title"] == "Leave the Tutorial"
    assert result[0]["state"] == "active"
    assert len(result[0]["goals_with_progress"]) == 1
    assert result[0]["goals_with_progress"][0]["goal_type"] == "complete_activity"
    assert result[0]["goals_with_progress"][0]["done"] is False


# ---- turn_in ----
def _make_turn_in_definition_row(quest_id: str = "turn_in_quest"):
    """Definition with auto_complete false and turn_in_entities."""
    row = MagicMock()
    row.id = quest_id
    row.definition = {
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
    }
    return row


@pytest.mark.asyncio
async def test_turn_in_auto_complete_returns_error(quest_service, mock_def_repo):
    """turn_in returns error when quest has auto_complete true."""
    row = _make_definition_row()
    row.definition["auto_complete"] = True
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    result = await quest_service.turn_in(uuid.uuid4(), "leave_the_tutorial", "room", "any_room")

    assert result["success"] is False
    assert "automatically" in result["message"].lower()


@pytest.mark.asyncio
async def test_turn_in_success(quest_service, mock_def_repo, mock_instance_repo):
    """turn_in applies rewards and sets instance completed when goals met and at valid entity."""
    player_id = uuid.uuid4()
    row = _make_turn_in_definition_row()
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "turn_in_quest"
    instance.state = "active"
    instance.progress = {"0": 1}
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=instance)
    mock_instance_repo.update_state_and_progress = AsyncMock()

    result = await quest_service.turn_in(player_id, "turn_in_quest", "npc", "npc_quest_giver_001")

    assert result["success"] is True
    mock_instance_repo.update_state_and_progress.assert_awaited_once()
    call_kw = mock_instance_repo.update_state_and_progress.call_args[1]
    assert call_kw.get("state") == "completed"
    assert "completed_at" in call_kw


@pytest.mark.asyncio
async def test_turn_in_wrong_entity_returns_error(quest_service, mock_def_repo):
    """turn_in returns error when at_entity_id not in turn_in_entities."""
    row = _make_turn_in_definition_row()
    mock_def_repo.get_by_id = AsyncMock(return_value=row)

    result = await quest_service.turn_in(uuid.uuid4(), "turn_in_quest", "npc", "wrong_npc")

    assert result["success"] is False
    assert "cannot turn in" in result["message"].lower() or "here" in result["message"].lower()


@pytest.mark.asyncio
async def test_turn_in_no_active_instance_returns_error(quest_service, mock_def_repo, mock_instance_repo):
    """turn_in returns error when player has no active instance."""
    row = _make_turn_in_definition_row()
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=None)

    result = await quest_service.turn_in(uuid.uuid4(), "turn_in_quest", "npc", "npc_quest_giver_001")

    assert result["success"] is False
    assert "do not have" in result["message"].lower() or "active" in result["message"].lower()


@pytest.mark.asyncio
async def test_turn_in_inventory_full_blocks_item_reward(mock_def_repo, mock_instance_repo):
    """When reward is item and inventory full, turn_in returns error (block turn-in)."""
    player_id = uuid.uuid4()
    row = _make_turn_in_definition_row()
    row.definition["rewards"] = [{"type": "item", "config": {"item_id": "quest_item_1"}}]
    instance = MagicMock()
    instance.id = uuid.uuid4()
    instance.quest_id = "turn_in_quest"
    instance.state = "active"
    instance.progress = {"0": 1}
    mock_def_repo.get_by_id = AsyncMock(return_value=row)
    mock_instance_repo.get_by_player_and_quest = AsyncMock(return_value=instance)
    mock_inventory = MagicMock()
    mock_inventory.has_inventory_slot = lambda _: False
    svc = QuestService(
        quest_definition_repository=mock_def_repo,
        quest_instance_repository=mock_instance_repo,
        inventory_service=mock_inventory,
    )

    result = await svc.turn_in(player_id, "turn_in_quest", "npc", "npc_quest_giver_001")

    assert result["success"] is False
    assert "inventory" in result["message"].lower() or "full" in result["message"].lower()
