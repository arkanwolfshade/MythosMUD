# ValidationError

> God node · 330 connections · `server/exceptions.py`

**Community:** [ValidationError](ValidationError.md)

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
- .test_mythos_exception_handler_sets_request_id() `EXTRACTED`
- test_handle_delirium_validation_generic_500() `EXTRACTED`
- test_handle_delirium_validation_lucidity_keyword() `EXTRACTED`
- test_handle_delirium_validation_must_be_delirious() `EXTRACTED`
- test_handle_delirium_validation_not_found() `EXTRACTED`
- test_handle_respawn_validation_generic_500() `EXTRACTED`
- test_handle_respawn_validation_must_be_dead() `EXTRACTED`
- test_handle_respawn_validation_not_found() `EXTRACTED`
- .test_mythos_exception_handler() `EXTRACTED`
- .test_mythos_exception_handler_with_debug() `EXTRACTED`
- test_parse_command_string_validation_error() `EXTRACTED`
- .test_create_error_response_sanitizes_unsafe_keys() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- [command_service.py](command_service.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- test_container_service.py `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- [container_persistence.py](container_persistence.py.md) `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- [test_movement_service.py](test_movement_service.py.md) `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- [test_command_factories_inventory.py](test_command_factories_inventory.py.md) `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- test_command_parser.py `EXTRACTED`
- command_parser.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`

### inherits
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._log_error() `EXTRACTED`

### rationale_for
- Data validation errors (e.g. empty local/whisper message). Log at warning, not… `EXTRACTED`

### uses
- [DatabaseManager](DatabaseManager.md) `INFERRED`
- TestErrorMapping `INFERRED`
- _map_error_type() `INFERRED`
- _get_status_code_for_error() `INFERRED`
- _get_severity_for_error() `INFERRED`
- validate_room_data() `INFERRED`
- [TestErrorHandlers](TestErrorHandlers.md) `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- init_npc_db() `INFERRED`
- _initialize_npc_database() `INFERRED`
- TestValidateRoomData `INFERRED`
- get_npc_database_path() `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- _create_engine_or_raise() `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- TestNPCDatabaseInitialization `INFERRED`
- TestCreateErrorResponse `INFERRED`
- load_database_url() `INFERRED`
- validate_database_url() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*