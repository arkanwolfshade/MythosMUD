# AsyncPersistenceLayer

> God node · 165 connections · `server/async_persistence.py`

**Community:** [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`

### contains
- async_persistence.py `EXTRACTED`

### imports
- server/dependencies.py `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- population_control.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- rooms.py `EXTRACTED`
- service.py `EXTRACTED`
- test_async_persistence_delegates.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- player_event_handlers_respawn.py `EXTRACTED`
- container_service.py `EXTRACTED`
- container_service_transfer_to.py `EXTRACTED`
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
- emit_close_container_event() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- validate_exit() `EXTRACTED`
- validate_player_room_membership() `EXTRACTED`
- validate_room_integrity() `EXTRACTED`
- ._init_npc_submodules() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _get_user_characters() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_persistence_and_event_bus() `EXTRACTED`

### uses
- [DatabaseError](DatabaseError.md) `INFERRED`
- CombatCommandHandler `INFERRED`
- HolidayService `INFERRED`
- ScheduleService `INFERRED`
- RoomCacheLoader `INFERRED`
- CombatDeathHandler `INFERRED`
- CreateItemInstanceInput `INFERRED`
- CoreBundle `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- _weapon_damage_from_equipped_player() `INFERRED`
- TestEmitCloseContainerEvent `INFERRED`
- _get_combat_container_services() `INFERRED`
- resolve_player_attack_damage() `INFERRED`
- _room_from_persistence() `INFERRED`
- _get_target_stats_for_damage() `INFERRED`
- test_apply_corruption_delegates() `INFERRED`
- test_apply_fear_delegates() `INFERRED`
- test_apply_lucidity_loss_delegates() `INFERRED`
- test_async_damage_player_delegates() `INFERRED`
- test_async_heal_player_delegates() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*