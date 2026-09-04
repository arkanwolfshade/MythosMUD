# LoggedHTTPException

> God node · 235 connections · `server/exceptions.py`

**Community:** [Test Auth Dependencies](Test_Auth_Dependencies.md)

## Connections by Relation

### calls
- create_character_with_stats() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- get_system_metrics() `EXTRACTED`
- create_dialogue_definition() `EXTRACTED`
- list_dialogue_definitions() `EXTRACTED`
- upsert_dialogue_definition() `EXTRACTED`
- get_npc_population_stats() `EXTRACTED`
- replay_dlq_message() `EXTRACTED`
- get_dialogue_definition() `EXTRACTED`
- get_admin_sessions() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- get_health_status() `EXTRACTED`
- delete_dialogue_definition() `EXTRACTED`
- create_npc_definition() `EXTRACTED`
- spawn_npc_instance() `EXTRACTED`
- get_npc_system_status() `EXTRACTED`
- get_npc_zone_stats() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- api/character_creation.py `EXTRACTED`
- api/monitoring.py `EXTRACTED`
- test_monitoring_endpoints.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_rooms_write_api.py `EXTRACTED`
- test_exceptions.py `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- test_metrics_endpoints.py `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
- npc_definitions_api.py `EXTRACTED`
- container_endpoints_loot.py `EXTRACTED`
- api/metrics.py `EXTRACTED`
- test_standardized_responses.py `EXTRACTED`
- test_error_handling_middleware.py `EXTRACTED`
- npc_instances_api.py `EXTRACTED`
- api/player_respawn.py `EXTRACTED`
- test_containers.py `EXTRACTED`
- dialogue_definitions_api.py `EXTRACTED`

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
- TestLootAllItems `INFERRED`
- TestMonitoringEndpoints `INFERRED`
- TestRegisterLootEndpoints `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestGetContainerAndPlayerForLootAll `INFERRED`
- TestHelperFunctions `INFERRED`
- test_create_room_exit_duplicate_direction_409() `INFERRED`
- TestHandleLootAllExceptions `INFERRED`
- TestHandleOpenContainerExceptions `INFERRED`
- test_create_room_exit_source_room_missing_404() `INFERRED`
- test_create_room_exit_target_room_missing_404() `INFERRED`
- test_update_room_exit_not_found_404() `INFERRED`
- TestCreateCharacterWithStats `INFERRED`
- TestHandleContainerServiceErrorEdgeCases `INFERRED`
- TestHandleContainerServiceError `INFERRED`
- TestCloseContainer `INFERRED`
- test_delete_room_exit_not_found_404() `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*