# LoggedHTTPException

> God node · 283 connections · `server/exceptions.py`

**Community:** [LoggedHTTPException](LoggedHTTPException.md)

## Connections by Relation

### calls
- create_character_with_stats() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
- update_room_position() `EXTRACTED`
- get_npc_definitions() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- get_npc_spawn_rules() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- select_character() `EXTRACTED`
- create_dialogue_definition() `EXTRACTED`
- list_dialogue_definitions() `EXTRACTED`
- upsert_dialogue_definition() `EXTRACTED`
- create_npc_definition() `EXTRACTED`
- get_npc_definition() `EXTRACTED`
- spawn_npc_instance() `EXTRACTED`
- get_npc_population_stats() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- maps.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- [test_monitoring_endpoints.py](test_monitoring_endpoints.py.md) `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- [test_maps.py](test_maps.py.md) `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- [test_exceptions.py](test_exceptions.py.md) `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) `EXTRACTED`
- [real_time.py](real_time.py.md) `EXTRACTED`
- rooms.py `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
- [api/player_effects.py](api-player_effects.py.md) `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`

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
- _invalid_credentials_exc() `EXTRACTED`

### uses
- [CircuitBreaker](CircuitBreaker.md) `INFERRED`
- TestErrorMapping `INFERRED`
- ErrorResponse `INFERRED`
- TestSanitization `INFERRED`
- TestErrorHandlers `INFERRED`
- TestCircuitBreaker `INFERRED`
- TestErrorResponse `INFERRED`
- TestCreateErrorResponse `INFERRED`
- TestLegacyHandlerSecurity `INFERRED`
- TestTransferAllItemsFromContainer `INFERRED`
- TestGracefulDegradation `INFERRED`
- _AppStateWithLegacyConfig `INFERRED`
- _AppWithLegacyConfigState `INFERRED`
- TestLootAllItems `INFERRED`
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestRegisterLootEndpoints `INFERRED`
- TestRollCharacterStats `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*