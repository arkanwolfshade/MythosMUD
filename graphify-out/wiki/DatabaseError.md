# DatabaseError

> God node · 247 connections · `server/exceptions.py`

**Community:** [[NPC Admin API]]

## Connections by Relation

### calls
- [[._execute_create_npc_definition()]] `EXTRACTED`
- [[._execute_npc_update()]] `EXTRACTED`
- [[._execute_create_spawn_rule()]] `EXTRACTED`
- [[.get_npc_definitions()]] `EXTRACTED`
- [[._get_room_uuid_by_stable_id()]] `EXTRACTED`
- [[.mark_room_as_explored()]] `EXTRACTED`
- [[.get_spawn_rules()]] `EXTRACTED`
- [[.is_room_explored()]] `EXTRACTED`
- [[.get_system_statistics()]] `EXTRACTED`
- [[.get_explored_rooms()]] `EXTRACTED`
- [[test_handle_mute_command_exception()]] `EXTRACTED`
- [[test_validate_token_impl_database_error()]] `EXTRACTED`
- [[test_establish_websocket_connection_error()]] `EXTRACTED`
- [[test_subscribe_to_room_events_impl_database_error()]] `EXTRACTED`
- [[test_unsubscribe_from_room_events_impl_database_error()]] `EXTRACTED`
- [[test_canonical_room_id_impl_database_error()]] `EXTRACTED`
- [[test_disconnect_connection_for_session_close_error()]] `EXTRACTED`
- [[test_broadcast_connection_message_impl_error()]] `EXTRACTED`
- [[test_track_player_disconnected_impl_error()]] `EXTRACTED`
- [[test_track_player_disconnected_impl_finally_cleanup()]] `EXTRACTED`

### contains
- [[exceptions.py]] `EXTRACTED`

### imports
- [[connection_manager_methods.py]] `EXTRACTED`
- [[database.py]] `EXTRACTED`
- [[async_persistence.py]] `EXTRACTED`
- [[players.py]] `EXTRACTED`
- [[test_container_persistence.py]] `EXTRACTED`
- [[test_player_service.py]] `EXTRACTED`
- [[maps.py]] `EXTRACTED`
- [[test_container_persistence_extended_row_helpers.py]] `EXTRACTED`
- [[test_connection_delegates.py]] `EXTRACTED`
- [[container_persistence.py]] `EXTRACTED`
- [[legacy_error_handlers.py]] `EXTRACTED`
- [[test_npc_service.py]] `EXTRACTED`
- [[test_connection_establishment.py]] `EXTRACTED`
- [[test_exploration_service.py]] `EXTRACTED`
- [[test_player_respawn_service.py]] `EXTRACTED`
- [[test_exceptions.py]] `EXTRACTED`
- [[test_database_error_handling.py]] `EXTRACTED`
- [[test_legacy_error_handlers.py]] `EXTRACTED`
- [[test_container_persistence_extended_crud.py]] `EXTRACTED`
- [[test_player_repository.py]] `EXTRACTED`

### inherits
- [[MythosMUDError]] `EXTRACTED`

### method
- [[.__init__()]] `EXTRACTED`

### rationale_for
- [[Database operation errors.]] `EXTRACTED`

### uses
- [[AsyncPersistenceLayer]] `INFERRED`
- [[PlayerSpellRepository]] `INFERRED`
- [[CircuitBreaker]] `INFERRED`
- [[ExplorationService]] `INFERRED`
- [[ErrorResponse]] `INFERRED`
- [[TestErrorMapping]] `INFERRED`
- [[RoomCacheLoader]] `INFERRED`
- [[PlayerRepository]] `INFERRED`
- [[TestSanitization]] `INFERRED`
- [[DatabaseManager]] `INFERRED`
- [[ConnectionCleaner]] `INFERRED`
- [[SkillRepository]] `INFERRED`
- [[TestErrorHandlers]] `INFERRED`
- [[PlayerSkillRepository]] `INFERRED`
- [[QuestInstanceRepository]] `INFERRED`
- [[Player]] `INFERRED`
- [[SkillUseLogRepository]] `INFERRED`
- [[TestCircuitBreaker]] `INFERRED`
- [[UUID]] `INFERRED`
- [[QuestDefinitionRepository]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
