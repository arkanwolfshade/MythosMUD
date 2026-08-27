# Player

> God node · 201 connections · `server/models/player.py`

**Community:** [ContainerComponent](ContainerComponent.md)

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
- server/models/__init__.py `EXTRACTED`
- models/user.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- test_player_model.py `EXTRACTED`
- [inventory_equip_command.py](inventory_equip_command.py.md) `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- [test_player_repository.py](test_player_repository.py.md) `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_inventory_equip_command.py `EXTRACTED`
- inventory_pickup_command.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- lucidity.py `EXTRACTED`
- inventory_unequip_command.py `EXTRACTED`
- container_service_transfer_to.py `EXTRACTED`
- [test_async_persistence_room_cache.py](test_async_persistence_room_cache.py.md) `EXTRACTED`
- container_helpers_inventory_find.py `EXTRACTED`
- database_helpers.py `EXTRACTED`
- [inventory_get_command.py](inventory_get_command.py.md) `EXTRACTED`
- router.py `EXTRACTED`

### inherits
- [Base](Base.md) `EXTRACTED`

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
- [Base](Base.md) `INFERRED`
- HealthRepository `INFERRED`
- PlayerRepository `INFERRED`
- [SpellTargetingService](SpellTargetingService.md) `INFERRED`
- [ExperienceRepository](ExperienceRepository.md) `INFERRED`
- LucidityExposureState `INFERRED`
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) `INFERRED`
- LucidityAdjustmentLog `INFERRED`
- LucidityCooldown `INFERRED`
- PlayerSpell `INFERRED`
- [PlayerSavePreparer](PlayerSavePreparer.md) `INFERRED`
- PositionState `INFERRED`
- PlayerSkill `INFERRED`
- PlayerEffect `INFERRED`
- validate_and_fix_player_room() `INFERRED`
- _sample_work() `INFERRED`
- should_skip_room_validation() `INFERRED`
- validate_and_fix_player_room_with_persistence() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*