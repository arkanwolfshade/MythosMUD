# DatabaseError

> God node · 434 connections · `server/exceptions.py`

**Community:** [Optimization Archive Modernization](Optimization_Archive_Modernization.md)

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
- test_get_current_room_id_none_when_persistence_errors() `EXTRACTED`
- test_handle_mute_command_exception() `EXTRACTED`
- test_validate_token_impl_database_error() `EXTRACTED`
- test_establish_websocket_connection_error() `EXTRACTED`
- test_subscribe_to_room_events_impl_database_error() `EXTRACTED`
- test_unsubscribe_from_room_events_impl_database_error() `EXTRACTED`
- test_canonical_room_id_impl_database_error() `EXTRACTED`
- test_disconnect_connection_for_session_close_error() `EXTRACTED`
- test_broadcast_connection_message_impl_error() `EXTRACTED`
- test_track_player_disconnected_impl_error() `EXTRACTED`

### contains
- exceptions.py `EXTRACTED`

### imports
- connection_manager_methods.py `EXTRACTED`
- database.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- test_container_persistence.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_player_service.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- test_connection_establishment.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- test_container_persistence_extended_crud.py `EXTRACTED`

### indirect_call
- _handle_admin_set_stat_command() `INFERRED`
- send_game_event() `INFERRED`
- track_player_disconnected_impl() `INFERRED`
- update_container() `INFERRED`
- create_container() `INFERRED`
- establish_websocket_connection() `INFERRED`
- handle_mute_command() `INFERRED`
- handle_teleport_command() `INFERRED`
- create_container() `INFERRED`
- get_container() `INFERRED`
- update_container() `INFERRED`
- canonical_room_id_impl() `INFERRED`
- get_container() `INFERRED`
- handle_goto_command() `INFERRED`
- track_player_connected_impl() `INFERRED`
- get_containers_by_entity_id() `INFERRED`
- delete_container() `INFERRED`
- cleanup_websocket_disconnect() `INFERRED`
- _disconnect_connection_for_session() `INFERRED`
- handle_new_game_session_impl() `INFERRED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- CircuitBreaker `INFERRED`
- ErrorResponse `INFERRED`
- PlayerSpellRepository `INFERRED`
- TestErrorMapping `INFERRED`
- PlayerRepository `INFERRED`
- TestSanitization `INFERRED`
- RoomCacheLoader `INFERRED`
- DatabaseManager `INFERRED`
- ConnectionCleaner `INFERRED`
- TestErrorHandlers `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- [Player](Player.md) `INFERRED`
- TestCircuitBreaker `INFERRED`
- UUID `INFERRED`
- Request `INFERRED`
- Any `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- HealthRepository `INFERRED`
- QuestInstanceRepository `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*