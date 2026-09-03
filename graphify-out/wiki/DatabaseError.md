# DatabaseError

> God node · 224 connections · `server/exceptions.py`

**Community:** [Error Handling & Exceptions](Error_Handling_&_Exceptions.md)

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
- connection_manager_methods.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- test_connection_session_management.py `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_admin_setlucidity_command.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- connection_establishment.py `EXTRACTED`
- test_container_persistence_extended_crud.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_container_persistence_async_helpers.py `EXTRACTED`
- test_player_repository.py `EXTRACTED`
- connection_delegates.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- PlayerSpellRepository `INFERRED`
- DialogueDefinitionRepository `INFERRED`
- HealthRepository `INFERRED`
- SkillRepository `INFERRED`
- PlayerRepository `INFERRED`
- ConnectionCleaner `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- PlayerSkillRepository `INFERRED`
- QuestInstanceRepository `INFERRED`
- QuestDefinitionRepository `INFERRED`
- SkillUseLogRepository `INFERRED`
- SpellRepository `INFERRED`
- EmoteRepository `INFERRED`
- ProfessionRepository `INFERRED`
- test_establish_websocket_connection_error() `INFERRED`
- test_disconnect_connection_for_session_close_error() `INFERRED`
- test_persist_all_players_database_error_on_player() `INFERRED`
- test_initialize_database_connection_error() `INFERRED`
- test_initialize_database_generic_exception() `INFERRED`
- test_initialize_database_os_error() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*