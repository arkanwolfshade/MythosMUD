"""Unit tests for PassiveMobNPC."""

import uuid
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from server.npc.passive_mob_npc import PassiveMobNPC


@pytest.fixture
def passive_npc() -> PassiveMobNPC:
    definition = SimpleNamespace(name="Rat", npc_type="passive_mob")
    npc = PassiveMobNPC(definition=definition, npc_id="npc-rat-1")
    npc._behavior_config = {
        "idle_movement_enabled": True,
        "idle_movement_interval": 10,
        "response_chance": 0.8,
    }
    npc.speak = MagicMock(return_value=True)
    return npc


def test_get_behavior_rules_returns_list(passive_npc: PassiveMobNPC) -> None:
    rules = passive_npc.get_behavior_rules()
    assert isinstance(rules, list)
    assert len(rules) >= 2


def test_should_schedule_movement_disabled(passive_npc: PassiveMobNPC) -> None:
    passive_npc._behavior_config["idle_movement_enabled"] = False
    assert passive_npc._should_schedule_movement(100.0) is False


def test_should_schedule_movement_first_time(passive_npc: PassiveMobNPC) -> None:
    passive_npc._last_idle_movement_time = None
    assert passive_npc._should_schedule_movement(100.0) is True


def test_should_schedule_movement_interval_not_elapsed(passive_npc: PassiveMobNPC) -> None:
    passive_npc._last_idle_movement_time = 95.0
    assert passive_npc._should_schedule_movement(100.0) is False


def test_should_schedule_movement_interval_elapsed(passive_npc: PassiveMobNPC) -> None:
    passive_npc._last_idle_movement_time = 80.0
    assert passive_npc._should_schedule_movement(100.0) is True


def test_create_wander_action(passive_npc: PassiveMobNPC) -> None:
    action = passive_npc._create_wander_action(123.45)
    assert action.npc_id == "npc-rat-1"
    assert action.timestamp == 123.45


def test_queue_wander_action_no_service(passive_npc: PassiveMobNPC) -> None:
    action = passive_npc._create_wander_action(1.0)
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        assert passive_npc._queue_wander_action(action, 1.0) is False


def test_respond_to_player_high_chance(passive_npc: PassiveMobNPC) -> None:
    player_id = str(uuid.uuid4())
    assert passive_npc.respond_to_player(player_id, "greet") is True
    passive_npc.speak.assert_called_once()


def test_respond_to_player_low_chance(passive_npc: PassiveMobNPC) -> None:
    passive_npc._behavior_config["response_chance"] = 0.1
    player_id = str(uuid.uuid4())
    assert passive_npc.respond_to_player(player_id, "greet") is False


def test_handle_respond_to_greeting(passive_npc: PassiveMobNPC) -> None:
    player_id = str(uuid.uuid4())
    with patch.object(passive_npc, "respond_to_player", return_value=True) as mock_resp:
        assert passive_npc._handle_respond_to_greeting({"player_id": player_id}) is True
    mock_resp.assert_called_once_with(player_id, "greet")


def test_handle_flee(passive_npc: PassiveMobNPC) -> None:
    assert passive_npc._handle_flee({}) is True
    passive_npc.speak.assert_called_once()


def test_schedule_idle_movement_queues_action(passive_npc: PassiveMobNPC) -> None:
    action = passive_npc._create_wander_action(50.0)
    with (
        patch.object(passive_npc, "_should_schedule_movement", return_value=True),
        patch.object(passive_npc, "_create_wander_action", return_value=action),
        patch.object(passive_npc, "_queue_wander_action", return_value=True),
    ):
        assert passive_npc.schedule_idle_movement() is True


def test_schedule_idle_movement_fallback_wander(passive_npc: PassiveMobNPC) -> None:
    with (
        patch.object(passive_npc, "_should_schedule_movement", return_value=True),
        patch.object(passive_npc, "_queue_wander_action", return_value=False),
        patch.object(passive_npc, "wander", return_value=True) as mock_wander,
    ):
        assert passive_npc.schedule_idle_movement() is True
    mock_wander.assert_called_once()


def test_wander_no_persistence(passive_npc: PassiveMobNPC) -> None:
    mock_container = MagicMock(async_persistence=None)
    with patch("server.container.ApplicationContainer.get_instance", return_value=mock_container):
        assert passive_npc.wander() is False


def test_wander_success(passive_npc: PassiveMobNPC) -> None:
    mock_persistence = MagicMock()
    mock_container = MagicMock(async_persistence=mock_persistence)
    mock_handler = MagicMock()
    mock_handler.execute_idle_movement.return_value = True

    with (
        patch("server.container.ApplicationContainer.get_instance", return_value=mock_container),
        patch("server.npc.idle_movement.IdleMovementHandler", return_value=mock_handler),
    ):
        assert passive_npc.wander() is True
    assert passive_npc._last_idle_movement_time is not None
