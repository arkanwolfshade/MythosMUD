# Player

> God node · 236 connections · `server/models/player.py`

**Community:** [combat models rationale](combat_models_rationale.md)

## Connections by Relation

### calls
- row_to_player() `EXTRACTED`
- .create_player_with_stats() `EXTRACTED`
- .create_player() `EXTRACTED`
- test_lucidity_adjustment_round_trip() `EXTRACTED`
- test_add_player_effect_generates_id() `EXTRACTED`
- quest_seed_data() `EXTRACTED`
- test_player_add_experience() `EXTRACTED`
- test_player_add_experience_zero() `EXTRACTED`
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

### contains
- player.py `EXTRACTED`

### imports
- async_persistence.py `EXTRACTED`
- __init__.py `EXTRACTED`
- game_tick_processing.py `EXTRACTED`
- user.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- lucidity_service.py `EXTRACTED`
- test_player_death_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- test_player_model.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_player_repository.py `EXTRACTED`
- websocket_helpers.py `EXTRACTED`
- test_inventory_equip_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- test_async_persistence_delegates.py `EXTRACTED`
- lucidity.py `EXTRACTED`

### indirect_call
- _sample_work() `INFERRED`
- .respawn_player() `INFERRED`
- .handle_player_death() `INFERRED`
- .respawn_player_from_delirium() `INFERRED`
- .respawn_player_from_sanitarium() `INFERRED`
- ._calculate_max_lcd() `INFERRED`
- .respawn_player_from_delirium_by_user_id() `INFERRED`
- .process_mortally_wounded_tick() `INFERRED`
- .get_respawn_room() `INFERRED`
- .move_player_to_limbo() `INFERRED`
- .respawn_player_by_user_id() `INFERRED`
- ._load_players() `INFERRED`
- .get_dead_players() `INFERRED`
- test_put_run_validated_container_error() `INFERRED`
- test_put_run_validated_success() `INFERRED`
- .get_mortally_wounded_players() `INFERRED`
- test_get_from_container_path_item_not_in_container() `INFERRED`
- test_get_from_container_path_missing_container() `INFERRED`
- test_equip_success_payload() `INFERRED`
- test_handle_put_command_success() `INFERRED`

### inherits
- Base `EXTRACTED`

### method
- .get_stats() `EXTRACTED`
- .set_stats() `EXTRACTED`
- .apply_dp_change() `EXTRACTED`
- .apply_dp_decay() `EXTRACTED`
- .get_equipped_items() `EXTRACTED`
- .restore_to_full_health() `EXTRACTED`
- .get_combat_stats() `EXTRACTED`
- .get_health_percentage() `EXTRACTED`
- .get_health_state() `EXTRACTED`
- .is_alive() `EXTRACTED`
- .is_dead() `EXTRACTED`
- .is_mortally_wounded() `EXTRACTED`
- .set_equipped_items() `EXTRACTED`
- .set_inventory() `EXTRACTED`
- .add_experience() `EXTRACTED`
- .get_inventory() `EXTRACTED`
- .get_status_effects() `EXTRACTED`
- .__init__() `EXTRACTED`
- .is_admin_user() `EXTRACTED`
- .__repr__() `EXTRACTED`

### rationale_for
- Player model for game data.      Stores all game-specific data for a user includ `EXTRACTED`

### references
- _convert_legacy_stats_string() `EXTRACTED`

### uses
- [User](User.md) `INFERRED`
- PlayerLucidity `INFERRED`
- Base `INFERRED`
- SpellTargetingService `INFERRED`
- HealthRepository `INFERRED`
- PlayerRepository `INFERRED`
- ExperienceRepository `INFERRED`
- PlayerDeathService `INFERRED`
- LucidityExposureState `INFERRED`
- LucidityCooldown `INFERRED`
- PlayerRepositoryProtocol `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- PlayerSpell `INFERRED`
- PositionState `INFERRED`
- PlayerEffect `INFERRED`
- PlayerSkill `INFERRED`
- PlayerSavePreparer `INFERRED`
- RoomRepositoryProtocol `INFERRED`
- LucidityActionCode `INFERRED`
- InventoryPayload `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*