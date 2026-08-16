# Player

> God node · 229 connections · `server/models/player.py`

**Community:** [Player](Player.md)

## Connections by Relation

### calls
- .create_player_with_stats() `EXTRACTED`
- .create_player() `EXTRACTED`
- quest_seed_data() `EXTRACTED`

### contains
- models/player.py `EXTRACTED`

### imports
- server/models/__init__.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- [game_tick_processing.py](game_tick_processing.py.md) `EXTRACTED`
- models/user.py `EXTRACTED`
- [look_command.py](look_command.py.md) `EXTRACTED`
- [test_player_respawn_service.py](test_player_respawn_service.py.md) `EXTRACTED`
- [test_player_death_service.py](test_player_death_service.py.md) `EXTRACTED`
- lucidity_service.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- [test_player_model.py](test_player_model.py.md) `EXTRACTED`
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) `EXTRACTED`
- [inventory_equip_command.py](inventory_equip_command.py.md) `EXTRACTED`
- websocket_initial_state.py `EXTRACTED`
- [test_async_persistence_core.py](test_async_persistence_core.py.md) `EXTRACTED`
- [test_player_repository.py](test_player_repository.py.md) `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- websocket_helpers.py `EXTRACTED`
- [test_inventory_equip_command.py](test_inventory_equip_command.py.md) `EXTRACTED`
- [service.py](service.py.md) `EXTRACTED`
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) `EXTRACTED`

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
- _convert_legacy_stats_string() `EXTRACTED`

### uses
- [User](User.md) `INFERRED`
- PlayerLucidity `INFERRED`
- Base `INFERRED`
- [HealthRepository](HealthRepository.md) `INFERRED`
- [PlayerRepository](PlayerRepository.md) `INFERRED`
- ExperienceRepository `INFERRED`
- SpellTargetingService `INFERRED`
- [PlayerDeathService](PlayerDeathService.md) `INFERRED`
- LucidityExposureState `INFERRED`
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) `INFERRED`
- LucidityCooldown `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- PlayerSpell `INFERRED`
- row_to_player() `INFERRED`
- PositionState `INFERRED`
- PlayerSavePreparer `INFERRED`
- PlayerSkill `INFERRED`
- PlayerEffect `INFERRED`
- validate_and_fix_player_room() `INFERRED`
- _sample_work() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*