# LoggedHTTPException

> God node · 358 connections · `server/exceptions.py`

**Community:** [server api players](server_api_players.md)

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
- spawn_npc_instance() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- get_npc_spawn_rules() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- select_character() `EXTRACTED`
- create_dialogue_definition() `EXTRACTED`
- list_dialogue_definitions() `EXTRACTED`
- upsert_dialogue_definition() `EXTRACTED`
- create_npc_definition() `EXTRACTED`
- get_npc_definition() `EXTRACTED`
- get_npc_population_stats() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- api/character_creation.py `EXTRACTED`
- maps.py `EXTRACTED`
- endpoints.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- test_monitoring_endpoints.py `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- legacy_error_handlers.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_legacy_error_handlers.py `EXTRACTED`
- rooms.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- real_time.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- api/player_effects.py `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`

### inherits
- LoggedException `EXTRACTED`
- HTTPException `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- HTTPException with automatic logging. This class extends FastAPI's… `EXTRACTED`

### references
- ._handle_logged_http_exception() `EXTRACTED`
- ._get_logged_http_user_friendly_message() `EXTRACTED`

### uses
- logged_http_exception_handler() `INFERRED`
- TestLootAllItems `INFERRED`
- TestErrorHandlers `INFERRED`
- TestMonitoringEndpoints `INFERRED`
- TestRegisterLootEndpoints `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- register_error_handlers() `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestGetContainerAndPlayerForLootAll `INFERRED`
- TestHelperFunctions `INFERRED`
- TestHandleLootAllExceptions `INFERRED`
- TestHandleOpenContainerExceptions `INFERRED`
- TestCreateCharacterWithStats `INFERRED`
- TestHandleContainerServiceErrorEdgeCases `INFERRED`
- TestHandleContainerServiceError `INFERRED`
- TestCloseContainer `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- test_register_pattern_invalid() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*