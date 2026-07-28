# AsyncPersistenceLayer

> God node · 183 connections · `server/async_persistence.py`

**Community:** [Server Infrastructure (4)](Server_Infrastructure_%284%29.md)

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
- endpoints.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- population_control.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_async_persistence_delegates.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- service.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- player_disconnect_handlers.py `EXTRACTED`
- combat_loader.py `EXTRACTED`

### indirect_call
- .is_admin() `INFERRED`
- resolve_player_attack_damage() `INFERRED`
- ._move_with_integration() `INFERRED`
- .add_admin() `INFERRED`
- .remove_admin() `INFERRED`

### method
- ._ensure_room_cache_loaded() `EXTRACTED`
- .__init__() `EXTRACTED`
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
- loot_all_items() `EXTRACTED`
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- get_async_persistence() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _weapon_damage_from_equipped_player() `EXTRACTED`
- validate_room_integrity() `EXTRACTED`
- ._init_npc_submodules() `EXTRACTED`
- .__init__() `EXTRACTED`
- _get_combat_container_services() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._get_persistence_from_app() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _get_target_stats_for_damage() `EXTRACTED`

### uses
- [DatabaseError](DatabaseError.md) `INFERRED`
- CombatCommandHandler `INFERRED`
- HolidayService `INFERRED`
- SkillService `INFERRED`
- RoomCacheLoader `INFERRED`
- Request `INFERRED`
- CombatCommandHandlerExtras `INFERRED`
- ScheduleService `INFERRED`
- CombatDeathHandler `INFERRED`
- _NpcWithLife `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- CoreBundle `INFERRED`
- CreateItemInstanceInput `INFERRED`
- Any `INFERRED`
- _CombatServiceDeps `INFERRED`
- _ConnectionManagerLike `INFERRED`
- _NPCCombatIntegrationLike `INFERRED`
- UUID `INFERRED`
- datetime `INFERRED`
- Any `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*