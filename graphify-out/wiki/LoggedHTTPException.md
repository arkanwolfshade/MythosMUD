# LoggedHTTPException

> God node · 261 connections · `server/exceptions.py`

**Community:** [[Container Exception Handlers]]

## Connections by Relation

### calls
- [[handle_transfer_items_exceptions()]] `EXTRACTED`
- [[roll_character_stats()]] `EXTRACTED`
- [[handle_open_container_exceptions()]] `EXTRACTED`
- [[handle_close_container_exceptions()]] `EXTRACTED`
- [[handle_loot_all_exceptions()]] `EXTRACTED`
- [[get_player_id_from_user()]] `EXTRACTED`
- [[handle_container_service_error()]] `EXTRACTED`
- [[create_character_with_stats()]] `EXTRACTED`
- [[get_container_and_player_for_loot_all()]] `EXTRACTED`
- [[_execute_create_character()]] `EXTRACTED`
- [[_roll_stats_with_profession_preview()]] `EXTRACTED`
- [[get_player_quests()]] `EXTRACTED`
- [[start_login_grace_period_endpoint()]] `EXTRACTED`
- [[update_room_position()]] `EXTRACTED`
- [[validate_character_stats()]] `EXTRACTED`
- [[replay_dlq_message()]] `EXTRACTED`
- [[_validate_character_access()]] `EXTRACTED`
- [[_update_npc_definition_internal()]] `EXTRACTED`
- [[get_health_status()]] `EXTRACTED`
- [[apply_lucidity_loss()]] `EXTRACTED`

### contains
- [[exceptions.py]] `EXTRACTED`

### imports
- [[players.py]] `EXTRACTED`
- [[monitoring.py]] `EXTRACTED`
- [[test_monitoring_endpoints.py]] `EXTRACTED`
- [[maps.py]] `EXTRACTED`
- [[endpoints.py]] `EXTRACTED`
- [[test_endpoints.py]] `EXTRACTED`
- [[legacy_error_handlers.py]] `EXTRACTED`
- [[character_creation.py]] `EXTRACTED`
- [[test_exceptions.py]] `EXTRACTED`
- [[container_helpers.py]] `EXTRACTED`
- [[test_legacy_error_handlers.py]] `EXTRACTED`
- [[test_container_helpers.py]] `EXTRACTED`
- [[container_endpoints_loot.py]] `EXTRACTED`
- [[test_metrics_endpoints.py]] `EXTRACTED`
- [[test_exceptions_comprehensive.py]] `EXTRACTED`
- [[rooms.py]] `EXTRACTED`
- [[real_time.py]] `EXTRACTED`
- [[standardized_responses.py]] `EXTRACTED`
- [[npc_definitions_api.py]] `EXTRACTED`
- [[player_effects.py]] `EXTRACTED`

### inherits
- [[LoggedException]] `EXTRACTED`
- [[HTTPException]] `EXTRACTED`

### method
- [[.__init__()]] `EXTRACTED`

### rationale_for
- [[HTTPException with automatic logging.      This class extends FastAPI's HTTPExce]] `EXTRACTED`

### uses
- [[CircuitBreaker]] `INFERRED`
- [[ErrorResponse]] `INFERRED`
- [[TestErrorMapping]] `INFERRED`
- [[TestSanitization]] `INFERRED`
- [[TestErrorHandlers]] `INFERRED`
- [[TestCircuitBreaker]] `INFERRED`
- [[JSONResponse]] `INFERRED`
- [[MythosMUDError]] `INFERRED`
- [[Request]] `INFERRED`
- [[TestTransferAllItemsFromContainer]] `INFERRED`
- [[TestHelperFunctions]] `INFERRED`
- [[TestOpenContainer]] `INFERRED`
- [[TestTransferItems]] `INFERRED`
- [[TestErrorResponse]] `INFERRED`
- [[TestLootAllItems]] `INFERRED`
- [[_AppStateWithLegacyConfig]] `INFERRED`
- [[_AppWithLegacyConfigState]] `INFERRED`
- [[FastAPI]] `INFERRED`
- [[HTTPException]] `INFERRED`
- [[TestCreateErrorResponse]] `INFERRED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
