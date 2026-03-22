"""
Unit tests for NPC combat integration service.

Tests the NPCCombatIntegrationService class for integrating NPCs with the combat system.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests assert on service internals; same intent as pylint protected-access for this module.

import uuid
from typing import TYPE_CHECKING, cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_combat_integration_service import NPCCombatIntegrationService

if TYPE_CHECKING:
    pass


class _StubGameConfig:
    """Minimal ``game`` section for ``get_config`` when constructing ``NPCCombatIntegrationService`` in tests."""

    combat_tick_interval: int = 10


class _StubConfigRoot:
    """Return value for patched ``get_config`` in this module's fixtures."""

    game: _StubGameConfig = _StubGameConfig()


# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=too-many-lines  # Reason: Single module for NPCCombatIntegrationService; split only if maintenance cost grows


@pytest.fixture
def mock_combat_service() -> MagicMock:
    """Create mock combat service."""
    service = MagicMock()
    service.auto_progression_enabled = False
    service.turn_interval_seconds = 10
    return service


@pytest.fixture
def mock_messaging_integration() -> MagicMock:
    """Create mock messaging integration."""
    return MagicMock()


@pytest.fixture
def mock_connection_manager() -> MagicMock:
    """Create mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_async_persistence() -> MagicMock:
    """Create mock async persistence layer."""
    return MagicMock()


@pytest.fixture
def integration_service(
    mock_combat_service: MagicMock,
    mock_connection_manager: MagicMock,
    mock_async_persistence: MagicMock,
) -> NPCCombatIntegrationService:
    """Create NPCCombatIntegrationService instance."""
    with patch("server.services.npc_combat_integration_service.get_config") as mock_config:
        mock_config.return_value = _StubConfigRoot()
        # Signature: __init__(self, event_bus=None, combat_service=None, player_combat_service=None, connection_manager=None, async_persistence=None)
        service = NPCCombatIntegrationService(
            event_bus=None,
            combat_service=mock_combat_service,
            player_combat_service=None,
            connection_manager=mock_connection_manager,
            async_persistence=mock_async_persistence,
        )
        return service


def test_integration_service_init(
    integration_service: NPCCombatIntegrationService,
    mock_combat_service: MagicMock,
) -> None:
    """Test NPCCombatIntegrationService initialization."""
    assert integration_service._combat_service == mock_combat_service
    assert cast(bool, mock_combat_service.auto_progression_enabled) is True


def test_integration_service_init_with_shared_player_combat_service(
    mock_combat_service: MagicMock,
    mock_connection_manager: MagicMock,
    mock_async_persistence: MagicMock,
) -> None:
    """Test init sets NPC combat integration reference on shared PlayerCombatService."""
    mock_player_combat_service = MagicMock()
    with patch("server.services.npc_combat_integration_service.get_config") as mock_config:
        mock_config.return_value = _StubConfigRoot()
        service = NPCCombatIntegrationService(
            event_bus=None,
            combat_service=mock_combat_service,
            player_combat_service=mock_player_combat_service,
            connection_manager=mock_connection_manager,
            async_persistence=mock_async_persistence,
        )
    assert service._player_combat_service == mock_player_combat_service
    assert (
        cast(NPCCombatIntegrationService | None, mock_player_combat_service._npc_combat_integration_service) is service
    )


def test_integration_service_init_creates_combat_service_when_none(
    mock_connection_manager: MagicMock,
    mock_async_persistence: MagicMock,
) -> None:
    """Test init creates CombatService when combat_service is None."""
    mock_combat_service_instance = MagicMock()
    with (
        patch("server.services.npc_combat_integration_service.get_config") as mock_config,
        patch("server.services.combat_service.CombatService", return_value=mock_combat_service_instance),
    ):
        mock_config.return_value = _StubConfigRoot()
        service = NPCCombatIntegrationService(
            event_bus=None,
            combat_service=None,
            player_combat_service=None,
            connection_manager=mock_connection_manager,
            async_persistence=mock_async_persistence,
        )
    assert service._combat_service == mock_combat_service_instance


@pytest.mark.asyncio
async def test_get_integration_config(integration_service: NPCCombatIntegrationService) -> None:
    """Test integration service has combat service with config."""
    # The service doesn't have get_integration_config method, but it has _combat_service
    assert integration_service._combat_service is not None
    assert hasattr(integration_service._combat_service, "turn_interval_seconds")


def test_is_auto_progression_enabled(integration_service: NPCCombatIntegrationService) -> None:
    """Test auto_progression_enabled is set on combat service."""
    # The service doesn't have is_auto_progression_enabled method, but it sets auto_progression_enabled on _combat_service
    assert integration_service._combat_service.auto_progression_enabled is True


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc(integration_service: NPCCombatIntegrationService) -> None:
    """Test handle_player_attack_on_npc handles attack."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.npc_id = npc_id
    npc_instance.current_room = room_id
    npc_instance.current_room_id = room_id
    npc_instance.is_alive = True
    mock_data_provider = MagicMock()
    mock_data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    mock_data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    mock_data_provider.get_player_name = AsyncMock(return_value="TestPlayer")
    mock_data_provider.get_player_combat_data = AsyncMock(return_value={})
    mock_data_provider.get_npc_combat_data = MagicMock(return_value={})
    mock_data_provider.get_npc_definition = AsyncMock(return_value=None)
    integration_service._data_provider = mock_data_provider
    integration_service._combat_memory = MagicMock()
    integration_service._combat_memory.record_attack = MagicMock(return_value=True)
    integration_service._uuid_mapping = MagicMock()

    def _convert_uuid_stub(_value: object) -> uuid.UUID:
        return uuid.uuid4()

    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=_convert_uuid_stub)
    integration_service._uuid_mapping.is_valid_uuid = MagicMock(return_value=False)
    integration_service._uuid_mapping.store_string_id_mapping = MagicMock()
    integration_service._combat_service = MagicMock()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    integration_service._combat_service.start_combat = AsyncMock()
    mock_combat_result = MagicMock()
    mock_combat_result.success = True
    integration_service._combat_service.process_attack = AsyncMock(return_value=mock_combat_result)
    integration_service._handlers = MagicMock()
    integration_service._handlers.handle_combat_result = AsyncMock(return_value=True)
    integration_service.handle_npc_death = AsyncMock()
    result = await integration_service.handle_player_attack_on_npc(
        player_id, npc_id, room_id, action_type, damage, npc_instance
    )
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_provided(integration_service: NPCCombatIntegrationService) -> None:
    """Test _validate_and_get_npc_instance uses provided instance."""
    player_id = "player_001"
    npc_id = "npc_001"
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, npc_instance)
    assert result == npc_instance


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_lookup(integration_service: NPCCombatIntegrationService) -> None:
    """Test _validate_and_get_npc_instance looks up NPC when not provided."""
    player_id = "player_001"
    npc_id = "npc_001"
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, None)
    assert result == npc_instance


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_dead(integration_service: NPCCombatIntegrationService) -> None:
    """Test _validate_and_get_npc_instance returns None for dead NPC."""
    player_id = "player_001"
    npc_id = "npc_001"
    npc_instance = MagicMock()
    npc_instance.is_alive = False
    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, npc_instance)
    assert result is None


@pytest.mark.asyncio
async def test_validate_combat_location(integration_service: NPCCombatIntegrationService) -> None:
    """Test _validate_combat_location validates location."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    result = await integration_service._validate_combat_location(player_id, npc_id, room_id, npc_instance)
    assert result is True


@pytest.mark.asyncio
async def test_validate_combat_location_different_rooms(integration_service: NPCCombatIntegrationService) -> None:
    """Test _validate_combat_location returns False for different rooms."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    npc_instance = MagicMock()
    npc_instance.current_room = "room_002"
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    result = await integration_service._validate_combat_location(player_id, npc_id, room_id, npc_instance)
    assert result is False


@pytest.mark.asyncio
async def test_validate_combat_location_combat_room_mismatch(integration_service: NPCCombatIntegrationService) -> None:
    """Test _validate_combat_location returns False when room_id does not match participant rooms."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    # Pass different combat_room_id (e.g. from stale command)
    result = await integration_service._validate_combat_location(player_id, npc_id, "room_other", npc_instance)
    assert result is False


@pytest.mark.asyncio
async def test_end_combat_if_participant_in_combat_ends_combat(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Test _end_combat_if_participant_in_combat ends combat when player is in one."""
    player_id = str(uuid.uuid4())
    npc_id = "npc_001"
    combat_id = uuid.uuid4()
    mock_combat = MagicMock()
    mock_combat.combat_id = combat_id
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)
    integration_service._combat_service.end_combat = AsyncMock()
    await integration_service._end_combat_if_participant_in_combat(player_id, npc_id)
    integration_service._combat_service.get_combat_by_participant.assert_called_once()
    integration_service._combat_service.end_combat.assert_called_once_with(
        combat_id, "Invalid combat location - participants not in same room"
    )


@pytest.mark.asyncio
async def test_end_combat_if_participant_in_combat_no_combat(integration_service: NPCCombatIntegrationService) -> None:
    """Test _end_combat_if_participant_in_combat does nothing when player not in combat."""
    player_id = str(uuid.uuid4())
    npc_id = "npc_001"
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    integration_service._combat_service.end_combat = AsyncMock()
    await integration_service._end_combat_if_participant_in_combat(player_id, npc_id)
    integration_service._combat_service.get_combat_by_participant.assert_called_once()
    integration_service._combat_service.end_combat.assert_not_called()


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_room_mismatch_ends_combat(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Test handle_player_attack_on_npc ends combat and returns False when rooms differ."""
    player_id = str(uuid.uuid4())
    npc_id = "npc_001"
    room_id = "room_001"
    npc_instance = MagicMock()
    npc_instance.current_room = "room_002"
    npc_instance.is_alive = True
    integration_service._validate_and_get_npc_instance = AsyncMock(return_value=npc_instance)
    integration_service._validate_combat_location = AsyncMock(return_value=False)
    integration_service._combat_service.get_combat_by_participant = AsyncMock(
        return_value=MagicMock(combat_id=uuid.uuid4())
    )
    integration_service._combat_service.end_combat = AsyncMock()
    result = await integration_service.handle_player_attack_on_npc(player_id, npc_id, room_id)
    assert result is False
    integration_service._combat_service.end_combat.assert_called_once()


@pytest.mark.asyncio
async def test_handle_npc_death(integration_service: NPCCombatIntegrationService) -> None:
    """Test handle_npc_death handles NPC death."""
    npc_id = "npc_001"
    room_id = "room_001"
    killer_id = "player_001"
    combat_id = "combat_001"
    # Mock the handlers and data provider
    integration_service._handlers = MagicMock()
    integration_service._handlers.handle_npc_death = AsyncMock(return_value=True)
    result = await integration_service.handle_npc_death(npc_id, room_id, killer_id, combat_id)
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_handle_npc_death_broadcasts_room_update(integration_service: NPCCombatIntegrationService) -> None:
    """Test handle_npc_death broadcasts room update when killer and room are set."""
    npc_id = "npc_001"
    room_id = "room_001"
    killer_id = str(uuid.uuid4())
    integration_service._handlers = MagicMock()
    integration_service._handlers.handle_npc_death = AsyncMock(return_value=True)
    mock_player = MagicMock()
    mock_player.current_room_id = "room_002"
    integration_service._messaging_integration.connection_manager = MagicMock()
    integration_service._messaging_integration.connection_manager.get_player = AsyncMock(  # pyright: ignore[reportAny]
        return_value=mock_player
    )
    with patch("server.realtime.websocket_room_updates.broadcast_room_update", new_callable=AsyncMock):
        result = await integration_service.handle_npc_death(npc_id, room_id, killer_id, None)
    assert result is True


@pytest.mark.asyncio
async def test_handle_npc_death_broadcast_failure_non_fatal(integration_service: NPCCombatIntegrationService) -> None:
    """Test handle_npc_death still returns True when broadcast fails (non-fatal)."""
    npc_id = "npc_001"
    room_id = "room_001"
    killer_id = "player_001"
    integration_service._handlers = MagicMock()
    integration_service._handlers.handle_npc_death = AsyncMock(return_value=True)
    with patch(
        "server.realtime.websocket_room_updates.broadcast_room_update",
        new_callable=AsyncMock,
        side_effect=RuntimeError("broadcast failed"),
    ):
        result = await integration_service.handle_npc_death(npc_id, room_id, killer_id, None)
    assert result is True


def test_get_npc_combat_memory(integration_service: NPCCombatIntegrationService) -> None:
    """Test get_npc_combat_memory returns last attacker via get_attacker."""
    npc_id = "npc_001"
    integration_service._combat_memory = MagicMock()
    integration_service._combat_memory.get_attacker = MagicMock(return_value="player_001")
    result = integration_service.get_npc_combat_memory(npc_id)
    assert result == "player_001"
    integration_service._combat_memory.get_attacker.assert_called_once_with(npc_id)  # pyright: ignore[reportAny]


def test_clear_npc_combat_memory(integration_service: NPCCombatIntegrationService) -> None:
    """Test clear_npc_combat_memory clears memory."""
    npc_id = "npc_001"
    integration_service._combat_memory = MagicMock()
    integration_service._combat_memory.clear_memory = MagicMock(return_value=True)
    result = integration_service.clear_npc_combat_memory(npc_id)
    assert isinstance(result, bool)


def test_get_original_string_id(integration_service: NPCCombatIntegrationService) -> None:
    """Test get_original_string_id returns original ID."""
    uuid_id = uuid.uuid4()
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.get_original_string_id = MagicMock(return_value="npc_001")
    result = integration_service.get_original_string_id(uuid_id)
    assert result == "npc_001"


@pytest.mark.asyncio
async def test_handle_npc_attack_delegates_to_handle_npc_attack_on_player(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """handle_npc_attack ignores attack_type/npc_stats and calls handle_npc_attack_on_player."""
    integration_service.handle_npc_attack_on_player = AsyncMock(return_value=True)
    ok = await integration_service.handle_npc_attack(
        "npc_1",
        str(uuid.uuid4()),
        "room_1",
        5,
        attack_type="ignored",
        npc_stats={"ignored": 1},
    )
    assert ok is True
    integration_service.handle_npc_attack_on_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_false_when_npc_dead(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Dead or missing NPC instance aborts before combat start."""
    dead = MagicMock()
    dead.is_alive = False
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=dead)
    target = str(uuid.uuid4())
    ok = await integration_service.handle_npc_attack_on_player("npc_1", target, "room_1", 10)
    assert ok is False


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_false_without_combat_service(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """No combat service returns False after location validation."""
    npc = MagicMock()
    npc.is_alive = True
    npc.current_room = "room_1"
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc)
    integration_service._validate_combat_location = AsyncMock(return_value=True)
    integration_service._combat_service = None  # pyright: ignore[reportAttributeAccessIssue] -- test: no combat service
    target = str(uuid.uuid4())
    ok = await integration_service.handle_npc_attack_on_player("npc_1", target, "room_1", 10, npc_instance=npc)
    assert ok is False


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_blocked_during_login_grace(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Login grace period check runs before NPC validation and blocks the attack."""
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.connection_manager = MagicMock()
    mock_app.state = mock_state
    player_id = str(uuid.uuid4())
    npc = MagicMock()
    npc.is_alive = True
    with (
        patch("server.services.npc_combat_integration_service.get_config") as mock_get_config,
        patch(
            "server.services.npc_combat_integration_service.is_player_in_login_grace_period",
            return_value=True,
        ),
    ):
        cfg = MagicMock()
        cfg._app_instance = mock_app
        mock_get_config.return_value = cfg
        ok = await integration_service.handle_player_attack_on_npc(
            player_id,
            "npc_1",
            "room_1",
            damage=1,
            npc_instance=npc,
        )
    assert ok is False


@pytest.mark.asyncio
async def test_process_combat_attack_queues_when_already_in_combat(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Existing combat: successful queue returns CombatResult without immediate damage."""
    from server.models.combat import CombatResult

    att = uuid.uuid4()
    tgt = uuid.uuid4()
    existing = MagicMock()
    existing.combat_id = uuid.uuid4()
    existing.combat_round = 0
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=existing)
    integration_service._combat_service.queue_combat_action = AsyncMock(return_value=True)
    with patch("server.app.lifespan.get_current_tick", return_value=99):
        result = cast(
            CombatResult,
            await integration_service._process_combat_attack(
                player_id=str(uuid.uuid4()),
                room_id="r1",
                attacker_uuid=att,
                target_uuid=tgt,
                damage=8,
                npc_instance=MagicMock(),
            ),
        )
    assert result.success is True
    assert result.damage == 0
    assert "queued" in result.message.lower()
    integration_service._combat_service.queue_combat_action.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_combat_attack_queue_fail_falls_back_to_process_attack(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """When queue_combat_action returns False, process_attack is used immediately."""
    att = uuid.uuid4()
    tgt = uuid.uuid4()
    existing = MagicMock()
    existing.combat_id = uuid.uuid4()
    existing.combat_round = 1
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=existing)
    integration_service._combat_service.queue_combat_action = AsyncMock(return_value=False)
    integration_service._combat_service.process_attack = AsyncMock(return_value=MagicMock(success=True))
    with patch("server.app.lifespan.get_current_tick", return_value=1):
        await integration_service._process_combat_attack(
            "pid",
            "r1",
            att,
            tgt,
            3,
            MagicMock(),
        )
    integration_service._combat_service.process_attack.assert_awaited()


@pytest.mark.asyncio
async def test_process_combat_attack_starts_new_combat_when_none(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """No existing combat: start_combat then process_attack with is_initial_attack."""
    att = uuid.uuid4()
    tgt = uuid.uuid4()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    integration_service._combat_service.start_combat = AsyncMock()
    integration_service._combat_service.process_attack = AsyncMock(return_value=MagicMock(success=True))
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_name = AsyncMock(return_value="Hero")
    integration_service._data_provider.get_player_combat_data = AsyncMock(return_value={})
    integration_service._data_provider.get_npc_combat_data = MagicMock(return_value={})
    npc = MagicMock()
    with patch("server.app.lifespan.get_current_tick", return_value=5):
        await integration_service._process_combat_attack("pid", "r1", att, tgt, 4, npc)
    integration_service._combat_service.start_combat.assert_awaited_once()
    process_mock = integration_service._combat_service.process_attack
    process_mock.assert_awaited()
    assert process_mock.await_args is not None
    process_kw = process_mock.await_args.kwargs
    assert process_kw.get("is_initial_attack") is True


@pytest.mark.asyncio
async def test_end_combat_if_participant_skips_when_player_id_unparseable(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Invalid player_id UUID: no combat_service lookup."""
    integration_service._combat_service.get_combat_by_participant = AsyncMock()
    await integration_service._end_combat_if_participant_in_combat("not-a-uuid", "npc_1")
    integration_service._combat_service.get_combat_by_participant.assert_not_called()


def test_setup_combat_uuids_npc_attacker_value_error_falls_back_to_random_uuids(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """ValueError from convert_to_uuid yields fresh UUID pair (combat can still proceed downstream)."""
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=ValueError("bad id"))
    a_uuid, b_uuid = integration_service._setup_combat_uuids_npc_attacker("npc_x", str(uuid.uuid4()))
    assert isinstance(a_uuid, uuid.UUID)
    assert isinstance(b_uuid, uuid.UUID)


@pytest.mark.asyncio
async def test_validate_combat_location_false_when_player_npc_different_rooms(
    integration_service: NPCCombatIntegrationService,
) -> None:
    """Cross-room participant check fails before combat_room_id check."""
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_room_id = AsyncMock(return_value="room_a")
    npc = MagicMock()
    npc.current_room = "room_b"
    ok = await integration_service._validate_combat_location("player-1", "npc-1", "room_a", npc)
    assert ok is False


# Removed test_setup_npc_for_combat - the method setup_npc_for_combat doesn't exist on NPCCombatIntegrationService
# If this functionality is needed, the method should be implemented first
