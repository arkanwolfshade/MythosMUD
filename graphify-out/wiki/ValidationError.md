# ValidationError

> God node · 582 connections · `server/exceptions.py`

**Community:** [add used user](add_used_user.md)

## Connections by Relation

### calls
- get_database_path() `EXTRACTED`
- handle_exception() `EXTRACTED`
- ._get_rooms_for_movement() `EXTRACTED`
- ._resolve_player_for_movement() `EXTRACTED`
- .test_roll_character_stats_profession_not_found() `EXTRACTED`
- test_apply_lucidity_loss_validation_maps_to_404() `EXTRACTED`
- test_respawn_player_from_delirium_not_found() `EXTRACTED`
- test_respawn_player_not_found() `EXTRACTED`
- test_respawn_player_validation_error() `EXTRACTED`
- test_handle_delirium_validation_generic_500() `EXTRACTED`
- test_handle_delirium_validation_lucidity_keyword() `EXTRACTED`
- test_handle_delirium_validation_must_be_delirious() `EXTRACTED`
- test_handle_delirium_validation_not_found() `EXTRACTED`
- test_handle_respawn_validation_generic_500() `EXTRACTED`
- test_handle_respawn_validation_must_be_dead() `EXTRACTED`
- test_handle_respawn_validation_not_found() `EXTRACTED`
- test_create_player_validation_error_to_400() `EXTRACTED`
- test_delete_player_validation_error() `EXTRACTED`
- test_get_database_path_none_url() `EXTRACTED`
- test_get_engine_raises_validation_error() `EXTRACTED`

### contains
- exceptions.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- database.py `EXTRACTED`
- test_container_service.py `EXTRACTED`
- players.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- test_command_factories_inventory.py `EXTRACTED`
- character_creation.py `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- command_parser.py `EXTRACTED`
- player_service.py `EXTRACTED`
- test_command_parser.py `EXTRACTED`
- test_movement_service.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`

### indirect_call
- handle_transfer_items_exceptions() `INFERRED`
- ._initialize_database() `INFERRED`
- validate_room_data() `INFERRED`
- .handle_exception() `INFERRED`
- register_error_handlers() `INFERRED`
- create_item_instance_async() `INFERRED`
- _execute_movement() `INFERRED`
- _weapon_from_prototype_registry() `INFERRED`
- _initialize_npc_database() `INFERRED`
- _populate_container_items_async() `INFERRED`
- create_item_instance() `INFERRED`
- _convert_inventory_list_to_inventory_stacks() `INFERRED`
- get_npc_database_path() `INFERRED`
- init_npc_db() `INFERRED`
- _seed_new_container_items() `INFERRED`
- .open_container() `INFERRED`
- update_container_items() `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- .create_player_with_stats() `INFERRED`
- .delete_player() `INFERRED`

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
- Request `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- TestErrorResponse `INFERRED`
- _AppStateWithLegacyConfig `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- ErrorResponseDetailsInput `INFERRED`
- FastAPI `INFERRED`
- TestGracefulDegradation `INFERRED`
- _CircuitBreakerResult `INFERRED`
- Exception `INFERRED`
- HTTPException `INFERRED`
- TestRollCharacterStats `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*