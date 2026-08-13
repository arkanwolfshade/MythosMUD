# LoggedHTTPException

> God node · 257 connections · `server/exceptions.py`

**Community:** [LoggedHTTPException](LoggedHTTPException.md)

## Connections by Relation

### calls
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- create_character_with_stats() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- _roll_stats_with_profession_preview() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- replay_dlq_message() `EXTRACTED`
- update_room_position() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- _run_set_map_origin() `EXTRACTED`
- get_health_status() `EXTRACTED`
- apply_lucidity_loss() `EXTRACTED`
- select_character() `EXTRACTED`
- _validate_character_access() `EXTRACTED`
- create_npc_definition() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- get_metrics() `EXTRACTED`
- apply_corruption() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- [api/monitoring.py](api-monitoring.py.md) `EXTRACTED`
- test_monitoring_endpoints.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- endpoints.py `EXTRACTED`
- test_endpoints.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- [rooms.py](rooms.py.md) `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- real_time.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
- test_container_exception_handlers.py `EXTRACTED`
- test_containers.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`

### inherits
- LoggedException `EXTRACTED`
- HTTPException `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- HTTPException with automatic logging. This class extends FastAPI's… `EXTRACTED`

### references
- logged_http_exception_handler() `EXTRACTED`
- ._handle_logged_http_exception() `EXTRACTED`
- ._get_logged_http_user_friendly_message() `EXTRACTED`

### uses
- [CircuitBreaker](CircuitBreaker.md) `INFERRED`
- TestErrorMapping `INFERRED`
- ErrorResponse `INFERRED`
- TestSanitization `INFERRED`
- TestErrorHandlers `INFERRED`
- TestCircuitBreaker `INFERRED`
- TestTransferAllItemsFromContainer `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestErrorResponse `INFERRED`
- TestLootAllItems `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestGracefulDegradation `INFERRED`
- _AppStateWithLegacyConfig `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- TestCloseContainer `INFERRED`
- TestHandleLootAllExceptions `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*