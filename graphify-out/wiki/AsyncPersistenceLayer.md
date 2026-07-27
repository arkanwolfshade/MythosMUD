# AsyncPersistenceLayer

> God node · 183 connections · `server/async_persistence.py`

**Community:** [Combat Command Handler](Combat_Command_Handler.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`
- test_async_persistence_layer_init_deprecated_params() `EXTRACTED`
- test_async_persistence_layer_init_skip_room_cache() `EXTRACTED`
- test_async_persistence_layer_init_with_room_cache() `EXTRACTED`

### contains
- async_persistence.py `EXTRACTED`

### imports
- dependencies.py `EXTRACTED`
- monitoring.py `EXTRACTED`
- maps.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_async_persistence_delegates.py `EXTRACTED`
- population_control.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- passive_lucidity_flux_service.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- player_respawn.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._ensure_room_cache_loaded() `EXTRACTED`
- .get_player_by_id() `EXTRACTED`
- .get_players_batch() `EXTRACTED`
- .apply_corruption() `EXTRACTED`
- .apply_fear() `EXTRACTED`
- .apply_lucidity_loss() `EXTRACTED`
- .async_damage_player() `EXTRACTED`
- .async_heal_player() `EXTRACTED`
- .create_container() `EXTRACTED`
- .damage_player() `EXTRACTED`
- .get_active_player_effects() `EXTRACTED`
- .get_active_players_by_user_id() `EXTRACTED`
- .get_container() `EXTRACTED`
- .get_containers_by_entity_id() `EXTRACTED`
- .get_decayed_containers() `EXTRACTED`
- .get_player_by_name() `EXTRACTED`
- .get_player_by_user_id() `EXTRACTED`
- .get_players_by_user_id() `EXTRACTED`
- .get_players_in_room() `EXTRACTED`

### rationale_for
- Async persistence layer using SQLAlchemy ORM for true async PostgreSQL operation `EXTRACTED`

### references
- get_async_persistence() `EXTRACTED`

### uses
- [DatabaseError](DatabaseError.md) `INFERRED`
- HolidayService `INFERRED`
- CombatCommandHandler `INFERRED`
- ScheduleService `INFERRED`
- SkillService `INFERRED`
- RoomCacheLoader `INFERRED`
- CombatDeathHandler `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- Request `INFERRED`
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- CombatParticipant `INFERRED`
- Any `INFERRED`
- _NpcWithLife `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- [AliasStorage](AliasStorage.md) `INFERRED`
- AppWithState `INFERRED`
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- CombatService `INFERRED`
- TargetMatch `INFERRED`
- CoreBundle `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*