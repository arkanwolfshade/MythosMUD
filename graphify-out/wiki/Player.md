# Player

> God node · 275 connections · `server/models/player.py`

**Community:** [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md)

## Connections by Relation

### calls
- row_to_player() `EXTRACTED`
- _exit_hook_setup() `EXTRACTED`
- _create_player() `EXTRACTED`
- quest_seed_data() `EXTRACTED`
- _create_player() `EXTRACTED`
- test_respawn_room_reward_moves_the_players_respawn() `EXTRACTED`
- test_respawn_room_reward_without_room_id_changes_nothing() `EXTRACTED`
- test_player_apply_dp_change_became_dead() `EXTRACTED`
- test_player_apply_dp_change_became_mortally_wounded() `EXTRACTED`
- test_player_apply_dp_change_updates_dp() `EXTRACTED`
- test_player_apply_dp_decay_caps_at_negative_10() `EXTRACTED`
- test_player_apply_dp_decay_changes_posture_when_crossing_zero() `EXTRACTED`
- test_player_apply_dp_decay_reduces_dp() `EXTRACTED`
- test_player_creation() `EXTRACTED`
- test_player_defaults() `EXTRACTED`
- test_player_get_combat_stats() `EXTRACTED`
- test_player_get_combat_stats_defaults() `EXTRACTED`
- test_player_get_equipped_items() `EXTRACTED`
- test_player_get_equipped_items_empty() `EXTRACTED`
- test_player_get_health_percentage() `EXTRACTED`

### contains
- models/player.py `EXTRACTED`

### imports
- server/models/__init__.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- models/user.py `EXTRACTED`
- test_wearable_container_service.py `EXTRACTED`
- test_movement_service.py `EXTRACTED`
- test_player_presence_tracker.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- look_command.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- player_presence_tracker.py `EXTRACTED`
- test_player_death_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- lucidity_service.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- test_quest_service.py `EXTRACTED`
- test_player_repository.py `EXTRACTED`
- test_player_disconnect_handlers.py `EXTRACTED`
- test_player_service_mutations.py `EXTRACTED`
- test_player_model.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`

### inherits
- Base `EXTRACTED`

### method
- .get_stats() `EXTRACTED`
- .set_stats() `EXTRACTED`
- .apply_dp_decay() `EXTRACTED`
- .restore_to_full_health() `EXTRACTED`
- .apply_dp_change() `EXTRACTED`
- .is_alive() `EXTRACTED`
- .is_mortally_wounded() `EXTRACTED`
- .is_dead() `EXTRACTED`
- .get_health_state() `EXTRACTED`
- .get_combat_stats() `EXTRACTED`
- .get_health_percentage() `EXTRACTED`
- .set_inventory() `EXTRACTED`
- .set_equipped_items() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__repr__() `EXTRACTED`
- .get_inventory() `EXTRACTED`
- .get_status_effects() `EXTRACTED`
- .set_status_effects() `EXTRACTED`
- .get_equipped_items() `EXTRACTED`
- .is_admin_user() `EXTRACTED`

### rationale_for
- Player model for game data. Stores all game-specific data for a user including… `EXTRACTED`

### references
- _convert_legacy_stats_string() `EXTRACTED`

### uses
- PlayerRepository `INFERRED`
- PlayerLucidity `INFERRED`
- HealthRepository `INFERRED`
- _assist() `INFERRED`
- _protect() `INFERRED`
- SpellTargetingService `INFERRED`
- PlayerRepositoryProtocol `INFERRED`
- PlayerDeathService `INFERRED`
- LucidityExposureState `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- LucidityCooldown `INFERRED`
- _bank_world() `INFERRED`
- PlayerSavePreparer `INFERRED`
- _sample_work() `INFERRED`
- CorruptionCooldown `INFERRED`
- validate_and_fix_player_room() `INFERRED`
- test_lucidity_adjustment_round_trip() `INFERRED`
- load_assister() `INFERRED`
- should_skip_room_validation() `INFERRED`
- _RespawnPersistence `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*