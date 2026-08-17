# DatabaseError

> God node · 264 connections · `server/exceptions.py`

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
- .test_get_severity_for_error_database() `EXTRACTED`
- .test_get_status_code_for_error_database() `EXTRACTED`
- .test_map_error_type_database() `EXTRACTED`
- test_is_transient_error_cause_chain_connection_closed() `INFERRED`
- test_is_transient_error_wrapped_connection_closed() `INFERRED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- [connection_manager_methods.py](connection_manager_methods.py.md) `EXTRACTED`
- async_persistence.py `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [test_combat_service_modules.py](test_combat_service_modules.py.md) `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- [persistence/container_persistence.py](persistence-container_persistence.py.md) `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- [test_connection_delegates.py](test_connection_delegates.py.md) `EXTRACTED`
- [test_connection_session_management.py](test_connection_session_management.py.md) `EXTRACTED`
- [test_npc_service.py](test_npc_service.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- [test_container_persistence_crud.py](test_container_persistence_crud.py.md) `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- PlayerSpellRepository `INFERRED`
- TestErrorMapping `INFERRED`
- [HealthRepository](HealthRepository.md) `INFERRED`
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) `INFERRED`
- PlayerRepository `INFERRED`
- SkillRepository `INFERRED`
- [ExperienceRepository](ExperienceRepository.md) `INFERRED`
- [ConnectionCleaner](ConnectionCleaner.md) `INFERRED`
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) `INFERRED`
- [RoomCacheLoader](RoomCacheLoader.md) `INFERRED`
- PlayerSkillRepository `INFERRED`
- _map_error_type() `INFERRED`
- QuestInstanceRepository `INFERRED`
- _get_status_code_for_error() `INFERRED`
- _get_severity_for_error() `INFERRED`
- PlayerEffectRepository `INFERRED`
- QuestDefinitionRepository `INFERRED`
- SkillUseLogRepository `INFERRED`
- SpellRepository `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*