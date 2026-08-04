# DatabaseError

> God node · 497 connections · `server/exceptions.py`

**Community:** [commands shutdown process](commands_shutdown_process.md)

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
- test_persist_all_players_database_error_on_player() `EXTRACTED`
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

### contains
- exceptions.py `EXTRACTED`

### imports
- connection_manager_methods.py `EXTRACTED`
- database.py `EXTRACTED`
- async_persistence.py `EXTRACTED`
- players.py `EXTRACTED`
- test_combat_service_modules.py `EXTRACTED`
- test_container_persistence.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- maps.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_connection_establishment.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_admin_setlucidity_command.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`

### indirect_call
- _handle_admin_set_stat_command() `INFERRED`
- handle_teleport_command() `INFERRED`
- send_game_event() `INFERRED`
- track_player_disconnected_impl() `INFERRED`
- update_container() `INFERRED`
- create_container() `INFERRED`
- establish_websocket_connection() `INFERRED`
- handle_goto_command() `INFERRED`
- handle_mute_command() `INFERRED`
- get_container_async() `INFERRED`
- create_container() `INFERRED`
- get_container() `INFERRED`
- update_container() `INFERRED`
- ._initialize_database() `INFERRED`
- canonical_room_id_impl() `INFERRED`
- handle_confirm_teleport_command() `INFERRED`
- handle_confirm_goto_command() `INFERRED`
- get_container() `INFERRED`
- track_player_connected_impl() `INFERRED`
- create_container_async() `INFERRED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- AsyncPersistenceLayer `INFERRED`
- CircuitBreaker `INFERRED`
- PlayerSpellRepository `INFERRED`
- ErrorResponse `INFERRED`
- TestErrorMapping `INFERRED`
- DialogueDefinitionRepository `INFERRED`
- HealthRepository `INFERRED`
- PlayerRepository `INFERRED`
- TestSanitization `INFERRED`
- RoomCacheLoader `INFERRED`
- DatabaseManager `INFERRED`
- SkillRepository `INFERRED`
- ExperienceRepository `INFERRED`
- ConnectionCleaner `INFERRED`
- TestErrorHandlers `INFERRED`
- PlayerSkillRepository `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- [Player](Player.md) `INFERRED`
- TestCircuitBreaker `INFERRED`
- UUID `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*