# DatabaseError

> God node · 297 connections · `server/exceptions.py`

**Community:** [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md)

## Connections by Relation

### calls
- ._get_room_uuid_by_stable_id() `EXTRACTED`
- .mark_room_as_explored() `EXTRACTED`
- ._execute_create_npc_definition() `EXTRACTED`
- ._execute_npc_update() `EXTRACTED`
- ._execute_create_spawn_rule() `EXTRACTED`
- .is_room_explored() `EXTRACTED`
- .get_npc_definitions() `EXTRACTED`
- .get_explored_rooms() `EXTRACTED`
- .get_system_statistics() `EXTRACTED`
- .get_spawn_rules() `EXTRACTED`
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
- connection_manager_methods.py `EXTRACTED`
- database.py `EXTRACTED`
- test_combat_service_modules.py `EXTRACTED`
- test_user_manager.py `EXTRACTED`
- test_player_presence_tracker.py `EXTRACTED`
- test_player_respawn_service.py `EXTRACTED`
- admin_setstat_command.py `EXTRACTED`
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- player_presence_tracker.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_connection_delegates.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_admin_commands.py `EXTRACTED`
- test_player_repository.py `EXTRACTED`
- test_connection_session_management.py `EXTRACTED`
- test_npc_service.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_container_persistence_async_helpers.py `EXTRACTED`

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
- DialogueDefinitionRepository `INFERRED`
- HealthRepository `INFERRED`
- ConnectionCleaner `INFERRED`
- RoomCacheLoader `INFERRED`
- PlayerSpellRepository `INFERRED`
- MythosTimeEventConsumer `INFERRED`
- ExperienceRepository `INFERRED`
- SkillRepository `INFERRED`
- _FakeMuteRepository `INFERRED`
- PlayerMuteRepository `INFERRED`
- PlayerSkillRepository `INFERRED`
- QuestInstanceRepository `INFERRED`
- PlayerEffectRepository `INFERRED`
- QuestRewardsMixin `INFERRED`
- SpellRepository `INFERRED`
- FakeBankPersistence `INFERRED`
- QuestDefinitionRepository `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*