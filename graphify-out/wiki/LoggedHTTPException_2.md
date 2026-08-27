# LoggedHTTPException

> God node · 271 connections · `server/exceptions.py`

**Community:** [NPCSpawningService](NPCSpawningService.md)

## Connections by Relation

### calls
- create_character_with_stats() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
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
- replay_dlq_message() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- test_players_api_coverage.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- [api/player_effects.py](api-player_effects.py.md) `EXTRACTED`
- test_npc_definitions_api.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- [subject_controller.py](subject_controller.py.md) `EXTRACTED`
- api/metrics.py `EXTRACTED`
- test_player_effects_endpoints.py `EXTRACTED`
- test_standardized_responses.py `EXTRACTED`
- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) `EXTRACTED`
- npc_instances_api.py `EXTRACTED`

### inherits
- LoggedException `EXTRACTED`
- HTTPException `EXTRACTED`

### method
- .__init__() `EXTRACTED`

### rationale_for
- HTTPException with automatic logging. This class extends FastAPI's… `EXTRACTED`

### uses
- TestLootAllItems `INFERRED`
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) `INFERRED`
- TestRegisterLootEndpoints `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestGetContainerAndPlayerForLootAll `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- TestHandleLootAllExceptions `INFERRED`
- TestHandleOpenContainerExceptions `INFERRED`
- TestCreateCharacterWithStats `INFERRED`
- TestHandleContainerServiceErrorEdgeCases `INFERRED`
- TestHandleContainerServiceError `INFERRED`
- TestCloseContainer `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- test_register_pattern_invalid() `INFERRED`
- TestExceptionChaining `INFERRED`
- TestExceptionHandlerContext `INFERRED`
- TestExceptionHandlerLoggerCalls `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*