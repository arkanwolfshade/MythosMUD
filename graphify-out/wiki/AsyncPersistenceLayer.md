# AsyncPersistenceLayer

> God node · 171 connections · `server/async_persistence.py`

**Community:** [Async Persistence](Async_Persistence.md)

## Connections by Relation

### calls
- .initialize() `EXTRACTED`
- async_persistence_layer() `EXTRACTED`
- test_async_persistence_layer_init_deprecated_params() `EXTRACTED`
- test_async_persistence_layer_init_skip_room_cache() `EXTRACTED`
- test_async_persistence_layer_init_with_room_cache() `EXTRACTED`

### contains
- async_persistence.py `EXTRACTED`

### imports
- server/dependencies.py `EXTRACTED`
- container_endpoints_basic.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- maps.py `EXTRACTED`
- npc_combat_integration_service.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- rooms.py `EXTRACTED`
- combat_handler.py `EXTRACTED`
- combat_turn_participant_actions.py `EXTRACTED`
- npc_base.py `EXTRACTED`
- population_control.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- lifecycle_manager.py `EXTRACTED`
- movement_service.py `EXTRACTED`
- service.py `EXTRACTED`
- test_async_persistence_delegates.py `EXTRACTED`
- container_service.py `EXTRACTED`
- container_service_transfer_to.py `EXTRACTED`
- game_tick_protocols.py `EXTRACTED`
- api/player_respawn.py `EXTRACTED`

### inherits
- AsyncPersistenceRoomFacade `EXTRACTED`

### method
- .get_container() `EXTRACTED`
- .__init__() `EXTRACTED`
- .create_container() `EXTRACTED`
- .get_player_by_id() `EXTRACTED`
- .get_user_by_username_case_insensitive() `EXTRACTED`
- .get_players_batch() `EXTRACTED`
- .update_player_last_active() `EXTRACTED`
- .get_professions() `EXTRACTED`
- .add_player_effect() `EXTRACTED`
- .get_active_player_effects() `EXTRACTED`
- .ensure_item_instance() `EXTRACTED`
- .set_instance_manager() `EXTRACTED`
- .get_player_by_name() `EXTRACTED`
- .get_players_by_user_id() `EXTRACTED`
- .get_active_players_by_user_id() `EXTRACTED`
- .get_player_by_user_id() `EXTRACTED`
- .soft_delete_player() `EXTRACTED`
- .save_player() `EXTRACTED`
- .list_players() `EXTRACTED`
- .get_room_by_id() `EXTRACTED`

### rationale_for
- Async persistence layer using SQLAlchemy ORM for true async PostgreSQL… `EXTRACTED`

### references
- transfer_items() `EXTRACTED`
- open_container() `EXTRACTED`
- close_container() `EXTRACTED`
- emit_close_container_event() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- validate_exit() `EXTRACTED`
- validate_player_room_membership() `EXTRACTED`
- validate_room_integrity() `EXTRACTED`
- ._init_npc_submodules() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- _get_user_characters() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- .__init__() `EXTRACTED`
- ._init_persistence_and_event_bus() `EXTRACTED`
- .__init__() `EXTRACTED`

### uses
- CombatCommandHandler `INFERRED`
- HolidayService `INFERRED`
- ScheduleService `INFERRED`
- RoomCacheLoader `INFERRED`
- CombatDeathHandler `INFERRED`
- get_container_async_persistence() `INFERRED`
- CreateItemInstanceInput `INFERRED`
- CoreBundle `INFERRED`
- EnsureItemInstanceInput `INFERRED`
- _LifecycleManagerForDeath `INFERRED`
- _weapon_damage_from_equipped_player() `INFERRED`
- TestEmitCloseContainerEvent `INFERRED`
- _get_combat_container_services() `INFERRED`
- resolve_player_attack_damage() `INFERRED`
- InstanceRoomLookup `INFERRED`
- test_build_room_objects_defaults_rest_location_false() `INFERRED`
- test_build_room_objects_promotes_rest_location_from_attributes() `INFERRED`
- PlayerEffectOptions `INFERRED`
- ContainerCreateKwargs `INFERRED`
- _room_from_persistence() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*