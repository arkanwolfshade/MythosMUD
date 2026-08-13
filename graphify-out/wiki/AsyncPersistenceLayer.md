# AsyncPersistenceLayer

> God node · 163 connections · `server/async_persistence.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`
- test_async_persistence_layer_init_deprecated_params() `EXTRACTED`
- test_async_persistence_layer_init_skip_room_cache() `EXTRACTED`
- test_async_persistence_layer_init_with_room_cache() `EXTRACTED`

### contains
- async_persistence.py `EXTRACTED`

### imports
- [server/dependencies.py](server-dependencies.py.md) `EXTRACTED`
- [game_tick_processing.py](game_tick_processing.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [api/monitoring.py](api-monitoring.py.md) `EXTRACTED`
- endpoints.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- population_control.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- [test_async_persistence_core.py](test_async_persistence_core.py.md) `EXTRACTED`
- [rooms.py](rooms.py.md) `EXTRACTED`
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) `EXTRACTED`
- movement_service.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- service.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- api/player_respawn.py `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._ensure_room_cache_loaded() `EXTRACTED`
- .get_player_by_id() `EXTRACTED`
- .get_players_batch() `EXTRACTED`
- .get_player_by_name() `EXTRACTED`
- .get_players_by_user_id() `EXTRACTED`
- .get_active_players_by_user_id() `EXTRACTED`
- .get_player_by_user_id() `EXTRACTED`
- .get_user_by_username_case_insensitive() `EXTRACTED`
- .list_players() `EXTRACTED`
- .get_players_in_room() `EXTRACTED`
- .update_player_last_active() `EXTRACTED`
- .get_professions() `EXTRACTED`
- .add_player_effect() `EXTRACTED`
- .get_active_player_effects() `EXTRACTED`
- .create_container() `EXTRACTED`
- .get_container() `EXTRACTED`
- .get_containers_by_entity_id() `EXTRACTED`
- .get_decayed_containers() `EXTRACTED`
- .set_instance_manager() `EXTRACTED`

### rationale_for
- Async persistence layer using SQLAlchemy ORM for true async PostgreSQL… `EXTRACTED`

### references
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- get_async_persistence() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _weapon_damage_from_equipped_player() `EXTRACTED`
- validate_room_integrity() `EXTRACTED`
- ._init_npc_submodules() `EXTRACTED`
- validate_player_room_membership() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _get_combat_container_services() `EXTRACTED`
- validate_exit() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _get_target_stats_for_damage() `EXTRACTED`

### uses
- [DatabaseError](DatabaseError.md) `INFERRED`
- CombatCommandHandler `INFERRED`
- [HolidayService](HolidayService.md) `INFERRED`
- SkillService `INFERRED`
- ScheduleService `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- [RoomCacheLoader](RoomCacheLoader.md) `INFERRED`
- CreateItemInstanceInput `INFERRED`
- CombatDeathHandler `INFERRED`
- _NpcWithLife `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- CoreBundle `INFERRED`
- _CombatServiceDeps `INFERRED`
- _ConnectionManagerLike `INFERRED`
- _NPCCombatIntegrationLike `INFERRED`
- _HolidayLoadResult `INFERRED`
- _DatabaseLoadResult `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*