# Test Suite Migration File Mapping

> *Complete mapping of all 204 test files from current flat structure to new hierarchical organization*

## Migration Status Legend

⏳ **Pending**: Not yet started

- 🔄 **In Progress**: Currently being migrated
- ✅ **Complete**: Successfully migrated and validated
- 🔀 **Merged**: Consolidated with another test file
- 🗑️ **Removed**: Obsolete or duplicate, removed

## Complete File Mapping

### Fixtures and Utilities

| Current Location                      | New Location                             | Status | Notes                            |
| ------------------------------------- | ---------------------------------------- | ------ | -------------------------------- |
| `mock_data.py`                        | `fixtures/mock_data.py`                  | ⏳      | Shared mock data generators      |
| `utils/test_environment.py`           | `fixtures/test_environment.py`           | ⏳      | Test environment utilities       |
| `utils/test_error_logging.py`         | `fixtures/test_error_logging.py`         | ⏳      | Error logging test utilities     |
| `utils/risk_mitigation.py`            | `fixtures/risk_mitigation.py`            | ⏳      | Risk mitigation utilities        |
| `utils/success_criteria_validator.py` | `fixtures/success_criteria_validator.py` | ⏳      | Success validation utilities     |
| `init_test_db.py`                     | `scripts/init_test_db.py`                | ⏳      | Test database initialization     |
| `init_npc_test_db.py`                 | `scripts/init_npc_test_db.py`            | ⏳      | NPC test database initialization |
| `verify_test_db.py`                   | `scripts/verify_test_db.py`              | ⏳      | Test database verification       |

### Unit Tests - Infrastructure

| Current Location                         | New Location                                       | Status | Notes                                   |
| ---------------------------------------- | -------------------------------------------------- | ------ | --------------------------------------- |
| `test_config.py`                         | `unit/infrastructure/test_config.py`               | ⏳      | Configuration tests                     |
| `test_database.py`                       | `unit/infrastructure/test_database.py`             | ⏳      | Database core tests                     |
| `test_app_factory.py`                    | `unit/infrastructure/test_app_factory.py`          | ⏳      | App factory pattern tests               |
| `test_app_lifespan.py`                   | `unit/infrastructure/test_lifespan.py`             | ⏳      | App lifespan tests                      |
| `test_lifespan.py`                       | `unit/infrastructure/test_lifespan.py`             | 🔀      | Merge with test_app_lifespan.py         |
| `test_main.py`                           | `unit/infrastructure/test_main.py`                 | ⏳      | Main app entry point tests              |
| `test_exceptions.py`                     | `unit/infrastructure/test_exceptions.py`           | ⏳      | Exception handling tests                |
| `test_dependency_injection.py`           | `unit/infrastructure/test_dependency_injection.py` | ⏳      | DI framework tests                      |
| `test_dependency_injection_functions.py` | `unit/infrastructure/test_dependency_injection.py` | 🔀      | Merge with test_dependency_injection.py |
| `test_dependency_functions.py`           | `unit/infrastructure/test_dependency_injection.py` | 🔀      | Merge with test_dependency_injection.py |
| `test_request_context.py`                | `unit/infrastructure/test_request_context.py`      | ⏳      | Request context tests                   |

### Unit Tests - API Layer

| Current Location                        | New Location                                 | Status | Notes                                       |
| --------------------------------------- | -------------------------------------------- | ------ | ------------------------------------------- |
| `test_api_base.py`                      | `unit/api/test_base.py`                      | ⏳      | Base API functionality                      |
| `test_api_players.py`                   | `unit/api/test_players.py`                   | ⏳      | Player API endpoints                        |
| `test_api_professions.py`               | `unit/api/test_professions.py`               | ⏳      | Profession API endpoints                    |
| `test_api_real_time.py`                 | `unit/api/test_real_time.py`                 | ⏳      | Real-time API endpoints                     |
| `test_health_endpoint.py`               | `unit/api/test_health_endpoints.py`          | ⏳      | Health check endpoints                      |
| `test_monitoring_api_endpoints.py`      | `unit/api/test_monitoring_endpoints.py`      | ⏳      | Monitoring API endpoints                    |
| `test_monitoring_api.py`                | `unit/api/test_monitoring_endpoints.py`      | 🔀      | Merge with test_monitoring_api_endpoints.py |
| `test_api_endpoints_dual_connection.py` | `unit/api/test_dual_connection_endpoints.py` | ⏳      | Dual connection API endpoints               |

### Unit Tests - Commands

| Current Location                  | New Location                                 | Status | Notes                              |
| --------------------------------- | -------------------------------------------- | ------ | ---------------------------------- |
| `test_command_handler.py`         | `unit/commands/test_command_handler.py`      | ⏳      | Core command handler               |
| `test_command_handler_v2.py`      | `unit/commands/test_command_handler.py`      | 🔀      | Merge with test_command_handler.py |
| `test_command_handler_unified.py` | `unit/commands/test_command_handler.py`      | 🔀      | Merge with test_command_handler.py |
| `test_unified_command_handler.py` | `unit/commands/test_command_handler.py`      | 🔀      | Merge with test_command_handler.py |
| `test_command_validation.py`      | `unit/commands/test_command_validation.py`   | ⏳      | Command validation logic           |
| `test_command_rate_limiter.py`    | `unit/commands/test_command_rate_limiter.py` | ⏳      | Command rate limiting              |
| `test_admin_teleport_commands.py` | `unit/commands/test_admin_commands.py`       | ⏳      | Admin command handlers             |
| `test_admin_actions_logger.py`    | `unit/logging/test_admin_actions_logger.py`  | ⏳      | Admin action logging               |
| `test_utility_commands.py`        | `unit/commands/test_utility_commands.py`     | ⏳      | Utility commands (help, who, etc.) |
| `test_system_commands.py`         | `unit/commands/test_system_commands.py`      | ⏳      | System commands                    |

### Unit Tests - Chat/Communication

| Current Location                                         | New Location                                  | Status | Notes                                              |
| -------------------------------------------------------- | --------------------------------------------- | ------ | -------------------------------------------------- |
| `test_chat_service.py`                                   | `unit/chat/test_chat_service.py`              | ⏳      | Core chat service                                  |
| `test_chat_logger.py`                                    | `unit/logging/test_chat_logger.py`            | ⏳      | Chat logging                                       |
| `test_emote_service.py`                                  | `unit/chat/test_emote_service.py`             | ⏳      | Emote service                                      |
| `test_emote_mute_filtering.py`                           | `unit/chat/test_emote_filtering.py`           | ⏳      | Emote mute filtering                               |
| `test_emote_types_mute_filtering.py`                     | `unit/chat/test_emote_filtering.py`           | 🔀      | Merge with test_emote_mute_filtering.py            |
| `test_whisper_channel.py`                                | `unit/chat/test_whisper_channel.py`           | ⏳      | Whisper channel                                    |
| `test_local_channel.py`                                  | `unit/chat/test_local_channel.py`             | ⏳      | Local channel                                      |
| `test_local_channel_commands.py`                         | `unit/chat/test_local_channel.py`             | 🔀      | Merge with test_local_channel.py                   |
| `test_local_channel_logging.py`                          | `unit/logging/test_local_channel_logging.py`  | ⏳      | Local channel logging                              |
| `test_global_channel_commands.py`                        | `unit/chat/test_global_channel.py`            | ⏳      | Global channel commands                            |
| `test_global_channel_logging.py`                         | `unit/logging/test_global_channel_logging.py` | ⏳      | Global channel logging                             |
| `test_system_channel.py`                                 | `unit/chat/test_system_channel.py`            | ⏳      | System channel                                     |
| `test_channel_broadcasting_strategies.py`                | `unit/chat/test_broadcasting_strategies.py`   | ⏳      | Broadcasting strategies                            |
| `test_channel_broadcasting_strategies_implementation.py` | `unit/chat/test_broadcasting_strategies.py`   | 🔀      | Merge with test_channel_broadcasting_strategies.py |

### Unit Tests - Player Management

| Current Location                           | New Location                                | Status | Notes                              |
| ------------------------------------------ | ------------------------------------------- | ------ | ---------------------------------- |
| `test_player_service.py`                   | `unit/player/test_player_service.py`        | ⏳      | Player service layer               |
| `test_player_service_layer.py`             | `unit/player/test_player_service.py`        | 🔀      | Merge with test_player_service.py  |
| `test_player_stats.py`                     | `unit/player/test_player_stats.py`          | ⏳      | Player statistics                  |
| `test_player_channel_preferences.py`       | `unit/player/test_player_preferences.py`    | ⏳      | Player channel preferences         |
| `test_player_guid_formatter.py`            | `unit/player/test_player_guid_formatter.py` | ⏳      | GUID formatting                    |
| `test_character_creation_service_layer.py` | `unit/player/test_character_creation.py`    | ⏳      | Character creation                 |
| `test_character_recovery_flow.py`          | `unit/player/test_character_recovery.py`    | ⏳      | Character recovery                 |
| `test_stats_generator.py`                  | `unit/player/test_stats_generator.py`       | ⏳      | Stats generation                   |
| `test_stats_random_generation.py`          | `unit/player/test_stats_generator.py`       | 🔀      | Merge with test_stats_generator.py |
| `test_user_manager.py`                     | `unit/player/test_user_manager.py`          | ⏳      | User management                    |

### Unit Tests - NPC System

| Current Location                    | New Location                              | Status | Notes                                     |
| ----------------------------------- | ----------------------------------------- | ------ | ----------------------------------------- |
| `test_npc_models.py`                | `unit/npc/test_npc_models.py`             | ⏳      | NPC data models                           |
| `test_npc_behaviors.py`             | `unit/npc/test_npc_behaviors.py`          | ⏳      | NPC behavior system                       |
| `test_npc_spawning_service.py`      | `unit/npc/test_npc_spawning_service.py`   | ⏳      | NPC spawning                              |
| `test_npc_lifecycle_manager.py`     | `unit/npc/test_npc_lifecycle_manager.py`  | ⏳      | NPC lifecycle                             |
| `test_npc_population_control.py`    | `unit/npc/test_npc_population_control.py` | ⏳      | Population control                        |
| `test_npc_population_management.py` | `unit/npc/test_npc_population_control.py` | 🔀      | Merge with test_npc_population_control.py |
| `test_npc_startup_service.py`       | `unit/npc/test_npc_startup_service.py`    | ⏳      | NPC startup                               |
| `test_npc_name_formatting.py`       | `unit/npc/test_npc_name_formatting.py`    | ⏳      | Name formatting                           |
| `test_npc_threading.py`             | `unit/npc/test_npc_threading.py`          | ⏳      | Threading handling                        |
| `test_npc_admin_api_simple.py`      | `unit/npc/test_npc_admin_api.py`          | ⏳      | Admin API                                 |
| `test_npc_admin_api.py`             | `unit/npc/test_npc_admin_api.py`          | 🔀      | Merge with test_npc_admin_api_simple.py   |

### Unit Tests - World/Rooms

| Current Location                    | New Location                              | Status | Notes                               |
| ----------------------------------- | ----------------------------------------- | ------ | ----------------------------------- |
| `test_room_model.py`                | `unit/world/test_room_models.py`          | ⏳      | Room data models                    |
| `test_room_service.py`              | `unit/world/test_room_service.py`         | ⏳      | Room service layer                  |
| `test_room_service_layer.py`        | `unit/world/test_room_service.py`         | 🔀      | Merge with test_room_service.py     |
| `test_room_utils.py`                | `unit/world/test_room_utils.py`           | ⏳      | Room utilities                      |
| `test_world_loader.py`              | `unit/world/test_world_loader.py`         | ⏳      | World loader                        |
| `test_world_loader_hierarchy.py`    | `unit/world/test_world_hierarchy.py`      | ⏳      | World hierarchy                     |
| `test_movement_service.py`          | `unit/world/test_movement_service.py`     | ⏳      | Movement service                    |
| `test_movement_comprehensive.py`    | `unit/world/test_movement_service.py`     | 🔀      | Merge with test_movement_service.py |
| `test_movement_persistence.py`      | `unit/world/test_movement_persistence.py` | ⏳      | Movement persistence                |
| `test_room_based_mute_filtering.py` | `unit/world/test_room_mute_filtering.py`  | ⏳      | Room-based mute filtering           |

### Unit Tests - Events

| Current Location                              | New Location                                            | Status | Notes                                       |
| --------------------------------------------- | ------------------------------------------------------- | ------ | ------------------------------------------- |
| `test_event_bus.py`                           | `unit/events/test_event_bus.py`                         | ⏳      | Event bus core                              |
| `test_event_bus_pure_asyncio_verification.py` | `verification/test_pure_async_eventbus_verification.py` | ⏳      | Async verification                          |
| `test_event_publisher.py`                     | `unit/events/test_event_publisher.py`                   | ⏳      | Event publisher                             |
| `test_event_handler_timestamps.py`            | `unit/events/test_event_handler.py`                     | ⏳      | Event handler                               |
| `test_event_handler_broadcasting.py`          | `unit/events/test_event_handler.py`                     | 🔀      | Merge with test_event_handler_timestamps.py |
| `test_message_handler_factory.py`             | `unit/events/test_message_handler_factory.py`           | ⏳      | Message handler factory                     |
| `test_working_event_system.py`                | `unit/events/test_event_system.py`                      | ⏳      | Event system integration                    |

### Unit Tests - Authentication

| Current Location                  | New Location                           | Status | Notes                   |
| --------------------------------- | -------------------------------------- | ------ | ----------------------- |
| `test_auth.py`                    | `unit/auth/test_auth.py`               | ⏳      | Core authentication     |
| `test_auth_utils.py`              | `unit/auth/test_auth_utils.py`         | ⏳      | Auth utilities          |
| `test_jwt_authentication_flow.py` | `unit/auth/test_jwt_authentication.py` | ⏳      | JWT authentication      |
| `test_argon2_utils.py`            | `unit/auth/test_argon2_utils.py`       | ⏳      | Argon2 password hashing |
| `test_email_utils.py`             | `unit/auth/test_email_utils.py`        | ⏳      | Email utilities         |

### Unit Tests - Middleware

| Current Location                           | New Location                                        | Status | Notes               |
| ------------------------------------------ | --------------------------------------------------- | ------ | ------------------- |
| `test_error_handling_middleware.py`        | `unit/middleware/test_error_handling_middleware.py` | ⏳      | Error handling      |
| `test_comprehensive_logging_middleware.py` | `unit/middleware/test_logging_middleware.py`        | ⏳      | Logging middleware  |
| `test_security_middleware.py`              | `unit/middleware/test_security_middleware.py`       | ⏳      | Security middleware |
| `test_cors_configuration_verification.py`  | `unit/middleware/test_cors_configuration.py`        | ⏳      | CORS configuration  |

### Unit Tests - Models

| Current Location                          | New Location                              | Status | Notes               |
| ----------------------------------------- | ----------------------------------------- | ------ | ------------------- |
| `test_models.py`                          | `unit/models/test_models.py`              | ⏳      | Base models         |
| `test_models_relationships.py`            | `unit/models/test_model_relationships.py` | ⏳      | Model relationships |
| `test_model_configuration_consistency.py` | `unit/models/test_model_configuration.py` | ⏳      | Model configuration |
| `test_profession_models.py`               | `unit/models/test_profession_models.py`   | ⏳      | Profession models   |
| `test_health_models.py`                   | `unit/models/test_health_models.py`       | ⏳      | Health models       |
| `test_alias_models.py`                    | `unit/models/test_alias_models.py`        | ⏳      | Alias models        |

### Unit Tests - Services

| Current Location                              | New Location                                   | Status | Notes                                           |
| --------------------------------------------- | ---------------------------------------------- | ------ | ----------------------------------------------- |
| `test_health_service.py`                      | `unit/services/test_health_service.py`         | ⏳      | Health check service                            |
| `test_game_tick_service.py`                   | `unit/services/test_game_tick_service.py`      | ⏳      | Game tick service                               |
| `test_memory_cleanup_service.py`              | `unit/services/test_memory_cleanup_service.py` | ⏳      | Memory cleanup                                  |
| `test_metrics_collector.py`                   | `unit/services/test_metrics_collector.py`      | ⏳      | Metrics collection                              |
| `test_service_dependency_injection.py`        | `unit/services/test_dependency_injection.py`   | ⏳      | Service DI                                      |
| `test_service_dependency_injection_simple.py` | `unit/services/test_dependency_injection.py`   | 🔀      | Merge with test_service_dependency_injection.py |

### Unit Tests - Real-time Communication

| Current Location                         | New Location                                      | Status | Notes                                   |
| ---------------------------------------- | ------------------------------------------------- | ------ | --------------------------------------- |
| `test_websocket_handler.py`              | `unit/realtime/test_websocket_handler.py`         | ⏳      | WebSocket handler                       |
| `test_websocket_message_handler.py`      | `unit/realtime/test_websocket_message_handler.py` | ⏳      | WS message handler                      |
| `test_websocket_connection_stability.py` | `unit/realtime/test_websocket_connection.py`      | ⏳      | WS connection                           |
| `test_sse_handler.py`                    | `unit/realtime/test_sse_handler.py`               | ⏳      | SSE handler                             |
| `test_sse_auth.py`                       | `unit/realtime/test_sse_auth.py`                  | ⏳      | SSE authentication                      |
| `test_nats_service.py`                   | `unit/realtime/test_nats_service.py`              | ⏳      | NATS service                            |
| `test_nats_message_handler.py`           | `unit/realtime/test_nats_message_handler.py`      | ⏳      | NATS message handler                    |
| `test_nats_message_handler_subzone.py`   | `unit/realtime/test_nats_message_handler.py`      | 🔀      | Merge with test_nats_message_handler.py |
| `test_nats_retry_handler.py`             | `unit/realtime/test_nats_retry_handler.py`        | ⏳      | NATS retry logic                        |
| `test_dead_letter_queue.py`              | `unit/realtime/test_dead_letter_queue.py`         | ⏳      | Dead letter queue                       |
| `test_real_time.py`                      | `unit/realtime/test_real_time.py`                 | ⏳      | Real-time core                          |

### Unit Tests - Logging

| Current Location              | New Location                                      | Status | Notes               |
| ----------------------------- | ------------------------------------------------- | ------ | ------------------- |
| `test_audit_logger.py`        | `unit/logging/test_audit_logger.py`               | ⏳      | Audit logging       |
| `test_log_analysis_tools.py`  | `unit/logging/test_log_analysis_tools.py`         | ⏳      | Log analysis        |
| `test_logging_integration.py` | `integration/logging/test_logging_integration.py` | ⏳      | Logging integration |

### Unit Tests - Utilities

| Current Location                           | New Location                                      | Status | Notes                             |
| ------------------------------------------ | ------------------------------------------------- | ------ | --------------------------------- |
| `test_security_utils.py`                   | `unit/utilities/test_security_utils.py`           | ⏳      | Security utilities                |
| `test_security_validator.py`               | `unit/utilities/test_security_validator.py`       | ⏳      | Security validation               |
| `test_rate_limiter.py`                     | `unit/utilities/test_rate_limiter.py`             | ⏳      | Rate limiter                      |
| `test_utils_rate_limiter.py`               | `unit/utilities/test_rate_limiter.py`             | 🔀      | Merge with test_rate_limiter.py   |
| `test_circuit_breaker.py`                  | `unit/utilities/test_circuit_breaker.py`          | ⏳      | Circuit breaker                   |
| `test_alias_graph.py`                      | `unit/utilities/test_alias_graph.py`              | ⏳      | Alias graph                       |
| `test_alias_storage.py`                    | `unit/utilities/test_alias_storage.py`            | ⏳      | Alias storage                     |
| `test_alias_integration.py`                | `integration/utilities/test_alias_integration.py` | ⏳      | Alias integration                 |
| `test_centralized_validation_functions.py` | `unit/utilities/test_validation_functions.py`     | ⏳      | Validation functions              |
| `test_error_handlers.py`                   | `unit/utilities/test_error_handlers.py`           | ⏳      | Error handlers                    |
| `test_legacy_error_handlers.py`            | `unit/utilities/test_error_handlers.py`           | 🔀      | Merge with test_error_handlers.py |
| `test_standardized_error_handling.py`      | `unit/utilities/test_error_handlers.py`           | 🔀      | Merge with test_error_handlers.py |
| `test_standardized_responses.py`           | `unit/utilities/test_standardized_responses.py`   | ⏳      | Standardized responses            |
| `test_pydantic_error_handler.py`           | `unit/utilities/test_pydantic_error_handler.py`   | ⏳      | Pydantic errors                   |
| `test_validation_error_imports.py`         | `verification/test_validation_error_imports.py`   | ⏳      | Validation imports                |

### Unit Tests - Other

| Current Location                           | New Location                                     | Status | Notes                          |
| ------------------------------------------ | ------------------------------------------------ | ------ | ------------------------------ |
| `test_persistence.py`                      | `unit/infrastructure/test_persistence.py`        | ⏳      | Persistence layer              |
| `test_persistence_error_logging.py`        | `unit/infrastructure/test_persistence.py`        | 🔀      | Merge with test_persistence.py |
| `test_motd_loader.py`                      | `unit/infrastructure/test_motd_loader.py`        | ⏳      | MOTD loader                    |
| `test_task_registry.py`                    | `unit/infrastructure/test_task_registry.py`      | ⏳      | Task registry                  |
| `test_connection_manager_comprehensive.py` | `unit/infrastructure/test_connection_manager.py` | ⏳      | Connection manager             |

### Integration Tests

| Current Location                                 | New Location                                                    | Status | Notes                                              |
| ------------------------------------------------ | --------------------------------------------------------------- | ------ | -------------------------------------------------- |
| `test_api_players_integration.py`                | `integration/api/test_api_players_integration.py`               | ⏳      | Player API integration                             |
| `test_dual_connection_integration.py`            | `integration/api/test_dual_connection_integration.py`           | ⏳      | Dual connection integration                        |
| `test_monitoring_dual_connections.py`            | `integration/api/test_monitoring_integration.py`                | ⏳      | Monitoring integration                             |
| `test_admin_teleport_integration.py`             | `integration/commands/test_admin_teleport_integration.py`       | ⏳      | Admin teleport integration                         |
| `test_whisper_command_integration.py`            | `integration/chat/test_whisper_integration.py`                  | ⏳      | Whisper integration                                |
| `test_local_channel_nats_integration.py`         | `integration/nats/test_local_channel_nats.py`                   | ⏳      | Local channel NATS                                 |
| `test_player_channel_preferences_integration.py` | `integration/chat/test_player_preferences_integration.py`       | ⏳      | Player preferences                                 |
| `test_mute_unmute_workflow_integration.py`       | `integration/chat/test_mute_workflow_integration.py`            | ⏳      | Mute workflow                                      |
| `test_system_channel_integration.py`             | `integration/chat/test_system_channel_integration.py`           | ⏳      | System channel                                     |
| `test_event_broadcasting_bugs.py`                | `integration/events/test_event_broadcasting.py`                 | ⏳      | Event broadcasting                                 |
| `test_complete_event_flow_integration.py`        | `integration/events/test_event_flow_integration.py`             | ⏳      | Event flow                                         |
| `test_real_event_flow.py`                        | `integration/events/test_event_flow_integration.py`             | 🔀      | Merge with test_complete_event_flow_integration.py |
| `test_realtime_event_handler_integration.py`     | `integration/events/test_realtime_event_handler_integration.py` | ⏳      | Real-time event handler                            |
| `test_websocket_connection_events.py`            | `integration/events/test_websocket_connection_events.py`        | ⏳      | WebSocket events                                   |
| `test_connection_manager_occupant_events.py`     | `integration/events/test_connection_manager_events.py`          | ⏳      | Connection manager events                          |
| `test_npc_integration.py`                        | `integration/npc/test_npc_integration.py`                       | ⏳      | NPC integration                                    |
| `test_npc_room_integration.py`                   | `integration/npc/test_npc_room_integration.py`                  | ⏳      | NPC room integration                               |
| `test_npc_admin_commands.py`                     | `integration/npc/test_npc_admin_commands_integration.py`        | ⏳      | NPC admin commands                                 |
| `test_npc_admin_commands_fixed.py`               | `integration/npc/test_npc_admin_commands_integration.py`        | 🔀      | Merge with test_npc_admin_commands.py              |
| `test_movement_integration.py`                   | `integration/movement/test_movement_integration.py`             | ⏳      | Movement integration                               |
| `test_room_synchronization.py`                   | `integration/movement/test_room_synchronization.py`             | ⏳      | Room synchronization                               |
| `test_nats_integration_e2e.py`                   | `integration/nats/test_nats_integration_e2e.py`                 | ⏳      | NATS E2E integration                               |
| `test_connection_manager_nats_integration.py`    | `integration/nats/test_connection_manager_nats.py`              | ⏳      | Connection manager NATS                            |
| `test_comprehensive_integration.py`              | `integration/comprehensive/test_comprehensive_integration.py`   | ⏳      | Comprehensive                                      |
| `test_simple_integration.py`                     | `integration/comprehensive/test_simple_integration.py`          | ⏳      | Simple integration                                 |
| `test_simple_connection_events.py`               | `integration/comprehensive/test_simple_integration.py`          | 🔀      | Merge with test_simple_integration.py              |
| `test_integration_bug_prevention.py`             | `integration/comprehensive/test_bug_prevention.py`              | ⏳      | Bug prevention                                     |
| `test_game_api_broadcast.py`                     | `integration/api/test_game_api_broadcast.py`                    | ⏳      | Game API broadcast                                 |

### E2E Tests

| Current Location                               | New Location                                   | Status | Notes                    |
| ---------------------------------------------- | ---------------------------------------------- | ------ | ------------------------ |
| `test_multiplayer_integration.py`              | `e2e/test_multiplayer_integration.py`          | ⏳      | Multiplayer E2E          |
| `test_e2e_multiplayer_connection_messaging.py` | `e2e/test_multiplayer_connection_messaging.py` | ⏳      | Multiplayer messaging    |
| `test_logout_integration.py`                   | `e2e/test_logout_integration.py`               | ⏳      | Logout workflow          |
| `test_dual_connection_testing_strategy.py`     | `e2e/test_dual_connection_testing_strategy.py` | ⏳      | Dual connection strategy |
| `test_game_mechanics.py`                       | `e2e/test_game_mechanics.py`                   | ⏳      | Game mechanics           |

### Performance Tests

| Current Location                       | New Location                                       | Status | Notes                |
| -------------------------------------- | -------------------------------------------------- | ------ | -------------------- |
| `test_dual_connection_performance.py`  | `performance/test_dual_connection_performance.py`  | ⏳      | Dual connection perf |
| `test_error_logging_performance.py`    | `performance/test_error_logging_performance.py`    | ⏳      | Error logging perf   |
| `test_mute_filtering_performance.py`   | `performance/test_mute_filtering_performance.py`   | ⏳      | Mute filtering perf  |
| `test_model_performance_benchmarks.py` | `performance/test_model_performance_benchmarks.py` | ⏳      | Model benchmarks     |

### Security Tests

| Current Location                          | New Location                                       | Status | Notes                   |
| ----------------------------------------- | -------------------------------------------------- | ------ | ----------------------- |
| `test_admin_teleport_security.py`         | `security/test_admin_teleport_security.py`         | ⏳      | Admin teleport security |
| `test_security_penetration.py`            | `security/test_security_penetration.py`            | ⏳      | Penetration testing     |
| `test_security_headers_verification.py`   | `security/test_security_headers_verification.py`   | ⏳      | Security headers        |
| `test_centralized_security_validation.py` | `security/test_centralized_security_validation.py` | ⏳      | Security validation     |
| `test_global_channel_access_control.py`   | `security/test_global_channel_access_control.py`   | ⏳      | Access control          |
| `test_file_containment.py`                | `security/test_file_containment.py`                | ⏳      | File containment        |

### Coverage Tests

| Current Location                           | New Location                                      | Status | Notes                                          |
| ------------------------------------------ | ------------------------------------------------- | ------ | ---------------------------------------------- |
| `test_command_handler_coverage.py`         | `coverage/test_command_handler_coverage.py`       | ⏳      | Command handler coverage                       |
| `test_command_handler_unified_coverage.py` | `coverage/test_command_handler_coverage.py`       | 🔀      | Merge with test_command_handler_coverage.py    |
| `test_command_rate_limiter_coverage.py`    | `coverage/test_command_rate_limiter_coverage.py`  | ⏳      | Rate limiter coverage                          |
| `test_comprehensive_logging_coverage.py`   | `coverage/test_comprehensive_logging_coverage.py` | ⏳      | Logging coverage                               |
| `test_system_commands_coverage.py`         | `coverage/test_system_commands_coverage.py`       | ⏳      | System commands coverage                       |
| `test_help_content_coverage.py`            | `coverage/test_help_content_coverage.py`          | ⏳      | Help content coverage                          |
| `test_simple_coverage_gaps.py`             | `coverage/test_simple_coverage_gaps.py`           | ⏳      | Coverage gap filling                           |
| `test_comprehensive_error_logging.py`      | `coverage/test_error_logging_coverage.py`         | ⏳      | Error logging coverage                         |
| `test_error_logging_integration.py`        | `coverage/test_error_logging_coverage.py`         | 🔀      | Merge with test_comprehensive_error_logging.py |

### Regression Tests

| Current Location                 | New Location                             | Status | Notes                               |
| -------------------------------- | ---------------------------------------- | ------ | ----------------------------------- |
| `test_unknown_room_fix.py`       | `regression/test_unknown_room_fix.py`    | ⏳      | Unknown room bug fix                |
| `test_movement_fix.py`           | `regression/test_movement_fix.py`        | ⏳      | Movement bug fix                    |
| `test_self_message_bug.py`       | `regression/test_self_message_bug.py`    | ⏳      | Self-message bug                    |
| `test_self_message_exclusion.py` | `regression/test_self_message_bug.py`    | 🔀      | Merge with test_self_message_bug.py |
| `test_npc_spawn_fix.py`          | `regression/test_npc_spawn_fix.py`       | ⏳      | NPC spawn bug fix                   |
| `test_unresolved_bugs.py`        | `regression/test_unresolved_bugs.py`     | ⏳      | Unresolved bugs tracking            |
| `test_debug_infinite_loop.py`    | `regression/test_infinite_loop_debug.py` | ⏳      | Infinite loop debug                 |

### Monitoring Tests

| Current Location                            | New Location                                    | Status | Notes                                         |
| ------------------------------------------- | ----------------------------------------------- | ------ | --------------------------------------------- |
| `test_mute_filtering_monitoring.py`         | `monitoring/test_mute_filtering_monitoring.py`  | ⏳      | Mute filtering monitoring                     |
| `test_movement_monitor.py`                  | `monitoring/test_movement_monitor.py`           | ⏳      | Movement monitoring                           |
| `test_occupant_count_integration.py`        | `monitoring/test_occupant_count_integration.py` | ⏳      | Occupant count                                |
| `test_occupant_count_simple_integration.py` | `monitoring/test_occupant_count_integration.py` | 🔀      | Merge with test_occupant_count_integration.py |
| `test_multiple_players_muting.py`           | `monitoring/test_multiple_players_muting.py`    | ⏳      | Multi-player muting                           |
| `test_mute_data_consistency.py`             | `verification/test_mute_data_consistency.py`    | ⏳      | Mute consistency                              |
| `test_temporary_permanent_mutes.py`         | `monitoring/test_temporary_permanent_mutes.py`  | ⏳      | Mute types                                    |

### Verification Tests

| Current Location                           | New Location                                            | Status | Notes                   |
| ------------------------------------------ | ------------------------------------------------------- | ------ | ----------------------- |
| `test_async_operations_verification.py`    | `verification/test_async_operations_verification.py`    | ⏳      | Async verification      |
| `test_async_pattern_standardization.py`    | `verification/test_async_pattern_standardization.py`    | ⏳      | Async patterns          |
| `test_async_route_handlers.py`             | `verification/test_async_route_handlers.py`             | ⏳      | Async route handlers    |
| `test_base_testing_async.py`               | `verification/test_base_testing_async.py`               | ⏳      | Base async testing      |
| `test_pure_async_eventbus_verification.py` | `verification/test_pure_async_eventbus_verification.py` | ⏳      | Pure async event bus    |
| `test_running_event_loop.py`               | `verification/test_running_event_loop.py`               | ⏳      | Event loop verification |
| `test_help_topic_validation.py`            | `verification/test_help_topic_validation.py`            | ⏳      | Help topic validation   |
| `test_event_verification_demo.py`          | `verification/test_event_verification_demo.py`          | ⏳      | Event verification demo |

### Special/Demo/Deprecated Tests

| Current Location | New Location  | Status | Notes                 |
| ---------------- | ------------- | ------ | --------------------- |
| `test_simple.py` | -             | 🗑️      | Obsolete/demo test    |
| `conftest.py`    | `conftest.py` | ⏳      | Update with new paths |

## Summary Statistics

### Total Files: 204

**By Action:**

- ⏳ Pending: 159 files
- 🔀 To Merge: 35 files (into 20 consolidated files)
- 🗑️ To Remove: 1 file
- ✅ Complete: 0 files (migration not started)
- 🔄 In Progress: 0 files

**Net Result:**

- Starting: 204 files
- Removing: 1 file
- Merging: 35 → 20 files (15 file reduction)
- **Final Count: ~168 test files** (18% reduction)

**By Category:**

- Unit Tests: ~110 files
- Integration Tests: ~30 files
- E2E Tests: ~5 files
- Performance Tests: ~4 files
- Security Tests: ~6 files
- Coverage Tests: ~7 files
- Regression Tests: ~7 files
- Monitoring Tests: ~6 files
- Verification Tests: ~8 files
- Fixtures/Utilities: ~8 files

---

*Migration mapping last updated: [Current Date]*
*Status will be updated as migration progresses*
