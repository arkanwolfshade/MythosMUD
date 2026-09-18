# DatabaseError

> God node · 214 connections · `server/exceptions.py`

**Community:** [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md)

## Connections by Relation

### calls
- ._execute_create_spawn_rule() `EXTRACTED`
- ._get_room_uuid_by_stable_id() `EXTRACTED`
- .mark_room_as_explored() `EXTRACTED`
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
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- test_combat_service_modules.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- test_connection_session_management.py `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- test_exploration_service.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- connection_establishment.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- test_container_persistence_extended_crud.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_async_persistence_core.py `EXTRACTED`
- test_container_persistence_async_helpers.py `EXTRACTED`
- admin_teleport_commands.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- HealthRepository `INFERRED`
- DialogueDefinitionRepository `INFERRED`
- ConnectionCleaner `INFERRED`
- ExperienceRepository `INFERRED`
- PlayerSpellRepository `INFERRED`
- SkillRepository `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- PlayerSkillRepository `INFERRED`
- PlayerEffectRepository `INFERRED`
- SpellRepository `INFERRED`
- QuestInstanceRepository `INFERRED`
- ProfessionRepository `INFERRED`
- SkillUseLogRepository `INFERRED`
- QuestDefinitionRepository `INFERRED`
- EmoteRepository `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- test_establish_websocket_connection_error() `INFERRED`
- test_disconnect_connection_for_session_close_error() `INFERRED`
- fetch_professions() `INFERRED`
- _create_engine_or_raise() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*