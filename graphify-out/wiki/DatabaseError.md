# DatabaseError

> God node · 206 connections · `server/exceptions.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- ._execute_create_npc_definition() `EXTRACTED`
- ._execute_npc_update() `EXTRACTED`
- ._execute_create_spawn_rule() `EXTRACTED`
- ._get_room_uuid_by_stable_id() `EXTRACTED`
- .mark_room_as_explored() `EXTRACTED`
- .get_npc_definitions() `EXTRACTED`
- test_persist_all_players_database_error_on_player() `EXTRACTED`
- .is_room_explored() `EXTRACTED`
- .get_spawn_rules() `EXTRACTED`
- .get_explored_rooms() `EXTRACTED`
- .get_system_statistics() `EXTRACTED`
- test_handle_mute_command_exception() `EXTRACTED`
- test_apply_lucidity_change_adjustment_error() `EXTRACTED`
- test_validate_token_impl_database_error() `EXTRACTED`
- test_establish_websocket_connection_error() `EXTRACTED`
- test_subscribe_to_room_events_impl_database_error() `EXTRACTED`
- test_unsubscribe_from_room_events_impl_database_error() `EXTRACTED`
- test_disconnect_connection_for_session_close_error() `EXTRACTED`
- test_broadcast_player_entered_game_success_and_error() `EXTRACTED`
- test_send_room_occupants_update_paths() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- async_persistence.py `EXTRACTED`
- database.py `EXTRACTED`
- [connection_manager_methods.py](connection_manager_methods.py.md) `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- [test_combat_service_modules.py](test_combat_service_modules.py.md) `EXTRACTED`
- [persistence/container_persistence.py](persistence-container_persistence.py.md) `EXTRACTED`
- [test_player_respawn_service.py](test_player_respawn_service.py.md) `EXTRACTED`
- [test_maps.py](test_maps.py.md) `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- [test_connection_establishment.py](test_connection_establishment.py.md) `EXTRACTED`
- [test_npc_service.py](test_npc_service.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) `EXTRACTED`
- [test_exceptions.py](test_exceptions.py.md) `EXTRACTED`
- [container_persistence/container_persistence.py](container_persistence-container_persistence.py.md) `EXTRACTED`

### inherits
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`

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
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) `INFERRED`
- [HealthRepository](HealthRepository.md) `INFERRED`
- PlayerRepository `INFERRED`
- TestSanitization `INFERRED`
- [SkillRepository](SkillRepository.md) `INFERRED`
- [ExperienceRepository](ExperienceRepository.md) `INFERRED`
- [ConnectionCleaner](ConnectionCleaner.md) `INFERRED`
- TestErrorHandlers `INFERRED`
- PlayerSkillRepository `INFERRED`
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) `INFERRED`
- [RoomCacheLoader](RoomCacheLoader.md) `INFERRED`
- DatabaseManager `INFERRED`
- TestCircuitBreaker `INFERRED`
- QuestInstanceRepository `INFERRED`
- TestErrorResponse `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*