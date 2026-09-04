"""
Unit tests for dependency injection functions in dependencies.py.

Tests all dependency injection providers to ensure proper container resolution
and error handling for missing services.

As noted in the Pnakotic Manuscripts, proper dependency resolution requires
testing both successful paths and the various failure modes that can occur
when services are not properly initialized.
"""

from unittest.mock import MagicMock

import pytest
from fastapi import Request

from server.container import ApplicationContainer
from server.dependencies import (
    get_async_persistence,
    get_catatonia_registry,
    get_chat_service,
    get_combat_service,
    get_connection_manager,
    get_container,
    get_exploration_service,
    get_magic_service,
    get_mp_regeneration_service,
    get_mythos_time_consumer,
    get_nats_message_handler,
    get_npc_lifecycle_manager,
    get_npc_population_controller,
    get_npc_spawning_service,
    get_passive_lucidity_flux_service,
    get_player_combat_service,
    get_player_death_service,
    get_player_respawn_service,
    get_player_service,
    get_player_service_for_testing,
    get_profession_service,
    get_room_service,
    get_spell_effects,
    get_spell_learning_service,
    get_spell_registry,
    get_spell_targeting_service,
    get_stats_generator,
)

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing


@pytest.fixture
def mock_request():
    """Create a mock FastAPI Request with app.state.container."""
    request = MagicMock(spec=Request)
    request.app.state.container = MagicMock(spec=ApplicationContainer)
    return request


@pytest.fixture
def mock_container(mock_request):
    """Get the container from mock_request."""
    return mock_request.app.state.container


class TestGetContainer:
    """Tests for get_container dependency function."""

    def test_get_container_success(self, mock_request):
        """Test get_container returns container when present."""
        result = get_container(mock_request)
        assert result == mock_request.app.state.container

    def test_get_container_missing_raises_runtime_error(self):
        """Test get_container raises RuntimeError when container not in app.state."""
        request = MagicMock(spec=Request)
        delattr(request.app.state, "container")

        with pytest.raises(RuntimeError, match="ApplicationContainer not found in app.state"):
            get_container(request)

    def test_get_container_no_state_attribute(self):
        """Test get_container raises RuntimeError when app.state doesn't exist."""
        request = MagicMock(spec=Request)
        delattr(request.app, "state")

        with pytest.raises(AttributeError):
            get_container(request)


class TestGetPlayerService:
    """Tests for get_player_service dependency function."""

    def test_get_player_service_success(self, mock_request, mock_container):
        """Test get_player_service returns service when present."""
        mock_service = MagicMock()
        mock_container.player_service = mock_service

        result = get_player_service(mock_request)
        assert result == mock_service

    def test_get_player_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_player_service raises RuntimeError when service is None."""
        mock_container.player_service = None

        with pytest.raises(RuntimeError, match="PlayerService not initialized in container"):
            get_player_service(mock_request)


class TestGetPlayerServiceForTesting:
    """Tests for get_player_service_for_testing helper function."""

    def test_get_player_service_for_testing_with_provided_service(self):
        """Test get_player_service_for_testing returns provided service."""
        mock_service = MagicMock()
        result = get_player_service_for_testing(mock_service)
        assert result == mock_service

    def test_get_player_service_for_testing_creates_mock(self):
        """Test get_player_service_for_testing creates PlayerService when None provided."""
        result = get_player_service_for_testing(None)
        assert result is not None
        # Verify it's a PlayerService instance (it creates a real instance with mock persistence)
        from server.game.player_service import PlayerService

        assert isinstance(result, PlayerService)
        assert hasattr(result, "persistence")  # PlayerService has persistence attribute


class TestGetRoomService:
    """Tests for get_room_service dependency function."""

    def test_get_room_service_success(self, mock_request, mock_container):
        """Test get_room_service returns service when present."""
        mock_service = MagicMock()
        mock_container.room_service = mock_service

        result = get_room_service(mock_request)
        assert result == mock_service

    def test_get_room_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_room_service raises RuntimeError when service is None."""
        mock_container.room_service = None

        with pytest.raises(RuntimeError, match="RoomService not initialized in container"):
            get_room_service(mock_request)


class TestGetStatsGenerator:
    """Tests for get_stats_generator dependency function."""

    def test_get_stats_generator_returns_instance(self):
        """Test get_stats_generator returns StatsGenerator instance."""
        result = get_stats_generator()
        assert result is not None
        # StatsGenerator is stateless, so multiple calls should work
        result2 = get_stats_generator()
        assert result is not result2  # Different instances


class TestGetConnectionManager:
    """Tests for get_connection_manager dependency function."""

    def test_get_connection_manager_success(self, mock_request, mock_container):
        """Test get_connection_manager returns service when present."""
        mock_service = MagicMock()
        mock_container.connection_manager = mock_service

        result = get_connection_manager(mock_request)
        assert result == mock_service

    def test_get_connection_manager_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_connection_manager raises RuntimeError when service is None."""
        mock_container.connection_manager = None

        with pytest.raises(RuntimeError, match="ConnectionManager not initialized in container"):
            get_connection_manager(mock_request)


class TestGetAsyncPersistence:
    """Tests for get_async_persistence dependency function."""

    def test_get_async_persistence_success(self, mock_request, mock_container):
        """Test get_async_persistence returns service when present."""
        mock_service = MagicMock()
        mock_container.async_persistence = mock_service

        result = get_async_persistence(mock_request)
        assert result == mock_service

    def test_get_async_persistence_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_async_persistence raises RuntimeError when service is None."""
        mock_container.async_persistence = None

        with pytest.raises(RuntimeError, match="AsyncPersistenceLayer not initialized in container"):
            get_async_persistence(mock_request)


class TestGetExplorationService:
    """Tests for get_exploration_service dependency function."""

    def test_get_exploration_service_success(self, mock_request, mock_container):
        """Test get_exploration_service returns service when present."""
        mock_service = MagicMock()
        mock_container.exploration_service = mock_service

        result = get_exploration_service(mock_request)
        assert result == mock_service

    def test_get_exploration_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_exploration_service raises RuntimeError when service is None."""
        mock_container.exploration_service = None

        with pytest.raises(RuntimeError, match="ExplorationService not initialized in container"):
            get_exploration_service(mock_request)


class TestGetPlayerRespawnService:
    """Tests for get_player_respawn_service dependency function."""

    def test_get_player_respawn_service_success(self, mock_request, mock_container):
        """Test get_player_respawn_service returns service when present."""
        mock_service = MagicMock()
        mock_container.player_respawn_service = mock_service

        result = get_player_respawn_service(mock_request)
        assert result == mock_service

    def test_get_player_respawn_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_player_respawn_service raises RuntimeError when service is None."""
        mock_container.player_respawn_service = None

        with pytest.raises(RuntimeError, match="PlayerRespawnService not initialized in container"):
            get_player_respawn_service(mock_request)


class TestGetProfessionService:
    """Tests for get_profession_service dependency function."""

    def test_get_profession_service_success(self, mock_request, mock_container):
        """Test get_profession_service creates service with persistence."""
        mock_persistence = MagicMock()
        mock_container.async_persistence = mock_persistence

        result = get_profession_service(mock_request)
        assert result is not None
        # ProfessionService is created with persistence
        assert hasattr(result, "_persistence") or hasattr(result, "persistence")


class TestGetPlayerCombatService:
    """Tests for get_player_combat_service dependency function."""

    def test_get_player_combat_service_success(self, mock_request, mock_container):
        """Test get_player_combat_service returns service when present."""
        mock_service = MagicMock()
        mock_container.player_combat_service = mock_service

        result = get_player_combat_service(mock_request)
        assert result == mock_service

    def test_get_player_combat_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_player_combat_service raises RuntimeError when service is None."""
        mock_container.player_combat_service = None

        with pytest.raises(RuntimeError, match="PlayerCombatService not initialized in container"):
            get_player_combat_service(mock_request)


class TestGetPlayerDeathService:
    """Tests for get_player_death_service dependency function."""

    def test_get_player_death_service_success(self, mock_request, mock_container):
        """Test get_player_death_service returns service when present."""
        mock_service = MagicMock()
        mock_container.player_death_service = mock_service

        result = get_player_death_service(mock_request)
        assert result == mock_service

    def test_get_player_death_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_player_death_service raises RuntimeError when service is None."""
        mock_container.player_death_service = None

        with pytest.raises(RuntimeError, match="PlayerDeathService not initialized in container"):
            get_player_death_service(mock_request)


class TestGetCombatService:
    """Tests for get_combat_service dependency function."""

    def test_get_combat_service_success(self, mock_request, mock_container):
        """Test get_combat_service returns service when present."""
        mock_service = MagicMock()
        mock_container.combat_service = mock_service

        result = get_combat_service(mock_request)
        assert result == mock_service

    def test_get_combat_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_combat_service raises RuntimeError when service is None."""
        mock_container.combat_service = None

        with pytest.raises(RuntimeError, match="CombatService not initialized in container"):
            get_combat_service(mock_request)


class TestGetMagicService:
    """Tests for get_magic_service dependency function."""

    def test_get_magic_service_success(self, mock_request, mock_container):
        """Test get_magic_service returns service when present."""
        mock_service = MagicMock()
        mock_container.magic_service = mock_service

        result = get_magic_service(mock_request)
        assert result == mock_service

    def test_get_magic_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_magic_service raises RuntimeError when service is None."""
        mock_container.magic_service = None

        with pytest.raises(RuntimeError, match="MagicService not initialized in container"):
            get_magic_service(mock_request)


class TestGetSpellRegistry:
    """Tests for get_spell_registry dependency function."""

    def test_get_spell_registry_success(self, mock_request, mock_container):
        """Test get_spell_registry returns service when present."""
        mock_service = MagicMock()
        mock_container.spell_registry = mock_service

        result = get_spell_registry(mock_request)
        assert result == mock_service

    def test_get_spell_registry_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_spell_registry raises RuntimeError when service is None."""
        mock_container.spell_registry = None

        with pytest.raises(RuntimeError, match="SpellRegistry not initialized in container"):
            get_spell_registry(mock_request)


class TestGetSpellTargetingService:
    """Tests for get_spell_targeting_service dependency function."""

    def test_get_spell_targeting_service_success(self, mock_request, mock_container):
        """Test get_spell_targeting_service returns service when present."""
        mock_service = MagicMock()
        mock_container.spell_targeting_service = mock_service

        result = get_spell_targeting_service(mock_request)
        assert result == mock_service

    def test_get_spell_targeting_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_spell_targeting_service raises RuntimeError when service is None."""
        mock_container.spell_targeting_service = None

        with pytest.raises(RuntimeError, match="SpellTargetingService not initialized in container"):
            get_spell_targeting_service(mock_request)


class TestGetSpellEffects:
    """Tests for get_spell_effects dependency function."""

    def test_get_spell_effects_success(self, mock_request, mock_container):
        """Test get_spell_effects returns service when present."""
        mock_service = MagicMock()
        mock_container.spell_effects = mock_service

        result = get_spell_effects(mock_request)
        assert result == mock_service

    def test_get_spell_effects_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_spell_effects raises RuntimeError when service is None."""
        mock_container.spell_effects = None

        with pytest.raises(RuntimeError, match="SpellEffects not initialized in container"):
            get_spell_effects(mock_request)


class TestGetSpellLearningService:
    """Tests for get_spell_learning_service dependency function."""

    def test_get_spell_learning_service_success(self, mock_request, mock_container):
        """Test get_spell_learning_service returns service when present."""
        mock_service = MagicMock()
        mock_container.spell_learning_service = mock_service

        result = get_spell_learning_service(mock_request)
        assert result == mock_service

    def test_get_spell_learning_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_spell_learning_service raises RuntimeError when service is None."""
        mock_container.spell_learning_service = None

        with pytest.raises(RuntimeError, match="SpellLearningService not initialized in container"):
            get_spell_learning_service(mock_request)


class TestGetMPRegenerationService:
    """Tests for get_mp_regeneration_service dependency function."""

    def test_get_mp_regeneration_service_success(self, mock_request, mock_container):
        """Test get_mp_regeneration_service returns service when present."""
        mock_service = MagicMock()
        mock_container.mp_regeneration_service = mock_service

        result = get_mp_regeneration_service(mock_request)
        assert result == mock_service

    def test_get_mp_regeneration_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_mp_regeneration_service raises RuntimeError when service is None."""
        mock_container.mp_regeneration_service = None

        with pytest.raises(RuntimeError, match="MPRegenerationService not initialized in container"):
            get_mp_regeneration_service(mock_request)


class TestGetNPCLifecycleManager:
    """Tests for get_npc_lifecycle_manager dependency function."""

    def test_get_npc_lifecycle_manager_success(self, mock_request, mock_container):
        """Test get_npc_lifecycle_manager returns service when present."""
        mock_service = MagicMock()
        mock_container.npc_lifecycle_manager = mock_service

        result = get_npc_lifecycle_manager(mock_request)
        assert result == mock_service

    def test_get_npc_lifecycle_manager_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_npc_lifecycle_manager raises RuntimeError when service is None."""
        mock_container.npc_lifecycle_manager = None

        with pytest.raises(RuntimeError, match="NPCLifecycleManager not initialized in container"):
            get_npc_lifecycle_manager(mock_request)


class TestGetNPCSpawningService:
    """Tests for get_npc_spawning_service dependency function."""

    def test_get_npc_spawning_service_success(self, mock_request, mock_container):
        """Test get_npc_spawning_service returns service when present."""
        mock_service = MagicMock()
        mock_container.npc_spawning_service = mock_service

        result = get_npc_spawning_service(mock_request)
        assert result == mock_service

    def test_get_npc_spawning_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_npc_spawning_service raises RuntimeError when service is None."""
        mock_container.npc_spawning_service = None

        with pytest.raises(RuntimeError, match="NPCSpawningService not initialized in container"):
            get_npc_spawning_service(mock_request)


class TestGetNPCPopulationController:
    """Tests for get_npc_population_controller dependency function."""

    def test_get_npc_population_controller_success(self, mock_request, mock_container):
        """Test get_npc_population_controller returns service when present."""
        mock_service = MagicMock()
        mock_container.npc_population_controller = mock_service

        result = get_npc_population_controller(mock_request)
        assert result == mock_service

    def test_get_npc_population_controller_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_npc_population_controller raises RuntimeError when service is None."""
        mock_container.npc_population_controller = None

        with pytest.raises(RuntimeError, match="NPCPopulationController not initialized in container"):
            get_npc_population_controller(mock_request)


class TestGetCatatoniaRegistry:
    """Tests for get_catatonia_registry dependency function."""

    def test_get_catatonia_registry_success(self, mock_request, mock_container):
        """Test get_catatonia_registry returns service when present."""
        mock_service = MagicMock()
        mock_container.catatonia_registry = mock_service

        result = get_catatonia_registry(mock_request)
        assert result == mock_service

    def test_get_catatonia_registry_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_catatonia_registry raises RuntimeError when service is None."""
        mock_container.catatonia_registry = None

        with pytest.raises(RuntimeError, match="CatatoniaRegistry not initialized in container"):
            get_catatonia_registry(mock_request)


class TestGetPassiveLucidityFluxService:
    """Tests for get_passive_lucidity_flux_service dependency function."""

    def test_get_passive_lucidity_flux_service_success(self, mock_request, mock_container):
        """Test get_passive_lucidity_flux_service returns service when present."""
        mock_service = MagicMock()
        mock_container.passive_lucidity_flux_service = mock_service

        result = get_passive_lucidity_flux_service(mock_request)
        assert result == mock_service

    def test_get_passive_lucidity_flux_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_passive_lucidity_flux_service raises RuntimeError when service is None."""
        mock_container.passive_lucidity_flux_service = None

        with pytest.raises(RuntimeError, match="PassiveLucidityFluxService not initialized in container"):
            get_passive_lucidity_flux_service(mock_request)


class TestGetMythosTimeConsumer:
    """Tests for get_mythos_time_consumer dependency function."""

    def test_get_mythos_time_consumer_success(self, mock_request, mock_container):
        """Test get_mythos_time_consumer returns service when present."""
        mock_service = MagicMock()
        mock_container.mythos_time_consumer = mock_service

        result = get_mythos_time_consumer(mock_request)
        assert result == mock_service

    def test_get_mythos_time_consumer_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_mythos_time_consumer raises RuntimeError when service is None."""
        mock_container.mythos_time_consumer = None

        with pytest.raises(RuntimeError, match="MythosTimeEventConsumer not initialized in container"):
            get_mythos_time_consumer(mock_request)


class TestGetChatService:
    """Tests for get_chat_service dependency function."""

    def test_get_chat_service_success(self, mock_request, mock_container):
        """Test get_chat_service returns service when present."""
        mock_service = MagicMock()
        mock_container.chat_service = mock_service

        result = get_chat_service(mock_request)
        assert result == mock_service

    def test_get_chat_service_none_raises_runtime_error(self, mock_request, mock_container):
        """Test get_chat_service raises RuntimeError when service is None."""
        mock_container.chat_service = None

        with pytest.raises(RuntimeError, match="ChatService not initialized in container"):
            get_chat_service(mock_request)


class TestGetNatsMessageHandler:
    """Tests for get_nats_message_handler dependency function."""

    def test_get_nats_message_handler_success(self, mock_request, mock_container):
        """Test get_nats_message_handler returns handler when present."""
        mock_handler = MagicMock()
        mock_container.nats_message_handler = mock_handler

        result = get_nats_message_handler(mock_request)
        assert result == mock_handler

    def test_get_nats_message_handler_none_returns_none(self, mock_request, mock_container):
        """Test get_nats_message_handler returns None when handler is None (NATS disabled)."""
        mock_container.nats_message_handler = None

        result = get_nats_message_handler(mock_request)
        assert result is None
