# DatabaseError

> God node · 203 connections · `server/exceptions.py`

**Community:** [ContainerComponent](ContainerComponent.md)

## Connections by Relation

### calls
- ._execute_create_npc_definition() `EXTRACTED`
- ._execute_npc_update() `EXTRACTED`
- ._execute_create_spawn_rule() `EXTRACTED`
- .get_npc_definitions() `EXTRACTED`
- .get_spawn_rules() `EXTRACTED`
- .get_system_statistics() `EXTRACTED`
- test_determine_error_type_from_exception_uses_attr() `EXTRACTED`
- test_canonical_room_id_impl_database_error() `EXTRACTED`
- test_is_transient_error_cause_chain_connection_closed() `INFERRED`
- test_is_transient_error_wrapped_connection_closed() `INFERRED`
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
- [maps.py](maps.py.md) `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- test_connection_session_management.py `EXTRACTED`
- [test_npc_service.py](test_npc_service.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- [connection_establishment.py](connection_establishment.py.md) `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) `EXTRACTED`
- [test_player_repository.py](test_player_repository.py.md) `EXTRACTED`
- connection_delegates.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- [admin_teleport_commands.py](admin_teleport_commands.py.md) `EXTRACTED`

### inherits
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- PlayerSpellRepository `INFERRED`
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) `INFERRED`
- HealthRepository `INFERRED`
- PlayerRepository `INFERRED`
- [ConnectionCleaner](ConnectionCleaner.md) `INFERRED`
- SkillRepository `INFERRED`
- [ExperienceRepository](ExperienceRepository.md) `INFERRED`
- [RoomCacheLoader](RoomCacheLoader.md) `INFERRED`
- PlayerSkillRepository `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- QuestInstanceRepository `INFERRED`
- PlayerEffectRepository `INFERRED`
- SpellRepository `INFERRED`
- QuestDefinitionRepository `INFERRED`
- SkillUseLogRepository `INFERRED`
- ProfessionRepository `INFERRED`
- test_establish_websocket_connection_error() `INFERRED`
- test_disconnect_connection_for_session_close_error() `INFERRED`
- _create_engine_or_raise() `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*