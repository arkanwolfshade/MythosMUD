# ValidationError

> God node · 189 connections · `server/exceptions.py`

**Community:** [[NPC Admin API]]

## Connections by Relation

### calls
- [[get_database_path()]] `EXTRACTED`
- [[handle_exception()]] `EXTRACTED`
- [[._get_rooms_for_movement()]] `EXTRACTED`
- [[._resolve_player_for_movement()]] `EXTRACTED`
- [[.test_roll_character_stats_profession_not_found()]] `EXTRACTED`
- [[test_apply_lucidity_loss_validation_maps_to_404()]] `EXTRACTED`
- [[.test_mythos_exception_handler_sets_request_id()]] `EXTRACTED`
- [[test_handle_delirium_validation_generic_500()]] `EXTRACTED`
- [[test_handle_delirium_validation_lucidity_keyword()]] `EXTRACTED`
- [[test_handle_delirium_validation_must_be_delirious()]] `EXTRACTED`
- [[test_handle_delirium_validation_not_found()]] `EXTRACTED`
- [[test_handle_respawn_validation_generic_500()]] `EXTRACTED`
- [[test_handle_respawn_validation_must_be_dead()]] `EXTRACTED`
- [[test_handle_respawn_validation_not_found()]] `EXTRACTED`
- [[test_create_player_validation_error_to_400()]] `EXTRACTED`
- [[test_parse_command_string_validation_error()]] `EXTRACTED`
- [[test_get_database_path_none_url()]] `EXTRACTED`
- [[test_close_db_engine_initialization_failure()]] `EXTRACTED`
- [[test_get_engine_raises_validation_error()]] `EXTRACTED`
- [[test_get_session_maker_raises_validation_error()]] `EXTRACTED`

### contains
- [[exceptions.py]] `EXTRACTED`

### imports
- [[command_service.py]] `EXTRACTED`
- [[database.py]] `EXTRACTED`
- [[players.py]] `EXTRACTED`
- [[test_container_persistence.py]] `EXTRACTED`
- [[test_player_service.py]] `EXTRACTED`
- [[test_container_persistence_extended_row_helpers.py]] `EXTRACTED`
- [[container_persistence.py]] `EXTRACTED`
- [[test_command_factories_utility.py]] `EXTRACTED`
- [[legacy_error_handlers.py]] `EXTRACTED`
- [[character_creation.py]] `EXTRACTED`
- [[test_command_factories_inventory.py]] `EXTRACTED`
- [[test_database_helpers.py]] `EXTRACTED`
- [[test_command_factories_exploration.py]] `EXTRACTED`
- [[test_database_extended.py]] `EXTRACTED`
- [[test_exceptions.py]] `EXTRACTED`
- [[test_command_parser.py]] `EXTRACTED`
- [[test_database_error_handling.py]] `EXTRACTED`
- [[test_legacy_error_handlers.py]] `EXTRACTED`
- [[inventory_command_helpers.py]] `EXTRACTED`
- [[command_parser.py]] `EXTRACTED`

### inherits
- [[MythosMUDError]] `EXTRACTED`

### method
- [[.__init__()]] `EXTRACTED`
- [[._log_error()]] `EXTRACTED`

### rationale_for
- [[Data validation errors (e.g. empty local/whisper message). Log at warning, not e]] `EXTRACTED`

### uses
- [[CircuitBreaker]] `INFERRED`
- [[ErrorResponse]] `INFERRED`
- [[TestErrorMapping]] `INFERRED`
- [[TestSanitization]] `INFERRED`
- [[DatabaseManager]] `INFERRED`
- [[TestErrorHandlers]] `INFERRED`
- [[TestCircuitBreaker]] `INFERRED`
- [[JSONResponse]] `INFERRED`
- [[MythosMUDError]] `INFERRED`
- [[Request]] `INFERRED`
- [[TestErrorResponse]] `INFERRED`
- [[_AppStateWithLegacyConfig]] `INFERRED`
- [[_AppWithLegacyConfigState]] `INFERRED`
- [[FastAPI]] `INFERRED`
- [[HTTPException]] `INFERRED`
- [[TestCreateErrorResponse]] `INFERRED`
- [[TestLegacyHandlerSecurity]] `INFERRED`
- [[TestHandleTransferItemsExceptions]] `INFERRED`
- [[ErrorResponseDetailsInput]] `INFERRED`
- [[ErrorSeverity]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
