# ValidationError

> God node · 182 connections · `server/exceptions.py`

**Community:** [get_logger](get_logger.md)

## Connections by Relation

### calls
- get_database_path() `EXTRACTED`
- handle_exception() `EXTRACTED`
- ._get_rooms_for_movement() `EXTRACTED`
- ._resolve_player_for_movement() `EXTRACTED`
- .test_roll_character_stats_profession_not_found() `EXTRACTED`
- test_apply_lucidity_loss_validation_maps_to_404() `EXTRACTED`
- .test_mythos_exception_handler_sets_request_id() `EXTRACTED`
- test_respawn_player_from_delirium_not_found() `EXTRACTED`
- test_respawn_player_not_found() `EXTRACTED`
- test_respawn_player_validation_error() `EXTRACTED`
- test_create_player_validation_error_to_400() `EXTRACTED`
- test_delete_player_validation_error() `EXTRACTED`
- test_get_database_path_none_url() `EXTRACTED`
- test_close_db_engine_initialization_failure() `EXTRACTED`
- test_get_engine_raises_validation_error() `EXTRACTED`
- test_get_session_maker_raises_validation_error() `EXTRACTED`
- .test_mythos_exception_handler() `EXTRACTED`
- .test_mythos_exception_handler_with_debug() `EXTRACTED`
- test_handle_delirium_validation_generic_500() `EXTRACTED`
- test_handle_delirium_validation_lucidity_keyword() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- test_container_service.py `EXTRACTED`
- [persistence/container_persistence.py](persistence-container_persistence.py.md) `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- [test_command_factories_utility.py](test_command_factories_utility.py.md) `EXTRACTED`
- [test_movement_service.py](test_movement_service.py.md) `EXTRACTED`
- [inventory_command_helpers.py](inventory_command_helpers.py.md) `EXTRACTED`
- [test_command_factories_exploration.py](test_command_factories_exploration.py.md) `EXTRACTED`
- test_command_factories_inventory.py `EXTRACTED`
- player_service.py `EXTRACTED`
- [test_database_helpers.py](test_database_helpers.py.md) `EXTRACTED`
- command_parser.py `EXTRACTED`
- [test_command_parser.py](test_command_parser.py.md) `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`
- [test_exceptions.py](test_exceptions.py.md) `EXTRACTED`

### inherits
- [MythosMUDError](MythosMUDError.md) `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._log_error() `EXTRACTED`

### rationale_for
- Data validation errors (e.g. empty local/whisper message). Log at warning, not… `EXTRACTED`

### uses
- [CircuitBreaker](CircuitBreaker.md) `INFERRED`
- TestErrorMapping `INFERRED`
- ErrorResponse `INFERRED`
- TestSanitization `INFERRED`
- TestErrorHandlers `INFERRED`
- DatabaseManager `INFERRED`
- TestCircuitBreaker `INFERRED`
- TestErrorResponse `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- TestGracefulDegradation `INFERRED`
- _AppStateWithLegacyConfig `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestGetRoomEnvironment `INFERRED`
- TestHandleLootAllExceptions `INFERRED`
- TestHandleOpenContainerExceptions `INFERRED`
- TestValidateRoomData `INFERRED`
- TestCreateCharacterWithStats `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*