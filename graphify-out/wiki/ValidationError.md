# ValidationError

> God node · 524 connections · `server/exceptions.py`

**Community:** [. init ()](_init_%28%29.md)

## Connections by Relation

### calls
- get_database_path() `EXTRACTED`
- handle_exception() `EXTRACTED`
- ._get_rooms_for_movement() `EXTRACTED`
- ._resolve_player_for_movement() `EXTRACTED`
- .test_roll_character_stats_profession_not_found() `EXTRACTED`
- test_apply_lucidity_loss_validation_maps_to_404() `EXTRACTED`
- test_handle_delirium_validation_generic_500() `EXTRACTED`
- test_handle_delirium_validation_lucidity_keyword() `EXTRACTED`
- test_handle_delirium_validation_must_be_delirious() `EXTRACTED`
- test_handle_delirium_validation_not_found() `EXTRACTED`
- test_handle_respawn_validation_generic_500() `EXTRACTED`
- test_handle_respawn_validation_must_be_dead() `EXTRACTED`
- test_handle_respawn_validation_not_found() `EXTRACTED`
- test_create_player_validation_error_to_400() `EXTRACTED`
- test_get_database_path_none_url() `EXTRACTED`
- test_get_engine_raises_validation_error() `EXTRACTED`
- test_get_session_maker_raises_validation_error() `EXTRACTED`
- .test_create_error_response_with_details() `EXTRACTED`
- .test_create_error_response_without_details() `EXTRACTED`
- .test_mythos_exception_handler() `EXTRACTED`

### contains
- exceptions.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- test_container_persistence.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- test_command_factories_inventory.py `EXTRACTED`
- character_creation.py `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_command_parser.py `EXTRACTED`
- command_parser.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`

### indirect_call
- handle_transfer_items_exceptions() `INFERRED`
- create_container() `INFERRED`
- .transfer_from_container() `INFERRED`
- update_container() `INFERRED`
- ._initialize_database() `INFERRED`
- validate_room_data() `INFERRED`
- .open_container() `INFERRED`
- .handle_exception() `INFERRED`
- .transfer_to_container() `INFERRED`
- _weapon_from_prototype_registry() `INFERRED`
- _initialize_npc_database() `INFERRED`
- .lock_container() `INFERRED`
- .unlock_container() `INFERRED`
- _convert_inventory_list_to_inventory_stacks() `INFERRED`
- register_error_handlers() `INFERRED`
- get_npc_database_path() `INFERRED`
- init_npc_db() `INFERRED`
- _seed_new_container_items() `INFERRED`
- update_container_items() `INFERRED`
- create_item_instance_async() `INFERRED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._log_error() `EXTRACTED`

### rationale_for
- Data validation errors (e.g. empty local/whisper message). Log at warning, not e `EXTRACTED`

### uses
- CircuitBreaker `INFERRED`
- ErrorResponse `INFERRED`
- TestErrorMapping `INFERRED`
- TestSanitization `INFERRED`
- DatabaseManager `INFERRED`
- TestErrorHandlers `INFERRED`
- TestCircuitBreaker `INFERRED`
- [Request](Request.md) `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- TestErrorResponse `INFERRED`
- _AppStateWithLegacyConfig `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- ErrorResponseDetailsInput `INFERRED`
- [FastAPI](FastAPI.md) `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestGracefulDegradation `INFERRED`
- _CircuitBreakerResult `INFERRED`
- Exception `INFERRED`
- HTTPException `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*