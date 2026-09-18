# Player

> God node · 286 connections · `server/models/player.py`

**Community:** [Player Creation Service](Player_Creation_Service.md)

## Connections by Relation

### calls
- row_to_player() `EXTRACTED`
- .create_player_with_stats() `EXTRACTED`
- .create_player() `EXTRACTED`
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
- test_player_get_health_percentage() `EXTRACTED`
- test_player_get_health_percentage_full() `EXTRACTED`

### contains
- models/player.py `EXTRACTED`

### imports
- async_persistence.py `EXTRACTED`
- models/user.py `EXTRACTED`
- look_command.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- real_time.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- test_player_death_service.py `EXTRACTED`
- test_player_model.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- test_player_repository.py `EXTRACTED`
- test_websocket_initial_state.py `EXTRACTED`
- server/models/__init__.py `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- websocket_helpers.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_inventory_equip_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- logout_commands.py `EXTRACTED`
- disconnect_grace_period.py `EXTRACTED`

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
- .add_experience() `EXTRACTED`

### rationale_for
- Player model for game data. Stores all game-specific data for a user including… `EXTRACTED`

### references
- track_player_connected_impl() `EXTRACTED`
- _process_single_effect() `EXTRACTED`
- .send_initial_game_state() `EXTRACTED`
- _process_mortally_wounded_player() `EXTRACTED`
- _process_damage_over_time_effect() `EXTRACTED`
- ._validate_and_fix_player_room_with_persistence() `EXTRACTED`
- ._resolve_context_async() `EXTRACTED`
- ._resolve_player_and_context() `EXTRACTED`
- _process_heal_over_time_effect() `EXTRACTED`
- .get_player() `EXTRACTED`
- _validate_and_get_player() `EXTRACTED`
- _process_all_status_effects() `EXTRACTED`
- _update_player_status_effects() `EXTRACTED`
- _warm_corruption_tier_cache() `EXTRACTED`
- ._resolve_context() `EXTRACTED`
- ._filter_active_players() `EXTRACTED`
- ._evaluate_players_tick() `EXTRACTED`
- _handle_player_death_threshold() `EXTRACTED`
- ._get_player_data_for_client() `EXTRACTED`
- .get_player_by_id() `EXTRACTED`

### uses
- PlayerLucidity `INFERRED`
- HealthRepository `INFERRED`
- PlayerRepository `INFERRED`
- SpellTargetingService `INFERRED`
- ExperienceRepository `INFERRED`
- PlayerRepositoryProtocol `INFERRED`
- PlayerDeathService `INFERRED`
- LucidityExposureState `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- LucidityCooldown `INFERRED`
- PlayerSavePreparer `INFERRED`
- _sample_work() `INFERRED`
- CorruptionCooldown `INFERRED`
- validate_and_fix_player_room() `INFERRED`
- should_skip_room_validation() `INFERRED`
- test_lucidity_adjustment_round_trip() `INFERRED`
- CorruptionAdjustmentLog `INFERRED`
- validate_and_fix_player_room_with_persistence() `INFERRED`
- test_add_player_effect_generates_id() `INFERRED`
- test_put_run_validated_container_error() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*