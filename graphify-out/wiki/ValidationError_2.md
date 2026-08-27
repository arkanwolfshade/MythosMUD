# ValidationError

> God node · 282 connections · `server/exceptions.py`

**Community:** [generate_invites_db.py](generate_invites_db.py.md)

## Connections by Relation

### calls
- get_database_path() `EXTRACTED`
- handle_exception() `EXTRACTED`
- ._get_rooms_for_movement() `EXTRACTED`
- ._resolve_player_for_movement() `EXTRACTED`
- .test_roll_character_stats_profession_not_found() `EXTRACTED`
- test_get_database_path_none_url() `EXTRACTED`
- test_get_engine_raises_validation_error() `EXTRACTED`
- test_get_session_maker_raises_validation_error() `EXTRACTED`
- test_handle_delirium_validation_generic_500() `EXTRACTED`
- test_handle_delirium_validation_lucidity_keyword() `EXTRACTED`
- test_handle_delirium_validation_must_be_delirious() `EXTRACTED`
- test_handle_delirium_validation_not_found() `EXTRACTED`
- test_handle_respawn_validation_generic_500() `EXTRACTED`
- test_handle_respawn_validation_must_be_dead() `EXTRACTED`
- test_handle_respawn_validation_not_found() `EXTRACTED`
- test_parse_command_string_validation_error() `EXTRACTED`
- test_create_command_object_re_raises_mythos_validation_error() `EXTRACTED`
- test_process_command_string_mythos_validation_error() `EXTRACTED`
- .validate_and_get_profession() `EXTRACTED`
- test_handle_validation_error_security_sensitive() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- [command_service.py](command_service.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- [test_movement_service.py](test_movement_service.py.md) `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- test_command_parser.py `EXTRACTED`
- command_parser.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) `EXTRACTED`
- [test_command_processor.py](test_command_processor.py.md) `EXTRACTED`
- [test_command_service.py](test_command_service.py.md) `EXTRACTED`

### inherits
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._log_error() `EXTRACTED`

### rationale_for
- Data validation errors (e.g. empty local/whisper message). Log at warning, not… `EXTRACTED`

### uses
- [DatabaseManager](DatabaseManager.md) `INFERRED`
- validate_room_data() `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- init_npc_db() `INFERRED`
- _initialize_npc_database() `INFERRED`
- TestValidateRoomData `INFERRED`
- get_npc_database_path() `INFERRED`
- _create_engine_or_raise() `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- TestNPCDatabaseInitialization `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- load_database_url() `INFERRED`
- validate_database_url() `INFERRED`
- test_respawn_player_from_delirium_not_found() `INFERRED`
- test_respawn_player_not_found() `INFERRED`
- test_respawn_player_validation_error() `INFERRED`
- test_create_player_validation_error_to_400() `INFERRED`
- test_delete_player_validation_error() `INFERRED`
- test_resolve_player_username_error() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*