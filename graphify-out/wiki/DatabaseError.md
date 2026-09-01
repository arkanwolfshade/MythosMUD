# DatabaseError

> God node · 251 connections · `server/exceptions.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- ._execute_create_npc_definition() `EXTRACTED`
- ._execute_npc_update() `EXTRACTED`
- ._execute_create_spawn_rule() `EXTRACTED`
- ._get_room_uuid_by_stable_id() `EXTRACTED`
- .mark_room_as_explored() `EXTRACTED`
- .get_npc_definitions() `EXTRACTED`
- .is_room_explored() `EXTRACTED`
- .get_spawn_rules() `EXTRACTED`
- .get_explored_rooms() `EXTRACTED`
- .get_system_statistics() `EXTRACTED`
- test_determine_error_type_from_exception_uses_attr() `EXTRACTED`
- test_canonical_room_id_impl_database_error() `EXTRACTED`
- test_mark_room_as_explored_sync_with_error_handler() `EXTRACTED`
- test_is_transient_error_cause_chain_connection_closed() `INFERRED`
- test_is_transient_error_wrapped_connection_closed() `INFERRED`
- test_seed_new_container_items_skips_bad_rows_and_handles_ensure_error() `EXTRACTED`
- test_extract_player_name_user_access_error() `EXTRACTED`
- test_database_error() `EXTRACTED`
- test_database_error_initialization() `EXTRACTED`
- test_database_error_without_table() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- [connection_manager_methods.py](connection_manager_methods.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- [test_combat_service_modules.py](test_combat_service_modules.py.md) `EXTRACTED`
- test_maps.py `EXTRACTED`
- [test_player_respawn_service.py](test_player_respawn_service.py.md) `EXTRACTED`
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) `EXTRACTED`
- container_persistence.py `EXTRACTED`
- [test_connection_delegates.py](test_connection_delegates.py.md) `EXTRACTED`
- [test_connection_session_management.py](test_connection_session_management.py.md) `EXTRACTED`
- [test_npc_service.py](test_npc_service.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) `EXTRACTED`
- [test_exploration_service.py](test_exploration_service.py.md) `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- connection_establishment.py `EXTRACTED`
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) `EXTRACTED`
- [test_async_persistence_core.py](test_async_persistence_core.py.md) `EXTRACTED`

### inherits
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- PlayerSpellRepository `INFERRED`
- HealthRepository `INFERRED`
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) `INFERRED`
- PlayerRepository `INFERRED`
- SkillRepository `INFERRED`
- [ConnectionCleaner](ConnectionCleaner.md) `INFERRED`
- RoomCacheLoader `INFERRED`
- [ExperienceRepository](ExperienceRepository.md) `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- PlayerSkillRepository `INFERRED`
- QuestInstanceRepository `INFERRED`
- [PlayerEffectRepository](PlayerEffectRepository.md) `INFERRED`
- QuestDefinitionRepository `INFERRED`
- SkillUseLogRepository `INFERRED`
- SpellRepository `INFERRED`
- EmoteRepository `INFERRED`
- ProfessionRepository `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- test_establish_websocket_connection_error() `INFERRED`
- test_disconnect_connection_for_session_close_error() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*