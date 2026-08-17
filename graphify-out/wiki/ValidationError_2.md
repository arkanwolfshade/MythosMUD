# ValidationError

> God node · 337 connections · `server/exceptions.py`

**Community:** [ValidationError](ValidationError.md)

## Connections by Relation

### calls
- handle_exception() `EXTRACTED`
- ._get_rooms_for_movement() `EXTRACTED`
- ._resolve_player_for_movement() `EXTRACTED`
- .test_roll_character_stats_profession_not_found() `EXTRACTED`
- .test_mythos_exception_handler_sets_request_id() `EXTRACTED`
- .test_mythos_exception_handler() `EXTRACTED`
- .test_mythos_exception_handler_with_debug() `EXTRACTED`
- .test_create_error_response_sanitizes_unsafe_keys() `EXTRACTED`
- .test_create_error_response_with_details() `EXTRACTED`
- .test_create_error_response_without_details() `EXTRACTED`
- .test_get_status_code_for_error_validation() `EXTRACTED`
- .test_map_error_type_validation() `EXTRACTED`
- .validate_and_get_profession() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- [command_service.py](command_service.py.md) `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- test_container_service.py `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- [persistence/container_persistence.py](persistence-container_persistence.py.md) `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_movement_service.py `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- player_service.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- test_command_factories_inventory.py `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- [test_command_parser.py](test_command_parser.py.md) `EXTRACTED`
- command_parser.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- [test_database_extended.py](test_database_extended.py.md) `EXTRACTED`
- test_exceptions.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

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
- get_database_path() `INFERRED`
- validate_room_data() `INFERRED`
- TestErrorHandlers `INFERRED`
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

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*