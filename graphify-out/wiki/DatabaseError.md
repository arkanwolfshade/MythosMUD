# DatabaseError

> God node · 255 connections · `server/exceptions.py`

**Community:** [scripts populate test npc databases](scripts_populate_test_npc_databases.md)

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
- async_persistence.py `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- persistence/container_persistence.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- test_connection_session_management.py `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- test_admin_setlucidity_command.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_container_persistence_crud.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`
- container_persistence/container_persistence.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) `INFERRED`
- TestErrorMapping `INFERRED`
- HealthRepository `INFERRED`
- DialogueDefinitionRepository `INFERRED`
- PlayerRepository `INFERRED`
- SkillRepository `INFERRED`
- ExperienceRepository `INFERRED`
- PlayerSpellRepository `INFERRED`
- ConnectionCleaner `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- RoomCacheLoader `INFERRED`
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