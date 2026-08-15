# Graph Report - MythosMUD  (2026-08-14)

## Corpus Check
- 3278 files · ~2,939,357 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 53190 nodes · 99100 edges · 2360 communities (1715 shown, 645 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 7349 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9d529f81`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- DistributedEventBus
- ExceptionTracker
- test_spell_effects.py
- AliasStorage
- npc_definitions_api.py
- websocket_initial_state.py
- models/user.py
- test_command_moderation.py
- test_email_utils.py
- is_player_in_login_grace_period
- MythosMUDError
- Communities (355 total, 223 thin omitted)
- container_persistence/container_persistence.py
- test_command_parser_helpers.py
- container_endpoints_basic.py
- test_player_service_mutations.py
- server/models/game.py
- BaseCommand
- test_security_validator.py
- handle_transfer_items_exceptions
- test_command_communication.py
- test_websocket_handler_error_handling.py
- connection_manager_methods.py
- test_look_container.py
- WearableContainerServiceError
- test_player_disconnect_handlers.py
- ConnectionManager
- api/monitoring.py
- test_look_npc.py
- test_admin_commands.py
- test_container_persistence_extended_crud.py
- test_command_admin.py
- test_websocket_handler_core.py
- test_magic_commands.py
- command_result_text
- inventory_command_helpers.py
- Room
- test_lifecycle_periodic.py
- test_level_service.py
- ContainerComponent
- test_command_parser.py
- websocket_handler_commands.py
- test_connection_helpers_impl.py
- SkillUseLog
- ApplicationContainer
- NPCStartupService
- get_username_from_user
- test_behavior_engine.py
- test_connection_delegates.py
- CombatParticipant
- CombatParticipantData
- PlayerPositionService
- test_player_repository.py
- test_command_factories.py
- test_npc_utils.py
- ExplorationService
- ErrorContext
- Stats
- debrief_command.py
- CombatInstance
- RoomService
- lifespan.py
- test_command_factories_utility.py
- test_connection_statistics.py
- test_combat_attack_handler.py
- PlayerStateService
- PanelState
- test_command_combat.py
- DatabaseManager
- PayloadOptimizer
- api/player_effects.py
- test_lucidity_event_dispatcher.py
- alias_storage.py
- test_command_inventory.py
- NATSService
- test_combat_validator.py
- EldritchIcon.tsx
- request_with_app_container
- send_game_event
- .state
- test_lucidity_recovery_commands.py
- test_auth_utils.py
- Reporter
- test_npc_combat_handlers.py
- mock_connection_manager
- test_status_commands.py
- build_event
- test_npc_combat_integration_service.py
- test_container_helpers_inventory_find.py
- map/types.ts
- PlayerEventHandlerUtils
- test_look_room.py
- test_rescue_service.py
- NATSMessageBroker
- test_go_command.py
- test_movement_service.py
- multiplayer.ts
- test_nats_service.py
- test_admin_setlucidity_command.py
- config/models/__init__.py
- manual_dependency_analysis.py
- item_instance_persistence.py
- test_container_helpers_inventory_ops.py
- test_player_presence_tracker.py
- Lint Remediation Prompt - AI-Optimized Version
- test_message_handlers.py
- LoggedHTTPException
- test_room_sync_service.py
- RoomLoader
- test_channel_broadcasting_strategies.py
- test_circuit_breaker.py
- CorpseOverlay.tsx
- test_follow_service.py
- test_nats_broker.py
- test_websocket_handler_validation_errors.py
- UserManager
- test_look_player.py
- test_logging_utilities.py
- User
- test_combat_monitoring_service.py
- _NPCCombatIntegrationDeps
- test_nats_message_handler_chat.py
- run_flee_effect
- types/mythosTime.ts
- SchemaValidator
- test_command_factories_moderation.py
- test_chat_npc_system.py
- test_container_websocket_events.py
- MinimapRenderer
- MythosChronicle
- MythosTimeEventConsumer
- chatPanelRuntimeUtils.ts
- test_room_utils.py
- Any
- test_alias_commands.py
- WebSocketMessageValidator
- test_skill_service.py
- RoomDataCache
- asyncio
- server/schemas/__init__.py
- NPCCombatIntegrationService
- catatonia_check.py
- NATSError
- TrackedTaskManager
- test_rest_command.py
- test_user_schemas.py
- WearableContainerService
- PlayerRespawnService
- test_npc_combat_integration_class.py
- test_player_death_service.py
- admin_summon_command.py
- LootAllRequest
- PassiveMobNPC
- quality_fragmentation_ai_guardrails.py
- test_population_stats.py
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- test_connection_cleanup_methods.py
- talk_command.py
- legacy_error_sanitization.py
- test_websocket_messages.py
- get_logger
- test_room_subscription_manager_drops.py
- PlayerChannelPreferences
- test_validation.py
- rescue_commands.py
- test_combat_service_modules.py
- CombatConfiguration
- middleware
- chat_service.py
- test_command_magic.py
- test_wearable_container_service.py
- PartyService
- AggressiveMobNPC
- test_quest_service.py
- test_async_persistence_room_cache.py
- session_factory
- NATSMessageSubscriptionMixin
- CatatoniaRegistry
- mapUtils.ts
- test_occupant_formatter.py
- test_party_service.py
- UUID
- App.tsx
- test_container_persistence.py
- useGameClientV2Container.ts
- test_player_service.py
- Uplift Strategy
- TargetResolutionService
- QuestService
- fixtures/unit/__init__.py
- asyncio
- test_memory_profiler.py
- test_combat_event_publisher.py
- .load_room_data
- test_command_player_state.py
- IdleMovementHandler
- _handle_admin_set_stat_command
- test_error_logging.py
- combat_taunt.py
- Any
- DeadLetterQueue
- Commands
- CombatPersistenceHandler
- test_map_helpers.py
- test_inventory_helpers.py
- Any
- MonitoringDashboard
- EventHandler
- useAsciiMapState.ts
- FStringLoggingFixer
- MemoryMonitor
- fixtures/auth.ts
- NPCCombatUUIDMapping
- logging_file_setup.py
- _as_mgr
- safe_run_static
- gen_arena_migration_sql.py
- ResourceManager
- NATSSubjectManager
- api/player_respawn.py
- asyncio
- TestRoomDataFixer
- test_channel_commands.py
- test_connection_cleaner.py
- Any
- CombatMonitoringService
- TargetMatch
- asyncio
- ChatService
- test_rest_and_grace_period.py
- logoutHandler.ts
- QuestInstanceRepository
- collect_inventory.py
- ChatModeration
- resolve_weapon_attack_from_equipped
- EnvironmentalContainerLoader
- mapPageRenderer.tsx
- test_chat_pose_helpers.py
- asyncio.to_thread Offloading
- NPCCombatIntegrationBase
- maps.py
- RoomDataValidator
- apiTypeGuards.ts
- test_error_handling_middleware.py
- fix_markdown_blanks_around_lists.py
- _find_container_in_room
- LogAggregator
- PlayerNameExtractor
- TestErrorHandlers
- GameMechanicsService
- useDraggablePanelInteractions.ts
- Test Suite Refactoring Plan
- test_nats_messages.py
- FastAPI Code Review - Anti-Patterns and Best Practices
- test_logout_commands.py
- test_player_occupant_processor.py
- test_message_queue.py
- persistence/container_persistence.py
- test_game_tick_processing_async.py
- GameLogPanel.tsx
- NPCCombatIntegrationReadApi
- vim Best Practices and Coding Standards
- migration_examples.py
- test_npc_admin_commands.py
- RoomMapEditorRuntime.tsx
- test_room_service.py
- subzone_schema.json
- ChatChannelLoggerMixin
- player.ts
- DialogueDefinitionRepository
- NATSRetryHandler
- _MagicServiceCore
- FeatureFlagService
- test_memory_leak_metrics.py
- alias_schema.json
- Any
- RoomIDUtils
- admin_shutdown_command.py
- 🧪 MythosMUD E2E Testing Strategy
- PerformanceMonitor
- verify_enhanced_logging_compliance.py
- NPCCombatLucidity
- GameClientV2ContainerView.tsx
- ErrorMonitor
- Memory Leak Prevention System - Implementation Summary
- test_pattern_matcher.py
- compare_linting_results.py
- HealthService
- .__init__
- test_look_item_helpers.py
- models/combat.py
- test_room_subscription_manager_helpers.py
- test_command_processing.py
- useRespawnHandlers.ts
- handle_read_command
- inventory_get_command.py
- .move_to_room
- test_look_container_helpers.py
- Bug Investigator Subagent
- test_windows_safe_rotation.py
- skills.py
- TargetResolutionResult
- character-cleanup.ts
- WebSocketRequestContext
- E2E Test Suite AI Execution Improvements - Summary
- Async Persistence Migration Plan
- _find_container_wearable
- TestMonitoringEndpoints
- TestCombatMessagingService
- TestHierarchicalSchema
- test_combat_cleanup_handler.py
- Paired YAML and Env Config Tuples
- Execution Steps
- look_container.py
- test_combat_persistence_handler_persistence.py
- get_async_session
- HallucinationFrequencyService
- AliasGraph
- _format_container_display
- ValidationError
- Graceful Degradation Planning
- SchemaValidator
- NATS Complete Remediation Summary
- PostgreSQL & SQL Audit Report
- File-by-File Changes
- quest_chat_notify.py
- chatPanelRefactoredDerived.ts
- Test Suite Analyzer Subagent
- map_minimap.py
- TestNPCCombatRewards
- PlayerCombatService
- Container System
- test_websocket_handler_coverage_gaps.py
- ZoneConfiguration
- look_command.py
- utils/layout.ts
- multiplayer-browser-helpers.js
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- Structured Error Logging
- emotes.schema.json
- test_corpse_lifecycle_service.py
- onboard/SKILL.md
- test_optimized_security_validator.py
- message_handler_factory.py
- generate_sql.mjs
- ._build_player_attacked_event
- roomHandlers.ts
- Enhanced Logging Migration Complete
- Migration Final Report
- Structlog Implementation Plan
- .get_instance
- combat_attack.py
- MythosLoginForm.tsx
- test_command_alias.py
- PlayerRepositoryProtocol
- Test Pruning Candidates - Detailed List
- handle_emote_command
- CombatCommandHandler
- EventPublisher
- Profession
- RoomCacheLoader
- test_goto_helpers.py
- skills_commands.py
- Performance Profiler Subagent
- Three-Column Game UI Layout
- DialogueEditorPage.tsx
- e2e-bootstrap.ts
- GameTerminalContext.test.tsx
- utils/config.ts
- authenticated.ts
- Coverage Improvement Summary - Plan 2 Execution
- test_postgres_adapter.py
- Memory Leak Audit Report
- test_audit_logger.py
- command_handler_unified.py
- websocket_helpers.py
- test_movement_monitor.py
- command.py
- test_shutdown_sequence.py
- useRoomEditModal.ts
- test_rate_limiter_utils.py
- Phase 3, Task 3.2: NATS Subject Manager Usage Review
- MythosTickScheduler
- NATS Anti-Patterns and Best Practices Review
- test_connection_error_methods.py
- Spell
- inventory_equip_command.py
- Migration Strategy
- ChatPoseManager
- test_container_query_helpers_async.py
- devDependencies
- TestCombatConfigurationService
- test_communication_commands_flows.py
- test_quest_service_collect.py
- retry.py
- Any
- test_health_monitor.py
- Persistence Layer Refactoring - COMPLETE ✅
- Player
- emote_schema.json
- Incremental Upgrade Strategy (Report)
- Persistence Layer Refactoring Summary
- FeedbackManager
- Architecture Remediation Implementation Summary
- Feature Requirements Document: Random Stats Generator
- StyleGuideSections.tsx
- ConnectionCleaner
- ValidationRule
- test_player_preferences_service.py
- npc_database.py
- stateNormalization.ts
- start_grace_period
- Dependency Upgrade Strategy Specification
- deprecated_patterns.py
- rescue_service.py
- Security Auditor Subagent
- NATSConnectionStateMachine
- real_time.py
- test_dependency_analysis.py
- handle_teach_command
- test_who_commands.py
- register_default_reactions_for_npc
- Advanced Chat Channels Specification
- test_chat_logger.py
- properties
- MythosMUD Dependency Upgrade Strategy - Implementation Summary
- testing_examples.py
- compilerOptions
- Authoritative Environment DML
- Execution Steps
- Execution Steps
- Async Audit Executive Summary
- inventory_commands.py
- Critical Coverage Gaps
- Communities (19 total, 4 thin omitted)
- projectorRoom.ts
- security.ts
- generate_html_visualization.py
- Execution Steps
- combat_service_npc.py
- channel_broadcasting_strategies.py
- Migration 019 Testing Guide
- PlayerService
- test_flee_command.py
- PARALLEL EXECUTION RESULTS (2025-11-05)
- Hierarchical Test Structure
- test_user_manager.py
- RoomEventHandler
- websocket_handler.py
- SkillAssignmentScreen.tsx
- multiplayer-colocated.ts
- Environment Contamination Audit Report
- Complexity Checking Alignment: Ruff C901 vs Pylint
- Stop-MythosMudProjectProcessTree
- Execution Steps
- The Toolkit
- test_npc_service.py
- Dependency Upgrade Strategy Agent
- useThemeContext.ts
- multiplayer-browser-helpers.bundle.js
- codacy.yaml Tool Manifest
- Pydantic Code Review - feature/sqlite-to-postgresql Branch
- GameTerminal.tsx
- test_nats_message_handler.py
- validate.py
- get_admin_auth_service
- MemoryThresholdMonitor
- ui-v2/types.ts
- TestVerificationSqlUsersPlayers
- MythosPanel.tsx
- RoomInfoPanel.tsx
- test_nats_retry_handler.py
- Scenario 20 Logout Errors
- test_magic_service.py
- MessageBroadcaster
- container_helpers_inventory_display.py
- quest_commands.py
- static_data/package.json
- admin_teleport_commands.py
- Lint Remediation Prompt - AI-Optimized Version
- ADR-012: python-statemachine for Backend Connection FSM
- compilerOptions
- enum
- WebSocket Best Practices Compliance
- properties
- EdgeDetailsPanel.tsx
- Main Foyer Starting Room
- gameStore.ts
- HealthRepository
- PostgresConnection
- properties
- DatabaseError
- Execution Steps
- Prometheus Configuration
- EmoteService
- test_room_occupant_manager.py
- test_message_broadcaster.py
- load_world_seed.py
- edgeModalLogic.ts
- ReactNodeUpgradeAnalyzer
- test_combat_flee_helpers.py
- player_service
- useWebSocketConnection.ts
- Cursor Subagents Overview
- validate_room_data
- Multiplayer Architecture Planning
- test_combat_death_handler.py
- room_validator/tests/conftest.py
- Lint Remediation Prompt - AI-Optimized Version
- Execution Steps
- AnyIO vs Asyncio: High-Level Comparison and Decision Guide
- ADR-003 Dual Event Systems EventBus NATS
- MovementService
- properties
- Pre-commit Logging Validation
- test_admin_shutdown_command.py
- test_room_subscription_manager_npcs.py
- test_security_headers.py
- Per-Recipient Whisper Rate Limit
- usePanelContext.ts
- Any
- Phase 1: Core Separation
- Disconnect Grace Period and Rest Command
- MythosMUD UI Component Library
- player_connection_setup.py
- Phase 2: Enhanced Features
- type
- generate_sql.mjs
- PrototypeRegistry
- Phase 2: Qualitative Analysis Results
- WebSocket Code Review - Branch: feature/sqlite-to-postgresql
- GameTickService
- LRUCache
- Dual Connection Monitoring Guide
- TestPathValidator
- test_event_bus.py
- server/tests/conftest.py
- HealthMonitor
- optimized_validate_player_name
- optimized_security_validator.py
- PanelContextRuntime.tsx
- RoomInfo.tsx
- test_admin_teleport_commands.py
- MessageBatcher
- required
- schemas/unified_room_schema.json
- FollowService
- Communities (11 total, 0 thin omitted)
- Test Server Remediation Prompt - Cursor Executable Version
- required
- Chat Panel Separation Implementation Tasks
- Communities (11 total, 0 thin omitted)
- test_container_persistence_sql_injection.py
- MPRegenerationService
- AnyIO Code Review - Anti-Patterns and Issues
- ChatLogger
- test_inventory_mutation_guard.py
- Communities (10 total, 0 thin omitted)
- 🎯 Async Remediation - Final Report
- establish_websocket_connection
- NPCCombatDataProvider
- NATS Subject Patterns
- NATS Code Review - Branch: feature/sqlite-to-postgresql
- performance.test.tsx
- Persistence Layer Extraction - COMPLETE ✅
- ChannelBroadcastingStrategyFactory
- UnknownChannelStrategy
- verify_linting_parity.py
- CoordinateGenerator
- properties
- 🔴 CRITICAL ISSUES
- .claude/hooks/record_edited_file.py
- asyncio
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- Phase 3: Polish and Optimization
- Phase 4: Testing and Refinement
- command_handler_v2
- test_lifespan_event_subscriptions.py
- fix_fstring_logging.py
- Tiered Test Coverage Strategy
- TestLogoutCommand
- properties
- Path
- AsyncPersistenceLayer Pattern
- LucidityFluxService
- test_chat_moderation.py
- 3. REFACTOR Findings (935 findings)
- test_chat_nats_publisher.py
- Whisper Location Independence
- properties
- Communities (10 total, 2 thin omitted)
- InventorySchemaValidationError
- test_statistics_aggregator.py
- properties
- MapPerformanceMonitor
- useMythosAppActions.ts
- properties
- LogAnalyzer
- properties
- required
- test_shopkeeper_npc.py
- Test Coverage Summary: Disconnect Grace Period & Rest Command
- CoordinateValidator
- RoomCacheService
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)
- deque
- test_command_processor.py
- server/dependencies.py
- test_npc_startup_service.py
- test_player_event_handlers_utils.py
- test_combat_persistence_handler_events.py
- test_chat_validator.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)
- room_hierarchy_schema.json
- GridLayoutManager.tsx
- PydanticErrorHandler
- Game Subsystem Design Documents
- REQUIRED TOOL USAGE PATTERN
- CircuitBreaker Implementation Planning Document
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)
- properties
- properties
- ContainerData
- multiplayer-playwright-testing.md
- Mypy Type Checking Remediation Prompt - AI-Optimized Version
- get_config
- PrototypeRegistryError
- Movement Subsystem Design
- load_test_10_players.spec.ts
- enum
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)
- properties
- days
- enum
- mock_container
- Comprehensive System Audit
- player_effect_repository.py
- NPCCommunicationIntegration
- Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch
- Security Implementation
- test_argon2_utils.py
- migrate_combat_data.py
- PersonalMessageSender
- PeriodicOrphanAuditor
- should_spawn_npc
- TestMinimapExplorationInvestigationDoc
- test_player_event_handlers_room.py
- test_inventory_command_prototype.py
- PostgresRow
- CORSConfig
- RateLimiter
- get_room_environment
- optimized_validate_action_content
- optimized_validate_alias_name
- PlayerGuidFormatter
- optimized_sanitize_unicode_input
- optimized_validate_security_comprehensive
- TestRunner
- asyncio
- test_lucidity_command_disruption.py
- enum
- weather_patterns
- run-playwright-tests.js
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- required
- SQLAlchemyAsyncLinter
- CombatValidator
- applies_to
- required
- Technical Implementation
- Implementation Notes
- extract_player_name
- test_npc_event_handlers_helpers.py
- errorHandler.ts
- test_party_commands.py
- zone_schema.json
- test_connection_establishment.py
- required
- quality_fragmentation_graph.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)
- Async Facades Implementation - COMPLETE ✅
- attach_compatibility_properties
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)
- format_markdown_file
- migrate_rooms.py
- run-vitest.js
- usePerformanceMonitor.ts
- holidays.schema.json
- npc_schedules.schema.json
- 1. Enhanced ChatPanel (New Chat Input Panel)
- Implementation Phases
- Migration 019: Complete Implementation Summary
- enum
- enum
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)
- enum
- holiday.schema.json
- schedule.schema.json
- Environment Configuration Refactoring
- required
- required
- validate.mjs
- test_load_world_seed.py
- MythosMUD Worldbuilding Source
- realtime/realtime.py
- Migration 019 Verification Report
- ContainerServiceError
- test_player_event_handlers_room_left.py
- Phase 4: Recommendations
- test_async_persistence_room_loading.py
- UUID
- Design Critique
- plane
- test_combat_messaging_integration.py
- test_rate_limiter.py
- test_cache_service.py
- chat_message.py
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- validate_secure_path
- MetricsCollector
- optimized_validate_filter_name
- optimized_validate_target_player
- optimized_validate_help_topic
- verify_migration.py
- optimized_comprehensive_sanitize_input
- required
- useGridLayout.ts
- Geography Overview.md
- Chat Panel Separation Specification
- Code Review: Import Analysis and Anti-Patterns
- enum
- enum
- room_validator/schemas/unified_room_schema.json
- properties
- 🔧 COMMON FIX TEMPLATES
- Who Command Enhancement
- 🔧 COMMON FIX TEMPLATES
- test_quality_fragmentation_guard.py
- E2E Tests Playwright
- compilerOptions
- compilerOptions
- 🔧 COMMON FIX TEMPLATES
- Common Test Failure Categories
- FAILURE PATTERN RECOGNITION
- MUD Disconnect Grace Period & Rest Command: Industry Comparison
- bonus_tags
- ComprehensiveLoggingMiddleware
- items
- Bounded Contexts and Service Boundaries
- asyncio.run Anti-Pattern
- Implementation Details
- Client Layout Baseline
- ContainerRepository
- ContainerRepository and ItemRepository: Review and Full Async Migration Plan
- magic_service_completion.py
- Quest System Features
- Testing Guide
- test_combat_service.py
- Documentation Updates - ConnectionManager Refactoring
- Domain Model Anemic Anti-Pattern Audit
- test_security_utils.py
- MessageHandlerFactory
- TestNPCCombatLifecycle
- _format_room_posture_message
- ._cleanup_player_mutes
- container
- Local Channel System
- fix_suppression_alignment.py
- identify_critical_code.py
- AdminActionsLogger
- Delight Techniques
- holidays
- schedules
- Asyncio Code Review - feature/sqlite-to-postgresql Branch
- _process_mortally_wounded_player
- StatisticsAggregator
- asyncio
- Ruff to Pylint Rule Mapping
- SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch
- test_players_quests.py
- MythosMUD Test Suite Modernization Plan
- Codebase Explorer Subagent
- Implement Animations
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)
- Updated Coverage Targets
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)
- Polish Systematically
- record_edited_file.py
- Command Handler Patterns
- database_config_helpers.py
- party_service.py
- ChatMessage
- Playwright MCP Primary Testing Tool
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)
- AsciiMapRenderer
- test_game_state_provider.py
- test_metrics.py
- .check_bidirectional_connections
- test_lifespan_shutdown.py
- CombatService
- Introduce Color Strategically
- test_occupants.py
- audit_suppressions.py
- fix_markdown_line_length.py
- populate_npc_sample_data.py
- NPCDied
- test_users_current_user_logging.py
- start_hour
- test_connection_session_management.py
- Implement Adaptations
- RoomRepository
- Improve Copy Systematically
- scripts
- waitForMessage
- compilerOptions
- 🎯 Test Categories
- NATS Medium-Priority Remediation Summary
- NATS Anti-Patterns Remediation Summary
- ClientLogger
- Color & Contrast
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)
- ConnectionPanel.tsx
- global-teardown.ts
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)
- ConnectionManager Refactoring Summary
- Phase 2: Categorize and Prioritize Mypy Issues
- Phase 5: Fix Implementation Patterns
- 4. Common Fix Patterns
- DML Migrations
- UX Writing
- LoggingPatternLinter
- enum
- Arkham City (MOTD Zone)
- UI/UX Considerations
- MythosMUD Database Placement
- CommandRateLimiter
- fix_markdown_common_issues.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)
- 3. Simplified CommandPanel
- Implementation Phases
- handle_time_command
- SpellEffectType
- extract_room_id_from_npc
- UpgradeImplementationPlan
- PlayerRespawnWrapper
- GET /v1/monitoring/health
- items
- item_prototype.schema.json
- description
- 2025_01_XX_convert_players_player_id_to_uuid.py
- 2025_11_21_convert_players_player_id_to_uuid.py
- 2025_11_25_normalize_container_schema.py
- 2025_11_25_remove_get_container_contents_json_procedure.py
- 2025_11_25_remove_items_json_column.py
- 2025_11_26_ensure_item_instance_foreign_keys.py
- 2026_02_09_add_player_effects_table.py
- ApplicationContainer Structure Analysis and Domain-Specific Split Proposal
- 2026_02_18_add_player_skills_table.py
- 2026_02_18_add_profession_modifiers_columns.py
- 2026_02_19_add_quest_tables.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)
- 2026_02_19_seed_quest_leave_the_tutorial.py
- test_command_validator.py
- 2026_02_26_add_arena_zone_type.py
- rename_players_to_population.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)
- DomainError
- CI Environment Alignment
- GitHub Actions Runner Parity Container
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)
- ConnectionErrorHandler
- test_look_item.py
- Changes by document
- Lizard Complexity Analysis Findings
- Real-Time Architecture
- test_grype.py
- description
- name
- MockEventClass
- VirtualizedMessageList.tsx
- 2. Mythos Time Model Draft
- 🔄 COMMON SCENARIOS AND SOLUTIONS
- 🔍 DEBUGGING GUIDE
- 🚀 OPTIMIZATION TIPS
- MessageBroker
- 7. Common Test Failure Solutions
- PostgresCursor
- NPCMovementIntegration
- 9. Test Maintenance Best Practices
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- 2. Auto-Attack During Grace Period
- 3. Grace Period Visibility & Messaging
- 4. Rest/Quit Command During Combat
- 5. Rest Command Countdown Duration
- 6. Rest Location (Inn/Hotel) Behavior
- 7. Reconnection During Grace Period
- combat_loader.py
- 8. Grace Period After Intentional Disconnect
- 9. Command Blocking During Grace Period
- Recommendations Summary
- Code Graph Entry
- DML Migrations Apply Paths
- Cosmic Horror.md
- GameConfig
- day
- duration_hours
- RetryConfig
- Spatial Design
- days
- effects
- end_hour
- start_hour
- exits
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)
- Migration Considerations
- Mandatory AI Execution Contract
- Success Criteria
- Risk Assessment
- Testing Strategy
- Phase 2: Database Layer Integration
- Phase 3: Real-Time Communication Protection
- Phase 4: File System Operations
- Phase 6: Monitoring and Observability
- Scenario 22 Administrative Summon
- Future Enhancements
- Monitoring and Alerting
- Success Criteria
- Shared JSON schemas
- init_npc_database.py
- Testing Strategy
- fixtures/shared/__init__.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)
- BehaviorEngine
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)
- validate_admin_permission
- Typography
- fix_markdown_code_block_style.py
- day
- holiday
- duration_hours
- month
- factory.py
- run_quality_fragmentation_guard.py
- long_description
- prototype_id
- short_description
- ConnectionManager Modular Architecture
- rest_location
- Enhanced Logging Quick Reference
- sub_zone
- zone
- NumPy Code Review - MythosMUD Codebase
- start_server.ps1
- MythosMUD Code Quality Targets for AI
- Python Model Updates Required for Migration 019
- Skill: Create a New Worktree for a Task
- Transaction Boundaries Audit
- main
- CircuitState
- asyncio
- test_validate_secure_path_path_traversal_commonpath
- test_asyncio_run_guardrails.py
- description
- exits
- name
- plane
- fix_file
- jackson_linter.py
- RoomFilenameMigrator
- .call
- RetryableMessage
- exits
- plane
- zone
- npc_spawn_modifier
- special_rules
- Client Security and Privacy Policies
- PlayerPanel.tsx
- RoomPanel.tsx
- LoginGracePeriodBanner.tsx
- mythosTheme.ts
- multiplayer-browser-helpers.d.ts
- Expansion Backlog (Raw)
- 1774539086359-useMythosAppState.ts
- 🚨 AI ERROR HANDLING
- Event Ownership Matrix
- Step-by-Step Remediation Process
- NPCCacheService
- Graphify Code Graph
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)
- Chaosium CoC Catalog
- plane
- AI Development Workflow
- Architecture Overview
- Any
- setup.ts
- Frontend Design Skill
- weight
- npc_instances_api.py
- asyncio
- test_aggressive_mob_npc.py
- _as_ws
- asyncio
- fix_markdown_file
- analyze-product.md
- create-spec.md
- analyze_coverage_gaps.py
- _apply_arena_seed_patch.py
- create-tasks.md
- execute-tasks.md
- test_shutdown_process_termination.py
- tailwindcss
- apply_communication_dampening
- typescript
- playwright.runtime.config.ts
- deps/package.json
- LLM Wiki Pattern.md
- Geography and Major Locations.md
- db/migrations/README.md
- Aggro and Threat System Design
- MOTD Sacred Styling
- Realtime Messaging Subsystem
- NPC Startup Duplication Analysis
- Gladiator Ring (Arena) Implementation Plan
- fixture
- Room Subscription Timing Race
- Deprecated get_async_persistence Global
- schemas/__init__.py
- High-Risk Major Package Updates
- Codacy configuration
- constants/__init__.py
- asyncio
- test_ascii_map_renderer_exits.py
- .measure_model_deserialization
- entities/__init__.py
- domain/events/__init__.py
- domain/__init__.py
- domain/repositories/__init__.py
- domain/services/__init__.py
- value_objects/__init__.py
- server/game/magic/__init__.py
- load_motd
- Generate Comprehensive Report
- is_safe_filename
- POSTGRES_SEARCH_PATH for invites schema
- Optimization Strategy
- test_utility_commands_whoami.py
- _validate_app_state_for_status_effects
- persistence/utils/__init__.py
- _NPCCombatIntegrationValidationDeps
- server/structured_logging/__init__.py
- Pydantic Anti-Patterns Remediation (3ee32154)
- server/tests/__init__.py
- command_handler_unified/__init__.py
- ✅ Async Remediation Complete
- test_websocket_handler_rate_limit.py
- Phase 2 Async Persistence Migration - Status Update
- parse_shutdown_parameters
- Quick Start: Running E2E Tests
- asyncio
- Implementation Phases
- process_room_files
- validate_codacy_coverage_gate.py
- test_check_no_production_assert.py
- ._handle_exception
- CacheManager
- messageHandlers.ts
- _find_item_in_equipped
- Any
- test_admin_auth_service.py
- test_player_spell_repository.py
- unit/container_persistence/__init__.py
- unit/game/magic/__init__.py
- asyncio
- extract_definition_id_from_npc
- fixture
- AGENTS.md agent instructions
- handle_new_game_session_impl
- Architecture Decision Records Index
- Fixture Optimization Complete
- _find_item_in_inventory
- test_invite_schemas.py
- check_no_production_assert.py
- executeCommand
- overrides
- test_command_service.py
- test_performance_tracker.py
- Cursor Workflows
- NPCOccupantProcessor
- Async Persistence Migration Tracker
- SQLAlchemy Async Best Practices
- analyze_log_file
- Migration 019: Ready for Deployment
- _meta
- nats_exceptions.py
- test_world_loader.py
- 🟢 MEDIUM PRIORITY IMPROVEMENTS
- Critical Insights
- magic_service.py
- Test Suite Quality Audit - Executive Summary
- correct_patterns.py
- TestValidatorIntegration
- HolidayService
- CommunicationIntegrationProtocol
- rest_countdown_task.py
- Server Realtime Module
- lifespan_magic.py
- add_suppression_to_file
- field_validator
- find_fstring_logging_violations
- lint_sql_guardrails.py
- Improve Layout Systematically
- Simplify the Design
- _utc_now
- CircuitBreaker
- test_mp_regeneration_service.py
- asyncio
- test_process_exit_rows_debug_logging
- asyncio
- test_process_room_rows_with_full_room_id
- Asynchronous Code Audit - December 3, 2025
- Easy Coverage Wins - Quick Analysis
- Test Value Distribution Chart
- test_zone_config_loader.py
- test_game_tick_processing.py
- asyncio
- test_process_exit_rows_empty_list
- test_process_exit_rows_multiple_exits_same_room
- Players API Code Coverage Plan
- sub_zone
- test_profession_service.py
- unit/infrastructure/__init__.py
- test_process_exit_rows_zone_single_part
- idle_movement_handler
- rules
- dependencies
- test_process_room_rows_with_partial_room_id
- test_persistence_container_persistence.py
- test_build_room_objects_without_environment_in_attributes
- asyncio
- asyncio
- TestValidatorComponents
- Azotottal.md
- PlayerOccupantProcessor
- test_process_room_rows_with_none_attributes
- test_process_room_rows_zone_without_slash
- .validate_combat_command
- server/services/__init__.py
- Earth Plane
- compilerOptions
- Actionable Recommendations
- Execution Timeline
- MockPersistence
- Amplify the Design
- Interaction Design
- Hardening Dimensions
- Async Remediation Summary - December 3, 2025
- MythosMUD LLM Wiki (Obsidian)
- Migration Guide: From Default Logging to Enhanced Logging
- properties
- properties
- properties
- main
- main
- SyntaxErrorFixer
- test_npc_combat_integration_service_player_attacks.py
- ADR-018: New Game Session vs Grace Reconnect
- CombatAuditLogger
- unit/middleware/__init__.py
- unit/monitoring/__init__.py
- unit/persistence/__init__.py
- unit/realtime/integration/__init__.py
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- Migration Roadmap
- asyncio
- CacheService
- PhantomHostileService
- MotdInterstitialScreen.tsx
- _format_container_contents
- PlayerPreferencesService
- _is_websocket_connected
- test_monitoring_init.py
- Async Code Review - Post Phase 2 Migration
- ✅ Best Practices Compliance
- LLM Wiki Vault Schema
- test_build_room_objects_with_exits
- generate_schema_from_dev.ps1
- 🔍 Specific File Reviews
- Enhanced Logging Best Practices for MythosMUD
- Nameless Horrors - 2nd Edition (source summary)
- S. Petersen's Field Guide to Lovecraftian Horrors (source summary)
- test_npc_spawn_rules_api.py
- eslint.config.js
- TaskRegistry
- extract_npc_metadata
- Test Suite Quality Audit Report
- parse_json_field
- npc_combat_grace.py
- create_error_context
- ._trim_samples
- .load_player_mutes
- Cursor Hooks Development Plan
- event_bus
- debugLogger
- test_publish_attack_event_emits_npc_attacked
- test_connection_models.py
- PlayerDeathService
- Multi-Character Support System
- test_quest_instance_repository.py
- Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES
- grype.py
- main
- Recommended Test Additions
- Appendices
- MythosMUD Testing Strategy (Greenfield Suite)
- test_validate_codacy_coverage_gate.py
- Dialogue Content Tools (Content Creators)
- snapshot_chaosium_graphify.ps1
- test_message_filtering.py
- _FakeNPCService
- test_player_repository_room.py
- cached
- LoggedException
- .change_position
- test_inventory_mutation_guard_async.py
- CircuitBreaker
- test_player_event_handlers_respawn.py
- eslint
- eslint-plugin-jsx-a11y
- happy-dom
- markdownlint-cli
- CI Workflow
- Agent OS
- patch-package
- @playwright/test
- @testing-library/dom
- @testing-library/react
- @testing-library/user-event
- mcp.json
- Owner and App Roles Per Environment
- vite
- test_websocket_handler_validation.py
- CombatEventPublisherProtocol
- Enhanced Logging Guide
- test_subscribe_invalid_event_type
- ._compose_memory_stats
- test_ascii_map_renderer_grid.py
- 🟡 HIGH PRIORITY ISSUES
- Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE
- PR Coverage Thresholds
- 🔴 Anti-Patterns Check (Critical)
- add_hashed_password_column.py
- Persistence Layer Async Migration Plan
- Any
- rename_invites_columns.py
- Python Code Coverage Status
- **~25-30% provide CRITICAL coverage**
- UUID
- Net Impact Summary
- test_npc_combat_integration_service_npc_aggro.py
- test_build_room_objects_with_non_dict_attributes
- bench_cache.py
- run_make_stages.py
- Whisper Channel System
- properties
- _StubPlayerRepo
- properties
- analyze_file
- main
- main
- main
- lucidity_trigger_handlers.py
- mp_regeneration_service
- _errors_len
- CommandService
- MemoryProfiler
- Responsive Design
- Refine the Design
- Teach Impeccable Skill
- useMythosAppState.ts
- Improve Typography Systematically
- ✅ Verified Already Implemented
- API Endpoints (Phase 2)
- ✅ Phase 2 Async Persistence Migration - COMPLETE
- UUID
- initialize_components
- NPCCombatIntegration
- SystemAdminChannelStrategy
- Client Updates System Audit
- AttributeError
- SecureBaseModel
- asyncio
- test_run_make_stages.py
- Any
- Aggro and Threat System Implementation Plan
- ✅ POSITIVE FINDINGS
- 🔴 CRITICAL ISSUES
- unit/services/nats_subject_manager/__init__.py
- messaging_integration
- ✅ Positive Findings
- 🚫 Anti-Patterns NOT Found (Good!)
- Entries
- Migration Workflow (Per File)
- Recommended Decision
- 3.3 Value Distribution Calculation
- Projected Optimization Impact
- ._build_connection_stats
- gh-stack (MythosMUD)
- Mypy Type Checking Remediation Prompt - AI-Optimized Version
- Authoritative DML Seed Data
- .__init__
- items
- 🔍 Anti-Pattern Check
- 📚 Documentation Created
- Summary (from Codacy UI snapshot)
- Core Logging Principles
- Common Mistakes and How to Fix Them
- Python Coverage Targets
- Enhanced Logging Features
- Security Environment Variables
- Log Levels and Usage
- Enhanced Logging Migration Report
- Mythos Holiday Candidates
- 💡 Key Improvements
- PostgreSQL Procedures Migration - Audit Spreadsheet
- Real-Time Communication (WebSocket)
- Implementation Approach Decision
- test_lifecycle_respawn.py
- Backward Compatibility Strategy
- rename_used_to_is_active.py
- Test Suite Analysis
- Modern Testing Patterns
- Test Modernization Checklist
- Testing Requirements
- Test Suite Optimization Roadmap
- Phase 5: Strategic Additions (Week 5)
- AsyncPersistenceLayer
- Measurement and Validation
- JSON Schema Validation
- _run_dialogue_ddl
- bench_cache_professions.py
- mock_app
- check_file
- lucidity_migration.py
- Party
- ._attack_target_impl
- npc_utils.py
- players/player_respawn.py
- _FakeMessageQueue
- TestResolveExitTarget
- test_process_exit_rows_with_partial_room_ids
- 🎓 Best Practice Examples to Share
- test_load_room_cache_with_rooms_logs_sample_ids
- Common Conversion Patterns
- TestHorizontalExitCharBetween
- Gotchas & Solutions
- 🎭 Closing Remarks
- Financial Impact (If You're Tracking Dev Time)
- Phase 1: Quick Wins (Week 1)
- Church of Sunyata.md
- Phase 2: Infrastructure Test Reduction (Week 2)
- Phase 4: Test Consolidation (Week 4)
- Phase 6: Long-Term Optimizations (Ongoing)
- Phase 1: Quantitative Analysis Results
- Dark Young of Shub-Niggurath.md
- Dimensional Shambler.md
- Summary: Test Quality Metrics
- Risk Assessment and Mitigation
- Map Regression Tests Proposal
- Configuration Files Reference
- A Cold Fire Within (source summary)
- Alone Against the Dark (source summary)
- Workflows
- Alone Against the Frost (source summary)
- .claude/commands/multiplayer-playwright-testing.md
- Alone against the Tide (source summary)
- NPCActionMessage
- spell_effects_support.py
- client/package.json
- include
- vite.userConfig.ts
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- Berlin - The Wicked City (source summary)
- main
- mythos_dev mythos_unit mythos_e2e Databases
- main
- Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)
- Motion Design
- Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)
- _collect_python_public_defs_and_tiny
- Call of Cthulhu Investigator Handbook 7th Edition (source summary)
- handle_system_command
- Call of Cthulhu Keeper Tips (source summary)
- test_users.py
- Frontend Aesthetics Guidelines
- Call of Cthulhu Starter Set (source summary)
- Call of Cthulhu_ The Coloring Book (source summary)
- ._get_vertical_exit_char
- CommandProcessor
- event_handler
- mock_utils
- MythosMUD Server Runbook Skill
- overrides
- 1. Component Refactoring
- player_event_handler_utils
- asyncio
- .execute_idle_movement
- webhook
- character_sheets (source summary)
- Room Pathing Validator Implementation Spec
- validator.py CLI
- Cthulhu Dark Ages - 3rd Edition (source summary)
- Dead Light and Other Dark Turns (source summary)
- _filter_lines
- fix_room_references
- player_inventory_migration.py
- Does Love Forgive_ (source summary)
- run_bug_prevention_tests.ps1
- Doors to Darkness (source summary)
- Down Darker Trails (source summary)
- test_logging_handlers.py
- Gateways to Terror (source summary)
- Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)
- Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)
- The Grand Grimoire of Cthulhu Mythos Magic (source summary)
- Worktree Plan Metadata
- The Malleus Monstrorum Keeper Deck (source summary)
- fixture
- zone
- persistence/container_helpers.py
- ItemPrototypeModel
- HADS tooling (MythosMUD)
- RateLimiter
- .extract_command_data
- Chaosium graphify snapshot - A Cold Fire Within
- cli.sh
- Chaosium graphify snapshot - Alone Against the Dark
- Chaosium graphify snapshot - Alone Against the Frost
- Chaosium graphify snapshot - Alone against the Tide
- Chaosium graphify snapshot - Berlin - The Wicked City
- Chaosium graphify snapshot - Call of Cthulhu 7th Edition - Keeper's Rulebook
- Chaosium graphify snapshot - Call of Cthulhu 7th Edition Keeper Screen Pack
- Chaosium graphify snapshot - Call of Cthulhu Investigator Handbook 7th Edition
- Chaosium graphify snapshot - Call of Cthulhu Keeper Tips
- Chaosium graphify snapshot - Call of Cthulhu Starter Set
- Chaosium graphify snapshot - Call of Cthulhu_ The Coloring Book
- unit/structured_logging/__init__.py
- unit/validators/__init__.py
- room_validator/tests/__init__.py
- Vite HTML Entry
- Client Layer Layout
- Zustand Stores
- Codacy CLI via WSL on Windows
- MythosMUD Wiki Index
- R'lyeh
- Mythos Magic
- Whisper NATS Subject Bug Fix
- MythosMUD Obsidian Vault
- Event-Sourced Projector
- make verify-schema
- Configuration Refactoring Complete
- Simultaneous WebSocket and SSE
- Impeccable design context
- Dual Connection System Tasks
- Dual Connection Troubleshooting Guide
- Dual Command Processing Architecture
- PLANNING.md Single Source of Truth
- Legacy Test File Consolidation
- Test Migration Validation
- ensure_directory_exists
- Chaosium graphify snapshot - character_sheets
- Test Refactoring Executive Summary
- Any
- migrate_file
- gh-stack
- Chaosium graphify snapshot - Cthulhu Dark Ages - 3rd Edition
- Step 2: Ask UX-Focused Questions
- Whisper System Production-Ready
- Structured Logging Correct Patterns
- Chaosium graphify snapshot - Dead Light and Other Dark Turns
- mythosmud
- main
- apply_migration
- HealthRepository
- RoomRepository
- Memory Leak Monitoring Endpoints
- PostgreSQL Player Persistence
- World Loading
- invites table
- Mythos-themed invite codes
- jsonschema dependency
- Chaosium graphify snapshot - Does Love Forgive_
- sub_zone
- Chaosium graphify snapshot - Doors to Darkness
- Chaosium graphify snapshot - Down Darker Trails
- Chaosium graphify snapshot - Gateways to Terror
- Persistence Repository Layer
- Chaosium graphify snapshot - Malleus Monstrorum - Cthulhu Mythos Bestiary
- Chaosium graphify snapshot - Mansions of Madness_ Vol 1 - Behind Closed Doors
- Chaosium graphify snapshot - Nameless Horrors - 2nd Edition
- Chaosium graphify snapshot - Petersen's Abominations
- Chaosium graphify snapshot - Pulp Cthulhu (7th edition Call of Cthulhu)
- test_logging_processors.py
- Chaosium graphify snapshot - Reign of Terror
- Chaosium graphify snapshot - S. Petersen's Field Guide to Lovecraftian Horrors
- Chaosium graphify snapshot - The Grand Grimoire of Cthulhu Mythos Magic
- Lucidity System Expansion Scenarios
- Chaosium graphify snapshot - The Malleus Monstrorum Keeper Deck
- Petersen's Abominations (source summary)
- Pulp Cthulhu (7th edition Call of Cthulhu) (source summary)
- Reign of Terror (source summary)
- message-match.test.ts
- calculate_notification_times
- 📚 REFERENCES AND RESOURCES
- 📊 METRICS AND SUCCESS CRITERIA
- WebSocket-Only Migration
- NPCThreadManager
- intersection_schema.json
- 🚀 DEPLOYMENT STRATEGY
- 🔧 Code Changes Made
- room_schema.json
- main
- 🏆 Achievement Highlights
- Attack Command Not Starting Combat
- Second NPC Combat And Linkdead Findings
- Multi-Word Spell Name Parsing Failure
- Respawn Subsystem
- 🎭 Closing Remarks
- Chat Panel
- graceful_degradation
- test_room_subscription_manager.py
- Dietrich Zann.md
- Flying Polyp.md
- Fungi from Yuggoth.md
- Ghoul.md
- Hotel Hell.md
- Mohole.md
- 🎯 Performance Improvements
- 💰 ROI Analysis
- 📚 Deliverables
- 🚀 Deployment Readiness
- 💡 Recommendations
- 📞 Next Steps
- Context Management
- 🚨 CRITICAL ANTI-PATTERNS - DO NOT USE
- Rollback Procedures
- Success Metrics
- 🚀 Deployment Readiness
- 🎓 Lessons Learned
- 📚 Changes by Category
- 🚦 Next Steps
- MythosMUD Server Test Suite
- ✅ Verification Results
- Missing Test Scenarios
- Next Steps
- Net Impact Projection
- Implementation Timeline
- Phase 3: Coverage Test Optimization (Week 3)
- Executive Summary
- Appendix: Quick Reference Commands
- Detailed Category Value Breakdown
- Time Distribution Analysis
- Container System API Reference
- sub_zone
- main
- exception_metrics.py
- .get_memory_status_report
- ._get_npc_display_name
- validate_calendar.py
- .check_and_cleanup
- occupant_display.py
- Player Command Pipeline
- 📈 Performance Impact Assessment
- 🎯 Code Quality Assessment
- 🎯 Final Verdict
- 📈 Success Metrics
- 🎓 Technical Debt Reduced
- 🎯 Audit Compliance Score
- 🎓 Key Learnings
- 🔍 Testing Strategy
- 🎯 Success Criteria - Status
- 🚨 Risk Assessment
- Performance Logging
- Log Rotation and Management
- Log Analysis and Monitoring
- Security Considerations
- InviteBase
- Decision Points
- Monitoring & Validation
- Round-Based Combat
- Testing Strategy
- pyrightconfig.json
- 📊 Final Results
- 📈 Performance Impact
- core/fixer.py
- 🎯 Async Compliance Score
- 🧪 Testing Status
- 🔧 Changes Summary
- check_file_for_logging_issues
- e2e_reset_players.py
- Final Recommendation
- Optimization Strategy Overview
- Monitoring and Validation
- NPC Occupants Verification Summary
- Success Criteria
- Visual Test Value Distribution
- E2E Testing Guide
- _FakeRoomManager
- Combat Client Crash
- Respawn Death Screen Loop Limbo ID Mismatch
- test_websocket_handler_json_error.py
- NPC Combat Start Race Condition
- MemoryMonitor
- MythosMUD Full-Stack Feature Skill
- frontend-design/SKILL.md
- Enhanced Structured Logging System
- fixture
- test_cancel_shutdown_countdown_no_active
- test_process_tick_regeneration_fractional_accumulation
- MythosMUD ADR Authoring
- MythosMUD Commit Messages
- test_restore_mp_from_rest_restores_mp
- @eslint/js
- test_restore_mp_from_rest_calculates_max_from_power
- test_restore_mp_from_meditation_higher_than_rest
- Magic and Spellcasting System
- Lucidity Tiers
- Critical Discovery & Fix
- test_restore_mp_from_item_player_not_found
- Phase 1: Fix Failing Integration Tests (Week 1-2) 🚧 **IN PROGRESS**
- Four-Level Room Hierarchy
- test_restore_mp_from_item_restores_mp
- MythosMUD Logging Standards
- test_process_tick_regeneration_lying_position
- Files Affected
- MythosMUD OpenAPI Workflow
- Category D: API Endpoint Tests (App State)
- Files to Update
- MythosMUD Server Runbook
- gh-stack (MythosMUD)
- Files to Update
- Phase 3: Modernize Test Patterns (Week 5)
- _update_player_status_effects
- Canonical Worktree Layout
- AFTER
- Files to Update
- New Tests to Add
- Memory Leak Metrics Usage Guide
- NATS Manual Acknowledgment Guide
- task_registry.py
- _FakeWebSocket
- test_ensure_processing_started
- CircuitBreakerOpen
- command_service
- mock_zone_config
- handle_unequip_command
- test_unsubscribe_all_for_service_partial_cleanup
- ._get_room_uuid_by_stable_id
- SampleModel
- Modular E2E Test Suite
- Playwright MCP Scenarios
- .enforce_rate_limit
- Thinking about stack structure
- 🔧 COMMON FIX TEMPLATES
- extract/SKILL.md
- MythosMUD Pre-Commit Checklist
- MagicPointsMeter.tsx
- .execute_behavior
- is_postgres_url
- AI PR Reviewer Instructions
- handle_ping_message
- schemas/auth/__init__.py
- fixture
- InviteCreate
- ._compute_player_context
- Quest System Gap
- UserBase
- test_db_connectivity_create_and_read_user
- Container Contents Synchronization Bug
- description
- environment
- name
- test_websocket_handler_disconnect.py
- description
- environment
- test_websocket_handler_helpers.py
- test_magic_healing_events.py
- Phase 2: Categorize and Prioritize Mypy Issues
- Phase 5: Fix Implementation Patterns
- test_protocols.py
- lock_state
- get_npc_name_from_instance
- send_system_message
- ._background_audit_cycle
- fix_file
- check_codacy_yaml
- new-worktree.md
- MythosMUD COPPA Checklist
- normalize/SKILL.md
- Phase 2: Categorize and Prioritize Lint Issues
- TestPostgresConnectionPool
- 3. Systematic Investigation Approach
- add_fastapi_users_columns.py
- add_used_by_user_id_column.py
- MythosMUD Pre-Commit Checklist Skill
- process_npc_maintenance
- _AppStateWithLegacyConfig
- _RoomPersistence
- .get_room_by_id
- _EventBusPublishPort
- registry_with_switchblade
- message_filtering_helper
- Phase 2: Categorize and Prioritize Lint Issues
- 🔄 COMMON SCENARIOS AND SOLUTIONS
- _make_mock_row
- get_alerts
- 🔍 DEBUGGING GUIDE
- 🚀 OPTIMIZATION TIPS
- month
- test_professions_endpoints.py
- Structured Logging Patterns
- id
- metadata
- ._handle_hunt_target
- PerformanceStats
- ._handle_patrol_territory
- .is_npc_death_suppressed
- ._flush_memory_indexes_cache
- ._exit_is_bidirectional
- _UserWithGet
- WebSocket and SSE Dual Connections
- test_disconnect_connection_for_session_key_error
- .get_memory_usage_summary
- 🚨 AI ERROR HANDLING
- 🚨 AI ERROR HANDLING
- id
- _NpcWithLife
- ._resolve_hourly_holidays
- Scenario 42 Quest Log Visible After Login
- .force_single_audit_cycle
- _resolve_npc_combat_service_raw
- MythosMUD Product Requirements
- .get_stats
- party_service
- mock_send_game_event
- monitor
- auditor
- Any
- subscription_manager
- combat_validator
- subscription_manager
- .stop_audit_scheduler
- verify_npc_occupants.py
- asyncio
- @vitejs/plugin-react
- .__init__
- .shutdown_all
- verify_schema_match.sh
- test_event_bus_publish_no_subscribers
- .__init__
- ._get_npc_stats
- server/realtime/maintenance/__init__.py
- ._render_empty_map
- test_parse_command_string_success
- Claude Pointer (.claude/CLAUDE.md)
- test_spell_repository.py
- test_parse_command_string_with_subcommand
- test_parse_command_string_unexpected_error
- test_prepare_command_data_with_pipe_target
- test_evaluate_equality_false
- test_evaluate_equality_string
- test_evaluate_equality_not_equality
- test_evaluate_equality_invalid_format
- Logging Best Practices
- test_evaluate_inequality_true
- test_evaluate_inequality_false
- test_evaluate_numeric_comparison_less_equal
- test_evaluate_condition_greater_than
- test_evaluate_condition_less_than
- test_evaluate_condition_unknown
- test_extract_parsed_fields_with_pipe_target
- test_execute_command_handler_error
- zone_config_loader.py
- Scenario Group Execution
- .add_message
- Per-Recipient Whisper Rate Limiting
- test_process_command_parse_error
- test_process_command_no_handler
- test_get_available_commands
- test_unregister_command_handler
- test_unregister_command_handler_nonexistent
- asyncio
- test_log_parsed_command_inspection
- test_process_validated_command_no_command_type
- test_restore_mp_from_rest_player_not_found
- test_restore_mp_from_rest_at_max
- ._connect_nats
- test_restore_mp_from_item_calculates_max_from_power
- test_process_tick_regeneration_player_not_found
- Vite Best-Practices Remediation
- Success Metrics
- test_process_tick_regeneration_at_max
- test_process_room_rows_empty_list
- test_get_attack_damage_from_behavior_config
- test_get_attack_damage_invalid_string_falls_back_to_one
- test_hunt_target_avoids_duplicate_ids
- Scenario 32 Disconnect Grace Period
- test_enrich_behavior_context_swallows_compute_errors
- plane
- test_enrich_behavior_context_sets_player_in_range_when_players_in_room
- test_get_applicable_rules_priority_order
- test_evaluate_condition_handles_exception
- test_calculate_damage_physical_strength_bonus
- fixture
- test_calculate_damage_weapon_type_no_strength_bonus
- test_list_players_empty
- npc_event_handler
- test_convert_room_uuids_to_names_no_player_ids
- test_get_applicable_rules_no_matching
- test_execute_applicable_rules_no_matching
- test_register_action_handler_overwrites
- test_execute_action_success
- test_evaluate_boolean_condition_false
- id
- plane
- test_remove_rule_success
- zone
- test_remove_rule_not_found
- test_circuit_breaker_init
- test_get_room_occupants
- properties
- apply_migration
- _resolved_npm
- verify_tutorial_migrations.ps1
- preferences_service
- test_get_player_not_found
- F-String Logging Violations
- test_reset
- test_convert_room_uuids_to_names_invalid_uuid
- test_get_room_occupants_empty_online_players
- test_get_room_occupants_with_online_players
- test_send_initial_game_state_no_player
- test_send_initial_game_state_send_fails
- Catatonic Movement Prevention Bug
- test_convert_room_uuids_with_npcs
- Rooms List SQL ::uuid[] Parameter Conflict
- test_should_apply_mute_check_sensitive_channel
- test_get_following_for_client
- test_get_quest_log_for_client
- test_get_players_batch
- test_should_apply_mute_check_non_sensitive_channel
- test_get_players_batch_empty
- test_compare_canonical_rooms_same
- .get_lifecycle_statistics
- test_compare_canonical_rooms_different
- test_get_player_room_from_online_players
- monitoring_service
- test_get_player_room_from_online_players_not_found
- Character Creation Revamp
- Dead Code Cleanup Completion
- test_get_player_room_from_persistence_not_found
- test_is_player_in_room_false
- test_is_player_muted_by_receiver_not_muted
- Single Session Per User
- Test Warning Remediation
- Random Stats Generator Planning
- test_get_user_manager_custom
- test_message_filtering_helper_init
- position_commands.py
- test_preload_receiver_mute_data
- Party System Reference
- test_collect_room_targets_with_canonical_id
- test_extract_chat_event_info
- test_retry_async_increments_attempt
- test_retry_async_calls_function
- test_get_player_data_for_respawn_no_connection_manager
- test_get_player_data_for_respawn_no_persistence
- Test File Migration Mapping
- sample_container
- test_send_respawn_event_with_retry_success
- test_send_respawn_event_with_retry_timeout
- zone
- .get_task_lifecycle_metrics
- .create_supervised_task
- test_handle_player_respawned_success
- check_postgresql.sh
- setup_postgresql_test_db.sh
- test_adjust_room_drop_invalid_index
- test_list_room_drops_with_drops
- test_add_room_drop_new_room
- test_add_room_drop_existing_room
- test_take_room_drop_success
- test_take_room_drop_index_out_of_range
- test_take_room_drop_zero_quantity
- test_take_room_drop_full_quantity
- test_take_room_drop_partial_quantity
- test_take_room_drop_removes_empty_room
- GameState Event Projection
- test_adjust_room_drop_index_out_of_range
- Truly Dead Code
- test_adjust_room_drop_quantity_zero
- test_adjust_room_drop_negative_quantity
- test_add_room_drop_zero_quantity
- test_list_room_drops
- test_add_room_drop_error_handling
- test_take_room_drop_error_handling
- test_adjust_room_drop_error_handling
- test_handle_player_respawned_error_handling
- Dependency Review Workflow
- test_get_current_lucidity_not_found
- test_get_player_data_for_delirium_respawn_no_connection_manager
- test_get_player_data_for_delirium_respawn_error_handling
- test_handle_player_delirium_respawned_success
- test_handle_player_delirium_respawned_error_handling
- test_prepare_room_data_for_respawn_no_connection_manager
- test_get_player_data_for_respawn_no_get_stats
- 10 Concurrent Players Load Test
- test_get_player_data_for_respawn_success
- test_log_player_movement_error_handling
- test_normalize_event_ids_both_provided
- test_normalize_event_ids_none_values
- server/main.py
- test_extract_name_from_occupant_dict_with_player_name
- test_extract_name_from_occupant_dict_with_npc_name
- Cursor Rules as Canonical Config
- test_extract_name_from_occupant_dict_with_name
- test_extract_name_from_occupant_string
- Logging Aggregator Verification
- Memory Leak Remediation
- Playwright DI Migration Validation
- Server Authority Remediation
- test_extract_name_from_occupant_invalid_type
- test_extract_occupant_names_valid_names
- test_extract_occupant_names_invalid_names
- test_list_room_drops_error
- test_list_room_drops_empty
- test_add_room_drop
- test_add_room_drop_invalid_quantity
- Persistence Async Migration Guide
- test_extract_occupant_names_empty_list
- test_extract_occupant_names_none
- test_add_valid_name_to_lists_player
- test_add_valid_name_to_lists_npc
- test_build_room_objects_with_dict_attributes
- test_take_room_drop_all
- test_take_room_drop_invalid_index
- test_adjust_room_drop
- Scenario 34 Two Players Same Room Visibility
- test_behavior_engine_init
- test_evaluate_inequality_not_inequality
- remove_dir
- load_seed_data
- safe_print
- parse_lint_findings
- verify_e2e_users_seeded.py
- test_adjust_room_drop_remove
- test_add_valid_name_to_lists_invalid_name
- test_evaluate_numeric_comparison_greater_equal
- test_add_rule_success
- test_evaluate_numeric_comparison_false
- test_evaluate_condition_equality
- NPCs Not Updating On Player Movement
- Combat Messages Dual Panel Display
- Test Suite Stall After Performance Comparison
- test_evaluate_condition_inequality
- test_add_room_occupant_new_room
- test_evaluate_condition_less_equal
- test_remove_room_occupant
- test_execute_applicable_rules_executes_highest_priority
- Ground Command
- Rest Subsystem
- LevelService
- test_add_rule_missing_fields
- test_execute_applicable_rules_no_handler
- test_register_action_handler
- test_state_direct_access
- test_remove_room_occupant_not_occupant
- test_remove_room_occupant_removes_empty_room
- test_add_room_occupant_error_handling
- test_evaluate_boolean_condition_variable_false
- test_room_subscription_manager_init
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
- test_set_async_persistence
- test_add_valid_name_to_lists_none_name
- test_subscribe_to_room_multiple_players
- test_unsubscribe_from_room
- test_unsubscribe_from_room_not_subscribed
- test_subscribe_to_room_error
- test_unsubscribe_from_room_error
- InstanceManager
- React Node Upgrade Plan
- .get_combat_stats
- test_process_dict_occupant_with_npc_name
- Mid-Run Disconnect Reasons
- .cleanup_empty_subzone_subscriptions
- bcrypt Fresh Session Isolation
- .handle_player_movement
- Git Submodule Setup
- test_process_dict_occupant_with_name
- Error Monitoring Scripts
- test_process_dict_occupant_invalid_name
- test_build_occupants_snapshot_data_mixed
- ApplicationContainer
- test_build_occupants_snapshot_data_none
- Chat Messages Not Displayed to Sender (Bug #2)
- Mute Command Server Error (Bug #1)
- mythos_e2e Database
- Playwright MCP core-tabs Capability
- Playwright MCP Timing Limitation
- test_count_occupants_by_type_mixed
- test_is_player_disconnecting_true
- test_is_player_disconnecting_string_id
- test_is_player_disconnecting_no_connection_manager
- test_is_player_disconnecting_no_disconnecting_players_attr
- test_player_event_handler_utils_init
- test_normalize_player_id_uuid
- test_normalize_player_id_string
- test_normalize_player_id_invalid_string
- test_add_room_occupant
- test_broadcast_combat_death
- test_broadcast_combat_ended
- test_broadcast_combat_end
- test_broadcast_combat_error
- test_broadcast_player_mortally_wounded
- test_broadcast_player_died
- TestGetRoomService
- test_broadcast_player_mortally_wounded_with_attacker
- test_broadcast_player_respawn_personal_message_error
- test_broadcast_combat_error_send_error
- test_connection_manager_lazy_load_called
- test_broadcast_player_mortally_wounded_personal_message_error
- applies_to
- test_send_dp_decay_message
- test_send_dp_decay_message_error
- test_broadcast_combat_start
- test_broadcast_combat_attack
- test_process_command_string_key_error
- test_process_command_string_runtime_error
- ._get_player_mute_file
- test_extract_attributes_basic
- test_extract_attributes_missing_attribute
- test_is_combat_command_attack
- test_is_combat_command_strike
- test_is_combat_command_non_combat
- integration
- player_repository
- RateLimiter
- test_extract_command_data_basic
- test_extract_command_data_with_target
- test_extract_command_data_combat_target
- user_manager
- wearable_service
- _is_npc_follow_value
- test_extract_command_data_multiple_attributes
- enabled
- test_validate_command_safety_safe
- test_get_command_help_success
- test_get_command_help_none
- test_process_command_string_success
- test_get_command_help_attribute_error
- test_get_command_help_key_error
- test_process_command_string_type_error
- test_process_command_string_attribute_error
- test_memory_profiler_get_current_memory_usage
- description
- test_get_rate_limit_info_calculates_retry_after
- .get_config_summary
- .__del__
- .set_main_loop
- AGENTS.md Authoritative Guidance
- .to_dict
- test_build_room_objects_debug_logging
- test_get_rate_limit_info_filters_old_requests
- autoprefixer
- test_enforce_rate_limit_allows_request
- test_enforce_rate_limit_includes_retry_after
- test_stats_roll_limiter_initialized
- test_character_creation_limiter_initialized
- test_check_rate_limit_multiple_requests
- ._handle_combat_started_event
- ._handle_event_message
- ._handle_game_tick_event
- ._handle_npc_attacked_event
- ._handle_npc_died_event
- ._handle_player_entered_event
- .unsubscribe_from_room
- OccupantFormatter
- test_event_bus_set_main_loop
- test_event_bus_publish_multiple_subscribers
- test_event_bus_init
- test_unsubscribe_all_for_service
- test_unsubscribe_all_for_service_nonexistent
- test_get_subscriber_stats
- Bug Report Issue Template
- Issue Template Config
- Item System Blueprint
- test_event_bus_get_subscriber_count
- test_check_rate_limit_exceeds_limit
- test_check_rate_limit_different_users
- test_check_rate_limit_removes_old_requests
- test_get_rate_limit_info_with_requests
- test_validate_combat_command_rate_limited
- test_validate_combat_command_exception_handling
- test_validate_target_exists_exact_match
- test_validate_target_exists_partial_match
- test_validate_target_exists_no_match
- test_validate_target_alive_alive
- test_validate_combat_state_not_in_combat_required
- test_combat_validator_init
- test_validate_attack_strength_success
- test_validate_attack_strength_target_too_strong
- test_validate_attack_strength_target_significantly_stronger
- test_validate_attack_strength_weak_weapon
- test_validate_combat_command_valid
- test_is_rate_limited
- test_get_random_error_message_unknown_type
- test_get_combat_help_message
- test_get_combat_status_message_in_combat
- test_get_combat_status_message_not_in_combat
- test_get_combat_result_message_success_with_damage
- test_get_combat_result_message_failure
- test_validate_combat_command_invalid_command_type
- test_validate_combat_command_all_attack_aliases
- test_validate_combat_state_edge_case_return_true
- test_validate_combat_command_suspicious_patterns_with_mock
- test_validate_combat_command_target_too_long_with_mock
- test_validate_combat_command_no_target
- test_validate_combat_command_invalid_target_name
- test_get_user_by_username_case_insensitive_no_session
- test_get_professions_no_session
- test_get_players_batch_with_players
- test_generate_room_id_from_zone_data_with_prefix
- test_generate_room_id_from_zone_data_needs_generation
- test_parse_exits_json_string_valid
- test_parse_exits_json_list
- test_load_room_cache_async_rooms_none
- test_parse_exits_json_other_type
- test_process_exits_for_room_multiple_exits
- test_process_combined_rows_no_exits
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
- test_process_room_rows_with_none_zone_stable_id
- test_process_room_rows_with_none_stable_id
- test_process_exit_rows_missing_zone
- test_process_exit_rows_missing_stable_id
- test_load_room_cache_async_warning_logging
- test_warmup_room_cache
- test_get_player_by_name_database_error
- test_save_player_with_bool_is_admin
- test_save_player_database_error
- test_list_players_database_error
- test_get_player_by_user_id_success
- test_soft_delete_player_not_found
- test_get_players_batch_success
- test_subscribe_player_to_room_success
- test_subscribe_player_to_room_invalid_id
- test_subscribe_player_to_room_error
- test_send_room_name_message
- test_prepare_room_data_with_to_dict
- test_send_room_update_to_player_no_connection_manager
- test_send_room_update_to_player_room_not_found
- test_send_room_update_to_player_error_handling
- test_build_room_occupants_message
- test_send_occupants_snapshot_to_player_success
- test_send_occupants_snapshot_to_player_string_id
- test_send_occupants_snapshot_to_player_no_connection_manager
- test_send_occupants_snapshot_to_player_error_handling
- test_send_room_updates_to_entering_player_success
- test_send_room_updates_to_entering_player_error_handling
- test_process_player_entered_event_success
- test_process_player_entered_event_no_player_info
- test_handle_player_entered_success
- test_handle_player_entered_no_connection_manager
- test_handle_player_entered_no_player_info
- test_log_player_movement_left
- test_log_player_movement_no_room
- test_get_room_data_with_conversion
- test_subscribe_to_room
- test_log_player_movement_joined
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
- GitHub Issues task tracking
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
- Docker Best Practices Rule
- finalize_build_touch Rebuild Trigger

## God Nodes (most connected - your core abstractions)
1. `get_logger()` - 525 edges
2. `LoggedHTTPException` - 358 edges
3. `ValidationError` - 337 edges
4. `User` - 293 edges
5. `AliasStorage` - 264 edges
6. `DatabaseError` - 264 edges
7. `ConnectionManager` - 254 edges
8. `Player` - 228 edges
9. `log_and_raise()` - 196 edges
10. `CombatParticipant` - 194 edges

## Surprising Connections (you probably didn't know these)
- `Grype SCA exclude paths` --semantically_similar_to--> `Codacy exclude_paths`  [INFERRED] [semantically similar]
  .grype.yaml → .codacy.yml
- `Arkham City Graph PNG` --semantically_similar_to--> `Simple Room Graph - Arkham City`  [INFERRED] [semantically similar]
  data/local/arkham_city_graph.png → data/local/simple_room_visualization.html
- `update_player_background_task()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py
- `update_player_background_task()` --calls--> `clear_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py
- `webhook()` --calls--> `JSONResponse`  [INFERRED]
  monitoring/webhook-receiver.py → docs/examples/logging/fastapi_integration.py

## Import Cycles
- 2-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 2-file cycle: `client/src/components/map/useAsciiMap.ts -> client/src/components/map/useAsciiMapState.ts -> client/src/components/map/useAsciiMap.ts`
- 3-file cycle: `server/realtime/connection_cleanup_methods.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_cleanup_methods.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- 3-file cycle: `client/src/components/panels/chatPanelChannelFilter.ts -> client/src/components/panels/chatPanelChannelVisibility.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelChannelFilter.ts`
- 3-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelUnreadBump.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `server/realtime/connection_establishment.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_establishment.py`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`

## Hyperedges (group relationships)
- **Agent instruction routing chain** — claude_md_agent_router, agents_md_agent_instructions, user_rules_md_server_startup_rules [EXTRACTED 1.00]
- **Lucidity hallucination effects group** — docs_archive_lucidity_system_lucidity_system, docs_archive_phantom_hostile_requirements_phantom_hostiles, docs_archive_reversed_compass_directions_requirements_reversed_compass [EXTRACTED 1.00]
- **Client panel separation triad** — docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_chat_panel, docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_game_log_panel, docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_commands_panel [EXTRACTED 1.00]
- **Uncoordinated NPC startup spawners** — docs_archive_npc_startup_duplication_analysis_npc_startup_service, docs_archive_npc_startup_duplication_analysis_npc_lifecycle_manager, docs_archive_npc_startup_duplication_analysis_npc_population_controller [EXTRACTED 1.00]
- **Container inventory synchronization cluster** — investigations_remediation_plans_2025_01_27_container_sync_remediation_container_sync_bug, investigations_sessions_2025_01_27_session_001_inventory_slot_calculation_bug_inventory_slot_bug, investigations_sessions_2025_01_27_session_001_inventory_slot_calculation_bug_dual_storage [EXTRACTED 1.00]
- **Enhanced logging f-string compliance cluster** — investigations_sessions_2025_01_28_session_enhanced_logging_compliance_audit_logging_audit, investigations_sessions_2025_01_28_session_fstring_violations_remediated_fstring_remediation, investigations_sessions_2025_01_28_session_pre_commit_hook_analysis_precommit_gaps, investigations_sessions_2025_01_28_session_pre_commit_hook_fix_ast_fstring_detector [EXTRACTED 1.00]
- **December 3 character and occupants UI cluster** — investigations_sessions_2025_12_03_final_summary_dec3_summary, investigations_sessions_2025_12_03_session_001_character_info_panel_character_info_stats, investigations_sessions_2025_12_03_session_002_room_occupants_display_occupants_duplicates [EXTRACTED 1.00]
- **Historical pre-authoritative DDL verification snapshots** — db_verification_ddl_status_historical_partial_status, db_verification_ddl_final_status_historical_final_status, db_verification_ddl_verification_summary_historical_summary [EXTRACTED 1.00]
- **Local server start/stop lifecycle scripts** — scripts_readme_start_server, scripts_readme_stop_server, scripts_readme_start_local, scripts_readme_port_54768 [EXTRACTED 1.00]
- **Quest system documentation** — docs_quest_design_guidelines_doc, docs_quest_system_features_doc [EXTRACTED 1.00]
- **AI execution improvement documentation set** — e2e_tests_ai_execution_improvements_mandatory_execution_protocol, e2e_tests_ai_executor_quick_reference_seven_commandments, e2e_tests_execution_guards_max_step_attempts, e2e_tests_improvements_summary_infinite_loop_prevention [EXTRACTED 1.00]
- **Whisper Phase 3 NATS review artifacts** — e2e_tests_phase_3_complete_summary_phase_3_code_review, e2e_tests_phase_3_code_review_findings_nats_subject_manager, e2e_tests_phase_3_task_2_subject_manager_review_dual_path_subject_construction, e2e_tests_phase_3_task_3_documentation_review_nats_subject_patterns_doc [EXTRACTED 1.00]
- **Whisper remediation documentation cluster** — e2e_tests_whisper_system_investigation_report_whisper_system_investigation, e2e_tests_whisper_fix_phase_1_complete_whisper_nats_subject_bug_fix, e2e_tests_whisper_testing_complete_whisper_system_production_ready, e2e_tests_work_completed_and_remaining_whisper_work_completed [EXTRACTED 1.00]
- **Design skills depend on frontend-design** — skills_frontend_design, skills_adapt, skills_animate, skills_arrange, skills_bolder, skills_clarify, skills_colorize, skills_critique, skills_delight, skills_distill, skills_extract [EXTRACTED 1.00]
- **Design skills requiring teach-impeccable** — skills_teach_impeccable, skills_onboard, skills_optimize, skills_overdrive, skills_polish, skills_quieter, skills_typeset, skills_design_context_persistence [EXTRACTED 1.00]
- **Earth-plane major geography locations** — data_mythosmud_obsidian_raw_sources_mythosmud_worldbuilding_earth_plane, data_mythosmud_obsidian_raw_sources_geography_major_locations_arkham_city, data_mythosmud_obsidian_raw_sources_geography_major_locations_innsmouth, data_mythosmud_obsidian_raw_sources_geography_major_locations_rlyeh [EXTRACTED 1.00]
- **Effects and grace period cluster** — plans_effects_system_adr_and_implementation, plans_effects_system_implementation, plans_disconnect_grace_period_and_rest, plans_effects_login_warded [EXTRACTED 1.00]
- **Event projection and room handoff authority path** — client_src_components_ui_v2_eventlog_events_schema_event_projector, client_src_components_ui_v2_eventlog_events_schema_room_state, client_src_components_ui_v2_eventlog_handoffs_enter_room_rr, client_src_components_ui_v2_eventlog_handoffs_server_authority [EXTRACTED 1.00]
- **Frontend-design reference docs** — skills_frontend_design_ref_color_and_contrast, skills_frontend_design_ref_interaction_design, skills_frontend_design_ref_motion_design, skills_frontend_design_ref_responsive_design, skills_frontend_design_ref_spatial_design, skills_frontend_design_ref_typography, skills_frontend_design_ref_ux_writing [EXTRACTED 1.00]
- **Memory leak metrics and remediation** — plans_memory_leak_metrics_collection, plans_memory_leak_remediation, plans_memory_closed_websockets_deque [EXTRACTED 1.00]
- **MOTD listed known zones** — data_local_motd_message_of_the_day, data_local_motd_arkham_city, data_local_motd_innsmouth, data_local_motd_katmandu [EXTRACTED 1.00]
- **Quest gap analysis to implementation** — plans_mud_subsystems_gap_analysis, plans_mud_quest_gap, plans_quest_subsystem_implementation, plans_quest_system [EXTRACTED 1.00]
- **Canonical seed path via authoritative DML** — data_spells_readme_spells_seed_deprecated, data_static_generated_sql_readme_world_and_emotes_sql, data_static_generated_sql_readme_static_seed_deprecated, data_spells_readme_authoritative_dml [EXTRACTED 1.00]
- **Alert evaluation and routing pipeline** — monitoring_prometheus_yml_prometheus_config, monitoring_mythos_alerts_yml_alert_rules, monitoring_alertmanager_yml_alertmanager_config [EXTRACTED 1.00]
- **Core monitoring stack services** — monitoring_docker_compose_prometheus, monitoring_docker_compose_alertmanager, monitoring_docker_compose_grafana [EXTRACTED 1.00]
- **WebSocket message accept-validate-route-broadcast pipeline** — server_realtime_readme_websocket_api, server_realtime_readme_connection_manager, server_realtime_readme_message_validator, server_realtime_readme_nats_message_handler, server_realtime_readme_room_broadcasts [EXTRACTED 1.00]
- **Room validator core modules** — tools_room_toolkit_room_validator_readme_room_loader, tools_room_toolkit_room_validator_readme_schema_validator, tools_room_toolkit_room_validator_readme_path_validator, tools_room_toolkit_room_validator_readme_reporter, tools_room_toolkit_room_validator_readme_fixer [EXTRACTED 1.00]
- **Multi-character scenario group 27-30** — e2e_tests_scenarios_scenario_27_character_selection_character_selection, e2e_tests_scenarios_scenario_28_multi_character_creation_multi_character_creation, e2e_tests_scenarios_scenario_29_character_deletion_character_soft_deletion, e2e_tests_scenarios_scenario_30_character_name_uniqueness_case_insensitive_name_uniqueness [EXTRACTED 1.00]
- **Skills scenario group 39-41** — e2e_tests_scenarios_scenario_39_skills_new_tab_skills_new_tab, e2e_tests_scenarios_scenario_40_skills_command_skills_slash_command, e2e_tests_scenarios_scenario_41_skills_after_creation_skills_after_creation [EXTRACTED 1.00]
- **Visibility and combat scenarios 34-36** — e2e_tests_scenarios_scenario_34_two_players_same_room_same_room_visibility, e2e_tests_scenarios_scenario_35_player_combat_player_combat, e2e_tests_scenarios_scenario_36_movement_visibility_movement_visibility [EXTRACTED 1.00]
- **JSON validate generate merge seed pipeline** — scripts_static_data_readme_generate_sql_mjs, scripts_static_data_readme_ajv_validation, scripts_static_data_readme_world_emotes_sql, scripts_static_data_readme_canonical_dml_merge, scripts_static_data_readme_uuid_v5_namespace [EXTRACTED 1.00]
- **Combat start XP and second-NPC cluster** — investigations_sessions_2025_12_08_session_combat_start_failure_missing_await, investigations_sessions_2025_12_14_session_002_xp_award_error_investigation_xp_award_error, investigations_sessions_2026_02_04_combat_second_npc_and_linkdead_findings_second_npc_combat [INFERRED 0.75]
- **Explored rooms filtering and minimap cluster** — investigations_sessions_2025_12_07_session_sql_syntax_error_rooms_list_sql_cast_param, investigations_sessions_2026_01_04_session_minimap_explored_rooms_bug_minimap_explored [INFERRED 0.75]
- **GitHub security scanning suite** — github_workflows_codeql_codeql_workflow, github_workflows_dependency_review_dependency_review_workflow, github_workflows_scorecards_scorecard_workflow [INFERRED 0.75]
- **Death, rest, and rescue lifecycle** — docs_subsystems_subsystem_status_effects_design_status_effects, docs_subsystems_subsystem_respawn_design_respawn_subsystem, docs_subsystems_subsystem_rescue_design_rescue_subsystem, docs_subsystems_subsystem_rest_design_rest_subsystem [INFERRED 0.75]
- **Realtime messaging stack** — docs_architecture_decisions_adr_003_dual_event_systems_eventbus_nats_eventbus, docs_architecture_decisions_adr_003_dual_event_systems_eventbus_nats_nats, docs_architecture_decisions_adr_004_websocket_only_realtime_websocket_only, docs_architecture_distributed_eventbus_nats_nats_eventbus_bridge [INFERRED 0.85]
- **Chat and NATS migration linkage** — docs_archive_planning_redis_to_nats_migration_redis_to_nats, docs_archive_planning_redis_to_nats_migration_nats_service, docs_archive_planning_chat_system_chat_system_plan [INFERRED 0.85]
- **NPC occupants display investigation cluster** — investigations_sessions_2025_01_28_session_npc_display_final_fixes_npc_display_fixes, investigations_sessions_2025_01_28_session_npc_occupants_verification_summary_npc_occupants_verification, investigations_sessions_2025_01_29_session_001_npc_occupants_display_issue_dual_tracking, investigations_sessions_2025_01_30_session_001_npcs_not_updating_on_player_movement_npc_movement_update, investigations_sessions_2025_01_xx_session_npc_spawning_occupants_issue_npc_spawning_display, investigations_sessions_2025_01_xx_session_occupants_npc_display_flat_occupants_list [INFERRED 0.85]
- **Combat messaging and NATS failure cluster** — investigations_sessions_2025_11_19_session_001_nats_message_validation_failure_nats_event_data, investigations_sessions_2025_11_19_session_002_combat_client_crash_combat_client_crash, investigations_sessions_2025_11_19_session_002_combat_message_uuid_display_combat_uuid_display, investigations_sessions_2025_11_19_session_003_combat_messages_dual_panel_display_combat_dual_panel, investigations_sessions_2025_12_01_session_npc_death_messages_not_displaying_npc_death_messages [INFERRED 0.85]
- **Death limbo and respawn investigation cluster** — investigations_sessions_2025_11_19_session_005_respawn_death_screen_loop_limbo_room_id_mismatch, investigations_sessions_2025_11_20_respawn_persistence_bug_investigation_respawn_persistence, investigations_sessions_2025_11_20_session_002_death_posture_bugs_death_posture [INFERRED 0.85]
- **Command development guide set** — docs_command_handler_patterns_doc, docs_command_models_reference_doc, docs_command_security_guide_doc, docs_command_testing_guide_doc [INFERRED 0.85]
- **Cursor IDE tooling documentation** — docs_cursor_cli_doc, docs_cursor_hooks_doc, docs_cursor_setup_guide_doc, docs_cursor_subagents_doc, docs_cursor_workflows_doc [INFERRED 0.85]
- **Contribution and triage templates** — github_issue_template_bug_report_bug_report_template, github_issue_template_documentation_documentation_template, github_issue_template_feature_request_feature_request_template, github_pull_request_template_pr_template [INFERRED 0.85]
- **Combat feature plans cluster** — plans_combat_round_system_refactor, plans_combat_bugs_investigation_and_fixes, plans_flee_command_and_effect, plans_first_weapon_switchblade [INFERRED 0.85]
- **MythosMUD operational skills cluster** — skills_mythosmud_server_runbook, skills_mythosmud_pre_commit_checklist, skills_mythosmud_test_writing, skills_mythosmud_worktree_workflow, skills_one_server_only_rule, skills_definition_of_done [INFERRED 0.85]
- **WebSocket migration and client message pipeline** — plans_websocket_only_migration, plans_websocket_best_practices_remediation, plans_unify_client_message_handling, plans_websocket_only_architecture [INFERRED 0.85]
- **Quality and security tooling cluster** — codacy_yml_codacy_configuration, pre_commit_config_yaml_pre_commit_hooks, semgrep_yml_no_select_star, bandit_yml_bandit_config, grype_yaml_sca_excludes [INFERRED 0.85]
- **Dual connection documentation set** — docs_archive_dual_connection_api_reference_dual_connection_api, docs_archive_dual_connection_client_guide_dual_connection_client, docs_archive_dual_connection_deployment_guide_dual_connection_deploy, docs_archive_dual_connection_api_reference_websocket_sse_dual [INFERRED 0.95]
- **Enhanced logging documentation cluster** — docs_archive_implementation_complete_enhanced_logging_complete, docs_archive_logging_implementation_summary_enhanced_logging, docs_archive_logging_migration_complete_logging_migration [INFERRED 0.95]
- **Spell command and casting failure cluster** — investigations_sessions_2025_12_14_session_001_spell_commands_failure_spell_commands_missing, investigations_sessions_2025_12_14_session_002_spell_cast_failure_multiword_spell, investigations_sessions_2025_12_14_session_003_minor_heal_casting_delay_missing_async_heal, investigations_sessions_2025_12_14_session_004_heal_spell_casting_failure_session_boundary [INFERRED 0.95]
- **Logging and error handling guides** — docs_enhanced_logging_guide_doc, docs_error_handling_guide_doc, docs_error_logging_implementation_guide_doc [INFERRED 0.95]

## Communities (2360 total, 645 thin omitted)

### Community 0 - "DistributedEventBus"
Cohesion: 0.04
Nodes (68): ModuleType, DistributedEventBus, Any, Distributed EventBus that uses NATS for cross-instance event distribution.…, EventBus that distributes domain events via NATS for horizontal scaling. When…, Initialize distributed EventBus. Args: nats_service: NATS service for…, Set NATS service and start the bridge (call after NATS connects)., Publish event locally and to NATS when bridge is active. (+60 more)

### Community 1 - "ExceptionTracker"
Cohesion: 0.06
Nodes (32): ExceptionRecord, ExceptionTracker, ExceptionTrackInput, Any, Exception, Track an exception with full context information. Args: exception: The…, Get an exception record by ID. Args: exception_id: Unique exception ID Returns:…, Get all exceptions of a specific type. Args: exception_type: Exception type… (+24 more)

### Community 2 - "test_spell_effects.py"
Cohesion: 0.04
Nodes (70): Optional deps for SpellEffects beyond player_service., SpellEffectsDeps, mock_player_service(), mock_spell(), mock_target_match(), asyncio, fixture, Unit tests for spell effects. Tests the SpellEffects class. (+62 more)

### Community 3 - "AliasStorage"
Cohesion: 0.01
Nodes (198): AliasStorage, Manages player alias storage in JSON files. Each player's aliases are stored in…, List all alias files in the storage directory., handle_mute_global_command(), Handle the mute_global command for global muting. Args: command_data: Command…, Command service for MythosMUD. This module provides the main command processing…, Help command adapter module. The original help command handler lives in…, handle_inventory_command() (+190 more)

### Community 4 - "npc_definitions_api.py"
Cohesion: 0.09
Nodes (55): create_npc_definition(), delete_npc_definition(), get_npc_definition(), get_npc_definitions(), AsyncSession, delete, get, post (+47 more)

### Community 5 - "websocket_initial_state.py"
Cohesion: 0.03
Nodes (111): _accumulate_valid_occupant_name(), convert_uuids_to_strings(), get_occupant_names(), Validate that a name is not a UUID string., Parse one occupant row: append display name or log when it looks like a UUID., Extract and validate occupant names from room occupants list., Recursively convert UUID objects to strings for JSON serialization., validate_occupant_name() (+103 more)

### Community 6 - "models/user.py"
Cohesion: 0.03
Nodes (108): get_current_verified_user(), get_optional_current_user(), Authentication dependencies for MythosMUD. This module provides dependency…, Get current verified user or raise 403., Validate invite code for registration., Get current user if authenticated, otherwise None., require_invite_code(), Authentication module for MythosMUD. This package contains all authentication-… (+100 more)

### Community 7 - "test_command_moderation.py"
Cohesion: 0.03
Nodes (91): AddAdminCommand, AdminCommand, MuteCommand, MuteGlobalCommand, MutesCommand, field_validator, Moderation command models for MythosMUD. This module provides command models…, Command for showing current mute status. (+83 more)

### Community 8 - "test_email_utils.py"
Cohesion: 0.18
Nodes (17): generate_unique_bogus_email(), is_bogus_email(), AsyncSession, Email utilities for MythosMUD authentication. This module provides utilities…, Generate a unique bogus email address for a user. This function creates a bogus…, Check if an email address is a bogus email generated by our system. Args:…, Validate that a bogus email follows our expected format. Args: email: The email…, validate_bogus_email_format() (+9 more)

### Community 9 - "is_player_in_login_grace_period"
Cohesion: 0.03
Nodes (122): Get login grace period status for player., cancel_login_grace_period(), get_login_grace_period_remaining(), _grace_period_expiration_handler(), _grace_period_task(), is_player_in_login_grace_period(), Any, UUID (+114 more)

### Community 10 - "MythosMUDError"
Cohesion: 0.01
Nodes (269): JSONResponse, Validate password input before Argon2 hashing., _validate_password_for_hashing(), Error handlers package for MythosMUD. This package provides specialized error…, Pydantic error handler for consistent error processing. This module provides a…, _contains_file_path_in_exception(), _contains_sensitive_exception_pattern(), create_standardized_error_response() (+261 more)

### Community 11 - "Communities (355 total, 223 thin omitted)"
Cohesion: 0.02
Nodes (133): Communities (355 total, 223 thin omitted), Community 0 - "Nyarlathotep Avatars", Community 100 - "Call Daoloth / Daoloth", Community 101 - "Call Nyogtha / Clutch of Nyogtha", Community 102 - "Call Saaitii / Saaitii", Community 103 - "Call Zu-Che-Quon / Enchant Bells of Horror", Community 104 - "Cast Out Shan / Shaggai", Community 105 - "Casting the Runes / Elder Sign" (+125 more)

### Community 12 - "container_persistence/container_persistence.py"
Cohesion: 0.03
Nodes (132): ContainerData, Container data class for the unified container system., Data class for container information., Convert container data to dictionary for ContainerComponent., allowed_roles_from_row(), as_opt_datetime(), as_opt_str(), as_opt_uuid() (+124 more)

### Community 13 - "test_command_parser_helpers.py"
Cohesion: 0.05
Nodes (40): command_parser(), fixture, Unit tests for command_parser helper methods. Tests the helper methods in…, Test _create_command_object() handles 'l' alias., Test _create_command_object() handles 'g' alias., Test _create_command_object() handles 'w' alias., Test _create_command_object() raises error for unsupported command., Test _create_command_object() handles PydanticValidationError. (+32 more)

### Community 14 - "container_endpoints_basic.py"
Cohesion: 0.01
Nodes (205): get_async_persistence, get_connection_manager, _apply_inventory_stack_defaults(), _as_inventory_dicts(), _as_str_list(), _as_str_object_dict(), _as_str_object_mapping(), _build_container_data_from_dict() (+197 more)

### Community 15 - "test_player_service_mutations.py"
Cohesion: 0.05
Nodes (61): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service mutations. Covers delete, location update, mythos…, Test apply_corruption() applies corruption., Test gain_occult_knowledge() increases occult knowledge., Test heal_player() heals player. (+53 more)

### Community 16 - "server/models/game.py"
Cohesion: 0.02
Nodes (152): Item prototype registry for command modules., _apply_player_status_with_grace_check(), _apply_status_effect_to_player(), _grace_period_blocks_negative_status_effect(), _handle_player_status_effect(), _maybe_run_force_flee_effect(), _parse_status_effect_metadata(), Any (+144 more)

### Community 17 - "BaseCommand"
Cohesion: 0.01
Nodes (274): BaseCommand, BaseModel, Base class for all MythosMUD commands. Provides common validation and security…, Command for clean disconnection with optional countdown., RestCommand, JournalCommand, QuestCommand, QuestsCommand (+266 more)

### Community 18 - "test_security_validator.py"
Cohesion: 0.02
Nodes (185): _handle_processing_error(), Exception, Handle a general exception during command processing., field_validator, Validate target player name format using centralized validation., Validate message content for security using centralized validation., Validate message content for security using centralized validation., Validate message content for security using centralized validation. (+177 more)

### Community 19 - "handle_transfer_items_exceptions"
Cohesion: 0.02
Nodes (86): handle_close_container_exceptions(), handle_loot_all_exceptions(), handle_open_container_exceptions(), handle_transfer_items_exceptions(), Any, Exception, Request, UUID (+78 more)

### Community 20 - "test_command_communication.py"
Cohesion: 0.02
Nodes (146): EmoteCommand, LocalCommand, MeCommand, PoseCommand, Communication command models for MythosMUD. This module provides command models…, Command for whispering to a specific player., Command for replying to the last whisper received., Command for saying something to other players in the room. (+138 more)

### Community 21 - "test_websocket_handler_error_handling.py"
Cohesion: 0.15
Nodes (13): mock_websocket(), asyncio, fixture, Unit tests for websocket handler error handling. Tests the error handling…, Create a mock WebSocket., Test _send_error_response() successfully sends error., Test _send_error_response() handles WebSocket disconnection., Test _handle_runtime_error() detects WebSocket disconnection. (+5 more)

### Community 22 - "connection_manager_methods.py"
Cohesion: 0.01
Nodes (194): delegate_game_state_provider(), Generic delegate for game state provider methods. Args: game_state_provider:…, Any, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events., subscribe_to_room_events_impl(), unsubscribe_from_room_events_impl(), broadcast_global_event_impl() (+186 more)

### Community 23 - "test_look_container.py"
Cohesion: 0.08
Nodes (34): asyncio, Unit tests for container look functionality. Tests the helper functions for…, Test finding container via inner_container_id., Test finding container via inner_container when not present., Test finding container via inner_container with invalid UUID., Test getting container description from container metadata., Test getting container description when prototype_id is missing., Test finding container in room or equipped when in room. (+26 more)

### Community 24 - "WearableContainerServiceError"
Cohesion: 0.07
Nodes (28): Base exception for wearable container service operations., WearableContainerServiceError, Test add_items_to_wearable_container raises error when container not found., Test add_items_to_wearable_container raises error when capacity exceeded., Test handle_container_overflow raises error when player not found., Test handle_equip_wearable_container handles container creation error., Test add_items_to_wearable_container raises error when container belongs to…, Test add_items_to_wearable_container raises error when container is not… (+20 more)

### Community 25 - "test_player_disconnect_handlers.py"
Cohesion: 0.04
Nodes (71): Disconnect grace period management for MythosMUD. This module handles the…, _cleanup_player_references(), _collect_disconnect_keys(), _get_session_maps_for_age_off(), handle_player_disconnect_broadcast(), _purge_expired_sessions_from_maps(), Player, UUID (+63 more)

### Community 26 - "ConnectionManager"
Cohesion: 0.02
Nodes (155): emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), ContainerComponent, UUID, WebSocket event emission helpers for container API endpoints. This module…, Emit WebSocket event for container closing. Args: connection_manager:… (+147 more)

### Community 27 - "api/monitoring.py"
Cohesion: 0.02
Nodes (233): _assemble_health_response(), force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_health_status(), get_memory_alerts() (+225 more)

### Community 28 - "test_look_npc.py"
Cohesion: 0.02
Nodes (169): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_description(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result() (+161 more)

### Community 29 - "test_admin_commands.py"
Cohesion: 0.03
Nodes (108): handle_admin_command(), _handle_admin_status_command(), _handle_admin_time_command(), Any, Administrative commands for MythosMUD. This module contains the main admin…, Expose current Mythos time metadata, active holidays, and freeze diagnostics., Entry point for general admin commands that expose subcommands like `admin…, Provide contextual status information about the caller's administrative… (+100 more)

### Community 30 - "test_container_persistence_extended_crud.py"
Cohesion: 0.04
Nodes (60): parse_jsonb_column(), Parse a JSONB column value from database. JSONB columns may be returned as: -…, _build_container_data_from_row(), get_containers_by_entity_id(), get_containers_by_room_id(), get_decayed_containers(), Any, ContainerData (+52 more)

### Community 31 - "test_command_admin.py"
Cohesion: 0.03
Nodes (83): GotoCommand, NPCCommand, field_validator, Admin command models for MythosMUD. This module provides command models for…, Command for shutting down the server (admin only). Args can be: - Empty:…, Command for NPC administrative utilities with subcommands., Administrative command for summoning prototypes into the current room., Validate prototype ID format. Args: value: The prototype ID to validate… (+75 more)

### Community 32 - "test_websocket_handler_core.py"
Cohesion: 0.04
Nodes (71): handle_websocket_message(), WebSocket, Handle a WebSocket message from a player. Args: websocket: The WebSocket…, asyncio, Unit tests for core websocket handler functions. Tests core WebSocket handler…, Test _process_message processes message., Test _process_message returns True when rate limit exceeded., Test _validate_player_and_persistence validates successfully. (+63 more)

### Community 33 - "test_magic_commands.py"
Cohesion: 0.03
Nodes (84): handler(), mock_chat_service(), mock_magic_service(), mock_player(), mock_player_spell_repository(), mock_spell_learning_service(), mock_spell_registry(), MockEffectType (+76 more)

### Community 34 - "command_result_text"
Cohesion: 0.05
Nodes (83): handle_pickup_command(), Move an item stack from room drops into the player's inventory., handle_put_command(), _put_resolve_container_id(), _put_run_validated(), _put_transfer_finish(), PutCommandRuntime, PutValidatedWork (+75 more)

### Community 35 - "inventory_command_helpers.py"
Cohesion: 0.02
Nodes (164): _DropResolved, _FloorPickupResolved, Parse numeric fields from object-typed JSON command payloads., Protocol, Shared types for inventory command handlers (Lizard: keep main module small)., Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, add_pickup_to_inventory() (+156 more)

### Community 36 - "Room"
Cohesion: 0.02
Nodes (117): Instance, InstanceManager, Room, UUID, Return template rooms matching instance_template_id., Clone template rooms into instance-scoped rooms with remapped exits., Extract stable_id from room - use room.id if it looks like a full path., Remap exit targets: same-instance rooms use instance IDs, outside exits use… (+109 more)

### Community 37 - "test_lifecycle_periodic.py"
Cohesion: 0.08
Nodes (46): Clean up old lifecycle records (delegates to lifecycle_periodic)., Perform periodic maintenance (delegates to lifecycle_periodic)., _attempt_optional_npc_spawn(), check_optional_npc_spawns_impl(), _check_spawn_conditions_for_optional_npc(), cleanup_old_records_impl(), get_spawn_room_for_definition(), get_zone_key_for_definition() (+38 more)

### Community 38 - "test_level_service.py"
Cohesion: 0.05
Nodes (56): level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level(), UUID (+48 more)

### Community 39 - "ContainerComponent"
Cohesion: 0.02
Nodes (200): ContainerComponent, ContainerFactoryOptions, ContainerLockState, ContainerSourceType, Any, BaseModel, datetime, field_validator (+192 more)

### Community 40 - "test_command_parser.py"
Cohesion: 0.02
Nodes (95): Smoke test for command parser., Test basic command parsing., Test command parsing with arguments., Test command parsing with pipes., test_parse_command_basic(), test_parse_command_with_args(), test_parse_command_with_pipes(), command_parser() (+87 more)

### Community 41 - "websocket_handler_commands.py"
Cohesion: 0.04
Nodes (97): create_websocket_request_context(), Factory function to create a WebSocket request context. Args: app_state: Real…, _mirror_service_to_app_state(), WebSocket app.state / container service wiring for command processing.…, Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state. Mutates…, resolve_and_setup_app_state_services() (+89 more)

### Community 42 - "test_connection_helpers_impl.py"
Cohesion: 0.04
Nodes (87): broadcast_global_event_impl(), broadcast_room_event_impl(), convert_uuids_to_strings(), handle_new_login_impl(), mark_player_seen_impl(), _optimize_payload(), Any, _queue_message_if_needed() (+79 more)

### Community 43 - "SkillUseLog"
Cohesion: 0.21
Nodes (10): Base, One recorded successful use of a skill by a character at a given level.…, SkillUseLog, Unit tests for SkillUseLog ORM model., SkillUseLog can be instantiated with required fields., SkillUseLog maps to the expected table., SkillUseLog __repr__ includes key identifiers., test_skill_use_log_creation() (+2 more)

### Community 44 - "ApplicationContainer"
Cohesion: 0.02
Nodes (157): ChatBundle, Chat bundle: chat service. Depends on Core (config, persistence), Game…, Initialize chat service., CombatBundle, Combat bundle: player combat, death, respawn, combat service, catatonia,…, Raise if prerequisites for NATS combat are missing., Create CombatService with NATS and register it. Assumes NATS is connected., Start NATS message handler if available. Logs and swallows errors. (+149 more)

### Community 45 - "NPCStartupService"
Cohesion: 0.15
Nodes (13): _merge_phase_into_startup(), _new_spawn_results(), NPCStartupService, Any, Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…, Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…, Second pass: spawn one instance per definition (that was spawned in…, Determine the appropriate room for spawning an NPC. Args: npc_def: NPC… (+5 more)

### Community 46 - "get_username_from_user"
Cohesion: 0.04
Nodes (72): Unit tests for command_helpers utility functions. Tests the utility functions…, Test validate_command_safety() returns True for safe commands., Test validate_command_safety() returns False for shell metacharacters., Test validate_command_safety() returns False for SQL injection attempts., Test validate_command_safety() returns False for Python injection attempts., Test validate_command_safety() returns False for format string injection., Test validate_command_safety() returns False for XSS attempts., Test get_command_help() returns help for specific command. (+64 more)

### Community 47 - "test_behavior_engine.py"
Cohesion: 0.07
Nodes (29): Unit tests for behavior engine. Tests the BehaviorEngine class., Test _evaluate_equality() returns True for matching condition., Test _evaluate_equality() handles boolean true., Test _evaluate_numeric_comparison() handles > operator., Test _evaluate_numeric_comparison() raises ValueError for non-numeric values., Test evaluate_condition() handles >= operator., Test get_applicable_rules() returns matching rules., Test execute_applicable_rules() handles exceptions. (+21 more)

### Community 48 - "test_connection_delegates.py"
Cohesion: 0.02
Nodes (159): _async_callable(), cleanup_dead_websocket_impl(), _close_dead_websocket_if_open(), delegate_connection_cleaner(), delegate_connection_cleaner_sync(), delegate_error_handler(), delegate_game_state_provider_sync(), delegate_health_monitor() (+151 more)

### Community 49 - "CombatParticipant"
Cohesion: 0.02
Nodes (196): CombatAction, CombatParticipant, _get_default_damage(), Check if participant can perform voluntary combat actions. Unconscious (DP <=…, Apply damage to this participant and determine resulting death states.…, Get the default damage value from configuration., Represents a combat action., Represents a participant in combat. (+188 more)

### Community 50 - "CombatParticipantData"
Cohesion: 0.05
Nodes (42): _build_combat_instance(), _build_participant(), CombatInitializer, _compute_turn_order(), UUID, Combat initialization logic. Handles creation and setup of combat instances., Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…, Build CombatParticipant from CombatParticipantData. (+34 more)

### Community 51 - "PlayerPositionService"
Cohesion: 0.07
Nodes (50): PlayerPositionService, Coordinate player posture transitions with persistence and live presence…, asyncio, Unit tests for player position service. Tests the PlayerPositionService for…, Test change_position raises ValueError for invalid position., Test change_position returns error when no persistence., Test change_position returns error when player not found., Test change_position handles database errors gracefully. (+42 more)

### Community 52 - "test_player_repository.py"
Cohesion: 0.12
Nodes (15): Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes with room cache., Test PlayerRepository initializes with event bus., Test validate_and_fix_player_room returns False for valid room., Test validate_and_fix_player_room fixes invalid room., Test get_player_by_id returns None when player not found., Test save_players successfully saves multiple players., Test PlayerRepository initializes correctly. (+7 more)

### Community 53 - "test_command_factories.py"
Cohesion: 0.02
Nodes (114): factory(), fixture, Unit tests for command factories. Tests the CommandFactory class., Test create_channel_command delegates to communication factory., Test create_go_command delegates to exploration factory., Test create_sit_command delegates to exploration factory., Test create_stand_command delegates to exploration factory., Test create_lie_command delegates to exploration factory. (+106 more)

### Community 54 - "test_npc_utils.py"
Cohesion: 0.11
Nodes (17): Unit tests for NPC utility functions. Tests the utility functions in…, Test get_zone_key_from_room_id() extracts zone key from valid room ID., Test get_zone_key_from_room_id() handles room ID with description., Test get_zone_key_from_room_id() handles Innsmouth room ID., Test get_zone_key_from_room_id() returns 'unknown/unknown' for short room ID., Test get_zone_key_from_room_id() returns 'unknown/unknown' for too short room…, Test get_zone_key_from_room_id() handles room ID with exactly 4 parts., Test get_zone_key_from_room_id() handles room ID with many parts. (+9 more)

### Community 55 - "ExplorationService"
Cohesion: 0.04
Nodes (95): _MapRooms, _apply_exploration_filter_if_needed(), _filter_explored_rooms(), UUID, Filter rooms to only include explored ones using RoomService. This is a thin…, Apply exploration filter to rooms if user is not admin/superuser. Args: rooms:…, ExplorationService, Service for tracking player room exploration. This service manages the… (+87 more)

### Community 56 - "ErrorContext"
Cohesion: 0.03
Nodes (62): ErrorContext, Any, Initialize MythosMUD error. Args: message: Technical error message context:…, Convert error to dictionary for API responses., Log validation errors at warning so expected user-input errors do not flood…, Contextual information for error handling. Provides structured context for…, Initialize LoggedHTTPException. Args: status_code: HTTP status code detail:…, Convert context to dictionary for logging. (+54 more)

### Community 57 - "Stats"
Cohesion: 0.01
Nodes (181): computed_field, get_stats_generator(), Get a StatsGenerator instance via dependency injection. StatsGenerator is…, CharacterCreationService, Any, UUID, Character creation service for MythosMUD server. This module handles all…, Validate character stats against class prerequisites. Args: stats: The stats… (+173 more)

### Community 58 - "debrief_command.py"
Cohesion: 0.08
Nodes (48): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+40 more)

### Community 59 - "CombatInstance"
Cohesion: 0.03
Nodes (100): CombatInstance, UUID, Represents an active combat instance., Get the participant whose turn it is., Advance to the next round - all participants act each round. In round-based…, Check if combat should end. CRITICAL: Combat should NOT end when a player is…, Get all participants that are not dead (includes mortally wounded players at 0…, Update the last activity tick and datetime. (+92 more)

### Community 60 - "RoomService"
Cohesion: 0.03
Nodes (84): RoomDictList, _apply_exploration_filter_if_needed(), get_room(), _invalidate_room_cache(), list_rooms(), Any, AsyncSession, BaseModel (+76 more)

### Community 61 - "lifespan.py"
Cohesion: 0.02
Nodes (145): BaseUserManager, ID, _calculate_metrics_delta(), _cleanup_container_on_error(), _initialize_enhanced_systems(), lifespan(), _log_memory_metrics_periodically(), _persist_metrics_to_file() (+137 more)

### Community 62 - "test_command_factories_utility.py"
Cohesion: 0.03
Nodes (84): Unit tests for utility command factories. Tests the UtilityCommandFactory class…, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+76 more)

### Community 63 - "test_connection_statistics.py"
Cohesion: 0.06
Nodes (45): Get presence tracking statistics., get_online_player_by_display_name_impl(), get_player_presence_info_impl(), get_presence_statistics_impl(), Any, Get online player information by display name., Get detailed presence information for a player., Validate player presence and clean up any inconsistencies. (+37 more)

### Community 64 - "test_combat_attack_handler.py"
Cohesion: 0.03
Nodes (90): CombatStatus, Status of a combat instance., CombatAttackHandler, Any, UUID, Combat attack processing logic. Handles attack validation, damage application,…, Apply damage to target and update combat state. Args: combat: Combat instance…, Validate attack and retrieve combat participants. Args: attacker_id: ID of the… (+82 more)

### Community 65 - "PlayerStateService"
Cohesion: 0.06
Nodes (29): PlayerCreationService, Any, Stats, UUID, Create a new player character with specific stats. Args: name: The player's…, Service for player creation operations., Initialize with persistence layer, schema converter, and optional instance…, Resolve starting room and tutorial instance ID. For tutorial players, returns… (+21 more)

### Community 66 - "PanelState"
Cohesion: 0.04
Nodes (72): PanelManager(), PanelManagerProps, minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapPanelSection(), MinimapPanelSectionProps, PanelContainerProps, PanelContainerProps (+64 more)

### Community 67 - "test_command_combat.py"
Cohesion: 0.02
Nodes (113): AttackCommand, FleeCommand, KickCommand, PunchCommand, field_validator, Combat command models for MythosMUD. This module provides command models for…, Command for attacking a target., Validate combat target name format using centralized validation. (+105 more)

### Community 68 - "DatabaseManager"
Cohesion: 0.01
Nodes (317): close_db(), get_test_database_url(), Get test override database URL., DatabaseManager, ensure_database_directory(), get_database_path(), get_database_url(), _get_database_url_state() (+309 more)

### Community 69 - "PayloadOptimizer"
Cohesion: 0.09
Nodes (29): get_payload_optimizer(), PayloadOptimizer, Any, Payload optimization for WebSocket messages. This module provides utilities for…, Create an incremental update payload containing only changed fields. Args:…, Optimizes payloads for WebSocket transmission. Features: - Size limit…, Get the global payload optimizer instance., Initialize the payload optimizer. Args: max_payload_size: Maximum payload size… (+21 more)

### Community 70 - "api/player_effects.py"
Cohesion: 0.04
Nodes (90): apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest, post (+82 more)

### Community 71 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.06
Nodes (68): _dispatch_player_event(), _format_liabilities(), LucidityChangeEventExtras, LiabilityStackEntry, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send rescue progress/status updates to either participant. (+60 more)

### Community 72 - "alias_storage.py"
Cohesion: 0.02
Nodes (97): AliasPayload, AliasRecord, _AliasValidatorCache, _apply_alias_timestamps(), _as_alias_payload(), _as_alias_record(), _empty_alias_payload(), _get_alias_validator() (+89 more)

### Community 73 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (134): DropCommand, EquipCommand, GetCommand, InventoryCommand, PickupCommand, PutCommand, field_validator, model_validator (+126 more)

### Community 74 - "NATSService"
Cohesion: 0.02
Nodes (122): NATS, NATSConfig, Any, BaseSettings, field_validator, NATS messaging configuration., Validate TLS file paths exist when TLS is enabled., Validate max payload is reasonable. (+114 more)

### Community 75 - "test_combat_validator.py"
Cohesion: 0.06
Nodes (33): Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_combat_command with target name too long., Test validate_target_exists with case-insensitive match., Test validate_target_exists with empty target name., Test validate_target_alive when target is dead., Test validate_combat_state when in combat and combat required., Test validate_combat_state when in combat but combat not required., Test validate_combat_state when not in combat and combat not required. (+25 more)

### Community 76 - "EldritchIcon.tsx"
Cohesion: 0.02
Nodes (115): ChatMessage, ChatMessageType, ChatPanelTest(), mockClick, mockCreateObjectURL, mockRevokeObjectURL, DraggablePanel, DraggablePanelTest() (+107 more)

### Community 77 - "request_with_app_container"
Cohesion: 0.04
Nodes (90): handle_me_command(), handle_pose_command(), handle_reply_command(), handle_say_command(), handle_whisper_command(), Reply to last whisper sender., Room-wide say; returns user-facing result dict., Set or clear persistent pose text. (+82 more)

### Community 78 - "send_game_event"
Cohesion: 0.07
Nodes (40): broadcast_game_event(), _ConnectionManagerAPI, Protocol, UUID, Send a system notification to a player. Args: player_id: The player's ID…, Send a player status update to a player. Args: player_id: The player's ID…, Send room description to a player. Args: player_id: The player's ID room_data:…, Structural type for API helpers; avoids importing ConnectionManager. (+32 more)

### Community 79 - ".state"
Cohesion: 0.09
Nodes (27): Current FSM state as a single State. Uses python-statemachine 3.x configuration…, GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data. (+19 more)

### Community 80 - "test_lucidity_recovery_commands.py"
Cohesion: 0.02
Nodes (157): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+149 more)

### Community 81 - "test_auth_utils.py"
Cohesion: 0.03
Nodes (96): create_access_token(), hash_password(), timedelta, Hash a plaintext password using Argon2id. This function provides superior…, Create a JWT access token., fixture, MonkeyPatch, Unit tests for authentication utilities. (+88 more)

### Community 82 - "Reporter"
Cohesion: 0.03
Nodes (46): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+38 more)

### Community 83 - "test_npc_combat_handlers.py"
Cohesion: 0.06
Nodes (42): CombatResultCtx, Bundle for handle_combat_result (lizard PARAM)., Handle combat result, broadcast, and NPC death., mock_combat_memory(), mock_combat_result(), mock_data_provider(), mock_lifecycle(), mock_messaging_integration() (+34 more)

### Community 84 - "mock_connection_manager"
Cohesion: 0.29
Nodes (7): mock_connection_manager(), mock_validator(), mock_websocket(), fixture, Create a mock WebSocket., Create a mock connection manager., Create a mock message validator.

### Community 85 - "test_status_commands.py"
Cohesion: 0.04
Nodes (81): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_profession_info(), _get_status_persistence(), handle_status_command() (+73 more)

### Community 86 - "build_event"
Cohesion: 0.03
Nodes (89): build_event(), _get_next_global_sequence(), Protocol, UUID, Event envelope utilities for MythosMUD real-time messages. Provides a single,…, Minimal typing for connection_manager passed to build_event (sequence_counter…, Custom JSON encoder that handles UUID objects., Thread-safe global sequence number generation (fallback when no… (+81 more)

### Community 87 - "test_npc_combat_integration_service.py"
Cohesion: 0.04
Nodes (75): integration_service(), asyncio, MonkeyPatch, Unit tests for NPC combat integration service. Tests the…, Test init sets NPC combat integration reference on shared PlayerCombatService., Test init creates CombatService when combat_service is None., Test integration service has combat service with config., Test auto_progression_enabled is set on combat service. (+67 more)

### Community 88 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (88): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+80 more)

### Community 89 - "map/types.ts"
Cohesion: 0.10
Nodes (24): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeBody(), ExitEdgeLabels() (+16 more)

### Community 90 - "PlayerEventHandlerUtils"
Cohesion: 0.01
Nodes (283): Any, UUID, Get the next sequence number for events., Subscribe to relevant game events., Delegate player entered event to specialized handler., Delegate player left event to specialized handler., Delegate NPC entered event to specialized handler., Delegate NPC left event to specialized handler. (+275 more)

### Community 91 - "test_look_room.py"
Cohesion: 0.03
Nodes (102): _filter_other_players(), _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id() (+94 more)

### Community 92 - "test_rescue_service.py"
Cohesion: 0.05
Nodes (57): async_session_factory(), lucidity_service_factory(), mock_event_dispatcher(), mock_lucidity_service(), mock_persistence(), mock_session(), asyncio, fixture (+49 more)

### Community 93 - "NATSMessageBroker"
Cohesion: 0.06
Nodes (38): MessageBrokerConnectionError, MessageBrokerError, PublishError, Exception, Message Broker abstraction for MythosMUD. This module defines the MessageBroker…, Base exception for message broker errors., Exception raised when connection to message broker fails., Exception raised when publishing message fails. (+30 more)

### Community 94 - "test_go_command.py"
Cohesion: 0.04
Nodes (88): handle_explore_command(), Any, Exploration commands for MythosMUD. This module contains handlers for…, Handle exploration requests by returning a simple message. This lightweight…, _cancel_rest_if_moving(), _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement() (+80 more)

### Community 95 - "test_movement_service.py"
Cohesion: 0.03
Nodes (98): check_combat_state(), check_player_posture(), extract_player_id(), Any, Room, UUID, Movement validation helpers for MovementService. Cohesive validation and room-…, Validate player is in the from_room, auto-adding if database matches. (+90 more)

### Community 96 - "multiplayer.ts"
Cohesion: 0.13
Nodes (27): primeBothForCoLocate(), waitForLookReflected(), NOTE: The 'open' command does not exist yet., NOTE: The 'open' command does not exist yet., ensureE2eRuntimeReady(), ensureMultiplayerCoLocated(), cleanupMultiPlayerContexts(), createMultiPlayerContexts() (+19 more)

### Community 97 - "test_nats_service.py"
Cohesion: 0.02
Nodes (140): NATSRequestError, Raised when request/response operations fail., NATSMetrics, Any, NATS metrics collection for MythosMUD. This module provides metrics collection…, NATS-specific metrics collection for monitoring and alerting., Record publish operation metrics., Record subscribe operation metrics. (+132 more)

### Community 98 - "test_admin_setlucidity_command.py"
Cohesion: 0.06
Nodes (73): _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), _get_current_lcd(), _get_player_service_from_app(), _handle_admin_set_lucidity_command() (+65 more)

### Community 99 - "config/models/__init__.py"
Cohesion: 0.02
Nodes (100): Composite application configuration model., ChatConfig, BaseSettings, field_validator, Chat and time configuration models., Chat system configuration., Validate rate limits are reasonable., Ensure we never divide by zero or run the chronicle backward. (+92 more)

### Community 100 - "manual_dependency_analysis.py"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 101 - "item_instance_persistence.py"
Cohesion: 0.05
Nodes (62): CreateItemInstanceInput, EnsureItemInstanceInput, TypedDict, Constants and shared types for async persistence layer. Extracted to keep…, Optional fields for create_item_instance. owner_type, owner_id, etc. with…, Optional fields for ensure_item_instance., Create a new item instance. Delegates to ItemRepository., create_item_instance_async() (+54 more)

### Community 102 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.05
Nodes (91): object, _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch() (+83 more)

### Community 103 - "test_player_presence_tracker.py"
Cohesion: 0.04
Nodes (91): _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _disconnect_during_rest_is_intentional(), _get_instance_manager_from_manager(), Any, UUID, Player presence tracking helper for connection manager. This module provides… (+83 more)

### Community 104 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.05
Nodes (43): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔧 COMMON FIX TEMPLATES, 🔴 CRITICAL (Fix First - Blocking Issues), 🔴 CRITICAL FIXES - Compilation Errors, 🔍 DEBUGGING GUIDE (+35 more)

### Community 105 - "test_message_handlers.py"
Cohesion: 0.09
Nodes (42): handle_chat_message(), handle_client_error_report_message(), handle_command_message(), handle_follow_response_message(), handle_party_invite_response_message(), Any, WebSocket, Handle party_invite_response message (accept/decline party invite). (+34 more)

### Community 106 - "LoggedHTTPException"
Cohesion: 0.06
Nodes (84): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+76 more)

### Community 107 - "test_room_sync_service.py"
Cohesion: 0.03
Nodes (83): get_room_sync_service(), Any, T, Process room update with comprehensive validation. Args: room_data: Room data…, Invalidate stale room cache entry. Args: room_id: Room ID to invalidate…, Fetch fresh room data from room service. Args: room_id: Room ID to fetch…, Handle stale room data by requesting fresh data. Args: room_data: Stale room…, Process room transition with proper ordering and validation. Args:… (+75 more)

### Community 108 - "RoomLoader"
Cohesion: 0.03
Nodes (71): option, fixture, Create a temporary directory for testing., temp_dir(), Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer (+63 more)

### Community 109 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.12
Nodes (24): PartyChannelStrategy, Strategy for party channel broadcasting. Delivers only to current party members., asyncio, Unit tests for channel broadcasting strategies. Tests the…, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() sends personal message. (+16 more)

### Community 110 - "test_circuit_breaker.py"
Cohesion: 0.10
Nodes (19): Unit tests for circuit breaker. Tests the CircuitBreaker class and…, Test _on_success() resets failure count in CLOSED state., Test _on_failure() increments failure count., Test _on_failure() resets success count., Test _should_attempt_reset() returns True after timeout., Test _should_attempt_reset() returns False when not OPEN., Test _time_until_retry() returns 0 after timeout., Test get_stats() returns comprehensive statistics. (+11 more)

### Community 111 - "CorpseOverlay.tsx"
Cohesion: 0.04
Nodes (71): BackpackTab(), BackpackTabProps, ContainerSplitPane(), ContainerSplitPaneProps, ContainerInventoryPaneProps, ContainerItemRow(), ContainerSplitPaneView(), ContainerSplitPaneViewModel (+63 more)

### Community 112 - "test_follow_service.py"
Cohesion: 0.03
Nodes (79): connection_manager(), event_bus(), follow_service(), movement_service(), asyncio, fixture, Unit tests for FollowService. Covers: request_follow (self reject, NPC…, follow_request producer emits a build_event-shaped envelope. (+71 more)

### Community 113 - "test_nats_broker.py"
Cohesion: 0.03
Nodes (82): nats_broker(), nats_config(), asyncio, fixture, Unit tests for NATS message broker. Tests the NATSMessageBroker class., Test connect() passes TLS options to nats.connect when tls_enabled=True., Test disconnect() does nothing when no client., Test disconnect() successfully disconnects. (+74 more)

### Community 114 - "test_websocket_handler_validation_errors.py"
Cohesion: 0.04
Nodes (62): asyncio, Unit tests for WebSocket handler validation, rate limiting, and error paths.…, _validate_message should pass expected token from connection metadata into…, When metadata.token is missing, validate JWT from message and restore metadata., Test _send_error_response handles WebSocket disconnect., Test _send_error_response handles RuntimeError with disconnect message., Test _send_error_response handles RuntimeError with close message., Test _send_error_response handles other RuntimeError. (+54 more)

### Community 115 - "UserManager"
Cohesion: 0.07
Nodes (31): UUID, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Update cache to mark load as failed., Convert mute_info datetime and UUID objects to JSON-serializable formats., Save player mutes to data dictionary for JSON serialization., Save channel mutes to data dictionary for JSON serialization., Save global mutes applied by this player to data dictionary for JSON… (+23 more)

### Community 116 - "test_look_player.py"
Cohesion: 0.02
Nodes (181): _get_health_label(), _get_lucidity_label(), _get_visible_equipment(), _get_wearable_container_service(), _is_direction(), _parse_instance_number(), Any, Helper functions for look command. This module contains utility functions used… (+173 more)

### Community 117 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (90): _collect_rotatable_logs(), detect_environment(), ensure_log_directory(), BoundLogger, Path, Logging utilities for directory management, path resolution, and environment…, Resolve log_base path to absolute path relative to project root. Args:…, Collect non-empty log files eligible for rotation. (+82 more)

### Community 118 - "User"
Cohesion: 0.02
Nodes (175): CharacterInfo, get_container, get_current_active_user, IntegrityError, get_current_superuser(), Get current superuser or raise 403., _authenticate_user_credentials(), _check_shutdown_status() (+167 more)

### Community 119 - "test_combat_monitoring_service.py"
Cohesion: 0.03
Nodes (91): AlertSeverity, AlertType, CombatMetrics, end_combat_monitoring(), get_combat_metrics(), get_combat_monitoring(), Enum, Combat monitoring and alerting service for MythosMUD. This service provides… (+83 more)

### Community 120 - "_NPCCombatIntegrationDeps"
Cohesion: 0.13
Nodes (15): NPCCombatIntegrationCombatMixin, _NPCCombatIntegrationDeps, Protocol, UUID, Structured logging / observability trail when NPC-initiated combat begins., Process combat attack, starting new combat or continuing existing one., Start a new combat and process initial attack., Broadcast room occupants update to killer's room after NPC death. Swallows… (+7 more)

### Community 121 - "test_nats_message_handler_chat.py"
Cohesion: 0.03
Nodes (76): asyncio, Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _get_player_lucidity_tier returns default on error., Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_name…, Test _validate_chat_message_fields raises TypeError for invalid content type., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _extract_chat_message_fields handles whisper target_id. (+68 more)

### Community 122 - "run_flee_effect"
Cohesion: 0.15
Nodes (28): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+20 more)

### Community 123 - "types/mythosTime.ts"
Cohesion: 0.08
Nodes (41): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, appendDaypartChange(), appendHourChime() (+33 more)

### Community 124 - "SchemaValidator"
Cohesion: 0.03
Nodes (44): Path, Convert legacy string format exits to new object format internally. This allows…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in… (+36 more)

### Community 125 - "test_command_factories_moderation.py"
Cohesion: 0.04
Nodes (56): Unit tests for moderation command factories. Tests the ModerationCommandFactory…, Test create_mute_global_command() with duration and reason., Test create_mute_global_command() with reason but no duration., Test create_unmute_global_command() creates UnmuteGlobalCommand., Test create_unmute_global_command() raises error with no args., Test create_unmute_global_command() raises error with multiple args., Test create_admin_command() creates AdminCommand., Test create_mute_command() creates MuteCommand. (+48 more)

### Community 126 - "test_chat_npc_system.py"
Cohesion: 0.06
Nodes (58): _ChatDeliveryService, deliver_npc_room_speech(), deliver_personal_system(), npc_sender_id(), _on_npc_spoke(), Protocol, UUID, NPC and personal system chat delivery via ChatService (issue #146 MVP). #… (+50 more)

### Community 127 - "test_container_websocket_events.py"
Cohesion: 0.09
Nodes (41): emit_container_closed(), emit_container_decayed(), emit_container_opened(), emit_container_opened_to_room(), emit_container_updated(), Any, ContainerComponent, datetime (+33 more)

### Community 128 - "MinimapRenderer"
Cohesion: 0.10
Nodes (16): MinimapRenderer, Any, Renders room connectivity graphs in various visual formats. Implements the…, Extract street acronym from room ID. Args: room_id: Full room ID (e.g.,…, Extract street name from room ID. Args: room_id: Full room ID Returns: Street…, Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…, Render the mini-map as ASCII art with grid-based visualization. Args:…, Initialize the mini-map renderer. (+8 more)

### Community 129 - "MythosChronicle"
Cohesion: 0.02
Nodes (119): Container API endpoints for unified container system. As documented in the…, broadcast_message(), get_game_status(), get_mythos_time(), get, post, Game mechanics API endpoints for MythosMUD server. This module handles all game…, Return the current Mythos calendar metadata for HUD initialization. In-memory… (+111 more)

### Community 130 - "MythosTimeEventConsumer"
Cohesion: 0.04
Nodes (34): MythosHourTickEvent, Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type. (+26 more)

### Community 131 - "chatPanelRuntimeUtils.ts"
Cohesion: 0.05
Nodes (71): filterMessagesForChannelView(), EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW, isGloballyExcludedFromChannelView(), isVisibleInChannelView(), matchesChannelSelection(), resolveMessageChannelForFilter(), buildChatExportCSV(), buildChatExportCsvRow() (+63 more)

### Community 132 - "test_room_utils.py"
Cohesion: 0.07
Nodes (42): Unit tests for room_utils. Tests utility functions for room operations., Test get_subzone_local_channel_subject() generates subject., Test get_subzone_local_channel_subject() returns None for invalid room ID., Test extract_subzone_from_room_id() extracts subzone., Test extract_subzone_from_room_id() extracts different subzone., Test extract_subzone_from_room_id() returns None for invalid format., Test get_zone_from_room_id() extracts zone., Test get_zone_from_room_id() extracts different zone. (+34 more)

### Community 133 - "Any"
Cohesion: 0.06
Nodes (21): Any, Retrieve current room drops as a defensive copy for callers. Args: room_id: The…, Append an item stack to the room drop ledger. Args: room_id: The room receiving…, Remove quantity of a drop entry, returning the removed stack. Args: room_id:…, Adjust quantity for an existing drop entry; removing entry when zero. Args:…, Add a player as an occupant of a room. Args: player_id: The player's ID…, Remove a player as an occupant of a room. Args: player_id: The player's ID…, Get online player occupants from room_occupants and room_subscriptions. Uses… (+13 more)

### Community 134 - "test_alias_commands.py"
Cohesion: 0.05
Nodes (70): _create_alias(), _extract_alias_params(), handle_alias_command(), handle_aliases_command(), handle_unalias_command(), Any, Alias management commands for MythosMUD. This module contains handlers for…, Handle the aliases command for listing all aliases. Args: command_data: Command… (+62 more)

### Community 135 - "WebSocketMessageValidator"
Cohesion: 0.05
Nodes (67): MessageValidationError, BaseModel, Exception, WebSocket message validation for MythosMUD. This module provides comprehensive…, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Validate message against Pydantic schema. Args: message: Parsed JSON message…, Raised when message validation fails. (+59 more)

### Community 136 - "test_skill_service.py"
Cohesion: 0.05
Nodes (65): catalog_with_own_language_and_mythos(), mock_persistence(), mock_player_skill_repo(), mock_skill_repo(), mock_skill_use_log_repo(), _occupation_slots_9(), _personal_interest_4(), asyncio (+57 more)

### Community 137 - "RoomDataCache"
Cohesion: 0.04
Nodes (39): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Manages room data caching and freshness validation., Check if new data is newer than old data for a specific key. Args: old_data:…, Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,… (+31 more)

### Community 138 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_player_data_for_respawn() returns None when player not found., Test get_player_data_for_respawn() handles errors., Test send_respawn_event_with_retry() is a no-op when connection manager is…, Test get_current_lucidity() returns lucidity from database., Test get_player_data_for_delirium_respawn() successfully retrieves player data., Test get_player_data_for_delirium_respawn() returns None when player not found., test_get_current_lucidity_found() (+5 more)

### Community 139 - "server/schemas/__init__.py"
Cohesion: 0.02
Nodes (178): get_current_user(), Get current user with enhanced logging., _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _as_float(), _as_int(), _check_shutdown_status(), _convert_stat_summary_to_stat_summary_model() (+170 more)

### Community 140 - "NPCCombatIntegrationService"
Cohesion: 0.03
Nodes (58): NPCCombatHandlers, Any, Handle NPC death when combat ends, with defensive exception handling. Args:…, Handle NPC death and related effects., Check if a string is a valid UUID., Handles combat result processing and NPC death operations., Initialize the combat handlers. Args: data_provider: NPC combat data provider…, NPCCombatIntegrationService (+50 more)

### Community 141 - "catatonia_check.py"
Cohesion: 0.03
Nodes (90): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+82 more)

### Community 142 - "NATSError"
Cohesion: 0.04
Nodes (74): NATSError, Base exception for all NATS-related errors., asyncio, Unit tests for NATS message handler subzone and event handling. Tests subzone…, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test subscribe_to_subzone raises error when subject manager unavailable., Test unsubscribe_from_event_subjects handles partial success. (+66 more)

### Community 143 - "TrackedTaskManager"
Cohesion: 0.09
Nodes (27): memory_leak_prevention_channel_start_session(), patch_asyncio_create_task_with_tracking(), Audit and reclaim orphaned task candidates across the system. Returns: Number…, Proactively clean up orphaned tasks by cancelling leak prevention violations.…, Return count of currently tracked task references within the manager's…, Attach a TaskRegistry instance to this Tracker for shared coordination. Args:…, Central namespace for tracked task lifecycle coordination preventing orphaned…, Reset the global tracked manager for testing. (+19 more)

### Community 144 - "test_rest_command.py"
Cohesion: 0.05
Nodes (79): Check if player is resting or in login grace period, interrupt rest if needed.…, Check if player is resting or in login grace period, interrupt rest if needed., _begin_seated_rest_countdown(), cancel_rest_countdown(), _check_player_in_combat(), _check_rest_location(), _disconnect_player_intentionally(), _execute_rest_flow() (+71 more)

### Community 145 - "test_user_schemas.py"
Cohesion: 0.17
Nodes (15): Schema for creating a new user., Schema for updating user data., UserCreate, UserUpdate, Unit tests for user schemas. Tests the Pydantic models in user.py module., Test UserCreate can be instantiated., Test UserCreate validates password length., Test UserUpdate can be instantiated with optional fields. (+7 more)

### Community 146 - "WearableContainerService"
Cohesion: 0.10
Nodes (25): _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Wearable container service for unified container system. As documented in the…, Return existing equipment container ID for item instance if present., Create wearable container in persistence and return container_id payload. (+17 more)

### Community 147 - "PlayerRespawnService"
Cohesion: 0.10
Nodes (23): PlayerRespawnService, AsyncSession, Player, UUID, Return current_dp as an int, defaulting to 0 for non-numeric values., Return (allowed, current_dp_int) for limbo movement gate checks., Publish delirium respawn event when event bus is available., Clear combat state for a respawning player, logging and swallowing DB errors. (+15 more)

### Community 148 - "test_npc_combat_integration_class.py"
Cohesion: 0.07
Nodes (39): asyncio, Unit tests for server.npc.combat_integration.NPCCombatIntegration (helpers and…, Invalid UUID with npc_stats returns normalized NPC stats., Killer path loads player and calls game mechanics helpers., After damage, old_dp reflects pre-hit value., Display name resolves from lifecycle_manager.active_npcs when present., When lifecycle manager is unavailable, display name lookup returns None., Digit strings coerce to int. (+31 more)

### Community 149 - "test_player_death_service.py"
Cohesion: 0.03
Nodes (85): mock_event_bus(), mock_player_combat_service(), mock_session(), player_death_service(), player_death_service_no_dependencies(), asyncio, fixture, Unit tests for player death service. Tests the PlayerDeathService class for… (+77 more)

### Community 150 - "admin_summon_command.py"
Cohesion: 0.08
Nodes (51): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), handle_summon_command(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any (+43 more)

### Community 151 - "LootAllRequest"
Cohesion: 0.03
Nodes (81): _audit_loot_all(), _build_loot_all_response(), loot_all_items(), Any, APIRouter, Request, Container loot-all endpoint. Handles the convenience action to transfer all…, Register loot-all endpoint to the router. (+73 more)

### Community 152 - "PassiveMobNPC"
Cohesion: 0.06
Nodes (52): PassiveMobNPC, Respond to player interaction., Handle responding to greeting action., Handle fleeing action., Passive mob NPC type with wandering and response behaviors., Setup passive mob-specific behavior rules., Get passive mob-specific behavior rules., asyncio (+44 more)

### Community 153 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.10
Nodes (52): check_ai_guardrails(), _check_single_use_file(), _collect_code_texts(), _guardrail_scan_inputs(), _is_single_use_small_file(), _process_added_file_checks(), build_context(), ChangedFile (+44 more)

### Community 154 - "test_population_stats.py"
Cohesion: 0.05
Nodes (39): Unit tests for population statistics. Tests the PopulationStats class., Test remove_npc() removes optional NPC., Test remove_npc() decrements count when multiple exist., Test remove_npc() handles removal when NPC not found., Test PopulationStats initialization., Test remove_npc() prevents negative counts., Test remove_npc() handles None definition_id., Test remove_npc() updates last_updated timestamp. (+31 more)

### Community 155 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.05
Nodes (37): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI SUCCESS METRICS, 🔧 COMMON FIX TEMPLATES, Component Rendering Issues, 🔴 CRITICAL (Fix First - Blocking Issues), 🔴 CRITICAL FIXES - TypeScript Errors, For Each Failure Category (+29 more)

### Community 156 - "test_connection_cleanup_methods.py"
Cohesion: 0.08
Nodes (31): check_and_cleanup_impl(), cleanup_dead_connections_impl(), cleanup_ghost_players_impl(), cleanup_orphaned_data_impl(), force_cleanup_impl(), prune_stale_players_impl(), Any, UUID (+23 more)

### Community 157 - "talk_command.py"
Cohesion: 0.04
Nodes (73): _emit_prompt(), handle_talk_command(), UUID, talk / talk <n> command for NPC dialogue trees (#583)., Handle talk <npc> or talk <n> against same-room NPCs., Extract player UUID from player model., Join talk args into a single remainder string., Send personal system message for a node; return short command result. (+65 more)

### Community 158 - "legacy_error_sanitization.py"
Cohesion: 0.05
Nodes (44): _collect_safe_context_fields(), _contains_sensitive_detail_pattern(), is_safe_detail_key(), Sanitization helpers for legacy MythosMUD error responses. Extracted from…, Sanitize dictionary detail values, keeping only safe keys., Sanitize each element in a list detail value., Return detail dict entries that use safe keys with sanitized values., Sanitize a detail value to prevent information exposure. Uses bleach for HTML… (+36 more)

### Community 159 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages. These schemas define the structure and… (+55 more)

### Community 160 - "get_logger"
Cohesion: 0.00
Nodes (865): HolidayResolver, NPC population and system status admin endpoints. Split out from…, NPC Admin API endpoints for MythosMUD server. This module provides the router…, Router and shared auth helper for NPC Admin API. Submodules import from here to…, Base API router and common dependencies for MythosMUD server. This module…, Game tick processing functions. This module handles all game tick processing…, # NOTE: This remains global for now as it's shared state needed by combat system, Event subscription setup for application startup. Extracted from… (+857 more)

### Community 161 - "test_room_subscription_manager_drops.py"
Cohesion: 0.20
Nodes (9): Unit tests for room subscription manager drop functions. Tests the room drop…, Test take_room_drop() with quantity larger than available., Test adjust_room_drop() successfully adjusts quantity., Test add_room_drop() handles negative quantity gracefully., Test take_room_drop() removes drop from room., test_add_room_drop_negative_quantity(), test_adjust_room_drop_success(), test_take_room_drop() (+1 more)

### Community 162 - "PlayerChannelPreferences"
Cohesion: 0.17
Nodes (12): PlayerChannelPreferences, Player channel preferences model for Advanced Chat Channels. Stores player…, Test PlayerChannelPreferences can be instantiated with required fields., Test PlayerChannelPreferences has correct default values., Test PlayerChannelPreferences can have muted channels., Test PlayerChannelPreferences has correct table name., Test PlayerChannelPreferences __repr__ method., test_player_channel_preferences_creation() (+4 more)

### Community 163 - "test_validation.py"
Cohesion: 0.02
Nodes (101): get_chat_subscription_patterns(), get_event_subscription_patterns(), get_subscription_pattern(), Any, Subscription pattern utilities for NATS Subject Manager. This module provides…, Convert a pattern template into a subscription pattern with wildcards. Args:…, Get all chat-related subscription patterns. Args: patterns: Dictionary of…, Get all event-related subscription patterns. Args: patterns: Dictionary of… (+93 more)

### Community 164 - "rescue_commands.py"
Cohesion: 0.06
Nodes (63): _apply_grounding_adjustment(), _complete_ground_command(), _get_ground_services(), handle_ground_command(), handle_rescue_command(), _normalize_player_ids(), Any, UUID (+55 more)

### Community 165 - "test_combat_service_modules.py"
Cohesion: 0.04
Nodes (79): clear_aggro_for_combat(), Clear all aggro state for this combat (call on combat end)., CombatDPSync, Any, Get persistence layer from application container. Args: player_id: Player ID…, Verify that player DP was successfully saved to database. Args: persistence:…, Log death threshold events based on DP changes. Args: current_dp: New current…, Update player DP and save to database. Args: persistence: Persistence layer… (+71 more)

### Community 166 - "CombatConfiguration"
Cohesion: 0.04
Nodes (50): CombatConfiguration, CombatConfigurationError, CombatConfigurationScope, CombatConfigurationService, get_combat_config(), get_combat_configuration(), is_combat_available(), Any (+42 more)

### Community 167 - "middleware"
Cohesion: 0.10
Nodes (32): CorrelationMiddleware, create_correlation_middleware(), create_websocket_correlation_middleware(), _get_header(), ASGIApp, Receive, Scope, Send (+24 more)

### Community 168 - "chat_service.py"
Cohesion: 0.05
Nodes (69): ChatResult, _append_channel_history(), _authorize_global_sender(), _authorize_system_sender(), ChatLogger, ChatPlayerService, ChatPlayerView, ChatRateLimiter (+61 more)

### Community 169 - "test_command_magic.py"
Cohesion: 0.04
Nodes (58): CastCommand, LearnCommand, field_validator, Magic command models for MythosMUD. This module provides command models for…, Command for casting a spell., Validate spell name format., Validate target format., Command for viewing spell details. (+50 more)

### Community 170 - "test_wearable_container_service.py"
Cohesion: 0.03
Nodes (82): asyncio, Unit tests for wearable container service. Tests the WearableContainerService…, Test handle_unequip_wearable_container returns None when no item_instance_id., Test handle_unequip_wearable_container preserves container., Test handle_unequip_wearable_container returns None when container not found., Test get_wearable_containers_for_player returns containers., Test get_wearable_containers_for_player returns empty list when no containers., Test get_wearable_containers_for_player handles errors gracefully. (+74 more)

### Community 171 - "PartyService"
Cohesion: 0.10
Nodes (26): PartyService, Any, UUID, Create a new party with the given player as leader. Returns dict with success…, Disband a party. If by_player_id is given, only the leader may disband. If…, Add a player to a party. Fails if party does not exist or player is already in…, Remove expired pending invites and notify inviters., Send a command_response-style message to a single player. (+18 more)

### Community 172 - "AggressiveMobNPC"
Cohesion: 0.14
Nodes (11): AggressiveMobNPC, Flee from current situation., Aggressive mob NPC type with hunting and territorial behaviors., Handle fleeing action., Initialize aggressive mob NPC., Setup aggressive mob-specific behavior rules., Get aggressive mob-specific behavior rules., _enrich_behavior_context sets False when current_room is None. (+3 more)

### Community 173 - "test_quest_service.py"
Cohesion: 0.06
Nodes (82): _DefinitionRow, _FullInventory, _InstanceStub, _make_definition_row(), _make_kill_definition_row(), _make_turn_in_definition_row(), _message(), mock_def_repo() (+74 more)

### Community 174 - "test_async_persistence_room_cache.py"
Cohesion: 0.14
Nodes (13): Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test _generate_room_id_from_zone_data with None values., Test _parse_exits_json with invalid JSON string., Test _process_exits_for_room processes exits with direction., Test _process_exits_for_room skips exits without direction., Test _process_combined_rows processes rows with exits JSON., Test _process_exit_rows handles missing direction., test_generate_room_id_from_zone_data_none_values() (+5 more)

### Community 175 - "session_factory"
Cohesion: 0.08
Nodes (42): FixtureRequest, get_postgres_connect_args(), Build connect_args for asyncpg when POSTGRES_SEARCH_PATH is set. Used so unit…, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url() (+34 more)

### Community 176 - "NATSMessageSubscriptionMixin"
Cohesion: 0.12
Nodes (9): NATSMessageSubscriptionMixin, Mixin: room, subzone, and event NATS subscription lifecycle., Subscribe to chat messages for a specific room. Args: room_id: Room ID to…, Subscribe to all event-related NATS subjects using standardized patterns.…, Unsubscribe from all event-related NATS subjects using standardized patterns.…, Get the number of active event subscriptions. Returns: Number of active event…, Check if a specific event subscription is active. Args: subject: NATS subject…, Get the number of active subscriptions. (+1 more)

### Community 177 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (34): CatatoniaRegistry, datetime, UUID, Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not…, asyncio (+26 more)

### Community 178 - "mapUtils.ts"
Cohesion: 0.12
Nodes (30): fetchSpy, useMapLayout(), buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData(), UseRoomMapDataResult (+22 more)

### Community 179 - "test_occupant_formatter.py"
Cohesion: 0.04
Nodes (45): Unit tests for occupant formatter. Tests the occupant_formatter module classes…, Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists., Test OccupantFormatter._process_player_name_for_update() adds valid player name., Test OccupantFormatter.__init__() initializes formatter., Test OccupantFormatter._process_player_name_for_update() skips UUID player name., Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name., Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes player… (+37 more)

### Community 180 - "test_party_service.py"
Cohesion: 0.04
Nodes (49): Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves., Leader can disband the party., Non-leader cannot disband. (+41 more)

### Community 181 - "UUID"
Cohesion: 0.17
Nodes (8): UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return True if websocket appears dead (should be cleaned up)., Return list of player IDs to check (single player or all)., Clean up dead connections for a single player., Clean up dead connections for a specific player or all players. Args:…

### Community 182 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 183 - "test_container_persistence.py"
Cohesion: 0.05
Nodes (37): Unit tests for container_persistence helpers and fetch_container_items. Tests…, Test fetch_container_items with items., Test fetch_container_items skips rows with missing item_instance_id., Test fetch_container_items handles non-dictionary rows., Test fetch_container_items parses string metadata., Test fetch_container_items handles invalid JSON metadata., Test fetch_container_items handles non-dict metadata., Test parsing None JSONB column. (+29 more)

### Community 184 - "useGameClientV2Container.ts"
Cohesion: 0.09
Nodes (44): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), forceLogoutFallback(), performGameClientLogout(), stillShowingGameClient() (+36 more)

### Community 185 - "test_player_service.py"
Cohesion: 0.06
Nodes (45): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service CRUD and lookup. Delete, location, mythos status,…, Test get_player_by_id() when player is not found., Test get_player_by_name() when player is found., Test get_player_by_name() when player is not found. (+37 more)

### Community 186 - "Uplift Strategy"
Cohesion: 0.04
Nodes (49): 0.2 Update conftest.py ✅, 2.1 Categorize Unit Tests by Dependency Pattern, 4.1 Test ApplicationContainer Itself, Actions, AFTER, AFTER, AFTER, AFTER (+41 more)

### Community 187 - "TargetResolutionService"
Cohesion: 0.02
Nodes (115): BaseModel, Target metadata schema for MythosMUD. This module defines Pydantic models for…, Metadata about a target in target resolution. This model represents additional…, TargetMetadata, StrEnum, Target resolution schemas for MythosMUD. This module defines Pydantic models…, Enumeration of possible target types., TargetType (+107 more)

### Community 188 - "QuestService"
Cohesion: 0.05
Nodes (60): Persist player after spell mutations., Quest subsystem: service, goal progression, rewards., _build_collect_n_progress(), _call_add_item_to_inventory(), _collect_goal_prototype_id(), _collect_goal_required_count(), _consume_collect_goals_from_player(), _definition_completion_mode_error() (+52 more)

### Community 189 - "fixtures/unit/__init__.py"
Cohesion: 0.13
Nodes (18): MockerFixture, dummy_request(), fakerandom(), Any, fixture, SimpleNamespace, Unit-tier fixtures with strict mocking and in-memory fakes., Provide deterministic random seed for unit tests. (+10 more)

### Community 190 - "asyncio"
Cohesion: 0.05
Nodes (37): asyncio, Test is_player_muted_async() returns True when player is muted., Test is_player_muted_async() returns False when player is not muted., Test add_admin() handles missing container., Test add_admin() handles missing persistence., Test add_admin() handles player not found., Test remove_admin() handles missing container., Test remove_admin() handles missing persistence. (+29 more)

### Community 191 - "test_memory_profiler.py"
Cohesion: 0.09
Nodes (21): Unit tests for memory profiler utilities. Tests the MemoryProfiler class…, Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test MemoryProfiler.measure_model_deserialization() returns stats., Test MemoryProfiler initialization., Test MemoryProfiler.compare_models_memory_usage() aggregates stats., Test MemoryProfiler.print_comparison_results() prints stats block., Test MemoryProfiler.start_profiling() sets baseline. (+13 more)

### Community 192 - "test_combat_event_publisher.py"
Cohesion: 0.03
Nodes (125): CombatEndedEvent, CombatStartedEvent, CombatTimeoutEvent, CombatTurnAdvancedEvent, NPCAttackedEvent, NPCTookDamageEvent, PlayerAttackedEvent, Combat-specific events for the MUD. This module defines combat-related events… (+117 more)

### Community 193 - ".load_room_data"
Cohesion: 0.06
Nodes (19): Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path., Validate or update room ID based on filename and location., Validate required fields are present., Add location fields if missing. (+11 more)

### Community 194 - "test_command_player_state.py"
Cohesion: 0.06
Nodes (47): GroundCommand, LieCommand, LogoutCommand, field_validator, QuitCommand, Player state command models for MythosMUD. This module provides command models…, Command for quitting the game., Command for logging out of the game. (+39 more)

### Community 195 - "IdleMovementHandler"
Cohesion: 0.04
Nodes (67): IdleMovementHandler, Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement. Checks multiple conditions: -…, Check if NPC is in combat via UUID lookup. Args: npc_id: NPC ID (string or…, Check if NPC is in combat via string ID mapping. Args: npc_id: NPC ID as string…, Check if an NPC is currently in combat. Args: npc_instance: The NPC instance to…, Handler for NPC idle movement logic. This class manages the decision-making and…, patch (+59 more)

### Community 196 - "_handle_admin_set_stat_command"
Cohesion: 0.05
Nodes (72): _AdminSetStatApplyContext, _AdminSetStatLogContext, _apply_stat_change_and_build_result(), _build_set_stat_error_response(), _calculate_stat_warnings(), _get_app_or_error(), _handle_admin_set_stat_command(), _log_admin_set_stat() (+64 more)

### Community 197 - "test_error_logging.py"
Cohesion: 0.05
Nodes (66): log_with_context(), BoundLogger, Log a message with the current context automatically included. Args:…, Unit tests for enhanced_error_logging utilities. Tests error logging helper…, Test create_error_context() creates error context., test_create_enhanced_error_context(), test_create_error_context(), test_create_logged_http_exception_enhanced() (+58 more)

### Community 198 - "combat_taunt.py"
Cohesion: 0.06
Nodes (49): _apply_taunt_and_maybe_broadcast(), AppWithState, Protocol, UUID, Taunt command flow: validation and execution. Extracted from combat.py to…, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Apply taunt and broadcast target switch if aggro changed. Returns error dict or… (+41 more)

### Community 199 - "Any"
Cohesion: 0.17
Nodes (9): Any, WebSocket, Handle a specific message type. Args: websocket: The WebSocket connection…, Handle command message type., Handle chat message type., Handle ping message type., Handle follow_response message type., Handle party_invite_response message type. (+1 more)

### Community 200 - "DeadLetterQueue"
Cohesion: 0.02
Nodes (112): DeadLetterMessage, DeadLetterQueue, Any, Path, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve and remove oldest message from DLQ (async version). Returns: Message…, Retrieve and remove oldest message from DLQ (sync version). Returns: Message… (+104 more)

### Community 201 - "Commands"
Cohesion: 0.17
Nodes (12): Add a branch — `gh stack add`, Check out a stack — `gh stack checkout`, Commands, Initialize a stack — `gh stack init`, Link branches as a stack (no local tracking) — `gh stack link`, Navigate the stack, Push branches to remote — `gh stack push`, Rebase the stack — `gh stack rebase` (+4 more)

### Community 202 - "CombatPersistenceHandler"
Cohesion: 0.05
Nodes (39): CombatPersistenceHandler, Any, UUID, Combat persistence handling logic. Handles player DP persistence, verification,…, # NOTE: The game tick loop will also check for dead players, but this provides…, Synchronously persist player DP to database. This is the actual persistence…, Persist player DP to database in background (fire-and-forget). This method runs…, Handles combat-related persistence operations. (+31 more)

### Community 203 - "test_map_helpers.py"
Cohesion: 0.08
Nodes (36): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities. Extracted from… (+28 more)

### Community 204 - "test_inventory_helpers.py"
Cohesion: 0.03
Nodes (129): _equip_stack_from_inventory_index(), _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), handle_wearable_container_on_unequip(), normalize_equipped_items(), InventoryStack, Player (+121 more)

### Community 205 - "Any"
Cohesion: 0.06
Nodes (18): Any, T, Task, Signal shutdown to async processing loop., Cancel the main processing task if it exists., Cancel all active tasks and wait for graceful shutdown., Finalize shutdown by clearing tasks and logging., Stop pure async event processing gracefully. (+10 more)

### Community 206 - "MonitoringDashboard"
Cohesion: 0.03
Nodes (94): PerformanceStats, Response model for system monitoring summary., SystemMonitoringSummaryResponse, get_system_health(), get_system_metrics(), get_system_monitoring_alerts(), get_system_monitoring_summary(), get (+86 more)

### Community 207 - "EventHandler"
Cohesion: 0.06
Nodes (41): _as_event_data_dict(), EventHandler, _npc_died_ids_or_warn(), _participant_key_strings(), Handler for NATS event messages., Initialize event handler. Args: connection_manager: ConnectionManager instance…, Get mapping of event types to their handler methods. Returns: Dictionary…, Validate that event message has required fields. Args: event_type: Event type… (+33 more)

### Community 208 - "useAsciiMapState.ts"
Cohesion: 0.08
Nodes (38): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+30 more)

### Community 209 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 210 - "MemoryMonitor"
Cohesion: 0.07
Nodes (16): ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor, MemoryMonitorOptions (+8 more)

### Community 211 - "fixtures/auth.ts"
Cohesion: 0.07
Nodes (45): nudgeStandBothPlayers(), loginAdminPlayable(), assertCommandChannelReady(), ensurePlayableConnection(), EnsurePlayableConnectionOptions, getLivePageForUsername(), getPageSessionCredentials(), isPageUsable() (+37 more)

### Community 212 - "NPCCombatUUIDMapping"
Cohesion: 0.05
Nodes (34): Return UUID mapping dependency for integration collaborators., NPCCombatUUIDMapping, UUID, Get the original string ID from a UUID. Args: uuid_id: The UUID to look up…, Get XP value for a UUID. Args: uuid_id: The UUID to look up Returns: XP value…, Manages UUID mappings for NPC combat., Initialize UUID mapping storage., Check if a string is a valid UUID. Args: uuid_string: String to check Returns:… (+26 more)

### Community 213 - "logging_file_setup.py"
Cohesion: 0.04
Nodes (78): Formatter, Logger, _PlayerGuidFormatterType, Queue, QueueListener, _add_handler_to_loggers(), _CategoryHandlerConfig, _ConsoleHandlerConfig (+70 more)

### Community 214 - "_as_mgr"
Cohesion: 0.13
Nodes (25): _as_mgr(), _FakeSessionManager, _make_manager(), asyncio, Typed stand-in for ConnectionManager; MagicMock attributes are Any., Test _disconnect_connection_for_session() returns False when not in…, Test _disconnect_connection_for_session() handles None websocket., Test _disconnect_all_connections_for_session() handles empty list. (+17 more)

### Community 215 - "safe_run_static"
Cohesion: 0.05
Nodes (52): get_project_root(), Determine the project root based on current working directory, main(), Run a psql command and return the result., Load all seed data files., run_psql_command(), _combined_output(), _CompletedProcessLike (+44 more)

### Community 216 - "gen_arena_migration_sql.py"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 217 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 218 - "NATSSubjectManager"
Cohesion: 0.01
Nodes (195): get_patterns(), get_subject_manager_dependency(), get_subject_statistics(), PatternsResponse, BaseModel, get, post, NATS Subject Management API Controller for MythosMUD. This module provides REST… (+187 more)

### Community 219 - "api/player_respawn.py"
Cohesion: 0.12
Nodes (37): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Any, post, Request, ValidationError, Player respawn API endpoints. This module handles endpoints for respawning…, Respawn a delirious player at the Sanitarium with restored lucidity. This… (+29 more)

### Community 220 - "asyncio"
Cohesion: 0.10
Nodes (32): broadcast_tick_event(), game_tick_loop(), _process_all_status_effects(), process_casting_progress(), process_dp_decay_and_death(), process_player_effects_expiration(), _process_player_status_effects(), process_status_effects() (+24 more)

### Community 221 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+21 more)

### Community 222 - "test_channel_commands.py"
Cohesion: 0.09
Nodes (40): _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting(), Any, Channel management commands for Advanced Chat Channels. This module provides…, Validate channel name. Returns error dict if invalid, None if valid., Handle the channel command for switching channels or setting default channel.… (+32 more)

### Community 223 - "test_connection_cleaner.py"
Cohesion: 0.08
Nodes (30): connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue(), mock_rate_limiter(), mock_room_manager() (+22 more)

### Community 224 - "Any"
Cohesion: 0.10
Nodes (15): Any, UUID, Raise ValueError if any skill_id appears in both occupation and personal…, Build skill_key -> total modifier from profession skill_modifiers (supports…, Compute final skill_id -> value: base + profession mod, then occupation…, Validate skills allocation without persisting. Raises ValueError if invalid.…, Set all skills for a character at creation. Validates occupation_slots (9…, Return list of {skill_id, skill_key, skill_name, value} for the player. If the… (+7 more)

### Community 225 - "CombatMonitoringService"
Cohesion: 0.04
Nodes (36): Alert, CombatMonitoringService, Any, Convert to dictionary., Comprehensive combat monitoring and alerting service. Tracks combat system…, Initialize the combat monitoring service., Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier… (+28 more)

### Community 226 - "TargetMatch"
Cohesion: 0.03
Nodes (125): Resolve a typed target match for the given name in the current context., NpcIntegrationStringIdPort, NpcLifecycleManagerPort, NpcSpellDamageTarget, PlayerPersistenceSpellPort, PlayerServiceHealPort, Protocol, UUID (+117 more)

### Community 227 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test get_room_occupants() returns occupants., Test get_room_occupants() returns empty list when no occupants., Test get_room_occupants() handles errors gracefully., Test get_room_subscribers() returns subscribers., test_get_room_occupants() (+5 more)

### Community 228 - "ChatService"
Cohesion: 0.02
Nodes (120): ChatService, _publish_room_chat(), ChatMessage, UUID, _rate_limit_result(), Chat service for handling real-time communication between players. This service…, Normalize player identifiers to string form., Send a say message to players in the same room. This method publishes the… (+112 more)

### Community 229 - "test_rest_and_grace_period.py"
Cohesion: 0.07
Nodes (40): is_player_in_grace_period(), Check if a player is currently in grace period. Args: player_id: The player's…, mock_app_with_services(), mock_connection_manager_full(), mock_persistence_full(), MockPersistenceFull, asyncio, fixture (+32 more)

### Community 230 - "logoutHandler.ts"
Cohesion: 0.11
Nodes (24): isGracePeriodServerUnavailableError(), hoisted, useMythosSessionChrome(), fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler, asRecordUnknown() (+16 more)

### Community 231 - "QuestInstanceRepository"
Cohesion: 0.11
Nodes (23): integration, Any, datetime, UUID, QuestInstanceRepository, Get the quest instance for this player and quest (any state). Returns None if…, Update an instance's state and/or progress. Pass only fields to change., List all active quest instances for the player. (+15 more)

### Community 232 - "collect_inventory.py"
Cohesion: 0.07
Nodes (44): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+36 more)

### Community 233 - "ChatModeration"
Cohesion: 0.04
Nodes (44): ChatModeration, normalize_player_id(), PlayerServiceProtocol, Any, datetime, Protocol, UUID, Chat moderation utilities. This module provides moderation functionality… (+36 more)

### Community 234 - "resolve_weapon_attack_from_equipped"
Cohesion: 0.09
Nodes (34): Pydantic models for item prototype validation. This module defines the…, _prototype_from_equipped_stack(), NamedTuple, Weapon resolution helpers for combat. Resolves equipped main-hand items to…, Result of resolving an equipped item to a weapon attack. base_damage: Rolled…, Resolve equipped main-hand stack to weapon attack info, or None if unarmed., resolve_weapon_attack_from_equipped(), _roll_weapon_attack() (+26 more)

### Community 235 - "EnvironmentalContainerLoader"
Cohesion: 0.12
Nodes (21): EnvironmentalContainerLoader, Any, ContainerComponent, ContainerLockState, UUID, migrate_room_container_to_postgresql., Load all environmental containers for a room from PostgreSQL. Args: room_id:…, Service for loading environmental containers from JSON and PostgreSQL. Handles… (+13 more)

### Community 236 - "mapPageRenderer.tsx"
Cohesion: 0.16
Nodes (17): MapPage, RoomMapViewerProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView(), renderMapPageState(), renderStatusGate() (+9 more)

### Community 237 - "test_chat_pose_helpers.py"
Cohesion: 0.16
Nodes (25): clear_player_pose(), get_player_pose(), get_room_poses(), normalize_player_id(), Any, UUID, Pose management helpers for chat service., Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose… (+17 more)

### Community 239 - "NPCCombatIntegrationBase"
Cohesion: 0.07
Nodes (24): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Apply combat effects to a target (player or NPC). Args: target_id: ID of the…, Convert target_id to UUID, accepting either string or UUID input., Apply combat effects to a player. (+16 more)

### Community 240 - "maps.py"
Cohesion: 0.05
Nodes (94): MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter…, _AsciiMapViewport, _build_ascii_map_response(), _build_ascii_minimap_response(), _CoordGenCtx, _ensure_coordinates_generated() (+86 more)

### Community 241 - "RoomDataValidator"
Cohesion: 0.07
Nodes (42): NPCCombatIntegrationValidationMixin, Validate that player and NPC are in the same room., Room checks, NPC resolution, UUID mapping, and XP mapping for combat…, Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Check if occupant count matches the actual occupants list length. Args:…, Validates room data structure and content. (+34 more)

### Community 242 - "apiTypeGuards.ts"
Cohesion: 0.12
Nodes (43): ApiErrorWithDetail, assertCharacterInfoArray(), assertRefreshTokenResponse(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString(), hasServerCharacterCoreFields(), hasServerCharacterIdentifierFields() (+35 more)

### Community 243 - "test_error_handling_middleware.py"
Cohesion: 0.09
Nodes (41): add_error_handling_middleware(), ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, FastAPI, Protocol, Error handling middleware for FastAPI integration. This module provides…, Add error handling middleware to FastAPI application. Args: app: FastAPI… (+33 more)

### Community 244 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.17
Nodes (17): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+9 more)

### Community 245 - "_find_container_in_room"
Cohesion: 0.07
Nodes (30): _find_container_in_room(), Find a container in room containers by name or container_id. Args: containers:…, Test _find_container_in_room() with instance number out of range., Test _find_container_in_room() with instance number zero., Test _find_container_in_room() finds container by name., Test _find_container_in_room() returns None when container not found., Test _find_container_in_room() with instance number., Test _find_container_in_room() with empty list. (+22 more)

### Community 246 - "LogAggregator"
Cohesion: 0.07
Nodes (43): LogEntry, aggregate_log_entry(), get_log_aggregator(), LogAggregator, LogEntry, LogQueryFilter, Any, Path (+35 more)

### Community 247 - "PlayerNameExtractor"
Cohesion: 0.02
Nodes (84): PlayerNameExtractor, Any, UUID, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:…, Perform basic validation on player name (not None, is string, not empty). Args:…, Utility class for extracting and validating player names. CRITICAL: NEVER uses… (+76 more)

### Community 248 - "TestErrorHandlers"
Cohesion: 0.10
Nodes (16): asyncio, Test error handler functions., Test mythos_exception_handler., Test mythos_exception_handler with debug enabled., Test mythos_exception_handler sets request_id in context., Test general_exception_handler., Test logged_http_exception_handler for 401., Test logged_http_exception_handler for 404. (+8 more)

### Community 249 - "GameMechanicsService"
Cohesion: 0.09
Nodes (27): GameMechanicsService, Any, Heal a player's health., Damage a player's health., Award experience points to a player. CRITICAL FIX: This method prevents XP…, Service class for game mechanics operations., Initialize the game mechanics service with a persistence layer., Apply lucidity loss to a player. (+19 more)

### Community 250 - "useDraggablePanelInteractions.ts"
Cohesion: 0.06
Nodes (51): DraggablePanel(), DraggablePanelProps, DraggablePanelResizeHandles(), DraggablePanelResizeHandlesProps, HANDLE_CONFIGS, HandleConfig, isMouseEventOnHeader(), isPanelDragBlockedTarget() (+43 more)

### Community 251 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 252 - "test_nats_messages.py"
Cohesion: 0.06
Nodes (51): Realtime domain schemas: realtime API, NATS messages, WebSocket messages., BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, field_validator, Pydantic schemas for NATS message validation. This module provides type-safe… (+43 more)

### Community 253 - "FastAPI Code Review - Anti-Patterns and Best Practices"
Cohesion: 0.05
Nodes (40): 10. ℹ️ **Dependency Injection Pattern**, 11. ℹ️ **API Versioning** (OPTIONAL - NOT REQUIRED FOR WEBAPP), 1. ✅ **Inconsistent Response Models** - **RESOLVED**, 1. Response Models (Critical Issue #1) ✅, 2. Dependency Injection (Critical Issue #3) ✅, 2. 🟡 **Fat Endpoints with Business Logic** - **IN PROGRESS**, 3. ✅ **Direct app.state Access Instead of Dependency Injection** - **RESOLVED**, 3. Error Handling (Medium Issue #7) ✅ (+32 more)

### Community 254 - "test_logout_commands.py"
Cohesion: 0.04
Nodes (103): _clear_corrupted_cache_entry(), _disconnect_player_connections(), _force_disconnect_player(), _get_app_services(), _get_player_for_logout(), _get_player_position_from_connection_manager(), handle_logout_command(), handle_quit_command() (+95 more)

### Community 255 - "test_player_occupant_processor.py"
Cohesion: 0.04
Nodes (49): mock_connection_manager(), mock_name_extractor(), processor(), asyncio, fixture, Unit tests for player occupant processor. Tests the PlayerOccupantProcessor…, Test _convert_player_ids_to_uuids handles mixed string and UUID types., Test _convert_player_ids_to_uuids handles UUID objects. (+41 more)

### Community 256 - "test_message_queue.py"
Cohesion: 0.03
Nodes (57): Unit tests for message queue. Tests the message_queue module classes and…, Test MessageQueue.get_messages() retrieves and clears messages., Test MessageQueue.get_messages() returns empty list for player with no messages., Test MessageQueue.get_messages() handles errors., Test MessageQueue.__init__() with default values., Test MessageQueue.has_messages() returns True when player has messages., Test MessageQueue.has_messages() returns False when player has no messages., Test MessageQueue.has_messages() returns False for empty list. (+49 more)

### Community 257 - "persistence/container_persistence.py"
Cohesion: 0.08
Nodes (66): _after_container_insert(), _allowed_roles_from_row(), _as_opt_datetime(), _as_opt_str(), _as_opt_uuid(), _as_uuid(), _coerce_item_quantity(), _container_data_from_row() (+58 more)

### Community 258 - "test_game_tick_processing_async.py"
Cohesion: 0.08
Nodes (40): process_combat_tick(), _process_damage_over_time_effect(), _process_heal_over_time_effect(), _process_single_effect(), Process a damage over time effect. Returns: True if effect was applied, False…, Process a heal over time effect. Returns: True if effect was applied, False…, Process a single status effect. Returns: Tuple of (updated_effect_dict or None…, Process combat auto-progression. (+32 more)

### Community 259 - "GameLogPanel.tsx"
Cohesion: 0.07
Nodes (40): GameTerminalPresentation(), GameTerminalPresentationProps, GameLogListMessage, GameLogMessagesList(), GameLogMessagesListProps, GameLogPanel(), GameLogPanelProps, GameLogPanelFilterBar() (+32 more)

### Community 260 - "NPCCombatIntegrationReadApi"
Cohesion: 0.08
Nodes (23): EventBusPublish, lifecycle_lookup_id(), NPCCombatIntegrationReadApi, NPCCombatRewardsLike, original_string_id_for_npc(), PersistenceWithNpcLifecycleManager, PlayerXpLike, Protocol (+15 more)

### Community 261 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 262 - "migration_examples.py"
Cohesion: 0.04
Nodes (46): database, Simulate database operations., Simulate database query., Simulate database execute., database, expensive_operation(), migration_example_1(), migration_example_10() (+38 more)

### Community 263 - "test_npc_admin_commands.py"
Cohesion: 0.03
Nodes (152): handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command., Handle NPC reaction trigger command., Handle NPC behavior stop command. (+144 more)

### Community 264 - "RoomMapEditorRuntime.tsx"
Cohesion: 0.06
Nodes (45): HistoryEntry, MapEditingChanges, useMapEditing(), UseMapEditingOptions, UseMapEditingResult, UseMapLayoutResult, UseRoomMapDataOptions, MapEditToolbar() (+37 more)

### Community 265 - "test_room_service.py"
Cohesion: 0.02
Nodes (109): mock_persistence(), mock_room_cache(), asyncio, fixture, Unit tests for room service. Tests the RoomService class for room-related…, Test get_room() returns None when room not found in persistence., Test get_room() handles dict from persistence., Test get_room_by_name() returns None (not implemented). (+101 more)

### Community 266 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 267 - "ChatChannelLoggerMixin"
Cohesion: 0.10
Nodes (19): ChatChannelLoggerMixin, Any, Path, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper…, Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs. (+11 more)

### Community 268 - "player.ts"
Cohesion: 0.11
Nodes (32): locationIndicatesDeathVoid(), requiredAliveButDeadMessage(), assertLookVisibleInPanels(), lookAndStand(), prepAwForAdminSet(), prepNonAdminForSetAttempt(), runAdminSetWithRecovery(), assertNpcSpawnVisible() (+24 more)

### Community 269 - "DialogueDefinitionRepository"
Cohesion: 0.19
Nodes (20): _definition_dict(), DialogueDefinitionRepository, Coerce JSONB definition cell to a plain string-keyed dict., Repository for dialogue_definitions via stored procedures., _mock_session_with_rows(), asyncio, fixture, Unit tests for DialogueDefinitionRepository. (+12 more)

### Community 270 - "NATSRetryHandler"
Cohesion: 0.02
Nodes (68): MessageFilteringHelper, Any, Extract information from chat event. Args: chat_event: Chat event dictionary…, Determine if mute check should be applied for a channel. Args: channel: Channel…, Compare two room IDs using canonical room ID resolution. Args: player_room_id:…, Get player's current room ID from online players cache. Args: player_id: Player…, Get player's current room ID from async persistence layer. Args: player_id:…, Helper class for message filtering operations. (+60 more)

### Community 271 - "_MagicServiceCore"
Cohesion: 0.08
Nodes (29): _MagicServiceCore, Any, UUID, Return (False, message) if not enough MP, else (True, '')., Return (False, message) if Mythos spell and not enough lucidity, else (True,…, Return (False, message) if player has not learned the spell, else (True, '')., Return (False, message) if spell requires materials and any are missing, else…, Check if a player can cast a spell. Args: player_id: Player ID spell: Spell to… (+21 more)

### Community 272 - "FeatureFlagService"
Cohesion: 0.03
Nodes (54): Initialize the combat configuration service., FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature… (+46 more)

### Community 273 - "test_memory_leak_metrics.py"
Cohesion: 0.05
Nodes (42): collector(), fixture, Unit tests for memory leak metrics collector. Tests the…, Test collection of cache metrics., Test collection of task metrics., Test collection of NATS metrics., Test collection of all metrics., Test calculation of growth rates. (+34 more)

### Community 274 - "alias_schema.json"
Cohesion: 0.04
Nodes (51): command, version, additionalProperties, additionalProperties, description, properties, required, type (+43 more)

### Community 275 - "Any"
Cohesion: 0.13
Nodes (12): Any, Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits…, Build exit lookup map from room data., Center viewport on the character's current room so the player is in the middle…, Render a single row of rooms with horizontal exits., Render an ASCII map as HTML. Args: rooms: List of room dictionaries with…, Return the horizontal exit character (—, >, or <) given east/west exit state,… (+4 more)

### Community 276 - "RoomIDUtils"
Cohesion: 0.07
Nodes (35): Any, Check if NPC room IDs match target room IDs using fallback comparison. Args:…, Check if NPC room matches target room using normalized comparison. Args:…, Utilities for room ID normalization and comparison., Initialize room ID utilities. Args: connection_manager: ConnectionManager…, Get canonical room ID for consistent comparison. Args: room_id: The room ID…, Normalize room ID for comparison. Args: rid: Room ID to normalize Returns:…, Check if two normalized room IDs match. Args: id1: First normalized room ID… (+27 more)

### Community 277 - "admin_shutdown_command.py"
Cohesion: 0.10
Nodes (39): _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state(), countdown_loop(), _create_countdown_task() (+31 more)

### Community 278 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 279 - "PerformanceMonitor"
Cohesion: 0.02
Nodes (101): auth_service(), BackgroundTasks, create_player(), File, general_exception_handler(), get_player(), http_exception_handler(), list_players() (+93 more)

### Community 280 - "verify_enhanced_logging_compliance.py"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 281 - "NPCCombatLucidity"
Cohesion: 0.06
Nodes (31): Return lucidity dependency for integration collaborators., _EncounterCtx, NPCCombatLucidity, Any, NamedTuple, Apply lucidity loss when a player engages an eldritch entity. Args: player_id:…, Determine encounter category based on NPC definition metadata. Args:…, Context for applying encounter lucidity loss. (+23 more)

### Community 282 - "GameClientV2ContainerView.tsx"
Cohesion: 0.06
Nodes (27): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, MapView(), MapViewBody() (+19 more)

### Community 283 - "ErrorMonitor"
Cohesion: 0.13
Nodes (17): ErrorMonitor, main(), Any, datetime, Path, Detect error trends over time. Returns trend analysis results., Check for alert conditions. Returns list of active alerts., Monitor errors continuously for a specified duration. Args: log_dir: Directory… (+9 more)

### Community 284 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 285 - "test_pattern_matcher.py"
Cohesion: 0.06
Nodes (36): pattern_matcher(), fixture, Unit tests for NATS Pattern Matcher. Tests the PatternMatcher class., Test _components_match_pattern() matches exact components., Test _components_match_pattern() matches placeholder components., Test _components_match_pattern() returns False for mismatch., Test _components_match_pattern() validates placeholder values., Test _components_match_pattern() disallows underscores in strict mode. (+28 more)

### Community 286 - "compare_linting_results.py"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 287 - "HealthService"
Cohesion: 0.08
Nodes (24): HealthStatus, HealthService, Any, Async database health check., check_database_health., Check connection manager health., Get server component health status., Get database component health status (async version with actual validation). (+16 more)

### Community 288 - ".__init__"
Cohesion: 0.20
Nodes (7): Check if the status effect is still active., Any, Initialize Invite with defaults., _npc_alive_and_active(), setter, Return True if NPC is alive (determination_points > 0)., Allow backward-compatible assignment (npc.is_alive = False).

### Community 289 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (49): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id. Args: room_drops: List of…, Unit tests for look item helper functions. Tests the helper functions in…, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items. (+41 more)

### Community 290 - "models/combat.py"
Cohesion: 0.03
Nodes (142): CombatParticipantType, Enum, Combat system models for in-memory state management. This module defines the…, Type of combat participant., add_damage_threat(), add_heal_threat(), _aggression_scale(), apply_stealth_wipe() (+134 more)

### Community 291 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 292 - "test_command_processing.py"
Cohesion: 0.12
Nodes (24): _dispatch_parsed_command(), _handle_validation_error(), _log_security_sensitive_command(), _parse_command_line_or_client_error(), CommandExecutionRequest, ValidationError, Log a security-sensitive command for auditing., Handle a validation error during command processing. (+16 more)

### Community 293 - "useRespawnHandlers.ts"
Cohesion: 0.13
Nodes (28): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), handleIntentionalDisconnect() (+20 more)

### Community 294 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 295 - "inventory_get_command.py"
Cohesion: 0.13
Nodes (34): _container_transfer_messages(), _get_from_container_path(), _get_route_after_validation(), _get_transfer_out_of_container(), GetCommandRuntime, GetItemSpec, handle_get_command(), _handle_get_from_room() (+26 more)

### Community 296 - ".move_to_room"
Cohesion: 0.25
Nodes (4): Return True if NPC is in combat (blocks movement); False on lookup failure., Move NPC using movement integration; return True if successful., Move NPC without integration (simple room update)., Move NPC to a room; blocked in combat. Return True if successful.

### Community 297 - "test_look_container_helpers.py"
Cohesion: 0.08
Nodes (28): asyncio, Unit tests for look container helper functions. Tests the helper functions in…, Test _find_container_via_inner_container() when item has no inner_container., Test _find_container_via_inner_container() with invalid UUID., Test _find_container_via_inner_container() when persistence has no…, Test _matches_item_instance_id() returns True when IDs match., Test _matches_item_instance_id() returns False when IDs don't match., Test _matches_item_instance_id() returns False when either ID is None. (+20 more)

### Community 298 - "Bug Investigator Subagent"
Cohesion: 0.07
Nodes (27): Authentication/Login Issues, Best Practices, Bug Investigator Subagent, Capabilities, Chat/Communication Issues, Critical Requirements, Evidence Collection, Evidence Standards (+19 more)

### Community 299 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 300 - "skills.py"
Cohesion: 0.10
Nodes (25): get_skills_catalog(), get, Request, Skills catalog API endpoints. GET /v1/skills returns the skills catalog for…, Return the skills catalog (base values, allow_at_creation). Cthulhu Mythos is…, Skill catalog API response schemas. Used by GET /v1/skills (or equivalent) for…, Single skill catalog entry., Response model for skills catalog list. (+17 more)

### Community 301 - "TargetResolutionResult"
Cohesion: 0.06
Nodes (63): _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), _load_follow_context(), Any, Follow commands for MythosMUD. Handlers for /follow, /unfollow, and /following.…, Handle /following - show who you follow and who follows you. (+55 more)

### Community 302 - "character-cleanup.ts"
Cohesion: 0.10
Nodes (25): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+17 more)

### Community 303 - "WebSocketRequestContext"
Cohesion: 0.07
Nodes (34): Any, Get the event bus from the request context., Get the alias storage from the request context., Creates FastAPI Request-like objects for WebSocket commands. This allows…, Initialize the WebSocket request context. Args: app_state: Real application…, Set the alias storage in the app state. Args: alias_storage: Alias storage…, Set the app state services in the request context. Note: This method is kept…, Get the persistence layer from the request context. (+26 more)

### Community 304 - "E2E Test Suite AI Execution Improvements - Summary"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 305 - "Async Persistence Migration Plan"
Cohesion: 0.05
Nodes (37): 1.1 Find all PersistenceLayer usage, 1.2 Document call sites, 2.1 Update ApplicationContainer, 2.2 Update lifespan.py, 2.3 Migrate API endpoints, 2.4 Migrate services, 2.5 Migrate commands, 2.6 Update test fixtures (+29 more)

### Community 306 - "_find_container_wearable"
Cohesion: 0.07
Nodes (28): _find_container_wearable(), Find a wearable container in equipped items by name or prototype_id. This…, Test _find_container_wearable() with empty dict., Test _find_container_wearable() with no matching containers., Test _find_container_wearable() with multiple matches (ambiguous)., Test _find_container_wearable() with instance number., Test _find_container_wearable() with instance number out of range., Test _find_container_wearable() finds wearable container. (+20 more)

### Community 307 - "TestMonitoringEndpoints"
Cohesion: 0.07
Nodes (22): asyncio, fixture, Test health check endpoint returns system health., Test health check endpoint handles errors., Test metrics endpoint returns monitoring data., Test metrics endpoint handles errors., Test monitoring summary endpoint returns summary data., Test lifespan() context manager. (+14 more)

### Community 308 - "TestCombatMessagingService"
Cohesion: 0.05
Nodes (34): CombatMessages, CombatMessagingService, Any, Generate combat start messages for all room occupants. Args: attacker_name:…, Generate combat end messages for all room occupants. Args: winner_name: Name of…, Generate thematic error messages for combat actions. Args: error_type: Type of…, Validate NPC message templates against the schema. Args: messages_data: NPC…, Service for generating combat messages. This service creates thematic,… (+26 more)

### Community 309 - "TestHierarchicalSchema"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 310 - "test_combat_cleanup_handler.py"
Cohesion: 0.08
Nodes (27): cleanup_handler(), mock_combat(), mock_combat_service(), asyncio, fixture, Unit tests for combat cleanup handler. Tests the CombatCleanupHandler class for…, Test cleanup_stale_combats handles missing end_combat method., Test cleanup_stale_combats when no stale combats exist. (+19 more)

### Community 312 - "Execution Steps"
Cohesion: 0.05
Nodes (36): BEFORE EXECUTING THIS SCENARIO, YOU MUST, BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, CONFIRMATION CHECKLIST, EXECUTION AFFIRMATION (Type this before proceeding), 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER, Execution Steps, Expected Results (+28 more)

### Community 313 - "look_container.py"
Cohesion: 0.13
Nodes (26): _extract_container_metadata(), _find_container_in_room_or_equipped(), _find_container_via_inner_container(), _find_container_via_wearable_service(), _get_container_data_from_component(), _get_container_description(), _handle_container_look(), _matches_item_instance_id() (+18 more)

### Community 314 - "test_combat_persistence_handler_persistence.py"
Cohesion: 0.07
Nodes (38): mock_combat_service(), mock_player(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - persistence operations. Tests…, Test _persist_player_dp_sync calls _verify_player_save., Test _persist_player_dp_sync handles save_player error. (+30 more)

### Community 315 - "get_async_session"
Cohesion: 0.05
Nodes (39): add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., main(), Load seed data and verify., normalize_database_url(), Set test override database URL. (+31 more)

### Community 316 - "HallucinationFrequencyService"
Cohesion: 0.08
Nodes (31): HallucinationFrequencyService, Any, AsyncSession, UUID, Check if hallucination should trigger on room entry (Uneasy tier). Args:…, Check if hallucination should trigger based on time (Fractured/Deranged tiers).…, Service for managing hallucination frequency checks based on player tier., Initialize the hallucination frequency service. (+23 more)

### Community 317 - "AliasGraph"
Cohesion: 0.09
Nodes (22): Unit tests for alias_graph utilities. Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+14 more)

### Community 318 - "_format_container_display"
Cohesion: 0.08
Nodes (26): _format_container_display(), Format the complete container display text., Test _format_container_display() with locked container., Test _format_container_display() with sealed container., Test _format_container_display() with look_in flag., Test _format_container_display() with target_type container., test_format_container_display_locked(), test_format_container_display_sealed() (+18 more)

### Community 319 - "ValidationError"
Cohesion: 0.02
Nodes (171): Data validation errors (e.g. empty local/whisper message). Log at warning, not…, ValidationError, Player state management service. This module handles player state modifications…, increment_exception(), Increment the count for a specific exception type. Args: exc_type: The…, Test remove_player_from_room validates empty player_id., test_remove_player_invalid_params(), Test ValidationError can be instantiated. (+163 more)

### Community 321 - "SchemaValidator"
Cohesion: 0.10
Nodes (18): create_validator(), Any, Path, Shared schema validator for room definition files. This module provides JSON…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a serialized alias bundle against the alias schema. Args: alias_data:…, Validate emote definition data against the emote schema. Args: emote_data:… (+10 more)

### Community 322 - "NATS Complete Remediation Summary"
Cohesion: 0.05
Nodes (36): 1. Error Handling Standardization, 2. Message Validation, 3. Batch Flush Error Recovery, 4. Connection Pool Error Handling, 5. Subject Manager Integration, 6. Health Monitoring, 7. Acknowledgment Metrics, 8. Wildcard Validation (+28 more)

### Community 323 - "PostgreSQL & SQL Audit Report"
Cohesion: 0.05
Nodes (36): 10. Prioritized Fixes, 11. Summary Table, 1.1. Snake_case (GOOD), 1.2. Quoted Identifier, 1. Naming Conventions, 2.1. Uppercase SQL Keywords, 2. SQL Formatting (Keywords Lowercase), 3.1. Explicit Joins (GOOD) (+28 more)

### Community 324 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 325 - "quest_chat_notify.py"
Cohesion: 0.13
Nodes (25): Schedule personal system chat from sync or async callers., schedule_personal_system(), _as_int(), _goal_is_met(), notify_quest_abandoned(), notify_quest_completed(), notify_quest_progress(), notify_quest_started() (+17 more)

### Community 326 - "chatPanelRefactoredDerived.ts"
Cohesion: 0.32
Nodes (11): ChatPanelRefactored(), ChatPanelRefactoredProps, computeChannelMessages(), computeFilteredMessages(), computeUnreadCounts(), filterNonSystemMessages(), isDisplayableChatMessage(), resolveMessageChannel() (+3 more)

### Community 327 - "Test Suite Analyzer Subagent"
Cohesion: 0.08
Nodes (23): Best Practices, Capabilities, Coverage Analysis, Coverage Gap Analysis, Coverage Requirements, Critical Files Requiring High Coverage, Critical Path Coverage, Example Scenarios (+15 more)

### Community 328 - "map_minimap.py"
Cohesion: 0.07
Nodes (41): _append_room_with_fallback_coords_if_needed(), _apply_minimap_fallback_coordinates(), _ensure_current_room_in_minimap_rooms(), generate_minimap_html(), Any, AsyncSession, UUID, Minimap orchestration for the map API. Extracted from maps.py so the router… (+33 more)

### Community 329 - "TestNPCCombatRewards"
Cohesion: 0.07
Nodes (21): asyncio, fixture, Unit tests for NPC combat rewards. Tests the NPCCombatRewards class for XP…, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class. (+13 more)

### Community 330 - "PlayerCombatService"
Cohesion: 0.03
Nodes (92): Get base stats as dictionary., Set the player combat service for the connection manager., Attach or replace the player combat service (shared instance wiring)., PlayerCombatService, PlayerCombatState, UUID, Attach NPC combat integration for UUID/XP mapping (post-construction wiring)., Track a player's combat state. Args: player_id: ID of the player player_name:… (+84 more)

### Community 331 - "Container System"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 332 - "test_websocket_handler_coverage_gaps.py"
Cohesion: 0.07
Nodes (44): handle_chat_message(), Handle a chat message from a player. Args: websocket: The WebSocket connection…, asyncio, Unit tests to fill coverage gaps in websocket_handler.py. These tests target…, Test handle_game_command exception handling path (lines 472-480)., Test handle_game_command RuntimeError handling path (lines 472-480)., Test process_websocket_command resolves connection_manager from app when None…, Test handle_chat_message resolves connection_manager from app when None (lines… (+36 more)

### Community 333 - "ZoneConfiguration"
Cohesion: 0.05
Nodes (53): Represents the configuration for a zone or sub-zone., Calculate effective spawn probability based on zone modifiers. Args:…, Check if a player can access this zone based on requirements. Args:…, ZoneConfiguration, Test get_zone_configuration() returns exact match., Test get_zone_configuration() falls back to zone-level config., Test get_zone_configuration() handles zone key without slash., Test _check_spawn_requirements_for_room() checks NPC definitions. (+45 more)

### Community 334 - "look_command.py"
Cohesion: 0.06
Nodes (56): _get_app_and_persistence(), _get_room_drops(), _handle_implicit_target_lookup(), handle_look_command(), Any, Look command for MythosMUD. This module handles the look command for examining…, Try to handle explicit player look., Try to handle explicit item look. (+48 more)

### Community 335 - "utils/layout.ts"
Cohesion: 0.10
Nodes (37): UseMapLayoutOptions, applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyGridLayout() (+29 more)

### Community 336 - "multiplayer-browser-helpers.js"
Cohesion: 0.15
Nodes (29): buttonHasLoginSubmitLabel(), captureGameUiDiagnosticsInBrowser(), captureOccupantsSnapshotInBrowser(), computedStyleHidesElement(), elementShowsConnectedStatus(), elementTextIncludesGameInfo(), evaluateGameUiLoaded(), fieldHasCommandPlaceholder() (+21 more)

### Community 337 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.06
Nodes (31): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI SUCCESS METRICS, 🔧 COMMON FIX TEMPLATES, Component Rendering Issues, 🔴 CRITICAL (Fix First - Blocking Issues), 🔴 CRITICAL FIXES - TypeScript Errors, For Each Failure Category (+23 more)

### Community 338 - "Structured Error Logging"
Cohesion: 0.50
Nodes (4): MythosMUDError Hierarchy, Structured Error Logging, log_and_raise Utilities, Test/Production Environment Separation

### Community 339 - "emotes.schema.json"
Cohesion: 0.06
Nodes (31): additionalProperties, additionalProperties, properties, required, type, items, type, uniqueItems (+23 more)

### Community 340 - "test_corpse_lifecycle_service.py"
Cohesion: 0.03
Nodes (88): CorpseLifecycleService, CorpseNotFoundError, CorpseServiceError, _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID (+80 more)

### Community 341 - "onboard/SKILL.md"
Cohesion: 0.08
Nodes (23): Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption, Guided Tours & Walkthroughs (+15 more)

### Community 342 - "test_optimized_security_validator.py"
Cohesion: 0.09
Nodes (31): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test validating message with path traversal pattern., Test validating message with javascript: URL., Test validating message with event handler. (+23 more)

### Community 343 - "message_handler_factory.py"
Cohesion: 0.14
Nodes (22): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, PartyInviteResponseMessageHandler, PingMessageHandler, ABC (+14 more)

### Community 344 - "generate_sql.mjs"
Cohesion: 0.25
Nodes (8): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Static Data SQL Generation, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 345 - "._build_player_attacked_event"
Cohesion: 0.11
Nodes (12): UUID, Resolve the player and UUID needed for DP update events., Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated., Publish the PlayerDPUpdated event to the event bus., Publish NPC-on-player attack as player_attacked to NATS so the client receives…, Resolve the combat event publisher used to send PlayerAttacked events to NATS., Resolve target UUID, player object, and stats needed for NATS attack event., Construct the PlayerAttackedEvent payload for NATS publication. (+4 more)

### Community 346 - "roomHandlers.ts"
Cohesion: 0.05
Nodes (56): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+48 more)

### Community 347 - "Enhanced Logging Migration Complete"
Cohesion: 0.67
Nodes (3): Enhanced Logging Implementation Complete, Enhanced Logging Implementation Summary, Enhanced Logging Migration Complete

### Community 350 - ".get_instance"
Cohesion: 0.04
Nodes (58): _ensure_room_cache_before_npc_startup(), Ensure room cache is loaded before NPC startup; raise in production if empty., get_container(), Get the singleton container instance., Reset the container singleton. ONLY use this in tests., Set the singleton container instance., Get the application container singleton. Backward compatibility., Reset the container singleton. ONLY use this in tests. (+50 more)

### Community 351 - "combat_attack.py"
Cohesion: 0.08
Nodes (39): _execute_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution. Extracted from combat.py to…, Resolve damage from equipped weapon or fall back to config unarmed damage., Execute combat action using the proper combat service., Handle attack commands (attack, punch, kick, etc.)., Validate target name, load player/room, check DP and no_combat. Returns… (+31 more)

### Community 353 - "test_command_alias.py"
Cohesion: 0.07
Nodes (38): AliasCommand, AliasesCommand, field_validator, Alias command models for MythosMUD. This module provides command models for…, Command for creating or viewing command aliases., Validate alias name format using centralized validation., Validate command content for security using centralized validation., Command for listing all aliases. (+30 more)

### Community 354 - "PlayerRepositoryProtocol"
Cohesion: 0.15
Nodes (14): PlayerRepositoryProtocol, Player, Protocol, Protocol for player persistence operations. Defines the contract used by…, Get the first active player for a user ID., Get all players (including deleted) for a user ID., Get active (non-deleted) players for a user ID., Get an active player by name (case-insensitive). (+6 more)

### Community 355 - "Test Pruning Candidates - Detailed List"
Cohesion: 0.06
Nodes (35): 1. Command Validation Tests, 2. Error Response Tests, 3. Permission Check Tests, Aggressive Estimate (Full Optimization), Category A: Infrastructure Tests Testing Framework Behavior, Category B: Coverage Tests Written for Metrics, Category C: Model Property Tests, Conclusion (+27 more)

### Community 356 - "handle_emote_command"
Cohesion: 0.14
Nodes (22): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+14 more)

### Community 357 - "CombatCommandHandler"
Cohesion: 0.03
Nodes (82): CombatCommandHandler, Any, AppWithState, Combat service for command modules., Movement service for command modules., Player position service for command modules., Extract command type and target name from command_data. Public API., Validate that target name is provided. Public API. (+74 more)

### Community 358 - "EventPublisher"
Cohesion: 0.04
Nodes (72): EventPublisher, Any, Publish a player_left event to NATS. Args: player_id: ID of the player who left…, Service for publishing real-time game events to NATS subjects. This service…, Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…, Initialize EventPublisher service. Args: nats_service: NATS service instance…, Create a standardized event message structure. Args: event_type: Type of event…, Get the next sequence number for event ordering. Returns: Next sequence number (+64 more)

### Community 359 - "Profession"
Cohesion: 0.05
Nodes (52): buildCreateCharacterPayload(), CharacterNameScreen(), CharacterNameScreenProps, CreateCharacterPayload, OccupationSlotPayload, PersonalInterestPayload, MechanicalEffect, Profession (+44 more)

### Community 360 - "RoomCacheLoader"
Cohesion: 0.20
Nodes (5): Any, BaseException, Loads room data from the database and populates a room cache dict. Used by…, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 361 - "test_goto_helpers.py"
Cohesion: 0.12
Nodes (43): execute_confirm_goto(), execute_goto_teleport(), log_goto_failure(), Any, Exception, Helper functions for goto command operations., Log failed goto action., Validate app context and get current player with admin permissions. Returns… (+35 more)

### Community 362 - "skills_commands.py"
Cohesion: 0.14
Nodes (22): _format_skills_output(), _get_container_services(), handle_skills_command(), Any, UUID, Skills command handler (plan 10.7 V4). Returns the active character's skills as…, Get container, persistence, and skill_service from request, or None if…, Extract and validate player_id from player object, returning UUID or None. (+14 more)

### Community 363 - "Performance Profiler Subagent"
Cohesion: 0.09
Nodes (22): Bottleneck Identification, Capabilities, Code Performance Review, Database Performance, Database Performance, Database Query Optimization, Enhanced Logging Integration, Example Scenarios (+14 more)

### Community 364 - "Three-Column Game UI Layout"
Cohesion: 0.29
Nodes (7): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe

### Community 365 - "DialogueEditorPage.tsx"
Cohesion: 0.09
Nodes (26): baseUrl(), buildHeaders(), deleteDialogueDefinition(), DialogueDefinitionDto, DialogueNodeDto, DialogueOptionDto, DialogueTreeDto, listDialogueDefinitions() (+18 more)

### Community 366 - "e2e-bootstrap.ts"
Cohesion: 0.14
Nodes (29): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+21 more)

### Community 367 - "GameTerminalContext.test.tsx"
Cohesion: 0.16
Nodes (17): GameTerminalContext, GameTerminalContextType, GameTerminalProvider(), GameTerminalProviderProps, useConnectionState(), useGameActions(), useGameState(), useGameTerminalContext() (+9 more)

### Community 368 - "utils/config.ts"
Cohesion: 0.09
Nodes (33): ConnectionHealthStats(), DualConnectionStats(), formatNumber(), formatPercentage(), formatTime(), loadMonitoringSnapshot(), MonitoringData, MonitoringPanel() (+25 more)

### Community 369 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 370 - "Coverage Improvement Summary - Plan 2 Execution"
Cohesion: 0.06
Nodes (34): 🏆 Achievement Highlights, API Endpoints (Tests Created, Pending Fresh Session), Auth (Tests Created, Pending Fresh Session), Caching (100% Complete), Challenges Encountered, Code Quality, Commands (Tests Created, Pending Fresh Session), ✅ COMPLETED & VERIFIED (6 modules) (+26 more)

### Community 371 - "test_postgres_adapter.py"
Cohesion: 0.14
Nodes (12): connect_postgres(), convert_sqlite_to_postgres_query(), Create a PostgreSQL connection. Args: database_url: PostgreSQL connection URL…, Convert legacy SQLite query syntax to PostgreSQL syntax. Note: This function is…, Unit tests for PostgreSQL adapter. Tests PostgresRow, PostgresConnection,…, Test utility functions., Test connect_postgres()., Test connect_postgres() with driver prefix. (+4 more)

### Community 372 - "Memory Leak Audit Report"
Cohesion: 0.06
Nodes (34): 1.1 Database Connection Pools, 1.2 WebSocket Connection Leaks, 1.3 NATS Connection and Subscription Leaks, 1. Connection Management Leaks, 2.1 EventBus Subscriber Leaks, 2.2 Client-Side Event Handler Leaks, 2. Event System Leaks, 3.1 Task Registry Leaks (+26 more)

### Community 373 - "test_audit_logger.py"
Cohesion: 0.07
Nodes (34): _logger(), Path, Unit tests for audit_logger utilities. Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries. (+26 more)

### Community 374 - "command_handler_unified.py"
Cohesion: 0.01
Nodes (205): check_alias_safety(), handle_expanded_command(), Any, CommandExecutionRequest, Handle command processing with alias expansion and loop detection. This…, Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:…, validate_expanded_command() (+197 more)

### Community 375 - "websocket_helpers.py"
Cohesion: 0.04
Nodes (68): Any, Convert alias to dictionary for JSON serialization., AsyncPersistenceRoomLookup, PlayerDisconnectService, Protocol, Notify subsystems when a WebSocket session ends for a player., Narrow persistence surface for loading ``Room`` by id in the WS handler., _AppStateForPlayerService (+60 more)

### Community 376 - "test_movement_monitor.py"
Cohesion: 0.03
Nodes (75): MovementMonitor, Any, UUID, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms., Get comprehensive movement metrics., Get current alerts based on thresholds. (+67 more)

### Community 377 - "command.py"
Cohesion: 0.02
Nodes (136): CommandType, Direction, StrEnum, Base command models and enums for MythosMUD. This module provides the…, Valid directions for movement and looking., Valid command types for MythosMUD., ChannelCommand, Channel management command models for MythosMUD. This module provides command… (+128 more)

### Community 378 - "test_shutdown_sequence.py"
Cohesion: 0.10
Nodes (48): Schedule a best-effort graceful process termination after a short delay. This…, schedule_process_termination(), _cancel_background_tasks(), _cleanup_connection_manager(), _despawn_all_npcs(), _disconnect_all_players(), _disconnect_nats_service(), execute_shutdown_sequence() (+40 more)

### Community 379 - "useRoomEditModal.ts"
Cohesion: 0.07
Nodes (19): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, fieldBorderClass(), RoomEditDescriptionField(), RoomEditFormData, RoomEditModalForm() (+11 more)

### Community 380 - "test_rate_limiter_utils.py"
Cohesion: 0.17
Nodes (11): Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…, Test get_rate_limit_info calculates reset time correctly., Test enforce_rate_limit raises RateLimitError when limit exceeded., Test RateLimiter initializes correctly., Test check_rate_limit allows first request., Test get_rate_limit_info returns correct info for no requests., test_check_rate_limit_first_request(), test_enforce_rate_limit_raises_when_exceeded() (+3 more)

### Community 381 - "Phase 3, Task 3.2: NATS Subject Manager Usage Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 382 - "MythosTickScheduler"
Cohesion: 0.11
Nodes (27): mock_chronicle(), mock_event_bus(), mock_task_registry(), asyncio, fixture, Unit tests for MythosTickScheduler., scheduler(), test_emit_pending_ticks_initializes_last_hour() (+19 more)

### Community 383 - "NATS Anti-Patterns and Best Practices Review"
Cohesion: 0.06
Nodes (33): 10. **Missing Connection Health Monitoring in Broker** (Observability), 1. **Excellent Error Boundary Implementation**, 1. **Synchronous Operations in Non-Handler Context** (Low Priority), 2. **Event Handler Callbacks May Block** (Anti-pattern), 2. **Good Connection State Management**, 3. **Inconsistent Error Handling Patterns** (Code Quality), 3. **Proper Async/Await Usage**, 4. **Missing Input Validation in Some Methods** (Security/Reliability) (+25 more)

### Community 384 - "test_connection_error_methods.py"
Cohesion: 0.10
Nodes (28): detect_and_handle_error_state_impl(), handle_authentication_error_impl(), handle_security_violation_impl(), handle_websocket_error_impl(), Any, UUID, Error-handling method implementations for ConnectionManager. Thin wrappers that…, Detect when a client is in an error state and handle it appropriately. (+20 more)

### Community 385 - "Spell"
Cohesion: 0.10
Nodes (30): Any, UUID, Learn a spell for a player., Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…, Service for handling spell learning from various sources. Manages spell…, Learn a spell from a spellbook item. Args: player_id: Player ID…, Learn a spell from an NPC teacher. Args: player_id: Player ID npc_id: ID of the…, Learn a spell as a quest reward. Args: player_id: Player ID quest_id: ID of the… (+22 more)

### Community 386 - "inventory_equip_command.py"
Cohesion: 0.12
Nodes (42): normalize_inventory_slots(), Normalize slot_type in inventory list in-place., _equip_build_work(), _equip_inventory_rollback_snapshot(), _equip_persist_or_rollback(), _equip_run_mutation(), _equip_success_payload(), _equip_target_slot_or_error() (+34 more)

### Community 387 - "Migration Strategy"
Cohesion: 0.08
Nodes (25): Access Patterns, App.State to Dependency Injection Migration Plan, Current State Analysis, Dependencies, Dependency Injection Pattern, Estimated Effort, Implementation Guidelines, Migration Strategy (+17 more)

### Community 388 - "ChatPoseManager"
Cohesion: 0.07
Nodes (17): ChatPoseManager, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…, Get a player's current pose. Args: player_id: ID of the player Returns: Current…, Clear a player's pose. Args: player_id: ID of the player Returns: True if pose…, Get all poses (for testing/debugging). Returns: Dictionary mapping player IDs… (+9 more)

### Community 389 - "test_container_query_helpers_async.py"
Cohesion: 0.17
Nodes (22): get_containers_by_entity_id_async(), get_containers_by_room_id_async(), get_decayed_containers_async(), _parse_jsonb(), Any, AsyncSession, ContainerData, datetime (+14 more)

### Community 390 - "devDependencies"
Cohesion: 0.05
Nodes (41): devDependencies, cross-env, esbuild, eslint-plugin-playwright, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, jsdom (+33 more)

### Community 391 - "TestCombatConfigurationService"
Cohesion: 0.05
Nodes (23): fixture, Test suite for CombatConfigurationService class., Create a mock config object., Create a CombatConfigurationService instance for testing., Test CombatConfigurationService initialization., Test get_combat_configuration returns configuration., Test get_combat_configuration caches configuration., Test get_combat_configuration_for_scope with global scope. (+15 more)

### Community 392 - "test_communication_commands_flows.py"
Cohesion: 0.03
Nodes (138): _chat_send_with_room_bundle(), _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_global_command(), flow_local_command(), flow_reply_command(), flow_say_command(), flow_system_command() (+130 more)

### Community 393 - "test_quest_service_collect.py"
Cohesion: 0.13
Nodes (27): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in… (+19 more)

### Community 394 - "retry.py"
Cohesion: 0.07
Nodes (42): asyncio, Unit tests for retry utilities. Tests the retry decorator and retry logic., Test retry_with_backoff() with async function succeeds on first attempt., Test is_transient_error() identifies transient errors., Test retry_with_backoff() with async function retries on failure then succeeds., Test is_transient_error() returns False for non-transient errors., DatabaseError wrapping asyncpg closed-connection must still retry (e2e…, __cause__ ConnectionDoesNotExistError makes the outer wrapper transient. (+34 more)

### Community 395 - "Any"
Cohesion: 0.09
Nodes (18): Any, Task, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task…, Cancel specific task with logical timeout boundaries. Args: task: Task…, Metadata for tracked asyncio.Tasks. (+10 more)

### Community 396 - "test_health_monitor.py"
Cohesion: 0.07
Nodes (35): health_monitor(), mock_cleanup_dead_websocket(), mock_is_websocket_open(), mock_performance_tracker(), mock_validate_token(), asyncio, fixture, Unit tests for health monitor. Tests the HealthMonitor class. (+27 more)

### Community 397 - "Persistence Layer Refactoring - COMPLETE ✅"
Cohesion: 0.06
Nodes (33): 1. Modular Architecture, 2. Async Foundation, 3. Zero Breaking Changes, 4. Comprehensive Documentation, 5. Quality Maintained, Backward Compatibility, 📈 Benefits, Code Created (+25 more)

### Community 398 - "Player"
Cohesion: 0.00
Nodes (796): AsyncPersistenceLayer, get_async_persistence(), Any, datetime, Player, Profession, UUID, Set the instance manager for instanced room lookup (instance-first). (+788 more)

### Community 399 - "emote_schema.json"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 401 - "Persistence Layer Refactoring Summary"
Cohesion: 0.06
Nodes (33): 1. PlayerRepository (439 lines), 2. RoomRepository (42 lines), 3. ProfessionRepository (74 lines), 4. HealthRepository (165 lines), 5. ExperienceRepository (203 lines), 6. ContainerRepository (80 lines), 7. ItemRepository (84 lines), Async Repository Structure (+25 more)

### Community 402 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 404 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 405 - "StyleGuideSections.tsx"
Cohesion: 0.05
Nodes (59): animations, borderRadius, breakpoints, buildClasses, ButtonVariant, colors, ColorVariant, ComponentSize (+51 more)

### Community 406 - "ConnectionCleaner"
Cohesion: 0.15
Nodes (13): ConnectionCleaner, Any, Return connection IDs that exceed max_connection_age., Extract player_id from connection metadata if present., Close stale WebSocket and remove from tracking. Handles None websocket…, Clean up orphaned data that might accumulate over time. Args:…, Return set of online player IDs as strings (room._players uses string UUIDs)., Return players in room but not online. Empty if room has no get_players. (+5 more)

### Community 407 - "ValidationRule"
Cohesion: 0.09
Nodes (15): ABC, Base validation rule class. This module defines the abstract base class for all…, Create a validation error for this rule. Args: room_id: Room ID where error…, Represents a validation error with metadata. As documented in the restricted…, Create a validation warning for this rule. Args: room_id: Room ID where warning…, Get information about this rule. Returns: Dictionary with rule information, Initialize a validation error. Args: rule_name: Name of the rule that generated…, Convert error to dictionary format. (+7 more)

### Community 408 - "test_player_preferences_service.py"
Cohesion: 0.03
Nodes (102): asyncio, Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID., Test creating player preferences when they already exist., Test creating player preferences with invalid ID., Test creating player preferences with integrity error. (+94 more)

### Community 409 - "npc_database.py"
Cohesion: 0.03
Nodes (88): _execute_spawn_loop(), _normalize_spawn_room_id(), _parse_npc_spawn_args(), _parse_npc_spawn_name(), _parse_npc_spawn_numeric(), NPC instance management commands (spawn, despawn, move, stats)., Run the spawn loop and return result message or error., npc' means current location; return None to resolve from player. (+80 more)

### Community 410 - "stateNormalization.ts"
Cohesion: 0.16
Nodes (18): createEntityMap(), denormalizeGameData(), Entity, EntityMap, extractEntities(), GameData, getEntitiesByIds(), getEntitiesByType() (+10 more)

### Community 411 - "start_grace_period"
Cohesion: 0.09
Nodes (33): cancel_grace_period(), Any, UUID, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, Start a grace period for a disconnected player. During the grace period, the…, start_grace_period(), mock_manager(), asyncio (+25 more)

### Community 412 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 413 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 414 - "rescue_service.py"
Cohesion: 0.16
Nodes (18): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+10 more)

### Community 415 - "Security Auditor Subagent"
Cohesion: 0.09
Nodes (21): Authentication & Authorization, Authentication Security Review, Capabilities, COPPA Compliance, COPPA Compliance (Critical), COPPA Compliance Verification, Example Scenarios, Input Validation (+13 more)

### Community 416 - "NATSConnectionStateMachine"
Cohesion: 0.02
Nodes (96): ConnectionEvent, NATSConnectionStateMachine, Any, Enum, Exception, Connection state machine for NATS messaging. Implements a robust state machine…, Initialize connection state machine. Args: connection_id: Unique identifier for…, Called whenever state machine enters a new state. Logs state transitions for… (+88 more)

### Community 417 - "real_time.py"
Cohesion: 0.06
Nodes (66): _ensure_connection_manager(), _extract_bearer_token(), get_connection_statistics(), get_player_connections(), handle_new_game_session(), _parse_subprotocol_token(), _parse_websocket_token(), Any (+58 more)

### Community 418 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 419 - "handle_teach_command"
Cohesion: 0.18
Nodes (22): _format_teach_result(), _get_teach_services(), handle_teach_command(), Any, Teach command handler for learning spells from NPC teachers. This module…, Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, _resolve_npc_teacher(), asyncio (+14 more)

### Community 420 - "test_who_commands.py"
Cohesion: 0.03
Nodes (110): Utility commands for MythosMUD. This module contains handlers for utility…, filter_online_players(), filter_players_by_name(), format_player_entry(), format_player_location(), format_who_result(), get_players_for_who(), handle_who_command() (+102 more)

### Community 421 - "register_default_reactions_for_npc"
Cohesion: 0.05
Nodes (40): Get attribute from obj with default to avoid lazy-loading issues., Set npc_type, name, current_room, spawn_room_id from definition., Setup base behavior rules common to all NPCs., Return stats[key] as int, or default if missing/None., Return current_dp, max_dp, dexterity for CombatParticipantData., Heal and update determination points (DP)., Write new_dp to determination_points and dp for backward compatibility., Initialize the NPC base class. (+32 more)

### Community 422 - "Advanced Chat Channels Specification"
Cohesion: 0.40
Nodes (5): Advanced Chat Channels Specification, Global Chat Channel, Local Chat Channel, Advanced Chat Channels Tasks, Whisper Chat Channel

### Community 423 - "test_chat_logger.py"
Cohesion: 0.05
Nodes (35): Initialize the rate limiter with configuration-based limits., chat_logger(), fixture, Unit tests for chat logger service. Tests the ChatLogger class for structured…, Test log_player_muted writes entry., Test log_player_unmuted writes entry., Test log_player_joined_room writes entry., Test log_rate_limit_violation writes entry. (+27 more)

### Community 424 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 425 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 426 - "testing_examples.py"
Cohesion: 0.04
Nodes (51): async_operation(), client, database, LoggingMiddleware, process_batch(), process_item(), asyncio, Test WebSocket logging in integration tests. (+43 more)

### Community 427 - "compilerOptions"
Cohesion: 0.09
Nodes (22): compilerOptions, baseUrl, lib, module, moduleResolution, noEmit, noFallthroughCasesInSwitch, noUnusedLocals (+14 more)

### Community 428 - "Authoritative Environment DML"
Cohesion: 0.18
Nodes (12): Authoritative Environment DML, Spells Seed Data (Deprecated), static_seed.sql (Deprecated), Generated World and Emotes SQL, DB Bootstrap Execution Order, Authoritative Environment DML, Removed Schema and Migration SQL, Legacy Schema Files Removed (+4 more)

### Community 430 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 431 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 432 - "Async Audit Executive Summary"
Cohesion: 0.06
Nodes (31): Alternative Approaches Considered, Async Audit Executive Summary, Benefit, Break-Even, Contact, Cost, Cost-Benefit Analysis, Critical Findings (+23 more)

### Community 433 - "inventory_commands.py"
Cohesion: 0.07
Nodes (49): Inventory and equipment command handlers for MythosMUD. Heavy handlers live in…, build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any (+41 more)

### Community 434 - "Critical Coverage Gaps"
Cohesion: 0.06
Nodes (32): Critical Coverage Gaps, Gap 10: Configuration Edge Cases, Gap 1: Domain Layer (NEW ARCHITECTURE), Gap 2: Message Broker Abstraction, Gap 3: ApplicationContainer Lifecycle, Gap 4: Error Recovery Paths, Gap 5: Async/Await Pattern Verification, Gap 6: Rate Limiting and Throttling (+24 more)

### Community 435 - "Communities (19 total, 4 thin omitted)"
Cohesion: 0.07
Nodes (26): Ambiguous Edges - Review These, Communities (19 total, 4 thin omitted), Community 0 - "Yog-Sothoth Keeper Decks", Community 10 - "Tsathoggua Formless Spawn", Community 11 - "Ygolonac and Xiclotl", Community 12 - "Nyogtha Spawn", Community 13 - "Hastur Spawn", Community 14 - "Fthagghua Fire Vampires" (+18 more)

### Community 436 - "projectorRoom.ts"
Cohesion: 0.10
Nodes (41): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), messageHandlers, ProjectorHandler, stateHandlers, appendMessage() (+33 more)

### Community 437 - "security.ts"
Cohesion: 0.04
Nodes (47): SafeHtml(), SafeHtmlProps, AsciiMinimap(), AsciiMinimapProps, deriveEffectiveLocation(), MinimapDisplayProps, POSITION_CLASSES, useAsciiMinimapData() (+39 more)

### Community 438 - "generate_html_visualization.py"
Cohesion: 0.13
Nodes (22): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+14 more)

### Community 439 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 440 - "combat_service_npc.py"
Cohesion: 0.05
Nodes (62): DataProviderProtocol, _fallback_find_combat_id_for_npc(), find_participant_uuid_by_string_id(), get_combat_by_participant(), get_combat_id_for_npc(), get_combat_id_for_npc_via_mapping(), _get_data_provider(), get_npc_participant_current_room() (+54 more)

### Community 441 - "channel_broadcasting_strategies.py"
Cohesion: 0.19
Nodes (12): ChannelBroadcastingStrategy, GlobalChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for whisper channel broadcasting., Abstract base class for channel broadcasting strategies., Initialize the strategy factory., Strategy for room-based channels (say, local, emote, pose). (+4 more)

### Community 443 - "PlayerService"
Cohesion: 0.03
Nodes (133): create_player(), delete_character(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), _force_disconnect_character(), get_available_classes(), get_class_description() (+125 more)

### Community 444 - "test_flee_command.py"
Cohesion: 0.09
Nodes (38): flee_handler_deps(), _FleeCmdApp, _FleeCmdAppState, _FleeCmdRequest, FleeHandlerDeps, _GetCombatHandlerLoaderApp, _GetCombatHandlerLoaderAppState, _GetCombatHandlerLoaderContainer (+30 more)

### Community 445 - "PARALLEL EXECUTION RESULTS (2025-11-05)"
Cohesion: 0.06
Nodes (31): 1. **Mark Additional Slow Tests**, 2. **Investigate Heavy Setup Tests**, 3. **Verify Marker Application**, 4. **Target Time Budget (5-7 min = 300-420 seconds)**, After Parallelization, Argon2 Password Tests (1.4+ seconds), Auth & Security Tests (21+ seconds setup each), Before Parallelization (+23 more)

### Community 447 - "test_user_manager.py"
Cohesion: 0.02
Nodes (97): Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() successfully globally mutes a player., Test mute_global() fails when trying to mute admin. (+89 more)

### Community 448 - "RoomEventHandler"
Cohesion: 0.12
Nodes (22): Any, UUID, Handle PlayerEnteredRoom events by broadcasting updated occupant count., Handle PlayerLeftRoom events by broadcasting updated occupant count., Handles room movement events and broadcasts occupant updates. This class…, Initialize the room event handler. Args: room_manager: RoomSubscriptionManager…, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events. (+14 more)

### Community 449 - "websocket_handler.py"
Cohesion: 0.03
Nodes (100): is_shutdown_pending(), Check if server shutdown is currently pending. Args: app: FastAPI application…, get_message_validator(), Get the global message validator instance., cleanup_websocket_connection(), UUID, WebSocket, Send welcome event to the client. Returns: True if successful, False if… (+92 more)

### Community 450 - "SkillAssignmentScreen.tsx"
Cohesion: 0.21
Nodes (18): SkillsPayload, loadSkillsCatalog(), MIN_TOUCH_TARGET_STYLE, OCCUPATION_VALUES, renderErrorState(), renderLoadingState(), renderOccupationSlots(), renderPersonalInterestSlots() (+10 more)

### Community 451 - "multiplayer-colocated.ts"
Cohesion: 0.17
Nodes (17): forceLogoutPlayer(), assertNoRestDisconnectPollution(), assertNotStuckOnLogin(), executeCommandTrusted(), logoutPlayer(), EnsureMultiplayerCoLocatedOptions, ensureMultiplayerReadyForCoLocate(), ensurePlayersInSameRoom() (+9 more)

### Community 452 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 453 - "Complexity Checking Alignment: Ruff C901 vs Pylint"
Cohesion: 0.06
Nodes (30): 1. Use Ruff for Cyclomatic Complexity ✅, 2. Suppress Pylint Complexity Metrics ✅, 3. Align Inline Suppressions, Complexity Checking Alignment: Ruff C901 vs Pylint, Conclusion, Configuration, Configuration, Current State Analysis (+22 more)

### Community 454 - "Stop-MythosMudProjectProcessTree"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 455 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 456 - "The Toolkit"
Cohesion: 0.09
Nodes (21): Animate complex properties, Assess What "Extraordinary" Means Here, For data-heavy interfaces, For functional UI, For performance-critical UI, For visual/marketing surfaces, Implement with Discipline, Interact with the device (+13 more)

### Community 457 - "test_npc_service.py"
Cohesion: 0.01
Nodes (227): _JSONDict, Base, _loads_json_dict(), NPCRelationship, NPCSpawnRule, DeclarativeBase, Set base stats from dictionary., Get behavior configuration as dictionary. (+219 more)

### Community 458 - "Dependency Upgrade Strategy Agent"
Cohesion: 0.22
Nodes (10): Batch Update Strategy, Breaking Change Detection, Dependency Compatibility Matrix, Dependency Update Analysis, Incremental Upgrade Strategy, Dependency Rollback Strategy, Dependency Upgrade Strategy Agent, Dependency Upgrade Report (+2 more)

### Community 459 - "useThemeContext.ts"
Cohesion: 0.22
Nodes (17): useAccessibilityPreference(), useAnimationPreference(), useColorSchemePreference(), useCompactModePreference(), useDebugInfoPreference(), useFontSizePreference(), useTheme(), useThemePreference() (+9 more)

### Community 460 - "multiplayer-browser-helpers.bundle.js"
Cohesion: 0.20
Nodes (17): buttonHasLoginSubmitLabel(), computedStyleHidesElement(), elementTextIncludesGameInfo(), fieldHasCommandPlaceholder(), getBodyInnerText(), hasCommandInputInBrowser(), hasGameInfoAnyMessageInBrowser(), hasGameInfoPanelInBrowser() (+9 more)

### Community 461 - "codacy.yaml Tool Manifest"
Cohesion: 0.33
Nodes (6): codacy.yaml Tool Manifest, Lizard Complexity Tool Pin, Trivy Codacy Tool Pin, MythosMUD Codacy Tool Suite, Grype Local vs Trivy Codacy SCA, Manually Managed codacy.yaml

### Community 462 - "Pydantic Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.06
Nodes (30): ⚠️ Areas for Improvement, 🟡 Business Logic in Models - Stats.**init**, Code Quality Observations, Conclusion, Critical Issues, 🔴 CRITICAL: Security Vulnerability - `extra="allow"` in Stats Model, Executive Summary, 🟢 Field Validator Organization (+22 more)

### Community 463 - "GameTerminal.tsx"
Cohesion: 0.04
Nodes (56): buildHealthStatus(), ChatMessage, formatPosture(), GameTerminal(), Player, Room, IncapacitatedBanner, IncapacitatedBannerProps (+48 more)

### Community 464 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (128): asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not…, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes. (+120 more)

### Community 465 - "validate.py"
Cohesion: 0.10
Nodes (30): BugBlock, check_bug_content(), _check_bugs(), check_loose_tags(), _check_required_structure(), _exit_code_for_errors(), find_bug_blocks(), find_first_content_section() (+22 more)

### Community 466 - "get_admin_auth_service"
Cohesion: 0.05
Nodes (85): create_dialogue_definition(), delete_dialogue_definition(), get_dialogue_definition(), list_dialogue_definitions(), delete, get, post, put (+77 more)

### Community 467 - "MemoryThresholdMonitor"
Cohesion: 0.10
Nodes (34): create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryThresholdMonitor, Create an instance of the MemoryThresholdMonitor with user-specified…, Factory function returning implementation conforming to Task 4.3 Specified…, Runtime monitor for detecting memory threshold violations requiring cleanup.…, asyncio, Unit tests for memory threshold monitoring and managed task cleanup. (+26 more)

### Community 468 - "ui-v2/types.ts"
Cohesion: 0.04
Nodes (106): GameTerminalProps, formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, eventHandlers, processGameEvent(), hoisted (+98 more)

### Community 469 - "TestVerificationSqlUsersPlayers"
Cohesion: 0.10
Nodes (12): PostgreSQL-focused tests for verification and maintenance SQL scripts.…, Tests for db/verification/users_players.sql alignment with current schema., Verification SQL file must exist., Verification SQL must not reference staging tables or select obsolete columns., Verification SQL must use explicit join syntax for multi-table queries., Verification SQL must reference users and players tables., Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)., NPC name constraint script must exist. (+4 more)

### Community 470 - "MythosPanel.tsx"
Cohesion: 0.10
Nodes (27): appendCommands(), CommandCategories(), CommandPanelTest(), COMMAND_CATEGORIES, DEFAULT_COMMAND_HISTORY, EXAMPLES, FEATURES, MOVEMENT_COMMANDS (+19 more)

### Community 471 - "RoomInfoPanel.tsx"
Cohesion: 0.13
Nodes (16): applyRoomDefaultFields(), DEV_FALLBACK_ROOM, fixOccupantCountMismatch(), formatDescription(), formatExitDirections(), formatLocationName(), KNOWN_LOCATION_PATTERNS, logRoomInfoRenderDebug() (+8 more)

### Community 472 - "test_nats_retry_handler.py"
Cohesion: 0.09
Nodes (21): Unit tests for NATS retry handler. Tests the NATSRetryHandler class and related…, Test get_retry_stats() returns correct statistics., Test update_config() updates valid field., Test update_config() updates multiple fields., Test update_config() ignores invalid field., Test NATSRetryHandler initialization., Test NATSRetryHandler default values., Test calculate_backoff() with base attempt. (+13 more)

### Community 473 - "Scenario 20 Logout Errors"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 474 - "test_magic_service.py"
Cohesion: 0.06
Nodes (63): CastingState, CastingStateManager, Any, UUID, Casting state manager for tracking active spell castings. This module manages…, Check if a player is currently casting. Args: player_id: Player ID to check…, Get the casting state for a player. Args: player_id: Player ID Returns:…, Complete and remove a casting state. Args: player_id: Player ID Returns:… (+55 more)

### Community 475 - "MessageBroadcaster"
Cohesion: 0.10
Nodes (22): SendPersonalMessage, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Convert string player IDs to UUIDs for message sending. Args: target_list: List…, Process results from batch message delivery. Args: delivery_results: Results…, Fallback to individual message sending if batch fails. Args: target_mapping:… (+14 more)

### Community 476 - "container_helpers_inventory_display.py"
Cohesion: 0.12
Nodes (28): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+20 more)

### Community 477 - "quest_commands.py"
Cohesion: 0.04
Nodes (87): ExitStack, _active_npc_ids_in_room(), _emit_npc_lines_for_results(), _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence() (+79 more)

### Community 478 - "static_data/package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 479 - "admin_teleport_commands.py"
Cohesion: 0.03
Nodes (112): Admin teleport command handlers for MythosMUD. This module provides handlers…, broadcast_teleport_effects(), create_teleport_effect_message(), get_online_player_by_display_name(), notify_player_of_teleport(), Any, Teleport utility functions for admin commands in MythosMUD. This module…, Notify a player that they are being teleported by an admin. Args:… (+104 more)

### Community 480 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.12
Nodes (16): 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases, For Performance (+8 more)

### Community 481 - "ADR-012: python-statemachine for Backend Connection FSM"
Cohesion: 0.09
Nodes (21): 10. Related ADRs, 11. Changelog, 1. Overview, 2. Context and Problem Statement, 3. Decision Drivers, 4. Considered Options, 5. Decision Outcome, 6. Implementation Details (+13 more)

### Community 482 - "compilerOptions"
Cohesion: 0.04
Nodes (48): compilerOptions, allowImportingTsExtensions, baseUrl, isolatedModules, jsx, lib, module, moduleResolution (+40 more)

### Community 483 - "enum"
Cohesion: 0.11
Nodes (19): ACCESSORY, AMULET, BELT, CURSED, FEET, GLOW, HANDS, HEAD (+11 more)

### Community 485 - "properties"
Cohesion: 0.11
Nodes (19): integer, minimum, type, minimum, type, null, maxLength, minLength (+11 more)

### Community 486 - "EdgeDetailsPanel.tsx"
Cohesion: 0.11
Nodes (15): buildEdgeFieldModel(), EdgeAdminActionsProps, EdgeDeleteConfirmProps, EdgeDetailRow(), EdgeDetailRowProps, EdgeDetailsFields(), EdgeDetailsFieldsProps, EdgeDetailsPanel() (+7 more)

### Community 487 - "Main Foyer Starting Room"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 488 - "gameStore.ts"
Cohesion: 0.05
Nodes (58): GameTerminalContainer(), createDefaultGameTerminalState(), useGameTerminalMock, applyTestCommandHistoryCap(), CHANNEL_TYPE_MAP, ChatMessageLike, GameTerminalState, mockCommandState (+50 more)

### Community 489 - "HealthRepository"
Cohesion: 0.08
Nodes (35): HealthRepository, Exception, Player, UUID, Log critical damage persistence failure., Execute atomic health update via update_player_health procedure., Damage a player and persist health changes atomically. Args: player: Player to…, Heal a player and persist health changes atomically. (+27 more)

### Community 490 - "PostgresConnection"
Cohesion: 0.08
Nodes (18): PostgresConnection, connection, Commit the current transaction., Rollback the current transaction., Close the connection., PostgreSQL connection wrapper for persistence layer operations., Test PostgresConnection initialization., Test PostgresConnection.execute(). (+10 more)

### Community 491 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, minLength, type, type, minLength, type, properties (+10 more)

### Community 492 - "DatabaseError"
Cohesion: 0.01
Nodes (453): get_10_active_invites(), main(), Get 10 active invite codes from the database., F, get_npc_data_from_source(), get_npc_database_url(), main(), populate_database() (+445 more)

### Community 493 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 494 - "Prometheus Configuration"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 495 - "EmoteService"
Cohesion: 0.07
Nodes (28): EmoteDefinition, _EmoteLoadResult, _EmoteRowData, EmoteService, _get_emote_validator(), TypedDict, Async helper to load emotes from PostgreSQL database., Check if a command is an emote alias. Args: command: The command to check… (+20 more)

### Community 496 - "test_room_occupant_manager.py"
Cohesion: 0.09
Nodes (29): mock_connection_manager(), occupant_manager(), asyncio, fixture, Unit tests for room occupant manager. Tests the RoomOccupantManager class for…, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test get_room_occupants handles get_players error. (+21 more)

### Community 497 - "test_message_broadcaster.py"
Cohesion: 0.07
Nodes (41): message_broadcaster(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for message broadcaster. Tests the MessageBroadcaster class., Test broadcast_global() excludes specified player., Test broadcast_global() when no players online. (+33 more)

### Community 498 - "load_world_seed.py"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 499 - "edgeModalLogic.ts"
Cohesion: 0.09
Nodes (30): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+22 more)

### Community 500 - "ReactNodeUpgradeAnalyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 501 - "test_combat_flee_helpers.py"
Cohesion: 0.05
Nodes (62): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules. Keeps…, Application object with a ``state`` namespace (dynamic attributes)., _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id() (+54 more)

### Community 503 - "useWebSocketConnection.ts"
Cohesion: 0.17
Nodes (12): ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach(), wsConnectionBeforeEach() (+4 more)

### Community 504 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 505 - "validate_room_data"
Cohesion: 0.15
Nodes (14): patch, Test validate_room_data() function., Test validate_room_data() returns empty list when validation not available., Test validate_room_data() with provided validator., Test validate_room_data() creates validator when not provided., Test validate_room_data() returns validation errors., Test validate_room_data() raises exception in strict mode with errors., Test validate_room_data() returns empty list when validator creation fails. (+6 more)

### Community 506 - "Multiplayer Architecture Planning"
Cohesion: 0.25
Nodes (8): Performance Optimization Summary, Alias System Implementation Plan, Chat System Implementation Plan, Planning Completion Summary, Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 507 - "test_combat_death_handler.py"
Cohesion: 0.13
Nodes (22): combat(), combat_service(), handler(), npc_target(), player_target(), asyncio, fixture, patch (+14 more)

### Community 508 - "room_validator/tests/conftest.py"
Cohesion: 0.15
Nodes (18): dead_end_room(), invalid_room_data(), fixture, Pytest configuration and fixtures for room validator tests. Provides test data…, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit. (+10 more)

### Community 509 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.11
Nodes (19): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases (+11 more)

### Community 510 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 511 - "AnyIO vs Asyncio: High-Level Comparison and Decision Guide"
Cohesion: 0.07
Nodes (29): 1. **Structured Concurrency**, 2. **Backend Abstraction**, 3. **API Design Philosophy**, Adjusts spectacles and peers at the codebase, anyio Cons ❌, anyio Pros ✅, `anyio` (Third-Party Library), AnyIO vs Asyncio: High-Level Comparison and Decision Guide (+21 more)

### Community 512 - "ADR-003 Dual Event Systems EventBus NATS"
Cohesion: 0.13
Nodes (17): FastAPI-Generated OpenAPI 3.1, API OpenAPI Specification, ADR-001 Layered Architecture Event-Driven, ADR-002 ApplicationContainer DI, ADR-003 Dual Event Systems EventBus NATS, In-Process EventBus, NATS Distributed Messaging, ADR-004 WebSocket-Only Realtime (+9 more)

### Community 513 - "MovementService"
Cohesion: 0.06
Nodes (32): MovementService, Any, Exception, Room, UUID, Validate movement parameters. Returns False if validation fails (same room),…, Resolve player by ID or name and return player object and resolved ID., Get and validate rooms for movement. (+24 more)

### Community 514 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 516 - "test_admin_shutdown_command.py"
Cohesion: 0.06
Nodes (50): _asyncio_mark, _AppWithoutState, _await_shutdown_result(), _InitiateAppStub, _InitiateStateStub, Unit tests for admin shutdown command handler. Tests the shutdown command…, Test handle_shutdown_command() when player service is not available., Test handle_shutdown_command() when player is not found. (+42 more)

### Community 517 - "test_room_subscription_manager_npcs.py"
Cohesion: 0.09
Nodes (23): asyncio, fixture, Unit tests for room subscription manager NPC helpers. Tests NPC-related helpers…, Test get_room_occupants() includes NPCs from lifecycle manager., Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager…, Create a RoomSubscriptionManager instance., Test _get_npc_name_from_lifecycle_manager gets NPC name., Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found. (+15 more)

### Community 518 - "test_security_headers.py"
Cohesion: 0.05
Nodes (49): MutableHeaders, Any, ASGIApp, Receive, Request, Scope, Send, Backward-compatible dispatch method for BaseHTTPMiddleware interface. This… (+41 more)

### Community 520 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 521 - "Any"
Cohesion: 0.10
Nodes (11): Any, Get room data with caching. Args: room_id: The room ID Returns: Room data…, Get room data with caching (synchronous version). Args: room_id: The room ID…, Initialize the NPC cache service. Args: npc_service: NPC service instance, Get NPC definitions with caching. Args: session: Database session Returns: List…, Get a specific NPC definition with caching. Args: session: Database session…, Get NPC spawn rules with caching. Args: session: Database session Returns: List…, Initialize the profession cache service. Args: persistence: Persistence layer… (+3 more)

### Community 522 - "Phase 1: Core Separation"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 1: Core Separation, Sub-tasks, Sub-tasks (+8 more)

### Community 523 - "Disconnect Grace Period and Rest Command"
Cohesion: 0.29
Nodes (7): Disconnect Grace Period and Rest Command, Rest Command, 30-Second Disconnect Grace Period, ADR-009 Effects System Architecture, LOGIN_WARDED Effect, Effects System ADR and Implementation, Effects System Implementation

### Community 524 - "MythosMUD UI Component Library"
Cohesion: 0.67
Nodes (3): Mythos Terminal Theme Tokens, StatusPanel, MythosMUD UI Component Library

### Community 525 - "player_connection_setup.py"
Cohesion: 0.11
Nodes (38): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions. This module handles the setup tasks when a…, Broadcast a structured entry event to other occupants (excluding the newcomer).… (+30 more)

### Community 526 - "Phase 2: Enhanced Features"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 2: Enhanced Features, Sub-tasks, Sub-tasks (+8 more)

### Community 527 - "type"
Cohesion: 0.13
Nodes (16): items, type, items, type, uniqueItems, minLength, type, effect_components (+8 more)

### Community 528 - "generate_sql.mjs"
Cohesion: 0.30
Nodes (15): ajv, __dirname, ensureDir(), __filename, generateEmotes(), generateHolidays(), generateNpcSchedules(), generateRooms() (+7 more)

### Community 529 - "PrototypeRegistry"
Cohesion: 0.12
Nodes (25): Initialize the item factory with a prototype registry. Args: registry: The…, PrototypeRegistry, Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, In-memory registry for validated item prototypes., Load prototypes from a directory of JSON files. (+17 more)

### Community 530 - "Phase 2: Qualitative Analysis Results"
Cohesion: 0.07
Nodes (30): 2.1 Regression Test Audit (★★★★★ HIGH VALUE), 2.2 Integration Test Analysis (★★★★☆ HIGH-MEDIUM VALUE), 2.3 Coverage Test Review (★★☆☆☆ MEDIUM-LOW VALUE), 2.4 Unit Test Pattern Analysis (★★★☆☆ MIXED VALUE), 2.5 Infrastructure Test Review (★☆☆☆☆ LOW VALUE), 2.6 E2E Test Analysis (★★★★★ HIGH VALUE), 2.7 Security Test Analysis (★★★★★ HIGH VALUE), Assessment (+22 more)

### Community 531 - "WebSocket Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (29): 10. **No Message Batching**, 11. **Missing Rate Limiting on WebSocket Messages**, 12. **Insufficient Authentication Validation**, 1. **Dependency Injection Pattern**, 1. **Event Loop Anti-Pattern in Connection Manager**, 2. **Missing Input Validation on Server Side**, 2. **Modern Async Patterns**, 3. **Error Boundaries** (+21 more)

### Community 532 - "GameTickService"
Cohesion: 0.05
Nodes (32): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+24 more)

### Community 533 - "LRUCache"
Cohesion: 0.04
Nodes (45): K, LRUCache, Put an item into the cache. Args: key: The key to store value: The value to…, Delete an item from the cache. Args: key: The key to delete Returns: True if…, Clear all items from the cache., Get the current number of items in the cache., Check if the cache is at maximum capacity., Get an item from the cache, or set it using a factory function if not found.… (+37 more)

### Community 535 - "TestPathValidator"
Cohesion: 0.10
Nodes (12): fixture, Tests for path validator functionality. Validates room connectivity analysis…, Test detection of mismatched return paths across zones., Test suite for path validation functionality., Create a path validator instance., Sample rooms with zone transitions., Test detection of zone transitions in room connections., Test detection of broken zone transitions. (+4 more)

### Community 536 - "test_event_bus.py"
Cohesion: 0.07
Nodes (27): Unit tests for event bus. Tests the EventBus class., Test EventBus.unsubscribe() with multiple handlers., Test EventBus.get_all_subscriber_counts() with no subscribers., Test EventBus.get_all_subscriber_counts() with multiple event types., Test subscribe() raises error for non-callable handler., Test unsubscribe() raises error for invalid event type., Test publish() raises error for invalid event., Test EventBus.subscribe() with service_id for tracking. (+19 more)

### Community 537 - "server/tests/conftest.py"
Cohesion: 0.10
Nodes (28): Config, Item, _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables(), _get_db_name_from_url(), AbstractEventLoop (+20 more)

### Community 538 - "HealthMonitor"
Cohesion: 0.04
Nodes (60): Lock, initialize_connection_cleaner(), initialize_connection_state(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging(), initialize_room_event_handler() (+52 more)

### Community 539 - "optimized_validate_player_name"
Cohesion: 0.12
Nodes (16): Test validating empty player name., Test validating valid player name., Test validating player name with underscore., Test validating player name with hyphen., Test validating player name with numbers., Test validating player name starting with number (invalid)., Test validating player name with special characters (invalid)., test_optimized_validate_player_name_empty() (+8 more)

### Community 540 - "optimized_security_validator.py"
Cohesion: 0.13
Nodes (15): Test benchmark function runs without errors., Test stripping ANSI codes from empty string., Test stripping ANSI codes from text without ANSI., Test stripping ANSI codes from text with ANSI., test_benchmark_validation_performance(), test_optimized_strip_ansi_codes_empty(), test_optimized_strip_ansi_codes_no_ansi(), test_optimized_strip_ansi_codes_with_ansi() (+7 more)

### Community 541 - "PanelContextRuntime.tsx"
Cohesion: 0.21
Nodes (9): defaultPanels, PanelContext, PanelContextType, PanelLayout, PanelPosition, PanelProvider(), PanelProviderProps, PanelSize (+1 more)

### Community 542 - "RoomInfo.tsx"
Cohesion: 0.29
Nodes (13): CompleteRoomInfo(), DebugInfo(), RoomDescription(), RoomEntities(), RoomExits(), RoomInfo(), RoomInfoContext, RoomInfoContextType (+5 more)

### Community 543 - "test_admin_teleport_commands.py"
Cohesion: 0.16
Nodes (42): handle_confirm_goto_command(), handle_confirm_teleport_command(), handle_goto_command(), handle_teleport_command(), Any, Handle the goto command for teleporting the admin to a player's location. Args:…, Handle the confirm teleport command for executing the actual teleportation.…, Handle the confirm goto command for executing the actual teleportation. Args:… (+34 more)

### Community 544 - "MessageBatcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 545 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 546 - "schemas/unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 547 - "FollowService"
Cohesion: 0.09
Nodes (27): FollowService, Any, UserManager, UUID, Fire-and-forget; close coro if no running event loop (e.g. sync unit tests)., Send a command_response-style message to a single player., Send command_response with result message and optional player_update (e.g.…, Send follow_state event so client can update title panel (who I am following). (+19 more)

### Community 548 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "A Message of Art; And Some Fell on Stony Ground; Nameless Ho", Community 10 - "Stowell; Betty Considine (waitress); Wesley Frost (bank cler", Community 1 - "Handout: Amaranthine 1; Dunwich (Keeper Map); Dunwich Throug", Community 2 - "An Amaranthine Desire; Captain Louis Gerd; Dunwich (Suffolk)", Community 3 - "An Amaranthine Desire; Clare Boone; Dunwich, Suffolk, Englan", Community 4 - "A Message of Art; Evocations of the Inner God; Josephin Pela", Community 5 - "Church of Sunyata; Craig Steele; The Hungry Void" (+12 more)

### Community 549 - "Test Server Remediation Prompt - Cursor Executable Version"
Cohesion: 0.14
Nodes (13): Best Practices, COMPLETION VERIFICATION, CRITICAL "DO NOT" INSTRUCTIONS, CRITICAL: EXECUTION REQUIREMENTS, DECISION TREE - START HERE, ERROR HANDLING PROTOCOL, MANDATORY PROGRESS TRACKING, MANDATORY VERIFICATION CHECKPOINTS (+5 more)

### Community 550 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 551 - "Chat Panel Separation Implementation Tasks"
Cohesion: 0.20
Nodes (9): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Overview, Phase Dependencies, Risk Mitigation, Technical Risks (+1 more)

### Community 552 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "Pandora's Box / Pandora Handout 10", Community 10 - "Chapter 6: Pulp Magic, Psychic Powers, and Weird S / Psychic Powers", Community 1 - "Disintegrator device / Handout: Disintegrator 1", Community 2 - "Chapter 1: The Pulps / Chapter 7: Running Pulp Games", Community 3 - "Avoiding Certain Death / Call of Cthulhu 7th Edition", Community 4 - "Cthulhu Mythos / Deep One", Community 5 - "Seekers of Eternal Wisdom / Handout: Pandora's Box 12" (+12 more)

### Community 553 - "test_container_persistence_sql_injection.py"
Cohesion: 0.17
Nodes (10): _create_mock_container_row(), UUID, Tests for SQL injection protection in container persistence operations. These…, Test that update_container uses parameterized queries, not string concatenation., Test that column names are hardcoded, not from user input., Create a complete mock container row with all required columns., Test SQL injection protection in container persistence., Test that SQL injection in lock_state is prevented. (+2 more)

### Community 554 - "MPRegenerationService"
Cohesion: 0.15
Nodes (13): MPRegenerationService, Any, UUID, MP regeneration service for passive and active magic point recovery. This…, Get MP regeneration multiplier based on player state. Args: stats: Player stats…, # TODO: Check status effects for meditation when status effect system supports…, Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…, # NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per… (+5 more)

### Community 555 - "AnyIO Code Review - Anti-Patterns and Issues"
Cohesion: 0.07
Nodes (28): 1. Entry Point Anti-Pattern: `asyncio.run()` Usage, 2.1 `asyncio.sleep()` Usage, 2.2 `asyncio.Lock()` Usage, 2.3 `asyncio.Event()` Usage, 2.4 `asyncio.Queue()` Usage, 2.5 `asyncio.wait_for()` Usage, 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage, 3.1 `asyncio.create_task()` Usage (+20 more)

### Community 556 - "ChatLogger"
Cohesion: 0.07
Nodes (25): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+17 more)

### Community 557 - "test_inventory_mutation_guard.py"
Cohesion: 0.07
Nodes (29): guard(), asyncio, fixture, Unit tests for inventory mutation guard - core functionality. Tests…, Test acquire_async without token allows mutation., Test acquire_async with unique token allows mutation., Test acquire_async with duplicate token suppresses mutation., Test acquire_async allows same token for different players. (+21 more)

### Community 558 - "Communities (10 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (19): Communities (10 total, 0 thin omitted), Community 0 - "Hotel Hell", Community 1 - "Petersen's Abominations", Community 2 - "Hotel Hell", Community 3 - "Voice on the Phone", Community 4 - "Mohole", Community 5 - "Panacea", Community 6 - "Panacea" (+11 more)

### Community 559 - "🎯 Async Remediation - Final Report"
Cohesion: 0.07
Nodes (28): All async anti-patterns have been exorcised from the codebase, All Targets Met, API/Commands (2 files), 🎯 Async Remediation - Final Report, Checklist, ✅ COMPLETE - ALL 48 INSTANCES MIGRATED, Core Infrastructure (2 files), 📚 Documentation Delivered (+20 more)

### Community 560 - "establish_websocket_connection"
Cohesion: 0.11
Nodes (31): _cleanup_dead_connections(), _cleanup_failed_connection(), establish_websocket_connection(), _EstablishmentConnectionManager, _find_dead_connections(), Player, Protocol, UUID (+23 more)

### Community 561 - "NPCCombatDataProvider"
Cohesion: 0.09
Nodes (27): NPCCombatDataProvider, Any, UUID, Get player name for messaging. Args: player_id: ID of the player Returns:…, Get the current room ID for a player. Args: player_id: ID of the player (must…, Get player combat participant data from persistence. Args: player_id: ID of the…, Get NPC combat participant data from NPC instance. Args: npc_instance: NPC…, Provides data retrieval and preparation for NPC combat. (+19 more)

### Community 562 - "NATS Subject Patterns"
Cohesion: 0.67
Nodes (3): NATS Error Handling Strategy, NATS Subject Patterns, NATS Subject Naming Patterns

### Community 563 - "NATS Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (28): 10. **Inconsistent Error Handling**, 11. **Missing Input Validation**, 1. **Blocking Operations in Message Handlers** (Anti-pattern violation), 1. **Excellent Error Boundary Implementation**, 2. **Good Connection State Management**, 2. **Missing Message Acknowledgment** (Anti-pattern violation), 3. **Connection Pool Not Used by Default** (Inefficiency), 3. **Proper Async/Await Usage** (+20 more)

### Community 564 - "performance.test.tsx"
Cohesion: 0.12
Nodes (13): Channel, ChannelSelectorProps, MemoryUsageDisplayProps, PerformanceChartProps, TerminalButtonProps, TerminalInputProps, ExtendedPerformance, PerformanceMemory (+5 more)

### Community 565 - "Persistence Layer Extraction - COMPLETE ✅"
Cohesion: 0.07
Nodes (28): Architecture Changes, Benefits, Cleanup, Conclusion, File Size Reduction, Files Modified, Group 1: Player Operations (~800 lines → ~80 lines), Group 2: Health & XP Operations (~400 lines → ~40 lines) (+20 more)

### Community 566 - "ChannelBroadcastingStrategyFactory"
Cohesion: 0.17
Nodes (11): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Register a new strategy for a channel type. Args: channel_type: Channel type to…, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…, Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., Test ChannelBroadcastingStrategyFactory.register_strategy() registers new…, Test global channel_strategy_factory instance exists., test_channel_broadcasting_strategy_factory_get_strategy_known() (+3 more)

### Community 567 - "UnknownChannelStrategy"
Cohesion: 0.25
Nodes (6): Strategy for unknown channel types., Initialize unknown channel strategy. Args: channel_type: Unknown channel type, Get strategy for channel type. Args: channel_type: Type of channel to get…, UnknownChannelStrategy, Test ChannelBroadcastingStrategyFactory.get_strategy() returns…, test_channel_broadcasting_strategy_factory_get_strategy_unknown()

### Community 568 - "verify_linting_parity.py"
Cohesion: 0.15
Nodes (27): check_alignment(), _check_pylint_suppressions(), _check_ruff_suppressions(), find_suppressions(), _has_pylint_equivalent(), _has_ruff_equivalent(), main(), parse_pylint_suppression() (+19 more)

### Community 569 - "CoordinateGenerator"
Cohesion: 0.07
Nodes (24): CoordinateGenerator, Any, AsyncSession, Load rooms and their exits from database. Args: plane: Plane name zone: Zone…, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits., Assign coordinates using BFS starting from origin., Detect conflicts (multiple rooms at same x,y coordinates). (+16 more)

### Community 570 - "properties"
Cohesion: 0.14
Nodes (14): description, description, description, description, type, properties, field1, field2 (+6 more)

### Community 571 - "🔴 CRITICAL ISSUES"
Cohesion: 0.07
Nodes (28): 10. Use of `BETWEEN` with Integer Ranges, 11. Missing Indexes on Foreign Keys, 12. Inconsistent Constraint Naming, 13. Mixed Case in Table/Column Names, 14. Missing `UNIQUE` Constraints Where Appropriate, 15. Inconsistent Use of `NOT NULL` Constraints, 16. Missing Documentation for Complex Constraints, 1. Use of `serial`/`SERIAL` Instead of `bigint generated always as identity` (+20 more)

### Community 572 - ".claude/hooks/record_edited_file.py"
Cohesion: 0.15
Nodes (20): _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path(), Any (+12 more)

### Community 573 - "asyncio"
Cohesion: 0.04
Nodes (45): asyncio, Test spawn_npc_instance() successfully spawns NPC., Test spawn_npc_instance() raises ValueError when definition not found., Test spawn_npc_instance() raises RuntimeError when spawn fails., Test despawn_npc_instance() successfully despawns NPC., Test despawn_npc_instance() is idempotent when NPC not found., Test despawn_npc_instance() raises RuntimeError when despawn fails., Test move_npc_instance() successfully moves NPC. (+37 more)

### Community 574 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.15
Nodes (13): 🔴 CRITICAL FIXES - Compilation Errors, For Each Issue Category, 🟡 HIGH PRIORITY FIXES - Code Quality Issues, 🎯 MANDATORY AI EXECUTION PROTOCOL, 🟢 MEDIUM PRIORITY FIXES - Style Issues, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide (+5 more)

### Community 575 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.15
Nodes (13): 🔴 CRITICAL FIXES - Compilation Errors, For Each Issue Category, 🟡 HIGH PRIORITY FIXES - Code Quality Issues, 🎯 MANDATORY AI EXECUTION PROTOCOL, 🟢 MEDIUM PRIORITY FIXES - Style Issues, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide (+5 more)

### Community 576 - "Phase 3: Polish and Optimization"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 3: Polish and Optimization, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 577 - "Phase 4: Testing and Refinement"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 4: Testing and Refinement, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 579 - "test_lifespan_event_subscriptions.py"
Cohesion: 0.17
Nodes (19): Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), subscribe_room_occupants_refresh(), QuestCompleted, Event fired when a quest instance is completed (rewards applied, state set to…, asyncio, Unit tests for lifespan event subscription producers. (+11 more)

### Community 580 - "fix_fstring_logging.py"
Cohesion: 0.12
Nodes (24): _build_structured_params(), _clean_message(), _create_replacement_for_fstring(), create_structured_log_message(), extract_variables_from_fstring(), fix_fstring_logging_in_file(), _handle_no_variables_case(), main() (+16 more)

### Community 581 - "Tiered Test Coverage Strategy"
Cohesion: 0.50
Nodes (4): Critical Code 90% Coverage, Global 70% Coverage Threshold, Tiered Test Coverage Strategy, Vitest Unit Tests

### Community 582 - "TestLogoutCommand"
Cohesion: 0.11
Nodes (17): Any, asyncio, fixture, Unit tests for the logout command handler., Test logout command when persistence is not available., Test logout command when persistence operations fail., Test cases for the logout command handler., Test logout command when connection cleanup fails. (+9 more)

### Community 583 - "properties"
Cohesion: 0.15
Nodes (13): minLength, type, maximum, minimum, type, minLength, type, type (+5 more)

### Community 584 - "Path"
Cohesion: 0.10
Nodes (14): Path, Fix self-references by adding proper flags. Args: room_database: Complete room…, Find the file for a room. Returns None if file doesn't exist., Create backup if requested., Fix missing exits field. Returns True if fixed., Fix missing optional fields. Returns True if any fixed., Initialize the room fixer. Args: base_path: Base directory for room files, Fix missing fields based on errors. Returns True if any fixed. (+6 more)

### Community 585 - "AsyncPersistenceLayer Pattern"
Cohesion: 0.38
Nodes (7): AsyncPersistenceLayer Pattern, Database Access Patterns, Eager Loading Best Practices, SQLAlchemy ORM Pattern, AsyncPG Connection Pool, Database Pool Configuration, SQLAlchemy Connection Pool

### Community 586 - "LucidityFluxService"
Cohesion: 0.04
Nodes (75): PassiveLucidityFluxService, FluxServiceConfig, lookup_profile(), normalize_environment_config(), period_label(), Any, datetime, Configuration and normalization for passive lucidity flux. (+67 more)

### Community 587 - "test_chat_moderation.py"
Cohesion: 0.11
Nodes (20): moderation(), player_service(), asyncio, fixture, Unit tests for chat moderation operations., test_add_admin_returns_true(), test_get_mute_status_handles_internal_error(), test_get_mute_status_includes_player_name() (+12 more)

### Community 588 - "3. REFACTOR Findings (935 findings)"
Cohesion: 0.07
Nodes (27): 1.1 Missing Module Docstrings (C0114), 1.2 Invalid Name (C0103), 1.3 Too Many Lines in Module (C0302), 1.4 Use Implicit Booleaness (C1805, C1804), 1.5 Singleton Comparison (C0121), 1.6 Missing Function Docstring (C0116), 1. CONVENTION Findings (260 findings), 2.1 No Name in Module (E0611) (+19 more)

### Community 589 - "test_chat_nats_publisher.py"
Cohesion: 0.08
Nodes (55): _build_legacy_subject(), _build_nats_message_data(), build_nats_subject(), _build_standardized_subject(), _chat_passes_nats_validation(), _extract_subzone_from_room(), _log_nats_publish_error(), _log_nats_unexpected_error() (+47 more)

### Community 591 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 592 - "Communities (10 total, 2 thin omitted)"
Cohesion: 0.11
Nodes (17): Communities (10 total, 2 thin omitted), Community 0 - "Azotottal (fallen angel beyond the stars) / Captain Louis Malon", Community 1 - "Charenton (Paris district / asylum) / Christophe Pressi — Soldat (Soldier), age 20", Community 2 - "Dreamlands / Fenalik's Mansion (Poissy)", Community 3 - "Reign of Terror / Call of Cthulhu 7th Edition", Community 4 - "Bastille / James Coquillat", Community 5 - "Azathoth / Celine Bessette", Community 6 - "Christophe Pressi / Comte Benoit" (+9 more)

### Community 593 - "InventorySchemaValidationError"
Cohesion: 0.07
Nodes (43): _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Player save/upsert helpers for PlayerRepository. Handles inventory validation,…, Validate and serialize inventory payload. Returns (inventory_json,… (+35 more)

### Community 594 - "test_statistics_aggregator.py"
Cohesion: 0.10
Nodes (24): mock_memory_monitor(), mock_message_queue(), mock_performance_tracker(), mock_rate_limiter(), mock_room_manager(), fixture, Unit tests for statistics aggregator. Tests the StatisticsAggregator class., Test get_connection_stats() returns connection statistics. (+16 more)

### Community 595 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 596 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 597 - "useMythosAppActions.ts"
Cohesion: 0.08
Nodes (50): CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), fetchCharactersList(), formatCharacterDate() (+42 more)

### Community 598 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, properties, minLength, type, id, name, season (+4 more)

### Community 599 - "LogAnalyzer"
Cohesion: 0.12
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time. Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 600 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, minLength, type, properties, minLength, type, type (+4 more)

### Community 601 - "required"
Cohesion: 0.17
Nodes (12): $defs, scheduleEntry, applies_to, category, days, end_hour, id, name (+4 more)

### Community 602 - "test_shopkeeper_npc.py"
Cohesion: 0.06
Nodes (35): Buy item from player., Calculate final price with markup., Handle greeting customer action., Handle restocking inventory action., Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., Shopkeeper NPC type with buy/sell functionality., Initialize shopkeeper NPC., Setup shopkeeper-specific behavior rules. (+27 more)

### Community 603 - "Test Coverage Summary: Disconnect Grace Period & Rest Command"
Cohesion: 0.07
Nodes (27): Coverage Targets, Coverage Verification, Critical Files (90% Target), E2E Scenarios, E2E Test Scenarios, E2E Test Scenarios, Expected Coverage Results, Grace Period System Tests (+19 more)

### Community 604 - "CoordinateValidator"
Cohesion: 0.14
Nodes (15): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Coordinate validation service for ASCII maps. This module provides conflict…, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:…, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate… (+7 more)

### Community 605 - "RoomCacheService"
Cohesion: 0.12
Nodes (11): Service for caching room data., Initialize the room cache service. Args: persistence: Persistence layer instance, Invalidate cached room data. Args: room_id: The room ID to invalidate, Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload, Initialize the cache service. Args: persistence: Persistence layer instance…, RoomCacheService, get_cache_manager(), Get the global cache manager instance. Returns: The global cache manager… (+3 more)

### Community 606 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)"
Cohesion: 0.12
Nodes (16): Communities (9 total, 4 thin omitted), Community 0 - "De Vermiis Mysteriis; Dust of Ibn-Ghazi", Community 1 - "Character Creation", Community 2 - "Alone Against the Flame", Community 3 - "Cover Art", Community 4 - "Azathoth; Banishment Chant (Latin)", Community Hubs (Navigation), Corpus Check (+8 more)

### Community 607 - "deque"
Cohesion: 0.08
Nodes (49): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+41 more)

### Community 608 - "test_command_processor.py"
Cohesion: 0.10
Nodes (19): Unit tests for command processor. Tests the CommandProcessor class which…, Test _is_combat_command returns True for punch command., Test _is_combat_command returns True for kick command., Test extract_command_data handles player_name attribute., Test CommandProcessor initializes correctly., Test validate_command_safety returns False for unsafe command., Test get_command_help handles ValueError., Test get_command_help handles TypeError. (+11 more)

### Community 609 - "server/dependencies.py"
Cohesion: 0.01
Nodes (187): LevelUpHook, get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service() (+179 more)

### Community 610 - "test_npc_startup_service.py"
Cohesion: 0.10
Nodes (20): npc_startup_service(), fixture, Unit tests for NPC startup service. Tests the NPCStartupService class., Test _get_default_room_for_sub_zone() returns correct room for known sub-zone., Test _get_default_room_for_sub_zone() returns None for unknown sub-zone., Test _get_default_room_for_sub_zone() is case insensitive., Test get_npc_startup_service() returns service instance., Create an NPCStartupService instance. (+12 more)

### Community 611 - "test_player_event_handlers_utils.py"
Cohesion: 0.12
Nodes (15): Unit tests for player event handler utilities. Tests the…, Test normalize_event_ids() with string IDs., Test process_dict_occupant() processes player occupant., Test build_occupants_snapshot_data() with empty list., Test count_occupants_by_type() with empty list., Test is_player_disconnecting() returns False when player is not disconnecting., Test is_player_disconnecting() handles invalid player_id., Test normalize_player_id() with None returns None without warning. (+7 more)

### Community 612 - "test_combat_persistence_handler_events.py"
Cohesion: 0.06
Nodes (43): mock_combat_service(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully., Test _publish_player_dp_update_event_impl handles no NATS service., Test _publish_player_dp_update_event_impl with all optional parameters. (+35 more)

### Community 613 - "test_chat_validator.py"
Cohesion: 0.14
Nodes (24): contains_malicious_content(), Chat message validation utilities. This module provides validation functions…, Validate chat message before transmission. Args: chat_message: The chat message…, Validate sender has access to the room. Args: sender_id: ID of the message…, Check for malicious content patterns. Args: content: The message content to…, validate_chat_message(), validate_room_access(), _message() (+16 more)

### Community 614 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)"
Cohesion: 0.12
Nodes (15): Communities (17 total, 12 thin omitted), Community 0 - "Character and Skills", Community 1 - "Character and Skills (1)", Community 2 - "Core Rules", Community 3 - "Core Rules (3)", Community 4 - "Character Sheets", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 615 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (12 total, 7 thin omitted), Community 0 - "Call of Cthulhu (7th Edition); Chaosium Inc.", Community 1 - "APP; Characteristics", Community 2 - "Everett Scanlon; Gustavo Romero", Community 3 - "First Aid; Hit Points", Community 4 - "Formless Spawn of Tsathoggua; Rudolf Zimmer", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 616 - "room_hierarchy_schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, anyOf, description, description, exits, id, name, required (+3 more)

### Community 617 - "GridLayoutManager.tsx"
Cohesion: 0.20
Nodes (5): GridLayoutManager(), GridLayoutManagerProps, layoutConfig, PanelComponent, ResponsiveGridLayout

### Community 618 - "PydanticErrorHandler"
Cohesion: 0.05
Nodes (45): MythosValidationError, convert_pydantic_error(), _ExtractedErrorInfo, _ExtractedFieldErrorInfo, handle_pydantic_error(), TypedDict, Unpack, ValidationError (+37 more)

### Community 619 - "Game Subsystem Design Documents"
Cohesion: 0.13
Nodes (18): Linkdead Grace Period, Gunicorn + Uvicorn Production, HTTPS and WSS Requirement, Disconnect Grace Period (linkdead), Login Grace Period (warded), WebSocket JWT in URL Query String, Item System Observability Runbook, Game Subsystem Design Documents (+10 more)

### Community 620 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.22
Nodes (9): 10. Final Verification, 5. Test Environment Setup, 6. Quality Assurance Checklist, 8. Error Handling and Debugging, Common Debug Commands, Environment Variables, REQUIRED TOOL USAGE PATTERN, Test Configuration (+1 more)

### Community 621 - "CircuitBreaker Implementation Planning Document"
Cohesion: 0.18
Nodes (10): CircuitBreaker Implementation Planning Document, Configuration Schema, Dependencies, Gradual Rollback, Immediate Rollback, Objectives, Overview, Rollback Plan (+2 more)

### Community 622 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (5 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Bernard Corbitt; Randolph Tomaszewski", Community 2 - "Ramasekva; Yog-Sothoth", Community 3 - "Arthur Cornthwaite; Fitzgerald Manse", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions) (+7 more)

### Community 623 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 624 - "properties"
Cohesion: 0.18
Nodes (11): description, type, description, type, description, minimum, type, combat_modifier (+3 more)

### Community 625 - "ContainerData"
Cohesion: 0.03
Nodes (122): ContainerData, ContainerDataCore, ContainerDataExtras, Container data class for persistence operations., Identity and placement fields for a container row., Optional payload and timestamps for a container row., Data class for container information., Convert container data to dictionary. Returns dictionary with model field names… (+114 more)

### Community 626 - "multiplayer-playwright-testing.md"
Cohesion: 0.20
Nodes (9): 🎯 AVAILABLE SCENARIOS, 🔄 BACKWARD COMPATIBILITY, 🚨 CRITICAL AI EXECUTOR REQUIREMENTS 🚨, 📋 EXECUTION OPTIONS, 📖 MANDATORY EXECUTION ORDER, 🛑 MANDATORY EXECUTION PROTOCOL 🛑, 🎮 MODULAR E2E TEST SUITE STRUCTURE 🎮, 🔧 TESTING APPROACH (+1 more)

### Community 627 - "Mypy Type Checking Remediation Prompt - AI-Optimized Version"
Cohesion: 0.20
Nodes (9): 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, Common Mypy Error Codes, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, 📊 MYPY ERROR CODE CATEGORIZATION GUIDE, Mypy Type Checking Remediation Prompt - AI-Optimized Version (+1 more)

### Community 628 - "get_config"
Cohesion: 0.04
Nodes (61): _create_config_instance(), get_config(), _get_config_cached(), _get_config_test(), _is_test_mode(), Reset the configuration cache. In test mode, this is a no-op since get_config()…, Detect if running in test environment. Uses multiple detection methods to…, Create a new AppConfig instance from current environment. This is a helper… (+53 more)

### Community 629 - "PrototypeRegistryError"
Cohesion: 0.09
Nodes (29): ItemInstance, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError, Any, Exception, Item factory for creating item instances from prototypes. This module provides…, Raised when the factory cannot produce a valid instance. (+21 more)

### Community 630 - "Movement Subsystem Design"
Cohesion: 0.17
Nodes (11): 1. Overview, 2. Architecture, 3. Key design decisions, 4. Constraints, 5. Component interactions, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 631 - "load_test_10_players.spec.ts"
Cohesion: 0.22
Nodes (6): generateLoadTestCredential(), INVITE_CODES, PLAYER_CONFIGS, PlayerConfig, NOTE: This test is designed to be executed using Playwright MCP tools for, registerPlayer()

### Community 632 - "enum"
Cohesion: 0.20
Nodes (10): city, countryside, desert, mountains, swamp, tundra, zone_type, description (+2 more)

### Community 633 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (10 total, 4 thin omitted), Community 0 - "Azathoth / Byakhee", Community 1 - "Call of Cthulhu / Chaosium Inc.", Community 2 - "Dimensional Shambler / Elder Thing", Community 3 - "Abhoth / Atlach-Nacha", Community 4 - "Deep One / Ghast", Community 5 - "Dark Young / Dark Young of Shub-Niggurath", Community Hubs (Navigation) (+7 more)

### Community 634 - "properties"
Cohesion: 0.20
Nodes (10): properties, minLength, pattern, type, minLength, type, type, id (+2 more)

### Community 635 - "days"
Cohesion: 0.22
Nodes (10): items, items, minItems, type, items, type, pattern, type (+2 more)

### Community 636 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 637 - "mock_container"
Cohesion: 0.11
Nodes (25): mock_connection_manager(), mock_container(), fixture, Create mock connection manager., Create mock container., _assign_container_get_instance(), Test _determine_spawn_room() uses NPC's room_id when available., Test _determine_spawn_room() uses sub_zone default when room_id not available. (+17 more)

### Community 638 - "Comprehensive System Audit"
Cohesion: 0.67
Nodes (3): CI/CD Enhanced Logging Validation, Comprehensive System Audit, Database Migration Guide

### Community 639 - "player_effect_repository.py"
Cohesion: 0.05
Nodes (54): PlayerEffect, Base, Persistent player effect (status effect) with tick-based duration. Table:…, _add_effect_params(), AddEffectInput, _int_opt(), _opt_str(), PlayerEffectRepository (+46 more)

### Community 640 - "NPCCommunicationIntegration"
Cohesion: 0.10
Nodes (23): NPCCommunicationIntegration, Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…, Process a message to determine if the NPC should respond. Args: npc_id: ID of…, Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…, Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…, Integrates NPCs with the existing chat and whisper systems. This class provides…, Initialize the NPC communication integration. Args: event_bus: Optional…, Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the… (+15 more)

### Community 641 - "Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.07
Nodes (26): 1. Deprecated `asyncio.get_event_loop()` Usage, 1. Proper Connection Pool Management, 2. Good Error Handling Patterns, 2. SQL Injection Risk in Field Name Construction, 3. Async/Await Usage, 3. Connection Pool Cleanup Verification, 4. Blocking Operations in Async Context, 4. Security Considerations (+18 more)

### Community 642 - "Security Implementation"
Cohesion: 0.29
Nodes (7): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection, SSE Authentication System

### Community 643 - "test_argon2_utils.py"
Cohesion: 0.03
Nodes (86): PasswordHasher, E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio. (+78 more)

### Community 644 - "migrate_combat_data.py"
Cohesion: 0.05
Nodes (77): Draft7Validator, add_default_combat_data_to_config(), add_default_combat_data_to_stats(), CombatSchemaValidationError, get_combat_stats_summary(), Any, Exception, Combat system JSON schema validation. This module provides JSON schema… (+69 more)

### Community 645 - "PersonalMessageSender"
Cohesion: 0.12
Nodes (26): PersonalMessageSender, Any, UUID, Send message to a single WebSocket connection. Returns True if successful., Queue message if no active connections., Send a personal message to a player via WebSocket. Args: player_id: The…, Get message delivery statistics for a player., Sends personal messages to individual players. This class provides: - Personal… (+18 more)

### Community 646 - "PeriodicOrphanAuditor"
Cohesion: 0.12
Nodes (30): create_lifespan_memory_service(), PeriodicOrphanAuditor, Create a centralized memory operations coordinator instance targeted for…, Periodic background auditor that investigates orphanage patterns and memory…, asyncio, Unit tests for periodic orphan auditing and lifespan memory coordination., No orphans and no threshold breach skips cleanup., Audit cycle errors are logged without propagating. (+22 more)

### Community 647 - "should_spawn_npc"
Cohesion: 0.08
Nodes (37): _population_allows_spawn(), Any, Spawn Validator Module. This module provides logic for validating whether NPCs…, Determine if an NPC should spawn based on conditions. Args: definition: NPC…, Return False when zone population blocks this NPC definition., Evaluate one spawn rule; return True when probability roll succeeds., Return True when any spawn rule passes probability checks., should_spawn_npc() (+29 more)

### Community 648 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 649 - "test_player_event_handlers_room.py"
Cohesion: 0.17
Nodes (11): Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test broadcast_player_entered_message() skips when room_id is None., Test _prepare_room_data() handles room without to_dict method., Test send_room_update_to_player() successfully sends room update., Test PlayerRoomEventHandler initialization., Test log_player_movement() skips when connection manager not available., test_broadcast_player_entered_message_no_room_id(), test_log_player_movement_no_connection_manager() (+3 more)

### Community 650 - "test_inventory_command_prototype.py"
Cohesion: 0.12
Nodes (26): _first_normalized_wear_slot(), infer_equip_slot_from_prototype(), _inventory_prototype_id(), prototype_from_registry(), prototype_registry_from_request(), Prototype registry access and equip-slot inference for inventory items., Resolve prototype registry from FastAPI-style request (agent-readable…, Return the prototype object for ``prototype_id``, or None if missing or invalid. (+18 more)

### Community 651 - "PostgresRow"
Cohesion: 0.11
Nodes (13): PostgresRow, Row-like object for PostgreSQL query results., Test PostgresRow class., Test PostgresRow initialization., Test PostgresRow.__getitem__ with string key., Test PostgresRow.__getitem__ with integer index., Test PostgresRow.__getitem__ with out-of-range integer index., Test PostgresRow.__iter__. (+5 more)

### Community 652 - "CORSConfig"
Cohesion: 0.08
Nodes (29): CORSConfig, Any, BaseSettings, field_validator, model_validator, Parse comma-separated string into cleaned list., Parse comma separated strings or lists into a cleaned list of strings., Parse allowed origins from various input formats. (+21 more)

### Community 653 - "RateLimiter"
Cohesion: 0.10
Nodes (17): Any, RateLimiter, Remove timestamps older than the window size. Args: player_id: Player ID…, Check if a player is within rate limits for a channel. Args: player_id: Player…, Record a message for rate limiting. Args: player_id: Player ID channel: Channel…, Sliding window rate limiter for chat channels. Implements per-user, per-channel…, Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…, Reset rate limiting for a player. Args: player_id: Player ID channel: Specific… (+9 more)

### Community 654 - "get_room_environment"
Cohesion: 0.12
Nodes (14): Test get_room_environment() treats empty string as no environment., Test get_room_environment() function., Test get_room_environment() returns room-specific environment., Test get_room_environment() returns subzone environment when room doesn't have…, Test get_room_environment() returns zone environment when room and subzone…, Test get_room_environment() returns default 'outdoors' when no environment…, Test get_room_environment() prioritizes room environment over subzone and zone., Test get_room_environment() prioritizes subzone environment over zone. (+6 more)

### Community 655 - "optimized_validate_action_content"
Cohesion: 0.20
Nodes (10): Test validating empty action., Test validating valid action., Test validating action with dangerous characters., Test validating action with injection pattern., test_optimized_validate_action_content_dangerous_chars(), test_optimized_validate_action_content_empty(), test_optimized_validate_action_content_injection(), test_optimized_validate_action_content_valid() (+2 more)

### Community 656 - "optimized_validate_alias_name"
Cohesion: 0.20
Nodes (10): Test validating empty alias name., Test validating valid alias name., Test validating alias name starting with number (invalid)., Test validating alias name with hyphen (invalid - aliases don't allow hyphens)., test_optimized_validate_alias_name_empty(), test_optimized_validate_alias_name_hyphen(), test_optimized_validate_alias_name_starts_with_number(), test_optimized_validate_alias_name_valid() (+2 more)

### Community 657 - "PlayerGuidFormatter"
Cohesion: 0.05
Nodes (53): PlayerGuidFormatter, LogRecord, Player GUID Formatter for MythosMUD logging system. This module provides a…, Determine if a GUID is likely to be a player ID based on context. Args: guid:…, Get player name for GUID from in-memory data. Args: guid: The player GUID to…, Custom formatter that converts player GUIDs to "<name>: <GUID>" format. This…, Initialize the PlayerGuidFormatter. Args: player_service: Service for accessing…, Format a log record with enhanced player GUID display. Args: record: The log… (+45 more)

### Community 658 - "optimized_sanitize_unicode_input"
Cohesion: 0.20
Nodes (10): Test sanitizing empty string., Test sanitizing normal text (no changes expected)., Test sanitizing text with Unicode issues., test_optimized_sanitize_unicode_input_empty(), test_optimized_sanitize_unicode_input_normal_text(), test_optimized_sanitize_unicode_input_unicode(), _cached_ftfy_fix(), optimized_sanitize_unicode_input() (+2 more)

### Community 659 - "optimized_validate_security_comprehensive"
Cohesion: 0.20
Nodes (10): Test comprehensive security validation of empty string., Test comprehensive security validation of valid text., Test comprehensive security validation with dangerous characters., Test comprehensive security validation with injection pattern., test_optimized_validate_security_comprehensive_dangerous_chars(), test_optimized_validate_security_comprehensive_empty(), test_optimized_validate_security_comprehensive_injection(), test_optimized_validate_security_comprehensive_valid() (+2 more)

### Community 660 - "TestRunner"
Cohesion: 0.12
Nodes (13): main(), Path, Verify test database configuration. Note: For PostgreSQL databases, schema is…, Build the pytest command with proper configuration. Args: test_paths: List of…, Run the test suite with proper configuration. Args: test_paths: List of test…, Run integration tests only., Run all tests (unit, integration, but not E2E by default)., Generate coverage report only. (+5 more)

### Community 661 - "asyncio"
Cohesion: 0.10
Nodes (21): asyncio, Test _spawn_required_npcs() successfully spawns required NPCs., Test _spawn_required_npcs() handles spawn failures., Test _spawn_optional_npcs() spawns based on probability., Test _spawn_optional_npcs() skips NPCs with low probability., Test _spawn_optional_npcs() handles missing spawn room., Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute., Arena pass is skipped when required/optional passes spawned nothing. (+13 more)

### Community 662 - "test_lucidity_command_disruption.py"
Cohesion: 0.16
Nodes (19): can_perform_action(), get_misfire_message(), Command disruption utilities for lucidity system. Implements command misfires…, Check if a command should misfire based on tier and command type. Args:…, Get the misfire message for a failed command. Args: command_type: Type of…, Check if player should involuntarily flee. Args: tier: Current lucidity tier…, Check if player can perform actions (motor lock check). Args: tier: Current…, should_involuntary_flee() (+11 more)

### Community 663 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 664 - "weather_patterns"
Cohesion: 0.40
Nodes (5): type, weather_patterns, description, items, type

### Community 665 - "run-playwright-tests.js"
Cohesion: 0.22
Nodes (7): clientRoot, __dirname, E2E_BACKEND_BASE_URL, env, __filename, playwright, testsDir

### Community 666 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.22
Nodes (9): For Each Issue Category, 🎯 MANDATORY AI EXECUTION PROTOCOL, Mypy Type Checking, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide, Phase 6: Verification Protocol, Phase 7: Success Validation (+1 more)

### Community 667 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 668 - "SQLAlchemyAsyncLinter"
Cohesion: 0.11
Nodes (18): Await, lint_directory(), lint_file(), main(), Call, Import, ImportFrom, Path (+10 more)

### Community 669 - "CombatValidator"
Cohesion: 0.08
Nodes (18): When party_service is None, validate_can_attack_target allows attack., When both players are in same party, validate_can_attack_target blocks attack., When players are not in same party, validate_can_attack_target allows attack., test_validate_can_attack_target_different_party_allows(), test_validate_can_attack_target_no_party_service_allows(), test_validate_can_attack_target_same_party_blocks(), CombatValidator, Enhanced combat command validator with thematic error messages. Provides… (+10 more)

### Community 670 - "applies_to"
Cohesion: 0.28
Nodes (9): items, minItems, type, uniqueItems, items, items, minLength, type (+1 more)

### Community 671 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 672 - "Technical Implementation"
Cohesion: 0.22
Nodes (9): 2. Message Routing Logic, 3. State Management, 4. Event Handling, Command Routing Logic, Current Logic (in CommandPanel), New Logic Distribution, New State Structure, State Distribution (+1 more)

### Community 673 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 674 - "extract_player_name"
Cohesion: 0.13
Nodes (24): extract_player_name(), _get_name_from_user(), get_player_position(), _is_uuid_string(), _is_valid_name(), Any, Player, UUID (+16 more)

### Community 675 - "test_npc_event_handlers_helpers.py"
Cohesion: 0.09
Nodes (25): mock_connection_manager(), mock_message_builder(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers helper functions. Tests the helper functions…, Test _determine_direction_from_rooms() determines direction., Test _determine_direction_from_rooms() returns None when direction not found. (+17 more)

### Community 676 - "errorHandler.ts"
Cohesion: 0.13
Nodes (33): getCreateCharacterErrorMessage(), extractErrorMessageFromResponseBody(), errorMessageFromApiBody(), messageFromCreationRefreshHttpError(), parseRefreshFailure(), isObject(), loginFailureMessage(), tryStartLoginGracePeriod() (+25 more)

### Community 677 - "test_party_commands.py"
Cohesion: 0.08
Nodes (50): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+42 more)

### Community 678 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 679 - "test_connection_establishment.py"
Cohesion: 0.08
Nodes (52): _as_mgr(), _FakeEstablishmentManager, _make_manager(), asyncio, Unit tests for connection establishment. Tests the connection_establishment…, Test _find_dead_connections() returns empty list when player not found., Test _find_dead_connections() skips connections not in active_websockets., Test _find_dead_connections() raises ConnectionError when websocket is None. (+44 more)

### Community 680 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 681 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 682 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)"
Cohesion: 0.13
Nodes (14): Communities (8 total, 5 thin omitted), Community 0 - "Baron Arthur von Kleist; Pyotr Shabelsky-Bork", Community 1 - "The Demon-Großmann; Demonic Mutation Table", Community 2 - "Erwin Kern; Manfred Freiherr von Killinger", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11) (+6 more)

### Community 683 - "Async Facades Implementation - COMPLETE ✅"
Cohesion: 0.08
Nodes (25): (A) and (B) Relationship: **Complementary**, (A) AsyncPersistenceLayer Integration ✅, Async Facades Implementation - COMPLETE ✅, Async Tests, (B) Sync Shim - NOT NEEDED ⏭️, Benefits Achieved, Both facades are now operational, Conclusion (+17 more)

### Community 684 - "attach_compatibility_properties"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 685 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Anna Konrad; Lucas Reston", Community 2 - "Does Love Forgive", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12) (+6 more)

### Community 686 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 687 - "migrate_rooms.py"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 688 - "run-vitest.js"
Cohesion: 0.25
Nodes (7): args, clientRoot, __dirname, env, __filename, vitest, vitestBin

### Community 689 - "usePerformanceMonitor.ts"
Cohesion: 0.29
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 690 - "holidays.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 691 - "npc_schedules.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 692 - "1. Enhanced ChatPanel (New Chat Input Panel)"
Cohesion: 0.25
Nodes (8): 1. Enhanced ChatPanel (New Chat Input Panel), 2. Renamed Game Log Panel (Formerly ChatPanel), ChatPanel Layout Structure, Enhanced ChatPanel Interface, Game Log Panel Layout Structure, New Features to Add, Proposed Changes, Purpose and Functionality

### Community 693 - "Implementation Phases"
Cohesion: 0.25
Nodes (8): 1.1 Enhance CircuitBreaker Class, 1.2 Create CircuitBreaker Manager, 1.3 Add Configuration Support, 5.1 Authentication Operations, 5.2 Rate Limiting Integration, Implementation Phases, Phase 1: Core Infrastructure Enhancement, Phase 5: Authentication and Security

### Community 694 - "Migration 019: Complete Implementation Summary"
Cohesion: 0.08
Nodes (25): 1. Database Schema Updates ✅, 2. Python Model Updates ✅, 3. Migration Script Created ✅, 4. Testing Infrastructure ✅, Before Production, Conclusion, Created Files (5), Documentation Files (4) (+17 more)

### Community 695 - "enum"
Cohesion: 0.20
Nodes (10): artifact, consumable, container, currency, equipment, quest, enum, type (+2 more)

### Community 696 - "enum"
Cohesion: 0.25
Nodes (8): catholic, islamic, jewish, mythos, neo_pagan, tradition, enum, type

### Community 697 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Pre-Generated Investigators", Community 1 - "Pre-Generated Investigators (1)", Community 2 - "Pre-Generated Investigators (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12) (+6 more)

### Community 698 - "enum"
Cohesion: 0.25
Nodes (8): Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, enum

### Community 699 - "holiday.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 700 - "schedule.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 702 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 703 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 704 - "validate.mjs"
Cohesion: 0.32
Nodes (7): ajv, __dirname, __filename, loadJson(), main(), root, validateFile()

### Community 705 - "test_load_world_seed.py"
Cohesion: 0.12
Nodes (25): regression, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, CaptureFixture, fixture, MonkeyPatch, Protocol (+17 more)

### Community 706 - "MythosMUD Worldbuilding Source"
Cohesion: 0.67
Nodes (3): MythosMUD Wiki Log, MythosMUD Worldbuilding Foundation (Raw), MythosMUD Worldbuilding Source

### Community 707 - "realtime/realtime.py"
Cohesion: 0.13
Nodes (22): ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD. This module defines…, Presence statistics for connection monitoring. This model represents aggregate…, Session statistics for connection monitoring. This model represents aggregate…, Error statistics for connection monitoring. This model represents aggregate…, SessionStatistics (+14 more)

### Community 708 - "Migration 019 Verification Report"
Cohesion: 0.08
Nodes (24): 1. Code Quality Checks, 2. Model Updates Verified, 3. Type Compatibility, 4. Database Schema Alignment, Before Production Deployment, Conclusion, Documentation (3 files), Files Modified Summary (+16 more)

### Community 709 - "ContainerServiceError"
Cohesion: 0.02
Nodes (163): ContainerAccessMixin, ContainerComponent, UUID, Container access validation (ownership, proximity, roles, corpse grace). Mixin…, Deny non-owner corpse access during (or without) a timed grace period., Validate corpse grace period access rules., Validate that player has access to the container. Checks proximity, ownership,…, Return True if player inventory contains the required key item_id. (+155 more)

### Community 710 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

### Community 711 - "Phase 4: Recommendations"
Cohesion: 0.08
Nodes (25): 1. Prune Infrastructure Tests (Save ~3 minutes, Remove ~350 tests), 2. Consolidate Coverage Tests (Save ~1 minute, Reduce ~60 tests), 3. Parametrize Repetitive Tests (Save ~1 minute, Reduce ~300 tests), 4.1 Pruning Candidates (750 tests, ~5 minutes savings), 4.2 Consolidation Opportunities, 4.3 Coverage Gap Identification, 4.4 Optimization Recommendations, 4. Migrate Model Tests to Property-Based Testing (+17 more)

### Community 712 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _build_room_objects successfully builds room objects., Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., test_build_room_objects_success(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

### Community 713 - "UUID"
Cohesion: 0.17
Nodes (9): Any, UUID, Broadcast party message to party members only, with dampening and mute checks., Send whisper message to specific player with communication dampening., Broadcast system/admin message; personal when target_player_id is set., Handle unknown channel type., Broadcast message according to channel strategy. Args: chat_event: WebSocket…, Broadcast room-based message with server-side filtering. (+1 more)

### Community 714 - "Design Critique"
Cohesion: 0.10
Nodes (19): 10. Microcopy & Voice, 1. AI Slop Detection (CRITICAL), 2. Visual Hierarchy, 3. Information Architecture, 4. Emotional Resonance, 5. Discoverability & Affordance, 6. Composition & Balance, 7. Typography as Communication (+11 more)

### Community 715 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 716 - "test_combat_messaging_integration.py"
Cohesion: 0.11
Nodes (17): Unit tests for combat messaging integration. Tests the…, Test connection_manager setter updates value., Test connection_manager setter overrides lazy load mechanism., Test CombatMessagingIntegration initialization., Test CombatMessagingIntegration initialization without connection manager., Test connection_manager property lazy loads from container., Test _resolve_connection_manager_from_container resolves manager., Test _resolve_connection_manager_from_container raises when no manager. (+9 more)

### Community 717 - "test_rate_limiter.py"
Cohesion: 0.03
Nodes (60): mock_config(), fixture, rate_limiter(), Unit tests for rate limiter service. Tests the RateLimiter class which provides…, Test check_rate_limit returns True when within limits., Test check_rate_limit returns False when limit exceeded., Test check_rate_limit always returns True when disabled., Test check_rate_limit handles errors gracefully (fails open). (+52 more)

### Community 718 - "test_cache_service.py"
Cohesion: 0.15
Nodes (11): ProfessionCacheService, Service for caching profession data., Invalidate all profession caches., Reset the global cache manager (for testing)., reset_cache_manager(), Create room and profession cache services; set to None on RuntimeError., _Profession, fixture (+3 more)

### Community 719 - "chat_message.py"
Cohesion: 0.15
Nodes (16): create_and_log_chat_message(), create_and_log_say_message(), Message creation and storage helpers for chat service., Create chat message and log it., Create say chat message and log it., Store message in room history with limit management., Store global message in history., store_global_message_in_history() (+8 more)

### Community 720 - "optimized_validate_command_content"
Cohesion: 0.25
Nodes (8): Test validating empty command content., Test validating valid command content., Test validating command content with injection pattern., test_optimized_validate_command_content_empty(), test_optimized_validate_command_content_injection(), test_optimized_validate_command_content_valid(), optimized_validate_command_content(), Optimized validation for command content fields. Args: value: The command…

### Community 721 - "optimized_validate_reason_content"
Cohesion: 0.25
Nodes (8): Test validating empty reason content., Test validating valid reason content., Test validating reason content with injection pattern., test_optimized_validate_reason_content_empty(), test_optimized_validate_reason_content_injection(), test_optimized_validate_reason_content_valid(), optimized_validate_reason_content(), Optimized validation for reason content fields. Args: value: The reason to…

### Community 722 - "optimized_validate_pose_content"
Cohesion: 0.25
Nodes (8): Test validating empty pose content., Test validating valid pose content., Test validating pose content with injection pattern., test_optimized_validate_pose_content_empty(), test_optimized_validate_pose_content_injection(), test_optimized_validate_pose_content_valid(), optimized_validate_pose_content(), Optimized validation for pose content fields. Args: value: The pose to validate…

### Community 723 - "validate_secure_path"
Cohesion: 0.08
Nodes (24): Validate and sanitize a user-provided path to prevent path traversal attacks.…, validate_secure_path(), Test validate_secure_path detects when common_path != base_path (lines 59-66)., Test validate_secure_path with valid path., Test validate_secure_path handles different drives on Windows., Test validate_secure_path rejects path traversal with .., Test validate_secure_path rejects path traversal with ~, Test validate_secure_path with nested valid path. (+16 more)

### Community 724 - "MetricsCollector"
Cohesion: 0.08
Nodes (18): MetricsCollector, Any, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or…, Simple metrics collector for NATS message delivery. Thread-safe metrics…, Get concise metrics summary. Returns: High-level metrics summary AI: For quick… (+10 more)

### Community 725 - "optimized_validate_filter_name"
Cohesion: 0.25
Nodes (8): Test validating empty filter name., Test validating valid filter name., Test validating invalid filter name., test_optimized_validate_filter_name_empty(), test_optimized_validate_filter_name_invalid(), test_optimized_validate_filter_name_valid(), optimized_validate_filter_name(), Optimized validation for filter name fields. Args: value: The filter name to…

### Community 726 - "optimized_validate_target_player"
Cohesion: 0.25
Nodes (8): Test validating empty target player name., Test validating valid target player name., Test validating invalid target player name., test_optimized_validate_target_player_empty(), test_optimized_validate_target_player_invalid(), test_optimized_validate_target_player_valid(), optimized_validate_target_player(), Optimized validation for target player fields. Args: value: The target player…

### Community 727 - "optimized_validate_help_topic"
Cohesion: 0.25
Nodes (8): Test validating empty help topic., Test validating valid help topic., Test validating invalid help topic., test_optimized_validate_help_topic_empty(), test_optimized_validate_help_topic_invalid(), test_optimized_validate_help_topic_valid(), optimized_validate_help_topic(), Optimized validation for help topic fields. Args: value: The help topic to…

### Community 728 - "verify_migration.py"
Cohesion: 0.15
Nodes (22): _check_foreign_keys(), _check_null_values(), _check_table_exists(), main(), _print_json_validation_results(), _print_sample_data(), _print_verification_summary(), Connection (+14 more)

### Community 729 - "optimized_comprehensive_sanitize_input"
Cohesion: 0.25
Nodes (8): Test comprehensive sanitization of empty string., Test comprehensive sanitization of normal text., Test that optimized comprehensive sanitization normalizes newlines to spaces., test_optimized_comprehensive_sanitize_input_empty(), test_optimized_comprehensive_sanitize_input_normal(), test_optimized_comprehensive_sanitize_input_normalizes_newlines(), optimized_comprehensive_sanitize_input(), Optimized comprehensive input sanitization. Args: text: Raw input text to…

### Community 730 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 731 - "useGridLayout.ts"
Cohesion: 0.33
Nodes (5): layoutConfig, PanelState, STORAGE_KEYS, useGridLayout(), UseGridLayoutReturn

### Community 732 - "Geography Overview.md"
Cohesion: 0.15
Nodes (8): Bleak Prospect, Dreamlands, Geography Overview, Engineering memory, MythosMUD, Sources, World, Paris (Reign of Terror)

### Community 733 - "Chat Panel Separation Specification"
Cohesion: 0.29
Nodes (6): Chat Panel Separation Specification, Conclusion, Current Integration Points, Current State Analysis, Existing Structure, Overview

### Community 734 - "Code Review: Import Analysis and Anti-Patterns"
Cohesion: 0.08
Nodes (23): 1. **Import Inconsistency in `server/persistence.py`**, 2. **Import Organization Pattern**, Additional Findings, Best Practices Analysis, Code Review: Import Analysis and Anti-Patterns, Conclusion, Configuration Files, Container Files (+15 more)

### Community 735 - "enum"
Cohesion: 0.29
Nodes (7): autumn, spring, summer, winter, season, enum, type

### Community 736 - "enum"
Cohesion: 0.29
Nodes (7): description, enum, type, indoors, outdoors, underwater, environment

### Community 737 - "room_validator/schemas/unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 738 - "properties"
Cohesion: 0.25
Nodes (8): description, enum, type, indoors, outdoors, underwater, properties, environment

### Community 739 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Python Import Fix, Template 2: Python Import Sorting Fix, Template 3: Python Line Length Fix, Template 4: React Hook Dependency Fix, Template 5: TypeScript Unused Variable Fix

### Community 740 - "Who Command Enhancement"
Cohesion: 0.67
Nodes (3): Who Command Name Filtering, Who Command Enhancement, Who Command Implementation Tasks

### Community 741 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Python Import Fix, Template 2: Python Import Sorting Fix, Template 3: Python Line Length Fix, Template 4: React Hook Dependency Fix, Template 5: TypeScript Unused Variable Fix

### Community 742 - "test_quality_fragmentation_guard.py"
Cohesion: 0.12
Nodes (35): _build_python_call_usage_map(), _call_target_name(), Call, ChangedFile, Build a repo-wide call usage map from Python AST call sites., scan_changed_files(), _ChangedFile, _load_guard_module() (+27 more)

### Community 743 - "E2E Tests Playwright"
Cohesion: 0.22
Nodes (10): Playwright E2E Runtime Tests, ArkanWolfshade E2E Account, E2E Tests Playwright, Ithaqua E2E Account, mythos_e2e Database, Runtime Auth Isolation, Playwright storageState Session Sharing, E2E Login Timeout Issue (+2 more)

### Community 744 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 745 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 746 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Add Missing Type Imports, Template 2: Fix Function Signature, Template 3: Handle Optional Values, Template 4: Fix Type Narrowing, Template 5: Add Generic Type Parameters

### Community 747 - "Common Test Failure Categories"
Cohesion: 0.33
Nodes (6): 1. Database Test Failures, 2. Authentication Test Failures, 3. WebSocket Test Failures, 4. Game Logic Test Failures, 5. Integration Test Failures, Common Test Failure Categories

### Community 748 - "FAILURE PATTERN RECOGNITION"
Cohesion: 0.33
Nodes (6): A. Database-Related Failures, B. Authentication/Security Failures, C. WebSocket/Connection Failures, D. Game Logic Failures, E. Integration Test Failures, FAILURE PATTERN RECOGNITION

### Community 749 - "MUD Disconnect Grace Period & Rest Command: Industry Comparison"
Cohesion: 0.33
Nodes (5): 11. Missing Features from Other MUDs, Executive Summary, Features We're NOT Implementing (but exist elsewhere), MUD Disconnect Grace Period & Rest Command: Industry Comparison, Questions for Discussion

### Community 750 - "bonus_tags"
Cohesion: 0.33
Nodes (6): items, type, uniqueItems, minLength, type, bonus_tags

### Community 751 - "ComprehensiveLoggingMiddleware"
Cohesion: 0.10
Nodes (23): ComprehensiveLoggingMiddleware, Any, ASGIApp, Exception, Receive, Request, Scope, Send (+15 more)

### Community 752 - "items"
Cohesion: 0.33
Nodes (6): additionalProperties, properties, schedules, items, minItems, type

### Community 753 - "Bounded Contexts and Service Boundaries"
Cohesion: 0.67
Nodes (3): Bounded Contexts, Bounded Contexts and Service Boundaries, Service Boundaries

### Community 755 - "Implementation Details"
Cohesion: 0.33
Nodes (6): CircuitBreaker Manager, Database Operations, Enhanced CircuitBreaker Class, Implementation Details, Integration Examples, NATS Operations

### Community 757 - "ContainerRepository"
Cohesion: 0.10
Nodes (31): _container_data_to_dict(), ContainerRepository, Any, ContainerData, datetime, UUID, Update a container (async)., Get decayed containers (async). (+23 more)

### Community 758 - "ContainerRepository and ItemRepository: Review and Full Async Migration Plan"
Cohesion: 0.08
Nodes (23): 1.1 Current Architecture, 1.2 Impact of Current Wrappers, 1.3 Recommendation, 1. Review Summary, 2.1 Functions to Migrate, 2.2 Callers, 2. Scope of Migration, 3. Migration Options (+15 more)

### Community 759 - "magic_service_completion.py"
Cohesion: 0.18
Nodes (16): _is_heal_other_target(), MagicServiceCompletionMixin, Any, UUID, Casting completion flow for spellcasting. Mixin that handles completing a…, Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…, Parse target_id from casting state. Returns None if missing or invalid., Apply costs and queue spell for next combat round. Returns True if queued,… (+8 more)

### Community 760 - "Quest System Features"
Cohesion: 0.40
Nodes (6): Quest Design Guidelines, Quest Design Principles, Quest System Features, Event-Driven Quest Progression, Quest Goal Types, Declarative YAML Quest Config

### Community 761 - "Testing Guide"
Cohesion: 0.40
Nodes (6): Quick Start E2E Tests, E2E Test Server Quick Start, bcrypt PyO3 Fresh Session Limitation, Testing Guide, Pydantic Testing Patterns, Two-Tier Test Suite (make test)

### Community 762 - "test_combat_service.py"
Cohesion: 0.07
Nodes (57): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+49 more)

### Community 763 - "Documentation Updates - ConnectionManager Refactoring"
Cohesion: 0.08
Nodes (23): 1. **Accurate Reference Material**, ✅ 1. `REAL_TIME_ARCHITECTURE.md`, ✅ 2. `CONNECTION_MANAGER_ARCHITECTURE.md` (NEW), 2. **Reduced Confusion**, 3. **Better Onboarding**, ✅ 3. `WEBSOCKET_CODE_REVIEW.md`, ✅ 4. `DEVELOPMENT_AI.md`, 4. **Historical Record** (+15 more)

### Community 764 - "Domain Model Anemic Anti-Pattern Audit"
Cohesion: 0.08
Nodes (23): 1. Already Addressed (Prior Work), 2.1 Player Death Service – DP Decay, 2.2 Combat Turn Processor – “Can Act” Checks, 2.3 Combat HP Sync – Death Threshold Logic, 2.4 Combat Persistence Handler – Same Patterns, 2.5 Player Respawn Service – Stats Restoration, 2. High Priority – Domain Logic in Services, 3.1 Wearable Container Service – Capacity Checks (+15 more)

### Community 765 - "test_security_utils.py"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory. Args: filename: The filename…, Unit tests for security utilities. Tests path validation and file security…, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 766 - "MessageHandlerFactory"
Cohesion: 0.11
Nodes (16): MessageHandlerFactory, Register a new message handler. Args: message_type: The message type to handle…, Get a handler for the specified message type. Args: message_type: The message…, Handle a WebSocket message using the appropriate handler. Args: websocket: The…, Get a list of supported message types. Returns: List of supported message type…, Factory for creating and managing message handlers. This factory pattern…, Test MessageHandlerFactory.get_supported_message_types() returns list of types., Test global message_handler_factory instance exists. (+8 more)

### Community 767 - "TestNPCCombatLifecycle"
Cohesion: 0.11
Nodes (14): asyncio, fixture, Unit tests for NPC combat lifecycle. Tests the NPCCombatLifecycle class for…, Test _despawn_npc handles NPC not in active_npcs., Test suite for NPCCombatLifecycle class., Create a mock persistence layer., Create a NPCCombatLifecycle instance for testing., Test NPCCombatLifecycle initialization. (+6 more)

### Community 768 - "_format_room_posture_message"
Cohesion: 0.17
Nodes (15): _format_room_posture_message(), Create a descriptive room message for posture changes., Unit tests for position command helper functions. Tests helper functions in…, Test _format_room_posture_message() formats sitting message., Test _format_room_posture_message() formats lying message., Test _format_room_posture_message() formats standing from lying message., Test _format_room_posture_message() formats standing from sitting message., Test _format_room_posture_message() formats standing with no previous position. (+7 more)

### Community 769 - "._cleanup_player_mutes"
Cohesion: 0.12
Nodes (11): datetime, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired player mutes., Clean up expired channel mutes., Clean up expired global mutes., Clean up expired mutes from all storage. (+3 more)

### Community 770 - "container"
Cohesion: 0.33
Nodes (6): enabled, additionalProperties, description, required, type, container

### Community 771 - "Local Channel System"
Cohesion: 0.40
Nodes (5): Local Channel Sub-Zone Routing, Scenario 10 Local Channel Movement, Scenario 11 Local Channel Errors, Scenario 12 Local Channel Integration, Local Channel System

### Community 772 - "fix_suppression_alignment.py"
Cohesion: 0.16
Nodes (21): add_pylint_suppression(), add_ruff_suppression(), _apply_fixes_to_line(), fix_file(), _group_fixes_by_line(), main(), parse_alignment_report(), _parse_file_line_pattern() (+13 more)

### Community 773 - "identify_critical_code.py"
Cohesion: 0.15
Nodes (21): analyze_file(), analyze_function(), calculate_complexity(), calculate_priority(), check_file_keywords(), check_function_keywords(), main(), process_ast_functions() (+13 more)

### Community 774 - "AdminActionsLogger"
Cohesion: 0.08
Nodes (38): AdminActionsLogger, Any, datetime, Path, TypedDict, Admin actions logger for MythosMUD. This module provides comprehensive logging…, Log a general admin command action., Log permission check attempts. Args: player_name: Name of the player attempting… (+30 more)

### Community 775 - "Delight Techniques"
Cohesion: 0.11
Nodes (18): Appropriate to Context, Assess Delight Opportunities, Celebration Moments, Compound Over Time, Delight Amplifies, Never Blocks, Delight Principles, Delight Techniques, Easter Eggs & Hidden Delights (+10 more)

### Community 776 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 777 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 778 - "Asyncio Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.09
Nodes (21): 1. Blocking Synchronous Operations in Async Methods, 2. asyncio.run() Called from Context with Existing Event Loop, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Event Loop Change Detection May Not Handle All Cases, 6. Synchronous Database Operations in Async Context, 7. Missing Transaction Management in Batch Operations, 8. Connection Pool Size Configuration (+13 more)

### Community 779 - "_process_mortally_wounded_player"
Cohesion: 0.11
Nodes (25): _handle_player_death_threshold(), _player_in_active_combat(), _process_dead_players(), _process_mortally_wounded_player(), _process_mortally_wounded_players(), _process_mp_regeneration(), _process_passive_lucidity_flux(), _process_session_dp_decay_and_death() (+17 more)

### Community 780 - "StatisticsAggregator"
Cohesion: 0.12
Nodes (12): Analyze connection health distribution. Args: connection_metadata: Connection…, Analyze connection types. Args: connection_metadata: Connection metadata…, Analyze connection ages. Args: connection_metadata: Connection metadata now:…, Analyze session health. Args: connection_metadata: Connection metadata Returns:…, Calculate session health percentages. Args: session_health: Session health…, Build health trends statistics. Args: connection_ages: List of connection ages…, Build connection health statistics response. Args: total_connections: Total…, Aggregates statistics from connection management components. This class… (+4 more)

### Community 781 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test get_player_by_name returns None when player not found., Test save_player successfully saves player., Test get_player_by_user_id returns None when no players., Test soft_delete_player successfully soft deletes player., Test delete_player successfully deletes player., Test delete_player returns False when player not found., Test update_player_last_active successfully updates timestamp. (+9 more)

### Community 782 - "Ruff to Pylint Rule Mapping"
Cohesion: 0.09
Nodes (21): B008 - Function calls in argument defaults, B904 - Broad except, C901 - Too complex (PRIMARY COMPLEXITY CHECKER), Category Mappings, Complexity Checking, `docs/**/*` files: Multiple rules, E402 - Module level import not at top, E501 - Line too long (+13 more)

### Community 783 - "SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.09
Nodes (21): 1. SQL Injection Vulnerability in `update_player_stat_field()` - ✅ FIXED, 2. Missing Eager Loading for Relationships, 3. Mixed Database Access Patterns, 4. F-String SQL Construction (Even with Constants), 5. Missing Indexes on Foreign Keys, 6. Long-Lived Sessions, 7. Connection Pool Configuration, 8. Transaction Boundaries (+13 more)

### Community 784 - "test_players_quests.py"
Cohesion: 0.14
Nodes (18): mock_player_service(), mock_quest_service(), mock_request(), mock_user(), player_id(), asyncio, fixture, Unit tests for GET /api/players/{player_id}/quests (quest log). Tests… (+10 more)

### Community 785 - "MythosMUD Test Suite Modernization Plan"
Cohesion: 0.09
Nodes (21): Current State, Decision Framework: Uplift vs Greenfield Rewrite, Executive Summary, Goal, Greenfield Only If, Key Files, Known Risks, MythosMUD Test Suite Modernization Plan (+13 more)

### Community 786 - "Codebase Explorer Subagent"
Cohesion: 0.11
Nodes (17): Architecture Analysis, Architecture Analysis, Best Practices, Capabilities, Codebase Explorer Subagent, Dependency Research, Dependency Research, Example Scenarios (+9 more)

### Community 787 - "Implement Animations"
Cohesion: 0.11
Nodes (17): Accessibility, Assess Animation Opportunities, CSS Animations, Delight Moments, Entrance Animations, Feedback & Guidance, Implement Animations, JavaScript Animation (+9 more)

### Community 788 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (16 total, 14 thin omitted), Community 0 - "Open Mind Circle", Community 1 - "Campaign Materials", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 790 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (6 total, 4 thin omitted), Community 0 - "Solo Investigators", Community 1 - "Design & Authorship", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 791 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (4 total, 1 thin omitted), Community 0 - "Keeper Screen References", Community 1 - "Keeper Screen References (1)", Community 2 - "Keeper Screen References (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12) (+5 more)

### Community 792 - "Polish Systematically"
Cohesion: 0.11
Nodes (17): Code Quality, Color & Contrast, Content & Copy, Edge Cases & Error States, Final Verification, Forms & Inputs, Icons & Images, Interaction States (+9 more)

### Community 793 - "record_edited_file.py"
Cohesion: 0.15
Nodes (20): _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path(), Any (+12 more)

### Community 794 - "Command Handler Patterns"
Cohesion: 0.29
Nodes (7): Command Handler Patterns, Command Models Reference, Pydantic Command Models, Command Security Guide, Command Role-Based Access Control, Command Testing Guide, Command Test-Driven Development

### Community 795 - "database_config_helpers.py"
Cohesion: 0.07
Nodes (41): configure_pool_settings(), get_asyncpg_server_settings_for_database_url(), Database configuration helper functions. This module provides utility functions…, Build asyncpg ``server_settings`` so unqualified table names resolve like…, Configure pool settings based on database URL and config. When full config is…, _async_load_lucidity_rate_overrides(), build_override_key(), extract_lucidity_rate() (+33 more)

### Community 796 - "party_service.py"
Cohesion: 0.16
Nodes (16): PartyUpdated, Event fired when party membership or leadership changes. Emitted by…, Party service for MythosMUD. In-memory ephemeral party state: parties exist…, event_bus(), party_events(), party_service(), asyncio, fixture (+8 more)

### Community 797 - "ChatMessage"
Cohesion: 0.14
Nodes (37): ChatLogger, ChatMessage, Any, Represents a chat message with metadata., Convert message to dictionary for serialization., Log this chat message to the communications log., normalize_player_id(), ChatMessage (+29 more)

### Community 798 - "Playwright MCP Primary Testing Tool"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 799 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (3 total, 0 thin omitted), Community 0 - "Call of Cthulhu Stat Block; Chaosium Inc.", Community 1 - "Mythos Elements", Community 2 - "Mythos Elements (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12) (+5 more)

### Community 800 - "AsciiMapRenderer"
Cohesion: 0.15
Nodes (11): AsciiMapRenderer, Renders ASCII maps from room coordinate data. Supports multiple map styles…, Initialize the ASCII map renderer., Tests for _vertical_exit_char_between (|, v, ^)., Bidirectional vertical exit renders as a vertical bar., One-way south exit renders as a lowercase 'v'., One-way north exit renders as a caret., When there are no vertical exits, the helper returns None. (+3 more)

### Community 801 - "test_game_state_provider.py"
Cohesion: 0.09
Nodes (21): Unit tests for game state provider. Tests the GameStateProvider class., Test get_npcs_batch() returns NPC names., Test get_npcs_batch() returns empty dict for empty input., Test get_npcs_batch() handles None in NPC IDs list., Test _get_fallback_player_data() uses get_stats when available., Test _get_fallback_player_data() parses JSON stats string., Test _get_player_name_with_grace_periods() returns name with grace indicators., Test get_npcs_batch() resolves names from active NPCs. (+13 more)

### Community 802 - "test_metrics.py"
Cohesion: 0.04
Nodes (53): Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, metrics(), fixture, Unit tests for NATS Subject Manager Metrics. Tests the SubjectManagerMetrics…, Test record_build() stores build times., Test record_error() records pattern_not_found error. (+45 more)

### Community 803 - ".check_bidirectional_connections"
Cohesion: 0.11
Nodes (9): Get the opposite direction for bidirectional checking., Find rooms with no exits (dead ends). Args: room_database: Dictionary mapping…, Find rooms that reference themselves in exits. Args: room_database: Dictionary…, Generate minimap graph data for visualization. Args: room_database: Dictionary…, Build adjacency graph from room database. Args: room_database: Dictionary…, Get target room ID from exit data., Check if exit is marked as one-way., Extract zone and sub_zone from room data. Args: room_id: Room identifier… (+1 more)

### Community 804 - "test_lifespan_shutdown.py"
Cohesion: 0.13
Nodes (36): FastAPI, Application shutdown logic. This module handles graceful shutdown of all…, Shutdown event bus and clean up all service subscriptions., Handle graceful shutdown of all services., Shutdown and persist mythos chronicle state., Shutdown NATS message handler if present., Shutdown connection manager if present., Shutdown mythos tick scheduler if present. (+28 more)

### Community 805 - "CombatService"
Cohesion: 0.02
Nodes (145): NPCDiedEvent, Event fired when an NPC dies., combat_room_id_for_npc_spell(), Internal helpers for spell_effects.py (coercion, combat room lookup). Keeps the…, Active combat room_id for an NPC, if any., CombatResult, Result of a combat action., CombatCleanupHandler (+137 more)

### Community 806 - "Introduce Color Strategically"
Cohesion: 0.12
Nodes (16): Accent Color Application, Accessibility, Assess Color Opportunity, Background & Surfaces, Balance & Refinement, Borders & Accents, Cohesion, Data Visualization (+8 more)

### Community 807 - "test_occupants.py"
Cohesion: 0.18
Nodes (16): _format_occupants_result(), _get_event_handler_for_test_occupants(), _get_room_id_for_test_occupants(), Any, NPC test-occupants command for debugging occupant queries., Resolve application, player, room_id, and event handler for NPC test occupants…, Get room_id from args or current room. Returns (room_id, error_result)., Get event handler from app.state. Returns (event_handler, error_result). (+8 more)

### Community 808 - "audit_suppressions.py"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 809 - "fix_markdown_line_length.py"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 810 - "populate_npc_sample_data.py"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 811 - "NPCDied"
Cohesion: 0.03
Nodes (106): NPCDied, Event fired when an NPC dies. This event is triggered when an NPC's…, _entity_id_for_quest_offer(), _make_on_npc_died(), _make_on_player_entered(), _make_on_player_left(), _parse_player_id(), Any (+98 more)

### Community 812 - "test_users_current_user_logging.py"
Cohesion: 0.17
Nodes (19): DependsParam, get_current_user_with_logging(), Enhanced get_current_user with detailed logging., asyncio, Unit tests for get_current_user_with_logging wrapper., Test _get_current_user_with_logging when HTTPException is raised., Test _get_current_user_with_logging with successful authentication., Test _get_current_user_with_logging when generic Exception is raised. (+11 more)

### Community 813 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 814 - "test_connection_session_management.py"
Cohesion: 0.16
Nodes (15): _EmptyClientState, _meta(), ConnectionMetadata, UUID, Unit tests for connection session management. Tests the…, Test _is_websocket_connected() handles missing name attribute., Test _disconnect_all_connections_for_session() disconnects all connections., Test _disconnect_all_connections_for_session() handles partial disconnections. (+7 more)

### Community 815 - "Implement Adaptations"
Cohesion: 0.12
Nodes (15): Assess Adaptation Challenge, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Techniques, MANDATORY PREPARATION, Mobile Adaptation (Desktop → Mobile) (+7 more)

### Community 816 - "RoomRepository"
Cohesion: 0.14
Nodes (12): Repository for room persistence operations. Handles room caching and retrieval.…, Initialize the room repository. Args: room_cache: Shared room cache dictionary, Get a room by ID from cache. Args: room_id: Room identifier Returns: Room |…, List all cached rooms. Returns: list[Room]: List of all rooms Note: This is…, Save a room to the cache. Args: room: Room object to save Note: Rooms are…, Save multiple rooms to the cache. Args: rooms: List of room objects to save…, RoomRepository, Unit tests for RoomRepository. (+4 more)

### Community 817 - "Improve Copy Systematically"
Cohesion: 0.12
Nodes (15): Apply Clarity Principles, Assess Current Copy, Button & CTA Text, Confirmation Dialogs, Empty States, Error Messages, Form Labels & Instructions, Help Text & Tooltips (+7 more)

### Community 818 - "scripts"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 819 - "waitForMessage"
Cohesion: 0.27
Nodes (19): despawnArmitage(), DIALOGUE, ensureArmitagePresent(), listArmitageIds(), executeCommandWithoutRecovery(), getMessages(), waitForMessage(), abandonCollectNQuest() (+11 more)

### Community 820 - "compilerOptions"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 821 - "🎯 Test Categories"
Cohesion: 0.10
Nodes (20): 1. Application Startup & CORS (create_app), 2. WebSocket Connections, 3. Room Operations, 4. Container Operations, 5. Player Respawn, 6. Game Tick Processing, 7. Integration Tests, Complexity Refactoring Test Plan (+12 more)

### Community 822 - "NATS Medium-Priority Remediation Summary"
Cohesion: 0.10
Nodes (20): 1. Integrated Subject Manager into NATSMessageBroker, 2. Added Health Monitoring to NATSMessageBroker, 3. Documented Manual Acknowledgment Strategy, After Medium-Priority Fixes, Before Medium-Priority Fixes, Completed Medium-Priority Fixes ✅, Configuration Options, Event Callback Improvements (+12 more)

### Community 823 - "NATS Anti-Patterns Remediation Summary"
Cohesion: 0.10
Nodes (20): 1. Fixed Synchronous Operation in WebSocket Helpers, 2. Standardized Error Handling, 3. Added Message Validation to NATSMessageBroker, 4. Improved Batch Flush Error Recovery, 5. Improved Connection Pool Error Handling, After Remediation, Backward Compatibility, Before Remediation (+12 more)

### Community 825 - "Color & Contrast"
Cohesion: 0.12
Nodes (15): Alpha Is A Design Smell, Building Functional Palettes, Color & Contrast, Color Spaces: Use OKLCH, Contrast & Accessibility, Dangerous Color Combinations, Dark Mode Is Not Inverted Light Mode, Never Use Pure Gray or Pure Black (+7 more)

### Community 826 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)"
Cohesion: 0.15
Nodes (12): Communities (4 total, 2 thin omitted), Community 0 - "Kingsport Setting", Community 1 - "Solo Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11), Hyperedges (group relationships) (+4 more)

### Community 827 - "ConnectionPanel.tsx"
Cohesion: 0.50
Nodes (3): ConnectionPanel(), ConnectionPanelProps, localStorageMock

### Community 828 - "global-teardown.ts"
Cohesion: 0.40
Nodes (3): __dirname, __filename, projectRoot

### Community 829 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (3 total, 1 thin omitted), Community 0 - "Scenario Design", Community 1 - "Call of Cthulhu Roleplaying Game; Keeper Tips: C", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12), Hyperedges (group relationships) (+4 more)

### Community 830 - "ConnectionManager Refactoring Summary"
Cohesion: 0.10
Nodes (20): 1. Statistics & Monitoring (`realtime/monitoring/`), 2. Error Handling (`realtime/errors/`), 3. Health Monitoring (`realtime/monitoring/`), 4. Cleanup & Maintenance (`realtime/maintenance/`), 5. Game State Management (`realtime/integration/`), 6. Room Event Integration (`realtime/integration/`), 7. Message Broadcasting (`realtime/messaging/`), After (+12 more)

### Community 831 - "Phase 2: Categorize and Prioritize Mypy Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Mypy Issues

### Community 832 - "Phase 5: Fix Implementation Patterns"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL FIXES - Import and Name Errors, 🟡 HIGH PRIORITY FIXES - Type Errors, 🔵 LOW PRIORITY FIXES - Type Precision, 🟢 MEDIUM PRIORITY FIXES - Type Refinement, Phase 5: Fix Implementation Patterns

### Community 833 - "4. Common Fix Patterns"
Cohesion: 0.40
Nodes (5): 4. Common Fix Patterns, Authentication Test Patterns, Database Test Patterns, Game Logic Test Patterns, WebSocket Test Patterns

### Community 834 - "DML Migrations"
Cohesion: 0.40
Nodes (4): Dialogue definitions (#583), DML Migrations, Historical CSV files, Migration files

### Community 835 - "UX Writing"
Cohesion: 0.12
Nodes (16): Avoid Redundant Copy, Confirmation Dialogs: Use Sparingly, Consistency: The Terminology Problem, Don't Blame the User, Empty States Are Opportunities, Error Message Templates, Error Messages: The Formula, Form Instructions (+8 more)

### Community 836 - "LoggingPatternLinter"
Cohesion: 0.11
Nodes (15): FormattedValue, lint_file(), LoggingPatternLinter, main(), Call, Import, ImportFrom, Path (+7 more)

### Community 837 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 838 - "Arkham City (MOTD Zone)"
Cohesion: 0.18
Nodes (14): Arkham City Graph PNG, Arkham City PDF Map, Arkham City (MOTD Zone), Welcome to the Dreamlands, Innsmouth (MOTD Zone), Katmandu, MythosMUD Message of the Day, The Yellow Sign (+6 more)

### Community 839 - "UI/UX Considerations"
Cohesion: 0.40
Nodes (5): 1. Visual Distinction, 2. Panel Positioning, 3. Responsive Design, 4. Accessibility, UI/UX Considerations

### Community 840 - "MythosMUD Database Placement"
Cohesion: 0.12
Nodes (14): Allowed Paths Only, Data Types, Forbidden, MythosMUD Database Placement, PostgreSQL Access (Procedures and Functions), Reference, When Adding or Moving Persistence, Authority (+6 more)

### Community 841 - "CommandRateLimiter"
Cohesion: 0.10
Nodes (22): CommandRateLimiter, Any, datetime, Per-player command rate limiting. Prevents command flooding and denial-of-…, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate… (+14 more)

### Community 842 - "fix_markdown_common_issues.py"
Cohesion: 0.22
Nodes (14): fix_emphasis_as_heading(), fix_first_line_heading(), fix_link_fragments(), fix_markdown_file(), generate_anchor(), main(), parse_markdownlint_output(), Path (+6 more)

### Community 843 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (17 total, 16 thin omitted), Community 0 - "Scenario Handouts", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12), Hyperedges (group relationships), Import Cycles (+4 more)

### Community 844 - "3. Simplified CommandPanel"
Cohesion: 0.40
Nodes (5): 3. Simplified CommandPanel, CommandPanel Layout Structure, Features to Keep, Features to Remove, Simplified CommandPanel Interface

### Community 845 - "Implementation Phases"
Cohesion: 0.40
Nodes (5): Implementation Phases, Phase 1: Core Separation, Phase 2: Enhanced Features, Phase 3: Polish and Optimization, Phase 4: Testing and Refinement

### Community 846 - "handle_time_command"
Cohesion: 0.20
Nodes (15): handle_time_command(), Any, Handle the time command, exposing the current Mythos time and active holidays., asyncio, Unit tests for time command handlers. Tests the time command functionality., Test handle_time_command() handles holiday service errors., Test handle_time_command() handles missing holiday service., Test handle_time_command() returns time information. (+7 more)

### Community 847 - "SpellEffectType"
Cohesion: 0.04
Nodes (105): BaseModel, StrEnum, Valid target types for spells., Valid range types for spells., Valid effect types for spells., Material component required for casting a spell., SpellEffectType, SpellMaterial (+97 more)

### Community 848 - "extract_room_id_from_npc"
Cohesion: 0.12
Nodes (16): extract_room_id_from_npc(), Extract room ID from NPC instance with fallback logic. Args: npc_instance: The…, Test extract_room_id_from_npc() extracts from current_room., Test extract_room_id_from_npc() extracts from current_room_id., Test extract_room_id_from_npc() extracts from room_id., Test extract_room_id_from_npc() falls back to spawn_room_id., Literal 'unknown' on current_room must fall through to a real attr., Test extract_room_id_from_npc() returns 'unknown' when not found. (+8 more)

### Community 849 - "UpgradeImplementationPlan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 850 - "PlayerRespawnWrapper"
Cohesion: 0.19
Nodes (15): PlayerRespawnWrapper, Any, Respawn a delirious player by user ID. This method handles the complete…, Wrapper service for player respawn operations., Initialize with a persistence layer., Respawn a dead player by user ID. This method handles the complete respawn…, _dead_player(), asyncio (+7 more)

### Community 852 - "items"
Cohesion: 0.40
Nodes (5): items, type, pattern, type, bonus_tags

### Community 853 - "item_prototype.schema.json"
Cohesion: 0.40
Nodes (4): additionalProperties, $schema, title, type

### Community 854 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 855 - "2025_01_XX_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 856 - "2025_11_21_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 857 - "2025_11_25_normalize_container_schema.py"
Cohesion: 0.40
Nodes (4): downgrade(), Normalize container schema with proper relational structure., Revert to denormalized schema with items_json., upgrade()

### Community 858 - "2025_11_25_remove_get_container_contents_json_procedure.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove deprecated stored procedure., Restore deprecated stored procedure., upgrade()

### Community 859 - "2025_11_25_remove_items_json_column.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove items_json column from containers table., Restore items_json column (data will be empty)., upgrade()

### Community 860 - "2025_11_26_ensure_item_instance_foreign_keys.py"
Cohesion: 0.40
Nodes (4): downgrade(), Ensure foreign key constraints exist for item_instances., This migration only ensures constraints exist - no downgrade needed., upgrade()

### Community 861 - "2026_02_09_add_player_effects_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_effects table and indexes (ADR-009 effects system)., Drop player_effects table and indexes., upgrade()

### Community 862 - "ApplicationContainer Structure Analysis and Domain-Specific Split Proposal"
Cohesion: 0.10
Nodes (19): 1. Executive Summary, 2.1 Attribute Inventory by Domain, 2.2 Initialization Order and Dependencies, 2.3 Private Initializers and Helpers, 2.4 Public API and Consumers, 2. Current Structure Analysis, 3.1 Option A: Internal Bundles (Recommended), 3.2 Option B: Composed Sub-Containers (Alternative) (+11 more)

### Community 863 - "2026_02_18_add_player_skills_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_skills table if not exists (matches db/migrations/025)., Drop player_skills table., upgrade()

### Community 864 - "2026_02_18_add_profession_modifiers_columns.py"
Cohesion: 0.40
Nodes (4): downgrade(), Add stat_modifiers and skill_modifiers columns to professions table., Remove stat_modifiers and skill_modifiers columns from professions table., upgrade()

### Community 865 - "2026_02_19_add_quest_tables.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create quest_definitions, quest_instances, quest_offers tables., Drop quest tables (order matters for FKs)., upgrade()

### Community 866 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)"
Cohesion: 0.17
Nodes (11): Communities (2 total, 1 thin omitted), Community 0 - "Expedition Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 867 - "2026_02_19_seed_quest_leave_the_tutorial.py"
Cohesion: 0.40
Nodes (4): downgrade(), Insert leave_the_tutorial quest and quest_offers row., Remove seed quest and its offer., upgrade()

### Community 868 - "test_command_validator.py"
Cohesion: 0.03
Nodes (109): Unit tests for command validator., Test validate_command_length returns True for valid length., Test validate_command_length returns False for too long command., Test validate_command_length with custom max_length., Test validate_command_format returns True for valid command., Test validate_command_format returns False for empty command., Test validate_command_format returns False for suspicious command., Test validate_command_format returns False for too long command. (+101 more)

### Community 869 - "2026_02_26_add_arena_zone_type.py"
Cohesion: 0.40
Nodes (4): downgrade(), Allow zone_type 'arena' in zones CHECK., Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)., upgrade()

### Community 870 - "rename_players_to_population.py"
Cohesion: 0.40
Nodes (4): downgrade(), Rename columns from min_players/max_players to min_population/max_population., Revert column names back to min_players/max_players., upgrade()

### Community 871 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (3 total, 2 thin omitted), Community 0 - "Player Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 872 - "DomainError"
Cohesion: 0.40
Nodes (4): DomainError, Exception, Domain-specific exceptions for MythosMUD. These exceptions represent business…, Base exception for all domain errors.

### Community 875 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (8 total, 7 thin omitted), Community 0 - "Character Sheets", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 876 - "ConnectionErrorHandler"
Cohesion: 0.11
Nodes (26): ConnectionErrorHandler, Any, UUID, Handle WebSocket-specific errors. Args: player_id: The player's ID…, Handle authentication-related errors. Args: player_id: The player's ID…, Handle security violations. Args: player_id: The player's ID violation_type:…, Attempt to recover from an error state for a player. Args: player_id: The…, Get error handling statistics. Args: online_players: Online players dictionary… (+18 more)

### Community 877 - "test_look_item.py"
Cohesion: 0.09
Nodes (27): _get_item_description_from_prototype(), Get item description from prototype registry. Returns: Formatted result string…, Unit tests for item look functionality. Tests the helper functions for looking…, Test finding item in equipped items by name., Test finding item in equipped items when not found., Test getting item description from prototype., Test getting item description when prototype registry is None., Test getting item description when prototype_id is missing. (+19 more)

### Community 878 - "Changes by document"
Cohesion: 0.10
Nodes (19): Audit date, Changes by document, CLAUDE.md, docs/COMMAND_MODELS_REFERENCE.md, docs/CONFIGURATION_FILES_REFERENCE.md, docs/CONTAINER_SYSTEM_API_REFERENCE.md, docs/DATABASE_ACCESS_PATTERNS.md, docs/E2E_TESTING_GUIDE.md (+11 more)

### Community 879 - "Lizard Complexity Analysis Findings"
Cohesion: 0.10
Nodes (19): 1. `create_app` - CCN: 22, 2. `_load_rooms_with_coordinates` - CCN: 12, 3. `_parse_websocket_token` - CCN: 12, 4. `_ensure_coordinates_generated` - CCN: 11, 🔴 CRITICAL: Functions Exceeding Threshold (CCN > 10), Functions with CCN = 10, Functions with CCN = 9, Lizard Complexity Analysis Findings (+11 more)

### Community 880 - "Real-Time Architecture"
Cohesion: 0.50
Nodes (4): Real-Time Architecture, WebSocket and NATS Realtime Stack, Structured Concurrency Patterns, Structured Concurrency Task Tracking

### Community 882 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 883 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 884 - "MockEventClass"
Cohesion: 0.10
Nodes (20): MockEventClass, Test EventBus.inject() delivers event to subscribers (used by distributed…, Mock event class for testing., Test _handle_event_async() when no subscribers., Test _handle_event_async() handles sync subscriber errors., Test _handle_event_async() handles async subscriber errors., Test _handle_task_result_async() with successful task., Test _handle_task_result_async() with task that raises error. (+12 more)

### Community 886 - "2. Mythos Time Model Draft"
Cohesion: 0.10
Nodes (19): 1. Research Synthesis, 2. Mythos Time Model Draft, 3. Implementation Blueprint, 4. Client HUD Implementation, Calendar structure, Chronicle bootstrap, Configuration & persistence, Core services (+11 more)

### Community 887 - "🔄 COMMON SCENARIOS AND SOLUTIONS"
Cohesion: 0.50
Nodes (4): 🔄 COMMON SCENARIOS AND SOLUTIONS, Scenario 1: Third-Party Library Without Stubs, Scenario 2: Complex Union Types, Scenario 3: Recursive Types

### Community 888 - "🔍 DEBUGGING GUIDE"
Cohesion: 0.50
Nodes (4): 🔍 DEBUGGING GUIDE, If Mypy Command Fails, If Specific Issues Persist, Understanding Type Checker Behavior

### Community 889 - "🚀 OPTIMIZATION TIPS"
Cohesion: 0.50
Nodes (4): For Large Codebases, For Performance, 🚀 OPTIMIZATION TIPS, Type Annotation Strategies

### Community 890 - "MessageBroker"
Cohesion: 0.11
Nodes (12): Infrastructure layer for MythosMUD. This package contains abstractions for…, MessageBroker, Any, Protocol, Send a request and wait for a reply (request-reply pattern). Args: subject:…, Protocol defining the message broker interface. This abstract interface allows…, Connect to the message broker. Returns: bool: True if connection successful,…, Disconnect from the message broker. Closes all subscriptions and releases… (+4 more)

### Community 891 - "7. Common Test Failure Solutions"
Cohesion: 0.50
Nodes (4): 7. Common Test Failure Solutions, Authentication Test Issues, Database Connection Issues, WebSocket Test Issues

### Community 892 - "PostgresCursor"
Cohesion: 0.12
Nodes (12): PostgresCursor, cursor, PostgreSQL cursor wrapper for query result access., Get the number of rows affected., Test PostgresCursor class., Test PostgresCursor initialization., Test PostgresCursor.fetchone() with row., Test PostgresCursor.fetchone() with None. (+4 more)

### Community 893 - "NPCMovementIntegration"
Cohesion: 0.05
Nodes (44): NPCMovementIntegration, Room, Get room objects and validate they exist. Args: npc_id: ID of the NPC…, Update room occupancy by removing NPC from source and adding to destination.…, Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…, Move an NPC to a different room with full integration. This method provides…, Get the current room ID for an NPC. Args: npc_id: ID of the NPC Returns:…, Get list of NPC IDs in a room. Args: room_id: ID of the room Returns:… (+36 more)

### Community 894 - "9. Test Maintenance Best Practices"
Cohesion: 0.50
Nodes (4): 9. Test Maintenance Best Practices, Performance Considerations, Test Data Management, Test Isolation

### Community 895 - "10. Grace Period Persistence"
Cohesion: 0.50
Nodes (4): 10. Grace Period Persistence, Gap Analysis, Industry Practices, Our Plan

### Community 896 - "1. Disconnect Grace Period Duration"
Cohesion: 0.50
Nodes (4): 1. Disconnect Grace Period Duration, Gap Analysis, Industry Practices, Our Plan

### Community 897 - "2. Auto-Attack During Grace Period"
Cohesion: 0.50
Nodes (4): 2. Auto-Attack During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 898 - "3. Grace Period Visibility & Messaging"
Cohesion: 0.50
Nodes (4): 3. Grace Period Visibility & Messaging, Gap Analysis, Industry Practices, Our Plan

### Community 899 - "4. Rest/Quit Command During Combat"
Cohesion: 0.50
Nodes (4): 4. Rest/Quit Command During Combat, Gap Analysis, Industry Practices, Our Plan

### Community 900 - "5. Rest Command Countdown Duration"
Cohesion: 0.50
Nodes (4): 5. Rest Command Countdown Duration, Gap Analysis, Industry Practices, Our Plan

### Community 901 - "6. Rest Location (Inn/Hotel) Behavior"
Cohesion: 0.50
Nodes (4): 6. Rest Location (Inn/Hotel) Behavior, Gap Analysis, Industry Practices, Our Plan

### Community 902 - "7. Reconnection During Grace Period"
Cohesion: 0.50
Nodes (4): 7. Reconnection During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 903 - "combat_loader.py"
Cohesion: 0.07
Nodes (51): CombatCommandHandlerExtras, Optional services from the app container (keeps…, format_combat_status(), get_combat_target(), Any, Produce a human-readable combat status string. This helper is retained for…, Resolve a combat target by name. The current implementation is intentionally…, _app_from_request() (+43 more)

### Community 904 - "8. Grace Period After Intentional Disconnect"
Cohesion: 0.50
Nodes (4): 8. Grace Period After Intentional Disconnect, Gap Analysis, Industry Practices, Our Plan

### Community 905 - "9. Command Blocking During Grace Period"
Cohesion: 0.50
Nodes (4): 9. Command Blocking During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 906 - "Recommendations Summary"
Cohesion: 0.50
Nodes (4): High Priority Decisions, Low Priority (Future Considerations), Medium Priority Enhancements, Recommendations Summary

### Community 907 - "Code Graph Entry"
Cohesion: 0.50
Nodes (3): Code Graph Entry, Live exploration (preferred for "how does X work?"), Synced community wiki (read-only dump)

### Community 908 - "DML Migrations Apply Paths"
Cohesion: 0.50
Nodes (3): Agent rule, DML Migrations Apply Paths, Facts

### Community 909 - "Cosmic Horror.md"
Cohesion: 0.13
Nodes (9): Chaosium catalog notes, Cosmic Horror, Evocations of the Inner God, Lucidity, Pandora's Box (Pulp campaign), Pulp Sanity, The Hungry Void, Using Luck (Pulp) (+1 more)

### Community 910 - "GameConfig"
Cohesion: 0.14
Nodes (12): GameConfig, BaseSettings, field_validator, Game-specific configuration., Validate combat alert threshold., Validate combat performance threshold., Validate combat error threshold., Validate max connections is reasonable. (+4 more)

### Community 911 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 912 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 913 - "RetryConfig"
Cohesion: 0.12
Nodes (13): Get current retry configuration. Returns: Current RetryConfig AI: Useful for…, Configuration for retry behavior. Defines retry parameters for handling…, Calculate delay for a given attempt number. Uses exponential backoff capped at…, Initialize retry handler. Args: max_retries: Maximum number of retry attempts…, RetryConfig, Test RetryConfig.calculate_delay() with base delay., Test get_config() returns current RetryConfig., Test RetryConfig.calculate_delay() respects max_delay. (+5 more)

### Community 914 - "Spatial Design"
Cohesion: 0.13
Nodes (14): Cards Are Not Required, Container Queries, Depth & Elevation, Grid Systems, Hierarchy Through Multiple Dimensions, Name Tokens Semantically, Optical Adjustments, Spacing Systems (+6 more)

### Community 915 - "days"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, days

### Community 916 - "effects"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, effects

### Community 917 - "end_hour"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 918 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 919 - "exits"
Cohesion: 0.50
Nodes (4): type, additionalProperties, type, exits

### Community 920 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (1 total, 0 thin omitted), Community 0 - "Mythos Subjects", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12), Knowledge Gaps, Suggested Questions (+2 more)

### Community 921 - "Migration Considerations"
Cohesion: 0.50
Nodes (4): Backward Compatibility, Data Migration, Migration Considerations, Performance Impact

### Community 923 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Non-Functional Requirements, Success Criteria, User Experience Requirements

### Community 924 - "Risk Assessment"
Cohesion: 0.50
Nodes (4): Implementation Risks, Risk Assessment, Technical Risks, User Experience Risks

### Community 925 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Testing Strategy, Unit Tests, User Acceptance Tests

### Community 926 - "Phase 2: Database Layer Integration"
Cohesion: 0.50
Nodes (4): 2.1 Persistence Layer Protection, 2.2 Database Connection Protection, 2.3 Configuration, Phase 2: Database Layer Integration

### Community 927 - "Phase 3: Real-Time Communication Protection"
Cohesion: 0.50
Nodes (4): 3.1 NATS Integration, 3.2 WebSocket Protection, 3.3 Configuration, Phase 3: Real-Time Communication Protection

### Community 928 - "Phase 4: File System Operations"
Cohesion: 0.50
Nodes (4): 4.1 Room Loading Protection, 4.2 Player Data File Operations, 4.3 Configuration, Phase 4: File System Operations

### Community 929 - "Phase 6: Monitoring and Observability"
Cohesion: 0.50
Nodes (4): 6.1 Metrics Collection, 6.2 Health Check Endpoints, 6.3 Logging Integration, Phase 6: Monitoring and Observability

### Community 931 - "Future Enhancements"
Cohesion: 0.50
Nodes (4): Advanced Features, Document metadata, Future Enhancements, Integration Opportunities

### Community 932 - "Monitoring and Alerting"
Cohesion: 0.50
Nodes (4): Alerting Rules, Health Checks, Metrics to Monitor, Monitoring and Alerting

### Community 933 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Monitoring Requirements, Performance Requirements, Success Criteria

### Community 934 - "Shared JSON schemas"
Cohesion: 0.50
Nodes (4): alias_schema.json, emote_schema.json, Shared JSON schemas, unified_room_schema.json

### Community 935 - "init_npc_database.py"
Cohesion: 0.16
Nodes (17): _determine_database_init_flags(), get_npc_database_url(), get_npc_seed_data_from_postgresql(), init_database_schema(), _initialize_database_with_url(), main(), populate_npc_data(), _print_final_message() (+9 more)

### Community 936 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Load Tests, Testing Strategy, Unit Tests

### Community 937 - "fixtures/shared/__init__.py"
Cohesion: 0.13
Nodes (15): fake_clock(), make_player_dict(), make_user_dict(), Any, fixture, Shared fixtures and builders for all test tiers., Create a user dictionary for testing., Create a player dictionary for testing. (+7 more)

### Community 938 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (2 total, 2 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 939 - "BehaviorEngine"
Cohesion: 0.12
Nodes (13): BehaviorEngine, Deterministic behavior engine for NPCs. This engine evaluates rules based on…, Initialize the behavior engine., Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…, Get the behavior engine for this NPC., Test _evaluate_equality() handles boolean false., Test _evaluate_numeric_comparison() handles < operator., Test _evaluate_numeric_comparison() returns None for invalid format. (+5 more)

### Community 940 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Ambiguous Edges - Review These, Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 941 - "validate_admin_permission"
Cohesion: 0.20
Nodes (15): Any, Admin permission validation utilities for MythosMUD. This module provides…, Validate that a player has admin permissions. Args: player: Player object to…, validate_admin_permission(), _BrokenAdminPlayer, mock_admin_logger(), asyncio, fixture (+7 more)

### Community 942 - "Typography"
Cohesion: 0.13
Nodes (14): Accessibility Considerations, Choosing Distinctive Fonts, Classic Typography Principles, Fluid Type, Font Selection & Pairing, Modern Web Typography, Modular Scale & Hierarchy, OpenType Features (+6 more)

### Community 943 - "fix_markdown_code_block_style.py"
Cohesion: 0.24
Nodes (12): detect_code_language(), fix_code_block_style(), fix_markdown_file(), is_indented_code_line(), main(), parse_markdownlint_output(), Path, Parse markdownlint output to get files with MD046 issues. (+4 more)

### Community 944 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 945 - "holiday"
Cohesion: 0.50
Nodes (4): $defs, holiday, additionalProperties, type

### Community 946 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 947 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 948 - "factory.py"
Cohesion: 0.08
Nodes (35): main(), Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., _sanitize_token_examples(), _apply_cors_env_overrides(), _configure_cors(), CORSConfigDict, CORSConfigOverrides (+27 more)

### Community 949 - "run_quality_fragmentation_guard.py"
Cohesion: 0.31
Nodes (12): _argv_char_len(), _build_guard_command(), _changed_files_between(), _git_executable(), _is_graphify_path(), _local_changed_files(), main(), Path (+4 more)

### Community 950 - "long_description"
Cohesion: 0.50
Nodes (4): maxLength, minLength, type, long_description

### Community 951 - "prototype_id"
Cohesion: 0.50
Nodes (4): prototype_id, maxLength, minLength, type

### Community 952 - "short_description"
Cohesion: 0.50
Nodes (4): short_description, maxLength, minLength, type

### Community 954 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 955 - "Enhanced Logging Quick Reference"
Cohesion: 0.11
Nodes (18): API Requests, Clear Context, Common Patterns, Context Binding, 🚨 CRITICAL: DO NOT USE, Database Operations, Enhanced Logging Quick Reference, Errors with Context (+10 more)

### Community 956 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 957 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 958 - "NumPy Code Review - MythosMUD Codebase"
Cohesion: 0.11
Nodes (18): Code Quality Improvements Achieved, Completed Actions, Conclusion, Executive Summary, Findings, 🟡 HIGH PRIORITY: Manual Statistical Calculations, ✅ Implementation Status, Issue 1: Performance Monitor - Manual Statistics (+10 more)

### Community 959 - "start_server.ps1"
Cohesion: 0.50
Nodes (4): Default Server Port 54768, start_local.ps1, start_server.ps1, stop_server.ps1

### Community 960 - "MythosMUD Code Quality Targets for AI"
Cohesion: 0.13
Nodes (14): `__all__` for public modules, As You Touch, Client return types (TypeScript), Complexity policy, Docstrings (D), High Priority, Medium Priority, MythosMUD Code Quality Targets for AI (+6 more)

### Community 961 - "Python Model Updates Required for Migration 019"
Cohesion: 0.11
Nodes (18): 1. Import BigInteger, 2. Files Requiring Updates, Impact Assessment, Integer → BigInteger, Low Risk Changes, No Breaking Changes Expected, Overview, Python Model Updates Required for Migration 019 (+10 more)

### Community 962 - "Skill: Create a New Worktree for a Task"
Cohesion: 0.13
Nodes (14): Canonical Layout (Summary), MythosMUD Worktree Workflow, Preconditions and Safety, Skill: Clean Up a Completed or Stale Worktree, Skill: Create a New Worktree for a Task, Step 1 — Gather Task Metadata, Step 2 — Derive Names and Paths, Step 3 — Ensure Canonical Repo Context (+6 more)

### Community 963 - "Transaction Boundaries Audit"
Cohesion: 0.11
Nodes (18): ✅ AsyncPersistenceLayer (Async), Audit Date, Audited Operations, Current State: ✅ GOOD, Future Improvements, Multi-Step Operations, Notes, Pattern 1: Connection Context Manager (PersistenceLayer) (+10 more)

### Community 964 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 965 - "CircuitState"
Cohesion: 0.14
Nodes (13): CircuitState, Enum, Circuit breaker pattern for NATS message processing. Implements three-state…, Circuit breaker states. - CLOSED: Normal operation, requests pass through -…, Get current circuit state. Returns: Current CircuitState AI: For monitoring and…, Test _on_success() increments success count in HALF_OPEN state., Test _on_failure() opens circuit at threshold., Test _should_attempt_reset() returns False before timeout. (+5 more)

### Community 966 - "asyncio"
Cohesion: 0.09
Nodes (22): asyncio, Test EventBus.publish() queues or processes event., Test EventBus.shutdown() stops processing., Test EventBus.shutdown() is idempotent., Test _stop_processing() when not running., Test EventBus.shutdown() automatically cleans up all service subscriptions., Test multiple services subscribing to the same event type., Test that service shutdown removes all subscribers for that service. This test… (+14 more)

### Community 967 - "test_validate_secure_path_path_traversal_commonpath"
Cohesion: 0.33
Nodes (4): Test validate_secure_path normalizes backslashes., Test validate_secure_path detects path traversal via commonpath check., test_validate_secure_path_path_traversal_commonpath(), test_validate_secure_path_with_backslash()

### Community 968 - "test_asyncio_run_guardrails.py"
Cohesion: 0.50
Nodes (3): Test that server library code does not use asyncio.run() (AnyIO best practice).…, Assert server/ has no asyncio.run() in library code (use anyio.run() at entry…, test_no_asyncio_run_in_server_library_code()

### Community 969 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 970 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 971 - "name"
Cohesion: 0.50
Nodes (4): description, minLength, type, name

### Community 972 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 973 - "fix_file"
Cohesion: 0.18
Nodes (16): fix_blanks_around_fences(), fix_blanks_around_headings(), fix_blanks_around_lists(), fix_fence_language(), fix_file(), fix_line_length(), fix_trailing_punctuation_in_headings(), main() (+8 more)

### Community 974 - "jackson_linter.py"
Cohesion: 0.20
Nodes (16): collect_json_files(), _file_appears_binary_or_terminal_output(), _first_fallback_encoding_that_parses(), _is_vscode_jsonc_settings(), main(), Path, Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1…, VS Code allows JSON with Comments in settings.json; stdlib json cannot parse it. (+8 more)

### Community 975 - "RoomFilenameMigrator"
Cohesion: 0.19
Nodes (10): main(), Path, Update the room ID in the JSON file to match new naming schema., Execute the migration., Handles migration of room filenames from old to new schema., Initialize the migrator., Parse old filename format to extract components., Discover all room files that need migration. (+2 more)

### Community 976 - ".call"
Cohesion: 0.16
Nodes (8): Any, Handle successful function call. Updates state based on current circuit state:…, Handle failed function call. Updates state based on failure count: - Increments…, Check if enough time has passed to attempt circuit reset. Returns: True if…, Calculate seconds until circuit can attempt reset. Returns: Seconds until retry…, Transition circuit to new state. Args: new_state: State to transition to AI:…, Get circuit breaker statistics. Returns: Dictionary with circuit breaker…, Execute function through circuit breaker. Enforces circuit breaker logic: -…

### Community 977 - "RetryableMessage"
Cohesion: 0.13
Nodes (14): Exception, Determine if a message should be retried. Args: message: Message that failed…, Message that can be retried with tracking metadata. Stores message data along…, RetryableMessage, Test should_retry() returns False when at max retries., Test should_retry() returns False when over max retries., Test retry_async() requests backoff delay (sleep called with positive delay)., Test retry_async() handles zero delay. (+6 more)

### Community 978 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 979 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 980 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 981 - "npc_spawn_modifier"
Cohesion: 0.50
Nodes (4): description, minimum, type, npc_spawn_modifier

### Community 982 - "special_rules"
Cohesion: 0.50
Nodes (4): special_rules, additionalProperties, description, type

### Community 983 - "Client Security and Privacy Policies"
Cohesion: 0.67
Nodes (3): Client Security and Privacy Policies, DOMPurify Sanitization, WebSocket Subprotocol Auth

### Community 990 - "Expansion Backlog (Raw)"
Cohesion: 0.67
Nodes (3): Delta Green, Expansion Backlog (Raw), Things and Notes to Expand On

### Community 991 - "1774539086359-useMythosAppState.ts"
Cohesion: 0.11
Nodes (29): AuthSlice, authSliceReducer(), CreationSlice, creationSliceReducer(), INITIAL_AUTH_SLICE, INITIAL_CREATION_SLICE, PendingSkillsPayload, resolveNextState() (+21 more)

### Community 992 - "🚨 AI ERROR HANDLING"
Cohesion: 0.67
Nodes (3): 🚨 AI ERROR HANDLING, If Multiple Categories Have Issues, If Mypy Still Fails After Fixes

### Community 993 - "Event Ownership Matrix"
Cohesion: 0.50
Nodes (4): Event Ownership Matrix, Event Publishing Layers, Event Subscription Cleanup Patterns, Event Subscription service_id Tracking

### Community 994 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 995 - "NPCCacheService"
Cohesion: 0.23
Nodes (8): NPCCacheService, Service for caching NPC definitions and spawn rules., Invalidate all NPC definition caches., Invalidate all NPC spawn rule caches., _NpcDef, asyncio, _SpawnRule, TestNPCCacheService

### Community 996 - "Graphify Code Graph"
Cohesion: 0.50
Nodes (3): Chaosium pack graphs (external), Graphify Code Graph, Relationship to this vault

### Community 997 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)"
Cohesion: 0.20
Nodes (9): Communities (1 total, 1 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12), Knowledge Gaps, Suggested Questions, Summary (+1 more)

### Community 998 - "Chaosium CoC Catalog"
Cohesion: 0.20
Nodes (9): Chaosium CoC Catalog, Creature / motif families (adaptation stubs), How to use, MythosMUD adaptation notes, Ongoing ops, Tier A (full or batch-promoted), Tier B (source-only), Tier C (+1 more)

### Community 999 - "plane"
Cohesion: 0.67
Nodes (3): minLength, type, plane

### Community 1000 - "AI Development Workflow"
Cohesion: 0.67
Nodes (3): AI Command Development Workflow, Cursor AI Tooling, AI Development Workflow

### Community 1001 - "Architecture Overview"
Cohesion: 0.67
Nodes (3): Architecture Overview, CircuitBreaker States, Integration Points

### Community 1002 - "Any"
Cohesion: 0.20
Nodes (4): Any, Return the keys of the row dictionary. Returns: dict_keys: The keys of the row…, Execute a query and return a cursor. Args: query: SQL query with PostgreSQL %s…, Get a cursor from the underlying connection. This method provides direct access…

### Community 1003 - "setup.ts"
Cohesion: 0.16
Nodes (6): createDomPurifyTestWindow(), installDomPurifyTestWindow(), defaultFetchMock, installLocalStorageShim(), isUsableStorage(), peekExistingLocalStorage()

### Community 1004 - "Frontend Design Skill"
Cohesion: 0.13
Nodes (16): Tailwind CSS Anti-Pattern Remediation, Adapt Skill, Animate Skill, Arrange Skill, Audit Skill, Bolder Skill, Clarify Skill, Colorize Skill (+8 more)

### Community 1005 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1007 - "npc_instances_api.py"
Cohesion: 0.06
Nodes (63): despawn_npc_instance(), get_npc_instances(), get_npc_stats(), move_npc_instance(), Any, delete, get, NPCSpawnRequest (+55 more)

### Community 1008 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test _execute_command_handler successfully executes handler., Test process_command successfully processes command string., Test _execute_command_handler handles handler returning non-dict., Test process_validated_command successfully routes to handler., Test process_validated_command handles unknown command type., Test process_validated_command handles handler errors., Test process_validated_command handles logging errors gracefully. (+7 more)

### Community 1009 - "test_aggressive_mob_npc.py"
Cohesion: 0.25
Nodes (14): _make_aggro(), asyncio, Unit tests for AggressiveMobNPC. Regression test: aggressive mobs must have…, test_attack_target_error_returns_false(), test_attack_target_fallback_publishes_event(), test_attack_via_combat_integration_none_when_missing(), test_attack_via_create_task_with_running_loop(), test_attack_via_dropped_without_loop_or_bus() (+6 more)

### Community 1010 - "_as_ws"
Cohesion: 0.16
Nodes (12): _as_ws(), _FakeClientState, _FakeWebSocket, WebSocket, Test _disconnect_connection_for_session() successfully disconnects connection., Test _disconnect_connection_for_session() handles disconnected websocket., Test _disconnect_connection_for_session() handles close error., Test handle_new_game_session_impl() successfully handles new session. (+4 more)

### Community 1011 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test MessageHandlerFactory.handle_message() successfully handles message., Test MessageHandlerFactory.handle_message() sends error for unknown type., Test MessageHandlerFactory.handle_message() handles message with no type., Test ClientErrorReportMessageHandler logs via logger.error., Test CommandMessageHandler.handle() calls handle_command_message., Test ChatMessageHandler.handle() calls handle_chat_message., Test PingMessageHandler.handle() calls handle_ping_message. (+7 more)

### Community 1012 - "fix_markdown_file"
Cohesion: 0.36
Nodes (8): fix_markdown_file(), fix_multiple_blanks(), main(), parse_markdownlint_output(), Path, Fix multiple consecutive blank lines (MD012). Returns: (new_content,…, Parse markdownlint output to get files with MD012 issues., Fix multiple blank lines in a single markdown file. Returns: (changed,…

### Community 1015 - "analyze_coverage_gaps.py"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and…, Write critical files below threshold section. (+7 more)

### Community 1016 - "_apply_arena_seed_patch.py"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 1019 - "test_shutdown_process_termination.py"
Cohesion: 0.08
Nodes (24): _find_uvicorn_processes(), Any, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available., _terminate_child_processes(), _terminate_uvicorn_processes() (+16 more)

### Community 1021 - "apply_communication_dampening"
Cohesion: 0.17
Nodes (21): apply_communication_dampening(), _apply_receiver_effects(), _apply_sender_effects(), DampeningResult, _maybe_muffle_fractured_message(), _maybe_scramble_deranged_message(), TypedDict, Communication dampening utilities for lucidity system. Implements communication… (+13 more)

### Community 1028 - "Aggro and Threat System Design"
Cohesion: 0.50
Nodes (4): Aggro and Threat System Design, Hate List, Aggro Stability Margin, UpdateAggro

### Community 1031 - "NPC Startup Duplication Analysis"
Cohesion: 0.33
Nodes (6): NPC Duplication Bug Fix Plan, NPC Population Field Rename, NPC Lifecycle Manager, NPC Population Controller, NPC Startup Duplication Analysis, NPC Startup Service

### Community 1032 - "Gladiator Ring (Arena) Implementation Plan"
Cohesion: 0.11
Nodes (16): Gladiator Ring (Arena) — Implementation Todos, Phase 1: Schema and world data (Codebase Explorer for DML/schema pattern discovery) — DONE, Phase 2: Tutorial exit and respawn (main agent), Phase 3: NPC startup — also spawn in arena (main agent) — DONE, Phase 4: Tests and validation (main agent / Test Suite Analyzer) — DONE, Plan frontmatter todos (for Cursor plan file), Subagent usage, Todos (detailed) (+8 more)

### Community 1033 - "fixture"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request object., Create a mock persistence layer., Create a mock connection manager. (+1 more)

### Community 1038 - "Codacy configuration"
Cohesion: 0.13
Nodes (15): Bandit configuration, Bandit B101 B105 B106 test skips, Codacy configuration, Enforced coverage gates, Codacy exclude_paths, Lizard CCN and NLOC thresholds, Grype SCA exclude paths, F-string logging anti-pattern detector (+7 more)

### Community 1040 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test should_retry() returns True when under max retries., Test retry_with_backoff() succeeds on first attempt., Test retry_with_backoff() succeeds after retries., Test retry_with_backoff() returns False when all retries fail., Test retry_with_backoff() doesn't sleep after last attempt., Test retry_with_backoff() preserves exception type., Test retry_with_backoff() handles different error types. (+7 more)

### Community 1041 - "test_ascii_map_renderer_exits.py"
Cohesion: 0.13
Nodes (11): fixture, Unit tests for AsciiMapRenderer exit character and exit resolution. Guards…, Tests for _get_exit_entries_for_room., Valid exits for a room produce one entry with correct direction and coordinates., Exits whose targets are missing are skipped when building exit entries., Viewport bounds: return None when next cell is outside viewport., Returns None when the next horizontal cell lies at or beyond the viewport's…, Return a fresh AsciiMapRenderer instance for each test. (+3 more)

### Community 1042 - ".measure_model_deserialization"
Cohesion: 0.20
Nodes (8): BaseModel, Measure memory usage for model deserialization. Args: model_class: The Pydantic…, Start memory profiling., Stop memory profiling., Get current memory usage in bytes., Get memory delta from baseline., Measure memory usage for model instantiation. Args: model_class: The Pydantic…, Measure memory usage for model serialization. Args: instances: List of model…

### Community 1050 - "load_motd"
Cohesion: 0.23
Nodes (11): Unit tests for motd_loader utilities. Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+3 more)

### Community 1051 - "Generate Comprehensive Report"
Cohesion: 0.14
Nodes (13): Anti-Patterns Verdict, Critical Issues, Detailed Findings by Severity, Diagnostic Scan, Executive Summary, Generate Comprehensive Report, High-Severity Issues, Low-Severity Issues (+5 more)

### Community 1052 - "is_safe_filename"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters). Args:…, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 1054 - "Optimization Strategy"
Cohesion: 0.14
Nodes (13): Animation Performance, Assess Performance Issues, Core Web Vitals Optimization, Cumulative Layout Shift (CLS < 0.1), First Input Delay (FID < 100ms) / INP (< 200ms), Largest Contentful Paint (LCP < 2.5s), Loading Performance, Network Optimization (+5 more)

### Community 1055 - "test_utility_commands_whoami.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for utility command handlers. Tests the whoami command functionality., Test handle_whoami_command() returns player information., Test handle_whoami_command() handles missing persistence., Test handle_whoami_command() handles player not found., test_handle_whoami_command(), test_handle_whoami_command_no_persistence(), test_handle_whoami_command_player_not_found()

### Community 1056 - "_validate_app_state_for_status_effects"
Cohesion: 0.14
Nodes (14): Validate app state has required components for status effect processing.…, _validate_app_state_for_status_effects(), Test _validate_app_state_for_status_effects returns True when all required…, Test _validate_app_state_for_status_effects returns False when container is…, Test _validate_app_state_for_status_effects returns False when…, Test _validate_app_state_for_status_effects returns False when no container., Test _validate_app_state_for_status_effects returns False when no…, Test _validate_app_state_for_status_effects returns False when no… (+6 more)

### Community 1058 - "_NPCCombatIntegrationValidationDeps"
Cohesion: 0.10
Nodes (18): _coerce_xp_mapping_value(), _NPCCombatIntegrationValidationDeps, Protocol, UUID, End any active combat that includes this player when room validation fails., Convert string IDs to UUIDs and set up XP mappings., Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,…, Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1). (+10 more)

### Community 1065 - "✅ Async Remediation Complete"
Cohesion: 0.12
Nodes (16): Adjusts spectacles with scholarly satisfaction, ✅ Async Remediation Complete, Critical Fixes Implemented (4 Code Changes), December 3, 2025, Documentation Created (5 Documents, ~2,500 lines), 📚 Key Documents, 🎓 Key Takeaway, Mission Accomplished (+8 more)

### Community 1066 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 1067 - "Phase 2 Async Persistence Migration - Status Update"
Cohesion: 0.12
Nodes (16): adjusts spectacles and awaits instruction, Awaiting Your Direction, Professor Wolfshade, ✅ Completed Today, Critical Phase 1 Fixes (100% Complete), 🚦 Current Status, 🎯 Decision Point, 📊 Effort Analysis, My Recommendation (+8 more)

### Community 1068 - "parse_shutdown_parameters"
Cohesion: 0.14
Nodes (14): parse_shutdown_parameters(), Parse shutdown command parameters. Args: command_data: Command data dictionary…, Test parse_shutdown_parameters() with no args defaults to 10 seconds., Test parse_shutdown_parameters() with cancel action., Test parse_shutdown_parameters() with seconds., Test parse_shutdown_parameters() with negative seconds., Test parse_shutdown_parameters() with zero seconds., Test parse_shutdown_parameters() with invalid string. (+6 more)

### Community 1069 - "Quick Start: Running E2E Tests"
Cohesion: 0.12
Nodes (16): Expected Results, Method A: Use the E2E startup script (Simplest), Method B: Manual startup (More control), Next Actions, Prerequisites ✅, Problem: "element(s) not found" errors, Problem: Login failed (500), Problem: Server won't start (+8 more)

### Community 1070 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test get_players_batch() handles player not found., Test convert_room_uuids_to_names() converts UUIDs to names., Test send_initial_game_state() sends initial state., Test convert_room_uuids_to_names() with empty room_data., Test convert_room_uuids_to_names() when player not found., Test _process_occupants_with_grace_periods() splits players and NPCs., Test _get_player_data_for_client() uses PlayerService when available. (+11 more)

### Community 1071 - "Implementation Phases"
Cohesion: 0.12
Nodes (17): Deliverables, Deliverables, Deliverables, Deliverables, Deliverables, Implementation Phases, Phase 0: Foundation (Week 1) - 40 hours, Phase 1: Fix Failing Tests (Week 1-2) - 40 hours (+9 more)

### Community 1072 - "process_room_files"
Cohesion: 0.21
Nodes (14): load_room_file(), main(), process_room_files(), Path, Load a room file safely., Save a room file safely., Convert room ID to lowercase., Convert filename to lowercase. (+6 more)

### Community 1073 - "validate_codacy_coverage_gate.py"
Cohesion: 0.25
Nodes (14): cobertura_has_server_sources(), cobertura_root_line_rate(), lcov_aggregate_hits(), main(), _parse_cobertura_xml(), Path, Parse Cobertura XML with defusedxml (lazy import: LCOV-only runs skip this…, Return root line-rate from Cobertura XML (0.0--1.0). (+6 more)

### Community 1074 - "test_check_no_production_assert.py"
Cohesion: 0.18
Nodes (15): _load_checker(), _NoProductionAssertModule, Path, Protocol, Tests for scripts/check_no_production_assert.py., Verify no-production-assert hook targets server code and excludes tests., Public surface of check_no_production_assert loaded via importlib., test_find_assert_line_numbers_detects_assert() (+7 more)

### Community 1075 - "._handle_exception"
Cohesion: 0.20
Nodes (10): Exception, Receive, Request, Response, Scope, Send, ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…, Handle an exception and send a standardized error response. Args: scope: ASGI… (+2 more)

### Community 1076 - "CacheManager"
Cohesion: 0.11
Nodes (11): CacheManager, Any, Get cache statistics. Returns: Dictionary containing cache statistics, String representation of the cache., Centralized cache manager for MythosMUD server. Manages multiple LRU caches for…, Initialize the cache manager., Initialize default caches with appropriate configurations., Get a cache by name. Args: name: The name of the cache Returns: The cache… (+3 more)

### Community 1077 - "messageHandlers.ts"
Cohesion: 0.16
Nodes (14): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+6 more)

### Community 1078 - "_find_item_in_equipped"
Cohesion: 0.11
Nodes (24): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _handle_item_look(), Any, Item look functionality for MythosMUD. This module handles looking at items,…, Find an item in equipped items by name or prototype_id. Args: equipped:…, Check if item found in a location and return formatted result. (+16 more)

### Community 1079 - "Any"
Cohesion: 0.11
Nodes (13): Any, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string…, Evaluate boolean conditions and variable lookups. Args: condition: Condition…, Evaluate a condition string against context. Args: condition: Condition string… (+5 more)

### Community 1080 - "test_admin_auth_service.py"
Cohesion: 0.02
Nodes (124): AdminAction, AdminAuthService, AdminRole, AdminSession, _HasId, _HasIsAdmin, _HasIsSuperuser, _HasUsername (+116 more)

### Community 1081 - "test_player_spell_repository.py"
Cohesion: 0.27
Nodes (16): _mock_session_with_rows(), asyncio, fixture, Unit tests for PlayerSpellRepository., repo(), _spell_row(), test_get_player_spell_found(), test_get_player_spell_missing() (+8 more)

### Community 1084 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test handling item look when item is in room drops., Test handling item look when item is in inventory., Test handling item look when item is equipped., Test handling item look when item not found., Test handling item look with look_in flag skips equipped items., Test trying implicit lookup when item is in room drops., Test trying implicit lookup when item not found. (+17 more)

### Community 1085 - "extract_definition_id_from_npc"
Cohesion: 0.14
Nodes (14): extract_definition_id_from_npc(), Extract definition ID from NPC instance or lifecycle record. Args:…, Test extract_definition_id_from_npc() extracts from NPC instance., Test extract_definition_id_from_npc() returns None for non-int., Test extract_definition_id_from_npc() extracts from lifecycle manager., Test extract_definition_id_from_npc() returns None when no lifecycle record., Test extract_definition_id_from_npc() returns None when record has no…, Test extract_definition_id_from_npc() returns None when no manager and no… (+6 more)

### Community 1086 - "fixture"
Cohesion: 0.29
Nodes (4): fixture, Create a mock psycopg2 connection., Create a mock psycopg2 cursor., Create a mock psycopg2 cursor.

### Community 1087 - "AGENTS.md agent instructions"
Cohesion: 0.08
Nodes (24): AGENTS.md agent instructions, COPPA compliance requirements, Obsidian LLM wiki permanent memory, One server only rule, PostgreSQL procedures/functions access, Server authority rule, CLAUDE.md agent router, Contributor Covenant Code of Conduct (+16 more)

### Community 1088 - "handle_new_game_session_impl"
Cohesion: 0.23
Nodes (14): _cleanup_old_session_tracking(), _cleanup_player_data_for_session(), _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), handle_new_game_session_impl(), Protocol, UUID, Disconnect all connections for a new game session. Args: connection_ids: List… (+6 more)

### Community 1089 - "Architecture Decision Records Index"
Cohesion: 0.20
Nodes (10): ADR-013 Pydantic BaseSettings Configuration, ADR-014 NATS Circuit Breaker and DLQ, Dead Letter Queue, db/procedures Stored Functions, ADR-015 PostgreSQL Procedures Migration, ADR-016 Aggro Threat Management, Room-Based Combat Aggro, ADR-017 AST Console Pruning (+2 more)

### Community 1090 - "Fixture Optimization Complete"
Cohesion: 0.67
Nodes (3): E2E Testing Setup Status, Fixture Optimization Complete, Test Suite Post-Merge Refactoring

### Community 1091 - "_find_item_in_inventory"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id. Args: inventory: List…, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 1092 - "test_invite_schemas.py"
Cohesion: 0.18
Nodes (13): InviteUpdate, Schema for updating invite data., Unit tests for invite schemas. Tests the Pydantic models in invite.py module., Test InviteUpdate can be instantiated with all fields optional., Test InviteUpdate validates invite_code length when provided., Test InviteRead can be instantiated., Test InviteRead with used_by_user_id., Test InviteUpdate can be instantiated with optional fields. (+5 more)

### Community 1093 - "check_no_production_assert.py"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 1094 - "executeCommand"
Cohesion: 0.10
Nodes (34): expectWhoListingOnPage(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), ensureIthaquaInFoyer() (+26 more)

### Community 1095 - "overrides"
Cohesion: 0.11
Nodes (18): overrides, @asyncapi/generator, @asyncapi/generator-components, @asyncapi/generator-helpers, @asyncapi/specs, fast-uri, flatted, glob (+10 more)

### Community 1096 - "test_command_service.py"
Cohesion: 0.14
Nodes (13): Unit tests for command service. Tests the CommandService class which handles…, Test _prepare_command_data creates basic command_data dict., Test _extract_parsed_fields extracts basic fields., Test _extract_parsed_fields handles missing attributes gracefully., Test register_command_handler adds new handler., Test register_command_handler overwrites existing handler., Test _log_model_dump_result logs model dump., test_extract_parsed_fields_basic() (+5 more)

### Community 1097 - "test_performance_tracker.py"
Cohesion: 0.14
Nodes (13): Unit tests for PerformanceTracker., Samples beyond max_samples are trimmed from the front., Empty tracker returns zero averages., get_stats computes min/max/avg for recorded metrics., Only websocket connection types count toward websocket stats., Exception during stats calculation returns error payload., Recording events updates totals and sample lists., test_get_stats_calculates_averages() (+5 more)

### Community 1098 - "Cursor Workflows"
Cohesion: 0.22
Nodes (9): Cursor Agent CLI, Cursor CLI, Cursor Hooks, Cursor Lifecycle Hooks, Cursor Setup Guide, Cursor Subagents, Built-in Explore Bash Browser Subagents, Cursor Workflows (+1 more)

### Community 1099 - "NPCOccupantProcessor"
Cohesion: 0.11
Nodes (23): NPCOccupantProcessor, NPC occupant processing utilities. This module handles querying and processing…, Processes NPC occupants for rooms., Get lifecycle manager for filtering fallback NPCs. Returns: Lifecycle manager…, Check if a single fallback NPC should be included. Args: npc_id: The NPC ID to…, Filter fallback NPCs to only include those in active_npcs and alive. Args:…, Room ID normalization and comparison utilities. This module provides utilities…, Initialize the room occupant manager. Args: connection_manager:… (+15 more)

### Community 1100 - "Async Persistence Migration Tracker"
Cohesion: 0.12
Nodes (15): Async Persistence Migration Tracker, Current Status, Decision Tree, Files Requiring Migration, Migration Pattern, Migration Strategy, Overview, Phase 1: High Priority (✅ COMPLETE) (+7 more)

### Community 1102 - "analyze_log_file"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 1103 - "Migration 019: Ready for Deployment"
Cohesion: 0.12
Nodes (15): Application Script, Database Schema, Documentation, Files Ready, Implementation Complete, Migration 019: Ready for Deployment, Migration Script, Next Action (+7 more)

### Community 1104 - "_meta"
Cohesion: 0.18
Nodes (14): _meta(), _player_with_room(), ConnectionMetadata, UUID, Test establish_websocket_connection() cleans up dead connections., New session_id closes prior sockets before append-register (#610)., Same session_id appends; does not kill a healthy prior socket (#610)., No player_sessions entry: first session_id appends; does not close leftover… (+6 more)

### Community 1105 - "nats_exceptions.py"
Cohesion: 0.05
Nodes (41): NATSConnectionError, NATSHealthCheckError, NATSPublishError, NATSSubscribeError, Exception, NATS-specific exception hierarchy for standardized error handling. This module…, Raised when NATS connection operations fail., Raised when message publishing fails. (+33 more)

### Community 1106 - "test_world_loader.py"
Cohesion: 0.19
Nodes (9): Unit tests for world loader utility functions. Tests room ID generation,…, Test generate_room_id() function., Test generate_room_id() with basic components., Test generate_room_id() handles components with underscores., Test generate_room_id() with empty components., Test generate_room_id() preserves special characters in components., TestGenerateRoomId, generate_room_id() (+1 more)

### Community 1107 - "🟢 MEDIUM PRIORITY IMPROVEMENTS"
Cohesion: 0.13
Nodes (15): 15. Hardcoded Connection Pool Sizes, 16. Deprecated asyncio.get_event_loop() Usage, 17. Inconsistent Error Handling Patterns, 18. Memory Leak Risk in Metrics Collection, 19. Missing Message Acknowledgment in NATS, 20. Subject Naming Inconsistency, 21. No Connection Health Monitoring, 🟢 MEDIUM PRIORITY IMPROVEMENTS (+7 more)

### Community 1108 - "Critical Insights"
Cohesion: 0.13
Nodes (15): 1. Infrastructure Tests are the Main Optimization Target, 2. Regression Tests are 100% High-Value, 3. Coverage Tests Written for Metrics, Not Quality, 4. No Parametrized Tests (Major Opportunity), 5. Critical Gaps in New Architecture, Critical Insights, Example, Example Low-Value Test (+7 more)

### Community 1109 - "magic_service.py"
Cohesion: 0.05
Nodes (39): Healing event notification for spellcasting. Mixin that sends player_dp_updated…, MagicServiceOptionalDeps, TypedDict, Core magic service for spellcasting. This module provides the main magic…, Optional dependencies for MagicService. All keys optional; defaults applied in…, Initialize the magic service. Args: spell_registry: Registry for spell lookups…, Any, UUID (+31 more)

### Community 1110 - "Test Suite Quality Audit - Executive Summary"
Cohesion: 0.13
Nodes (15): **25-30% (~1,250-1,500 tests) provide CRITICAL regression protection**, Answer to Original Question, Breakdown, By Category, Comparison to Industry Benchmarks, Created Documents, Deliverables Summary, Key Findings (+7 more)

### Community 1111 - "correct_patterns.py"
Cohesion: 0.04
Nodes (57): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+49 more)

### Community 1112 - "TestValidatorIntegration"
Cohesion: 0.14
Nodes (8): Integration tests for the main validator., Test validator with valid room files., Test validator with invalid room files., Test validator JSON output format., Test validator zone filtering., Test that help text is properly displayed., Test schema-only validation flag., TestValidatorIntegration

### Community 1113 - "HolidayService"
Cohesion: 0.01
Nodes (167): Game bundle: player, room, movement, exploration, user_manager,…, Wire holiday/schedule services and Mythos tick scheduler., Record the schedule categories currently active for NPC routines., HolidayCollection, HolidayEntry, BaseModel, Calendar ingestion schemas for MythosMUD. These models provide a typed wrapper…, Create a mapping of holiday IDs to holiday entries. Returns: dict[str,… (+159 more)

### Community 1114 - "CommunicationIntegrationProtocol"
Cohesion: 0.14
Nodes (10): CombatIntegrationProtocol, CommunicationIntegrationProtocol, Protocol, Protocols for NPC combat and communication integration (used by NPCBase)., Handle NPC death in the combat integration layer., Protocol for communication integration (whisper, room message, handle player…, Send a private whisper from this NPC to a single player., Send a message from this NPC to all players in a room. (+2 more)

### Community 1115 - "rest_countdown_task.py"
Cohesion: 0.24
Nodes (14): create_rest_countdown_task(), _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, Task, UUID, Rest countdown task implementation. This module contains the async task that… (+6 more)

### Community 1116 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1117 - "lifespan_magic.py"
Cohesion: 0.04
Nodes (59): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+51 more)

### Community 1118 - "add_suppression_to_file"
Cohesion: 0.47
Nodes (5): add_suppression_to_file(), main(), Path, Add suppression comment to a PowerShell file if it uses Write-Host and doesn't…, Process all PowerShell scripts in the scripts directory.

### Community 1119 - "field_validator"
Cohesion: 0.14
Nodes (8): Any, field_validator, Validate schedule entry days are standard English weekday names (Sunday,…, Validate slug-formatted list entries. Args: value: Sequence of strings to…, Ensure the schedule window moves time forward like the Chronology Tablets…, Validate tradition value. Args: value: The tradition string to validate…, Validate season value. Args: value: The season string to validate Returns: str:…, Validate bonus tags format.

### Community 1120 - "find_fstring_logging_violations"
Cohesion: 0.20
Nodes (11): find_fstring_logging_violations(), format_violation_report(), FStringLoggingDetector, main(), Call, Path, Main function to scan files and report violations., AST visitor to detect f-string logging violations. (+3 more)

### Community 1121 - "lint_sql_guardrails.py"
Cohesion: 0.23
Nodes (13): check_not_in_subquery(), check_select_star(), _collect_sql_files(), main(), Path, Lightweight guardrails for hand-maintained PostgreSQL SQL. Warns on: - select *…, Return line with line comment removed (-- ...)., Return content with block comments /* ... */ removed (simple, no nested). (+5 more)

### Community 1122 - "Improve Layout Systematically"
Cohesion: 0.15
Nodes (12): Assess Current Layout, Break Card Grid Monotony, Choose the Right Layout Tool, Create Visual Rhythm, Establish a Spacing System, Improve Layout Systematically, Manage Depth & Elevation, MANDATORY PREPARATION (+4 more)

### Community 1123 - "Simplify the Design"
Cohesion: 0.15
Nodes (12): Assess Current State, Code Simplification, Content Simplification, Document Removed Complexity, Information Architecture, Interaction Simplification, Layout Simplification, MANDATORY PREPARATION (+4 more)

### Community 1124 - "_utc_now"
Cohesion: 0.21
Nodes (12): datetime, Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE…, _utc_now(), Unit tests for lucidity model utility functions. Tests the _utc_now utility…, Test _utc_now returns a datetime object., Test _utc_now returns naive datetime (tzinfo=None)., Test _utc_now returns time close to current UTC time., Test _utc_now returns different times on subsequent calls. (+4 more)

### Community 1125 - "CircuitBreaker"
Cohesion: 0.15
Nodes (11): CircuitBreaker, timedelta, Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…, Circuit breaker for NATS message processing. Implements Martin Fowler's circuit…, Initialize circuit breaker. Args: failure_threshold: Number of failures before…, Test _time_until_retry() returns 0 when not OPEN., Test _time_until_retry() returns remaining time., Test _transition_to() updates state. (+3 more)

### Community 1126 - "test_mp_regeneration_service.py"
Cohesion: 0.14
Nodes (13): Unit tests for MP regeneration service. Tests the MPRegenerationService class…, Test _get_regen_multiplier() returns 1.0 for standing position., Test _get_regen_multiplier() returns REST multiplier for sitting., Test _get_regen_multiplier() returns enhanced REST multiplier for lying., Test _get_regen_multiplier() defaults to 1.0 when position not specified., Test MPRegenerationService initialization., Test MPRegenerationService initialization with custom regen_rate., test_get_regen_multiplier_default_position() (+5 more)

### Community 1127 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test cleanup_orphaned_data() cleans up orphaned data., Test cleanup_dead_connections() cleans up dead websocket connections., Test cleanup_orphaned_data() closes stale active connections., Test check_and_cleanup() no-ops when memory monitor does not request cleanup., Test force_cleanup() performs forced cleanup., Test check_and_cleanup() performs cleanup check., test_check_and_cleanup() (+5 more)

### Community 1129 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test call() closes circuit from HALF_OPEN after success threshold., Test call() reopens circuit from HALF_OPEN on failure., Test call() executes successfully in CLOSED state., Test call() handles failure in CLOSED state., Test call() opens circuit after failure threshold., Test call() transitions to HALF_OPEN after timeout., test_call_closes_from_half_open_on_success() (+5 more)

### Community 1131 - "Asynchronous Code Audit - December 3, 2025"
Cohesion: 0.14
Nodes (13): adjusts spectacles grimly, Asynchronous Code Audit - December 3, 2025, ✍️ AUDIT CONCLUSION, Audit Status**: ✅**COMPLETE, Blocking Risks, 📞 ESCALATION MATRIX, Executive Summary, Non-Blocking Risks (+5 more)

### Community 1132 - "Easy Coverage Wins - Quick Analysis"
Cohesion: 0.14
Nodes (13): Easy Coverage Wins - Quick Analysis, 🚀 Next Steps, Phase 1: Quick Wins (Tier 1 + Tier 2) ✅ COMPLETED, Phase 2: Medium Effort (Tier 3) ✅ COMPLETED, Phase 3: New Small Files (Tier 4) ✅ COMPLETED, Phase 4: Additional Realtime Files 🔄 IN PROGRESS, 📊 Recommended Priority Order, 🎉 Summary (+5 more)

### Community 1133 - "Test Value Distribution Chart"
Cohesion: 0.14
Nodes (13): Coverage vs Value Analysis, Declare Success When, Efficiency = Value per Second of Execution, Interpretation, Success Celebration Criteria, Target Quadrants, Test Execution Time Efficiency, Test Maintenance Burden (+5 more)

### Community 1134 - "test_zone_config_loader.py"
Cohesion: 0.09
Nodes (41): async_load_zone_configurations(), process_subzone_rows(), process_zone_rows(), Connection, Process subzone rows from database and populate subzone configurations. Args:…, Async helper to load zone configurations from PostgreSQL database., Result of loading zone and sub-zone configs from PostgreSQL., Process zone rows from database and populate zone configurations. Args: conn:… (+33 more)

### Community 1135 - "test_game_tick_processing.py"
Cohesion: 0.11
Nodes (26): cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _create_corpse_lifecycle_service(), _log_cleanup_results(), Validate that required services exist for MP regeneration. Args: container:…, Reset the current tick for testing., Create and initialize CorpseLifecycleService. Args: app: FastAPI application…, Cleanup a single decayed corpse. Args: corpse_service: Corpse lifecycle service… (+18 more)

### Community 1136 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test broadcast_combat_attack handles personal message errors gracefully., Test broadcast_player_mortally_wounded without attacker., Test broadcast_player_respawn broadcasts respawn message., Test broadcast_combat_attack sends personal message to attacker., Test broadcast_combat_attack without attacker_id., Test broadcast_player_death handles personal message errors., test_broadcast_combat_attack_no_attacker_id() (+5 more)

### Community 1140 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1141 - "test_profession_service.py"
Cohesion: 0.25
Nodes (13): persistence(), _profession(), asyncio, fixture, Unit tests for ProfessionService., service(), test_get_all_professions_dict(), test_get_profession_by_id_dict_found() (+5 more)

### Community 1144 - "idle_movement_handler"
Cohesion: 0.29
Nodes (7): idle_movement_handler(), mock_event_bus(), mock_persistence(), fixture, Create a mock persistence layer., Create a mock event bus., Create an IdleMovementHandler instance.

### Community 1145 - "rules"
Cohesion: 0.08
Nodes (25): entry, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries, dependencies (+17 more)

### Community 1146 - "dependencies"
Cohesion: 0.08
Nodes (25): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-resizable, react-rnd (+17 more)

### Community 1148 - "test_persistence_container_persistence.py"
Cohesion: 0.14
Nodes (13): Unit tests for persistence.container_persistence module. This module tests the…, Test parsing None JSONB column., Test parsing string JSONB column., Test parsing dict JSONB column., Test parsing empty string JSONB column., Test parsing list JSONB column., Test parsing invalid JSON string., test_parse_jsonb_column_dict() (+5 more)

### Community 1150 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test _ensure_room_cache_loaded returns early when cache is already loaded., Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…, Test _ensure_room_cache_loaded handles DatabaseError gracefully., Test _ensure_room_cache_loaded handles OSError gracefully., Test _ensure_room_cache_loaded handles RuntimeError gracefully., test_ensure_room_cache_loaded_already_loaded(), test_ensure_room_cache_loaded_concurrent_load() (+3 more)

### Community 1151 - "asyncio"
Cohesion: 0.14
Nodes (14): asyncio, Test get_player_room_from_persistence() returns player room., Test is_player_in_room() returns True when player is in room., Test preload_receiver_mute_data() excludes sender from targets., test_check_player_mute_status_patched_and_emote(), test_filter_target_players_room_and_mute(), test_get_player_room_from_persistence(), test_get_player_room_from_persistence_mock_player() (+6 more)

### Community 1152 - "TestValidatorComponents"
Cohesion: 0.17
Nodes (7): Test path validator integration., Test reporter integration., Test the full validation pipeline., Test individual validator components., Test room loader integration., Test schema validator integration., TestValidatorComponents

### Community 1153 - "Azotottal.md"
Cohesion: 0.33
Nodes (3): Azotottal, Comte Fenalik, The Old Gods (nameless patrons)

### Community 1154 - "PlayerOccupantProcessor"
Cohesion: 0.16
Nodes (13): PlayerOccupantProcessor, Any, UUID, Process players and convert to occupant information. Args: room_id: The room ID…, Processes player occupants for rooms., Initialize player occupant processor. Args: connection_manager:…, Ensure a player is included in the player ID strings list if specified. Args:…, Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:… (+5 more)

### Community 1157 - ".validate_combat_command"
Cohesion: 0.17
Nodes (7): Any, Initialize the combat validator. Args: party_service: Optional PartyService for…, Validate a combat command with thematic error messages. Args: command_data: The…, Check if target name is valid., Check for suspicious patterns in target name., Check if player is rate limited., Get a thematic combat status message.

### Community 1158 - "server/services/__init__.py"
Cohesion: 0.03
Nodes (122): AbstractContextManager, _ensure_shared_services_initialized(), get_shared_services(), Shared service initialization for inventory commands., Clear lazy singletons so each test gets a fresh init path. For unit tests only;…, Resolve async_persistence from the request and construct shared singletons., Get shared service instances, initializing them lazily if needed. This ensures…, reset_shared_inventory_services_for_tests() (+114 more)

### Community 1159 - "Earth Plane"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1160 - "compilerOptions"
Cohesion: 0.15
Nodes (12): compilerOptions, allowImportingTsExtensions, composite, noEmit, rootDir, types, exclude, extends (+4 more)

### Community 1161 - "Actionable Recommendations"
Cohesion: 0.15
Nodes (13): Actionable Recommendations, Add Missing Integration Tests (70 tests, 0% risk, 10 hours effort), Command, Critical Gap Action (Month 2), Files, High-Priority Action (Next 2 Weeks), Immediate Action (This Week), Parametrize Repetitive Tests (170 → 50, 0% risk, 8 hours effort) (+5 more)

### Community 1162 - "Execution Timeline"
Cohesion: 0.15
Nodes (13): Execution Timeline, Month 1: Pruning Phase, Month 2: Consolidation + Gap Filling, Month 3+: Continuous Improvement, Ongoing Tasks, Week 1: Quick Wins, Week 2: Infrastructure Reduction, Week 3: Coverage Test Optimization (+5 more)

### Community 1163 - "MockPersistence"
Cohesion: 0.10
Nodes (16): mock_app(), mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), MockPersistence, fixture, Create a mock FastAPI app. (+8 more)

### Community 1164 - "Amplify the Design"
Cohesion: 0.17
Nodes (11): Amplify the Design, Assess Current State, Color Intensification, Composition Boldness, MANDATORY PREPARATION, Motion & Animation, Plan Amplification, Spatial Drama (+3 more)

### Community 1165 - "Interaction Design"
Cohesion: 0.17
Nodes (12): Destructive Actions: Undo > Confirm, Focus Rings: Do Them Right, Form Design: The Non-Obvious, Gesture Discoverability, Interaction Design, Keyboard Navigation Patterns, Loading States, Modals: The Inert Approach (+4 more)

### Community 1166 - "Hardening Dimensions"
Cohesion: 0.17
Nodes (11): Accessibility Resilience, Assess Hardening Needs, Edge Cases & Boundary Conditions, Error Handling, Hardening Dimensions, Input Validation & Sanitization, Internationalization (i18n), Performance Resilience (+3 more)

### Community 1167 - "Async Remediation Summary - December 3, 2025"
Cohesion: 0.17
Nodes (11): Async Remediation Summary - December 3, 2025, Executive Summary, 📝 Git Commit Message, Issues Addressed (12 of 12), New Tests Created, Phase 2: Async Persistence Migration (2-3 weeks), 📋 Remaining Work, 📊 Remediation Results (+3 more)

### Community 1168 - "MythosMUD LLM Wiki (Obsidian)"
Cohesion: 0.17
Nodes (11): Chaosium ingest, Division of labor, Graphify sync, Ingest, Lint, MythosMUD LLM Wiki (Obsidian), Non-goals, Query (durable) (+3 more)

### Community 1169 - "Migration Guide: From Default Logging to Enhanced Logging"
Cohesion: 0.17
Nodes (12): 1. Update Import Statements, 2. Migrate Context Parameters, 3. Convert String Formatting to Structured Logging, 4. Add Rich Context to Error Messages, Issue 1: ImportError when using enhanced logging, Issue 2: TypeError with context parameter, Issue 3: Logs not appearing in files, Issue 4: Sensitive data appearing in logs (+4 more)

### Community 1170 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 1171 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 1172 - "properties"
Cohesion: 0.11
Nodes (19): description, items, type, default, description, maximum, minimum, type (+11 more)

### Community 1173 - "main"
Cohesion: 0.22
Nodes (12): analyze_connectivity(), generate_dot_file(), load_room_data(), main(), print_detailed_statistics(), print_room_listing(), Print a detailed listing of all rooms by subzone., Load all room and intersection data from the zone directory. (+4 more)

### Community 1174 - "main"
Cohesion: 0.22
Nodes (12): fix_md001_heading_increment(), fix_md013_line_length(), fix_md041_first_line_heading(), fix_md051_link_fragments(), main(), parse_errors(), Fix MD001: Heading levels should only increment by one level at a time., Parse markdownlint output file and extract errors. (+4 more)

### Community 1175 - "SyntaxErrorFixer"
Cohesion: 0.22
Nodes (8): main(), Path, Process multiple files and return statistics., Main function to run the syntax error fixer., Tool to fix syntax errors introduced by automated f-string remediation., Fix malformed logger calls with broken syntax., Fix syntax errors in a specific file., SyntaxErrorFixer

### Community 1176 - "test_npc_combat_integration_service_player_attacks.py"
Cohesion: 0.09
Nodes (30): asyncio, Unit tests for NPC combat integration service - player-initiated combat paths., Test handle_player_attack_on_npc returns False when NPC not found., Test handle_player_attack_on_npc handles exceptions gracefully., Test _setup_combat_uuids_and_mappings handles ValueError., Test _setup_combat_uuids_and_mappings with valid UUID., Test store_npc_xp_mapping_for_mixin when NPC definition is not found., Test store_npc_xp_mapping_for_mixin when base_stats is not a dict. (+22 more)

### Community 1177 - "ADR-018: New Game Session vs Grace Reconnect"
Cohesion: 0.18
Nodes (10): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. References, 8. Changelog (+2 more)

### Community 1178 - "CombatAuditLogger"
Cohesion: 0.05
Nodes (59): CombatAttackDetails, CombatAuditLogger, CombatMonitoringAlert, CombatParties, CombatSecurityEvent, Any, datetime, Combat-specific audit logging and monitoring. This module provides specialized… (+51 more)

### Community 1186 - "Migration Roadmap"
Cohesion: 0.17
Nodes (12): Files to Migrate (11 total), Files to Migrate (2 total), Files to Migrate (6 total), Game Systems (3 files), Migration Roadmap, NPC Systems (7 files), Phase 2: API Endpoints (Priority 1) 🎯, Phase 3: Real-Time Handlers (Priority 2) 🚀 (+4 more)

### Community 1187 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test restore_mp_from_meditation() returns error when player not found., Test restore_mp_from_meditation() returns message when MP already at max., Test restore_mp_from_meditation() restores MP., Test restore_mp_from_item() respects max_mp limit., Test restore_mp_from_item() uses magic_service if available., Test process_tick_regeneration() uses REST multiplier for sitting position., Test process_tick_regeneration() restores MP. (+9 more)

### Community 1188 - "CacheService"
Cohesion: 0.26
Nodes (4): CacheService, Main cache service that coordinates all caching operations. This service…, Preload frequently accessed data into caches. This method loads commonly used…, TestCacheService

### Community 1189 - "PhantomHostileService"
Cohesion: 0.04
Nodes (52): FakeHallucinationService, Any, UUID, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Select which type of fake hallucination to trigger (50/50 chance). Returns:…, Service for generating fake NPC tells and room text overlays. These…, Initialize the fake hallucination service., Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will… (+44 more)

### Community 1190 - "MotdInterstitialScreen.tsx"
Cohesion: 0.21
Nodes (5): MotdContent(), MOTD_BUTTON_STYLE, MotdInterstitialScreen(), MotdInterstitialScreenProps, MotdInterstitialScreen

### Community 1191 - "_format_container_contents"
Cohesion: 0.17
Nodes (12): _format_container_contents(), Format container contents as list of lines., Test _format_container_contents() with empty list., Test _format_container_contents() with items having quantity., test_format_container_contents_empty(), test_format_container_contents_with_quantity(), Test formatting container contents with items., Test formatting container contents when empty. (+4 more)

### Community 1192 - "PlayerPreferencesService"
Cohesion: 0.14
Nodes (18): PlayerPreferencesService, Any, AsyncSession, UUID, Player Preferences Service for Advanced Chat Channels. This module provides…, Get preferences for a player. Args: session: Database session player_id: The…, Update a player's default channel. Args: session: Database session player_id:…, Mute a channel for a player. Args: session: Database session player_id: The… (+10 more)

### Community 1193 - "_is_websocket_connected"
Cohesion: 0.18
Nodes (11): _is_websocket_connected(), WebSocket, Check if a WebSocket is connected. Args: websocket: The WebSocket to check…, Test _is_websocket_connected() returns True for connected websocket., Test _is_websocket_connected() returns False for disconnected websocket., Test _is_websocket_connected() handles missing client_state., Stand-in whose missing client_state trips AttributeError in the helper., test_is_websocket_connected_connected() (+3 more)

### Community 1194 - "test_monitoring_init.py"
Cohesion: 0.17
Nodes (11): Unit tests for server.monitoring lazy __getattr__ re-exports., Exception tracker symbols import without triggering numpy lazy paths., __getattr__ resolves MonitoringDashboard and get_monitoring_dashboard., __getattr__ resolves PerformanceStats and get_performance_monitor., Unknown attribute names raise AttributeError., Direct __getattr__ covers both branch returns for dashboard imports., test_monitoring_eager_imports(), test_monitoring_getattr_direct_call() (+3 more)

### Community 1195 - "Async Code Review - Post Phase 2 Migration"
Cohesion: 0.18
Nodes (10): anyio.mdc Compliance, Async Code Review - Post Phase 2 Migration, asyncio.mdc Compliance, 📋 Checklist Against Best Practices, 📊 Compliance Scorecard, 📝 Conclusion, Executive Summary, 🟡 Minor Recommendations (Not Blocking) (+2 more)

### Community 1196 - "✅ Best Practices Compliance"
Cohesion: 0.18
Nodes (11): 10. Exception Handling in Async Operations (asyncio.mdc Section 2.5), 1. Blocking the Event Loop (asyncio.mdc Section 2.3), 2. Async/Await Usage (anyio.mdc Section 2.2), 3. Method Signature Consistency (asyncio.mdc Section 2.1), 4. Error Handling (asyncio.mdc Section 2.5), 5. Resource Management (anyio.mdc Section 2.1), 6. Task Groups / Structured Concurrency (anyio.mdc Section 2.1), 7. Avoiding asyncio.run() in Library Code (asyncio.mdc Section 6.1) (+3 more)

### Community 1197 - "LLM Wiki Vault Schema"
Cohesion: 0.50
Nodes (4): LLM Wiki Vault Schema, Raw Sources Layer, Wiki Layer, Wiki Page Template

### Community 1200 - "🔍 Specific File Reviews"
Cohesion: 0.18
Nodes (11): ✅ container_service.py, ✅ corpse_lifecycle_service.py, ✅ database.py, ✅ exploration_service.py, ✅ npc_combat_integration_service.py, ✅ passive_lucidity_flux_service.py, ✅ persistence.py, ✅ player_death_service.py (+3 more)

### Community 1201 - "Enhanced Logging Best Practices for MythosMUD"
Cohesion: 0.20
Nodes (9): Common Anti-Patterns, Conclusion, ✅ Do This Instead, ❌ Don't Do This, Enhanced Logging Best Practices for MythosMUD, Integration Tests, Overview, Testing Logging (+1 more)

### Community 1202 - "Nameless Horrors - 2nd Edition (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extractions pages, Nameless Horrors - 2nd Edition (source summary)

### Community 1203 - "S. Petersen's Field Guide to Lovecraftian Horrors (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extrated pages, S. Petersen's Field Guide to Lovecraftian Horrors (source summary)

### Community 1204 - "test_npc_spawn_rules_api.py"
Cohesion: 0.13
Nodes (26): NPCSpawnRuleResponse, Model for NPC spawn rule responses., Create response from ORM object., create_npc_spawn_rule(), delete_npc_spawn_rule(), get_npc_spawn_rules(), AsyncSession, delete (+18 more)

### Community 1206 - "TaskRegistry"
Cohesion: 0.23
Nodes (22): Centralized asyncio task registry for lifecycle-tracking with timeout…, TaskRegistry, _hang_until_cancelled(), asyncio, fixture, MonkeyPatch, Unit tests for asyncio TaskRegistry lifecycle management., registry() (+14 more)

### Community 1207 - "extract_npc_metadata"
Cohesion: 0.17
Nodes (12): extract_npc_metadata(), Extract NPC type and required status from NPC instance. Args: npc_instance: The…, Test extract_npc_metadata() returns defaults when missing., Test extract_npc_metadata() handles non-string npc_type., Test extract_npc_metadata() converts truthy is_required., Test extract_npc_metadata() handles None is_required., Test extract_npc_metadata() extracts valid metadata., test_extract_npc_metadata_defaults() (+4 more)

### Community 1208 - "Test Suite Quality Audit Report"
Cohesion: 0.18
Nodes (10): ~25-30% (1,250-1,500 tests) provide CRITICAL protection, Answer to Your Question, Conclusion, Phase A: Quick Wins (1-2 hours effort), Phase B: Medium Effort (4-8 hours effort), Phase C: Strategic Enhancements (8-16 hours effort), Recommended Action, Specific Actionable Recommendations (+2 more)

### Community 1209 - "parse_json_field"
Cohesion: 0.17
Nodes (12): parse_json_field(), Parse a JSON field from database, handling both dict/list and string formats.…, Test parse_json_field() returns default when None., Test parse_json_field() parses JSON string., Test parse_json_field() returns dict as-is., Test parse_json_field() returns list as-is., Test parse_json_field() raises error on invalid JSON string., test_parse_json_field_dict() (+4 more)

### Community 1210 - "npc_combat_grace.py"
Cohesion: 0.18
Nodes (16): get_app_instance(), Return the runtime app instance attached during lifespan startup. This provides…, _connection_manager_from_config_app(), is_npc_attack_on_player_blocked_by_login_grace_period(), is_player_attack_blocked_by_login_grace_period(), UUID, Login grace-period checks for NPC combat integration (extracted to keep service…, Resolve connection_manager from the public config app accessor. Uses getattr on… (+8 more)

### Community 1211 - "create_error_context"
Cohesion: 0.21
Nodes (10): create_error_context(), Any, Request, Shared helper functions for player API endpoints., Create error context from request and user. Helper function to reduce…, Unit tests for server.api.player_helpers (error context helper)., When current_user is None, context gets metadata only., When current_user is set, user_id is populated and metadata merged. (+2 more)

### Community 1212 - "._trim_samples"
Cohesion: 0.17
Nodes (6): Record a session switch event. Args: duration_ms: Duration in milliseconds, Record a health check event. Args: duration_ms: Duration in milliseconds, Trim samples to prevent unbounded memory growth. Args: metric_key: Key in…, Record a connection establishment event. Args: connection_type: Type of…, Record a message delivery event. Args: message_type: Type of message…, Record a disconnection event. Args: connection_type: Type of connection…

### Community 1213 - ".load_player_mutes"
Cohesion: 0.21
Nodes (6): Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory., Load channel mutes from JSON data into memory., Load global mutes from JSON data into memory., Load mute data for a specific player from JSON file. Args: player_id: Player ID…

### Community 1215 - "event_bus"
Cohesion: 0.67
Nodes (3): event_bus(), fixture, Create an EventBus instance.

### Community 1216 - "debugLogger"
Cohesion: 0.13
Nodes (5): debugLogger, LogConfig, LogEntry, LogLevel, mockConsole

### Community 1217 - "test_publish_attack_event_emits_npc_attacked"
Cohesion: 0.09
Nodes (12): _publish_attack_event forwards to event bus when configured., Empty npc_stats yields default strength/constitution., Provided npc_stats are returned as-is., First underscore segment title-cased., Fallback max_dp uses (con+siz)//5., hp alias filled from determination_points., test_calculate_max_dp_from_constitution_and_size(), test_derive_npc_name_from_id() (+4 more)

### Community 1218 - "test_connection_models.py"
Cohesion: 0.17
Nodes (11): Unit tests for connection models. Tests the connection_models module classes., Test ConnectionMetadata inequality comparison., Test ConnectionMetadata.__init__() creates metadata with required fields., Test ConnectionMetadata.__init__() with optional fields., Test ConnectionMetadata has all expected dataclass fields., Test ConnectionMetadata equality comparison., test_connection_metadata_dataclass_fields(), test_connection_metadata_equality() (+3 more)

### Community 1219 - "PlayerDeathService"
Cohesion: 0.10
Nodes (21): PlayerLifecycleServices, Small types shared by CombatService wiring., Player death and respawn services for CombatService injection., PlayerDeathService, Any, AsyncSession, Player, UUID (+13 more)

### Community 1220 - "Multi-Character Support System"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1221 - "test_quest_instance_repository.py"
Cohesion: 0.11
Nodes (33): _make_session_context(), mock_quest_instance(), asyncio, fixture, quest_instance_repository(), Unit tests for QuestInstanceRepository. Tests create, get_by_player_and_quest,…, Test get_by_player_and_quest returns mapped instance when found., Test get_by_player_and_quest returns None when not found. (+25 more)

### Community 1222 - "Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES"
Cohesion: 0.20
Nodes (10): Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES, Phase 3: Medium Priority Improvements (Week 4) - POLISH, 📋 REMEDIATION PLAN, Task 1.1: Fix Synchronous Blocking in Passive Lucidity Flux Service, Task 1.2: Eliminate asyncio.run() from Library Code, Task 1.3: Ensure Connection Pool Cleanup, Task 1.4: Add Exception Handling to Pool Creation, Task 1.5: Fix Blocking Operations in NATS Message Handlers (+2 more)

### Community 1223 - "grype.py"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1224 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1225 - "Recommended Test Additions"
Cohesion: 0.20
Nodes (10): 1. MessageBroker Integration Tests (15 tests, ~1 hour), 2. ApplicationContainer Lifecycle Tests (10 tests, ~1 hour), 3. Database Migration Tests (10 tests, ~1.5 hours), 4. WebSocket Edge Case Tests (15 tests, ~2 hours), 5. Error Recovery Tests (20 tests, ~3 hours), Immediate Priority (Add First), Recommended Test Additions, Secondary Priority (Add Second) (+2 more)

### Community 1226 - "Appendices"
Cohesion: 0.20
Nodes (10): Appendices, Appendix A: Test File Inventory, Appendix B: Direct app.state Access Locations, Appendix C: Fixture Audit, Consolidation Opportunities, Current Fixture Categories, High Priority (Integration Tests), Low Priority (Other) (+2 more)

### Community 1227 - "MythosMUD Testing Strategy (Greenfield Suite)"
Cohesion: 0.20
Nodes (9): Coverage policy, Fixtures/layout, Isolation rules, Logging and diagnostics, Markers, Mocking standards, MythosMUD Testing Strategy (Greenfield Suite), Tiers and commands (+1 more)

### Community 1228 - "test_validate_codacy_coverage_gate.py"
Cohesion: 0.23
Nodes (12): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., test_cobertura_root_line_rate_parses(), test_lcov_aggregate_and_gate() (+4 more)

### Community 1229 - "Dialogue Content Tools (Content Creators)"
Cohesion: 0.20
Nodes (9): 1. Overview, 2. Open the editor, 3. Tree shape (nav-only), 4. Editor workflow, 5. Player verification, 6. Seed and API reference, 7. Related docs, AI READING INSTRUCTION (+1 more)

### Community 1230 - "snapshot_chaosium_graphify.ps1"
Cohesion: 0.70
Nodes (4): Export-PackSnapshot(), Get-ChaosiumSlug(), Get-GraphCount(), Get-HonestyNote()

### Community 1231 - "test_message_filtering.py"
Cohesion: 0.17
Nodes (9): Unit tests for message filtering. Tests the MessageFilteringHelper class., Test is_player_muted_by_receiver() checks mute status., Test _get_user_manager() returns global user manager when custom not set., Test collect_room_targets() returns subscribed players., Test collect_room_targets() returns empty set when no subscribers., test_collect_room_targets(), test_collect_room_targets_empty(), test_get_user_manager_global() (+1 more)

### Community 1232 - "_FakeNPCService"
Cohesion: 0.31
Nodes (5): bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…

### Community 1233 - "test_player_repository_room.py"
Cohesion: 0.20
Nodes (20): Any, Player, Player room validation helpers for PlayerRepository. Validates and fixes…, Return True if room validation should be skipped (cache empty, instanced, or…, Validate player's current room and fix if invalid. Args: room_cache: Shared…, Validate and fix player room, persisting the fix if needed. Args: room_cache:…, should_skip_room_validation(), validate_and_fix_player_room() (+12 more)

### Community 1234 - "cached"
Cohesion: 0.33
Nodes (5): cached(), Decorator to cache function results. Args: cache_name: Name of the cache to use…, Keep players cache truthy; empty LRUCache is bool-false via __len__., _seed_players_cache(), TestCachedDecorator

### Community 1235 - "LoggedException"
Cohesion: 0.12
Nodes (18): LoggedException, Exception, Marker base class indicating an exception has already produced a log entry., Return True if this exception instance has already been logged., _as_bound_logger(), BoundLogger, Unit tests for enhanced_logging_config helpers. Covers log_exception_once…, Minimal stand-in for BoundLogger: only what log_exception_once touches for… (+10 more)

### Community 1236 - ".change_position"
Cohesion: 0.09
Nodes (16): PositionChangeResponse, Player, TypedDict, Validate and normalize position., Get player for position change. Returns: Tuple of (player, response_dict) if…, Copy player identity fields into the position-change response., Load player stats, returning {} when loading fails., Get current position from player stats. (+8 more)

### Community 1237 - "test_inventory_mutation_guard_async.py"
Cohesion: 0.17
Nodes (15): guard(), asyncio, fixture, Unit tests for inventory mutation guard - asynchronous acquire operations.…, Test acquire_async serializes concurrent mutations for same player., Create an InventoryMutationGuard instance., Test acquire_async enforces max_tokens limit., Test acquire_async allows token reuse after expiry. (+7 more)

### Community 1238 - "CircuitBreaker"
Cohesion: 0.10
Nodes (15): _CircuitBreakerResult, CircuitBreaker, Simple circuit breaker pattern implementation. Provides fault tolerance for…, Execute function with circuit breaker protection. Args: func: Function to…, Handle successful operation., Handle failed operation., Check if circuit breaker should attempt reset., Test CircuitBreaker class. (+7 more)

### Community 1239 - "test_player_event_handlers_respawn.py"
Cohesion: 0.17
Nodes (11): Unit tests for player respawn event handlers. Tests the…, Test send_respawn_event_with_retry() waits for connection to become available., Test PlayerRespawnEventHandler initialization., Test update_connection_manager_position() updates position., Test update_connection_manager_position() handles player not in online_players., Test update_connection_manager_position() handles missing online_players…, test_player_respawn_event_handler_init(), test_send_respawn_event_with_retry_waits_for_connection() (+3 more)

### Community 1244 - "CI Workflow"
Cohesion: 0.25
Nodes (11): CodeQL Configuration, CodeQL Test Credential Exclusions, CI Python Backend Job, CI Workflow, Codacy Coverage Finalize Job, CI React Client Job, step-security Harden Runner, mythos_unit CI Database Bootstrap (+3 more)

### Community 1251 - "mcp.json"
Cohesion: 0.20
Nodes (11): codacy, context7, jcodemunch, playwright, JCODEMUNCH_MAX_FOLDER_FILES, npx, uvx, @codacy/codacy-mcp (+3 more)

### Community 1254 - "test_websocket_handler_validation.py"
Cohesion: 0.20
Nodes (11): mock_validator(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler message validation. Tests the message…, Create a mock WebSocket., Create a mock message validator., Test _validate_message() returns message when validation succeeds. (+3 more)

### Community 1255 - "CombatEventPublisherProtocol"
Cohesion: 0.29
Nodes (6): CombatEventPublisherProtocol, NpcCombatServiceProtocol, Protocol, Typed surface for npc_combat_service.handle_npc_attack_on_player., Handle an NPC attack against a player via the main combat service., Combat event publisher (avoids importing CombatEventPublisher).

### Community 1256 - "Enhanced Logging Guide"
Cohesion: 0.25
Nodes (9): AI Agent Development Guide, AI Enhanced Logging Mandate, Enhanced Logging Guide, MDC Request Context Binding, measure_performance Span, Error Handling Guide, MythosMUDError Hierarchy, Error Logging Implementation Guide (+1 more)

### Community 1258 - "._compose_memory_stats"
Cohesion: 0.25
Nodes (6): MemoryStatsSnapshot, TypedDict, Assemble memory stats from a snapshot dict (keeps call sites param-stable)., Expose memory monitor configuration knobs for stats payload., Connection-manager snapshot consumed by get_memory_stats., Get comprehensive memory and connection statistics. Args: snap: Connection-…

### Community 1259 - "test_ascii_map_renderer_grid.py"
Cohesion: 0.17
Nodes (10): fixture, Unit tests for AsciiMapRenderer grid building. Guards against regressions in…, Return a fresh AsciiMapRenderer instance for each test., Tests for _build_grid player marker when multiple rooms share coordinates., Multiple rooms at same (x,y): cell keeps player marker even if player room is…, render_map covers empty map, styles, exits, and row rendering., renderer(), test_determine_map_style_and_symbols() (+2 more)

### Community 1260 - "🟡 HIGH PRIORITY ISSUES"
Cohesion: 0.22
Nodes (9): 10. Loading All Players Instead of Active Only, 11. NATS Connection Pool Not Used by Default, 12. No TLS Configuration for NATS, 13. Event Loop Change Detection Edge Cases, 14. Missing Transaction Rollback on Critical Failures, 7. Missing Room Lookup Caching, 8. Incomplete Migration to Async Persistence, 9. Multiple Database Flushes Before Commit (+1 more)

### Community 1261 - "Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE"
Cohesion: 0.22
Nodes (9): Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE, Task 2.1: Add Room Lookup Caching, Task 2.2: Complete Async Persistence Migration, Task 2.3: Optimize Database Flush Operations, Task 2.4: Load Only Active Players, Task 2.5: Use NATS Connection Pool by Default, Task 2.6: Add TLS Configuration, Task 2.7: Improve Event Loop Change Detection (+1 more)

### Community 1263 - "🔴 Anti-Patterns Check (Critical)"
Cohesion: 0.22
Nodes (9): 1. Blocking the Event Loop?, 2. Missing `await` Keywords?, 3. Using `asyncio.run()` in Library Code?, 4. Mixing Sync and Async Code Incorrectly?, 5. Forgetting to Await Awaitable Objects?, 6. Not Handling Exceptions?, 7. Over-using Locks?, 8. Unstructured Concurrency? (+1 more)

### Community 1264 - "add_hashed_password_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add hashed_password column. Args: database_url:…

### Community 1265 - "Persistence Layer Async Migration Plan"
Cohesion: 0.22
Nodes (8): Aggressive Timeline (Focused Migration), Conclusion, Conservative Timeline (Gradual Migration), Migration Timeline, Persistence Layer Async Migration Plan, Phase 1: Foundation Complete ✅, References, Total Migration Effort

### Community 1266 - "Any"
Cohesion: 0.09
Nodes (13): Any, Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…, Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…, Process a message for an NPC., Resolve active NPC instance and definition for a WANDER action., Parse NPC behavior config from instance attribute (dict or JSON string)., Run idle movement for a resolved wander NPC., Process a WANDER action for idle movement. Args: npc_id: ID of the NPC to move… (+5 more)

### Community 1267 - "rename_invites_columns.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Apply the migration to rename columns. Args: database_url: PostgreSQL database…, Main entry point for the migration script.

### Community 1268 - "Python Code Coverage Status"
Cohesion: 0.22
Nodes (8): Critical Files Below Threshold, Immediate Priority (Critical Files), Normal Files Below 70% Threshold, Priority Recommendations, Python Code Coverage Status, Secondary Priority (Normal Files), Showing top 50 files with largest coverage gaps, Summary

### Community 1269 - "**~25-30% provide CRITICAL coverage**"
Cohesion: 0.22
Nodes (8): **~25-30% provide CRITICAL coverage**, Immediate (This Week), Medium-Term (Next Month), Next Steps, Quick Reference, Short-Term (This Month), Specifically, The other 70-75%

### Community 1270 - "UUID"
Cohesion: 0.28
Nodes (5): UUID, Count active connections not tied to any online player., Build the connections subsection of memory stats., Build the sessions subsection of memory stats., Return numerator/denominator, or 0 when denominator is empty.

### Community 1271 - "Net Impact Summary"
Cohesion: 0.22
Nodes (8): Additions, Coverage Gap Priority Matrix, If We Execute Full Recommendations, Net Impact Summary, Net Result, Removals, Test Coverage Gaps Report, "The goal is not comprehensive coverage of all code, but comprehensive protection of all user value."

### Community 1272 - "test_npc_combat_integration_service_npc_aggro.py"
Cohesion: 0.08
Nodes (33): mock_async_persistence(), mock_combat_service(), mock_connection_manager(), mock_messaging_integration(), asyncio, Unit tests for NPC combat integration service - NPC-initiated aggro combat…, Test handle_npc_attack_on_player returns False when NPC instance cannot be…, Test handle_npc_attack_on_player returns False when NPC is dead. (+25 more)

### Community 1274 - "bench_cache.py"
Cohesion: 0.31
Nodes (6): bench_room_cache(), _FakePersistence, main(), Any, Lightweight cache benchmark for CI artifacts. Measures miss vs. hit timings for…, Fake persistence layer providing async_get_room with simulated latency.

### Community 1275 - "run_make_stages.py"
Cohesion: 0.33
Nodes (8): keep_going_requested(), main(), _print_fail(), Return True when Make was invoked with -k / --keep-going., Return a short failure reason, or None if the stage is OK., Run `make <stage>`, stream output, return (exit_code, captured_output)., run_stage(), stage_failed_from_output()

### Community 1276 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 1277 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 1278 - "_StubPlayerRepo"
Cohesion: 0.14
Nodes (4): UUID, _StubPlayerRepo, Retry decorator must not treat wrapped closed-connection as final on attempt 1., test_retry_retries_wrapped_connection_closed_then_succeeds()

### Community 1279 - "properties"
Cohesion: 0.17
Nodes (12): description, description, description, description, maxLength, minLength, type, properties (+4 more)

### Community 1280 - "analyze_file"
Cohesion: 0.22
Nodes (10): analyze_file(), check_comment_references_nonexistent_code(), extract_function_and_class_names(), main(), Any, Path, Analyze a single file for comment issues. Args: file_path: Path to file to…, Main entry point for comment analysis. (+2 more)

### Community 1281 - "main"
Cohesion: 0.25
Nodes (10): apply_migration_013(), apply_migration_014(), check_migration_013(), check_migration_014(), main(), Main function to check and apply migrations., Check if migration 013 (map_x/map_y columns) has been applied., Check if migration 014 (player_exploration table) has been applied. (+2 more)

### Community 1282 - "main"
Cohesion: 0.29
Nodes (10): check_thresholds(), _ensure_coverage_xml_or_exit(), main(), parse_coverage_xml(), _print_results_and_exit(), Path, Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't…, Print coverage results and exit with appropriate code. (+2 more)

### Community 1283 - "main"
Cohesion: 0.25
Nodes (10): generate_simple_dot_file(), generate_simple_html_visualization(), load_room_data(), main(), print_simple_statistics(), Load all room and intersection data from the zone directory., Print simplified statistics about the room data., Main function to generate the simplified visualization. (+2 more)

### Community 1284 - "lucidity_trigger_handlers.py"
Cohesion: 0.11
Nodes (32): CatatoniaObserverProtocol, Protocol, UUID, Handle a player returning from catatonia., Handle a player requiring sanitarium failover., Return False to suppress failover (debounce); True allows failover handling., Protocol for observers interested in catatonia state changes., Handle a player crossing into catatonia. (+24 more)

### Community 1285 - "mp_regeneration_service"
Cohesion: 0.22
Nodes (9): mock_player(), mock_player_service(), mp_regeneration_service(), fixture, Create a mock player service., Create an MPRegenerationService instance., Create a sample player ID., Create a mock player. (+1 more)

### Community 1286 - "_errors_len"
Cohesion: 0.17
Nodes (12): _errors_len(), Test _spawn_required_npcs() handles missing spawn room., Test _spawn_required_npcs() handles exceptions during spawning., Narrow spawn/startup result dict for len(results['errors']) without propagating…, Test _spawn_optional_npcs() handles exceptions during spawning., Test spawn_npcs_on_startup() handles exceptions during session processing., Test spawn_npcs_on_startup() handles critical exceptions., test_spawn_npcs_on_startup_critical_exception() (+4 more)

### Community 1287 - "CommandService"
Cohesion: 0.09
Nodes (17): CommandHandler, CommandService, Command, Main command processing service for MythosMUD. This service handles command…, Initialize the command service., Process a validated command with routing. Args: command_data: The validated…, Parse and validate command string. Returns: tuple of (parsed_command, cmd,…, Prepare command_data dictionary by merging parsed command fields. Returns:… (+9 more)

### Community 1288 - "MemoryProfiler"
Cohesion: 0.17
Nodes (11): Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.print_model_memory_usage() doesn't raise., Test MemoryProfiler.print_model_memory_usage() handles error dict., Test MemoryProfiler.get_memory_delta() returns 0 if no baseline., test_memory_profiler_get_memory_delta_no_baseline(), test_memory_profiler_measure_model_instantiation_zero_iterations(), test_memory_profiler_print_model_memory_usage(), test_memory_profiler_print_model_memory_usage_error() (+3 more)

### Community 1289 - "Responsive Design"
Cohesion: 0.18
Nodes (10): Breakpoints: Content-Driven, Detect Input Method, Not Just Screen Size, Layout Adaptation Patterns, Mobile-First: Write It Right, Picture Element for Art Direction, Responsive Design, Responsive Images: Get It Right, Safe Areas: Handle the Notch (+2 more)

### Community 1290 - "Refine the Design"
Cohesion: 0.18
Nodes (10): Assess Current State, Color Refinement, Composition Refinement, MANDATORY PREPARATION, Motion Reduction, Plan Refinement, Refine the Design, Simplification (+2 more)

### Community 1291 - "Teach Impeccable Skill"
Cohesion: 0.24
Nodes (11): Aha Moment Onboarding, Core Web Vitals Performance, Design Context Persistence (.impeccable.md), Onboard Skill, Optimize Skill, Overdrive Skill, Overdrive Mode, Polish Skill (+3 more)

### Community 1292 - "useMythosAppState.ts"
Cohesion: 0.11
Nodes (22): MythosAppViewModel, AppActions, AppState, buildActionViewModel(), buildMythosAppViewModel(), buildStateViewModel(), hoisted, useMythosApp() (+14 more)

### Community 1293 - "Improve Typography Systematically"
Cohesion: 0.18
Nodes (10): Assess Current Typography, Establish Hierarchy, Fix Readability, Font Selection, Improve Typography Systematically, MANDATORY PREPARATION, Plan Typography Improvements, Refine Details (+2 more)

### Community 1294 - "✅ Verified Already Implemented"
Cohesion: 0.25
Nodes (8): 10. TLS Configuration, 4. Connection Pool Cleanup, 5. Mute Data Caching, 6. F-String Logging, 7. Database Flush Operations, 8. Active Player Filtering, 9. NATS Connection Pooling, ✅ Verified Already Implemented

### Community 1295 - "API Endpoints (Phase 2)"
Cohesion: 0.25
Nodes (8): API Endpoints (Phase 2), Detailed File Migration Instructions, `server/api/containers.py`, `server/api/players.py`, `server/api/rooms.py`, `server/services/combat_service.py`, `server/services/user_manager.py`, Services (Phase 4)

### Community 1296 - "✅ Phase 2 Async Persistence Migration - COMPLETE"
Cohesion: 0.25
Nodes (7): 🏆 Achievement Summary, 📝 Git Commit Message, 📋 Migration Checklist, 🎯 Mission Accomplished, Phase 1 + Phase 2 Complete, ✅ Phase 2 Async Persistence Migration - COMPLETE, Status**: ✅**100% COMPLETE

### Community 1297 - "UUID"
Cohesion: 0.18
Nodes (6): datetime, UUID, Get multiple players by IDs in a single query., Soft delete a player (sets is_deleted=True)., Delete a player from the database., Update the last_active timestamp for a player.

### Community 1298 - "initialize_components"
Cohesion: 0.29
Nodes (8): initialize_components(), Any, Component hook coordination for freshly minted item instances., Prepare component state metadata for a new item instance. This routine…, Unit tests for item component hooks., test_initialize_components_empty_prototype(), test_initialize_components_merges_overrides(), test_initialize_components_records_prototype_components()

### Community 1299 - "NPCCombatIntegration"
Cohesion: 0.16
Nodes (23): NPCCombatIntegration, Publish NPC attack event to event bus., Integrates NPCs with the existing combat and game mechanics systems. Extends…, Handle NPC death and related effects. Args: npc_id: ID of the dead NPC room_id:…, integration(), asyncio, fixture, Unit tests for NPCCombatIntegrationBase helpers. (+15 more)

### Community 1300 - "SystemAdminChannelStrategy"
Cohesion: 0.25
Nodes (7): Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy. Args: channel_type: Type of…, SystemAdminChannelStrategy, Test SystemAdminChannelStrategy.broadcast() broadcasts globally., Personal system messages deliver to target_player_id only., test_system_admin_channel_strategy_broadcast(), test_system_admin_channel_strategy_personal_target()

### Community 1301 - "Client Updates System Audit"
Cohesion: 0.67
Nodes (3): Architecture Review Plan, Option C Replacement Client Updates, Client Updates System Audit

### Community 1302 - "AttributeError"
Cohesion: 0.02
Nodes (151): AttributeError, broadcast_room_update(), build_room_update_event(), get_npc_occupants_fallback(), get_npc_occupants_from_lifecycle_manager(), get_player_occupants(), Any, WebSocket room update and broadcast functions for MythosMUD real-time… (+143 more)

### Community 1303 - "SecureBaseModel"
Cohesion: 0.25
Nodes (8): Pydantic schemas for Invite model. This module defines Pydantic schemas for…, Pydantic schemas for User model. This module defines Pydantic schemas for user…, BaseModel, Base Pydantic model classes for MythosMUD schemas. This module provides base…, Base model with standard security configuration. All models that handle user…, Base model for API response schemas. Response models may need additional…, ResponseBaseModel, SecureBaseModel

### Community 1304 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., party_invite producer emits a build_event-shaped envelope., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success() (+3 more)

### Community 1305 - "test_run_make_stages.py"
Cohesion: 0.39
Nodes (6): _load_module(), Tests for scripts/run_make_stages.py fail-fast helpers., test_keep_going_requested(), test_stage_failed_from_output_nonzero(), test_stage_failed_from_output_ok(), test_stage_failed_from_output_traceback()

### Community 1306 - "Any"
Cohesion: 0.14
Nodes (10): Any, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:…, Get and validate NPC lifecycle manager. Args: room_id: The room ID for logging…, Get fallback NPCs from room.get_npcs() if lifecycle manager query fails. Args:…, Process NPC IDs and convert to occupant information. Args: npc_ids: List of NPC… (+2 more)

### Community 1307 - "Aggro and Threat System Implementation Plan"
Cohesion: 0.29
Nodes (6): Aggro and Threat System Implementation Plan, Constants (locked), Integration with NPC static data (behavior_config / npc_type), Key Modules and Files, References, Status

### Community 1308 - "✅ POSITIVE FINDINGS"
Cohesion: 0.29
Nodes (7): 1. Excellent Error Boundary Implementation, 2. Proper Use of asyncio.gather with return_exceptions=True, 3. Task Tracking and Lifecycle Management, 4. Good Connection State Management, 5. Proper Async Context Managers, 6. Enhanced Structured Logging, ✅ POSITIVE FINDINGS

### Community 1309 - "🔴 CRITICAL ISSUES"
Cohesion: 0.29
Nodes (7): 1. Synchronous Blocking Operations in Async Context (CONFIRMED PERFORMANCE ISSUE), 2. asyncio.run() Called from Existing Event Loop Context, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Blocking Operations in NATS Message Handlers, 6. F-String Logging Destroying Structured Logging, 🔴 CRITICAL ISSUES

### Community 1311 - "messaging_integration"
Cohesion: 0.40
Nodes (5): messaging_integration(), mock_connection_manager(), fixture, Create mock connection manager., Create CombatMessagingIntegration instance.

### Community 1312 - "✅ Positive Findings"
Cohesion: 0.29
Nodes (7): 1. Consistent Pattern Application, 2. Proper Async Propagation, 3. Exception Handling Preserved, 4. Resource Cleanup Maintained, 5. Proper Import Organization, 6. Documentation Added, ✅ Positive Findings

### Community 1313 - "🚫 Anti-Patterns NOT Found (Good!)"
Cohesion: 0.29
Nodes (7): 🚫 Anti-Patterns NOT Found (Good!), ❌ Calling async without await, ❌ Creating tasks without tracking, ❌ Global state issues, ❌ Nested event loops, ❌ Not closing resources, ❌ Using time.sleep() in async functions

### Community 1314 - "Entries"
Cohesion: 0.29
Nodes (6): 2026-02-24 — Wave 3 (Backend security) completed, 2026-02-24 — Wave 4 (Frontend security) verified, 2026-02-24 — Wave 5 (Complexity refactors), 2026-02-24 — Wave 6 (Metrics and hardening), Codacy High/Critical Remediation Progress, Entries

### Community 1315 - "Migration Workflow (Per File)"
Cohesion: 0.29
Nodes (7): Migration Workflow (Per File), Step 1: Pre-Migration Assessment, Step 2: Create Async Repository Instances, Step 3: Convert Methods to Async, Step 4: Update All Callers, Step 5: Test Migration, Step 6: Validate Performance

### Community 1316 - "Recommended Decision"
Cohesion: 0.29
Nodes (7): Commit to full 2-month optimization plan, Implement gap filling only (skip pruning), Implement only Phase 1 (Quick Wins), Option A: Full Optimization (Recommended), Option B: Quick Wins Only, Option C: Strategic Focus, Recommended Decision

### Community 1317 - "3.3 Value Distribution Calculation"
Cohesion: 0.29
Nodes (7): 3.1 Scoring Criteria Matrix, 3.2 Category Scores, 3.3 Value Distribution Calculation, 🔴 CRITICAL VALUE TESTS (Score ≥75): **1,272 tests (25.6%)**, 🟡 IMPORTANT VALUE TESTS (Score 50-74): **2,943 tests (59.3%)**, 🟢 LOW VALUE TESTS (Score <50): **750 tests (15.1%)**, Phase 3: Test Value Scoring

### Community 1318 - "Projected Optimization Impact"
Cohesion: 0.29
Nodes (7): After Phase 1-3: Pruning (Month 1), After Phase 4: Consolidation (Month 2), After Phase 5: Gap Filling (Month 2), Current State (Baseline), Final State Comparison, Net Benefit, Projected Optimization Impact

### Community 1319 - "._build_connection_stats"
Cohesion: 0.25
Nodes (4): Count how many sessions have each connection-count size., Return (avg, max, min) connection ages; zeros when the list is empty., Compose connection statistics payload (extracted to keep get_connection_stats…, Get comprehensive connection statistics. Args: player_websockets: Player to…

### Community 1320 - "gh-stack (MythosMUD)"
Cohesion: 0.20
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1321 - "Mypy Type Checking Remediation Prompt - AI-Optimized Version"
Cohesion: 0.20
Nodes (9): 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, Common Mypy Error Codes, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, 📊 MYPY ERROR CODE CATEGORIZATION GUIDE, Mypy Type Checking Remediation Prompt - AI-Optimized Version (+1 more)

### Community 1324 - "items"
Cohesion: 0.33
Nodes (6): items, minItems, type, additionalProperties, properties, holidays

### Community 1325 - "🔍 Anti-Pattern Check"
Cohesion: 0.33
Nodes (6): 🔍 Anti-Pattern Check, ❌ Blocking Calls in Async Functions?, ❌ Ignoring Exceptions?, ❌ Long-Running Coroutines?, ❌ Missing `await` Keywords?, ❌ Unstructured Concurrency?

### Community 1326 - "📚 Documentation Created"
Cohesion: 0.33
Nodes (6): 1. Comprehensive Audit Report, 2. Executive Summary, 3. Developer Quick Reference, 4. Migration Tracker, 5. Test Suite, 📚 Documentation Created

### Community 1327 - "Summary (from Codacy UI snapshot)"
Cohesion: 0.33
Nodes (5): Codacy High/Critical Baseline – MythosMUD, Distribution notes, Example issue types, Summary (from Codacy UI snapshot), Top code patterns by issue count

### Community 1328 - "Core Logging Principles"
Cohesion: 0.33
Nodes (6): 1. **Structured Logging**, 2. **Context is Everything**, 3. **Security First**, 4. **Performance Aware**, 5. **Actionable Information**, Core Logging Principles

### Community 1329 - "Common Mistakes and How to Fix Them"
Cohesion: 0.33
Nodes (6): Common Mistakes and How to Fix Them, Mistake 1: Forgetting to Update Imports, Mistake 2: Using Deprecated Context Parameter, Mistake 3: String Formatting in Log Messages, Mistake 4: Missing Context in Error Logs, Mistake 5: Wrong Log Levels

### Community 1331 - "Enhanced Logging Features"
Cohesion: 0.33
Nodes (6): Correlation IDs, Enhanced Logging Features, Exception Tracking, MDC (Mapped Diagnostic Context), Performance Monitoring, Security Sanitization

### Community 1333 - "Log Levels and Usage"
Cohesion: 0.33
Nodes (6): CRITICAL, DEBUG, ERROR, INFO, Log Levels and Usage, WARNING

### Community 1334 - "Enhanced Logging Migration Report"
Cohesion: 0.33
Nodes (5): Enhanced Logging Features, Enhanced Logging Migration Report, Next Steps, Successfully Updated Files, Summary

### Community 1335 - "Mythos Holiday Candidates"
Cohesion: 0.33
Nodes (5): Canonical and Derived Observances, Implementation Notes, Mythos Holiday Candidates, Narrative Flavor Seeds, Opportunities for Expansion

### Community 1336 - "💡 Key Improvements"
Cohesion: 0.33
Nodes (6): 1. Eliminated Event Loop Blocking, 2. Consistent Async Patterns, 3. Proper Error Handling, 4. Resource Management, 5. Performance Optimization, 💡 Key Improvements

### Community 1337 - "PostgreSQL Procedures Migration - Audit Spreadsheet"
Cohesion: 0.33
Nodes (5): Audit Table, Domain Grouping Summary, Existing PostgreSQL Functions (Already in DDL), PostgreSQL Procedures Migration - Audit Spreadsheet, Scope

### Community 1338 - "Real-Time Communication (WebSocket)"
Cohesion: 0.33
Nodes (5): Authentication and Token in URL, Connection Grace Periods, Deprecated Endpoints, Production: HTTPS and WSS, Real-Time Communication (WebSocket)

### Community 1339 - "Implementation Approach Decision"
Cohesion: 0.33
Nodes (6): Alternative: **GREENFIELD REWRITE**, Cons, Implementation Approach Decision, Pros, Recommended: **PHASED UPLIFT**, Would Choose If

### Community 1340 - "test_lifecycle_respawn.py"
Cohesion: 0.18
Nodes (26): Process the respawn queue and spawn NPCs that are ready (delegates to…, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…, Process the respawn queue and spawn NPCs that are ready. Args: manager:… (+18 more)

### Community 1341 - "Backward Compatibility Strategy"
Cohesion: 0.33
Nodes (6): Backward Compatibility Strategy, Layer 1: New Tests (Use Container), Layer 2: Updated Tests (Hybrid), Layer 3: Legacy Tests (Unchanged), Migration Flags, Three-Layer Compatibility

### Community 1342 - "rename_used_to_is_active.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to rename used back to is_active. Args: database_url:…

### Community 1343 - "Test Suite Analysis"
Cohesion: 0.33
Nodes (6): Current Test Organization, Dependency Access Patterns, Pattern 1: Direct app.state Access (Broken - 445 instances), Pattern 2: Using Real Lifespan (Works - Limited), Pattern 3: Fixture-Based Mocking (Mixed), Test Suite Analysis

### Community 1344 - "Modern Testing Patterns"
Cohesion: 0.33
Nodes (6): Modern Testing Patterns, Pattern 1: Container-Based Fixtures, Pattern 2: Mock Container for Unit Tests, Pattern 3: Parametrized Integration Tests, Pattern 4: Fixture Factories, Pattern 5: Async Test Context Managers

### Community 1345 - "Test Modernization Checklist"
Cohesion: 0.33
Nodes (6): Phase 0: Foundation, Phase 1: Fix Failures, Phase 2: Modernize Units, Phase 3: Pattern Updates, Phase 4: New Coverage, Test Modernization Checklist

### Community 1346 - "Testing Requirements"
Cohesion: 0.33
Nodes (6): Phase 0 Testing, Phase 1 Testing, Phase 2 Testing, Phase 3 Testing, Phase 4 Testing, Testing Requirements

### Community 1347 - "Test Suite Optimization Roadmap"
Cohesion: 0.33
Nodes (5): Recommended Execution Order, Risk Mitigation Strategy, Rollback Plan, Safety Measures, Test Suite Optimization Roadmap

### Community 1348 - "Phase 5: Strategic Additions (Week 5)"
Cohesion: 0.33
Nodes (6): Phase 5: Strategic Additions (Week 5), Task 5.1: Add MessageBroker Integration Tests (3 hours), Task 5.2: Add ApplicationContainer Lifecycle Tests (2 hours), Task 5.3: Add Database Migration Tests (3 hours), Task 5.4: Add WebSocket Edge Case Tests (4 hours), Task 5.5: Add Error Recovery Tests (3 hours)

### Community 1350 - "Measurement and Validation"
Cohesion: 0.33
Nodes (6): After Each Phase, Before Starting Optimization, Capture Baseline, Measurement and Validation, Verify Metrics, Weekly Dashboard

### Community 1352 - "_run_dialogue_ddl"
Cohesion: 0.40
Nodes (5): main(), cursor, Create dialogue_definitions table if missing in the given schema., Connect via DATABASE_URL and ensure dialogue_definitions exists., _run_dialogue_ddl()

### Community 1353 - "bench_cache_professions.py"
Cohesion: 0.31
Nodes (7): bench_profession_cache(), _FakePersistence, _get_empty_dict(), main(), Any, Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…, Helper function to return empty dict for mock methods.

### Community 1354 - "mock_app"
Cohesion: 0.29
Nodes (7): mock_app(), mock_container(), mock_player(), fixture, Create a mock FastAPI app., Create a mock ApplicationContainer., Create a mock player.

### Community 1355 - "check_file"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1356 - "lucidity_migration.py"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1357 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 1358 - "._attack_target_impl"
Cohesion: 0.20
Nodes (5): Resolve attack_damage from behavior config with robust typing., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target., Attack a specific target., Handle attacking target action.

### Community 1359 - "npc_utils.py"
Cohesion: 0.24
Nodes (9): extract_room_id_from_lifecycle_record(), Any, NPC Utility Functions. This module provides utility functions for extracting…, Return stable room id for zone parsing; strip instance_<uuid>_ prefix if…, Return usable room_id from a single lifecycle event, if present., Return the latest non-unknown room_id from a lifecycle record's events, if any., _room_id_from_lifecycle_event(), _stable_room_id_for_zone() (+1 more)

### Community 1360 - "players/player_respawn.py"
Cohesion: 0.22
Nodes (8): BaseModel, Player respawn API response schemas for MythosMUD server. This module provides…, Simplified player data returned in respawn responses., RespawnPlayerData, BaseModel, Room data schema for MythosMUD. This module defines Pydantic models for room…, Room data structure for API responses. This model represents room information…, RoomData

### Community 1361 - "_FakeMessageQueue"
Cohesion: 0.20
Nodes (3): _FakeMessageQueue, _FakeRateLimiter, _FakeRoomManager

### Community 1362 - "TestResolveExitTarget"
Cohesion: 0.20
Nodes (6): Room without a reverse exit is not considered bidirectional., If the target room ID does not exist, the helper returns None., If the target room lacks map coordinates, the helper returns None., Tests for _resolve_exit_target., Room with a reverse exit is treated as bidirectional and returns its…, TestResolveExitTarget

### Community 1364 - "🎓 Best Practice Examples to Share"
Cohesion: 0.40
Nodes (4): 🎓 Best Practice Examples to Share, Example 1: Proper Blocking Operation Offloading, Example 2: Caching with TTL, Example 3: Exception Handling for Connection Failures

### Community 1366 - "Common Conversion Patterns"
Cohesion: 0.40
Nodes (5): Common Conversion Patterns, Pattern 1: Simple Query, Pattern 2: Batch Operations, Pattern 3: Health Operations, Pattern 4: FastAPI Dependency Injection

### Community 1367 - "TestHorizontalExitCharBetween"
Cohesion: 0.20
Nodes (6): Tests for _horizontal_exit_char_between (em dash, >, <)., Bidirectional horizontal exit between two rooms uses an em dash., One-way east exit renders as a greater-than sign., One-way west exit renders as a less-than sign., When there are no horizontal exits, the helper returns None., TestHorizontalExitCharBetween

### Community 1368 - "Gotchas & Solutions"
Cohesion: 0.40
Nodes (5): Gotcha 1: Async Propagation, Gotcha 2: Mixing Sync and Async, Gotcha 3: Transaction Management, Gotcha 4: Testing Async Code, Gotchas & Solutions

### Community 1369 - "🎭 Closing Remarks"
Cohesion: 0.40
Nodes (5): Adjusts spectacles with profound satisfaction, 🎭 Closing Remarks, December 3, 2025, Status**: ✅**PHASE 2 COMPLETE - READY FOR TESTING, "The last synchronous operation has been banished to the thread pool, where it belongs."

### Community 1370 - "Financial Impact (If You're Tracking Dev Time)"
Cohesion: 0.40
Nodes (5): CI/CD Time Saved, Developer Time Saved, Financial Impact (If You're Tracking Dev Time), Maintenance Time Saved, Time Savings Calculation

### Community 1371 - "Phase 1: Quick Wins (Week 1)"
Cohesion: 0.40
Nodes (5): Phase 1: Quick Wins (Week 1), Task 1.1: Remove Placeholder Tests (30 minutes), Task 1.2: Remove Trivial Type Assertions (1 hour), Task 1.3: Remove Duplicate Tests (30 minutes), Task 1.4: Delete Empty Test File (5 minutes)

### Community 1373 - "Phase 2: Infrastructure Test Reduction (Week 2)"
Cohesion: 0.40
Nodes (5): Phase 2: Infrastructure Test Reduction (Week 2), Task 2.1: Reduce Dependency Injection Tests (2 hours), Task 2.2: Consolidate Dependency Injection Test Files (2 hours), Task 2.3: Reduce App Factory Tests (1 hour), Task 2.4: Review Lifespan Tests (1 hour)

### Community 1374 - "Phase 4: Test Consolidation (Week 4)"
Cohesion: 0.40
Nodes (5): Phase 4: Test Consolidation (Week 4), Task 4.1: Parametrize Command Validation Tests (4 hours), Task 4.2: Parametrize Error Response Tests (3 hours), Task 4.3: Parametrize Permission Tests (2 hours), Task 4.4: Consolidate Similar Integration Tests (3 hours)

### Community 1375 - "Phase 6: Long-Term Optimizations (Ongoing)"
Cohesion: 0.40
Nodes (5): Phase 6: Long-Term Optimizations (Ongoing), Task 6.1: Establish Test Quality Gates, Task 6.2: Monthly Test Quality Review, Task 6.3: Performance Optimization, Task 6.4: Parallel Test Execution (Investigation)

### Community 1376 - "Phase 1: Quantitative Analysis Results"
Cohesion: 0.40
Nodes (5): 1.1 Test Distribution by Category, 1.2 Largest Test Files (Splitting/Pruning Candidates), 1.3 Infrastructure Test Analysis, Files, Phase 1: Quantitative Analysis Results

### Community 1379 - "Summary: Test Quality Metrics"
Cohesion: 0.40
Nodes (5): By removing 15% of tests, we, Current State, Optimized State (After Pruning), Summary: Test Quality Metrics, Value Proposition

### Community 1380 - "Risk Assessment and Mitigation"
Cohesion: 0.40
Nodes (5): Automatic Rollback If, Review and Reconsider If, Risk Assessment and Mitigation, Risks by Phase, Rollback Triggers

### Community 1381 - "Map Regression Tests Proposal"
Cohesion: 0.67
Nodes (3): ASCII Map Context Preparation, ASCII Minimap Generation, Map Regression Tests Proposal

### Community 1382 - "Configuration Files Reference"
Cohesion: 0.40
Nodes (5): Configuration File Tuples, Configuration Files Reference, .env.local Secrets Pattern, COPPA Compliance Checklist, Development Environment Setup

### Community 1383 - "A Cold Fire Within (source summary)"
Cohesion: 0.50
Nodes (3): A Cold Fire Within (source summary), For MythosMUD design, Links

### Community 1384 - "Alone Against the Dark (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Dark (source summary), For MythosMUD design, Links

### Community 1385 - "Workflows"
Cohesion: 0.22
Nodes (9): End-to-end: create a stack from scratch, Handle rebase conflicts (agent workflow), Making mid-stack changes, Modify a mid-stack branch and sync, Parsing `--json` output, Restructure a stack (remove a branch, reorder, or rename), Routine sync after merges, Squash-merge recovery (+1 more)

### Community 1386 - "Alone Against the Frost (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Frost (source summary), For MythosMUD design, Links

### Community 1387 - ".claude/commands/multiplayer-playwright-testing.md"
Cohesion: 0.22
Nodes (8): 🎯 AVAILABLE SCENARIOS, 🚨 CRITICAL AI EXECUTOR REQUIREMENTS 🚨, 📋 EXECUTION OPTIONS, 📖 MANDATORY EXECUTION ORDER, 🛑 MANDATORY EXECUTION PROTOCOL 🛑, 🎮 MODULAR E2E TEST SUITE STRUCTURE 🎮, 🔧 TESTING APPROACH, 📝 USAGE EXAMPLES

### Community 1388 - "Alone against the Tide (source summary)"
Cohesion: 0.50
Nodes (3): Alone against the Tide (source summary), For MythosMUD design, Links

### Community 1389 - "NPCActionMessage"
Cohesion: 0.09
Nodes (18): Check if idle movement should be scheduled based on configuration and timing.…, Create a WANDER action message. Args: current_time: Current timestamp Returns:…, Queue a WANDER action via the thread manager. Args: wander_action: The wander…, Schedule a WANDER action for idle movement if interval has elapsed. This method…, Handle wandering action., Perform wandering behavior using idle movement system., NPCActionMessage, NPCActionType (+10 more)

### Community 1390 - "spell_effects_support.py"
Cohesion: 0.11
Nodes (34): apply_stat_modifications(), Stat modification helpers for spell effects. This module contains utility…, Apply stat modification dict to stats. Returns (updated stats, stat_changes,…, _apply_stat_modify_to_player(), _build_stat_modifications(), _create_object_for_player(), _create_object_for_room(), process_create_object_effect() (+26 more)

### Community 1391 - "client/package.json"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 1392 - "include"
Cohesion: 0.11
Nodes (17): compilerOptions, noEmit, types, exclude, extends, include, node, src/**/*.spec.ts (+9 more)

### Community 1393 - "vite.userConfig.ts"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1394 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.22
Nodes (9): For Each Issue Category, 🎯 MANDATORY AI EXECUTION PROTOCOL, Mypy Type Checking, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide, Phase 6: Verification Protocol, Phase 7: Success Validation (+1 more)

### Community 1395 - "Berlin - The Wicked City (source summary)"
Cohesion: 0.50
Nodes (3): Berlin - The Wicked City (source summary), For MythosMUD design, Links

### Community 1396 - "main"
Cohesion: 0.31
Nodes (8): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Entry point: read hook payload from stdin, check edited-files state, and…

### Community 1398 - "main"
Cohesion: 0.31
Nodes (8): _exit_empty(), _load_state(), main(), NoReturn, Path, Exit successfully with no decision (allow the stop)., Load and validate edited-files state. Returns None if missing or invalid., Entry point: read hook payload from stdin, check edited-files state, and…

### Community 1399 - "Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary), For MythosMUD design, Links

### Community 1400 - "Motion Design"
Cohesion: 0.22
Nodes (8): Duration: The 100/300/500 Rule, Easing: Pick the Right Curve, Motion Design, Perceived Performance, Performance, Reduced Motion, Staggered Animations, The Only Two Properties You Should Animate

### Community 1401 - "Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition Keeper Screen Pack (source summary), For MythosMUD design, Links

### Community 1402 - "_collect_python_public_defs_and_tiny"
Cohesion: 0.23
Nodes (12): _check_exports_and_tiny_functions(), _collect_python_public_defs_and_tiny(), _is_public_function_stmt(), _is_test_file_path(), _is_tiny_single_use(), AST, AsyncFunctionDef, FunctionDef (+4 more)

### Community 1403 - "Call of Cthulhu Investigator Handbook 7th Edition (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Investigator Handbook 7th Edition (source summary), For MythosMUD design, Links

### Community 1404 - "handle_system_command"
Cohesion: 0.24
Nodes (11): handle_system_command(), Any, Broadcast a system-level message via the chat service if available., asyncio, Unit tests for system command handlers. Tests the system command functionality., Test handle_system_command() broadcasts system message., Test handle_system_command() handles missing message., Test handle_system_command() handles missing chat service. (+3 more)

### Community 1405 - "Call of Cthulhu Keeper Tips (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Keeper Tips (source summary), For MythosMUD design, Links

### Community 1406 - "test_users.py"
Cohesion: 0.03
Nodes (118): AuthenticationBackend, JWT strategy that rejects tokens issued before the current server start., RestartInvalidatingJWTStrategy, get_auth_backend(), get_user_db(), get_user_manager(), get_username_auth_backend(), AsyncSession (+110 more)

### Community 1407 - "Frontend Aesthetics Guidelines"
Cohesion: 0.22
Nodes (9): Color & Theme, Frontend Aesthetics Guidelines, Interaction, Layout & Space, Motion, Responsive, Typography, UX Writing (+1 more)

### Community 1408 - "Call of Cthulhu Starter Set (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Starter Set (source summary), For MythosMUD design, Links

### Community 1409 - "Call of Cthulhu_ The Coloring Book (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu_ The Coloring Book (source summary), For MythosMUD design, Links

### Community 1410 - "._get_vertical_exit_char"
Cohesion: 0.22
Nodes (6): _ExitRowContext, NamedTuple, Render a single row of vertical exits between room rows., Viewport and style context for vertical exit row rendering., Return the vertical exit character (|, v, or ^) given south/north exit state,…, Get exit character to display between rows for vertical (north/south) exits.…

### Community 1411 - "CommandProcessor"
Cohesion: 0.13
Nodes (12): command_processor(), fixture, Create a CommandProcessor instance., Test get_command_processor returns global instance., Test process_command_string handles Pydantic validation errors., test_get_command_processor(), test_process_command_string_pydantic_validation_error(), CommandProcessor (+4 more)

### Community 1412 - "event_handler"
Cohesion: 0.22
Nodes (9): event_handler(), mock_connection_manager(), mock_event_bus(), mock_task_registry(), fixture, Create a mock EventBus., Create a mock ConnectionManager., Create a mock TaskRegistry. (+1 more)

### Community 1413 - "mock_utils"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_logger(), mock_utils(), player_respawn_event_handler(), fixture, Create a mock connection manager., Create a mock PlayerEventHandlerUtils., Create a mock logger. (+1 more)

### Community 1414 - "MythosMUD Server Runbook Skill"
Cohesion: 0.67
Nodes (3): MythosMUD Server Runbook Skill, MythosMUD Worktree Workflow Skill, One Server Only Rule

### Community 1415 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 1416 - "1. Component Refactoring"
Cohesion: 0.50
Nodes (4): 1. Component Refactoring, ChatPanel.tsx Enhancements (New Chat Input Panel), CommandPanel.tsx Simplifications, GameLogPanel.tsx (Renamed from ChatPanel.tsx)

### Community 1417 - "player_event_handler_utils"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), fixture, Create a mock connection manager., Create a mock name extractor., Create a mock logger. (+1 more)

### Community 1418 - "asyncio"
Cohesion: 0.22
Nodes (9): asyncio, Test get_player_info() returns None for invalid player_id., Test get_player_info() returns None when player not found., Test get_player_info() successfully retrieves player info., Test get_player_info() returns None when connection manager not available., test_get_player_info_invalid_player_id(), test_get_player_info_no_connection_manager(), test_get_player_info_player_not_found() (+1 more)

### Community 1419 - ".execute_idle_movement"
Cohesion: 0.10
Nodes (12): _cfg_bool(), _cfg_float(), _npc_id_str(), _passes_movement_probability(), Get exits from current room that stay within subzone boundaries. Args:…, Calculate weight for an exit based on distance from spawn. Args:…, Calculate weights for all exits. Args: valid_exits: Dictionary of direction ->…, Select exit based on weighted probabilities. Args: exit_weights: List of… (+4 more)

### Community 1420 - "webhook"
Cohesion: 0.50
Nodes (4): post, Request, Receive and log alert webhooks, webhook()

### Community 1421 - "character_sheets (source summary)"
Cohesion: 0.50
Nodes (3): character_sheets (source summary), For MythosMUD design, Links

### Community 1422 - "Room Pathing Validator Implementation Spec"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1423 - "validator.py CLI"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1424 - "Cthulhu Dark Ages - 3rd Edition (source summary)"
Cohesion: 0.50
Nodes (3): Cthulhu Dark Ages - 3rd Edition (source summary), For MythosMUD design, Links

### Community 1425 - "Dead Light and Other Dark Turns (source summary)"
Cohesion: 0.50
Nodes (3): Dead Light and Other Dark Turns (source summary), For MythosMUD design, Links

### Community 1426 - "_filter_lines"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after…, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1427 - "fix_room_references"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area. Args: base_path: Path to the…, save_room_file()

### Community 1428 - "player_inventory_migration.py"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1429 - "Does Love Forgive_ (source summary)"
Cohesion: 0.50
Nodes (3): Does Love Forgive_ (source summary), For MythosMUD design, Links

### Community 1430 - "run_bug_prevention_tests.ps1"
Cohesion: 0.53
Nodes (8): Invoke-ClientTest(), Invoke-IntegrationTest(), Invoke-ServerTest(), Show-TestSummary(), Test-Command(), Write-ColorOutput(), Write-Header(), Write-Section()

### Community 1431 - "Doors to Darkness (source summary)"
Cohesion: 0.50
Nodes (3): Doors to Darkness (source summary), For MythosMUD design, Links

### Community 1432 - "Down Darker Trails (source summary)"
Cohesion: 0.50
Nodes (3): Down Darker Trails (source summary), For MythosMUD design, Links

### Community 1433 - "test_logging_handlers.py"
Cohesion: 0.04
Nodes (65): _aggregator_handler_class_for_windows(), AsyncioConnLostWriteFilter, create_aggregator_handler(), _make_exec_for_aggregator(), Any, LogRecord, Path, RotatingFileHandler (+57 more)

### Community 1434 - "Gateways to Terror (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Gateways to Terror (source summary), Links

### Community 1435 - "Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)

### Community 1436 - "Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)

### Community 1437 - "The Grand Grimoire of Cthulhu Mythos Magic (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Grand Grimoire of Cthulhu Mythos Magic (source summary)

### Community 1439 - "The Malleus Monstrorum Keeper Deck (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Malleus Monstrorum Keeper Deck (source summary)

### Community 1440 - "fixture"
Cohesion: 0.18
Nodes (11): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), fixture, Create a mock room manager., Create a mock get_async_persistence callback. (+3 more)

### Community 1441 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1442 - "persistence/container_helpers.py"
Cohesion: 0.18
Nodes (16): Composed, build_update_query(), _coerce_row_quantity(), fetch_container_items(), _item_dict_from_contents_row(), _metadata_dict_from_cell(), datetime, PsycopgConnection (+8 more)

### Community 1443 - "ItemPrototypeModel"
Cohesion: 0.11
Nodes (22): Constants supporting item prototype validation. These enumerations anchor the…, ItemPrototypeModel, BaseModel, field_validator, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validated representation of an item prototype definition. This model keeps the…, Validate that item_type is in the allowed list. Args: value: The item type to… (+14 more)

### Community 1444 - "HADS tooling (MythosMUD)"
Cohesion: 0.40
Nodes (4): HADS tooling (MythosMUD), Policy, Source pin, Usage

### Community 1445 - "RateLimiter"
Cohesion: 0.22
Nodes (7): fixture, rate_limiter(), Create a RateLimiter instance for testing., Utility modules for MythosMUD server. This package contains various utility…, RateLimiter, Simple in-memory rate limiter for API endpoints. This rate limiter tracks…, Initialize the rate limiter. Args: max_requests: Maximum number of requests…

### Community 1446 - ".extract_command_data"
Cohesion: 0.25
Nodes (5): Any, Extract attributes from validated command using a mapping configuration. Args:…, Check if a command type is a combat command. Args: command_type: The command…, Extract command data from a validated Pydantic command object. This method…, Process a raw command string through the new validation system. Args:…

### Community 1448 - "cli.sh"
Cohesion: 0.39
Nodes (6): download(), download_cli(), download_file(), get_latest_version(), handle_rate_limit(), cli.sh script

### Community 1474 - "Whisper NATS Subject Bug Fix"
Cohesion: 0.25
Nodes (8): Admin Teleportation Display Bug, E2E Session Report 2025-12-02, Whisper Messages Not Received Bug, chat.whisper.player Subject Segment, Whisper NATS Subject Bug Fix, Missing player Segment Root Cause, Whisper System Investigation, Whisper Work Completed and Remaining

### Community 1476 - "Event-Sourced Projector"
Cohesion: 0.32
Nodes (8): Event-Sourced Projector, Client Event Schema, game_state Event, GameState, room_state Event, Critical State Handoffs, Enter-Room Request/Response, Server Authority Over Client

### Community 1480 - "Impeccable design context"
Cohesion: 0.67
Nodes (3): Impeccable design context, Legibility under pressure, Dark terminal-first aesthetic

### Community 1487 - "ensure_directory_exists"
Cohesion: 0.25
Nodes (8): ensure_directory_exists(), Ensure a directory exists and return its absolute path. Args: directory: The…, Test ensure_directory_exists with existing directory., Test ensure_directory_exists creates directory if it doesn't exist., Test ensure_directory_exists with relative path., test_ensure_directory_exists_creates(), test_ensure_directory_exists_existing(), test_ensure_directory_exists_relative_path()

### Community 1490 - "Any"
Cohesion: 0.25
Nodes (6): benchmark_model_memory_usage(), Any, Compare memory usage across multiple model classes. Args: model_classes: List…, Print formatted model memory usage results., Print formatted comparison results., Benchmark memory usage for all major models.

### Community 1491 - "migrate_file"
Cohesion: 0.36
Nodes (7): main(), migrate_file(), MigrationResult, NamedTuple, Path, Result of a file migration., Migrate a single file to use async persistence patterns. Args: file_path: Path…

### Community 1492 - "gh-stack"
Cohesion: 0.25
Nodes (8): Agent rules, Exit codes and error recovery, gh-stack, Known limitations, Output conventions, Prerequisites, Quick reference, When to use this skill

### Community 1494 - "Step 2: Ask UX-Focused Questions"
Cohesion: 0.25
Nodes (7): Accessibility & Inclusion, Aesthetic Preferences, Brand & Personality, Step 1: Explore the Codebase, Step 2: Ask UX-Focused Questions, Step 3: Write Design Context, Users & Purpose

### Community 1501 - "main"
Cohesion: 0.36
Nodes (7): main(), cursor, Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial),…, Create quest_definitions, quest_instances, quest_offers tables and indexes., Insert leave_the_tutorial quest definition and room offer (idempotent)., _run_quest_ddl(), _seed_leave_the_tutorial()

### Community 1502 - "apply_migration"
Cohesion: 0.36
Nodes (7): apply_migration(), check_schema(), main(), Cursor, Path, Check current schema of npc_spawn_rules table, Apply the migration to rename columns

### Community 1536 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1540 - "Persistence Repository Layer"
Cohesion: 0.50
Nodes (4): Persistence Repository Architecture, Persistence Repository Layer, PostgreSQL Contributor Guide, PostgreSQL Stored Procedures Pattern

### Community 1546 - "test_logging_processors.py"
Cohesion: 0.04
Nodes (80): EventDict, configure_enhanced_structlog(), Configure enhanced Structlog with MDC, security, and performance features.…, add_correlation_id(), add_request_context(), _database_error_type(), _enhance_one_player_id(), enhance_player_ids() (+72 more)

### Community 1550 - "Lucidity System Expansion Scenarios"
Cohesion: 0.67
Nodes (4): Lucidity System Expansion Scenarios, Catatonia Grounding Ritual Scenario, player_lucidity Ledger, Sanitarium Failover Escalation

### Community 1556 - "calculate_notification_times"
Cohesion: 0.25
Nodes (8): calculate_notification_times(), Calculate notification times for countdown. Notifications occur: - Every 10…, Test calculate_notification_times() for short countdown., Test calculate_notification_times() for long countdown., Test calculate_notification_times() returns sorted descending., test_calculate_notification_times_long(), test_calculate_notification_times_short(), test_calculate_notification_times_sorted()

### Community 1557 - "📚 REFERENCES AND RESOURCES"
Cohesion: 0.50
Nodes (4): Best Practice Documents, External Resources, Investigation Reports, 📚 REFERENCES AND RESOURCES

### Community 1558 - "📊 METRICS AND SUCCESS CRITERIA"
Cohesion: 0.50
Nodes (4): Code Quality Metrics, 📊 METRICS AND SUCCESS CRITERIA, Performance Metrics, Test Coverage

### Community 1559 - "WebSocket-Only Migration"
Cohesion: 0.33
Nodes (6): SSE Connection Removal, Unified Client Message Pipeline, Unify Client Message Handling, WebSocket Best-Practices Remediation, WebSocket-Only Architecture, WebSocket-Only Migration

### Community 1560 - "NPCThreadManager"
Cohesion: 0.07
Nodes (33): NPCCommunicationBridge, NPCMessageQueue, NPCThreadManager, Initialize the NPC message queue. Args: max_messages_per_npc: Maximum number of…, Clear all pending messages for an NPC. Args: npc_id: The NPC's ID Returns:…, Get the number of pending messages for an NPC., Get the total number of pending messages across all NPCs., Manages NPC threads and their lifecycle. This class handles the creation,… (+25 more)

### Community 1561 - "intersection_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1562 - "🚀 DEPLOYMENT STRATEGY"
Cohesion: 0.50
Nodes (4): 🚀 DEPLOYMENT STRATEGY, Monitoring Post-Deployment, Pre-Deployment Checklist, Rollback Plan

### Community 1563 - "🔧 Code Changes Made"
Cohesion: 0.50
Nodes (4): 1. Fixed Event Loop Blocking in PassiveLucidityFluxService, 2. Removed asyncio.run() from Exploration Service, 3. Added Exception Handling for Database Engine Creation, 🔧 Code Changes Made

### Community 1564 - "room_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1565 - "main"
Cohesion: 0.38
Nodes (6): generate_html_visualization(), load_room_data(), main(), Load all room and intersection data from the zone directory., Main function to generate the HTML visualization., Generate an HTML visualization of the room network.

### Community 1566 - "🏆 Achievement Highlights"
Cohesion: 0.50
Nodes (4): 🏆 Achievement Highlights, Code Quality, Critical Fixes (Phase 1), Performance Optimizations

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

### Community 1571 - "🎭 Closing Remarks"
Cohesion: 0.50
Nodes (4): Adjusts spectacles with scholarly satisfaction, 🎭 Closing Remarks, "In the house of the event loop, all operations must flow as one.", Status**: ✅**REMEDIATION COMPLETE

### Community 1572 - "Chat Panel"
Cohesion: 0.29
Nodes (7): Chat Message Type Categorization Bug, Chat Panel, Commands Panel, Game Log Panel, Chat Message Routing Bug Fix, Room Description Routing Bug Fix, Bug Prevention Testing Strategy

### Community 1573 - "graceful_degradation"
Cohesion: 0.29
Nodes (6): graceful_degradation(), Context manager for graceful degradation. Provides fallback behavior when…, Test graceful_degradation context manager., Test graceful_degradation with successful operation., Test graceful_degradation catches exceptions., TestGracefulDegradation

### Community 1574 - "test_room_subscription_manager.py"
Cohesion: 0.20
Nodes (9): Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test add_room_occupant() with multiple occupants., Test add_room_occupant() adds occupant to existing room., Test remove_room_occupant() handles errors gracefully., Test unsubscribe_from_room() removes room when last subscriber leaves., test_add_room_occupant_existing_room(), test_add_room_occupant_multiple(), test_remove_room_occupant_error_handling() (+1 more)

### Community 1581 - "🎯 Performance Improvements"
Cohesion: 0.50
Nodes (4): After Fixes, Before Fixes, 🎯 Performance Improvements, Room Cache Performance

### Community 1582 - "💰 ROI Analysis"
Cohesion: 0.50
Nodes (4): Break-Even, Investment, Return, 💰 ROI Analysis

### Community 1583 - "📚 Deliverables"
Cohesion: 0.50
Nodes (4): Code Changes (4 files modified), 📚 Deliverables, Documentation (5 files, ~2,500 lines), Tests (1 file, 250+ lines)

### Community 1584 - "🚀 Deployment Readiness"
Cohesion: 0.50
Nodes (4): Critical Blockers - RESOLVED, 🚀 Deployment Readiness, Phase 2 Recommendation, Production Ready Status

### Community 1585 - "💡 Recommendations"
Cohesion: 0.50
Nodes (4): Immediate, Medium-Term (Next 2-3 Weeks), 💡 Recommendations, Short-Term (This Week)

### Community 1586 - "📞 Next Steps"
Cohesion: 0.50
Nodes (4): Immediate (Today), Medium-Term (Next Sprint), 📞 Next Steps, Short-Term (This Week)

### Community 1587 - "Context Management"
Cohesion: 0.50
Nodes (4): Context Management, Request Context, System Context, User Context

### Community 1588 - "🚨 CRITICAL ANTI-PATTERNS - DO NOT USE"
Cohesion: 0.50
Nodes (4): 🚨 CRITICAL ANTI-PATTERNS - DO NOT USE, ❌ FORBIDDEN IMPORT PATTERNS, ❌ FORBIDDEN LOGGING PATTERNS, ✅ MANDATORY CORRECT PATTERNS

### Community 1589 - "Rollback Procedures"
Cohesion: 0.50
Nodes (4): Emergency Rollback, Individual File Rollback, Phase Rollback, Rollback Procedures

### Community 1590 - "Success Metrics"
Cohesion: 0.50
Nodes (4): Overall Migration Metrics, Per-File Metrics, Per-Phase Metrics, Success Metrics

### Community 1591 - "🚀 Deployment Readiness"
Cohesion: 0.50
Nodes (4): Async Compliance, Code Quality, 🚀 Deployment Readiness, Remaining Work

### Community 1592 - "🎓 Lessons Learned"
Cohesion: 0.50
Nodes (4): Best Practices Reinforced, Challenges Encountered, 🎓 Lessons Learned, What Worked Well

### Community 1593 - "📚 Changes by Category"
Cohesion: 0.50
Nodes (4): 📚 Changes by Category, Combat/Death (2 files), Core Layer (4 files), Service Layer (8 files)

### Community 1594 - "🚦 Next Steps"
Cohesion: 0.50
Nodes (4): Immediate (Today), 🚦 Next Steps, Production Deployment, This Week

### Community 1595 - "MythosMUD Server Test Suite"
Cohesion: 0.33
Nodes (6): Command Tests Relocated, server/tests/unit/commands/, Integration Test Tier, make test-server, MythosMUD Server Test Suite, Unit Test Tier

### Community 1596 - "✅ Verification Results"
Cohesion: 0.50
Nodes (4): Linting, Result**: ✅**ALL CHECKS PASSED, Test Results, ✅ Verification Results

### Community 1597 - "Missing Test Scenarios"
Cohesion: 0.50
Nodes (4): Database Connection Loss, Missing Test Scenarios, NATS Unavailability, Room Data Corruption

### Community 1598 - "Next Steps"
Cohesion: 0.50
Nodes (4): Immediate (This Session), Medium Term (Weeks 2-6), Next Steps, Short Term (Week 1)

### Community 1599 - "Net Impact Projection"
Cohesion: 0.50
Nodes (4): After Month 1 (Pruning Phase), After Month 2 (Consolidation + Additions), After Month 3+ (Continuous Improvement), Net Impact Projection

### Community 1600 - "Implementation Timeline"
Cohesion: 0.50
Nodes (4): Implementation Timeline, Month 1: Pruning and Quick Wins, Month 2: Consolidation and Additions, Month 3+: Continuous Improvement

### Community 1601 - "Phase 3: Coverage Test Optimization (Week 3)"
Cohesion: 0.50
Nodes (4): Phase 3: Coverage Test Optimization (Week 3), Task 3.1: Reduce Command Handler Coverage Tests (3 hours), Task 3.2: Reduce Error Logging Coverage Tests (2 hours), Task 3.3: Merge Coverage Tests into Domain Tests (3 hours)

### Community 1602 - "Executive Summary"
Cohesion: 0.50
Nodes (4): Executive Summary, 🟡 IMPORTANT (Medium-Value):**~2,500-3,000 tests (50-60%) —**~15-18 minutes, Key Findings, Test Value Distribution

### Community 1603 - "Appendix: Quick Reference Commands"
Cohesion: 0.50
Nodes (4): Appendix: Quick Reference Commands, Test Analysis Commands, Test Removal Workflow, "The optimization of tests is not destruction, but refinement — removing the dross to reveal the gold beneath."

### Community 1604 - "Detailed Category Value Breakdown"
Cohesion: 0.50
Nodes (4): 🔴 CRITICAL VALUE TESTS (1,272 tests = 25.6%), Detailed Category Value Breakdown, 🟡 IMPORTANT VALUE TESTS (2,943 tests = 59.3%), 🟢 LOW VALUE TESTS (750 tests = 15.1%)

### Community 1605 - "Time Distribution Analysis"
Cohesion: 0.50
Nodes (4): Current Time Allocation, Highest Impact (Remove), Optimization Targets, Time Distribution Analysis

### Community 1606 - "Container System API Reference"
Cohesion: 0.50
Nodes (4): Container System API, Container System API Reference, Container Item System, Container System Architecture

### Community 1607 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1608 - "main"
Cohesion: 0.67
Nodes (3): main(), Entry point: ensure collect_n quest seed and clear instances via anyio., _reset_collect_n_quest()

### Community 1609 - "exception_metrics.py"
Cohesion: 0.40
Nodes (4): get_summary(), Any, Exception metrics tracking for monitoring. This module provides thread-safe…, Get a summary of exception counts. Returns: dict[str, Any]: Dictionary…

### Community 1610 - ".get_memory_status_report"
Cohesion: 0.22
Nodes (5): Any, Generate status report for diagnostic monitoring. Returns: Dictionary…, Runtime detection and cleanup of orphaned tasks based on memory thresholds.…, Get current memory usage in bytes for this process., Get count of active tasks in the current event loop.

### Community 1611 - "._get_npc_display_name"
Cohesion: 0.25
Nodes (4): Resolve NPC instance display name from lifecycle manager, or derive from npc_id., Best-effort lookup of NPC name from the lifecycle manager., Resolve the NPC lifecycle manager from the app state, if available., Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->…

### Community 1612 - "validate_calendar.py"
Cohesion: 0.06
Nodes (41): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+33 more)

### Community 1613 - ".check_and_cleanup"
Cohesion: 0.25
Nodes (6): Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops., Force immediate cleanup of all orphaned data. Args: cleanup_stats: Cleanup…, Periodically check for cleanup conditions and perform cleanup if needed. Args:…, _stale_prune_max_age_seconds(), Test _stale_prune_max_age_seconds uses longer threshold in local env., test_stale_prune_max_age_local()

### Community 1614 - "occupant_display.py"
Cohesion: 0.46
Nodes (7): _apply_grace_badges(), format_occupant_display_name(), _parse_occupant_player_id(), Any, UUID, Shared occupant display names for look text and Occupants panel events., Format an in-room player's Occupants/look name. Always list; grace badges only.

### Community 1616 - "📈 Performance Impact Assessment"
Cohesion: 0.67
Nodes (3): After Migration, Before Migration, 📈 Performance Impact Assessment

### Community 1617 - "🎯 Code Quality Assessment"
Cohesion: 0.67
Nodes (3): Areas for Future Enhancement (Not Blocking), 🎯 Code Quality Assessment, Strengths

### Community 1618 - "🎯 Final Verdict"
Cohesion: 0.67
Nodes (3): Code Quality: ✅ EXCELLENT (A), 🎯 Final Verdict, Recommendations for Deployment

### Community 1619 - "📈 Success Metrics"
Cohesion: 0.67
Nodes (3): Achieved, 📈 Success Metrics, To Verify (After Deployment)

### Community 1620 - "🎓 Technical Debt Reduced"
Cohesion: 0.67
Nodes (3): After, Before, 🎓 Technical Debt Reduced

### Community 1621 - "🎯 Audit Compliance Score"
Cohesion: 0.67
Nodes (3): After Remediation, 🎯 Audit Compliance Score, Before Remediation

### Community 1622 - "🎓 Key Learnings"
Cohesion: 0.67
Nodes (3): Best Practices Reinforced, 🎓 Key Learnings, What We Found

### Community 1623 - "🔍 Testing Strategy"
Cohesion: 0.67
Nodes (3): Immediate Testing (This Session), Performance Testing (After Deployment), 🔍 Testing Strategy

### Community 1624 - "🎯 Success Criteria - Status"
Cohesion: 0.67
Nodes (3): Phase 1 (Critical) - ✅ COMPLETE, Phase 2 (Performance) - 📋 PLANNED, 🎯 Success Criteria - Status

### Community 1625 - "🚨 Risk Assessment"
Cohesion: 0.67
Nodes (3): Remaining Risks, 🚨 Risk Assessment, Risks Eliminated

### Community 1626 - "Performance Logging"
Cohesion: 0.67
Nodes (3): API Request Logging, Database Query Logging, Performance Logging

### Community 1627 - "Log Rotation and Management"
Cohesion: 0.67
Nodes (3): Configuration, Log Cleanup, Log Rotation and Management

### Community 1628 - "Log Analysis and Monitoring"
Cohesion: 0.67
Nodes (3): Custom Log Analysis, Log Analysis and Monitoring, Using Our Log Analysis Tools

### Community 1629 - "Security Considerations"
Cohesion: 0.67
Nodes (3): Data Sanitization, Security Considerations, Sensitive Data Protection

### Community 1630 - "InviteBase"
Cohesion: 0.25
Nodes (8): InviteBase, Base invite schema with common fields., Test InviteBase can be instantiated., Test InviteBase has correct default values., Test InviteBase validates invite_code length., test_invite_base(), test_invite_base_defaults(), test_invite_base_validation()

### Community 1631 - "Decision Points"
Cohesion: 0.67
Nodes (3): Decision Points, When NOT to Migrate, When TO Migrate

### Community 1632 - "Monitoring & Validation"
Cohesion: 0.67
Nodes (3): Metrics to Track, Monitoring & Validation, Performance Validation

### Community 1633 - "Round-Based Combat"
Cohesion: 0.33
Nodes (6): Combat Action Queue, Combat Bugs Investigation and Fixes, Round-Based Combat, Combat Round System Refactor, First Weapon Switchblade, Flee Command and Effect

### Community 1634 - "Testing Strategy"
Cohesion: 0.67
Nodes (3): Per-File Testing, Regression Testing, Testing Strategy

### Community 1635 - "pyrightconfig.json"
Cohesion: 0.25
Nodes (7): extends, extraPaths, pythonVersion, venv, venvPath, ., ./pyproject.toml

### Community 1636 - "📊 Final Results"
Cohesion: 0.67
Nodes (3): Additional Files Updated, Files Migrated (12 of 12 - 100%), 📊 Final Results

### Community 1637 - "📈 Performance Impact"
Cohesion: 0.67
Nodes (3): After Migration, Before Migration, 📈 Performance Impact

### Community 1639 - "🎯 Async Compliance Score"
Cohesion: 0.67
Nodes (3): 🎯 Async Compliance Score, Final Score: 100%, Overall Compliance**: 🟢**A+ (100%)

### Community 1640 - "🧪 Testing Status"
Cohesion: 0.67
Nodes (3): Automated Tests, Manual Testing Required, 🧪 Testing Status

### Community 1641 - "🔧 Changes Summary"
Cohesion: 0.67
Nodes (3): 🔧 Changes Summary, Methods Made Async, Pattern Applied (48 times)

### Community 1642 - "check_file_for_logging_issues"
Cohesion: 0.47
Nodes (5): check_file_for_logging_issues(), main(), Path, Check a single file for logging consistency issues. Args: file_path: Path to…, Main function to check all service files for logging consistency.

### Community 1643 - "e2e_reset_players.py"
Cohesion: 0.47
Nodes (5): _load_default_respawn_room(), main(), Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the…, Entry point: run E2E player reset via anyio., _reset_e2e_players()

### Community 1644 - "Final Recommendation"
Cohesion: 0.67
Nodes (3): Final Recommendation, Start with Option B (Quick Wins) Immediately, Then Proceed to Option A (Full Optimization)

### Community 1645 - "Optimization Strategy Overview"
Cohesion: 0.67
Nodes (3): Guiding Principles, Optimization Strategy Overview, Success Metrics

### Community 1646 - "Monitoring and Validation"
Cohesion: 0.67
Nodes (3): Monitoring and Validation, Monthly Review Questions, Weekly Metrics

### Community 1647 - "NPC Occupants Verification Summary"
Cohesion: 0.33
Nodes (6): NPC Display Final Fixes, room_update Overwriting NPC Data, asyncpg UUID replace AttributeError, Legacy Occupants Snapshot Format, NPC Occupants Verification Summary, Rooms API User Object AttributeError

### Community 1648 - "Success Criteria"
Cohesion: 0.67
Nodes (3): Qualitative Goals, Quantitative Goals, Success Criteria

### Community 1649 - "Visual Test Value Distribution"
Cohesion: 0.67
Nodes (3): Overall Test Suite Composition (4,965 Tests), Test Count by Category, Visual Test Value Distribution

### Community 1650 - "E2E Testing Guide"
Cohesion: 1.00
Nodes (3): E2E Testing Guide, Playwright CLI E2E Tests, Playwright MCP Multiplayer Scenarios

### Community 1652 - "Combat Client Crash"
Cohesion: 0.33
Nodes (6): event_data vs data Field Name Mismatch, NATS Event Message Field Mismatch, Combat Client Crash, CombatMessaging Connection Manager Init Failure, Combat Disconnect At NPC Death, Passive Lucidity Flux Performance Degradation

### Community 1653 - "Respawn Death Screen Loop Limbo ID Mismatch"
Cohesion: 0.33
Nodes (6): limbo_death_void vs limbo_death_void_limbo_death_void, Respawn Death Screen Loop Limbo ID Mismatch, SQLAlchemy JSONB Mutation Detection, Respawn Persistence JSONB Mutation Failure, Death Threshold and Posture Bugs, HP -10 Limbo Transition Delay

### Community 1654 - "test_websocket_handler_json_error.py"
Cohesion: 0.25
Nodes (7): mock_websocket(), asyncio, fixture, Unit tests for websocket handler JSON error handling. Tests the JSON decode…, Create a mock WebSocket., Test _handle_json_decode_error() sends error response., test_handle_json_decode_error()

### Community 1655 - "NPC Combat Start Race Condition"
Cohesion: 0.33
Nodes (6): NPC Combat Start Race Condition, Redundant NPC Instance Lookup Failure, NPCs Incorrectly Marked is_alive False, December 3 Final Investigation Summary, Character Info Panel Missing Stats Field, Room Occupants Duplicates and Missing Player

### Community 1656 - "MemoryMonitor"
Cohesion: 0.08
Nodes (29): _max_connection_age_seconds(), MemoryMonitor, Any, Get memory-related alerts based on current usage and connection statistics.…, Update the last cleanup time to the current time., Force garbage collection to free memory., Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops., Monitor memory usage and trigger cleanup when needed. This class provides… (+21 more)

### Community 1657 - "MythosMUD Full-Stack Feature Skill"
Cohesion: 0.33
Nodes (6): MythosMUD COPPA Checklist Skill, MythosMUD Database Placement Skill, MythosMUD Full-Stack Feature Skill, MythosMUD OpenAPI Workflow Skill, player_id is UUID, Server Authority over Client

### Community 1658 - "frontend-design/SKILL.md"
Cohesion: 0.29
Nodes (4): Context Gathering Protocol, Design Direction, Implementation Principles, The AI Slop Test

### Community 1659 - "Enhanced Structured Logging System"
Cohesion: 0.40
Nodes (6): bind_request_context, Dual Logging (warnings/errors aggregators), Enhanced Structured Logging System, F-String Logging Anti-Pattern, get_logger, sanitize_sensitive_data Processor

### Community 1660 - "fixture"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Create a mock prototype registry., Create a sample room drop item., Create a sample inventory item., Create a sample equipped item., sample_equipped_item(), sample_inventory_item() (+1 more)

### Community 1661 - "test_cancel_shutdown_countdown_no_active"
Cohesion: 0.21
Nodes (13): _PendingCheckAppStub, _PendingCheckStateStub, Test is_shutdown_pending() returns True when shutdown is pending., Test is_shutdown_pending() returns False when shutdown is not pending., Test cancel_shutdown_countdown() when no shutdown is active., Test cancel_shutdown_countdown() successfully cancels shutdown., _ShutdownCancelAppStub, _ShutdownCancelStateStub (+5 more)

### Community 1663 - "MythosMUD ADR Authoring"
Cohesion: 0.29
Nodes (6): Index Update, Location, MythosMUD ADR Authoring, Reference, Structure, Template

### Community 1664 - "MythosMUD Commit Messages"
Cohesion: 0.29
Nodes (6): Examples, Format, MythosMUD Commit Messages, Rules, Template, Types

### Community 1669 - "Magic and Spellcasting System"
Cohesion: 0.40
Nodes (5): EffectList Pattern, Effects System Reference, Magic Points MP, Magic and Spellcasting System, Spell Registry

### Community 1670 - "Lucidity Tiers"
Cohesion: 0.60
Nodes (5): Catatonic Rescue Window, Lucidity System (LCD), Lucidity Tiers, Phantom Hostiles, Reversed Compass Directions

### Community 1674 - "Four-Level Room Hierarchy"
Cohesion: 0.40
Nodes (5): Environment Classification, Four-Level Room Hierarchy, Environment Inheritance, Room Hierarchy Implementation, Hierarchical World Loader

### Community 1676 - "MythosMUD Logging Standards"
Cohesion: 0.29
Nodes (6): Import, MythosMUD Logging Standards, Optional Helpers, Reference, Structured Logging, Summary

### Community 1679 - "MythosMUD OpenAPI Workflow"
Cohesion: 0.29
Nodes (6): Commands, MythosMUD OpenAPI Workflow, Output, Reference, Requirements, When to Regenerate

### Community 1682 - "MythosMUD Server Runbook"
Cohesion: 0.29
Nodes (6): Commands, Critical Rules, MythosMUD Server Runbook, ONE SERVER ONLY RULE, Pre-Start Checklist, Reference

### Community 1683 - "gh-stack (MythosMUD)"
Cohesion: 0.29
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1686 - "_update_player_status_effects"
Cohesion: 0.29
Nodes (7): Update and save player status effects if changes occurred. Returns: True if…, _update_player_status_effects(), Test _update_player_status_effects() when no changes occurred., Test _update_player_status_effects() when changes occurred., test_update_player_status_effects_changes(), test_update_player_status_effects_no_changes(), test_update_player_status_effects_saves()

### Community 1693 - "task_registry.py"
Cohesion: 0.29
Nodes (6): get_registry(), Centralized TaskRegistry for MythosMUD server task lifecycle management. This…, Convenience function for unregistering tasks with global registry., Access the global TaskRegistry., unregister_task(), test_get_registry_returns_global_instance()

### Community 1694 - "_FakeWebSocket"
Cohesion: 0.09
Nodes (26): _as_ws(), _FakeClientState, _FakeWebSocket, WebSocket, Test _find_dead_connections() returns empty list when all connections are…, Test _find_dead_connections() finds dead connections., Test _remove_dead_connection() removes connection from tracking., Test _update_player_connection_list() keeps active connections. (+18 more)

### Community 1696 - "CircuitBreakerOpen"
Cohesion: 0.29
Nodes (7): CircuitBreakerOpen, Exception, Exception raised when circuit breaker is open. Indicates the protected service…, Test CircuitBreakerOpen exception., Test call() raises CircuitBreakerOpen when circuit is OPEN., test_call_rejects_when_open(), test_circuit_breaker_open_exception()

### Community 1697 - "command_service"
Cohesion: 0.29
Nodes (7): command_service(), mock_request(), mock_user(), fixture, Create a CommandService instance., Create a mock request object., Create a mock user object.

### Community 1698 - "mock_zone_config"
Cohesion: 0.29
Nodes (7): mock_npc_definition(), mock_population_stats(), mock_zone_config(), fixture, Create a mock NPC definition., Create a mock zone configuration., Create mock population statistics.

### Community 1699 - "handle_unequip_command"
Cohesion: 0.29
Nodes (16): handle_unequip_command(), CommandResponse, Player, Unequip an item into the player's inventory., _unequip_persist_or_rollback(), _unequip_run_mutation(), _unequip_success_payload(), _mutation_cm() (+8 more)

### Community 1701 - "._get_room_uuid_by_stable_id"
Cohesion: 0.17
Nodes (10): Any, AsyncSession, UUID, Get room UUID by stable_id (hierarchical room ID). Args: stable_id:…, Mark room as explored using the provided session. Args: session: Database…, Get list of room IDs that a player has explored. Args: player_id: UUID of the…, Check if a player has explored a specific room. Args: player_id: UUID of the…, Synchronous wrapper for mark_room_as_explored. This method is designed to be… (+2 more)

### Community 1702 - "SampleModel"
Cohesion: 0.29
Nodes (7): OtherModel, BaseModel, Test Pydantic model for memory profiling tests., Test MemoryProfiler.measure_model_serialization() returns stats., Second model for compare_models_memory_usage., SampleModel, test_memory_profiler_measure_model_serialization()

### Community 1703 - "Modular E2E Test Suite"
Cohesion: 0.40
Nodes (5): Modular E2E Test Suite, MULTIPLAYER_SCENARIOS_PLAYBOOK, E2E Validation Passed, AI Context Limit 20KB, E2E Test Suite README

### Community 1704 - "Playwright MCP Scenarios"
Cohesion: 0.40
Nodes (5): Automated Playwright CLI Tests, Hybrid E2E Testing Approach, Mandatory Execution Order, Playwright MCP Scenarios, Room Occupants Fix

### Community 1705 - ".enforce_rate_limit"
Cohesion: 0.29
Nodes (4): Any, Check if a user has exceeded the rate limit. Args: user_id: The user's ID…, Get rate limit information for a user. Args: user_id: The user's ID Returns:…, Enforce rate limiting for a user. Args: user_id: The user's ID Raises:…

### Community 1706 - "Thinking about stack structure"
Cohesion: 0.33
Nodes (6): Branch naming, Dependency chain, One stack, one story, Staging changes deliberately, Thinking about stack structure, When to create a new branch

### Community 1707 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Add Missing Type Imports, Template 2: Fix Function Signature, Template 3: Handle Optional Values, Template 4: Fix Type Narrowing, Template 5: Add Generic Type Parameters

### Community 1708 - "extract/SKILL.md"
Cohesion: 0.33
Nodes (5): Discover, Document, Extract & Enrich, Migrate, Plan Extraction

### Community 1709 - "MythosMUD Pre-Commit Checklist"
Cohesion: 0.33
Nodes (5): Definition of Done, Full Pipeline (Optional), MythosMUD Pre-Commit Checklist, Order, Reference

### Community 1710 - "MagicPointsMeter.tsx"
Cohesion: 0.53
Nodes (4): formatDelta(), MagicPointsMeter, MagicPointsMeterProps, MagicPointsStatus

### Community 1711 - ".execute_behavior"
Cohesion: 0.33
Nodes (3): Schedule idle movement; default False. Override in subclasses (e.g.…, Hook for subclasses to add context before behavior rules run. Override in…, Execute NPC behavior based on context.

### Community 1712 - "is_postgres_url"
Cohesion: 0.33
Nodes (4): is_postgres_url(), Check if the database URL is PostgreSQL., Test is_postgres_url() with PostgreSQL URL., Test is_postgres_url() with non-PostgreSQL URL.

### Community 1713 - "AI PR Reviewer Instructions"
Cohesion: 0.40
Nodes (5): AI PR Reviewer Instructions, COPPA and Security Review Mandates, Review Coverage Thresholds, player_id UUID Type Rule, Server Authority Review Rule

### Community 1714 - "handle_ping_message"
Cohesion: 0.33
Nodes (6): handle_ping_message(), Handle ping message type., Test handle_ping_message() ignores data and sends pong., Test handle_ping_message() sends pong response., test_handle_ping_message(), test_handle_ping_message_with_data()

### Community 1715 - "schemas/auth/__init__.py"
Cohesion: 0.33
Nodes (5): Auth domain schemas: user and invite., Schema for reading user data., UserRead, Test UserRead can be instantiated., test_user_read()

### Community 1716 - "fixture"
Cohesion: 0.12
Nodes (17): mock_chat_logger(), mock_connection_manager(), mock_message_builder(), mock_name_extractor(), mock_occupant_manager(), mock_room_sync_service(), mock_task_registry(), player_event_handler() (+9 more)

### Community 1717 - "InviteCreate"
Cohesion: 0.33
Nodes (6): InviteCreate, Schema for creating a new invite., Test InviteCreate can be instantiated., Test InviteCreate can be instantiated without expiry., test_invite_create(), test_invite_create_no_expiry()

### Community 1718 - "._compute_player_context"
Cohesion: 0.25
Nodes (4): Get list of player IDs currently in the room. Returns: List of player IDs in…, Debug log for context enrichment (best-effort, must not fail)., Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…, Get player_in_range, enemy_nearby, and target_id from persistence. Returns…

### Community 1719 - "Quest System Gap"
Cohesion: 0.40
Nodes (5): Quest System Gap, MUD Subsystems Gap Analysis, Player Skills and Profession Modifiers, Quest Subsystem Implementation, Quest System

### Community 1720 - "UserBase"
Cohesion: 0.33
Nodes (6): Base user schema with common fields., UserBase, Test UserBase can be instantiated., Test UserBase has correct default values., test_user_base(), test_user_base_defaults()

### Community 1721 - "test_db_connectivity_create_and_read_user"
Cohesion: 0.33
Nodes (5): asyncio, serial, Integration test for database connectivity., Test that we can create and read a User from the database. CRITICAL: This test…, test_db_connectivity_create_and_read_user()

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

### Community 1726 - "test_websocket_handler_disconnect.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler disconnect handling. Tests the disconnect…, Test _handle_websocket_disconnect() returns True., Test _handle_websocket_disconnect() with no connection_id., test_handle_websocket_disconnect(), test_handle_websocket_disconnect_no_connection_id()

### Community 1727 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1728 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1729 - "test_websocket_handler_helpers.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler helper functions. Tests the helper functions…, Test _is_websocket_disconnected() returns True for disconnection messages., Test _is_websocket_disconnected() returns False for other messages., test_is_websocket_disconnected_false(), test_is_websocket_disconnected_true()

### Community 1730 - "test_magic_healing_events.py"
Cohesion: 0.09
Nodes (31): MagicServiceHealingMixin, Any, UUID, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or…, True if effect result indicates healing was applied (success, effect_applied,… (+23 more)

### Community 1731 - "Phase 2: Categorize and Prioritize Mypy Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Mypy Issues

### Community 1732 - "Phase 5: Fix Implementation Patterns"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL FIXES - Import and Name Errors, 🟡 HIGH PRIORITY FIXES - Type Errors, 🔵 LOW PRIORITY FIXES - Type Precision, 🟢 MEDIUM PRIORITY FIXES - Type Refinement, Phase 5: Fix Implementation Patterns

### Community 1733 - "test_protocols.py"
Cohesion: 0.29
Nodes (5): asyncio, Runtime checks for persistence repository protocols., _StubRoomRepo, test_player_repository_protocol_stub(), test_room_repository_protocol_stub()

### Community 1734 - "lock_state"
Cohesion: 0.25
Nodes (8): locked, sealed, unlocked, default, description, enum, type, lock_state

### Community 1735 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from…, Unit tests for connection utils. Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 1736 - "send_system_message"
Cohesion: 0.18
Nodes (15): Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler system message functions. Tests the system…, Create a mock WebSocket., Test send_system_message() successfully sends message. (+7 more)

### Community 1737 - "._background_audit_cycle"
Cohesion: 0.33
Nodes (3): Core capability for granular investigation cycles. Repeated universal analysis…, Start the background auditing scheduler responsible for identifying orphan…, Primary background cycle consuming auditor implementation. Executes periodic…

### Community 1738 - "fix_file"
Cohesion: 0.60
Nodes (4): fix_file(), main(), Path, Fix suppressions in a file. Returns: (number_fixed, list of changes)

### Community 1739 - "check_codacy_yaml"
Cohesion: 0.50
Nodes (4): check_codacy_yaml(), _content_is_valid(), Return (valid, list of reasons if invalid)., Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit.

### Community 1740 - "new-worktree.md"
Cohesion: 0.40
Nodes (4): Arguments, Behavior, Purpose, Usage Notes for Agents

### Community 1741 - "MythosMUD COPPA Checklist"
Cohesion: 0.40
Nodes (4): Checklist, Implementation, MythosMUD COPPA Checklist, Reference

### Community 1742 - "normalize/SKILL.md"
Cohesion: 0.40
Nodes (4): Clean Up, Execute, MANDATORY PREPARATION, Plan

### Community 1743 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 1744 - "TestPostgresConnectionPool"
Cohesion: 0.15
Nodes (13): PostgresConnectionPool, Thread-safe PostgreSQL connection pool., Get or create a connection pool for the given database URL., Get a connection from the pool., patch, Test PostgresConnectionPool class., Test get_pool() creates new pool., Test get_pool() reuses existing pool. (+5 more)

### Community 1745 - "3. Systematic Investigation Approach"
Cohesion: 0.40
Nodes (5): 3. Systematic Investigation Approach, For Authentication Failures, For Database-Related Failures, For Game Logic Failures, For WebSocket Failures

### Community 1746 - "add_fastapi_users_columns.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add FastAPI Users columns. Args: database_url:…

### Community 1747 - "add_used_by_user_id_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add used_by_user_id column. Args: database_url:…

### Community 1748 - "MythosMUD Pre-Commit Checklist Skill"
Cohesion: 0.40
Nodes (5): Definition of Done Checklist, MythosMUD Code Quality AI Skill, MythosMUD Commit Messages Skill, MythosMUD Pre-Commit Checklist Skill, MythosMUD Test Writing Skill

### Community 1749 - "process_npc_maintenance"
Cohesion: 0.40
Nodes (4): process_npc_maintenance(), Process NPC lifecycle maintenance (every 60 ticks = 1 minute)., Check if NPC maintenance should run on this tick. Args: tick_count: Current…, test_process_npc_maintenance_runs_on_interval()

### Community 1750 - "_AppStateWithLegacyConfig"
Cohesion: 0.40
Nodes (5): _AppStateWithLegacyConfig, _AppWithLegacyConfigState, Protocol, Minimal app.state shape for legacy error-handler debug config., Minimal FastAPI app shape for reading legacy config from state.

### Community 1751 - "_RoomPersistence"
Cohesion: 0.40
Nodes (4): Protocol, Protocol for persistence with get_room_by_id., Return the room object for the given room_id, or None if not found., _RoomPersistence

### Community 1752 - ".get_room_by_id"
Cohesion: 0.40
Nodes (3): Room, List all cached rooms., Get a room by ID from cache.

### Community 1753 - "_EventBusPublishPort"
Cohesion: 0.40
Nodes (4): _EventBusPublishPort, Protocol, Minimal surface for publishing domain events from ConnectionManager.event_bus., Publish a single event to the in-process bus.

### Community 1754 - "registry_with_switchblade"
Cohesion: 0.40
Nodes (5): fixture, Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade)., PrototypeRegistry containing only the switchblade., registry_with_switchblade(), switchblade_prototype()

### Community 1755 - "message_filtering_helper"
Cohesion: 0.40
Nodes (5): message_filtering_helper(), mock_connection_manager(), fixture, Create a mock connection manager., Create a MessageFilteringHelper instance.

### Community 1756 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 1757 - "🔄 COMMON SCENARIOS AND SOLUTIONS"
Cohesion: 0.50
Nodes (4): 🔄 COMMON SCENARIOS AND SOLUTIONS, Scenario 1: Third-Party Library Without Stubs, Scenario 2: Complex Union Types, Scenario 3: Recursive Types

### Community 1758 - "_make_mock_row"
Cohesion: 0.13
Nodes (15): _make_mock_row(), UUID, Test get_player_by_name successfully retrieves player., Test list_players successfully retrieves players., Create a mock procedure result row for row_to_player., Test get_player_by_id successfully retrieves player., Test get_players_by_user_id successfully retrieves players., Test get_active_players_by_user_id successfully retrieves active players. (+7 more)

### Community 1759 - "get_alerts"
Cohesion: 0.40
Nodes (5): get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing)

### Community 1760 - "🔍 DEBUGGING GUIDE"
Cohesion: 0.50
Nodes (4): 🔍 DEBUGGING GUIDE, If Mypy Command Fails, If Specific Issues Persist, Understanding Type Checker Behavior

### Community 1761 - "🚀 OPTIMIZATION TIPS"
Cohesion: 0.50
Nodes (4): For Large Codebases, For Performance, 🚀 OPTIMIZATION TIPS, Type Annotation Strategies

### Community 1762 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1763 - "test_professions_endpoints.py"
Cohesion: 0.27
Nodes (13): get_all_professions(), get_profession_by_id(), get, Request, Retrieve all available professions for character creation with caching. :param…, Retrieve specific profession details by ID with caching. :param profession_id:…, asyncio, Unit tests for server.api.professions. (+5 more)

### Community 1764 - "Structured Logging Patterns"
Cohesion: 0.50
Nodes (4): Basic Logging, Error Logging with Context, Performance Logging, Structured Logging Patterns

### Community 1765 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 1766 - "metadata"
Cohesion: 0.67
Nodes (3): additionalProperties, type, metadata

### Community 1768 - "PerformanceStats"
Cohesion: 0.67
Nodes (3): PerformanceStats, TypedDict, Type definition for performance statistics tracking.

### Community 1774 - "WebSocket and SSE Dual Connections"
Cohesion: 0.50
Nodes (4): Dual Connection API Reference, WebSocket and SSE Dual Connections, Dual Connection Client Guide, Dual Connection Deployment Guide

### Community 1775 - "test_disconnect_connection_for_session_key_error"
Cohesion: 0.50
Nodes (3): _DelKeyErrorSockets, Test _disconnect_connection_for_session() handles KeyError when deleting., test_disconnect_connection_for_session_key_error()

### Community 1777 - "🚨 AI ERROR HANDLING"
Cohesion: 0.67
Nodes (3): 🚨 AI ERROR HANDLING, If Multiple Categories Have Issues, If Mypy Still Fails After Fixes

### Community 1778 - "🚨 AI ERROR HANDLING"
Cohesion: 0.67
Nodes (3): 🚨 AI ERROR HANDLING, If Lint Still Fails After Fixes, If Multiple Categories Have Issues

### Community 1779 - "id"
Cohesion: 0.67
Nodes (3): minLength, type, id

### Community 1780 - "_NpcWithLife"
Cohesion: 0.67
Nodes (3): _NpcWithLife, Protocol, NPC instance shape for alive check before accepting an attack target.

### Community 1785 - "_resolve_npc_combat_service_raw"
Cohesion: 0.67
Nodes (3): Return the live NPC combat integration service for delegation. Prefer…, _resolve_npc_combat_service_raw(), test_resolve_npc_combat_service_from_container()

### Community 1786 - "MythosMUD Product Requirements"
Cohesion: 0.50
Nodes (4): Aggro System, Lucidity System, MythosMUD Product Requirements, Room-Based Combat

### Community 1788 - "party_service"
Cohesion: 0.67
Nodes (3): party_service(), fixture, PartyService with no dependencies (in-memory only).

### Community 1789 - "mock_send_game_event"
Cohesion: 0.67
Nodes (3): mock_send_game_event(), fixture, Create a mock send_game_event function.

### Community 1790 - "monitor"
Cohesion: 0.67
Nodes (3): monitor(), fixture, Monitor with tiny thresholds for easy triggering in tests.

### Community 1791 - "auditor"
Cohesion: 0.67
Nodes (3): auditor(), fixture, Auditor with short interval and auto cleanup enabled.

### Community 1792 - "Any"
Cohesion: 0.15
Nodes (7): Any, Get mapping of event types to their handler methods., Validate that event message has required fields., Handle player_left event., Handle combat_ended event., Handle player_attacked event., Handle npc_took_damage event.

### Community 1793 - "subscription_manager"
Cohesion: 0.67
Nodes (3): fixture, Create a RoomSubscriptionManager instance., subscription_manager()

### Community 1794 - "combat_validator"
Cohesion: 0.67
Nodes (3): combat_validator(), fixture, Create a CombatValidator instance.

### Community 1795 - "subscription_manager"
Cohesion: 0.67
Nodes (3): fixture, Create a RoomSubscriptionManager instance., subscription_manager()

### Community 1797 - "verify_npc_occupants.py"
Cohesion: 0.23
Nodes (12): _check_service_availability(), _collect_npcs_by_room(), _print_summary(), Any, Verification script to check NPCs in lifecycle manager and test occupant query…, Print verification summary. Args: npc_count: Total number of active NPCs…, Verify NPCs exist in lifecycle manager and test query logic., Check if NPC service, lifecycle manager, and active_npcs are available.… (+4 more)

### Community 1798 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_players_batch with empty list., Test _load_room_cache_async logs sample room IDs when rooms are loaded…, Test _load_room_cache_async handles table not found error., Test _load_room_cache_async raises other errors., Test _query_rooms_with_exits_async handles table not found error., Test _query_rooms_with_exits_async raises other errors., test_get_players_batch_empty_list() (+5 more)

### Community 1801 - ".shutdown_all"
Cohesion: 0.17
Nodes (6): Cancel lifecycle/critical tasks first (Phase 1)., Cancel remaining active tasks (Phase 2)., Wait for task completion with timeout., Forcibly cancel any lingering tasks that didn't respond to graceful…, Clean up active collections after final shutdown., Gracefully shutdown all tracked tasks with timeout coordination. Implements…

### Community 1809 - "Claude Pointer (.claude/CLAUDE.md)"
Cohesion: 0.67
Nodes (4): AGENTS.md Authoritative Reference, Cursor Rules (.cursor/rules/), Claude Pointer (.claude/CLAUDE.md), Root CLAUDE.md Router Stub

### Community 1810 - "test_spell_repository.py"
Cohesion: 0.19
Nodes (15): Any, Map procedure result row to spell dict., Get all spells from the database. Returns: list[dict]: List of all spell…, _row_to_spell_dict(), _mock_session(), asyncio, fixture, Unit tests for SpellRepository. (+7 more)

### Community 1819 - "Logging Best Practices"
Cohesion: 0.67
Nodes (4): Logging Best Practices, Structured Key-Value Logging, Logging Quick Reference, Forbidden Logging Patterns

### Community 1828 - "zone_config_loader.py"
Cohesion: 0.09
Nodes (25): extract_zone_name(), parse_zone_special_rules(), Record, TypedDict, Zone Configuration Loader Module. This module handles loading zone and sub-zone…, Build and store one subzone configuration from a database row., Parse a zone special_rules field from the database., Extract zone name from stable_id (format: 'plane/zone'). Args: stable_id: The… (+17 more)

### Community 1829 - "Scenario Group Execution"
Cohesion: 0.50
Nodes (4): Scenario Group Execution, Local Channel Scenario Group (8-12), Logout Scenario Group (19-21), Whisper Channel Scenario Group (13-18)

### Community 1830 - ".add_message"
Cohesion: 0.18
Nodes (6): Any, Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…, Check if a message is recent (within the specified age limit). Args: msg:…, Get message queue statistics. Returns: Dict[str, Any]: Statistics about the…, Add a message to a player's pending message queue. Args: player_id: The…, Get all pending messages for a player and clear the queue. Args: player_id: The…

### Community 1831 - "Per-Recipient Whisper Rate Limiting"
Cohesion: 0.50
Nodes (4): Whisper System Remediation, Per-Recipient Whisper Rate Limiting, Global Whisper Rate Limit, Scenario 15 Rate Limiting Blocked

### Community 1837 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test query_room_occupants_snapshot() queries occupants., Test send_room_updates_to_entering_player() handles invalid player_id., Test _process_player_entered_event() returns None when room_id is None., Test handle_player_entered() handles errors., Test broadcast_player_entered_message() broadcasts to room., test_broadcast_player_entered_message(), test_handle_player_entered_error_handling() (+3 more)

### Community 1842 - "._connect_nats"
Cohesion: 0.22
Nodes (6): Any, BaseException, Raise RuntimeError when e2e requires live NATS; no-op for other environments., Convert connect failures into hard error (e2e) or soft log (other envs)., Handle connect() returning False; raise for e2e, soft-warn otherwise., Connect to NATS if enabled and not unit_test. Returns NATSService or None.…

### Community 1845 - "Vite Best-Practices Remediation"
Cohesion: 0.50
Nodes (4): Test Suite Improvement, Vite Best-Practices Remediation, import.meta.env (Vite), Vitest Best-Practices Remediation

### Community 1846 - "Success Metrics"
Cohesion: 0.50
Nodes (4): Functional Metrics, Quality Metrics, Success Metrics, Timeline Metrics

### Community 1852 - "Scenario 32 Disconnect Grace Period"
Cohesion: 0.50
Nodes (4): Scenario 32 Disconnect Grace Period, Linkdead Zombie State, Scenario 33 Rest Command, Scenario 35 Player Combat

### Community 1854 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1859 - "fixture"
Cohesion: 0.22
Nodes (9): connection_manager(), follow_service(), movement_service(), fixture, Mock MovementService; move_player returns True then we can set False for…, Mock UserManager; not muted., Mock ConnectionManager (optional for this flow)., FollowService wired to real EventBus and mock MovementService. (+1 more)

### Community 1862 - "npc_event_handler"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), fixture, Create a mock connection manager., Create a mock message builder., Create a mock send_occupants_update function. (+1 more)

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

### Community 1881 - "preferences_service"
Cohesion: 0.22
Nodes (9): mock_session(), preferences_service(), fixture, Create a PlayerPreferencesService instance., Create a mock async session., Create a sample player ID., Create sample player preferences., sample_player_id() (+1 more)

### Community 1883 - "F-String Logging Violations"
Cohesion: 0.40
Nodes (5): F-String Logging Violations, Enhanced Logging Compliance Audit, F-String Logging Remediation Complete, Pre-Commit F-String Hook Gaps, AST-Based F-String Logging Detector

### Community 1890 - "Catatonic Movement Prevention Bug"
Cohesion: 0.50
Nodes (4): Catatonic Movement Prevention Bug, WebSocket Go Command Unified Handler Bypass, current_room_id VARCHAR(50) Truncation, Movement Valid Exits Rejection Bug

### Community 1892 - "Rooms List SQL ::uuid[] Parameter Conflict"
Cohesion: 0.50
Nodes (4): asyncpg Colon Cast Parameter Parsing, Rooms List SQL ::uuid[] Parameter Conflict, Minimap Explored Rooms UUID vs stable_id, Explored Room UUIDs Treated As stable_ids

### Community 1900 - ".get_lifecycle_statistics"
Cohesion: 0.25
Nodes (4): Get overall lifecycle statistics. Returns: Dictionary containing lifecycle…, Return counts of lifecycle records by current_state., Return counts of lifecycle records by NPC type string., Return (total_spawns, total_despawns, total_errors) across all lifecycle…

### Community 1903 - "monitoring_service"
Cohesion: 0.25
Nodes (8): mock_combat_config(), mock_config(), mock_feature_flags(), monitoring_service(), fixture, Create mock feature flags., Create mock combat config., Create CombatMonitoringService instance with mocked dependencies.

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

### Community 1915 - "position_commands.py"
Cohesion: 0.08
Nodes (36): _broadcast_posture_change(), _build_posture_change_event(), _EventSequence, _get_position_command_services(), handle_lie_command(), _handle_position_change(), handle_sit_command(), handle_stand_command() (+28 more)

### Community 1917 - "Party System Reference"
Cohesion: 0.67
Nodes (3): Party Invite Command, Party System Reference, Ephemeral Grouping Party Planning

### Community 1924 - "Test File Migration Mapping"
Cohesion: 0.67
Nodes (3): Test Suite Hierarchical Migration, Test File Migration Mapping, Test Suite Refactoring Deliverables

### Community 1926 - "sample_container"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Test getting container description from equipped item., Create a sample container., Create a sample equipped container item., Create a mock prototype registry., sample_container(), sample_equipped_container() (+1 more)

### Community 1929 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1930 - ".get_task_lifecycle_metrics"
Cohesion: 0.33
Nodes (3): Get count of active tasks., Get task breakdown by type., Get task lifecycle metrics including creation and completion rates.

### Community 1931 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

### Community 1945 - "GameState Event Projection"
Cohesion: 0.67
Nodes (3): Client EventStore, GameState Event Projection, Server Authority over Client State

### Community 1947 - "Truly Dead Code"
Cohesion: 0.67
Nodes (3): Knip Client Dead Code Tooling, Truly Dead Code, Vulture Allowlist

### Community 1956 - "Dependency Review Workflow"
Cohesion: 0.67
Nodes (3): Dependabot Dependency Updates, Dependency Review Workflow, UV Lock Dependency Snapshot Gate

### Community 1964 - "10 Concurrent Players Load Test"
Cohesion: 0.67
Nodes (3): who Command Unawaited Coroutine Bug, 10 Concurrent Players Load Test, Load Test Suite

### Community 1969 - "server/main.py"
Cohesion: 0.19
Nodes (12): _create_get_app(), main(), Any, FastAPI, get, MythosMUD Server - Main Application Entry Point This module serves as the…, Root endpoint providing basic server information., Test endpoint to verify JWT authentication is working. (+4 more)

### Community 1972 - "Cursor Rules as Canonical Config"
Cohesion: 0.67
Nodes (3): Cursor-Centric AI Config, Cursor Rules as Canonical Config, GitHub Worktrees Cursor Setup

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

### Community 2055 - ".get_combat_stats"
Cohesion: 0.33
Nodes (3): Get combat stats for a player., Normalize NPC stats to include 'hp' for backward compatibility., Get combat-relevant stats for an entity. Args: entity_id: ID of the entity…

### Community 2058 - ".cleanup_empty_subzone_subscriptions"
Cohesion: 0.33
Nodes (3): Unsubscribe from local channel messages for a specific sub-zone. Args: subzone:…, Get list of players currently in a specific sub-zone. Args: subzone: Sub-zone…, Clean up sub-zone subscriptions that have no active players.

### Community 2060 - ".handle_player_movement"
Cohesion: 0.33
Nodes (3): Track a player's sub-zone subscription for local channels. Args: player_id:…, Handle player movement between rooms and update sub-zone subscriptions. Args:…, Subscribe to local channel messages for a specific sub-zone. Args: subzone:…

### Community 2089 - "TestGetRoomService"
Cohesion: 0.33
Nodes (4): Test get_room_service() function., Test get_room_service() returns room service from container., Test get_room_service() raises error when service not initialized., TestGetRoomService

### Community 2095 - "applies_to"
Cohesion: 0.67
Nodes (3): minItems, type, applies_to

### Community 2102 - "._get_player_mute_file"
Cohesion: 0.29
Nodes (5): _get_proper_data_dir(), Path, Get the mute data file path for a specific player., Get the proper environment-aware data directory for user management. Uses…, Initialize the user manager. Args: data_dir: Directory for player-specific mute…

### Community 2108 - "integration"
Cohesion: 0.40
Nodes (5): integration(), mock_persistence(), fixture, Persistence mock with async get_player_by_id for integration tests., NPCCombatIntegration wired to the mock persistence layer.

### Community 2109 - "player_repository"
Cohesion: 0.40
Nodes (5): mock_player(), player_repository(), fixture, Create a PlayerRepository instance., Create a mock player for save operations.

### Community 2110 - "RateLimiter"
Cohesion: 0.02
Nodes (172): _cleanup_connection_tracking(), _cleanup_fully_disconnected_player(), _cleanup_player_data(), _cleanup_room_subscriptions(), cleanup_websocket_disconnect(), disconnect_all_websockets_impl(), disconnect_connection_by_id_impl(), _disconnect_single_websocket() (+164 more)

### Community 2114 - "user_manager"
Cohesion: 0.40
Nodes (5): mock_data_dir(), fixture, Create a temporary data directory., Create a UserManager instance., user_manager()

### Community 2115 - "wearable_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), fixture, Create mock persistence layer., Create WearableContainerService instance., wearable_service()

### Community 2116 - "_is_npc_follow_value"
Cohesion: 0.50
Nodes (4): _FollowTargetValue, _is_npc_follow_value(), TypeGuard, True when v is the 3-tuple (target_id, 'npc', display_name).

### Community 2118 - "enabled"
Cohesion: 0.50
Nodes (4): default, description, type, enabled

### Community 2128 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 2150 - "OccupantFormatter"
Cohesion: 0.12
Nodes (20): OccupantFormatter, Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Formats and separates occupants by type., Initialize occupant formatter., Check if a string looks like a UUID. Args: value: The string to check Returns:… (+12 more)

## Knowledge Gaps
- **5986 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `JCODEMUNCH_MAX_FOLDER_FILES`, `@codacy/codacy-mcp` (+5981 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **645 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `DistributedEventBus`, `AliasStorage`, `npc_definitions_api.py`, `websocket_initial_state.py`, `models/user.py`, `test_email_utils.py`, `is_player_in_login_grace_period`, `MythosMUDError`, `container_persistence/container_persistence.py`, `player_connection_setup.py`, `container_endpoints_basic.py`, `server/models/game.py`, `PrototypeRegistry`, `BaseCommand`, `handle_transfer_items_exceptions`, `connection_manager_methods.py`, `test_player_disconnect_handlers.py`, `ConnectionManager`, `api/monitoring.py`, `test_look_npc.py`, `test_admin_commands.py`, `test_container_persistence_extended_crud.py`, `server/tests/conftest.py`, `optimized_security_validator.py`, `command_result_text`, `inventory_command_helpers.py`, `FollowService`, `Room`, `websocket_handler_commands.py`, `MPRegenerationService`, `ApplicationContainer`, `test_connection_delegates.py`, `CombatParticipant`, `CombatParticipantData`, `_find_item_in_equipped`, `ErrorContext`, `Stats`, `debrief_command.py`, `test_admin_auth_service.py`, `RoomService`, `lifespan.py`, `CombatInstance`, `test_combat_attack_handler.py`, `DatabaseManager`, `PayloadOptimizer`, `api/player_effects.py`, `test_lucidity_event_dispatcher.py`, `alias_storage.py`, `NATSService`, `NPCOccupantProcessor`, `test_chat_nats_publisher.py`, `test_lucidity_recovery_commands.py`, `test_status_commands.py`, `magic_service.py`, `build_event`, `HolidayService`, `PlayerEventHandlerUtils`, `test_look_room.py`, `rest_countdown_task.py`, `lifespan_magic.py`, `test_go_command.py`, `test_movement_service.py`, `NATSMessageBroker`, `server/dependencies.py`, `test_admin_setlucidity_command.py`, `config/models/__init__.py`, `CoordinateValidator`, `test_chat_validator.py`, `item_instance_persistence.py`, `OccupantFormatter`, `test_player_presence_tracker.py`, `LoggedHTTPException`, `ContainerData`, `test_look_player.py`, `PrototypeRegistryError`, `User`, `test_combat_monitoring_service.py`, `test_chat_npc_system.py`, `player_effect_repository.py`, `test_container_websocket_events.py`, `MythosChronicle`, `PlayerOccupantProcessor`, `migrate_combat_data.py`, `test_alias_commands.py`, `server/services/__init__.py`, `should_spawn_npc`, `WebSocketMessageValidator`, `server/schemas/__init__.py`, `catatonia_check.py`, `test_rest_command.py`, `WearableContainerService`, `admin_summon_command.py`, `LootAllRequest`, `test_lucidity_command_disruption.py`, `CombatAuditLogger`, `task_registry.py`, `talk_command.py`, `rescue_commands.py`, `test_party_commands.py`, `CombatConfiguration`, `middleware`, `chat_service.py`, `test_combat_service_modules.py`, `PhantomHostileService`, `PartyService`, `PlayerPreferencesService`, `session_factory`, `npc_combat_grace.py`, `TargetResolutionService`, `QuestService`, `test_combat_event_publisher.py`, `_handle_admin_set_stat_command`, `ContainerServiceError`, `test_error_logging.py`, `CombatPersistenceHandler`, `test_map_helpers.py`, `test_inventory_helpers.py`, `MonitoringDashboard`, `chat_message.py`, `add_fastapi_users_columns.py`, `add_used_by_user_id_column.py`, `NATSSubjectManager`, `api/player_respawn.py`, `test_channel_commands.py`, `TargetMatch`, `QuestInstanceRepository`, `ChatModeration`, `resolve_weapon_attack_from_equipped`, `test_chat_pose_helpers.py`, `ComprehensiveLoggingMiddleware`, `maps.py`, `add_hashed_password_column.py`, `test_error_handling_middleware.py`, `rename_invites_columns.py`, `ContainerRepository`, `LogAggregator`, `magic_service_completion.py`, `PlayerNameExtractor`, `test_logout_commands.py`, `persistence/container_persistence.py`, `lucidity_trigger_handlers.py`, `AdminActionsLogger`, `test_npc_admin_commands.py`, `DialogueDefinitionRepository`, `FeatureFlagService`, `initialize_components`, `admin_shutdown_command.py`, `AttributeError`, `PerformanceMonitor`, `Any`, `database_config_helpers.py`, `party_service.py`, `models/combat.py`, `test_lifespan_shutdown.py`, `zone_config_loader.py`, `handle_read_command`, `inventory_get_command.py`, `test_occupants.py`, `CombatService`, `NPCDied`, `skills.py`, `TargetResolutionResult`, `RoomRepository`, `look_container.py`, `test_lifecycle_respawn.py`, `rename_used_to_is_active.py`, `ValidationError`, `map_minimap.py`, `CommandRateLimiter`, `lucidity_migration.py`, `look_command.py`, `test_corpse_lifecycle_service.py`, `message_handler_factory.py`, `combat_attack.py`, `handle_emote_command`, `test_goto_helpers.py`, `skills_commands.py`, `spell_effects_support.py`, `command_handler_unified.py`, `websocket_helpers.py`, `test_movement_monitor.py`, `test_shutdown_sequence.py`, `position_commands.py`, `test_users.py`, `inventory_equip_command.py`, `ChatPoseManager`, `test_communication_commands_flows.py`, `retry.py`, `Player`, `player_inventory_migration.py`, `npc_database.py`, `rescue_service.py`, `NATSConnectionStateMachine`, `real_time.py`, `persistence/container_helpers.py`, `handle_teach_command`, `test_who_commands.py`, `register_default_reactions_for_npc`, `validate_admin_permission`, `inventory_commands.py`, `server/main.py`, `factory.py`, `channel_broadcasting_strategies.py`, `PlayerService`, `websocket_handler.py`, `CircuitState`, `test_npc_service.py`, `get_admin_auth_service`, `test_magic_service.py`, `quest_commands.py`, `admin_teleport_commands.py`, `HealthRepository`, `DatabaseError`, `npc_instances_api.py`, `apply_communication_dampening`?**
  _High betweenness centrality (0.169) - this node is a cross-community bridge._
- **Why does `ValidationError` connect `ValidationError` to `MovementService`, `persistence/container_persistence.py`, `AliasStorage`, `MythosMUDError`, `server/schemas/__init__.py`, `container_persistence/container_persistence.py`, `test_command_parser_helpers.py`, `Player`, `test_player_service_mutations.py`, `BaseCommand`, `handle_transfer_items_exceptions`, `NPCCombatIntegration`, `test_command_communication.py`, `admin_summon_command.py`, `npc_database.py`, `database_config_helpers.py`, `get_logger`, `persistence/container_helpers.py`, `inventory_command_helpers.py`, `test_command_processing.py`, `ContainerComponent`, `test_command_parser.py`, `get_username_from_user`, `ErrorContext`, `Stats`, `test_player_service.py`, `PlayerService`, `test_command_factories_utility.py`, `DatabaseManager`, `ContainerServiceError`, `api/player_effects.py`, `test_error_logging.py`, `test_command_service.py`, `PlayerRespawnWrapper`, `test_world_loader.py`, `api/player_respawn.py`, `test_go_command.py`, `test_movement_service.py`, `test_command_processor.py`, `item_instance_persistence.py`, `PydanticErrorHandler`, `EnvironmentalContainerLoader`, `DatabaseError`, `validate_room_data`, `EmoteService`, `ContainerData`, `test_profession_service.py`, `TestErrorHandlers`, `GameMechanicsService`, `test_command_factories_moderation.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `ApplicationContainer` connect `ApplicationContainer` to `MythosChronicle`, `api/monitoring.py`, `get_logger`, `models/combat.py`, `test_lifespan_shutdown.py`, `CombatService`, `Stats`, `lifespan.py`, `fixtures/unit/__init__.py`, `test_lifespan_event_subscriptions.py`, `CombatPersistenceHandler`, `validate_calendar.py`, `send_game_event`, `MonitoringDashboard`, `magic_service.py`, `build_event`, `HolidayService`, `lifespan_magic.py`, `.get_instance`, `server/dependencies.py`, `User`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **Are the 137 inferred relationships involving `LoggedHTTPException` (e.g. with `logged_http_exception_handler()` and `register_error_handlers()`) actually correct?**
  _`LoggedHTTPException` has 137 INFERRED edges - model-reasoned connections that need verification._
- **Are the 223 inferred relationships involving `ValidationError` (e.g. with `fetch_user_by_username_case_insensitive()` and `load_database_url()`) actually correct?**
  _`ValidationError` has 223 INFERRED edges - model-reasoned connections that need verification._
- **Are the 90 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 90 INFERRED edges - model-reasoned connections that need verification._
- **Are the 79 inferred relationships involving `AliasStorage` (e.g. with `_ensure_alias_storage()` and `_handle_special_command_routing()`) actually correct?**
  _`AliasStorage` has 79 INFERRED edges - model-reasoned connections that need verification._