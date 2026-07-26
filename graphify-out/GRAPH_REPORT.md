# Graph Report - MythosMUD  (2026-07-26)

## Corpus Check
- 2869 files · ~2,620,471 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 44047 nodes · 79760 edges · 1910 communities (1291 shown, 619 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 4830 edges (avg confidence: 0.66)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8b0ec539`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- .get_instance
- connection_manager.py
- AsyncPersistenceLayer
- test_alias_commands.py
- test_security_validator.py
- useMythosAppState.ts
- types.ts
- inventory_pickup_command.py
- CombatService
- PlayerRoomEventHandler
- MythosMUDError
- test_command_factories_inventory.py
- LoggedHTTPException
- get_logger
- npc_base.py
- player_connection_setup.py
- User
- ErrorContext
- test_wearable_container_service.py
- .state
- ContainerComponent
- ContainerService
- test_npc_combat_integration_service.py
- test_command_inventory.py
- test_health_service.py
- error_types.py
- test_nats_message_handler.py
- test_command_validator.py
- test_look_npc.py
- Room
- .create_instance
- UUID
- game.py
- Invite
- EldritchIcon.tsx
- spell_effects_heal.py
- dependencies.py
- BehaviorEngine
- lucidity.py
- admin_teleport_commands.py
- _MagicServiceCore
- test_user_manager.py
- __init__.py
- test_zone_config_loader.py
- NATSMessageHandler
- Any
- inventory_command_helpers.py
- websocket_handler.py
- test_room_service.py
- IdleMovementHandler
- test_player_preferences_service.py
- SpellLearningService
- test_communication_commands_flows.py
- test_connection_delegates.py
- Player
- test_container_persistence.py
- __init__.py
- test_npc_database.py
- PlayerOccupantProcessor
- character_creation.py
- test_command_factories_utility.py
- validate_room_data
- __init__.py
- ApplicationContainer
- PassiveLucidityFluxService
- is_player_in_login_grace_period
- test_player_service.py
- test_command_factories_exploration.py
- get_admin_auth_service
- test_login_grace_period_visual_indicator.py
- chatPanelRuntimeUtils.ts
- RateLimiter
- test_admin_auth_service.py
- ChatService
- CombatInstance
- test_quest_service.py
- test_npc_service.py
- test_websocket_handler_core.py
- test_look_helpers.py
- websocket_initial_state.py
- multiplayer.ts
- test_auth_utils.py
- Reporter
- test_magic_commands.py
- AppConfig
- test_status_commands.py
- lifespan.py
- panelReducerHandlers.ts
- test_container_helpers_inventory_find.py
- LucidityService
- exceptions.py
- test_look_room.py
- MessageQueue
- test_connection_disconnection.py
- test_exploration_service.py
- NPCBase
- test_lifespan_startup.py
- Alias
- test_player_presence_tracker.py
- test_command_admin.py
- DependencyAnalyzer
- EventPublisher
- test_container_helpers_inventory_ops.py
- get_username_from_user
- test_game.py
- container_persistence_async.py
- security.ts
- HolidayService
- RoomLoader
- UUID
- test_combat_monitoring_service.py
- ConnectionManager
- aggro_threat.py
- _handle_admin_set_stat_command
- test_mp_regeneration_service.py
- UserManager
- test_look_player.py
- test_logging_utilities.py
- main.py
- logger.ts
- test_command_moderation.py
- PlayerPositionService
- FeatureFlagService
- Stats
- SchemaValidator
- .to_dict
- test_lucidity_recovery_commands.py
- test_enhanced_logging_config.py
- PathValidator
- UUID
- test_invite_schemas.py
- test_manager.py
- systemHandlers.ts
- ScheduleEntry
- container_endpoints_basic.py
- test_websocket_messages.py
- ChatLogger
- RoomSyncService
- extract_room_id_from_npc
- NPCCombatIntegrationBase
- .get_room
- catatonia_check.py
- CircuitBreaker
- .build_subject
- test_skill_service.py
- test_combat_flee_helpers.py
- test_follow_commands.py
- test_room_subscription_manager_drops.py
- test_validation.py
- test_room_sync_service.py
- test_container_websocket_events.py
- apiTypeGuards.ts
- CombatConfiguration
- quality_fragmentation_ai_guardrails.py
- test_character_creation_service.py
- test_npc_models.py
- test_admin_commands.py
- test_websocket_handler_validation_errors.py
- websocket_handler_commands.py
- RoomDataCache
- test_player_event_handlers_respawn.py
- CorpseOverlay.tsx
- NPCSpawnRule
- useGameClientV2Container.ts
- sanitize_detail_value
- test_rate_limiter.py
- PlayerChannelPreferences
- test_room_renderer.py
- chat_service.py
- test_rescue_service.py
- projectorHandlersMessages.ts
- useGameConnectionRefactored.ts
- AggressiveMobNPC
- test_spell_effects.py
- ZoneConfiguration
- test_party_service.py
- get_cache_manager
- CatatoniaRegistry
- test_nats_broker.py
- ._is_valid_name_for_occupant
- App.tsx
- CommandRequest
- MemoryMonitor
- test_world.py
- test_inventory_commands.py
- fastapi_integration.py
- test_logout_commands.py
- ResourceManager
- QuestService
- NATSMessageBroker
- lucidity_service.py
- MemoryProfiler
- ._prepare_sanitarium_respawn
- __init__.py
- metrics.py
- NPCMovementIntegration
- test_movement_monitor.py
- test_command_factories_moderation.py
- .check_level_up
- auth.ts
- test_corpse_lifecycle_service.py
- test_follow_service.py
- test_alias_storage.py
- test_map_helpers.py
- TaskRegistry
- test_game_state_provider.py
- test_room_subscription_manager.py
- websocket_helpers.py
- test_websocket_handler_helpers_extended.py
- FStringLoggingFixer
- correlation_middleware.py
- RoomMapEditorRuntime.tsx
- test_connection_statistics.py
- logging_file_setup.py
- test_connection_session_management.py
- safe_run_static
- gen_arena_migration_sql.py
- NPCThreadManager
- container_helpers_inventory_display.py
- test_command_combat.py
- gameStore.ts
- PatternNotFoundError
- RoomDataValidator
- NPC Duplication Bug Fix Plan
- test_websocket_helpers.py
- CombatMonitoringService
- command_input.py
- PassiveMobNPC
- UUID
- container_persistence.py
- TestValidatorIntegration
- useGameTerminal.ts
- Test Suite Refactoring Plan
- ChatModeration
- NATSRetryHandler
- NATSEventBusBridge
- test_player_occupant_processor.py
- test_who_commands.py
- Three-Phase Async Remediation Plan
- Player
- npc_definitions_api.py
- look_command.py
- datetime
- error_handling_middleware.py
- fix_markdown_blanks_around_lists.py
- GameLogPanel.tsx
- LogAggregator
- LRUCache
- SubjectValidationError
- vim Best Practices and Coding Standards
- testing_examples.py
- subzone_schema.json
- test_nats_messages.py
- User Experience & Commands
- coerce_int
- PydanticErrorHandler
- NPCDefinitionCRUDMixin
- PlayerInventory
- test_memory_leak_metrics.py
- test_room_utils.py
- Enhanced Logging Implementation Summary
- 🧪 MythosMUD E2E Testing Strategy
- GameTerminal.tsx
- executeCommand
- Memory Leak Prevention System - Implementation Summary
- deprecated_patterns.py
- test_game_tick_processing_async.py
- game_tick_processing.py
- test_admin_shutdown_command.py
- test_combat_schema.py
- quest_commands.py
- test_look_item.py
- test_population_stats.py
- test_room_subscription_manager_helpers.py
- version
- AsciiMapRenderer
- combat_attack.py
- PlayerLucidity
- test_command_processor.py
- .__post_init__
- verify_enhanced_logging_compliance.py
- test_item.py
- GameClientV2ContainerView.tsx
- deque
- character-cleanup.ts
- test_pattern_matcher.py
- compare_linting_results.py
- monitoring.py
- test_connection_cleaner.py
- TestCombatMessagingService
- TestRoomDataFixer
- test_npc_combat_handlers.py
- test_command_parser_helpers.py
- player_service
- handle_read_command
- test_dependency_injection.py
- Execution Steps
- test_combat_persistence_handler_persistence.py
- EdgeCreationModal.tsx
- test_windows_safe_rotation.py
- ExplorationService
- real_time.py
- _check_grace_period_block
- EventHandler
- E2E Test Suite AI Execution Improvements - Summary
- __init__.py
- test_room_id_utils.py
- test_command_base.py
- File-by-File Changes
- TestHierarchicalSchema
- BaseCommand
- Paired YAML and Env Config Tuples
- Alias System Implementation Plan
- SchemaValidator
- migration_examples.py
- test_command_exploration.py
- NATS Sync Ops in Async Handlers
- npc_config_parsing.py
- test_message_filtering.py
- .apply_costs
- Graceful Degradation Planning
- test_aggro_threat.py
- get_asyncpg_server_settings_for_database_url
- MovementService
- TestNPCCombatRewards
- player_effect_repository.py
- StatusPanel.tsx
- multiplayer-browser-helpers.js
- HealthService
- consume_prototype_from_player
- WebSocketRequestContext
- Container System
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- emotes.schema.json
- map_minimap.py
- SSE Authentication System
- test_metrics_endpoints.py
- _find_container_in_room
- Structured Error Logging
- npc_admin.py
- AliasGraph
- hallucinations.py
- test_optimized_security_validator.py
- SafeHtml.tsx
- generate_sql.mjs
- test_command_service.py
- Bug Investigator Subagent
- Enhanced Logging Implementation Complete
- Migration Final Report
- Structlog Implementation Plan
- admin_shutdown_command.py
- PlayerEffect
- e2e-bootstrap.ts
- Test Suite Optimization Status
- authenticated.ts
- Performance Optimization Summary
- MovementMonitor
- FollowService
- test_spawn_validator.py
- test_connection_state_machine.py
- test_room_occupant_manager.py
- test_chat_logger.py
- debugLogger
- Environment Configuration Refactoring
- Three-Column Game UI Layout
- UserManagerProtocol
- .__init__
- TargetResolutionService
- send_game_event
- NPCOccupantProcessor
- Container/Item Repository Async Migration Plan
- test_postgres_adapter.py
- AsciiMapViewer.tsx
- AuditLogger
- rooms.py
- config.ts
- GameInfoPanel.tsx
- Migration Strategy
- transfer_all_items_from_container
- test_game_tick_processing.py
- UUID
- Phase 3, Task 3.2: NATS Subject Manager Usage Review
- chat_nats_publisher.py
- _find_item_in_room_drops
- format_message_content
- test_lru_cache.py
- PeriodicOrphanAuditor
- Planning Completion Summary
- test_player_event_handlers_room_left.py
- performance.test.tsx
- devDependencies
- FeedbackManager
- Test Suite Analyzer Subagent
- Feature Requirements Document: Random Stats Generator
- retry.py
- PlayerRespawnEventHandler
- get_async_session
- subject_controller.py
- ValidationRule
- emote_schema.json
- Incremental Upgrade Strategy (Report)
- layout.ts
- Cursor Subagents Overview
- stateNormalization.ts
- Performance Profiler Subagent
- command_handler_unified.py
- Domain Model Anemic Anti-Pattern Audit
- Dependency Upgrade Strategy Specification
- Any
- RoomCacheLoader
- _find_item_in_inventory
- AsyncPersistenceLayer
- ShopkeeperNPC
- convert_uuids_to_strings
- realtime.py
- test_look_item_helpers.py
- PlayerNameExtractor
- test_health_monitor.py
- test_dependency_analysis.py
- test_rate_limiter_utils.py
- test_npc_event_handlers_helpers.py
- ChatPanelRefactoredView.tsx
- Global Chat Channel
- GameTerminalContext.test.tsx
- Security Auditor Subagent
- properties
- CI/CD Enhanced Logging Validation
- test_look_container.py
- MythosMUD Dependency Upgrade Strategy - Implementation Summary
- bind_request_context
- compilerOptions
- Execution Steps
- Execution Steps
- test_combat_persistence_handler.py
- playerHandlers.ts
- inventory_drop_command.py
- Execution Steps
- test_event_bus.py
- generate_html_visualization.py
- admin_auth_service.py
- _make_session_context
- test_room_subscription_manager_npcs.py
- Testing Steps
- mapPageRenderer.tsx
- designTokens.ts
- Environment Contamination Audit Report
- Hierarchical Test Structure
- Execution Steps
- item_instance_persistence_async.py
- _find_item_in_equipped
- CorpseLifecycleService
- ChatPanel
- messageHandlers.ts
- useThemeContext.ts
- Stop-MythosMudProjectProcessTree
- multiplayer-browser-helpers.bundle.js
- ConnectionErrorHandler
- MessageFilteringHelper
- Dependency Upgrade Strategy Agent
- update_aggro
- ._cleanup_player_mutes
- codacy.yaml Tool Manifest
- shutdown_sequence.py
- TestVerificationSqlUsersPlayers
- test_profession.py
- TestNPCCombatLifecycle
- test_npc_startup_service.py
- _assign_container_get_instance
- TestPathValidator
- package.json
- useDraggablePanelInteractions.ts
- NPCEventHandler
- roomHandlers.ts
- Scenario 20 Logout Errors
- Codebase Explorer Subagent
- Lint Remediation Prompt - AI-Optimized Version
- ADR-012: python-statemachine for Backend Connection FSM
- enum
- properties
- MemoryThresholdMonitor
- is_shutdown_pending
- inventory_put_command.py
- compilerOptions
- get_help_content
- WebSocket Best Practices Compliance
- MessageBrokerError
- MemoryMonitor
- Main Foyer Starting Room
- properties
- Execution Steps
- PostgresConnection
- EmoteService
- PartyService
- test_channel_broadcasting_strategies.py
- Prometheus Configuration
- CombatMetrics
- HealthRepository
- NPCStartupService
- load_world_seed.py
- canonical_room_id_impl
- ReactNodeUpgradeAnalyzer
- test_level_service.py
- test_npc_utils.py
- test_occupant_formatter.py
- Address Semgrep Security Findings Plan
- MonitoringPanel.test.tsx
- Multiplayer Architecture Planning
- Lint Remediation Prompt - AI-Optimized Version
- Execution Steps
- conftest.py
- _JSONDict
- AliasStorage
- ADR-005 Repository Pattern
- create_hasher_with_params
- properties
- Pre-commit Logging Validation Hook
- RoomCacheService
- Profession
- channel_broadcasting_strategies.py
- Per-Recipient Whisper Rate Limit
- cleanup_websocket_connection
- __init__.py
- ._get_room_uuid_by_stable_id
- Disconnect Grace Period and Rest Command
- RoomEditModal.tsx
- RateLimiter
- usePanelContext.ts
- Phase 1: Core Separation
- Phase 2: Enhanced Features
- 📅 Implementation Plan
- type
- generate_sql.mjs
- _format_room_posture_message
- ChatPoseManager
- Dual Connection Monitoring Guide
- ChatWhisperTracker
- ._handle_npc_follower_move
- pytest_asyncio_loop_factories
- ConnectionMetadata
- get_npc_name_from_instance
- DeadLetterMessage
- NATS Error Handling Strategy
- PersonalMessageSender
- OccupantFormatter
- GameTickService
- MockEventClass
- test_dead_letter_queue.py
- test_message_filtering_helpers.py
- TestGameTickService
- test_combat_audit.py
- optimized_validate_player_name
- optimized_security_validator.py
- PanelContextRuntime.tsx
- SpellRegistry
- RoomInfo.tsx
- MessageBatcher
- E2E Testing Setup Status
- Test/Production Environment Separation
- required
- unified_room_schema.json
- _process_session_dp_decay_and_death
- CreateItemInstanceInput
- npc_combat_grace.py
- Async Remediation Complete
- Any
- .call
- conftest.py
- ErrorMonitor
- verify_linting_parity.py
- CoordinateGenerator
- Test Server Remediation Prompt - Cursor Executable Version
- required
- Chat Panel Separation Implementation Tasks
- Main.py Refactoring Plan
- parse_shutdown_parameters
- _should_include_npc
- skills_commands.py
- chat_pose_helpers.py
- command_handler_v2
- total_xp_for_level
- extract_definition_id_from_npc
- Tiered Test Coverage Strategy
- TestLogoutCommand
- DeadLetterQueue
- RoomFixer
- AsyncPersistenceLayer Pattern
- HealthMonitor
- Linting Complexity Alignment
- RetryConfig
- .load_player_mutes
- Whisper Location Independence
- test_player_schema_converter_weapon.py
- test_command_factories.py
- UUID
- StatisticsAggregator
- load_motd
- properties
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- LogAnalyzer
- MythosMUD Wiki Log
- InventoryMutationGuard
- Phase 3: Polish and Optimization
- Phase 4: Testing and Refinement
- Fixture Optimization Complete
- applies_to
- Subagent Automatic Discovery
- properties
- profession.py
- Any
- properties
- properties
- MapPerformanceMonitor
- properties
- properties
- test_go_command.py
- required
- level_from_total_xp
- .despawn_npc
- PostgreSQL Procedures Migration - Audit Spreadsheet
- extract_npc_metadata
- ._trim_samples
- ._is_uuid_string
- WebSocketMessageValidator
- TestPrepareCommandForProcessing
- test_config.py
- PlayerEventHandlerUtils
- test_config_init.py
- test_player_event_handlers_utils.py
- test_websocket_handler_error_handling.py
- test_websocket_handler_rate_limit.py
- _errors_len
- test_combat_validator.py
- room_hierarchy_schema.json
- GridLayoutManager.tsx
- GameClientV2Dock.test.tsx
- REQUIRED TOOL USAGE PATTERN
- CircuitBreaker Implementation Planning Document
- Comprehensive System Audit
- Any
- NPCMaintenanceConfig
- .publish
- Security Implementation
- CircuitBreakerOpen
- .check_player_mute_status
- .retry_async
- Enhanced Logging Migration Report
- wrap_third_party_exception
- properties
- properties
- RoomInfoPanel.tsx
- PostgresRow
- TargetMatch
- Any
- multiplayer-playwright-testing.md
- Mypy Type Checking Remediation Prompt - AI-Optimized Version
- MythosMUD Wiki Index
- PlayerGuidFormatter
- websocket_endpoint
- load_test_10_players.spec.ts
- TestRunner
- test_combat_persistence_handler_events.py
- get_cached_player
- enum
- Chat Panel
- enum
- COPPA Compliance Checklist
- alias_schema.json
- SQLAlchemyAsyncLinter
- quality_fragmentation_lizard.py
- properties
- InventorySchemaValidationError
- enum
- test_level_curve.py
- UnsubscribeError
- schedule_end_combat_if_npc_died_best_effort
- test_lucidity_models.py
- MagicServiceCompletionMixin
- ChannelBroadcastingStrategyFactory
- UnknownChannelStrategy
- RoomBasedChannelStrategy
- get_or_create_hate_list
- CombatAuditLogger
- TestProcessAliasExpansion
- attach_compatibility_properties
- TestHandleSpecialCommandRouting
- format_markdown_file
- migrate_rooms.py
- TestValidateCommandBasics
- TestCheckCastingState
- TestCheckAllCommandBlocks
- TestMinimapExplorationInvestigationDoc
- test_nats_message_handler_chat.py
- test_nats_message_handler_subzone_events.py
- test_npc_event_handlers.py
- test_player_event_handlers_room.py
- test_websocket_handler_validation.py
- optimized_validate_action_content
- optimized_validate_alias_name
- optimized_sanitize_unicode_input
- optimized_validate_security_comprehensive
- Explicit Configuration Migration
- enum
- run-playwright-tests.js
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- test_load_world_seed.py
- required
- applies_to
- handle_system_command
- test_inventory_helpers.py
- CombatDPSync
- MinimapRenderer
- required
- PostgresConnection Context Manager
- Technical Implementation
- Container System API
- 1. **Server-Side Unit Tests** (`server/tests/test_event_broadcasting_bugs.py`)
- Implementation Notes
- Structured Concurrency Task Tracking
- client
- zone_schema.json
- properties
- required
- validate_secure_path
- MetricsCollector
- TauntCommandHandler
- Any
- check_invites.py
- verify_migration.py
- run-vitest.js
- MotdInterstitialScreen.tsx
- usePerformanceMonitor.ts
- holidays.schema.json
- npc_schedules.schema.json
- 1. Enhanced ChatPanel (New Chat Input Panel)
- Implementation Phases
- database
- enum
- alias
- enum
- Who Command Enhancement
- holiday.schema.json
- test_quality_fragmentation_guard.py
- E2E Tests Playwright
- compilerOptions
- compilerOptions
- schedule.schema.json
- required
- handle_emote_command
- required
- router.py
- validate.mjs
- calculate_notification_times
- ApplicationContainer
- asyncio.run Anti-Pattern
- get_shutdown_blocking_message
- Client Layout Baseline
- Playwright CLI E2E Tests
- reset_config
- .call
- Quest System Features
- FieldInfo Type Checker Issues
- .get_lifecycle_statistics
- .from_dict
- TestHandleSpecialCommandRouting
- test_security_utils.py
- TestEnsureAliasStorage
- test_utility_commands_whoami.py
- test_async_persistence_room_cache.py
- .__call__
- test_async_persistence_room_loading.py
- test_combat_messaging_integration.py
- fix_suppression_alignment.py
- identify_critical_code.py
- AdminActionsLogger
- test_error_logging.py
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- optimized_validate_filter_name
- optimized_validate_target_player
- optimized_validate_help_topic
- ValidationError
- optimized_comprehensive_sanitize_input
- required
- properties
- useGridLayout.ts
- MythosMUD
- Chat Panel Separation Specification
- Placeholder Test Removal
- Architecture Remediation Implementation Summary
- __init__.py
- Bug Prevention Testing Strategy
- record_edited_file.py
- Command Handler Patterns
- Bugs Addressed
- 4. **Client-Side Tests** (`client/src/components/GameTerminalWithPanels.test.tsx`)
- Argon2 Implementation Plan
- Playwright MCP Primary Testing Tool
- enum
- Any
- Any
- test_metrics.py
- ._get_player_mute_file
- subscribe_to_room_events_impl
- DatabaseError
- generate_unique_codes
- enum
- audit_suppressions.py
- fix_markdown_line_length.py
- populate_npc_sample_data.py
- unified_room_schema.json
- MagicPointsMeter.tsx
- 🔧 COMMON FIX TEMPLATES
- 🔧 COMMON FIX TEMPLATES
- 🔧 COMMON FIX TEMPLATES
- Common Test Failure Categories
- FAILURE PATTERN RECOGNITION
- scripts
- MUD Disconnect Grace Period & Rest Command: Industry Comparison
- compilerOptions
- MythosMUD Obsidian Vault
- items
- sanitizeChatMessageForState
- items
- Architecture Decision Records (ADRs)
- Best Practices Implemented
- 2. **Unresolved Bug Tests** (`server/tests/test_unresolved_bugs.py`)
- Implementation Details
- Problems Identified
- Purpose
- name
- holidays
- schedules
- PublishError
- test_connection_establishment.py
- LoggingPatternLinter
- SubscribeError
- Arkham City (MOTD Zone)
- CastingStateManager
- graceful_degradation
- CommandRateLimiter
- .get_stat_requirements
- add_damage_threat
- processing.py
- .refresh_configuration
- ._despawn_npc
- TestCheckRateLimit
- test_inventory_service_helpers.py
- UpgradeImplementationPlan
- DraggablePanelResizeHandles.tsx
- ConnectionManager
- ConnectionPanel.tsx
- global-teardown.ts
- Phase 2: Categorize and Prioritize Lint Issues
- Phase 2: Categorize and Prioritize Lint Issues
- Phase 2: Categorize and Prioritize Mypy Issues
- Phase 5: Fix Implementation Patterns
- 4. Common Fix Patterns
- enum
- UI/UX Considerations
- 3. Simplified CommandPanel
- Implementation Phases
- Architecture Patterns Implemented
- Phase 3: Architecture Modernization (COMPLETED ✓)
- Future Bug Prevention
- ✅ Implementation Timeline - COMPLETED
- 🚀 **DEPLOYMENT PHASE - COMPLETED SUCCESSFULLY**
- 🏆 **MAJOR ACCOMPLISHMENT: Pydantic + Click Command Validation System**
- 🧪 Testing Strategy
- command
- items
- item_prototype.schema.json
- .venv-ci Shared Dependencies
- GHA Runner Container
- description
- 2025_01_XX_convert_players_player_id_to_uuid.py
- 2025_11_21_convert_players_player_id_to_uuid.py
- Persistence Extraction Complete
- 2025_11_25_normalize_container_schema.py
- Real-Time Architecture
- 2025_11_25_remove_get_container_contents_json_procedure.py
- 2025_11_25_remove_items_json_column.py
- 2025_11_26_ensure_item_instance_foreign_keys.py
- 2026_02_09_add_player_effects_table.py
- 2026_02_18_add_player_skills_table.py
- 2026_02_18_add_profession_modifiers_columns.py
- 2026_02_19_add_quest_tables.py
- 2026_02_19_seed_quest_leave_the_tutorial.py
- 2026_02_26_add_arena_zone_type.py
- MessageBroker
- rename_players_to_population.py
- PostgresCursor
- _find_uvicorn_processes
- .get_stats
- DomainError
- add_fastapi_users_columns.py
- add_hashed_password_column.py
- add_used_by_user_id_column.py
- rename_invites_columns.py
- Whisper Channel System
- rename_used_to_is_active.py
- test_grype.py
- description
- name
- weather_patterns
- ChatExportDialog.tsx
- VirtualizedMessageList.tsx
- xstateInspector.test.ts
- lifespan_shutdown.py
- 🔄 COMMON SCENARIOS AND SOLUTIONS
- 🔍 DEBUGGING GUIDE
- 🚀 OPTIMIZATION TIPS
- 7. Common Test Failure Solutions
- 9. Test Maintenance Best Practices
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- Memory Leak Monitoring Endpoints
- 2. Auto-Attack During Grace Period
- 3. Grace Period Visibility & Messaging
- 4. Rest/Quit Command During Combat
- 5. Rest Command Countdown Duration
- Mandatory AI Execution Contract
- 6. Rest Location (Inn/Hotel) Behavior
- 7. Reconnection During Grace Period
- 8. Grace Period After Intentional Disconnect
- MessageBroadcaster
- 9. Command Blocking During Grace Period
- Recommendations Summary
- DML Migrations
- Scenario 22 Administrative Summon
- Code Graph Entry
- DML Migrations Apply Paths
- Cosmic Horror.md
- Shared JSON schemas
- init_npc_database.py
- Base
- __init__.py
- day
- duration_hours
- month
- days
- effects
- end_hour
- Documentation Audit
- start_hour
- exits
- 1. Component Refactoring
- Migration Considerations
- Success Criteria
- Risk Assessment
- Testing Strategy
- Phase 1: Critical Foundation (COMPLETED ✓)
- Phase 2: Architecture Cleanup (COMPLETED ✓)
- Metrics and Impact
- LoggedHTTPException Pattern
- Duplicate Event Analysis
- Lessons Learned
- Test Coverage
- Phase 2: Database Layer Integration
- Phase 3: Real-Time Communication Protection
- Phase 4: File System Operations
- .spawn_npcs_on_startup
- Phase 6: Monitoring and Observability
- Future Enhancements
- Monitoring and Alerting
- Success Criteria
- Testing Strategy
- Technical Implementation Details
- ✅ Mitigation Strategies - IMPLEMENTED
- ✅ IMPLEMENTATION COMPLETED
- Performance Considerations
- ✅ Success Criteria - ACHIEVED
- fix_file
- jackson_linter.py
- RoomFilenameMigrator
- Risk Assessment
- Implementation Strategy
- Testing Strategy
- 🎉 Expected Benefits
- 🛠️ Technical Implementation Details
- 🎯 **NEXT MOST CRITICAL ITEM**
- get_invite_codes.py
- _is_npc_follow_value
- .__init__
- id
- day
- UI Screenshot Arena Cell 6,5
- message_handler_factory.py
- holiday
- Expansion Backlog (Raw)
- duration_hours
- month
- Event Subscription service_id Tracking
- id
- start_hour
- long_description
- prototype_id
- generate_invites_db.py
- short_description
- rest_location
- enabled
- plane
- sub_zone
- Frontend Design Skill
- zone
- quest_events.py
- main
- start_server.ps1
- .async_heal_player
- Local Channel System
- .to_dict
- npc_utils.py
- .is_player_muted_by_receiver
- check_invite_status.py
- analyze_coverage_gaps.py
- _apply_arena_seed_patch.py
- list_active_invites.py
- .__init__
- .start
- chat_logger
- TestCreateCharacterWithStats
- test_validate_secure_path_path_traversal_commonpath
- test_asyncio_run_guardrails.py
- description
- exits
- id
- name
- Aggro Threat Implementation Plan
- plane
- Stats
- NPC Population Field Rename
- exits
- plane
- zone
- description
- npc_spawn_modifier
- special_rules
- Codacy configuration
- Contributor Covenant Code of Conduct
- Client Security and Privacy Policies
- test_rest_command.py
- handle_time_command
- PlayerPanel.tsx
- RoomPanel.tsx
- LoginGracePeriodBanner.tsx
- mythosTheme.ts
- multiplayer-browser-helpers.d.ts
- 📊 LINT ISSUE CATEGORIZATION GUIDE
- 🚨 AI ERROR HANDLING
- Step-by-Step Remediation Process
- is_safe_filename
- POSTGRES_SEARCH_PATH for invites schema
- MagicServiceHealingMixin
- SpellMaterialsService
- ConnectionCleaner
- 3. Systematic Investigation Approach
- Graphify Code Graph
- name
- plane
- AI Development Workflow
- Pydantic Anti-Patterns Remediation (3ee32154)
- Documentation Created
- Technical Debt Addressed
- Migration Strategy
- References
- Risk Mitigation
- Architecture Overview
- ✅ Rollback Plan - MAINTAINED
- Future Considerations
- Security Considerations
- process_room_files
- validate_codacy_coverage_gate.py
- test_check_no_production_assert.py
- test_container_persistence_sql_injection.py
- Phase 2: API Routes & Validation (Days 4-7) ✅ **COMPLETED**
- ⚠️ Risk Mitigation
- Lucidity Subsystem
- metadata
- weight
- .set_main_loop
- ConnectionEvent
- PerformanceStats
- .__init__
- .__init__
- MythosMUD project overview
- test_logger
- Architecture Decision Records Index
- Test Suite Post-Merge Refactoring
- analyze-product.md
- create-spec.md
- check_no_production_assert.py
- create-tasks.md
- overrides
- execute-tasks.md
- Complexity Refactoring Edge Cases
- Cursor Workflows
- knip
- tailwindcss
- SQLAlchemy text() Async Usage
- analyze_log_file
- @types/react
- typescript
- playwright.runtime.config.ts
- package.json
- MythosMUD Worldbuilding Foundation (Raw)
- test_player_repository.py
- Path
- LLM Wiki Pattern.md
- Geography and Major Locations.md
- README.md
- MOTD Sacred Styling
- Realtime Messaging Subsystem
- Persistence Refactoring Complete
- MythosMUD Server Test Suite
- Room Subscription Timing Race
- Deprecated get_async_persistence Global
- __init__.py
- find_fstring_logging_violations
- lint_sql_guardrails.py
- High-Risk Major Package Updates
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- npc_spawn_rules_api.py
- __init__.py
- __init__.py
- PostgreSQL procedures/functions access
- __init__.py
- __init__.py
- follow_service
- Players API Code Coverage Plan
- __init__.py
- test_find_item_in_equipped_not_found
- test_get_item_description_from_prototype_no_registry
- test_get_item_description_from_prototype_no_prototype_id
- test_check_item_in_location_success
- rules
- dependencies
- test_check_equipped_item_not_found
- test_handle_item_look_in_room_drops
- .resolve_spell_target
- test_try_lookup_item_implicit_not_found
- test_check_equipped_item_no_get_equipped_items_method
- test_handle_item_look_player_no_get_inventory
- test_try_lookup_item_implicit_player_no_get_inventory
- __init__.py
- test_event_bus_publish
- test_get_username_from_user_object
- test_get_username_dict_without_username
- test_get_user_id_from_user_object
- Earth Plane
- test_validate_permission_superuser_all_actions
- test_validate_permission_viewer_limited
- test_has_permission_superuser
- test_has_permission_admin
- test_has_permission_viewer
- test_check_rate_limit_adds_request
- test_update_session_creates_new
- test_connection_helpers_impl.py
- test_update_session_no_request
- test_log_audit_event
- properties
- properties
- container
- main
- main
- SyntaxErrorFixer
- test_log_audit_event_no_request
- .load_container_from_room_json
- datetime
- test_log_audit_event_limits_size
- test_get_active_sessions_filters_expired
- test_cleanup_expired_sessions
- superuser
- test_cleanup_expired_sessions_no_expired
- test_get_admin_auth_service
- test_validate_permission_logs_audit
- test_admin_role_enum
- __init__.py
- test_admin_action_enum
- test_create_player_preferences_success
- enhanced_error_logging.py
- test_create_player_preferences_with_string_id
- test_create_player_preferences_already_exists
- test_get_player_preferences_not_found
- test_get_player_preferences_database_error
- test_update_default_channel_invalid_channel
- test_security_headers.py
- LLM Wiki Vault Schema
- test_update_default_channel_not_found
- Authoritative Environment DML
- test_mute_channel_already_muted
- test_mute_channel_system_channel
- test_unmute_channel_success
- __init__.py
- test_get_user_by_username_case_insensitive_no_session
- verify_npc_occupants.py
- test_get_professions_no_session
- test_get_players_batch_empty_list
- test_get_players_batch_with_players
- test_generate_room_id_from_zone_data_with_prefix
- test_generate_room_id_from_zone_data_needs_generation
- test_generate_room_id_from_zone_data_none_values
- test_parse_exits_json_string_valid
- test_parse_exits_json_string_invalid
- Cursor hooks.json
- test_parse_exits_json_list
- test_load_room_cache_async_rooms_none
- test_parse_exits_json_other_type
- test_process_exits_for_room_with_direction
- test_process_exits_for_room_no_direction
- Multi-Character Support System
- test_process_exits_for_room_multiple_exits
- test_process_combined_rows_with_exits
- grype.py
- main
- Any
- test_process_combined_rows_no_exits
- test_process_room_rows_with_none_zone_stable_id
- test_validate_codacy_coverage_gate.py
- test_process_room_rows_with_none_stable_id
- test_process_exit_rows_missing_direction
- test_process_exit_rows_missing_zone
- test_load_room_cache_async_warning_logging
- test_load_room_cache_async_success_with_rooms_logs_sample_ids
- test_load_room_cache_async_other_error_raises
- test_query_rooms_with_exits_async_table_not_found
- test_query_rooms_with_exits_async_other_error_raises
- test_process_exit_rows_with_full_room_ids
- test_process_exit_rows_debug_logging
- test_build_room_objects_success
- .dispatch
- test_process_room_rows_with_full_room_id
- test_build_room_objects_with_non_dict_attributes
- zone
- CI Workflow
- Agent OS
- test_restore_mp_from_meditation_at_max
- test_restore_mp_from_meditation_higher_than_rest
- test_restore_mp_from_item_restores_mp
- test_restore_mp_from_item_respects_max
- lifecycle_periodic.py
- mcp.json
- mythos_dev mythos_unit mythos_e2e Databases
- test_restore_mp_from_item_calculates_max_from_power
- test_process_tick_regeneration_sitting_position
- test_process_tick_regeneration_lying_position
- Enhanced Logging Guide
- test_mp_regeneration_service_init
- test_mp_regeneration_service_init_custom_rate
- Full Async Persistence Target
- Test Audit Executive Summary
- test_process_tick_regeneration_player_not_found
- PR Coverage Thresholds
- test_process_tick_regeneration_at_max
- test_process_tick_regeneration_restores_mp
- test_process_tick_regeneration_calculates_max_from_power
- idle_movement_handler
- test_should_idle_move_true_when_not_in_combat_and_probability_succeeds
- test_get_valid_exits_empty_room
- __init__.py
- test_get_valid_exits_no_subzone
- test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows
- test_select_exit_empty_dict
- test_select_exit_multiple_exits
- test_select_exit_weighted_home_disabled
- test_calculate_distance_to_room_same_room
- test_calculate_distance_to_room_same_subzone
- properties
- test_calculate_distance_to_room_different_subzone
- properties
- analyze_file
- main
- main
- main
- test_execute_idle_movement_no_valid_exits
- test_idle_movement_handler_init
- test_idle_movement_handler_init_no_persistence
- test_should_idle_move_disabled
- test_should_idle_move_probability_check
- test_update_player_connection_list_no_player
- test_update_player_connection_list_with_active
- Teach Impeccable Skill
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- Mandatory server startup rules
- test_register_new_connection_existing_player
- NATSEventBusBridge
- Client Updates System Audit
- test_track_player_presence_new_player
- test_track_player_presence_existing_player
- test_establish_websocket_connection_player_not_found
- mock_connection_manager
- mock_logger
- mock_name_extractor
- test_get_player_info_invalid_player_id
- test_get_player_info_player_not_found
- test_normalize_event_ids_both_provided
- test_normalize_event_ids_string_ids
- test_normalize_event_ids_none_values
- test_extract_name_from_occupant_dict_with_player_name
- test_extract_name_from_occupant_string
- test_extract_name_from_occupant_invalid_type
- test_extract_occupant_names_valid_names
- handle_explore_command
- test_extract_occupant_names_invalid_names
- test_extract_occupant_names_empty_list
- test_extract_occupant_names_none
- test_add_valid_name_to_lists_player
- Authoritative DML Seed Data
- test_add_valid_name_to_lists_npc
- test_add_valid_name_to_lists_invalid_name
- test_add_valid_name_to_lists_none_name
- test_process_dict_occupant_with_player_name
- test_process_dict_occupant_with_npc_name
- test_process_dict_occupant_with_name
- test_process_dict_occupant_invalid_name
- Python Coverage Targets
- test_build_occupants_snapshot_data_mixed
- Security Environment Variables
- test_build_occupants_snapshot_data_empty
- test_build_occupants_snapshot_data_none
- test_count_occupants_by_type_empty
- test_get_player_lucidity_tier_default
- test_validate_chat_message_fields_type_errors
- test_validate_chat_message_fields_sender_name_type_error
- test_validate_chat_message_fields_content_type_error
- lifecycle_respawn.py
- test_validate_chat_message_fields_sender_id_type_error
- test_extract_chat_message_fields
- test_convert_ids_to_uuids_uuid_objects
- test_process_message_with_retry_failure
- test_broadcast_by_channel_type_exception
- test_send_messages_to_players_no_original_content
- test_send_messages_to_players_blocked
- .test_extract_initial_player_name_with_getattr
- AsyncPersistenceLayer
- test_send_messages_to_players_with_tags
- JSON Schema Validation
- test_send_messages_to_players_invalid_player_id
- test_should_echo_to_sender_not_echo_channel
- test_should_echo_to_sender_not_chat_message
- check_file
- lucidity_migration.py
- test_should_echo_to_sender_no_message_id
- .test_try_user_object_name_with_user
- test_should_echo_to_sender_with_targets
- test_should_echo_to_sender_no_targets_already_notified
- test_echo_message_to_sender_success
- test_echo_message_to_sender_exception
- test_validate_chat_message_fields
- test_broadcast_to_room_with_filtering_exception
- test_apply_dampening_and_send_message_blocked
- test_get_player_lucidity_tier_with_uuid
- test_get_player_lucidity_tier_exception_in_processing
- test_validate_chat_message_fields_missing
- test_build_chat_event
- test_convert_ids_to_uuids
- test_convert_ids_to_uuids_none_target
- test_format_message_for_receiver
- test_get_player_lucidity_tier
- .test_extract_player_name_from_player
- .test_extract_player_name_from_user_object
- .test_extract_player_name_placeholder
- .test_validate_player_name_not_uuid_valid
- .test_is_valid_name_for_occupant_invalid
- .test_is_valid_name_valid_string
- .test_is_valid_name_none
- Map Regression Tests Proposal
- .test_is_valid_name_not_string
- .test_is_valid_name_uuid_string
- messaging_integration
- mock_connection_manager
- test_broadcast_combat_attack_personal_message_error
- test_broadcast_combat_death
- test_broadcast_combat_ended
- test_broadcast_combat_end
- test_broadcast_combat_error
- package.json
- include
- vite.userConfig.ts
- test_broadcast_player_died
- test_broadcast_player_mortally_wounded_with_attacker
- main
- test_broadcast_player_mortally_wounded_no_attacker
- test_broadcast_player_respawn
- test_broadcast_player_respawn_personal_message_error
- test_broadcast_combat_error_send_error
- test_connection_manager_lazy_load_called
- test_broadcast_combat_attack_with_attacker_id
- test_broadcast_combat_attack_no_attacker_id
- test_broadcast_player_mortally_wounded_personal_message_error
- test_broadcast_player_death_personal_message_error
- quality_fragmentation_graph.py
- test_send_dp_decay_message
- test_send_dp_decay_message_error
- test_connection_manager_setter
- test_connection_manager_setter_overrides_lazy_load
- test_messaging_integration_init
- test_connection_manager_property_lazy_load
- test_resolve_connection_manager_from_container
- MythosMUD Server Runbook Skill
- overrides
- test_resolve_connection_manager_from_container_no_manager
- test_broadcast_combat_start
- test_broadcast_combat_attack
- .test_get_death_message_custom
- .test_get_combat_start_messages
- .test_get_combat_start_messages_single_occupant
- Room Pathing Validator Implementation Spec
- validator.py CLI
- .test_get_combat_end_messages_winner_perspective
- .test_get_attack_message_defender_perspective
- _filter_lines
- fix_room_references
- player_inventory_migration.py
- populate_test_npc_databases.py
- run_bug_prevention_tests.ps1
- .test_get_attack_message_other_perspective
- .log_combat_monitoring_alert
- test_logging_handlers.py
- .test_get_attack_message_custom_npc_messages
- .test_get_attack_message_fallback_to_default
- .test_get_death_message_default
- test_unmute_player_not_muted
- Worktree Plan Metadata
- test_mute_channel_already_muted
- test_unmute_channel_success
- test_mute_global_success
- test_is_player_muted_true
- test_is_channel_muted_true
- test_is_channel_muted_false
- test_is_globally_muted_true
- test_is_admin_no_container
- test_load_player_mutes_file_not_exists
- cli.sh
- test_unmute_player_not_found
- test_normalize_to_uuid_invalid
- test_is_admin_sync_false
- test_normalize_command_removes_slash
- test_normalize_command_cleans_whitespace
- test_normalize_command_no_slash
- test_parse_command_parts_empty_string
- test_create_command_object_value_error
- test_occupant_formatter_process_player_name_for_update_valid
- test_occupant_formatter_init
- test_occupant_formatter_process_dict_occupant_for_update_fallback_name
- test_occupant_formatter_process_string_occupant_for_update_uuid
- test_occupant_formatter_separate_occupants_by_type_none
- test_occupant_formatter_is_valid_name_for_occupant_uuid
- test_occupant_formatter_is_valid_name_for_occupant_none
- test_occupant_formatter_is_valid_name_for_occupant_non_string
- test_create_command_object_type_error
- test_create_command_object_runtime_error
- test_parse_command_whitespace_only
- test_get_command_help_none
- test_get_command_help_case_insensitive
- test_get_rate_limit_info_calculates_reset_time
- test_get_rate_limit_info_filters_old_requests
- test_enforce_rate_limit_allows_request
- test_enforce_rate_limit_includes_retry_after
- Whisper NATS Subject Bug Fix
- test_stats_roll_limiter_initialized
- Event-Sourced Projector
- test_character_creation_limiter_initialized
- test_check_rate_limit_first_request
- test_check_rate_limit_different_users
- Combat verification UI-v2 five-pane layout
- test_check_rate_limit_removes_old_requests
- test_get_rate_limit_info_with_requests
- ensure_directory_exists
- webhook
- migrate_file
- main
- apply_migration
- player_event_handler_utils
- Mythos Holiday Observances
- PostgreSQL Anti-Patterns Review
- __init__.py
- test_logging_processors.py
- Lucidity System Expansion Scenarios
- WebSocket-Only Migration
- intersection_schema.json
- room_schema.json
- main
- Attack Command Not Starting Combat
- Second NPC Combat And Linkdead Findings
- Multi-Word Spell Name Parsing Failure
- Respawn Subsystem
- test_game_tick_service.py
- .test_stop_task_already_done
- .test_get_tick_count
- .test_reset_tick_count
- .test_tick_loop_handles_cancellation
- .test_tick_loop_handles_publish_failure
- .test_init_custom_interval
- .test_start_success
- .test_start_already_running
- .test_start_failure
- .test_stop_success
- __init__.py
- test_combat_audit_logger_log_combat_start
- Player Command Developer Guide
- test_combat_audit_logger_log_combat_monitoring_alert_low
- test_combat_audit_logger_get_combat_audit_summary
- test_combat_audit_logger_get_combat_audit_summary_with_player
- test_global_combat_audit_logger
- test_combat_audit_logger_log_combat_start_with_timestamp
- test_combat_audit_logger_log_combat_death
- test_create_channel_command
- test_create_go_command
- test_create_sit_command
- test_create_lie_command
- test_create_ground_command
- test_create_pickup_command
- test_create_drop_command
- test_create_put_command
- test_create_get_command
- test_create_equip_command
- Round-Based Combat
- test_create_unequip_command
- pyrightconfig.json
- test_create_mute_command
- test_create_unmute_command
- core/fixer.py
- test_create_mute_global_command
- test_create_unmute_global_command
- properties
- check_file_for_logging_issues
- e2e_reset_players.py
- test_create_add_admin_command
- test_create_admin_command
- test_create_mutes_command
- NPC Occupants Verification Summary
- test_create_status_command
- test_command_factory_init
- test_create_time_command
- test_create_whoami_command
- Combat Client Crash
- Respawn Death Screen Loop Limbo ID Mismatch
- test_create_who_command
- NPC Combat Start Race Condition
- test_create_quit_command
- MythosMUD Full-Stack Feature Skill
- test_create_logout_command
- Enhanced Structured Logging System
- test_create_rest_command
- test_create_punch_command
- test_create_kick_command
- test_create_strike_command
- test_create_alias_command
- test_create_aliases_command
- test_create_unalias_command
- test_create_help_command
- test_create_npc_command
- Magic and Spellcasting System
- Lucidity Tiers
- test_create_spawn_command
- test_create_summon_command
- test_create_teleport_command
- Four-Level Room Hierarchy
- test_create_goto_command
- test_create_shutdown_command
- test_command_factory_has_create_methods
- test_create_spell_command
- test_create_learn_command
- test_command_factory_create_existing_command
- test_create_say_command
- test_create_local_command
- test_create_system_command
- test_create_emote_command
- test_create_me_command
- test_create_whisper_command
- Canonical Worktree Layout
- __init__.py
- combat_validator
- Modular E2E Test Suite
- Playwright MCP Scenarios
- .to_dict
- AI PR Reviewer Instructions
- Quest System Gap
- ArkanWolfshade Say Chat UI
- Container Contents Synchronization Bug
- description
- environment
- name
- description
- environment
- lock_state
- fix_file
- check_codacy_yaml
- safe_subprocess.py
- TestPostgresConnectionPool
- MythosMUD Pre-Commit Checklist Skill
- __init__.py
- Vite HTML Entry
- Client Layer Layout
- Zustand Stores
- Codacy CLI via WSL on Windows
- Official Test Credentials
- R'lyeh
- Mythos Magic
- generate_schema_from_dev.ps1
- make verify-schema
- Owner and App Roles Per Environment
- Hate List
- Aggro Stability Margin
- UpdateAggro
- Local Chat Channel
- Advanced Chat Channels Tasks
- Whisper Chat Channel
- Architecture Remediation Plan
- Configuration Refactoring Complete
- WebSocket and SSE Dual Connections
- Simultaneous WebSocket and SSE
- Dual Connection System Tasks
- Dual Connection Troubleshooting Guide
- NPC Lifecycle Manager
- NPC Startup Service
- PLANNING.md Single Source of Truth
- Legacy Test File Consolidation
- Test Migration Validation
- Test Refactoring Executive Summary
- Async Code Review Post Migration
- Phase 2 Service Layer Migration
- MythosMUD Product Requirements
- Configuration File Tuples
- .env.local Secrets Pattern
- Container Item System
- Cursor Lifecycle Hooks
- Database Pool Configuration
- Migration 019 Verification
- ConnectionManager Modular Split
- Admin Commands Subsystem
- Emote / Pose Subsystem
- Follow Subsystem
- Whisper System Production-Ready
- Structured Logging Correct Patterns
- mythosmud
- verify_schema_match.sh
- HealthRepository
- Claude Pointer (.claude/CLAUDE.md)
- RoomRepository
- FastAPI
- GET /v1/monitoring/health
- PostgreSQL Player Persistence
- World Loading
- Message Validator
- Logging Best Practices
- Scenario Group Execution
- Per-Recipient Whisper Rate Limiting
- invites table
- Mythos-themed invite codes
- RoomSubscriptionManager
- jsonschema dependency
- Vite Best-Practices Remediation
- Scenario 32 Disconnect Grace Period
- plane
- id
- plane
- zone
- properties
- apply_migration
- _resolved_npm
- verify_tutorial_migrations.ps1
- F-String Logging Violations
- Catatonic Movement Prevention Bug
- Rooms List SQL ::uuid[] Parameter Conflict
- Character Creation Revamp
- Dead Code Cleanup Completion
- Single Session Per User
- Test Warning Remediation
- Random Stats Generator Planning
- Party System Reference
- Test File Migration Mapping
- Disconnect Grace Period Rest Coverage
- check_postgresql.sh
- setup_postgresql_test_db.sh
- AnyIO vs Asyncio Comparison
- GameState Event Projection
- Easy Coverage Wins
- Truly Dead Code
- FastAPI Code Review
- Dependency Review Workflow
- 10 Concurrent Players Load Test
- Cursor Rules as Canonical Config
- Gladiator Ring Arena
- Logging Aggregator Verification
- Memory Leak Remediation
- Playwright DI Migration Validation
- Server Authority Remediation
- Scenario 34 Two Players Same Room Visibility
- remove_dir
- load_seed_data
- safe_print
- parse_lint_findings
- verify_e2e_users_seeded.py
- NPCs Not Updating On Player Movement
- Combat Messages Dual Panel Display
- Test Suite Stall After Performance Comparison
- Ground Command
- Rest Subsystem
- LevelService
- httpOnly Cookie Token Storage
- Combat Health Persistence Bug
- container_test_client Fixture
- Panel Layout Libraries Spec
- players.current_room_id Index Gap
- E2E Scenario Conversion
- CWE-209 Information Exposure
- ftfy Unicode Normalization
- Temporal NPC Schedules
- Vite Logo SVG
- wsl-bashrc-codacy.sh
- ensure_codacy_coverage_reporter_ci.sh
- ensure_uv_ci.sh
- generate_schema_from_dev.sh script
- install_ci_dependencies.sh
- InstanceManager
- React Node Upgrade Plan
- Code Review Import Analysis
- Mid-Run Disconnect Reasons
- Async Facades Implementation Summary
- bcrypt Fresh Session Isolation
- NumPy Code Review
- Git Submodule Setup
- Temporal System Research
- Error Monitoring Scripts
- Deprecated get_event_loop Antipattern
- ApplicationContainer
- Chat Messages Not Displayed to Sender (Bug #2)
- Mute Command Server Error (Bug #1)
- mythos_e2e Database
- Playwright MCP core-tabs Capability
- Playwright MCP Timing Limitation
- AGENTS.md Authoritative Guidance
- Codacy High/Critical Baseline
- Bug Report Issue Template
- Issue Template Config
- Item System Blueprint
- factory.py
- test_nats_service.py
- authoritative_schema.sql
- CoC Spells Proposal
- Convert E2E Scenarios to Playwright CLI
- Temporal System 4:1 Calendar Conversion
- Critical File Coverage Improvement
- Eliminate Raw CRUD SQL
- Follow Command Feature
- Limbo Arena Zone
- 10-Second Login Grace Period
- Codacy 8100+ Remediation
- PostgreSQL Audit Remediation
- React Best-Practices Remediation
- Requests Best Practices Remediation
- app.state Global State Anti-Pattern
- apply_container_migrations.py
- gen_arena_uuids.py
- _scan_dml_blank_before_terminator.py
- Private vulnerability disclosure
- player_respawned Event Payload Gap
- passive_lucidity_flux_tick Performance Alert
- Movement Message Dual Panel Routing
- Missing Hourly Clock Chimes
- UI Panel Resize Bug
- Three-Column Panel Wireframe Layout
- E2E Multiplayer Playbook Findings
- Character Info Combat HP Update Delay
- Missing Delirium Respawn Feature
- Admin Look Mob Stats Bug
- Create New Character Rendering Gap
- 4pt Spacing System
- ADR Structure (Status/Context/Decision)
- Eight Interactive States
- Color and Contrast Reference
- Motion Design Reference
- Responsive Design Reference
- Typography Reference
- UX Writing Reference
- get_logger Structured Logging
- Harden Skill
- MythosMUD LLM Wiki Skill
- Online via last_active Threshold
- Local agent task notes
- Admin Teleport Feature
- Argon2 Security Review
- datetime.utcnow Deprecation Fix
- Semgrep Windows UTF-8 Fix
- Documentation Issue Template
- MythosMUD Local Data Directory
- Click Best-Practices Remediation
- Code Practice Rules Reference Doc
- GitHub Actions Remediation
- Pytest Best-Practices Remediation
- Playwright Test Report UI
- Docker Best Practices Rule
- finalize_build_touch Rebuild Trigger

## God Nodes (most connected - your core abstractions)
1. `ValidationError` - 537 edges
2. `get_logger()` - 506 edges
3. `DatabaseError` - 432 edges
4. `LoggedHTTPException` - 401 edges
5. `User` - 306 edges
6. `AliasStorage` - 230 edges
7. `Player` - 200 edges
8. `AsyncPersistenceLayer` - 183 edges
9. `CombatService` - 181 edges
10. `ConnectionManager` - 172 edges

## Surprising Connections (you probably didn't know these)
- `Arkham City Graph PNG` --semantically_similar_to--> `Simple Room Graph - Arkham City`  [INFERRED] [semantically similar]
  data/local/arkham_city_graph.png → data/local/simple_room_visualization.html
- `Combat verification UI-v2 five-pane layout` --conceptually_related_to--> `Dark terminal-first aesthetic`  [INFERRED]
  .playwright-mcp/combat-verification-screenshot.png → .impeccable.md
- `Grype SCA exclude paths` --semantically_similar_to--> `Codacy exclude_paths`  [INFERRED] [semantically similar]
  .grype.yaml → .codacy.yml
- `_handle_admin_status_command()` --indirect_call--> `player_service()`  [INFERRED]
  server/commands/admin_commands.py → docs/examples/logging/fastapi_integration.py
- `_get_player_service_from_app()` --indirect_call--> `player_service()`  [INFERRED]
  server/commands/admin_setlucidity_command.py → docs/examples/logging/fastapi_integration.py

## Import Cycles
- 1-file cycle: `scripts/psscriptanalyzer.ps1 -> scripts/psscriptanalyzer.ps1`
- 1-file cycle: `server/structured_logging/logging_handlers.py -> server/structured_logging/logging_handlers.py`
- 2-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelUnreadBump.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 3-file cycle: `client/src/components/panels/chatPanelChannelFilter.ts -> client/src/components/panels/chatPanelChannelVisibility.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelChannelFilter.ts`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `server/npc/spawning_service.py -> server/services/npc_combat_integration_service.py -> server/realtime/connection_manager.py -> server/realtime/integration/game_state_provider.py -> server/services/npc_instance_service.py -> server/npc/spawning_service.py`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`

## Hyperedges (group relationships)
- **Command development guide set** — docs_command_handler_patterns_doc, docs_command_models_reference_doc, docs_command_security_guide_doc, docs_command_testing_guide_doc [INFERRED 0.85]
- **Linting and complexity tooling docs** — docs_linting_complexity_alignment_doc, docs_linting_pylint_unique_findings_doc, docs_linting_ruff_pylint_mapping_doc, docs_lizard_complexity_findings_doc [INFERRED 0.85]
- **PostgreSQL guidance and audit docs** — docs_postgresql_anti_patterns_review_doc, docs_postgresql_audit_report_2026_doc, docs_postgresql_contributor_guide_doc [INFERRED 0.85]
- **Test quality audit and optimization docs** — docs_test_audit_executive_summary_doc, docs_test_quality_audit_report_doc, docs_test_value_distribution_doc, docs_test_optimization_roadmap_doc, docs_test_pruning_candidates_doc, docs_test_timing_analysis_doc [INFERRED 0.95]
- **Realtime messaging stack** — docs_architecture_decisions_adr_003_dual_event_systems_eventbus_nats_eventbus, docs_architecture_decisions_adr_003_dual_event_systems_eventbus_nats_nats, docs_architecture_decisions_adr_004_websocket_only_realtime_websocket_only, docs_architecture_distributed_eventbus_nats_nats_eventbus_bridge [INFERRED 0.85]
- **Client panel separation triad** — docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_chat_panel, docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_game_log_panel, docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_commands_panel [EXTRACTED 1.00]
- **Dual connection documentation set** — docs_archive_dual_connection_api_reference_dual_connection_api, docs_archive_dual_connection_client_guide_dual_connection_client, docs_archive_dual_connection_deployment_guide_dual_connection_deploy, docs_archive_dual_connection_api_reference_websocket_sse_dual [INFERRED 0.95]
- **Uncoordinated NPC startup spawners** — docs_archive_npc_startup_duplication_analysis_npc_startup_service, docs_archive_npc_startup_duplication_analysis_npc_lifecycle_manager, docs_archive_npc_startup_duplication_analysis_npc_population_controller [EXTRACTED 1.00]
- **Lucidity hallucination effects group** — docs_archive_lucidity_system_lucidity_system, docs_archive_phantom_hostile_requirements_phantom_hostiles, docs_archive_reversed_compass_directions_requirements_reversed_compass [EXTRACTED 1.00]
- **Death, rest, and rescue lifecycle** — docs_subsystems_subsystem_status_effects_design_status_effects, docs_subsystems_subsystem_respawn_design_respawn_subsystem, docs_subsystems_subsystem_rescue_design_rescue_subsystem, docs_subsystems_subsystem_rest_design_rest_subsystem [INFERRED 0.75]
- **Combat feature plans cluster** — plans_combat_round_system_refactor, plans_combat_bugs_investigation_and_fixes, plans_flee_command_and_effect, plans_first_weapon_switchblade [INFERRED 0.85]
- **Effects and grace period cluster** — plans_effects_system_adr_and_implementation, plans_effects_system_implementation, plans_disconnect_grace_period_and_rest, plans_effects_login_warded [EXTRACTED 1.00]
- **Memory leak metrics and remediation** — plans_memory_leak_metrics_collection, plans_memory_leak_remediation, plans_memory_closed_websockets_deque [EXTRACTED 1.00]
- **Quest gap analysis to implementation** — plans_mud_subsystems_gap_analysis, plans_mud_quest_gap, plans_quest_subsystem_implementation, plans_quest_system [EXTRACTED 1.00]
- **Design skills depend on frontend-design** — skills_frontend_design, skills_adapt, skills_animate, skills_arrange, skills_bolder, skills_clarify, skills_colorize, skills_critique, skills_delight, skills_distill, skills_extract [EXTRACTED 1.00]
- **WebSocket migration and client message pipeline** — plans_websocket_only_migration, plans_websocket_best_practices_remediation, plans_unify_client_message_handling, plans_websocket_only_architecture [INFERRED 0.85]
- **Frontend-design reference docs** — skills_frontend_design_ref_color_and_contrast, skills_frontend_design_ref_interaction_design, skills_frontend_design_ref_motion_design, skills_frontend_design_ref_responsive_design, skills_frontend_design_ref_spatial_design, skills_frontend_design_ref_typography, skills_frontend_design_ref_ux_writing [EXTRACTED 1.00]
- **MythosMUD operational skills cluster** — skills_mythosmud_server_runbook, skills_mythosmud_pre_commit_checklist, skills_mythosmud_test_writing, skills_mythosmud_worktree_workflow, skills_one_server_only_rule, skills_definition_of_done [INFERRED 0.85]
- **Design skills requiring teach-impeccable** — skills_teach_impeccable, skills_onboard, skills_optimize, skills_overdrive, skills_polish, skills_quieter, skills_typeset, skills_design_context_persistence [EXTRACTED 1.00]
- **AI execution improvement documentation set** — e2e_tests_ai_execution_improvements_mandatory_execution_protocol, e2e_tests_ai_executor_quick_reference_seven_commandments, e2e_tests_execution_guards_max_step_attempts, e2e_tests_improvements_summary_infinite_loop_prevention [EXTRACTED 1.00]
- **Whisper Phase 3 NATS review artifacts** — e2e_tests_phase_3_complete_summary_phase_3_code_review, e2e_tests_phase_3_code_review_findings_nats_subject_manager, e2e_tests_phase_3_task_2_subject_manager_review_dual_path_subject_construction, e2e_tests_phase_3_task_3_documentation_review_nats_subject_patterns_doc [EXTRACTED 1.00]
- **Whisper remediation documentation cluster** — e2e_tests_whisper_system_investigation_report_whisper_system_investigation, e2e_tests_whisper_fix_phase_1_complete_whisper_nats_subject_bug_fix, e2e_tests_whisper_testing_complete_whisper_system_production_ready, e2e_tests_work_completed_and_remaining_whisper_work_completed [EXTRACTED 1.00]
- **Multi-character scenario group 27-30** — e2e_tests_scenarios_scenario_27_character_selection_character_selection, e2e_tests_scenarios_scenario_28_multi_character_creation_multi_character_creation, e2e_tests_scenarios_scenario_29_character_deletion_character_soft_deletion, e2e_tests_scenarios_scenario_30_character_name_uniqueness_case_insensitive_name_uniqueness [EXTRACTED 1.00]
- **Skills scenario group 39-41** — e2e_tests_scenarios_scenario_39_skills_new_tab_skills_new_tab, e2e_tests_scenarios_scenario_40_skills_command_skills_slash_command, e2e_tests_scenarios_scenario_41_skills_after_creation_skills_after_creation [EXTRACTED 1.00]
- **Visibility and combat scenarios 34-36** — e2e_tests_scenarios_scenario_34_two_players_same_room_same_room_visibility, e2e_tests_scenarios_scenario_35_player_combat_player_combat, e2e_tests_scenarios_scenario_36_movement_visibility_movement_visibility [EXTRACTED 1.00]
- **NPC occupants display investigation cluster** — investigations_sessions_2025_01_28_session_npc_display_final_fixes_npc_display_fixes, investigations_sessions_2025_01_28_session_npc_occupants_verification_summary_npc_occupants_verification, investigations_sessions_2025_01_29_session_001_npc_occupants_display_issue_dual_tracking, investigations_sessions_2025_01_30_session_001_npcs_not_updating_on_player_movement_npc_movement_update, investigations_sessions_2025_01_xx_session_npc_spawning_occupants_issue_npc_spawning_display, investigations_sessions_2025_01_xx_session_occupants_npc_display_flat_occupants_list [INFERRED 0.85]
- **Container inventory synchronization cluster** — investigations_remediation_plans_2025_01_27_container_sync_remediation_container_sync_bug, investigations_sessions_2025_01_27_session_001_inventory_slot_calculation_bug_inventory_slot_bug, investigations_sessions_2025_01_27_session_001_inventory_slot_calculation_bug_dual_storage [EXTRACTED 1.00]
- **Combat messaging and NATS failure cluster** — investigations_sessions_2025_11_19_session_001_nats_message_validation_failure_nats_event_data, investigations_sessions_2025_11_19_session_002_combat_client_crash_combat_client_crash, investigations_sessions_2025_11_19_session_002_combat_message_uuid_display_combat_uuid_display, investigations_sessions_2025_11_19_session_003_combat_messages_dual_panel_display_combat_dual_panel, investigations_sessions_2025_12_01_session_npc_death_messages_not_displaying_npc_death_messages [INFERRED 0.85]
- **Death limbo and respawn investigation cluster** — investigations_sessions_2025_11_19_session_005_respawn_death_screen_loop_limbo_room_id_mismatch, investigations_sessions_2025_11_20_respawn_persistence_bug_investigation_respawn_persistence, investigations_sessions_2025_11_20_session_002_death_posture_bugs_death_posture [INFERRED 0.85]
- **December 3 character and occupants UI cluster** — investigations_sessions_2025_12_03_final_summary_dec3_summary, investigations_sessions_2025_12_03_session_001_character_info_panel_character_info_stats, investigations_sessions_2025_12_03_session_002_room_occupants_display_occupants_duplicates [EXTRACTED 1.00]
- **Spell command and casting failure cluster** — investigations_sessions_2025_12_14_session_001_spell_commands_failure_spell_commands_missing, investigations_sessions_2025_12_14_session_002_spell_cast_failure_multiword_spell, investigations_sessions_2025_12_14_session_003_minor_heal_casting_delay_missing_async_heal, investigations_sessions_2025_12_14_session_004_heal_spell_casting_failure_session_boundary [INFERRED 0.95]
- **Explored rooms filtering and minimap cluster** — investigations_sessions_2025_12_07_session_sql_syntax_error_rooms_list_sql_cast_param, investigations_sessions_2026_01_04_session_minimap_explored_rooms_bug_minimap_explored [INFERRED 0.75]
- **Combat start XP and second-NPC cluster** — investigations_sessions_2025_12_08_session_combat_start_failure_missing_await, investigations_sessions_2025_12_14_session_002_xp_award_error_investigation_xp_award_error, investigations_sessions_2026_02_04_combat_second_npc_and_linkdead_findings_second_npc_combat [INFERRED 0.75]
- **Event projection and room handoff authority path** — client_src_components_ui_v2_eventlog_events_schema_event_projector, client_src_components_ui_v2_eventlog_events_schema_room_state, client_src_components_ui_v2_eventlog_handoffs_enter_room_rr, client_src_components_ui_v2_eventlog_handoffs_server_authority [EXTRACTED 1.00]
- **Wireframe panels realized in terminal game UI** — client_wireframe_ui_wireframe, playwright_report_data_terminal_game_ui, client_wireframe_three_column_layout [INFERRED 0.85]
- **Say chat dual-player screenshot pair** — playwright_report_data_aw_say_chat_ui, playwright_report_data_ithaqua_say_reply_ui, playwright_report_data_say_channel [INFERRED 0.85]
- **Earth-plane major geography locations** — data_mythosmud_obsidian_raw_sources_mythosmud_worldbuilding_earth_plane, data_mythosmud_obsidian_raw_sources_geography_major_locations_arkham_city, data_mythosmud_obsidian_raw_sources_geography_major_locations_innsmouth, data_mythosmud_obsidian_raw_sources_geography_major_locations_rlyeh [EXTRACTED 1.00]
- **MOTD listed known zones** — data_local_motd_message_of_the_day, data_local_motd_arkham_city, data_local_motd_innsmouth, data_local_motd_katmandu [EXTRACTED 1.00]
- **GitHub security scanning suite** — github_workflows_codeql_codeql_workflow, github_workflows_dependency_review_dependency_review_workflow, github_workflows_scorecards_scorecard_workflow [INFERRED 0.75]
- **Contribution and triage templates** — github_issue_template_bug_report_bug_report_template, github_issue_template_documentation_documentation_template, github_issue_template_feature_request_feature_request_template, github_pull_request_template_pr_template [INFERRED 0.85]
- **Historical pre-authoritative DDL verification snapshots** — db_verification_ddl_status_historical_partial_status, db_verification_ddl_final_status_historical_final_status, db_verification_ddl_verification_summary_historical_summary [EXTRACTED 1.00]
- **Dual SCA Grype local and Trivy Codacy** — codacy_readme_grype_vs_trivy, codacy_codacy_yaml_trivy_tool, codacy_tools_configs_trivy_trivy_scan_config [EXTRACTED 1.00]
- **Lizard complexity analysis stack** — codacy_codacy_yaml_lizard_tool, codacy_tools_configs_lizard_lizard_thresholds, codacy_tools_configs_lizard_ccn_minor_threshold, codacy_tools_configs_lizard_file_nloc_medium [EXTRACTED 1.00]
- **WebSocket message accept-validate-route-broadcast pipeline** — server_realtime_readme_websocket_api, server_realtime_readme_connection_manager, server_realtime_readme_message_validator, server_realtime_readme_nats_message_handler, server_realtime_readme_room_broadcasts [EXTRACTED 1.00]
- **Local server start/stop lifecycle scripts** — scripts_readme_start_server, scripts_readme_stop_server, scripts_readme_start_local, scripts_readme_port_54768 [EXTRACTED 1.00]
- **JSON validate generate merge seed pipeline** — scripts_static_data_readme_generate_sql_mjs, scripts_static_data_readme_ajv_validation, scripts_static_data_readme_world_emotes_sql, scripts_static_data_readme_canonical_dml_merge, scripts_static_data_readme_uuid_v5_namespace [EXTRACTED 1.00]
- **Room validator core modules** — tools_room_toolkit_room_validator_readme_room_loader, tools_room_toolkit_room_validator_readme_schema_validator, tools_room_toolkit_room_validator_readme_path_validator, tools_room_toolkit_room_validator_readme_reporter, tools_room_toolkit_room_validator_readme_fixer [EXTRACTED 1.00]
- **Core monitoring stack services** — monitoring_docker_compose_prometheus, monitoring_docker_compose_alertmanager, monitoring_docker_compose_grafana [EXTRACTED 1.00]
- **Alert evaluation and routing pipeline** — monitoring_prometheus_yml_prometheus_config, monitoring_mythos_alerts_yml_alert_rules, monitoring_alertmanager_yml_alertmanager_config [EXTRACTED 1.00]
- **Agent instruction routing chain** — claude_md_agent_router, agents_md_agent_instructions, user_rules_md_server_startup_rules [EXTRACTED 1.00]
- **Quality and security tooling cluster** — codacy_yml_codacy_configuration, pre_commit_config_yaml_pre_commit_hooks, semgrep_yml_no_select_star, bandit_yml_bandit_config, grype_yaml_sca_excludes [INFERRED 0.85]
- **UI-v2 design intent and screenshots** — impeccable_md_design_context, playwright_mcp_combat_verification_screenshot_ui_v2_layout, playwright_mcp_death_respawn_ui_test_ui_v2_layout [INFERRED 0.85]

## Communities (1910 total, 619 thin omitted)

### Community 0 - ".get_instance"
Cohesion: 0.01
Nodes (307): close_db(), get_test_database_url(), Get test override database URL., Set test override database URL., set_test_database_url(), DatabaseManager, ensure_database_directory(), get_database_path() (+299 more)

### Community 1 - "connection_manager.py"
Cohesion: 0.01
Nodes (269): cleanup_dead_websocket_impl(), delegate_connection_cleaner(), delegate_connection_cleaner_sync(), delegate_error_handler(), delegate_game_state_provider(), delegate_game_state_provider_sync(), delegate_health_monitor(), delegate_health_monitor_sync() (+261 more)

### Community 2 - "AsyncPersistenceLayer"
Cohesion: 0.03
Nodes (88): Initialize the spell targeting service.          Args:             target_resolu, Attach or replace the player combat service (shared instance wiring)., PlayerCombatService, UUID, Attach NPC combat integration for UUID/XP mapping (post-construction wiring)., Track a player's combat state.          Args:             player_id: ID of th, Get a player's combat state.          Args:             player_id: ID of the, Clear a player's combat state.          Args:             player_id: ID of th (+80 more)

### Community 3 - "test_alias_commands.py"
Cohesion: 0.02
Nodes (161): Create CombatService with NATS and register it. Assumes NATS is connected., CombatStartedEvent, Event fired when combat begins., combat_room_id_for_npc_spell(), Internal helpers for spell_effects.py (coercion, combat room lookup).  Keeps the, Active combat room_id for an NPC, if any., CombatResult, Result of a combat action. (+153 more)

### Community 4 - "test_security_validator.py"
Cohesion: 0.02
Nodes (163): Unit tests for security validation utilities.  Tests the security validator func, Test that comprehensive sanitization removes null bytes., Test that comprehensive sanitization removes control characters., Test that comprehensive sanitization normalizes newlines to spaces., Test that comprehensive sanitization preserves tabs., Test that comprehensive sanitization removes zero-width characters., Test validating empty message content., Test validating normal message content. (+155 more)

### Community 5 - "useMythosAppState.ts"
Cohesion: 0.06
Nodes (73): CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), extractErrorMessageFromResponseBody(), fetchCharactersList(), handleRefreshCharactersFailure(), AuthSlice, authSliceReducer() (+65 more)

### Community 6 - "types.ts"
Cohesion: 0.02
Nodes (134): _build_container_data_from_dict(), close_container(), _convert_container_dict_to_container_data(), _convert_datetime_to_iso(), _convert_inventory_list_to_inventory_stacks(), _convert_uuid_to_string(), open_container(), Any (+126 more)

### Community 7 - "inventory_pickup_command.py"
Cohesion: 0.02
Nodes (110): BaseCommand, BaseModel, Base class for all MythosMUD commands.      Provides common validation and secur, Unit tests for base command models and enums.  Tests the Direction and CommandTy, Test CommandType enum contains combat commands., Test CommandType enum contains magic commands., Test CommandType enum values can be compared to strings., Test BaseCommand can be instantiated (though it's abstract). (+102 more)

### Community 8 - "CombatService"
Cohesion: 0.03
Nodes (81): NPCCombatIntegrationService, Return combat messaging integration for room broadcasts (e.g. aggro switches)., Return combat service dependency for integration collaborators., Handle NPC death and related effects.          Args:             npc_id: ID of t, Get the last attacker for an NPC., Clear combat memory for an NPC., Service for integrating NPCs with the combat system.      This service handles:, Initialize the NPC combat integration service.          Args:             event_ (+73 more)

### Community 9 - "PlayerRoomEventHandler"
Cohesion: 0.17
Nodes (17): normalize_database_url(), Normalize database URL for asyncpg.      Args:         database_url: Original da, create_invite_in_db(), generate_invite_code(), generate_unique_codes(), get_existing_codes(), main(), parse_expires_date() (+9 more)

### Community 10 - "MythosMUDError"
Cohesion: 0.01
Nodes (305): _CircuitBreakerResult, JSONResponse, Pydantic error handler for consistent error processing.  This module provides a, Initialize the Pydantic error handler.          Args:             context: Optio, Standardized error response formats for all API endpoints.  This module provides, Handle MythosMUDError instances., Determine ErrorType from MythosMUDError instance., Generate user-friendly message for error. (+297 more)

### Community 11 - "test_command_factories_inventory.py"
Cohesion: 0.02
Nodes (140): Unit tests for inventory command factory helper functions.  Tests the helper fun, Test create_equip_command() with item name and inferred slot., Test create_unequip_command() with slot., Test create_unequip_command() with item name., Test create_inventory_command() creates InventoryCommand., Test create_inventory_command() raises error with args., Test create_pickup_command() with numeric index., Test create_pickup_command() with quantity. (+132 more)

### Community 12 - "LoggedHTTPException"
Cohesion: 0.02
Nodes (183): ContainerLockState, Dependency to require admin permissions.      Args:         current_user: Curren, require_admin_user(), handle_close_container_exceptions(), handle_loot_all_exceptions(), handle_open_container_exceptions(), handle_transfer_items_exceptions(), Exception (+175 more)

### Community 13 - "get_logger"
Cohesion: 0.01
Nodes (417): _create_npc_services_on_app(), Create NPC spawning, lifecycle, population services and instance service. Attach, NPCBundle, NPC bundle: lifecycle manager, spawning service, population controller.  Depends, NPC services: lifecycle, spawning, population control., Initialize NPC services and load definitions., EventBus, Event bus for MythosMUD.  This module provides the EventBus class that implement (+409 more)

### Community 14 - "npc_base.py"
Cohesion: 0.14
Nodes (9): NPCCommunicationIntegration, Handle a message received by an NPC from a player.          Args:             np, Process a message to determine if the NPC should respond.          Args:, Subscribe an NPC to messages in a specific room.          Args:             npc_, Unsubscribe an NPC from messages in a specific room.          Args:, Integrates NPCs with the existing chat and whisper systems.      This class prov, Initialize the NPC communication integration.          Args:             event_b, Send a message from an NPC to a room.          Args:             npc_id: ID of t (+1 more)

### Community 15 - "player_connection_setup.py"
Cohesion: 0.09
Nodes (37): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions.  This module handles the setup tasks when a p, Broadcast a structured entry event to other occupants (excluding the newcomer). (+29 more)

### Community 16 - "User"
Cohesion: 0.02
Nodes (179): IntegrityError, Container for subprocess result data (returncode, stdout, stderr)., Result, generate_unique_bogus_email(), AsyncSession, Generate a unique bogus email address for a user.      This function creates a b, _authenticate_user_credentials(), _check_shutdown_status() (+171 more)

### Community 17 - "ErrorContext"
Cohesion: 0.08
Nodes (29): LoggedException, Exception, Keyword arguments accepted by create_error_context and ErrorContext()., Marker base class indicating an exception has already produced a log entry., Return True if this exception instance has already been logged., _as_bound_logger(), BoundLogger, Unit tests for enhanced_logging_config helpers.  Covers log_exception_once ded (+21 more)

### Community 18 - "test_wearable_container_service.py"
Cohesion: 0.02
Nodes (127): _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Handle unequipping a wearable container item.          Preserves the container a, Get all wearable containers for a player.          Args:             player_id:, Add items to a wearable container.          Args:             player_id: UUID of (+119 more)

### Community 19 - ".state"
Cohesion: 0.10
Nodes (23): GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation.          Args:, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names.          CRITICAL: NEVER (+15 more)

### Community 20 - "ContainerComponent"
Cohesion: 0.04
Nodes (58): get_container_and_player_for_loot_all(), handle_container_service_error(), ContainerComponent, InventoryStack, UUID, Handle ContainerServiceError with appropriate status codes.      Args:         e, Get container and player data for loot_all operation., Transfer all items from container to player, returning updated container and inv (+50 more)

### Community 21 - "ContainerService"
Cohesion: 0.02
Nodes (84): CombatInstance, UUID, Apply damage to this participant and determine resulting death states., Represents an active combat instance., Get the participant whose turn it is., Advance to the next round - all participants act each round.          In round-b, Check if combat should end.          CRITICAL: Combat should NOT end when a play, Get all participants that are not dead (includes mortally wounded players at 0 D (+76 more)

### Community 22 - "test_npc_combat_integration_service.py"
Cohesion: 0.03
Nodes (58): mock_async_persistence(), mock_combat_service(), mock_connection_manager(), Unit tests for NPC combat integration service - NPC-initiated aggro combat paths, Test handle_npc_attack_on_player returns False when NPC instance cannot be found, Test handle_npc_attack_on_player returns False when NPC is dead., Test handle_npc_attack_on_player returns False when combat location is invalid., Test handle_npc_attack_on_player returns False when combat service is missing. (+50 more)

### Community 23 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (129): DropCommand, EquipCommand, GetCommand, PickupCommand, PutCommand, Strip and validate search term., Ensure either index or search_term is provided., Validate target slot value.          Args:             value: The target slot va (+121 more)

### Community 24 - "test_health_service.py"
Cohesion: 0.06
Nodes (66): get_health_status(), Get comprehensive system health status with timeout protection.      This endpoi, ConnectionsComponent, DatabaseComponent, HealthComponents, HealthErrorResponse, HealthResponse, BaseModel (+58 more)

### Community 25 - "error_types.py"
Cohesion: 0.03
Nodes (69): MythosValidationError, Error handlers package for MythosMUD.  This package provides specialized error h, convert_pydantic_error(), _ExtractedErrorInfo, _ExtractedFieldErrorInfo, handle_pydantic_error(), TypedDict, Unpack (+61 more)

### Community 26 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (117): Unit tests for NATS message handler.  Tests the NATSMessageHandler class lifecyc, Test _subscribe_to_chat_subjects() raises error when subject manager not availab, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes., Test _unsubscribe_from_subject() handles subscription not found. (+109 more)

### Community 27 - "test_command_validator.py"
Cohesion: 0.05
Nodes (66): Validate lock_state parameter.      Args:         lock_state: Lock state to v, validate_lock_state(), _build_item_dict(), _call_create_container_procedure(), create_container_async(), delete_container_async(), fetch_container_items_async(), _finalize_container_creation() (+58 more)

### Community 28 - "test_look_npc.py"
Cohesion: 0.02
Nodes (166): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_description(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result() (+158 more)

### Community 29 - "Room"
Cohesion: 0.09
Nodes (18): Instance, InstanceManager, Room, UUID, Return template rooms matching instance_template_id., Clone template rooms into instance-scoped rooms with remapped exits., Extract stable_id from room - use room.id if it looks like a full path., Remap exit targets: same-instance rooms use instance IDs, outside exits use fixe (+10 more)

### Community 30 - ".create_instance"
Cohesion: 0.13
Nodes (21): create_teleport_effect_message(), Create teleport effect message for visual display.      Args:         player_nam, Unit tests for admin_commands helper functions.  Tests helper functions in admin, Test DIRECTION_OPPOSITES dictionary contains correct mappings., Test create_teleport_effect_message() for teleport departure., Test create_teleport_effect_message() for teleport departure with direction., Test create_teleport_effect_message() for teleport arrival., Test create_teleport_effect_message() for teleport arrival with direction. (+13 more)

### Community 31 - "UUID"
Cohesion: 0.02
Nodes (65): Any, Player, UUID, Get the first WebSocket connection ID for a player (backward compatibility)., Check if a player has any WebSocket connections., Get the number of connections for a player by type., Subscribe a player to a room (compatibility method)., Unsubscribe a player from a room (compatibility method). (+57 more)

### Community 32 - "game.py"
Cohesion: 0.05
Nodes (49): InventoryItem, Player, BaseModel, Represents an item in a player's inventory., Pydantic Player model for game logic and validation.      This is separate from, Add an item to the player's inventory.          Args:             item_id: Uniqu, Remove an item from the player's inventory.          Args:             item_id:, Add a status effect to the player.          Args:             effect: StatusEffe (+41 more)

### Community 33 - "Invite"
Cohesion: 0.05
Nodes (45): datetime, Request, UUID, Mark an invite as used by a specific user., Get all invites used by a user., Get all unused invites., Remove expired invites and return count of removed invites., Validate an invite code. (+37 more)

### Community 34 - "EldritchIcon.tsx"
Cohesion: 0.03
Nodes (81): ChatMessage, ChatMessageType, ChatPanelTest(), mockClick, mockCreateObjectURL, mockRevokeObjectURL, CommandPanelTest(), DraggablePanelTest() (+73 more)

### Community 35 - "spell_effects_heal.py"
Cohesion: 0.01
Nodes (320): PlayerDPDecayEvent, PlayerDPUpdated, PlayerEnteredRoom, PlayerLeftRoom, Event fired when a player's DP changes.      This event is triggered when a play, Event fired when a mortally wounded player loses DP due to decay.      This even, Event fired when a player enters a room.      This event is triggered when a pla, Event fired when a player leaves a room.      This event is triggered when a pla (+312 more)

### Community 36 - "dependencies.py"
Cohesion: 0.01
Nodes (180): Initialize the database manager., get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service() (+172 more)

### Community 37 - "BehaviorEngine"
Cohesion: 0.02
Nodes (121): BehaviorEngine, Any, Get all behavior rules., Evaluate equality condition (==).          Returns:             bool if conditio, Evaluate inequality condition (!=).          Returns:             bool if condit, Evaluate numeric comparison conditions (>=, <=, >, <).          Args:, Try multiple evaluator methods in sequence.          Args:             condition, Evaluate boolean conditions and variable lookups.          Args:             con (+113 more)

### Community 38 - "lucidity.py"
Cohesion: 0.21
Nodes (12): datetime, Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibi, _utc_now(), Unit tests for lucidity model utility functions.  Tests the _utc_now utility fun, Test _utc_now returns a datetime object., Test _utc_now returns naive datetime (tzinfo=None)., Test _utc_now returns time close to current UTC time., Test _utc_now returns different times on subsequent calls. (+4 more)

### Community 39 - "admin_teleport_commands.py"
Cohesion: 0.03
Nodes (107): _accumulate_valid_occupant_name(), get_occupant_names(), Validate that a name is not a UUID string., Parse one occupant row: append display name or log when it looks like a UUID., Extract and validate occupant names from room occupants list., validate_occupant_name(), add_npc_occupants_to_list(), _AppStateForEventHandler (+99 more)

### Community 40 - "_MagicServiceCore"
Cohesion: 0.08
Nodes (29): _MagicServiceCore, Any, UUID, Return (False, message) if not enough MP, else (True, '')., Return (False, message) if Mythos spell and not enough lucidity, else (True, ''), Return (False, message) if player has not learned the spell, else (True, '')., Return (False, message) if spell requires materials and any are missing, else (T, Check if a player can cast a spell.          Args:             player_id: Player (+21 more)

### Community 41 - "test_user_manager.py"
Cohesion: 0.02
Nodes (109): mock_data_dir(), Unit tests for user manager service.  Tests the UserManager class., Test mute_channel() successfully mutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() fails when trying to mute admin., Test unmute_global() successfully unmutes a player., Test unmute_global() when player is not globally muted., Test is_player_muted() returns False when player is not muted. (+101 more)

### Community 42 - "__init__.py"
Cohesion: 0.09
Nodes (19): PlayerRepositoryProtocol, datetime, Player, Protocol, UUID, Repository protocols for MythosMUD persistence layer.  Explicit typing.Protocol, Protocol for player persistence operations.      Defines the contract used by As, Get the first active player for a user ID. (+11 more)

### Community 43 - "test_zone_config_loader.py"
Cohesion: 0.03
Nodes (116): handle_global_command(), handle_local_command(), handle_me_command(), handle_reply_command(), handle_system_command(), handle_whisper_command(), Communication commands for MythosMUD.  Handlers delegate heavy logic to commun, Local channel message. (+108 more)

### Community 44 - "NATSMessageHandler"
Cohesion: 0.02
Nodes (70): NATSMessageHandler, _not_configured_async(), Any, UUID, Compare two room IDs using canonical room ID resolution., Get player's current room ID from online players cache., Get player's current room ID from async persistence layer., Check if a player is currently in the specified room. (+62 more)

### Community 45 - "Any"
Cohesion: 0.11
Nodes (10): Any, Despawn an NPC instance.          Args:             npc_id: ID of the NPC to, Move an NPC instance to a different room.          Args:             npc_id:, Get all active NPC instances.          Returns:             List of NPC insta, Get detailed stats for a specific NPC instance.          Args:             np, Get NPC population statistics.          Returns:             Dictionary with, Get NPC zone statistics.          Returns:             Dictionary with zone s, Get system-wide NPC statistics.          Returns:             Dictionary with (+2 more)

### Community 46 - "inventory_command_helpers.py"
Cohesion: 0.03
Nodes (87): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), handle_summon_command(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any (+79 more)

### Community 47 - "websocket_handler.py"
Cohesion: 0.07
Nodes (43): handle_json_decode_error(), handle_message_loop_exception(), handle_websocket_disconnect(), handle_websocket_generic_exception(), handle_websocket_message_loop(), handle_websocket_runtime_error(), process_exception_in_message_loop(), process_websocket_inbound_message() (+35 more)

### Community 48 - "test_room_service.py"
Cohesion: 0.02
Nodes (107): mock_persistence(), mock_room_cache(), Unit tests for room service.  Tests the RoomService class for room-related opera, Test get_room() returns None when room not found in persistence., Test get_room() handles dict from persistence., Test get_room_by_name() returns None (not implemented)., Test list_rooms_in_zone() returns empty list (not implemented)., Test get_adjacent_rooms() returns adjacent rooms. (+99 more)

### Community 49 - "IdleMovementHandler"
Cohesion: 0.03
Nodes (65): GameMechanicsService, Any, Heal a player's health., Damage a player's health., Award experience points to a player.          CRITICAL FIX: This method prevents, Service class for game mechanics operations., Initialize the game mechanics service with a persistence layer., Apply fear to a player. (+57 more)

### Community 50 - "test_player_preferences_service.py"
Cohesion: 0.02
Nodes (107): mock_session(), preferences_service(), Unit tests for player preferences service.  Tests the PlayerPreferencesService f, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID., Test creating player preferences when they already exist., Test creating player preferences with invalid ID. (+99 more)

### Community 51 - "SpellLearningService"
Cohesion: 0.03
Nodes (116): _MapRooms, RoomDictList, MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter count, generate_minimap_html(), UUID, Minimap orchestration for the map API.  Extracted from maps.py so the router sta (+108 more)

### Community 52 - "test_communication_commands_flows.py"
Cohesion: 0.04
Nodes (75): Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC, Subscribe to room events for quest triggers and progress (start on enter, comple, subscribe_quest_events(), subscribe_room_occupants_refresh(), _ensure_room_cache_before_npc_startup(), _get_item_prototype_count(), _get_item_prototype_entries(), initialize_chat_service() (+67 more)

### Community 53 - "test_connection_delegates.py"
Cohesion: 0.06
Nodes (56): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules.  Keeps ``A, Application object with a ``state`` namespace (dynamic attributes)., _AppStatePersistence, _AppWithPersistence, _as_app_with_state(), _CmdType (+48 more)

### Community 54 - "Player"
Cohesion: 0.02
Nodes (72): AsyncPersistenceLayer, CreateItemInstanceInput, TypedDict, Constants and shared types for async persistence layer.  Extracted to keep async, Optional fields for create_item_instance. owner_type, owner_id, etc. with defaul, Any, datetime, Player (+64 more)

### Community 55 - "test_container_persistence.py"
Cohesion: 0.02
Nodes (168): ContainerData, create_container(), delete_container(), _fetch_container_items(), get_container(), get_containers_by_entity_id(), get_containers_by_room_id(), _parse_jsonb_column() (+160 more)

### Community 56 - "__init__.py"
Cohesion: 0.04
Nodes (69): ItemInstance, initialize_components(), Any, Prepare component state metadata for a new item instance.      This routine curr, Constants supporting item prototype validation.  These enumerations anchor the s, Item system package.  This module exposes the prototype schema and registry util, ItemFactory, ItemFactoryError (+61 more)

### Community 57 - "test_npc_database.py"
Cohesion: 0.03
Nodes (68): get_postgres_connect_args(), Build connect_args for asyncpg when POSTGRES_SEARCH_PATH is set.      Used so un, Initialize database engine and session maker from configuration.          CRITIC, close_npc_db(), ensure_npc_database_directory(), get_npc_database_path(), get_npc_engine(), get_npc_session() (+60 more)

### Community 58 - "PlayerOccupantProcessor"
Cohesion: 0.03
Nodes (123): GameTerminalProps, LucidityMeter, LucidityMeterProps, TIER_DESCRIPTIONS, MagicPointsMeter, MagicPointsMeterProps, MagicPointsStatus, handleCombatDeath() (+115 more)

### Community 59 - "character_creation.py"
Cohesion: 0.04
Nodes (73): _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _check_shutdown_status(), _convert_stat_summary_to_stat_summary_model(), create_character_with_stats(), _execute_create_character(), Any, Request (+65 more)

### Community 60 - "test_command_factories_utility.py"
Cohesion: 0.02
Nodes (107): Unit tests for utility command factories.  Tests the UtilityCommandFactory class, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+99 more)

### Community 61 - "validate_room_data"
Cohesion: 0.05
Nodes (36): Record the schedule categories currently active for NPC routines., Any, Single schedule block describing routine availability (`data/<env>/calendar/sche, Validate schedule entry days are standard English weekday names (Sunday, Monday,, Validate slug-formatted list entries.          Args:             value: Sequence, Ensure the schedule window moves time forward like the Chronology Tablets prescr, ScheduleEntry, _DatabaseLoadResult (+28 more)

### Community 62 - "__init__.py"
Cohesion: 0.05
Nodes (87): apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest, UUID (+79 more)

### Community 63 - "ApplicationContainer"
Cohesion: 0.03
Nodes (84): PlayerPersistenceSpellPort, Async persistence surface used by SpellEffects player-targeting paths., Increase lucidity from a spell effect., Decrease lucidity from a spell effect., coerce_effect_float_times_mastery_as_int(), Coerce to float first, then apply mastery (lucidity-style deltas)., UUID, Spell effects processing engine.  This module handles applying spell effects t (+76 more)

### Community 64 - "PassiveLucidityFluxService"
Cohesion: 0.06
Nodes (41): FluxServiceConfig, lookup_profile(), normalize_environment_config(), period_label(), Any, datetime, Configuration and normalization for passive lucidity flux., Optional configuration for PassiveLucidityFluxService. All fields have defaults. (+33 more)

### Community 65 - "is_player_in_login_grace_period"
Cohesion: 0.03
Nodes (98): cancel_login_grace_period(), get_login_grace_period_remaining(), _grace_period_expiration_handler(), _grace_period_task(), is_player_in_login_grace_period(), Any, UUID, Login grace period management for MythosMUD.  This module handles the 10-second (+90 more)

### Community 66 - "test_player_service.py"
Cohesion: 0.01
Nodes (159): Data validation errors (e.g. empty local/whisper message). Log at warning, not e, Log validation errors at warning so expected user-input errors do not flood erro, ValidationError, mock_profession_service(), mock_request(), mock_stats_generator(), Unit tests for character creation API endpoints.  Tests roll stats, create chara, Test roll_character_stats() enforces rate limiting. (+151 more)

### Community 67 - "test_command_factories_exploration.py"
Cohesion: 0.02
Nodes (99): Unit tests for exploration command factories.  Tests the ExplorationCommandFacto, Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_sit_command() creates SitCommand., Test create_sit_command() raises error with args., Test create_stand_command() creates StandCommand., Test create_stand_command() raises error with args. (+91 more)

### Community 68 - "get_admin_auth_service"
Cohesion: 0.03
Nodes (80): GotoCommand, NPCCommand, Command for shutting down the server (admin only).      Args can be:     - Empty, Command for NPC administrative utilities with subcommands., Administrative command for summoning prototypes into the current room., Validate prototype ID format.          Args:             value: The prototype ID, Command for teleporting a player to the admin's location., Ensure provided direction is part of the allowed set. (+72 more)

### Community 69 - "test_login_grace_period_visual_indicator.py"
Cohesion: 0.02
Nodes (108): _filter_other_players(), Room look functionality for MythosMUD.  This module handles looking at rooms, in, Filter out the current player from the list of players in room.     Adds "(linkd, cancel_grace_period(), is_player_in_grace_period(), Any, UUID, Disconnect grace period management for MythosMUD.  This module handles the 30-se (+100 more)

### Community 70 - "chatPanelRuntimeUtils.ts"
Cohesion: 0.07
Nodes (49): filterMessagesForChannelView(), EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW, isGloballyExcludedFromChannelView(), isVisibleInChannelView(), matchesChannelSelection(), resolveMessageChannelForFilter(), buildChatExportCSV(), buildChatExportCsvRow() (+41 more)

### Community 71 - "RateLimiter"
Cohesion: 0.04
Nodes (88): _cleanup_connection_tracking(), _cleanup_fully_disconnected_player(), _cleanup_player_data(), _cleanup_room_subscriptions(), cleanup_websocket_disconnect(), disconnect_all_websockets_impl(), disconnect_connection_by_id_impl(), _disconnect_single_websocket() (+80 more)

### Community 72 - "test_admin_auth_service.py"
Cohesion: 0.03
Nodes (102): Command Input Utilities for MythosMUD.  This module provides utilities for clean, Unit tests for command validator., Test validate_command_length returns True for valid length., Test validate_command_length returns False for too long command., Test validate_command_length with custom max_length., Test validate_command_format returns True for valid command., Test validate_command_format returns False for empty command., Test validate_command_format returns False for suspicious command. (+94 more)

### Community 73 - "ChatService"
Cohesion: 0.03
Nodes (76): ChatService, Get all poses for players in a room.          Args:             room_id: ID of t, Check if a player can send a message., Store the last whisper sender for a player to enable reply functionality., Get the last whisper sender for a player.          Args:             player_name, Clear the last whisper sender for a player.          Args:             player_na, Chat service for handling real-time communication between players.      This ser, Unit tests for chat service.  Tests the ChatService class and ChatMessage class. (+68 more)

### Community 74 - "CombatInstance"
Cohesion: 0.03
Nodes (139): _apply_taunt_and_maybe_broadcast(), AppWithState, Protocol, UUID, Taunt command flow: validation and execution.  Extracted from combat.py to reduc, Validate taunt preconditions and resolve combat/NPC.     Returns error dict or (, Validate and resolve target name from command_data. Returns error dict or target, Apply taunt and broadcast target switch if aggro changed. Returns error dict or (+131 more)

### Community 75 - "test_quest_service.py"
Cohesion: 0.04
Nodes (61): _make_definition_row(), _make_turn_in_definition_row(), mock_def_repo(), mock_instance_repo(), Unit tests for QuestService.  Covers: resolve_name_to_quest_id, start_quest, a, start_quest returns error when quest id not found., start_quest returns error when player already has active instance., start_quest returns error when player already completed quest. (+53 more)

### Community 76 - "test_npc_service.py"
Cohesion: 0.04
Nodes (75): _def_row(), _mock_result_mappings_all(), mock_session(), Unit tests for NPC service.  Tests the NPCService class., Build mock result such that result.mappings().all() returns rows., Test get_npc_definitions() successfully retrieves definitions., Test get_npc_definitions() returns empty list when no definitions., Test get_npc_definition() returns definition when found. (+67 more)

### Community 77 - "test_websocket_handler_core.py"
Cohesion: 0.03
Nodes (85): handle_websocket_message(), WebSocket, Handle a WebSocket message from a player.      Args:         websocket: The WebS, Send a system message to a player.      Args:         websocket: The WebSocket c, send_system_message(), Unit tests for core websocket handler functions.  Tests core WebSocket handler f, Test _process_message processes message., Test _process_message returns True when rate limit exceeded. (+77 more)

### Community 78 - "test_look_helpers.py"
Cohesion: 0.02
Nodes (172): _handle_implicit_target_lookup(), Handle implicit target lookup with priority resolution., _get_health_label(), _get_lucidity_label(), _get_visible_equipment(), _get_wearable_container_service(), _is_direction(), _parse_instance_number() (+164 more)

### Community 79 - "websocket_initial_state.py"
Cohesion: 0.05
Nodes (56): Any, Convert alias to dictionary for JSON serialization., _AppStateForPlayerService, build_basic_player_data(), convert_schema_to_dict(), _ensure_player_in_room_occupancy(), get_player_and_room(), get_player_service_from_connection_manager() (+48 more)

### Community 80 - "multiplayer.ts"
Cohesion: 0.10
Nodes (42): nudgeStandBothPlayers(), primeBothForCoLocate(), waitForLookReflected(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers() (+34 more)

### Community 81 - "test_auth_utils.py"
Cohesion: 0.04
Nodes (73): E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio., One row in users plus optional default character for login E2E. (+65 more)

### Community 82 - "Reporter"
Cohesion: 0.03
Nodes (45): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+37 more)

### Community 83 - "test_magic_commands.py"
Cohesion: 0.17
Nodes (11): mock_chat_service(), mock_magic_service(), mock_player(), Unit tests for magic commands.  Tests the /cast, /spells, /spell, /learn, and /s, Create a mock chat service., Test cast command success., Test spells command when player is not found., Create a mock magic service. (+3 more)

### Community 84 - "AppConfig"
Cohesion: 0.02
Nodes (122): _create_config_instance(), _get_config_cached(), _get_config_test(), Configuration module for MythosMUD server.  This module provides type-safe, vali, Create a new AppConfig instance from current environment.      This is a helper, Production config loader with caching.      Uses both @lru_cache and global _con, Test config loader without caching - always returns fresh instances.      This e, AppConfig (+114 more)

### Community 85 - "test_status_commands.py"
Cohesion: 0.04
Nodes (85): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _get_combat_status(), _get_profession_info(), handle_status_command(), handle_whoami_command(), Any (+77 more)

### Community 86 - "lifespan.py"
Cohesion: 0.02
Nodes (149): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+141 more)

### Community 87 - "panelReducerHandlers.ts"
Cohesion: 0.05
Nodes (68): PanelManager(), PanelManagerProps, GameClientV2AuxiliaryPanels(), renderCharacterInfoPanel(), renderCommandHistoryPanel(), renderCommandInputPanel(), renderMinimapPanel(), minimapBackdropLayout() (+60 more)

### Community 88 - "test_container_helpers_inventory_find.py"
Cohesion: 0.05
Nodes (87): Update equipped items' metadata to include container information., update_equipped_with_container_info(), check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container() (+79 more)

### Community 89 - "LucidityService"
Cohesion: 0.03
Nodes (98): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+90 more)

### Community 90 - "exceptions.py"
Cohesion: 0.03
Nodes (116): delete_character(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), get_available_classes(), _get_connection_manager(), get_player(), get_player_by_name() (+108 more)

### Community 91 - "test_look_room.py"
Cohesion: 0.03
Nodes (90): _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id(), _handle_direction_look() (+82 more)

### Community 92 - "MessageQueue"
Cohesion: 0.10
Nodes (22): _make_session_context(), Test get_by_player_and_quest returns mapped instance when found., Test get_by_player_and_quest returns None when not found., Test get_by_player_and_quest accepts UUID for player_id., Test update_state_and_progress updates and commits., Test update_state_and_progress still calls procedure and commit when only instan, Test list_active_by_player returns list of mapped active instances., Test list_active_by_player returns empty list when none. (+14 more)

### Community 93 - "test_connection_disconnection.py"
Cohesion: 0.04
Nodes (51): Unit tests for command parser.  Tests the CommandParser class which provides sec, Test parse_command handles 'g' alias for global/system., Test _parse_command_parts parses basic command., Test _parse_command_parts handles command without args., Test _parse_command_parts handles multiple arguments., Test _parse_command_parts detects mock objects., Test _create_command_object successfully creates command., Test _create_command_object handles 'w' alias. (+43 more)

### Community 94 - "test_exploration_service.py"
Cohesion: 0.06
Nodes (61): _chat_send_with_room_bundle(), flow_global_command(), flow_local_command(), flow_say_command(), _global_player_bundle(), _message_from_command(), Handle the `say` command: broadcast speech to the current room., Handle the `local` command: room-only speech (not global). (+53 more)

### Community 95 - "NPCBase"
Cohesion: 0.04
Nodes (29): NPCActionType, NPCCommunicationBridge, NPCMessageQueue, Any, Enum, Initialize the NPC message queue.          Args:             max_messages_per_np, Add a message to an NPC's pending message queue.          Args:             npc_, Get all pending messages for an NPC.          Args:             npc_id: The NPC' (+21 more)

### Community 96 - "test_lifespan_startup.py"
Cohesion: 0.14
Nodes (15): NPCCombatIntegrationCombatMixin, _NPCCombatIntegrationDeps, Protocol, UUID, Structured logging / observability trail when NPC-initiated combat begins., Process combat attack, starting new combat or continuing existing one., Start a new combat and process initial attack., Broadcast room occupants update to killer's room after NPC death. Swallows error (+7 more)

### Community 97 - "Alias"
Cohesion: 0.03
Nodes (70): Alias, BaseModel, Alias model for command aliases.  This module defines the Alias model for storin, Alias model for command aliases.      Stores player command aliases for quick ac, String representation of the alias., Check equality based on name and command., Hash based on name and command for use in sets/dicts., Update the updated_at timestamp to current time. (+62 more)

### Community 98 - "test_player_presence_tracker.py"
Cohesion: 0.04
Nodes (81): _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _get_instance_manager_from_manager(), Any, UUID, Player presence tracking helper for connection manager.  This module provides he, Extract InstanceManager from ConnectionManager via app.container. (+73 more)

### Community 99 - "test_command_admin.py"
Cohesion: 0.02
Nodes (89): Any, UUID, Add a player to the room without triggering an event.          This method is us, Remove a player from the room without triggering an event.          This method, Remove a player from the room and trigger event.          Args:             play, Add an object to the room and trigger event.          Args:             object_i, Remove an object from the room and trigger event.          Args:             obj, Remove an NPC from the room and trigger event.          Args:             npc_id (+81 more)

### Community 100 - "DependencyAnalyzer"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 101 - "EventPublisher"
Cohesion: 0.06
Nodes (33): event_publisher(), mock_nats_service(), mock_subject_manager(), Unit tests for event publisher.  Tests the EventPublisher class., Test publish_game_tick_event() when NATS is not connected., Test get_next_sequence_number() returns and increments sequence., Test reset_sequence_number() resets sequence to 0., Test EventPublisher initialization without subject manager. (+25 more)

### Community 102 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.05
Nodes (79): _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch(), filter_valid_items() (+71 more)

### Community 103 - "get_username_from_user"
Cohesion: 0.04
Nodes (51): mock_alias(), mock_alias_storage(), Unit tests for alias command handlers.  Tests the alias, aliases, and unalias co, Test handle_alias_command creating alias from structured data., Test handle_alias_command with alias name too long., Test handle_alias_command with command too long., Test handle_alias_command with circular reference., Create a mock alias storage. (+43 more)

### Community 104 - "test_game.py"
Cohesion: 0.04
Nodes (54): broadcast_message(), get_game_status(), get_mythos_time(), Return the current Mythos calendar metadata for HUD initialization.      In-memo, Get current game status and connection information., Broadcast a message to all connected players (admin only).      Requires superus, BroadcastMessageResponse, BroadcastStats (+46 more)

### Community 105 - "container_persistence_async.py"
Cohesion: 0.03
Nodes (99): Validate player name format using centralized validation., AddAdminCommand, AdminCommand, MuteCommand, MuteGlobalCommand, MutesCommand, Moderation command models for MythosMUD.  This module provides command models fo, Command for showing current mute status. (+91 more)

### Community 106 - "security.ts"
Cohesion: 0.06
Nodes (33): SkillEntry, SkillsPage(), hoisted, fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler, asRecordUnknown() (+25 more)

### Community 107 - "HolidayService"
Cohesion: 0.04
Nodes (45): HolidayCollection, HolidayEntry, Create a mapping of holiday IDs to holiday entries.          Returns:, Ensure all holiday IDs are unique.          Raises:             ValueError: If d, Single holiday definition loaded from data/<env>/calendar/holidays.json., Validate tradition value.          Args:             value: The tradition string, Validate season value.          Args:             value: The season string to va, Validate bonus tags format. (+37 more)

### Community 108 - "RoomLoader"
Cohesion: 0.03
Nodes (63): Create a temporary directory for testing., temp_dir(), Path, Generate room ID from parsed filename and location data.          Args:, Recursively scan directory for all room JSON files.          Args:             b, Validate basic room structure., Extract plane, zone, sub_zone from file path., Handles discovery and loading of room definition files.      As noted in the Pna (+55 more)

### Community 109 - "UUID"
Cohesion: 0.17
Nodes (9): Any, UUID, Broadcast party message to party members only, with dampening and mute checks., Send whisper message to specific player with communication dampening., Broadcast system/admin message to all players., Handle unknown channel type., Broadcast message according to channel strategy.          Args:             chat, Broadcast room-based message with server-side filtering. (+1 more)

### Community 110 - "test_combat_monitoring_service.py"
Cohesion: 0.03
Nodes (71): mock_combat_config(), mock_feature_flags(), Unit tests for combat monitoring service.  Tests the CombatMonitoringService cla, Test end_combat_monitoring with failed combat., Test end_combat_monitoring when combat not found., Test start_turn_monitoring tracks turn., Test end_turn_monitoring updates metrics., Test end_turn_monitoring when turn not found. (+63 more)

### Community 111 - "ConnectionManager"
Cohesion: 0.01
Nodes (204): ConnectionManager, WebSocket, Manages real-time connections for the game.      This refactored version uses mo, Check if a WebSocket is open., Check if a WebSocket ID is in the closed set., Mark a WebSocket ID as closed., Get the count of closed WebSocket IDs being tracked., Safely close a WebSocket connection. (+196 more)

### Community 112 - "aggro_threat.py"
Cohesion: 0.04
Nodes (60): _make_mock_row(), player_repository(), UUID, Unit tests for player repository.  Tests the PlayerRepository class which handle, Test PlayerRepository initializes with room cache., Test PlayerRepository initializes with event bus., Test validate_and_fix_player_room returns False for valid room., Test validate_and_fix_player_room fixes invalid room. (+52 more)

### Community 113 - "_handle_admin_set_stat_command"
Cohesion: 0.04
Nodes (70): _AdminSetStatApplyContext, _AdminSetStatLogContext, _apply_stat_change_and_build_result(), _build_set_stat_error_response(), _calculate_stat_warnings(), _get_app_or_error(), _handle_admin_set_stat_command(), _log_admin_set_stat() (+62 more)

### Community 114 - "test_mp_regeneration_service.py"
Cohesion: 0.10
Nodes (19): mock_player_service(), Unit tests for MP regeneration service.  Tests the MPRegenerationService class f, Test process_tick_regeneration() accumulates fractional MP., Test _get_regen_multiplier() returns 1.0 for standing position., Test _get_regen_multiplier() defaults to 1.0 when position not specified., Test restore_mp_from_meditation() returns error when player not found., Create a mock player service., Test restore_mp_from_meditation() restores MP. (+11 more)

### Community 115 - "UserManager"
Cohesion: 0.07
Nodes (31): UUID, Check if a player is globally muted by any other player.          Args:, Get information about who muted a player.          Args:             player_i, Update cache to mark load as failed., Convert mute_info datetime and UUID objects to JSON-serializable formats., Save player mutes to data dictionary for JSON serialization., Save channel mutes to data dictionary for JSON serialization., Save global mutes applied by this player to data dictionary for JSON serializati (+23 more)

### Community 116 - "test_look_player.py"
Cohesion: 0.03
Nodes (96): EmoteCommand, LocalCommand, MeCommand, PoseCommand, Command for whispering to a specific player., Validate target player name format using centralized validation., Validate message content for security using centralized validation., Command for replying to the last whisper received. (+88 more)

### Community 117 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (71): Path, Resolve log_base path to absolute path relative to project root.      Args:, resolve_log_base(), Path, Unit tests for logging utilities.  Tests the logging utilities for directory man, Test resolve_log_base() returns absolute path as-is., Test resolve_log_base() resolves relative path using pyproject.toml., Test resolve_log_base() falls back to current directory if no pyproject.toml. (+63 more)

### Community 118 - "main.py"
Cohesion: 0.03
Nodes (73): generate_random_stats(), Generate Stats with random attribute values.      Factory function for creating, Any, Core character statistics with Lovecraftian horror elements., Initialize Stats with provided data.          For random stat generation, use ge, Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes precedenc, Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded)., Calculate max lucidity based on education.          AI: This computed field uses (+65 more)

### Community 119 - "logger.ts"
Cohesion: 0.02
Nodes (81): mock_event_bus(), mock_player(), mock_player_combat_service(), mock_session(), Unit tests for player death service.  Tests the PlayerDeathService class for man, Test get_mortally_wounded_players() finds mortally wounded players., Test get_mortally_wounded_players() excludes healthy players., Test get_mortally_wounded_players() excludes dead players. (+73 more)

### Community 120 - "test_command_moderation.py"
Cohesion: 0.04
Nodes (59): Unit tests for moderation command factories.  Tests the ModerationCommandFactory, Test create_mute_global_command() with duration and reason., Test create_mute_global_command() with reason but no duration., Test create_unmute_global_command() creates UnmuteGlobalCommand., Test create_unmute_global_command() raises error with no args., Test create_unmute_global_command() raises error with multiple args., Test create_admin_command() creates AdminCommand., Test create_mute_command() creates MuteCommand. (+51 more)

### Community 121 - "PlayerPositionService"
Cohesion: 0.12
Nodes (9): Test get_combat_end_messages generates messages for all occupants., Test suite for CombatMessagingService class., Test get_combat_end_messages from loser perspective., Test get_combat_end_messages with empty occupants list., Test get_attack_message handles zero damage., Test get_attack_message handles high damage values., Test get_attack_message from attacker perspective., Test get_attack_message with custom action type. (+1 more)

### Community 122 - "FeatureFlagService"
Cohesion: 0.03
Nodes (53): FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD.  This service provides centralized feature f, Clear the feature flag cache.          This should be called when configuration (+45 more)

### Community 123 - "Stats"
Cohesion: 0.02
Nodes (109): ContainerComponent, Any, BaseModel, Validate that metadata does not contain personal information (COPPA compliance)., Validate and convert source_type to enum., Validate and convert lock_state to enum., Check if container is locked or sealed., Check if container is unlocked. (+101 more)

### Community 124 - "SchemaValidator"
Cohesion: 0.03
Nodes (44): Path, Convert legacy string format exits to new object format internally.          Thi, Validate a room file against the schema.          Args:             file_path: P, Validate all rooms in a database against the schema.          Args:, Extract target room ID from exit data, handling both formats.          Args:, Extract flags from exit data, handling both formats.          Args:, Check if an exit is marked as one-way.          Args:             exit_data: Exi, Check if an exit is marked as self-reference.          Args:             exit_da (+36 more)

### Community 125 - ".to_dict"
Cohesion: 0.04
Nodes (35): Return UUID mapping dependency for integration collaborators., NPCCombatUUIDMapping, UUID, NPC Combat UUID Mapping Management.  This module handles UUID-to-string ID and U, Get the original string ID from a UUID.          Args:             uuid_id: The, Get XP value for a UUID.          Args:             uuid_id: The UUID to look up, Manages UUID mappings for NPC combat., Initialize UUID mapping storage. (+27 more)

### Community 126 - "test_lucidity_recovery_commands.py"
Cohesion: 0.02
Nodes (153): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+145 more)

### Community 127 - "test_enhanced_logging_config.py"
Cohesion: 0.05
Nodes (41): Unit tests for async persistence layer: init, close, player, user, room, profess, Test get_user_by_username_case_insensitive when user not found., Test get_user_by_username_case_insensitive with database error., Test get_room_by_id delegates to RoomRepository., Test get_room_by_id when room not found., Test list_rooms delegates to RoomRepository., Test AsyncPersistenceLayer initialization with skipped room cache., Test async_list_rooms delegates to RoomRepository. (+33 more)

### Community 128 - "PathValidator"
Cohesion: 0.08
Nodes (28): Room fixer for automatic issue resolution.  This module handles automatic fixing, Core validation components for the MythosMUD room validator.  This module contai, Mini-map renderer for room connectivity visualization.  This module provides vis, Path validator for room connectivity analysis.  This module handles graph traver, Reporter for validation results.  This module handles formatting and displaying, Room loader for discovering and parsing room definition files.  This module hand, Tests for the reporter module.  Tests output formatting, color handling, and JSO, Tests for the room loader module.  Tests file discovery, JSON parsing, and room (+20 more)

### Community 129 - "UUID"
Cohesion: 0.03
Nodes (70): MessageQueue, Any, Check if a player has pending messages.          Args:             player_id: Th, Get the number of pending messages for a player.          Args:             play, Remove all pending messages for a specific player.          Args:             pl, Clean up old messages to prevent memory bloat.          Args:             max_ag, Message queue for guaranteed delivery of messages to players.      This class ha, Clean up large data structures to prevent memory bloat.          Args: (+62 more)

### Community 130 - "test_invite_schemas.py"
Cohesion: 0.05
Nodes (61): Auth domain schemas: user and invite., InviteBase, InviteCreate, InviteUpdate, Pydantic schemas for Invite model.  This module defines Pydantic schemas for inv, Base invite schema with common fields., Schema for creating a new invite., Schema for updating invite data. (+53 more)

### Community 131 - "test_manager.py"
Cohesion: 0.04
Nodes (49): Unit tests for NATS Subject Manager.  Tests the NATSSubjectManager class., Test build_subject() raises SubjectValidationError for invalid parameter., Test validate_subject() returns True for valid subject., Test validate_subject() returns False for invalid subject., Test validate_subject() accepts events.domain.{event_type} (distributed EventBus, Test validate_subject() returns False for empty subject., Test validate_subject() uses cache for repeated validations., Test validate_subject() doesn't use cache when disabled. (+41 more)

### Community 132 - "systemHandlers.ts"
Cohesion: 0.09
Nodes (36): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, handleIntentionalDisconnect(), handleLucidityChange() (+28 more)

### Community 133 - "ScheduleEntry"
Cohesion: 0.05
Nodes (44): HealthMonitor, Any, UUID, Find player_id for cleanup when metadata is missing., Check if connection is stale based on timeout., Check if WebSocket is actually open., Validate token and update last validation time if needed., Process health check for a single connection. (+36 more)

### Community 134 - "container_endpoints_basic.py"
Cohesion: 0.03
Nodes (76): _emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), Any, ContainerComponent, UUID, WebSocket event emission helpers for container API endpoints.  This module conta (+68 more)

### Community 135 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages.  These schemas define the structure and (+55 more)

### Community 136 - "ChatLogger"
Cohesion: 0.06
Nodes (24): ChatLogger, Any, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed.          Args:             time, Get the current log file path for the specified type.          Args:, Write a log entry to the appropriate log file.          Args:             log_ty, Log a chat message for AI processing.          Args:             message_data: C, Structured logging service for chat system events.      This logger creates JSON (+16 more)

### Community 137 - "RoomSyncService"
Cohesion: 0.05
Nodes (62): NpcIntegrationStringIdPort, NpcLifecycleManagerPort, NpcSpellDamageTarget, PlayerServiceHealPort, Protocol, UUID, Shared Protocol types for spell effect modules.  Used by basedpyright to type NP, Apply healing to a player by id. (+54 more)

### Community 138 - "extract_room_id_from_npc"
Cohesion: 0.04
Nodes (72): age_off_disconnected_sessions(), _cleanup_player_references(), _collect_disconnect_keys(), _get_session_maps_for_age_off(), handle_player_disconnect_broadcast(), _purge_expired_sessions_from_maps(), Player, UUID (+64 more)

### Community 139 - "NPCCombatIntegrationBase"
Cohesion: 0.06
Nodes (30): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Apply combat effects to a target (player or NPC).          Args:, Convert target_id to UUID, accepting either string or UUID input., Apply combat effects to a player. (+22 more)

### Community 140 - ".get_room"
Cohesion: 0.08
Nodes (46): _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_reply_command(), flow_system_command(), flow_whisper_command(), _player_id_bundle(), Room/global/system/whisper/reply flows for communication command handlers.  Ex, Handle the `system` command: admin-only system channel message. (+38 more)

### Community 141 - "catatonia_check.py"
Cohesion: 0.04
Nodes (55): handle_expanded_command(), Any, CommandExecutionRequest, Handle command processing with alias expansion and loop detection.      This fun, check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid() (+47 more)

### Community 142 - "CircuitBreaker"
Cohesion: 0.03
Nodes (78): CircuitBreaker, CircuitBreakerOpen, CircuitState, Any, Enum, Exception, timedelta, Circuit breaker pattern for NATS message processing.  Implements three-state cir (+70 more)

### Community 143 - ".build_subject"
Cohesion: 0.06
Nodes (46): Register a new subject pattern.      This endpoint allows administrators to dyna, register_pattern(), InvalidPatternError, MissingParameterError, NATSSubjectError, PatternNotFoundError, Exception, Base exception for NATS subject-related errors. (+38 more)

### Community 144 - "test_skill_service.py"
Cohesion: 0.02
Nodes (112): get_skills_catalog(), Request, Return the  skills catalog (base values, allow_at_creation).      Cthulhu Mythos, Any, UUID, SkillService: skills catalog, set_player_skills, get_player_skills (with ownersh, Raise ValueError if any skill_id appears in both occupation and personal interes, Build skill_key -> total modifier from profession skill_modifiers (supports skil (+104 more)

### Community 145 - "test_combat_flee_helpers.py"
Cohesion: 0.05
Nodes (57): _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id(), _PlayerForFlee, _PlayerPositionServiceLike, AppWithState, Protocol (+49 more)

### Community 146 - "test_follow_commands.py"
Cohesion: 0.07
Nodes (30): _append_room_with_fallback_coords_if_needed(), _apply_minimap_fallback_coordinates(), _ensure_current_room_in_minimap_rooms(), Any, AsyncSession, Get current room from pre-filter list or load by stable_id. Returns None if not, Append room to list; use fallback map_x/map_y=0 if room has None coords. Mutates, If current_room_id is missing from rooms, re-add it from rooms_before_filter or (+22 more)

### Community 147 - "test_room_subscription_manager_drops.py"
Cohesion: 0.03
Nodes (61): Unit tests for room subscription manager drop functions.  Tests the room drop fu, Test adjust_room_drop() returns False for invalid index., Test list_room_drops() returns room drops., Test add_room_drop() adds drop to new room., Test add_room_drop() adds drop to existing room., Test take_room_drop() successfully takes drop., Test take_room_drop() with index out of range., Test take_room_drop() with quantity larger than available. (+53 more)

### Community 148 - "test_validation.py"
Cohesion: 0.03
Nodes (63): custom_length_validator(), Unit tests for NATS Subject Validator.  Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter., Test validate_parameter_value() raises error for empty parameter. (+55 more)

### Community 149 - "test_room_sync_service.py"
Cohesion: 0.03
Nodes (75): Any, T, Process room update with comprehensive validation.          Args:             ro, Invalidate stale room cache entry.          Args:             room_id: Room ID t, Fetch fresh room data from room service.          Args:             room_id: Roo, Handle stale room data by requesting fresh data.          Args:             room, Process room transition with proper ordering and validation.          Args:, Get statistics about the room data cache.          Returns:             Dict[str (+67 more)

### Community 150 - "test_container_websocket_events.py"
Cohesion: 0.05
Nodes (56): ContainerLockState, datetime, InventoryStack, StrEnum, UUID, Container component model for the unified container system.  As documented in th, Validate that room_id is provided for environment and corpse containers., Validate that entity_id is provided for equipment containers. (+48 more)

### Community 151 - "apiTypeGuards.ts"
Cohesion: 0.11
Nodes (47): LoginResponse, ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString() (+39 more)

### Community 152 - "CombatConfiguration"
Cohesion: 0.03
Nodes (67): CombatConfiguration, CombatConfigurationError, CombatConfigurationScope, CombatConfigurationService, get_combat_configuration(), is_combat_available(), Any, Enum (+59 more)

### Community 153 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.09
Nodes (48): _build_python_call_usage_map(), _call_target_name(), check_ai_guardrails(), _check_exports_and_tiny_functions(), _check_single_use_file(), _collect_code_texts(), _collect_python_public_defs_and_tiny(), _guardrail_scan_inputs() (+40 more)

### Community 154 - "test_character_creation_service.py"
Cohesion: 0.03
Nodes (61): CharacterCreationService, Any, UUID, Validate character stats against class prerequisites.          Args:, Create a new character with specific stats.          Args:             name: The, Get information about all available character classes and their prerequisites., Service class for character creation and stats generation business operations., Get a description for a character class. (+53 more)

### Community 155 - "test_npc_models.py"
Cohesion: 0.02
Nodes (136): _JSONDict, Base, _loads_json_dict(), NPCRelationship, NPCSpawnRule, DeclarativeBase, Get base stats as dictionary., Set base stats from dictionary. (+128 more)

### Community 156 - "test_admin_commands.py"
Cohesion: 0.05
Nodes (34): MessageFilteringHelper, Any, Extract information from chat event.          Args:             chat_event: Chat, Determine if mute check should be applied for a channel.          Args:, Compare two room IDs using canonical room ID resolution.          Args:, Get player's current room ID from online players cache.          Args:, Get player's current room ID from async persistence layer.          Args:, Helper class for message filtering operations. (+26 more)

### Community 157 - "test_websocket_handler_validation_errors.py"
Cohesion: 0.07
Nodes (19): Any, AsyncSession, UUID, Get a list of rooms adjacent to the specified room.          Args:             r, Get the scope of rooms for local chat (current room + adjacent rooms)., Validate that a room exists using cached data.          Args:             room_i, Validate that there's a valid exit from one room to another.          Args:, Get all occupants (players and NPCs) currently in a room using cached data. (+11 more)

### Community 158 - "websocket_handler_commands.py"
Cohesion: 0.08
Nodes (41): _attach_room_state_to_result(), handle_game_command(), _invoke_get_room_state_event(), parse_game_command_tokens(), process_websocket_command(), WebSocket, Handle a game command from a player.      Args:         websocket: The WebSoc, Return get_room_state_event(player_id, room_id) coroutine factory, or None if un (+33 more)

### Community 159 - "RoomDataCache"
Cohesion: 0.04
Nodes (40): Any, Room data cache and freshness management for MythosMUD.  This module provides ca, Get statistics about the room data cache.          Args:             is_room_dat, Merge room data with proper conflict resolution.          Args:             old_, Manages room data caching and freshness validation., Check if new data is newer than old data for a specific key.          Args:, Initialize the room data cache.          Args:             freshness_threshold_s, Check if room data is fresh enough to use.          Args:             room_data: (+32 more)

### Community 160 - "test_player_event_handlers_respawn.py"
Cohesion: 0.06
Nodes (47): ChannelActivityIndicators(), ChannelActivityIndicatorsProps, getActivityColor(), ChannelSelectorSection(), ChannelSelectorSectionProps, ChatStatistics(), ChatStatisticsProps, ChatPanelRefactored() (+39 more)

### Community 161 - "CorpseOverlay.tsx"
Cohesion: 0.06
Nodes (47): BackpackTab(), BackpackTabProps, ContainerSplitPane(), ContainerSplitPaneProps, formatWeaponStats(), calculateTimeRemaining(), CorpseOverlay(), CorpseOverlayProps (+39 more)

### Community 162 - "NPCSpawnRule"
Cohesion: 0.09
Nodes (30): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatMapErrorResponse(), AsciiMapEditorProps (+22 more)

### Community 163 - "useGameClientV2Container.ts"
Cohesion: 0.05
Nodes (56): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, MapView(), MapViewProps (+48 more)

### Community 164 - "sanitize_detail_value"
Cohesion: 0.07
Nodes (23): Return lucidity dependency for integration collaborators., NPCCombatLucidity, Any, Determine encounter category based on NPC definition metadata.          Args:, Manages lucidity effects for NPC encounters., Apply lucidity loss when a player engages an eldritch entity.          Args:, Unit tests for NPC combat lucidity effects.  Tests the NPCCombatLucidity class f, Test _resolve_lucidity_category handles non-dict base_stats. (+15 more)

### Community 165 - "test_rate_limiter.py"
Cohesion: 0.03
Nodes (57): mock_config(), Unit tests for rate limiter service.  Tests the RateLimiter class which provides, Test check_rate_limit returns True when within limits., Test check_rate_limit returns False when limit exceeded., Test check_rate_limit always returns True when disabled., Test check_rate_limit handles errors gracefully (fails open)., Test record_message adds timestamp to window., Create a mock config with chat rate limits. (+49 more)

### Community 166 - "PlayerChannelPreferences"
Cohesion: 0.06
Nodes (48): PlayerChannelPreferences, Player channel preferences model for Advanced Chat Channels.      Stores player, PlayerPreferencesService, Any, AsyncSession, UUID, Get preferences for a player.          Args:             session: Database sessi, Update a player's default channel.          Args:             session: Database (+40 more)

### Community 167 - "test_room_renderer.py"
Cohesion: 0.04
Nodes (70): Unit tests for room_renderer utility functions.  Tests the utility functions in, Test clone_room_drops() returns empty list for None., Test format_room_drop_lines() formats room drops., Test format_room_drop_lines() returns empty message for empty drops., Test format_room_drop_lines() handles None., Test format_room_drop_lines() uses fallback for missing item_name., Test build_room_drop_summary() returns newline-separated summary., Test build_room_drop_summary() handles empty drops. (+62 more)

### Community 168 - "chat_service.py"
Cohesion: 0.08
Nodes (52): ChatMessage, ChatMessage, create_and_log_chat_message(), create_and_log_say_message(), Message creation and storage helpers for chat service., Create chat message and log it., Create say chat message and log it., Store message in room history with limit management. (+44 more)

### Community 169 - "test_rescue_service.py"
Cohesion: 0.04
Nodes (57): async_session_factory(), lucidity_service_factory(), mock_event_dispatcher(), mock_lucidity_service(), mock_persistence(), mock_session(), Unit tests for rescue service.  Tests the RescueService class for performing res, Test rescue() returns error when persistence is not available. (+49 more)

### Community 170 - "projectorHandlersMessages.ts"
Cohesion: 0.04
Nodes (70): _dispatch_player_event(), _format_liabilities(), LucidityChangeEventExtras, LiabilityStackEntry, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send an event to a specific player, swallowing transport errors in headless test (+62 more)

### Community 171 - "useGameConnectionRefactored.ts"
Cohesion: 0.16
Nodes (11): ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach(), wsConnectionBeforeEach(), wsTestState (+3 more)

### Community 172 - "AggressiveMobNPC"
Cohesion: 0.06
Nodes (47): _apply_player_status_with_grace_check(), _apply_status_effect_to_player(), _grace_period_blocks_negative_status_effect(), _handle_player_status_effect(), _parse_status_effect_metadata(), Any, UUID, Status effect spell logic (apply/remove status, force-flee, grace-period checks) (+39 more)

### Community 173 - "test_spell_effects.py"
Cohesion: 0.05
Nodes (39): Unit tests for room subscription manager helper functions.  Tests the helper fun, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully., Test get_stats() returns stats for empty manager. (+31 more)

### Community 174 - "ZoneConfiguration"
Cohesion: 0.01
Nodes (198): PopulationStats, Any, Statistics for NPC population in a zone or sub-zone., Initialize population statistics.          Args:             zone_id: The zone i, Add an NPC to the population statistics.          Args:             npc_type: Ty, Remove an NPC from the population statistics.          Args:             npc_typ, Convert population statistics to dictionary., NPCSpawnRequest (+190 more)

### Community 175 - "test_party_service.py"
Cohesion: 0.03
Nodes (105): PartyUpdated, Event fired when party membership or leadership changes.      Emitted by PartySe, Party, PartyService, Any, UUID, Party service for MythosMUD.  In-memory ephemeral party state: parties exist onl, Create a new party with the given player as leader.          Returns dict with s (+97 more)

### Community 176 - "get_cache_manager"
Cohesion: 0.13
Nodes (12): bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for NP, NPCCacheService, Service for caching NPC definitions and spawn rules., Get NPC definitions with caching.          Args:             session: Database s (+4 more)

### Community 177 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (33): CatatoniaRegistry, datetime, UUID, Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not deboun, Unit tests for catatonia registry.  Tests the CatatoniaRegistry class for tracki (+25 more)

### Community 178 - "test_nats_broker.py"
Cohesion: 0.03
Nodes (61): Exception raised when request-reply fails., RequestError, nats_config(), Unit tests for NATS message broker.  Tests the NATSMessageBroker class., Test disconnect() does nothing when no client., Test disconnect() successfully disconnects., Test disconnect() unsubscribes from all subscriptions., Test disconnect() handles unsubscribe errors gracefully. (+53 more)

### Community 179 - "._is_valid_name_for_occupant"
Cohesion: 0.24
Nodes (7): Any, Process a dictionary occupant and add to appropriate lists if valid.          Ar, Separate occupants into players, NPCs, and all occupants lists.          Args:, Check if a name is valid for use as an occupant name.          Args:, Add a valid name to both target list and all occupants list.          Args:, Process a player name and add to appropriate lists if valid.          Args:, Process an NPC name and add to appropriate lists if valid.          Args:

### Community 180 - "App.tsx"
Cohesion: 0.09
Nodes (28): App(), fetchSpy, AppRouter(), MapPage, SkillsPage, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full (+20 more)

### Community 181 - "CommandRequest"
Cohesion: 0.07
Nodes (29): Setup base behavior rules common to all NPCs., Return stats[key] as int, or default if missing/None., Return current_dp, max_dp, dexterity for CombatParticipantData., Heal and update determination points (DP)., Write new_dp to determination_points and dp for backward compatibility., Initialize the NPC base class., Get attribute from obj with default to avoid lazy-loading issues., Set npc_type, name, current_room, spawn_room_id from definition. (+21 more)

### Community 182 - "MemoryMonitor"
Cohesion: 0.06
Nodes (15): ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor, MemoryMonitorOptions (+7 more)

### Community 183 - "test_world.py"
Cohesion: 0.05
Nodes (37): mock_combat_memory(), mock_combat_result(), mock_data_provider(), mock_lifecycle(), mock_messaging_integration(), mock_npc_instance(), mock_rewards(), npc_combat_handlers() (+29 more)

### Community 184 - "test_inventory_commands.py"
Cohesion: 0.05
Nodes (64): Remove or update item quantity in player inventory after transfer., remove_item_from_inventory(), handle_pickup_command(), Move an item stack from room drops into the player's inventory., handle_put_command(), _put_resolve_container_id(), _put_run_validated(), _put_transfer_finish() (+56 more)

### Community 185 - "fastapi_integration.py"
Cohesion: 0.07
Nodes (30): _create_get_app(), main(), Any, FastAPI, MythosMUD Server - Main Application Entry Point  This module serves as the prima, Root endpoint providing basic server information., Test endpoint to verify JWT authentication is working., Main entry point for the MythosMUD server. (+22 more)

### Community 186 - "test_logout_commands.py"
Cohesion: 0.03
Nodes (102): _clear_corrupted_cache_entry(), _disconnect_player_connections(), _get_player_for_logout(), _get_player_position_from_connection_manager(), handle_logout_command(), Any, Logout and quit command handlers for MythosMUD.  This module contains handlers f, Update and save player's last active timestamp.      Args:         persistence: (+94 more)

### Community 187 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 188 - "QuestService"
Cohesion: 0.06
Nodes (44): _call_add_item_to_inventory(), _definition_completion_mode_error(), _goals_met(), _has_collect_n_goals(), _parse_definition(), Any, UUID, QuestService (+36 more)

### Community 189 - "NATSMessageBroker"
Cohesion: 0.06
Nodes (29): PublishError, Exception raised when publishing message fails., NATSMessageBroker, Any, Exception, Connect to NATS server.          Returns:             bool: True if connection s, Check if connected to NATS and healthy.          Returns:             bool: True, Publish message to NATS subject.          Args:             subject: NATS subjec (+21 more)

### Community 190 - "lucidity_service.py"
Cohesion: 0.05
Nodes (37): Unit tests for command_parser helper methods.  Tests the helper methods in Comma, Test _create_command_object() handles 'l' alias., Test _create_command_object() handles 'g' alias., Test _create_command_object() handles 'w' alias., Test _create_command_object() raises error for unsupported command., Test _create_command_object() handles PydanticValidationError., Test _create_command_object() handles ValueError., Test _normalize_command() removes leading slash. (+29 more)

### Community 191 - "MemoryProfiler"
Cohesion: 0.07
Nodes (37): BaseModel, Unit tests for memory profiler utilities.  Tests the MemoryProfiler class method, Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test Pydantic model for memory profiling tests., Test MemoryProfiler.print_model_memory_usage() doesn't raise., Test MemoryProfiler initialization. (+29 more)

### Community 192 - "._prepare_sanitarium_respawn"
Cohesion: 0.05
Nodes (51): _PlayerCombatClearing, PlayerRespawnService, AsyncSession, datetime, Player, Protocol, UUID, _RandomChoiceSource (+43 more)

### Community 193 - "__init__.py"
Cohesion: 0.04
Nodes (66): CombatCommandHandler, Any, AppWithState, Combat service for command modules., Movement service for command modules., Player position service for command modules., Item prototype registry for command modules., Check if player is resting or in login grace period, interrupt rest if needed. P (+58 more)

### Community 194 - "metrics.py"
Cohesion: 0.06
Nodes (75): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+67 more)

### Community 195 - "NPCMovementIntegration"
Cohesion: 0.10
Nodes (25): applyModalBodyScrollLock(), deriveEdgeCreationData(), EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModal(), EdgeCreationModalViewProps, edgeFormCanSubmit(), EdgeFormFields, EdgeFormResetters (+17 more)

### Community 196 - "test_movement_monitor.py"
Cohesion: 0.04
Nodes (53): Unit tests for movement monitor.  Tests the MovementMonitor class for monitoring, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data., Test validate_room_integrity() detects duplicate players., Test validate_room_integrity() handles empty rooms dict., Test validate_room_integrity() handles rooms without get_players method., Test get_metrics() returns metrics for empty monitor. (+45 more)

### Community 197 - "test_command_factories_moderation.py"
Cohesion: 0.24
Nodes (14): AuthSessionSetters, persistTokensAndApplySession(), SetBool, SetChars, SetStep, toCharacterInfoFromLogin(), AuthSuccessPayload, SanitizedCredentials (+6 more)

### Community 198 - ".check_level_up"
Cohesion: 0.06
Nodes (19): UUID, Resolve the player and UUID needed for DP update events., Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated., Publish the PlayerDPUpdated event to the event bus., Publish NPC-on-player attack as player_attacked to NATS so the client receives i, Resolve target UUID, player object, and stats needed for NATS attack event., Construct the PlayerAttackedEvent payload for NATS publication., Handle NPC death and related effects.          Args:             npc_id: ID of t (+11 more)

### Community 199 - "auth.ts"
Cohesion: 0.08
Nodes (33): clickLogout(), assertCommandChannelReady(), clickWithoutStability(), EnsurePlayableConnectionOptions, executeCommandTrusted(), executeCommandWithoutRecovery(), isPageUsable(), isUsernameLoginVisible() (+25 more)

### Community 200 - "test_corpse_lifecycle_service.py"
Cohesion: 0.03
Nodes (96): CorpseLifecycleService, CorpseNotFoundError, CorpseServiceError, _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID (+88 more)

### Community 201 - "test_follow_service.py"
Cohesion: 0.03
Nodes (65): connection_manager(), event_bus(), follow_service(), movement_service(), Unit tests for FollowService.  Covers: request_follow (self reject, NPC immediat, If already following someone, request_follow is rejected., Accepting a follow request establishes follow and notifies both., Declining removes pending request and does not add follow. (+57 more)

### Community 202 - "test_alias_storage.py"
Cohesion: 0.02
Nodes (112): Path, Unit tests for alias storage utilities.  Tests the AliasStorage class for managi, Test _load_alias_data handles invalid JSON gracefully., Test _load_alias_data handles IO errors gracefully., Test _save_alias_data successfully saves data., Test _save_alias_data handles IO errors., Test get_player_aliases returns empty list for player with no aliases., Test get_player_aliases returns aliases from file. (+104 more)

### Community 203 - "test_map_helpers.py"
Cohesion: 0.08
Nodes (35): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities.  Extracted from maps.p (+27 more)

### Community 204 - "TaskRegistry"
Cohesion: 0.01
Nodes (256): MockerFixture, Read process output in background thread., read_output(), create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryThresholdMonitor, Any, Managed Task Cleanup Service - Runtime Detection for Memory Threshold Monitoring (+248 more)

### Community 205 - "test_game_state_provider.py"
Cohesion: 0.04
Nodes (51): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), Unit tests for game state provider.  Tests the GameStateProvider class., Test get_players_batch() handles player not found., Test get_npcs_batch() returns NPC names. (+43 more)

### Community 206 - "test_room_subscription_manager.py"
Cohesion: 0.04
Nodes (51): Unit tests for room subscription manager.  Tests the RoomSubscriptionManager cla, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test add_room_occupant() adds occupant., Test add_room_occupant() with multiple occupants., Test add_room_occupant() adds occupant to new room., Test add_room_occupant() adds occupant to existing room., Test remove_room_occupant() removes occupant. (+43 more)

### Community 207 - "websocket_helpers.py"
Cohesion: 0.04
Nodes (68): Unit tests for command_helpers utility functions.  Tests the utility functions i, Test validate_command_safety() returns True for safe commands., Test validate_command_safety() returns False for shell metacharacters., Test validate_command_safety() returns False for SQL injection attempts., Test validate_command_safety() returns False for Python injection attempts., Test validate_command_safety() returns False for format string injection., Test validate_command_safety() returns False for XSS attempts., Test get_command_help() returns help for specific command. (+60 more)

### Community 208 - "test_websocket_handler_helpers_extended.py"
Cohesion: 0.04
Nodes (51): mock_connection_manager(), mock_validator(), mock_websocket(), Extended unit tests for websocket handler helper functions.  Tests additional he, Test _send_error_response() handles WebSocketDisconnect., Test _send_error_response() returns False for RuntimeError indicating disconnect, Test _send_error_response() returns False for RuntimeError with close message., Test _send_error_response() returns True for other errors. (+43 more)

### Community 209 - "FStringLoggingFixer"
Cohesion: 0.05
Nodes (43): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+35 more)

### Community 210 - "correlation_middleware.py"
Cohesion: 0.04
Nodes (42): bench_room_cache(), _FakePersistence, main(), Any, Lightweight cache benchmark for CI artifacts.  Measures miss vs. hit timings for, Fake persistence layer providing async_get_room with simulated latency., Service for caching room data., Get room data with caching.          Args:             room_id: The room ID (+34 more)

### Community 211 - "RoomMapEditorRuntime.tsx"
Cohesion: 0.11
Nodes (30): EdgeCreationModalProps, EdgeDetailsPanel(), EdgeDetailsPanelProps, EdgeCreationData, EdgeValidationResult, HistoryEntry, MapEditingChanges, useMapEditing() (+22 more)

### Community 212 - "test_connection_statistics.py"
Cohesion: 0.04
Nodes (43): _build_combat_instance(), _build_participant(), CombatInitializer, _compute_turn_order(), UUID, Combat initialization logic.  Handles creation and setup of combat instances., Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds * 10, Build CombatParticipant from CombatParticipantData. (+35 more)

### Community 213 - "logging_file_setup.py"
Cohesion: 0.05
Nodes (74): Formatter, Handler, Logger, _PlayerGuidFormatterType, Queue, QueueListener, _add_handler_to_loggers(), _CategoryHandlerConfig (+66 more)

### Community 214 - "test_connection_session_management.py"
Cohesion: 0.06
Nodes (59): _cleanup_old_session_tracking(), _cleanup_player_data_for_session(), _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), handle_new_game_session_impl(), _is_websocket_connected(), Any, UUID (+51 more)

### Community 215 - "safe_run_static"
Cohesion: 0.07
Nodes (35): get_project_root(), Determine the project root based on current working directory, _is_tool_crash(), Return True when sqlint failed to start rather than reporting SQL issues., Return sqlint command argv when the tool is installed and runnable., _resolve_sqlint_cmd(), Any, CompletedProcess (+27 more)

### Community 216 - "gen_arena_migration_sql.py"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 217 - "NPCThreadManager"
Cohesion: 0.10
Nodes (16): CORSConfig, Any, BaseSettings, Parse comma-separated string into cleaned list., Parse comma separated strings or lists into a cleaned list of strings., Parse allowed origins from various input formats., Parse and validate CORS allowed methods. Converts all methods to uppercase., Parse and validate CORS allowed headers. (+8 more)

### Community 218 - "container_helpers_inventory_display.py"
Cohesion: 0.05
Nodes (65): create_access_token(), decode_access_token(), timedelta, Decode and validate a JWT access token., Create a JWT access token., MonkeyPatch, Unit tests for authentication utilities., Test decoding invalid access token returns None. (+57 more)

### Community 219 - "test_command_combat.py"
Cohesion: 0.02
Nodes (106): AttackCommand, KickCommand, PunchCommand, Command for attacking a target., Validate combat target name format using centralized validation., Command for punching a target., Validate combat target name format using centralized validation., Command for kicking a target. (+98 more)

### Community 220 - "gameStore.ts"
Cohesion: 0.16
Nodes (25): fetchSpy, useMapLayout(), useRoomMapData(), UseRoomMapDataResult, MapControls(), MapControlsProps, RoomDetailsPanel(), RoomDetailsPanelProps (+17 more)

### Community 221 - "PatternNotFoundError"
Cohesion: 0.04
Nodes (62): handle_chat_message(), handle_websocket_connection(), UUID, Handle a WebSocket connection for a player.      Args:         websocket: The We, Handle a chat message from a player.      Args:         websocket: The WebSocket, Test handle_websocket_connection handles shutdown rejection., Test handle_websocket_connection handles connection failure., Test handle_websocket_connection handles should_exit from initial state. (+54 more)

### Community 222 - "RoomDataValidator"
Cohesion: 0.06
Nodes (39): Any, Validate occupant count consistency.          Args:             room_data: Room, Validate room ID format.          Args:             room_id: Room ID to validate, Check if occupant count matches the actual occupants list length.          Args:, Validates room data structure and content., Check for duplicate occupants in the room.          Args:             room_data:, Check if room has occupants but no name.          Args:             room_data: R, Validate room data structure and content.          Args:             room_data: (+31 more)

### Community 223 - "NPC Duplication Bug Fix Plan"
Cohesion: 0.04
Nodes (47): 1.1 Remove Duplicate Event Subscription, 1.2 Verify Population Controller Authority, 2.1 Atomic Population Updates, 2.2 Add Spawn Validation Lock, 3.1 Consolidate Spawn Logic, 3.2 Improve Service Integration, 4.1 Unit Tests, 4.2 Integration Tests (+39 more)

### Community 224 - "test_websocket_helpers.py"
Cohesion: 0.24
Nodes (8): Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (be, Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (be, schedule_end_combat_if_npc_died_best_effort(), Unit tests for best-effort NPC combat cleanup scheduling., When combat service is missing, scheduling is a no-op., Without a running asyncio loop, scheduling fails quietly (RuntimeError path)., test_schedule_end_combat_if_npc_died_no_running_loop(), test_schedule_end_combat_if_npc_died_no_service()

### Community 225 - "CombatMonitoringService"
Cohesion: 0.04
Nodes (49): Alert, AlertSeverity, AlertType, CombatMonitoringService, end_combat_monitoring(), get_combat_monitoring(), Any, Enum (+41 more)

### Community 226 - "command_input.py"
Cohesion: 0.05
Nodes (56): CastCommand, LearnCommand, Magic command models for MythosMUD.  This module provides command models for mag, Command for casting a spell., Validate spell name format., Validate target format., Command for viewing spell details., Validate spell name format. (+48 more)

### Community 227 - "PassiveMobNPC"
Cohesion: 0.31
Nodes (9): _int_opt(), _opt_str(), Any, Return str(val) or empty string if val is None., Return int value or default if val is None., Return str value or default if val is None., Map procedure result row to PlayerEffect model., _row_to_player_effect() (+1 more)

### Community 228 - "UUID"
Cohesion: 0.04
Nodes (28): Any, UUID, Normalize player identifiers to string form., Send a local message to players in the same sub-zone.          This method publi, Send a global message to all players.          This method publishes the global, Send a party (ephemeral group) chat message. Only current party members, Send a system message to all players.          This method publishes the system, Send a whisper message from one player to another.          This method publishe (+20 more)

### Community 229 - "container_persistence.py"
Cohesion: 0.03
Nodes (173): Composed, ContainerCreateParams, Shared parameters for container creation (sync DB and async repository paths)., Optional fields for creating a container row (beyond source_type)., ContainerData, ContainerDataCore, ContainerDataExtras, Container data class for persistence operations. (+165 more)

### Community 230 - "TestValidatorIntegration"
Cohesion: 0.12
Nodes (15): dead_end_room(), invalid_room_data(), Pytest configuration and fixtures for room validator tests.  Provides test data, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit., Room data with no exits (dead end). (+7 more)

### Community 231 - "useGameTerminal.ts"
Cohesion: 0.05
Nodes (40): GameTerminalContainer(), useGameTerminalMock, GameTerminalState, mockCommandState, mockConnectionState, mockGameState, mockSessionState, testCommandHistoryCap (+32 more)

### Community 232 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 233 - "ChatModeration"
Cohesion: 0.07
Nodes (31): ChatModeration, normalize_player_id(), PlayerServiceProtocol, Any, datetime, UUID, Chat moderation utilities.  This module provides moderation functionality includ, Mute a specific channel for a player. (+23 more)

### Community 234 - "NATSRetryHandler"
Cohesion: 0.04
Nodes (76): NATSRetryHandler, Any, Exception, Calculate exponential backoff delay with jitter.          Args:             atte, Determine if a message should be retried.          Args:             message: Me, Retry a function with exponential backoff.          Args:             func: Asyn, Get retry statistics.          Returns:             Dictionary with retry metric, Retry async function with exponential backoff.          Attempts the function up (+68 more)

### Community 235 - "NATSEventBusBridge"
Cohesion: 0.02
Nodes (109): DistributedEventBus, Any, Distributed EventBus that uses NATS for cross-instance event distribution.  Wrap, EventBus that distributes domain events via NATS for horizontal scaling.      Wh, Initialize distributed EventBus.          Args:             nats_service: NATS s, Set NATS service and start the bridge (call after NATS connects)., Publish event locally and to NATS when bridge is active., Shutdown EventBus and stop NATS bridge. (+101 more)

### Community 236 - "test_player_occupant_processor.py"
Cohesion: 0.04
Nodes (47): mock_connection_manager(), mock_name_extractor(), processor(), Unit tests for player occupant processor.  Tests the PlayerOccupantProcessor cla, Test _convert_player_ids_to_uuids handles mixed string and UUID types., Test _convert_player_ids_to_uuids handles UUID objects., Test _create_player_occupant_info returns None for invalid name., Test _create_player_occupant_info adds (linkdead) indicator. (+39 more)

### Community 237 - "test_who_commands.py"
Cohesion: 0.08
Nodes (23): Unit tests for who commands., Test filter_online_players with some players offline., Test filter_online_players with players without last_active., Test filtering players with no filter term., Test format_who_result with no players and filter term., Test format_who_result with players., Test handle_who_command when no players are found., Test handle_who_command successful execution. (+15 more)

### Community 239 - "Player"
Cohesion: 0.02
Nodes (157): PlayerCreationService, Any, Stats, UUID, Player creation service.  This module handles player character creation operatio, Create a new player character with specific stats.          Args:             na, Service for player creation operations., Initialize with persistence layer, schema converter, and optional instance manag (+149 more)

### Community 240 - "npc_definitions_api.py"
Cohesion: 0.02
Nodes (227): cleanup_admin_sessions(), get_admin_audit_log(), get_admin_sessions(), Request, Admin session and audit log endpoints under /admin/npc.  Split out from server.a, Get active admin sessions., Clean up expired admin sessions., create_npc_definition() (+219 more)

### Community 241 - "look_command.py"
Cohesion: 0.15
Nodes (24): _get_app_and_persistence(), _get_room_drops(), handle_look_command(), Any, Look command for MythosMUD.  This module handles the look command for examining, Try to handle explicit player look., Try to handle explicit item look., Try to handle explicit container look or container inspection. (+16 more)

### Community 242 - "datetime"
Cohesion: 0.04
Nodes (56): HolidayResolver, MythosHourTickEvent, Event fired when the accelerated Mythos clock rolls over to a new hour., Time management package for MythosMUD.  This package provides time-related servi, MythosTickScheduler, datetime, Sleep until the next Mythos hour boundary, respecting compression ratio., Publish the hourly tick event to the EventBus. (+48 more)

### Community 243 - "error_handling_middleware.py"
Cohesion: 0.06
Nodes (42): Response, add_error_handling_middleware(), ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Exception, FastAPI, Protocol (+34 more)

### Community 244 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.06
Nodes (51): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+43 more)

### Community 245 - "GameLogPanel.tsx"
Cohesion: 0.07
Nodes (39): GameLogListMessage, GameLogMessagesList(), GameLogMessagesListProps, GameLogPanel(), GameLogPanelProps, GameLogPanelFilterBar(), GameLogPanelFilterBarProps, GameLogPanelHeader() (+31 more)

### Community 246 - "LogAggregator"
Cohesion: 0.07
Nodes (28): aggregate_log_entry(), get_log_aggregator(), LogAggregator, LogEntry, Any, datetime, Path, Log aggregation and centralized collection system for MythosMUD server.  This mo (+20 more)

### Community 247 - "LRUCache"
Cohesion: 0.02
Nodes (83): K, bench_profession_cache(), _FakePersistence, _get_empty_dict(), main(), Any, Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit timing, Helper function to return empty dict for mock methods. (+75 more)

### Community 248 - "SubjectValidationError"
Cohesion: 0.06
Nodes (44): Custom exceptions for NATS Subject Manager.  This module defines all exception c, Exception raised when subject validation fails., SubjectValidationError, NATS Subject Manager for MythosMUD.  This package provides centralized subject n, NATS Subject Manager for MythosMUD.  This module provides centralized subject na, Performance metrics for NATS Subject Manager operations.  This module provides m, Predefined subject patterns for MythosMUD chat system.  This module contains all, get_chat_subscription_patterns() (+36 more)

### Community 249 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 250 - "testing_examples.py"
Cohesion: 0.10
Nodes (21): LoggingMiddleware, Test that sensitive data is properly sanitized in logs., Test logging performance metrics., Test basic logging functionality., Test logging correlation IDs., Test logging in middleware., Test error logging functionality., Simulate middleware processing. (+13 more)

### Community 251 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 252 - "test_nats_messages.py"
Cohesion: 0.06
Nodes (48): Realtime domain schemas: realtime API, NATS messages, WebSocket messages., BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, Pydantic schemas for NATS message validation.  This module provides type-safe me, Validate an event message against the schema.      Args:         data: Message d (+40 more)

### Community 253 - "User Experience & Commands"
Cohesion: 0.05
Nodes (42): 1. Chat Interface (`client/src/components/ChatInterface.tsx`), 1. Chat Service (`server/game/chat_service.py`), 2. Chat Hook (`client/src/hooks/useChat.ts`), 2. Chat Models (`server/models/chat.py`), 3. Chat API Endpoints (`server/api/chat.py`), Advanced Features (Issue #58), Backend Components, Channel Management Commands (+34 more)

### Community 254 - "coerce_int"
Cohesion: 0.11
Nodes (15): Get player stats as dictionary.          Returns a MutableDict instance that aut, Set player stats from dictionary.          Accepts both plain dict and MutableDi, Check if player is alive (DP > 0)., Check if player is mortally wounded (0 >= DP > -10).          Returns:, Check if player is dead (DP <= -10).          Returns:             True if playe, Get player's current health state.          Returns:             "alive" if DP >, Get stats used for combat participant creation.          Returns current_dp, max, Get player determination points (DP) as percentage. (+7 more)

### Community 255 - "PydanticErrorHandler"
Cohesion: 0.22
Nodes (18): _cleanup_dead_connections(), establish_websocket_connection(), Any, UUID, WebSocket, Connection establishment management for connection manager.  This module handles, Register a new WebSocket connection.      Args:         websocket: The WebSocket, Create and store connection metadata.      Args:         connection_id: The conn (+10 more)

### Community 256 - "NPCDefinitionCRUDMixin"
Cohesion: 0.10
Nodes (20): NPCDefinitionCRUDMixin, Any, AsyncSession, Execute create_npc_definition stored procedure and return the created definition, Validate create_npc_definition parameters. Raises ValueError if invalid., Log successful NPC definition creation., Validate NPC update parameters., Add a simple field to update_data if value is not None. (+12 more)

### Community 257 - "PlayerInventory"
Cohesion: 0.11
Nodes (19): Initialize the player repository.          Args:             room_cache: Shared, _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Player save/upsert helpers for PlayerRepository.  Handles inventory validation, (+11 more)

### Community 258 - "test_memory_leak_metrics.py"
Cohesion: 0.05
Nodes (41): collector(), Unit tests for memory leak metrics collector.  Tests the MemoryLeakMetricsCollec, Test collection of cache metrics., Test collection of task metrics., Test collection of NATS metrics., Test collection of all metrics., Test calculation of growth rates., Create a MemoryLeakMetricsCollector instance. (+33 more)

### Community 259 - "test_room_utils.py"
Cohesion: 0.05
Nodes (56): _build_legacy_subject(), build_nats_subject(), _build_standardized_subject(), _extract_subzone_from_room(), Any, Chat NATS publishing utilities.  This module provides NATS subject building and, Build NATS subject using standardized patterns or fallback to legacy constructio, Extract subzone from room_id, returning 'unknown' if extraction fails. (+48 more)

### Community 260 - "Enhanced Logging Implementation Summary"
Cohesion: 0.05
Nodes (40): 1. **Fixed Context Parameter Usage** ✅, 2. **Implemented MDC (Mapped Diagnostic Context)** ✅, 3. **Added Correlation IDs for Request Tracing** ✅, 4. **Implemented Security Sanitization** ✅, 5. **Performance Optimization with Async Logging** ✅, 6. **Enhanced Error Handling with Structured Logging** ✅, 7. **Log Aggregation and Centralized Collection** ✅, 8. **Monitoring Integration with Metrics** ✅ (+32 more)

### Community 261 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 262 - "GameTerminal.tsx"
Cohesion: 0.04
Nodes (41): buildHealthStatus(), ChatMessage, formatPosture(), GameTerminal(), Player, Room, GameTerminalPresentation(), GameTerminalPresentationProps (+33 more)

### Community 263 - "executeCommand"
Cohesion: 0.11
Nodes (36): assertNpcSpawnVisible(), hasCombatMessage(), isInCombatStatus(), isInDeathVoid(), isWardBlockingCombat(), keepFirstCultistInstanceId(), resolveSpawnedCultistTarget(), retryUntilCombatStarted() (+28 more)

### Community 264 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 265 - "deprecated_patterns.py"
Cohesion: 0.09
Nodes (22): deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_logging_in_loops(), deprecated_logging_without_context(), deprecated_performance_logging(), deprecated_request_context(), deprecated_security_logging() (+14 more)

### Community 266 - "test_game_tick_processing_async.py"
Cohesion: 0.03
Nodes (124): broadcast_tick_event(), cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _create_corpse_lifecycle_service(), game_tick_loop(), get_current_tick(), get_tick_interval(), _log_cleanup_results() (+116 more)

### Community 267 - "game_tick_processing.py"
Cohesion: 0.10
Nodes (30): handle_chat_message(), handle_client_error_report_message(), handle_command_message(), handle_follow_response_message(), handle_party_invite_response_message(), handle_ping_message(), Any, WebSocket (+22 more)

### Community 268 - "test_admin_shutdown_command.py"
Cohesion: 0.03
Nodes (61): Unit tests for admin command handlers.  Tests the admin command handler function, Test handle_mute_command() with no target player., Test handle_mute_command() successful execution., Test handle_unmute_command() when user manager is not available., Test handle_unmute_command() with no target player., Test handle_unmute_command() successful execution., Test handle_unmute_command() succeeds when target was not muted (E2E cleanup pat, Test handle_mute_global_command() when user manager is not available. (+53 more)

### Community 269 - "test_combat_schema.py"
Cohesion: 0.07
Nodes (57): Draft7Validator, add_default_combat_data_to_config(), add_default_combat_data_to_stats(), CombatSchemaValidationError, get_combat_stats_summary(), Any, Exception, Combat system JSON schema validation.  This module provides JSON schema validati (+49 more)

### Community 270 - "quest_commands.py"
Cohesion: 0.05
Nodes (69): ExitStack, _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence(), _get_quest_service(), handle_journal_command() (+61 more)

### Community 271 - "test_look_item.py"
Cohesion: 0.05
Nodes (39): mock_prototype_registry(), Unit tests for item look functionality.  Tests the helper functions for looking, Test finding item in equipped items by name., Test getting item description from prototype., Test getting item description with fallback name when prototype exists., Test checking item in location with location name., Test checking item in location when prototype not found., Test checking equipped item successfully. (+31 more)

### Community 272 - "test_population_stats.py"
Cohesion: 0.05
Nodes (37): Any, Stats, Roll Size using formula: (2D6+6)*5 (range 40-90)., Roll stats using 3d6 method (scaled to 15-90 range)., Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)., Generate stats using a point-buy system (balanced, scaled to 1-100 range)., Check if stats meet the prerequisites for a given class.          Args:, Get a list of classes that the character qualifies for.          Args: (+29 more)

### Community 273 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.04
Nodes (58): check_shutdown_and_reject(), convert_uuids_to_strings(), load_player_mute_data(), WebSocket, Load player mute data when they connect.      AI: Uses async version to avoid, Recursively convert UUID objects to strings for JSON serialization., Check if server is shutting down and reject connection if so. Returns True if re, Unit tests for WebSocket helpers.  Tests the websocket_helpers module functions. (+50 more)

### Community 274 - "version"
Cohesion: 0.20
Nodes (10): description, items, type, $ref, properties, aliases, version, description (+2 more)

### Community 275 - "AsciiMapRenderer"
Cohesion: 0.03
Nodes (57): AsciiMapRenderer, Any, Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if i, Return list of (direction, (target_x, target_y), is_bidirectional) for exits, Build exit lookup map from room data., Center viewport on the character's current room so the player is in the middle o, Render a single row of rooms with horizontal exits., Render a single row of vertical exits between room rows. (+49 more)

### Community 276 - "combat_attack.py"
Cohesion: 0.08
Nodes (37): _execute_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution.  Extracted from combat.py to redu, Resolve damage from equipped weapon or fall back to config unarmed damage., Execute combat action using the proper combat service., Handle attack commands (attack, punch, kick, etc.)., Validate target name, load player/room, check DP and no_combat.     Returns (pla (+29 more)

### Community 277 - "PlayerLucidity"
Cohesion: 0.06
Nodes (35): Unit tests for rescue command handlers.  Tests the rescue command functionality., Test handle_ground_command() handles missing target., Test handle_ground_command() handles rescuer not found., Test handle_ground_command() handles target not found., Test handle_ground_command() handles different rooms., Test handle_ground_command() handles rescuer with no room., Test handle_ground_command() handles missing lucidity record., Test handle_rescue_command() delegates to RescueService. (+27 more)

### Community 278 - "test_command_processor.py"
Cohesion: 0.04
Nodes (55): Unit tests for command processor.  Tests the CommandProcessor class which integr, Test process_command_string handles KeyError., Test process_command_string handles RuntimeError., Test _extract_attributes extracts attributes correctly., Test _extract_attributes handles missing attributes., Test _is_combat_command returns True for attack command., Test _is_combat_command returns True for punch command., Test _is_combat_command returns True for kick command. (+47 more)

### Community 279 - ".__post_init__"
Cohesion: 0.10
Nodes (22): _coerce_xp_mapping_value(), _NPCCombatIntegrationValidationDeps, NPCCombatIntegrationValidationMixin, Protocol, UUID, Validation and UUID-mapping helpers for NPC combat integration (mixin)., Validate that player and NPC are in the same room., End any active combat that includes this player when room validation fails. (+14 more)

### Community 280 - "verify_enhanced_logging_compliance.py"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 281 - "test_item.py"
Cohesion: 0.01
Nodes (253): PlayerDeliriumRespawnedEvent, Event fired when a player respawns after delirium.      This event is triggered, Player respawn wrapper service.  This module provides wrapper methods for player, Base, DeclarativeBase, Shared SQLAlchemy DeclarativeBase for all models.  This module provides a single, Shared declarative base for all MythosMUD models.      All models (User, Player,, HolidayModel (+245 more)

### Community 282 - "GameClientV2ContainerView.tsx"
Cohesion: 0.07
Nodes (52): _FloorPickupResolved, Protocol, Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, add_pickup_to_inventory(), get_room_manager(), prepare_extracted_stack(), UUID (+44 more)

### Community 283 - "deque"
Cohesion: 0.09
Nodes (48): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+40 more)

### Community 284 - "character-cleanup.ts"
Cohesion: 0.10
Nodes (25): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+17 more)

### Community 285 - "test_pattern_matcher.py"
Cohesion: 0.05
Nodes (43): Initialize NATS Subject Manager.          Args:             enable_cache: Enable, PatternMatcher, Any, Pattern matching utilities for NATS Subject Manager.  This module provides patte, Matcher for validating subjects against registered patterns., Initialize pattern matcher.          Args:             strict_validation: Enable, Check if subject matches any registered pattern.          Args:             subj, Check if subject components match a pattern.          Args:             componen (+35 more)

### Community 286 - "compare_linting_results.py"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 287 - "monitoring.py"
Cohesion: 0.02
Nodes (153): PerformanceStats, Response model for system metrics., SystemMetricsResponse, get_system_health(), get_system_metrics(), get_system_monitoring_alerts(), get_system_monitoring_summary(), Request (+145 more)

### Community 288 - "test_connection_cleaner.py"
Cohesion: 0.08
Nodes (27): ConnectionCleaner, Any, UUID, Connection cleanup and maintenance for connection management.  This module provi, Identify players whose last_seen timestamp exceeds the max age.          Args:, Remove all data for a stale player.          Args:             pid: Player ID to, Remove players whose presence is stale beyond the threshold.          Args:, Return connection IDs that exceed max_connection_age. (+19 more)

### Community 289 - "TestCombatMessagingService"
Cohesion: 0.04
Nodes (56): HealthStatus, StrEnum, Health status enumeration for system components., get_health_service(), Get the global health service instance.      Args:         connection_manager: O, mock_connection_manager(), Unit tests for health service.  Tests the health monitoring service for system h, Test check_database_health returns degraded status. (+48 more)

### Community 290 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible.          Args:             roo (+21 more)

### Community 291 - "test_npc_combat_handlers.py"
Cohesion: 0.05
Nodes (46): _inventory_item_with_weapon(), PlayerSchemaConverter, Any, Get stats, inventory, and status_effects from player, handling async methods., Compute derived stats fields (max_dp, max_magic_points, max_lucidity)., Get PositionState from position value, with fallback to STANDING., Create PlayerRead schema from player object., Create PlayerRead schema from player dictionary. (+38 more)

### Community 292 - "test_command_parser_helpers.py"
Cohesion: 0.02
Nodes (112): PlayerStateService, Any, UUID, Player state management service.  This module handles player state modifications, Gain occult knowledge (with lucidity loss).          Args:             player_id, Heal a player's health.          Args:             player_id: The player's ID (U, Service for managing player state modifications., Damage a player's health.          Args:             player_id: The player's ID (+104 more)

### Community 293 - "player_service"
Cohesion: 0.04
Nodes (55): mock_player_service(), mock_target_match(), Unit tests for spell effects.  Tests the SpellEffects class., Test process_effect() routes to lucidity adjust handler., Test process_effect() routes to corruption adjust handler., Test process_effect() routes to teleport handler., Test process_effect() routes to create object handler., Test process_effect() FLEE returns failure when combat/movement services not con (+47 more)

### Community 294 - "handle_read_command"
Cohesion: 0.05
Nodes (55): AttributeError, Any, Subscribe to room movement events for occupant broadcasting., subscribe_to_room_events_impl(), broadcast_game_event(), UUID, Public API utility functions for connection manager.  This module provides conve, Send a system notification to a player.      Args:         player_id: The player (+47 more)

### Community 295 - "test_dependency_injection.py"
Cohesion: 0.15
Nodes (19): AppCreationFlowViews(), AppDemoView(), CharacterNameScreen, CharacterSelectionScreen, EldritchEffectsDemo, GameClientV2Container, LoadingFallback(), MotdInterstitialScreen (+11 more)

### Community 296 - "Execution Steps"
Cohesion: 0.05
Nodes (36): BEFORE EXECUTING THIS SCENARIO, YOU MUST, BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, CONFIRMATION CHECKLIST, EXECUTION AFFIRMATION (Type this before proceeding), 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER, Execution Steps, Expected Results (+28 more)

### Community 297 - "test_combat_persistence_handler_persistence.py"
Cohesion: 0.05
Nodes (35): mock_combat_service(), persistence_handler(), Unit tests for combat persistence handler - persistence operations.  Tests playe, Test _persist_player_dp_sync calls _verify_player_save., Test _persist_player_dp_sync handles save_player error., Test _persist_player_dp_sync completes full flow with verification and logging., Test _persist_player_dp_sync handles get_stats error., Test _persist_player_dp_sync complete flow including verification. (+27 more)

### Community 298 - "EdgeCreationModal.tsx"
Cohesion: 0.04
Nodes (55): mock_app(), mock_connection_manager(), mock_player(), mock_request(), Unit tests for rest command handlers.  Tests the rest command functionality incl, Test handle_rest_command() handles missing persistence., Test handle_rest_command() handles missing connection manager., Test handle_rest_command() handles player not found. (+47 more)

### Community 299 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (50): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers.  These handlers avoid rename-while-open issu, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file.      This av, Copy the source log file to the destination, then truncate the source.      Publ, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+42 more)

### Community 300 - "ExplorationService"
Cohesion: 0.03
Nodes (81): _async_session_maker_mock(), exploration_service(), mock_database_manager(), Unit tests for exploration service.  Tests the ExplorationService class., Test mark_room_as_explored() returns False when room not found., Test mark_room_as_explored() raises DatabaseError on database failure., Test _get_room_uuid_by_stable_id() with provided session., Test _get_room_uuid_by_stable_id() creates session when none provided. (+73 more)

### Community 301 - "real_time.py"
Cohesion: 0.10
Nodes (40): _ensure_connection_manager(), _extract_bearer_token(), get_connection_statistics(), get_player_connections(), handle_new_game_session(), _parse_subprotocol_token(), _parse_websocket_token(), Any (+32 more)

### Community 302 - "_check_grace_period_block"
Cohesion: 0.04
Nodes (53): Reset the global async persistence instance for testing.      DEPRECATED: Use Ap, reset_async_persistence(), Unit tests for async persistence layer: health, container, item, singleton, cons, Test async_heal_player delegates to HealthRepository., Test damage_player delegates to HealthRepository., Test async_damage_player delegates to HealthRepository., Test get_container delegates to ContainerRepository., Test get_containers_by_room_id delegates to ContainerRepository. (+45 more)

### Community 303 - "EventHandler"
Cohesion: 0.04
Nodes (53): Unit tests for WebSocket handler validation, rate limiting, and error paths.  Te, _validate_message should pass expected token from connection metadata into valid, When metadata.token is missing, validate JWT from message and restore metadata., Test _send_error_response handles WebSocket disconnect., Test _send_error_response handles RuntimeError with disconnect message., Test _send_error_response handles RuntimeError with close message., Test _send_error_response handles other RuntimeError., Test _handle_websocket_disconnect returns True. (+45 more)

### Community 304 - "E2E Test Suite AI Execution Improvements - Summary"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 305 - "__init__.py"
Cohesion: 0.08
Nodes (40): FixtureRequest, Database fixtures for integration tests.  This module provides database connecti, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+32 more)

### Community 306 - "test_room_id_utils.py"
Cohesion: 0.04
Nodes (52): NPCOccupantProcessor, Any, NPC occupant processing utilities.  This module handles querying and processing, Determine if NPC should be included in room query results.          Args:, Scan active NPCs to find those in the target room.          Args:             ac, Processes NPC occupants for rooms., Initialize NPC occupant processor.          Args:             connection_manager, Query NPCs for a room from lifecycle manager.          Args:             room_id (+44 more)

### Community 307 - "test_command_base.py"
Cohesion: 0.08
Nodes (32): _FollowTargetValue, FollowService, _is_npc_follow_value(), Any, TypeGuard, UserManager, UUID, Send a command_response-style message to a single player. (+24 more)

### Community 308 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 309 - "TestHierarchicalSchema"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation.  This module tests the new hierar, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 310 - "BaseCommand"
Cohesion: 0.02
Nodes (165): Admin command models for MythosMUD.  This module provides command models for adm, AliasesCommand, Alias command models for MythosMUD.  This module provides command models for man, Command for listing all aliases., CommandType, Direction, StrEnum, Base command models and enums for MythosMUD.  This module provides the foundatio (+157 more)

### Community 312 - "Alias System Implementation Plan"
Cohesion: 0.06
Nodes (34): 1.1 Data Model and Storage, 1.2 Command Integration, 1.3 Client Integration, 2.1 Security Implementation, 2.2 User Experience, 3.1 Testing, 3.2 Documentation, Alias Management Commands (+26 more)

### Community 313 - "SchemaValidator"
Cohesion: 0.03
Nodes (60): create_validator(), Any, Path, Shared schema validator for room definition files.  This module provides JSON sc, Validate a room file against the schema.          Args:             file_path: P, Validate all rooms in a database against the schema.          Args:, Validate a serialized alias bundle against the alias schema.          Args:, Validate emote definition data against the emote schema.          Args: (+52 more)

### Community 314 - "migration_examples.py"
Cohesion: 0.05
Nodes (40): database, expensive_operation(), migration_example_1(), migration_example_10(), migration_example_11(), migration_example_12(), migration_example_13(), migration_example_14() (+32 more)

### Community 315 - "test_command_exploration.py"
Cohesion: 0.14
Nodes (27): _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), _get_current_lcd(), _get_player_service_from_app(), _handle_admin_set_lucidity_command() (+19 more)

### Community 316 - "NATS Sync Ops in Async Handlers"
Cohesion: 0.33
Nodes (6): NATS Anti-Patterns Review 2026-01-13, NATS Sync Ops in Async Handlers, NATS Connection Pooling, NATS Code Review, NATS Manual Acknowledgment, NATS Remediation Complete

### Community 317 - "npc_config_parsing.py"
Cohesion: 0.04
Nodes (49): Load all spells from the database into memory.          This should be called du, BaseModel, Material component required for casting a spell., SpellMaterial, Unit tests for spell models.  Tests the Spell, SpellMaterial models and related, Test SpellMaterial can be created with required fields., Test SpellMaterial defaults consumed to True., Test SpellMaterial can have consumed set to False. (+41 more)

### Community 318 - "test_message_filtering.py"
Cohesion: 0.04
Nodes (47): message_filtering_helper(), mock_connection_manager(), Unit tests for message filtering.  Tests the MessageFilteringHelper class., Test should_apply_mute_check() returns True for sensitive channels., Test should_apply_mute_check() returns False for non-sensitive channels., Test compare_canonical_rooms() returns True for same rooms., Test compare_canonical_rooms() returns False for different rooms., Test get_player_room_from_online_players() returns player room. (+39 more)

### Community 319 - ".apply_costs"
Cohesion: 0.10
Nodes (23): get_asyncpg_server_settings_for_database_url(), Build asyncpg ``server_settings`` so unqualified table names resolve like SQLAlc, _holiday_entry_from_row(), _HolidayLoadResult, Record, TypedDict, Async helper to load holidays from PostgreSQL database., Normalize nullable PostgreSQL array columns to string values. (+15 more)

### Community 321 - "test_aggro_threat.py"
Cohesion: 0.05
Nodes (57): CombatCommandHandlerExtras, Combat command handler class and shared helpers.  Extracted from combat.py to, Optional services from the app container (keeps ``CombatCommandHandler.__init__`, _app_from_request(), get_combat_command_handler(), handle_attack_command(), handle_flee_command(), handle_kick_command() (+49 more)

### Community 322 - "get_asyncpg_server_settings_for_database_url"
Cohesion: 0.13
Nodes (21): _async_load_lucidity_rate_overrides(), build_override_key(), extract_lucidity_rate(), _LucidityRateLoadResult, _normalize_database_url(), _parse_special_rules_from_raw(), _parse_zone_stable_id(), _process_override_row() (+13 more)

### Community 323 - "MovementService"
Cohesion: 0.03
Nodes (69): MovementService, Any, Exception, Room, UUID, Resolve player by ID or name and return player object and resolved ID., Get and validate rooms for movement., Execute the atomic room transfer. (+61 more)

### Community 324 - "TestNPCCombatRewards"
Cohesion: 0.06
Nodes (18): Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class., Test award_xp_to_killer handles zero XP., Create a mock persistence layer., Create a mock game mechanics service. (+10 more)

### Community 325 - "player_effect_repository.py"
Cohesion: 0.06
Nodes (43): create_websocket_request_context(), Any, Get the event bus from the request context., Get the alias storage from the request context., Factory function to create a WebSocket request context.      Args:         app_s, Creates FastAPI Request-like objects for WebSocket commands.      This allows We, Initialize the WebSocket request context.          Args:             app_state:, Set the alias storage in the app state.          Args:             alias_storage (+35 more)

### Community 326 - "StatusPanel.tsx"
Cohesion: 0.07
Nodes (47): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), Any, Read command handler for reading spellbooks and other readable items.  This modu (+39 more)

### Community 327 - "multiplayer-browser-helpers.js"
Cohesion: 0.15
Nodes (29): buttonHasLoginSubmitLabel(), captureGameUiDiagnosticsInBrowser(), captureOccupantsSnapshotInBrowser(), computedStyleHidesElement(), elementShowsConnectedStatus(), elementTextIncludesGameInfo(), evaluateGameUiLoaded(), fieldHasCommandPlaceholder() (+21 more)

### Community 328 - "HealthService"
Cohesion: 0.08
Nodes (21): HealthStatus, HealthService, Any, Check database connectivity and health with actual query validation.          Th, Check database connectivity and health (sync wrapper).          For async contex, Check connection manager health., Get server component health status., Get database component health status (async version with actual validation). (+13 more)

### Community 329 - "consume_prototype_from_player"
Cohesion: 0.07
Nodes (42): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _dict_stacks_from_callable(), _dict_stacks_from_equipped() (+34 more)

### Community 330 - "WebSocketRequestContext"
Cohesion: 0.07
Nodes (27): guard(), Unit tests for inventory mutation guard - core functionality.  Tests initializat, Test acquire_async without token allows mutation., Test acquire_async with unique token allows mutation., Test acquire_async with duplicate token suppresses mutation., Test acquire_async allows same token for different players., Create an InventoryMutationGuard instance., Test MutationDecision initialization. (+19 more)

### Community 331 - "Container System"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 332 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.06
Nodes (31): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI SUCCESS METRICS, 🔧 COMMON FIX TEMPLATES, Component Rendering Issues, 🔴 CRITICAL (Fix First - Blocking Issues), 🔴 CRITICAL FIXES - TypeScript Errors, For Each Failure Category (+23 more)

### Community 333 - "emotes.schema.json"
Cohesion: 0.06
Nodes (31): additionalProperties, additionalProperties, properties, required, type, items, type, uniqueItems (+23 more)

### Community 334 - "map_minimap.py"
Cohesion: 0.08
Nodes (40): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+32 more)

### Community 335 - "SSE Authentication System"
Cohesion: 0.06
Nodes (31): API Endpoints, Architecture, Authentication Errors, Authentication Flow, Authentication Mechanisms, Best Practices, Common Issues, Components (+23 more)

### Community 336 - "test_metrics_endpoints.py"
Cohesion: 0.06
Nodes (27): clean_command_input(), normalize_command(), Clean and normalize command input by collapsing multiple spaces and stripping wh, Normalize command input by removing optional slash prefix.      Supports both tr, Check if a single word command should be treated as an emote.      This function, should_treat_as_emote(), Unit tests for command input processing.  Tests command normalization, cleaning,, Test should_treat_as_emote() returns False for system commands. (+19 more)

### Community 337 - "_find_container_in_room"
Cohesion: 0.15
Nodes (14): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeProps, defaultExitEdgeProps (+6 more)

### Community 338 - "Structured Error Logging"
Cohesion: 0.67
Nodes (3): MythosMUDError Hierarchy, Structured Error Logging, log_and_raise Utilities

### Community 339 - "npc_admin.py"
Cohesion: 0.06
Nodes (37): _NpcWithLife, Protocol, Resolve combat target using target resolution service. Public API., Validate target_result and resolve to a live NPC target_match., Resolve combat target using target resolution service., NPC instance shape for alive check before accepting an attack target., BaseModel, Target metadata schema for MythosMUD.  This module defines Pydantic models for t (+29 more)

### Community 340 - "AliasGraph"
Cohesion: 0.05
Nodes (23): Initialize the idle movement handler.          Args:             event_bus: O, NPCMovementIntegration, Room, Get room objects and validate they exist.          Args:             npc_id:, Update room occupancy by removing NPC from source and adding to destination., Update NPC instance room tracking for occupant queries.          Args:, Move an NPC to a different room with full integration.          This method pr, Get the current room ID for an NPC.          Args:             npc_id: ID of (+15 more)

### Community 341 - "hallucinations.py"
Cohesion: 0.07
Nodes (28): FakeHallucinationService, Any, UUID, Generate a room text overlay hallucination.          Args:             player_id, Select which type of fake hallucination to trigger (50/50 chance).          Retu, Service for generating fake NPC tells and room text overlays.      These halluci, Initialize the fake hallucination service., Generate a fake NPC tell hallucination.          Args:             player_id: Pl (+20 more)

### Community 342 - "test_optimized_security_validator.py"
Cohesion: 0.09
Nodes (31): Unit tests for optimized security validation utilities.  Tests the optimized sec, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test validating message with path traversal pattern., Test validating message with javascript: URL., Test validating message with event handler. (+23 more)

### Community 343 - "SafeHtml.tsx"
Cohesion: 0.08
Nodes (27): SafeHtml(), SafeHtmlProps, chatMessageVisibleInGameInfo(), GAME_INFO_CHAT_CHANNELS, GameInfoPanel(), GameInfoPanelProps, createDomPurifyTestWindow(), installDomPurifyTestWindow() (+19 more)

### Community 344 - "generate_sql.mjs"
Cohesion: 0.29
Nodes (7): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 345 - "test_command_service.py"
Cohesion: 0.25
Nodes (7): mock_user(), Unit tests for command service.  Tests the CommandService class which handles co, Create a mock user object., Test _log_model_dump_result logs model dump., Test process_validated_command handles handler errors., test_log_model_dump_result(), test_process_validated_command_handler_error()

### Community 346 - "Bug Investigator Subagent"
Cohesion: 0.07
Nodes (29): Authentication/Login Issues, Best Practices, Bug Investigator Subagent, Capabilities, Chat/Communication Issues, Critical Requirements, Evidence Collection, Evidence Standards (+21 more)

### Community 350 - "admin_shutdown_command.py"
Cohesion: 0.07
Nodes (42): get_npc_current_target(), Return current target participant_id for this NPC, or None., _apply_physical_strength_bonus(), _attacker_stats_dict_from_full_player(), _execute_npc_attack(), _execute_player_attack(), _get_combat_container_services(), _get_target_stats_for_damage() (+34 more)

### Community 351 - "PlayerEffect"
Cohesion: 0.10
Nodes (23): _make_effect(), Unit tests for PlayerEffectRepository (ADR-009 effects system).  Tests add_effec, get_active_effects_for_player returns only effects with remaining_ticks > 0 (pro, has_effect returns True when player has active effect of type., has_effect returns False when no active effect of type., get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick)., get_effect_remaining_ticks returns None when no matching effect., expire_effects_for_tick returns (player_id, effect_type) and deletes rows via pr (+15 more)

### Community 352 - "e2e-bootstrap.ts"
Cohesion: 0.17
Nodes (25): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT, failBootstrap() (+17 more)

### Community 353 - "Test Suite Optimization Status"
Cohesion: 0.07
Nodes (28): ✅ 1.1 Placeholder Tests Removed, ⏳ 1.2 Trivial Type Assertions (Pending), ⏳ 1.3 Duplicate Tests (Pending), Baseline (Before Optimization), ✅ CI/CD Workflow Updated, Configuration Updates, Coverage Verification, Current Status (+20 more)

### Community 354 - "authenticated.ts"
Cohesion: 0.18
Nodes (16): testAPIEndpoint(), adminTest, AuthenticatedPage, authenticatedTest, openAuthenticatedPage(), setupAuthStorage(), executeCommand(), sendCommandToPage() (+8 more)

### Community 355 - "Performance Optimization Summary"
Cohesion: 0.07
Nodes (27): 1. Advanced Caching Strategies, 1. Validation Performance Optimization, 2. Memory Optimization, 2. Memory Usage Optimization, 3. Model Instantiation Performance, 3. Validation Optimization, 4. Lazy Loading Implementation, 4. Performance Monitoring (+19 more)

### Community 356 - "MovementMonitor"
Cohesion: 0.08
Nodes (21): MovementMonitor, Any, UUID, Record concurrent movement count., Record an integrity check result., Validate room data integrity.          Returns a dictionary with validation resu, Get comprehensive movement metrics., Comprehensive monitoring system for the movement system.      This class provide (+13 more)

### Community 357 - "FollowService"
Cohesion: 0.13
Nodes (25): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in consumpti, sync_collect_progress reflects increased and decreased holdings., Nested inner_container items count toward collect_n progress. (+17 more)

### Community 358 - "test_spawn_validator.py"
Cohesion: 0.06
Nodes (37): extract_observance_ids(), load_schedule_directory(), BaseModel, Path, Calendar ingestion schemas for MythosMUD.  These models provide a typed wrapper, Load holiday collection from JSON file., Wrapper around an array of schedule entries., Load schedule collection from a JSON file.          Args:             path: Path (+29 more)

### Community 359 - "test_connection_state_machine.py"
Cohesion: 0.07
Nodes (38): AlertResolveResponse, AlertsResponse, CacheMetricsResponse, ConnectionHealthStatsResponse, DualConnectionStatsResponse, EventBusMetricsResponse, IntegrityResponse, MemoryAlertsResponse (+30 more)

### Community 360 - "test_room_occupant_manager.py"
Cohesion: 0.08
Nodes (25): mock_connection_manager(), occupant_manager(), Unit tests for room occupant manager.  Tests the RoomOccupantManager class for q, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test separate_occupants_by_type with empty list., Create mock connection manager., Create RoomOccupantManager instance. (+17 more)

### Community 361 - "test_chat_logger.py"
Cohesion: 0.07
Nodes (27): Unit tests for chat logger service.  Tests the ChatLogger class for structured c, Test log_player_muted writes entry., Test log_player_unmuted writes entry., Test log_player_joined_room writes entry., Test log_rate_limit_violation writes entry., Create a temporary directory for chat logs., Test get_log_file_paths returns correct paths., Test get_log_stats returns statistics. (+19 more)

### Community 362 - "debugLogger"
Cohesion: 0.07
Nodes (37): get_current_superuser(), get_current_verified_user(), get_optional_current_user(), Get current superuser or raise 403., Get current verified user or raise 403., Validate invite code for registration., Get current user if authenticated, otherwise None., require_invite_code() (+29 more)

### Community 363 - "Environment Configuration Refactoring"
Cohesion: 0.07
Nodes (26): Benefits, Configuration Files by Environment, Configuration Loading Order, Documentation, E2E Testing (Playwright), Environment Configuration Refactoring, Files Created in This Refactoring, For CI/CD (+18 more)

### Community 364 - "Three-Column Game UI Layout"
Cohesion: 0.09
Nodes (25): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe, Scenario 42 Quest Log Visible After Login (+17 more)

### Community 365 - "UserManagerProtocol"
Cohesion: 0.07
Nodes (12): Protocol, Protocol for user manager., Mute a channel for a player., Unmute a channel for a player., Check if channel is muted., Mute a player for another player., Unmute a player for another player., Check if player is muted. (+4 more)

### Community 366 - ".__init__"
Cohesion: 0.08
Nodes (37): handle_wearable_container_on_unequip(), normalize_equipped_items(), Handle wearable container preservation when unequipping a container item., Normalize slot names and slot_type in equipped items., build_and_broadcast_inventory_event(), clone_inventory(), persist_player(), Player (+29 more)

### Community 367 - "TargetResolutionService"
Cohesion: 0.03
Nodes (113): _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), Any, Follow commands for MythosMUD.  Handlers for /follow, /unfollow, and /following., Handle /following - show who you follow and who follows you., Get application container from request. (+105 more)

### Community 368 - "send_game_event"
Cohesion: 0.14
Nodes (18): DraggablePanel(), DraggablePanelProps, DraggablePanelResizeHandles(), DraggablePanelResizeHandlesProps, HANDLE_CONFIGS, HandleConfig, isMouseEventOnHeader(), isPanelDragBlockedTarget() (+10 more)

### Community 369 - "NPCOccupantProcessor"
Cohesion: 0.07
Nodes (34): AliasCommand, Command for creating or viewing command aliases., Validate alias name format using centralized validation., Validate command content for security using centralized validation., Command for removing an alias., Validate alias name format using centralized validation., UnaliasCommand, Unit tests for alias command models.  Tests the alias command models and their v (+26 more)

### Community 371 - "test_postgres_adapter.py"
Cohesion: 0.14
Nodes (12): connect_postgres(), convert_sqlite_to_postgres_query(), Create a PostgreSQL connection.      Args:         database_url: PostgreSQL conn, Convert legacy SQLite query syntax to PostgreSQL syntax.      Note: This functio, Unit tests for PostgreSQL adapter.  Tests PostgresRow, PostgresConnection, Postg, Test utility functions., Test connect_postgres()., Test connect_postgres() with driver prefix. (+4 more)

### Community 372 - "AsciiMapViewer.tsx"
Cohesion: 0.09
Nodes (29): HealthMeter, TIER_METADATA, TierMetadata, handlePlayerDeliriumRespawned(), handlePlayerDied(), handlePlayerDpUpdated(), handlePlayerEntered(), handlePlayerEnteredGame() (+21 more)

### Community 373 - "AuditLogger"
Cohesion: 0.08
Nodes (26): Unit tests for audit_logger utilities.  Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries., test_audit_logger_get_recent_entries(), test_audit_logger_init() (+18 more)

### Community 374 - "rooms.py"
Cohesion: 0.08
Nodes (33): get_room(), _invalidate_room_cache(), BaseModel, Request, Room management API endpoints for MythosMUD server.  This module handles all roo, Update room position in database and verify the update succeeded., Invalidate room cache to force reload., # IMPORTANT: /list route must come BEFORE /{room_id} route (+25 more)

### Community 375 - "config.ts"
Cohesion: 0.06
Nodes (35): hash_password(), Authentication utilities for JWT token generation and validation.  JWT encode/, Hash a plaintext password using Argon2id.      This function provides superior, Verify a plaintext password against a hash.      This function safely handles, verify_password(), Test hash_password raises AuthenticationError on AuthenticationError from argon2, Test hash_password raises AuthenticationError on ValueError., Test hash_password raises AuthenticationError on TypeError. (+27 more)

### Community 376 - "GameInfoPanel.tsx"
Cohesion: 0.19
Nodes (18): UseMapLayoutOptions, applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyGridLayout(), applyLinkForces() (+10 more)

### Community 377 - "Migration Strategy"
Cohesion: 0.08
Nodes (25): Access Patterns, App.State to Dependency Injection Migration Plan, Current State Analysis, Dependencies, Dependency Injection Pattern, Estimated Effort, Implementation Guidelines, Migration Strategy (+17 more)

### Community 378 - "transfer_all_items_from_container"
Cohesion: 0.08
Nodes (23): guard(), Unit tests for inventory mutation guard - internal helper methods.  Tests intern, Test _cleanup_async_state removes empty state., Test _prune_tokens_async removes expired tokens., Test _prune_tokens_async with token_ttl=0 doesn't prune., Test _enforce_limit_async removes oldest tokens when limit exceeded., Create an InventoryMutationGuard instance., Test _prune_tokens removes expired tokens. (+15 more)

### Community 379 - "test_game_tick_processing.py"
Cohesion: 0.16
Nodes (10): Any, WebSocket, Handle a WebSocket message using the appropriate handler.          Args:, Handle a specific message type.          Args:             websocket: The WebSoc, Handle command message type., Handle chat message type., Handle ping message type., Handle follow_response message type. (+2 more)

### Community 380 - "UUID"
Cohesion: 0.16
Nodes (16): GameTerminalContext, GameTerminalContextType, GameTerminalProvider(), GameTerminalProviderProps, useConnectionState(), useGameActions(), useGameState(), useGameTerminalContext() (+8 more)

### Community 381 - "Phase 3, Task 3.2: NATS Subject Manager Usage Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 382 - "chat_nats_publisher.py"
Cohesion: 0.29
Nodes (7): contains_malicious_content(), Chat message validation utilities.  This module provides validation functions fo, Validate chat message before transmission.      Args:         chat_message: The, Validate sender has access to the room.      Args:         sender_id: ID of the, Check for malicious content patterns.      Args:         content: The message co, validate_chat_message(), validate_room_access()

### Community 383 - "_find_item_in_room_drops"
Cohesion: 0.11
Nodes (16): Command, command_parser(), command_parser(), Create a CommandParser instance., Create a CommandParser instance., Test _create_command_object handles Pydantic validation errors., test_create_command_object_pydantic_validation_error(), CommandParser (+8 more)

### Community 384 - "format_message_content"
Cohesion: 0.09
Nodes (22): format_message_content(), Format message content based on channel type and sender name.      Args:, Test format_message_content() formats 'say' channel messages., Test format_message_content() formats 'local' channel messages., Test format_message_content() formats 'global' channel messages., Test format_message_content() formats 'emote' channel messages., Test format_message_content() formats 'pose' channel messages., Test format_message_content() formats 'whisper' channel messages (default). (+14 more)

### Community 385 - "test_lru_cache.py"
Cohesion: 0.06
Nodes (35): connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue(), mock_rate_limiter(), mock_room_manager() (+27 more)

### Community 386 - "PeriodicOrphanAuditor"
Cohesion: 0.06
Nodes (19): Test _try_player_username rejects UUID-formatted string as username., Test suite for PlayerNameExtractor class., Test _try_player_username when username is None., Test _try_user_object_name without user attribute., Test _try_user_object_name when user is None., Test _try_fallback_name_sources with user object fallback., Test _check_uuid_pattern_match with invalid pattern., Test _check_uuid_string_matches with exact match. (+11 more)

### Community 388 - "test_player_event_handlers_room_left.py"
Cohesion: 0.13
Nodes (17): create_item_instance_async(), ensure_item_instance_async(), item_instance_exists_async(), Any, AsyncSession, Async item instance persistence operations.  Provides async implementations usin, Check if an item instance exists in the database via item_instance_exists proced, Ensure an item instance exists in the database, creating it if necessary.      A (+9 more)

### Community 389 - "performance.test.tsx"
Cohesion: 0.07
Nodes (25): ChatPanel(), Channel, ChannelSelectorProps, TerminalButtonProps, TerminalInputProps, Channel, ChannelSelectorProps, TerminalButtonProps (+17 more)

### Community 390 - "devDependencies"
Cohesion: 0.03
Nodes (65): autoprefixer, devDependencies, autoprefixer, cross-env, esbuild, eslint, @eslint/js, eslint-plugin-jsx-a11y (+57 more)

### Community 391 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 392 - "Test Suite Analyzer Subagent"
Cohesion: 0.08
Nodes (24): Best Practices, Capabilities, Coverage Analysis, Coverage Gap Analysis, Coverage Requirements, Critical Files Requiring High Coverage, Critical Path Coverage, Example Scenarios (+16 more)

### Community 393 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 394 - "retry.py"
Cohesion: 0.08
Nodes (35): F, Unit tests for retry utilities.  Tests the retry decorator and retry logic., Test is_transient_error() identifies transient errors., Test is_transient_error() returns False for non-transient errors., Test retry_with_backoff() succeeds on first attempt., Test retry_with_backoff() retries on failure then succeeds., Test retry_with_backoff() with async function succeeds on first attempt., Test retry_with_backoff() with async function retries on failure then succeeds. (+27 more)

### Community 395 - "PlayerRespawnEventHandler"
Cohesion: 0.04
Nodes (67): Parse numeric fields from object-typed JSON command payloads., PlayerRespawnedEvent, Event fired when a player respawns after death.      This event is triggered whe, Delegate player respawned event to specialized handler., _append_unique_valid_occupant(), _ensure_respawned_player_in_lists(), _is_npc_occupant_row(), _occupant_str_field() (+59 more)

### Community 396 - "get_async_session"
Cohesion: 0.10
Nodes (32): handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command., Handle NPC reaction trigger command., Handle NPC behavior stop command. (+24 more)

### Community 397 - "subject_controller.py"
Cohesion: 0.06
Nodes (33): _format_container_contents(), Format container contents as list of lines., Unit tests for look container helper functions.  Tests the helper functions in l, Test _find_container_via_inner_container() when item has no inner_container., Test _find_container_via_inner_container() with invalid UUID., Test _find_container_via_inner_container() when persistence has no get_container, Test _matches_item_instance_id() returns True when IDs match., Test _matches_item_instance_id() returns False when IDs don't match. (+25 more)

### Community 398 - "ValidationRule"
Cohesion: 0.09
Nodes (15): ABC, Base validation rule class.  This module defines the abstract base class for all, Create a validation error for this rule.          Args:             room_id: Roo, Represents a validation error with metadata.      As documented in the restricte, Create a validation warning for this rule.          Args:             room_id: R, Get information about this rule.          Returns:             Dictionary with r, Initialize a validation error.          Args:             rule_name: Name of the, Convert error to dictionary format. (+7 more)

### Community 399 - "emote_schema.json"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 401 - "layout.ts"
Cohesion: 0.08
Nodes (33): _mirror_service_to_app_state(), Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state.      Muta, resolve_and_setup_app_state_services(), _services_from_container(), Unit tests for WebSocket handler app state resolution and connection handling., Test _resolve_and_setup_app_state_services when only user_manager is available. (+25 more)

### Community 403 - "stateNormalization.ts"
Cohesion: 0.16
Nodes (18): createEntityMap(), denormalizeGameData(), Entity, EntityMap, extractEntities(), GameData, getEntitiesByIds(), getEntitiesByType() (+10 more)

### Community 404 - "Performance Profiler Subagent"
Cohesion: 0.08
Nodes (23): Bottleneck Identification, Capabilities, Code Performance Review, Database Performance, Database Performance, Database Query Optimization, Enhanced Logging Integration, Example Scenarios (+15 more)

### Community 405 - "command_handler_unified.py"
Cohesion: 0.03
Nodes (77): player_service(), Simulate player service., check_alias_safety(), Check if an alias is safe to expand.      Builds an alias dependency graph and c, Validate an expanded command for length and content.      Args:         expanded, validate_expanded_command(), _check_all_command_blocks(), _check_casting_state() (+69 more)

### Community 406 - "Domain Model Anemic Anti-Pattern Audit"
Cohesion: 0.08
Nodes (23): 1. Already Addressed (Prior Work), 2.1 Player Death Service – DP Decay, 2.2 Combat Turn Processor – “Can Act” Checks, 2.3 Combat HP Sync – Death Threshold Logic, 2.4 Combat Persistence Handler – Same Patterns, 2.5 Player Respawn Service – Stats Restoration, 2. High Priority – Domain Logic in Services, 3.1 Wearable Container Service – Capacity Checks (+15 more)

### Community 407 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 408 - "Any"
Cohesion: 0.10
Nodes (16): command_processor(), Create a CommandProcessor instance., Test get_command_processor returns global instance., Test process_command_string handles Pydantic validation errors., test_get_command_processor(), test_process_command_string_pydantic_validation_error(), CommandProcessor, Any (+8 more)

### Community 409 - "RoomCacheLoader"
Cohesion: 0.15
Nodes (8): Profession, Get all available professions using SQLAlchemy ORM., Get a profession by ID. Delegates to ProfessionRepository., Any, BaseException, Loads room data from the database and populates a room cache dict.      Used by, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 410 - "_find_item_in_inventory"
Cohesion: 0.09
Nodes (21): instance_manager(), Unit tests for InstanceManager.  Tests instance creation, destruction, room clon, Test get_exit_room_id returns fixed exit room., Test get_room_by_id returns None for non-instance room IDs., Test get_room_by_id returns room when room is in an instance., Create tutorial bedroom template room., Room cache with tutorial template., Create InstanceManager with tutorial template in cache. (+13 more)

### Community 412 - "ShopkeeperNPC"
Cohesion: 0.16
Nodes (14): format_combat_status(), get_combat_target(), Any, Produce a human-readable combat status string.      This helper is retained for, Resolve a combat target by name.      The current implementation is intentionall, Unit tests for combat command helper functions.  Tests helper functions in comba, Test format_combat_status() formats combat status., Test format_combat_status() handles player not in combat. (+6 more)

### Community 413 - "convert_uuids_to_strings"
Cohesion: 0.09
Nodes (21): Unit tests for room subscription manager NPC helpers.  Tests NPC-related helpers, Test get_room_occupants() includes NPCs from lifecycle manager., Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager f, Create a RoomSubscriptionManager instance., Test _get_npc_name_from_lifecycle_manager gets NPC name., Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found., Test _get_npc_name_from_lifecycle_manager handles errors gracefully., Test _add_npc_to_occupants adds NPC to list. (+13 more)

### Community 414 - "realtime.py"
Cohesion: 0.10
Nodes (31): Shared schemas: base models, target resolution, inventory validation., _build_validator(), InventorySchemaValidationError, Any, Exception, Inventory JSON schema validation utilities.  As recorded in the restricted stack, Internal helper to construct a Draft7 validator instance., Validate a complete inventory payload against the canonical schema.      Raises: (+23 more)

### Community 415 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (33): Initialize the connection manager with modular components., _max_connection_age_seconds(), MemoryMonitor, Any, Memory monitoring and cleanup management for MythosMUD.  This module provides me, Get memory-related alerts based on current usage and connection statistics., Update the last cleanup time to the current time., Force garbage collection to free memory. (+25 more)

### Community 416 - "PlayerNameExtractor"
Cohesion: 0.09
Nodes (19): Any, UUID, Get name from user object (username or display_name).          Args:, Try to get name from related User object.          Args:             player: The, Try to get player name from fallback sources (username, user object).          A, Perform basic validation on player name (not None, is string, not empty)., Check if player name matches UUID pattern.          Args:             player_nam, Check if player name matches any UUID string representation.          Args: (+11 more)

### Community 417 - "test_health_monitor.py"
Cohesion: 0.06
Nodes (32): _find_container_in_room(), Find a container in room containers by name or container_id.      Args:, Test _find_container_in_room() with instance number out of range., Test _find_container_in_room() with instance number zero., Test _find_container_in_room() finds container by name., Test _find_container_in_room() returns None when container not found., Test _find_container_in_room() with instance number., Test _find_container_in_room() with empty list. (+24 more)

### Community 418 - "test_dependency_analysis.py"
Cohesion: 0.09
Nodes (35): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+27 more)

### Community 419 - "test_rate_limiter_utils.py"
Cohesion: 0.14
Nodes (13): Unit tests for rate limiting utilities.  Tests the simple in-memory rate limiter, Test get_rate_limit_info calculates retry_after correctly., Test enforce_rate_limit raises RateLimitError when limit exceeded., Test RateLimiter initializes correctly., Test check_rate_limit allows multiple requests within limit., Test check_rate_limit returns False when limit exceeded., Test get_rate_limit_info returns correct info for no requests., test_check_rate_limit_exceeds_limit() (+5 more)

### Community 420 - "test_npc_event_handlers_helpers.py"
Cohesion: 0.10
Nodes (11): Test _despawn_npc handles NPC not in active_npcs., Test suite for NPCCombatLifecycle class., Create a mock persistence layer., Create a NPCCombatLifecycle instance for testing., Test NPCCombatLifecycle initialization., Test despawn_npc_safely successfully despawns NPC., Test despawn_npc_safely handles missing lifecycle manager., Test despawn_npc_safely handles exceptions gracefully. (+3 more)

### Community 421 - "ChatPanelRefactoredView.tsx"
Cohesion: 0.07
Nodes (30): Convenience helper for composing uniqueness checks in higher layers., Unit tests for item models.  Tests the ItemPrototype, ItemInstance, and ItemComp, Test unique_key returns different tuples for different inputs., Test primary_slot returns first wear slot when slots exist., Test unique_key returns different tuples for same instance, different component., Test unique_key returns different tuples for different instance, same component., Test unique_key handles empty strings., Test unique_key is a static method (can be called without instance). (+22 more)

### Community 423 - "GameTerminalContext.test.tsx"
Cohesion: 0.22
Nodes (8): PayloadOptimizer, Any, Create an incremental update payload containing only changed fields.          Ar, Optimizes payloads for WebSocket transmission.      Features:     - Size limit e, Initialize the payload optimizer.          Args:             max_payload_size: M, Calculate the size of a payload in bytes.          Args:             payload: Th, Compress a large payload using gzip compression.          Args:             payl, Optimize a payload by applying size limits and compression if needed.          A

### Community 424 - "Security Auditor Subagent"
Cohesion: 0.09
Nodes (22): Authentication & Authorization, Authentication Security Review, Capabilities, COPPA Compliance, COPPA Compliance (Critical), COPPA Compliance Verification, Example Scenarios, Input Validation (+14 more)

### Community 425 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 426 - "CI/CD Enhanced Logging Validation"
Cohesion: 0.09
Nodes (22): CI/CD Enhanced Logging Validation, Common Issues, COPPA Compliance Checker, COPPA Compliance Issues, Debugging Commands, Docker Configuration, Documentation References, Enhanced Logging in Production (+14 more)

### Community 427 - "test_look_container.py"
Cohesion: 0.04
Nodes (49): _get_container_description(), Get container description from prototype registry., mock_prototype_registry(), Unit tests for container look functionality.  Tests the helper functions for loo, Test finding container via inner_container_id., Test finding container via inner_container when not present., Test finding container via inner_container with invalid UUID., Test formatting container contents with items. (+41 more)

### Community 428 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 429 - "bind_request_context"
Cohesion: 0.22
Nodes (17): calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractRoomMetadata(), getFinalNpcs(), getFinalPlayers(), getRoomDataFromEvent() (+9 more)

### Community 430 - "compilerOptions"
Cohesion: 0.09
Nodes (22): compilerOptions, baseUrl, lib, module, moduleResolution, noEmit, noFallthroughCasesInSwitch, noUnusedLocals (+14 more)

### Community 431 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 432 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 433 - "test_combat_persistence_handler.py"
Cohesion: 0.10
Nodes (22): PlayerDeathService, Any, AsyncSession, Player, UUID, Process DP decay for a single mortally wounded player.          Decreases player, Ensure player posture is set to lying when dead.          Args:             play, Clear player combat state when they die.          BUGFIX #244: As documented in (+14 more)

### Community 434 - "playerHandlers.ts"
Cohesion: 0.08
Nodes (24): Resolve a room id to the canonical Room.id value (public method)., Resolve a room id to the canonical Room.id value (compatibility method)., Remove a player from all room subscriptions and occupant lists (compatibility me, canonical_room_id_impl(), prune_player_from_all_rooms_impl(), Any, Resolve a room id to the canonical Room.id value.      Args:         room_id: Th, Remove a player from all room subscriptions and occupant lists. (+16 more)

### Community 435 - "inventory_drop_command.py"
Cohesion: 0.05
Nodes (76): async_load_zone_configurations(), extract_zone_name(), parse_json_field(), parse_zone_special_rules(), process_subzone_rows(), process_zone_rows(), Connection, Record (+68 more)

### Community 436 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 437 - "test_event_bus.py"
Cohesion: 0.03
Nodes (81): event_bus(), MockEventClass, Unit tests for event bus.  Tests the EventBus class., Test EventBus.publish() queues or processes event., Test EventBus.shutdown() stops processing., Test EventBus.set_main_loop() sets main loop., Test EventBus.unsubscribe() with multiple handlers., Test EventBus.get_all_subscriber_counts() with no subscribers. (+73 more)

### Community 438 - "generate_html_visualization.py"
Cohesion: 0.08
Nodes (33): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+25 more)

### Community 439 - "admin_auth_service.py"
Cohesion: 0.17
Nodes (24): SERVER_UNAVAILABLE_PATTERNS, useProfessions(), UseProfessionsOptions, errorMessageFromApiBody(), loginFailureMessage(), formatValidationErrors(), messageFromNestedError(), messageFromValidationDetail() (+16 more)

### Community 440 - "_make_session_context"
Cohesion: 0.09
Nodes (22): Unit tests for alias_graph utilities.  Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+14 more)

### Community 441 - "test_room_subscription_manager_npcs.py"
Cohesion: 0.08
Nodes (24): Infrastructure layer for MythosMUD.  This package contains abstractions for exte, MessageBrokerConnectionError, MessageBrokerError, Exception, Message Broker abstraction for MythosMUD.  This module defines the MessageBroker, Base exception for message broker errors., Exception raised when connection to message broker fails., Exception raised when subscribing to subject fails. (+16 more)

### Community 442 - "Testing Steps"
Cohesion: 0.07
Nodes (29): Migration 019 Complete Summary, Migration 019 Ready for Deployment, Issue: "cannot alter type of column because there is a default", Issue: "column already has identity", Issue: Foreign key constraint violations, Issue: "function convert_serial_to_identity does not exist", Migration 019 Testing Guide, Option 1: Restore from Backup (+21 more)

### Community 443 - "mapPageRenderer.tsx"
Cohesion: 0.17
Nodes (16): RoomMapViewerProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView(), renderMapPageState(), renderStatusGate(), resolveMapViewProps() (+8 more)

### Community 444 - "designTokens.ts"
Cohesion: 0.15
Nodes (19): animations, borderRadius, breakpoints, buildClasses, ButtonVariant, colors, ColorVariant, ComponentSize (+11 more)

### Community 445 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 447 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 448 - "item_instance_persistence_async.py"
Cohesion: 0.05
Nodes (28): Get list of NPC IDs currently in the room.          Returns:             List of, PersistenceProtocol, PlayerServiceProtocol, Player, Protocol, Room, UUID, Validate player exists and is in a room. Returns (room_id, error_result). (+20 more)

### Community 449 - "_find_item_in_equipped"
Cohesion: 0.12
Nodes (17): useConnectionState(), UseConnectionStateResult, ConnectionContext, ConnectionEvent, connectionMachine, ConnectionMachineInput, ConnectionState, mockWebSocket (+9 more)

### Community 450 - "CorpseLifecycleService"
Cohesion: 0.02
Nodes (134): CombatEndedEvent, CombatTimeoutEvent, CombatTurnAdvancedEvent, NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent, Combat-specific events for the MUD.  This module defines combat-related events t (+126 more)

### Community 451 - "ChatPanel"
Cohesion: 0.18
Nodes (7): mock_persistence(), MockPersistence, Mock persistence layer with async methods., Mock async method that uses configured mock., Mock method that uses configured mock., Allow setting get_player_by_name and get_room_by_id to mocks., Create a mock persistence layer.

### Community 452 - "messageHandlers.ts"
Cohesion: 0.22
Nodes (13): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+5 more)

### Community 453 - "useThemeContext.ts"
Cohesion: 0.22
Nodes (17): useAccessibilityPreference(), useAnimationPreference(), useColorSchemePreference(), useCompactModePreference(), useDebugInfoPreference(), useFontSizePreference(), useTheme(), useThemePreference() (+9 more)

### Community 454 - "Stop-MythosMudProjectProcessTree"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 455 - "multiplayer-browser-helpers.bundle.js"
Cohesion: 0.20
Nodes (17): buttonHasLoginSubmitLabel(), computedStyleHidesElement(), elementTextIncludesGameInfo(), fieldHasCommandPlaceholder(), getBodyInnerText(), hasCommandInputInBrowser(), hasGameInfoAnyMessageInBrowser(), hasGameInfoPanelInBrowser() (+9 more)

### Community 456 - "ConnectionErrorHandler"
Cohesion: 0.17
Nodes (13): create_error_context(), Any, Request, Shared helper functions for player API endpoints., Create error context from request and user.      Helper function to reduce dupli, Unit tests for server.api.player_helpers (error context helper)., When current_user is None, context gets metadata only., When current_user is set, user_id is populated and metadata merged. (+5 more)

### Community 457 - "MessageFilteringHelper"
Cohesion: 0.11
Nodes (16): CommandHandler, CommandService, Any, Main command processing service for MythosMUD.      This service handles command, Process a validated command with routing.          Args:             command_dat, Parse and validate command string.          Returns:             tuple of (parse, Prepare command_data dictionary by merging parsed command fields.          Retur, Extract non-private, non-callable attributes from parsed_command, excluding keys (+8 more)

### Community 458 - "Dependency Upgrade Strategy Agent"
Cohesion: 0.22
Nodes (10): Batch Update Strategy, Breaking Change Detection, Dependency Compatibility Matrix, Dependency Update Analysis, Incremental Upgrade Strategy, Dependency Rollback Strategy, Dependency Upgrade Strategy Agent, Dependency Upgrade Report (+2 more)

### Community 459 - "update_aggro"
Cohesion: 0.07
Nodes (28): _find_container_wearable(), Find a wearable container in equipped items by name or prototype_id.      This f, Test _find_container_wearable() with empty dict., Test _find_container_wearable() with no matching containers., Test _find_container_wearable() with multiple matches (ambiguous)., Test _find_container_wearable() with instance number., Test _find_container_wearable() with instance number out of range., Test _find_container_wearable() finds wearable container. (+20 more)

### Community 460 - "._cleanup_player_mutes"
Cohesion: 0.12
Nodes (11): datetime, Get active global mutes applied by a player., Get all mutes applied by a player.          Args:             player_id: Play, Get system-wide user management statistics.          Returns:             Dic, Clean up expired player mutes., Clean up expired channel mutes., Clean up expired global mutes., Clean up expired mutes from all storage. (+3 more)

### Community 461 - "codacy.yaml Tool Manifest"
Cohesion: 0.14
Nodes (14): Codacy CLI Local Mode, codacy.yaml Tool Manifest, Lizard Complexity Tool Pin, Trivy Codacy Tool Pin, MythosMUD Codacy Tool Suite, Grype Local vs Trivy Codacy SCA, Manually Managed codacy.yaml, Dart Analyzer Options (+6 more)

### Community 462 - "shutdown_sequence.py"
Cohesion: 0.10
Nodes (30): _find_uvicorn_processes(), Any, Process termination utilities for graceful server shutdown.  This module handles, Schedule a best-effort graceful process termination after a short delay.      Th, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available. (+22 more)

### Community 463 - "TestVerificationSqlUsersPlayers"
Cohesion: 0.10
Nodes (12): PostgreSQL-focused tests for verification and maintenance SQL scripts.  Validate, Tests for db/verification/users_players.sql alignment with current schema., Verification SQL file must exist., Verification SQL must not reference staging tables or select obsolete columns., Verification SQL must use explicit join syntax for multi-table queries., Verification SQL must reference users and players tables., Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)., NPC name constraint script must exist. (+4 more)

### Community 464 - "test_profession.py"
Cohesion: 0.03
Nodes (72): Profession service for MythosMUD server.  This module handles profession-related, Profession, Any, Base, Check if given stats meet the profession requirements.          Args:, Check if profession is available for player selection., Get formatted text for displaying stat requirements.          Returns:, Profession model for game data.      Stores profession information including nam (+64 more)

### Community 465 - "TestNPCCombatLifecycle"
Cohesion: 0.14
Nodes (7): Signal shutdown to async processing loop., Cancel the main processing task if it exists., Cancel all active tasks and wait for graceful shutdown., Finalize shutdown by clearing tasks and logging., Stop pure async event processing gracefully., Unsubscribe all handlers for a specific service.          Args:             serv, Shutdown the pure asyncio event bus with proper grace period coordination.

### Community 466 - "test_npc_startup_service.py"
Cohesion: 0.04
Nodes (83): NPCStartupService, Any, Spawn all required NPCs.          Args:             required_npcs: List of requi, Spawn optional NPCs based on spawn probability.          Args:             optio, Second pass: spawn one instance per definition (that was spawned in required/opt, Service for automatic NPC spawning during server startup.      This service coor, Determine the appropriate room for spawning an NPC.          Args:             n, Get a default room for a given sub-zone.          Args:             sub_zone_id: (+75 more)

### Community 467 - "_assign_container_get_instance"
Cohesion: 0.07
Nodes (15): PlayerNameExtractor, Utility class for extracting and validating player names.      CRITICAL: NEVER u, Initialize the player name extractor., Tests for player name extraction and validation utilities.  As documented in "Id, Test _get_name_from_user_object with getattr fallback., Test PlayerNameExtractor initialization., Test _get_name_from_user_object when no name available., Test _try_fallback_name_sources with username fallback. (+7 more)

### Community 468 - "TestPathValidator"
Cohesion: 0.04
Nodes (31): PathValidator, Get the opposite direction for bidirectional checking., Validates room connectivity using graph traversal algorithms.      Implements th, Find rooms with no exits (dead ends).          Args:             room_database:, Find rooms that cannot be reached from the start room.          Args:, Find rooms that reference themselves in exits.          Args:             room_d, Generate minimap graph data for visualization.          Args:             room_d, Initialize the path validator.          Args:             schema_validator: Opti (+23 more)

### Community 469 - "package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 470 - "useDraggablePanelInteractions.ts"
Cohesion: 0.09
Nodes (26): _dispatch_parsed_command(), _handle_processing_error(), _handle_validation_error(), _log_security_sensitive_command(), _parse_command_line_or_client_error(), process_command_with_validation(), CommandExecutionRequest, Exception (+18 more)

### Community 471 - "NPCEventHandler"
Cohesion: 0.03
Nodes (77): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), Unit tests for NPC event handlers.  Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON., Test handle_npc_entered_room() processes event., Test handle_npc_left_room() processes event. (+69 more)

### Community 472 - "roomHandlers.ts"
Cohesion: 0.08
Nodes (18): CommandRequest, BaseModel, Request model for command processing., Test process_command_unified processes normal commands., Test handle_command HTTP endpoint., Test handle_command raises HTTPException when not authenticated., Test handle_command successfully processes command., Test legacy compatibility functions. (+10 more)

### Community 473 - "Scenario 20 Logout Errors"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 474 - "Codebase Explorer Subagent"
Cohesion: 0.11
Nodes (18): Architecture Analysis, Architecture Analysis, Best Practices, Capabilities, Codebase Explorer Subagent, Dependency Research, Dependency Research, Example Scenarios (+10 more)

### Community 475 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.12
Nodes (16): 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases, For Performance (+8 more)

### Community 476 - "ADR-012: python-statemachine for Backend Connection FSM"
Cohesion: 0.11
Nodes (18): ADR-012: python-statemachine for Backend Connection FSM, Consequences, Considered Options, Context and Problem Statement, Decision Drivers, Decision Outcome, Implementation Details, Integration with NATS Service (+10 more)

### Community 477 - "enum"
Cohesion: 0.11
Nodes (19): ACCESSORY, AMULET, BELT, CURSED, FEET, GLOW, HANDS, HEAD (+11 more)

### Community 478 - "properties"
Cohesion: 0.11
Nodes (19): minimum, type, type, additionalProperties, type, maxLength, minLength, type (+11 more)

### Community 479 - "MemoryThresholdMonitor"
Cohesion: 0.08
Nodes (26): _format_container_display(), Format the complete container display text., Test _format_container_display() with locked container., Test _format_container_display() with sealed container., Test _format_container_display() with look_in flag., Test _format_container_display() with target_type container., test_format_container_display_locked(), test_format_container_display_sealed() (+18 more)

### Community 480 - "is_shutdown_pending"
Cohesion: 0.03
Nodes (123): _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), calculate_notification_times(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state(), countdown_loop() (+115 more)

### Community 481 - "inventory_put_command.py"
Cohesion: 0.08
Nodes (26): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id.      Args:         room_drop, Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() returns None when item not found., Test _find_item_in_room_drops() with instance number., Test _find_item_in_room_drops() with multiple matches (ambiguous)., Test _find_item_in_room_drops() with instance number., test_find_item_in_room_drops_found() (+18 more)

### Community 482 - "compilerOptions"
Cohesion: 0.04
Nodes (48): compilerOptions, allowImportingTsExtensions, baseUrl, isolatedModules, jsx, lib, module, moduleResolution (+40 more)

### Community 483 - "get_help_content"
Cohesion: 0.12
Nodes (9): Any, UUID, Get player name for messaging.          Args:             player_id: ID of th, Get the current room ID for a player.          Args:             player_id: I, Get player combat participant data from persistence.          Args:, Get NPC combat participant data from NPC instance.          Args:, Initialize the data provider.          Args:             async_persistence: A, Get NPC instance from the spawning service.          Args:             npc_id (+1 more)

### Community 485 - "MessageBrokerError"
Cohesion: 0.12
Nodes (15): Unit tests for AggressiveMobNPC.  Regression test: aggressive mobs must have pla, _enrich_behavior_context sets False when current_room is None., _get_attack_damage coerces behavior_config attack_damage robustly., Non-digit attack_damage string in behavior_config falls back to 1., hunt_target appends each id once; repeated calls keep a single _targets entry., Warnings path: failure in _compute_player_context must not raise., _enrich_behavior_context sets player_in_range and enemy_nearby True when players, _enrich_behavior_context sets player_in_range and enemy_nearby False when room e (+7 more)

### Community 486 - "MemoryMonitor"
Cohesion: 0.12
Nodes (15): guard(), Unit tests for inventory mutation guard - error handling and monitoring.  Tests, Test acquire_async handles record_custom_alert with message parameter., Test acquire handles TypeError from record_custom_alert and uses fallback., Test acquire_async handles TypeError from record_custom_alert and uses fallback., Create an InventoryMutationGuard instance., Test _cleanup_async_state handles AttributeError from lock.locked()., Test _cleanup_async_state handles RuntimeError from lock.locked(). (+7 more)

### Community 487 - "Main Foyer Starting Room"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 488 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, type, minLength, type, minLength, type, properties (+10 more)

### Community 489 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 490 - "PostgresConnection"
Cohesion: 0.07
Nodes (20): PostgresConnection, connection, Commit the current transaction., Rollback the current transaction., Close the connection., PostgreSQL connection wrapper for persistence layer operations., Create a mock psycopg2 connection., Create a mock psycopg2 cursor. (+12 more)

### Community 491 - "EmoteService"
Cohesion: 0.30
Nodes (11): _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, UUID, Rest countdown task implementation.  This module contains the async task that ha, Check if rest countdown was interrupted.      Args:         player_id: Player UU, Send countdown message to player.      Args:         player_id: Player UUID (+3 more)

### Community 492 - "PartyService"
Cohesion: 0.08
Nodes (25): Unit tests for player room event handlers (player left / unsubscribe / broadcast, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player., Test unsubscribe_player_from_room() handles string player_id. (+17 more)

### Community 493 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.14
Nodes (17): PartyChannelStrategy, Strategy for party channel broadcasting. Delivers only to current party members., Unit tests for channel broadcasting strategies.  Tests the channel_broadcasting_, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() handles missing target_player_id., Test SystemAdminChannelStrategy.broadcast() broadcasts globally. (+9 more)

### Community 494 - "Prometheus Configuration"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 495 - "CombatMetrics"
Cohesion: 0.12
Nodes (15): get_combat_config(), Get the global combat configuration service instance.      Returns:         Comb, CombatMetrics, get_combat_metrics(), Initialize the combat monitoring service., Get current combat metrics.          Returns:             CombatMetrics: Current, Combat system metrics., Save current metrics as a snapshot. (+7 more)

### Community 496 - "HealthRepository"
Cohesion: 0.12
Nodes (16): HealthRepository, Exception, Player, UUID, Log critical damage persistence failure., Execute atomic health update via update_player_health procedure., Damage a player and persist health changes atomically.          Args:, Heal a player and persist health changes atomically. (+8 more)

### Community 497 - "NPCStartupService"
Cohesion: 0.08
Nodes (25): Unit tests for player schemas.  Tests the Pydantic models in player.py module., Test CharacterInfo can be instantiated., Test CharacterInfo has correct default values., Test PlayerUpdate can be instantiated with optional fields., Test PlayerUpdate can be instantiated with all fields optional., Test PlayerBase rejects extra fields (extra='forbid')., Test PlayerCreate rejects extra fields (extra='forbid')., Test PlayerBase can be instantiated. (+17 more)

### Community 498 - "load_world_seed.py"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 499 - "canonical_room_id_impl"
Cohesion: 0.14
Nodes (24): create_player(), get_class_description(), Get a description for a character class., Validate and convert character ID string to UUID.      Args:         character_i, Validate character exists, belongs to user, and is not deleted.      Delegates t, Create a new player character.      :param name: Display name for the new charac, _validate_character_access(), _validate_character_id() (+16 more)

### Community 500 - "ReactNodeUpgradeAnalyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 501 - "test_level_service.py"
Cohesion: 0.04
Nodes (60): LevelUpHook, level_from_total_xp(), Level and XP curve for MythosMUD.  Placeholder implementation: XP required for n, Total XP required to reach a given level (cumulative).      Level 1 requires 0 X, XP required to go from (level - 1) to level.      Args:         level: Target le, Compute character level from total experience points.      Uses the same curve a, total_xp_for_level(), xp_required_for_level() (+52 more)

### Community 502 - "test_npc_utils.py"
Cohesion: 0.03
Nodes (73): extract_definition_id_from_npc(), extract_npc_metadata(), extract_room_id_from_npc(), get_zone_key_from_room_id(), Any, NPC Utility Functions.  This module provides utility functions for extracting me, Extract room ID from NPC instance with fallback logic.      Args:         npc_in, Extract NPC type and required status from NPC instance.      Args:         npc_i (+65 more)

### Community 503 - "test_occupant_formatter.py"
Cohesion: 0.11
Nodes (17): Unit tests for occupant formatter.  Tests the occupant_formatter module classes, Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes player dict, Test OccupantFormatter._process_string_occupant_for_update() adds valid string., Test OccupantFormatter.separate_occupants_by_type() separates dict NPCs., Test OccupantFormatter.separate_occupants_by_type() processes string occupants., Test OccupantFormatter.separate_occupants_by_type() handles mixed types., Test OccupantFormatter.separate_occupants_by_type() handles empty list. (+9 more)

### Community 505 - "MonitoringPanel.test.tsx"
Cohesion: 0.20
Nodes (14): MonitoringData, MonitoringPanel(), MonitoringPanelProps, fetchSpy, EMPTY_MONITORING_MOCKS, FetchSpy, mockOkJsonResponse(), MonitoringMocks (+6 more)

### Community 506 - "Multiplayer Architecture Planning"
Cohesion: 0.50
Nodes (4): Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 507 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.11
Nodes (19): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases (+11 more)

### Community 508 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 509 - "conftest.py"
Cohesion: 0.09
Nodes (27): jsxA11yRecommendedWarnRules, jsxA11yRulesOff, Config, Item, _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables() (+19 more)

### Community 510 - "_JSONDict"
Cohesion: 0.24
Nodes (7): Room and subscription utility helpers for connection manager.  This module provi, Ensure room_occupants only contains currently online players., reconcile_room_presence_impl(), Unit tests for connection room utils.  Tests the connection_room_utils module fu, Test canonical_room_id_impl() handles DatabaseError., test_canonical_room_id_impl_database_error(), test_reconcile_room_presence_impl()

### Community 511 - "AliasStorage"
Cohesion: 0.01
Nodes (483): AliasStorage, Alias storage utilities for MythosMUD.  As noted in the restricted archives of M, List all alias files in the storage directory., Manages player alias storage in JSON files.      Each player's aliases are store, Base API router and common dependencies for MythosMUD server.  This module provi, Alias Expansion Logic for MythosMUD.  This module handles alias resolution, expa, HTTP Request or WebSocketRequestContext for unified command processing., Command Processing Logic for MythosMUD.  This module contains the core command (+475 more)

### Community 512 - "ADR-005 Repository Pattern"
Cohesion: 0.12
Nodes (18): FastAPI-Generated OpenAPI 3.1, API OpenAPI Specification, ADR-001 Layered Architecture Event-Driven, ADR-002 ApplicationContainer DI, ADR-003 Dual Event Systems EventBus NATS, In-Process EventBus, NATS Distributed Messaging, ADR-004 WebSocket-Only Realtime (+10 more)

### Community 513 - "create_hasher_with_params"
Cohesion: 0.12
Nodes (24): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _get_item_description_from_prototype(), _handle_item_look(), Any, Item look functionality for MythosMUD.  This module handles looking at items, in, Find an item in equipped items by name or prototype_id.      Args:         equip (+16 more)

### Community 514 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 516 - "RoomCacheService"
Cohesion: 0.14
Nodes (13): guard(), Unit tests for inventory mutation guard - asynchronous acquire operations.  Test, Test acquire_async serializes concurrent mutations for same player., Create an InventoryMutationGuard instance., Test acquire_async enforces max_tokens limit., Test acquire_async allows token reuse after expiry., Test acquire_async with token_ttl=0 (no expiry)., Test acquire_async cleans up state when tokens are empty. (+5 more)

### Community 517 - "Profession"
Cohesion: 0.17
Nodes (11): Unit tests for inventory mutation guard - synchronous acquire operations.  Tests, Test acquire serializes mutations per player., Test acquire allows token reuse after expiry., Test acquire with token_ttl=0 (no expiry)., Test acquire enforces max_tokens limit., Test acquire cleans up state when tokens are empty., test_acquire_cleanup_empty_state(), test_acquire_enforces_max_tokens() (+3 more)

### Community 518 - "channel_broadcasting_strategies.py"
Cohesion: 0.16
Nodes (14): ChannelBroadcastingStrategy, GlobalChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler.  This module implement, Strategy for whisper channel broadcasting., Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy.          Args:             channel_typ, Abstract base class for channel broadcasting strategies. (+6 more)

### Community 521 - "__init__.py"
Cohesion: 0.10
Nodes (13): Path, Queue a log entry for writing by the background thread.          Args:, Get the local channel log file path for a specific sub-zone.          Args:, Log a local channel message to sub-zone specific file.          Args:, Log a global channel message to global.log file.          Args:             mess, Get the global channel log file path.          Returns:             Path to the, Log a system channel message to system.log file.          Args:             mess, Log a whisper channel message to whisper.log file.          Args:             me (+5 more)

### Community 522 - "._get_room_uuid_by_stable_id"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id.      Args:         inv, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 523 - "Disconnect Grace Period and Rest Command"
Cohesion: 0.29
Nodes (7): Disconnect Grace Period and Rest Command, Rest Command, 30-Second Disconnect Grace Period, ADR-009 Effects System Architecture, LOGIN_WARDED Effect, Effects System ADR and Implementation, Effects System Implementation

### Community 524 - "RoomEditModal.tsx"
Cohesion: 0.16
Nodes (9): buildInitialFormData(), EditableRoomField, ENVIRONMENT_OPTIONS, EnvironmentOption, FIELD_VALIDATORS, RoomEditFormData, RoomEditModal(), RoomEditModalProps (+1 more)

### Community 525 - "RateLimiter"
Cohesion: 0.09
Nodes (19): Any, RateLimiter, Remove timestamps older than the window size.          Args:             player_, Check if a player is within rate limits for a channel.          Args:, Record a message for rate limiting.          Args:             player_id: Player, Sliding window rate limiter for chat channels.      Implements per-user, per-cha, Get rate limiting statistics for a player.          Args:             player_id:, Reset rate limiting for a player.          Args:             player_id: Player I (+11 more)

### Community 526 - "usePanelContext.ts"
Cohesion: 0.26
Nodes (12): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+4 more)

### Community 527 - "Phase 1: Core Separation"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 1: Core Separation, Sub-tasks, Sub-tasks (+8 more)

### Community 528 - "Phase 2: Enhanced Features"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 2: Enhanced Features, Sub-tasks, Sub-tasks (+8 more)

### Community 529 - "📅 Implementation Plan"
Cohesion: 0.12
Nodes (16): Deliverables, Deliverables, Deliverables, Deliverables, Deliverables, 📅 Implementation Plan, Phase 1: Foundation & Security (Days 1-3) ✅ **COMPLETED**, Phase 3: Business Logic & Performance (Days 8-11) ✅ **COMPLETED** (+8 more)

### Community 530 - "type"
Cohesion: 0.15
Nodes (14): items, items, type, uniqueItems, minLength, type, flags, tags (+6 more)

### Community 531 - "generate_sql.mjs"
Cohesion: 0.30
Nodes (15): ajv, __dirname, ensureDir(), __filename, generateEmotes(), generateHolidays(), generateNpcSchedules(), generateRooms() (+7 more)

### Community 532 - "_format_room_posture_message"
Cohesion: 0.14
Nodes (22): _build_npc_edit_params(), _execute_npc_edit(), handle_npc_create_command(), handle_npc_delete_command(), handle_npc_edit_command(), handle_npc_list_command(), _parse_npc_edit_args(), Any (+14 more)

### Community 533 - "ChatPoseManager"
Cohesion: 0.08
Nodes (16): ChatPoseManager, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory.          Args:             player_id: ID of the p, Get a player's current pose.          Args:             player_id: ID of the pla, Clear a player's pose.          Args:             player_id: ID of the player, Get all poses (for testing/debugging).          Returns:             Dictionary (+8 more)

### Community 535 - "ChatWhisperTracker"
Cohesion: 0.08
Nodes (23): Unit tests for look item helper functions.  Tests the helper functions in look_i, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items., Test _find_item_in_equipped() with multiple matches (ambiguous)., Test _find_item_in_equipped() with instance number., Test _find_item_in_equipped() with instance number out of range. (+15 more)

### Community 536 - "._handle_npc_follower_move"
Cohesion: 0.08
Nodes (35): Get NPC instance from the spawning service. Public API., Get NPC instance from the spawning service., NPC Admin Commands for MythosMUD.  This module provides administrative slash com, _execute_spawn_loop(), handle_npc_despawn_command(), handle_npc_move_command(), handle_npc_spawn_command(), handle_npc_stats_command() (+27 more)

### Community 537 - "pytest_asyncio_loop_factories"
Cohesion: 0.08
Nodes (23): mock_event_bus(), mock_persistence(), Unit tests for idle movement.  Tests the IdleMovementHandler class., Movement runs when random.random() <= idle_movement_probability (exclusive upper, Test _is_npc_in_combat() when NPC is in combat., Test _is_npc_in_combat() handles missing in_combat attribute., Create a mock persistence layer., Subzone boundary validation drops exits that would leave the NPC subzone. (+15 more)

### Community 538 - "ConnectionMetadata"
Cohesion: 0.17
Nodes (14): ConnectionMetadata, Data models for connection management.  This module defines data structures used, Metadata for tracking connection details in the WebSocket-only system.      This, Unit tests for connection models.  Tests the connection_models module classes., Test ConnectionMetadata inequality comparison., Test ConnectionMetadata.__init__() creates metadata with required fields., Test ConnectionMetadata.__init__() with optional fields., Test ConnectionMetadata has all expected dataclass fields. (+6 more)

### Community 539 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from databas, Unit tests for connection utils.  Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 540 - "DeadLetterMessage"
Cohesion: 0.04
Nodes (68): DeadLetterMessage, DeadLetterQueue, Any, Path, Dead Letter Queue for failed NATS messages.  Stores messages that fail after all, Add failed message to dead letter queue (async version).          Args:, Add failed message to dead letter queue (sync version).          Args:, Retrieve and remove oldest message from DLQ (async version).          Returns: (+60 more)

### Community 541 - "NATS Error Handling Strategy"
Cohesion: 0.05
Nodes (41): 1. Always Handle Exceptions, 2. Use Specific Exception Types, 3. Preserve Exception Context, 4. Log with Context, 5. Don't Swallow Exceptions, Best Practices, Connection Errors, Error Handling Patterns (+33 more)

### Community 542 - "PersonalMessageSender"
Cohesion: 0.08
Nodes (23): mock_connection_manager(), mock_message_builder(), npc_event_handler(), Unit tests for NPC event handlers helper functions.  Tests the helper functions, Test _determine_direction_from_rooms() determines direction., Test _determine_direction_from_rooms() returns None when direction not found., Test _get_npc_departure_message() returns departure message., Create a mock connection manager. (+15 more)

### Community 543 - "OccupantFormatter"
Cohesion: 0.12
Nodes (15): OccupantFormatter, Formats and separates occupants by type., Initialize occupant formatter., Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists., Test OccupantFormatter._process_player_name_for_update() skips UUID player name., Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict., Test OccupantFormatter.separate_occupants_by_type() separates dict players. (+7 more)

### Community 544 - "GameTickService"
Cohesion: 0.12
Nodes (9): GameTickService, Get the current tick count.          Returns:             int: Current number of, Reset the tick count to zero., Get the current tick interval.          Returns:             float: Current tick, Set a new tick interval.          Args:             interval: New tick interval, Check if the service is currently running.          Returns:             bool: T, Service that manages the game tick system.      The game tick system runs at reg, Initialize the GameTickService.          Args:             event_publisher: Even (+1 more)

### Community 545 - "MockEventClass"
Cohesion: 0.15
Nodes (22): _extract_container_metadata(), _find_container_in_room_or_equipped(), _find_container_via_inner_container(), _find_container_via_wearable_service(), _get_container_data_from_component(), _handle_container_look(), _matches_item_instance_id(), _matches_name_or_slot() (+14 more)

### Community 546 - "test_dead_letter_queue.py"
Cohesion: 0.10
Nodes (22): Emote, Base, Predefined emote definitions., Unit tests for emote models.  Tests the Emote and EmoteAlias SQLAlchemy models., Test EmoteAlias aliases are case sensitive., Test Emote can be instantiated with required fields., Test Emote has correct table name., Test Emote __repr__ method. (+14 more)

### Community 547 - "test_message_filtering_helpers.py"
Cohesion: 0.11
Nodes (13): Get the number of rows affected., datetime, UUID, Set or update cooldown for a player and action., Delete all cooldowns for a player matching an action code pattern., Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE., Get player lucidity record., Get existing player lucidity record or create a new one. (+5 more)

### Community 548 - "TestGameTickService"
Cohesion: 0.12
Nodes (9): Test stop handles exceptions gracefully., Test get_tick_interval returns interval., Test _tick_loop increments tick count., Test _tick_loop publishes game tick events., Test suite for GameTickService class., Test GameTickService initialization with default interval., Test _tick_loop handles exceptions and continues., Test stop returns True when not running. (+1 more)

### Community 549 - "test_combat_audit.py"
Cohesion: 0.12
Nodes (15): Unit tests for combat audit logging.  Tests the combat_audit module classes and, Test CombatAuditLogger.log_combat_end() logs combat end., Test CombatAuditLogger.log_combat_security_event() logs security event., Test CombatAuditLogger.__init__() initializes logger., Test CombatAuditLogger.log_combat_security_event() handles no additional data., Test CombatAuditLogger.log_combat_validation_failure() logs validation failure., Test CombatAuditLogger.log_combat_monitoring_alert() logs high severity alert., Test CombatAuditLogger.log_combat_attack() logs combat attack. (+7 more)

### Community 550 - "optimized_validate_player_name"
Cohesion: 0.12
Nodes (16): Test validating empty player name., Test validating valid player name., Test validating player name with underscore., Test validating player name with hyphen., Test validating player name with numbers., Test validating player name starting with number (invalid)., Test validating player name with special characters (invalid)., test_optimized_validate_player_name_empty() (+8 more)

### Community 551 - "optimized_security_validator.py"
Cohesion: 0.20
Nodes (10): Test stripping ANSI codes from empty string., Test stripping ANSI codes from text without ANSI., Test stripping ANSI codes from text with ANSI., test_optimized_strip_ansi_codes_empty(), test_optimized_strip_ansi_codes_no_ansi(), test_optimized_strip_ansi_codes_with_ansi(), _cached_strip_ansi(), optimized_strip_ansi_codes() (+2 more)

### Community 552 - "PanelContextRuntime.tsx"
Cohesion: 0.16
Nodes (12): react, PanelProvider(), defaultPanels, PanelContext, PanelContextType, PanelLayout, PanelPosition, PanelProvider() (+4 more)

### Community 553 - "SpellRegistry"
Cohesion: 0.03
Nodes (116): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+108 more)

### Community 554 - "RoomInfo.tsx"
Cohesion: 0.29
Nodes (13): CompleteRoomInfo(), DebugInfo(), RoomDescription(), RoomEntities(), RoomExits(), RoomInfo(), RoomInfoContext, RoomInfoContextType (+5 more)

### Community 555 - "MessageBatcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 556 - "E2E Testing Setup Status"
Cohesion: 0.13
Nodes (14): Automated Test Files Created, ✅ Completed Work, Configuration Refactoring, ⚠️ Current Blocker, E2E Test Infrastructure, E2E Testing Setup Status, 🔧 Immediate Fix Needed, 🎯 Next Action Required (+6 more)

### Community 557 - "Test/Production Environment Separation"
Cohesion: 0.13
Nodes (14): 1. Configuration-Based Separation, 2. Automatic Test Detection, 3. Configuration-Driven Logging, 4. Configuration Files, Benefits, Environment Variables, Files Modified, Notes (+6 more)

### Community 558 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 559 - "unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 560 - "_process_session_dp_decay_and_death"
Cohesion: 0.19
Nodes (20): ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD.  This module defines Pydant, Presence statistics for connection monitoring.      This model represents aggreg, Session statistics for connection monitoring.      This model represents aggrega, Error statistics for connection monitoring.      This model represents aggregate, SessionStatistics (+12 more)

### Community 561 - "CreateItemInstanceInput"
Cohesion: 0.01
Nodes (219): AuthenticationBackend, BaseUserManager, ID, add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., main() (+211 more)

### Community 562 - "npc_combat_grace.py"
Cohesion: 0.10
Nodes (17): get_app_instance(), Return the runtime app instance attached during lifespan startup.      This prov, _connection_manager_from_config_app(), is_npc_attack_on_player_blocked_by_login_grace_period(), is_player_attack_blocked_by_login_grace_period(), UUID, Login grace-period checks for NPC combat integration (extracted to keep service, Resolve connection_manager from the public config app accessor.      Uses geta (+9 more)

### Community 563 - "Async Remediation Complete"
Cohesion: 0.28
Nodes (9): asyncio.to_thread Offloading, Async Audit 2025-12-03, Passive Lucidity Flux Blocking, Async Remediation Complete, Room Cache 60s TTL, Async Remediation Final Report, Async Remediation Summary 2025-12-03, Asyncio Code Review (+1 more)

### Community 564 - "Any"
Cohesion: 0.13
Nodes (20): filter_online_players(), filter_players_by_name(), format_who_result(), get_players_for_who(), handle_who_command(), Any, Who command handlers and utilities for MythosMUD.  This module contains the who, Filter players to only those who are online (active within threshold).      Args (+12 more)

### Community 565 - ".call"
Cohesion: 0.10
Nodes (11): Any, Broadcast combat start message to all players in the room., Broadcast combat attack to room. Excludes attacker from broadcast; sends them a, Broadcast NPC death message to all players in the room., Build perspective-specific attack messages., Broadcast combat end message to all players in the room., Broadcast combat error message to a specific player., Broadcast one short room message when an NPC switches aggro target (ADR-016). (+3 more)

### Community 566 - "conftest.py"
Cohesion: 0.10
Nodes (20): parse_last_active_datetime(), Parse last_active from string or datetime object to timezone-aware datetime., Test parse_last_active_datetime with None., Test parse_last_active_datetime with empty string., Test parse_last_active_datetime with string ending in Z., Test parse_last_active_datetime with string containing timezone., Test parse_last_active_datetime with string without timezone., Test parse_last_active_datetime with naive datetime. (+12 more)

### Community 567 - "ErrorMonitor"
Cohesion: 0.14
Nodes (17): ErrorMonitor, main(), Any, datetime, Path, Detect error trends over time.          Returns trend analysis results., Check for alert conditions.          Returns list of active alerts., Monitor errors continuously for a specified duration.          Args: (+9 more)

### Community 568 - "verify_linting_parity.py"
Cohesion: 0.12
Nodes (32): add_suppression_to_file(), main(), Path, Add suppression comment to a PowerShell file if it uses Write-Host and doesn't a, Process all PowerShell scripts in the scripts directory., check_alignment(), _check_pylint_suppressions(), _check_ruff_suppressions() (+24 more)

### Community 569 - "CoordinateGenerator"
Cohesion: 0.11
Nodes (16): CoordinateGenerator, Any, AsyncSession, Coordinate generation service for ASCII maps.  This module provides hierarchical, Load rooms and their exits from database.          Args:             plane: Plan, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits., Assign coordinates using BFS starting from origin. (+8 more)

### Community 570 - "Test Server Remediation Prompt - Cursor Executable Version"
Cohesion: 0.14
Nodes (13): Best Practices, COMPLETION VERIFICATION, CRITICAL "DO NOT" INSTRUCTIONS, CRITICAL: EXECUTION REQUIREMENTS, DECISION TREE - START HERE, ERROR HANDLING PROTOCOL, MANDATORY PROGRESS TRACKING, MANDATORY VERIFICATION CHECKPOINTS (+5 more)

### Community 571 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 572 - "Chat Panel Separation Implementation Tasks"
Cohesion: 0.20
Nodes (9): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Overview, Phase Dependencies, Risk Mitigation, Technical Risks (+1 more)

### Community 573 - "Main.py Refactoring Plan"
Cohesion: 0.14
Nodes (13): 📝 Conclusion, 📋 **CURRENT SESSION STATUS**, Directory Structure, 📋 Executive Summary, 🎯 Goals & Success Criteria, Main.py Refactoring Plan, **Memory Leak Prevention Work - REMOVED**, Phase Completion Checklist (+5 more)

### Community 574 - "parse_shutdown_parameters"
Cohesion: 0.18
Nodes (12): ConnectionErrorHandler, Any, UUID, Handle WebSocket-specific errors.          Args:             player_id: The play, Handle authentication-related errors.          Args:             player_id: The, Handle security violations.          Args:             player_id: The player's I, Attempt to recover from an error state for a player.          Args:, Get error handling statistics.          Args:             online_players: Online (+4 more)

### Community 575 - "_should_include_npc"
Cohesion: 0.10
Nodes (19): Unit tests for calendar models.  Tests the HolidayModel and NPCScheduleModel SQL, Test NPCScheduleModel can have optional notes., Test NPCScheduleModel has correct table name., Test NPCScheduleModel __repr__ method., Test HolidayModel can be instantiated with required fields., Test NPCScheduleModel can have empty arrays., Test HolidayModel can have bonus_tags., Test HolidayModel has correct table name. (+11 more)

### Community 576 - "skills_commands.py"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 577 - "chat_pose_helpers.py"
Cohesion: 0.23
Nodes (13): clear_player_pose(), get_player_pose(), get_room_poses(), normalize_player_id(), Any, UUID, Pose management helpers for chat service., Clear a player's pose.      Args:         player_id: ID of the player         po (+5 more)

### Community 579 - "total_xp_for_level"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 580 - "extract_definition_id_from_npc"
Cohesion: 0.18
Nodes (18): _format_occupants_result(), _get_event_handler_for_test_occupants(), _get_room_id_for_test_occupants(), handle_npc_test_occupants_command(), Any, NPC test-occupants command for debugging occupant queries., Resolve application, player, room_id, and event handler for NPC test occupants c, Handle NPC test occupants command - manually trigger occupant query for debuggin (+10 more)

### Community 581 - "Tiered Test Coverage Strategy"
Cohesion: 0.50
Nodes (4): Critical Code 90% Coverage, Global 70% Coverage Threshold, Tiered Test Coverage Strategy, Vitest Unit Tests

### Community 582 - "TestLogoutCommand"
Cohesion: 0.09
Nodes (15): Any, Unit tests for the logout command handler., Test logout command when persistence is not available., Test logout command when persistence operations fail., Test cases for the logout command handler., Test logout command when connection cleanup fails., Create a mock request object., Test logout command with arguments (should be ignored). (+7 more)

### Community 583 - "DeadLetterQueue"
Cohesion: 0.50
Nodes (3): Initialize NPCDefinition with defaults., Apply a default attribute value when SQLAlchemy leaves it unset or None., _set_default_if_missing()

### Community 584 - "RoomFixer"
Cohesion: 0.11
Nodes (17): Path, Fix self-references by adding proper flags.          Args:             room_data, Automatically fixes common room validation issues.      Implements safe correcti, Find the file for a room. Returns None if file doesn't exist., Create backup if requested., Fix missing exits field. Returns True if fixed., Fix missing optional fields. Returns True if any fixed., Initialize the room fixer.          Args:             base_path: Base directory (+9 more)

### Community 587 - "Linting Complexity Alignment"
Cohesion: 0.40
Nodes (6): Linting Complexity Alignment, Ruff C901 McCabe Complexity, Pylint Unique Findings, Ruff to Pylint Mapping, Lizard CCN Threshold (>10), Lizard Complexity Findings

### Community 588 - "RetryConfig"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 589 - ".load_player_mutes"
Cohesion: 0.16
Nodes (16): AsyncPersistenceRoomLookup, cleanup_websocket_connection(), PlayerDisconnectService, Protocol, UUID, WebSocket, WebSocket connection lifecycle: setup, welcome, and cleanup on disconnect.  Extr, Send welcome event to the client.      Returns:         True if successful, Fals (+8 more)

### Community 591 - "test_player_schema_converter_weapon.py"
Cohesion: 0.23
Nodes (18): _make_combat_instance(), _make_participant(), _make_service(), Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is returne, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat., process_attack orchestrates helper calls and returns the final CombatResult. (+10 more)

### Community 592 - "test_command_factories.py"
Cohesion: 0.14
Nodes (13): Unit tests for command factories.  Tests the CommandFactory class., Test create_stand_command delegates to exploration factory., Test create_cast_command delegates to utility factory., Test create_spells_command delegates to utility factory., Test CommandFactory.create_*() methods exist for all command types., Test create_pose_command delegates to communication factory., Test create_reply_command delegates to communication factory., test_command_factory_create_nonexistent_command() (+5 more)

### Community 593 - "UUID"
Cohesion: 0.16
Nodes (12): MPRegenerationService, Any, UUID, Get MP regeneration multiplier based on player state.          Args:, Restore MP from resting (accelerated regeneration).          Args:             p, Restore MP from meditation (highly accelerated regeneration).          Args:, Restore MP from consuming an item.          Args:             player_id: Player, Service for managing MP regeneration.      Handles passive regeneration over tim (+4 more)

### Community 594 - "StatisticsAggregator"
Cohesion: 0.05
Nodes (39): Any, UUID, Get comprehensive connection statistics.          Args:             player_webso, Analyze connection health distribution.          Args:             connection_me, Aggregates statistics from connection management components.      This class pro, Analyze connection types.          Args:             connection_metadata: Connec, Analyze connection ages.          Args:             connection_metadata: Connect, Analyze session health.          Args:             connection_metadata: Connecti (+31 more)

### Community 595 - "load_motd"
Cohesion: 0.23
Nodes (11): Unit tests for motd_loader utilities.  Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+3 more)

### Community 596 - "properties"
Cohesion: 0.14
Nodes (14): description, description, description, description, type, properties, field1, field2 (+6 more)

### Community 597 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.11
Nodes (18): 🔴 CRITICAL (Fix First - Blocking Issues), 🔴 CRITICAL FIXES - Compilation Errors, For Each Issue Category, 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🟡 HIGH PRIORITY FIXES - Code Quality Issues, 🔵 LOW PRIORITY (Fix Last - Polish), 🎯 MANDATORY AI EXECUTION PROTOCOL, 🟢 MEDIUM PRIORITY (Fix Third - Enhancement) (+10 more)

### Community 598 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.15
Nodes (13): 🔴 CRITICAL FIXES - Compilation Errors, For Each Issue Category, 🟡 HIGH PRIORITY FIXES - Code Quality Issues, 🎯 MANDATORY AI EXECUTION PROTOCOL, 🟢 MEDIUM PRIORITY FIXES - Style Issues, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide (+5 more)

### Community 599 - "LogAnalyzer"
Cohesion: 0.13
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time.          Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 600 - "MythosMUD Wiki Log"
Cohesion: 0.13
Nodes (14): [2026-07-19] ingest | Geography and Major Locations, [2026-07-19] ingest | MythosMUD worldbuilding, [2026-07-19] ingest | Things and notes to expand on, [2026-07-19] query | DML migrations apply paths, [2026-07-19] setup | external vault junctions, [2026-07-19] setup | Karpathy LLM wiki vault, [2026-07-19] sync | graphify code wiki, [2026-07-19] sync | graphify community labels (+6 more)

### Community 601 - "InventoryMutationGuard"
Cohesion: 0.02
Nodes (153): AbstractContextManager, Lock, _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str() (+145 more)

### Community 602 - "Phase 3: Polish and Optimization"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 3: Polish and Optimization, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 603 - "Phase 4: Testing and Refinement"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 4: Testing and Refinement, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 604 - "Fixture Optimization Complete"
Cohesion: 0.15
Nodes (12): 1. Created Class-Scoped Fixture (`container_test_client_class`), 2. Updated Test Classes to Use Optimized Fixture, 3. Marked All Slow Tests, After (Expected), Before, Changes Implemented, Files Modified, Fixture Optimization Complete (+4 more)

### Community 605 - "applies_to"
Cohesion: 0.17
Nodes (13): items, minItems, type, items, minItems, type, items, type (+5 more)

### Community 607 - "properties"
Cohesion: 0.15
Nodes (13): minLength, type, minLength, type, type, category, name, notes (+5 more)

### Community 610 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 611 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 612 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 613 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, properties, minLength, type, id, name, season (+4 more)

### Community 614 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, minLength, type, properties, minLength, type, type (+4 more)

### Community 615 - "test_go_command.py"
Cohesion: 0.04
Nodes (68): _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement(), _movement_combat_and_event_bus_from_go_app(), _movement_service_for_go_command(), Any, Validate that exit exists and target room is valid., Resolve player_combat_service and event_bus from DI container or legacy app.stat (+60 more)

### Community 616 - "required"
Cohesion: 0.17
Nodes (12): $defs, scheduleEntry, applies_to, category, days, end_hour, id, name (+4 more)

### Community 617 - "level_from_total_xp"
Cohesion: 0.23
Nodes (16): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+8 more)

### Community 618 - ".despawn_npc"
Cohesion: 0.33
Nodes (9): Any, Player, Player room validation helpers for PlayerRepository.  Validates and fixes invali, Return True if room validation should be skipped (cache empty, instanced, or tut, Validate player's current room and fix if invalid.      Args:         room_cache, Validate and fix player room, persisting the fix if needed.      Args:         r, should_skip_room_validation(), validate_and_fix_player_room() (+1 more)

### Community 619 - "PostgreSQL Procedures Migration - Audit Spreadsheet"
Cohesion: 0.12
Nodes (15): Linkdead Grace Period, Gunicorn + Uvicorn Production, HTTPS and WSS Requirement, Audit Table, Domain Grouping Summary, Existing PostgreSQL Functions (Already in DDL), PostgreSQL Procedures Migration - Audit Spreadsheet, Scope (+7 more)

### Community 620 - "extract_npc_metadata"
Cohesion: 0.22
Nodes (7): client, Test logging in FastAPI endpoints., Simulate client POST request., Simulate client GET request., Test API request logging in integration tests., test_api_request_logging(), test_fastapi_endpoint_logging()

### Community 621 - "._trim_samples"
Cohesion: 0.11
Nodes (15): Shared SQLAlchemy metadata for MythosMUD models.  This module provides the share, NPC Database metadata for MythosMUD.  This module defines the SQLAlchemy metadat, Unit tests for metadata modules.  Tests the shared SQLAlchemy metadata instances, Test that metadata is a MetaData instance., Test that npc_metadata is a MetaData instance., Test that metadata and npc_metadata are separate instances., Test that Base is a DeclarativeBase subclass., Test that Base has metadata attribute set to shared metadata. (+7 more)

### Community 622 - "._is_uuid_string"
Cohesion: 0.17
Nodes (10): Process a string occupant (legacy format) and add to list if valid.          Arg, Check if a string looks like a UUID.          Args:             value: The strin, Test OccupantFormatter._is_uuid_string() returns True for valid UUID., Test OccupantFormatter._is_uuid_string() returns False for invalid length., Test OccupantFormatter._is_uuid_string() returns False for wrong dash count., Test OccupantFormatter._is_uuid_string() returns False for invalid characters., test_occupant_formatter_is_uuid_string_invalid_chars(), test_occupant_formatter_is_uuid_string_invalid_dashes() (+2 more)

### Community 623 - "WebSocketMessageValidator"
Cohesion: 0.04
Nodes (72): get_message_validator(), MessageValidationError, BaseModel, Exception, WebSocket message validation for MythosMUD.  This module provides comprehensiv, Calculate the maximum nesting depth of a JSON structure.          Args:, Validate that strings in the JSON structure don't exceed length limits., Validate message against Pydantic schema.          Args:             message: (+64 more)

### Community 624 - "TestPrepareCommandForProcessing"
Cohesion: 0.12
Nodes (17): PasswordHasher, create_hasher_with_params(), Create a PasswordHasher with custom parameters., Test that create_hasher_with_params logs warning for low time_cost., Test that create_hasher_with_params logs warning for low memory_cost., Test creating hasher with valid parameters., Test creating hasher with invalid time_cost., Test creating hasher with invalid memory_cost. (+9 more)

### Community 625 - "test_config.py"
Cohesion: 0.01
Nodes (289): CombatAction, CombatParticipant, CombatParticipantType, CombatStatus, _get_default_damage(), Enum, Combat system models for in-memory state management.  This module defines the da, Check if participant can perform voluntary combat actions.          Unconscious (+281 more)

### Community 626 - "PlayerEventHandlerUtils"
Cohesion: 0.03
Nodes (59): mock_connection_manager(), mock_logger(), mock_utils(), player_respawn_event_handler(), Unit tests for player respawn event handlers.  Tests the PlayerRespawnEventHandl, Test get_player_data_for_respawn() returns None when connection manager not avai, Test get_player_data_for_respawn() returns None when persistence not available., Test get_player_data_for_respawn() returns None when player not found. (+51 more)

### Community 627 - "test_config_init.py"
Cohesion: 0.28
Nodes (6): PlayerRespawnWrapper, Any, Respawn a delirious player by user ID.          This method handles the complete, Wrapper service for player respawn operations., Initialize with a persistence layer., Respawn a dead player by user ID.          This method handles the complete resp

### Community 628 - "test_player_event_handlers_utils.py"
Cohesion: 0.17
Nodes (11): Unit tests for player event handler utilities.  Tests the PlayerEventHandlerUtil, Test _extract_name_from_occupant() with dict containing npc_name., Test _extract_name_from_occupant() with dict containing name., Test count_occupants_by_type() with mixed occupants., Test is_player_disconnecting() returns False when player is not disconnecting., Test normalize_player_id() with invalid string., test_count_occupants_by_type_mixed(), test_extract_name_from_occupant_dict_with_name() (+3 more)

### Community 629 - "test_websocket_handler_error_handling.py"
Cohesion: 0.17
Nodes (11): mock_websocket(), Unit tests for websocket handler error handling.  Tests the error handling funct, Create a mock WebSocket., Test _send_error_response() successfully sends error., Test _send_error_response() handles WebSocket disconnection., Test _handle_runtime_error() detects WebSocket disconnection., Test _handle_runtime_error() handles other runtime errors., test_handle_runtime_error_disconnected() (+3 more)

### Community 630 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.17
Nodes (11): mock_connection_manager(), mock_websocket(), Unit tests for websocket handler rate limiting.  Tests the rate limiting functio, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id., Test _check_rate_limit() returns True when rate limit check passes., Test _check_rate_limit() returns False when rate limit exceeded. (+3 more)

### Community 631 - "_errors_len"
Cohesion: 0.13
Nodes (14): IdleMovementHandler, Check if NPC is in combat via UUID lookup.          Args:             npc_id:, Check if NPC is in combat via string ID mapping.          Args:             n, Handler for NPC idle movement logic.      This class manages the decision-maki, Movement is skipped when random.random() > idle_movement_probability., Gating skips idle movement when combat service lists this NPC., Test _is_npc_in_combat() returns False when NPC is not in combat., Test _calculate_distance_to_room() with different rooms. (+6 more)

### Community 632 - "test_combat_validator.py"
Cohesion: 0.02
Nodes (87): Unit tests for combat validator.  Tests the CombatValidator class for combat com, Test validate_combat_command with target name too long., Test validate_combat_command when rate limited., Test validate_combat_command handles exceptions gracefully., Test validate_target_exists with exact match., Test validate_target_exists with case-insensitive match., Test validate_target_exists with partial match., Test validate_target_exists with no match. (+79 more)

### Community 633 - "room_hierarchy_schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, anyOf, description, description, exits, id, name, required (+3 more)

### Community 634 - "GridLayoutManager.tsx"
Cohesion: 0.20
Nodes (5): GridLayoutManager(), GridLayoutManagerProps, layoutConfig, PanelComponent, ResponsiveGridLayout

### Community 635 - "GameClientV2Dock.test.tsx"
Cohesion: 0.06
Nodes (51): buildCreateCharacterPayload(), CharacterNameScreen(), CharacterNameScreenProps, CreateCharacterPayload, getCreateCharacterErrorMessage(), OccupationSlotPayload, PersonalInterestPayload, SkillsPayload (+43 more)

### Community 636 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.22
Nodes (9): 10. Final Verification, 5. Test Environment Setup, 6. Quality Assurance Checklist, 8. Error Handling and Debugging, Common Debug Commands, Environment Variables, REQUIRED TOOL USAGE PATTERN, Test Configuration (+1 more)

### Community 637 - "CircuitBreaker Implementation Planning Document"
Cohesion: 0.18
Nodes (10): CircuitBreaker Implementation Planning Document, Configuration Schema, Dependencies, Gradual Rollback, Immediate Rollback, Objectives, Overview, Rollback Plan (+2 more)

### Community 639 - "Any"
Cohesion: 0.17
Nodes (10): Any, AsyncSession, UUID, Get room UUID by stable_id (hierarchical room ID).          Args:             st, Mark room as explored using the provided session.          Args:             ses, Get list of room IDs that a player has explored.          Args:             play, Check if a player has explored a specific room.          Args:             playe, Synchronous wrapper for mark_room_as_explored.          This method is designed (+2 more)

### Community 640 - "NPCMaintenanceConfig"
Cohesion: 0.18
Nodes (7): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD.  This module defines configuration settings for, Configuration for NPC lifecycle maintenance.      This class centralizes all tim, Get the respawn delay for a specific NPC type.          Args:             npc_ty, Check if NPC maintenance should run on this tick.          Args:             tic, Get a summary of all NPC configuration values.          Returns:             Dic

### Community 641 - ".publish"
Cohesion: 0.12
Nodes (16): mock_player_service(), mock_quest_service(), mock_request(), mock_user(), player_id(), Unit tests for GET /api/players/{player_id}/quests (quest log).  Tests get_playe, GET quests with include_completed=False passes to get_quest_log., GET quests raises 403 when validate_character_access returns not ok. (+8 more)

### Community 642 - "Security Implementation"
Cohesion: 0.33
Nodes (6): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection

### Community 643 - "CircuitBreakerOpen"
Cohesion: 0.17
Nodes (13): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _ensure_uuid(), _maybe_await(), Any, UUID, Rescue service encapsulating rescue flows with injectable dependencies.  This is (+5 more)

### Community 644 - ".check_player_mute_status"
Cohesion: 0.17
Nodes (15): _format_room_posture_message(), Create a descriptive room message for posture changes., Unit tests for position command helper functions.  Tests helper functions in pos, Test _format_room_posture_message() formats sitting message., Test _format_room_posture_message() formats lying message., Test _format_room_posture_message() formats standing from lying message., Test _format_room_posture_message() formats standing from sitting message., Test _format_room_posture_message() formats standing with no previous position. (+7 more)

### Community 645 - ".retry_async"
Cohesion: 0.18
Nodes (10): Any, UUID, Build final inventory with consumed materials removed.          Args:, Consume spell materials from player inventory.          Args:             player, Service for handling spell material requirements.      Handles checking if playe, Initialize the spell materials service.          Args:             player_servic, Check if player has all required materials.          Args:             player_id, Process a single material requirement.          Args:             material: Mate (+2 more)

### Community 646 - "Enhanced Logging Migration Report"
Cohesion: 0.33
Nodes (5): Enhanced Logging Features, Enhanced Logging Migration Report, Next Steps, Successfully Updated Files, Summary

### Community 647 - "wrap_third_party_exception"
Cohesion: 0.17
Nodes (9): _cfg_float(), _npc_id_str(), _passes_movement_probability(), Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement.          Checks multiple con, Check if an NPC is currently in combat.          Args:             npc_instan, Get exits from current room that stay within subzone boundaries.          Args, Execute idle movement for an NPC.          This method orchestrates the full i (+1 more)

### Community 648 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 649 - "properties"
Cohesion: 0.18
Nodes (11): description, type, description, type, description, minimum, type, combat_modifier (+3 more)

### Community 650 - "RoomInfoPanel.tsx"
Cohesion: 0.29
Nodes (14): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Request, ValidationError, Convert ValidationError to appropriate HTTPException for respawn.      Args:, Convert ValidationError to appropriate HTTPException for delirium respawn., test_handle_delirium_validation_generic_500(), test_handle_delirium_validation_lucidity_keyword() (+6 more)

### Community 651 - "PostgresRow"
Cohesion: 0.09
Nodes (15): PostgresRow, Any, Row-like object for PostgreSQL query results., Return the keys of the row dictionary.          Returns:             dict_keys:, Test PostgresRow class., Test PostgresRow initialization., Test PostgresRow.__getitem__ with string key., Test PostgresRow.__getitem__ with integer index. (+7 more)

### Community 652 - "TargetMatch"
Cohesion: 0.17
Nodes (10): _create_mock_container_row(), UUID, Tests for SQL injection protection in container persistence operations.  These t, Test that update_container uses parameterized queries, not string concatenation., Test that column names are hardcoded, not from user input., Create a complete mock container row with all required columns., Test SQL injection protection in container persistence., Test that SQL injection in lock_state is prevented. (+2 more)

### Community 653 - "Any"
Cohesion: 0.25
Nodes (12): get_all_professions(), get_profession_by_id(), Request, Profession management API endpoints for MythosMUD server.  This module handles a, Retrieve all available professions for character creation with caching.      :pa, Retrieve specific profession details by ID with caching.      :param profession_, Unit tests for server.api.professions., test_get_all_professions_requires_auth() (+4 more)

### Community 654 - "multiplayer-playwright-testing.md"
Cohesion: 0.20
Nodes (9): 🎯 AVAILABLE SCENARIOS, 🔄 BACKWARD COMPATIBILITY, 🚨 CRITICAL AI EXECUTOR REQUIREMENTS 🚨, 📋 EXECUTION OPTIONS, 📖 MANDATORY EXECUTION ORDER, 🛑 MANDATORY EXECUTION PROTOCOL 🛑, 🎮 MODULAR E2E TEST SUITE STRUCTURE 🎮, 🔧 TESTING APPROACH (+1 more)

### Community 655 - "Mypy Type Checking Remediation Prompt - AI-Optimized Version"
Cohesion: 0.20
Nodes (9): 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, Common Mypy Error Codes, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, 📊 MYPY ERROR CODE CATEGORIZATION GUIDE, Mypy Type Checking Remediation Prompt - AI-Optimized Version (+1 more)

### Community 656 - "MythosMUD Wiki Index"
Cohesion: 0.20
Nodes (9): Code (curated), Concepts, External folders (junctions; not wiki), Hubs, MythosMUD Wiki Index, Raw inventory (immutable), Sources (summaries), Syntheses / comparisons / queries (+1 more)

### Community 657 - "PlayerGuidFormatter"
Cohesion: 0.04
Nodes (59): BoundLogger, Logging utilities for directory management, path resolution, and environment det, # NOTE: Using structlog directly here to avoid circular import., # NOTE: Using structlog directly here to avoid circular import., # NOTE: Infrastructure files may use structlog.get_logger() directly to avoid, Structlog logger for rotate_log_files (cast silences basedpyright Any from get_l, _rotation_bound_logger(), PlayerGuidFormatter (+51 more)

### Community 658 - "websocket_endpoint"
Cohesion: 0.18
Nodes (7): Check if the status effect is still active., Get all currently active status effects.          Args:             current_tick, Any, Initialize Invite with defaults., _npc_alive_and_active(), Return True if NPC is alive (determination_points > 0)., Allow backward-compatible assignment (npc.is_alive = False).

### Community 659 - "load_test_10_players.spec.ts"
Cohesion: 0.22
Nodes (6): generateLoadTestCredential(), INVITE_CODES, PLAYER_CONFIGS, PlayerConfig, NOTE: This test is designed to be executed using Playwright MCP tools for, registerPlayer()

### Community 660 - "TestRunner"
Cohesion: 0.13
Nodes (14): main(), Path, Verify test database configuration.          Note: For PostgreSQL databases, sch, Build the pytest command with proper configuration.          Args:             t, # NOTE: Test runner uses minimal structlog configuration for console output, Run the test suite with proper configuration.          Args:             test_pa, Run integration tests only., Run all tests (unit, integration, but not E2E by default). (+6 more)

### Community 661 - "test_combat_persistence_handler_events.py"
Cohesion: 0.03
Nodes (78): CombatPersistenceHandler, Any, UUID, Combat persistence handling logic.  Handles player DP persistence, verification,, # NOTE: The game tick loop will also check for dead players, but this provides i, Synchronously persist player DP to database.          This is the actual persist, Persist player DP to database in background (fire-and-forget).          This met, Handles combat-related persistence operations. (+70 more)

### Community 662 - "get_cached_player"
Cohesion: 0.13
Nodes (23): Unit tests for player_cache utilities.  Tests the player caching functions for r, Test get_cached_player() returns None when no cache exists., Test cache_player() and get_cached_player() operations., Test get_cached_player() returns None for nonexistent key., Test cache_player() can cache multiple players., Test cache_player() overwrites existing entries., Test get_cached_player() handles missing state., Test cache_player() handles missing state gracefully. (+15 more)

### Community 663 - "enum"
Cohesion: 0.20
Nodes (10): artifact, consumable, container, currency, equipment, quest, enum, type (+2 more)

### Community 664 - "Chat Panel"
Cohesion: 0.33
Nodes (6): Chat Message Type Categorization Bug, Chat Panel, Commands Panel, Game Log Panel, Chat Message Routing Bug Fix, Room Description Routing Bug Fix

### Community 665 - "enum"
Cohesion: 0.20
Nodes (10): city, countryside, desert, mountains, swamp, tundra, zone_type, description (+2 more)

### Community 667 - "alias_schema.json"
Cohesion: 0.20
Nodes (9): version, additionalProperties, description, $id, aliases, required, $schema, title (+1 more)

### Community 668 - "SQLAlchemyAsyncLinter"
Cohesion: 0.11
Nodes (18): Await, lint_directory(), lint_file(), main(), Call, Import, ImportFrom, Path (+10 more)

### Community 669 - "quality_fragmentation_lizard.py"
Cohesion: 0.17
Nodes (25): git_show_file(), _check_head_rows(), check_lizard_limits(), _has_file_nloc_override(), has_lizard_override(), _has_override_in_file(), _iter_lizard_function_maps(), _lizard_entries() (+17 more)

### Community 670 - "properties"
Cohesion: 0.20
Nodes (10): properties, minLength, pattern, type, minLength, type, type, id (+2 more)

### Community 671 - "InventorySchemaValidationError"
Cohesion: 0.38
Nodes (4): Any, Initialize LucidityAdjustmentLog with defaults., Initialize LucidityExposureState with defaults., Initialize PlayerLucidity with defaults.

### Community 672 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 673 - "test_level_curve.py"
Cohesion: 0.14
Nodes (14): format_player_location(), Format player location as Zone: Sub-zone: Room from room ID.      Args:, Test format_player_location() handles invalid room ID., test_format_player_location_invalid(), Test format_player_location() with short room ID format., Test format_player_location() with non-string input., Test formatting valid player location., Test formatting invalid player location. (+6 more)

### Community 674 - "UnsubscribeError"
Cohesion: 0.03
Nodes (75): Any, RateLimiter, Clean up old rate limit attempts to prevent memory bloat.          Args:, Clean up large data structures to prevent memory bloat.          Args:, Remove all rate limit data for a specific player.          Args:             pla, Rate limiter for connection attempts and other operations.      This class provi, Get rate limiter statistics.          Returns:             dict: Statistics abou, Check if a connection has exceeded message rate limits.          Args: (+67 more)

### Community 675 - "schedule_end_combat_if_npc_died_best_effort"
Cohesion: 0.33
Nodes (5): database, deprecated_database_logging(), Demonstrate DEPRECATED database logging patterns., Simulate database operations., Simulate database query.

### Community 676 - "test_lucidity_models.py"
Cohesion: 0.22
Nodes (8): Any, UUID, Resolve the target for a spell cast.          Args:             player_id: ID of, Get player object from persistence., Get the combat target for a player if they are in combat.          Args:, Resolve self-target spell. Returns (target_match, error_message)., Resolve area/all target spell. Returns (target_match, error_message)., Resolve entity/location target spell with explicit target. Returns (target_match

### Community 677 - "MagicServiceCompletionMixin"
Cohesion: 0.09
Nodes (21): Unit tests for connection establishment.  Tests the connection_establishment mod, Test _remove_dead_connection() handles connection not present., Test _update_player_connection_list() removes player when no active connections., Test _cleanup_dead_connections() handles empty list., Test _cleanup_dead_connections() cleans up dead connections., Test _register_new_connection() registers new connection., Test _setup_connection_metadata() handles None session and token., Test establish_websocket_connection() successfully establishes connection. (+13 more)

### Community 678 - "ChannelBroadcastingStrategyFactory"
Cohesion: 0.20
Nodes (9): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Register a new strategy for a channel type.          Args:             channel_t, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default stra, Test ChannelBroadcastingStrategyFactory.register_strategy() registers new strate, Test global channel_strategy_factory instance exists., test_channel_broadcasting_strategy_factory_init(), test_channel_broadcasting_strategy_factory_register_strategy() (+1 more)

### Community 679 - "UnknownChannelStrategy"
Cohesion: 0.20
Nodes (8): Strategy for unknown channel types., Initialize unknown channel strategy.          Args:             channel_type: Un, Get strategy for channel type.          Args:             channel_type: Type of, UnknownChannelStrategy, Test UnknownChannelStrategy.broadcast() handles unknown channel., Test ChannelBroadcastingStrategyFactory.get_strategy() returns UnknownChannelStr, test_channel_broadcasting_strategy_factory_get_strategy_unknown(), test_unknown_channel_strategy_broadcast()

### Community 680 - "RoomBasedChannelStrategy"
Cohesion: 0.20
Nodes (9): Strategy for room-based channels (say, local, emote, pose)., Initialize room-based channel strategy.          Args:             channel_type:, RoomBasedChannelStrategy, Test RoomBasedChannelStrategy.broadcast() broadcasts to room., Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., Test RoomBasedChannelStrategy.broadcast() handles missing room_id., test_channel_broadcasting_strategy_factory_get_strategy_known(), test_room_based_channel_strategy_broadcast() (+1 more)

### Community 681 - "get_or_create_hate_list"
Cohesion: 0.33
Nodes (6): deprecated_error_handling(), deprecated_exception_handling(), Demonstrate DEPRECATED exception handling patterns., Simulate a risky operation., Demonstrate DEPRECATED error handling patterns., risky_operation()

### Community 682 - "CombatAuditLogger"
Cohesion: 0.20
Nodes (9): CombatAuditLogger, Specialized logger for combat events and security monitoring.      Provides stru, Initialize the combat audit logger., Test CombatAuditLogger.log_combat_rate_limit() logs rate limit., Test CombatAuditLogger.log_combat_monitoring_alert() includes player info., Test CombatAuditLogger.get_combat_audit_summary() uses time range., test_combat_audit_logger_get_combat_audit_summary_with_time_range(), test_combat_audit_logger_log_combat_monitoring_alert_with_player() (+1 more)

### Community 683 - "TestProcessAliasExpansion"
Cohesion: 0.33
Nodes (6): process_batch(), process_item(), Test batch operation logging., Simulate batch processing., Simulate item processing., test_batch_logging()

### Community 684 - "attach_compatibility_properties"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager.  This module provides compatibilit, Create getter, setter, and deleter functions for a property.      Args: (+17 more)

### Community 685 - "TestHandleSpecialCommandRouting"
Cohesion: 0.40
Nodes (4): Test WebSocket logging in integration tests., Simulate WebSocket connection., test_websocket_logging(), WebSocket

### Community 686 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 687 - "migrate_rooms.py"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 688 - "TestValidateCommandBasics"
Cohesion: 0.16
Nodes (8): Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory., Load channel mutes from JSON data into memory., Load global mutes from JSON data into memory., Load mute data for a specific player from JSON file.          Args:, Create a UserManager instance., user_manager()

### Community 689 - "TestCheckCastingState"
Cohesion: 0.06
Nodes (69): force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_memory_alerts(), get_memory_leak_metrics(), get_memory_stats() (+61 more)

### Community 690 - "TestCheckAllCommandBlocks"
Cohesion: 0.33
Nodes (3): Schedule idle movement; default False. Override in subclasses (e.g. PassiveMobNP, Hook for subclasses to add context before behavior rules run.         Override, Execute NPC behavior based on context.

### Community 691 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation.  Ensures the investigation w, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not stable_id, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 692 - "test_nats_message_handler_chat.py"
Cohesion: 0.03
Nodes (71): Unit tests for NATS message handler chat and messaging.  Tests chat field extrac, Test _get_player_lucidity_tier returns default on error., Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_name type, Test _validate_chat_message_fields raises TypeError for invalid content type., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _extract_chat_message_fields handles whisper target_id., Test _extract_chat_message_fields extracts fields. (+63 more)

### Community 693 - "test_nats_message_handler_subzone_events.py"
Cohesion: 0.03
Nodes (67): Unit tests for NATS message handler subzone and event handling.  Tests subzone s, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test subscribe_to_subzone raises error when subject manager unavailable., Test unsubscribe_from_event_subjects handles partial success., Test subscribe_to_event_subjects handles partial failure., Test get_event_subscription_count returns count., Test is_event_subscription_active checks subscription. (+59 more)

### Community 694 - "test_npc_event_handlers.py"
Cohesion: 0.21
Nodes (12): MechanicalEffect, ProfessionData, ProfessionListResponse, ProfessionResponse, BaseModel, Profession API response schemas for MythosMUD server.  This module provides Pyda, Stat requirement for a profession., Mechanical effect of a profession. (+4 more)

### Community 695 - "test_player_event_handlers_room.py"
Cohesion: 0.03
Nodes (69): Unit tests for player room event handlers.  Tests the PlayerRoomEventHandler cla, Test broadcast_player_entered_message() skips when room_id is None., Test subscribe_player_to_room() successfully subscribes player., Test subscribe_player_to_room() handles invalid player_id., Test subscribe_player_to_room() handles subscription errors., Test _send_room_name_message() sends room name., Test _prepare_room_data() prepares room data with to_dict., Test _prepare_room_data() handles room without to_dict method. (+61 more)

### Community 697 - "optimized_validate_action_content"
Cohesion: 0.20
Nodes (10): Test validating empty action., Test validating valid action., Test validating action with dangerous characters., Test validating action with injection pattern., test_optimized_validate_action_content_dangerous_chars(), test_optimized_validate_action_content_empty(), test_optimized_validate_action_content_injection(), test_optimized_validate_action_content_valid() (+2 more)

### Community 698 - "optimized_validate_alias_name"
Cohesion: 0.20
Nodes (10): Test validating empty alias name., Test validating valid alias name., Test validating alias name starting with number (invalid)., Test validating alias name with hyphen (invalid - aliases don't allow hyphens)., test_optimized_validate_alias_name_empty(), test_optimized_validate_alias_name_hyphen(), test_optimized_validate_alias_name_starts_with_number(), test_optimized_validate_alias_name_valid() (+2 more)

### Community 699 - "optimized_sanitize_unicode_input"
Cohesion: 0.20
Nodes (10): Test sanitizing empty string., Test sanitizing normal text (no changes expected)., Test sanitizing text with Unicode issues., test_optimized_sanitize_unicode_input_empty(), test_optimized_sanitize_unicode_input_normal_text(), test_optimized_sanitize_unicode_input_unicode(), _cached_ftfy_fix(), optimized_sanitize_unicode_input() (+2 more)

### Community 700 - "optimized_validate_security_comprehensive"
Cohesion: 0.20
Nodes (10): Test comprehensive security validation of empty string., Test comprehensive security validation of valid text., Test comprehensive security validation with dangerous characters., Test comprehensive security validation with injection pattern., test_optimized_validate_security_comprehensive_dangerous_chars(), test_optimized_validate_security_comprehensive_empty(), test_optimized_validate_security_comprehensive_injection(), test_optimized_validate_security_comprehensive_valid() (+2 more)

### Community 702 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 703 - "run-playwright-tests.js"
Cohesion: 0.22
Nodes (7): clientRoot, __dirname, E2E_BACKEND_BASE_URL, env, __filename, playwright, testsDir

### Community 704 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.22
Nodes (9): For Each Issue Category, 🎯 MANDATORY AI EXECUTION PROTOCOL, Mypy Type Checking, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide, Phase 6: Verification Protocol, Phase 7: Success Validation (+1 more)

### Community 705 - "test_load_world_seed.py"
Cohesion: 0.13
Nodes (23): CaptureFixture, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, MonkeyPatch, Protocol, Regression tests for scripts/load_world_seed.py (URL parsing, allowlist, search_, When POSTGRES_SEARCH_PATH is unset, search_path defaults to the DB name from the (+15 more)

### Community 706 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 707 - "applies_to"
Cohesion: 0.28
Nodes (9): items, minItems, type, uniqueItems, items, items, minLength, type (+1 more)

### Community 708 - "handle_system_command"
Cohesion: 0.24
Nodes (10): handle_system_command(), Any, Broadcast a system-level message via the chat service if available., Unit tests for system command handlers.  Tests the system command functionality., Test handle_system_command() broadcasts system message., Test handle_system_command() handles missing message., Test handle_system_command() handles missing chat service., test_handle_system_command() (+2 more)

### Community 709 - "test_inventory_helpers.py"
Cohesion: 0.09
Nodes (31): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+23 more)

### Community 710 - "CombatDPSync"
Cohesion: 0.14
Nodes (13): CombatDPSync, Any, UUID, Get persistence layer from application container.          Args:             pla, Verify that player DP was successfully saved to database.          Args:, Log death threshold events based on DP changes.          Args:             curre, Update player DP and save to database.          Args:             persistence: P, Synchronously persist player DP to database.          This is the actual persist (+5 more)

### Community 711 - "MinimapRenderer"
Cohesion: 0.10
Nodes (16): MinimapRenderer, Any, Renders room connectivity graphs in various visual formats.      Implements the, Extract street acronym from room ID.          Args:             room_id: Full ro, Extract street name from room ID.          Args:             room_id: Full room, Get color code for a street.          Args:             room_id: Full room ID, Render the mini-map as ASCII art with grid-based visualization.          Args:, Initialize the mini-map renderer. (+8 more)

### Community 712 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 714 - "Technical Implementation"
Cohesion: 0.22
Nodes (9): 2. Message Routing Logic, 3. State Management, 4. Event Handling, Command Routing Logic, Current Logic (in CommandPanel), New Logic Distribution, New State Structure, State Distribution (+1 more)

### Community 716 - "1. **Server-Side Unit Tests** (`server/tests/test_event_broadcasting_bugs.py`)"
Cohesion: 0.22
Nodes (9): 1. **Server-Side Unit Tests** (`server/tests/test_event_broadcasting_bugs.py`), 3. **Integration Tests** (`server/tests/test_integration_bug_prevention.py`), Connection Timeout Tests, End-to-End Bug Scenarios, EventBus Integration Tests, Integration Test Categories, Player Movement Message Exclusion Tests, Room Event Broadcasting Tests (+1 more)

### Community 717 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 719 - "client"
Cohesion: 0.25
Nodes (8): Track connection in session.      Args:         connection_id: The connection ID, _setup_session_tracking(), Test _setup_session_tracking() handles None session_id., Test _setup_session_tracking() creates new session entry., Test _setup_session_tracking() adds to existing session., test_setup_session_tracking_existing_session(), test_setup_session_tracking_new_session(), test_setup_session_tracking_no_session_id()

### Community 720 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 721 - "properties"
Cohesion: 0.22
Nodes (9): properties, description, pattern, type, created_at, updated_at, description, pattern (+1 more)

### Community 722 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 723 - "validate_secure_path"
Cohesion: 0.08
Nodes (24): Validate and sanitize a user-provided path to prevent path traversal     attacks, validate_secure_path(), Test validate_secure_path detects when common_path != base_path (lines 59-66)., Test validate_secure_path with valid path., Test validate_secure_path handles different drives on Windows., Test validate_secure_path rejects path traversal with .., Test validate_secure_path rejects path traversal with ~, Test validate_secure_path with nested valid path. (+16 more)

### Community 724 - "MetricsCollector"
Cohesion: 0.09
Nodes (13): MetricsCollector, Any, Record a circuit breaker state change.          Args:             old_state: Pre, Record message processing time.          Args:             duration_ms: Processi, Get current metrics snapshot.          Returns:             Dictionary containin, Reset all metrics counters.          Useful for clearing metrics after a deploym, Simple metrics collector for NATS message delivery.      Thread-safe metrics col, Get concise metrics summary.          Returns:             High-level metrics su (+5 more)

### Community 725 - "TauntCommandHandler"
Cohesion: 0.17
Nodes (7): Any, Broadcast player respawn message to all players in the room., Send DP decay message to a specific mortally wounded player., Build personal and room messages for mortally wounded broadcast., Send mortally wounded personal message. Logs warning on failure., Broadcast player mortally wounded to room. Sends personal message to wounded pla, Broadcast player death message to all players in the room.

### Community 726 - "Any"
Cohesion: 0.17
Nodes (12): _find_dead_connections(), Find dead WebSocket connections for a player before acquiring lock.      Args:, Test _find_dead_connections() returns empty list when player not found., Test _find_dead_connections() returns empty list when all connections are active, Test _find_dead_connections() skips connections not in active_websockets., Test _find_dead_connections() raises ConnectionError when websocket is None., Test _find_dead_connections() finds dead connections., test_find_dead_connections_all_active() (+4 more)

### Community 727 - "check_invites.py"
Cohesion: 0.33
Nodes (4): Any, Called whenever state machine enters a new state.          Logs state transition, Get connection statistics.          Returns:             Dictionary with connect, State

### Community 728 - "verify_migration.py"
Cohesion: 0.15
Nodes (22): _check_foreign_keys(), _check_null_values(), _check_table_exists(), main(), _print_json_validation_results(), _print_sample_data(), _print_verification_summary(), Connection (+14 more)

### Community 729 - "run-vitest.js"
Cohesion: 0.25
Nodes (7): args, clientRoot, __dirname, env, __filename, vitest, vitestBin

### Community 730 - "MotdInterstitialScreen.tsx"
Cohesion: 0.36
Nodes (4): MotdContent(), MOTD_BUTTON_STYLE, MotdInterstitialScreen(), MotdInterstitialScreenProps

### Community 731 - "usePerformanceMonitor.ts"
Cohesion: 0.32
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 732 - "holidays.schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, minItems, type, $id, holidays, properties, holidays, required (+3 more)

### Community 733 - "npc_schedules.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 734 - "1. Enhanced ChatPanel (New Chat Input Panel)"
Cohesion: 0.25
Nodes (8): 1. Enhanced ChatPanel (New Chat Input Panel), 2. Renamed Game Log Panel (Formerly ChatPanel), ChatPanel Layout Structure, Enhanced ChatPanel Interface, Game Log Panel Layout Structure, New Features to Add, Proposed Changes, Purpose and Functionality

### Community 735 - "Implementation Phases"
Cohesion: 0.25
Nodes (8): 1.1 Enhance CircuitBreaker Class, 1.2 Create CircuitBreaker Manager, 1.3 Add Configuration Support, 5.1 Authentication Operations, 5.2 Rate Limiting Integration, Implementation Phases, Phase 1: Core Infrastructure Enhancement, Phase 5: Authentication and Security

### Community 736 - "database"
Cohesion: 0.05
Nodes (38): get_subject_manager_dependency(), Dependency function to inject NATSSubjectManager.      Returns:         Global N, Initialize combat event publisher.          Args:             nats_service: NATS, NATSSubjectManager, Any, Build a NATS subject from a pattern and parameters.          Args:             p, Ensure pattern exists in registry.          Args:             pattern_name: Name, Ensure all required parameters are provided.          Args:             pattern_ (+30 more)

### Community 737 - "enum"
Cohesion: 0.25
Nodes (8): catholic, islamic, jewish, mythos, neo_pagan, tradition, enum, type

### Community 738 - "alias"
Cohesion: 0.25
Nodes (8): command, additionalProperties, description, required, type, $defs, alias, name

### Community 739 - "enum"
Cohesion: 0.25
Nodes (8): Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, enum

### Community 740 - "Who Command Enhancement"
Cohesion: 0.67
Nodes (3): Who Command Name Filtering, Who Command Enhancement, Who Command Implementation Tasks

### Community 741 - "holiday.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 742 - "test_quality_fragmentation_guard.py"
Cohesion: 0.21
Nodes (23): ChangedFile, scan_changed_files(), _ChangedFile, _load_guard_module(), _load_trends_module(), Path, Protocol, _QualityGuardModule (+15 more)

### Community 743 - "E2E Tests Playwright"
Cohesion: 0.22
Nodes (10): Playwright E2E Runtime Tests, ArkanWolfshade E2E Account, E2E Tests Playwright, Ithaqua E2E Account, mythos_e2e Database, Runtime Auth Isolation, Playwright storageState Session Sharing, E2E Login Timeout Issue (+2 more)

### Community 744 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 745 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 746 - "schedule.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 747 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 748 - "handle_emote_command"
Cohesion: 0.23
Nodes (3): UseRoomMapDataOptions, RoomMapEditorProps, useRoomMapDataMock

### Community 749 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 750 - "router.py"
Cohesion: 0.05
Nodes (43): Unit tests for NPC admin command handlers.  Tests the NPC admin command function, Test validate_npc_admin_permission() when player is not admin., Test validate_npc_admin_permission() when player is admin., Test handle_npc_create_command() with no arguments., Test handle_npc_list_command() lists NPCs., Test handle_npc_delete_command() with no arguments., Test handle_npc_create_command() with invalid NPC type., Test handle_npc_create_command() when database is not available. (+35 more)

### Community 751 - "validate.mjs"
Cohesion: 0.32
Nodes (7): ajv, __dirname, __filename, loadJson(), main(), root, validateFile()

### Community 752 - "calculate_notification_times"
Cohesion: 0.17
Nodes (7): CombatMessages, Any, Generate combat start messages for all room occupants.          Args:, Generate combat end messages for all room occupants.          Args:, Validate NPC message templates against the schema.          Args:             me, Generate an attack message based on perspective and NPC configuration., Generate a death message for an NPC.          Args:             npc_name: Name o

### Community 753 - "ApplicationContainer"
Cohesion: 0.40
Nodes (6): ApplicationContainer, Application Container Analysis, Domain Container Bundles, Container Initialization Phases, Bounded Contexts, Service Boundaries

### Community 755 - "get_shutdown_blocking_message"
Cohesion: 0.33
Nodes (3): Despawn NPC with defensive error handling.          Args:             npc_id: ID, Despawn an NPC.          Args:             npc_id: ID of the NPC to despawn, Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.

### Community 756 - "Client Layout Baseline"
Cohesion: 0.10
Nodes (20): StatusPanel, Chat Panel, Client Layout Baseline, Commands Panel, File Locations, Game Log Panel, Header Configuration, Key Implementation Details (+12 more)

### Community 758 - "reset_config"
Cohesion: 0.26
Nodes (12): _DropResolved, _drop_finish_after_persist(), _drop_parsed_quantity_or_error(), _drop_quantity_bounds_or_error(), _drop_quantity_or_error(), _drop_resolve_stack_or_error(), _drop_slot_index_or_error(), CommandResponse (+4 more)

### Community 759 - ".call"
Cohesion: 0.47
Nodes (4): Unit tests for inventory_service_helpers.get_shared_services., _request_with_persistence(), test_get_shared_services_initializes_and_reuses_singletons(), test_get_shared_services_raises_without_async_persistence()

### Community 760 - "Quest System Features"
Cohesion: 0.40
Nodes (5): Quest Design Principles, Quest System Features, Event-Driven Quest Progression, Quest Goal Types, Declarative YAML Quest Config

### Community 761 - "FieldInfo Type Checker Issues"
Cohesion: 0.10
Nodes (21): Quick Start E2E Tests, E2E Test Server Quick Start, Container-Based Test Fixtures, Test Modernization Plan, bcrypt PyO3 Fresh Session Limitation, Testing Guide, Alternative Approaches, ✅ Correct Pattern (No Pylint Errors) (+13 more)

### Community 762 - ".get_lifecycle_statistics"
Cohesion: 0.25
Nodes (4): Get overall lifecycle statistics.          Returns:             Dictionary co, Return counts of lifecycle records by current_state., Return counts of lifecycle records by NPC type string., Return (total_spawns, total_despawns, total_errors) across all lifecycle records

### Community 763 - ".from_dict"
Cohesion: 0.25
Nodes (8): _cleanup_failed_connection(), Cleanup connection on failure.      Args:         connection_id: The connection, Test _cleanup_failed_connection() handles None connection_id., Test _cleanup_failed_connection() cleans up connection., Test _cleanup_failed_connection() handles errors during cleanup., test_cleanup_failed_connection_error(), test_cleanup_failed_connection_none(), test_cleanup_failed_connection_success()

### Community 764 - "TestHandleSpecialCommandRouting"
Cohesion: 0.17
Nodes (12): format_player_entry(), Format a single player entry for the who command output.      Args:         play, Test format_player_entry() formats player entry., test_format_player_entry(), Test formatting basic player entry., Test formatting admin player entry., Test formatting player entry with missing attributes., Test format_player_entry() handles errors gracefully. (+4 more)

### Community 765 - "test_security_utils.py"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory.      Args:         filename: The, Unit tests for security utilities.  Tests path validation and file security func, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 766 - "TestEnsureAliasStorage"
Cohesion: 0.23
Nodes (12): _coerce_row_stats(), _defaulted_numerics(), _defaulted_strings(), _parse_equipped_safely(), Any, Player, Extract and coerce stats from row. Returns empty dict if not a dict., Parse equipped_json to dict. Returns empty dict on parse error or invalid type. (+4 more)

### Community 767 - "test_utility_commands_whoami.py"
Cohesion: 0.17
Nodes (7): CombatMessagingService, Generate thematic error messages for combat actions.          Args:, Service for generating combat messages.      This service creates thematic, pers, Initialize the combat messaging service., Unit tests for combat messaging service.  Tests the CombatMessagingService class, Create a CombatMessagingService instance for testing., Test CombatMessagingService initialization.

### Community 768 - "test_async_persistence_room_cache.py"
Cohesion: 0.03
Nodes (59): Unit tests for async persistence layer: load_room_cache_async, query_rooms, warm, Test get_user_by_username_case_insensitive when no session is yielded., Test get_professions when no session is yielded., Test get_players_batch with empty list., Test get_players_batch with actual players (UUID conversion)., Test _generate_room_id_from_zone_data when stable_id already has full path., Test _generate_room_id_from_zone_data when room ID needs generation., Test _generate_room_id_from_zone_data with None values. (+51 more)

### Community 769 - ".__call__"
Cohesion: 0.17
Nodes (11): mock_request(), Unit tests for grace period command blocking in unified command handler.  Tests, Create a mock request., Test _check_grace_period_block() blocks commands for grace period players., Test _check_grace_period_block() allows commands when player not in grace period, Test _check_grace_period_block() handles missing services gracefully., Test _check_grace_period_block() handles player not found gracefully., test_check_grace_period_block_allows_commands_when_not_in_grace_period() (+3 more)

### Community 770 - "test_async_persistence_room_loading.py"
Cohesion: 0.04
Nodes (51): Unit tests for async persistence layer: process_room_rows, process_exit_rows, bu, Test _process_exit_rows with stable_ids that already contain full hierarchical p, Test _process_exit_rows with stable_ids that need room ID generation., Test _process_exit_rows logs debug info for specific room., Test _build_room_objects successfully builds room objects., Test _process_room_rows with stable_id that already contains full hierarchical p, Test _build_room_objects handles non-dict attributes., Test _build_room_objects logs debug info for specific room. (+43 more)

### Community 771 - "test_combat_messaging_integration.py"
Cohesion: 0.25
Nodes (7): Unit tests for combat messaging integration.  Tests the CombatMessagingIntegrati, Test broadcast_player_mortally_wounded broadcasts message., Test CombatMessagingIntegration initialization without connection manager., Test _resolve_connection_manager_from_container handles errors., test_broadcast_player_mortally_wounded(), test_messaging_integration_init_no_connection_manager(), test_resolve_connection_manager_from_container_error()

### Community 772 - "fix_suppression_alignment.py"
Cohesion: 0.16
Nodes (21): add_pylint_suppression(), add_ruff_suppression(), _apply_fixes_to_line(), fix_file(), _group_fixes_by_line(), main(), parse_alignment_report(), _parse_file_line_pattern() (+13 more)

### Community 773 - "identify_critical_code.py"
Cohesion: 0.15
Nodes (21): analyze_file(), analyze_function(), calculate_complexity(), calculate_priority(), check_file_keywords(), check_function_keywords(), main(), process_ast_functions() (+13 more)

### Community 774 - "AdminActionsLogger"
Cohesion: 0.15
Nodes (13): AdminActionsLogger, Any, Path, Log a general admin command action.          Args:             admin_name: Name, Log permission check attempts.          Args:             player_name: Name of t, Write a log entry to the current log file.          Args:             log_entry:, Logger for admin actions with structured logging and file persistence.      Prov, Retrieve recent admin actions from the log files.          Args:             hou (+5 more)

### Community 775 - "test_error_logging.py"
Cohesion: 0.25
Nodes (7): Unit tests for error_logging utilities.  Tests error logging helper functions., Test create_error_context() creates error context., Test create_error_context() can include metadata., Test error context to_dict() method., test_create_error_context(), test_create_error_context_with_metadata(), test_error_context_to_dict()

### Community 776 - "optimized_validate_command_content"
Cohesion: 0.25
Nodes (8): Test validating empty command content., Test validating valid command content., Test validating command content with injection pattern., test_optimized_validate_command_content_empty(), test_optimized_validate_command_content_injection(), test_optimized_validate_command_content_valid(), optimized_validate_command_content(), Optimized validation for command content fields.      Args:         value: The c

### Community 777 - "optimized_validate_reason_content"
Cohesion: 0.25
Nodes (8): Test validating empty reason content., Test validating valid reason content., Test validating reason content with injection pattern., test_optimized_validate_reason_content_empty(), test_optimized_validate_reason_content_injection(), test_optimized_validate_reason_content_valid(), optimized_validate_reason_content(), Optimized validation for reason content fields.      Args:         value: The re

### Community 778 - "optimized_validate_pose_content"
Cohesion: 0.25
Nodes (8): Test validating empty pose content., Test validating valid pose content., Test validating pose content with injection pattern., test_optimized_validate_pose_content_empty(), test_optimized_validate_pose_content_injection(), test_optimized_validate_pose_content_valid(), optimized_validate_pose_content(), Optimized validation for pose content fields.      Args:         value: The pose

### Community 779 - "optimized_validate_filter_name"
Cohesion: 0.25
Nodes (8): Test validating empty filter name., Test validating valid filter name., Test validating invalid filter name., test_optimized_validate_filter_name_empty(), test_optimized_validate_filter_name_invalid(), test_optimized_validate_filter_name_valid(), optimized_validate_filter_name(), Optimized validation for filter name fields.      Args:         value: The filte

### Community 780 - "optimized_validate_target_player"
Cohesion: 0.25
Nodes (8): Test validating empty target player name., Test validating valid target player name., Test validating invalid target player name., test_optimized_validate_target_player_empty(), test_optimized_validate_target_player_invalid(), test_optimized_validate_target_player_valid(), optimized_validate_target_player(), Optimized validation for target player fields.      Args:         value: The tar

### Community 781 - "optimized_validate_help_topic"
Cohesion: 0.25
Nodes (8): Test validating empty help topic., Test validating valid help topic., Test validating invalid help topic., test_optimized_validate_help_topic_empty(), test_optimized_validate_help_topic_invalid(), test_optimized_validate_help_topic_valid(), optimized_validate_help_topic(), Optimized validation for help topic fields.      Args:         value: The help t

### Community 782 - "ValidationError"
Cohesion: 0.04
Nodes (61): Unit tests for communication command factories.  Tests the CommunicationCommandF, Test create_me_command() creates MeCommand., Test create_me_command() raises error with no args., Test create_pose_command() creates PoseCommand., Test create_pose_command() allows no args (sets pose to None)., Test create_channel_command() creates ChannelCommand., Test create_channel_command() handles 'default' action., Test create_channel_command() raises error with no args. (+53 more)

### Community 783 - "optimized_comprehensive_sanitize_input"
Cohesion: 0.25
Nodes (8): Test comprehensive sanitization of empty string., Test comprehensive sanitization of normal text., Test that optimized comprehensive sanitization normalizes newlines to spaces., test_optimized_comprehensive_sanitize_input_empty(), test_optimized_comprehensive_sanitize_input_normal(), test_optimized_comprehensive_sanitize_input_normalizes_newlines(), optimized_comprehensive_sanitize_input(), Optimized comprehensive input sanitization.      Args:         text: Raw input t

### Community 784 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 785 - "properties"
Cohesion: 0.25
Nodes (8): description, enum, type, indoors, outdoors, underwater, properties, environment

### Community 786 - "useGridLayout.ts"
Cohesion: 0.33
Nodes (5): layoutConfig, PanelState, STORAGE_KEYS, useGridLayout(), UseGridLayoutReturn

### Community 787 - "MythosMUD"
Cohesion: 0.29
Nodes (5): Geography Overview, Engineering memory, MythosMUD, Sources, World

### Community 788 - "Chat Panel Separation Specification"
Cohesion: 0.29
Nodes (6): Chat Panel Separation Specification, Conclusion, Current Integration Points, Current State Analysis, Existing Structure, Overview

### Community 790 - "Architecture Remediation Implementation Summary"
Cohesion: 0.29
Nodes (6): Architecture Remediation Implementation Summary, Before vs After Comparison, Conclusion, Executive Summary, Quality Attributes Assessment, Test Integration Status

### Community 791 - "__init__.py"
Cohesion: 0.03
Nodes (111): _equip_stack_from_inventory_index(), Equipment-related helper functions for inventory commands., Resolve slot from command data for unequip command., Deep-copy inventory stack at index and normalize slot_type., resolve_unequip_slot(), _try_resolve_unequip_by_search(), _try_resolve_unequip_slot_key(), _unequip_usage_missing_slot() (+103 more)

### Community 792 - "Bug Prevention Testing Strategy"
Cohesion: 0.29
Nodes (6): Bug Prevention Testing Strategy, Conclusion, Manual Test Execution, Overview, Running All Tests, Test Execution

### Community 793 - "record_edited_file.py"
Cohesion: 0.15
Nodes (20): _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path(), Any (+12 more)

### Community 794 - "Command Handler Patterns"
Cohesion: 0.29
Nodes (7): Command Handler Patterns, Command Models Reference, Pydantic Command Models, Command Security Guide, Command Role-Based Access Control, Command Testing Guide, Command Test-Driven Development

### Community 795 - "Bugs Addressed"
Cohesion: 0.29
Nodes (7): 1. **"twibble" Emote Bug**, 2. **Self-Message Exclusion Bug**, 3. **Chat Buffer Persistence Bug**, 4. **Event Storm Bug**, 5. **Connection Timeout Bug**, 6. **UUID Serialization Bug**, Bugs Addressed

### Community 796 - "4. **Client-Side Tests** (`client/src/components/GameTerminalWithPanels.test.tsx`)"
Cohesion: 0.29
Nodes (7): 4. **Client-Side Tests** (`client/src/components/GameTerminalWithPanels.test.tsx`), Chat Buffer Persistence Bug Tests, Command Processing Integration Tests, Connection State Management Tests, Message Formatting and Display Tests, Room Event Message Display Tests, Self-Message Exclusion on Client Side

### Community 797 - "Argon2 Implementation Plan"
Cohesion: 0.29
Nodes (6): Argon2 Implementation Plan, Current State Analysis, Existing Authentication System, Files Requiring Updates, Overview, References

### Community 798 - "Playwright MCP Primary Testing Tool"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 799 - "enum"
Cohesion: 0.29
Nodes (7): autumn, spring, summer, winter, season, enum, type

### Community 800 - "Any"
Cohesion: 0.17
Nodes (7): Test _prepare_command_for_processing function., Test _prepare_command_for_processing returns rate limit result when rate limited, Test _prepare_command_for_processing returns validation result when validation f, Test _prepare_command_for_processing handles empty command after cleaning., Test _prepare_command_for_processing handles empty command after normalization., Test _prepare_command_for_processing successfully prepares command., TestPrepareCommandForProcessing

### Community 801 - "Any"
Cohesion: 0.17
Nodes (7): Test _check_grace_period_block function., Test _check_grace_period_block returns None when no connection manager., Test _check_grace_period_block returns None when no player service., Test _check_grace_period_block returns None when player not found., Test _check_grace_period_block returns block result when player in grace period., Test _check_grace_period_block returns None on error., TestCheckGracePeriodBlock

### Community 802 - "test_metrics.py"
Cohesion: 0.03
Nodes (59): Any, Get current metrics summary.          Returns:             Dictionary containing, Calculate percentile from list of times.          Args:             times: List, Reset all metrics to zero., Performance metrics for NATS Subject Manager operations.      Tracks validation, Initialize metrics collection., Record a validation operation.          Args:             duration: Time taken i, Record a build operation.          Args:             duration: Time taken in sec (+51 more)

### Community 803 - "._get_player_mute_file"
Cohesion: 0.40
Nodes (5): 3. Systematic Investigation Approach, For Authentication Failures, For Database-Related Failures, For Game Logic Failures, For WebSocket Failures

### Community 804 - "subscribe_to_room_events_impl"
Cohesion: 0.17
Nodes (14): Event subscription helpers for connection manager.  This module provides helper, Unsubscribe from room movement events., unsubscribe_from_room_events_impl(), Unit tests for connection event helpers.  Tests the connection_event_helpers mod, Test unsubscribe_from_room_events_impl() handles AttributeError., Test subscribe_to_room_events_impl() handles DatabaseError., Test unsubscribe_from_room_events_impl() successfully unsubscribes from events., Test unsubscribe_from_room_events_impl() handles missing event bus. (+6 more)

### Community 805 - "DatabaseError"
Cohesion: 0.01
Nodes (237): fetch_professions(), fetch_user_by_username_case_insensitive(), Profession, Direct async SQL queries used by AsyncPersistenceLayer.  Extracted to keep async, Get a user by username (case-insensitive).      MULTI-CHARACTER: Usernames are s, Get all available professions using SQLAlchemy ORM., Async persistence layer for MythosMUD.  This module provides an async version of, Initialize the async persistence layer.          This facade delegates to focuse (+229 more)

### Community 806 - "generate_unique_codes"
Cohesion: 0.06
Nodes (43): get_config(), _is_test_mode(), Reset the configuration cache.      In test mode, this is a no-op since get_conf, Detect if running in test environment.      Uses multiple detection methods to r, Get application configuration (singleton in production, fresh in tests).      In, reset_config(), Reset config singleton before and after each test.      In test mode, get_config, reset_config_singleton() (+35 more)

### Community 807 - "enum"
Cohesion: 0.29
Nodes (7): description, enum, type, indoors, outdoors, underwater, environment

### Community 808 - "audit_suppressions.py"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 809 - "fix_markdown_line_length.py"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file.      Returns:         (changed, lines (+12 more)

### Community 810 - "populate_npc_sample_data.py"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data.      Args:         database (+12 more)

### Community 811 - "unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 812 - "MagicPointsMeter.tsx"
Cohesion: 0.40
Nodes (4): database, Test database operation logging., Simulate database execute., test_database_logging()

### Community 813 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Python Import Fix, Template 2: Python Import Sorting Fix, Template 3: Python Line Length Fix, Template 4: React Hook Dependency Fix, Template 5: TypeScript Unused Variable Fix

### Community 814 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Python Import Fix, Template 2: Python Import Sorting Fix, Template 3: Python Line Length Fix, Template 4: React Hook Dependency Fix, Template 5: TypeScript Unused Variable Fix

### Community 815 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Add Missing Type Imports, Template 2: Fix Function Signature, Template 3: Handle Optional Values, Template 4: Fix Type Narrowing, Template 5: Add Generic Type Parameters

### Community 816 - "Common Test Failure Categories"
Cohesion: 0.33
Nodes (6): 1. Database Test Failures, 2. Authentication Test Failures, 3. WebSocket Test Failures, 4. Game Logic Test Failures, 5. Integration Test Failures, Common Test Failure Categories

### Community 817 - "FAILURE PATTERN RECOGNITION"
Cohesion: 0.33
Nodes (6): A. Database-Related Failures, B. Authentication/Security Failures, C. WebSocket/Connection Failures, D. Game Logic Failures, E. Integration Test Failures, FAILURE PATTERN RECOGNITION

### Community 818 - "scripts"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 819 - "MUD Disconnect Grace Period & Rest Command: Industry Comparison"
Cohesion: 0.33
Nodes (5): 11. Missing Features from Other MUDs, Executive Summary, Features We're NOT Implementing (but exist elsewhere), MUD Disconnect Grace Period & Rest Command: Industry Comparison, Questions for Discussion

### Community 820 - "compilerOptions"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 821 - "MythosMUD Obsidian Vault"
Cohesion: 0.33
Nodes (5): Graphify, Layout, MythosMUD Obsidian Vault, Quick start, Recommended Obsidian settings

### Community 822 - "items"
Cohesion: 0.25
Nodes (8): items, type, uniqueItems, items, additionalProperties, minLength, type, bonus_tags

### Community 823 - "sanitizeChatMessageForState"
Cohesion: 0.17
Nodes (11): Unit tests for who command helper functions.  Tests the helper functions in who_, Test filter_players_by_name() filters players by name., Test filter_players_by_name() returns empty list when no matches., Test filter_players_by_name() returns all players when filter is empty., Test format_player_location() formats valid room ID., Test format_player_entry() includes admin indicator., test_filter_players_by_name_empty_filter(), test_filter_players_by_name_found() (+3 more)

### Community 824 - "items"
Cohesion: 0.33
Nodes (6): additionalProperties, properties, schedules, items, minItems, type

### Community 825 - "Architecture Decision Records (ADRs)"
Cohesion: 0.33
Nodes (6): ADR-001: Dependency Injection Container, ADR-002: EventBus as Single Source of Truth, ADR-003: MessageBroker Abstraction, ADR-004: Direct Model Relationships, ADR-005: Domain Layer Introduction, Architecture Decision Records (ADRs)

### Community 826 - "Best Practices Implemented"
Cohesion: 0.33
Nodes (6): 1. **Test-Driven Development**, 2. **Comprehensive Mocking**, 3. **Async Testing**, 4. **Edge Case Coverage**, 5. **Real-World Scenarios**, Best Practices Implemented

### Community 827 - "2. **Unresolved Bug Tests** (`server/tests/test_unresolved_bugs.py`)"
Cohesion: 0.33
Nodes (6): 2. **Unresolved Bug Tests** (`server/tests/test_unresolved_bugs.py`), Chat Buffer Persistence Tests, Event Ordering and Timing Tests, Self-Message Exclusion Edge Cases, UUID Serialization Edge Cases, WebSocket Message Delivery Tests

### Community 828 - "Implementation Details"
Cohesion: 0.33
Nodes (6): CircuitBreaker Manager, Database Operations, Enhanced CircuitBreaker Class, Implementation Details, Integration Examples, NATS Operations

### Community 829 - "Problems Identified"
Cohesion: 0.33
Nodes (6): 🔴 Critical Issues (Must Fix), 🔍 Current State Analysis, 🟡 Important Issues (Should Fix), 🟢 Minor Issues (Nice to Fix), Problems Identified, Strengths to Preserve

### Community 830 - "Purpose"
Cohesion: 0.33
Nodes (5): Administrative Summon Etiquette, Item System Observability Runbook, Migration & Durability Recovery, Purpose, Seed Regeneration Checklist

### Community 831 - "name"
Cohesion: 0.33
Nodes (6): description, maxLength, minLength, pattern, type, name

### Community 832 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 833 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 834 - "PublishError"
Cohesion: 0.20
Nodes (7): Protocol, Debug log for context enrichment (best-effort, must not fail)., Populate player_in_range, enemy_nearby, and target_id for attack rules., Protocol for persistence with get_room_by_id., Return the room object for the given room_id, or None if not found., Get player_in_range, enemy_nearby, and target_id from persistence.         Retu, _RoomPersistence

### Community 835 - "test_connection_establishment.py"
Cohesion: 0.20
Nodes (10): Get player and setup room subscription.      Args:         player_id: The player, _setup_player_and_room(), Test _setup_player_and_room() successfully sets up player and room., Test _setup_player_and_room() returns False when player not found., Test _setup_player_and_room() handles no persistence., Test _setup_player_and_room() handles player with no room_id., test_setup_player_and_room_no_persistence(), test_setup_player_and_room_no_player() (+2 more)

### Community 836 - "LoggingPatternLinter"
Cohesion: 0.11
Nodes (15): FormattedValue, lint_file(), LoggingPatternLinter, main(), Call, Import, ImportFrom, Path (+7 more)

### Community 837 - "SubscribeError"
Cohesion: 0.40
Nodes (5): integer, minimum, type, null, durability

### Community 838 - "Arkham City (MOTD Zone)"
Cohesion: 0.18
Nodes (14): Arkham City Graph PNG, Arkham City PDF Map, Arkham City (MOTD Zone), Welcome to the Dreamlands, Innsmouth (MOTD Zone), Katmandu, MythosMUD Message of the Day, The Yellow Sign (+6 more)

### Community 839 - "CastingStateManager"
Cohesion: 0.18
Nodes (6): _cfg_bool(), Calculate weight for an exit based on distance from spawn.          Args:, Calculate weights for all exits.          Args:             valid_exits: Dict, Select exit based on weighted probabilities.          Args:             exit_, Select an exit using weighted random selection favoring exits closer to spawn ro, Calculate approximate distance between two rooms.          This is a simplifie

### Community 840 - "graceful_degradation"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add FastAPI Users columns.      Args:         database_ur

### Community 841 - "CommandRateLimiter"
Cohesion: 0.10
Nodes (12): CommandRateLimiter, Any, datetime, Get number of commands player can still execute.          Args:             play, Reset rate limit for a specific player.          Useful for admin commands or wh, Reset rate limit for all players.          Clears all accumulated timestamp data, Get system-wide rate limiting statistics.          Returns:             Dictiona, Remove timestamp data for players who haven't been active recently.          Pre (+4 more)

### Community 842 - ".get_stat_requirements"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add hashed_password column.      Args:         database_u

### Community 843 - "add_damage_threat"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add used_by_user_id column.      Args:         database_u

### Community 844 - "processing.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Apply the migration to rename columns.      Args:         database_url: PostgreS, Main entry point for the migration script.

### Community 845 - ".refresh_configuration"
Cohesion: 0.33
Nodes (4): Refresh configuration from source., Clear configuration cache., Refresh combat configuration by clearing cache and reloading., refresh_combat_configuration()

### Community 846 - "._despawn_npc"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to rename used back to is_active.      Args:         databas

### Community 847 - "TestCheckRateLimit"
Cohesion: 0.33
Nodes (4): Test _check_rate_limit function., Test _check_rate_limit returns None when allowed., Test _check_rate_limit returns result when blocked., TestCheckRateLimit

### Community 848 - "test_inventory_service_helpers.py"
Cohesion: 0.12
Nodes (31): _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), normalize_inventory_slots(), InventoryStack, Player, Find the equipped slot and item after equipping., Handle wearable container creation when equipping a container item. (+23 more)

### Community 849 - "UpgradeImplementationPlan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 850 - "DraggablePanelResizeHandles.tsx"
Cohesion: 0.24
Nodes (7): NPCQueryMixin, Any, AsyncSession, Mixin providing NPC query operations., Get NPC definitions by type., Get NPC definitions by sub-zone., Get system-wide NPC statistics.

### Community 851 - "ConnectionManager"
Cohesion: 0.50
Nodes (4): ConnectionManager, NATS Message Handler, Room Broadcasts, WebSocket API /api/ws

### Community 852 - "ConnectionPanel.tsx"
Cohesion: 0.50
Nodes (3): ConnectionPanel(), ConnectionPanelProps, localStorageMock

### Community 853 - "global-teardown.ts"
Cohesion: 0.40
Nodes (3): __dirname, __filename, projectRoot

### Community 854 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.20
Nodes (6): Test _process_alias_expansion function., Test _process_alias_expansion returns None when no alias storage., Test _process_alias_expansion returns None when alias not found., Test _process_alias_expansion returns error for unsafe alias., Test _process_alias_expansion returns error for invalid expanded command., TestProcessAliasExpansion

### Community 855 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.20
Nodes (6): Tests for _handle_special_command_routing function., Test _handle_special_command_routing processes alias commands., Test _handle_special_command_routing returns error when alias_storage is None., Test _handle_special_command_routing converts single-word emotes., Test _handle_special_command_routing returns None for normal commands., TestHandleSpecialCommandRouting

### Community 856 - "Phase 2: Categorize and Prioritize Mypy Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Mypy Issues

### Community 857 - "Phase 5: Fix Implementation Patterns"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL FIXES - Import and Name Errors, 🟡 HIGH PRIORITY FIXES - Type Errors, 🔵 LOW PRIORITY FIXES - Type Precision, 🟢 MEDIUM PRIORITY FIXES - Type Refinement, Phase 5: Fix Implementation Patterns

### Community 858 - "4. Common Fix Patterns"
Cohesion: 0.40
Nodes (5): 4. Common Fix Patterns, Authentication Test Patterns, Database Test Patterns, Game Logic Test Patterns, WebSocket Test Patterns

### Community 859 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 860 - "UI/UX Considerations"
Cohesion: 0.40
Nodes (5): 1. Visual Distinction, 2. Panel Positioning, 3. Responsive Design, 4. Accessibility, UI/UX Considerations

### Community 861 - "3. Simplified CommandPanel"
Cohesion: 0.40
Nodes (5): 3. Simplified CommandPanel, CommandPanel Layout Structure, Features to Keep, Features to Remove, Simplified CommandPanel Interface

### Community 862 - "Implementation Phases"
Cohesion: 0.40
Nodes (5): Implementation Phases, Phase 1: Core Separation, Phase 2: Enhanced Features, Phase 3: Polish and Optimization, Phase 4: Testing and Refinement

### Community 863 - "Architecture Patterns Implemented"
Cohesion: 0.40
Nodes (5): 1. Dependency Injection Container, 2. Hexagonal Architecture (Ports & Adapters), 3. Event-Driven Architecture, 4. Clean Architecture Principles, Architecture Patterns Implemented

### Community 864 - "Phase 3: Architecture Modernization (COMPLETED ✓)"
Cohesion: 0.40
Nodes (5): 3.1 Circular Dependency Elimination ✓, 3.2 TypeScript Path Aliases ✓, 3.3 Domain Layer Structure ✓, 3.4 Configuration Simplification ✓, Phase 3: Architecture Modernization (COMPLETED ✓)

### Community 865 - "Future Bug Prevention"
Cohesion: 0.40
Nodes (5): 1. **Continuous Integration**, 2. **Monitoring and Alerting**, 3. **Code Review Guidelines**, 4. **Documentation**, Future Bug Prevention

### Community 866 - "✅ Implementation Timeline - COMPLETED"
Cohesion: 0.40
Nodes (5): ✅ Implementation Timeline - COMPLETED, ✅ Week 1: Foundation - COMPLETED, ✅ Week 2: Integration - COMPLETED, ✅ Week 3: Validation - COMPLETED, ✅ Week 4: Deployment - COMPLETED

### Community 867 - "🚀 **DEPLOYMENT PHASE - COMPLETED SUCCESSFULLY**"
Cohesion: 0.40
Nodes (5): 🚀 **DEPLOYMENT PHASE - COMPLETED SUCCESSFULLY**, **Deployment Summary (Current Session)**, **Quality Assurance:**, **Security Status:**, **What Was Deployed:**

### Community 868 - "🏆 **MAJOR ACCOMPLISHMENT: Pydantic + Click Command Validation System**"
Cohesion: 0.40
Nodes (5): **Files Created:**, 🏆 **MAJOR ACCOMPLISHMENT: Pydantic + Click Command Validation System**, **Quality Assurance:**, **Security Improvements:**, **What Was Implemented:**

### Community 869 - "🧪 Testing Strategy"
Cohesion: 0.40
Nodes (5): Integration Testing, Regression Testing, Security Testing, 🧪 Testing Strategy, Unit Testing

### Community 870 - "command"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, command

### Community 871 - "items"
Cohesion: 0.40
Nodes (5): items, type, pattern, type, bonus_tags

### Community 872 - "item_prototype.schema.json"
Cohesion: 0.40
Nodes (4): additionalProperties, $schema, title, type

### Community 875 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 876 - "2025_01_XX_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID.      PostgreSQL can directly cas, Convert players.player_id from UUID back to VARCHAR.      This is a downgrade pa, upgrade()

### Community 877 - "2025_11_21_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID.      PostgreSQL can directly cas, Convert players.player_id from UUID back to VARCHAR.      This is a downgrade pa, upgrade()

### Community 879 - "2025_11_25_normalize_container_schema.py"
Cohesion: 0.40
Nodes (4): downgrade(), Normalize container schema with proper relational structure., Revert to denormalized schema with items_json., upgrade()

### Community 881 - "2025_11_25_remove_get_container_contents_json_procedure.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove deprecated stored procedure., Restore deprecated stored procedure., upgrade()

### Community 882 - "2025_11_25_remove_items_json_column.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove items_json column from containers table., Restore items_json column (data will be empty)., upgrade()

### Community 883 - "2025_11_26_ensure_item_instance_foreign_keys.py"
Cohesion: 0.40
Nodes (4): downgrade(), Ensure foreign key constraints exist for item_instances., This migration only ensures constraints exist - no downgrade needed., upgrade()

### Community 884 - "2026_02_09_add_player_effects_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_effects table and indexes (ADR-009 effects system)., Drop player_effects table and indexes., upgrade()

### Community 885 - "2026_02_18_add_player_skills_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_skills table if not exists (matches db/migrations/025)., Drop player_skills table., upgrade()

### Community 886 - "2026_02_18_add_profession_modifiers_columns.py"
Cohesion: 0.40
Nodes (4): downgrade(), Add stat_modifiers and skill_modifiers columns to professions table., Remove stat_modifiers and skill_modifiers columns from professions table., upgrade()

### Community 887 - "2026_02_19_add_quest_tables.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create quest_definitions, quest_instances, quest_offers tables., Drop quest tables (order matters for FKs)., upgrade()

### Community 888 - "2026_02_19_seed_quest_leave_the_tutorial.py"
Cohesion: 0.40
Nodes (4): downgrade(), Insert leave_the_tutorial quest and quest_offers row., Remove seed quest and its offer., upgrade()

### Community 889 - "2026_02_26_add_arena_zone_type.py"
Cohesion: 0.40
Nodes (4): downgrade(), Allow zone_type 'arena' in zones CHECK., Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)., upgrade()

### Community 890 - "MessageBroker"
Cohesion: 0.12
Nodes (11): MessageBroker, Any, Protocol, Send a request and wait for a reply (request-reply pattern).          Args:, Protocol defining the message broker interface.      This abstract interface all, Connect to the message broker.          Returns:             bool: True if conne, Disconnect from the message broker.          Closes all subscriptions and releas, Check if connected to the message broker.          Returns:             bool: Tr (+3 more)

### Community 891 - "rename_players_to_population.py"
Cohesion: 0.40
Nodes (4): downgrade(), Rename columns from min_players/max_players to min_population/max_population., Revert column names back to min_players/max_players., upgrade()

### Community 892 - "PostgresCursor"
Cohesion: 0.13
Nodes (11): PostgresCursor, PostgreSQL cursor wrapper for query result access., Test PostgresCursor class., Create a mock psycopg2 cursor., Test PostgresCursor initialization., Test PostgresCursor.fetchone() with row., Test PostgresCursor.fetchone() with None., Test PostgresCursor.fetchall() with rows. (+3 more)

### Community 893 - "_find_uvicorn_processes"
Cohesion: 0.50
Nodes (4): deprecated_api_logging(), process_request(), Demonstrate DEPRECATED API logging patterns., Simulate request processing.

### Community 894 - ".get_stats"
Cohesion: 0.50
Nodes (4): async_operation(), Test logging in async functions., Simulate async operation., test_async_logging()

### Community 895 - "DomainError"
Cohesion: 0.40
Nodes (4): DomainError, Exception, Domain-specific exceptions for MythosMUD.  These exceptions represent business r, Base exception for all domain errors.

### Community 896 - "add_fastapi_users_columns.py"
Cohesion: 0.50
Nodes (4): Test logging error handling., Simulate risky operation that raises exception., risky_operation(), test_logging_error_handling()

### Community 897 - "add_hashed_password_column.py"
Cohesion: 0.50
Nodes (4): _build_collect_n_progress(), _collect_goal_prototype_id(), Return collect_n prototype id from goal target or config., Recompute collect_n goal counters from holdings into a progress dict.

### Community 900 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 903 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 904 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 905 - "weather_patterns"
Cohesion: 0.40
Nodes (5): type, weather_patterns, description, items, type

### Community 906 - "ChatExportDialog.tsx"
Cohesion: 0.67
Nodes (3): ChatExportDialog(), ChatExportDialogProps, collectFocusableElements()

### Community 909 - "lifespan_shutdown.py"
Cohesion: 0.20
Nodes (6): Test _validate_command_basics function., Test _validate_command_basics returns result for empty command., Test _validate_command_basics returns result for command too long., Test _validate_command_basics returns result for invalid command content., Test _validate_command_basics returns None for valid command., TestValidateCommandBasics

### Community 910 - "🔄 COMMON SCENARIOS AND SOLUTIONS"
Cohesion: 0.50
Nodes (4): 🔄 COMMON SCENARIOS AND SOLUTIONS, Scenario 1: Third-Party Library Without Stubs, Scenario 2: Complex Union Types, Scenario 3: Recursive Types

### Community 911 - "🔍 DEBUGGING GUIDE"
Cohesion: 0.50
Nodes (4): 🔍 DEBUGGING GUIDE, If Mypy Command Fails, If Specific Issues Persist, Understanding Type Checker Behavior

### Community 912 - "🚀 OPTIMIZATION TIPS"
Cohesion: 0.50
Nodes (4): For Large Codebases, For Performance, 🚀 OPTIMIZATION TIPS, Type Annotation Strategies

### Community 913 - "7. Common Test Failure Solutions"
Cohesion: 0.50
Nodes (4): 7. Common Test Failure Solutions, Authentication Test Issues, Database Connection Issues, WebSocket Test Issues

### Community 914 - "9. Test Maintenance Best Practices"
Cohesion: 0.50
Nodes (4): 9. Test Maintenance Best Practices, Performance Considerations, Test Data Management, Test Isolation

### Community 915 - "10. Grace Period Persistence"
Cohesion: 0.50
Nodes (4): 10. Grace Period Persistence, Gap Analysis, Industry Practices, Our Plan

### Community 916 - "1. Disconnect Grace Period Duration"
Cohesion: 0.50
Nodes (4): 1. Disconnect Grace Period Duration, Gap Analysis, Industry Practices, Our Plan

### Community 918 - "2. Auto-Attack During Grace Period"
Cohesion: 0.50
Nodes (4): 2. Auto-Attack During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 919 - "3. Grace Period Visibility & Messaging"
Cohesion: 0.50
Nodes (4): 3. Grace Period Visibility & Messaging, Gap Analysis, Industry Practices, Our Plan

### Community 920 - "4. Rest/Quit Command During Combat"
Cohesion: 0.50
Nodes (4): 4. Rest/Quit Command During Combat, Gap Analysis, Industry Practices, Our Plan

### Community 921 - "5. Rest Command Countdown Duration"
Cohesion: 0.50
Nodes (4): 5. Rest Command Countdown Duration, Gap Analysis, Industry Practices, Our Plan

### Community 923 - "6. Rest Location (Inn/Hotel) Behavior"
Cohesion: 0.50
Nodes (4): 6. Rest Location (Inn/Hotel) Behavior, Gap Analysis, Industry Practices, Our Plan

### Community 924 - "7. Reconnection During Grace Period"
Cohesion: 0.50
Nodes (4): 7. Reconnection During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 925 - "8. Grace Period After Intentional Disconnect"
Cohesion: 0.50
Nodes (4): 8. Grace Period After Intentional Disconnect, Gap Analysis, Industry Practices, Our Plan

### Community 926 - "MessageBroadcaster"
Cohesion: 0.03
Nodes (89): initialize_connection_cleaner(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging(), initialize_room_event_handler(), Any, Initialization helpers for connection manager.  This module provides helper func (+81 more)

### Community 927 - "9. Command Blocking During Grace Period"
Cohesion: 0.50
Nodes (4): 9. Command Blocking During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 928 - "Recommendations Summary"
Cohesion: 0.50
Nodes (4): High Priority Decisions, Low Priority (Future Considerations), Medium Priority Enhancements, Recommendations Summary

### Community 929 - "DML Migrations"
Cohesion: 0.50
Nodes (3): DML Migrations, Historical CSV files, Migration files

### Community 931 - "Code Graph Entry"
Cohesion: 0.50
Nodes (3): Code Graph Entry, Live exploration (preferred for "how does X work?"), Synced community wiki (read-only dump)

### Community 932 - "DML Migrations Apply Paths"
Cohesion: 0.50
Nodes (3): Agent rule, DML Migrations Apply Paths, Facts

### Community 934 - "Shared JSON schemas"
Cohesion: 0.50
Nodes (4): alias_schema.json, emote_schema.json, Shared JSON schemas, unified_room_schema.json

### Community 935 - "init_npc_database.py"
Cohesion: 0.16
Nodes (17): _determine_database_init_flags(), get_npc_database_url(), get_npc_seed_data_from_postgresql(), init_database_schema(), _initialize_database_with_url(), main(), populate_npc_data(), _print_final_message() (+9 more)

### Community 937 - "__init__.py"
Cohesion: 0.14
Nodes (14): fake_clock(), make_player_dict(), make_user_dict(), Any, Shared fixtures and builders for all test tiers., Create a user dictionary for testing., Create a player dictionary for testing., Provide a monotonic counter for time-based tests. (+6 more)

### Community 938 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 939 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 940 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 941 - "days"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, days

### Community 942 - "effects"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, effects

### Community 943 - "end_hour"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 945 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 946 - "exits"
Cohesion: 0.50
Nodes (4): type, additionalProperties, type, exits

### Community 947 - "1. Component Refactoring"
Cohesion: 0.50
Nodes (4): 1. Component Refactoring, ChatPanel.tsx Enhancements (New Chat Input Panel), CommandPanel.tsx Simplifications, GameLogPanel.tsx (Renamed from ChatPanel.tsx)

### Community 948 - "Migration Considerations"
Cohesion: 0.50
Nodes (4): Backward Compatibility, Data Migration, Migration Considerations, Performance Impact

### Community 949 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Non-Functional Requirements, Success Criteria, User Experience Requirements

### Community 950 - "Risk Assessment"
Cohesion: 0.50
Nodes (4): Implementation Risks, Risk Assessment, Technical Risks, User Experience Risks

### Community 951 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Testing Strategy, Unit Tests, User Acceptance Tests

### Community 952 - "Phase 1: Critical Foundation (COMPLETED ✓)"
Cohesion: 0.50
Nodes (4): 1.1 Dependency Injection Container ✓, 1.2 EventBus Audit & Consolidation ✓, 1.3 Async Persistence Integration ✓, Phase 1: Critical Foundation (COMPLETED ✓)

### Community 953 - "Phase 2: Architecture Cleanup (COMPLETED ✓)"
Cohesion: 0.50
Nodes (4): 2.1 CORS Middleware Consolidation ✓, 2.2 Message Broker Abstraction ✓, 2.3 Error Handler Migration ✓, Phase 2: Architecture Cleanup (COMPLETED ✓)

### Community 954 - "Metrics and Impact"
Cohesion: 0.50
Nodes (4): Architecture Quality, Code Quality Improvements, Files Changed Summary, Metrics and Impact

### Community 956 - "Duplicate Event Analysis"
Cohesion: 0.05
Nodes (38): Canonical Event Sources, Consolidation Strategy, 🔴 CRITICAL: Player Movement Duplication - CONFIRMED, Duplicate Event Analysis, Event Flow Diagram, Event Ownership Matrix, Event Ownership Recommendations, Event Publishing Layers (+30 more)

### Community 957 - "Lessons Learned"
Cohesion: 0.50
Nodes (4): Challenges Encountered, Lessons Learned, Recommendations for Future Work, What Went Well

### Community 958 - "Test Coverage"
Cohesion: 0.50
Nodes (4): Client-Side Coverage, Integration Coverage, Server-Side Coverage, Test Coverage

### Community 959 - "Phase 2: Database Layer Integration"
Cohesion: 0.50
Nodes (4): 2.1 Persistence Layer Protection, 2.2 Database Connection Protection, 2.3 Configuration, Phase 2: Database Layer Integration

### Community 960 - "Phase 3: Real-Time Communication Protection"
Cohesion: 0.50
Nodes (4): 3.1 NATS Integration, 3.2 WebSocket Protection, 3.3 Configuration, Phase 3: Real-Time Communication Protection

### Community 961 - "Phase 4: File System Operations"
Cohesion: 0.50
Nodes (4): 4.1 Room Loading Protection, 4.2 Player Data File Operations, 4.3 Configuration, Phase 4: File System Operations

### Community 963 - "Phase 6: Monitoring and Observability"
Cohesion: 0.50
Nodes (4): 6.1 Metrics Collection, 6.2 Health Check Endpoints, 6.3 Logging Integration, Phase 6: Monitoring and Observability

### Community 964 - "Future Enhancements"
Cohesion: 0.50
Nodes (4): Advanced Features, Document metadata, Future Enhancements, Integration Opportunities

### Community 965 - "Monitoring and Alerting"
Cohesion: 0.50
Nodes (4): Alerting Rules, Health Checks, Metrics to Monitor, Monitoring and Alerting

### Community 966 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Monitoring Requirements, Performance Requirements, Success Criteria

### Community 967 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Load Tests, Testing Strategy, Unit Tests

### Community 968 - "Technical Implementation Details"
Cohesion: 0.50
Nodes (4): ✅ Argon2 Configuration - IMPLEMENTED, ✅ Authentication Logic - IMPLEMENTED, ✅ Hash Format - IMPLEMENTED, Technical Implementation Details

### Community 969 - "✅ Mitigation Strategies - IMPLEMENTED"
Cohesion: 0.50
Nodes (4): ✅ Authentication Failures - RESOLVED, ✅ Mitigation Strategies - IMPLEMENTED, ✅ Performance Issues - RESOLVED, ✅ Security Vulnerabilities - RESOLVED

### Community 970 - "✅ IMPLEMENTATION COMPLETED"
Cohesion: 0.50
Nodes (4): Completed Work Summary, Files Modified/Created, ✅ IMPLEMENTATION COMPLETED, Technical Implementation Details

### Community 971 - "Performance Considerations"
Cohesion: 0.50
Nodes (4): ✅ Database Impact - VERIFIED, ✅ Hash Generation Time - OPTIMIZED, ✅ Memory Usage - OPTIMIZED, Performance Considerations

### Community 972 - "✅ Success Criteria - ACHIEVED"
Cohesion: 0.50
Nodes (4): ✅ Functional Requirements - COMPLETED, ✅ Quality Requirements - COMPLETED, ✅ Security Requirements - COMPLETED, ✅ Success Criteria - ACHIEVED

### Community 973 - "fix_file"
Cohesion: 0.18
Nodes (16): fix_blanks_around_fences(), fix_blanks_around_headings(), fix_blanks_around_lists(), fix_fence_language(), fix_file(), fix_line_length(), fix_trailing_punctuation_in_headings(), main() (+8 more)

### Community 974 - "jackson_linter.py"
Cohesion: 0.20
Nodes (16): collect_json_files(), _file_appears_binary_or_terminal_output(), _first_fallback_encoding_that_parses(), _is_vscode_jsonc_settings(), main(), Path, Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1 failur, VS Code allows JSON with Comments in settings.json; stdlib json cannot parse it. (+8 more)

### Community 975 - "RoomFilenameMigrator"
Cohesion: 0.20
Nodes (10): main(), Path, Update the room ID in the JSON file to match new naming schema., Execute the migration., Handles migration of room filenames from old to new schema., Initialize the migrator., Parse old filename format to extract components., Discover all room files that need migration. (+2 more)

### Community 976 - "Risk Assessment"
Cohesion: 0.50
Nodes (4): ✅ High Risk - MITIGATED, ✅ Low Risk - RESOLVED, ✅ Medium Risk - RESOLVED, Risk Assessment

### Community 977 - "Implementation Strategy"
Cohesion: 0.50
Nodes (4): Implementation Strategy, ✅ Phase 1: Dependency and Setup - COMPLETED, ✅ Phase 2: Integration - COMPLETED, ✅ Phase 3: Testing and Validation - COMPLETED

### Community 978 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): ✅ Integration Tests - COMPLETED, ✅ Security Tests - COMPLETED, Testing Strategy, ✅ Unit Tests - COMPLETED

### Community 979 - "🎉 Expected Benefits"
Cohesion: 0.50
Nodes (4): Code Quality, Development Experience, 🎉 Expected Benefits, Future Development

### Community 980 - "🛠️ Technical Implementation Details"
Cohesion: 0.50
Nodes (4): Code Quality Enhancements, Performance Optimizations, Security Improvements, 🛠️ Technical Implementation Details

### Community 981 - "🎯 **NEXT MOST CRITICAL ITEM**"
Cohesion: 0.50
Nodes (4): 🎯 **NEXT MOST CRITICAL ITEM**, **Priority 1: Rate Limiting Implementation**, **Priority 2: Database Connection Pool Optimization**, **Priority 3: Memory Leak Prevention**

### Community 982 - "get_invite_codes.py"
Cohesion: 0.09
Nodes (13): Buy item from player., Calculate final price with markup., Handle greeting customer action., Handle restocking inventory action., Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., Shopkeeper NPC type with buy/sell functionality., Initialize shopkeeper NPC., Setup shopkeeper-specific behavior rules. (+5 more)

### Community 983 - "_is_npc_follow_value"
Cohesion: 0.20
Nodes (6): Test _check_casting_state function., Test _check_casting_state allows stop/interrupt/status during casting., Test _check_casting_state returns None when no magic service., Test _check_casting_state returns block result when player is casting., Test _check_casting_state returns None on error., TestCheckCastingState

### Community 984 - ".__init__"
Cohesion: 0.20
Nodes (6): Test _check_all_command_blocks function., Test _check_all_command_blocks returns block result for catatonia., Test _check_all_command_blocks returns block result for grace period., Test _check_all_command_blocks returns block result for casting., Test _check_all_command_blocks returns None when no blocks., TestCheckAllCommandBlocks

### Community 985 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 986 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 987 - "UI Screenshot Arena Cell 6,5"
Cohesion: 0.67
Nodes (3): Mythos Terminal Theme Tokens, MythosMUD Terminal Game UI Layout, UI Screenshot Arena Cell 6,5

### Community 988 - "message_handler_factory.py"
Cohesion: 0.06
Nodes (51): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, MessageHandlerFactory, PartyInviteResponseMessageHandler, PingMessageHandler (+43 more)

### Community 989 - "holiday"
Cohesion: 0.50
Nodes (4): $defs, holiday, additionalProperties, type

### Community 990 - "Expansion Backlog (Raw)"
Cohesion: 0.67
Nodes (3): Delta Green, Expansion Backlog (Raw), Things and Notes to Expand On

### Community 991 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 992 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 994 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 995 - "start_hour"
Cohesion: 0.20
Nodes (9): mock_validator(), mock_websocket(), Unit tests for websocket handler message validation.  Tests the message validati, Create a mock WebSocket., Create a mock message validator., Test _validate_message() returns message when validation succeeds., Test _validate_message() returns None when validation fails., test_validate_message_failure() (+1 more)

### Community 996 - "long_description"
Cohesion: 0.50
Nodes (4): maxLength, minLength, type, long_description

### Community 997 - "prototype_id"
Cohesion: 0.50
Nodes (4): prototype_id, maxLength, minLength, type

### Community 998 - "generate_invites_db.py"
Cohesion: 0.22
Nodes (7): rate_limiter(), Create a RateLimiter instance for testing., Utility modules for MythosMUD server.  This package contains various utility mod, RateLimiter, Rate limiting utilities for MythosMUD API endpoints.  This module provides rate, Simple in-memory rate limiter for API endpoints.      This rate limiter tracks r, Initialize the rate limiter.          Args:             max_requests: Maximum nu

### Community 999 - "short_description"
Cohesion: 0.50
Nodes (4): short_description, maxLength, minLength, type

### Community 1000 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1001 - "enabled"
Cohesion: 0.22
Nodes (9): MockEffectType, MockRangeType, MockSchool, MockTargetType, Enum, Mock spell school enum., Mock target type enum., Mock range type enum. (+1 more)

### Community 1002 - "plane"
Cohesion: 0.31
Nodes (8): check_invite_status(), count_invites(), list_all_invites(), main(), Count invite codes by status., Main function to handle command line arguments., List all invite codes in the database with their status., Check the status of a specific invite code.

### Community 1003 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1004 - "Frontend Design Skill"
Cohesion: 0.13
Nodes (16): Tailwind CSS Anti-Pattern Remediation, Adapt Skill, Animate Skill, Arrange Skill, Audit Skill, Bolder Skill, Clarify Skill, Colorize Skill (+8 more)

### Community 1005 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1006 - "quest_events.py"
Cohesion: 0.04
Nodes (38): Event subscription setup for application startup.  Extracted from lifespan_start, PlayerMortallyWoundedEvent, QuestCompleted, Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type. (+30 more)

### Community 1007 - "main"
Cohesion: 0.67
Nodes (3): main(), Entry point: clear daisy quest instances via anyio., _reset_daisy_quest()

### Community 1008 - "start_server.ps1"
Cohesion: 0.50
Nodes (4): Default Server Port 54768, start_local.ps1, start_server.ps1, stop_server.ps1

### Community 1009 - ".async_heal_player"
Cohesion: 0.25
Nodes (7): NPCService, Comprehensive NPC management service.      Handles CRUD operations for NPC defin, Initialize the NPC service., npc_service(), Test NPCService initialization., Create NPCService instance., test_npc_service_init()

### Community 1010 - "Local Channel System"
Cohesion: 0.40
Nodes (5): Local Channel Sub-Zone Routing, Scenario 10 Local Channel Movement, Scenario 11 Local Channel Errors, Scenario 12 Local Channel Integration, Local Channel System

### Community 1011 - ".to_dict"
Cohesion: 0.25
Nodes (5): Test _handle_special_command_routing function., Test _handle_special_command_routing handles alias management commands., Test _handle_special_command_routing returns error when alias storage unavailabl, Test _handle_special_command_routing converts single-word emotes., TestHandleSpecialCommandRouting

### Community 1012 - "npc_utils.py"
Cohesion: 0.25
Nodes (5): Test _ensure_alias_storage function., Test _ensure_alias_storage returns existing storage if provided., Test _ensure_alias_storage initializes new storage when None., Test _ensure_alias_storage returns None on initialization error., TestEnsureAliasStorage

### Community 1013 - ".is_player_muted_by_receiver"
Cohesion: 0.25
Nodes (7): Unit tests for help command handlers.  Tests the help command functionality., Test handle_help_command() returns general help when no topic., Test handle_help_command() returns help for specific topic., Test handle_help_command() handles unknown topic., test_handle_help_command_no_topic(), test_handle_help_command_unknown_topic(), test_handle_help_command_with_topic()

### Community 1014 - "check_invite_status.py"
Cohesion: 0.29
Nodes (5): _get_proper_data_dir(), Path, Get the mute data file path for a specific player., Get the proper environment-aware data directory for user management.      Uses, Initialize the user manager.          Args:             data_dir: Directory f

### Community 1015 - "analyze_coverage_gaps.py"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and meet, Write critical files below threshold section. (+7 more)

### Community 1016 - "_apply_arena_seed_patch.py"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 1017 - "list_active_invites.py"
Cohesion: 0.29
Nodes (4): Any, Check if a user has exceeded the rate limit.          Args:             user_id:, Get rate limit information for a user.          Args:             user_id: The u, Enforce rate limiting for a user.          Args:             user_id: The user's

### Community 1018 - ".__init__"
Cohesion: 0.33
Nodes (6): default, description, maximum, minimum, type, capacity_slots

### Community 1020 - "chat_logger"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 1022 - "test_validate_secure_path_path_traversal_commonpath"
Cohesion: 0.33
Nodes (4): Test validate_secure_path normalizes backslashes., Test validate_secure_path detects path traversal via commonpath check., test_validate_secure_path_path_traversal_commonpath(), test_validate_secure_path_with_backslash()

### Community 1023 - "test_asyncio_run_guardrails.py"
Cohesion: 0.50
Nodes (3): Test that server library code does not use asyncio.run() (AnyIO best practice)., Assert server/ has no asyncio.run() in library code (use anyio.run() at entry po, test_no_asyncio_run_in_server_library_code()

### Community 1024 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1025 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 1027 - "name"
Cohesion: 0.50
Nodes (4): description, minLength, type, name

### Community 1029 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1030 - "Stats"
Cohesion: 0.50
Nodes (4): main(), Run a psql command and return the result., Load all seed data files., run_psql_command()

### Community 1032 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 1033 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1034 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1035 - "description"
Cohesion: 0.50
Nodes (4): Functional Metrics, Quality Metrics, Success Metrics, Timeline Metrics

### Community 1036 - "npc_spawn_modifier"
Cohesion: 0.50
Nodes (4): description, minimum, type, npc_spawn_modifier

### Community 1037 - "special_rules"
Cohesion: 0.50
Nodes (4): special_rules, additionalProperties, description, type

### Community 1038 - "Codacy configuration"
Cohesion: 0.13
Nodes (15): Bandit configuration, Bandit B101 B105 B106 test skips, Codacy configuration, Enforced coverage gates, Codacy exclude_paths, Lizard CCN and NLOC thresholds, Grype SCA exclude paths, F-string logging anti-pattern detector (+7 more)

### Community 1039 - "Contributor Covenant Code of Conduct"
Cohesion: 0.12
Nodes (15): 1. Correction, 2. Warning, 3. Temporary Ban, 4. Permanent Ban, Attribution, Contributor Covenant Code of Conduct, Enforcement, Enforcement Guidelines (+7 more)

### Community 1040 - "Client Security and Privacy Policies"
Cohesion: 0.67
Nodes (3): Client Security and Privacy Policies, DOMPurify Sanitization, WebSocket Subprotocol Auth

### Community 1041 - "test_rest_command.py"
Cohesion: 0.05
Nodes (58): PlayerPositionService, Any, Extract player information for response., Get current position from player stats., Update player position in persistence., Mutate persistence and in-memory tracking to reflect the requested position., Mirror posture changes into the live connection manager., Coordinate player posture transitions with persistence and live presence trackin (+50 more)

### Community 1042 - "handle_time_command"
Cohesion: 0.67
Nodes (3): get_10_active_invites(), main(), Get 10 active invite codes from the database.

### Community 1049 - "📊 LINT ISSUE CATEGORIZATION GUIDE"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 1050 - "🚨 AI ERROR HANDLING"
Cohesion: 0.67
Nodes (3): 🚨 AI ERROR HANDLING, If Multiple Categories Have Issues, If Mypy Still Fails After Fixes

### Community 1051 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 1052 - "is_safe_filename"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters).      Arg, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 1054 - "MagicServiceHealingMixin"
Cohesion: 0.23
Nodes (10): MagicServiceHealingMixin, Any, UUID, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or s, True if effect result indicates healing was applied (success, effect_applied, he (+2 more)

### Community 1055 - "SpellMaterialsService"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1056 - "ConnectionCleaner"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1057 - "3. Systematic Investigation Approach"
Cohesion: 0.50
Nodes (4): Refresh collect_n quest progress after a successful inventory persist., _sync_collect_quests_after_inventory_save(), quest_service(), QuestService with mocked repos.

### Community 1059 - "name"
Cohesion: 0.50
Nodes (3): check_invite(), Check the status of a specific invite code., Check the status of an invite code.

### Community 1060 - "plane"
Cohesion: 0.67
Nodes (3): minLength, type, plane

### Community 1061 - "AI Development Workflow"
Cohesion: 0.67
Nodes (3): AI Command Development Workflow, Cursor AI Tooling, AI Development Workflow

### Community 1063 - "Documentation Created"
Cohesion: 0.67
Nodes (3): Architecture Documentation, Documentation Created, Domain Layer Documentation

### Community 1064 - "Technical Debt Addressed"
Cohesion: 0.67
Nodes (3): Eliminated Technical Debt, Remaining Technical Debt, Technical Debt Addressed

### Community 1065 - "Migration Strategy"
Cohesion: 0.67
Nodes (3): Gradual Migration Approach, Migration Strategy, Recommended Next Steps

### Community 1066 - "References"
Cohesion: 0.67
Nodes (3): Key Files, References, Related Documents

### Community 1067 - "Risk Mitigation"
Cohesion: 0.67
Nodes (3): Known Issues, Risk Mitigation, Strategies Employed

### Community 1068 - "Architecture Overview"
Cohesion: 0.67
Nodes (3): Architecture Overview, CircuitBreaker States, Integration Points

### Community 1069 - "✅ Rollback Plan - MAINTAINED"
Cohesion: 0.67
Nodes (3): Emergency Rollback, Monitoring and Alerts, ✅ Rollback Plan - MAINTAINED

### Community 1070 - "Future Considerations"
Cohesion: 0.67
Nodes (3): Future Considerations, Long-term Maintenance, Scalability

### Community 1071 - "Security Considerations"
Cohesion: 0.67
Nodes (3): ✅ Hash Parameters - IMPLEMENTED, Security Considerations, ✅ Security Implementation - COMPLETED

### Community 1072 - "process_room_files"
Cohesion: 0.21
Nodes (14): load_room_file(), main(), process_room_files(), Path, Load a room file safely., Save a room file safely., Convert room ID to lowercase., Convert filename to lowercase. (+6 more)

### Community 1073 - "validate_codacy_coverage_gate.py"
Cohesion: 0.25
Nodes (14): cobertura_has_server_sources(), cobertura_root_line_rate(), lcov_aggregate_hits(), main(), _parse_cobertura_xml(), Path, Parse Cobertura XML with defusedxml (lazy import: LCOV-only runs skip this depen, Return root line-rate from Cobertura XML (0.0--1.0). (+6 more)

### Community 1074 - "test_check_no_production_assert.py"
Cohesion: 0.18
Nodes (15): _load_checker(), _NoProductionAssertModule, Path, Protocol, Tests for scripts/check_no_production_assert.py., Verify no-production-assert hook targets server code and excludes tests., Public surface of check_no_production_assert loaded via importlib., test_find_assert_line_numbers_detects_assert() (+7 more)

### Community 1075 - "test_container_persistence_sql_injection.py"
Cohesion: 0.50
Nodes (3): list_active(), List active invite codes., List active invite codes.

### Community 1076 - "Phase 2: API Routes & Validation (Days 4-7) ✅ **COMPLETED**"
Cohesion: 0.67
Nodes (3): Deliverables, Phase 2: API Routes & Validation (Days 4-7) ✅ **COMPLETED**, Tasks

### Community 1077 - "⚠️ Risk Mitigation"
Cohesion: 0.67
Nodes (3): Mitigation Strategies, Potential Risks, ⚠️ Risk Mitigation

### Community 1078 - "Lucidity Subsystem"
Cohesion: 0.67
Nodes (3): Lucidity Subsystem, Lucidity Recovery Rituals, Magic Subsystem

### Community 1080 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1083 - "ConnectionEvent"
Cohesion: 0.50
Nodes (3): Initialize the rate limiter with configuration-based limits., chat_logger(), Create a ChatLogger instance with temp directory.

### Community 1085 - ".__init__"
Cohesion: 0.50
Nodes (3): Unit tests for PlayerSpell model.  Tests the PlayerSpell SQLAlchemy model., Test __repr__ returns expected string format., test_player_spell_repr()

### Community 1086 - ".__init__"
Cohesion: 0.50
Nodes (4): Test benchmark function runs without errors., test_benchmark_validation_performance(), benchmark_validation_performance(), Benchmark the performance of optimized vs original validation functions.

### Community 1087 - "MythosMUD project overview"
Cohesion: 0.33
Nodes (6): Comprehensive planning document, Father-son Mythos MUD vision, Pylint protected-access findings snapshot, Dual connection system with NATS, MythosMUD project overview, Tech stack FastAPI React PostgreSQL

### Community 1088 - "test_logger"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1089 - "Architecture Decision Records Index"
Cohesion: 0.20
Nodes (10): ADR-013 Pydantic BaseSettings Configuration, ADR-014 NATS Circuit Breaker and DLQ, Dead Letter Queue, db/procedures Stored Functions, ADR-015 PostgreSQL Procedures Migration, ADR-016 Aggro Threat Management, Room-Based Combat Aggro, ADR-017 AST Console Pruning (+2 more)

### Community 1093 - "check_no_production_assert.py"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 1095 - "overrides"
Cohesion: 0.11
Nodes (19): overrides, @asyncapi/generator, @asyncapi/generator-components, @asyncapi/generator-helpers, @asyncapi/specs, fast-uri, flatted, glob (+11 more)

### Community 1098 - "Cursor Workflows"
Cohesion: 0.29
Nodes (7): Cursor Agent CLI, Cursor CLI, Cursor Setup Guide, Cursor Subagents, Built-in Explore Bash Browser Subagents, Cursor Workflows, Cursor Rules Commands Subagents

### Community 1099 - "knip"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1100 - "tailwindcss"
Cohesion: 0.67
Nodes (3): 🚨 AI ERROR HANDLING, If Lint Still Fails After Fixes, If Multiple Categories Have Issues

### Community 1102 - "analyze_log_file"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 1103 - "@types/react"
Cohesion: 0.67
Nodes (3): minLength, type, description

### Community 1104 - "typescript"
Cohesion: 0.67
Nodes (3): get_commands_by_category(), Any, Get all commands in a specific category.

### Community 1116 - "MythosMUD Server Test Suite"
Cohesion: 0.33
Nodes (6): Command Tests Relocated, server/tests/unit/commands/, Integration Test Tier, make test-server, MythosMUD Server Test Suite, Unit Test Tier

### Community 1120 - "find_fstring_logging_violations"
Cohesion: 0.20
Nodes (11): find_fstring_logging_violations(), format_violation_report(), FStringLoggingDetector, main(), Call, Path, Main function to scan files and report violations., AST visitor to detect f-string logging violations. (+3 more)

### Community 1121 - "lint_sql_guardrails.py"
Cohesion: 0.23
Nodes (13): check_not_in_subquery(), check_select_star(), _collect_sql_files(), main(), Path, Lightweight guardrails for hand-maintained PostgreSQL SQL.  Warns on: - select *, Return line with line comment removed (-- ...)., Return content with block comments /* ... */ removed (simple, no nested). (+5 more)

### Community 1135 - "PostgreSQL procedures/functions access"
Cohesion: 0.18
Nodes (11): AGENTS.md agent instructions, Obsidian LLM wiki permanent memory, PostgreSQL procedures/functions access, Server authority rule, CLAUDE.md agent router, apply_procedures.ps1, Container Functions Moved from DDL, Procedures as CRUD Boundary (+3 more)

### Community 1145 - "rules"
Cohesion: 0.08
Nodes (25): entry, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries, dependencies (+17 more)

### Community 1146 - "dependencies"
Cohesion: 0.09
Nodes (23): dependencies, dompurify, lucide-react, react-dom, react-grid-layout, react-resizable, react-rnd, react-router-dom (+15 more)

### Community 1159 - "Earth Plane"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1167 - "test_connection_helpers_impl.py"
Cohesion: 0.04
Nodes (84): broadcast_global_event_impl(), broadcast_room_event_impl(), convert_uuids_to_strings(), handle_new_login_impl(), mark_player_seen_impl(), _optimize_payload(), Any, _queue_message_if_needed() (+76 more)

### Community 1170 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 1171 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 1172 - "container"
Cohesion: 0.33
Nodes (6): enabled, additionalProperties, description, required, type, container

### Community 1173 - "main"
Cohesion: 0.22
Nodes (12): analyze_connectivity(), generate_dot_file(), load_room_data(), main(), print_detailed_statistics(), print_room_listing(), Print a detailed listing of all rooms by subzone., Load all room and intersection data from the zone directory. (+4 more)

### Community 1174 - "main"
Cohesion: 0.22
Nodes (12): fix_md001_heading_increment(), fix_md013_line_length(), fix_md041_first_line_heading(), fix_md051_link_fragments(), main(), parse_errors(), Fix MD001: Heading levels should only increment by one level at a time., Parse markdownlint output file and extract errors. (+4 more)

### Community 1175 - "SyntaxErrorFixer"
Cohesion: 0.23
Nodes (8): main(), Path, Process multiple files and return statistics., Main function to run the syntax error fixer., Tool to fix syntax errors introduced by automated f-string remediation., Fix malformed logger calls with broken syntax., Fix syntax errors in a specific file., SyntaxErrorFixer

### Community 1177 - ".load_container_from_room_json"
Cohesion: 0.18
Nodes (10): EnvironmentalContainerLoader, Any, ContainerComponent, UUID, Environmental container loader for unified container system.  As documented in t, Migrate a container from room JSON to PostgreSQL.          Checks if container a, Load all environmental containers for a room from PostgreSQL.          Args:, Service for loading environmental containers from JSON and PostgreSQL.      Hand (+2 more)

### Community 1178 - "datetime"
Cohesion: 0.18
Nodes (6): datetime, Log the death of a combat target.          Args:             player_id: ID of th, Log the end of a combat encounter.          Args:             player_id: ID of t, Log a combat rate limit event.          Args:             player_id: ID of the p, Log the start of a combat encounter.          Args:             player_id: ID of, Log a combat attack.          Args:             player_id: ID of the attacking p

### Community 1190 - "enhanced_error_logging.py"
Cohesion: 0.22
Nodes (9): create_logged_http_exception(), log_and_raise_http(), log_error_with_context(), Any, Exception, HTTPException, Log an error with structured context. Delegates to log_structured_error., Create an HTTPException with proper logging and return it. Delegates to enhanced (+1 more)

### Community 1197 - "LLM Wiki Vault Schema"
Cohesion: 0.50
Nodes (4): LLM Wiki Vault Schema, Raw Sources Layer, Wiki Layer, Wiki Page Template

### Community 1199 - "Authoritative Environment DML"
Cohesion: 0.20
Nodes (11): Authoritative Environment DML, static_seed.sql (Deprecated), Generated World and Emotes SQL, DB Bootstrap Execution Order, Authoritative Environment DML, Removed Schema and Migration SQL, Legacy Schema Files Removed, Historical DDL Final Status (+3 more)

### Community 1205 - "verify_npc_occupants.py"
Cohesion: 0.23
Nodes (12): _check_service_availability(), _collect_npcs_by_room(), _print_summary(), Any, Verification script to check NPCs in lifecycle manager and test occupant query l, Print verification summary.      Args:         npc_count: Total number of active, Verify NPCs exist in lifecycle manager and test query logic., Check if NPC service, lifecycle manager, and active_npcs are available.      Ret (+4 more)

### Community 1220 - "Multi-Character Support System"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1223 - "grype.py"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior)., Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1224 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1225 - "Any"
Cohesion: 0.33
Nodes (3): cursor, Execute a query and return a cursor.          Args:             query: SQL query, Get a cursor from the underlying connection.          This method provides direc

### Community 1228 - "test_validate_codacy_coverage_gate.py"
Cohesion: 0.23
Nodes (12): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., test_cobertura_root_line_rate_parses(), test_lcov_aggregate_and_gate() (+4 more)

### Community 1244 - "CI Workflow"
Cohesion: 0.25
Nodes (11): CodeQL Configuration, CodeQL Test Credential Exclusions, CI Python Backend Job, CI Workflow, Codacy Coverage Finalize Job, CI React Client Job, step-security Harden Runner, mythos_unit CI Database Bootstrap (+3 more)

### Community 1250 - "lifecycle_periodic.py"
Cohesion: 0.14
Nodes (20): Clean up old lifecycle records (delegates to lifecycle_periodic)., Perform periodic maintenance (delegates to lifecycle_periodic)., _attempt_optional_npc_spawn(), check_optional_npc_spawns_impl(), _check_spawn_conditions_for_optional_npc(), cleanup_old_records_impl(), get_spawn_room_for_definition(), get_zone_key_for_definition() (+12 more)

### Community 1251 - "mcp.json"
Cohesion: 0.22
Nodes (10): codacy, context7, jcodemunch, playwright, npx, uvx, @codacy/codacy-mcp, jcodemunch-mcp (+2 more)

### Community 1256 - "Enhanced Logging Guide"
Cohesion: 0.29
Nodes (8): AI Agent Development Guide, AI Enhanced Logging Mandate, Documentation Updates ConnectionManager, Enhanced Logging Guide, MDC Request Context Binding, measure_performance Span, Error Handling Guide, MythosMUDError Hierarchy

### Community 1259 - "Full Async Persistence Target"
Cohesion: 0.33
Nodes (6): Persistence Async Migration Guide, Full Async Persistence Target, Persistence Async Migration Plan, Phase 2 Migration Complete, Phase 2 Persistence Migration, Phase 2 Migration Status

### Community 1260 - "Test Audit Executive Summary"
Cohesion: 0.22
Nodes (11): 25-30% Critical Regression Tests, Test Audit Executive Summary, Test Optimization Roadmap, Test Optimization Phases, Test Pruning Candidates, Low-Value Test Pruning Candidates, Test Quality Audit Report, Test Timing Analysis (+3 more)

### Community 1277 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, properties, field1, field2, field3, sub_zone (+3 more)

### Community 1279 - "properties"
Cohesion: 0.17
Nodes (12): description, description, description, description, maxLength, minLength, type, properties (+4 more)

### Community 1280 - "analyze_file"
Cohesion: 0.22
Nodes (10): analyze_file(), check_comment_references_nonexistent_code(), extract_function_and_class_names(), main(), Any, Path, Analyze a single file for comment issues.      Args:         file_path: Path to, Main entry point for comment analysis. (+2 more)

### Community 1281 - "main"
Cohesion: 0.25
Nodes (10): apply_migration_013(), apply_migration_014(), check_migration_013(), check_migration_014(), main(), Main function to check and apply migrations., Check if migration 013 (map_x/map_y columns) has been applied., Check if migration 014 (player_exploration table) has been applied. (+2 more)

### Community 1282 - "main"
Cohesion: 0.29
Nodes (10): check_thresholds(), _ensure_coverage_xml_or_exit(), main(), parse_coverage_xml(), _print_results_and_exit(), Path, Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't, Print coverage results and exit with appropriate code. (+2 more)

### Community 1283 - "main"
Cohesion: 0.25
Nodes (10): generate_simple_dot_file(), generate_simple_html_visualization(), load_room_data(), main(), print_simple_statistics(), Load all room and intersection data from the zone directory., Print simplified statistics about the room data., Main function to generate the simplified visualization. (+2 more)

### Community 1291 - "Teach Impeccable Skill"
Cohesion: 0.24
Nodes (11): Aha Moment Onboarding, Core Web Vitals Performance, Design Context Persistence (.impeccable.md), Onboard Skill, Optimize Skill, Overdrive Skill, Overdrive Mode, Polish Skill (+3 more)

### Community 1301 - "Client Updates System Audit"
Cohesion: 0.67
Nodes (3): Architecture Review Plan, Option C Replacement Client Updates, Client Updates System Audit

### Community 1317 - "handle_explore_command"
Cohesion: 0.28
Nodes (8): handle_explore_command(), Any, Handle exploration requests by returning a simple message.      This lightweight, Unit tests for exploration command handlers.  Tests the exploration command func, Test handle_explore_command() explores area., Test handle_explore_command() handles missing persistence., test_handle_explore_command(), test_handle_explore_command_no_persistence()

### Community 1340 - "lifecycle_respawn.py"
Cohesion: 0.23
Nodes (11): Process the respawn queue and spawn NPCs that are ready (delegates to lifecycle_, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle.  Extracted from lifecycle_manager to, Process the respawn queue and spawn NPCs that are ready.      Args:         mana (+3 more)

### Community 1355 - "check_file"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1356 - "lucidity_migration.py"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1381 - "Map Regression Tests Proposal"
Cohesion: 0.67
Nodes (3): ASCII Map Context Preparation, ASCII Minimap Generation, Map Regression Tests Proposal

### Community 1391 - "package.json"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 1392 - "include"
Cohesion: 0.10
Nodes (19): compilerOptions, allowImportingTsExtensions, composite, noEmit, types, exclude, extends, include (+11 more)

### Community 1393 - "vite.userConfig.ts"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1396 - "main"
Cohesion: 0.31
Nodes (8): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Entry point: read hook payload from stdin, check edited-files state, and optiona

### Community 1406 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 1414 - "MythosMUD Server Runbook Skill"
Cohesion: 0.67
Nodes (3): MythosMUD Server Runbook Skill, MythosMUD Worktree Workflow Skill, One Server Only Rule

### Community 1415 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 1422 - "Room Pathing Validator Implementation Spec"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1423 - "validator.py CLI"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1426 - "_filter_lines"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after th, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1427 - "fix_room_references"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area.      Args:         base_path: Path, save_room_file()

### Community 1428 - "player_inventory_migration.py"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing players, Run the migration across multiple database paths.

### Community 1429 - "populate_test_npc_databases.py"
Cohesion: 0.31
Nodes (8): get_npc_data_from_source(), get_npc_database_url(), main(), populate_database(), Populate a PostgreSQL database with NPC data.      Args:         target_url: Pos, Main function to populate test NPC databases., Get NPC database URL for the specified environment.      Args:         environme, Extract NPC data from the source PostgreSQL database.      Args:         source_

### Community 1430 - "run_bug_prevention_tests.ps1"
Cohesion: 0.53
Nodes (8): Invoke-ClientTest(), Invoke-IntegrationTest(), Invoke-ServerTest(), Show-TestSummary(), Test-Command(), Write-ColorOutput(), Write-Header(), Write-Section()

### Community 1432 - ".log_combat_monitoring_alert"
Cohesion: 0.22
Nodes (5): Any, Log a combat-related security event.          Args:             event_type: Type, Log a combat validation failure.          Args:             player_id: ID of the, Log a combat monitoring alert.          Args:             alert_type: Type of al, Get a summary of combat audit events.          Args:             player_id: ID o

### Community 1433 - "test_logging_handlers.py"
Cohesion: 0.05
Nodes (63): _aggregator_handler_class_for_windows(), create_aggregator_handler(), _make_exec_for_aggregator(), Any, LogRecord, Path, RotatingFileHandler, Logging handlers for file-based logging with rotation and Windows safety.  This (+55 more)

### Community 1448 - "cli.sh"
Cohesion: 0.39
Nodes (6): download(), download_cli(), download_file(), get_latest_version(), handle_rate_limit(), cli.sh script

### Community 1474 - "Whisper NATS Subject Bug Fix"
Cohesion: 0.25
Nodes (8): Admin Teleportation Display Bug, E2E Session Report 2025-12-02, Whisper Messages Not Received Bug, chat.whisper.player Subject Segment, Whisper NATS Subject Bug Fix, Missing player Segment Root Cause, Whisper System Investigation, Whisper Work Completed and Remaining

### Community 1476 - "Event-Sourced Projector"
Cohesion: 0.32
Nodes (8): Event-Sourced Projector, Client Event Schema, game_state Event, GameState, room_state Event, Critical State Handoffs, Enter-Room Request/Response, Server Authority Over Client

### Community 1480 - "Combat verification UI-v2 five-pane layout"
Cohesion: 0.25
Nodes (8): Impeccable design context, Legibility under pressure, Dark terminal-first aesthetic, Combat hit and defeat game log, Sanitarium Entrance room pane, Combat verification UI-v2 five-pane layout, Death/respawn UI-v2 five-pane layout, Unknown command health chat message

### Community 1487 - "ensure_directory_exists"
Cohesion: 0.25
Nodes (8): ensure_directory_exists(), Ensure a directory exists and return its absolute path.      Args:         direc, Test ensure_directory_exists with existing directory., Test ensure_directory_exists creates directory if it doesn't exist., Test ensure_directory_exists with relative path., test_ensure_directory_exists_creates(), test_ensure_directory_exists_existing(), test_ensure_directory_exists_relative_path()

### Community 1488 - "webhook"
Cohesion: 0.25
Nodes (7): get_alerts(), health(), Request, Receive and log alert webhooks, Health check endpoint, Get recent alerts (for testing), webhook()

### Community 1491 - "migrate_file"
Cohesion: 0.36
Nodes (7): main(), migrate_file(), MigrationResult, NamedTuple, Path, Result of a file migration., Migrate a single file to use async persistence patterns.      Args:         file

### Community 1501 - "main"
Cohesion: 0.39
Nodes (7): main(), cursor, Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial), th, Create quest_definitions, quest_instances, quest_offers tables and indexes., Insert leave_the_tutorial quest definition and room offer (idempotent)., _run_quest_ddl(), _seed_leave_the_tutorial()

### Community 1502 - "apply_migration"
Cohesion: 0.36
Nodes (7): apply_migration(), check_schema(), main(), Cursor, Path, Check current schema of npc_spawn_rules table, Apply the migration to rename columns

### Community 1540 - "PostgreSQL Anti-Patterns Review"
Cohesion: 0.29
Nodes (7): Persistence Repository Layer, PostgreSQL Anti-Patterns, PostgreSQL Anti-Patterns Review, PostgreSQL 2026 Audit Findings, PostgreSQL Audit Report 2026, PostgreSQL Contributor Guide, PostgreSQL Stored Procedures Pattern

### Community 1546 - "test_logging_processors.py"
Cohesion: 0.04
Nodes (72): EventDict, add_correlation_id(), add_request_context(), enhance_player_ids(), _PlayerServiceHolder, Logging processors for structlog event processing.  This module provides process, Add correlation ID to log entries if not already present.      This processor en, Add request context information to log entries.      This processor adds context (+64 more)

### Community 1550 - "Lucidity System Expansion Scenarios"
Cohesion: 0.67
Nodes (4): Lucidity System Expansion Scenarios, Catatonia Grounding Ritual Scenario, player_lucidity Ledger, Sanitarium Failover Escalation

### Community 1559 - "WebSocket-Only Migration"
Cohesion: 0.33
Nodes (6): SSE Connection Removal, Unified Client Message Pipeline, Unify Client Message Handling, WebSocket Best-Practices Remediation, WebSocket-Only Architecture, WebSocket-Only Migration

### Community 1561 - "intersection_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1564 - "room_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1565 - "main"
Cohesion: 0.38
Nodes (6): generate_html_visualization(), load_room_data(), main(), Load all room and intersection data from the zone directory., Main function to generate the HTML visualization., Generate an HTML visualization of the room network.

### Community 1567 - "Attack Command Not Starting Combat"
Cohesion: 0.29
Nodes (7): Attack Command Not Starting Combat, CommandType Enum vs String Comparison, Target Resolution via Lifecycle Manager, NPC Dual Tracking System Issue, Stale Room.get_npcs After Persistence Reload, NPC Spawning vs Occupants Display Issue, Flattened Occupants Losing Player NPC Distinction

### Community 1568 - "Second NPC Combat And Linkdead Findings"
Cohesion: 0.29
Nodes (7): Coroutine Object Has No current_room_id, Combat Start Missing Await get_player_by_name, get_player_by_id vs async_get_player Mismatch, XP Award async_get_player Missing Method, Linkdead WebSocket Grace Period, Second NPC Combat And Linkdead Findings, Stale Queued Attack Target Validation

### Community 1569 - "Multi-Word Spell Name Parsing Failure"
Cohesion: 0.29
Nodes (7): Missing cast spell spells Pydantic Models, Spell Slash Commands Missing From Validation, create_cast_command First-Word-Only Parse, Multi-Word Spell Name Parsing Failure, Missing async_heal_player Method, record_spell_cast Cross-Session Object Use, Heal Spell SQLAlchemy Session Boundary Error

### Community 1570 - "Respawn Subsystem"
Cohesion: 0.33
Nodes (7): Limbo Room Death State, PlayerRespawnService, Respawn Subsystem, Determination Points (DP), Incapacitation (DP 0 to -9), no_death Rooms (ADR-009), Status Effects Subsystem

### Community 1615 - "Player Command Developer Guide"
Cohesion: 0.33
Nodes (6): Player Command Pipeline, Player Command Developer Guide, Pydantic Code Review, Pydantic Model Validation Patterns, Python Model Updates Required, Python Model Sync Requirements

### Community 1633 - "Round-Based Combat"
Cohesion: 0.33
Nodes (6): Combat Action Queue, Combat Bugs Investigation and Fixes, Round-Based Combat, Combat Round System Refactor, First Weapon Switchblade, Flee Command and Effect

### Community 1635 - "pyrightconfig.json"
Cohesion: 0.25
Nodes (7): extends, extraPaths, pythonVersion, venv, venvPath, ., ./pyproject.toml

### Community 1641 - "properties"
Cohesion: 0.12
Nodes (17): description, items, type, properties, default, description, type, type (+9 more)

### Community 1642 - "check_file_for_logging_issues"
Cohesion: 0.47
Nodes (5): check_file_for_logging_issues(), main(), Path, Check a single file for logging consistency issues.      Args:         file_path, Main function to check all service files for logging consistency.

### Community 1643 - "e2e_reset_players.py"
Cohesion: 0.47
Nodes (5): _load_default_respawn_room(), main(), Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the serv, Entry point: run E2E player reset via anyio., _reset_e2e_players()

### Community 1647 - "NPC Occupants Verification Summary"
Cohesion: 0.33
Nodes (6): NPC Display Final Fixes, room_update Overwriting NPC Data, asyncpg UUID replace AttributeError, Legacy Occupants Snapshot Format, NPC Occupants Verification Summary, Rooms API User Object AttributeError

### Community 1652 - "Combat Client Crash"
Cohesion: 0.33
Nodes (6): event_data vs data Field Name Mismatch, NATS Event Message Field Mismatch, Combat Client Crash, CombatMessaging Connection Manager Init Failure, Combat Disconnect At NPC Death, Passive Lucidity Flux Performance Degradation

### Community 1653 - "Respawn Death Screen Loop Limbo ID Mismatch"
Cohesion: 0.33
Nodes (6): limbo_death_void vs limbo_death_void_limbo_death_void, Respawn Death Screen Loop Limbo ID Mismatch, SQLAlchemy JSONB Mutation Detection, Respawn Persistence JSONB Mutation Failure, Death Threshold and Posture Bugs, HP -10 Limbo Transition Delay

### Community 1655 - "NPC Combat Start Race Condition"
Cohesion: 0.33
Nodes (6): NPC Combat Start Race Condition, Redundant NPC Instance Lookup Failure, NPCs Incorrectly Marked is_alive False, December 3 Final Investigation Summary, Character Info Panel Missing Stats Field, Room Occupants Duplicates and Missing Player

### Community 1657 - "MythosMUD Full-Stack Feature Skill"
Cohesion: 0.33
Nodes (6): MythosMUD COPPA Checklist Skill, MythosMUD Database Placement Skill, MythosMUD Full-Stack Feature Skill, MythosMUD OpenAPI Workflow Skill, player_id is UUID, Server Authority over Client

### Community 1659 - "Enhanced Structured Logging System"
Cohesion: 0.40
Nodes (5): bind_request_context, Dual Logging (warnings/errors aggregators), Enhanced Structured Logging System, get_logger, sanitize_sensitive_data Processor

### Community 1669 - "Magic and Spellcasting System"
Cohesion: 0.40
Nodes (5): EffectList Pattern, Effects System Reference, Magic Points MP, Magic and Spellcasting System, Spell Registry

### Community 1670 - "Lucidity Tiers"
Cohesion: 0.60
Nodes (5): Catatonic Rescue Window, Lucidity System (LCD), Lucidity Tiers, Phantom Hostiles, Reversed Compass Directions

### Community 1674 - "Four-Level Room Hierarchy"
Cohesion: 0.40
Nodes (5): Environment Classification, Four-Level Room Hierarchy, Environment Inheritance, Room Hierarchy Implementation, Hierarchical World Loader

### Community 1689 - "combat_validator"
Cohesion: 0.06
Nodes (28): combat_validator(), Create a CombatValidator instance., When party_service is None, validate_can_attack_target allows attack., When both players are in same party, validate_can_attack_target blocks attack., When players are not in same party, validate_can_attack_target allows attack., test_validate_can_attack_target_different_party_allows(), test_validate_can_attack_target_no_party_service_allows(), test_validate_can_attack_target_same_party_blocks() (+20 more)

### Community 1703 - "Modular E2E Test Suite"
Cohesion: 0.40
Nodes (5): Modular E2E Test Suite, MULTIPLAYER_SCENARIOS_PLAYBOOK, E2E Validation Passed, AI Context Limit 20KB, E2E Test Suite README

### Community 1704 - "Playwright MCP Scenarios"
Cohesion: 0.40
Nodes (5): Automated Playwright CLI Tests, Hybrid E2E Testing Approach, Mandatory Execution Order, Playwright MCP Scenarios, Room Occupants Fix

### Community 1713 - "AI PR Reviewer Instructions"
Cohesion: 0.40
Nodes (5): AI PR Reviewer Instructions, COPPA and Security Review Mandates, Review Coverage Thresholds, player_id UUID Type Rule, Server Authority Review Rule

### Community 1719 - "Quest System Gap"
Cohesion: 0.40
Nodes (5): Quest System Gap, MUD Subsystems Gap Analysis, Player Skills and Profession Modifiers, Quest Subsystem Implementation, Quest System

### Community 1720 - "ArkanWolfshade Say Chat UI"
Cohesion: 0.50
Nodes (5): ArkanWolfshade Say Chat UI, Ithaqua Say Reply UI, Say Room Chat Channel, Chat Test Failed AW Screenshot, Chat Test Failed Ithaqua Screenshot

### Community 1722 - "Container Contents Synchronization Bug"
Cohesion: 0.50
Nodes (5): Container Contents Synchronization Bug, Fail-Fast Container Error Philosophy, slot_type backpack Assignment, Dual Inventory Storage Architecture, Inventory Slot Calculation Bug

### Community 1723 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1724 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1725 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1727 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1728 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1734 - "lock_state"
Cohesion: 0.25
Nodes (8): locked, sealed, unlocked, default, description, enum, type, lock_state

### Community 1738 - "fix_file"
Cohesion: 0.60
Nodes (4): fix_file(), main(), Path, Fix suppressions in a file.      Returns:         (number_fixed, list of changes

### Community 1739 - "check_codacy_yaml"
Cohesion: 0.50
Nodes (4): check_codacy_yaml(), _content_is_valid(), Return (valid, list of reasons if invalid)., Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit.

### Community 1740 - "safe_subprocess.py"
Cohesion: 0.31
Nodes (12): _argv_char_len(), _build_guard_command(), _changed_files_between(), _git_executable(), _is_graphify_path(), _local_changed_files(), main(), Path (+4 more)

### Community 1744 - "TestPostgresConnectionPool"
Cohesion: 0.10
Nodes (16): is_postgres_url(), PostgresConnectionPool, Thread-safe PostgreSQL connection pool., Get or create a connection pool for the given database URL., Get a connection from the pool., Check if the database URL is PostgreSQL., Test PostgresConnectionPool class., Test is_postgres_url() with PostgreSQL URL. (+8 more)

### Community 1748 - "MythosMUD Pre-Commit Checklist Skill"
Cohesion: 0.40
Nodes (5): Definition of Done Checklist, MythosMUD Code Quality AI Skill, MythosMUD Commit Messages Skill, MythosMUD Pre-Commit Checklist Skill, MythosMUD Test Writing Skill

### Community 1774 - "WebSocket and SSE Dual Connections"
Cohesion: 0.50
Nodes (4): Dual Connection API Reference, WebSocket and SSE Dual Connections, Dual Connection Client Guide, Dual Connection Deployment Guide

### Community 1786 - "MythosMUD Product Requirements"
Cohesion: 0.50
Nodes (4): Aggro System, Lucidity System, MythosMUD Product Requirements, Room-Based Combat

### Community 1809 - "Claude Pointer (.claude/CLAUDE.md)"
Cohesion: 0.67
Nodes (4): AGENTS.md Authoritative Reference, Cursor Rules (.cursor/rules/), Claude Pointer (.claude/CLAUDE.md), Root CLAUDE.md Router Stub

### Community 1819 - "Logging Best Practices"
Cohesion: 0.67
Nodes (4): Logging Best Practices, Structured Key-Value Logging, Logging Quick Reference, Forbidden Logging Patterns

### Community 1829 - "Scenario Group Execution"
Cohesion: 0.50
Nodes (4): Scenario Group Execution, Local Channel Scenario Group (8-12), Logout Scenario Group (19-21), Whisper Channel Scenario Group (13-18)

### Community 1831 - "Per-Recipient Whisper Rate Limiting"
Cohesion: 0.50
Nodes (4): Whisper System Remediation, Per-Recipient Whisper Rate Limiting, Global Whisper Rate Limit, Scenario 15 Rate Limiting Blocked

### Community 1840 - "RoomSubscriptionManager"
Cohesion: 0.06
Nodes (31): SendPersonalMessage, Initialize the message broadcaster.          Args:             room_manager: Roo, Any, Retrieve current room drops as a defensive copy for callers.          Args:, Append an item stack to the room drop ledger.          Args:             room_id, Remove quantity of a drop entry, returning the removed stack.          Args:, Adjust quantity for an existing drop entry; removing entry when zero.          A, Manages room subscriptions and occupant tracking.      This class handles room s (+23 more)

### Community 1845 - "Vite Best-Practices Remediation"
Cohesion: 0.50
Nodes (4): Test Suite Improvement, Vite Best-Practices Remediation, import.meta.env (Vite), Vitest Best-Practices Remediation

### Community 1852 - "Scenario 32 Disconnect Grace Period"
Cohesion: 0.50
Nodes (4): Scenario 32 Disconnect Grace Period, Linkdead Zombie State, Scenario 33 Rest Command, Scenario 35 Player Combat

### Community 1854 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1869 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1870 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1872 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1876 - "properties"
Cohesion: 0.11
Nodes (19): description, description, description, description, type, description, maxLength, minLength (+11 more)

### Community 1877 - "apply_migration"
Cohesion: 0.67
Nodes (3): apply_migration(), main(), Apply migration to a single database.

### Community 1879 - "_resolved_npm"
Cohesion: 0.67
Nodes (3): main(), Return absolute path to npm (prefer npm.cmd on Windows), or None if not found., _resolved_npm()

### Community 1880 - "verify_tutorial_migrations.ps1"
Cohesion: 0.83
Nodes (3): Test-Migration08(), Test-Migration12(), Write-ColorOutput()

### Community 1883 - "F-String Logging Violations"
Cohesion: 0.50
Nodes (4): F-String Logging Violations, F-String Logging Remediation Complete, Pre-Commit F-String Hook Gaps, AST-Based F-String Logging Detector

### Community 1890 - "Catatonic Movement Prevention Bug"
Cohesion: 0.50
Nodes (4): Catatonic Movement Prevention Bug, WebSocket Go Command Unified Handler Bypass, current_room_id VARCHAR(50) Truncation, Movement Valid Exits Rejection Bug

### Community 1892 - "Rooms List SQL ::uuid[] Parameter Conflict"
Cohesion: 0.50
Nodes (4): asyncpg Colon Cast Parameter Parsing, Rooms List SQL ::uuid[] Parameter Conflict, Minimap Explored Rooms UUID vs stable_id, Explored Room UUIDs Treated As stable_ids

### Community 1905 - "Character Creation Revamp"
Cohesion: 0.67
Nodes (3): Character Creation Revamp, CoC-Style Skills Allocation, Skill Use Tracking and Level-Up Improvement

### Community 1906 - "Dead Code Cleanup Completion"
Cohesion: 0.67
Nodes (3): Legacy Files Cleanup Summary, Dead Code Cleanup Completion, Dead Code Cleanup Planning

### Community 1910 - "Single Session Per User"
Cohesion: 0.67
Nodes (3): force_disconnect_player, Single Session Per User, Player Spawn Protection

### Community 1911 - "Test Warning Remediation"
Cohesion: 0.67
Nodes (3): Early Logging Initialization, datetime.utcnow Deprecation Fix, Test Warning Remediation

### Community 1912 - "Random Stats Generator Planning"
Cohesion: 0.67
Nodes (3): Pydantic Click Command Validation Integration, Random Stats Generator Technical Plan, Random Stats Generator Planning

### Community 1917 - "Party System Reference"
Cohesion: 0.67
Nodes (3): Party Invite Command, Party System Reference, Ephemeral Grouping Party Planning

### Community 1924 - "Test File Migration Mapping"
Cohesion: 0.67
Nodes (3): Test Suite Hierarchical Migration, Test File Migration Mapping, Test Suite Refactoring Deliverables

### Community 1944 - "AnyIO vs Asyncio Comparison"
Cohesion: 0.67
Nodes (3): AnyIO Code Review and Migration, AnyIO vs Asyncio Comparison, Structured Concurrency

### Community 1945 - "GameState Event Projection"
Cohesion: 0.67
Nodes (3): Client EventStore, GameState Event Projection, Server Authority over Client State

### Community 1946 - "Easy Coverage Wins"
Cohesion: 0.67
Nodes (3): Coverage Improvement Summary, Easy Coverage Wins, Tiered Coverage Wins

### Community 1947 - "Truly Dead Code"
Cohesion: 0.67
Nodes (3): Knip Client Dead Code Tooling, Truly Dead Code, Vulture Allowlist

### Community 1948 - "FastAPI Code Review"
Cohesion: 0.67
Nodes (3): FastAPI Dependency Injection, FastAPI Code Review, FastAPI Response Models

### Community 1956 - "Dependency Review Workflow"
Cohesion: 0.67
Nodes (3): Dependabot Dependency Updates, Dependency Review Workflow, UV Lock Dependency Snapshot Gate

### Community 1964 - "10 Concurrent Players Load Test"
Cohesion: 0.67
Nodes (3): who Command Unawaited Coroutine Bug, 10 Concurrent Players Load Test, Load Test Suite

### Community 1972 - "Cursor Rules as Canonical Config"
Cohesion: 0.67
Nodes (3): Cursor-Centric AI Config, Cursor Rules as Canonical Config, GitHub Worktrees Cursor Setup

### Community 1974 - "Gladiator Ring Arena"
Cohesion: 0.67
Nodes (3): Arena Implementation Todos, Arena Center Tutorial Exit and Respawn, Gladiator Ring Arena

### Community 1975 - "Logging Aggregator Verification"
Cohesion: 0.67
Nodes (3): Logging Aggregator Verification, warnings.log and errors.log Aggregators, Structlog Anti-Pattern Remediation

### Community 1976 - "Memory Leak Remediation"
Cohesion: 0.67
Nodes (3): Closed WebSockets Deque Cap, Memory Leak Metrics Collection, Memory Leak Remediation

### Community 1977 - "Playwright DI Migration Validation"
Cohesion: 0.67
Nodes (3): Playwright Best-Practices Remediation, Playwright DI Migration Validation, E2E Harness Overhaul

### Community 1978 - "Server Authority Remediation"
Cohesion: 0.67
Nodes (3): game_state Room Replace (not Merge), Server Authority Remediation, Server Authority Rule

### Community 1996 - "Scenario 34 Two Players Same Room Visibility"
Cohesion: 0.67
Nodes (3): Scenario 34 Two Players Same Room Visibility, Scenario 36 Movement Visibility, Scenario 37 Chat Message Ordering

### Community 2011 - "NPCs Not Updating On Player Movement"
Cohesion: 0.67
Nodes (3): exclude_player Occupants Snapshot Pattern, NPCs Not Updating On Player Movement, Canonical Room ID NPC Matching Remediation

### Community 2012 - "Combat Messages Dual Panel Display"
Cohesion: 0.67
Nodes (3): Combat Turn Order UUID Display, Combat Messages Dual Panel Display, Missing NPC Death Message Handlers

### Community 2013 - "Test Suite Stall After Performance Comparison"
Cohesion: 0.67
Nodes (3): Docker Build mythos_unitql Typo, Test Suite Stall After Performance Comparison, thread.join Without Timeout Hang

### Community 2019 - "Ground Command"
Cohesion: 0.67
Nodes (3): Catatonic Rescue Target, Ground Command, Rescue Subsystem

### Community 2020 - "Rest Subsystem"
Cohesion: 0.67
Nodes (3): Rest Countdown Disconnect, Rest Location Instant Disconnect, Rest Subsystem

### Community 2021 - "LevelService"
Cohesion: 1.00
Nodes (3): LevelService, SkillService, Skills / Level Subsystem

### Community 2199 - "factory.py"
Cohesion: 0.03
Nodes (87): MutableHeaders, main(), Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., _sanitize_token_examples(), _configure_cors(), CORSConfigDict, create_app() (+79 more)

### Community 2205 - "test_nats_service.py"
Cohesion: 0.01
Nodes (326): NATS, ConnectionEvent, NATSConnectionStateMachine, Enum, Exception, Connection state machine for NATS messaging.  Implements a robust state machine, Initialize connection state machine.          Args:             connection_id: U, Handler for connect transition.          Resets reconnection counter and prepare (+318 more)

## Knowledge Gaps
- **3642 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `@codacy/codacy-mcp`, `@playwright/mcp` (+3637 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **619 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `AliasStorage` to `.get_instance`, `create_hasher_with_params`, `connection_manager.py`, `test_alias_commands.py`, `types.ts`, `channel_broadcasting_strategies.py`, `MythosMUDError`, `test_command_factories_inventory.py`, `LoggedHTTPException`, `get_logger`, `player_connection_setup.py`, `User`, `_format_room_posture_message`, `._handle_npc_follower_move`, `test_command_validator.py`, `test_look_npc.py`, `Room`, `DeadLetterMessage`, `OccupantFormatter`, `MockEventClass`, `spell_effects_heal.py`, `dependencies.py`, `admin_teleport_commands.py`, `SpellRegistry`, `test_zone_config_loader.py`, `inventory_command_helpers.py`, `websocket_handler.py`, `CreateItemInstanceInput`, `npc_combat_grace.py`, `SpellLearningService`, `test_communication_commands_flows.py`, `Any`, `IdleMovementHandler`, `test_container_persistence.py`, `__init__.py`, `test_npc_database.py`, `CoordinateGenerator`, `character_creation.py`, `__init__.py`, `ApplicationContainer`, `PassiveLucidityFluxService`, `chat_pose_helpers.py`, `is_player_in_login_grace_period`, `test_command_factories_exploration.py`, `extract_definition_id_from_npc`, `test_login_grace_period_visual_indicator.py`, `test_player_service.py`, `RateLimiter`, `test_admin_auth_service.py`, `CombatInstance`, `.load_player_mutes`, `test_look_helpers.py`, `websocket_initial_state.py`, `AppConfig`, `test_status_commands.py`, `lifespan.py`, `LucidityService`, `exceptions.py`, `InventoryMutationGuard`, `test_player_presence_tracker.py`, `test_command_admin.py`, `HolidayService`, `ConnectionManager`, `WebSocketMessageValidator`, `_handle_admin_set_stat_command`, `test_config.py`, `test_command_moderation.py`, `FeatureFlagService`, `.to_dict`, `test_lucidity_recovery_commands.py`, `CircuitBreakerOpen`, `container_endpoints_basic.py`, `RoomSyncService`, `extract_room_id_from_npc`, `.get_room`, `Any`, `catatonia_check.py`, `CircuitBreaker`, `test_skill_service.py`, `test_connection_helpers_impl.py`, `test_combat_persistence_handler_events.py`, `test_container_websocket_events.py`, `factory.py`, `CombatConfiguration`, `.load_container_from_room_json`, `combat_validator`, `test_nats_service.py`, `RoomDataCache`, `chat_service.py`, `projectorHandlersMessages.ts`, `CombatAuditLogger`, `AggressiveMobNPC`, `test_party_service.py`, `TestCheckCastingState`, `CommandRequest`, `test_inventory_commands.py`, `fastapi_integration.py`, `test_logout_commands.py`, `metrics.py`, `test_inventory_helpers.py`, `test_corpse_lifecycle_service.py`, `test_map_helpers.py`, `TaskRegistry`, `correlation_middleware.py`, `test_connection_statistics.py`, `test_connection_session_management.py`, `test_command_combat.py`, `CombatMonitoringService`, `lifecycle_periodic.py`, `container_persistence.py`, `ChatModeration`, `NATSEventBusBridge`, `Player`, `npc_definitions_api.py`, `look_command.py`, `datetime`, `error_handling_middleware.py`, `LogAggregator`, `LRUCache`, `PydanticErrorHandler`, `PlayerInventory`, `test_room_utils.py`, `test_game_tick_processing_async.py`, `game_tick_processing.py`, `test_combat_schema.py`, `quest_commands.py`, `ValidationError`, `combat_attack.py`, `__init__.py`, `.__post_init__`, `test_item.py`, `GameClientV2ContainerView.tsx`, `monitoring.py`, `test_connection_cleaner.py`, `test_command_parser_helpers.py`, `DatabaseError`, `subscribe_to_room_events_impl`, `handle_read_command`, `real_time.py`, `__init__.py`, `test_room_id_utils.py`, `test_command_base.py`, `SchemaValidator`, `test_command_exploration.py`, `lifecycle_respawn.py`, `test_aggro_threat.py`, `get_asyncpg_server_settings_for_database_url`, `MovementService`, `StatusPanel.tsx`, `graceful_degradation`, `consume_prototype_from_player`, `.get_stat_requirements`, `add_damage_threat`, `lucidity_migration.py`, `processing.py`, `._despawn_npc`, `map_minimap.py`, `test_inventory_service_helpers.py`, `hallucinations.py`, `admin_shutdown_command.py`, `MovementMonitor`, `.__init__`, `TargetResolutionService`, `rooms.py`, `config.ts`, `chat_nats_publisher.py`, `test_player_event_handlers_room_left.py`, `retry.py`, `get_async_session`, `player_inventory_migration.py`, `command_handler_unified.py`, `MessageBroadcaster`, `test_look_item_helpers.py`, `inventory_drop_command.py`, `CorpseLifecycleService`, `shutdown_sequence.py`, `test_profession.py`, `_assign_container_get_instance`, `message_handler_factory.py`, `is_shutdown_pending`, `EmoteService`, `quest_events.py`, `HealthRepository`, `test_level_service.py`, `conftest.py`, `_JSONDict`?**
  _High betweenness centrality (0.169) - this node is a cross-community bridge._
- **Why does `ValidationError` connect `test_player_service.py` to `.get_instance`, `test_invite_schemas.py`, `test_player_event_handlers_room_left.py`, `types.ts`, `container_endpoints_basic.py`, `inventory_pickup_command.py`, `test_websocket_messages.py`, `MythosMUDError`, `NPCCombatIntegrationBase`, `LoggedHTTPException`, `get_logger`, `RoomInfoPanel.tsx`, `ValidationError`, `User`, `test_command_factories_inventory.py`, `test_command_processor.py`, `test_command_inventory.py`, `test_health_service.py`, `error_types.py`, `test_character_creation_service.py`, `test_item.py`, `test_command_validator.py`, `.load_container_from_room_json`, `game.py`, `test_npc_combat_handlers.py`, `test_command_parser_helpers.py`, `DatabaseError`, `AggressiveMobNPC`, `inventory_command_helpers.py`, `CreateItemInstanceInput`, `IdleMovementHandler`, `BaseCommand`, `test_container_persistence.py`, `SchemaValidator`, `test_npc_database.py`, `character_creation.py`, `test_command_factories_utility.py`, `npc_config_parsing.py`, `__init__.py`, `validate_room_data`, `lucidity_service.py`, `MovementService`, `get_admin_auth_service`, `test_command_factories_exploration.py`, `.check_level_up`, `websocket_helpers.py`, `test_profession.py`, `test_command_service.py`, `exceptions.py`, `test_command_combat.py`, `test_connection_disconnection.py`, `Alias`, `command_input.py`, `container_persistence.py`, `test_spawn_validator.py`, `test_go_command.py`, `container_persistence_async.py`, `Player`, `NPCOccupantProcessor`, `NPCStartupService`, `test_config_init.py`, `error_handling_middleware.py`, `canonical_room_id_impl`, `test_look_player.py`, `test_command_moderation.py`, `Stats`, `test_nats_messages.py`, `AliasStorage`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `DatabaseError` connect `DatabaseError` to `.get_instance`, `connection_manager.py`, `NPCDefinitionCRUDMixin`, `PydanticErrorHandler`, `test_player_event_handlers_room_left.py`, `test_async_persistence_room_loading.py`, `MythosMUDError`, `test_logging_processors.py`, `test_admin_shutdown_command.py`, `get_logger`, `test_connection_helpers_impl.py`, `test_skill_service.py`, `player_connection_setup.py`, `Any`, `test_rest_command.py`, `populate_test_npc_databases.py`, `RoomCacheLoader`, `test_item.py`, `test_command_validator.py`, `test_npc_models.py`, `MessageBroadcaster`, `test_connection_cleaner.py`, `test_npc_combat_handlers.py`, `subscribe_to_room_events_impl`, `MagicServiceCompletionMixin`, `handle_read_command`, `test_command_parser_helpers.py`, `SpellRegistry`, `ExplorationService`, `inventory_command_helpers.py`, `CreateItemInstanceInput`, `playerHandlers.ts`, `SpellLearningService`, `Player`, `test_container_persistence.py`, `test_command_exploration.py`, `PassiveLucidityFluxService`, `._prepare_sanitarium_respawn`, `test_player_service.py`, `MovementService`, `.check_level_up`, `RateLimiter`, `CombatDPSync`, `test_npc_service.py`, `shutdown_sequence.py`, `webhook`, `DraggablePanelResizeHandles.tsx`, `test_player_repository.py`, `test_connection_session_management.py`, `exceptions.py`, `test_player_presence_tracker.py`, `PassiveMobNPC`, `container_persistence.py`, `test_go_command.py`, `HealthRepository`, `_handle_admin_set_stat_command`, `aggro_threat.py`, `datetime`, `.from_dict`, `test_enhanced_logging_config.py`, `_JSONDict`, `AliasStorage`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 418 inferred relationships involving `ValidationError` (e.g. with `_CircuitBreakerResult` and `_convert_inventory_list_to_inventory_stacks()`) actually correct?**
  _`ValidationError` has 418 INFERRED edges - model-reasoned connections that need verification._
- **Are the 299 inferred relationships involving `DatabaseError` (e.g. with `_CircuitBreakerResult` and `EventDict`) actually correct?**
  _`DatabaseError` has 299 INFERRED edges - model-reasoned connections that need verification._
- **Are the 208 inferred relationships involving `LoggedHTTPException` (e.g. with `_CircuitBreakerResult` and `loot_all_items()`) actually correct?**
  _`LoggedHTTPException` has 208 INFERRED edges - model-reasoned connections that need verification._
- **Are the 68 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 68 INFERRED edges - model-reasoned connections that need verification._