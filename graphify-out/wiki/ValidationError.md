# ValidationError

> God node · 249 connections · `server/exceptions.py`

**Community:** [Community 32](Community_32.md)

## Connections by Relation

### calls
- handle_exception() `EXTRACTED`
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
- test_process_command_string_mythos_validation_error() `EXTRACTED`
- .validate_and_get_profession() `EXTRACTED`
- test_handle_validation_error_security_sensitive() `EXTRACTED`
- test_create_character_with_stats_validation_error() `EXTRACTED`
- test_validation_error() `EXTRACTED`
- test_validation_error_initialization() `EXTRACTED`
- test_validation_error_without_field() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- database.py `EXTRACTED`
- players.py `EXTRACTED`
- test_container_service.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- test_command_factories_inventory.py `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_database_error_handling.py `EXTRACTED`
- test_container_persistence_async_helpers.py `EXTRACTED`
- test_command_processor.py `EXTRACTED`
- enhanced_error_logging.py `EXTRACTED`
- test_command_service.py `EXTRACTED`
- api/player_effects.py `EXTRACTED`
- admin_summon_command.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`
- ._log_error() `EXTRACTED`

### rationale_for
- Data validation errors (e.g. empty local/whisper message). Log at warning, not… `EXTRACTED`

### uses
- DatabaseManager `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestValidateRoomData `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- _create_engine_or_raise() `INFERRED`
- TestNPCDatabaseInitialization `INFERRED`
- load_database_url() `INFERRED`
- validate_database_url() `INFERRED`
- test_respawn_player_from_delirium_not_found() `INFERRED`
- test_respawn_player_not_found() `INFERRED`
- test_respawn_player_validation_error() `INFERRED`
- test_resolve_player_username_error() `INFERRED`
- test_get_database_path_none_url_raises() `INFERRED`
- test_get_database_path_unsupported_raises() `INFERRED`
- test_initialize_database_config_runtime_error() `INFERRED`
- test_initialize_database_config_validation_error() `INFERRED`
- test_initialize_database_none_url() `INFERRED`
- test_initialize_database_type_error() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*