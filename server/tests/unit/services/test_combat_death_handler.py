"""Unit tests for CombatDeathHandler."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.combat_death_handler import CombatDeathHandler


@pytest.fixture
def combat_service():
    svc = MagicMock()
    svc.get_connection_manager = MagicMock(return_value=None)
    svc.get_npc_combat_integration_service = MagicMock(return_value=None)
    svc.publish_npc_died_event_to_nats = AsyncMock(return_value=True)
    return svc


@pytest.fixture
def handler(combat_service):
    return CombatDeathHandler(combat_service)


@pytest.fixture
def combat():
    instance = MagicMock(spec=CombatInstance)
    instance.combat_id = uuid.uuid4()
    instance.room_id = "room-001"
    return instance


@pytest.fixture
def player_target():
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name="Victim",
        participant_type=CombatParticipantType.PLAYER,
        current_dp=-10,
        max_dp=100,
        dexterity=10,
    )


@pytest.fixture
def npc_target():
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        name="Goblin",
        participant_type=CombatParticipantType.NPC,
        current_dp=0,
        max_dp=30,
        dexterity=8,
    )


def test_resolve_connection_manager_from_service(handler, combat_service):
    manager = MagicMock()
    combat_service.get_connection_manager.return_value = manager
    assert handler._resolve_connection_manager_for_corpse_creation() is manager


def test_resolve_connection_manager_missing_getter(handler, combat_service):
    del combat_service.get_connection_manager
    assert handler._resolve_connection_manager_for_corpse_creation() is None


@pytest.mark.asyncio
@patch("server.services.combat_death_handler.CombatDeathHandler._create_corpse_on_death", new_callable=AsyncMock)
@patch("server.services.combat_messaging_integration.combat_messaging_integration")
async def test_handle_player_death_events_success(mock_messaging, mock_corpse, handler, player_target, combat):
    mock_messaging.broadcast_player_death = AsyncMock(return_value=True)
    await handler._handle_player_death_events(player_target, combat)
    mock_messaging.broadcast_player_death.assert_awaited_once()
    mock_corpse.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.services.combat_messaging_integration.combat_messaging_integration")
async def test_handle_player_death_events_broadcast_error(mock_messaging, handler, player_target, combat):
    mock_messaging.broadcast_player_death = AsyncMock(side_effect=RuntimeError("nats down"))
    await handler._handle_player_death_events(player_target, combat)


@pytest.mark.asyncio
@patch("server.container.ApplicationContainer.get_instance", side_effect=RuntimeError("no container"))
async def test_create_corpse_skips_without_persistence(_mock_get_instance, handler, player_target, combat):
    # Explicitly fail container lookup so xdist cannot see a live ApplicationContainer singleton.
    await handler._create_corpse_on_death(player_target, combat)


@pytest.mark.asyncio
@patch("server.services.corpse_lifecycle_service.CorpseLifecycleService")
@patch("server.container.ApplicationContainer.get_instance")
async def test_create_corpse_success(mock_container_cls, mock_corpse_cls, handler, player_target, combat):
    persistence = MagicMock()
    container = MagicMock()
    container.connection_manager = MagicMock()
    container.async_persistence = persistence
    mock_container_cls.return_value = container
    corpse = MagicMock(container_id=uuid.uuid4())
    mock_corpse_cls.return_value.create_corpse_on_death = AsyncMock(return_value=corpse)
    await handler._create_corpse_on_death(player_target, combat)
    mock_corpse_cls.return_value.create_corpse_on_death.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.services.corpse_lifecycle_service.CorpseLifecycleService")
@patch("server.container.ApplicationContainer.get_instance")
async def test_create_corpse_service_error(mock_container_cls, mock_corpse_cls, handler, player_target, combat):
    container = MagicMock()
    container.connection_manager = None
    container.async_persistence = MagicMock()
    mock_container_cls.return_value = container
    mock_corpse_cls.return_value.create_corpse_on_death = AsyncMock(side_effect=OSError("disk"))
    await handler._create_corpse_on_death(player_target, combat)


@patch("server.container.ApplicationContainer.get_instance")
def test_log_room_subscribers(mock_container_cls, handler, combat):
    manager = MagicMock()
    manager.canonical_room_id.return_value = "room-001"
    manager.room_subscriptions = {"room-001": {"player-1"}}
    container = MagicMock(connection_manager=manager)
    mock_container_cls.return_value = container
    handler._log_room_subscribers_before_npc_death(combat)


@patch("server.container.ApplicationContainer.get_instance", side_effect=RuntimeError("no container"))
def test_log_room_subscribers_error(mock_container_cls, handler, combat):
    handler._log_room_subscribers_before_npc_death(combat)


def test_resolve_original_npc_id_no_integration(handler, npc_target, combat):
    npc_id = handler._resolve_original_npc_id(npc_target, combat)
    assert npc_id == str(npc_target.participant_id)


def test_resolve_original_npc_id_with_mapping(handler, combat_service, npc_target, combat):
    integration = MagicMock()
    integration.get_original_string_id.return_value = "npc-string-1"
    combat_service.get_npc_combat_integration_service.return_value = integration
    assert handler._resolve_original_npc_id(npc_target, combat) == "npc-string-1"


def test_resolve_original_npc_id_missing_mapping(handler, combat_service, npc_target, combat):
    integration = MagicMock()
    integration.get_original_string_id.return_value = None
    combat_service.get_npc_combat_integration_service.return_value = integration
    assert handler._resolve_original_npc_id(npc_target, combat) == str(npc_target.participant_id)


@pytest.mark.asyncio
async def test_publish_npc_death_event_success(handler, combat_service, npc_target, combat):
    await handler._publish_npc_death_event(npc_target, combat, 50, "killer-1", "npc-string-1")
    combat_service.publish_npc_died_event_to_nats.assert_awaited_once()


@pytest.mark.asyncio
async def test_publish_npc_death_event_error(handler, combat_service, npc_target, combat):
    combat_service.publish_npc_died_event_to_nats = AsyncMock(side_effect=RuntimeError("publish failed"))
    await handler._publish_npc_death_event(npc_target, combat, 50, None, "npc-string-1")


@pytest.mark.asyncio
@patch.object(CombatDeathHandler, "_publish_npc_death_event", new_callable=AsyncMock)
@patch.object(CombatDeathHandler, "_resolve_original_npc_id", return_value="npc-1")
@patch.object(CombatDeathHandler, "_log_room_subscribers_before_npc_death")
async def test_handle_npc_death(mock_log, mock_resolve, mock_publish, handler, npc_target, combat):
    await handler.handle_npc_death(npc_target, combat, 25, killer_id="killer-1")
    mock_log.assert_called_once()
    mock_resolve.assert_called_once()
    mock_publish.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.services.combat_messaging_integration.combat_messaging_integration")
async def test_handle_target_state_mortally_wounded(mock_messaging, handler, player_target, combat):
    mock_messaging.broadcast_player_mortally_wounded = AsyncMock(return_value=True)
    attacker = MagicMock(name="Attacker")
    await handler.handle_target_state_changes(
        player_target, attacker, target_mortally_wounded=True, target_died=False, combat=combat
    )
    mock_messaging.broadcast_player_mortally_wounded.assert_awaited_once()


@pytest.mark.asyncio
@patch.object(CombatDeathHandler, "_handle_player_death_events", new_callable=AsyncMock)
async def test_handle_target_state_player_death(mock_death, handler, player_target, combat):
    await handler.handle_target_state_changes(
        player_target, MagicMock(), target_mortally_wounded=False, target_died=True, combat=combat
    )
    mock_death.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.services.combat_messaging_integration.combat_messaging_integration")
async def test_handle_target_state_mortally_wounded_error(mock_messaging, handler, player_target, combat):
    mock_messaging.broadcast_player_mortally_wounded = AsyncMock(side_effect=KeyError("bad"))
    await handler.handle_target_state_changes(
        player_target, MagicMock(), target_mortally_wounded=True, target_died=False, combat=combat
    )
