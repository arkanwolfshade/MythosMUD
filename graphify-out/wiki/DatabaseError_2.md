# DatabaseError

> God node · 167 connections · `server/exceptions.py`

**Community:** [DatabaseError](DatabaseError.md)

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
- test_handle_mute_command_exception() `EXTRACTED`
- test_validate_token_impl_database_error() `EXTRACTED`
- test_establish_websocket_connection_error() `EXTRACTED`
- test_subscribe_to_room_events_impl_database_error() `EXTRACTED`
- test_unsubscribe_from_room_events_impl_database_error() `EXTRACTED`
- test_disconnect_connection_for_session_close_error() `EXTRACTED`
- test_broadcast_connection_message_impl_error() `EXTRACTED`
- test_track_player_disconnected_impl_error() `EXTRACTED`
- test_track_player_disconnected_impl_finally_cleanup() `EXTRACTED`
- test_change_position_database_error() `EXTRACTED`

### contains
- [server/exceptions.py](server-exceptions.py.md) `EXTRACTED`

### imports
- [database.py](database.py.md) `EXTRACTED`
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [test_container_persistence.py](test_container_persistence.py.md) `EXTRACTED`
- [persistence/container_persistence.py](persistence-container_persistence.py.md) `EXTRACTED`
- [test_player_service.py](test_player_service.py.md) `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- connection_manager_methods.py `EXTRACTED`
- [test_connection_delegates.py](test_connection_delegates.py.md) `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- [test_connection_establishment.py](test_connection_establishment.py.md) `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- player_service.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- PlayerSpellRepository `INFERRED`
- [CircuitBreaker](CircuitBreaker.md) `INFERRED`
- TestErrorMapping `INFERRED`
- ErrorResponse `INFERRED`
- PlayerRepository `INFERRED`
- TestSanitization `INFERRED`
- [ConnectionCleaner](ConnectionCleaner.md) `INFERRED`
- TestErrorHandlers `INFERRED`
- [RoomCacheLoader](RoomCacheLoader.md) `INFERRED`
- [DatabaseManager](DatabaseManager.md) `INFERRED`
- TestCircuitBreaker `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- [HealthRepository](HealthRepository.md) `INFERRED`
- QuestInstanceRepository `INFERRED`
- TestErrorResponse `INFERRED`
- SkillRepository `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- PlayerEffectRepository `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*