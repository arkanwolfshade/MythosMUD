# Player

> God node · 200 connections · `server/models/player.py`

**Community:** [Player Creation Service](Player_Creation_Service.md)

## Connections by Relation

### calls
- row_to_player() `EXTRACTED`
- .create_player_with_stats() `EXTRACTED`
- .create_player() `EXTRACTED`
- test_lucidity_adjustment_round_trip() `EXTRACTED`
- test_add_player_effect_generates_id() `EXTRACTED`
- quest_seed_data() `EXTRACTED`
- test_get_player_combat_data_uses_get_combat_stats() `EXTRACTED`
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

### contains
- player.py `EXTRACTED`

### imports
- game_tick_processing.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- [__init__.py](__init__.py.md) `EXTRACTED`
- user.py `EXTRACTED`
- test_player_death_service.py `EXTRACTED`
- lucidity_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- test_player_model.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_player_repository.py `EXTRACTED`
- websocket_helpers.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- test_async_persistence_delegates.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- lucidity.py `EXTRACTED`

### indirect_call
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
- .get_mortally_wounded_players() `INFERRED`
- test_apply_corruption_delegates() `INFERRED`
- test_apply_fear_delegates() `INFERRED`
- test_apply_lucidity_loss_delegates() `INFERRED`
- test_async_damage_player_delegates() `INFERRED`
- test_async_heal_player_delegates() `INFERRED`
- test_damage_player_delegates() `INFERRED`
- test_get_player_by_user_id_delegates() `INFERRED`

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
- PlayerRepository `INFERRED`
- PlayerDeathService `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- LucidityExposureState `INFERRED`
- PlayerSpell `INFERRED`
- LucidityCooldown `INFERRED`
- PlayerRepositoryProtocol `INFERRED`
- PositionState `INFERRED`
- HealthRepository `INFERRED`
- PlayerEffect `INFERRED`
- PlayerSkill `INFERRED`
- ExperienceRepository `INFERRED`
- PlayerSavePreparer `INFERRED`
- RoomRepositoryProtocol `INFERRED`
- LucidityActionCode `INFERRED`
- InventoryPayload `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*