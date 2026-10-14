# Player

> God node · 281 connections · `server/models/player.py`

**Community:** [Player](Player.md)

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
- async_persistence.py `EXTRACTED`
- server/models/__init__.py `EXTRACTED`
- models/user.py `EXTRACTED`
- [test_wearable_container_service.py](test_wearable_container_service.py.md) `EXTRACTED`
- [test_movement_service.py](test_movement_service.py.md) `EXTRACTED`
- [test_player_respawn_service.py](test_player_respawn_service.py.md) `EXTRACTED`
- [player_presence_tracker.py](player_presence_tracker.py.md) `EXTRACTED`
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) `EXTRACTED`
- [look_command.py](look_command.py.md) `EXTRACTED`
- [websocket_initial_state.py](websocket_initial_state.py.md) `EXTRACTED`
- [test_player_death_service.py](test_player_death_service.py.md) `EXTRACTED`
- lucidity_service.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) `EXTRACTED`
- [real_time.py](real_time.py.md) `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- inventory_equip_command.py `EXTRACTED`
- [test_quest_service.py](test_quest_service.py.md) `EXTRACTED`
- [test_player_repository.py](test_player_repository.py.md) `EXTRACTED`
- [game_tick_death.py](game_tick_death.py.md) `EXTRACTED`

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
- [User](User.md) `INFERRED`
- PlayerLucidity `INFERRED`
- Base `INFERRED`
- PlayerRepository `INFERRED`
- HealthRepository `INFERRED`
- _assist() `INFERRED`
- [PlayerDeathService](PlayerDeathService.md) `INFERRED`
- [SpellTargetingService](SpellTargetingService.md) `INFERRED`
- LucidityCooldown `INFERRED`
- _protect() `INFERRED`
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) `INFERRED`
- LucidityExposureState `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- PlayerSpell `INFERRED`
- PositionState `INFERRED`
- PlayerSavePreparer `INFERRED`
- PlayerEffect `INFERRED`
- PlayerSkill `INFERRED`
- _bank_world() `INFERRED`
- CorruptionCooldown `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*