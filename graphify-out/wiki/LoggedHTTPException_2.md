# LoggedHTTPException

> God node · 369 connections · `server/exceptions.py`

**Community:** [LoggedHTTPException](LoggedHTTPException.md)

## Connections by Relation

### calls
- create_character_with_stats() `EXTRACTED`
- create_room_exit() `EXTRACTED`
- get_player_id_from_user() `EXTRACTED`
- handle_container_service_error() `EXTRACTED`
- update_room() `EXTRACTED`
- update_room_exit() `EXTRACTED`
- get_player_quests() `EXTRACTED`
- get_container_and_player_for_loot_all() `EXTRACTED`
- delete_room_exit() `EXTRACTED`
- _update_npc_definition_internal() `EXTRACTED`
- _start_login_grace_period_body() `EXTRACTED`
- update_room_position() `EXTRACTED`
- get_npc_definitions() `EXTRACTED`
- spawn_npc_instance() `EXTRACTED`
- create_npc_spawn_rule() `EXTRACTED`
- get_npc_spawn_rules() `EXTRACTED`
- validate_character_stats() `EXTRACTED`
- delete_player() `EXTRACTED`
- get_player() `EXTRACTED`
- select_character() `EXTRACTED`

### contains
- server/exceptions.py `EXTRACTED`

### imports
- players.py `EXTRACTED`
- [api/character_creation.py](api-character_creation.py.md) `EXTRACTED`
- [maps.py](maps.py.md) `EXTRACTED`
- endpoints.py `EXTRACTED`
- [api/monitoring.py](api-monitoring.py.md) `EXTRACTED`
- rooms.py `EXTRACTED`
- [test_players_api_coverage.py](test_players_api_coverage.py.md) `EXTRACTED`
- test_monitoring_endpoints.py `EXTRACTED`
- test_maps.py `EXTRACTED`
- test_container_helpers.py `EXTRACTED`
- test_rooms_write_api.py `EXTRACTED`
- [test_exceptions.py](test_exceptions.py.md) `EXTRACTED`
- api/container_helpers.py `EXTRACTED`
- [real_time.py](real_time.py.md) `EXTRACTED`
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) `EXTRACTED`
- [test_real_time_helpers.py](test_real_time_helpers.py.md) `EXTRACTED`
- api/player_effects.py `EXTRACTED`
- test_exceptions_comprehensive.py `EXTRACTED`
- standardized_responses.py `EXTRACTED`
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
- TestLootAllItems `INFERRED`
- TestMonitoringEndpoints `INFERRED`
- TestRegisterLootEndpoints `INFERRED`
- TestRollCharacterStats `INFERRED`
- TestHandleTransferItemsExceptions `INFERRED`
- TestOpenContainer `INFERRED`
- TestTransferItems `INFERRED`
- TestGetContainerAndPlayerForLootAll `INFERRED`
- [TestHelperFunctions](TestHelperFunctions.md) `INFERRED`
- test_create_room_exit_duplicate_direction_409() `INFERRED`
- TestHandleLootAllExceptions `INFERRED`
- TestHandleOpenContainerExceptions `INFERRED`
- test_apply_lucidity_loss_validation_maps_to_404() `INFERRED`
- test_create_room_exit_source_room_missing_404() `INFERRED`
- test_create_room_exit_target_room_missing_404() `INFERRED`
- test_update_room_exit_not_found_404() `INFERRED`
- TestCreateCharacterWithStats `INFERRED`
- TestHandleContainerServiceErrorEdgeCases `INFERRED`
- TestHandleContainerServiceError `INFERRED`
- TestCloseContainer `INFERRED`

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*