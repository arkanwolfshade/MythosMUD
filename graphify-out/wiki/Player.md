# Player

> God node · 185 connections · `server/models/player.py`

**Community:** [[Player Domain Model]]

## Connections by Relation

### calls
- [[row_to_player()]] `EXTRACTED`
- [[.create_player_with_stats()]] `EXTRACTED`
- [[.create_player()]] `EXTRACTED`
- [[test_add_player_effect_generates_id()]] `EXTRACTED`
- [[test_lucidity_adjustment_round_trip()]] `EXTRACTED`
- [[quest_seed_data()]] `EXTRACTED`
- [[test_player_add_experience()]] `EXTRACTED`
- [[test_player_add_experience_zero()]] `EXTRACTED`
- [[test_player_apply_dp_change_became_dead()]] `EXTRACTED`
- [[test_player_apply_dp_change_became_mortally_wounded()]] `EXTRACTED`
- [[test_player_apply_dp_change_updates_dp()]] `EXTRACTED`
- [[test_player_apply_dp_decay_caps_at_negative_10()]] `EXTRACTED`
- [[test_player_apply_dp_decay_changes_posture_when_crossing_zero()]] `EXTRACTED`
- [[test_player_apply_dp_decay_reduces_dp()]] `EXTRACTED`
- [[test_player_creation()]] `EXTRACTED`
- [[test_player_defaults()]] `EXTRACTED`
- [[test_player_get_combat_stats()]] `EXTRACTED`
- [[test_player_get_combat_stats_defaults()]] `EXTRACTED`
- [[test_player_get_equipped_items()]] `EXTRACTED`
- [[test_player_get_equipped_items_empty()]] `EXTRACTED`

### contains
- [[player.py]] `EXTRACTED`

### imports
- [[async_persistence.py]] `EXTRACTED`
- [[__init__.py]] `EXTRACTED`
- [[game_tick_processing.py]] `EXTRACTED`
- [[test_player_death_service.py]] `EXTRACTED`
- [[test_player_model.py]] `EXTRACTED`
- [[lucidity_service.py]] `EXTRACTED`
- [[inventory_equip_command.py]] `EXTRACTED`
- [[websocket_initial_state.py]] `EXTRACTED`
- [[test_player_respawn_service.py]] `EXTRACTED`
- [[test_websocket_initial_state.py]] `EXTRACTED`
- [[inventory_command_helpers.py]] `EXTRACTED`
- [[user.py]] `EXTRACTED`
- [[test_player_repository.py]] `EXTRACTED`
- [[test_async_persistence_core.py]] `EXTRACTED`
- [[player_respawn_service.py]] `EXTRACTED`
- [[inventory_pickup_command.py]] `EXTRACTED`
- [[websocket_helpers.py]] `EXTRACTED`
- [[test_async_persistence_delegates.py]] `EXTRACTED`
- [[inventory_unequip_command.py]] `EXTRACTED`
- [[player_event_handlers_respawn.py]] `EXTRACTED`

### inherits
- [[Base]] `EXTRACTED`

### method
- [[.get_stats()]] `EXTRACTED`
- [[.set_stats()]] `EXTRACTED`
- [[.apply_dp_change()]] `EXTRACTED`
- [[.apply_dp_decay()]] `EXTRACTED`
- [[.restore_to_full_health()]] `EXTRACTED`
- [[.get_combat_stats()]] `EXTRACTED`
- [[.get_health_percentage()]] `EXTRACTED`
- [[.get_health_state()]] `EXTRACTED`
- [[.is_alive()]] `EXTRACTED`
- [[.is_dead()]] `EXTRACTED`
- [[.is_mortally_wounded()]] `EXTRACTED`
- [[.add_experience()]] `EXTRACTED`
- [[.get_equipped_items()]] `EXTRACTED`
- [[.get_inventory()]] `EXTRACTED`
- [[.get_status_effects()]] `EXTRACTED`
- [[.__init__()]] `EXTRACTED`
- [[.is_admin_user()]] `EXTRACTED`
- [[.__repr__()]] `EXTRACTED`
- [[.set_admin_status()]] `EXTRACTED`
- [[.set_equipped_items()]] `EXTRACTED`

### rationale_for
- [[Player model for game data.      Stores all game-specific data for a user includ]] `EXTRACTED`

### references
- [[_convert_legacy_stats_string()]] `EXTRACTED`

### uses
- [[User]] `INFERRED`
- [[Base]] `INFERRED`
- [[PlayerLucidity]] `INFERRED`
- [[PlayerDeathService]] `INFERRED`
- [[PlayerRepository]] `INFERRED`
- [[LucidityAdjustmentLog]] `INFERRED`
- [[AsyncPersistenceLayer]] `INFERRED`
- [[LucidityExposureState]] `INFERRED`
- [[LucidityCooldown]] `INFERRED`
- [[PlayerSpell]] `INFERRED`
- [[PlayerRepositoryProtocol]] `INFERRED`
- [[HealthRepository]] `INFERRED`
- [[PlayerSavePreparer]] `INFERRED`
- [[PositionState]] `INFERRED`
- [[PlayerSkill]] `INFERRED`
- [[PlayerEffect]] `INFERRED`
- [[ExperienceRepository]] `INFERRED`
- [[Player]] `INFERRED`
- [[Player]] `INFERRED`
- [[AsyncSession]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
