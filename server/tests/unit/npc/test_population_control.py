"""
Unit tests for NPC population control.

Tests the NPCPopulationController class.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerLeftRoom
from server.models.npc import NPCDefinition, NPCSpawnRule
from server.npc.population_control import NPCPopulationController
from server.npc.population_stats import PopulationStats
from server.npc.zone_configuration import ZoneConfiguration


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    return MagicMock(spec=EventBus)


@pytest.fixture
def mock_async_persistence():
    """Create a mock async persistence."""
    return MagicMock()


@pytest.fixture
def mock_lifecycle_manager():
    """Create a mock lifecycle manager."""
    manager = MagicMock()
    manager.active_npcs = {}
    return manager


@pytest.fixture
def population_controller(mock_event_bus, mock_async_persistence, mock_lifecycle_manager):
    """Create an NPCPopulationController instance."""
    with patch("server.npc.population_control.load_zone_configurations", return_value={}):
        controller = NPCPopulationController(
            event_bus=mock_event_bus,
            async_persistence=mock_async_persistence,
            lifecycle_manager=mock_lifecycle_manager,
        )
        return controller


def test_population_controller_init(mock_event_bus, mock_async_persistence, mock_lifecycle_manager):
    """Test NPCPopulationController initialization."""
    with patch("server.npc.population_control.load_zone_configurations", return_value={}):
        controller = NPCPopulationController(
            event_bus=mock_event_bus,
            async_persistence=mock_async_persistence,
            lifecycle_manager=mock_lifecycle_manager,
        )
        assert controller.event_bus == mock_event_bus
        assert controller.async_persistence == mock_async_persistence
        assert controller.lifecycle_manager == mock_lifecycle_manager
        assert controller.population_stats == {}
        assert controller.zone_configurations == {}
        assert controller.npc_definitions == {}
        assert controller.spawn_rules == {}
        assert "time_of_day" in controller.current_game_state


def test_population_controller_init_requires_async_persistence(mock_event_bus):
    """Test NPCPopulationController raises error when async_persistence is None."""
    with patch("server.npc.population_control.load_zone_configurations", return_value={}):
        with pytest.raises(ValueError, match="async_persistence is required"):
            NPCPopulationController(event_bus=mock_event_bus, async_persistence=None)


def test_load_npc_definitions(population_controller):
    """Test load_npc_definitions() loads definitions."""
    definition1 = MagicMock(spec=NPCDefinition)
    definition1.id = 1
    definition2 = MagicMock(spec=NPCDefinition)
    definition2.id = 2
    population_controller.load_npc_definitions([definition1, definition2])
    assert len(population_controller.npc_definitions) == 2
    assert population_controller.npc_definitions[1] == definition1
    assert population_controller.npc_definitions[2] == definition2


def test_load_npc_definitions_overwrites(population_controller):
    """Test load_npc_definitions() overwrites existing definitions."""
    definition1 = MagicMock(spec=NPCDefinition)
    definition1.id = 1
    population_controller.load_npc_definitions([definition1])
    definition1_updated = MagicMock(spec=NPCDefinition)
    definition1_updated.id = 1
    population_controller.load_npc_definitions([definition1_updated])
    assert population_controller.npc_definitions[1] == definition1_updated


def test_load_spawn_rules(population_controller):
    """Test load_spawn_rules() loads rules."""
    rule1 = MagicMock(spec=NPCSpawnRule)
    rule1.npc_definition_id = 1
    rule2 = MagicMock(spec=NPCSpawnRule)
    rule2.npc_definition_id = 1
    rule3 = MagicMock(spec=NPCSpawnRule)
    rule3.npc_definition_id = 2
    population_controller.load_spawn_rules([rule1, rule2, rule3])
    assert len(population_controller.spawn_rules) == 2
    assert len(population_controller.spawn_rules[1]) == 2
    assert len(population_controller.spawn_rules[2]) == 1


def test_load_spawn_rules_empty(population_controller):
    """Test load_spawn_rules() handles empty list."""
    population_controller.load_spawn_rules([])
    assert population_controller.spawn_rules == {}


def test_update_game_state(population_controller):
    """Test update_game_state() updates game state."""
    initial_state = population_controller.current_game_state.copy()
    population_controller.update_game_state({"time_of_day": "night", "weather": "storm"})
    assert population_controller.current_game_state["time_of_day"] == "night"
    assert population_controller.current_game_state["weather"] == "storm"
    # Other values should remain
    assert population_controller.current_game_state["player_count"] == initial_state["player_count"]


def test_update_game_state_partial(population_controller):
    """Test update_game_state() updates only provided values."""
    initial_player_count = population_controller.current_game_state["player_count"]
    population_controller.update_game_state({"time_of_day": "dusk"})
    assert population_controller.current_game_state["time_of_day"] == "dusk"
    assert population_controller.current_game_state["player_count"] == initial_player_count


def test_get_zone_configuration_exact_match(population_controller):
    """Test get_zone_configuration() returns exact match."""
    config = ZoneConfiguration({})
    population_controller.zone_configurations["arkhamcity/downtown"] = config
    result = population_controller.get_zone_configuration("arkhamcity/downtown")
    assert result == config


def test_get_zone_configuration_zone_fallback(population_controller):
    """Test get_zone_configuration() falls back to zone-level config."""
    config = ZoneConfiguration({})
    population_controller.zone_configurations["arkhamcity"] = config
    result = population_controller.get_zone_configuration("arkhamcity/downtown")
    assert result == config


def test_get_zone_configuration_not_found(population_controller):
    """Test get_zone_configuration() returns None when not found."""
    result = population_controller.get_zone_configuration("unknown/zone")
    assert result is None


def test_get_zone_configuration_no_slash(population_controller):
    """Test get_zone_configuration() handles zone key without slash."""
    config = ZoneConfiguration({})
    population_controller.zone_configurations["arkhamcity"] = config
    result = population_controller.get_zone_configuration("arkhamcity")
    assert result == config


def test_get_population_stats_existing(population_controller):
    """Test get_population_stats() returns existing stats."""
    stats = PopulationStats("arkhamcity", "downtown")
    population_controller.population_stats["arkhamcity/downtown"] = stats
    result = population_controller.get_population_stats("arkhamcity/downtown")
    assert result == stats


def test_get_population_stats_not_found(population_controller):
    """Test get_population_stats() returns None when not found."""
    result = population_controller.get_population_stats("unknown/zone")
    assert result is None


def test_get_zone_key_from_room_id(population_controller):
    """Test _get_zone_key_from_room_id() extracts zone key."""
    result = population_controller._get_zone_key_from_room_id("earth_arkhamcity_downtown_001")
    assert result == "arkhamcity/downtown"


def test_clear_population_stats(population_controller):
    """Test clear_population_stats() clears all stats."""
    stats1 = PopulationStats("arkhamcity", "downtown")
    stats2 = PopulationStats("innsmouth", "waterfront")
    population_controller.population_stats["arkhamcity/downtown"] = stats1
    population_controller.population_stats["innsmouth/waterfront"] = stats2
    population_controller.clear_population_stats()
    assert population_controller.population_stats == {}


def test_get_zone_population_summary_empty(population_controller):
    """Test get_zone_population_summary() returns empty summary."""
    summary = population_controller.get_zone_population_summary()
    assert summary["total_zones"] == 0
    assert summary["zones"] == {}
    assert summary["total_active_npcs"] == 0


def test_get_zone_population_summary_with_stats(population_controller):
    """Test get_zone_population_summary() includes zone stats."""
    stats = PopulationStats("arkhamcity", "downtown")
    stats.add_npc("aggressive_mob", "room-123", True, npc_definition_id=1)
    population_controller.population_stats["arkhamcity/downtown"] = stats
    summary = population_controller.get_zone_population_summary()
    assert summary["total_zones"] == 1
    assert "arkhamcity/downtown" in summary["zones"]
    assert summary["zones"]["arkhamcity/downtown"]["zone_id"] == "arkhamcity"


def test_handle_player_entered_room(population_controller):
    """Test _handle_player_entered_room() processes event."""
    event = PlayerEnteredRoom(player_id="player-123", room_id="room-456")
    with patch.object(population_controller, "_update_player_count") as mock_update:
        with patch.object(population_controller, "_check_spawn_requirements_for_room") as mock_check:
            population_controller._handle_player_entered_room(event)
            mock_update.assert_called_once()
            mock_check.assert_called_once_with("room-456")


def test_handle_player_left_room(population_controller):
    """Test _handle_player_left_room() processes event."""
    event = PlayerLeftRoom(player_id="player-123", room_id="room-456")
    with patch.object(population_controller, "_update_player_count") as mock_update:
        population_controller._handle_player_left_room(event)
        mock_update.assert_called_once()


def test_handle_npc_entered_room(population_controller):
    """Test _handle_npc_entered_room() processes event."""
    event = NPCEnteredRoom(npc_id="npc-123", room_id="room-456")
    # Should not raise
    population_controller._handle_npc_entered_room(event)


def test_handle_npc_left_room(population_controller):
    """Test _handle_npc_left_room() processes event."""
    event = NPCLeftRoom(npc_id="npc-123", room_id="room-456")
    # Should not raise
    population_controller._handle_npc_left_room(event)


def test_get_active_npcs_from_lifecycle_manager(population_controller, mock_lifecycle_manager):
    """Test _get_active_npcs_from_lifecycle_manager() returns active NPCs."""
    mock_npc = MagicMock()
    mock_lifecycle_manager.active_npcs = {"npc-123": mock_npc}
    result = population_controller._get_active_npcs_from_lifecycle_manager()
    assert result == {"npc-123": mock_npc}


def test_get_active_npcs_from_lifecycle_manager_empty(population_controller, mock_lifecycle_manager):
    """Test _get_active_npcs_from_lifecycle_manager() returns empty dict when no NPCs."""
    mock_lifecycle_manager.active_npcs = {}
    result = population_controller._get_active_npcs_from_lifecycle_manager()
    assert result == {}


def test_get_active_npcs_from_lifecycle_manager_no_manager(population_controller):
    """Test _get_active_npcs_from_lifecycle_manager() returns empty dict when no manager."""
    population_controller.lifecycle_manager = None
    result = population_controller._get_active_npcs_from_lifecycle_manager()
    assert result == {}


def test_subscribe_to_events(population_controller, mock_event_bus):
    """Test _subscribe_to_events() subscribes to all events."""
    # Re-subscribe to verify calls
    population_controller._subscribe_to_events()
    # Should subscribe to 4 event types
    assert mock_event_bus.subscribe.call_count >= 4


def test_update_player_count(population_controller):
    """Test _update_player_count() updates player count."""
    population_controller._update_player_count()
    # Should update to placeholder value
    assert population_controller.current_game_state["player_count"] == 1


def test_cleanup_inactive_npcs_empty(population_controller, mock_lifecycle_manager):
    """Test cleanup_inactive_npcs() returns 0 when no NPCs."""
    mock_lifecycle_manager.active_npcs = {}
    result = population_controller.cleanup_inactive_npcs()
    assert result == 0


def test_cleanup_inactive_npcs_removes_old_npcs(population_controller, mock_lifecycle_manager):
    """Test cleanup_inactive_npcs() removes old NPCs."""
    import time

    old_npc = MagicMock()
    old_npc.spawned_at = time.time() - 7200  # 2 hours ago
    old_npc.is_required = False
    new_npc = MagicMock()
    new_npc.spawned_at = time.time() - 300  # 5 minutes ago
    new_npc.is_required = False
    mock_lifecycle_manager.active_npcs = {"old-npc": old_npc, "new-npc": new_npc}
    with patch.object(population_controller, "despawn_npc", return_value=True) as mock_despawn:
        result = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)
        assert result == 1
        mock_despawn.assert_called_once_with("old-npc")


def test_cleanup_inactive_npcs_keeps_required(population_controller, mock_lifecycle_manager):
    """Test cleanup_inactive_npcs() keeps required NPCs."""
    import time

    old_required_npc = MagicMock()
    old_required_npc.spawned_at = time.time() - 7200  # 2 hours ago
    old_required_npc.is_required = True
    mock_lifecycle_manager.active_npcs = {"required-npc": old_required_npc}
    with patch.object(population_controller, "despawn_npc", return_value=True) as mock_despawn:
        result = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)
        assert result == 0
        mock_despawn.assert_not_called()


def test_cleanup_inactive_npcs_no_spawned_at(population_controller, mock_lifecycle_manager):
    """Test cleanup_inactive_npcs() skips NPCs without spawned_at."""
    npc = MagicMock()
    # No spawned_at attribute
    del npc.spawned_at
    mock_lifecycle_manager.active_npcs = {"npc-123": npc}
    with patch.object(population_controller, "despawn_npc", return_value=True) as mock_despawn:
        result = population_controller.cleanup_inactive_npcs()
        assert result == 0
        mock_despawn.assert_not_called()


def test_cleanup_inactive_npcs_invalid_spawned_at(population_controller, mock_lifecycle_manager):
    """Test cleanup_inactive_npcs() skips NPCs with invalid spawned_at."""
    npc = MagicMock()
    npc.spawned_at = "not-a-number"
    mock_lifecycle_manager.active_npcs = {"npc-123": npc}
    with patch.object(population_controller, "despawn_npc", return_value=True) as mock_despawn:
        result = population_controller.cleanup_inactive_npcs()
        assert result == 0
        mock_despawn.assert_not_called()


def test_cleanup_inactive_npcs_multiple_removals(population_controller, mock_lifecycle_manager):
    """Test cleanup_inactive_npcs() removes multiple old NPCs."""
    import time

    old_npc1 = MagicMock()
    old_npc1.spawned_at = time.time() - 7200
    old_npc1.is_required = False
    old_npc2 = MagicMock()
    old_npc2.spawned_at = time.time() - 8000
    old_npc2.is_required = False
    new_npc = MagicMock()
    new_npc.spawned_at = time.time() - 300
    new_npc.is_required = False
    mock_lifecycle_manager.active_npcs = {"old-npc1": old_npc1, "old-npc2": old_npc2, "new-npc": new_npc}
    with patch.object(population_controller, "despawn_npc", return_value=True) as mock_despawn:
        result = population_controller.cleanup_inactive_npcs(max_age_seconds=3600)
        assert result == 2
        assert mock_despawn.call_count == 2


def test_should_spawn_npc(population_controller):
    """Test _should_spawn_npc() delegates to should_spawn_npc function."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    zone_config = ZoneConfiguration({})
    room_id = "earth_arkhamcity_downtown_001"
    stats = PopulationStats("arkhamcity", "downtown")
    population_controller.population_stats["arkhamcity/downtown"] = stats
    with patch("server.npc.population_control.should_spawn_npc", return_value=True) as mock_should_spawn:
        result = population_controller._should_spawn_npc(definition, zone_config, room_id)
        assert result is True
        mock_should_spawn.assert_called_once()


def test_spawn_npc_no_lifecycle_manager(population_controller):
    """Test _spawn_npc() returns None when no lifecycle manager."""
    population_controller.lifecycle_manager = None
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.npc_type = "aggressive_mob"
    definition.is_required = MagicMock(return_value=False)
    result = population_controller._spawn_npc(definition, "room-123")
    assert result is None


def test_spawn_npc_success(population_controller, mock_lifecycle_manager):
    """Test _spawn_npc() successfully spawns NPC."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.npc_type = "aggressive_mob"
    definition.name = "Test NPC"
    definition.is_required = MagicMock(return_value=False)
    mock_lifecycle_manager.spawn_npc = MagicMock(return_value="npc-123")
    result = population_controller._spawn_npc(definition, "earth_arkhamcity_downtown_001")
    assert result == "npc-123"
    # Should update population stats
    assert "arkhamcity/downtown" in population_controller.population_stats


def test_spawn_npc_spawn_fails(population_controller, mock_lifecycle_manager):
    """Test _spawn_npc() returns None when spawn fails."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.npc_type = "aggressive_mob"
    definition.name = "Test NPC"
    definition.is_required = MagicMock(return_value=False)
    mock_lifecycle_manager.spawn_npc = MagicMock(return_value=None)
    result = population_controller._spawn_npc(definition, "earth_arkhamcity_downtown_001")
    assert result is None


def test_spawn_npc_handles_exception(population_controller, mock_lifecycle_manager):
    """Test _spawn_npc() handles exceptions."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.npc_type = "aggressive_mob"
    definition.name = "Test NPC"
    definition.is_required = MagicMock(return_value=False)
    mock_lifecycle_manager.spawn_npc = MagicMock(side_effect=ValueError("Spawn error"))
    result = population_controller._spawn_npc(definition, "earth_arkhamcity_downtown_001")
    assert result is None


def test_spawn_npc_public_api(population_controller, mock_lifecycle_manager):
    """Test spawn_npc() public API delegates to _spawn_npc."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.npc_type = "aggressive_mob"
    definition.name = "Test NPC"
    definition.is_required = MagicMock(return_value=False)
    with patch.object(population_controller, "_spawn_npc", return_value="npc-123") as mock_spawn:
        result = population_controller.spawn_npc(definition, "room-123")
        assert result == "npc-123"
        mock_spawn.assert_called_once_with(definition, "room-123")


def test_despawn_npc_success(population_controller, mock_lifecycle_manager):
    """Test despawn_npc() successfully despawns NPC."""
    npc = MagicMock()
    npc.npc_type = "aggressive_mob"
    npc.current_room = "room-123"
    npc.is_required = False
    npc.name = "Test NPC"
    mock_lifecycle_manager.active_npcs = {"npc-123": npc}
    # Create population stats for the zone
    stats = PopulationStats("arkhamcity", "downtown")
    stats.add_npc("aggressive_mob", "room-123", False, npc_definition_id=1)
    population_controller.population_stats["arkhamcity/downtown"] = stats
    with patch("server.npc.population_control.extract_definition_id_from_npc", return_value=1):
        with patch("server.npc.population_control.extract_npc_metadata", return_value=("aggressive_mob", False)):
            with patch(
                "server.npc.population_control.extract_room_id_from_npc", return_value="earth_arkhamcity_downtown_001"
            ):
                result = population_controller.despawn_npc("npc-123")
                assert result is True
                # Should update population stats
                assert stats.total_npcs == 0


def test_despawn_npc_not_found(population_controller, mock_lifecycle_manager):
    """Test despawn_npc() returns False when NPC not found."""
    mock_lifecycle_manager.active_npcs = {}
    result = population_controller.despawn_npc("npc-123")
    assert result is False


def test_despawn_npc_no_lifecycle_manager(population_controller):
    """Test despawn_npc() returns False when no lifecycle manager."""
    population_controller.lifecycle_manager = None
    result = population_controller.despawn_npc("npc-123")
    assert result is False


def test_check_spawn_requirements_for_room_no_config(population_controller):
    """Test _check_spawn_requirements_for_room() handles missing zone config."""
    population_controller.zone_configurations = {}
    # Should not raise
    population_controller._check_spawn_requirements_for_room("room-123")


def test_check_spawn_requirements_for_room_with_definitions(population_controller):
    """Test _check_spawn_requirements_for_room() checks NPC definitions."""
    zone_config = ZoneConfiguration({})
    population_controller.zone_configurations["arkhamcity/downtown"] = zone_config
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.name = "Test NPC"
    definition.sub_zone_id = "downtown"
    population_controller.npc_definitions = {1: definition}
    with patch.object(population_controller, "_should_spawn_npc", return_value=True) as mock_should:
        with patch.object(population_controller, "_spawn_npc", return_value="npc-123") as mock_spawn:
            population_controller._check_spawn_requirements_for_room("earth_arkhamcity_downtown_001")
            # Should check spawn conditions
            mock_should.assert_called()
            # Should spawn if conditions met
            mock_spawn.assert_called()
