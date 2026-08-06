# LoggedHTTPException

> God node · 474 connections · `server/exceptions.py`

**Community:** [services inventory mutation](services_inventory_mutation.md)

## Connections by Relation

### calls
- handle_transfer_items_exceptions() `EXTRACTED`
- handle_open_container_exceptions() `EXTRACTED`
- handle_loot_all_exceptions() `EXTRACTED`
- roll_character_stats() `EXTRACTED`
- handle_close_container_exceptions() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- get_ascii_minimap() `EXTRACTED`
- start_login_grace_period_endpoint() `EXTRACTED`
- update_room_position() `EXTRACTED`
- respawn_player() `EXTRACTED`
- get_npc_definitions() `EXTRACTED`
- get_npc_spawn_rules() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- _roll_stats_with_profession_preview() `EXTRACTED`
- set_map_origin() `EXTRACTED`

### contains
- exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- monitoring.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- test_monitoring_endpoints.py `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- maps.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- character_creation.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- real_time.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`

### indirect_call
- loot_all_items() `INFERRED`
- .handle_exception() `INFERRED`
- register_error_handlers() `INFERRED`
- register_error_handlers() `INFERRED`
- _authenticate_user_credentials() `INFERRED`
- test_login_user_authenticate_raises_exception() `INFERRED`
- test_login_user_authenticate_returns_none() `INFERRED`
- test_login_user_generic_exception() `INFERRED`
- test_login_user_id_mismatch() `INFERRED`
- test_login_user_invalid_credentials() `INFERRED`
- test_login_user_no_email() `INFERRED`
- test_register_user_duplicate_username() `INFERRED`
- test_register_user_email_constraint_violation() `INFERRED`
- test_register_user_generic_constraint_violation() `INFERRED`
- test_register_user_integrity_error() `INFERRED`
- test_register_user_username_constraint_violation() `INFERRED`
- test_register_pattern_invalid() `INFERRED`
- .test_create_character_rate_limit() `INFERRED`
- .test_roll_character_stats_profession_not_found() `INFERRED`
- .test_roll_character_stats_rate_limit() `INFERRED`

### inherits
- LoggedException `EXTRACTED`
- HTTPException `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- HTTPException with automatic logging.      This class extends FastAPI's HTTPExce `EXTRACTED`

### references
- logged_http_exception_handler() `EXTRACTED`
- ._handle_logged_http_exception() `EXTRACTED`
- ._get_logged_http_user_friendly_message() `EXTRACTED`
- _invalid_credentials_exc() `EXTRACTED`

### uses
- CircuitBreaker `INFERRED`
- ErrorResponse `INFERRED`
- TestErrorMapping `INFERRED`
- TestSanitization `INFERRED`
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
- TestTransferAllItemsFromContainer `INFERRED`
- TestGracefulDegradation `INFERRED`
- _CircuitBreakerResult `INFERRED`
- Exception `INFERRED`
- HTTPException `INFERRED`
- TestLootAllItems `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*