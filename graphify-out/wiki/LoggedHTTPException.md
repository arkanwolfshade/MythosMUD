# LoggedHTTPException

> God node · 405 connections · `server/exceptions.py`

**Community:** [Aggressive Mob NPC](Aggressive_Mob_NPC.md)

## Connections by Relation

### calls
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
- _roll_stats_with_profession_preview() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- update_room_position() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- _run_set_map_origin() `EXTRACTED`
- replay_dlq_message() `EXTRACTED`
- _validate_character_access() `EXTRACTED`
- get_health_status() `EXTRACTED`
- apply_lucidity_loss() `EXTRACTED`
- _handle_delirium_respawn_validation_error() `EXTRACTED`
- select_character() `EXTRACTED`
- create_npc_definition() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- _run_coordinate_recalculation() `EXTRACTED`

### contains
- exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- maps.py `EXTRACTED`
- monitoring.py `EXTRACTED`
- test_monitoring_endpoints.py `EXTRACTED`
- character_creation.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- test_endpoints.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- real_time.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
- test_container_exception_handlers.py `EXTRACTED`
- test_containers.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`

### indirect_call
- loot_all_items() `INFERRED`
- .handle_exception() `INFERRED`
- register_error_handlers() `INFERRED`
- register_error_handlers() `INFERRED`
- test_login_user_authenticate_raises_exception() `INFERRED`
- test_login_user_authenticate_returns_none() `INFERRED`
- test_login_user_generic_exception() `INFERRED`
- test_login_user_id_mismatch() `INFERRED`
- test_login_user_no_email() `INFERRED`
- test_register_user_duplicate_username() `INFERRED`
- test_register_user_email_constraint_violation() `INFERRED`
- test_register_user_generic_constraint_violation() `INFERRED`
- test_register_user_integrity_error() `INFERRED`
- test_register_user_username_constraint_violation() `INFERRED`
- .test_create_character_rate_limit() `INFERRED`
- .test_roll_character_stats_profession_not_found() `INFERRED`
- .test_roll_character_stats_rate_limit() `INFERRED`
- .test_loot_all_items_emit_event_failure() `INFERRED`
- .test_loot_all_items_capacity_error() `INFERRED`
- .test_loot_all_items_container_not_found() `INFERRED`

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

### uses
- CircuitBreaker `INFERRED`
- ErrorResponse `INFERRED`
- TestErrorMapping `INFERRED`
- TestSanitization `INFERRED`
- TestErrorHandlers `INFERRED`
- TestCircuitBreaker `INFERRED`
- Request `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- TestTransferAllItemsFromContainer `INFERRED`
- TestHelperFunctions `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestErrorResponse `INFERRED`
- _AppStateWithLegacyConfig `INFERRED`
- TestLootAllItems `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- ErrorResponseDetailsInput `INFERRED`
- FastAPI `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*