# DatabaseError

> God node · 297 connections · `server/exceptions.py`

**Community:** [LoggingPatternLinter](LoggingPatternLinter.md)

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
- .create_container() `EXTRACTED`
- test_mark_room_as_explored_sync_with_error_handler() `EXTRACTED`
- .delete() `EXTRACTED`
- test_is_transient_error_cause_chain_connection_closed() `INFERRED`
- test_is_transient_error_wrapped_connection_closed() `INFERRED`
- .load_active() `EXTRACTED`
- test_seed_new_container_items_skips_bad_rows_and_handles_ensure_error() `EXTRACTED`
- test_extract_player_name_user_access_error() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- [connection_manager_methods.py](connection_manager_methods.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- [test_combat_service_modules.py](test_combat_service_modules.py.md) `EXTRACTED`
- [test_player_respawn_service.py](test_player_respawn_service.py.md) `EXTRACTED`
- [admin_setstat_command.py](admin_setstat_command.py.md) `EXTRACTED`
- [test_user_manager.py](test_user_manager.py.md) `EXTRACTED`
- [player_presence_tracker.py](player_presence_tracker.py.md) `EXTRACTED`
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- player_respawn_service.py `EXTRACTED`
- test_admin_commands.py `EXTRACTED`
- [test_connection_delegates.py](test_connection_delegates.py.md) `EXTRACTED`
- [test_player_repository.py](test_player_repository.py.md) `EXTRACTED`
- [test_connection_session_management.py](test_connection_session_management.py.md) `EXTRACTED`
- [test_npc_service.py](test_npc_service.py.md) `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Database operation errors. `EXTRACTED`

### uses
- CombatTurnProcessor `INFERRED`
- GameBundle `INFERRED`
- PlayerRepository `INFERRED`
- PlayerSpellRepository `INFERRED`
- HealthRepository `INFERRED`
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) `INFERRED`
- SkillRepository `INFERRED`
- [ConnectionCleaner](ConnectionCleaner.md) `INFERRED`
- [RoomCacheLoader](RoomCacheLoader.md) `INFERRED`
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) `INFERRED`
- PlayerSkillRepository `INFERRED`
- [ExperienceRepository](ExperienceRepository.md) `INFERRED`
- _FakeMuteRepository `INFERRED`
- QuestInstanceRepository `INFERRED`
- PlayerMuteRepository `INFERRED`
- [PlayerEffectRepository](PlayerEffectRepository.md) `INFERRED`
- QuestDefinitionRepository `INFERRED`
- ItemCatalogRepository `INFERRED`
- FakeBankPersistence `INFERRED`
- SkillUseLogRepository `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*