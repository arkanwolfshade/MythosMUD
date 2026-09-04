"""
Unit-tier fixtures with strict mocking and in-memory fakes.
"""

from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

# Import strict_mocker from mock_helpers for compatibility
from .mock_helpers import strict_mocker


@pytest.fixture
def dummy_request() -> SimpleNamespace:
    """Provide a minimal request object for testing with container support."""
    from server.container import ApplicationContainer

    # Create a mock container
    container = MagicMock(spec=ApplicationContainer)
    container.persistence = MagicMock()
    container.async_persistence = MagicMock()
    container.event_bus = MagicMock()
    container.player_service = MagicMock()
    container.room_service = MagicMock()
    container.connection_manager = MagicMock()
    container.catatonia_registry = MagicMock()
    # Add new services
    container.player_combat_service = MagicMock()
    container.player_death_service = MagicMock()
    container.player_respawn_service = MagicMock()
    container.combat_service = MagicMock()
    container.passive_lucidity_flux_service = MagicMock()
    container.magic_service = MagicMock()
    container.spell_registry = MagicMock()
    container.spell_targeting_service = MagicMock()
    container.spell_effects = MagicMock()
    container.spell_learning_service = MagicMock()
    container.mp_regeneration_service = MagicMock()
    container.npc_lifecycle_manager = MagicMock()
    container.npc_spawning_service = MagicMock()
    container.npc_population_controller = MagicMock()
    container.chat_service = MagicMock()
    container.mythos_time_consumer = MagicMock()

    # Create app.state with container (preferred) and backward compatibility
    state = SimpleNamespace(
        container=container,
        # Backward compatibility: also set direct references
        persistence=container.async_persistence,
        event_bus=container.event_bus,
        player_service=container.player_service,
        room_service=container.room_service,
        connection_manager=container.connection_manager,
        catatonia_registry=container.catatonia_registry,
        player_combat_service=container.player_combat_service,
        player_death_service=container.player_death_service,
        player_respawn_service=container.player_respawn_service,
        combat_service=container.combat_service,
        passive_lucidity_flux_service=container.passive_lucidity_flux_service,
        magic_service=container.magic_service,
        spell_registry=container.spell_registry,
        spell_targeting_service=container.spell_targeting_service,
        spell_effects=container.spell_effects,
        spell_learning_service=container.spell_learning_service,
        mp_regeneration_service=container.mp_regeneration_service,
        npc_lifecycle_manager=container.npc_lifecycle_manager,
        npc_spawning_service=container.npc_spawning_service,
        npc_population_controller=container.npc_population_controller,
        chat_service=container.chat_service,
        mythos_time_consumer=container.mythos_time_consumer,
    )
    app = SimpleNamespace(state=state)
    return SimpleNamespace(app=app)


@pytest.fixture
def test_container() -> MagicMock:
    """
    Provide a mock ApplicationContainer for testing.

    This fixture creates a properly configured mock container with all services.
    Tests should use this instead of manually creating app.state mocks.
    """
    from server.container import ApplicationContainer

    container = MagicMock(spec=ApplicationContainer)
    # Set up all service mocks
    container.persistence = MagicMock()
    container.async_persistence = MagicMock()
    container.event_bus = MagicMock()
    container.player_service = MagicMock()
    container.room_service = MagicMock()
    container.connection_manager = MagicMock()
    container.catatonia_registry = MagicMock()
    container.player_combat_service = MagicMock()
    container.player_death_service = MagicMock()
    container.player_respawn_service = MagicMock()
    container.combat_service = MagicMock()
    container.passive_lucidity_flux_service = MagicMock()
    container.magic_service = MagicMock()
    container.spell_registry = MagicMock()
    container.spell_targeting_service = MagicMock()
    container.spell_effects = MagicMock()
    container.spell_learning_service = MagicMock()
    container.mp_regeneration_service = MagicMock()
    container.npc_lifecycle_manager = MagicMock()
    container.npc_spawning_service = MagicMock()
    container.npc_population_controller = MagicMock()
    container.chat_service = MagicMock()
    container.mythos_time_consumer = MagicMock()
    container.server_shutdown_pending = False
    container.shutdown_data = None
    container.tick_task = None

    return container


@pytest.fixture
def fakerandom() -> Any:
    """Provide deterministic random seed for unit tests."""
    import random

    random.seed(42)
    yield
    random.seed()
