# ValidationError

> God node · 327 connections · `server/exceptions.py`

**Community:** [Schema Validation & Channels](Schema_Validation_&_Channels.md)

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
- test_handle_validation_error_security_sensitive() `EXTRACTED`
- test_parse_command_string_validation_error() `EXTRACTED`
- .validate_and_get_profession() `EXTRACTED`
- test_create_character_with_stats_validation_error() `EXTRACTED`
- test_validation_error() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- command_service.py `EXTRACTED`
- database.py `EXTRACTED`
- test_container_service.py `EXTRACTED`
- test_command_factories_inventory.py `EXTRACTED`
- test_movement_service.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- players.py `EXTRACTED`
- test_command_factories_utility.py `EXTRACTED`
- test_container_persistence_extended_row_helpers.py `EXTRACTED`
- inventory_command_helpers.py `EXTRACTED`
- command_parser.py `EXTRACTED`
- test_command_parser.py `EXTRACTED`
- player_service.py `EXTRACTED`
- container_persistence.py `EXTRACTED`
- test_command_factories_exploration.py `EXTRACTED`
- test_container_persistence_async_helpers.py `EXTRACTED`
- test_player_service_mutations.py `EXTRACTED`
- test_database_helpers.py `EXTRACTED`
- test_database_extended.py `EXTRACTED`

### inherits
- MythosMUDError `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- Data validation errors (e.g. empty local/whisper message). Log at warning, not… `EXTRACTED`

### references
- ._handle_pydantic_validation_error() `EXTRACTED`
- _handle_validation_error() `EXTRACTED`

### uses
- DatabaseManager `INFERRED`
- SpellEffects `INFERRED`
- validate_room_data() `INFERRED`
- _initialize_npc_database() `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestValidateRoomData `INFERRED`
- init_npc_db() `INFERRED`
- get_npc_database_path() `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- TestNPCDatabaseInitialization `INFERRED`
- fetch_user_by_username_case_insensitive() `INFERRED`
- _create_engine_or_raise() `INFERRED`
- test_respawn_player_from_delirium_not_found() `INFERRED`
- test_respawn_player_not_found() `INFERRED`
- test_respawn_player_validation_error() `INFERRED`
- test_create_player_validation_error_to_400() `INFERRED`
- test_delete_player_validation_error() `INFERRED`
- test_resolve_player_username_error() `INFERRED`
- test_get_database_path_none_url_raises() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*