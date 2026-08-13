# Graph Report - MythosMUD  (2026-08-13)

## Corpus Check
- 3048 files · ~2,657,890 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 45443 nodes · 83472 edges · 1975 communities (1382 shown, 593 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 2981 edges (avg confidence: 0.6)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8decad67`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CommandFactory
- lifespan.py
- test_look_helpers.py
- Alias
- combat_flee.py
- websocket_initial_state.py
- NATSService
- test_command_inventory.py
- test_users.py
- is_player_in_login_grace_period
- MythosMUDError
- Communities (355 total, 223 thin omitted)
- ErrorType
- test_command_parser.py
- LoggedHTTPException
- players/__init__.py
- NPCCombatIntegrationService
- server/exceptions.py
- test_security_validator.py
- test_admin_auth_service.py
- RateLimiter
- test_command_factories_communication.py
- test_connection_delegates.py
- test_look_container.py
- test_wearable_container_service.py
- test_player_disconnect_handlers.py
- _def_row
- api/monitoring.py
- test_look_npc.py
- test_admin_commands.py
- container_persistence_async.py
- test_websocket_handler_coverage_gaps.py
- test_websocket_handler_core.py
- test_nats_message_handler.py
- test_inventory_commands.py
- inventory_command_helpers.py
- test_room_class.py
- lifecycle_periodic.py
- server/dependencies.py
- test_container.py
- TargetResolutionService
- MessageQueue
- server/schemas/__init__.py
- test_player_model.py
- NATSMessageHandler
- test_npc_startup_service.py
- test_command_admin.py
- test_behavior_engine.py
- test_follow_commands.py
- get_logger
- test_container_websocket_events.py
- test_database_helpers.py
- TestCombatInitializer
- test_command_factories.py
- Any
- ExplorationService
- test_combat_schema.py
- Stats
- test_player_respawn_service.py
- api/conftest.py
- rooms.py
- .reset_instance
- test_command_factories_utility.py
- test_health_service.py
- LucidityFluxService
- test_command_factories_exploration.py
- ui-v2/types.ts
- test_user_manager.py
- test_quest_instance_repository.py
- PayloadOptimizer
- test_command_service.py
- test_connection_establishment.py
- DatabaseError
- asyncio
- TauntCommandHandler
- test_combat_validator.py
- EldritchIcon.tsx
- communication_commands.py
- test_connection_helpers_impl.py
- CombatTurnProcessor
- test_connection_disconnection.py
- test_argon2_utils.py
- Reporter
- test_room_renderer.py
- test_websocket_handler_helpers_extended.py
- test_status_commands.py
- websocket_integration.py
- test_auth_utils.py
- test_container_helpers_inventory_find.py
- map/types.ts
- event_types.py
- test_look_room.py
- test_rescue_service.py
- NATSMessageBroker
- test_go_command.py
- test_lucidity_recovery_commands.py
- multiplayer.ts
- test_nats_service.py
- test_character_creation_service.py
- test_rate_limiter_utils.py
- Dependency Risk Analyzer
- server/persistence/__init__.py
- test_container_helpers_inventory_ops.py
- test_player_presence_tracker.py
- test_player_death_service.py
- RoomService
- test_metrics_endpoints.py
- test_room_sync_service.py
- RoomLoader
- asyncio
- CircuitBreaker
- CorpseOverlay.tsx
- PlayerEnteredRoom
- test_nats_broker.py
- RoomSubscriptionManager
- UserManager
- test_look_player.py
- test_logging_utilities.py
- User
- test_combat_monitoring_service.py
- test_lucidity_event_dispatcher.py
- test_nats_message_handler_chat.py
- run_flee_effect
- types/mythosTime.ts
- SchemaValidator
- DeadLetterQueue
- .get_instance
- Player
- PathValidator
- player_effect_repository.py
- .__post_init__
- chatPanelRuntimeUtils.ts
- test_room_utils.py
- test_movement_service.py
- test_alias_commands.py
- WebSocketMessageValidator
- asyncio
- RoomDataCache
- test_player_event_handlers_respawn.py
- api/character_creation.py
- HealthRepository
- catatonia_check.py
- test_nats_message_handler_subzone_events.py
- TaskRegistry
- test_rest_command.py
- test_user_schemas.py
- .transfer_from_container
- PlayerRespawnService
- test_npc_combat_integration_class.py
- test_look_npc_helpers.py
- AliasStorage
- TestHelperFunctions
- Stats
- quality_fragmentation_ai_guardrails.py
- test_combat_attack_handler.py
- test_connection_statistics.py
- player_schema_converter.py
- test_calendar_schemas.py
- NPCSpawnRule
- test_websocket_messages.py
- ApplicationContainer
- test_room_subscription_manager_drops.py
- PlayerSavePreparer
- test_validation.py
- .state
- TestSanitization
- CombatConfigurationService
- _asyncio_mark
- chat_message_senders.py
- inventory_equip_command.py
- test_corpse_lifecycle_service.py
- test_party_service.py
- maps.py
- test_quest_service.py
- test_async_persistence_room_cache.py
- fixtures/integration/__init__.py
- PydanticErrorHandler
- CatatoniaRegistry
- gameStore.ts
- OccupantFormatter
- admin_shutdown_command.py
- ConnectionCleaner
- App.tsx
- test_container_persistence.py
- useGameClientV2Container.ts
- command_input.py
- GameClientV2Dock.test.tsx
- ChatService
- QuestService
- strict_mocker
- quest_commands.py
- MemoryProfiler
- combat_event_publisher
- connection_initialization.py
- test_active_lucidity_service.py
- test_idle_movement.py
- _handle_admin_set_stat_command
- test_async_persistence_core.py
- stateUpdateUtils.ts
- Any
- test_message_filtering.py
- ChatPanelRuntimeViewParts.tsx
- test_combat_persistence_handler_events.py
- test_map_helpers.py
- test_inventory_helpers.py
- StatusEffect
- MonitoringDashboard
- EventHandler
- useAsciiMapState.ts
- FStringLoggingFixer
- MemoryMonitor
- fixtures/auth.ts
- handle_time_command
- logging_file_setup.py
- test_connection_session_management.py
- safe_run_static
- Arena Zone DML Generator
- ResourceManager
- test_manager.py
- test_async_persistence_delegates.py
- commandStore.ts
- TestRoomDataFixer
- HolidayCollection
- test_command_parser_helpers.py
- test_game_state_provider.py
- CombatMonitoringService
- PlayerService
- test_room_subscription_manager.py
- test_chat_service.py
- is_player_in_grace_period
- useMythosAppActions.ts
- WebSocketRequestContext
- collect_inventory.py
- ChatModeration
- resolve_weapon_attack_from_equipped
- EnvironmentalContainerLoader
- mapPageRenderer.tsx
- chat_service.py
- Async Remediation Complete
- NPCCombatIntegrationBase
- NATSConnectionError
- RoomDataValidator
- apiTypeGuards.ts
- error_handling_middleware.py
- fix_markdown_blanks_around_lists.py
- test_command_magic.py
- LogAggregator
- PlayerNameExtractor
- TestValidatorComponents
- log_and_raise
- useDraggablePanelInteractions.ts
- Test Suite Refactoring Plan
- test_nats_messages.py
- test_player_event_handlers_state.py
- test_logout_commands.py
- test_player_occupant_processor.py
- get_username_from_user
- persistence/container_persistence.py
- game_tick_processing.py
- GameLogPanel.tsx
- playerHandlers.ts
- vim Best Practices and Coding Standards
- migration_examples.py
- router.py
- RoomMapEditorRuntime.hooks.ts
- asyncio
- subzone_schema.json
- ChatChannelLoggerMixin
- player.ts
- PeriodicOrphanAuditor
- test_login_grace_period_visual_indicator.py
- PlayerPreferencesService
- TestFeatureFlagService
- test_memory_leak_metrics.py
- alias_schema.json
- Any
- RoomIDUtils
- test_admin_shutdown_command.py
- 🧪 MythosMUD E2E Testing Strategy
- ExceptionTracker
- Logging Compliance Checker
- disconnect_grace_period.py
- GameClientV2ContainerView.tsx
- ErrorMonitor
- Memory Leak Prevention System - Implementation Summary
- test_pattern_matcher.py
- Linting Results Comparator
- test_health.py
- .execute_idle_movement
- test_look_item_helpers.py
- test_aggro_threat.py
- test_room_subscription_manager_helpers.py
- test_command_combat.py
- useRespawnHandlers.ts
- handle_read_command
- NATSMetrics
- test_player_event_handlers.py
- get_async_session
- setup.ts
- test_windows_safe_rotation.py
- MessageFilteringHelper
- test_message_handlers.py
- character-cleanup.ts
- RealTimeEventHandler
- AI Executor Protocol
- HealthMonitor
- player_combat_service_support.py
- system_monitoring.py
- TestCombatMessagingService
- Hierarchical Schema Tests
- PlayerRead
- Configuration Architecture Docs
- Execution Steps
- handle_quest_command
- test_combat_persistence_handler_persistence.py
- SubjectValidator
- NATS Code Review
- AliasGraph
- ChatHistoryPanel.tsx
- realtime/realtime.py
- Memory Leak Prevention
- SchemaValidator
- TestCheckGracePeriodBlock
- test_item.py
- File-by-File Changes
- Player
- PlayerPositionService
- _MagicServiceCore
- map_minimap.py
- TestNPCCombatRewards
- send_game_event
- Container Looting Scenarios
- websocket_handler_commands.py
- StyleGuideSections.tsx
- look_command.py
- utils/layout.ts
- multiplayer-browser-helpers.js
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- Structured Error Logging
- emotes.schema.json
- PatternNotFoundError
- hallucinations.py
- WebSocket Handler Tests
- message_handler_factory.py
- generate_sql.mjs
- test_world.py
- roomHandlers.ts
- Enhanced Logging Migration Complete
- Migration Final Report
- Structlog Implementation Plan
- HealthService
- combat_attack.py
- MythosLoginForm.tsx
- test_magic_commands.py
- PlayerRepositoryProtocol
- Test Coverage Gaps
- MovementMonitor
- test_connection_cleaner.py
- test_event_publisher.py
- useMythosAppState.ts
- RoomCacheLoader
- admin_teleport_commands.py
- UUID
- test_maps.py
- Three-Column Game UI Layout
- worktree-ops.py
- e2e-bootstrap.ts
- CORSConfig
- MonitoringPanel.tsx
- authenticated.ts
- test_command_exploration.py
- TestUtilityFunctions
- Any
- AuditLogger
- command_handler_unified.py
- test_command_base.py
- test_movement_monitor.py
- validate_calendar.py
- shutdown_sequence.py
- useRoomEditModal.ts
- NPCEventHandler
- NATS Subject Manager Review
- hash_password
- debugLogger
- UserManagerProtocol
- NPCStartupService
- real_time.py
- Migration Strategy
- ChatPoseManager
- get_cached_player
- devDependencies
- TestCombatConfigurationService
- test_communication_commands_flows.py
- test_quest_service_collect.py
- retry.py
- Any
- test_health_monitor.py
- CommandPanel.tsx
- inventory_pickup_command.py
- Emote Schema Definition
- Dependency Upgrade Report
- performance.test.tsx
- FeedbackManager
- Architecture Remediation Implementation Summary
- Feature Requirements Document: Random Stats Generator
- test_room_occupant_manager.py
- test_lru_cache.py
- ValidationRule
- test_player_preferences_service.py
- npc_database.py
- stateNormalization.ts
- Async Persistence Migration
- Dependency Upgrade Strategy Specification
- deprecated_patterns.py
- RespawnPlayerEventPayload
- _str_id
- NATSConnectionStateMachine
- LucidityRepository
- test_dependency_analysis.py
- teach_command.py
- test_who_commands.py
- test_command_factories_combat.py
- Advanced Chat Channels Specification
- test_chat_logger.py
- properties
- MythosMUD Dependency Upgrade Strategy - Implementation Summary
- testing_examples.py
- compilerOptions
- Authoritative Environment DML
- Execution Steps
- Execution Steps
- designTokens.ts
- format_metadata
- log_with_context
- Communities (19 total, 4 thin omitted)
- projectorRoom.ts
- security.ts
- generate_html_visualization.py
- Execution Steps
- reset_config
- channel_broadcasting_strategies.py
- Migration 019 Ready for Deployment
- players.py
- test_flee_command.py
- test_command_alias.py
- Test Suite Refactoring Plan
- asyncio
- EmoteService
- websocket_handler.py
- SkillAssignmentScreen.tsx
- correct_patterns.py
- Environment Contamination Audit Report
- ContainerFactoryOptions
- Process Scope NATS Scripts
- Execution Steps
- connection_manager.py
- test_population_control.py
- Dependency Upgrade Strategy
- useThemeContext.ts
- multiplayer-browser-helpers.bundle.js
- codacy.yaml Tool Manifest
- CombatConfiguration
- GameTerminal.tsx
- build_event
- datetime
- get_npc_name_from_instance
- format_message_content
- GameClientV2.tsx
- TestVerificationSqlUsersPlayers
- MythosPanel.tsx
- CombatDPSync
- NATSRetryHandler
- Logout Error Scenarios
- test_player_related_models.py
- test_inventory_mutation_guard.py
- container_helpers_inventory_display.py
- mock_container
- static_data/package.json
- NPCCombatLucidity
- Lint Remediation Prompt - AI-Optimized Version
- ADR-012: python-statemachine for Backend Connection FSM
- TypeScript Compiler Config
- enum
- WebSocket Compliance Review
- properties
- EdgeDetailsPanel.tsx
- E2E Multiplayer Findings
- useGameTerminal.ts
- test_inventory_mutation_guard_internal.py
- PostgresConnection
- properties
- get_cache_manager
- Execution Steps
- Alertmanager Monitoring Stack
- handle_emote_command
- Any
- MessageBroadcaster
- World Seed Loader
- edgeModalLogic.ts
- React Node Upgrade Analyzer
- test_combat_flee_helpers.py
- fastapi_integration.py
- logger.ts
- Cursor Subagents Overview
- HolidayService
- Multiplayer Architecture Planning
- NPCOccupantProcessor
- room_validator/tests/conftest.py
- Lint Remediation Prompt - AI-Optimized Version
- Execution Steps
- asyncio
- ADR-003 Dual Event Systems EventBus NATS
- MovementService
- Linting Complexity Alignment
- Pre-commit Logging Validation
- errorHandler.ts
- test_room_subscription_manager_npcs.py
- test_security_headers.py
- Rate Limiting Scenario Blocked
- usePanelContext.ts
- RoomCacheService
- Phase 1: Core Separation
- Disconnect Grace Period Design
- MythosMUD UI Component Library
- player_connection_setup.py
- Phase 2: Enhanced Features
- type
- generate_sql.mjs
- PrototypeRegistry
- test_instance_manager.py
- test_calendar.py
- GameTickService
- LRUCache
- Dual Connection System Spec
- TestPathValidator
- test_event_bus.py
- server/tests/conftest.py
- server/services/__init__.py
- optimized_validate_player_name
- optimized_security_validator.py
- PanelContextRuntime.tsx
- RoomInfo.tsx
- BehaviorEngine
- MessageBatcher
- required
- schemas/unified_room_schema.json
- debrief_command.py
- Communities (11 total, 0 thin omitted)
- Test Server Remediation Prompt - Cursor Executable Version
- required
- Chat Panel Separation Implementation Tasks
- Communities (11 total, 0 thin omitted)
- update_container
- test_look_item.py
- ChatPanelRefactoredView.tsx
- ChatLogger
- test_emote.py
- Communities (10 total, 0 thin omitted)
- _format_npc_description
- npc_config_parsing.py
- AttributeError
- NATS Remediation Summary 2026-01-13
- patch
- test_statistics_aggregator.py
- generate_invites_db.py
- test_channel_broadcasting_strategies.py
- UnknownChannelStrategy
- verify_linting_parity.py
- CoordinateGenerator
- properties
- ._get_random_error_message
- messageHandlers.ts
- DatabaseManager
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- Phase 3: Polish and Optimization
- Phase 4: Testing and Refinement
- Unified Command Handler Plan
- test_websocket_handler_validation_errors.py
- fix_fstring_logging.py
- Client README Overview
- TestLogoutCommand
- properties
- Path
- Configuration Files Reference
- RoomBasedChannelStrategy
- Ruff Pylint Mapping
- _find_item_in_equipped
- chat_nats_publisher.py
- Whisper Scenario Test Report
- properties
- Communities (10 total, 2 thin omitted)
- test_event_publisher_helpers.py
- StatisticsAggregator
- properties
- MapPerformanceMonitor
- 1774539086359-useMythosAppState.ts
- properties
- Error Log Analyzer
- properties
- required
- ShopkeeperNPC
- asyncio
- CoordinateValidator
- _find_item_in_inventory
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)
- deque
- test_command_processor.py
- SessionManager
- test_combat_persistence_handler.py
- test_player_event_handlers_utils.py
- .to_dict
- patch
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)
- room_hierarchy_schema.json
- GridLayoutManager.tsx
- test_room_service.py
- Game Subsystem Design Documents
- REQUIRED TOOL USAGE PATTERN
- CircuitBreaker Implementation Planning Document
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)
- properties
- properties
- ModalContainer.tsx
- multiplayer-playwright-testing.md
- Mypy Type Checking Remediation Prompt - AI-Optimized Version
- fixture
- ItemFactory
- Movement Subsystem Design
- load_test_10_players.spec.ts
- enum
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)
- properties
- days
- enum
- _get_npc_room_id
- Comprehensive System Audit
- NATSEventBusBridge
- NPCCommunicationIntegration
- MagicServiceCompletionMixin
- Security Implementation
- test_level_service.py
- migrate_combat_data.py
- PersonalMessageSender
- Enhanced Logging Migration Report
- send_welcome_event
- TestMinimapExplorationInvestigationDoc
- test_player_event_handlers_room.py
- validate_inventory_payload
- PostgresRow
- TestValidateCommandBasics
- RateLimiter
- get_room_environment
- optimized_validate_action_content
- optimized_validate_alias_name
- PlayerGuidFormatter
- optimized_sanitize_unicode_input
- optimized_validate_security_comprehensive
- Runner Path
- inventory_put_command.py
- combat_flee_handler.py
- enum
- properties
- run-playwright-tests.js
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- required
- Lint Sqlalchemy Async
- quality_fragmentation_lizard.py
- applies_to
- required
- Technical Implementation
- Implementation Notes
- _holiday_entry_from_row
- test_connection_event_helpers.py
- test_inventory_mutation_guard_async.py
- party_commands.py
- zone_schema.json
- _mock_result_mappings_all
- required
- quality_fragmentation_graph.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)
- fixture
- Realtime Connection Compatibility
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)
- format_markdown_file
- Migrate Rooms
- run-vitest.js
- usePerformanceMonitor.ts
- holidays.schema.json
- npc_schedules.schema.json
- 1. Enhanced ChatPanel (New Chat Input Panel)
- Implementation Phases
- MockPersistence
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
- asyncio
- CombatPersistenceHandler
- rescue_service.py
- test_player_event_handlers_room_left.py
- utils/config.ts
- test_async_persistence_room_loading.py
- UUID
- enabled
- plane
- test_combat_messaging_integration.py
- test_rate_limiter.py
- RoomInfoPanel.tsx
- PartyService
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- Security Infrastructure
- MetricsCollector
- optimized_validate_filter_name
- optimized_validate_target_player
- optimized_validate_help_topic
- Verify Migration
- optimized_comprehensive_sanitize_input
- required
- useGridLayout.ts
- Geography Overview.md
- Chat Panel Separation Specification
- test_combat_flee_handler.py
- enum
- enum
- room_validator/schemas/unified_room_schema.json
- enum
- 🔧 COMMON FIX TEMPLATES
- Archive Who Command
- 🔧 COMMON FIX TEMPLATES
- Quality Fragmentation Guard
- E 2 E Readme Playwright
- Tsconfig App
- Tsconfig Build
- 🔧 COMMON FIX TEMPLATES
- Common Test Failure Categories
- FAILURE PATTERN RECOGNITION
- MUD Disconnect Grace Period & Rest Command: Industry Comparison
- items
- ComprehensiveLoggingMiddleware
- items
- Application Container Analysis
- Async Anti Patterns
- Implementation Details
- Client Layout Baseline
- _container_data_to_dict
- get_help_content
- .handle_player_death
- Quest System Features
- Testing Guide
- test_combat_service.py
- Any
- test_zone_config_loader.py
- Security Infrastructure
- populate_test_npc_databases.py
- test_skill_service.py
- test_websocket_handler_error_handling.py
- .on_enter_state
- container
- Local Channel System
- Fix Suppression Alignment
- Identify Critical Code
- AdminActionsLogger
- CommunicationIntegrationProtocol
- holidays
- schedules
- TestCombatParticipantData
- _process_session_dp_decay_and_death
- CommandRequest
- test_player_repository.py
- asyncio
- _occupation_slots_9
- UUID
- .create_supervised_task
- asyncio
- ItemPrototypeModel
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)
- Updated Coverage Targets
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)
- TestCheckRateLimit
- Cursor Hooks Record
- Command Handler Patterns
- _personal_interest_4
- test_profession.py
- reset_database
- E 2 E Scenario Scenarios
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)
- IdleMovementHandler
- _should_include_npc
- test_metrics.py
- test_metadata.py
- lifespan_shutdown.py
- ErrorContext
- field_validator
- Invite
- Audit Suppressions
- Fix Markdown Line
- Populate Npc Sample
- quest_events.py
- ._error_callback
- start_hour
- AsciiMapRenderer
- test_inventory_mutation_guard_error_handling.py
- .__call__
- NATSSubjectManager
- Package Scripts Build
- test_game_enums.py
- Tsconfig Node
- validate_shutdown_admin_permission
- test_npc_service.py
- connectionStore.ts
- ClientLogger
- persistence/container_helpers.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)
- ConnectionPanel.tsx
- global-teardown.ts
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)
- ScheduleCollection
- Phase 2: Categorize and Prioritize Mypy Issues
- Phase 5: Fix Implementation Patterns
- 4. Common Fix Patterns
- DML Migrations
- AppConfig
- Lint Logging Patterns
- enum
- Local Readme Motd
- UI/UX Considerations
- Any
- Middleware Command Rate
- fix_markdown_common_issues.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)
- 3. Simplified CommandPanel
- Implementation Phases
- asyncio
- MagicServiceHealingMixin
- Any
- Upgrade Implementation Plan
- ConnectionMetadata
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
- Domain Model Anemic Anti-Pattern Audit
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
- .detect_and_handle_error_state
- send_system_message
- 8. Error Handling and Debugging
- test_invite_schemas.py
- Real-Time Architecture
- test_grype.py
- description
- name
- MockEventClass
- VirtualizedMessageList.tsx
- generate_unique_codes
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
- combat_helpers.py
- 8. Grace Period After Intentional Disconnect
- 9. Command Blocking During Grace Period
- Recommendations Summary
- Code Graph Entry
- DML Migrations Apply Paths
- Cosmic Horror.md
- get_database_path
- day
- duration_hours
- test_websocket_handler_validation.py
- month
- days
- effects
- end_hour
- start_hour
- exits
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)
- Migration Considerations
- E 2 E Scenario Template
- Success Criteria
- Risk Assessment
- Testing Strategy
- Phase 2: Database Layer Integration
- Phase 3: Real-Time Communication Protection
- Phase 4: File System Operations
- Phase 6: Monitoring and Observability
- E 2 E Scenarios Scenario
- Future Enhancements
- Monitoring and Alerting
- Success Criteria
- Schemas Readme
- Npc Database
- Testing Strategy
- fixtures/shared/__init__.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)
- Phase 2: Categorize and Prioritize Lint Issues
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)
- test_player_service.py
- Any
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
- sample_container
- sub_zone
- zone
- main
- start_server.ps1
- _utc_now
- .is_alive
- Profession
- UUID
- main
- Any
- asyncio
- test_validate_secure_path_path_traversal_commonpath
- test_asyncio_run_guardrails.py
- description
- exits
- name
- plane
- Fix Markdownlint
- Jackson Linter
- Migrate Room Filenames
- handle_system_command
- FeatureFlagService
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
- Mythosmud Obsidian Wiki
- _errors_len
- 🚨 AI ERROR HANDLING
- Event Ownership Matrix
- Step-by-Step Remediation Process
- asyncio
- Graphify Code Graph
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)
- Chaosium CoC Catalog
- plane
- AI Development Workflow
- Architecture Overview
- Any
- test_skills.py
- Cursor Skills Skill
- weight
- skills_commands.py
- handle_explore_command
- quest_service.py
- _row_to_profession
- ._generate_alert
- fix_markdown_file
- analyze-product.md
- create-spec.md
- Analyze Coverage Gaps
- Apply Arena Seed
- create-tasks.md
- execute-tasks.md
- TestCheckAllCommandBlocks
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
- id
- fixture
- Room Subscription Timing Race
- Deprecated get_async_persistence Global
- schemas/__init__.py
- High-Risk Major Package Updates
- Pre Commit Config
- constants/__init__.py
- fixture
- _spawn_rule_row
- fixture
- entities/__init__.py
- domain/events/__init__.py
- domain/__init__.py
- domain/repositories/__init__.py
- domain/services/__init__.py
- value_objects/__init__.py
- server/game/magic/__init__.py
- load_motd
- MemoryMonitor
- Security Infrastructure
- Invite Readme
- .select_exit
- test_utility_commands_whoami.py
- zone
- persistence/utils/__init__.py
- SecureBaseModel
- server/structured_logging/__init__.py
- Cursor Plans Pydantic
- server/tests/__init__.py
- command_handler_unified/__init__.py
- npc_service
- test_websocket_handler_rate_limit.py
- test_error_logging.py
- Party
- monitoring_service
- ._attack_target_impl
- CombatConfigurationScope
- Standardize Room Names
- Validate Codacy Coverage
- Check No Production
- PrototypeRegistryError
- dummy_request
- TestResolveExitTarget
- TestHorizontalExitCharBetween
- .call
- .check_and_interrupt_rest
- UUID
- unit/container_persistence/__init__.py
- unit/game/magic/__init__.py
- .load_file
- test_npc_event_handlers.py
- fixture
- AGENTS.md agent instructions
- ._get_vertical_exit_char
- Architecture Decisions Adr
- Fixture Optimization Complete
- fixture
- asyncio
- Check No Production
- event_handler
- overrides
- test_ascii_map_renderer_exits.py
- Phase 2: Categorize and Prioritize Lint Issues
- Cursor Workflows
- test_ascii_map_renderer_grid.py
- calculate_notification_times
- SQLAlchemy Async Best Practices
- E 2 E Load Analyze
- .handle_attack_command
- fixture
- _send_combat_participant_updates
- .__init__
- InviteBase
- .perform_recovery_action
- .respawn_player_by_user_id
- .profession_to_dict
- bind_request_context
- .__init__
- Alert
- mock_async_persistence
- mock_app
- Server Realtime Module
- mock_connection_manager
- add_suppression_to_file
- sub_zone
- Check Logging Patterns
- Lint Sql Guardrails
- mock_persistence
- asyncio
- .auto_progression_enabled
- 📊 LINT ISSUE CATEGORIZATION GUIDE
- test_get_adjacent_rooms_source_not_found
- graceful_degradation
- test_process_exit_rows_debug_logging
- .get_stat_requirements
- test_process_room_rows_with_full_room_id
- .handle_player_message
- schemas/auth/__init__.py
- InviteCreate
- TestGetExitEntriesForRoom
- quest_service
- test_process_room_rows_empty_list
- test_process_exit_rows_empty_list
- test_process_exit_rows_multiple_exits_same_room
- Archive Planning E 2 E
- sub_zone
- test_nats_service_init_with_subject_manager
- unit/infrastructure/__init__.py
- test_process_exit_rows_zone_single_part
- idle_movement_handler
- Knip Entry Ignore Dependencies
- dependencies
- test_process_room_rows_with_partial_room_id
- test_build_room_objects_with_dict_attributes
- test_build_room_objects_without_environment_in_attributes
- asyncio
- persistence_handler
- MagicPointsMeter.tsx
- Azotottal.md
- .get_professions
- test_process_room_rows_with_none_attributes
- test_process_room_rows_zone_without_slash
- .validate_target_player
- _EventBusPublishPort
- Mythosmud Obsidian Sources
- test_cold_damage_resistance_reduces_damage
- test_filter_other_players_adds_linkdead_indicator
- persistence_handler
- registry_with_switchblade
- player_service
- nats_broker
- exploration_service
- .sample_holidays
- webhook
- nats_service
- Schemas Intersection Schema
- Schemas Room Schema
- properties
- Arkham Rooms Summary
- Fix Markdownlint Errors
- Fix Syntax Errors
- user_manager
- ._exit_is_bidirectional
- CombatAuditLogger
- unit/middleware/__init__.py
- unit/monitoring/__init__.py
- unit/persistence/__init__.py
- unit/realtime/integration/__init__.py
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- get_combat_monitoring
- test_mp_regeneration_service.py
- .__init__
- description
- id
- applies_to
- metadata
- .get_room_data
- .room_forbids_combat
- .validate_combat_action
- .validate_target_name
- Mythosmud Obsidian Readme
- test_build_room_objects_with_exits
- generate_schema_from_dev.ps1
- mock_lifecycle_manager
- .__init__
- Nameless Horrors - 2nd Edition (source summary)
- S. Petersen's Field Guide to Lovecraftian Horrors (source summary)
- test_broadcast_combat_end
- eslint.config.js
- test_broadcast_player_died
- test_broadcast_player_mortally_wounded_with_attacker
- test_broadcast_player_mortally_wounded_no_attacker
- get_alerts
- .__init__
- .__init__
- test_connection_manager_lazy_load_called
- mock_persistence
- Cursor Hooks Development Plan
- event_bus
- test_broadcast_player_mortally_wounded_personal_message_error
- asyncio
- test_send_dp_decay_message
- test_send_dp_decay_message_error
- E 2 E Scenarios Scenario
- party_service
- mock_connection_manager
- Grype Command Handle Result
- Visualize Arkham Rooms
- test_get_player_combat_data_uses_get_combat_stats
- autoprefixer
- ._log_error
- Validate Codacy Coverage
- .check_casting_progress
- snapshot_chaosium_graphify.ps1
- ._auto_center_viewport
- test_broadcast_combat_attack
- get_session_maker
- test_event_bus_set_main_loop
- test_event_bus_unsubscribe_multiple_handlers
- test_event_bus_get_all_subscriber_counts_empty
- npc_startup_service
- test_event_bus_get_all_subscriber_counts_multiple_types
- esbuild
- eslint
- eslint-plugin-jsx-a11y
- happy-dom
- markdownlint-cli
- Github Workflows Ci
- Claude Commands Product
- patch-package
- @playwright/test
- @testing-library/dom
- @testing-library/react
- @testing-library/user-event
- Cursor Mcp
- Owner and App Roles Per Environment
- vite
- @vitejs/plugin-react
- test_event_bus_publish_no_subscribers
- Enhanced Logging Guide
- test_subscribe_invalid_event_type
- test_subscribe_invalid_handler
- test_unsubscribe_invalid_event_type
- Audit Executive Summary
- test_event_bus_init
- Github Pull Request
- add_fastapi_users_columns.py
- add_hashed_password_column.py
- add_used_by_user_id_column.py
- test_handle_task_result_async_with_error
- rename_invites_columns.py
- test_unsubscribe_all_for_service
- test_unsubscribe_all_for_service_nonexistent
- .__init__
- test_event_bus_get_subscriber_count
- test_event_bus_get_subscriber_count_none
- test_build_room_objects_with_non_dict_attributes
- test_profession_get_mechanical_effects_invalid_json
- test_profession_get_mechanical_effects_empty_string
- Whisper Channel System
- properties
- test_profession_set_mechanical_effects
- properties
- Analyze Comments
- Check Apply Map
- Check Coverage Thresholds
- Simple Room Graph
- test_profession_repr
- test_profession_meets_stat_requirements_multiple_not_met
- test_profession_meets_stat_requirements_empty_requirements
- test_profession_meets_stat_requirements_invalid_json
- test_profession_meets_stat_requirements_extra_stats
- test_profession_is_available_for_selection_false
- test_profession_get_requirement_display_text_no_requirements
- Cursor Skills Skill
- test_profession_get_requirement_display_text_multiple_requirements
- test_profession_get_stat_requirements_empty_string
- test_profession_get_stat_requirements_none
- test_get_player_by_name_not_found
- test_list_players
- test_resolve_player_name_found
- test_profession_set_stat_requirements
- test_profession_set_stat_requirements_empty_dict
- test_create_player_with_stats_name_exists
- Plan Cursor Plans
- test_player_service_init
- test_validate_player_name_valid
- test_room_has_player
- test_room_has_object
- test_select_exit_empty_dict
- test_calculate_distance_to_room_same_subzone
- test_delete_player_success
- test_delete_player_not_found
- unit/services/nats_subject_manager/__init__.py
- messaging_integration
- test_update_player_location_success
- test_idle_movement_handler_init
- test_apply_fear
- test_get_player_lucidity_tier_default
- test_validate_chat_message_fields_sender_name_type_error
- test_soft_delete_character_not_found
- test_soft_delete_character_wrong_user
- test_validate_player_name_whitespace
- test_validate_player_name_invalid_characters
- test_delete_player_persistence_fails
- Readme Migrations
- test_soft_delete_character_persistence_fails
- test_create_player_name_exists
- test_apply_fear_player_not_found
- test_validate_chat_message_fields_content_type_error
- test_damage_player_player_not_found
- test_validate_player_name_too_short_one_char
- test_extract_chat_message_fields_whisper_target_id
- Python Coverage Status
- test_get_room_persistence_not_found
- Security Environment Variables
- test_get_room_persistence_returns_dict
- test_get_adjacent_rooms_success
- test_get_adjacent_rooms_null_exit
- test_get_local_chat_scope
- test_get_local_chat_scope_source_not_found
- test_validate_room_exists_cache_not_found
- test_validate_exit_exists_success
- Npc Lifecycle Respawn
- test_validate_exit_exists_invalid
- rename_used_to_is_active.py
- test_extract_chat_message_fields
- test_validate_exit_exists_no_exits
- test_get_room_occupants_with_cache_dict
- test_get_room_occupants_cache_not_found
- test_validate_player_in_room_with_cache_true
- test_validate_player_in_room_with_cache_false
- Persistence Repositories Readme
- test_validate_player_in_room_cache_dict
- Room Toolkit Validator
- test_get_room_exits_success
- test_get_room_exits_no_exits
- test_list_rooms_exclude_exits
- Check Asyncio Run
- Lucidity Migration
- test_get_room_info_success
- test_get_room_info_not_found
- test_alias_storage.py
- test_room_service_init
- test_room_service_init_with_cache
- test_get_room_without_cache
- test_process_exit_rows_with_partial_room_ids
- test_process_message_with_retry_failure
- test_load_room_cache_with_rooms_logs_sample_ids
- test_broadcast_by_channel_type_exception
- rate_limiter
- test_send_messages_to_players_blocked
- test_should_echo_to_sender_not_echo_channel
- test_should_echo_to_sender_with_targets
- test_should_echo_to_sender_no_targets_not_notified
- Church of Sunyata.md
- test_should_echo_to_sender_no_targets_already_notified
- test_echo_message_to_sender_success
- test_broadcast_to_room_with_filtering_exception
- test_apply_dampening_and_send_message_exception
- Dark Young of Shub-Niggurath.md
- Dimensional Shambler.md
- test_get_player_lucidity_tier_with_uuid
- test_build_chat_event
- Testing Map Regression
- test_convert_ids_to_uuids
- A Cold Fire Within (source summary)
- Alone Against the Dark (source summary)
- test_convert_ids_to_uuids_none_target
- Alone Against the Frost (source summary)
- test_format_message_for_receiver
- Alone against the Tide (source summary)
- test_get_player_lucidity_tier
- test_subscribe_to_subzone_no_subject_manager
- Package Engines Node
- include
- Vite Config Proxyauthorization
- test_subscribe_to_event_subjects_partial_failure
- Berlin - The Wicked City (source summary)
- Cursor Hooks Trigger
- mythos_dev mythos_unit mythos_e2e Databases
- test_unsubscribe_from_subzone_decrease_count
- Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)
- test_handle_player_movement_old_subzone_none
- Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)
- test_handle_player_movement_new_subzone_none
- Call of Cthulhu Investigator Handbook 7th Edition (source summary)
- test_handle_player_movement_error
- Call of Cthulhu Keeper Tips (source summary)
- test_subscribe_to_subzone_subscribe_failure
- test_unsubscribe_from_subzone_unsubscribe_failure
- Call of Cthulhu Starter Set (source summary)
- Call of Cthulhu_ The Coloring Book (source summary)
- test_handle_combat_started_event
- test_handle_combat_ended_event
- test_handle_npc_attacked_event
- test_broadcast_combat_error
- Cursor Skills Mythosmud
- overrides
- test_handle_npc_took_damage_event
- test_broadcast_player_respawn_personal_message_error
- test_broadcast_combat_error_send_error
- test_handle_npc_died_event
- test_handle_player_movement_different_subzone
- character_sheets (source summary)
- Room Validator Toolkit
- Room Toolkit Validator
- Cthulhu Dark Ages - 3rd Edition (source summary)
- Dead Light and Other Dark Turns (source summary)
- Filter Static Dml
- Fix Room References
- Player Inventory Migration
- Does Love Forgive_ (source summary)
- Run Bug Prevention
- Doors to Darkness (source summary)
- Down Darker Trails (source summary)
- test_logging_handlers.py
- Gateways to Terror (source summary)
- Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)
- Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)
- The Grand Grimoire of Cthulhu Mythos Magic (source summary)
- Cursor Templates Worktree
- The Malleus Monstrorum Keeper Deck (source summary)
- test_handle_player_movement_same_subzone
- zone
- test_handle_player_movement_exception
- prototype_registry.py
- test_broadcast_combat_attack_personal_message_error
- test_end_combat_monitoring_failure
- test_end_combat_monitoring_not_found
- Chaosium graphify snapshot - A Cold Fire Within
- Codacy Cli
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
- E 2 E Report Whisper
- MythosMUD Obsidian Vault
- Components Ui V 2
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
- Security Infrastructure
- Chaosium graphify snapshot - character_sheets
- Test Refactoring Executive Summary
- Async Code Review Post Migration
- Migrate Async Persistence
- Phase 2 Service Layer Migration
- Chaosium graphify snapshot - Cthulhu Dark Ages - 3rd Edition
- Migration 019 Verification
- Whisper System Production-Ready
- Structured Logging Correct Patterns
- Chaosium graphify snapshot - Dead Light and Other Dark Turns
- mythosmud
- Apply Quest Migrations
- Migrate Npc
- HealthRepository
- RoomRepository
- Memory Leak Monitoring Endpoints
- PostgreSQL Player Persistence
- World Loading
- invites table
- Mythos-themed invite codes
- jsonschema dependency
- Chaosium graphify snapshot - Does Love Forgive_
- Mythos Holiday Candidates
- Chaosium graphify snapshot - Doors to Darkness
- Chaosium graphify snapshot - Down Darker Trails
- Chaosium graphify snapshot - Gateways to Terror
- Persistence Repository Architecture
- Chaosium graphify snapshot - Malleus Monstrorum - Cthulhu Mythos Bestiary
- Chaosium graphify snapshot - Mansions of Madness_ Vol 1 - Behind Closed Doors
- Chaosium graphify snapshot - Nameless Horrors - 2nd Edition
- Chaosium graphify snapshot - Petersen's Abominations
- Chaosium graphify snapshot - Pulp Cthulhu (7th edition Call of Cthulhu)
- test_logging_processors.py
- Chaosium graphify snapshot - Reign of Terror
- Chaosium graphify snapshot - S. Petersen's Field Guide to Lovecraftian Horrors
- Chaosium graphify snapshot - The Grand Grimoire of Cthulhu Mythos Magic
- E 2 E Scenarios Lucidity
- Chaosium graphify snapshot - The Malleus Monstrorum Keeper Deck
- Petersen's Abominations (source summary)
- Pulp Cthulhu (7th edition Call of Cthulhu) (source summary)
- Reign of Terror (source summary)
- test_end_turn_monitoring_not_found
- test_record_combat_error_validation
- .validate_direction
- test_record_combat_error_system
- Cursor Plans Plan
- exception_metrics.py
- Schemas Intersection Schema
- test_update_resource_metrics
- PerformanceStats
- Schemas Room Schema
- Generate Html Visualization
- test_resolve_alert_not_found
- Investigations Sessions Session
- Investigations Sessions Combat
- Investigations Sessions Session
- Subsystems Subsystem Design
- test_check_error_threshold
- Chat Panel
- test_grace_period_blocking.py
- combat_validator
- Dietrich Zann.md
- Flying Polyp.md
- Fungi from Yuggoth.md
- Ghoul.md
- Hotel Hell.md
- Mohole.md
- .save_player
- Room
- test_check_resource_thresholds_memory
- test_check_performance_threshold
- test_get_combat_metrics
- test_update_timing_metrics
- .add_item_to_inventory
- test_start_combat_monitoring
- test_create_spawn_rule_invalid_min_population
- test_authentication_error
- test_configuration_error
- test_network_error
- test_resource_not_found_error
- test_mythos_mud_error_with_details
- MythosMUD Server Test Suite
- test_mythos_mud_error_with_user_friendly
- test_authentication_error_initialization
- test_configuration_error_initialization
- test_network_error_initialization
- test_network_error_default_connection_type
- test_get_player_by_id_not_found
- test_get_player_by_name_found
- test_resolve_player_name_not_found
- test_create_player_with_stats_character_limit
- test_validate_player_name_too_long
- test_validate_player_name_exists
- test_create_player_success
- test_get_online_players
- test_apply_lucidity_loss
- test_damage_player
- test_soft_delete_character_success
- test_gain_occult_knowledge_player_not_found
- test_get_player_by_id_found
- test_build_room_objects_debug_logging
- Player Command Developer
- test_evaluate_equality_false
- test_evaluate_equality_string
- test_behavior_engine_init
- test_evaluate_equality_not_equality
- test_evaluate_equality_invalid_format
- test_evaluate_inequality_true
- test_evaluate_inequality_false
- test_evaluate_inequality_not_inequality
- test_evaluate_numeric_comparison_greater_equal
- test_evaluate_numeric_comparison_less_equal
- test_add_rule_success
- test_evaluate_numeric_comparison_false
- test_evaluate_condition_equality
- test_evaluate_condition_inequality
- test_evaluate_condition_greater_than
- test_evaluate_condition_less_than
- test_evaluate_condition_less_equal
- Cursor Plans Plan
- test_evaluate_condition_unknown
- Pyrightconfig Extends Extra Paths
- test_get_applicable_rules_no_matching
- test_execute_applicable_rules_no_matching
- Room Toolkit Validator
- test_execute_applicable_rules_executes_highest_priority
- test_add_rule_missing_fields
- test_execute_applicable_rules_no_handler
- Check Logging Consistency
- e2e_reset_players.py
- test_register_action_handler
- test_register_action_handler_overwrites
- test_state_direct_access
- Investigations Sessions Session
- test_execute_action_success
- test_evaluate_boolean_condition_false
- test_evaluate_boolean_condition_variable_false
- test_remove_rule_success
- Investigations Sessions Session
- Investigations Sessions Session
- test_remove_rule_not_found
- Investigations Sessions Session
- test_whisper_channel_strategy_broadcast
- Cursor Skills Mythosmud
- test_resource_not_found_error_initialization
- Enhanced Structured Logging System
- test_resource_not_found_error_partial
- test_create_channel_command
- test_create_get_command
- test_create_equip_command
- test_create_unmute_global_command
- test_command_factory_init
- test_create_time_command
- test_create_logout_command
- test_create_rest_command
- Archive System Magic
- Archive Lucidity System
- test_create_kick_command
- test_create_alias_command
- test_create_npc_command
- Archive Room Planning
- test_create_summon_command
- test_create_goto_command
- test_command_factory_has_create_methods
- test_broadcast_combat_attack_with_attacker_id
- test_create_cast_command
- test_update_npc_definition_invalid_type
- test_update_npc_definition_invalid_probability
- test_create_learn_command
- test_command_factory_create_nonexistent_command
- test_create_local_command
- test_create_system_command
- test_create_emote_command
- Cursor Commands New
- test_create_reply_command
- E 2 E Comprehensive Overview
- E 2 E Multiplayer Rules
- Codacy Instructions Review
- test_check_rate_limit_within_limits
- Cursor Plans Plan
- Remediation Investigations Plans
- Schemas Intersection Schema
- Schemas Intersection Schema
- Schemas Intersection Schema
- Schemas Room Schema
- Schemas Room Schema
- test_broadcast_player_mortally_wounded
- Schemas Unified Room
- test_check_rate_limit_exceeds_limit
- test_record_message
- test_record_message_error_handling
- Batch Fix Suppressions
- Check Codacy Yaml
- test_reset_player_limits_specific_channel
- test_reset_player_limits_all_channels
- test_get_system_stats
- test_postgres_adapter.py
- test_get_system_stats_no_players
- Cursor Skills Mythosmud
- test_is_player_rate_limited_true
- test_is_player_rate_limited_false
- test_get_remaining_messages_error_handling
- test_rate_limit_different_channels
- test_rate_limit_different_players
- test_set_limit
- test_cleanup_old_entries
- test_validate_combat_command_target_too_long
- test_validate_combat_command_rate_limited
- test_validate_combat_command_exception_handling
- test_validate_target_exists_exact_match
- Archive Dual Connection
- test_validate_target_exists_case_insensitive
- test_validate_target_exists_partial_match
- test_validate_target_exists_no_match
- test_validate_target_exists_no_target_name
- test_validate_target_alive_alive
- test_validate_target_alive_dead
- test_validate_combat_state_in_combat_required
- Scenario 42 Quest Log Visible After Login
- test_validate_combat_state_not_in_combat_required
- test_combat_validator_init
- Archive Prd
- test_validate_combat_state_in_combat_not_required
- test_validate_combat_state_not_in_combat_not_required
- test_validate_attack_strength_success
- test_validate_attack_strength_target_too_strong
- test_validate_attack_strength_weak_weapon
- test_is_valid_target_name_valid
- test_is_valid_target_name_invalid
- test_validate_combat_command_valid
- test_contains_suspicious_patterns_detected
- test_is_rate_limited
- test_get_random_error_message
- test_get_combat_status_message_in_combat
- test_get_combat_status_message_not_in_combat
- test_get_combat_result_message_success_with_damage
- test_get_combat_result_message_success_no_damage
- Verify Schema Match
- test_get_combat_result_message_failure
- test_get_combat_death_message
- test_get_combat_victory_message
- test_validate_combat_command_all_attack_aliases
- test_validate_combat_state_edge_case_return_true
- test_validate_combat_command_suspicious_patterns_with_mock
- Claude Authoritative Reference
- test_validate_can_attack_target_no_party_service_allows
- test_validate_can_attack_target_same_party_blocks
- test_validate_can_attack_target_different_party_allows
- test_validate_combat_command_target_too_long_with_mock
- test_validate_combat_command_no_target
- test_validate_combat_command_invalid_target_name
- test_validate_combat_command_suspicious_patterns
- Logging Best Practices
- E 2 E Execution Validation
- E 2 E Scenario Blocked
- Cursor Plans Plan
- E 2 E Scenarios Scenario
- Schemas Intersection Schema
- Schemas Room Schema
- Schemas Room Schema
- Schemas Room Schema
- Schemas Unified Room
- Apply Players Migration
- Precommit Run Npm
- Verify Tutorial Migrations
- F-String Logging Violations
- Investigations Sessions Movement
- Investigations Sessions Session
- Archive Character Creation
- Archive Cleanup Dead
- Archive Connection Termination
- Archive Plan Warning
- Archive Planning Stats
- Archive Party System
- Archive Migration Completion
- Check Postgresql
- Setup Postgresql
- Anyio Vs Asyncio
- Message Handling
- Coverage Easy Wins
- Dead Code
- Fastapi Code Review
- Github Workflows Dependency
- Load E 2 E Analysis
- Cursor Plans Plan
- Plans Gladiator Ring
- Cursor Plans Plan
- Plan Cursor Plans
- Plan Cursor Plans
- Cursor Plans Authority
- E 2 E Scenarios Scenario
- Clean Path Remove Dir
- Load Seed Via
- Markdownlint Safe Print
- Parse Lint Findings
- Verify E 2 E Users
- Investigations Sessions Session
- Investigations Sessions Session
- Investigations Sessions Session
- Subsystems Subsystem Rescue
- Subsystems Subsystem Rest
- Subsystems Subsystem Skills
- Archive Architecture Improvements
- Archive Combat Health
- Archive Fixture Optimization
- Archive Panel Layout
- Archive Postgresql Code
- Archive Scenario Conversion
- Archive Security Fixes
- Archive Security Sanitization
- Archive Temporal Npc
- Assets React Public
- Codacy Wsl Bashrc
- Ensure Codacy Coverage
- Ensure Uv Ci
- Generate Schema Dev
- Install Ci Dependencies
- Architecture Decisions Adr
- Upgrade Archive Dependency
- Code Review Import
- Debugging Mid Run
- Facades Implementation Summary
- Fresh Session
- Numpy Code Review
- Submodule Setup
- Temporal System Research
- Troubleshooting Guide
- Uvicorn Code Review
- E 2 E Di Migration
- E 2 E Bugs Found
- E 2 E Bugs Found
- E 2 E Cleanup
- E 2 E Mcp Tab
- E 2 E Scenario Limitation
- Github Copilot Instructions
- Github Issue Template
- Github Issue Template
- Item System Archive
- Cursor Plans Generate
- Cursor Plans Coc
- Cursor Plans Plan
- Cursor Plans Convert
- Cursor Plans Plan
- Cursor Plans Eliminate
- Cursor Plans Follow
- Cursor Plans Gladiator
- Cursor Plans Login
- Cursor Plans Remediation
- Cursor Plans Postgresql
- Cursor Plans Plan
- Cursor Plans Requests
- Cursor Plans Uvicorn
- Apply Container Migrations
- Gen Arena Uuids
- Scan Dml Blank
- Security Private Vulnerability Disclosure
- Investigations Sessions Session
- Investigations Sessions Session
- Investigations Sessions Xx
- Investigations Sessions Xx
- Investigations Sessions Xx
- Investigations Sessions Xx
- Investigations Sessions E 2 E
- Investigations Sessions Session
- Investigations Sessions Session
- Investigations Sessions Session
- Investigations Sessions Session
- Design Cursor Skills
- Cursor Skills Mythosmud
- Design Cursor Skills
- Cursor Skills Frontend
- Design Cursor Skills
- Design Cursor Skills
- Cursor Skills Frontend
- Cursor Skills Frontend
- Cursor Skills Mythosmud
- Cursor Skills Skill
- Cursor Skills Mythosmud
- Subsystems Subsystem Who
- GitHub Issues task tracking
- Archive Admin Teleport
- Archive Argon 2 Security
- Archive Datetime Fix
- Archive Semgrep Unicode
- Github Issue Template
- Local Readme
- Cursor Plans Click
- Cursor Plans Code
- Cursor Plans Github
- Cursor Plans Pytest
- Cursor Rules Docker
- Finalize Build Touch

## God Nodes (most connected - your core abstractions)
1. `get_logger()` - 509 edges
2. `User` - 297 edges
3. `LoggedHTTPException` - 257 edges
4. `AliasStorage` - 217 edges
5. `CombatService` - 181 edges
6. `log_and_raise()` - 174 edges
7. `DatabaseError` - 167 edges
8. `CombatParticipant` - 167 edges
9. `AsyncPersistenceLayer` - 163 edges
10. `ConnectionManager` - 162 edges

## Surprising Connections (you probably didn't know these)
- `Grype SCA exclude paths` --semantically_similar_to--> `Codacy exclude_paths`  [INFERRED] [semantically similar]
  .grype.yaml → .codacy.yml
- `Arkham City Graph PNG` --semantically_similar_to--> `Simple Room Graph - Arkham City`  [INFERRED] [semantically similar]
  data/local/arkham_city_graph.png → data/local/simple_room_visualization.html
- `correct_async_logging()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/correct_patterns.py → server/structured_logging/logging_context.py
- `correct_async_logging()` --calls--> `clear_request_context()`  [INFERRED]
  docs/examples/logging/correct_patterns.py → server/structured_logging/logging_context.py
- `add_request_context()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py

## Import Cycles
- 2-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 2-file cycle: `client/src/components/map/useAsciiMap.ts -> client/src/components/map/useAsciiMapState.ts -> client/src/components/map/useAsciiMap.ts`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/connection_manager_health_cleanup.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `server/realtime/connection_initialization.py -> server/realtime/monitoring/health_monitor.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 3-file cycle: `client/src/components/panels/chatPanelChannelFilter.ts -> client/src/components/panels/chatPanelChannelVisibility.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelChannelFilter.ts`
- 3-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelUnreadBump.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `server/realtime/connection_establishment.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_establishment.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`

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
- **Migration 019 documentation set** — docs_migration_019_complete_summary_doc, docs_migration_019_ready_for_deployment_doc, docs_migration_019_testing_guide_doc, docs_migration_019_verification_doc [EXTRACTED 1.00]
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
- **Linting and complexity tooling docs** — docs_linting_complexity_alignment_doc, docs_linting_pylint_unique_findings_doc, docs_linting_ruff_pylint_mapping_doc, docs_lizard_complexity_findings_doc [INFERRED 0.85]
- **NATS operational guides** — docs_nats_error_handling_strategy_doc, docs_nats_manual_acknowledgment_guide_doc, docs_nats_subject_patterns_doc, docs_nats_remediation_summary_2026_01_13_doc, docs_nats_medium_priority_remediation_2026_01_13_doc [INFERRED 0.85]
- **Persistence migration and architecture docs** — docs_persistence_async_migration_guide_doc, docs_persistence_async_migration_plan_doc, docs_persistence_extraction_complete_doc, docs_persistence_refactoring_complete_doc, docs_persistence_refactoring_summary_doc, docs_persistence_repository_architecture_doc, docs_phase2_migration_complete_doc, docs_phase2_migration_status_doc [INFERRED 0.85]
- **PostgreSQL guidance and audit docs** — docs_postgresql_anti_patterns_review_doc, docs_postgresql_audit_report_2026_doc, docs_postgresql_contributor_guide_doc [INFERRED 0.85]
- **Contribution and triage templates** — github_issue_template_bug_report_bug_report_template, github_issue_template_documentation_documentation_template, github_issue_template_feature_request_feature_request_template, github_pull_request_template_pr_template [INFERRED 0.85]
- **Combat feature plans cluster** — plans_combat_round_system_refactor, plans_combat_bugs_investigation_and_fixes, plans_flee_command_and_effect, plans_first_weapon_switchblade [INFERRED 0.85]
- **MythosMUD operational skills cluster** — skills_mythosmud_server_runbook, skills_mythosmud_pre_commit_checklist, skills_mythosmud_test_writing, skills_mythosmud_worktree_workflow, skills_one_server_only_rule, skills_definition_of_done [INFERRED 0.85]
- **WebSocket migration and client message pipeline** — plans_websocket_only_migration, plans_websocket_best_practices_remediation, plans_unify_client_message_handling, plans_websocket_only_architecture [INFERRED 0.85]
- **Quality and security tooling cluster** — codacy_yml_codacy_configuration, pre_commit_config_yaml_pre_commit_hooks, semgrep_yml_no_select_star, bandit_yml_bandit_config, grype_yaml_sca_excludes [INFERRED 0.85]
- **Dual connection documentation set** — docs_archive_dual_connection_api_reference_dual_connection_api, docs_archive_dual_connection_client_guide_dual_connection_client, docs_archive_dual_connection_deployment_guide_dual_connection_deploy, docs_archive_dual_connection_api_reference_websocket_sse_dual [INFERRED 0.95]
- **Enhanced logging documentation cluster** — docs_archive_implementation_complete_enhanced_logging_complete, docs_archive_logging_implementation_summary_enhanced_logging, docs_archive_logging_migration_complete_logging_migration [INFERRED 0.95]
- **Spell command and casting failure cluster** — investigations_sessions_2025_12_14_session_001_spell_commands_failure_spell_commands_missing, investigations_sessions_2025_12_14_session_002_spell_cast_failure_multiword_spell, investigations_sessions_2025_12_14_session_003_minor_heal_casting_delay_missing_async_heal, investigations_sessions_2025_12_14_session_004_heal_spell_casting_failure_session_boundary [INFERRED 0.95]
- **Logging and error handling guides** — docs_enhanced_logging_guide_doc, docs_error_handling_guide_doc, docs_error_logging_implementation_guide_doc [INFERRED 0.95]
- **NATS review and remediation docs** — docs_nats_anti_patterns_review_2026_01_13_doc, docs_nats_code_review_doc, docs_nats_complete_remediation_summary_2026_01_13_doc [INFERRED 0.95]
- **Realtime architecture and ConnectionManager refactor** — docs_real_time_architecture_doc, docs_refactoring_summary_doc [INFERRED 0.95]
- **Test quality audit and optimization docs** — docs_test_audit_executive_summary_doc, docs_test_quality_audit_report_doc, docs_test_value_distribution_doc, docs_test_optimization_roadmap_doc, docs_test_pruning_candidates_doc, docs_test_timing_analysis_doc [INFERRED 0.95]

## Communities (1975 total, 593 thin omitted)

### Community 0 - "CommandFactory"
Cohesion: 0.01
Nodes (72): CommandFactory, Create GroundCommand from arguments., Create FollowCommand from arguments., Create UnfollowCommand from arguments., Create FollowingCommand from arguments., Create PartyCommand from arguments., Create InventoryCommand from arguments., Create PickupCommand from arguments. (+64 more)

### Community 1 - "lifespan.py"
Cohesion: 0.03
Nodes (79): BaseUserManager, ID, get_system_metrics(), Get system metrics from monitoring dashboard., _calculate_metrics_delta(), _cleanup_container_on_error(), _initialize_enhanced_systems(), lifespan() (+71 more)

### Community 2 - "test_look_helpers.py"
Cohesion: 0.03
Nodes (87): _get_health_label(), _get_lucidity_label(), _get_wearable_container_service(), _parse_instance_number(), Any, Get descriptive lucidity label based on lucidity percentage. Args: stats:…, Get shared WearableContainerService instance, initializing it lazily if needed.…, Parse instance number from target string. Supports two formats: - "backpack-2"… (+79 more)

### Community 3 - "Alias"
Cohesion: 0.02
Nodes (84): Any, Path, Save alias data to JSON file., Get all aliases for a player., Save aliases for a player., Add or update an alias for a player., Remove an alias for a player., Get a specific alias for a player. (+76 more)

### Community 4 - "combat_flee.py"
Cohesion: 0.08
Nodes (29): _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _PlayerForFlee, _PlayerPositionServiceLike, AppWithState, Protocol, UUID (+21 more)

### Community 5 - "websocket_initial_state.py"
Cohesion: 0.03
Nodes (103): add_npc_occupants_to_list(), _AppStateForEventHandler, _AppStateWithNpcLifecycle, _AppWithState, check_and_send_death_notification(), _ContainerWithNpcLifecycle, _get_death_location_name(), get_event_handler_for_initial_state() (+95 more)

### Community 6 - "NATSService"
Cohesion: 0.02
Nodes (78): NATS, CombatEventPublisher, _CombatPublishJob, Any, Shared NATS publish path for combat events., Publish combat started event to NATS., Publish combat ended event to NATS., Publish player attacked event to NATS. (+70 more)

### Community 7 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (125): EquipCommand, PickupCommand, field_validator, model_validator, Strip and validate search term., Ensure either index or search_term is provided., Validate target slot value. Args: value: The target slot value to validate (can…, Command for unequipping an item back to inventory. (+117 more)

### Community 8 - "test_users.py"
Cohesion: 0.01
Nodes (272): AuthenticationBackend, IntegrityError, _check_shutdown_status(), Check if server is shutting down and raise exception if so., _authenticate_user_credentials(), _check_shutdown_status(), _check_username_exists(), create_invite() (+264 more)

### Community 9 - "is_player_in_login_grace_period"
Cohesion: 0.05
Nodes (84): Get login grace period status for player., cancel_login_grace_period(), get_login_grace_period_remaining(), _grace_period_expiration_handler(), _grace_period_task(), is_player_in_login_grace_period(), Any, UUID (+76 more)

### Community 10 - "MythosMUDError"
Cohesion: 0.03
Nodes (114): ErrorSeverity, Error severity levels for logging and handling., AuthenticationError, ConfigurationError, GameLogicError, handle_exception(), MythosMUDError, NetworkError (+106 more)

### Community 11 - "Communities (355 total, 223 thin omitted)"
Cohesion: 0.02
Nodes (133): Communities (355 total, 223 thin omitted), Community 0 - "Nyarlathotep Avatars", Community 100 - "Call Daoloth / Daoloth", Community 101 - "Call Nyogtha / Clutch of Nyogtha", Community 102 - "Call Saaitii / Saaitii", Community 103 - "Call Zu-Che-Quon / Enchant Bells of Horror", Community 104 - "Cast Out Shan / Shaggai", Community 105 - "Casting the Runes / Elder Sign" (+125 more)

### Community 12 - "ErrorType"
Cohesion: 0.03
Nodes (91): JSONResponse, Error handlers package for MythosMUD. This package provides specialized error…, Pydantic error handler for consistent error processing. This module provides a…, _contains_file_path_in_exception(), _contains_sensitive_exception_pattern(), create_standardized_error_response(), handle_api_error(), Any (+83 more)

### Community 13 - "test_command_parser.py"
Cohesion: 0.02
Nodes (118): Smoke test for command parser., Test basic command parsing., Test command parsing with arguments., Test command parsing with pipes., test_parse_command_basic(), test_parse_command_with_args(), test_parse_command_with_pipes(), command_parser() (+110 more)

### Community 14 - "LoggedHTTPException"
Cohesion: 0.01
Nodes (423): _build_container_data_from_dict(), close_container(), _convert_container_dict_to_container_data(), _convert_datetime_to_iso(), _convert_inventory_list_to_inventory_stacks(), _convert_uuid_to_string(), open_container(), Any (+415 more)

### Community 15 - "players/__init__.py"
Cohesion: 0.04
Nodes (90): apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest, post (+82 more)

### Community 16 - "NPCCombatIntegrationService"
Cohesion: 0.01
Nodes (439): get_app_instance(), Return the runtime app instance attached during lifespan startup. This provides…, NPCCombatDataProvider, Any, UUID, Get player name for messaging. Args: player_id: ID of the player Returns:…, Get the current room ID for a player. Args: player_id: ID of the player (must…, Get player combat participant data from persistence. Args: player_id: ID of the… (+431 more)

### Community 17 - "server/exceptions.py"
Cohesion: 0.00
Nodes (721): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Any, post, Request, ValidationError, Player respawn API endpoints. This module handles endpoints for respawning…, Respawn a delirious player at the Sanitarium with restored lucidity. This… (+713 more)

### Community 18 - "test_security_validator.py"
Cohesion: 0.01
Nodes (225): field_validator, Validate alias name format using centralized validation., Validate command content for security using centralized validation., Validate alias name format using centralized validation., field_validator, Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation. (+217 more)

### Community 19 - "test_admin_auth_service.py"
Cohesion: 0.02
Nodes (112): AdminAuthService, AdminRole, AdminSession, Any, Request, Determine the admin role for a user. Args: current_user: The current user…, Safely get username from current user object., Safely get user ID from current user object. (+104 more)

### Community 20 - "RateLimiter"
Cohesion: 0.03
Nodes (73): Any, RateLimiter, Clean up old rate limit attempts to prevent memory bloat. Args:…, Clean up large data structures to prevent memory bloat. Args: max_entries:…, Remove all rate limit data for a specific player. Args: player_id: The player's…, Rate limiter for connection attempts and other operations. This class provides…, Get rate limiter statistics. Returns: dict: Statistics about current rate…, Check if a connection has exceeded message rate limits. Args: connection_id:… (+65 more)

### Community 21 - "test_command_factories_communication.py"
Cohesion: 0.04
Nodes (49): Unit tests for communication command factories. Tests the…, Test create_me_command() creates MeCommand., Test create_me_command() raises error with no args., Test create_pose_command() creates PoseCommand., Test create_pose_command() allows no args (sets pose to None)., Test create_channel_command() creates ChannelCommand., Test create_channel_command() handles 'default' action., Test create_channel_command() raises error with no args. (+41 more)

### Community 22 - "test_connection_delegates.py"
Cohesion: 0.03
Nodes (134): cleanup_dead_websocket_impl(), delegate_connection_cleaner(), delegate_connection_cleaner_sync(), delegate_error_handler(), delegate_game_state_provider_sync(), delegate_health_monitor(), delegate_health_monitor_sync(), delegate_message_broadcaster() (+126 more)

### Community 23 - "test_look_container.py"
Cohesion: 0.02
Nodes (184): _extract_container_metadata(), _find_container_in_room(), _find_container_in_room_or_equipped(), _find_container_via_inner_container(), _find_container_via_wearable_service(), _find_container_wearable(), _format_container_contents(), _format_container_display() (+176 more)

### Community 24 - "test_wearable_container_service.py"
Cohesion: 0.02
Nodes (140): _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Wearable container service for unified container system. As documented in the…, Return existing equipment container ID for item instance if present., Create wearable container in persistence and return container_id payload. (+132 more)

### Community 25 - "test_player_disconnect_handlers.py"
Cohesion: 0.04
Nodes (72): age_off_disconnected_sessions(), _cleanup_player_references(), _get_session_maps_for_age_off(), handle_player_disconnect_broadcast(), _purge_expired_sessions_from_maps(), UUID, Player disconnect handling functions. This module handles broadcasting…, Remove player from online tracking and room presence. Args: keys_to_remove: Set… (+64 more)

### Community 26 - "_def_row"
Cohesion: 0.11
Nodes (18): _def_row(), Test get_npc_definition_by_name() matches case-insensitively., Test get_npc_definition_by_name() returns None when not found., Test create_npc_definition() successfully creates definition., Test create_npc_definition() handles base_stats., Test delete_npc_definition() successfully deletes definition., Test create_spawn_rule() raises ValueError when max < min., Test get_npc_definitions_by_type() filters by type. (+10 more)

### Community 27 - "api/monitoring.py"
Cohesion: 0.04
Nodes (110): _assemble_health_response(), force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_health_status(), get_memory_alerts() (+102 more)

### Community 28 - "test_look_npc.py"
Cohesion: 0.05
Nodes (72): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result(), _get_lifecycle_manager() (+64 more)

### Community 29 - "test_admin_commands.py"
Cohesion: 0.05
Nodes (62): asyncio, Unit tests for admin command handlers. Tests the admin command handler…, Test handle_mute_command() with no target player., Test handle_mute_command() successful execution., Test handle_unmute_command() when user manager is not available., Test handle_unmute_command() with no target player., Test handle_unmute_command() successful execution., Test handle_unmute_command() succeeds when target was not muted (E2E cleanup… (+54 more)

### Community 30 - "container_persistence_async.py"
Cohesion: 0.04
Nodes (95): ContainerData, ContainerDataCore, ContainerDataExtras, Container data class for persistence operations., Identity and placement fields for a container row., Optional payload and timestamps for a container row., Data class for container information., Convert container data to dictionary. Returns dictionary with model field names… (+87 more)

### Community 31 - "test_websocket_handler_coverage_gaps.py"
Cohesion: 0.07
Nodes (44): handle_chat_message(), Handle a chat message from a player. Args: websocket: The WebSocket connection…, asyncio, Unit tests to fill coverage gaps in websocket_handler.py. These tests target…, Test handle_game_command exception handling path (lines 472-480)., Test handle_game_command RuntimeError handling path (lines 472-480)., Test process_websocket_command resolves connection_manager from app when None…, Test handle_chat_message resolves connection_manager from app when None (lines… (+36 more)

### Community 32 - "test_websocket_handler_core.py"
Cohesion: 0.04
Nodes (67): handle_websocket_message(), WebSocket, Handle a WebSocket message from a player. Args: websocket: The WebSocket…, asyncio, Unit tests for core websocket handler functions. Tests core WebSocket handler…, Test _process_message processes message., Test _process_message returns True when rate limit exceeded., Test _validate_player_and_persistence validates successfully. (+59 more)

### Community 33 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (133): CircuitBreakerOpen, Exception, Exception raised when circuit breaker is open. Indicates the protected service…, Test CircuitBreakerOpen exception., test_circuit_breaker_open_exception(), asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not… (+125 more)

### Community 34 - "test_inventory_commands.py"
Cohesion: 0.06
Nodes (57): handle_pickup_command(), Move an item stack from room drops into the player's inventory., command_result_text(), inventory_has_named_item(), PickupTestWiring, Shared helpers for inventory command unit tests., Normalize handler result message for assertions., True if inv is a sequence of dict rows containing item_name == name. (+49 more)

### Community 35 - "inventory_command_helpers.py"
Cohesion: 0.04
Nodes (95): add_pickup_to_inventory(), broadcast_room_event(), clone_inventory(), _collect_progress_sync(), ensure_item_instance_for_pickup(), persist_player(), _player_uuid_for_quest_sync(), Player (+87 more)

### Community 36 - "test_room_class.py"
Cohesion: 0.05
Nodes (37): Unit tests for Room class. Tests the Room class methods for managing room…, Test Room.remove_player_silently() removes player without event., Test Room.player_left() removes player and triggers event., Test Room.object_removed() removes object from room., Test Room.npc_entered() adds NPC to room., Test Room.npc_left() removes NPC from room., Test Room.get_objects() returns list of object IDs., Test Room.get_npcs() returns list of NPC IDs. (+29 more)

### Community 37 - "lifecycle_periodic.py"
Cohesion: 0.09
Nodes (27): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD. This module defines configuration settings for…, Configuration for NPC lifecycle maintenance. This class centralizes all timing…, Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…, Check if NPC maintenance should run on this tick. Args: tick_count: Current…, Get a summary of all NPC configuration values. Returns: Dictionary containing…, Clean up old lifecycle records (delegates to lifecycle_periodic). (+19 more)

### Community 38 - "server/dependencies.py"
Cohesion: 0.01
Nodes (201): get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service(), get_level_service() (+193 more)

### Community 39 - "test_container.py"
Cohesion: 0.03
Nodes (63): Unit tests for container models. Tests the ContainerComponent model including…, Test is_unlocked returns False when lock_state is LOCKED., Test is_unlocked returns False when lock_state is SEALED., Test has_capacity returns True when slots are available., Test has_capacity returns False when at capacity., Test has_room_for returns True when container has space for additional items., Test has_room_for returns False when adding items would exceed capacity., Test can_hold returns True when item_count fits capacity (replacement scenario). (+55 more)

### Community 40 - "TargetResolutionService"
Cohesion: 0.03
Nodes (79): PersistenceProtocol, PlayerServiceProtocol, Player, Protocol, Room, UUID, Validate player exists and is in a room. Returns (room_id, error_result)., Clean target name and extract disambiguation suffix. Returns (clean_target,… (+71 more)

### Community 41 - "MessageQueue"
Cohesion: 0.03
Nodes (70): MessageQueue, Any, Check if a player has pending messages. Args: player_id: The player's ID…, Get the number of pending messages for a player. Args: player_id: The player's…, Remove all pending messages for a specific player. Args: player_id: The…, Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…, Message queue for guaranteed delivery of messages to players. This class…, Clean up large data structures to prevent memory bloat. Args: max_entries:… (+62 more)

### Community 42 - "server/schemas/__init__.py"
Cohesion: 0.03
Nodes (147): cleanup_admin_sessions(), get_admin_audit_log(), get_admin_sessions(), get, post, Request, Admin session and audit log endpoints under /admin/npc. Split out from…, Get active admin sessions. (+139 more)

### Community 43 - "test_player_model.py"
Cohesion: 0.02
Nodes (87): Unit tests for Player SQLAlchemy model. Tests the Player model methods…, Test Player.get_inventory() handles empty inventory., Test Player.set_inventory() serializes to JSON., UUID fields in inventory entries should serialize to strings., Test Player can be instantiated with required fields., Test Player.get_status_effects() parses JSON status effects., Test Player.set_status_effects() serializes to JSON., Test Player.get_equipped_items() returns equipped items from _equipped_items… (+79 more)

### Community 44 - "NATSMessageHandler"
Cohesion: 0.02
Nodes (65): NATSMessageHandler, _not_configured_async(), Any, UUID, Compare two room IDs using canonical room ID resolution., Get player's current room ID from online players cache., Get player's current room ID from async persistence layer., Check if a player is currently in the specified room. (+57 more)

### Community 45 - "test_npc_startup_service.py"
Cohesion: 0.10
Nodes (19): Unit tests for NPC startup service. Tests the NPCStartupService class., Test _get_default_room_for_sub_zone() returns correct room for known sub-zone., Test _get_default_room_for_sub_zone() returns None for unknown sub-zone., Test _get_default_room_for_sub_zone() is case insensitive., Test get_npc_startup_service() returns service instance., Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute., Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center., Test spawn_npcs_on_startup() spawns optional NPCs. (+11 more)

### Community 46 - "test_command_admin.py"
Cohesion: 0.03
Nodes (76): field_validator, Administrative command for summoning prototypes into the current room., Validate prototype ID format. Args: value: The prototype ID to validate…, Command for teleporting a player to the admin's location., Validate player name format using centralized validation., Ensure provided direction is part of the allowed set., Validate player name format using centralized validation., SummonCommand (+68 more)

### Community 47 - "test_behavior_engine.py"
Cohesion: 0.07
Nodes (27): Unit tests for behavior engine. Tests the BehaviorEngine class., Test _evaluate_equality() handles boolean true., Test _evaluate_equality() handles boolean false., Test _evaluate_numeric_comparison() handles > operator., Test _evaluate_numeric_comparison() handles < operator., Test _evaluate_numeric_comparison() returns None for invalid format., Test evaluate_condition() handles >= operator., Test execute_applicable_rules() handles exceptions. (+19 more)

### Community 48 - "test_follow_commands.py"
Cohesion: 0.10
Nodes (44): _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), _load_follow_context(), Any, Follow commands for MythosMUD. Handlers for /follow, /unfollow, and /following.…, Handle /following - show who you follow and who follows you. (+36 more)

### Community 49 - "get_logger"
Cohesion: 0.00
Nodes (803): Base API router and common dependencies for MythosMUD server. This module…, Container API endpoints for unified container system. As documented in the…, initialize_nats_and_combat_services(), Initialize NATS-dependent services including combat service. DEPRECATED: This…, Centralized TaskRegistry for MythosMUD server task lifecycle management. This…, AsyncPersistenceLayer, Async persistence layer for MythosMUD. This module provides an async version of…, Delegate to room loader; exposed for unit tests. (+795 more)

### Community 50 - "test_container_websocket_events.py"
Cohesion: 0.09
Nodes (41): emit_container_closed(), emit_container_decayed(), emit_container_opened(), emit_container_opened_to_room(), emit_container_updated(), Any, ContainerComponent, datetime (+33 more)

### Community 51 - "test_database_helpers.py"
Cohesion: 0.04
Nodes (84): _get_database_url_state(), close_db(), ensure_database_directory(), get_async_session(), get_database_path(), get_database_url(), get_engine(), get_session_maker() (+76 more)

### Community 52 - "TestCombatInitializer"
Cohesion: 0.08
Nodes (14): fixture, Test create_combat_instance orders turns when target has higher dexterity., Test create_combat_instance handles equal dexterity., Test create_combat_instance with auto-progression disabled., Test create_combat_instance with different turn interval., Test suite for CombatInitializer class., Test create_combat_instance with damaged participants., Test create_combat_instance with zero tick. (+6 more)

### Community 53 - "test_command_factories.py"
Cohesion: 0.03
Nodes (69): Unit tests for command factories. Tests the CommandFactory class., Test create_go_command delegates to exploration factory., Test create_sit_command delegates to exploration factory., Test create_stand_command delegates to exploration factory., Test create_lie_command delegates to exploration factory., Test create_ground_command delegates to exploration factory., Test create_pickup_command delegates to inventory factory., Test create_drop_command delegates to inventory factory. (+61 more)

### Community 54 - "Any"
Cohesion: 0.06
Nodes (20): Any, T, Task, Legacy wrapper for API compatibility during transition., Pure async event processing loop replacing the dangerous threading pattern., Separate async and sync subscribers for appropriate execution. Uses…, Execute sync subscribers sequentially with error isolation. Sync subscribers…, Create asyncio tasks for async event subscribers and track their lifecycle.… (+12 more)

### Community 55 - "ExplorationService"
Cohesion: 0.04
Nodes (90): ExplorationService, Any, AsyncSession, UUID, Get room UUID by stable_id (hierarchical room ID). Args: stable_id:…, Mark room as explored using the provided session. Args: session: Database…, Get list of room IDs that a player has explored. Args: player_id: UUID of the…, Check if a player has explored a specific room. Args: player_id: UUID of the… (+82 more)

### Community 56 - "test_combat_schema.py"
Cohesion: 0.08
Nodes (42): Draft7Validator, add_default_combat_data_to_config(), add_default_combat_data_to_stats(), CombatSchemaValidationError, get_combat_stats_summary(), Any, Exception, Combat system JSON schema validation. This module provides JSON schema… (+34 more)

### Community 57 - "Stats"
Cohesion: 0.03
Nodes (71): computed_field, Any, model_validator, Core character statistics with Lovecraftian horror elements., Initialize Stats with provided data. For random stat generation, use…, Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes…, Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).…, Calculate max lucidity based on education. AI: This computed field uses the… (+63 more)

### Community 58 - "test_player_respawn_service.py"
Cohesion: 0.04
Nodes (72): datetime, Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE., _utc_now(), mock_event_bus(), mock_player_combat_service(), mock_session(), asyncio, fixture (+64 more)

### Community 59 - "api/conftest.py"
Cohesion: 0.17
Nodes (15): mock_connection_manager(), mock_container(), mock_container_service(), mock_persistence(), mock_player(), mock_request(), mock_user(), fixture (+7 more)

### Community 60 - "rooms.py"
Cohesion: 0.05
Nodes (54): RoomDictList, _apply_exploration_filter_if_needed(), get_room(), _invalidate_room_cache(), list_rooms(), Any, AsyncSession, BaseModel (+46 more)

### Community 61 - ".reset_instance"
Cohesion: 0.04
Nodes (73): Reset singleton for testing., asyncio, Unit tests for database error handling and edge cases. Tests error paths,…, Test _initialize_database converts postgresql:// to postgresql+asyncpg://., Test _initialize_database keeps postgresql+asyncpg:// URL as-is., Test _initialize_database uses NullPool for test URLs., Test _initialize_database uses pool config for production URLs., Test _initialize_database handles ValueError from create_async_engine. (+65 more)

### Community 62 - "test_command_factories_utility.py"
Cohesion: 0.02
Nodes (117): log_exception_once(), Exception, Log an exception once, respecting exceptions that have already been logged.…, _as_bound_logger(), BoundLogger, Minimal stand-in for BoundLogger: only what log_exception_once touches for…, Adapt test double to the function param type (structural use only)., Plain exceptions get _already_logged via __setattr__ fallback; second log is… (+109 more)

### Community 63 - "test_health_service.py"
Cohesion: 0.04
Nodes (59): get_health_service(), Get the global health service instance. Args: connection_manager: Optional…, health_service(), mock_connection_manager(), fixture, patch, Unit tests for health service. Tests the health monitoring service for system…, Test check_database_health returns degraded status. (+51 more)

### Community 64 - "LucidityFluxService"
Cohesion: 0.06
Nodes (46): LucidityUpdateResult, Normalized response describing the outcome of a lucidity adjustment., FluxServiceConfig, lookup_profile(), normalize_environment_config(), period_label(), Any, datetime (+38 more)

### Community 65 - "test_command_factories_exploration.py"
Cohesion: 0.03
Nodes (88): Unit tests for exploration command factories. Tests the…, Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_sit_command() creates SitCommand., Test create_sit_command() raises error with args., Test create_stand_command() creates StandCommand., Test create_stand_command() raises error with args. (+80 more)

### Community 66 - "ui-v2/types.ts"
Cohesion: 0.05
Nodes (75): PanelManager(), PanelManagerProps, minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapPanelSectionProps, PanelContainer, PanelContainerBody(), PanelContainerProps (+67 more)

### Community 67 - "test_user_manager.py"
Cohesion: 0.02
Nodes (97): Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() successfully globally mutes a player., Test mute_global() fails when trying to mute admin. (+89 more)

### Community 68 - "test_quest_instance_repository.py"
Cohesion: 0.03
Nodes (99): Base, QuestDefinition, QuestInstance, QuestOffer, Quest subsystem models: quest_definitions, quest_instances, quest_offers. Maps…, Quest template: id (PK), definition JSONB, timestamps., Per-character quest state: one row per player per quest., Junction: links a quest to an NPC or room that offers it. (+91 more)

### Community 69 - "PayloadOptimizer"
Cohesion: 0.22
Nodes (8): PayloadOptimizer, Any, Create an incremental update payload containing only changed fields. Args:…, Optimizes payloads for WebSocket transmission. Features: - Size limit…, Initialize the payload optimizer. Args: max_payload_size: Maximum payload size…, Calculate the size of a payload in bytes. Args: payload: The payload dictionary…, Compress a large payload using gzip compression. Args: payload: The payload…, Optimize a payload by applying size limits and compression if needed. Args:…

### Community 70 - "test_command_service.py"
Cohesion: 0.03
Nodes (67): MythosValidationError, Test handle_transfer_items_exceptions returns 400 for ValidationError., command_service(), mock_request(), mock_user(), asyncio, fixture, Unit tests for command service. Tests the CommandService class which handles… (+59 more)

### Community 71 - "test_connection_establishment.py"
Cohesion: 0.04
Nodes (96): _cleanup_dead_connections(), _cleanup_failed_connection(), establish_websocket_connection(), _find_dead_connections(), Any, UUID, WebSocket, Connection establishment management for connection manager. This module handles… (+88 more)

### Community 72 - "DatabaseError"
Cohesion: 0.01
Nodes (255): LevelUpHook, main(), Load seed data and verify., Core bundle: config, database, tasks, event bus, persistence. First bundle in…, Initialize core services. No dependencies., GameBundle, Any, datetime (+247 more)

### Community 73 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test create_player_with_stats() successful creation., Test search_players_by_name() returns matching players., Test update_player_location() when player not found., Test apply_corruption() applies corruption., Test gain_occult_knowledge() increases occult knowledge., Test get_user_characters() returns user's characters., Test soft_delete_character() when character already deleted. (+7 more)

### Community 74 - "TauntCommandHandler"
Cohesion: 0.05
Nodes (45): Handle taunt command: draw NPC aggro (ADR-016). Room-local only., AppWithState, Protocol, UUID, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Handle taunt command: draw NPC aggro (ADR-016). Room-local only., Minimal handler surface for taunt (avoids importing CombatCommandHandler:… (+37 more)

### Community 75 - "test_combat_validator.py"
Cohesion: 0.17
Nodes (11): Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_attack_strength when target is significantly stronger., Test _contains_suspicious_patterns with clean target name., Test _get_random_error_message with unknown error type., Test get_combat_help_message returns help message., Test validate_combat_command with invalid command type., test_contains_suspicious_patterns_clean(), test_get_combat_help_message() (+3 more)

### Community 76 - "EldritchIcon.tsx"
Cohesion: 0.04
Nodes (51): ChatMessage, ChatMessageType, ChatPanelTest(), mockClick, mockCreateObjectURL, mockRevokeObjectURL, DraggablePanelResizeHandles(), DraggablePanelResizeHandlesProps (+43 more)

### Community 77 - "communication_commands.py"
Cohesion: 0.03
Nodes (124): handle_global_command(), handle_local_command(), handle_pose_command(), handle_reply_command(), handle_say_command(), handle_system_command(), handle_whisper_command(), Communication commands for MythosMUD. Handlers delegate heavy logic to… (+116 more)

### Community 78 - "test_connection_helpers_impl.py"
Cohesion: 0.04
Nodes (86): broadcast_global_event_impl(), broadcast_room_event_impl(), convert_uuids_to_strings(), mark_player_seen_impl(), _optimize_payload(), Any, _queue_message_if_needed(), Queue message for later delivery if no active connections. Args: player_id: The… (+78 more)

### Community 79 - "CombatTurnProcessor"
Cohesion: 0.05
Nodes (67): CombatTurnProcessor, UUID, Resolve NPC participant UUID to string npc_id via combat integration service., Return True if npc_id_str is in the lifecycle manager's active_npcs., Load queued actions for the next round into combat.round_actions. Actions are…, Execute all actions for a round - all participants act sequentially in…, Handles combat turn processing and auto-progression., Initialize the turn processor. Args: combat_service: Reference to the parent… (+59 more)

### Community 80 - "test_connection_disconnection.py"
Cohesion: 0.04
Nodes (95): _cleanup_connection_tracking(), _cleanup_fully_disconnected_player(), _cleanup_player_data(), _cleanup_room_subscriptions(), cleanup_websocket_disconnect(), disconnect_all_websockets_impl(), disconnect_connection_by_id_impl(), _disconnect_single_websocket() (+87 more)

### Community 81 - "test_argon2_utils.py"
Cohesion: 0.03
Nodes (91): PasswordHasher, E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio. (+83 more)

### Community 82 - "Reporter"
Cohesion: 0.03
Nodes (46): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+38 more)

### Community 83 - "test_room_renderer.py"
Cohesion: 0.04
Nodes (70): Unit tests for room_renderer utility functions. Tests the utility functions in…, Test clone_room_drops() returns empty list for None., Test format_room_drop_lines() formats room drops., Test format_room_drop_lines() returns empty message for empty drops., Test format_room_drop_lines() handles None., Test format_room_drop_lines() uses fallback for missing item_name., Test build_room_drop_summary() returns newline-separated summary., Test build_room_drop_summary() handles empty drops. (+62 more)

### Community 84 - "test_websocket_handler_helpers_extended.py"
Cohesion: 0.05
Nodes (57): mock_connection_manager(), mock_validator(), mock_websocket(), asyncio, fixture, Extended unit tests for websocket handler helper functions. Tests additional…, Test _send_error_response() handles WebSocketDisconnect., Test _send_error_response() returns False for RuntimeError indicating… (+49 more)

### Community 85 - "test_status_commands.py"
Cohesion: 0.04
Nodes (81): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_profession_info(), _get_status_persistence(), handle_status_command() (+73 more)

### Community 86 - "websocket_integration.py"
Cohesion: 0.06
Nodes (28): auth_service, authenticate_websocket_connection(), chat_service, game_service, handle_chat_message(), handle_game_action(), handle_websocket_error(), handle_websocket_message() (+20 more)

### Community 87 - "test_auth_utils.py"
Cohesion: 0.05
Nodes (66): create_access_token(), decode_access_token(), timedelta, Decode and validate a JWT access token., Create a JWT access token., fixture, MonkeyPatch, Unit tests for authentication utilities. (+58 more)

### Community 88 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (88): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+80 more)

### Community 89 - "map/types.ts"
Cohesion: 0.08
Nodes (38): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeBody(), ExitEdgeLabels() (+30 more)

### Community 90 - "event_types.py"
Cohesion: 0.01
Nodes (231): CombatEndedEvent, CombatStartedEvent, CombatTimeoutEvent, CombatTurnAdvancedEvent, NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent (+223 more)

### Community 91 - "test_look_room.py"
Cohesion: 0.04
Nodes (95): _filter_other_players(), _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id() (+87 more)

### Community 92 - "test_rescue_service.py"
Cohesion: 0.08
Nodes (36): asyncio, Unit tests for rescue service. Tests the RescueService class for performing…, Test rescue() returns error when persistence is not available., Test rescue() returns error when rescuer is not found., Test rescue() returns error when target is not found., Test rescue() returns error when rescuer and target are in different rooms., Test rescue() returns error when lucidity record is not found., Test rescue() returns error when target is not catatonic. (+28 more)

### Community 93 - "NATSMessageBroker"
Cohesion: 0.07
Nodes (34): MessageBrokerConnectionError, MessageBrokerError, PublishError, Exception, Message Broker abstraction for MythosMUD. This module defines the MessageBroker…, Base exception for message broker errors., Exception raised when connection to message broker fails., Exception raised when publishing message fails. (+26 more)

### Community 94 - "test_go_command.py"
Cohesion: 0.05
Nodes (65): _canonical_room_id_for_go(), _execute_movement(), _movement_service_for_go_command(), Any, Validate that exit exists and target room is valid., Use container.movement_service when wired; else build MovementService (tests /…, Execute player movement using movement service., Return normalized direction string, or None if missing (after logging). (+57 more)

### Community 95 - "test_lucidity_recovery_commands.py"
Cohesion: 0.05
Nodes (72): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+64 more)

### Community 96 - "multiplayer.ts"
Cohesion: 0.09
Nodes (60): expectWhoListingOnPage(), nudgeStandBothPlayers(), primeBothForCoLocate(), waitForLookReflected(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), executeUnmuteAndWaitForAck() (+52 more)

### Community 97 - "test_nats_service.py"
Cohesion: 0.03
Nodes (86): asyncio, Unit tests for NATS service. Tests the NATSService class and NATSMetrics., Test NATSService initialization with NATSConfig., Test NATSService initialization with dict config., Test NATSService initializes connection pool structures., Test connect() successfully connects to NATS., Test connect() returns False when state machine blocks connection., Test connect() handles connection failure. (+78 more)

### Community 98 - "test_character_creation_service.py"
Cohesion: 0.03
Nodes (62): CharacterCreationService, Any, UUID, Validate character stats against class prerequisites. Args: stats: The stats…, Create a new character with specific stats. Args: name: The character's name…, Get information about all available character classes and their prerequisites.…, Service class for character creation and stats generation business operations., Get a description for a character class. (+54 more)

### Community 99 - "test_rate_limiter_utils.py"
Cohesion: 0.04
Nodes (45): fixture, rate_limiter(), Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…, Test get_rate_limit_info calculates reset time correctly., Test get_rate_limit_info calculates retry_after correctly., Test get_rate_limit_info filters out old requests., Test enforce_rate_limit allows request within limit., Test enforce_rate_limit raises RateLimitError when limit exceeded. (+37 more)

### Community 100 - "Dependency Risk Analyzer"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 101 - "server/persistence/__init__.py"
Cohesion: 0.09
Nodes (35): CreateItemInstanceInput, EnsureItemInstanceInput, TypedDict, Constants and shared types for async persistence layer. Extracted to keep…, Optional fields for create_item_instance. owner_type, owner_id, etc. with…, Optional fields for ensure_item_instance., Create a new item instance. Delegates to ItemRepository., Persistence package for MythosMUD. This package contains persistence utilities… (+27 more)

### Community 102 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.06
Nodes (81): _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch(), filter_valid_items() (+73 more)

### Community 103 - "test_player_presence_tracker.py"
Cohesion: 0.03
Nodes (106): _collect_disconnect_keys(), Player, Collect all keys (UUID and string) that need to be removed for player…, _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _disconnect_during_rest_is_intentional(), _get_instance_manager_from_manager() (+98 more)

### Community 104 - "test_player_death_service.py"
Cohesion: 0.03
Nodes (87): mock_event_bus(), mock_player(), mock_player_combat_service(), mock_session(), player_death_service(), player_death_service_no_dependencies(), asyncio, fixture (+79 more)

### Community 105 - "RoomService"
Cohesion: 0.07
Nodes (24): Any, AsyncSession, UUID, Get a list of rooms adjacent to the specified room. Args: room_id: The room's…, Get the scope of rooms for local chat (current room + adjacent rooms). Args:…, Validate that a room exists using cached data. Args: room_id: The room's ID…, Validate that there's a valid exit from one room to another. Args:…, Get all occupants (players and NPCs) currently in a room using cached data.… (+16 more)

### Community 106 - "test_metrics_endpoints.py"
Cohesion: 0.06
Nodes (79): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+71 more)

### Community 107 - "test_room_sync_service.py"
Cohesion: 0.03
Nodes (81): Any, T, Process room update with comprehensive validation. Args: room_data: Room data…, Invalidate stale room cache entry. Args: room_id: Room ID to invalidate…, Fetch fresh room data from room service. Args: room_id: Room ID to fetch…, Handle stale room data by requesting fresh data. Args: room_data: Stale room…, Process room transition with proper ordering and validation. Args:…, Get statistics about the room data cache. Returns: Dict[str, Any]: Cache… (+73 more)

### Community 108 - "RoomLoader"
Cohesion: 0.03
Nodes (54): fixture, Create a temporary directory for testing., temp_dir(), Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path. (+46 more)

### Community 109 - "asyncio"
Cohesion: 0.14
Nodes (17): PartyChannelStrategy, Strategy for party channel broadcasting. Delivers only to current party members., asyncio, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() handles missing target_player_id., Test SystemAdminChannelStrategy.broadcast() broadcasts globally. (+9 more)

### Community 110 - "CircuitBreaker"
Cohesion: 0.04
Nodes (69): CircuitBreaker, CircuitState, Any, Enum, timedelta, Handle successful function call. Updates state based on current circuit state:…, Handle failed function call. Updates state based on failure count: - Increments…, Check if enough time has passed to attempt circuit reset. Returns: True if… (+61 more)

### Community 111 - "CorpseOverlay.tsx"
Cohesion: 0.04
Nodes (69): BackpackTab(), BackpackTabProps, ContainerSplitPane(), ContainerSplitPaneProps, ContainerInventoryPaneProps, ContainerItemRow(), ContainerSplitPaneView(), ContainerSplitPaneViewModel (+61 more)

### Community 112 - "PlayerEnteredRoom"
Cohesion: 0.02
Nodes (126): _FollowTargetValue, NPCEnteredRoom, PlayerEnteredRoom, Event fired when an NPC enters a room. This event is triggered when an NPC…, Event fired when a player enters a room. This event is triggered when a player…, FollowService, _is_npc_follow_value(), Any (+118 more)

### Community 113 - "test_nats_broker.py"
Cohesion: 0.04
Nodes (74): asyncio, Unit tests for NATS message broker. Tests the NATSMessageBroker class., Test connect() passes TLS options to nats.connect when tls_enabled=True., Test disconnect() does nothing when no client., Test disconnect() successfully disconnects., Test disconnect() unsubscribes from all subscriptions., Test disconnect() handles unsubscribe errors gracefully., Test disconnect() raises MessageBrokerError on disconnect failure. (+66 more)

### Community 114 - "RoomSubscriptionManager"
Cohesion: 0.06
Nodes (27): SendPersonalMessage, Initialize the message broadcaster. Args: room_manager: RoomSubscriptionManager…, Any, Retrieve current room drops as a defensive copy for callers. Args: room_id: The…, Append an item stack to the room drop ledger. Args: room_id: The room receiving…, Remove quantity of a drop entry, returning the removed stack. Args: room_id:…, Adjust quantity for an existing drop entry; removing entry when zero. Args:…, Manages room subscriptions and occupant tracking. This class handles room… (+19 more)

### Community 115 - "UserManager"
Cohesion: 0.06
Nodes (39): UUID, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Clean up expired player mutes., Get the mute data file path for a specific player., Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory. (+31 more)

### Community 116 - "test_look_player.py"
Cohesion: 0.04
Nodes (91): _get_visible_equipment(), Get visible equipment from player, excluding internal/hidden slots. Visible…, _apply_grace_period_labels(), _find_matching_players(), _format_player_look_display(), _get_players_in_room(), _handle_player_look(), _player_id_uuid() (+83 more)

### Community 117 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (86): _collect_rotatable_logs(), detect_environment(), ensure_log_directory(), BoundLogger, Path, Logging utilities for directory management, path resolution, and environment…, Resolve log_base path to absolute path relative to project root. Args:…, Collect non-empty log files eligible for rotation. (+78 more)

### Community 118 - "User"
Cohesion: 0.01
Nodes (245): Admin API module for MythosMUD. This module provides administrative API…, get_patterns(), get_subject_statistics(), PatternsResponse, BaseModel, get, post, NATS Subject Management API Controller for MythosMUD. This module provides REST… (+237 more)

### Community 119 - "test_combat_monitoring_service.py"
Cohesion: 0.04
Nodes (47): Unit tests for combat monitoring service. Tests the CombatMonitoringService…, Test start_turn_monitoring tracks turn., Test end_turn_monitoring updates metrics., Test record_combat_error with timeout error., Test get_current_metrics returns metrics., Test get_metrics_history returns history., Test get_metrics_history with limit., Test add_alert_callback adds callback. (+39 more)

### Community 120 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.04
Nodes (89): _dispatch_player_event(), _format_liabilities(), LucidityChangeEventExtras, LiabilityStackEntry, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send rescue progress/status updates to either participant. (+81 more)

### Community 121 - "test_nats_message_handler_chat.py"
Cohesion: 0.12
Nodes (15): Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _convert_ids_to_uuids handles UUID objects., Test _should_echo_to_sender returns False for non-chat messages., Test _should_echo_to_sender returns False when message_id is None., Test _validate_chat_message_fields validates fields., Test _validate_chat_message_fields raises error when fields missing. (+7 more)

### Community 122 - "run_flee_effect"
Cohesion: 0.23
Nodes (16): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+8 more)

### Community 123 - "types/mythosTime.ts"
Cohesion: 0.07
Nodes (45): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, appendDaypartChange(), appendHourChime() (+37 more)

### Community 124 - "SchemaValidator"
Cohesion: 0.03
Nodes (44): Path, Convert legacy string format exits to new object format internally. This allows…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in… (+36 more)

### Community 125 - "DeadLetterQueue"
Cohesion: 0.04
Nodes (67): DeadLetterMessage, DeadLetterQueue, Any, Path, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve and remove oldest message from DLQ (async version). Returns: Message…, Retrieve and remove oldest message from DLQ (sync version). Returns: Message… (+59 more)

### Community 126 - ".get_instance"
Cohesion: 0.04
Nodes (62): Get the singleton instance., Test DatabaseManager.get_engine initializes if not initialized., Test DatabaseManager.get_engine reinitializes if engine is None., Test DatabaseManager.get_session_maker initializes if not initialized., Test DatabaseManager.get_database_url initializes if not initialized., Test DatabaseManager.get_database_path returns None for PostgreSQL., Test DatabaseManager.get_database_path raises for unsupported URL., test_database_manager_get_database_path_postgresql() (+54 more)

### Community 127 - "Player"
Cohesion: 0.01
Nodes (243): Player respawn wrapper service. This module provides wrapper methods for player…, Base, DeclarativeBase, Shared SQLAlchemy DeclarativeBase for all models. This module provides a single…, Shared declarative base for all MythosMUD models. All models (User, Player,…, SQLAlchemy models for emotes., AttributeType, PositionState (+235 more)

### Community 128 - "PathValidator"
Cohesion: 0.03
Nodes (68): option, Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer, Core validation components for the MythosMUD room validator. This module…, MinimapRenderer, Any (+60 more)

### Community 129 - "player_effect_repository.py"
Cohesion: 0.05
Nodes (53): _add_effect_params(), AddEffectInput, _int_opt(), _opt_str(), PlayerEffectRepository, Any, TypedDict, UUID (+45 more)

### Community 130 - ".__post_init__"
Cohesion: 0.05
Nodes (18): Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type. (+10 more)

### Community 131 - "chatPanelRuntimeUtils.ts"
Cohesion: 0.07
Nodes (56): filterMessagesForChannelView(), EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW, isGloballyExcludedFromChannelView(), isVisibleInChannelView(), matchesChannelSelection(), resolveMessageChannelForFilter(), buildChatExportCSV(), buildChatExportCsvRow() (+48 more)

### Community 132 - "test_room_utils.py"
Cohesion: 0.07
Nodes (37): Unit tests for room_utils. Tests utility functions for room operations., Test get_subzone_local_channel_subject() generates subject., Test get_subzone_local_channel_subject() returns None for invalid room ID., Test extract_subzone_from_room_id() extracts subzone., Test extract_subzone_from_room_id() extracts different subzone., Test extract_subzone_from_room_id() returns None for invalid format., Test get_zone_from_room_id() extracts zone., Test get_zone_from_room_id() extracts different zone. (+29 more)

### Community 133 - "test_movement_service.py"
Cohesion: 0.05
Nodes (45): mock_event_bus(), mock_persistence(), movement_service(), asyncio, fixture, Unit tests for movement service. Tests the MovementService class., Test add_player_to_room() when player is not found., Test remove_player_from_room() successfully removes player. (+37 more)

### Community 134 - "test_alias_commands.py"
Cohesion: 0.05
Nodes (53): mock_alias(), mock_alias_storage(), asyncio, fixture, Unit tests for alias command handlers. Tests the alias, aliases, and unalias…, Test handle_alias_command creating alias from structured data., Test handle_alias_command with alias name too long., Test handle_alias_command with command too long. (+45 more)

### Community 135 - "WebSocketMessageValidator"
Cohesion: 0.04
Nodes (67): MessageValidationError, BaseModel, Exception, WebSocket message validation for MythosMUD. This module provides comprehensive…, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Validate message against Pydantic schema. Args: message: Parsed JSON message…, Raised when message validation fails. (+59 more)

### Community 136 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, get_skills_catalog returns list of skill dicts., get_player_skills for owned player returns list of skill dicts., get_player_skills for another user's player returns None., record_successful_skill_use delegates to repo.record_use with correct args., get_skills_used_this_level returns distinct skill_ids from repo., When roll > current value, update_value called with new value (gain 1 or 1d10)., roll_skill_check when player has no value for skill_id returns False. (+9 more)

### Community 137 - "RoomDataCache"
Cohesion: 0.04
Nodes (39): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Manages room data caching and freshness validation., Check if new data is newer than old data for a specific key. Args: old_data:…, Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,… (+31 more)

### Community 138 - "test_player_event_handlers_respawn.py"
Cohesion: 0.04
Nodes (61): mock_connection_manager(), mock_logger(), mock_utils(), player_respawn_event_handler(), asyncio, fixture, Unit tests for player respawn event handlers. Tests the…, Test get_player_data_for_respawn() returns None when connection manager not… (+53 more)

### Community 139 - "api/character_creation.py"
Cohesion: 0.04
Nodes (80): _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _convert_stat_summary_to_stat_summary_model(), create_character_with_stats(), _dispatch_roll_stats(), _execute_create_character(), _prepare_create_character_request(), Any (+72 more)

### Community 140 - "HealthRepository"
Cohesion: 0.12
Nodes (16): HealthRepository, Exception, Player, UUID, Log critical damage persistence failure., Execute atomic health update via update_player_health procedure., Damage a player and persist health changes atomically. Args: player: Player to…, Heal a player and persist health changes atomically. (+8 more)

### Community 141 - "catatonia_check.py"
Cohesion: 0.04
Nodes (55): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+47 more)

### Community 142 - "test_nats_message_handler_subzone_events.py"
Cohesion: 0.10
Nodes (19): Unit tests for NATS message handler subzone and event handling. Tests subzone…, Test get_event_subscription_count returns count., Test is_event_subscription_active checks subscription., Test _get_user_manager returns injected manager., Test _get_user_manager falls back to global manager., Test _get_event_handler_map delegates to event handler., Test _validate_event_message delegates to event handler., Test track_player_subzone_subscription handles player moving to different… (+11 more)

### Community 143 - "TaskRegistry"
Cohesion: 0.02
Nodes (88): HolidayResolver, create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryThresholdMonitor, Any, Managed Task Cleanup Service - Runtime Detection for Memory Threshold…, Generate status report for diagnostic monitoring. Returns: Dictionary…, Runtime detection and cleanup of orphaned tasks based on memory thresholds.… (+80 more)

### Community 144 - "test_rest_command.py"
Cohesion: 0.04
Nodes (97): _connection_manager_from_go_app(), Go command for MythosMUD. This module handles the go command for player…, Resolve ConnectionManager from DI container or legacy app.state., If the player is resting, cancel rest and return an early client payload; else…, _rest_interrupt_payload_if_moving(), If player is resting, cancel rest countdown so they can cast. Swallows errors…, _begin_seated_rest_countdown(), cancel_rest_countdown() (+89 more)

### Community 145 - "test_user_schemas.py"
Cohesion: 0.13
Nodes (21): Base user schema with common fields., Schema for creating a new user., Schema for updating user data., UserBase, UserCreate, UserUpdate, Unit tests for user schemas. Tests the Pydantic models in user.py module., Test UserBase can be instantiated. (+13 more)

### Community 146 - ".transfer_from_container"
Cohesion: 0.07
Nodes (31): _filter_container_data(), _get_enum_value(), Any, ContainerComponent, ContainerLockState, InventoryStack, UUID, Validate corpse grace period access rules. (+23 more)

### Community 147 - "PlayerRespawnService"
Cohesion: 0.08
Nodes (29): _PlayerCombatClearing, PlayerRespawnService, AsyncSession, Player, Protocol, UUID, Return current_dp as an int, defaulting to 0 for non-numeric values., Return (allowed, current_dp_int) for limbo movement gate checks. (+21 more)

### Community 148 - "test_npc_combat_integration_class.py"
Cohesion: 0.06
Nodes (35): mock_persistence(), asyncio, fixture, Unit tests for server.npc.combat_integration.NPCCombatIntegration (helpers and…, Invalid UUID with npc_stats returns normalized NPC stats., Killer path loads player and calls game mechanics helpers., After damage, old_dp reflects pre-hit value., Display name resolves from lifecycle_manager.active_npcs when present. (+27 more)

### Community 149 - "test_look_npc_helpers.py"
Cohesion: 0.05
Nodes (43): _parse_stat_datetime(), Parse datetime value from various formats and return formatted string., Unit tests for look_npc helper functions. Tests the helper functions in…, Test _format_other_stats() returns empty list when no other stats., Test _parse_stat_datetime() handles datetime object., Test _parse_stat_datetime() handles timestamp., Test _parse_stat_datetime() handles ISO string., Test _parse_stat_datetime() returns 'Unknown' for None. (+35 more)

### Community 150 - "AliasStorage"
Cohesion: 0.02
Nodes (179): CommandHandler, AliasStorage, Alias storage utilities for MythosMUD. As noted in the restricted archives of…, List all alias files in the storage directory., Manages player alias storage in JSON files. Each player's aliases are stored in…, Alias Expansion Logic for MythosMUD. This module handles alias resolution,…, handle_admin_command(), _handle_admin_status_command() (+171 more)

### Community 151 - "TestHelperFunctions"
Cohesion: 0.03
Nodes (39): asyncio, Test _ensure_alias_storage returns None on error., Test _check_grace_period_block returns None when no connection manager., Test _check_grace_period_block returns None when not in grace period., Test _prepare_command_for_processing returns rate limit result., Test helper functions in command_handler_unified., Test _prepare_command_for_processing returns validation result., Test _prepare_command_for_processing returns empty result after cleaning. (+31 more)

### Community 152 - "Stats"
Cohesion: 0.10
Nodes (15): generate_random_stats(), Any, Stats, Roll Size using formula: (2D6+6)*5 (range 40-90)., Roll stats using 3d6 method (scaled to 15-90 range)., Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)., Generate stats using a point-buy system (balanced, scaled to 1-100 range)., Generate Stats with random attribute values. Factory function for creating… (+7 more)

### Community 153 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.09
Nodes (48): _build_python_call_usage_map(), _call_target_name(), check_ai_guardrails(), _check_exports_and_tiny_functions(), _check_single_use_file(), _collect_code_texts(), _collect_python_public_defs_and_tiny(), _guardrail_scan_inputs() (+40 more)

### Community 154 - "test_combat_attack_handler.py"
Cohesion: 0.04
Nodes (61): attack_handler(), mock_attacker(), mock_combat(), mock_combat_service(), mock_target_npc(), mock_target_player(), asyncio, fixture (+53 more)

### Community 155 - "test_connection_statistics.py"
Cohesion: 0.05
Nodes (52): Get session management statistics., Get detailed presence information for a player., Validate player presence and clean up any inconsistencies., Get presence tracking statistics., Get online player information by display name., get_online_player_by_display_name_impl(), get_player_presence_info_impl(), get_presence_statistics_impl() (+44 more)

### Community 156 - "player_schema_converter.py"
Cohesion: 0.07
Nodes (36): _inventory_item_with_weapon(), PlayerSchemaConverter, Any, Player schema conversion utilities. This module handles conversion of Player…, Get stats, inventory, and status_effects from player, handling async methods., Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…, Get PositionState from position value, with fallback to STANDING., Create PlayerRead schema from player object. (+28 more)

### Community 157 - "test_calendar_schemas.py"
Cohesion: 0.10
Nodes (19): Unit tests for calendar schemas. Tests the Pydantic models in calendar.py…, Test HolidayCollection.id_map property., Test HolidayCollection.ensure_unique_ids() detects duplicates., Test ScheduleEntry can be instantiated., Test ScheduleEntry validates days., Test HolidayEntry can be instantiated., Test HolidayEntry validates tradition., Test HolidayEntry validates season. (+11 more)

### Community 158 - "NPCSpawnRule"
Cohesion: 0.02
Nodes (138): _JSONDict, Base, _loads_json_dict(), NPCRelationship, NPCSpawnRule, DeclarativeBase, Get base stats as dictionary., Set base stats from dictionary. (+130 more)

### Community 159 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages. These schemas define the structure and… (+55 more)

### Community 160 - "ApplicationContainer"
Cohesion: 0.00
Nodes (789): Lock, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), _create_npc_services_on_app(), _ensure_room_cache_before_npc_startup(), _get_item_prototype_count(), _get_item_prototype_entries(), initialize_combat_services() (+781 more)

### Community 161 - "test_room_subscription_manager_drops.py"
Cohesion: 0.03
Nodes (64): fixture, Unit tests for room subscription manager drop functions. Tests the room drop…, Test adjust_room_drop() returns False for invalid index., Test list_room_drops() returns room drops., Test add_room_drop() adds drop to new room., Test add_room_drop() adds drop to existing room., Test take_room_drop() successfully takes drop., Test take_room_drop() with index out of range. (+56 more)

### Community 162 - "PlayerSavePreparer"
Cohesion: 0.11
Nodes (19): Initialize the player repository. Args: room_cache: Shared room cache for room…, _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Player save/upsert helpers for PlayerRepository. Handles inventory validation,… (+11 more)

### Community 163 - "test_validation.py"
Cohesion: 0.03
Nodes (64): custom_length_validator(), fixture, Unit tests for NATS Subject Validator. Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter. (+56 more)

### Community 164 - ".state"
Cohesion: 0.06
Nodes (64): _apply_grounding_adjustment(), _complete_ground_command(), _get_ground_services(), handle_ground_command(), handle_rescue_command(), _normalize_player_ids(), Any, UUID (+56 more)

### Community 165 - "TestSanitization"
Cohesion: 0.05
Nodes (44): _collect_safe_context_fields(), _contains_sensitive_detail_pattern(), is_safe_detail_key(), Sanitization helpers for legacy MythosMUD error responses. Extracted from…, Sanitize dictionary detail values, keeping only safe keys., Sanitize each element in a list detail value., Return detail dict entries that use safe keys with sanitized values., Sanitize a detail value to prevent information exposure. Uses bleach for HTML… (+36 more)

### Community 166 - "CombatConfigurationService"
Cohesion: 0.08
Nodes (19): CombatConfigurationService, get_combat_configuration(), Any, Initialize the combat configuration service., Get current combat configuration. Returns: CombatConfiguration: Current combat…, Get combat configuration for a specific scope. Args: scope: Configuration scope…, Update combat configuration. Args: updates: Dictionary of configuration updates…, Clear all configuration overrides. (+11 more)

### Community 167 - "_asyncio_mark"
Cohesion: 0.10
Nodes (27): _asyncio_mark, _await_shutdown_result(), Test handle_shutdown_command() when player service is not available., Test handle_shutdown_command() when player is not found., Test handle_shutdown_command() when player lacks admin permission., Test handle_shutdown_command() with invalid parameters., Test handle_shutdown_command() with cancel action., Test handle_shutdown_command() with cancel when no active shutdown. (+19 more)

### Community 168 - "chat_message_senders.py"
Cohesion: 0.07
Nodes (62): RoomChatHistory, normalize_player_id(), Any, ChatMessage, UUID, Channel message senders (system, whisper, party, global)., Send a whisper message from one player to another. This function publishes the…, Normalize player identifiers to string form. (+54 more)

### Community 169 - "inventory_equip_command.py"
Cohesion: 0.06
Nodes (64): _equip_stack_from_inventory_index(), _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), handle_wearable_container_on_unequip(), normalize_equipped_items(), normalize_inventory_slots(), InventoryStack (+56 more)

### Community 170 - "test_corpse_lifecycle_service.py"
Cohesion: 0.02
Nodes (116): CorpseLifecycleService, CorpseNotFoundError, CorpseServiceError, _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID (+108 more)

### Community 171 - "test_party_service.py"
Cohesion: 0.04
Nodes (49): Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves., Leader can disband the party., Non-leader cannot disband. (+41 more)

### Community 172 - "maps.py"
Cohesion: 0.07
Nodes (57): MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter…, _AsciiMapViewport, _build_ascii_map_response(), _build_ascii_minimap_response(), get_ascii_map(), get_ascii_minimap() (+49 more)

### Community 173 - "test_quest_service.py"
Cohesion: 0.06
Nodes (58): _make_definition_row(), _make_turn_in_definition_row(), asyncio, Unit tests for QuestService. Covers: resolve_name_to_quest_id, start_quest,…, start_quest returns error when quest id not found., start_quest returns error when player already has active instance., start_quest returns error when player already completed quest., start_quest re-activates abandoned instance instead of INSERT (avoids UNIQUE… (+50 more)

### Community 174 - "test_async_persistence_room_cache.py"
Cohesion: 0.04
Nodes (60): asyncio, Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test get_user_by_username_case_insensitive when no session is yielded., Test get_professions when no session is yielded., Test get_players_batch with empty list., Test get_players_batch with actual players (UUID conversion)., Test _generate_room_id_from_zone_data when stable_id already has full path., Test _generate_room_id_from_zone_data when room ID needs generation. (+52 more)

### Community 175 - "fixtures/integration/__init__.py"
Cohesion: 0.07
Nodes (48): FixtureRequest, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+40 more)

### Community 176 - "PydanticErrorHandler"
Cohesion: 0.07
Nodes (35): convert_pydantic_error(), _ExtractedErrorInfo, _ExtractedFieldErrorInfo, handle_pydantic_error(), TypedDict, Unpack, ValidationError, PydanticErrorHandler (+27 more)

### Community 177 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (35): CatatoniaRegistry, datetime, UUID, In-memory registry tracking catatonic investigators., Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not… (+27 more)

### Community 178 - "gameStore.ts"
Cohesion: 0.10
Nodes (36): fetchSpy, useMapLayout(), buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData(), UseRoomMapDataResult (+28 more)

### Community 179 - "OccupantFormatter"
Cohesion: 0.04
Nodes (65): OccupantFormatter, Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Formats and separates occupants by type., Initialize occupant formatter., Check if a string looks like a UUID. Args: value: The string to check Returns:… (+57 more)

### Community 180 - "admin_shutdown_command.py"
Cohesion: 0.10
Nodes (39): _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state(), countdown_loop(), _create_countdown_task() (+31 more)

### Community 181 - "ConnectionCleaner"
Cohesion: 0.08
Nodes (26): ConnectionCleaner, Any, UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return connection IDs that exceed max_connection_age., Extract player_id from connection metadata if present. (+18 more)

### Community 182 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 183 - "test_container_persistence.py"
Cohesion: 0.02
Nodes (146): ContainerData, create_container(), delete_container(), _fetch_container_items(), get_container(), get_containers_by_entity_id(), get_containers_by_room_id(), _parse_jsonb_column() (+138 more)

### Community 184 - "useGameClientV2Container.ts"
Cohesion: 0.09
Nodes (41): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), performGameClientLogout(), deriveActiveEffectsForHeader(), buildGameClientV2ContainerReturn() (+33 more)

### Community 185 - "command_input.py"
Cohesion: 0.06
Nodes (31): clean_command_input(), _is_predefined_emote(), normalize_command(), Command Input Utilities for MythosMUD. This module provides utilities for…, Clean and normalize command input by collapsing multiple spaces and stripping…, Normalize command input by removing optional slash prefix. Supports both…, Check if a command is a predefined emote alias. Args: command: The command to…, Check if a single word command should be treated as an emote. This function… (+23 more)

### Community 186 - "GameClientV2Dock.test.tsx"
Cohesion: 0.25
Nodes (9): chatHistoryLayoutIdentity, chatHistoryLayoutState, defaultChatHistoryLayoutKey, dockTest, mockPanelRecord(), mockPanelRecordCore(), mockPanelRecordFlags(), mockUsePanelManagerNoops() (+1 more)

### Community 187 - "ChatService"
Cohesion: 0.04
Nodes (37): ChatService, Any, UUID, Normalize player identifiers to string form., Send a say message to players in the same room. This method publishes the…, Send a local message to players in the same sub-zone. This method publishes the…, Send a global message to all players. This method publishes the global message…, Send a party (ephemeral group) chat message. Only current party members receive… (+29 more)

### Community 188 - "QuestService"
Cohesion: 0.06
Nodes (44): _call_add_item_to_inventory(), _definition_completion_mode_error(), _goals_met(), _has_collect_n_goals(), _parse_definition(), Any, UUID, QuestService (+36 more)

### Community 189 - "strict_mocker"
Cohesion: 0.28
Nodes (8): MockerFixture, Any, fixture, Strict mocking helpers for unit tests. Provides fixtures and helpers that…, Return a patch helper that enables autospec by default. Usage: patched_fn =…, Convenience helper for direct calls with autospec=True by default., strict_mocker(), strict_patch()

### Community 190 - "quest_commands.py"
Cohesion: 0.11
Nodes (35): _active_npc_ids_in_room(), _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence(), _get_quest_service(), handle_journal_command() (+27 more)

### Community 191 - "MemoryProfiler"
Cohesion: 0.05
Nodes (48): HealthResponse, Complete health response for the system., BaseModel, Unit tests for memory profiler utilities. Tests the MemoryProfiler class…, Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test Pydantic model for memory profiling tests. (+40 more)

### Community 192 - "combat_event_publisher"
Cohesion: 0.29
Nodes (7): combat_event_publisher(), mock_nats_service(), mock_subject_manager(), fixture, Create a mock NATS service., Create a mock subject manager., Create a CombatEventPublisher instance.

### Community 193 - "connection_initialization.py"
Cohesion: 0.04
Nodes (68): initialize_connection_cleaner(), initialize_connection_manager(), initialize_connection_maps(), initialize_core_components(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging() (+60 more)

### Community 194 - "test_active_lucidity_service.py"
Cohesion: 0.05
Nodes (59): active_lucidity_service(), mock_session(), asyncio, fixture, Unit tests for active lucidity service. Tests the ActiveLucidityService class…, Test apply_encounter_lucidity_loss() for acclimated encounter., Test apply_encounter_lucidity_loss() raises error for unknown category., Test apply_encounter_lucidity_loss() handles string player_id. (+51 more)

### Community 195 - "test_idle_movement.py"
Cohesion: 0.07
Nodes (27): Unit tests for idle movement. Tests the IdleMovementHandler class., Test _is_npc_in_combat() returns False when NPC is not in combat., Test _is_npc_in_combat() handles missing in_combat attribute., Test get_valid_exits() with room having no exits., Test get_valid_exits() when NPC definition has no sub_zone_id., When every target fails boundary validation, valid exits dict is empty., When validate_subzone_boundary accepts every target, all directions remain…, Test select_exit() with weighted_home disabled. (+19 more)

### Community 196 - "_handle_admin_set_stat_command"
Cohesion: 0.05
Nodes (72): _AdminSetStatApplyContext, _AdminSetStatLogContext, _apply_stat_change_and_build_result(), _build_set_stat_error_response(), _calculate_stat_warnings(), _get_app_or_error(), _handle_admin_set_stat_command(), _log_admin_set_stat() (+64 more)

### Community 197 - "test_async_persistence_core.py"
Cohesion: 0.04
Nodes (60): asyncio, Unit tests for async persistence layer: init, close, player, user, room,…, Test get_players_by_user_id delegates to PlayerRepository., Test get_active_players_by_user_id delegates to PlayerRepository., Test get_user_by_username_case_insensitive with successful lookup., Test get_user_by_username_case_insensitive when user not found., Test get_user_by_username_case_insensitive with database error., Test save_player delegates to PlayerRepository. (+52 more)

### Community 198 - "stateUpdateUtils.ts"
Cohesion: 0.10
Nodes (28): GameEvent, EventStore, IEventStore, HANDLERS, projectEvent(), projectState(), getInitialGameState(), PROJECTED_EVENT_TYPES (+20 more)

### Community 199 - "Any"
Cohesion: 0.16
Nodes (10): Any, WebSocket, Handle a WebSocket message using the appropriate handler. Args: websocket: The…, Handle a specific message type. Args: websocket: The WebSocket connection…, Handle command message type., Handle chat message type., Handle ping message type., Handle follow_response message type. (+2 more)

### Community 200 - "test_message_filtering.py"
Cohesion: 0.04
Nodes (49): message_filtering_helper(), mock_connection_manager(), asyncio, fixture, Unit tests for message filtering. Tests the MessageFilteringHelper class., Test should_apply_mute_check() returns True for sensitive channels., Test should_apply_mute_check() returns False for non-sensitive channels., Test compare_canonical_rooms() returns True for same rooms. (+41 more)

### Community 201 - "ChatPanelRuntimeViewParts.tsx"
Cohesion: 0.08
Nodes (25): ChannelActivityIndicators(), ChannelActivityIndicatorsProps, getActivityColor(), ChannelSelectorSection(), ChannelSelectorSectionProps, ChatHeader(), ChatExportDialog(), ChatExportDialogProps (+17 more)

### Community 202 - "test_combat_persistence_handler_events.py"
Cohesion: 0.07
Nodes (38): asyncio, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully., Test _publish_player_dp_update_event_impl handles no NATS service., Test _publish_player_dp_update_event_impl with all optional parameters., Test _publish_player_dp_update_event_impl handles event bus publish error., Test _publish_player_dp_correction_event publishes correction event., Test _publish_player_dp_correction_event handles errors gracefully. (+30 more)

### Community 203 - "test_map_helpers.py"
Cohesion: 0.08
Nodes (36): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities. Extracted from… (+28 more)

### Community 204 - "test_inventory_helpers.py"
Cohesion: 0.02
Nodes (120): Resolve persistence and connection manager from request., resolve_state(), _first_normalized_wear_slot(), infer_equip_slot_from_prototype(), _inventory_prototype_id(), prototype_from_registry(), prototype_registry_from_request(), Prototype registry access and equip-slot inference for inventory items. (+112 more)

### Community 205 - "StatusEffect"
Cohesion: 0.04
Nodes (71): InventoryItem, Player, BaseModel, Represents an item in a player's inventory., Pydantic Player model for game logic and validation. This is separate from the…, Add an item to the player's inventory. Args: item_id: Unique identifier for the…, Remove an item from the player's inventory. Args: item_id: Unique identifier…, Add a status effect to the player. Args: effect: StatusEffect to add (+63 more)

### Community 206 - "MonitoringDashboard"
Cohesion: 0.06
Nodes (40): PerformanceStats, ExceptionStats, Statistics for exception tracking., __getattr__(), Any, Monitoring package for MythosMUD server., Lazy import for modules that require numpy., Alert (+32 more)

### Community 207 - "EventHandler"
Cohesion: 0.08
Nodes (19): _as_event_data_dict(), EventHandler, Handler for NATS event messages., Initialize event handler. Args: connection_manager: ConnectionManager instance…, Get mapping of event types to their handler methods. Returns: Dictionary…, Validate that event message has required fields. Args: event_type: Event type…, Handle incoming event messages from NATS. Args: message_data: Event message…, Handle player_entered event. Args: data: Event data containing player and room… (+11 more)

### Community 208 - "useAsciiMapState.ts"
Cohesion: 0.06
Nodes (42): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+34 more)

### Community 209 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 210 - "MemoryMonitor"
Cohesion: 0.06
Nodes (17): useGameClientV2MemoryMonitorEffect(), ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor (+9 more)

### Community 211 - "fixtures/auth.ts"
Cohesion: 0.09
Nodes (31): assertCommandChannelReady(), EnsurePlayableConnectionOptions, executeCommandWithoutRecovery(), focusCommandInput(), getCommandPanelInput(), isPageUsable(), isUsernameLoginVisible(), loginPlayer() (+23 more)

### Community 212 - "handle_time_command"
Cohesion: 0.20
Nodes (15): handle_time_command(), Any, Handle the time command, exposing the current Mythos time and active holidays., asyncio, Unit tests for time command handlers. Tests the time command functionality., Test handle_time_command() handles holiday service errors., Test handle_time_command() handles missing holiday service., Test handle_time_command() returns time information. (+7 more)

### Community 213 - "logging_file_setup.py"
Cohesion: 0.05
Nodes (73): Handler, Logger, _PlayerGuidFormatterType, Queue, QueueListener, _add_handler_to_loggers(), _CategoryHandlerConfig, _ConsoleHandlerConfig (+65 more)

### Community 214 - "test_connection_session_management.py"
Cohesion: 0.06
Nodes (60): _cleanup_old_session_tracking(), _cleanup_player_data_for_session(), _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), handle_new_game_session_impl(), _is_websocket_connected(), Any, UUID (+52 more)

### Community 215 - "safe_run_static"
Cohesion: 0.07
Nodes (34): get_project_root(), Determine the project root based on current working directory, main(), Run a psql command and return the result., Load all seed data files., run_psql_command(), _combined_output(), _CompletedProcessLike (+26 more)

### Community 216 - "Arena Zone DML Generator"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 217 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 218 - "test_manager.py"
Cohesion: 0.03
Nodes (70): fixture, Unit tests for NATS Subject Manager. Tests the NATSSubjectManager class., Test build_subject() raises SubjectValidationError for invalid parameter., Test validate_subject() returns True for valid subject., Test validate_subject() returns False for invalid subject., Test validate_subject() accepts events.domain.{event_type} (distributed…, Test validate_subject() returns False for empty subject., Test validate_subject() uses cache for repeated validations. (+62 more)

### Community 219 - "test_async_persistence_delegates.py"
Cohesion: 0.05
Nodes (58): Reset the global async persistence instance for testing. DEPRECATED: Use…, reset_async_persistence(), asyncio, Unit tests for async persistence layer: health, container, item, singleton,…, Test async_heal_player delegates to HealthRepository., Test damage_player delegates to HealthRepository., Test async_damage_player delegates to HealthRepository., Test create_container with ContainerCreateParams. (+50 more)

### Community 220 - "commandStore.ts"
Cohesion: 0.16
Nodes (15): CommandActions, CommandAlias, CommandHistoryEntry, CommandSelectors, CommandState, CommandStore, CommandStoreGet, CommandStoreSet (+7 more)

### Community 221 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+21 more)

### Community 222 - "HolidayCollection"
Cohesion: 0.07
Nodes (21): HolidayCollection, Create a mapping of holiday IDs to holiday entries. Returns: dict[str,…, Ensure all holiday IDs are unique. Raises: ValueError: If duplicate holiday IDs…, Wrapper for the complete holiday JSON payload., Get the holiday collection. Returns: HolidayCollection: The loaded holiday…, Test refresh_active activates holidays matching current date., Test refresh_active returns empty when no holidays match., Test refresh_active expires holidays past their duration. (+13 more)

### Community 223 - "test_command_parser_helpers.py"
Cohesion: 0.05
Nodes (37): Unit tests for command_parser helper methods. Tests the helper methods in…, Test _create_command_object() handles 'l' alias., Test _create_command_object() handles 'g' alias., Test _create_command_object() handles 'w' alias., Test _create_command_object() raises error for unsupported command., Test _create_command_object() handles PydanticValidationError., Test _create_command_object() handles ValueError., Test _normalize_command() removes leading slash. (+29 more)

### Community 224 - "test_game_state_provider.py"
Cohesion: 0.05
Nodes (53): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for game state provider. Tests the GameStateProvider class. (+45 more)

### Community 225 - "CombatMonitoringService"
Cohesion: 0.08
Nodes (17): CombatMonitoringService, Comprehensive combat monitoring and alerting service. Tracks combat system…, Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier…, Start monitoring a combat turn. Args: combat_id: Unique combat identifier, End monitoring a combat turn. Args: combat_id: Unique combat identifier, Get current combat metrics. Returns: CombatMetrics: Current metrics, Resolve an alert. Args: alert_id: Alert identifier Returns: bool: True if alert… (+9 more)

### Community 226 - "PlayerService"
Cohesion: 0.01
Nodes (495): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+487 more)

### Community 227 - "test_room_subscription_manager.py"
Cohesion: 0.04
Nodes (53): asyncio, fixture, Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test add_room_occupant() adds occupant., Test add_room_occupant() with multiple occupants., Test add_room_occupant() adds occupant to new room. (+45 more)

### Community 228 - "test_chat_service.py"
Cohesion: 0.05
Nodes (56): asyncio, Unit tests for chat service. Tests the ChatService class and ChatMessage class., Test send_say_message() when rate limited., Test send_say_message() when player is not in a room., Test send_local_message() with empty message., Test send_global_message() with empty message., Test send_emote_message() with empty action., Test send_whisper_message() with no target. (+48 more)

### Community 229 - "is_player_in_grace_period"
Cohesion: 0.07
Nodes (40): is_player_in_grace_period(), Check if a player is currently in grace period. Args: player_id: The player's…, mock_app_with_services(), mock_connection_manager_full(), mock_persistence_full(), MockPersistenceFull, asyncio, fixture (+32 more)

### Community 230 - "useMythosAppActions.ts"
Cohesion: 0.07
Nodes (67): getCreateCharacterErrorMessage(), CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), extractErrorMessageFromResponseBody() (+59 more)

### Community 231 - "WebSocketRequestContext"
Cohesion: 0.05
Nodes (46): command_request_app_state(), CommandExecutionRequest, HTTP Request or WebSocketRequestContext for unified command processing., Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…, Any, Request context factory for WebSocket command processing. This module provides…, Get the event bus from the request context., Get the alias storage from the request context. (+38 more)

### Community 232 - "collect_inventory.py"
Cohesion: 0.07
Nodes (44): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+36 more)

### Community 233 - "ChatModeration"
Cohesion: 0.06
Nodes (32): ChatModeration, normalize_player_id(), PlayerServiceProtocol, Any, datetime, Protocol, UUID, Chat moderation utilities. This module provides moderation functionality… (+24 more)

### Community 234 - "resolve_weapon_attack_from_equipped"
Cohesion: 0.09
Nodes (33): Any, NamedTuple, Weapon resolution helpers for combat. Resolves equipped main-hand items to…, Result of resolving an equipped item to a weapon attack. base_damage: Rolled…, Resolve equipped main-hand stack to weapon attack info, or None if unarmed., resolve_weapon_attack_from_equipped(), _roll_weapon_attack(), _weapon_damage_bounds() (+25 more)

### Community 235 - "EnvironmentalContainerLoader"
Cohesion: 0.17
Nodes (10): EnvironmentalContainerLoader, Any, ContainerComponent, ContainerLockState, UUID, migrate_room_container_to_postgresql., Load all environmental containers for a room from PostgreSQL. Args: room_id:…, Service for loading environmental containers from JSON and PostgreSQL. Handles… (+2 more)

### Community 236 - "mapPageRenderer.tsx"
Cohesion: 0.09
Nodes (24): AppRouter(), MapPage, SkillsPage, RoomMapViewerProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView() (+16 more)

### Community 237 - "chat_service.py"
Cohesion: 0.07
Nodes (36): ChatMessage, Any, UUID, Chat message model for MythosMUD. This module provides the ChatMessage class…, Represents a chat message with metadata., Convert message to dictionary for serialization., Log this chat message to the communications log., clear_player_pose() (+28 more)

### Community 238 - "Async Remediation Complete"
Cohesion: 0.25
Nodes (11): asyncio.to_thread Offloading, Async Audit 2025-12-03, Passive Lucidity Flux Blocking, Async Audit Executive Summary, Three-Phase Async Remediation Plan, Async Remediation Complete, Room Cache 60s TTL, Async Remediation Final Report (+3 more)

### Community 239 - "NPCCombatIntegrationBase"
Cohesion: 0.06
Nodes (30): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Apply combat effects to a target (player or NPC). Args: target_id: ID of the…, Convert target_id to UUID, accepting either string or UUID input., Apply combat effects to a player. (+22 more)

### Community 240 - "NATSConnectionError"
Cohesion: 0.05
Nodes (35): NATSConnectionError, NATSHealthCheckError, Exception, Raised when NATS connection operations fail., Raised when health check operations fail., Unit tests for NATS exception classes. Tests the NATS exception hierarchy for…, Test NATSSubscribeError stores subject., Test NATSSubscribeError stores original error. (+27 more)

### Community 241 - "RoomDataValidator"
Cohesion: 0.06
Nodes (39): Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Check if occupant count matches the actual occupants list length. Args:…, Validates room data structure and content., Check for duplicate occupants in the room. Args: room_data: Room data to check…, Check if room has occupants but no name. Args: room_data: Room data to check…, Validate room data structure and content. Args: room_data: Room data to… (+31 more)

### Community 242 - "apiTypeGuards.ts"
Cohesion: 0.10
Nodes (48): LoginResponse, ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString() (+40 more)

### Community 243 - "error_handling_middleware.py"
Cohesion: 0.06
Nodes (43): Response, add_error_handling_middleware(), ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Exception, FastAPI, Protocol (+35 more)

### Community 244 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.17
Nodes (17): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+9 more)

### Community 245 - "test_command_magic.py"
Cohesion: 0.05
Nodes (52): CastCommand, LearnCommand, field_validator, Command for casting a spell., Validate spell name format., Validate target format., Validate spell name format., Command for learning a spell. (+44 more)

### Community 246 - "LogAggregator"
Cohesion: 0.07
Nodes (29): aggregate_log_entry(), get_log_aggregator(), LogAggregator, LogEntry, LogQueryFilter, Any, Path, Log aggregation and centralized collection system for MythosMUD server. This… (+21 more)

### Community 247 - "PlayerNameExtractor"
Cohesion: 0.02
Nodes (83): PlayerNameExtractor, Any, UUID, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:…, Perform basic validation on player name (not None, is string, not empty). Args:…, Utility class for extracting and validating player names. CRITICAL: NEVER uses… (+75 more)

### Community 248 - "TestValidatorComponents"
Cohesion: 0.14
Nodes (8): Integration tests for the main validator CLI. Tests the complete validation…, Test path validator integration., Test reporter integration., Test the full validation pipeline., Test individual validator components., Test room loader integration., Test schema validator integration., TestValidatorComponents

### Community 249 - "log_and_raise"
Cohesion: 0.05
Nodes (37): Heal a player's health., Damage a player's health., Award experience points to a player. CRITICAL FIX: This method prevents XP…, Apply lucidity loss to a player., Apply fear to a player., Apply corruption to a player., Get all players currently in a room. Args: room_id: The ID of the room to check…, _build_container_data_from_row() (+29 more)

### Community 250 - "useDraggablePanelInteractions.ts"
Cohesion: 0.09
Nodes (41): DraggablePanel(), DraggablePanelProps, isMouseEventOnHeader(), isPanelDragBlockedTarget(), PANEL_DRAG_BLOCK_SELECTORS, relativeSizeToAbsolute(), relativeToAbsolute(), applyDragMove() (+33 more)

### Community 251 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 252 - "test_nats_messages.py"
Cohesion: 0.06
Nodes (49): Realtime domain schemas: realtime API, NATS messages, WebSocket messages., BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, field_validator, Pydantic schemas for NATS message validation. This module provides type-safe… (+41 more)

### Community 253 - "test_player_event_handlers_state.py"
Cohesion: 0.05
Nodes (51): mock_connection_manager(), mock_logger(), mock_utils(), player_state_event_handler(), asyncio, fixture, Unit tests for player state event handlers. Tests the PlayerStateEventHandler…, Test handle_player_xp_awarded() handles player without current_room_id. (+43 more)

### Community 254 - "test_logout_commands.py"
Cohesion: 0.04
Nodes (103): _clear_corrupted_cache_entry(), _disconnect_player_connections(), _force_disconnect_player(), _get_app_services(), _get_player_for_logout(), _get_player_position_from_connection_manager(), handle_logout_command(), handle_quit_command() (+95 more)

### Community 255 - "test_player_occupant_processor.py"
Cohesion: 0.04
Nodes (49): mock_connection_manager(), mock_name_extractor(), processor(), asyncio, fixture, Unit tests for player occupant processor. Tests the PlayerOccupantProcessor…, Test _convert_player_ids_to_uuids handles mixed string and UUID types., Test _convert_player_ids_to_uuids handles UUID objects. (+41 more)

### Community 256 - "get_username_from_user"
Cohesion: 0.03
Nodes (87): _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting(), Any, Channel management commands for Advanced Chat Channels. This module provides…, Validate channel name. Returns error dict if invalid, None if valid., Handle the channel command for switching channels or setting default channel.… (+79 more)

### Community 257 - "persistence/container_persistence.py"
Cohesion: 0.04
Nodes (102): ContainerCreateParams, Shared parameters for container creation (sync DB and async repository paths)., Optional fields for creating a container row (beyond source_type)., _after_container_insert(), _allowed_roles_from_row(), _as_opt_datetime(), _as_opt_str(), _as_opt_uuid() (+94 more)

### Community 258 - "game_tick_processing.py"
Cohesion: 0.04
Nodes (104): broadcast_tick_event(), cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _create_corpse_lifecycle_service(), game_tick_loop(), get_current_tick(), get_tick_interval(), _log_cleanup_results() (+96 more)

### Community 259 - "GameLogPanel.tsx"
Cohesion: 0.09
Nodes (31): GameTerminalPresentation(), GameTerminalPresentationProps, GameLogListMessage, GameLogMessagesList(), GameLogMessagesListProps, GameLogPanel(), GameLogPanelProps, GameLogPanelFilterBar() (+23 more)

### Community 260 - "playerHandlers.ts"
Cohesion: 0.15
Nodes (22): handlePlayerDeliriumRespawned(), handlePlayerDied(), handlePlayerDpUpdated(), handlePlayerEntered(), handlePlayerEnteredGame(), handlePlayerLeft(), handlePlayerLeftGame(), handlePlayerRespawned() (+14 more)

### Community 261 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 262 - "migration_examples.py"
Cohesion: 0.06
Nodes (34): expensive_operation(), migration_example_1(), migration_example_10(), migration_example_11(), migration_example_12(), migration_example_13(), migration_example_14(), migration_example_15() (+26 more)

### Community 263 - "router.py"
Cohesion: 0.03
Nodes (141): handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command., Handle NPC reaction trigger command., Handle NPC behavior stop command. (+133 more)

### Community 264 - "RoomMapEditorRuntime.hooks.ts"
Cohesion: 0.10
Nodes (22): useMapEditing(), UseRoomMapDataOptions, MapEditToolbar(), MapEditToolbarProps, buildModalCreateEdgeHandler(), buildModalPreviewHandler(), buildModalUpdateEdgeHandler(), buildModalUpdateRoomHandler() (+14 more)

### Community 265 - "asyncio"
Cohesion: 0.07
Nodes (27): asyncio, Test get_adjacent_rooms() handles room with no exits., Test get_adjacent_rooms() handles target room not found., Test validate_room_exists() uses cache., Test validate_room_exists() falls back to persistence., Test validate_exit_exists() returns False when from_room not found., Test get_room_occupants() handles Room object with get_players/get_npcs., Test get_room_occupants() falls back to persistence. (+19 more)

### Community 266 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 267 - "ChatChannelLoggerMixin"
Cohesion: 0.10
Nodes (19): ChatChannelLoggerMixin, Any, Path, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper…, Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs. (+11 more)

### Community 268 - "player.ts"
Cohesion: 0.14
Nodes (24): assertNpcSpawnVisible(), hasCombatMessage(), isInCombatStatus(), isInDeathVoid(), isWardBlockingCombat(), keepFirstCultistInstanceId(), resolveSpawnedCultistTarget(), retryUntilCombatStarted() (+16 more)

### Community 269 - "PeriodicOrphanAuditor"
Cohesion: 0.13
Nodes (11): create_lifespan_memory_service(), PeriodicOrphanAuditor, Any, Core capability for granular investigation cycles. Repeated universal analysis…, Execute a single investigation loop synchronously producing operator summary.…, Stop the periodic orphan auditor background enforcement., Create a centralized memory operations coordinator instance targeted for…, Periodic background auditor that investigates orphanage patterns and memory… (+3 more)

### Community 270 - "test_login_grace_period_visual_indicator.py"
Cohesion: 0.06
Nodes (38): NPC occupant processing utilities. This module handles querying and processing…, Player name extraction and validation utilities. This module provides utilities…, PlayerOccupantProcessor, Any, UUID, Player occupant processing utilities. This module handles querying and…, Process players and convert to occupant information. Args: room_id: The room ID…, Processes player occupants for rooms. (+30 more)

### Community 271 - "PlayerPreferencesService"
Cohesion: 0.14
Nodes (18): PlayerPreferencesService, Any, AsyncSession, UUID, Player Preferences Service for Advanced Chat Channels. This module provides…, Get preferences for a player. Args: session: Database session player_id: The…, Update a player's default channel. Args: session: Database session player_id:…, Mute a channel for a player. Args: session: Database session player_id: The… (+10 more)

### Community 272 - "TestFeatureFlagService"
Cohesion: 0.05
Nodes (22): Test is_combat_monitoring_enabled returns True when enabled., Test is_combat_monitoring_enabled returns False when disabled., Test get_combat_configuration returns all combat settings., Test clear_cache resets all cached values., Test validate_combat_requirements returns True when combat is disabled., Test validate_combat_requirements returns True with valid configuration., Test suite for FeatureFlagService class., Test validate_combat_requirements returns False with invalid tick interval. (+14 more)

### Community 273 - "test_memory_leak_metrics.py"
Cohesion: 0.05
Nodes (42): collector(), fixture, Unit tests for memory leak metrics collector. Tests the…, Test collection of cache metrics., Test collection of task metrics., Test collection of NATS metrics., Test collection of all metrics., Test calculation of growth rates. (+34 more)

### Community 274 - "alias_schema.json"
Cohesion: 0.04
Nodes (51): command, version, additionalProperties, additionalProperties, description, properties, required, type (+43 more)

### Community 275 - "Any"
Cohesion: 0.13
Nodes (12): Any, Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits…, Build exit lookup map from room data., Render a single row of rooms with horizontal exits., Render an ASCII map as HTML. Args: rooms: List of room dictionaries with…, Return the horizontal exit character (—, >, or <) given east/west exit state,…, Get exit character to display after a room for horizontal (east/west) exits.… (+4 more)

### Community 276 - "RoomIDUtils"
Cohesion: 0.06
Nodes (35): Any, Check if NPC room IDs match target room IDs using fallback comparison. Args:…, Check if NPC room matches target room using normalized comparison. Args:…, Utilities for room ID normalization and comparison., Initialize room ID utilities. Args: connection_manager: ConnectionManager…, Get canonical room ID for consistent comparison. Args: room_id: The room ID…, Normalize room ID for comparison. Args: rid: Room ID to normalize Returns:…, Check if two normalized room IDs match. Args: id1: First normalized room ID… (+27 more)

### Community 277 - "test_admin_shutdown_command.py"
Cohesion: 0.07
Nodes (42): _AppWithoutState, _InitiateAppStub, _InitiateStateStub, _PendingCheckAppStub, _PendingCheckStateStub, Unit tests for admin shutdown command handler. Tests the shutdown command…, Test is_shutdown_pending() returns True when shutdown is pending., Test is_shutdown_pending() returns False when shutdown is not pending. (+34 more)

### Community 278 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 279 - "ExceptionTracker"
Cohesion: 0.05
Nodes (40): ExceptionContextTrackInput, ExceptionRecord, ExceptionTracker, ExceptionTrackInput, get_exception_tracker(), Any, Exception, TypedDict (+32 more)

### Community 280 - "Logging Compliance Checker"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 281 - "disconnect_grace_period.py"
Cohesion: 0.09
Nodes (34): cancel_grace_period(), Any, UUID, Disconnect grace period management for MythosMUD. This module handles the…, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, Start a grace period for a disconnected player. During the grace period, the…, start_grace_period(), mock_manager() (+26 more)

### Community 282 - "GameClientV2ContainerView.tsx"
Cohesion: 0.11
Nodes (16): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, TabbedInterfaceOverlay(), TabbedInterfaceOverlayProps (+8 more)

### Community 283 - "ErrorMonitor"
Cohesion: 0.13
Nodes (17): ErrorMonitor, main(), Any, datetime, Path, Detect error trends over time. Returns trend analysis results., Check for alert conditions. Returns list of active alerts., Monitor errors continuously for a specified duration. Args: log_dir: Directory… (+9 more)

### Community 284 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 285 - "test_pattern_matcher.py"
Cohesion: 0.05
Nodes (44): Initialize NATS Subject Manager. Args: enable_cache: Enable validation result…, PatternMatcher, Any, Pattern matching utilities for NATS Subject Manager. This module provides…, Matcher for validating subjects against registered patterns., Initialize pattern matcher. Args: strict_validation: Enable strict validation…, Check if subject matches any registered pattern. Args: subject: Subject string…, Check if subject components match a pattern. Args: components: Subject… (+36 more)

### Community 286 - "Linting Results Comparator"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 287 - "test_health.py"
Cohesion: 0.06
Nodes (61): ConnectionsComponent, DatabaseComponent, HealthErrorResponse, HealthStatus, BaseModel, StrEnum, Health monitoring models for MythosMUD. This module contains Pydantic models…, Error response for health check failures. (+53 more)

### Community 288 - ".execute_idle_movement"
Cohesion: 0.20
Nodes (8): _cfg_float(), _npc_id_str(), _passes_movement_probability(), Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement. Checks multiple conditions: -…, Get exits from current room that stay within subzone boundaries. Args:…, Execute idle movement for an NPC. This method orchestrates the full idle…, _resolve_spawn_room()

### Community 289 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (49): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id. Args: room_drops: List of…, Unit tests for look item helper functions. Tests the helper functions in…, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items. (+41 more)

### Community 290 - "test_aggro_threat.py"
Cohesion: 0.04
Nodes (98): _apply_taunt_and_maybe_broadcast(), Apply taunt and broadcast target switch if aggro changed. Returns error dict or…, add_damage_threat(), add_heal_threat(), _aggression_scale(), apply_stealth_wipe(), apply_taunt(), clear_aggro_for_combat() (+90 more)

### Community 291 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 292 - "test_command_combat.py"
Cohesion: 0.04
Nodes (49): Unit tests for combat command models. Tests the combat command models and their…, Test PunchCommand validates target min length., Test PunchCommand validates target max length., Test KickCommand has correct default values., Test KickCommand can have optional target., Test KickCommand calls validate_combat_target when target provided., Test KickCommand accepts None for target., Test KickCommand validates target min length. (+41 more)

### Community 293 - "useRespawnHandlers.ts"
Cohesion: 0.13
Nodes (27): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), fetchSpy (+19 more)

### Community 294 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 295 - "NATSMetrics"
Cohesion: 0.04
Nodes (41): NATSMetrics, Any, NATS metrics collection for MythosMUD. This module provides metrics collection…, NATS-specific metrics collection for monitoring and alerting., Record publish operation metrics., Record subscribe operation metrics., Record batch flush operation metrics., Update connection health score (0-100). (+33 more)

### Community 296 - "test_player_event_handlers.py"
Cohesion: 0.05
Nodes (51): mock_chat_logger(), mock_connection_manager(), mock_message_builder(), mock_name_extractor(), mock_occupant_manager(), mock_room_sync_service(), mock_task_registry(), player_event_handler() (+43 more)

### Community 297 - "get_async_session"
Cohesion: 0.06
Nodes (45): add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., fetch_professions(), Profession, Get all available professions using SQLAlchemy ORM., close_db() (+37 more)

### Community 298 - "setup.ts"
Cohesion: 0.21
Nodes (4): createDomPurifyTestWindow(), installDomPurifyTestWindow(), defaultFetchMock, installLocalStorageShim()

### Community 299 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 300 - "MessageFilteringHelper"
Cohesion: 0.05
Nodes (35): MessageFilteringHelper, Any, Extract information from chat event. Args: chat_event: Chat event dictionary…, Determine if mute check should be applied for a channel. Args: channel: Channel…, Compare two room IDs using canonical room ID resolution. Args: player_room_id:…, Get player's current room ID from online players cache. Args: player_id: Player…, Get player's current room ID from async persistence layer. Args: player_id:…, Helper class for message filtering operations. (+27 more)

### Community 301 - "test_message_handlers.py"
Cohesion: 0.11
Nodes (30): handle_chat_message(), handle_client_error_report_message(), handle_command_message(), handle_follow_response_message(), handle_party_invite_response_message(), handle_ping_message(), Any, WebSocket (+22 more)

### Community 302 - "character-cleanup.ts"
Cohesion: 0.08
Nodes (27): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+19 more)

### Community 303 - "RealTimeEventHandler"
Cohesion: 0.01
Nodes (173): Any, UUID, Get the next sequence number for events., Subscribe to relevant game events., Delegate player left event to specialized handler., Delegate NPC left event to specialized handler., Delegate player XP awarded event to specialized handler., Delegate player DP updated event to specialized handler. (+165 more)

### Community 304 - "AI Executor Protocol"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 305 - "HealthMonitor"
Cohesion: 0.11
Nodes (17): HealthMonitor, Any, UUID, Find player_id for cleanup when metadata is missing., Check if connection is stale based on timeout., Check if WebSocket is actually open., Validate token and update last validation time if needed., Process health check for a single connection. (+9 more)

### Community 306 - "player_combat_service_support.py"
Cohesion: 0.06
Nodes (35): Despawn NPC with defensive error handling. Args: npc_id: ID of the NPC to…, Despawn an NPC. Args: npc_id: ID of the NPC to despawn _room_id: ID of the room…, async_load_lifecycle_manager(), available_lifecycle_npc_ids(), EventBusPublish, lifecycle_lookup_id(), log_missing_lifecycle_npc(), NPCCombatIntegrationReadApi (+27 more)

### Community 307 - "system_monitoring.py"
Cohesion: 0.05
Nodes (38): Response model for system metrics., Response model for system monitoring summary., SystemMetricsResponse, SystemMonitoringSummaryResponse, get_system_health(), get_system_monitoring_alerts(), get_system_monitoring_summary(), get (+30 more)

### Community 308 - "TestCombatMessagingService"
Cohesion: 0.07
Nodes (22): asyncio, fixture, Test get_death_message with custom template., Test get_combat_start_messages generates messages for all occupants., Test get_combat_start_messages with single occupant., Test get_combat_end_messages generates messages for all occupants., Test suite for CombatMessagingService class., Test get_combat_end_messages from winner perspective. (+14 more)

### Community 309 - "Hierarchical Schema Tests"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 310 - "PlayerRead"
Cohesion: 0.04
Nodes (46): PlayerCreationService, Any, Stats, UUID, Create a new player character with specific stats. Args: name: The player's…, Service for player creation operations., Initialize with persistence layer, schema converter, and optional instance…, Resolve starting room and tutorial instance ID. For tutorial players, returns… (+38 more)

### Community 312 - "Execution Steps"
Cohesion: 0.05
Nodes (36): BEFORE EXECUTING THIS SCENARIO, YOU MUST, BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, CONFIRMATION CHECKLIST, EXECUTION AFFIRMATION (Type this before proceeding), 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER, Execution Steps, Expected Results (+28 more)

### Community 313 - "handle_quest_command"
Cohesion: 0.09
Nodes (38): ExitStack, handle_quest_command(), Handle quest command subcommands: abandon, ask, turnin. Usage: quest abandon…, current_user(), _enter_quest_command_patches(), mock_request(), asyncio, fixture (+30 more)

### Community 314 - "test_combat_persistence_handler_persistence.py"
Cohesion: 0.09
Nodes (32): asyncio, Unit tests for combat persistence handler - persistence operations. Tests…, Test _persist_player_dp_sync calls _verify_player_save., Test _persist_player_dp_sync handles save_player error., Test _persist_player_dp_sync completes full flow with verification and logging., Test _persist_player_dp_sync handles get_stats error., Test _persist_player_dp_sync complete flow including verification., Test _persist_player_dp_sync handles get_stats error gracefully. (+24 more)

### Community 315 - "SubjectValidator"
Cohesion: 0.06
Nodes (44): Custom exceptions for NATS Subject Manager. This module defines all exception…, Exception raised when subject validation fails., SubjectValidationError, NATS Subject Manager for MythosMUD. This package provides centralized subject…, NATS Subject Manager for MythosMUD. This module provides centralized subject…, Performance metrics for NATS Subject Manager operations. This module provides…, Predefined subject patterns for MythosMUD chat system. This module contains all…, get_chat_subscription_patterns() (+36 more)

### Community 316 - "NATS Code Review"
Cohesion: 0.38
Nodes (7): NATS Anti-Patterns Review 2026-01-13, NATS Sync Ops in Async Handlers, NATS Connection Pooling, NATS Code Review, NATS Manual Acknowledgment, NATS Complete Remediation Summary, NATS Remediation Complete

### Community 317 - "AliasGraph"
Cohesion: 0.09
Nodes (22): Unit tests for alias_graph utilities. Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+14 more)

### Community 318 - "ChatHistoryPanel.tsx"
Cohesion: 0.09
Nodes (26): ChatMessage(), ChatMessageProps, formatTimestamp(), getFontSizeClass(), getMessageClass(), ChatMessagesList(), ChatMessagesListProps, ChatHistoryMessageRow() (+18 more)

### Community 319 - "realtime/realtime.py"
Cohesion: 0.18
Nodes (22): ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD. This module defines…, Presence statistics for connection monitoring. This model represents aggregate…, Session statistics for connection monitoring. This model represents aggregate…, Error statistics for connection monitoring. This model represents aggregate…, SessionStatistics (+14 more)

### Community 321 - "SchemaValidator"
Cohesion: 0.10
Nodes (18): create_validator(), Any, Path, Shared schema validator for room definition files. This module provides JSON…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a serialized alias bundle against the alias schema. Args: alias_data:…, Validate emote definition data against the emote schema. Args: emote_data:… (+10 more)

### Community 322 - "TestCheckGracePeriodBlock"
Cohesion: 0.17
Nodes (7): Test _check_grace_period_block function., Test _check_grace_period_block returns None when no connection manager., Test _check_grace_period_block returns None when no player service., Test _check_grace_period_block returns None when player not found., Test _check_grace_period_block returns block result when player in grace period., Test _check_grace_period_block returns None on error., TestCheckGracePeriodBlock

### Community 323 - "test_item.py"
Cohesion: 0.06
Nodes (39): ItemComponentState, ItemInstance, ItemPrototype, Base, Idempotently apply a runtime-only flag override., Per-instance persisted state for modular item components., Convenience helper for composing uniqueness checks in higher layers., Immutable catalog entry describing a canonical item. (+31 more)

### Community 324 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 325 - "Player"
Cohesion: 0.02
Nodes (48): Any, datetime, Player, UUID, Set the instance manager for instanced room lookup (instance-first)., Ensure room cache is loaded (lazy loading with lock). This method uses a lock…, Load rooms from PostgreSQL via RoomCacheLoader., Delegate to room loader; exposed for unit tests. (+40 more)

### Community 326 - "PlayerPositionService"
Cohesion: 0.05
Nodes (60): PlayerPositionService, Any, Player posture coordination service for MythosMUD. As noted in the Pnakotic…, Extract player information for response., Get current position from player stats., Update player position in persistence., Mutate persistence and in-memory tracking to reflect the requested position., Mirror posture changes into the live connection manager. (+52 more)

### Community 327 - "_MagicServiceCore"
Cohesion: 0.10
Nodes (23): _MagicServiceCore, Any, UUID, Check if player is already casting a spell., Get spell from registry by ID or name., Validate spell can be cast and resolve target., Handle instant cast (casting_time == 0)., Calculate next initiative tick for combat casting. In round-based combat,… (+15 more)

### Community 328 - "map_minimap.py"
Cohesion: 0.07
Nodes (41): _append_room_with_fallback_coords_if_needed(), _apply_minimap_fallback_coordinates(), _ensure_current_room_in_minimap_rooms(), generate_minimap_html(), Any, AsyncSession, UUID, Minimap orchestration for the map API. Extracted from maps.py so the router… (+33 more)

### Community 329 - "TestNPCCombatRewards"
Cohesion: 0.08
Nodes (20): asyncio, fixture, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class., Test award_xp_to_killer handles zero XP. (+12 more)

### Community 330 - "send_game_event"
Cohesion: 0.08
Nodes (34): Any, UUID, Get MP regeneration multiplier based on player state. Args: stats: Player stats…, Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…, Restore MP from meditation (highly accelerated regeneration). Args: player_id:…, Restore MP from consuming an item. Args: player_id: Player ID amount: Amount of…, Process MP regeneration for a player on a game tick. Args: player_id: Player ID…, broadcast_game_event() (+26 more)

### Community 331 - "Container Looting Scenarios"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 332 - "websocket_handler_commands.py"
Cohesion: 0.03
Nodes (102): create_websocket_request_context(), Factory function to create a WebSocket request context. Args: app_state: Real…, _mirror_service_to_app_state(), WebSocket app.state / container service wiring for command processing.…, Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state. Mutates…, resolve_and_setup_app_state_services() (+94 more)

### Community 333 - "StyleGuideSections.tsx"
Cohesion: 0.07
Nodes (45): Channel, ChannelSelector(), ChannelSelectorProps, useChannelSelectorState(), AllStats(), CommandsCount(), ConnectionStatus(), CORE_ATTRIBUTES (+37 more)

### Community 334 - "look_command.py"
Cohesion: 0.12
Nodes (29): _get_app_and_persistence(), _get_room_drops(), _handle_implicit_target_lookup(), handle_look_command(), Any, Look command for MythosMUD. This module handles the look command for examining…, Try to handle explicit player look., Try to handle explicit item look. (+21 more)

### Community 335 - "utils/layout.ts"
Cohesion: 0.10
Nodes (36): UseMapLayoutOptions, applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyLinkForces() (+28 more)

### Community 336 - "multiplayer-browser-helpers.js"
Cohesion: 0.14
Nodes (30): buttonHasLoginSubmitLabel(), captureGameUiDiagnosticsInBrowser(), captureOccupantsSnapshotInBrowser(), computedStyleHidesElement(), elementShowsConnectedStatus(), elementTextIncludesGameInfo(), evaluateGameUiLoaded(), fieldHasCommandPlaceholder() (+22 more)

### Community 337 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.06
Nodes (31): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI SUCCESS METRICS, 🔧 COMMON FIX TEMPLATES, Component Rendering Issues, 🔴 CRITICAL (Fix First - Blocking Issues), 🔴 CRITICAL FIXES - TypeScript Errors, For Each Failure Category (+23 more)

### Community 338 - "Structured Error Logging"
Cohesion: 0.50
Nodes (4): MythosMUDError Hierarchy, Structured Error Logging, log_and_raise Utilities, Test/Production Environment Separation

### Community 339 - "emotes.schema.json"
Cohesion: 0.06
Nodes (31): additionalProperties, additionalProperties, properties, required, type, items, type, uniqueItems (+23 more)

### Community 340 - "PatternNotFoundError"
Cohesion: 0.10
Nodes (28): InvalidPatternError, MissingParameterError, NATSSubjectError, PatternNotFoundError, Exception, Base exception for NATS subject-related errors., Exception raised when a pattern name is not found in registry., Exception raised when required parameters are missing. (+20 more)

### Community 341 - "hallucinations.py"
Cohesion: 0.05
Nodes (43): FakeHallucinationService, Any, UUID, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Select which type of fake hallucination to trigger (50/50 chance). Returns:…, Service for generating fake NPC tells and room text overlays. These…, Initialize the fake hallucination service., Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will… (+35 more)

### Community 342 - "WebSocket Handler Tests"
Cohesion: 0.09
Nodes (31): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test validating message with path traversal pattern., Test validating message with javascript: URL., Test validating message with event handler. (+23 more)

### Community 343 - "message_handler_factory.py"
Cohesion: 0.06
Nodes (52): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, MessageHandlerFactory, PartyInviteResponseMessageHandler, PingMessageHandler (+44 more)

### Community 344 - "generate_sql.mjs"
Cohesion: 0.25
Nodes (8): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Static Data SQL Generation, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 345 - "test_world.py"
Cohesion: 0.05
Nodes (41): Unit tests for world models. Tests the Zone, Subzone, RoomModel, RoomLink, and…, Test Subzone can have None for optional fields., Test Subzone has correct table name., Test Subzone __repr__ method., Test RoomModel can be instantiated with required fields., Test RoomModel can have attributes dictionary., Test RoomModel has correct table name., Test RoomModel __repr__ method. (+33 more)

### Community 346 - "roomHandlers.ts"
Cohesion: 0.14
Nodes (28): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+20 more)

### Community 347 - "Enhanced Logging Migration Complete"
Cohesion: 0.67
Nodes (3): Enhanced Logging Implementation Complete, Enhanced Logging Implementation Summary, Enhanced Logging Migration Complete

### Community 350 - "HealthService"
Cohesion: 0.09
Nodes (23): HealthStatus, HealthComponents, Health status for all system components., HealthService, Any, Async database health check., check_database_health., Check connection manager health. (+15 more)

### Community 351 - "combat_attack.py"
Cohesion: 0.08
Nodes (39): _execute_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution. Extracted from combat.py to…, Resolve damage from equipped weapon or fall back to config unarmed damage., Execute combat action using the proper combat service., Handle attack commands (attack, punch, kick, etc.)., Validate target name, load player/room, check DP and no_combat. Returns… (+31 more)

### Community 353 - "test_magic_commands.py"
Cohesion: 0.03
Nodes (103): MagicCommandHandler, Any, Exception, Resolve player and spell parameters for a cast; returns error message if…, Build the response payload for a cast result and send announcements., Build the final success message for a cast spell., Handle /spells command - list learned spells. Args: command_data: Command data…, Handle /spell command - show spell details. (+95 more)

### Community 354 - "PlayerRepositoryProtocol"
Cohesion: 0.07
Nodes (24): PlayerRepositoryProtocol, datetime, Player, Protocol, Room, UUID, Repository protocols for MythosMUD persistence layer. Explicit typing.Protocol…, List all cached rooms. (+16 more)

### Community 355 - "Test Coverage Gaps"
Cohesion: 0.67
Nodes (3): Disconnect Grace Period Rest Coverage, Test Coverage Gaps, Coverage Gap Priority Matrix

### Community 356 - "MovementMonitor"
Cohesion: 0.08
Nodes (22): get_movement_monitor(), MovementMonitor, Any, UUID, Movement monitoring and validation system for MythosMUD. This module provides…, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms. (+14 more)

### Community 357 - "test_connection_cleaner.py"
Cohesion: 0.06
Nodes (39): CleanupContext, Context for periodic cleanup checks. Groups parameters to stay under param-…, connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue() (+31 more)

### Community 358 - "test_event_publisher.py"
Cohesion: 0.07
Nodes (35): event_publisher(), mock_nats_service(), mock_subject_manager(), asyncio, fixture, Unit tests for event publisher. Tests the EventPublisher class., Test publish_game_tick_event() when NATS is not connected., Test get_next_sequence_number() returns and increments sequence. (+27 more)

### Community 359 - "useMythosAppState.ts"
Cohesion: 0.05
Nodes (52): MechanicalEffect, Profession, ProfessionCard(), ProfessionCardProps, StatRequirement, ProfessionSelectionContentProps, ProfessionSelectionScreen(), ProfessionSelectionScreenProps (+44 more)

### Community 360 - "RoomCacheLoader"
Cohesion: 0.20
Nodes (5): Any, BaseException, Loads room data from the database and populates a room cache dict. Used by…, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 361 - "admin_teleport_commands.py"
Cohesion: 0.03
Nodes (117): Any, Admin permission validation utilities for MythosMUD. This module provides…, Validate that a player has admin permissions. Args: player: Player object to…, validate_admin_permission(), _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args() (+109 more)

### Community 362 - "UUID"
Cohesion: 0.09
Nodes (21): Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send…, Get list of occupants in a room. Args: room_id: The room ID online_players:… (+13 more)

### Community 363 - "test_maps.py"
Cohesion: 0.11
Nodes (36): _MapRooms, _apply_exploration_filter_if_needed(), _CoordGenCtx, _ensure_coordinates_generated(), _filter_explored_rooms(), _get_current_room_id(), _get_player_and_exploration_service(), _needs_coordinate_generation() (+28 more)

### Community 364 - "Three-Column Game UI Layout"
Cohesion: 0.29
Nodes (7): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe

### Community 365 - "worktree-ops.py"
Cohesion: 0.22
Nodes (17): get_current_worktree(), get_project_root(), install_dependencies(), main(), Run linting (worktree-aware), Determine the project root based on current working directory, Run formatting (worktree-aware), Show worktree and project status (+9 more)

### Community 366 - "e2e-bootstrap.ts"
Cohesion: 0.15
Nodes (27): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+19 more)

### Community 367 - "CORSConfig"
Cohesion: 0.10
Nodes (18): CORSConfig, Any, BaseSettings, field_validator, model_validator, Parse comma-separated string into cleaned list., Parse comma separated strings or lists into a cleaned list of strings., Parse allowed origins from various input formats. (+10 more)

### Community 368 - "MonitoringPanel.tsx"
Cohesion: 0.12
Nodes (23): ConnectionHealthStats(), DualConnectionStats(), formatNumber(), formatPercentage(), formatTime(), loadMonitoringSnapshot(), MonitoringData, MonitoringPanel() (+15 more)

### Community 369 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 370 - "test_command_exploration.py"
Cohesion: 0.07
Nodes (34): LookCommand, field_validator, Command for looking around, in a specific direction, or at an NPC., Validate direction is one of the allowed values., Validate direction is one of the allowed values., Unit tests for exploration command models. Tests the LookCommand and GoCommand…, Test GoCommand validates valid direction., Test GoCommand rejects invalid direction. (+26 more)

### Community 371 - "TestUtilityFunctions"
Cohesion: 0.15
Nodes (11): connect_postgres(), convert_sqlite_to_postgres_query(), Create a PostgreSQL connection. Args: database_url: PostgreSQL connection URL…, Convert legacy SQLite query syntax to PostgreSQL syntax. Note: This function is…, Test utility functions., Test connect_postgres()., Test connect_postgres() with driver prefix., Test convert_sqlite_to_postgres_query() basic conversion. (+3 more)

### Community 372 - "Any"
Cohesion: 0.15
Nodes (7): Any, Handle an incoming event and trigger appropriate NPC reactions. Args: event:…, Get context information for an NPC. This method attempts to get actual NPC…, Get statistics about an NPC's reactions. Args: npc_id: The ID of the NPC…, Initialize an NPC event reaction. Args: event_type: The type of event this…, Check if this reaction should trigger for the given event. Args: event: The…, Execute the reaction action. Args: event: The event that triggered the reaction…

### Community 373 - "AuditLogger"
Cohesion: 0.07
Nodes (31): Unit tests for audit_logger utilities. Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries., test_audit_logger_get_recent_entries(), test_audit_logger_init() (+23 more)

### Community 374 - "command_handler_unified.py"
Cohesion: 0.06
Nodes (54): check_alias_safety(), handle_expanded_command(), Any, CommandExecutionRequest, Handle command processing with alias expansion and loop detection. This…, Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:…, validate_expanded_command() (+46 more)

### Community 375 - "test_command_base.py"
Cohesion: 0.06
Nodes (35): Unit tests for base command models and enums. Tests the Direction and…, Test CommandType enum contains combat commands., Test CommandType enum contains magic commands., Test CommandType enum values can be compared to strings., Test BaseCommand can be instantiated (though it's abstract)., Test BaseCommand rejects unknown fields (extra='forbid')., Test BaseCommand has correct model configuration., Test BaseCommand has __slots__ defined. (+27 more)

### Community 376 - "test_movement_monitor.py"
Cohesion: 0.04
Nodes (56): movement_monitor(), fixture, Unit tests for movement monitor. Tests the MovementMonitor class for monitoring…, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data., Test validate_room_integrity() detects duplicate players., Test validate_room_integrity() handles empty rooms dict. (+48 more)

### Community 377 - "validate_calendar.py"
Cohesion: 0.18
Nodes (20): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+12 more)

### Community 378 - "shutdown_sequence.py"
Cohesion: 0.17
Nodes (20): Schedule a best-effort graceful process termination after a short delay. This…, schedule_process_termination(), _cancel_background_tasks(), _cleanup_connection_manager(), _despawn_all_npcs(), _disconnect_all_players(), _disconnect_nats_service(), execute_shutdown_sequence() (+12 more)

### Community 379 - "useRoomEditModal.ts"
Cohesion: 0.09
Nodes (14): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, RoomEditFormData, RoomEditModalForm(), RoomEditModalFormProps, RoomEditModalTabs() (+6 more)

### Community 380 - "NPCEventHandler"
Cohesion: 0.05
Nodes (45): NPCEventHandler, Any, Extract spawn_message from behavior_config. Args: behavior_config: The parsed…, Get the spawn message for an NPC from its behavior_config. If no custom spawn…, Get the name of an NPC by ID. Args: npc_id: The NPC ID Returns: NPC name or…, Determine the direction from one room to another by checking room exits. Args:…, Handles all NPC-related real-time events., Get the departure message for an NPC from its behavior_config. If no custom… (+37 more)

### Community 381 - "NATS Subject Manager Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 382 - "hash_password"
Cohesion: 0.06
Nodes (34): hash_password(), Hash a plaintext password using Argon2id. This function provides superior…, Verify a plaintext password against a hash. This function safely handles both…, verify_password(), Test hash_password raises AuthenticationError on AuthenticationError from…, Test hash_password raises AuthenticationError on ValueError., Test hash_password raises AuthenticationError on TypeError., Test hash_password raises AuthenticationError on RuntimeError. (+26 more)

### Community 383 - "debugLogger"
Cohesion: 0.13
Nodes (5): debugLogger, LogConfig, LogEntry, LogLevel, mockConsole

### Community 384 - "UserManagerProtocol"
Cohesion: 0.07
Nodes (11): Protocol for user manager., Mute a channel for a player., Unmute a channel for a player., Check if channel is muted., Mute a player for another player., Unmute a player for another player., Check if player is muted., Check if player is globally muted. (+3 more)

### Community 385 - "NPCStartupService"
Cohesion: 0.17
Nodes (12): _merge_phase_into_startup(), _new_spawn_results(), NPCStartupService, Any, Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…, Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…, Second pass: spawn one instance per definition (that was spawned in…, Determine the appropriate room for spawning an NPC. Args: npc_def: NPC… (+4 more)

### Community 386 - "real_time.py"
Cohesion: 0.10
Nodes (40): _ensure_connection_manager(), _extract_bearer_token(), get_connection_statistics(), get_player_connections(), handle_new_game_session(), _parse_subprotocol_token(), _parse_websocket_token(), Any (+32 more)

### Community 387 - "Migration Strategy"
Cohesion: 0.08
Nodes (25): Access Patterns, App.State to Dependency Injection Migration Plan, Current State Analysis, Dependencies, Dependency Injection Pattern, Estimated Effort, Implementation Guidelines, Migration Strategy (+17 more)

### Community 388 - "ChatPoseManager"
Cohesion: 0.08
Nodes (16): ChatPoseManager, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…, Get a player's current pose. Args: player_id: ID of the player Returns: Current…, Clear a player's pose. Args: player_id: ID of the player Returns: True if pose…, Get all poses (for testing/debugging). Returns: Dictionary mapping player IDs… (+8 more)

### Community 389 - "get_cached_player"
Cohesion: 0.13
Nodes (23): Unit tests for player_cache utilities. Tests the player caching functions for…, Test get_cached_player() returns None when no cache exists., Test cache_player() and get_cached_player() operations., Test get_cached_player() returns None for nonexistent key., Test cache_player() can cache multiple players., Test cache_player() overwrites existing entries., Test get_cached_player() handles missing state., Test cache_player() handles missing state gracefully. (+15 more)

### Community 390 - "devDependencies"
Cohesion: 0.05
Nodes (41): devDependencies, cross-env, @eslint/js, eslint-plugin-playwright, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, jsdom (+33 more)

### Community 391 - "TestCombatConfigurationService"
Cohesion: 0.05
Nodes (23): fixture, Test suite for CombatConfigurationService class., Create a mock config object., Create a CombatConfigurationService instance for testing., Test CombatConfigurationService initialization., Test get_combat_configuration returns configuration., Test get_combat_configuration caches configuration., Test get_combat_configuration_for_scope with global scope. (+15 more)

### Community 392 - "test_communication_commands_flows.py"
Cohesion: 0.04
Nodes (105): _chat_send_with_room_bundle(), _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_global_command(), flow_local_command(), flow_reply_command(), flow_say_command(), flow_system_command() (+97 more)

### Community 393 - "test_quest_service_collect.py"
Cohesion: 0.13
Nodes (27): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in… (+19 more)

### Community 394 - "retry.py"
Cohesion: 0.08
Nodes (36): F, asyncio, Unit tests for retry utilities. Tests the retry decorator and retry logic., Test is_transient_error() identifies transient errors., Test is_transient_error() returns False for non-transient errors., Test retry_with_backoff() succeeds on first attempt., Test retry_with_backoff() retries on failure then succeeds., Test retry_with_backoff() with async function succeeds on first attempt. (+28 more)

### Community 395 - "Any"
Cohesion: 0.07
Nodes (23): Any, Task, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task…, Cancel specific task with logical timeout boundaries. Args: task: Task…, Metadata for tracked asyncio.Tasks. (+15 more)

### Community 396 - "test_health_monitor.py"
Cohesion: 0.09
Nodes (29): health_monitor(), mock_cleanup_dead_websocket(), mock_is_websocket_open(), mock_performance_tracker(), mock_validate_token(), asyncio, fixture, Unit tests for health monitor. Tests the HealthMonitor class. (+21 more)

### Community 397 - "CommandPanel.tsx"
Cohesion: 0.10
Nodes (17): CommandPanel(), CommandPanelProps, logCommandPanelConnectionDebug(), prepareCommandForSubmit(), prependChannelShortcut(), prependPartyPrefix(), STANDALONE_COMMANDS, useCommandPanelEffects() (+9 more)

### Community 398 - "inventory_pickup_command.py"
Cohesion: 0.05
Nodes (68): _DropResolved, _FloorPickupResolved, Parse numeric fields from object-typed JSON command payloads., Protocol, Shared types for inventory command handlers (Lizard: keep main module small)., Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, build_and_broadcast_inventory_event() (+60 more)

### Community 399 - "Emote Schema Definition"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 401 - "performance.test.tsx"
Cohesion: 0.06
Nodes (28): ChatPanel(), ChatPanelRuntimeView(), ChatPanelRuntimeViewInner(), Channel, ChannelSelectorProps, TerminalButtonProps, TerminalInputProps, Channel (+20 more)

### Community 402 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 404 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 405 - "test_room_occupant_manager.py"
Cohesion: 0.09
Nodes (29): mock_connection_manager(), occupant_manager(), asyncio, fixture, Unit tests for room occupant manager. Tests the RoomOccupantManager class for…, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test get_room_occupants handles get_players error. (+21 more)

### Community 406 - "test_lru_cache.py"
Cohesion: 0.07
Nodes (27): cache_with_ttl(), cache_without_ttl(), asyncio, fixture, Unit tests for LRU cache expiration and eviction. Tests the LRUCache class,…, Test that expired entry count is tracked in cache stats., Test that expiration rate is calculated in stats., Test that cache size stays within bounds after expiration cleanup. (+19 more)

### Community 407 - "ValidationRule"
Cohesion: 0.09
Nodes (15): ABC, Base validation rule class. This module defines the abstract base class for all…, Create a validation error for this rule. Args: room_id: Room ID where error…, Represents a validation error with metadata. As documented in the restricted…, Create a validation warning for this rule. Args: room_id: Room ID where warning…, Get information about this rule. Returns: Dictionary with rule information, Initialize a validation error. Args: rule_name: Name of the rule that generated…, Convert error to dictionary format. (+7 more)

### Community 408 - "test_player_preferences_service.py"
Cohesion: 0.02
Nodes (111): mock_session(), preferences_service(), asyncio, fixture, Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID. (+103 more)

### Community 409 - "npc_database.py"
Cohesion: 0.09
Nodes (33): close_npc_db(), ensure_npc_database_directory(), get_npc_database_path(), get_npc_engine(), get_npc_session(), get_npc_session_maker(), init_npc_db(), _initialize_npc_database() (+25 more)

### Community 410 - "stateNormalization.ts"
Cohesion: 0.11
Nodes (26): createInitialState(), createSessionActions(), SessionActions, SessionSelectors, SessionState, SessionStore, touchActivity(), useSessionStore (+18 more)

### Community 412 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 413 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 414 - "RespawnPlayerEventPayload"
Cohesion: 0.09
Nodes (19): Player, UUID, Update connection manager's in-memory position state. As documented in…, Resolve posture string from player stats JSON., Build client-expected player payload for respawn events., Get updated player data for respawn event. As documented in "Resurrection and…, Send respawn event with retry logic to handle temporary connection…, Build respawn player payload from connection-manager player when persistence… (+11 more)

### Community 415 - "_str_id"
Cohesion: 0.14
Nodes (14): UUID, Add a player to a party. Fails if party does not exist or player is already in…, Remove expired pending invites and notify inviters., Send a command_response-style message to a single player., Create a pending party invite and send party_invite event to target. Target…, Normalize ID to string for dict keys and membership sets., Accept a party invite. Target is the player who accepted (the invitee)., Decline a party invite. (+6 more)

### Community 416 - "NATSConnectionStateMachine"
Cohesion: 0.03
Nodes (92): ConnectionEvent, NATSConnectionStateMachine, Enum, Exception, Connection state machine for NATS messaging. Implements a robust state machine…, Initialize connection state machine. Args: connection_id: Unique identifier for…, Handler for connect transition. Resets reconnection counter and prepares for…, Handler for successful connection. Records connection time and increments… (+84 more)

### Community 417 - "LucidityRepository"
Cohesion: 0.11
Nodes (16): LucidityRepository, AsyncSession, datetime, UUID, Set or update cooldown for a player and action., Delete all cooldowns for a player matching an action code pattern., Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE., Data-access helpers for lucidity persistence. (+8 more)

### Community 418 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 419 - "teach_command.py"
Cohesion: 0.21
Nodes (15): _format_teach_result(), _get_teach_services(), handle_teach_command(), Any, Teach command handler for learning spells from NPC teachers. This module…, Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, _resolve_npc_teacher(), asyncio (+7 more)

### Community 420 - "test_who_commands.py"
Cohesion: 0.03
Nodes (110): Utility commands for MythosMUD. This module contains handlers for utility…, filter_online_players(), filter_players_by_name(), format_player_entry(), format_player_location(), format_who_result(), get_players_for_who(), handle_who_command() (+102 more)

### Community 421 - "test_command_factories_combat.py"
Cohesion: 0.07
Nodes (28): Unit tests for combat command factories. Tests the CombatCommandFactory class…, Test create_attack_command() creates AttackCommand., Test create_attack_command() allows None target (validation happens later)., Test create_punch_command() creates PunchCommand., Test create_punch_command() allows None target (validation happens later)., Test create_kick_command() creates KickCommand., Test create_kick_command() allows None target (validation happens later)., Test create_strike_command() creates StrikeCommand. (+20 more)

### Community 422 - "Advanced Chat Channels Specification"
Cohesion: 0.40
Nodes (5): Advanced Chat Channels Specification, Global Chat Channel, Local Chat Channel, Advanced Chat Channels Tasks, Whisper Chat Channel

### Community 423 - "test_chat_logger.py"
Cohesion: 0.05
Nodes (35): Initialize the rate limiter with configuration-based limits., _get_proper_data_dir(), Path, Get the proper environment-aware data directory for user management. Uses…, Initialize the user manager. Args: data_dir: Directory for player-specific mute…, chat_logger(), fixture, Unit tests for chat logger service. Tests the ChatLogger class for structured… (+27 more)

### Community 424 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 425 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 426 - "testing_examples.py"
Cohesion: 0.04
Nodes (47): async_operation(), client, database, LoggingMiddleware, process_batch(), process_item(), asyncio, Test WebSocket logging in integration tests. (+39 more)

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

### Community 432 - "designTokens.ts"
Cohesion: 0.15
Nodes (19): animations, borderRadius, breakpoints, buildClasses, ButtonVariant, colors, ColorVariant, ComponentSize (+11 more)

### Community 433 - "format_metadata"
Cohesion: 0.09
Nodes (31): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+23 more)

### Community 434 - "log_with_context"
Cohesion: 0.08
Nodes (32): Resolve an alert. Args: alert_id: ID of the alert to resolve Returns: True if…, log_with_context(), BoundLogger, Log a message with the current context automatically included. Args:…, create_logged_http_exception_enhanced(), log_and_raise_http_enhanced(), _log_http_error(), log_performance_metric() (+24 more)

### Community 435 - "Communities (19 total, 4 thin omitted)"
Cohesion: 0.07
Nodes (26): Ambiguous Edges - Review These, Communities (19 total, 4 thin omitted), Community 0 - "Yog-Sothoth Keeper Decks", Community 10 - "Tsathoggua Formless Spawn", Community 11 - "Ygolonac and Xiclotl", Community 12 - "Nyogtha Spawn", Community 13 - "Hastur Spawn", Community 14 - "Fthagghua Fire Vampires" (+18 more)

### Community 436 - "projectorRoom.ts"
Cohesion: 0.09
Nodes (46): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), messageHandlers, ProjectorHandler, stateHandlers, appendMessage() (+38 more)

### Community 437 - "security.ts"
Cohesion: 0.06
Nodes (41): SafeHtml(), SafeHtmlProps, fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler, collectWindowCandidates(), COMMAND_PROBE_CONFIG (+33 more)

### Community 438 - "generate_html_visualization.py"
Cohesion: 0.13
Nodes (22): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+14 more)

### Community 439 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 440 - "reset_config"
Cohesion: 0.07
Nodes (30): _is_test_mode(), Reset the configuration cache. In test mode, this is a no-op since get_config()…, Detect if running in test environment. Uses multiple detection methods to…, reset_config(), Unit tests for config module initialization., Test that get_config() returns fresh instances in test mode., Test that reset_config() works in test mode., Test that config has server configuration. (+22 more)

### Community 441 - "channel_broadcasting_strategies.py"
Cohesion: 0.19
Nodes (12): ChannelBroadcastingStrategy, GlobalChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for whisper channel broadcasting., Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy. Args: channel_type: Type of…, Abstract base class for channel broadcasting strategies. (+4 more)

### Community 442 - "Migration 019 Ready for Deployment"
Cohesion: 0.67
Nodes (3): Migration 019 Complete Summary, Migration 019 Ready for Deployment, Migration 019 Testing Guide

### Community 443 - "players.py"
Cohesion: 0.03
Nodes (121): create_player(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), _force_disconnect_character(), get_available_classes(), get_class_description(), _get_connection_manager() (+113 more)

### Community 444 - "test_flee_command.py"
Cohesion: 0.10
Nodes (36): flee_handler_deps(), _FleeCmdApp, _FleeCmdAppState, _FleeCmdRequest, FleeHandlerDeps, _GetCombatHandlerLoaderApp, _GetCombatHandlerLoaderAppState, _GetCombatHandlerLoaderContainer (+28 more)

### Community 445 - "test_command_alias.py"
Cohesion: 0.09
Nodes (29): AliasCommand, Command for creating or viewing command aliases., Unit tests for alias command models. Tests the alias command models and their…, Test UnaliasCommand requires alias_name., Test UnaliasCommand calls validate_alias_name., Test UnaliasCommand validates alias_name min length., Test UnaliasCommand validates alias_name max length., Test AliasCommand requires alias_name. (+21 more)

### Community 447 - "asyncio"
Cohesion: 0.05
Nodes (37): asyncio, Test is_player_muted_async() returns True when player is muted., Test is_player_muted_async() returns False when player is not muted., Test add_admin() handles missing container., Test add_admin() handles missing persistence., Test add_admin() handles player not found., Test remove_admin() handles missing container., Test remove_admin() handles missing persistence. (+29 more)

### Community 448 - "EmoteService"
Cohesion: 0.09
Nodes (18): EmoteDefinition, _EmoteLoadResult, _EmoteRowData, EmoteService, _get_emote_validator(), TypedDict, Async helper to load emotes from PostgreSQL database., Check if a command is an emote alias. Args: command: The command to check… (+10 more)

### Community 449 - "websocket_handler.py"
Cohesion: 0.06
Nodes (45): get_message_validator(), Get the global message validator instance., handle_json_decode_error(), handle_message_loop_exception(), handle_websocket_disconnect(), handle_websocket_generic_exception(), handle_websocket_message_loop(), handle_websocket_runtime_error() (+37 more)

### Community 450 - "SkillAssignmentScreen.tsx"
Cohesion: 0.07
Nodes (34): buildCreateCharacterPayload(), CharacterNameScreen(), CharacterNameScreenProps, CreateCharacterPayload, OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, MotdContent() (+26 more)

### Community 451 - "correct_patterns.py"
Cohesion: 0.05
Nodes (35): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+27 more)

### Community 452 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 453 - "ContainerFactoryOptions"
Cohesion: 0.08
Nodes (19): ContainerFactoryOptions, Any, datetime, field_validator, TypedDict, UUID, Validate that metadata does not contain personal information (COPPA…, Validate and convert lock_state to enum. (+11 more)

### Community 454 - "Process Scope NATS Scripts"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 455 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 456 - "connection_manager.py"
Cohesion: 0.03
Nodes (119): delegate_game_state_provider(), delegate_personal_message_sender_sync(), Generic delegate for game state provider methods. Args: game_state_provider:…, Generic delegate for synchronous personal message sender methods. Args:…, broadcast_global_event_impl(), broadcast_global_impl(), broadcast_room_event_impl(), broadcast_to_room_impl() (+111 more)

### Community 457 - "test_population_control.py"
Cohesion: 0.01
Nodes (192): _population_allows_spawn(), Any, Spawn Validator Module. This module provides logic for validating whether NPCs…, Determine if an NPC should spawn based on conditions. Args: definition: NPC…, Return False when zone population blocks this NPC definition., Evaluate one spawn rule; return True when probability roll succeeds., Return True when any spawn rule passes probability checks., should_spawn_npc() (+184 more)

### Community 458 - "Dependency Upgrade Strategy"
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

### Community 462 - "CombatConfiguration"
Cohesion: 0.09
Nodes (17): CombatConfiguration, Combat configuration data class., Validate configuration and return list of errors., Test validate catches XP multiplier too high., Test validate catches alert threshold out of range., Test validate catches max participants out of range., Test suite for CombatConfiguration dataclass., Test CombatConfiguration initialization with defaults. (+9 more)

### Community 463 - "GameTerminal.tsx"
Cohesion: 0.06
Nodes (39): buildHealthStatus(), ChatMessage, formatPosture(), GameTerminal(), Player, Room, IncapacitatedBanner, IncapacitatedBannerProps (+31 more)

### Community 464 - "build_event"
Cohesion: 0.02
Nodes (102): CombatMessages, build_event(), _get_next_global_sequence(), Protocol, UUID, Event envelope utilities for MythosMUD real-time messages. Provides a single,…, Minimal typing for connection_manager passed to build_event (see…, Custom JSON encoder that handles UUID objects. (+94 more)

### Community 465 - "datetime"
Cohesion: 0.14
Nodes (9): datetime, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired channel mutes., Clean up expired global mutes., Clean up expired mutes from all storage., Get active player mutes for a player. (+1 more)

### Community 466 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from…, Unit tests for connection utils. Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 467 - "format_message_content"
Cohesion: 0.11
Nodes (25): format_message_content(), Format message content based on channel type and sender name. Args: channel:…, Unit tests for message formatters. Tests the message_formatters module…, Test format_message_content() formats 'say' channel messages., Test format_message_content() formats 'local' channel messages., Test format_message_content() formats 'global' channel messages., Test format_message_content() formats 'emote' channel messages., Test format_message_content() formats 'pose' channel messages. (+17 more)

### Community 468 - "GameClientV2.tsx"
Cohesion: 0.04
Nodes (71): GameTerminalProps, formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, eventHandlers, processGameEvent(), hoisted (+63 more)

### Community 469 - "TestVerificationSqlUsersPlayers"
Cohesion: 0.10
Nodes (12): PostgreSQL-focused tests for verification and maintenance SQL scripts.…, Tests for db/verification/users_players.sql alignment with current schema., Verification SQL file must exist., Verification SQL must not reference staging tables or select obsolete columns., Verification SQL must use explicit join syntax for multi-table queries., Verification SQL must reference users and players tables., Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)., NPC name constraint script must exist. (+4 more)

### Community 470 - "MythosPanel.tsx"
Cohesion: 0.10
Nodes (27): appendCommands(), CommandCategories(), CommandPanelTest(), COMMAND_CATEGORIES, DEFAULT_COMMAND_HISTORY, EXAMPLES, FEATURES, MOVEMENT_COMMANDS (+19 more)

### Community 471 - "CombatDPSync"
Cohesion: 0.14
Nodes (13): CombatDPSync, Any, UUID, Get persistence layer from application container. Args: player_id: Player ID…, Verify that player DP was successfully saved to database. Args: persistence:…, Log death threshold events based on DP changes. Args: current_dp: New current…, Update player DP and save to database. Args: persistence: Persistence layer…, Synchronously persist player DP to database. This is the actual persistence… (+5 more)

### Community 472 - "NATSRetryHandler"
Cohesion: 0.04
Nodes (75): NATSRetryHandler, Any, Exception, Calculate exponential backoff delay with jitter. Args: attempt: Current attempt…, Determine if a message should be retried. Args: message: Message that failed…, Retry a function with exponential backoff. Args: func: Async function to retry…, Get retry statistics. Returns: Dictionary with retry metrics AI: For monitoring…, Retry async function with exponential backoff. Attempts the function up to… (+67 more)

### Community 473 - "Logout Error Scenarios"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 474 - "test_player_related_models.py"
Cohesion: 0.07
Nodes (29): Unit tests for Player-related SQLAlchemy models. Tests…, Test PlayerInventory has correct table name., Test PlayerInventory __repr__ method., Test PlayerExploration can be instantiated with required fields., Test PlayerExploration has correct table name., Test PlayerExploration __repr__ method., Test PlayerChannelPreferences can be instantiated with required fields., Test PlayerExploration can track multiple rooms for same player. (+21 more)

### Community 475 - "test_inventory_mutation_guard.py"
Cohesion: 0.07
Nodes (29): guard(), asyncio, fixture, Unit tests for inventory mutation guard - core functionality. Tests…, Test acquire_async without token allows mutation., Test acquire_async with unique token allows mutation., Test acquire_async with duplicate token suppresses mutation., Test acquire_async allows same token for different players. (+21 more)

### Community 476 - "container_helpers_inventory_display.py"
Cohesion: 0.18
Nodes (15): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+7 more)

### Community 477 - "mock_container"
Cohesion: 0.11
Nodes (25): mock_connection_manager(), mock_container(), fixture, Create mock connection manager., Create mock container., _assign_container_get_instance(), Test _determine_spawn_room() uses NPC's room_id when available., Test _determine_spawn_room() uses sub_zone default when room_id not available. (+17 more)

### Community 478 - "static_data/package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 479 - "NPCCombatLucidity"
Cohesion: 0.05
Nodes (46): ActiveLucidityService, EncounterProfile, LucidityActionError, AsyncSession, datetime, RuntimeError, Active LCD adjustment helpers for encounters and recovery rituals., Base error for lucidity action operations. (+38 more)

### Community 480 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.11
Nodes (19): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases (+11 more)

### Community 481 - "ADR-012: python-statemachine for Backend Connection FSM"
Cohesion: 0.11
Nodes (18): ADR-012: python-statemachine for Backend Connection FSM, Consequences, Considered Options, Context and Problem Statement, Decision Drivers, Decision Outcome, Implementation Details, Integration with NATS Service (+10 more)

### Community 482 - "TypeScript Compiler Config"
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

### Community 487 - "E2E Multiplayer Findings"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 488 - "useGameTerminal.ts"
Cohesion: 0.09
Nodes (33): GameTerminalContainer(), createDefaultGameTerminalState(), useGameTerminalMock, GameTerminalContext, GameTerminalContextType, GameTerminalProvider(), GameTerminalProviderProps, useConnectionState() (+25 more)

### Community 489 - "test_inventory_mutation_guard_internal.py"
Cohesion: 0.09
Nodes (25): guard(), asyncio, fixture, Unit tests for inventory mutation guard - internal helper methods. Tests…, Test _cleanup_async_state removes empty state., Test _prune_tokens_async removes expired tokens., Test _prune_tokens_async with token_ttl=0 doesn't prune., Test _enforce_limit_async removes oldest tokens when limit exceeded. (+17 more)

### Community 490 - "PostgresConnection"
Cohesion: 0.08
Nodes (18): PostgresConnection, connection, Commit the current transaction., Rollback the current transaction., Close the connection., PostgreSQL connection wrapper for persistence layer operations., Test PostgresConnection initialization., Test PostgresConnection.execute(). (+10 more)

### Community 491 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, type, minLength, type, minLength, type, properties (+10 more)

### Community 492 - "get_cache_manager"
Cohesion: 0.09
Nodes (16): get_cache_manager(), Get the global cache manager instance. Returns: The global cache manager…, Any, Collect event metrics from EventBus. Returns: Dictionary with event metrics, Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics, Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics, Collect NATS subscription metrics from NATSService. Returns: Dictionary with…, Calculate growth rate for a single metric. Args: current: Current metrics… (+8 more)

### Community 493 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 494 - "Alertmanager Monitoring Stack"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 495 - "handle_emote_command"
Cohesion: 0.14
Nodes (22): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+14 more)

### Community 496 - "Any"
Cohesion: 0.11
Nodes (13): Any, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string…, Evaluate boolean conditions and variable lookups. Args: condition: Condition…, Evaluate a condition string against context. Args: condition: Condition string… (+5 more)

### Community 497 - "MessageBroadcaster"
Cohesion: 0.05
Nodes (53): Messaging components for connection management. This package provides modular…, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Message broadcasting for connection management. This module provides room and…, Convert string player IDs to UUIDs for message sending. Args: target_list: List…, Process results from batch message delivery. Args: delivery_results: Results… (+45 more)

### Community 498 - "World Seed Loader"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 499 - "edgeModalLogic.ts"
Cohesion: 0.09
Nodes (30): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+22 more)

### Community 500 - "React Node Upgrade Analyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 501 - "test_combat_flee_helpers.py"
Cohesion: 0.10
Nodes (28): _get_flee_room_id(), Ensure room exists and has exits; return (room_id, None) or (None, error_dict)., Resolve combat, room, exits, and movement service for flee. Returns (combat,…, _validate_flee_combat_and_room(), _participant(), asyncio, UUID, Unit tests for server.commands.combat_flee module-level helpers (not full /flee… (+20 more)

### Community 502 - "fastapi_integration.py"
Cohesion: 0.05
Nodes (38): add_request_context(), auth_service(), BackgroundTasks, create_player(), File, general_exception_handler(), get_current_user(), get_player() (+30 more)

### Community 503 - "logger.ts"
Cohesion: 0.06
Nodes (39): useGameConnectionManagement(), ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach() (+31 more)

### Community 504 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 505 - "HolidayService"
Cohesion: 0.11
Nodes (18): HolidayEntry, Single holiday definition loaded from data/<env>/calendar/holidays.json., _ensure_utc(), HolidayService, datetime, Update the active holiday window for the provided Mythos timestamp., Return currently active holiday entries., Get active holidays and serialize them for API responses. This method… (+10 more)

### Community 506 - "Multiplayer Architecture Planning"
Cohesion: 0.25
Nodes (8): Performance Optimization Summary, Alias System Implementation Plan, Chat System Implementation Plan, Planning Completion Summary, Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 507 - "NPCOccupantProcessor"
Cohesion: 0.13
Nodes (15): NPCOccupantProcessor, Any, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Processes NPC occupants for rooms., Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:…, Get lifecycle manager for filtering fallback NPCs. Returns: Lifecycle manager… (+7 more)

### Community 508 - "room_validator/tests/conftest.py"
Cohesion: 0.15
Nodes (18): dead_end_room(), invalid_room_data(), fixture, Pytest configuration and fixtures for room validator tests. Provides test data…, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit. (+10 more)

### Community 509 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.12
Nodes (16): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases (+8 more)

### Community 510 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 511 - "asyncio"
Cohesion: 0.09
Nodes (18): asyncio, Test NPC session management., Test get_npc_session() yields session., Test get_npc_session() rolls back on error during yield., Test get_npc_session() calls init_npc_db() for unit_test databases., Test init_npc_db() function., Test init_npc_db() successfully initializes database., Test init_npc_db() raises ValidationError when engine is None. (+10 more)

### Community 512 - "ADR-003 Dual Event Systems EventBus NATS"
Cohesion: 0.10
Nodes (22): FastAPI-Generated OpenAPI 3.1, API OpenAPI Specification, ADR-001 Layered Architecture Event-Driven, ADR-002 ApplicationContainer DI, ADR-003 Dual Event Systems EventBus NATS, In-Process EventBus, NATS Distributed Messaging, ADR-004 WebSocket-Only Realtime (+14 more)

### Community 513 - "MovementService"
Cohesion: 0.06
Nodes (30): MovementService, Any, Exception, Room, UUID, Validate movement parameters. Returns False if validation fails (same room),…, Resolve player by ID or name and return player object and resolved ID., Get and validate rooms for movement. (+22 more)

### Community 514 - "Linting Complexity Alignment"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 516 - "errorHandler.ts"
Cohesion: 0.14
Nodes (23): handleProfessionsFetchError(), loadProfessions(), parseDetailMessage(), parseProfessionsBody(), parseProfessionsErrorResponse(), SERVER_UNAVAILABLE_PATTERNS, UseProfessionsOptions, UseProfessionsResult (+15 more)

### Community 517 - "test_room_subscription_manager_npcs.py"
Cohesion: 0.09
Nodes (23): asyncio, fixture, Unit tests for room subscription manager NPC helpers. Tests NPC-related helpers…, Test get_room_occupants() includes NPCs from lifecycle manager., Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager…, Create a RoomSubscriptionManager instance., Test _get_npc_name_from_lifecycle_manager gets NPC name., Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found. (+15 more)

### Community 518 - "test_security_headers.py"
Cohesion: 0.05
Nodes (51): MutableHeaders, Any, ASGIApp, Receive, Request, Scope, Send, Backward-compatible dispatch method for BaseHTTPMiddleware interface. This… (+43 more)

### Community 520 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 521 - "RoomCacheService"
Cohesion: 0.04
Nodes (50): bench_room_cache(), _FakePersistence, main(), bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for… (+42 more)

### Community 522 - "Phase 1: Core Separation"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 1: Core Separation, Sub-tasks, Sub-tasks (+8 more)

### Community 523 - "Disconnect Grace Period Design"
Cohesion: 0.29
Nodes (7): Disconnect Grace Period and Rest Command, Rest Command, 30-Second Disconnect Grace Period, ADR-009 Effects System Architecture, LOGIN_WARDED Effect, Effects System ADR and Implementation, Effects System Implementation

### Community 524 - "MythosMUD UI Component Library"
Cohesion: 0.67
Nodes (3): Mythos Terminal Theme Tokens, StatusPanel, MythosMUD UI Component Library

### Community 525 - "player_connection_setup.py"
Cohesion: 0.14
Nodes (24): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions. This module handles the setup tasks when a…, Broadcast a structured entry event to other occupants (excluding the newcomer).… (+16 more)

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
Cohesion: 0.18
Nodes (11): PrototypeRegistry, Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, In-memory registry for validated item prototypes., Load prototypes from a directory of JSON files., main() (+3 more)

### Community 530 - "test_instance_manager.py"
Cohesion: 0.09
Nodes (22): instance_manager(), fixture, Unit tests for InstanceManager. Tests instance creation, destruction, room…, Test get_exit_room_id returns fixed exit room., Test get_room_by_id returns None for non-instance room IDs., Test get_room_by_id returns room when room is in an instance., Create tutorial bedroom template room., Room cache with tutorial template. (+14 more)

### Community 531 - "test_calendar.py"
Cohesion: 0.11
Nodes (24): HolidayModel, NPCScheduleModel, Base, SQLAlchemy models for calendar data (holidays and NPC schedules)., Mythos holidays tracker., Unit tests for calendar models. Tests the HolidayModel and NPCScheduleModel…, Test NPCScheduleModel can have optional notes., Test NPCScheduleModel has correct table name. (+16 more)

### Community 532 - "GameTickService"
Cohesion: 0.05
Nodes (32): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+24 more)

### Community 533 - "LRUCache"
Cohesion: 0.05
Nodes (29): K, CacheManager, LRUCache, Any, Put an item into the cache. Args: key: The key to store value: The value to…, Delete an item from the cache. Args: key: The key to delete Returns: True if…, Clear all items from the cache., Get the current number of items in the cache. (+21 more)

### Community 535 - "TestPathValidator"
Cohesion: 0.10
Nodes (12): fixture, Tests for path validator functionality. Validates room connectivity analysis…, Test detection of mismatched return paths across zones., Test suite for path validation functionality., Create a path validator instance., Sample rooms with zone transitions., Test detection of zone transitions in room connections., Test detection of broken zone transitions. (+4 more)

### Community 536 - "test_event_bus.py"
Cohesion: 0.09
Nodes (21): Unit tests for event bus. Tests the EventBus class., Test publish() raises error for invalid event., Test _ensure_processing_started() calls _ensure_async_processing., Test EventBus.subscribe() with service_id for tracking., Test EventBus.unsubscribe_all_for_service() only removes tracked handlers., Test EventBus.subscribe() adds subscriber., Test EventBus.get_subscriber_stats() returns subscriber statistics., Test EventBus.subscribe() with multiple handlers. (+13 more)

### Community 537 - "server/tests/conftest.py"
Cohesion: 0.10
Nodes (28): Config, Item, _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables(), _get_db_name_from_url(), AbstractEventLoop (+20 more)

### Community 538 - "server/services/__init__.py"
Cohesion: 0.02
Nodes (143): AbstractContextManager, _clone_equipped(), _clone_inventory(), EquipmentCapacityError, EquipmentService, EquipmentServiceError, Any, Exception (+135 more)

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

### Community 543 - "BehaviorEngine"
Cohesion: 0.09
Nodes (19): BehaviorEngine, Deterministic behavior engine for NPCs. This engine evaluates rules based on…, Initialize the behavior engine., Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…, Get the behavior engine for this NPC., Test _evaluate_equality() returns True for matching condition., Test _evaluate_numeric_comparison() raises ValueError for non-numeric values., Test get_applicable_rules() returns matching rules. (+11 more)

### Community 544 - "MessageBatcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 545 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 546 - "schemas/unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 547 - "debrief_command.py"
Cohesion: 0.19
Nodes (18): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+10 more)

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
Cohesion: 0.14
Nodes (13): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Functional Metrics, Overview, Phase Dependencies, Quality Metrics (+5 more)

### Community 552 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "Pandora's Box / Pandora Handout 10", Community 10 - "Chapter 6: Pulp Magic, Psychic Powers, and Weird S / Psychic Powers", Community 1 - "Disintegrator device / Handout: Disintegrator 1", Community 2 - "Chapter 1: The Pulps / Chapter 7: Running Pulp Games", Community 3 - "Avoiding Certain Death / Call of Cthulhu 7th Edition", Community 4 - "Cthulhu Mythos / Deep One", Community 5 - "Seekers of Eternal Wisdom / Handout: Pandora's Box 12" (+12 more)

### Community 553 - "update_container"
Cohesion: 0.10
Nodes (21): Apply item/lock/metadata updates; returns refreshed row or None if missing., update_container(), Test update_container successfully updates container., Test update_container returns None when container not found., Test update_container handles database errors., Test update_container with no updates provided (all None)., test_update_container_database_error(), test_update_container_no_updates() (+13 more)

### Community 554 - "test_look_item.py"
Cohesion: 0.09
Nodes (27): _get_item_description_from_prototype(), Get item description from prototype registry. Returns: Formatted result string…, Unit tests for item look functionality. Tests the helper functions for looking…, Test finding item in equipped items by name., Test finding item in equipped items when not found., Test getting item description from prototype., Test getting item description when prototype registry is None., Test getting item description when prototype_id is missing. (+19 more)

### Community 555 - "ChatPanelRefactoredView.tsx"
Cohesion: 0.20
Nodes (17): ChatHistoryToggle(), ChatStatistics(), ChatPanelRefactored(), ChatPanelRefactoredProps, computeChannelMessages(), computeFilteredMessages(), computeUnreadCounts(), filterNonSystemMessages() (+9 more)

### Community 556 - "ChatLogger"
Cohesion: 0.07
Nodes (25): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+17 more)

### Community 557 - "test_emote.py"
Cohesion: 0.11
Nodes (24): Emote, EmoteAlias, Base, Predefined emote definitions., Aliases for predefined emotes., Unit tests for emote models. Tests the Emote and EmoteAlias SQLAlchemy models., Test EmoteAlias aliases are case sensitive., Test Emote can be instantiated with required fields. (+16 more)

### Community 558 - "Communities (10 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (19): Communities (10 total, 0 thin omitted), Community 0 - "Hotel Hell", Community 1 - "Petersen's Abominations", Community 2 - "Hotel Hell", Community 3 - "Voice on the Phone", Community 4 - "Mohole", Community 5 - "Panacea", Community 6 - "Panacea" (+11 more)

### Community 559 - "_format_npc_description"
Cohesion: 0.10
Nodes (20): _format_npc_description(), Format NPC description with fallback., Test _format_npc_description() returns description from definition., Test _format_npc_description() uses fallback when description is empty., Test _format_npc_description() uses alternative attributes., test_format_npc_description(), test_format_npc_description_fallback(), test_format_npc_description_no_description() (+12 more)

### Community 560 - "npc_config_parsing.py"
Cohesion: 0.07
Nodes (29): Setup base behavior rules common to all NPCs., Return stats[key] as int, or default if missing/None., Return current_dp, max_dp, dexterity for CombatParticipantData., Heal and update determination points (DP)., Write new_dp to determination_points and dp for backward compatibility., Initialize the NPC base class., Get attribute from obj with default to avoid lazy-loading issues., Set npc_type, name, current_room, spawn_room_id from definition. (+21 more)

### Community 561 - "AttributeError"
Cohesion: 0.02
Nodes (210): AttributeError, Event subscription setup for application startup. Extracted from…, Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, subscribe_room_occupants_refresh(), _accumulate_valid_occupant_name(), _AppStateForPlayerService, build_basic_player_data(), check_shutdown_and_reject() (+202 more)

### Community 562 - "NATS Remediation Summary 2026-01-13"
Cohesion: 0.25
Nodes (8): NATS Error Handling Strategy, NATS Manual Acknowledgment Guide, NATS Manual Ack Pattern, NATS Medium Priority Remediation, NATS Critical Fixes Summary, NATS Remediation Summary 2026-01-13, NATS Subject Patterns, NATS Subject Naming Patterns

### Community 563 - "patch"
Cohesion: 0.10
Nodes (16): patch, Test get_npc_engine() uses NullPool for test databases., Test get_npc_database_path() function., Test get_npc_database_path() returns None for PostgreSQL., Test get_npc_database_path() raises for non-PostgreSQL URLs., Test ensure_npc_database_directory() function., Test ensure_npc_database_directory() is no-op for PostgreSQL., Test ensure_npc_database_directory() creates directory if needed. (+8 more)

### Community 564 - "test_statistics_aggregator.py"
Cohesion: 0.10
Nodes (24): mock_memory_monitor(), mock_message_queue(), mock_performance_tracker(), mock_rate_limiter(), mock_room_manager(), fixture, Unit tests for statistics aggregator. Tests the StatisticsAggregator class., Test get_connection_stats() returns connection statistics. (+16 more)

### Community 565 - "generate_invites_db.py"
Cohesion: 0.11
Nodes (24): Set test override database URL., set_test_database_url(), Reset database state for testing. This function resets the DatabaseManager…, reset_database(), fixture, Reset database state before each test., Test reset_database resets DatabaseManager singleton and module state., reset_db() (+16 more)

### Community 566 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.16
Nodes (14): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Register a new strategy for a channel type. Args: channel_type: Channel type to…, Unit tests for channel broadcasting strategies. Tests the…, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…, Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., Test ChannelBroadcastingStrategyFactory.get_strategy() returns…, Test ChannelBroadcastingStrategyFactory.register_strategy() registers new… (+6 more)

### Community 567 - "UnknownChannelStrategy"
Cohesion: 0.25
Nodes (6): Strategy for unknown channel types., Initialize unknown channel strategy. Args: channel_type: Unknown channel type, Get strategy for channel type. Args: channel_type: Type of channel to get…, UnknownChannelStrategy, Test UnknownChannelStrategy.broadcast() handles unknown channel., test_unknown_channel_strategy_broadcast()

### Community 568 - "verify_linting_parity.py"
Cohesion: 0.15
Nodes (27): check_alignment(), _check_pylint_suppressions(), _check_ruff_suppressions(), find_suppressions(), _has_pylint_equivalent(), _has_ruff_equivalent(), main(), parse_pylint_suppression() (+19 more)

### Community 569 - "CoordinateGenerator"
Cohesion: 0.12
Nodes (15): CoordinateGenerator, Any, AsyncSession, Load rooms and their exits from database. Args: plane: Plane name zone: Zone…, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits., Assign coordinates using BFS starting from origin., Detect conflicts (multiple rooms at same x,y coordinates). (+7 more)

### Community 570 - "properties"
Cohesion: 0.14
Nodes (14): description, description, description, description, type, properties, field1, field2 (+6 more)

### Community 571 - "._get_random_error_message"
Cohesion: 0.08
Nodes (13): Any, Initialize the combat validator. Args: party_service: Optional PartyService for…, Validate that attacker is allowed to attack target (e.g. not same party). Hook…, Validate a combat command with thematic error messages. Args: command_data: The…, Validate that a target exists with thematic error messages. Args: target_name:…, Validate that a target is alive with thematic error messages. Args:…, Validate combat state with thematic error messages. Args: is_in_combat: Whether…, Validate attack strength with thematic error messages. Args: player_level:… (+5 more)

### Community 572 - "messageHandlers.ts"
Cohesion: 0.16
Nodes (14): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+6 more)

### Community 573 - "DatabaseManager"
Cohesion: 0.09
Nodes (19): DatabaseManager, async_sessionmaker, AsyncSession, Thread-safe singleton for database management. Manages database engine, session…, Initialize the database manager., Get the async session maker, initializing if necessary. Returns:…, Get the database URL, initializing if necessary. Returns: str: The database URL…, Close database connections. (+11 more)

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

### Community 579 - "test_websocket_handler_validation_errors.py"
Cohesion: 0.04
Nodes (62): asyncio, Unit tests for WebSocket handler validation, rate limiting, and error paths.…, _validate_message should pass expected token from connection metadata into…, When metadata.token is missing, validate JWT from message and restore metadata., Test _send_error_response handles WebSocket disconnect., Test _send_error_response handles RuntimeError with disconnect message., Test _send_error_response handles RuntimeError with close message., Test _send_error_response handles other RuntimeError. (+54 more)

### Community 580 - "fix_fstring_logging.py"
Cohesion: 0.12
Nodes (24): _build_structured_params(), _clean_message(), _create_replacement_for_fstring(), create_structured_log_message(), extract_variables_from_fstring(), fix_fstring_logging_in_file(), _handle_no_variables_case(), main() (+16 more)

### Community 581 - "Client README Overview"
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

### Community 585 - "Configuration Files Reference"
Cohesion: 0.10
Nodes (22): Configuration File Tuples, Configuration Files Reference, .env.local Secrets Pattern, Container/Item Repository Async Migration Plan, SQLAlchemy Async Migration Option, Container System API, Container System API Reference, Container Item System (+14 more)

### Community 586 - "RoomBasedChannelStrategy"
Cohesion: 0.25
Nodes (7): Strategy for room-based channels (say, local, emote, pose)., Initialize room-based channel strategy. Args: channel_type: Type of room-based…, RoomBasedChannelStrategy, Test RoomBasedChannelStrategy.broadcast() broadcasts to room., Test RoomBasedChannelStrategy.broadcast() handles missing room_id., test_room_based_channel_strategy_broadcast(), test_room_based_channel_strategy_broadcast_no_room_id()

### Community 587 - "Ruff Pylint Mapping"
Cohesion: 0.40
Nodes (6): Linting Complexity Alignment, Ruff C901 McCabe Complexity, Pylint Unique Findings, Ruff to Pylint Mapping, Lizard CCN Threshold (>10), Lizard Complexity Findings

### Community 588 - "_find_item_in_equipped"
Cohesion: 0.11
Nodes (24): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _handle_item_look(), Any, Item look functionality for MythosMUD. This module handles looking at items,…, Find an item in equipped items by name or prototype_id. Args: equipped:…, Check if item found in a location and return formatted result. (+16 more)

### Community 589 - "chat_nats_publisher.py"
Cohesion: 0.13
Nodes (23): _build_legacy_subject(), build_nats_subject(), _build_standardized_subject(), _extract_subzone_from_room(), publish_chat_message_to_nats(), Any, Chat NATS publishing utilities. This module provides NATS subject building and…, Build NATS subject using standardized patterns or fallback to legacy… (+15 more)

### Community 591 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 592 - "Communities (10 total, 2 thin omitted)"
Cohesion: 0.11
Nodes (17): Communities (10 total, 2 thin omitted), Community 0 - "Azotottal (fallen angel beyond the stars) / Captain Louis Malon", Community 1 - "Charenton (Paris district / asylum) / Christophe Pressi — Soldat (Soldier), age 20", Community 2 - "Dreamlands / Fenalik's Mansion (Poissy)", Community 3 - "Reign of Terror / Call of Cthulhu 7th Edition", Community 4 - "Bastille / James Coquillat", Community 5 - "Azathoth / Celine Bessette", Community 6 - "Christophe Pressi / Comte Benoit" (+9 more)

### Community 593 - "test_event_publisher_helpers.py"
Cohesion: 0.14
Nodes (14): event_publisher(), mock_nats_service(), fixture, Unit tests for event publisher helper functions. Tests the helper functions in…, Create a mock NATS service., Create an EventPublisher instance., Test _create_event_message() creates event message., Test get_next_sequence_number() increments sequence. (+6 more)

### Community 594 - "StatisticsAggregator"
Cohesion: 0.11
Nodes (16): Any, UUID, Get comprehensive connection statistics. Args: player_websockets: Player to…, Analyze connection health distribution. Args: connection_metadata: Connection…, Aggregates statistics from connection management components. This class…, Analyze connection types. Args: connection_metadata: Connection metadata…, Analyze connection ages. Args: connection_metadata: Connection metadata now:…, Analyze session health. Args: connection_metadata: Connection metadata Returns:… (+8 more)

### Community 595 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 596 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 597 - "1774539086359-useMythosAppState.ts"
Cohesion: 0.11
Nodes (29): authSliceReducer(), creationSliceReducer(), INITIAL_AUTH_SLICE, INITIAL_CREATION_SLICE, PendingSkillsPayload, resolveNextState(), useAuthSliceSetters(), useCreationSliceSetters() (+21 more)

### Community 598 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, properties, minLength, type, id, name, season (+4 more)

### Community 599 - "Error Log Analyzer"
Cohesion: 0.12
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time. Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 600 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, minLength, type, properties, minLength, type, type (+4 more)

### Community 601 - "required"
Cohesion: 0.17
Nodes (12): $defs, scheduleEntry, applies_to, category, days, end_hour, id, name (+4 more)

### Community 602 - "ShopkeeperNPC"
Cohesion: 0.09
Nodes (13): Buy item from player., Calculate final price with markup., Handle greeting customer action., Handle restocking inventory action., Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., Shopkeeper NPC type with buy/sell functionality., Initialize shopkeeper NPC., Setup shopkeeper-specific behavior rules. (+5 more)

### Community 603 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test handling item look when item is in room drops., Test handling item look when item is in inventory., Test handling item look when item is equipped., Test handling item look when item not found., Test handling item look with look_in flag skips equipped items., Test trying implicit lookup when item is in room drops., Test trying implicit lookup when item not found. (+17 more)

### Community 604 - "CoordinateValidator"
Cohesion: 0.21
Nodes (9): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Coordinate validation service for ASCII maps. This module provides conflict…, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:…, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate… (+1 more)

### Community 605 - "_find_item_in_inventory"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id. Args: inventory: List…, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 606 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)"
Cohesion: 0.12
Nodes (16): Communities (9 total, 4 thin omitted), Community 0 - "De Vermiis Mysteriis; Dust of Ibn-Ghazi", Community 1 - "Character Creation", Community 2 - "Alone Against the Flame", Community 3 - "Cover Art", Community 4 - "Azathoth; Banishment Chant (Latin)", Community Hubs (Navigation), Corpus Check (+8 more)

### Community 607 - "deque"
Cohesion: 0.08
Nodes (50): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+42 more)

### Community 608 - "test_command_processor.py"
Cohesion: 0.04
Nodes (53): Unit tests for command processor. Tests the CommandProcessor class which…, Test process_command_string handles KeyError., Test process_command_string handles RuntimeError., Test _extract_attributes extracts attributes correctly., Test _extract_attributes handles missing attributes., Test _is_combat_command returns True for attack command., Test _is_combat_command returns True for punch command., Test _is_combat_command returns True for kick command. (+45 more)

### Community 610 - "test_combat_persistence_handler.py"
Cohesion: 0.09
Nodes (23): mock_combat_service(), mock_player(), persistence_handler(), fixture, Unit tests for combat persistence handler - core functionality. Tests…, Create mock combat service., Create CombatPersistenceHandler instance., Test CombatPersistenceHandler initialization. (+15 more)

### Community 611 - "test_player_event_handlers_utils.py"
Cohesion: 0.02
Nodes (91): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), asyncio, fixture, Unit tests for player event handler utilities. Tests the…, Test get_player_info() returns None for invalid player_id. (+83 more)

### Community 612 - ".to_dict"
Cohesion: 0.12
Nodes (9): Any, Get list of player IDs currently in the room. Returns: List of player IDs in…, Get list of object IDs currently in the room. Returns: List of object IDs in…, Get list of NPC IDs currently in the room. Returns: List of NPC IDs in the room, Get the total number of occupants in the room. Returns: Total count of players,…, Check if the room has no occupants. Returns: True if the room is empty, False…, Get list of containers in this room. Returns: List of container data…, Convert the room to a dictionary representation. Returns: Dictionary containing… (+1 more)

### Community 613 - "patch"
Cohesion: 0.12
Nodes (17): patch, Movement runs when random.random() <= idle_movement_probability (exclusive…, Movement is skipped when random.random() > idle_movement_probability., Gating skips idle movement when combat service lists this NPC., When combat service is empty and probability passes, idle move is allowed., Test _is_npc_in_combat() when NPC is in combat., Test should_idle_move() returns False when NPC is not alive., Test should_idle_move() returns False when NPC is not active. (+9 more)

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

### Community 618 - "test_room_service.py"
Cohesion: 0.08
Nodes (23): Unit tests for room service. Tests the RoomService class for room-related…, Test get_room_by_name() returns None (not implemented)., Test list_rooms_in_zone() returns empty list (not implemented)., Test update_environment_state() updates environment state., Test get_environment_state() returns current environment state., Test describe_lighting() returns description for day., Test describe_lighting() returns description for night., Test describe_lighting() returns default for unknown daypart. (+15 more)

### Community 619 - "Game Subsystem Design Documents"
Cohesion: 0.09
Nodes (23): Linkdead Grace Period, Gunicorn + Uvicorn Production, HTTPS and WSS Requirement, Audit Table, Domain Grouping Summary, Existing PostgreSQL Functions (Already in DDL), PostgreSQL Procedures Migration - Audit Spreadsheet, Scope (+15 more)

### Community 620 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.18
Nodes (11): 10. Final Verification, 3. Systematic Investigation Approach, 5. Test Environment Setup, 6. Quality Assurance Checklist, Environment Variables, For Authentication Failures, For Database-Related Failures, For Game Logic Failures (+3 more)

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

### Community 625 - "ModalContainer.tsx"
Cohesion: 0.24
Nodes (5): maxWidthClasses, ModalContainer(), ModalContainerProps, renderOpenModal(), useModalEscapeKey()

### Community 626 - "multiplayer-playwright-testing.md"
Cohesion: 0.20
Nodes (9): 🎯 AVAILABLE SCENARIOS, 🔄 BACKWARD COMPATIBILITY, 🚨 CRITICAL AI EXECUTOR REQUIREMENTS 🚨, 📋 EXECUTION OPTIONS, 📖 MANDATORY EXECUTION ORDER, 🛑 MANDATORY EXECUTION PROTOCOL 🛑, 🎮 MODULAR E2E TEST SUITE STRUCTURE 🎮, 🔧 TESTING APPROACH (+1 more)

### Community 627 - "Mypy Type Checking Remediation Prompt - AI-Optimized Version"
Cohesion: 0.20
Nodes (9): 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, Common Mypy Error Codes, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, 📊 MYPY ERROR CODE CATEGORIZATION GUIDE, Mypy Type Checking Remediation Prompt - AI-Optimized Version (+1 more)

### Community 628 - "fixture"
Cohesion: 0.09
Nodes (24): async_session_factory(), lucidity_service_factory(), mock_event_dispatcher(), mock_lucidity_service(), mock_persistence(), mock_session(), fixture, Create a mock persistence layer. (+16 more)

### Community 629 - "ItemFactory"
Cohesion: 0.13
Nodes (15): ItemInstance, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError, Any, Exception, Raised when the factory cannot produce a valid instance., Factory responsible for instantiating runtime item instances. (+7 more)

### Community 630 - "Movement Subsystem Design"
Cohesion: 0.20
Nodes (9): Architecture, Component interactions, Constraints, Developer guide, Key design decisions, Movement Subsystem Design, Overview, Related docs (+1 more)

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

### Community 637 - "_get_npc_room_id"
Cohesion: 0.12
Nodes (16): _get_npc_room_id(), _get_npcs_in_room(), Get the room ID from an NPC instance, checking both current_room and…, Get list of NPC names in a room from lifecycle manager., Test _get_npc_room_id() returns current_room_id when available., Test _get_npc_room_id() returns current_room when current_room_id is None., Test _get_npc_room_id() returns None when both are None., test_get_npc_room_id_from_current_room() (+8 more)

### Community 638 - "Comprehensive System Audit"
Cohesion: 0.67
Nodes (3): CI/CD Enhanced Logging Validation, Comprehensive System Audit, Database Migration Guide

### Community 639 - "NATSEventBusBridge"
Cohesion: 0.10
Nodes (16): Any, Initialize distributed EventBus. Args: nats_service: NATS service for…, Set NATS service and start the bridge (call after NATS connects)., NATSEventBusBridge, Any, Subscribe to NATS domain events and start receiving., Stop the bridge and unsubscribe from NATS., Bridges domain events between local EventBus and NATS for distribution. When… (+8 more)

### Community 640 - "NPCCommunicationIntegration"
Cohesion: 0.25
Nodes (5): NPCCommunicationIntegration, Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…, Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…, Integrates NPCs with the existing chat and whisper systems. This class provides…, Initialize the NPC communication integration. Args: event_bus: Optional…

### Community 641 - "MagicServiceCompletionMixin"
Cohesion: 0.19
Nodes (15): _is_heal_other_target(), MagicServiceCompletionMixin, Any, UUID, Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…, Parse target_id from casting state. Returns None if missing or invalid., Apply costs and queue spell for next combat round. Returns True if queued,…, Apply spell costs/effects, send completion message and healing event. (+7 more)

### Community 642 - "Security Implementation"
Cohesion: 0.29
Nodes (7): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection, SSE Authentication System

### Community 643 - "test_level_service.py"
Cohesion: 0.05
Nodes (56): level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level(), UUID (+48 more)

### Community 644 - "migrate_combat_data.py"
Cohesion: 0.18
Nodes (22): Validate combat data for an NPC definition. Args: npc_definition: NPCDefinition…, validate_npc_combat_data(), main(), migrate_npc_combat_data(), _migrate_one_npc(), _npc_has_combat_data(), _npc_has_full_combat_data(), Any (+14 more)

### Community 645 - "PersonalMessageSender"
Cohesion: 0.12
Nodes (21): _is_expected_websocket_close(), PersonalMessageSender, Any, UUID, Send message to a single WebSocket connection. Returns True if successful., Queue message if no active connections., Send a personal message to a player via WebSocket. Args: player_id: The…, Get message delivery statistics for a player. (+13 more)

### Community 647 - "send_welcome_event"
Cohesion: 0.15
Nodes (13): AsyncPersistenceRoomLookup, cleanup_websocket_connection(), PlayerDisconnectService, Protocol, UUID, WebSocket, Send welcome event to the client. Returns: True if successful, False if…, Notify subsystems when a WebSocket session ends for a player. (+5 more)

### Community 648 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 649 - "test_player_event_handlers_room.py"
Cohesion: 0.04
Nodes (70): asyncio, Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test broadcast_player_entered_message() skips when room_id is None., Test subscribe_player_to_room() successfully subscribes player., Test subscribe_player_to_room() handles invalid player_id., Test subscribe_player_to_room() handles subscription errors., Test _send_room_name_message() sends room name., Test _prepare_room_data() prepares room data with to_dict. (+62 more)

### Community 650 - "validate_inventory_payload"
Cohesion: 0.13
Nodes (21): _build_validator(), Any, Inventory JSON schema validation utilities. As recorded in the restricted…, Internal helper to construct a Draft7 validator instance., Validate a complete inventory payload against the canonical schema. Raises:…, Validate only the inventory portion to simplify testing workflows. Raises:…, validate_inventory_items(), validate_inventory_payload() (+13 more)

### Community 651 - "PostgresRow"
Cohesion: 0.11
Nodes (13): PostgresRow, Row-like object for PostgreSQL query results., Test PostgresRow class., Test PostgresRow initialization., Test PostgresRow.__getitem__ with string key., Test PostgresRow.__getitem__ with integer index., Test PostgresRow.__getitem__ with out-of-range integer index., Test PostgresRow.__iter__. (+5 more)

### Community 652 - "TestValidateCommandBasics"
Cohesion: 0.20
Nodes (6): Test _validate_command_basics function., Test _validate_command_basics returns result for empty command., Test _validate_command_basics returns result for command too long., Test _validate_command_basics returns result for invalid command content., Test _validate_command_basics returns None for valid command., TestValidateCommandBasics

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

### Community 660 - "Runner Path"
Cohesion: 0.11
Nodes (14): main(), Path, Verify test database configuration. Note: For PostgreSQL databases, schema is…, Build the pytest command with proper configuration. Args: test_paths: List of…, # NOTE: Test runner uses minimal structlog configuration for console output, Run the test suite with proper configuration. Args: test_paths: List of test…, Run integration tests only., Run all tests (unit, integration, but not E2E by default). (+6 more)

### Community 661 - "inventory_put_command.py"
Cohesion: 0.22
Nodes (16): Remove or update item quantity in player inventory after transfer., remove_item_from_inventory(), handle_put_command(), _put_resolve_container_id(), _put_run_validated(), _put_transfer_finish(), PutCommandRuntime, PutValidatedWork (+8 more)

### Community 662 - "combat_flee_handler.py"
Cohesion: 0.13
Nodes (21): check_involuntary_flee(), _check_involuntary_flee_with_session(), execute_voluntary_flee(), _handle_failed_voluntary_flee(), _involuntary_flee_on_cooldown(), Any, UUID, Combat flee handler for involuntary and voluntary flee logic. Handles checking… (+13 more)

### Community 663 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 664 - "properties"
Cohesion: 0.20
Nodes (10): description, minLength, type, type, properties, description, weather_patterns, description (+2 more)

### Community 665 - "run-playwright-tests.js"
Cohesion: 0.22
Nodes (7): clientRoot, __dirname, E2E_BACKEND_BASE_URL, env, __filename, playwright, testsDir

### Community 666 - "🎯 MANDATORY AI EXECUTION PROTOCOL"
Cohesion: 0.22
Nodes (9): For Each Issue Category, 🎯 MANDATORY AI EXECUTION PROTOCOL, Mypy Type Checking, Phase 1: Initial Assessment (REQUIRED FIRST), Phase 3: Systematic Fixing Process, Phase 4: Tool Selection Guide, Phase 6: Verification Protocol, Phase 7: Success Validation (+1 more)

### Community 667 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 668 - "Lint Sqlalchemy Async"
Cohesion: 0.11
Nodes (18): Await, lint_directory(), lint_file(), main(), Call, Import, ImportFrom, Path (+10 more)

### Community 669 - "quality_fragmentation_lizard.py"
Cohesion: 0.17
Nodes (25): git_show_file(), _check_head_rows(), check_lizard_limits(), _has_file_nloc_override(), has_lizard_override(), _has_override_in_file(), _iter_lizard_function_maps(), _lizard_entries() (+17 more)

### Community 670 - "applies_to"
Cohesion: 0.28
Nodes (9): items, minItems, type, uniqueItems, items, items, minLength, type (+1 more)

### Community 671 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 672 - "Technical Implementation"
Cohesion: 0.15
Nodes (13): 1. Component Refactoring, 2. Message Routing Logic, 3. State Management, 4. Event Handling, ChatPanel.tsx Enhancements (New Chat Input Panel), Command Routing Logic, CommandPanel.tsx Simplifications, Current Logic (in CommandPanel) (+5 more)

### Community 673 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 674 - "_holiday_entry_from_row"
Cohesion: 0.29
Nodes (6): _holiday_entry_from_row(), Record, Async helper to load holidays from PostgreSQL database., Normalize nullable PostgreSQL array columns to string values., Build a HolidayEntry from a calendar_holidays row., _string_list_from_row()

### Community 675 - "test_connection_event_helpers.py"
Cohesion: 0.14
Nodes (23): Any, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events., subscribe_to_room_events_impl(), unsubscribe_from_room_events_impl(), asyncio, Unit tests for connection event helpers. Tests the connection_event_helpers…, Test unsubscribe_from_room_events_impl() handles AttributeError. (+15 more)

### Community 676 - "test_inventory_mutation_guard_async.py"
Cohesion: 0.17
Nodes (15): guard(), asyncio, fixture, Unit tests for inventory mutation guard - asynchronous acquire operations.…, Test acquire_async serializes concurrent mutations for same player., Create an InventoryMutationGuard instance., Test acquire_async enforces max_tokens limit., Test acquire_async allows token reuse after expiry. (+7 more)

### Community 677 - "party_commands.py"
Cohesion: 0.18
Nodes (19): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+11 more)

### Community 678 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 679 - "_mock_result_mappings_all"
Cohesion: 0.12
Nodes (16): _mock_result_mappings_all(), Build mock result such that result.mappings().all() returns rows., Test get_npc_definitions() successfully retrieves definitions., Test get_npc_definitions() returns empty list when no definitions., Test get_npc_definition_by_name() returns definition when found., Test delete_npc_definition() returns False when not found., Test get_spawn_rule() returns None when not found., Test create_spawn_rule() raises ValueError when definition not found. (+8 more)

### Community 680 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 681 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 682 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)"
Cohesion: 0.13
Nodes (14): Communities (8 total, 5 thin omitted), Community 0 - "Baron Arthur von Kleist; Pyotr Shabelsky-Bork", Community 1 - "The Demon-Großmann; Demonic Mutation Table", Community 2 - "Erwin Kern; Manfred Freiherr von Killinger", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11) (+6 more)

### Community 683 - "fixture"
Cohesion: 0.15
Nodes (13): catalog_with_own_language_and_mythos(), mock_persistence(), mock_player_skill_repo(), mock_skill_repo(), mock_skill_use_log_repo(), fixture, Mock PlayerSkillRepository., Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id). (+5 more)

### Community 684 - "Realtime Connection Compatibility"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 685 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Anna Konrad; Lucas Reston", Community 2 - "Does Love Forgive", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12) (+6 more)

### Community 686 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 687 - "Migrate Rooms"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 688 - "run-vitest.js"
Cohesion: 0.25
Nodes (7): args, clientRoot, __dirname, env, __filename, vitest, vitestBin

### Community 689 - "usePerformanceMonitor.ts"
Cohesion: 0.29
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 690 - "holidays.schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, minItems, type, $id, holidays, properties, holidays, required (+3 more)

### Community 691 - "npc_schedules.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 692 - "1. Enhanced ChatPanel (New Chat Input Panel)"
Cohesion: 0.25
Nodes (8): 1. Enhanced ChatPanel (New Chat Input Panel), 2. Renamed Game Log Panel (Formerly ChatPanel), ChatPanel Layout Structure, Enhanced ChatPanel Interface, Game Log Panel Layout Structure, New Features to Add, Proposed Changes, Purpose and Functionality

### Community 693 - "Implementation Phases"
Cohesion: 0.25
Nodes (8): 1.1 Enhance CircuitBreaker Class, 1.2 Create CircuitBreaker Manager, 1.3 Add Configuration Support, 5.1 Authentication Operations, 5.2 Rate Limiting Integration, Implementation Phases, Phase 1: Core Infrastructure Enhancement, Phase 5: Authentication and Security

### Community 694 - "MockPersistence"
Cohesion: 0.10
Nodes (16): mock_app(), mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), MockPersistence, fixture, Create a mock FastAPI app. (+8 more)

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
Nodes (25): CaptureFixture, regression, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, fixture, MonkeyPatch, Protocol (+17 more)

### Community 706 - "MythosMUD Worldbuilding Source"
Cohesion: 0.67
Nodes (3): MythosMUD Wiki Log, MythosMUD Worldbuilding Foundation (Raw), MythosMUD Worldbuilding Source

### Community 707 - "asyncio"
Cohesion: 0.13
Nodes (12): asyncio, Test _handle_special_command_routing function., Test _handle_special_command_routing handles alias management commands., Test _handle_special_command_routing returns error when alias storage…, Test _handle_special_command_routing converts single-word emotes., Test _process_alias_expansion function., Test _process_alias_expansion returns None when no alias storage., Test _process_alias_expansion returns None when alias not found. (+4 more)

### Community 708 - "CombatPersistenceHandler"
Cohesion: 0.13
Nodes (14): CombatPersistenceHandler, Any, UUID, Synchronously persist player DP to database. This is the actual persistence…, Persist player DP to database in background (fire-and-forget). This method runs…, Handles combat-related persistence operations., Initialize the persistence handler. Args: combat_service: Reference to the…, Persist player DP to database in background (fire-and-forget). Public API… (+6 more)

### Community 709 - "rescue_service.py"
Cohesion: 0.16
Nodes (18): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+10 more)

### Community 710 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

### Community 711 - "utils/config.ts"
Cohesion: 0.17
Nodes (15): MapView(), MapViewBody(), MapViewProps, Room, useMapViewEffects(), AppCreationFlowViews(), creationShell(), renderNameStep() (+7 more)

### Community 712 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _build_room_objects successfully builds room objects., Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., test_build_room_objects_success(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

### Community 713 - "UUID"
Cohesion: 0.17
Nodes (9): Any, UUID, Broadcast party message to party members only, with dampening and mute checks., Send whisper message to specific player with communication dampening., Broadcast system/admin message to all players., Handle unknown channel type., Broadcast message according to channel strategy. Args: chat_event: WebSocket…, Broadcast room-based message with server-side filtering. (+1 more)

### Community 714 - "enabled"
Cohesion: 0.50
Nodes (4): default, description, type, enabled

### Community 715 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 716 - "test_combat_messaging_integration.py"
Cohesion: 0.11
Nodes (17): Unit tests for combat messaging integration. Tests the…, Test connection_manager setter updates value., Test connection_manager setter overrides lazy load mechanism., Test CombatMessagingIntegration initialization., Test CombatMessagingIntegration initialization without connection manager., Test connection_manager property lazy loads from container., Test _resolve_connection_manager_from_container resolves manager., Test _resolve_connection_manager_from_container raises when no manager. (+9 more)

### Community 717 - "test_rate_limiter.py"
Cohesion: 0.08
Nodes (25): Unit tests for rate limiter service. Tests the RateLimiter class which provides…, Test check_rate_limit always returns True when disabled., Test check_rate_limit handles errors gracefully (fails open)., Test record_message cleans up old entries., Test get_player_stats returns correct statistics., Test get_player_stats handles player with no messages., Test reset_player_limits handles nonexistent player., Test get_remaining_messages returns correct count. (+17 more)

### Community 718 - "RoomInfoPanel.tsx"
Cohesion: 0.13
Nodes (16): applyRoomDefaultFields(), DEV_FALLBACK_ROOM, fixOccupantCountMismatch(), formatDescription(), formatExitDirections(), formatLocationName(), KNOWN_LOCATION_PATTERNS, logRoomInfoRenderDebug() (+8 more)

### Community 719 - "PartyService"
Cohesion: 0.15
Nodes (19): PartyUpdated, Event fired when party membership or leadership changes. Emitted by…, PartyService, Party service for MythosMUD. In-memory ephemeral party state: parties exist…, Send party_invite event to the target player only., In-memory party management: create, disband, add/remove/kick members, leader…, event_bus(), party_events() (+11 more)

### Community 720 - "optimized_validate_command_content"
Cohesion: 0.25
Nodes (8): Test validating empty command content., Test validating valid command content., Test validating command content with injection pattern., test_optimized_validate_command_content_empty(), test_optimized_validate_command_content_injection(), test_optimized_validate_command_content_valid(), optimized_validate_command_content(), Optimized validation for command content fields. Args: value: The command…

### Community 721 - "optimized_validate_reason_content"
Cohesion: 0.25
Nodes (8): Test validating empty reason content., Test validating valid reason content., Test validating reason content with injection pattern., test_optimized_validate_reason_content_empty(), test_optimized_validate_reason_content_injection(), test_optimized_validate_reason_content_valid(), optimized_validate_reason_content(), Optimized validation for reason content fields. Args: value: The reason to…

### Community 722 - "optimized_validate_pose_content"
Cohesion: 0.25
Nodes (8): Test validating empty pose content., Test validating valid pose content., Test validating pose content with injection pattern., test_optimized_validate_pose_content_empty(), test_optimized_validate_pose_content_injection(), test_optimized_validate_pose_content_valid(), optimized_validate_pose_content(), Optimized validation for pose content fields. Args: value: The pose to validate…

### Community 723 - "Security Infrastructure"
Cohesion: 0.08
Nodes (24): Validate and sanitize a user-provided path to prevent path traversal attacks.…, validate_secure_path(), Test validate_secure_path detects when common_path != base_path (lines 59-66)., Test validate_secure_path with valid path., Test validate_secure_path handles different drives on Windows., Test validate_secure_path rejects path traversal with .., Test validate_secure_path rejects path traversal with ~, Test validate_secure_path with nested valid path. (+16 more)

### Community 724 - "MetricsCollector"
Cohesion: 0.09
Nodes (13): MetricsCollector, Any, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or…, Simple metrics collector for NATS message delivery. Thread-safe metrics…, Get concise metrics summary. Returns: High-level metrics summary AI: For quick… (+5 more)

### Community 725 - "optimized_validate_filter_name"
Cohesion: 0.25
Nodes (8): Test validating empty filter name., Test validating valid filter name., Test validating invalid filter name., test_optimized_validate_filter_name_empty(), test_optimized_validate_filter_name_invalid(), test_optimized_validate_filter_name_valid(), optimized_validate_filter_name(), Optimized validation for filter name fields. Args: value: The filter name to…

### Community 726 - "optimized_validate_target_player"
Cohesion: 0.25
Nodes (8): Test validating empty target player name., Test validating valid target player name., Test validating invalid target player name., test_optimized_validate_target_player_empty(), test_optimized_validate_target_player_invalid(), test_optimized_validate_target_player_valid(), optimized_validate_target_player(), Optimized validation for target player fields. Args: value: The target player…

### Community 727 - "optimized_validate_help_topic"
Cohesion: 0.25
Nodes (8): Test validating empty help topic., Test validating valid help topic., Test validating invalid help topic., test_optimized_validate_help_topic_empty(), test_optimized_validate_help_topic_invalid(), test_optimized_validate_help_topic_valid(), optimized_validate_help_topic(), Optimized validation for help topic fields. Args: value: The help topic to…

### Community 728 - "Verify Migration"
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

### Community 734 - "test_combat_flee_handler.py"
Cohesion: 0.15
Nodes (21): Roll for voluntary flee success (no side effects). Formula: base + (bonus *…, try_voluntary_flee_roll(), _make_participant(), asyncio, UUID, Unit tests for combat flee handler (voluntary flee roll and…, execute_voluntary_flee returns False when get_room_by_id returns None., execute_voluntary_flee returns False when room has no exits. (+13 more)

### Community 735 - "enum"
Cohesion: 0.29
Nodes (7): autumn, spring, summer, winter, season, enum, type

### Community 736 - "enum"
Cohesion: 0.29
Nodes (7): description, enum, type, indoors, outdoors, underwater, environment

### Community 737 - "room_validator/schemas/unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 738 - "enum"
Cohesion: 0.29
Nodes (7): description, enum, type, indoors, outdoors, underwater, environment

### Community 739 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Python Import Fix, Template 2: Python Import Sorting Fix, Template 3: Python Line Length Fix, Template 4: React Hook Dependency Fix, Template 5: TypeScript Unused Variable Fix

### Community 740 - "Archive Who Command"
Cohesion: 0.67
Nodes (3): Who Command Name Filtering, Who Command Enhancement, Who Command Implementation Tasks

### Community 741 - "🔧 COMMON FIX TEMPLATES"
Cohesion: 0.33
Nodes (6): 🔧 COMMON FIX TEMPLATES, Template 1: Python Import Fix, Template 2: Python Import Sorting Fix, Template 3: Python Line Length Fix, Template 4: React Hook Dependency Fix, Template 5: TypeScript Unused Variable Fix

### Community 742 - "Quality Fragmentation Guard"
Cohesion: 0.21
Nodes (23): ChangedFile, scan_changed_files(), _ChangedFile, _load_guard_module(), _load_trends_module(), Path, Protocol, _QualityGuardModule (+15 more)

### Community 743 - "E 2 E Readme Playwright"
Cohesion: 0.22
Nodes (10): Playwright E2E Runtime Tests, ArkanWolfshade E2E Account, E2E Tests Playwright, Ithaqua E2E Account, mythos_e2e Database, Runtime Auth Isolation, Playwright storageState Session Sharing, E2E Login Timeout Issue (+2 more)

### Community 744 - "Tsconfig App"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 745 - "Tsconfig Build"
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

### Community 750 - "items"
Cohesion: 0.25
Nodes (8): items, type, uniqueItems, items, additionalProperties, minLength, type, bonus_tags

### Community 751 - "ComprehensiveLoggingMiddleware"
Cohesion: 0.15
Nodes (14): ComprehensiveLoggingMiddleware, Any, ASGIApp, Exception, Receive, Request, Scope, Send (+6 more)

### Community 752 - "items"
Cohesion: 0.33
Nodes (6): additionalProperties, properties, schedules, items, minItems, type

### Community 753 - "Application Container Analysis"
Cohesion: 0.28
Nodes (9): ApplicationContainer, Application Container Analysis, Domain Container Bundles, Container Initialization Phases, Bounded Contexts, Bounded Contexts and Service Boundaries, Service Boundaries, Complexity Refactoring Test Plan (+1 more)

### Community 755 - "Implementation Details"
Cohesion: 0.33
Nodes (6): CircuitBreaker Manager, Database Operations, Enhanced CircuitBreaker Class, Implementation Details, Integration Examples, NATS Operations

### Community 757 - "_container_data_to_dict"
Cohesion: 0.14
Nodes (13): _container_data_to_dict(), Any, ContainerData, datetime, UUID, Update a container (async)., Get decayed containers (async)., Delete a container (async). (+5 more)

### Community 758 - "get_help_content"
Cohesion: 0.11
Nodes (20): get_command_categories(), get_commands_by_category(), _get_general_help(), get_help_content(), Any, Help content and command documentation for MythosMUD. This module contains the…, Get help content for commands. Args: command_name: Optional specific command…, Get general help content with command categories. (+12 more)

### Community 759 - ".handle_player_death"
Cohesion: 0.14
Nodes (12): Any, AsyncSession, Player, UUID, Process DP decay for a single mortally wounded player. Decreases player DP by…, Ensure player posture is set to lying when dead. Args: player: Player object to…, Clear player combat state when they die. BUGFIX #244: As documented in…, Publish player died event if event bus is available. Args: player_id: ID of the… (+4 more)

### Community 760 - "Quest System Features"
Cohesion: 0.40
Nodes (6): Quest Design Guidelines, Quest Design Principles, Quest System Features, Event-Driven Quest Progression, Quest Goal Types, Declarative YAML Quest Config

### Community 761 - "Testing Guide"
Cohesion: 0.29
Nodes (8): Quick Start E2E Tests, E2E Test Server Quick Start, Container-Based Test Fixtures, Test Modernization Plan, bcrypt PyO3 Fresh Session Limitation, Testing Guide, Pydantic Testing Patterns, Two-Tier Test Suite (make test)

### Community 762 - "test_combat_service.py"
Cohesion: 0.24
Nodes (19): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+11 more)

### Community 763 - "Any"
Cohesion: 0.11
Nodes (10): Any, Despawn an NPC instance. Args: npc_id: ID of the NPC to despawn reason: Reason…, Move an NPC instance to a different room. Args: npc_id: ID of the NPC to move…, Get all active NPC instances. Returns: List of NPC instance information, Get detailed stats for a specific NPC instance. Args: npc_id: ID of the NPC…, Get NPC population statistics. Returns: Dictionary with population statistics, Get NPC zone statistics. Returns: Dictionary with zone statistics, Get system-wide NPC statistics. Returns: Dictionary with system statistics (+2 more)

### Community 764 - "test_zone_config_loader.py"
Cohesion: 0.05
Nodes (69): async_load_zone_configurations(), extract_zone_name(), parse_json_field(), parse_zone_special_rules(), process_subzone_rows(), process_zone_rows(), Connection, Record (+61 more)

### Community 765 - "Security Infrastructure"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory. Args: filename: The filename…, Unit tests for security utilities. Tests path validation and file security…, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 766 - "populate_test_npc_databases.py"
Cohesion: 0.31
Nodes (8): get_npc_data_from_source(), get_npc_database_url(), main(), populate_database(), Populate a PostgreSQL database with NPC data. Args: target_url: PostgreSQL…, Main function to populate test NPC databases., Get NPC database URL for the specified environment. Args: environment:…, Extract NPC data from the source PostgreSQL database. Args: source_url:…

### Community 767 - "test_skill_service.py"
Cohesion: 0.17
Nodes (11): Unit tests for SkillService (get_skills_catalog, set_player_skills,…, run_improvement_rolls with new_level 1 does nothing (previous level 0)., run_improvement_rolls when no skills used at previous level does not update., When current >= 90, successful improvement adds 1 (cap 99)., When roll <= current value, no update_value call., When roll <= skill value, record_use is called and returns True., test_roll_skill_check_success_records_use_and_returns_true(), test_run_improvement_rolls_high_skill_gains_one() (+3 more)

### Community 768 - "test_websocket_handler_error_handling.py"
Cohesion: 0.15
Nodes (13): mock_websocket(), asyncio, fixture, Unit tests for websocket handler error handling. Tests the error handling…, Create a mock WebSocket., Test _send_error_response() successfully sends error., Test _send_error_response() handles WebSocket disconnection., Test _handle_runtime_error() detects WebSocket disconnection. (+5 more)

### Community 769 - ".on_enter_state"
Cohesion: 0.33
Nodes (4): Any, Called whenever state machine enters a new state. Logs state transitions for…, Get connection statistics. Returns: Dictionary with connection metrics AI: For…, State

### Community 770 - "container"
Cohesion: 0.33
Nodes (6): enabled, additionalProperties, description, required, type, container

### Community 771 - "Local Channel System"
Cohesion: 0.40
Nodes (5): Local Channel Sub-Zone Routing, Scenario 10 Local Channel Movement, Scenario 11 Local Channel Errors, Scenario 12 Local Channel Integration, Local Channel System

### Community 772 - "Fix Suppression Alignment"
Cohesion: 0.16
Nodes (21): add_pylint_suppression(), add_ruff_suppression(), _apply_fixes_to_line(), fix_file(), _group_fixes_by_line(), main(), parse_alignment_report(), _parse_file_line_pattern() (+13 more)

### Community 773 - "Identify Critical Code"
Cohesion: 0.15
Nodes (21): analyze_file(), analyze_function(), calculate_complexity(), calculate_priority(), check_file_keywords(), check_function_keywords(), main(), process_ast_functions() (+13 more)

### Community 774 - "AdminActionsLogger"
Cohesion: 0.12
Nodes (17): AdminActionsLogger, Any, datetime, Path, TypedDict, Log a general admin command action., Log permission check attempts. Args: player_name: Name of the player attempting…, Optional fields for teleport action logging. (+9 more)

### Community 775 - "CommunicationIntegrationProtocol"
Cohesion: 0.14
Nodes (10): CombatIntegrationProtocol, CommunicationIntegrationProtocol, Protocol, Protocols for NPC combat and communication integration (used by NPCBase)., Handle NPC death in the combat integration layer., Protocol for communication integration (whisper, room message, handle player…, Send a private whisper from this NPC to a single player., Send a message from this NPC to all players in a room. (+2 more)

### Community 776 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 777 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 778 - "TestCombatParticipantData"
Cohesion: 0.10
Nodes (11): Test CombatParticipantData with high stat values., Test CombatParticipantData allows current_dp to exceed max_dp., Test CombatParticipantData fields can be accessed but are not frozen., Test suite for CombatParticipantData dataclass., Test CombatParticipantData can be created with required fields., Test CombatParticipantData with explicit participant type., Test CombatParticipantData defaults to PLAYER type., Test CombatParticipantData equality comparison. (+3 more)

### Community 779 - "_process_session_dp_decay_and_death"
Cohesion: 0.14
Nodes (19): _handle_player_death_threshold(), _player_in_active_combat(), _process_dead_players(), _process_mortally_wounded_player(), _process_mortally_wounded_players(), _process_mp_regeneration(), _process_passive_lucidity_flux(), _process_session_dp_decay_and_death() (+11 more)

### Community 780 - "CommandRequest"
Cohesion: 0.08
Nodes (25): CommandRequest, get_help_content(), handle_command(), BaseModel, post, Request, Handle incoming HTTP command requests., Get help content for commands. This is a compatibility function that delegates… (+17 more)

### Community 781 - "test_player_repository.py"
Cohesion: 0.04
Nodes (68): _make_mock_row(), mock_player(), player_repository(), asyncio, fixture, UUID, Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes with room cache. (+60 more)

### Community 782 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test _spawn_required_npcs() successfully spawns required NPCs., Test _spawn_required_npcs() handles spawn failures., Test _spawn_optional_npcs() spawns based on probability., Test _spawn_optional_npcs() skips NPCs with low probability., Test _spawn_optional_npcs() handles missing spawn room., Arena pass is skipped when required/optional passes spawned nothing., One arena instance per definition_id present in required/optional spawned_npcs. (+11 more)

### Community 783 - "_occupation_slots_9"
Cohesion: 0.17
Nodes (12): _occupation_slots_9(), Valid 9 slots: one 70, two 60, three 50, three 40; 9 distinct skill_ids (no…, Personal interest with Cthulhu Mythos raises ValueError., personal_interest must have exactly 4 entries., occupation_slots with duplicate skill_id raises ValueError., personal_interest with duplicate skill_id raises ValueError., Occupation and personal interest sharing a skill_id raises ValueError., test_set_player_skills_cthulhu_mythos_in_personal_rejected() (+4 more)

### Community 784 - "UUID"
Cohesion: 0.02
Nodes (58): Any, Player, UUID, Initialize the connection manager with modular components., Get the first WebSocket connection ID for a player (backward compatibility)., Check if a player has any WebSocket connections., Get the number of connections for a player by type., Subscribe a player to a room (compatibility method). (+50 more)

### Community 785 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

### Community 786 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test NPCService initialization., Test get_npc_definitions() handles database errors., Test get_npc_definition() returns definition when found., Test create_npc_definition() raises ValueError for invalid probability., Test update_npc_definition() successfully updates definition., Test update_npc_definition() returns None when not found., Test get_system_statistics() handles database errors. (+7 more)

### Community 787 - "ItemPrototypeModel"
Cohesion: 0.14
Nodes (11): ItemPrototypeModel, BaseModel, field_validator, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validated representation of an item prototype definition. This model keeps the…, Validate that item_type is in the allowed list. Args: value: The item type to…, Validate that all flags are in the allowed list. Args: value: The list of flags… (+3 more)

### Community 788 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (16 total, 14 thin omitted), Community 0 - "Open Mind Circle", Community 1 - "Campaign Materials", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 790 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (6 total, 4 thin omitted), Community 0 - "Solo Investigators", Community 1 - "Design & Authorship", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 791 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (4 total, 1 thin omitted), Community 0 - "Keeper Screen References", Community 1 - "Keeper Screen References (1)", Community 2 - "Keeper Screen References (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12) (+5 more)

### Community 792 - "TestCheckRateLimit"
Cohesion: 0.33
Nodes (4): Test _check_rate_limit function., Test _check_rate_limit returns None when allowed., Test _check_rate_limit returns result when blocked., TestCheckRateLimit

### Community 793 - "Cursor Hooks Record"
Cohesion: 0.15
Nodes (20): _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path(), Any (+12 more)

### Community 794 - "Command Handler Patterns"
Cohesion: 0.29
Nodes (7): Command Handler Patterns, Command Models Reference, Pydantic Command Models, Command Security Guide, Command Role-Based Access Control, Command Testing Guide, Command Test-Driven Development

### Community 795 - "_personal_interest_4"
Cohesion: 0.17
Nodes (12): _personal_interest_4(), Four personal interest (skill_ids only); distinct and no overlap with…, set_player_skills with valid occupation and personal calls delete then…, When Own Language is not in occupation or personal, its value is stats_for_edu., Occupation slot with Cthulhu Mythos (allow_at_creation=False) raises ValueError., occupation_slots not length 9 raises ValueError., occupation_slots with wrong value set (e.g. two 70s) raises ValueError., test_set_player_skills_cthulhu_mythos_in_occupation_rejected() (+4 more)

### Community 796 - "test_profession.py"
Cohesion: 0.11
Nodes (17): Unit tests for the Profession model. Tests the Profession model methods…, Test get_mechanical_effects returns empty dict for invalid value., Test meets_stat_requirements returns False when one requirement is not met., Test meets_stat_requirements returns False when required stat is missing., Test get_requirement_display_text formats single requirement correctly., Test get_stat_requirements returns dict for valid JSON., Test get_requirement_display_text capitalizes stat names., Test get_stat_requirements returns empty dict for invalid JSON. (+9 more)

### Community 797 - "reset_database"
Cohesion: 0.11
Nodes (19): Reset the database connection state (for testing). This resets the…, Reset database URL state for testing. This is a public function to reset the…, reset_database(), _reset_database_url_state(), fixture, Reset database state before each test., Test reset_database resets module-level _database_url., reset_db_state() (+11 more)

### Community 798 - "E 2 E Scenario Scenarios"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 799 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (3 total, 0 thin omitted), Community 0 - "Call of Cthulhu Stat Block; Chaosium Inc.", Community 1 - "Mythos Elements", Community 2 - "Mythos Elements (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12) (+5 more)

### Community 800 - "IdleMovementHandler"
Cohesion: 0.12
Nodes (15): IdleMovementHandler, Check if NPC is in combat via UUID lookup. Args: npc_id: NPC ID (string or…, Check if NPC is in combat via string ID mapping. Args: npc_id: NPC ID as string…, Check if an NPC is currently in combat. Args: npc_instance: The NPC instance to…, Handler for NPC idle movement logic. This class manages the decision-making and…, Subzone boundary validation drops exits that would leave the NPC subzone., Test select_exit() with single exit., Test select_exit() with multiple exits. (+7 more)

### Community 801 - "_should_include_npc"
Cohesion: 0.14
Nodes (14): Check if an NPC should be included in the results (has name and is alive)., _should_include_npc(), Test _should_include_npc() returns True for valid NPC., Test _should_include_npc() returns False when no name., Test _should_include_npc() returns False when not alive., test_should_include_npc(), test_should_include_npc_no_name(), test_should_include_npc_not_alive() (+6 more)

### Community 802 - "test_metrics.py"
Cohesion: 0.03
Nodes (59): Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, Reset all metrics to zero., Performance metrics for NATS Subject Manager operations. Tracks validation…, Record a validation operation. Args: duration: Time taken in seconds success:…, Record a build operation. Args: duration: Time taken in seconds success:…, Record an error occurrence. Args: error_type: Type of error (pattern_not_found,… (+51 more)

### Community 803 - "test_metadata.py"
Cohesion: 0.11
Nodes (15): Shared SQLAlchemy metadata for MythosMUD models. This module provides the…, NPC Database metadata for MythosMUD. This module defines the SQLAlchemy…, Unit tests for metadata modules. Tests the shared SQLAlchemy metadata instances., Test that metadata is a MetaData instance., Test that npc_metadata is a MetaData instance., Test that metadata and npc_metadata are separate instances., Test that Base is a DeclarativeBase subclass., Test that Base has metadata attribute set to shared metadata. (+7 more)

### Community 804 - "lifespan_shutdown.py"
Cohesion: 0.19
Nodes (16): FastAPI, Application shutdown logic. This module handles graceful shutdown of all…, Shutdown event bus and clean up all service subscriptions., Handle graceful shutdown of all services., Shutdown and persist mythos chronicle state., Shutdown NATS message handler if present., Shutdown connection manager if present., Shutdown mythos tick scheduler if present. (+8 more)

### Community 805 - "ErrorContext"
Cohesion: 0.05
Nodes (42): create_error_context(), Any, Request, Create error context from request and user. Helper function to reduce…, Initialize the Pydantic error handler. Args: context: Optional error context…, ErrorContext, Any, Initialize MythosMUD error. Args: message: Technical error message context:… (+34 more)

### Community 806 - "field_validator"
Cohesion: 0.14
Nodes (8): Any, field_validator, Validate schedule entry days are standard English weekday names (Sunday,…, Validate slug-formatted list entries. Args: value: Sequence of strings to…, Ensure the schedule window moves time forward like the Chronology Tablets…, Validate tradition value. Args: value: The tradition string to validate…, Validate season value. Args: value: The season string to validate Returns: str:…, Validate bonus tags format.

### Community 807 - "Invite"
Cohesion: 0.06
Nodes (38): Get all unused invites., Invite, Base, Generate a unique invite code., Model for user registration invites., Check if the invite has expired. Handles naive timestamps as UTC., Check if the invite is valid (active and not expired)., Mark this invite as used by a specific user. (+30 more)

### Community 808 - "Audit Suppressions"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 809 - "Fix Markdown Line"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 810 - "Populate Npc Sample"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 811 - "quest_events.py"
Cohesion: 0.18
Nodes (15): _entity_id_for_quest_offer(), _make_on_npc_died(), _make_on_player_entered(), _make_on_player_left(), _parse_player_id(), Any, UUID, Quest event subscriptions: room entry (trigger start), room exit… (+7 more)

### Community 812 - "._error_callback"
Cohesion: 0.50
Nodes (3): Exception, Handle NATS errors. AI: Runs as fire-and-forget async task to prevent blocking…, Async handler for NATS connection errors.

### Community 813 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 814 - "AsciiMapRenderer"
Cohesion: 0.15
Nodes (11): AsciiMapRenderer, Renders ASCII maps from room coordinate data. Supports multiple map styles…, Initialize the ASCII map renderer., Tests for _vertical_exit_char_between (|, v, ^)., Bidirectional vertical exit renders as a vertical bar., One-way south exit renders as a lowercase 'v'., One-way north exit renders as a caret., When there are no vertical exits, the helper returns None. (+3 more)

### Community 815 - "test_inventory_mutation_guard_error_handling.py"
Cohesion: 0.13
Nodes (17): guard(), asyncio, fixture, Unit tests for inventory mutation guard - error handling and monitoring. Tests…, Test acquire_async handles record_custom_alert with message parameter., Test acquire handles TypeError from record_custom_alert and uses fallback., Test acquire_async handles TypeError from record_custom_alert and uses fallback., Create an InventoryMutationGuard instance. (+9 more)

### Community 816 - ".__call__"
Cohesion: 0.40
Nodes (3): LiabilityStackEntry, Decode stored liability text (or empty state) into stack rows., Encode stack rows into JSON suitable for PlayerLucidity.liabilities.

### Community 817 - "NATSSubjectManager"
Cohesion: 0.05
Nodes (34): get_subject_manager_dependency(), Dependency function to inject NATSSubjectManager. Returns: Global…, Initialize combat event publisher. Args: nats_service: NATS service instance…, NATSSubjectManager, Any, Build a NATS subject from a pattern and parameters. Args: pattern_name: Name of…, Ensure pattern exists in registry. Args: pattern_name: Name of the pattern to…, Ensure all required parameters are provided. Args: pattern_name: Name of the… (+26 more)

### Community 818 - "Package Scripts Build"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 819 - "test_game_enums.py"
Cohesion: 0.14
Nodes (13): Unit tests for game model enums. Tests AttributeType, StatusEffectType, and…, Test PositionState enum contains all expected states., Test AttributeType enum contains expected values., Test AttributeType enum contains all expected types., Test StatusEffectType enum contains expected values., Test StatusEffectType enum contains all expected types., Test PositionState enum contains expected values., test_attribute_type_enum_all_types() (+5 more)

### Community 820 - "Tsconfig Node"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 821 - "validate_shutdown_admin_permission"
Cohesion: 0.22
Nodes (8): Validate that a player has admin permissions for server shutdown. Args: player:…, validate_shutdown_admin_permission(), Test validate_shutdown_admin_permission() returns False when player is None., Test validate_shutdown_admin_permission() returns False when player is not…, Test validate_shutdown_admin_permission() returns True when player is admin., test_validate_shutdown_admin_permission_admin(), test_validate_shutdown_admin_permission_no_player(), test_validate_shutdown_admin_permission_not_admin()

### Community 822 - "test_npc_service.py"
Cohesion: 0.14
Nodes (13): Unit tests for NPC service. Tests the NPCService class., Test get_npc_definition() returns None when not found., Test get_npc_definition() handles errors., Test create_npc_definition() raises ValueError for invalid type., Test create_npc_definition() raises ValueError for invalid max population., Test get_spawn_rules() handles database errors., Test delete_spawn_rule() returns False when not found., test_create_npc_definition_invalid_max_population() (+5 more)

### Community 823 - "connectionStore.ts"
Cohesion: 0.21
Nodes (11): ConnectionActions, ConnectionHealth, ConnectionMetadata, ConnectionSelectors, ConnectionState, ConnectionStore, createInitialState(), GameEvent (+3 more)

### Community 825 - "persistence/container_helpers.py"
Cohesion: 0.18
Nodes (16): Composed, build_update_query(), _coerce_row_quantity(), fetch_container_items(), _item_dict_from_contents_row(), _metadata_dict_from_cell(), datetime, PsycopgConnection (+8 more)

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

### Community 830 - "ScheduleCollection"
Cohesion: 0.15
Nodes (15): extract_observance_ids(), BaseModel, Calendar ingestion schemas for MythosMUD. These models provide a typed wrapper…, Wrapper around an array of schedule entries., Normalize document observance names into snake_case ids., Parse table rows from MYTHOS_HOLIDAY_CANDIDATES.md into slug ids., ScheduleCollection, slugify_observance() (+7 more)

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

### Community 835 - "AppConfig"
Cohesion: 0.02
Nodes (131): _create_config_instance(), _get_config_cached(), _get_config_test(), Configuration module for MythosMUD server. This module provides type-safe,…, Create a new AppConfig instance from current environment. This is a helper…, Production config loader with caching. Uses both @lru_cache and global…, Test config loader without caching - always returns fresh instances. This…, AppConfig (+123 more)

### Community 836 - "Lint Logging Patterns"
Cohesion: 0.11
Nodes (15): FormattedValue, lint_file(), LoggingPatternLinter, main(), Call, Import, ImportFrom, Path (+7 more)

### Community 837 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 838 - "Local Readme Motd"
Cohesion: 0.18
Nodes (14): Arkham City Graph PNG, Arkham City PDF Map, Arkham City (MOTD Zone), Welcome to the Dreamlands, Innsmouth (MOTD Zone), Katmandu, MythosMUD Message of the Day, The Yellow Sign (+6 more)

### Community 839 - "UI/UX Considerations"
Cohesion: 0.40
Nodes (5): 1. Visual Distinction, 2. Panel Positioning, 3. Responsive Design, 4. Accessibility, UI/UX Considerations

### Community 840 - "Any"
Cohesion: 0.12
Nodes (10): Any, Record a combat error. Args: error_type: Type of error (validation, timeout,…, Get metrics history. Args: limit: Optional limit on number of records Returns:…, Get active alerts. Returns: List[Dict[str, Any]]: Active alerts, Get all alerts. Returns: List[Dict[str, Any]]: All alerts, Get monitoring summary. Returns: Dict[str, Any]]: Monitoring summary, Check if error threshold has been exceeded., Convenience function to record combat error. Args: error_type: Type of error… (+2 more)

### Community 841 - "Middleware Command Rate"
Cohesion: 0.10
Nodes (12): CommandRateLimiter, Any, datetime, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate…, Remove timestamp data for players who haven't been active recently. Prevents… (+4 more)

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

### Community 846 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test unsubscribe_from_event_subjects handles partial success., Test cleanup_empty_subzone_subscriptions handles NATSError., Test _handle_player_attacked_event delegates to event handler., Test unsubscribe_from_subzone handles not subscribed case., Test _handle_event_message delegates to event handler. (+9 more)

### Community 847 - "MagicServiceHealingMixin"
Cohesion: 0.23
Nodes (10): MagicServiceHealingMixin, Any, UUID, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or…, True if effect result indicates healing was applied (success, effect_applied,… (+2 more)

### Community 848 - "Any"
Cohesion: 0.17
Nodes (9): Any, UUID, Gain occult knowledge (with lucidity loss). Args: player_id: The player's ID…, Heal a player's health. Args: player_id: The player's ID (UUID) amount: Amount…, Damage a player's health. Args: player_id: The player's ID (UUID) amount:…, Initialize with a persistence layer., Apply lucidity loss to a player. Args: player_id: The player's ID (UUID)…, Apply fear to a player. Args: player_id: The player's ID (UUID) amount: Amount… (+1 more)

### Community 849 - "Upgrade Implementation Plan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 850 - "ConnectionMetadata"
Cohesion: 0.17
Nodes (14): ConnectionMetadata, Data models for connection management. This module defines data structures used…, Metadata for tracking connection details in the WebSocket-only system. This…, Unit tests for connection models. Tests the connection_models module classes., Test ConnectionMetadata inequality comparison., Test ConnectionMetadata.__init__() creates metadata with required fields., Test ConnectionMetadata.__init__() with optional fields., Test ConnectionMetadata has all expected dataclass fields. (+6 more)

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
Cohesion: 0.02
Nodes (126): _dispatch_parsed_command(), _handle_processing_error(), _handle_validation_error(), _log_security_sensitive_command(), _parse_command_line_or_client_error(), process_command_with_validation(), CommandExecutionRequest, Exception (+118 more)

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

### Community 876 - ".detect_and_handle_error_state"
Cohesion: 0.20
Nodes (9): Any, UUID, Handle WebSocket-specific errors. Args: player_id: The player's ID…, Handle authentication-related errors. Args: player_id: The player's ID…, Handle security violations. Args: player_id: The player's ID violation_type:…, Attempt to recover from an error state for a player. Args: player_id: The…, Get error handling statistics. Args: online_players: Online players dictionary…, Initialize the error handler. Args: force_disconnect_callback: Callback to… (+1 more)

### Community 877 - "send_system_message"
Cohesion: 0.18
Nodes (15): Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler system message functions. Tests the system…, Create a mock WebSocket., Test send_system_message() successfully sends message. (+7 more)

### Community 878 - "8. Error Handling and Debugging"
Cohesion: 0.67
Nodes (3): 8. Error Handling and Debugging, Common Debug Commands, Test Debugging

### Community 879 - "test_invite_schemas.py"
Cohesion: 0.17
Nodes (15): InviteRead, InviteUpdate, Schema for reading invite data., Schema for updating invite data., Unit tests for invite schemas. Tests the Pydantic models in invite.py module., Test InviteUpdate can be instantiated with all fields optional., Test InviteUpdate validates invite_code length when provided., Test InviteRead can be instantiated. (+7 more)

### Community 880 - "Real-Time Architecture"
Cohesion: 0.33
Nodes (6): Real-Time Architecture, WebSocket and NATS Realtime Stack, ConnectionManager Modular Split, ConnectionManager Refactoring Summary, Structured Concurrency Patterns, Structured Concurrency Task Tracking

### Community 882 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 883 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 884 - "MockEventClass"
Cohesion: 0.12
Nodes (16): MockEventClass, Test EventBus.publish() queues or processes event., Test EventBus.inject() delivers event to subscribers (used by distributed…, Test EventBus.publish() with multiple subscribers., Mock event class for testing., Test _handle_event_async() when no subscribers., Test _handle_event_async() handles sync subscriber errors., Test _handle_event_async() handles async subscriber errors. (+8 more)

### Community 886 - "generate_unique_codes"
Cohesion: 0.38
Nodes (6): generate_invite_code(), generate_unique_codes(), main(), Generate a unique Mythos-themed invite code., Generate a list of unique invite codes and store them in the database., Generate invite codes and store them in the database.

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
Cohesion: 0.08
Nodes (17): NPCMovementIntegration, Room, Get room objects and validate they exist. Args: npc_id: ID of the NPC…, Update room occupancy by removing NPC from source and adding to destination.…, Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…, Move an NPC to a different room with full integration. This method provides…, Publish NPC movement events. Args: npc_id: ID of the NPC from_room_id: Source…, Get the current room ID for an NPC. Args: npc_id: ID of the NPC Returns:… (+9 more)

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

### Community 903 - "combat_helpers.py"
Cohesion: 0.14
Nodes (13): format_combat_status(), Any, Shared helpers and exceptions for combat commands. Extracted from combat.py to…, Produce a human-readable combat status string. This helper is retained for…, Unit tests for combat command helper functions. Tests helper functions in…, Test format_combat_status() formats combat status., Test format_combat_status() handles player not in combat., Test get_combat_target() finds target. (+5 more)

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

### Community 910 - "get_database_path"
Cohesion: 0.13
Nodes (14): get_database_path(), get_database_url(), Path, Get the database file path. DEPRECATED: PostgreSQL does not use file paths.…, Get the database file path (deprecated for PostgreSQL). Returns: Path | None:…, Get the database URL from DatabaseManager. Returns: str | None: The database URL, Test get_database_url initializes database if not already initialized., test_get_database_url_initializes_database() (+6 more)

### Community 911 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 912 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 913 - "test_websocket_handler_validation.py"
Cohesion: 0.20
Nodes (11): mock_validator(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler message validation. Tests the message…, Create a mock WebSocket., Create a mock message validator., Test _validate_message() returns message when validation succeeds. (+3 more)

### Community 914 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

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

### Community 934 - "Schemas Readme"
Cohesion: 0.50
Nodes (4): alias_schema.json, emote_schema.json, Shared JSON schemas, unified_room_schema.json

### Community 935 - "Npc Database"
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

### Community 939 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 940 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Ambiguous Edges - Review These, Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 941 - "test_player_service.py"
Cohesion: 0.14
Nodes (13): Unit tests for player service. Tests the PlayerService class., Test validate_player_name() with name too short., Test heal_player() heals player., Test validate_player_name() with empty string., Test apply_lucidity_loss() when player not found., Test apply_corruption() when player not found., Test heal_player() when player not found., test_apply_corruption_player_not_found() (+5 more)

### Community 942 - "Any"
Cohesion: 0.21
Nodes (8): Any, Create a new party with the given player as leader. Returns dict with success…, Disband a party. If by_player_id is given, only the leader may disband. If…, Safely schedule an async notification, handling cases where no event loop is…, Notify a player they have been removed from a party. Resolves leader name., Remove a player from a party (leave or internal remove). If leader leaves,…, Remove a member from the party. Only the leader may kick., Emit PartyUpdated event if event_bus is set.

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
Nodes (32): main(), Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., _sanitize_token_examples(), _configure_cors(), CORSConfigDict, create_app(), _get_cors_config_from_app_config() (+24 more)

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

### Community 955 - "sample_container"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Test getting container description from equipped item., Create a sample container., Create a sample equipped container item., Create a mock prototype registry., sample_container(), sample_equipped_container() (+1 more)

### Community 956 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 957 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 958 - "main"
Cohesion: 0.67
Nodes (3): main(), Entry point: clear daisy quest instances via anyio., _reset_daisy_quest()

### Community 959 - "start_server.ps1"
Cohesion: 0.50
Nodes (4): Default Server Port 54768, start_local.ps1, start_server.ps1, stop_server.ps1

### Community 960 - "_utc_now"
Cohesion: 0.21
Nodes (12): datetime, Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE…, _utc_now(), Unit tests for lucidity model utility functions. Tests the _utc_now utility…, Test _utc_now returns a datetime object., Test _utc_now returns naive datetime (tzinfo=None)., Test _utc_now returns time close to current UTC time., Test _utc_now returns different times on subsequent calls. (+4 more)

### Community 961 - ".is_alive"
Cohesion: 0.20
Nodes (7): Check if the status effect is still active., Any, Initialize Invite with defaults., _npc_alive_and_active(), setter, Return True if NPC is alive (determination_points > 0)., Allow backward-compatible assignment (npc.is_alive = False).

### Community 962 - "Profession"
Cohesion: 0.13
Nodes (13): Profession, Base, Check if profession is available for player selection., Profession model for game data. Stores profession information including name,…, String representation of the profession., Test set_mechanical_effects handles empty dict., Test meets_stat_requirements returns True when all requirements are met., Test meets_stat_requirements returns True when stats exactly match requirements. (+5 more)

### Community 963 - "UUID"
Cohesion: 0.18
Nodes (6): UUID, Add a player to the room without triggering an event. This method is used for…, Remove a player from the room without triggering an event. This method is used…, Remove a player from the room and trigger event. Args: player_id: The ID of the…, Check if a player is in the room. Args: player_id: The ID of the player to…, Add a player to the room and trigger event. Args: player_id: The ID of the…

### Community 964 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 965 - "Any"
Cohesion: 0.13
Nodes (8): Any, Set profession stat requirements from dictionary., Get profession mechanical effects as dictionary., Set profession mechanical effects from dictionary., Get stat modifiers as list of {stat, value}., Set stat modifiers from list of {stat, value}., Get skill modifiers as list of {skill_key, value}., Set skill modifiers from list of {skill_key, value}.

### Community 966 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test EventBus.shutdown() stops processing., Test EventBus.shutdown() is idempotent., Test _stop_processing() when not running., Test EventBus.shutdown() automatically cleans up all service subscriptions., Test multiple services subscribing to the same event type., Test that service shutdown removes all subscribers for that service. This test…, Integration test: Multiple services subscribing to same events and cleanup.… (+7 more)

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

### Community 973 - "Fix Markdownlint"
Cohesion: 0.18
Nodes (16): fix_blanks_around_fences(), fix_blanks_around_headings(), fix_blanks_around_lists(), fix_fence_language(), fix_file(), fix_line_length(), fix_trailing_punctuation_in_headings(), main() (+8 more)

### Community 974 - "Jackson Linter"
Cohesion: 0.20
Nodes (16): collect_json_files(), _file_appears_binary_or_terminal_output(), _first_fallback_encoding_that_parses(), _is_vscode_jsonc_settings(), main(), Path, Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1…, VS Code allows JSON with Comments in settings.json; stdlib json cannot parse it. (+8 more)

### Community 975 - "Migrate Room Filenames"
Cohesion: 0.19
Nodes (10): main(), Path, Update the room ID in the JSON file to match new naming schema., Execute the migration., Handles migration of room filenames from old to new schema., Initialize the migrator., Parse old filename format to extract components., Discover all room files that need migration. (+2 more)

### Community 976 - "handle_system_command"
Cohesion: 0.24
Nodes (11): handle_system_command(), Any, Broadcast a system-level message via the chat service if available., asyncio, Unit tests for system command handlers. Tests the system command functionality., Test handle_system_command() broadcasts system message., Test handle_system_command() handles missing message., Test handle_system_command() handles missing chat service. (+3 more)

### Community 977 - "FeatureFlagService"
Cohesion: 0.07
Nodes (31): FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature…, Clear the feature flag cache. This should be called when configuration changes… (+23 more)

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

### Community 990 - "Mythosmud Obsidian Wiki"
Cohesion: 0.67
Nodes (3): Delta Green, Expansion Backlog (Raw), Things and Notes to Expand On

### Community 991 - "_errors_len"
Cohesion: 0.17
Nodes (12): _errors_len(), Test _spawn_required_npcs() handles missing spawn room., Test _spawn_required_npcs() handles exceptions during spawning., Narrow spawn/startup result dict for len(results['errors']) without propagating…, Test _spawn_optional_npcs() handles exceptions during spawning., Test spawn_npcs_on_startup() handles exceptions during session processing., Test spawn_npcs_on_startup() handles critical exceptions., test_spawn_npcs_on_startup_critical_exception() (+4 more)

### Community 992 - "🚨 AI ERROR HANDLING"
Cohesion: 0.67
Nodes (3): 🚨 AI ERROR HANDLING, If Multiple Categories Have Issues, If Mypy Still Fails After Fixes

### Community 993 - "Event Ownership Matrix"
Cohesion: 0.25
Nodes (8): Event Ownership Matrix, Event Publishing Layers, Event Subscription Cleanup Patterns, Event Subscription service_id Tracking, Memory Leak Audit Report, Memory Leak Audit Categories, Memory Leak Metrics Usage Guide, Memory Leak Monitoring Endpoints

### Community 994 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 995 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test _send_messages_to_players handles missing original_content., Test _send_messages_to_players adds tags from dampening., Test _send_messages_to_players handles invalid player_id., Test _echo_message_to_sender handles exceptions., Test _apply_dampening_and_send_message handles blocked messages., Test _apply_dampening_and_send_message handles missing original_content., Test _get_player_lucidity_tier handles exceptions during processing. (+7 more)

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

### Community 1003 - "test_skills.py"
Cohesion: 0.10
Nodes (24): get_skills_catalog(), get, Request, Return the skills catalog (base values, allow_at_creation). Cthulhu Mythos is…, Skill catalog API response schemas. Used by GET /v1/skills (or equivalent) for…, Single skill catalog entry., Response model for skills catalog list., SkillData (+16 more)

### Community 1004 - "Cursor Skills Skill"
Cohesion: 0.13
Nodes (16): Tailwind CSS Anti-Pattern Remediation, Adapt Skill, Animate Skill, Arrange Skill, Audit Skill, Bolder Skill, Clarify Skill, Colorize Skill (+8 more)

### Community 1005 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1007 - "skills_commands.py"
Cohesion: 0.24
Nodes (13): _format_skills_output(), _get_container_services(), handle_skills_command(), Any, UUID, Skills command handler (plan 10.7 V4). Returns the active character's skills as…, Get container, persistence, and skill_service from request, or None if…, Extract and validate player_id from player object, returning UUID or None. (+5 more)

### Community 1008 - "handle_explore_command"
Cohesion: 0.27
Nodes (9): handle_explore_command(), Any, Handle exploration requests by returning a simple message. This lightweight…, asyncio, Unit tests for exploration command handlers. Tests the exploration command…, Test handle_explore_command() explores area., Test handle_explore_command() handles missing persistence., test_handle_explore_command() (+1 more)

### Community 1009 - "quest_service.py"
Cohesion: 0.18
Nodes (12): Quest subsystem: service, goal progression, rewards., _build_collect_n_progress(), _collect_goal_prototype_id(), _collect_goal_required_count(), _consume_collect_goals_from_player(), _goal_activity_target(), Quest service: start, progress, complete, turn-in, abandon, and quest log.…, Recompute collect_n goal counters from holdings into a progress dict. (+4 more)

### Community 1010 - "_row_to_profession"
Cohesion: 0.19
Nodes (12): _bool_or_default(), Any, Profession, Get a profession by ID. Args: profession_id: Profession ID Returns: Profession…, Return value as str or a default if falsy., Return text value or default if falsy., Return bool(value) when not None, otherwise default., Map procedure result row to Profession model. (+4 more)

### Community 1011 - "._generate_alert"
Cohesion: 0.17
Nodes (9): AlertSeverity, AlertType, Enum, Update resource usage metrics. Args: memory_mb: Memory usage in MB cpu_percent:…, Alert severity levels., Alert types for combat monitoring., Check resource usage thresholds., Check if performance threshold has been exceeded. (+1 more)

### Community 1012 - "fix_markdown_file"
Cohesion: 0.36
Nodes (8): fix_markdown_file(), fix_multiple_blanks(), main(), parse_markdownlint_output(), Path, Fix multiple consecutive blank lines (MD012). Returns: (new_content,…, Parse markdownlint output to get files with MD012 issues., Fix multiple blank lines in a single markdown file. Returns: (changed,…

### Community 1015 - "Analyze Coverage Gaps"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and…, Write critical files below threshold section. (+7 more)

### Community 1016 - "Apply Arena Seed"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 1019 - "TestCheckAllCommandBlocks"
Cohesion: 0.20
Nodes (6): Test _check_all_command_blocks function., Test _check_all_command_blocks returns block result for catatonia., Test _check_all_command_blocks returns block result for grace period., Test _check_all_command_blocks returns block result for casting., Test _check_all_command_blocks returns None when no blocks., TestCheckAllCommandBlocks

### Community 1021 - "apply_communication_dampening"
Cohesion: 0.33
Nodes (8): apply_communication_dampening(), _apply_receiver_effects(), _apply_sender_effects(), Any, Communication dampening utilities for lucidity system. Implements communication…, Apply communication dampening based on lucidity tiers. Args: message: Original…, Check if shout should be blocked based on tier., should_block_shout()

### Community 1028 - "Aggro and Threat System Design"
Cohesion: 0.40
Nodes (5): Aggro Threat Implementation Plan, Aggro and Threat System Design, Hate List, Aggro Stability Margin, UpdateAggro

### Community 1031 - "NPC Startup Duplication Analysis"
Cohesion: 0.33
Nodes (6): NPC Duplication Bug Fix Plan, NPC Population Field Rename, NPC Lifecycle Manager, NPC Population Controller, NPC Startup Duplication Analysis, NPC Startup Service

### Community 1032 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1033 - "fixture"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request object., Create a mock persistence layer., Create a mock connection manager. (+1 more)

### Community 1038 - "Pre Commit Config"
Cohesion: 0.13
Nodes (15): Bandit configuration, Bandit B101 B105 B106 test skips, Codacy configuration, Enforced coverage gates, Codacy exclude_paths, Lizard CCN and NLOC thresholds, Grype SCA exclude paths, F-string logging anti-pattern detector (+7 more)

### Community 1040 - "fixture"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Create a mock prototype registry., Create a sample room drop item., Create a sample inventory item., Create a sample equipped item., sample_equipped_item(), sample_inventory_item() (+1 more)

### Community 1041 - "_spawn_rule_row"
Cohesion: 0.20
Nodes (10): Test get_spawn_rules() successfully retrieves rules., Test get_spawn_rule() returns rule when found., Test create_spawn_rule() successfully creates rule., Test delete_spawn_rule() successfully deletes rule., Build procedure result row for NPCSpawnRule., _spawn_rule_row(), test_create_spawn_rule_success(), test_delete_spawn_rule_success() (+2 more)

### Community 1042 - "fixture"
Cohesion: 0.22
Nodes (9): mock_persistence(), mock_room_cache(), fixture, Create a mock persistence layer., Create a mock room cache service., Create a RoomService instance with cache., Create a sample room dictionary., room_service_with_cache() (+1 more)

### Community 1050 - "load_motd"
Cohesion: 0.23
Nodes (11): Unit tests for motd_loader utilities. Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+3 more)

### Community 1051 - "MemoryMonitor"
Cohesion: 0.12
Nodes (12): _max_connection_age_seconds(), MemoryMonitor, Any, Get memory-related alerts based on current usage and connection statistics.…, Update the last cleanup time to the current time., Force garbage collection to free memory., Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops., Monitor memory usage and trigger cleanup when needed. This class provides… (+4 more)

### Community 1052 - "Security Infrastructure"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters). Args:…, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 1054 - ".select_exit"
Cohesion: 0.18
Nodes (6): _cfg_bool(), Calculate weight for an exit based on distance from spawn. Args:…, Calculate weights for all exits. Args: valid_exits: Dictionary of direction ->…, Select exit based on weighted probabilities. Args: exit_weights: List of…, Select an exit using weighted random selection favoring exits closer to spawn…, Calculate approximate distance between two rooms. This is a simplified distance…

### Community 1055 - "test_utility_commands_whoami.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for utility command handlers. Tests the whoami command functionality., Test handle_whoami_command() returns player information., Test handle_whoami_command() handles missing persistence., Test handle_whoami_command() handles player not found., test_handle_whoami_command(), test_handle_whoami_command_no_persistence(), test_handle_whoami_command_player_not_found()

### Community 1056 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1058 - "SecureBaseModel"
Cohesion: 0.25
Nodes (8): Pydantic schemas for Invite model. This module defines Pydantic schemas for…, Pydantic schemas for User model. This module defines Pydantic schemas for user…, BaseModel, Base Pydantic model classes for MythosMUD schemas. This module provides base…, Base model with standard security configuration. All models that handle user…, Base model for API response schemas. Response models may need additional…, ResponseBaseModel, SecureBaseModel

### Community 1065 - "npc_service"
Cohesion: 0.22
Nodes (9): mock_session(), npc_service(), fixture, Create a mock AsyncSession., Create NPCService instance., Create a sample NPC definition., Create a sample spawn rule., sample_npc_definition() (+1 more)

### Community 1066 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 1067 - "test_error_logging.py"
Cohesion: 0.25
Nodes (7): Unit tests for error_logging utilities. Tests error logging helper functions., Test create_error_context() creates error context., Test create_error_context() can include metadata., Test error context to_dict() method., test_create_error_context(), test_create_error_context_with_metadata(), test_error_context_to_dict()

### Community 1068 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 1069 - "monitoring_service"
Cohesion: 0.25
Nodes (8): mock_combat_config(), mock_config(), mock_feature_flags(), monitoring_service(), fixture, Create mock feature flags., Create mock combat config., Create CombatMonitoringService instance with mocked dependencies.

### Community 1070 - "._attack_target_impl"
Cohesion: 0.20
Nodes (5): Resolve attack_damage from behavior config with robust typing., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target., Attack a specific target., Handle attacking target action.

### Community 1071 - "CombatConfigurationScope"
Cohesion: 0.22
Nodes (8): CombatConfigurationError, CombatConfigurationScope, Enum, Exception, Clear configuration override for a specific scope. Args: scope: Configuration…, Exception raised for combat configuration errors., Scope for combat configuration changes., Unit tests for combat configuration service. Tests the…

### Community 1072 - "Standardize Room Names"
Cohesion: 0.21
Nodes (14): load_room_file(), main(), process_room_files(), Path, Load a room file safely., Save a room file safely., Convert room ID to lowercase., Convert filename to lowercase. (+6 more)

### Community 1073 - "Validate Codacy Coverage"
Cohesion: 0.25
Nodes (14): cobertura_has_server_sources(), cobertura_root_line_rate(), lcov_aggregate_hits(), main(), _parse_cobertura_xml(), Path, Parse Cobertura XML with defusedxml (lazy import: LCOV-only runs skip this…, Return root line-rate from Cobertura XML (0.0--1.0). (+6 more)

### Community 1074 - "Check No Production"
Cohesion: 0.18
Nodes (15): _load_checker(), _NoProductionAssertModule, Path, Protocol, Tests for scripts/check_no_production_assert.py., Verify no-production-assert hook targets server code and excludes tests., Public surface of check_no_production_assert loaded via importlib., test_find_assert_line_numbers_detects_assert() (+7 more)

### Community 1075 - "PrototypeRegistryError"
Cohesion: 0.29
Nodes (6): PrototypeRegistryError, Exception, Get a prototype by ID. Args: prototype_id: The ID of the prototype to retrieve…, Raised when prototype registry lookups fail., When prototype is not found, returns None., test_weapon_from_prototype_registry_missing_prototype_returns_none()

### Community 1076 - "dummy_request"
Cohesion: 0.25
Nodes (8): dummy_request(), fakerandom(), Any, fixture, Provide deterministic random seed for unit tests., Provide a minimal request object for testing with container support., Provide a mock ApplicationContainer for testing. This fixture creates a…, test_container()

### Community 1077 - "TestResolveExitTarget"
Cohesion: 0.20
Nodes (6): Room without a reverse exit is not considered bidirectional., If the target room ID does not exist, the helper returns None., If the target room lacks map coordinates, the helper returns None., Tests for _resolve_exit_target., Room with a reverse exit is treated as bidirectional and returns its…, TestResolveExitTarget

### Community 1078 - "TestHorizontalExitCharBetween"
Cohesion: 0.20
Nodes (6): Tests for _horizontal_exit_char_between (em dash, >, <)., Bidirectional horizontal exit between two rooms uses an em dash., One-way east exit renders as a greater-than sign., One-way west exit renders as a less-than sign., When there are no horizontal exits, the helper returns None., TestHorizontalExitCharBetween

### Community 1079 - ".call"
Cohesion: 0.22
Nodes (5): _CircuitBreakerResult, Execute function with circuit breaker protection. Args: func: Function to…, Handle successful operation., Handle failed operation., Check if circuit breaker should attempt reset.

### Community 1080 - ".check_and_interrupt_rest"
Cohesion: 0.25
Nodes (6): AppWithState, Check if player is resting or in login grace period, interrupt rest if needed.…, Get player data and room, returning error dict if any step fails. Public API., Check if player is resting or in login grace period, interrupt rest if needed., Resolve persistence from app (container preferred, then app.state). Returns…, Get player data and room, returning error dict if any step fails.

### Community 1081 - "UUID"
Cohesion: 0.22
Nodes (5): UUID, Apply healing to a player by id., Apply typed damage to a player; returns damage result payload., Load player by id; None if missing., Return registry string id for npc_uuid, or None if unmapped.

### Community 1084 - ".load_file"
Cohesion: 0.22
Nodes (7): Path, Load holiday collection from JSON file., Load schedule collection from a JSON file. Args: path: Path to the JSON file…, Test HolidayCollection.load_file() loads from JSON., Test ScheduleCollection.load_file() loads from JSON., test_holiday_collection_load_file(), test_schedule_collection_load_file()

### Community 1085 - "test_npc_event_handlers.py"
Cohesion: 0.03
Nodes (79): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers. Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON. (+71 more)

### Community 1086 - "fixture"
Cohesion: 0.29
Nodes (4): fixture, Create a mock psycopg2 connection., Create a mock psycopg2 cursor., Create a mock psycopg2 cursor.

### Community 1087 - "AGENTS.md agent instructions"
Cohesion: 0.08
Nodes (24): AGENTS.md agent instructions, COPPA compliance requirements, Obsidian LLM wiki permanent memory, One server only rule, PostgreSQL procedures/functions access, Server authority rule, CLAUDE.md agent router, Contributor Covenant Code of Conduct (+16 more)

### Community 1088 - "._get_vertical_exit_char"
Cohesion: 0.22
Nodes (6): _ExitRowContext, NamedTuple, Render a single row of vertical exits between room rows., Viewport and style context for vertical exit row rendering., Return the vertical exit character (|, v, or ^) given south/north exit state,…, Get exit character to display between rows for vertical (north/south) exits.…

### Community 1089 - "Architecture Decisions Adr"
Cohesion: 0.20
Nodes (10): ADR-013 Pydantic BaseSettings Configuration, ADR-014 NATS Circuit Breaker and DLQ, Dead Letter Queue, db/procedures Stored Functions, ADR-015 PostgreSQL Procedures Migration, ADR-016 Aggro Threat Management, Room-Based Combat Aggro, ADR-017 AST Console Pruning (+2 more)

### Community 1090 - "Fixture Optimization Complete"
Cohesion: 0.67
Nodes (3): E2E Testing Setup Status, Fixture Optimization Complete, Test Suite Post-Merge Refactoring

### Community 1091 - "fixture"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_persistence(), fixture, Create a mock connection manager., Create a mock persistence layer., Create sample container data for testing., Create a ContainerComponent from sample data., sample_container_component() (+1 more)

### Community 1092 - "asyncio"
Cohesion: 0.22
Nodes (9): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success(), test_request_party_invite_creates_pending() (+1 more)

### Community 1093 - "Check No Production"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 1094 - "event_handler"
Cohesion: 0.22
Nodes (9): event_handler(), mock_connection_manager(), mock_event_bus(), mock_task_registry(), fixture, Create a mock EventBus., Create a mock ConnectionManager., Create a mock TaskRegistry. (+1 more)

### Community 1095 - "overrides"
Cohesion: 0.11
Nodes (18): overrides, @asyncapi/generator, @asyncapi/generator-components, @asyncapi/generator-helpers, @asyncapi/specs, fast-uri, flatted, glob (+10 more)

### Community 1096 - "test_ascii_map_renderer_exits.py"
Cohesion: 0.22
Nodes (7): fixture, Unit tests for AsciiMapRenderer exit character and exit resolution. Guards…, Viewport bounds: return None when next cell is outside viewport., Returns None when the next horizontal cell lies at or beyond the viewport's…, Return a fresh AsciiMapRenderer instance for each test., renderer(), TestGetHorizontalExitCharViewportBounds

### Community 1097 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 1098 - "Cursor Workflows"
Cohesion: 0.22
Nodes (9): Cursor Agent CLI, Cursor CLI, Cursor Hooks, Cursor Lifecycle Hooks, Cursor Setup Guide, Cursor Subagents, Built-in Explore Bash Browser Subagents, Cursor Workflows (+1 more)

### Community 1099 - "test_ascii_map_renderer_grid.py"
Cohesion: 0.22
Nodes (7): fixture, Unit tests for AsciiMapRenderer grid building. Guards against regressions in…, Return a fresh AsciiMapRenderer instance for each test., Tests for _build_grid player marker when multiple rooms share coordinates., Multiple rooms at same (x,y): cell keeps player marker even if player room is…, renderer(), TestBuildGridPlayerMarker

### Community 1100 - "calculate_notification_times"
Cohesion: 0.25
Nodes (8): calculate_notification_times(), Calculate notification times for countdown. Notifications occur: - Every 10…, Test calculate_notification_times() for short countdown., Test calculate_notification_times() for long countdown., Test calculate_notification_times() returns sorted descending., test_calculate_notification_times_long(), test_calculate_notification_times_short(), test_calculate_notification_times_sorted()

### Community 1101 - "SQLAlchemy Async Best Practices"
Cohesion: 1.00
Nodes (3): SQLAlchemy Async Best Practices, SQLAlchemy text() Async Usage, SQLAlchemy Code Review

### Community 1102 - "E 2 E Load Analyze"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 1103 - ".handle_attack_command"
Cohesion: 0.25
Nodes (5): Any, Extract command type and target name from command_data. Public API., Extract command type and target name from command_data., Handle attack commands (attack, punch, kick, etc.)., Handle /flee command: leave combat and move to random adjacent room.

### Community 1104 - "fixture"
Cohesion: 0.25
Nodes (8): mock_container_service(), mock_persistence(), mock_request(), mock_user(), fixture, Create a mock request object., Create a mock persistence layer., Create a mock container service.

### Community 1105 - "_send_combat_participant_updates"
Cohesion: 0.25
Nodes (6): _participant_key_strings(), Handle combat_started event., Handle combat_ended event., Keys from a participants mapping (NATS may send dict-like payloads)., Push player_update to each combat participant (in_combat flag)., _send_combat_participant_updates()

### Community 1106 - ".__init__"
Cohesion: 0.25
Nodes (5): Any, UUID, Separate occupants into players, NPCs, and all occupants lists. Args:…, Initialize the room occupant manager. Args: connection_manager:…, Get the list of occupants in a room. Args: room_id: The room ID…

### Community 1107 - "InviteBase"
Cohesion: 0.25
Nodes (8): InviteBase, Base invite schema with common fields., Test InviteBase can be instantiated., Test InviteBase has correct default values., Test InviteBase validates invite_code length., test_invite_base(), test_invite_base_defaults(), test_invite_base_validation()

### Community 1108 - ".perform_recovery_action"
Cohesion: 0.32
Nodes (5): Any, UUID, Perform a recovery action and enforce cooldowns., Fetch the cooldown record for a recovery action., Apply LCD loss for a Mythos encounter.

### Community 1109 - ".respawn_player_by_user_id"
Cohesion: 0.29
Nodes (4): Any, Respawn a delirious player by user ID. This method handles the complete…, Initialize with a persistence layer., Respawn a dead player by user ID. This method handles the complete respawn…

### Community 1110 - ".profession_to_dict"
Cohesion: 0.38
Nodes (4): Any, Convert a Profession model to a dictionary for API responses. Args: profession:…, Get all available professions as dictionaries. Returns: list[dict[str, Any]]:…, Get a profession by ID as a dictionary. Args: profession_id: Profession ID…

### Community 1111 - "bind_request_context"
Cohesion: 0.04
Nodes (46): correct_request_context(), Demonstrate correct request context binding., process_websocket_message(), websocket, WebSocket endpoint with enhanced logging., Simulate WebSocket message processing., websocket_endpoint(), migration_example_5() (+38 more)

### Community 1112 - ".__init__"
Cohesion: 0.38
Nodes (4): Any, Initialize LucidityAdjustmentLog with defaults., Initialize LucidityExposureState with defaults., Initialize PlayerLucidity with defaults.

### Community 1113 - "Alert"
Cohesion: 0.29
Nodes (4): Alert, Convert to dictionary., Add alert callback function. Args: callback: Function to call when alert is…, Remove alert callback function. Args: callback: Function to remove

### Community 1114 - "mock_async_persistence"
Cohesion: 0.29
Nodes (7): mock_async_persistence(), mock_combat_service(), mock_connection_manager(), fixture, Create a mock ConnectionManager for integration testing., Create a mock async persistence layer., Create a mock combat service.

### Community 1115 - "mock_app"
Cohesion: 0.29
Nodes (7): mock_app(), mock_container(), mock_player(), fixture, Create a mock FastAPI app., Create a mock ApplicationContainer., Create a mock player.

### Community 1116 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1117 - "mock_connection_manager"
Cohesion: 0.29
Nodes (7): mock_connection_manager(), mock_persistence(), mock_request(), fixture, Create a mock ConnectionManager., Create a mock persistence layer., Create a mock FastAPI request.

### Community 1118 - "add_suppression_to_file"
Cohesion: 0.47
Nodes (5): add_suppression_to_file(), main(), Path, Add suppression comment to a PowerShell file if it uses Write-Host and doesn't…, Process all PowerShell scripts in the scripts directory.

### Community 1119 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1120 - "Check Logging Patterns"
Cohesion: 0.20
Nodes (11): find_fstring_logging_violations(), format_violation_report(), FStringLoggingDetector, main(), Call, Path, Main function to scan files and report violations., AST visitor to detect f-string logging violations. (+3 more)

### Community 1121 - "Lint Sql Guardrails"
Cohesion: 0.23
Nodes (13): check_not_in_subquery(), check_select_star(), _collect_sql_files(), main(), Path, Lightweight guardrails for hand-maintained PostgreSQL SQL. Warns on: - select *…, Return line with line comment removed (-- ...)., Return content with block comments /* ... */ removed (simple, no nested). (+5 more)

### Community 1122 - "mock_persistence"
Cohesion: 0.29
Nodes (7): mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request with app state and container., Create a mock persistence., Create a mock player.

### Community 1123 - "asyncio"
Cohesion: 0.29
Nodes (7): asyncio, Test cleanup_stale_combats handles missing end_combat method., Test cleanup_stale_combats when no stale combats exist., Test cleanup_stale_combats removes stale combats., test_cleanup_stale_combats(), test_cleanup_stale_combats_no_end_combat_method(), test_cleanup_stale_combats_no_stale_combats()

### Community 1124 - ".auto_progression_enabled"
Cohesion: 0.29
Nodes (5): setter, Return whether auto-progression is enabled., Enable or disable combat auto-progression., Return the turn interval in seconds., Set the turn interval in seconds.

### Community 1125 - "📊 LINT ISSUE CATEGORIZATION GUIDE"
Cohesion: 0.67
Nodes (3): 📊 LINT ISSUE CATEGORIZATION GUIDE, Python/Ruff Error Codes, React/ESLint Error Codes

### Community 1127 - "graceful_degradation"
Cohesion: 0.33
Nodes (4): graceful_degradation(), Context manager for graceful degradation. Provides fallback behavior when…, Test graceful_degradation with successful operation., Test graceful_degradation catches exceptions.

### Community 1129 - ".get_stat_requirements"
Cohesion: 0.33
Nodes (3): Check if given stats meet the profession requirements. Args: stats: Dictionary…, Get formatted text for displaying stat requirements. Returns: Formatted string…, Get profession stat requirements as dictionary.

### Community 1131 - ".handle_player_message"
Cohesion: 0.33
Nodes (3): Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…, Process a message to determine if the NPC should respond. Args: npc_id: ID of…, Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the…

### Community 1132 - "schemas/auth/__init__.py"
Cohesion: 0.33
Nodes (5): Auth domain schemas: user and invite., Schema for reading user data., UserRead, Test UserRead can be instantiated., test_user_read()

### Community 1133 - "InviteCreate"
Cohesion: 0.33
Nodes (6): InviteCreate, Schema for creating a new invite., Test InviteCreate can be instantiated., Test InviteCreate can be instantiated without expiry., test_invite_create(), test_invite_create_no_expiry()

### Community 1134 - "TestGetExitEntriesForRoom"
Cohesion: 0.33
Nodes (4): Tests for _get_exit_entries_for_room., Valid exits for a room produce one entry with correct direction and coordinates., Exits whose targets are missing are skipped when building exit entries., TestGetExitEntriesForRoom

### Community 1135 - "quest_service"
Cohesion: 0.29
Nodes (7): mock_def_repo(), mock_instance_repo(), fixture, quest_service(), Mock QuestDefinitionRepository., Mock QuestInstanceRepository., QuestService with mocked repos.

### Community 1140 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1141 - "test_nats_service_init_with_subject_manager"
Cohesion: 0.20
Nodes (6): Test NATSService initialization with None config., Test NATSService initialization with subject manager., Test NATSService initializes message batching structures., test_nats_service_init_message_batch(), test_nats_service_init_with_none(), test_nats_service_init_with_subject_manager()

### Community 1144 - "idle_movement_handler"
Cohesion: 0.29
Nodes (7): idle_movement_handler(), mock_event_bus(), mock_persistence(), fixture, Create a mock persistence layer., Create a mock event bus., Create an IdleMovementHandler instance.

### Community 1145 - "Knip Entry Ignore Dependencies"
Cohesion: 0.08
Nodes (25): entry, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries, dependencies (+17 more)

### Community 1146 - "dependencies"
Cohesion: 0.08
Nodes (25): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-resizable, react-rnd (+17 more)

### Community 1150 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test _ensure_room_cache_loaded returns early when cache is already loaded., Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…, Test _ensure_room_cache_loaded handles DatabaseError gracefully., Test _ensure_room_cache_loaded handles OSError gracefully., Test _ensure_room_cache_loaded handles RuntimeError gracefully., test_ensure_room_cache_loaded_already_loaded(), test_ensure_room_cache_loaded_concurrent_load() (+3 more)

### Community 1151 - "persistence_handler"
Cohesion: 0.33
Nodes (6): mock_combat_service(), mock_player(), persistence_handler(), fixture, Create mock combat service., Create CombatPersistenceHandler instance.

### Community 1152 - "MagicPointsMeter.tsx"
Cohesion: 0.53
Nodes (4): formatDelta(), MagicPointsMeter, MagicPointsMeterProps, MagicPointsStatus

### Community 1153 - "Azotottal.md"
Cohesion: 0.33
Nodes (3): Azotottal, Comte Fenalik, The Old Gods (nameless patrons)

### Community 1154 - ".get_professions"
Cohesion: 0.40
Nodes (3): Profession, Get all available professions using SQLAlchemy ORM., Get a profession by ID. Delegates to ProfessionRepository.

### Community 1157 - ".validate_target_player"
Cohesion: 0.40
Nodes (3): field_validator, Validate optional modifier for the lie command., Validate the target player name using shared validation rules.

### Community 1158 - "_EventBusPublishPort"
Cohesion: 0.40
Nodes (4): _EventBusPublishPort, Protocol, Minimal surface for publishing domain events from ConnectionManager.event_bus., Publish a single event to the in-process bus.

### Community 1159 - "Mythosmud Obsidian Sources"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1160 - "test_cold_damage_resistance_reduces_damage"
Cohesion: 0.40
Nodes (5): asyncio, Cold resistance should reduce incoming cold-type damage before persistence., Missing current_dp should use base investigator fallback to avoid inflated…, test_cold_damage_resistance_reduces_damage(), test_damage_defaults_current_dp_to_20_when_missing()

### Community 1161 - "test_filter_other_players_adds_linkdead_indicator"
Cohesion: 0.40
Nodes (5): asyncio, Test _filter_other_players() adds (linkdead) indicator for grace period players., Test _filter_other_players() does not add (linkdead) when player not in grace…, test_filter_other_players_adds_linkdead_indicator(), test_filter_other_players_no_linkdead_when_not_in_grace_period()

### Community 1162 - "persistence_handler"
Cohesion: 0.40
Nodes (5): mock_combat_service(), persistence_handler(), fixture, Create mock combat service., Create CombatPersistenceHandler instance.

### Community 1163 - "registry_with_switchblade"
Cohesion: 0.40
Nodes (5): fixture, Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade)., PrototypeRegistry containing only the switchblade., registry_with_switchblade(), switchblade_prototype()

### Community 1164 - "player_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), player_service(), fixture, Create a mock persistence layer., Create a PlayerService instance.

### Community 1165 - "nats_broker"
Cohesion: 0.40
Nodes (5): nats_broker(), nats_config(), fixture, Create a NATSConfig instance., Create a NATSMessageBroker instance.

### Community 1166 - "exploration_service"
Cohesion: 0.40
Nodes (5): exploration_service(), mock_database_manager(), fixture, Create a mock database manager., Create an ExplorationService instance.

### Community 1167 - ".sample_holidays"
Cohesion: 0.40
Nodes (3): fixture, Create a mock chronicle for testing., Create sample holiday entries for testing.

### Community 1168 - "webhook"
Cohesion: 0.50
Nodes (4): post, Request, Receive and log alert webhooks, webhook()

### Community 1169 - "nats_service"
Cohesion: 0.40
Nodes (5): nats_config(), nats_service(), fixture, Create a NATSConfig instance., Create a NATSService instance.

### Community 1170 - "Schemas Intersection Schema"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 1171 - "Schemas Room Schema"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 1172 - "properties"
Cohesion: 0.11
Nodes (19): description, items, type, default, description, maximum, minimum, type (+11 more)

### Community 1173 - "Arkham Rooms Summary"
Cohesion: 0.22
Nodes (12): analyze_connectivity(), generate_dot_file(), load_room_data(), main(), print_detailed_statistics(), print_room_listing(), Print a detailed listing of all rooms by subzone., Load all room and intersection data from the zone directory. (+4 more)

### Community 1174 - "Fix Markdownlint Errors"
Cohesion: 0.22
Nodes (12): fix_md001_heading_increment(), fix_md013_line_length(), fix_md041_first_line_heading(), fix_md051_link_fragments(), main(), parse_errors(), Fix MD001: Heading levels should only increment by one level at a time., Parse markdownlint output file and extract errors. (+4 more)

### Community 1175 - "Fix Syntax Errors"
Cohesion: 0.22
Nodes (8): main(), Path, Process multiple files and return statistics., Main function to run the syntax error fixer., Tool to fix syntax errors introduced by automated f-string remediation., Fix malformed logger calls with broken syntax., Fix syntax errors in a specific file., SyntaxErrorFixer

### Community 1176 - "user_manager"
Cohesion: 0.40
Nodes (5): mock_data_dir(), fixture, Create a temporary data directory., Create a UserManager instance., user_manager()

### Community 1178 - "CombatAuditLogger"
Cohesion: 0.05
Nodes (59): CombatAttackDetails, CombatAuditLogger, CombatMonitoringAlert, CombatParties, CombatSecurityEvent, Any, datetime, Combat-specific audit logging and monitoring. This module provides specialized… (+51 more)

### Community 1186 - "get_combat_monitoring"
Cohesion: 0.50
Nodes (4): get_combat_monitoring(), Get the global combat monitoring service instance. Returns:…, Test get_combat_monitoring returns global instance., test_get_combat_monitoring()

### Community 1187 - "test_mp_regeneration_service.py"
Cohesion: 0.04
Nodes (63): mock_player(), mock_player_service(), mp_regeneration_service(), asyncio, fixture, Unit tests for MP regeneration service. Tests the MPRegenerationService class…, Test process_tick_regeneration() accumulates fractional MP., Test _get_regen_multiplier() returns 1.0 for standing position. (+55 more)

### Community 1189 - "description"
Cohesion: 0.67
Nodes (3): minLength, type, description

### Community 1190 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 1191 - "applies_to"
Cohesion: 0.67
Nodes (3): minItems, type, applies_to

### Community 1192 - "metadata"
Cohesion: 0.67
Nodes (3): additionalProperties, type, metadata

### Community 1197 - "Mythosmud Obsidian Readme"
Cohesion: 0.50
Nodes (4): LLM Wiki Vault Schema, Raw Sources Layer, Wiki Layer, Wiki Page Template

### Community 1200 - "mock_lifecycle_manager"
Cohesion: 0.50
Nodes (4): mock_lifecycle_manager(), mock_npc(), fixture, Create a mock lifecycle manager.

### Community 1202 - "Nameless Horrors - 2nd Edition (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extractions pages, Nameless Horrors - 2nd Edition (source summary)

### Community 1203 - "S. Petersen's Field Guide to Lovecraftian Horrors (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extrated pages, S. Petersen's Field Guide to Lovecraftian Horrors (source summary)

### Community 1209 - "get_alerts"
Cohesion: 0.40
Nodes (5): get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing)

### Community 1213 - "mock_persistence"
Cohesion: 0.67
Nodes (3): mock_persistence(), fixture, Async persistence mock with player/room lookups wired for handler tests.

### Community 1215 - "event_bus"
Cohesion: 0.67
Nodes (3): event_bus(), fixture, Create an EventBus instance.

### Community 1217 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test broadcast_combat_death broadcasts death event., Test broadcast_combat_ended broadcasts combat ended event., Test broadcast_player_respawn broadcasts respawn message., Test broadcast_combat_attack without attacker_id., Test broadcast_player_death handles personal message errors., Test broadcast_combat_start broadcasts combat start event., test_broadcast_combat_attack_no_attacker_id() (+5 more)

### Community 1220 - "E 2 E Scenarios Scenario"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1221 - "party_service"
Cohesion: 0.67
Nodes (3): party_service(), fixture, PartyService with no dependencies (in-memory only).

### Community 1222 - "mock_connection_manager"
Cohesion: 0.67
Nodes (3): mock_connection_manager(), fixture, Create a mock ConnectionManager for testing.

### Community 1223 - "Grype Command Handle Result"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1224 - "Visualize Arkham Rooms"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1225 - "test_get_player_combat_data_uses_get_combat_stats"
Cohesion: 0.67
Nodes (3): asyncio, Test get_player_combat_data delegates to Player.get_combat_stats()., test_get_player_combat_data_uses_get_combat_stats()

### Community 1228 - "Validate Codacy Coverage"
Cohesion: 0.23
Nodes (12): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., test_cobertura_root_line_rate_parses(), test_lcov_aggregate_and_gate() (+4 more)

### Community 1230 - "snapshot_chaosium_graphify.ps1"
Cohesion: 0.70
Nodes (4): Export-PackSnapshot(), Get-ChaosiumSlug(), Get-GraphCount(), Get-HonestyNote()

### Community 1233 - "get_session_maker"
Cohesion: 0.03
Nodes (82): get_10_active_invites(), main(), Get 10 active invite codes from the database., get_session_maker(), Get the async session maker from DatabaseManager. Returns: async_sessionmaker:…, _coerce_row_stats(), _defaulted_numerics(), _defaulted_strings() (+74 more)

### Community 1237 - "npc_startup_service"
Cohesion: 0.67
Nodes (3): npc_startup_service(), fixture, Create an NPCStartupService instance.

### Community 1244 - "Github Workflows Ci"
Cohesion: 0.25
Nodes (11): CodeQL Configuration, CodeQL Test Credential Exclusions, CI Python Backend Job, CI Workflow, Codacy Coverage Finalize Job, CI React Client Job, step-security Harden Runner, mythos_unit CI Database Bootstrap (+3 more)

### Community 1251 - "Cursor Mcp"
Cohesion: 0.22
Nodes (10): codacy, context7, jcodemunch, playwright, npx, uvx, @codacy/codacy-mcp, jcodemunch-mcp (+2 more)

### Community 1256 - "Enhanced Logging Guide"
Cohesion: 0.22
Nodes (10): AI Agent Development Guide, AI Enhanced Logging Mandate, Documentation Updates ConnectionManager, Enhanced Logging Guide, MDC Request Context Binding, measure_performance Span, Error Handling Guide, MythosMUDError Hierarchy (+2 more)

### Community 1260 - "Audit Executive Summary"
Cohesion: 0.22
Nodes (11): 25-30% Critical Regression Tests, Test Audit Executive Summary, Test Optimization Roadmap, Test Optimization Phases, Test Pruning Candidates, Low-Value Test Pruning Candidates, Test Quality Audit Report, Test Timing Analysis (+3 more)

### Community 1263 - "add_fastapi_users_columns.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add FastAPI Users columns. Args: database_url:…

### Community 1264 - "add_hashed_password_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add hashed_password column. Args: database_url:…

### Community 1265 - "add_used_by_user_id_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add used_by_user_id column. Args: database_url:…

### Community 1267 - "rename_invites_columns.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Apply the migration to rename columns. Args: database_url: PostgreSQL database…, Main entry point for the migration script.

### Community 1276 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 1277 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, properties, field1, field2, field3, sub_zone (+3 more)

### Community 1279 - "properties"
Cohesion: 0.17
Nodes (12): description, description, description, description, maxLength, minLength, type, properties (+4 more)

### Community 1280 - "Analyze Comments"
Cohesion: 0.22
Nodes (10): analyze_file(), check_comment_references_nonexistent_code(), extract_function_and_class_names(), main(), Any, Path, Analyze a single file for comment issues. Args: file_path: Path to file to…, Main entry point for comment analysis. (+2 more)

### Community 1281 - "Check Apply Map"
Cohesion: 0.25
Nodes (10): apply_migration_013(), apply_migration_014(), check_migration_013(), check_migration_014(), main(), Main function to check and apply migrations., Check if migration 013 (map_x/map_y columns) has been applied., Check if migration 014 (player_exploration table) has been applied. (+2 more)

### Community 1282 - "Check Coverage Thresholds"
Cohesion: 0.29
Nodes (10): check_thresholds(), _ensure_coverage_xml_or_exit(), main(), parse_coverage_xml(), _print_results_and_exit(), Path, Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't…, Print coverage results and exit with appropriate code. (+2 more)

### Community 1283 - "Simple Room Graph"
Cohesion: 0.25
Nodes (10): generate_simple_dot_file(), generate_simple_html_visualization(), load_room_data(), main(), print_simple_statistics(), Load all room and intersection data from the zone directory., Print simplified statistics about the room data., Main function to generate the simplified visualization. (+2 more)

### Community 1291 - "Cursor Skills Skill"
Cohesion: 0.24
Nodes (11): Aha Moment Onboarding, Core Web Vitals Performance, Design Context Persistence (.impeccable.md), Onboard Skill, Optimize Skill, Overdrive Skill, Overdrive Mode, Polish Skill (+3 more)

### Community 1301 - "Plan Cursor Plans"
Cohesion: 0.67
Nodes (3): Architecture Review Plan, Option C Replacement Client Updates, Client Updates System Audit

### Community 1311 - "messaging_integration"
Cohesion: 0.40
Nodes (5): messaging_integration(), mock_connection_manager(), fixture, Create mock connection manager., Create CombatMessagingIntegration instance.

### Community 1340 - "Npc Lifecycle Respawn"
Cohesion: 0.23
Nodes (11): Process the respawn queue and spawn NPCs that are ready (delegates to…, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…, Process the respawn queue and spawn NPCs that are ready. Args: manager:… (+3 more)

### Community 1342 - "rename_used_to_is_active.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to rename used back to is_active. Args: database_url:…

### Community 1355 - "Check Asyncio Run"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1356 - "Lucidity Migration"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1359 - "test_alias_storage.py"
Cohesion: 0.02
Nodes (123): _get_alias_validator(), Lazily instantiate and cache the alias schema validator., alias_storage(), fixture, Path, Unit tests for alias storage utilities. Tests the AliasStorage class for…, Test _load_alias_data handles invalid JSON gracefully., Test _load_alias_data handles IO errors gracefully. (+115 more)

### Community 1367 - "rate_limiter"
Cohesion: 0.40
Nodes (5): mock_config(), fixture, rate_limiter(), Create a mock config with chat rate limits., Create a RateLimiter instance with mocked config.

### Community 1381 - "Testing Map Regression"
Cohesion: 0.67
Nodes (3): ASCII Map Context Preparation, ASCII Minimap Generation, Map Regression Tests Proposal

### Community 1383 - "A Cold Fire Within (source summary)"
Cohesion: 0.50
Nodes (3): A Cold Fire Within (source summary), For MythosMUD design, Links

### Community 1384 - "Alone Against the Dark (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Dark (source summary), For MythosMUD design, Links

### Community 1386 - "Alone Against the Frost (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Frost (source summary), For MythosMUD design, Links

### Community 1388 - "Alone against the Tide (source summary)"
Cohesion: 0.50
Nodes (3): Alone against the Tide (source summary), For MythosMUD design, Links

### Community 1391 - "Package Engines Node"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 1392 - "include"
Cohesion: 0.10
Nodes (19): compilerOptions, allowImportingTsExtensions, composite, noEmit, types, exclude, extends, include (+11 more)

### Community 1393 - "Vite Config Proxyauthorization"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1395 - "Berlin - The Wicked City (source summary)"
Cohesion: 0.50
Nodes (3): Berlin - The Wicked City (source summary), For MythosMUD design, Links

### Community 1396 - "Cursor Hooks Trigger"
Cohesion: 0.31
Nodes (8): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Entry point: read hook payload from stdin, check edited-files state, and…

### Community 1399 - "Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary), For MythosMUD design, Links

### Community 1401 - "Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition Keeper Screen Pack (source summary), For MythosMUD design, Links

### Community 1403 - "Call of Cthulhu Investigator Handbook 7th Edition (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Investigator Handbook 7th Edition (source summary), For MythosMUD design, Links

### Community 1405 - "Call of Cthulhu Keeper Tips (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Keeper Tips (source summary), For MythosMUD design, Links

### Community 1408 - "Call of Cthulhu Starter Set (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Starter Set (source summary), For MythosMUD design, Links

### Community 1409 - "Call of Cthulhu_ The Coloring Book (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu_ The Coloring Book (source summary), For MythosMUD design, Links

### Community 1414 - "Cursor Skills Mythosmud"
Cohesion: 0.67
Nodes (3): MythosMUD Server Runbook Skill, MythosMUD Worktree Workflow Skill, One Server Only Rule

### Community 1415 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 1421 - "character_sheets (source summary)"
Cohesion: 0.50
Nodes (3): character_sheets (source summary), For MythosMUD design, Links

### Community 1422 - "Room Validator Toolkit"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1423 - "Room Toolkit Validator"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1424 - "Cthulhu Dark Ages - 3rd Edition (source summary)"
Cohesion: 0.50
Nodes (3): Cthulhu Dark Ages - 3rd Edition (source summary), For MythosMUD design, Links

### Community 1425 - "Dead Light and Other Dark Turns (source summary)"
Cohesion: 0.50
Nodes (3): Dead Light and Other Dark Turns (source summary), For MythosMUD design, Links

### Community 1426 - "Filter Static Dml"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after…, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1427 - "Fix Room References"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area. Args: base_path: Path to the…, save_room_file()

### Community 1428 - "Player Inventory Migration"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1429 - "Does Love Forgive_ (source summary)"
Cohesion: 0.50
Nodes (3): Does Love Forgive_ (source summary), For MythosMUD design, Links

### Community 1430 - "Run Bug Prevention"
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
Nodes (69): _aggregator_formatter(), _aggregator_handler_class_for_windows(), create_aggregator_handler(), _make_exec_for_aggregator(), _open_aggregator_handler(), Any, Formatter, LogRecord (+61 more)

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

### Community 1441 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1443 - "prototype_registry.py"
Cohesion: 0.33
Nodes (3): Constants supporting item prototype validation. These enumerations anchor the…, Pydantic models for item prototype validation. This module defines the…, Prototype registry for managing item prototypes. This module provides the…

### Community 1448 - "Codacy Cli"
Cohesion: 0.39
Nodes (6): download(), download_cli(), download_file(), get_latest_version(), handle_rate_limit(), cli.sh script

### Community 1474 - "E 2 E Report Whisper"
Cohesion: 0.25
Nodes (8): Admin Teleportation Display Bug, E2E Session Report 2025-12-02, Whisper Messages Not Received Bug, chat.whisper.player Subject Segment, Whisper NATS Subject Bug Fix, Missing player Segment Root Cause, Whisper System Investigation, Whisper Work Completed and Remaining

### Community 1476 - "Components Ui V 2"
Cohesion: 0.32
Nodes (8): Event-Sourced Projector, Client Event Schema, game_state Event, GameState, room_state Event, Critical State Handoffs, Enter-Room Request/Response, Server Authority Over Client

### Community 1480 - "Impeccable design context"
Cohesion: 0.67
Nodes (3): Impeccable design context, Legibility under pressure, Dark terminal-first aesthetic

### Community 1487 - "Security Infrastructure"
Cohesion: 0.25
Nodes (8): ensure_directory_exists(), Ensure a directory exists and return its absolute path. Args: directory: The…, Test ensure_directory_exists with existing directory., Test ensure_directory_exists creates directory if it doesn't exist., Test ensure_directory_exists with relative path., test_ensure_directory_exists_creates(), test_ensure_directory_exists_existing(), test_ensure_directory_exists_relative_path()

### Community 1491 - "Migrate Async Persistence"
Cohesion: 0.36
Nodes (7): main(), migrate_file(), MigrationResult, NamedTuple, Path, Result of a file migration., Migrate a single file to use async persistence patterns. Args: file_path: Path…

### Community 1501 - "Apply Quest Migrations"
Cohesion: 0.36
Nodes (7): main(), cursor, Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial),…, Create quest_definitions, quest_instances, quest_offers tables and indexes., Insert leave_the_tutorial quest definition and room offer (idempotent)., _run_quest_ddl(), _seed_leave_the_tutorial()

### Community 1502 - "Migrate Npc"
Cohesion: 0.36
Nodes (7): apply_migration(), check_schema(), main(), Cursor, Path, Check current schema of npc_spawn_rules table, Apply the migration to rename columns

### Community 1540 - "Persistence Repository Architecture"
Cohesion: 0.11
Nodes (18): Persistence Async Migration Guide, Full Async Persistence Target, Persistence Async Migration Plan, Persistence Extraction Complete, Extracted Persistence Modules, Persistence Refactoring Complete, Persistence Refactoring Summary, Persistence Repository Architecture (+10 more)

### Community 1546 - "test_logging_processors.py"
Cohesion: 0.04
Nodes (80): EventDict, configure_enhanced_structlog(), Configure enhanced Structlog with MDC, security, and performance features.…, add_correlation_id(), add_request_context(), _database_error_type(), _enhance_one_player_id(), enhance_player_ids() (+72 more)

### Community 1550 - "E 2 E Scenarios Lucidity"
Cohesion: 0.67
Nodes (4): Lucidity System Expansion Scenarios, Catatonia Grounding Ritual Scenario, player_lucidity Ledger, Sanitarium Failover Escalation

### Community 1559 - "Cursor Plans Plan"
Cohesion: 0.33
Nodes (6): SSE Connection Removal, Unified Client Message Pipeline, Unify Client Message Handling, WebSocket Best-Practices Remediation, WebSocket-Only Architecture, WebSocket-Only Migration

### Community 1560 - "exception_metrics.py"
Cohesion: 0.40
Nodes (4): get_summary(), Any, Exception metrics tracking for monitoring. This module provides thread-safe…, Get a summary of exception counts. Returns: dict[str, Any]: Dictionary…

### Community 1561 - "Schemas Intersection Schema"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1563 - "PerformanceStats"
Cohesion: 0.67
Nodes (3): PerformanceStats, TypedDict, Type definition for performance statistics tracking.

### Community 1564 - "Schemas Room Schema"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1565 - "Generate Html Visualization"
Cohesion: 0.38
Nodes (6): generate_html_visualization(), load_room_data(), main(), Load all room and intersection data from the zone directory., Main function to generate the HTML visualization., Generate an HTML visualization of the room network.

### Community 1567 - "Investigations Sessions Session"
Cohesion: 0.29
Nodes (7): Attack Command Not Starting Combat, CommandType Enum vs String Comparison, Target Resolution via Lifecycle Manager, NPC Dual Tracking System Issue, Stale Room.get_npcs After Persistence Reload, NPC Spawning vs Occupants Display Issue, Flattened Occupants Losing Player NPC Distinction

### Community 1568 - "Investigations Sessions Combat"
Cohesion: 0.29
Nodes (7): Coroutine Object Has No current_room_id, Combat Start Missing Await get_player_by_name, get_player_by_id vs async_get_player Mismatch, XP Award async_get_player Missing Method, Linkdead WebSocket Grace Period, Second NPC Combat And Linkdead Findings, Stale Queued Attack Target Validation

### Community 1569 - "Investigations Sessions Session"
Cohesion: 0.29
Nodes (7): Missing cast spell spells Pydantic Models, Spell Slash Commands Missing From Validation, create_cast_command First-Word-Only Parse, Multi-Word Spell Name Parsing Failure, Missing async_heal_player Method, record_spell_cast Cross-Session Object Use, Heal Spell SQLAlchemy Session Boundary Error

### Community 1570 - "Subsystems Subsystem Design"
Cohesion: 0.33
Nodes (7): Limbo Room Death State, PlayerRespawnService, Respawn Subsystem, Determination Points (DP), Incapacitation (DP 0 to -9), no_death Rooms (ADR-009), Status Effects Subsystem

### Community 1572 - "Chat Panel"
Cohesion: 0.29
Nodes (7): Chat Message Type Categorization Bug, Chat Panel, Commands Panel, Game Log Panel, Chat Message Routing Bug Fix, Room Description Routing Bug Fix, Bug Prevention Testing Strategy

### Community 1573 - "test_grace_period_blocking.py"
Cohesion: 0.18
Nodes (13): mock_request(), asyncio, fixture, Unit tests for grace period command blocking in unified command handler. Tests…, Create a mock request., Test _check_grace_period_block() blocks commands for grace period players., Test _check_grace_period_block() allows commands when player not in grace…, Test _check_grace_period_block() handles missing services gracefully. (+5 more)

### Community 1574 - "combat_validator"
Cohesion: 0.67
Nodes (3): combat_validator(), fixture, Create a CombatValidator instance.

### Community 1582 - "Room"
Cohesion: 0.07
Nodes (22): Add an object to the room and trigger event. Args: object_id: The ID of the…, Remove an object from the room and trigger event. Args: object_id: The ID of…, Add an NPC to the room and trigger event. Args: npc_id: The ID of the NPC…, Remove an NPC from the room and trigger event. Args: npc_id: The ID of the NPC…, Represents a room in the MythosMUD game world. This class provides a stateless…, Check if an object is in the room. Args: object_id: The ID of the object to…, Check if an NPC is in the room. Args: npc_id: The ID of the NPC to check…, String representation of the room. (+14 more)

### Community 1595 - "MythosMUD Server Test Suite"
Cohesion: 0.33
Nodes (6): Command Tests Relocated, server/tests/unit/commands/, Integration Test Tier, make test-server, MythosMUD Server Test Suite, Unit Test Tier

### Community 1615 - "Player Command Developer"
Cohesion: 0.33
Nodes (6): Player Command Pipeline, Player Command Developer Guide, Pydantic Code Review, Pydantic Model Validation Patterns, Python Model Updates Required, Python Model Sync Requirements

### Community 1633 - "Cursor Plans Plan"
Cohesion: 0.33
Nodes (6): Combat Action Queue, Combat Bugs Investigation and Fixes, Round-Based Combat, Combat Round System Refactor, First Weapon Switchblade, Flee Command and Effect

### Community 1635 - "Pyrightconfig Extends Extra Paths"
Cohesion: 0.25
Nodes (7): extends, extraPaths, pythonVersion, venv, venvPath, ., ./pyproject.toml

### Community 1642 - "Check Logging Consistency"
Cohesion: 0.47
Nodes (5): check_file_for_logging_issues(), main(), Path, Check a single file for logging consistency issues. Args: file_path: Path to…, Main function to check all service files for logging consistency.

### Community 1643 - "e2e_reset_players.py"
Cohesion: 0.47
Nodes (5): _load_default_respawn_room(), main(), Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the…, Entry point: run E2E player reset via anyio., _reset_e2e_players()

### Community 1647 - "Investigations Sessions Session"
Cohesion: 0.33
Nodes (6): NPC Display Final Fixes, room_update Overwriting NPC Data, asyncpg UUID replace AttributeError, Legacy Occupants Snapshot Format, NPC Occupants Verification Summary, Rooms API User Object AttributeError

### Community 1652 - "Investigations Sessions Session"
Cohesion: 0.33
Nodes (6): event_data vs data Field Name Mismatch, NATS Event Message Field Mismatch, Combat Client Crash, CombatMessaging Connection Manager Init Failure, Combat Disconnect At NPC Death, Passive Lucidity Flux Performance Degradation

### Community 1653 - "Investigations Sessions Session"
Cohesion: 0.33
Nodes (6): limbo_death_void vs limbo_death_void_limbo_death_void, Respawn Death Screen Loop Limbo ID Mismatch, SQLAlchemy JSONB Mutation Detection, Respawn Persistence JSONB Mutation Failure, Death Threshold and Posture Bugs, HP -10 Limbo Transition Delay

### Community 1655 - "Investigations Sessions Session"
Cohesion: 0.33
Nodes (6): NPC Combat Start Race Condition, Redundant NPC Instance Lookup Failure, NPCs Incorrectly Marked is_alive False, December 3 Final Investigation Summary, Character Info Panel Missing Stats Field, Room Occupants Duplicates and Missing Player

### Community 1657 - "Cursor Skills Mythosmud"
Cohesion: 0.33
Nodes (6): MythosMUD COPPA Checklist Skill, MythosMUD Database Placement Skill, MythosMUD Full-Stack Feature Skill, MythosMUD OpenAPI Workflow Skill, player_id is UUID, Server Authority over Client

### Community 1659 - "Enhanced Structured Logging System"
Cohesion: 0.40
Nodes (6): bind_request_context, Dual Logging (warnings/errors aggregators), Enhanced Structured Logging System, F-String Logging Anti-Pattern, get_logger, sanitize_sensitive_data Processor

### Community 1669 - "Archive System Magic"
Cohesion: 0.40
Nodes (5): EffectList Pattern, Effects System Reference, Magic Points MP, Magic and Spellcasting System, Spell Registry

### Community 1670 - "Archive Lucidity System"
Cohesion: 0.60
Nodes (5): Catatonic Rescue Window, Lucidity System (LCD), Lucidity Tiers, Phantom Hostiles, Reversed Compass Directions

### Community 1674 - "Archive Room Planning"
Cohesion: 0.40
Nodes (5): Environment Classification, Four-Level Room Hierarchy, Environment Inheritance, Room Hierarchy Implementation, Hierarchical World Loader

### Community 1703 - "E 2 E Comprehensive Overview"
Cohesion: 0.40
Nodes (5): Modular E2E Test Suite, MULTIPLAYER_SCENARIOS_PLAYBOOK, E2E Validation Passed, AI Context Limit 20KB, E2E Test Suite README

### Community 1704 - "E 2 E Multiplayer Rules"
Cohesion: 0.40
Nodes (5): Automated Playwright CLI Tests, Hybrid E2E Testing Approach, Mandatory Execution Order, Playwright MCP Scenarios, Room Occupants Fix

### Community 1713 - "Codacy Instructions Review"
Cohesion: 0.40
Nodes (5): AI PR Reviewer Instructions, COPPA and Security Review Mandates, Review Coverage Thresholds, player_id UUID Type Rule, Server Authority Review Rule

### Community 1719 - "Cursor Plans Plan"
Cohesion: 0.40
Nodes (5): Quest System Gap, MUD Subsystems Gap Analysis, Player Skills and Profession Modifiers, Quest Subsystem Implementation, Quest System

### Community 1722 - "Remediation Investigations Plans"
Cohesion: 0.50
Nodes (5): Container Contents Synchronization Bug, Fail-Fast Container Error Philosophy, slot_type backpack Assignment, Dual Inventory Storage Architecture, Inventory Slot Calculation Bug

### Community 1723 - "Schemas Intersection Schema"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1724 - "Schemas Intersection Schema"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1725 - "Schemas Intersection Schema"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1727 - "Schemas Room Schema"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1728 - "Schemas Room Schema"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1734 - "Schemas Unified Room"
Cohesion: 0.25
Nodes (8): locked, sealed, unlocked, default, description, enum, type, lock_state

### Community 1738 - "Batch Fix Suppressions"
Cohesion: 0.60
Nodes (4): fix_file(), main(), Path, Fix suppressions in a file. Returns: (number_fixed, list of changes)

### Community 1739 - "Check Codacy Yaml"
Cohesion: 0.50
Nodes (4): check_codacy_yaml(), _content_is_valid(), Return (valid, list of reasons if invalid)., Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit.

### Community 1744 - "test_postgres_adapter.py"
Cohesion: 0.11
Nodes (18): is_postgres_url(), PostgresConnectionPool, Thread-safe PostgreSQL connection pool., Get or create a connection pool for the given database URL., Get a connection from the pool., Check if the database URL is PostgreSQL., patch, Unit tests for PostgreSQL adapter. Tests PostgresRow, PostgresConnection,… (+10 more)

### Community 1748 - "Cursor Skills Mythosmud"
Cohesion: 0.40
Nodes (5): Definition of Done Checklist, MythosMUD Code Quality AI Skill, MythosMUD Commit Messages Skill, MythosMUD Pre-Commit Checklist Skill, MythosMUD Test Writing Skill

### Community 1774 - "Archive Dual Connection"
Cohesion: 0.50
Nodes (4): Dual Connection API Reference, WebSocket and SSE Dual Connections, Dual Connection Client Guide, Dual Connection Deployment Guide

### Community 1786 - "Archive Prd"
Cohesion: 0.50
Nodes (4): Aggro System, Lucidity System, MythosMUD Product Requirements, Room-Based Combat

### Community 1809 - "Claude Authoritative Reference"
Cohesion: 0.67
Nodes (4): AGENTS.md Authoritative Reference, Cursor Rules (.cursor/rules/), Claude Pointer (.claude/CLAUDE.md), Root CLAUDE.md Router Stub

### Community 1819 - "Logging Best Practices"
Cohesion: 0.67
Nodes (4): Logging Best Practices, Structured Key-Value Logging, Logging Quick Reference, Forbidden Logging Patterns

### Community 1829 - "E 2 E Execution Validation"
Cohesion: 0.50
Nodes (4): Scenario Group Execution, Local Channel Scenario Group (8-12), Logout Scenario Group (19-21), Whisper Channel Scenario Group (13-18)

### Community 1831 - "E 2 E Scenario Blocked"
Cohesion: 0.50
Nodes (4): Whisper System Remediation, Per-Recipient Whisper Rate Limiting, Global Whisper Rate Limit, Scenario 15 Rate Limiting Blocked

### Community 1845 - "Cursor Plans Plan"
Cohesion: 0.50
Nodes (4): Test Suite Improvement, Vite Best-Practices Remediation, import.meta.env (Vite), Vitest Best-Practices Remediation

### Community 1852 - "E 2 E Scenarios Scenario"
Cohesion: 0.50
Nodes (4): Scenario 32 Disconnect Grace Period, Linkdead Zombie State, Scenario 33 Rest Command, Scenario 35 Player Combat

### Community 1854 - "Schemas Intersection Schema"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1869 - "Schemas Room Schema"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1870 - "Schemas Room Schema"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1872 - "Schemas Room Schema"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1876 - "Schemas Unified Room"
Cohesion: 0.11
Nodes (19): description, description, description, description, type, description, maxLength, minLength (+11 more)

### Community 1877 - "Apply Players Migration"
Cohesion: 0.67
Nodes (3): apply_migration(), main(), Apply migration to a single database.

### Community 1879 - "Precommit Run Npm"
Cohesion: 0.67
Nodes (3): main(), Return absolute path to npm (prefer npm.cmd on Windows), or None if not found., _resolved_npm()

### Community 1880 - "Verify Tutorial Migrations"
Cohesion: 0.83
Nodes (3): Test-Migration08(), Test-Migration12(), Write-ColorOutput()

### Community 1883 - "F-String Logging Violations"
Cohesion: 0.40
Nodes (5): F-String Logging Violations, Enhanced Logging Compliance Audit, F-String Logging Remediation Complete, Pre-Commit F-String Hook Gaps, AST-Based F-String Logging Detector

### Community 1890 - "Investigations Sessions Movement"
Cohesion: 0.50
Nodes (4): Catatonic Movement Prevention Bug, WebSocket Go Command Unified Handler Bypass, current_room_id VARCHAR(50) Truncation, Movement Valid Exits Rejection Bug

### Community 1892 - "Investigations Sessions Session"
Cohesion: 0.50
Nodes (4): asyncpg Colon Cast Parameter Parsing, Rooms List SQL ::uuid[] Parameter Conflict, Minimap Explored Rooms UUID vs stable_id, Explored Room UUIDs Treated As stable_ids

### Community 1905 - "Archive Character Creation"
Cohesion: 0.67
Nodes (3): Character Creation Revamp, CoC-Style Skills Allocation, Skill Use Tracking and Level-Up Improvement

### Community 1906 - "Archive Cleanup Dead"
Cohesion: 0.67
Nodes (3): Legacy Files Cleanup Summary, Dead Code Cleanup Completion, Dead Code Cleanup Planning

### Community 1910 - "Archive Connection Termination"
Cohesion: 0.67
Nodes (3): force_disconnect_player, Single Session Per User, Player Spawn Protection

### Community 1911 - "Archive Plan Warning"
Cohesion: 0.67
Nodes (3): Early Logging Initialization, datetime.utcnow Deprecation Fix, Test Warning Remediation

### Community 1912 - "Archive Planning Stats"
Cohesion: 0.67
Nodes (3): Pydantic Click Command Validation Integration, Random Stats Generator Technical Plan, Random Stats Generator Planning

### Community 1917 - "Archive Party System"
Cohesion: 0.67
Nodes (3): Party Invite Command, Party System Reference, Ephemeral Grouping Party Planning

### Community 1924 - "Archive Migration Completion"
Cohesion: 0.67
Nodes (3): Test Suite Hierarchical Migration, Test File Migration Mapping, Test Suite Refactoring Deliverables

### Community 1944 - "Anyio Vs Asyncio"
Cohesion: 0.67
Nodes (3): AnyIO Code Review and Migration, AnyIO vs Asyncio Comparison, Structured Concurrency

### Community 1945 - "Message Handling"
Cohesion: 0.67
Nodes (3): Client EventStore, GameState Event Projection, Server Authority over Client State

### Community 1946 - "Coverage Easy Wins"
Cohesion: 0.67
Nodes (3): Coverage Improvement Summary, Easy Coverage Wins, Tiered Coverage Wins

### Community 1947 - "Dead Code"
Cohesion: 0.67
Nodes (3): Knip Client Dead Code Tooling, Truly Dead Code, Vulture Allowlist

### Community 1948 - "Fastapi Code Review"
Cohesion: 0.67
Nodes (3): FastAPI Dependency Injection, FastAPI Code Review, FastAPI Response Models

### Community 1956 - "Github Workflows Dependency"
Cohesion: 0.67
Nodes (3): Dependabot Dependency Updates, Dependency Review Workflow, UV Lock Dependency Snapshot Gate

### Community 1964 - "Load E 2 E Analysis"
Cohesion: 0.67
Nodes (3): who Command Unawaited Coroutine Bug, 10 Concurrent Players Load Test, Load Test Suite

### Community 1972 - "Cursor Plans Plan"
Cohesion: 0.67
Nodes (3): Cursor-Centric AI Config, Cursor Rules as Canonical Config, GitHub Worktrees Cursor Setup

### Community 1974 - "Plans Gladiator Ring"
Cohesion: 0.67
Nodes (3): Arena Implementation Todos, Arena Center Tutorial Exit and Respawn, Gladiator Ring Arena

### Community 1975 - "Cursor Plans Plan"
Cohesion: 0.67
Nodes (3): Logging Aggregator Verification, warnings.log and errors.log Aggregators, Structlog Anti-Pattern Remediation

### Community 1976 - "Plan Cursor Plans"
Cohesion: 0.67
Nodes (3): Closed WebSockets Deque Cap, Memory Leak Metrics Collection, Memory Leak Remediation

### Community 1977 - "Plan Cursor Plans"
Cohesion: 0.67
Nodes (3): Playwright Best-Practices Remediation, Playwright DI Migration Validation, E2E Harness Overhaul

### Community 1978 - "Cursor Plans Authority"
Cohesion: 0.67
Nodes (3): game_state Room Replace (not Merge), Server Authority Remediation, Server Authority Rule

### Community 1996 - "E 2 E Scenarios Scenario"
Cohesion: 0.67
Nodes (3): Scenario 34 Two Players Same Room Visibility, Scenario 36 Movement Visibility, Scenario 37 Chat Message Ordering

### Community 2011 - "Investigations Sessions Session"
Cohesion: 0.67
Nodes (3): exclude_player Occupants Snapshot Pattern, NPCs Not Updating On Player Movement, Canonical Room ID NPC Matching Remediation

### Community 2012 - "Investigations Sessions Session"
Cohesion: 0.67
Nodes (3): Combat Turn Order UUID Display, Combat Messages Dual Panel Display, Missing NPC Death Message Handlers

### Community 2013 - "Investigations Sessions Session"
Cohesion: 0.67
Nodes (3): Docker Build mythos_unitql Typo, Test Suite Stall After Performance Comparison, thread.join Without Timeout Hang

### Community 2019 - "Subsystems Subsystem Rescue"
Cohesion: 0.67
Nodes (3): Catatonic Rescue Target, Ground Command, Rescue Subsystem

### Community 2020 - "Subsystems Subsystem Rest"
Cohesion: 0.67
Nodes (3): Rest Countdown Disconnect, Rest Location Instant Disconnect, Rest Subsystem

### Community 2021 - "Subsystems Subsystem Skills"
Cohesion: 1.00
Nodes (3): LevelService, SkillService, Skills / Level Subsystem

## Knowledge Gaps
- **3611 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `@codacy/codacy-mcp`, `@playwright/mcp` (+3606 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **593 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `lifespan.py`, `MovementService`, `websocket_initial_state.py`, `test_users.py`, `is_player_in_login_grace_period`, `MythosMUDError`, `ErrorType`, `player_connection_setup.py`, `LoggedHTTPException`, `players/__init__.py`, `NPCCombatIntegrationService`, `server/exceptions.py`, `PrototypeRegistry`, `test_command_parser.py`, `test_security_validator.py`, `test_connection_delegates.py`, `test_look_container.py`, `test_wearable_container_service.py`, `test_player_disconnect_handlers.py`, `server/services/__init__.py`, `api/monitoring.py`, `test_look_npc.py`, `server/tests/conftest.py`, `container_persistence_async.py`, `optimized_security_validator.py`, `debrief_command.py`, `inventory_command_helpers.py`, `lifecycle_periodic.py`, `server/dependencies.py`, `server/schemas/__init__.py`, `test_follow_commands.py`, `AttributeError`, `npc_config_parsing.py`, `test_database_helpers.py`, `test_container_websocket_events.py`, `rooms.py`, `LucidityFluxService`, `test_quest_instance_repository.py`, `test_connection_establishment.py`, `DatabaseError`, `_find_item_in_equipped`, `communication_commands.py`, `chat_nats_publisher.py`, `test_connection_disconnection.py`, `.__init__`, `test_status_commands.py`, `event_types.py`, `test_look_room.py`, `CoordinateValidator`, `NATSMessageBroker`, `test_lucidity_recovery_commands.py`, `.to_dict`, `server/persistence/__init__.py`, `test_player_presence_tracker.py`, `test_metrics_endpoints.py`, `PlayerEnteredRoom`, `test_look_player.py`, `User`, `test_lucidity_event_dispatcher.py`, `Player`, `player_effect_repository.py`, `migrate_combat_data.py`, `WebSocketMessageValidator`, `api/character_creation.py`, `HealthRepository`, `catatonia_check.py`, `TaskRegistry`, `test_rest_command.py`, `inventory_put_command.py`, `AliasStorage`, `combat_flee_handler.py`, `CombatAuditLogger`, `test_connection_statistics.py`, `player_schema_converter.py`, `NPCSpawnRule`, `ApplicationContainer`, `PlayerSavePreparer`, `.state`, `party_commands.py`, `chat_message_senders.py`, `inventory_equip_command.py`, `test_corpse_lifecycle_service.py`, `maps.py`, `fixtures/integration/__init__.py`, `CatatoniaRegistry`, `OccupantFormatter`, `admin_shutdown_command.py`, `test_container_persistence.py`, `command_input.py`, `quest_commands.py`, `connection_initialization.py`, `_handle_admin_set_stat_command`, `rescue_service.py`, `test_map_helpers.py`, `MonitoringDashboard`, `PartyService`, `get_session_maker`, `test_connection_session_management.py`, `PlayerService`, `WebSocketRequestContext`, `ChatModeration`, `resolve_weapon_attack_from_equipped`, `chat_service.py`, `add_fastapi_users_columns.py`, `add_hashed_password_column.py`, `add_used_by_user_id_column.py`, `error_handling_middleware.py`, `rename_invites_columns.py`, `get_help_content`, `PlayerNameExtractor`, `LogAggregator`, `log_and_raise`, `test_logout_commands.py`, `get_username_from_user`, `persistence/container_persistence.py`, `game_tick_processing.py`, `router.py`, `test_login_grace_period_visual_indicator.py`, `PlayerPreferencesService`, `ExceptionTracker`, `disconnect_grace_period.py`, `test_health.py`, `test_aggro_threat.py`, `lifespan_shutdown.py`, `ErrorContext`, `handle_read_command`, `quest_events.py`, `RealTimeEventHandler`, `player_combat_service_support.py`, `system_monitoring.py`, `persistence/container_helpers.py`, `Npc Lifecycle Respawn`, `rename_used_to_is_active.py`, `AppConfig`, `PlayerPositionService`, `map_minimap.py`, `send_game_event`, `websocket_handler_commands.py`, `Lucidity Migration`, `look_command.py`, `hallucinations.py`, `message_handler_factory.py`, `combat_attack.py`, `test_command_validator.py`, `MovementMonitor`, `admin_teleport_commands.py`, `AuditLogger`, `command_handler_unified.py`, `shutdown_sequence.py`, `NPCEventHandler`, `real_time.py`, `test_communication_commands_flows.py`, `retry.py`, `inventory_pickup_command.py`, `Player Inventory Migration`, `npc_database.py`, `NATSConnectionStateMachine`, `teach_command.py`, `test_who_commands.py`, `prototype_registry.py`, `format_metadata`, `log_with_context`, `factory.py`, `channel_broadcasting_strategies.py`, `players.py`, `websocket_handler.py`, `connection_manager.py`, `test_population_control.py`, `build_event`, `FeatureFlagService`, `NPCCombatLucidity`, `handle_emote_command`, `skills_commands.py`, `quest_service.py`, `MessageBroadcaster`, `NPCOccupantProcessor`, `apply_communication_dampening`?**
  _High betweenness centrality (0.164) - this node is a cross-community bridge._
- **Why does `AliasStorage` connect `AliasStorage` to `get_username_from_user`, `Alias`, `router.py`, `CommandRequest`, `inventory_pickup_command.py`, `test_rest_command.py`, `inventory_put_command.py`, `test_admin_shutdown_command.py`, `TestHelperFunctions`, `ApplicationContainer`, `test_inventory_commands.py`, `debrief_command.py`, `.state`, `party_commands.py`, `handle_read_command`, `teach_command.py`, `_asyncio_mark`, `inventory_equip_command.py`, `test_follow_commands.py`, `get_logger`, `admin_shutdown_command.py`, `handle_quest_command`, `AliasGraph`, `quest_commands.py`, `SchemaValidator`, `_handle_admin_set_stat_command`, `PlayerPositionService`, `TauntCommandHandler`, `websocket_handler_commands.py`, `communication_commands.py`, `look_command.py`, `.handle_attack_command`, `handle_system_command`, `test_alias_storage.py`, `handle_time_command`, `test_status_commands.py`, `test_lucidity_recovery_commands.py`, `test_magic_commands.py`, `PlayerService`, `test_command_validator.py`, `admin_teleport_commands.py`, `handle_emote_command`, `handle_explore_command`, `skills_commands.py`, `command_handler_unified.py`, `test_logout_commands.py`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Why does `log_and_raise_enhanced()` connect `server/exceptions.py` to `get_username_from_user`, `test_command_factories_exploration.py`, `PlayerService`, `DatabaseError`, `MythosMUDError`, `test_command_parser.py`, `Any`, `get_logger`, `log_with_context`, `.respawn_player_by_user_id`, `PlayerRead`, `log_and_raise`, `test_command_factories_utility.py`, `Player`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `LoggedHTTPException` (e.g. with `_AppStateWithLegacyConfig` and `_AppWithLegacyConfigState`) actually correct?**
  _`LoggedHTTPException` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `AliasStorage` (e.g. with `SchemaValidator` and `CommandRequest`) actually correct?**
  _`AliasStorage` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `CombatService` (e.g. with `_FleeCommandHandlerLike` and `_PlayerForFlee`) actually correct?**
  _`CombatService` has 42 INFERRED edges - model-reasoned connections that need verification._