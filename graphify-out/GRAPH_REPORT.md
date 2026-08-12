# Graph Report - MythosMUD  (2026-08-12)

## Corpus Check
- 2929 files · ~2,619,569 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 44623 nodes · 82737 edges · 1897 communities (1298 shown, 599 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 2994 edges (avg confidence: 0.6)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0d45837f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_zone_config_loader.py
- test_connection_delegates.py
- test_users.py
- Alias
- test_combat_flee_helpers.py
- websocket_initial_state.py
- NATSService
- test_command_inventory.py
- User
- is_player_in_login_grace_period
- MythosMUDError
- TargetMatch
- ErrorType
- test_player_model.py
- ContainerServiceError
- players/__init__.py
- NPCCombatIntegrationService
- BaseCommand
- test_security_validator.py
- TargetResolutionService
- test_inventory_service_helpers.py
- test_command_communication.py
- connection_manager.py
- test_look_container.py
- test_wearable_container_service.py
- test_config_models.py
- test_npc_service.py
- api/monitoring.py
- test_look_npc.py
- test_admin_commands.py
- _parse_jsonb_column
- test_command_admin.py
- test_websocket_handler_core.py
- test_nats_message_handler.py
- inventory_commands.py
- test_inventory_helpers_extended.py
- Room
- lifecycle_periodic.py
- server/dependencies.py
- ContainerComponent
- PlayerCombatService
- lifespan_startup.py
- server/schemas/__init__.py
- coerce_int
- NATSMessageHandler
- test_npc_startup_service.py
- test_command_moderation.py
- BehaviorEngine
- get_username_from_user
- CombatParticipant
- test_container_websocket_events.py
- .get_instance
- CombatParticipantData
- test_command_factories.py
- BaseEvent
- ExplorationService
- test_combat_schema.py
- Stats
- test_command_combat.py
- api/conftest.py
- _apply_exploration_filter_if_needed
- CombatAttackHandler
- test_command_factories_utility.py
- magic_service_completion.py
- LucidityFluxService
- .create_look_command
- ui-v2/types.ts
- test_user_manager.py
- test_quest_instance_repository.py
- PayloadOptimizer
- test_command_service.py
- test_connection_establishment.py
- connection_manager_health_cleanup.py
- asyncio
- CombatService
- test_combat_validator.py
- EldritchIcon.tsx
- request_with_app_container
- test_room_renderer.py
- test_npc_models.py
- time.py
- test_auth_utils.py
- Reporter
- get_npc_instance_service
- test_websocket_handler_helpers_extended.py
- test_status_commands.py
- WebSocketManager
- create_access_token
- test_container_helpers_inventory_find.py
- map/types.ts
- combat_service.py
- test_look_room.py
- test_rescue_service.py
- NATSMessageBroker
- test_go_command.py
- test_lucidity_recovery_commands.py
- multiplayer.ts
- test_nats_service.py
- test_character_creation_service.py
- LoggedHTTPException
- Dependency Risk Analyzer
- RealTimeEventHandler
- test_container_helpers_inventory_ops.py
- test_player_presence_tracker.py
- test_player_death_service.py
- test_npc_utils.py
- test_metrics_endpoints.py
- test_room_sync_service.py
- RoomLoader
- asyncio
- CircuitBreaker
- CorpseOverlay.tsx
- PlayerEnteredRoom
- test_nats_broker.py
- command.py
- UserManager
- test_look_player.py
- test_logging_utilities.py
- test_game.py
- test_combat_monitoring_service.py
- test_lucidity_event_dispatcher.py
- test_nats_message_handler_chat.py
- spell_effects.py
- GameTerminal.tsx
- SchemaValidator
- DeadLetterMessage
- test_population_control.py
- LucidityService
- PathValidator
- test_websocket_helpers.py
- .__post_init__
- chatPanelRuntimeUtils.ts
- test_room_utils.py
- test_movement_service.py
- test_alias_commands.py
- WebSocketMessageValidator
- asyncio
- RoomDataCache
- asyncio
- api/character_creation.py
- CombatPersistenceHandler
- catatonia_check.py
- test_nats_message_handler_subzone_events.py
- ScheduleService
- test_rest_command.py
- test_user_schemas.py
- ContainerService
- PlayerRespawnService
- test_npc_combat_integration_class.py
- Spell
- AliasStorage
- TestHelperFunctions
- StatsGenerator
- quality_fragmentation_ai_guardrails.py
- websocket_helpers.py
- test_connection_statistics.py
- test_player_schema_converter_weapon.py
- test_active_lucidity_service.py
- NPCDefinitionCRUDMixin
- test_websocket_messages.py
- EventBus
- test_room_subscription_manager_drops.py
- PlayerSavePreparer
- test_validation.py
- .state
- ChatHistoryPanel.tsx
- CombatConfiguration
- _asyncio_mark
- chat_message_senders.py
- inventory_equip_command.py
- test_corpse_lifecycle_service.py
- test_party_service.py
- maps.py
- test_quest_service.py
- test_async_persistence_room_cache.py
- fixtures/integration/__init__.py
- test_look_helpers.py
- CatatoniaRegistry
- mapUtils.ts
- test_occupant_formatter.py
- admin_shutdown_command.py
- test_connection_cleaner.py
- App.tsx
- test_container_persistence.py
- useGameClientV2Container.ts
- normalize_command
- GameClientV2.tsx
- ChatService
- QuestService
- fixtures/unit/__init__.py
- quest_commands.py
- MemoryProfiler
- test_command_exploration.py
- test_connection_initialization.py
- CorpseLifecycleService
- IdleMovementHandler
- _handle_admin_set_stat_command
- test_async_persistence_core.py
- eventHandlers/types.ts
- MessageHandler
- test_message_filtering.py
- channels.ts
- test_combat_persistence_handler_events.py
- test_map_helpers.py
- test_inventory_helpers.py
- server/models/game.py
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
- test_player_preferences_service.py
- commandStore.ts
- TestRoomDataFixer
- HolidayService
- test_spell_effects.py
- test_game_state_provider.py
- CombatMonitoringService
- magic_service.py
- asyncio
- test_chat_service.py
- is_player_in_grace_period
- deleteCharacterFlow.ts
- WebSocketRequestContext
- collect_inventory.py
- ChatModeration
- resolve_weapon_attack_from_equipped
- EnvironmentalContainerLoader
- rescue_service.py
- chat_service.py
- Async Remediation Complete
- NPCCombatIntegrationBase
- communication_commands_flows.py
- RoomDataValidator
- apiTypeGuards.ts
- error_handling_middleware.py
- fix_markdown_blanks_around_lists.py
- container_endpoints_basic.py
- LogAggregator
- PlayerNameExtractor
- TestValidatorComponents
- _fetch_container_items
- useDraggablePanelInteractions.ts
- Test Suite Refactoring Plan
- test_nats_messages.py
- test_command_factories_combat.py
- test_logout_commands.py
- test_player_occupant_processor.py
- test_command_helpers_functions.py
- server/exceptions.py
- game_tick_processing.py
- GameLogPanel.tsx
- health.ts
- vim Best Practices and Coding Standards
- migration_examples.py
- alias_storage.py
- RoomMapEditorRuntime.hooks.ts
- asyncio
- subzone_schema.json
- ChatChannelLoggerMixin
- executeCommand
- .get_player_aliases
- test_communication_commands_flows.py
- PlayerPreferencesService
- FeatureFlagService
- MemoryLeakMetricsCollector
- Alias JSON Schema
- AsciiMapRenderer
- test_room_id_utils.py
- test_admin_shutdown_command.py
- 🧪 MythosMUD E2E Testing Strategy
- ExceptionTracker
- Logging Compliance Checker
- test_game_tick_processing_async.py
- GameClientV2ContainerView.tsx
- ErrorMonitor
- Memory Leak Prevention System - Implementation Summary
- test_pattern_matcher.py
- Linting Results Comparator
- test_health_service.py
- PlayerRoomEventHandler
- test_look_item_helpers.py
- Any
- test_room_subscription_manager_helpers.py
- SecurityHeadersMiddleware
- useRespawnHandlers.ts
- handle_read_command
- NATSMetrics
- test_player_event_handlers.py
- go_command.py
- ansiToHtml.ts
- test_windows_safe_rotation.py
- MessageFilteringHelper
- test_command_base.py
- character-cleanup.ts
- ConnectionManager
- AI Executor Protocol
- PlayerRepositoryProtocol
- realtime/conftest.py
- lifespan.py
- TestCombatMessagingService
- Hierarchical Schema Tests
- format_metadata
- Configuration Architecture Docs
- Execution Steps
- handle_quest_command
- test_combat_persistence_handler_persistence.py
- SubjectValidator
- NATS Code Review
- AliasGraph
- test_spell.py
- realtime/realtime.py
- Memory Leak Prevention
- test_command_player_state.py
- _check_grace_period_block
- Result
- File-by-File Changes
- AsyncPersistenceLayer
- PlayerPositionService
- WearableContainerService
- RoomService
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
- test_message_handler_factory.py
- generate_sql.mjs
- player_effect_repository.py
- roomHandlers.ts
- Enhanced Logging Migration Complete
- Migration Final Report
- Structlog Implementation Plan
- gameStore.ts
- combat_attack.py
- appLazyScreens.tsx
- test_magic_commands.py
- container_persistence/container_persistence.py
- Test Coverage Gaps
- MovementMonitor
- process_command_with_validation
- test_event_publisher.py
- useMythosAppActions.ts
- RoomCacheLoader
- admin_setlucidity_command.py
- rate_overrides.py
- Profession
- Three-Column Game UI Layout
- worktree-ops.py
- e2e-bootstrap.ts
- test_invite_schemas.py
- MonitoringPanel.tsx
- authenticated.ts
- test_message_broadcaster.py
- test_postgres_adapter.py
- _MagicServiceCore
- AuditLogger
- command_handler_unified.py
- test_quest_definition_repository.py
- test_movement_monitor.py
- bundles/game.py
- shutdown_sequence.py
- useRoomEditModal.ts
- subject_controller.py
- NATS Subject Manager Review
- handle_whisper_command
- debugLogger
- UserManagerProtocol
- NPCStartupService
- real_time.py
- Migration Strategy
- ChatPoseManager
- get_cached_player
- devDependencies
- TestCombatConfigurationService
- test_communication_commands_support.py
- test_quest_service_collect.py
- retry.py
- TaskRegistry
- test_health_monitor.py
- TestNPCCombatLifecycle
- inventory_pickup_command.py
- Emote Schema Definition
- Dependency Upgrade Report
- CommandPanel.tsx
- FeedbackManager
- Architecture Remediation Implementation Summary
- Feature Requirements Document: Random Stats Generator
- test_room_occupant_manager.py
- LRUCache
- ValidationRule
- asyncio
- ValidationError
- stateNormalization.ts
- Async Persistence Migration
- Dependency Upgrade Strategy Specification
- deprecated_patterns.py
- ZoneConfiguration
- _str_id
- NATSConnectionStateMachine
- LucidityRepository
- test_dependency_analysis.py
- teach_command.py
- format_player_entry
- api/player_respawn.py
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
- InventorySchemaValidationError
- CommandService
- ConnectionCleaner
- projectorRoom.ts
- security.ts
- generate_html_visualization.py
- Execution Steps
- logout_commands.py
- channel_broadcasting_strategies.py
- Migration 019 Ready for Deployment
- PlayerService
- test_flee_command.py
- factory.py
- Test Suite Refactoring Plan
- asyncio
- test_combat_flee_handler.py
- websocket_handler.py
- SkillAssignmentScreen.tsx
- test_logout_commands_helpers.py
- Environment Contamination Audit Report
- ApplicationContainer
- Process Scope NATS Scripts
- Execution Steps
- canonical_room_id_impl
- zone_config_loader.py
- Dependency Upgrade Strategy
- useThemeContext.ts
- multiplayer-browser-helpers.bundle.js
- codacy.yaml Tool Manifest
- useRoomMapData.ts
- RoomInfoPanel.tsx
- CombatMessagingService
- ._cleanup_player_mutes
- get_npc_name_from_instance
- _process_session_dp_decay_and_death
- Room
- TestVerificationSqlUsersPlayers
- MythosPanel.tsx
- CombatDPSync
- NATSRetryHandler
- Logout Error Scenarios
- Any
- CacheManager
- container_helpers_inventory_display.py
- mock_container
- static_data/package.json
- ActiveLucidityService
- Lint Remediation Prompt - AI-Optimized Version
- ADR-012: python-statemachine for Backend Connection FSM
- TypeScript Compiler Config
- enum
- WebSocket Compliance Review
- properties
- EdgeDetailsPanel.tsx
- E2E Multiplayer Findings
- GameTerminalContext.test.tsx
- parse_last_active_datetime
- PostgresConnection
- properties
- inventory_command_helpers.py
- Execution Steps
- Alertmanager Monitoring Stack
- handle_emote_command
- test_who_commands.py
- MessageBroadcaster
- World Seed Loader
- edgeModalLogic.ts
- React Node Upgrade Analyzer
- NPCEventHandler
- fastapi_integration.py
- useWebSocketConnection.ts
- Cursor Subagents Overview
- RoomNodeData
- Multiplayer Architecture Planning
- test_occupants.py
- room_validator/tests/conftest.py
- Lint Remediation Prompt - AI-Optimized Version
- Execution Steps
- useGameConnectionRefactored.ts
- ADR-003 Dual Event Systems EventBus NATS
- MovementService
- Linting Complexity Alignment
- Pre-commit Logging Validation
- NPCSpawnRuleCRUDMixin
- GameBundle
- test_security_headers.py
- Rate Limiting Scenario Blocked
- usePanelContext.ts
- NPCCacheService
- Phase 1: Core Separation
- Disconnect Grace Period Design
- MythosMUD UI Component Library
- player_connection_setup.py
- Phase 2: Enhanced Features
- type
- generate_sql.mjs
- PrototypeRegistry
- _NPCCombatIntegrationDeps
- asyncio
- GameTickService
- K
- Dual Connection System Spec
- TestPathValidator
- test_event_bus.py
- server/tests/conftest.py
- InventoryMutationGuard
- optimized_validate_player_name
- optimized_security_validator.py
- PanelContextRuntime.tsx
- RoomInfo.tsx
- GameStateProvider
- MessageBatcher
- required
- schemas/unified_room_schema.json
- debrief_command.py
- Any
- Test Server Remediation Prompt - Cursor Executable Version
- required
- Chat Panel Separation Implementation Tasks
- HallucinationFrequencyService
- test_message_filtering_helpers.py
- test_look_item.py
- ProfessionCacheService
- ChatLogger
- test_combat_persistence_handler.py
- test_command_magic.py
- test_invite.py
- test_lucidity_service.py
- get_logger
- NATS Remediation Summary 2026-01-13
- PartyService
- test_database_config_helpers_asyncpg_settings.py
- generate_invites_db.py
- test_channel_broadcasting_strategies.py
- UnknownChannelStrategy
- verify_linting_parity.py
- CoordinateGenerator
- properties
- who_commands.py
- messageHandlers.ts
- _PlayerCombatClearing
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
- combat_loader.py
- test_event_publisher_helpers.py
- StatisticsAggregator
- properties
- MapPerformanceMonitor
- lucidityEventUtils.ts
- properties
- Error Log Analyzer
- properties
- required
- Any
- asyncio
- CoordinateValidator
- _find_item_in_inventory
- parse_shutdown_parameters
- deque
- test_command_processor.py
- SessionManager
- _clear_corrupted_cache_entry
- test_player_event_handlers_utils.py
- format_player_location
- SpellLearningService
- Any
- .resolve_spell_target
- room_hierarchy_schema.json
- GridLayoutManager.tsx
- test_room_service.py
- Game Subsystem Design Documents
- REQUIRED TOOL USAGE PATTERN
- CircuitBreaker Implementation Planning Document
- fixture
- properties
- properties
- ModalContainer.tsx
- multiplayer-playwright-testing.md
- Mypy Type Checking Remediation Prompt - AI-Optimized Version
- OccupantFormatter
- item_factory.py
- Movement Subsystem Design
- load_test_10_players.spec.ts
- enum
- alias_schema.json
- properties
- days
- enum
- player_repository_room.py
- Comprehensive System Audit
- test_maps.py
- ._get_next_sequence
- test_exceptions.py
- Security Implementation
- test_level_service.py
- RetryConfig
- migrate_combat_data.py
- Enhanced Logging Migration Report
- validate_occupant_name
- TestMinimapExplorationInvestigationDoc
- test_player_event_handlers_room.py
- .dispatch
- PostgresRow
- TestValidateCommandBasics
- RateLimiter
- validate_room_data
- optimized_validate_action_content
- optimized_validate_alias_name
- PlayerGuidFormatter
- optimized_sanitize_unicode_input
- optimized_validate_security_comprehensive
- Runner Path
- persist_player
- test_inventory_commands_more_helpers.py
- enum
- weather_patterns
- run-playwright-tests.js
- 🎯 MANDATORY AI EXECUTION PROTOCOL
- required
- Lint Sqlalchemy Async
- quality_fragmentation_lizard.py
- applies_to
- required
- Technical Implementation
- Implementation Notes
- _PopulationLifecycleManager
- test_connection_event_helpers.py
- skills_commands.py
- party_commands.py
- zone_schema.json
- properties
- required
- quality_fragmentation_graph.py
- Protocol
- fixture
- Realtime Connection Compatibility
- handle_channel_command
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
- alias
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
- asyncio
- test_combat_service.py
- test_player_event_handlers_room_left.py
- ._create_grid_map
- test_async_persistence_room_loading.py
- UUID
- enabled
- plane
- test_combat_messaging_integration.py
- test_rate_limiter.py
- threading.py
- ._is_valid_name_for_occupant
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
- MythosMUD
- Chat Panel Separation Specification
- seed_e2e_users.py
- enum
- enum
- room_validator/schemas/unified_room_schema.json
- properties
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
- bonus_tags
- ComprehensiveLoggingMiddleware
- items
- Application Container Analysis
- Async Anti Patterns
- Implementation Details
- Client Layout Baseline
- player_combat_service.py
- get_help_content
- items
- Quest System Features
- Testing Guide
- ._is_uuid_string
- Any
- parse_json_field
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
- name
- holidays
- schedules
- ._load_player_mutes_from_data
- asyncio
- CommandRequest
- asyncio
- asyncio
- _occupation_slots_9
- UUID
- .create_supervised_task
- test_context_binding
- ItemPrototypeModel
- spell_effects_status.py
- Updated Coverage Targets
- test_metadata.py
- alias_storage
- TestCheckRateLimit
- Cursor Hooks Record
- Command Handler Patterns
- _personal_interest_4
- Profession
- test_player_event_handlers_respawn.py
- E 2 E Scenario Scenarios
- test_command_helpers.py
- .add_message
- wrap_third_party_exception
- test_metrics.py
- RoomCacheService
- lifespan_shutdown.py
- create_error_context
- ._connect_nats
- Invite
- Audit Suppressions
- Fix Markdown Line
- Populate Npc Sample
- NPCMovementIntegration
- ._error_callback
- start_hour
- Party
- extract_zone_name
- DecodeLiabilitiesFn
- NATSSubjectManager
- Package Scripts Build
- .call
- Tsconfig Node
- validate_shutdown_admin_permission
- .connect_websocket
- chat_logger
- test_player_repository.py
- mock_utils
- id
- ConnectionPanel.tsx
- global-teardown.ts
- test_dead_letter_queue.py
- player_event_handler_utils
- Phase 2: Categorize and Prioritize Mypy Issues
- Phase 5: Fix Implementation Patterns
- 4. Common Fix Patterns
- DML Migrations
- AppConfig
- Lint Logging Patterns
- enum
- Local Readme Motd
- UI/UX Considerations
- asyncio
- Middleware Command Rate
- fix_markdown_common_issues.py
- applies_to
- 3. Simplified CommandPanel
- Implementation Phases
- ._generate_invite_code
- rest_countdown_task.py
- command
- Upgrade Implementation Plan
- .create_invite
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
- load_zone_configurations
- 2026_02_19_seed_quest_leave_the_tutorial.py
- test_command_validator.py
- 2026_02_26_add_arena_zone_type.py
- rename_players_to_population.py
- CorpseServiceError
- DomainError
- CI Environment Alignment
- GitHub Actions Runner Parity Container
- mock_connection_manager
- description
- CircuitBreakerOpen
- 8. Error Handling and Debugging
- UUID
- Real-Time Architecture
- test_grype.py
- description
- name
- .validate_timestamp
- VirtualizedMessageList.tsx
- generate_unique_codes
- 🔄 COMMON SCENARIOS AND SOLUTIONS
- 🔍 DEBUGGING GUIDE
- 🚀 OPTIMIZATION TIPS
- MessageBroker
- 7. Common Test Failure Solutions
- PostgresCursor
- .get_room_occupants
- 9. Test Maintenance Best Practices
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- 2. Auto-Attack During Grace Period
- 3. Grace Period Visibility & Messaging
- 4. Rest/Quit Command During Combat
- 5. Rest Command Countdown Duration
- 6. Rest Location (Inn/Hotel) Behavior
- 7. Reconnection During Grace Period
- _make_mock_row
- 8. Grace Period After Intentional Disconnect
- 9. Command Blocking During Grace Period
- Recommendations Summary
- Code Graph Entry
- DML Migrations Apply Paths
- Cosmic Horror.md
- asyncio
- day
- duration_hours
- test_initiate_shutdown_countdown_success
- month
- days
- effects
- end_hour
- start_hour
- exits
- SpellMaterialsService
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
- DeadLetterQueue
- Phase 2: Categorize and Prioritize Lint Issues
- WebSocket
- test_player_service.py
- type
- fix_markdown_code_block_style.py
- day
- holiday
- duration_hours
- month
- ConnectionErrorHandler
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
- .is_active
- NpcCombatServiceProtocol
- _EventBusPublishPort
- main
- test_filter_other_players_adds_linkdead_indicator
- MutableHeaders
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
- TestGlobalFunctions
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
- test_help_commands.py
- Graphify Code Graph
- corpse_service
- Any
- plane
- AI Development Workflow
- Architecture Overview
- Path
- test_skills.py
- Cursor Skills Skill
- weight
- asyncio
- handle_explore_command
- .check_and_cleanup
- wearable_service
- test_room_subscription_manager.py
- fix_markdown_file
- analyze-product.md
- create-spec.md
- Analyze Coverage Gaps
- Apply Arena Seed
- create-tasks.md
- execute-tasks.md
- webhook
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
- asyncio
- fixture
- entities/__init__.py
- domain/events/__init__.py
- domain/__init__.py
- domain/repositories/__init__.py
- domain/services/__init__.py
- value_objects/__init__.py
- server/game/magic/__init__.py
- asyncio
- test_damage_grace_period.py
- Security Infrastructure
- Invite Readme
- preferences_service
- .resolve_player_name
- zone
- persistence/utils/__init__.py
- description
- server/structured_logging/__init__.py
- Cursor Plans Pydantic
- server/tests/__init__.py
- command_handler_unified/__init__.py
- .from_dict
- test_websocket_handler_rate_limit.py
- test_error_logging.py
- .on_connection_failed
- monitoring_service
- _get_death_location_name
- player_service
- Standardize Room Names
- Validate Codacy Coverage
- Check No Production
- PrototypeRegistryError
- load_motd
- @eslint/js
- test_create_container_invalid_source_type
- test_get_containers_by_room_id_empty
- test_update_container_invalid_lock_state
- test_delete_container_success
- unit/container_persistence/__init__.py
- unit/game/magic/__init__.py
- test_create_container_database_error
- test_npc_event_handlers.py
- fixture
- AGENTS.md agent instructions
- test_create_container_success
- Architecture Decisions Adr
- Fixture Optimization Complete
- test_create_container_with_items
- test_get_containers_by_entity_id_database_error
- Check No Production
- test_update_container_only_items_json_no_updates
- overrides
- test_update_container_items_json_only_no_item_ids
- Phase 2: Categorize and Prioritize Lint Issues
- Cursor Workflows
- database
- process_item
- SQLAlchemy Async Best Practices
- E 2 E Load Analyze
- risky_operation
- process_batch
- test_occupant_formatter_process_player_name_for_update_valid
- test_occupant_formatter_init
- test_validate_player_name_too_short
- test_update_player_location_player_not_found
- test_occupant_formatter_process_dict_occupant_for_update_fallback_name
- test_occupant_formatter_process_string_occupant_for_update_uuid
- sub_zone
- test_occupant_formatter_separate_occupants_by_type_none
- test_occupant_formatter_is_valid_name_for_occupant_uuid
- test_occupant_formatter_is_valid_name_for_occupant_none
- test_occupant_formatter_is_valid_name_for_occupant_non_string
- Server Realtime Module
- WebSocket
- add_suppression_to_file
- sub_zone
- Check Logging Patterns
- Lint Sql Guardrails
- test_apply_corruption
- test_apply_corruption_player_not_found
- test_heal_player_player_not_found
- 📊 LINT ISSUE CATEGORIZATION GUIDE
- test_get_adjacent_rooms_source_not_found
- test_get_user_by_username_case_insensitive_no_session
- test_process_exit_rows_debug_logging
- test_build_room_objects_success
- test_process_room_rows_with_full_room_id
- test_get_professions_no_session
- test_get_players_batch_with_players
- test_generate_room_id_from_zone_data_with_prefix
- test_build_room_objects_with_non_dict_attributes
- persistence_handler
- test_process_room_rows_empty_list
- test_process_exit_rows_empty_list
- test_process_exit_rows_multiple_exits_same_room
- Archive Planning E 2 E
- sub_zone
- test_nats_service_init_with_subject_manager
- unit/infrastructure/__init__.py
- test_process_exit_rows_zone_single_part
- test_async_logging
- Knip Entry Ignore Dependencies
- dependencies
- test_process_room_rows_with_partial_room_id
- test_build_room_objects_with_dict_attributes
- test_build_room_objects_without_environment_in_attributes
- asyncio
- client
- LoggingMiddleware
- WebSocketRateLimiter
- test_generate_room_id_from_zone_data_needs_generation
- test_process_room_rows_with_none_attributes
- test_process_room_rows_zone_without_slash
- shutdown_process_termination.py
- test_parse_exits_json_string_valid
- Mythosmud Obsidian Sources
- test_parse_exits_json_list
- test_load_room_cache_async_rooms_none
- test_parse_exits_json_other_type
- registry_with_switchblade
- player_service
- nats_broker
- player_repository
- persistence_handler
- test_process_exits_for_room_multiple_exits
- nats_service
- Schemas Intersection Schema
- Schemas Room Schema
- properties
- Arkham Rooms Summary
- Fix Markdownlint Errors
- Fix Syntax Errors
- user_manager
- 1. Component Refactoring
- CombatAuditLogger
- unit/middleware/__init__.py
- unit/monitoring/__init__.py
- unit/persistence/__init__.py
- unit/realtime/integration/__init__.py
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- migration_example_4
- test_mp_regeneration_service.py
- risky_operation
- test_process_combined_rows_no_exits
- id
- test_process_room_rows_with_none_zone_stable_id
- test_process_room_rows_with_none_stable_id
- test_process_exit_rows_missing_zone
- test_process_exit_rows_missing_stable_id
- test_load_room_cache_async_warning_logging
- test_warmup_room_cache
- Mythosmud Obsidian Readme
- test_build_room_objects_with_exits
- generate_schema_from_dev.ps1
- mock_lifecycle_manager
- test_broadcast_combat_attack_personal_message_error
- test_apply_dampening_and_send_message_exception
- test_handle_combat_ended_event
- test_broadcast_combat_end
- eslint.config.js
- test_broadcast_player_died
- test_broadcast_player_mortally_wounded_with_attacker
- test_broadcast_player_mortally_wounded_no_attacker
- database
- test_get_player_data_for_respawn_no_connection_manager
- test_get_player_data_for_respawn_no_persistence
- test_connection_manager_lazy_load_called
- test_send_respawn_event_with_retry_success
- Cursor Hooks Development Plan
- test_send_respawn_event_with_retry_timeout
- test_broadcast_player_mortally_wounded_personal_message_error
- asyncio
- test_send_dp_decay_message
- test_send_dp_decay_message_error
- E 2 E Scenarios Scenario
- test_handle_player_respawned_success
- test_handle_player_respawned_error_handling
- Grype Command Handle Result
- Visualize Arkham Rooms
- test_get_current_lucidity_not_found
- test_get_player_data_for_delirium_respawn_no_connection_manager
- test_get_player_data_for_delirium_respawn_error_handling
- Validate Codacy Coverage
- test_handle_player_delirium_respawned_success
- mock_app
- subscription_manager
- test_broadcast_combat_attack
- Player
- subscription_manager
- test_handle_player_delirium_respawned_error_handling
- test_prepare_room_data_for_respawn_no_connection_manager
- npc_startup_service
- test_get_player_data_for_respawn_no_get_stats
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
- migration_example_1
- Enhanced Logging Guide
- migration_example_12
- migration_example_15
- migration_example_2
- Audit Executive Summary
- test_logging_performance_metrics
- Github Pull Request
- test_basic_logging
- test_fastapi_endpoint_logging
- test_exception_tracking
- test_get_player_data_for_respawn_success
- test_build_room_occupants_message
- test_normalize_event_ids_both_provided
- test_normalize_event_ids_none_values
- .__init__
- test_extract_name_from_occupant_dict_with_player_name
- test_extract_name_from_occupant_dict_with_npc_name
- test_extract_name_from_occupant_dict_with_name
- test_extract_name_from_occupant_string
- test_extract_name_from_occupant_invalid_type
- Whisper Channel System
- properties
- test_extract_occupant_names_valid_names
- properties
- Analyze Comments
- Check Apply Map
- Check Coverage Thresholds
- Simple Room Graph
- test_extract_occupant_names_invalid_names
- test_extract_occupant_names_empty_list
- test_extract_occupant_names_none
- test_add_valid_name_to_lists_player
- test_add_valid_name_to_lists_npc
- test_add_valid_name_to_lists_invalid_name
- test_add_valid_name_to_lists_none_name
- Cursor Skills Skill
- test_process_dict_occupant_with_npc_name
- test_process_dict_occupant_with_name
- test_process_dict_occupant_invalid_name
- test_get_player_by_name_not_found
- test_list_players
- test_resolve_player_name_found
- test_build_occupants_snapshot_data_mixed
- test_build_occupants_snapshot_data_none
- test_create_player_with_stats_name_exists
- Plan Cursor Plans
- test_player_service_init
- test_validate_player_name_valid
- test_count_occupants_by_type_mixed
- test_is_player_disconnecting_true
- test_is_player_disconnecting_string_id
- test_is_player_disconnecting_no_connection_manager
- test_delete_player_success
- test_delete_player_not_found
- unit/services/nats_subject_manager/__init__.py
- messaging_integration
- test_update_player_location_success
- test_is_player_disconnecting_no_disconnecting_players_attr
- test_apply_fear
- test_player_event_handler_utils_init
- test_normalize_player_id_uuid
- test_soft_delete_character_not_found
- test_soft_delete_character_wrong_user
- test_validate_player_name_whitespace
- test_validate_player_name_invalid_characters
- test_delete_player_persistence_fails
- Readme Migrations
- test_soft_delete_character_persistence_fails
- test_create_player_name_exists
- test_apply_fear_player_not_found
- test_normalize_player_id_string
- test_damage_player_player_not_found
- test_validate_player_name_too_short_one_char
- test_normalize_player_id_invalid_string
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
- test_create_channel_command
- test_validate_exit_exists_from_room_not_found
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
- test_subscribe_to_room
- test_load_room_cache_with_rooms_logs_sample_ids
- test_create_get_command
- test_create_equip_command
- test_add_security_headers_to_response_hsts_without_subdomains
- test_broadcast_combat_attack_no_attacker_id
- test_create_player_preferences_success
- test_create_player_preferences_integrity_error
- test_create_unmute_global_command
- test_get_player_preferences_not_found
- test_update_default_channel_not_found
- test_mute_channel_already_muted
- test_delete_player_preferences_success
- test_command_factory_init
- test_create_time_command
- test_delete_player_preferences_not_found
- test_is_channel_muted_invalid_id
- Testing Map Regression
- test_is_channel_muted_not_found
- test_create_logout_command
- test_create_rest_command
- test_handle_unequip_wearable_container_not_found
- test_create_kick_command
- test_add_items_to_wearable_container_capacity_exceeded
- test_create_alias_command
- test_update_wearable_container_items
- test_handle_container_overflow
- Package Engines Node
- include
- Vite Config Proxyauthorization
- test_handle_container_overflow_player_not_found
- test_create_npc_command
- Cursor Hooks Trigger
- mythos_dev mythos_unit mythos_e2e Databases
- test_wearable_container_service_init_no_persistence
- test_create_summon_command
- test_add_items_to_wearable_container_wrong_player
- test_create_goto_command
- test_update_wearable_container_items_not_found
- test_command_factory_has_create_methods
- test_update_wearable_container_items_capacity_exceeded
- test_create_learn_command
- test_update_wearable_container_items_update_fails
- test_get_enum_value_with_enum
- test_create_local_command
- test_create_system_command
- test_handle_equip_wearable_container_filters_non_equipment
- test_handle_unequip_wearable_container_no_allowed_roles
- test_handle_equip_wearable_container_existing_container_no_metadata
- test_broadcast_combat_error
- Cursor Skills Mythosmud
- overrides
- test_handle_equip_wearable_container_existing_container_different_item_instance
- test_broadcast_player_respawn_personal_message_error
- test_broadcast_combat_error_send_error
- test_handle_container_overflow_room_id_empty_string
- test_handle_equip_wearable_container_capacity_exceeded
- test_load_alias_data_invalid_json
- Room Validator Toolkit
- Room Toolkit Validator
- test_get_player_aliases_invalid_alias_data
- test_create_emote_command
- Filter Static Dml
- Fix Room References
- Player Inventory Migration
- test_save_player_aliases
- Run Bug Prevention
- test_remove_alias_nonexistent
- test_clear_aliases
- test_logging_handlers.py
- test_validate_alias_name_invalid_format
- test_validate_alias_command_starts_with_reserved
- test_create_alias_limit_reached
- test_list_alias_files_empty
- Cursor Templates Worktree
- test_delete_player_aliases_io_error
- test_backup_aliases_io_error
- test_get_alias_validator_import_failure
- test_alias_storage_creates_directory
- test_get_alias_file_path
- Codacy Cli
- test_get_player_by_name_database_error
- test_save_player_success
- test_save_player_with_bool_is_admin
- test_save_player_database_error
- test_list_players_database_error
- test_get_player_by_user_id_success
- test_soft_delete_player_not_found
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
- test_get_players_batch_success
- Test Refactoring Executive Summary
- Async Code Review Post Migration
- Migrate Async Persistence
- Phase 2 Service Layer Migration
- Migration 019 Verification
- Whisper System Production-Ready
- Structured Logging Correct Patterns
- test_enqueue_writes_correct_data
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
- test_dequeue_returns_oldest_message
- Mythos Holiday Candidates
- Persistence Repository Architecture
- test_logging_processors.py
- E 2 E Scenarios Lucidity
- test_get_player_lucidity_tier_default
- test_validate_chat_message_fields_sender_name_type_error
- test_validate_chat_message_fields_content_type_error
- test_extract_chat_message_fields_whisper_target_id
- test_extract_chat_message_fields
- Cursor Plans Plan
- test_process_message_with_retry_failure
- Schemas Intersection Schema
- test_send_messages_to_players_blocked
- Schemas Room Schema
- Generate Html Visualization
- test_should_echo_to_sender_not_echo_channel
- Investigations Sessions Session
- Investigations Sessions Combat
- Investigations Sessions Session
- Subsystems Subsystem Design
- test_should_echo_to_sender_with_targets
- Chat Panel
- test_should_echo_to_sender_no_targets_not_notified
- test_should_echo_to_sender_no_targets_already_notified
- test_echo_message_to_sender_success
- test_echo_message_to_sender_exception
- test_broadcast_to_room_with_filtering_exception
- test_get_player_lucidity_tier_with_uuid
- test_build_chat_event
- test_convert_ids_to_uuids
- test_convert_ids_to_uuids_none_target
- test_format_message_for_receiver
- test_get_player_lucidity_tier
- test_subscribe_to_subzone_no_subject_manager
- test_subscribe_to_event_subjects_partial_failure
- test_unsubscribe_from_subzone_decrease_count
- test_handle_player_movement_old_subzone_none
- MythosMUD Server Test Suite
- test_handle_player_movement_new_subzone_none
- test_handle_player_movement_error
- test_subscribe_to_subzone_subscribe_failure
- test_unsubscribe_from_subzone_unsubscribe_failure
- test_handle_combat_started_event
- test_handle_npc_attacked_event
- test_handle_npc_took_damage_event
- test_handle_npc_died_event
- test_handle_player_movement_different_subzone
- test_handle_player_movement_same_subzone
- test_handle_player_movement_exception
- test_subscribe_player_to_room_success
- test_subscribe_player_to_room_invalid_id
- test_subscribe_player_to_room_error
- test_send_room_name_message
- test_prepare_room_data_with_to_dict
- test_send_room_update_to_player_no_connection_manager
- test_send_room_update_to_player_room_not_found
- test_send_room_update_to_player_error_handling
- Player Command Developer
- test_send_occupants_snapshot_to_player_success
- test_send_occupants_snapshot_to_player_string_id
- test_send_occupants_snapshot_to_player_no_connection_manager
- test_send_occupants_snapshot_to_player_error_handling
- test_send_room_updates_to_entering_player_success
- test_log_player_movement_joined
- test_send_room_updates_to_entering_player_error_handling
- test_process_player_entered_event_success
- test_process_player_entered_event_no_player_info
- test_handle_player_entered_success
- test_handle_player_entered_no_connection_manager
- test_handle_player_entered_no_player_info
- test_log_player_movement_left
- test_log_player_movement_no_room
- test_broadcast_player_entered_message
- Cursor Plans Plan
- Pyrightconfig Extends Extra Paths
- Room Toolkit Validator
- Check Logging Consistency
- E 2 E Reset Players
- Investigations Sessions Session
- Investigations Sessions Session
- Investigations Sessions Session
- Investigations Sessions Session
- Cursor Skills Mythosmud
- Enhanced Structured Logging System
- Archive System Magic
- Archive Lucidity System
- Archive Room Planning
- test_adjust_room_drop_invalid_index
- test_list_room_drops_with_drops
- test_add_room_drop_new_room
- test_add_room_drop_existing_room
- test_take_room_drop_success
- Cursor Commands New
- test_take_room_drop_index_out_of_range
- test_take_room_drop_zero_quantity
- test_take_room_drop_full_quantity
- test_take_room_drop_partial_quantity
- test_take_room_drop_removes_empty_room
- test_adjust_room_drop_index_out_of_range
- test_adjust_room_drop_quantity_zero
- test_adjust_room_drop_negative_quantity
- test_add_room_drop_zero_quantity
- test_list_room_drops
- test_add_room_drop_error_handling
- test_take_room_drop_error_handling
- test_adjust_room_drop_error_handling
- test_list_room_drops_error
- test_list_room_drops_empty
- E 2 E Comprehensive Overview
- E 2 E Multiplayer Rules
- test_add_room_drop
- test_add_room_drop_invalid_quantity
- test_take_room_drop_all
- test_take_room_drop_invalid_index
- test_adjust_room_drop
- test_adjust_room_drop_remove
- test_add_room_occupant
- test_add_room_occupant_multiple
- Codacy Instructions Review
- test_add_room_occupant_new_room
- test_remove_room_occupant
- test_remove_room_occupant_not_occupant
- test_remove_room_occupant_removes_empty_room
- Cursor Plans Plan
- test_room_subscription_manager_init
- test_set_async_persistence
- Remediation Investigations Plans
- Schemas Intersection Schema
- Schemas Intersection Schema
- Schemas Intersection Schema
- test_subscribe_to_room_multiple_players
- Schemas Room Schema
- Schemas Room Schema
- test_unsubscribe_from_room
- test_unsubscribe_from_room_not_subscribed
- test_subscribe_to_room_error
- test_unsubscribe_from_room_error
- test_broadcast_player_mortally_wounded
- Schemas Unified Room
- Batch Fix Suppressions
- Check Codacy Yaml
- test_get_muted_channels_success
- TestPostgresConnectionPool
- test_is_channel_muted_invalid_channel
- test_mute_channel_not_found
- Cursor Skills Mythosmud
- test_get_player_preferences_invalid_id
- test_update_default_channel_invalid_id
- test_mute_channel_invalid_id
- test_remove_alias_case_insensitive
- test_create_alias_invalid_command
- test_backup_aliases_nonexistent_file
- Archive Dual Connection
- test_get_alias_validator_creation_failure
- test_create_cast_command
- test_command_factory_create_nonexistent_command
- test_create_reply_command
- Scenario 42 Quest Log Visible After Login
- Archive Prd
- Verify Schema Match
- Claude Authoritative Reference
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
- `webhook()` --calls--> `JSONResponse`  [INFERRED]
  monitoring/webhook-receiver.py → docs/examples/logging/fastapi_integration.py
- `migration_example_4()` --calls--> `measure_performance()`  [INFERRED]
  docs/examples/logging/migration_examples.py → server/monitoring/performance_monitor.py
- `migration_example_5()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/migration_examples.py → server/structured_logging/logging_context.py

## Import Cycles
- 2-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 2-file cycle: `client/src/components/map/useAsciiMap.ts -> client/src/components/map/useAsciiMapState.ts -> client/src/components/map/useAsciiMap.ts`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/realtime/connection_initialization.py -> server/realtime/monitoring/health_monitor.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/connection_manager_health_cleanup.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `client/src/components/panels/chatPanelChannelFilter.ts -> client/src/components/panels/chatPanelChannelVisibility.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelChannelFilter.ts`
- 3-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelUnreadBump.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`

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

## Communities (1897 total, 599 thin omitted)

### Community 0 - "test_zone_config_loader.py"
Cohesion: 0.14
Nodes (28): async_load_zone_configurations(), Async helper to load zone configurations from PostgreSQL database., _empty_zone_load_result(), asyncio, MonkeyPatch, Unit tests for zone configuration loader. Tests the zone_config_loader module…, Test process_zone_rows() handles empty result., Test process_zone_rows() parses JSON string fields. (+20 more)

### Community 1 - "test_connection_delegates.py"
Cohesion: 0.04
Nodes (74): cleanup_dead_websocket_impl(), Validate a JWT token for a connection. Args: token: JWT token to validate…, Clean up a dead WebSocket connection. Args: player_id: The player's ID…, validate_token_impl(), asyncio, Unit tests for connection delegates. Tests the connection_delegates module…, Test cleanup_dead_websocket_impl() handles websocket not in active_websockets., Test cleanup_dead_websocket_impl() handles close timeout. (+66 more)

### Community 2 - "test_users.py"
Cohesion: 0.02
Nodes (125): AuthenticationBackend, get_current_user_with_logging(), get_user_db(), get_username_auth_backend(), Any, AsyncSession, Request, UUID (+117 more)

### Community 3 - "Alias"
Cohesion: 0.03
Nodes (69): Alias, Any, BaseModel, Alias model for command aliases. Stores player command aliases for quick access…, String representation of the alias., Check equality based on name and command., Hash based on name and command for use in sets/dicts., Update the updated_at timestamp to current time. (+61 more)

### Community 4 - "test_combat_flee_helpers.py"
Cohesion: 0.05
Nodes (58): _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id(), _PlayerForFlee, _PlayerPositionServiceLike, AppWithState, Protocol (+50 more)

### Community 5 - "websocket_initial_state.py"
Cohesion: 0.05
Nodes (79): add_npc_occupants_to_list(), check_and_send_death_notification(), get_event_handler_for_initial_state(), _get_event_handler_from_app_host(), get_npc_lifecycle_manager_from_connection_manager(), _get_player_for_death_check(), _NpcLifecycleManagerForOccupants, prepare_initial_room_data() (+71 more)

### Community 6 - "NATSService"
Cohesion: 0.02
Nodes (72): NATS, CombatEventPublisher, _CombatPublishJob, Any, Shared NATS publish path for combat events., Publish combat started event to NATS., Publish combat ended event to NATS., Publish player attacked event to NATS. (+64 more)

### Community 7 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (134): DropCommand, EquipCommand, GetCommand, InventoryCommand, PickupCommand, PutCommand, field_validator, model_validator (+126 more)

### Community 8 - "User"
Cohesion: 0.02
Nodes (225): auth_service(), Simulate auth service., auth_service, IntegrityError, Game mechanics API endpoints for MythosMUD server. This module handles all game…, get_current_superuser(), get_current_verified_user(), get_optional_current_user() (+217 more)

### Community 9 - "is_player_in_login_grace_period"
Cohesion: 0.03
Nodes (120): Get login grace period status for player., cancel_login_grace_period(), get_login_grace_period_remaining(), _grace_period_expiration_handler(), _grace_period_task(), is_player_in_login_grace_period(), Any, UUID (+112 more)

### Community 10 - "MythosMUDError"
Cohesion: 0.02
Nodes (190): ErrorSeverity, Error severity levels for logging and handling., AuthenticationError, ConfigurationError, create_error_context(), GameLogicError, handle_exception(), MythosMUDError (+182 more)

### Community 11 - "TargetMatch"
Cohesion: 0.03
Nodes (98): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules. Keeps…, Application object with a ``state`` namespace (dynamic attributes)., Resolve combat target using target resolution service. Public API., Validate target_result and resolve to a live NPC target_match., Resolve combat target using target resolution service., BaseModel (+90 more)

### Community 12 - "ErrorType"
Cohesion: 0.02
Nodes (126): JSONResponse, Error handlers package for MythosMUD. This package provides specialized error…, convert_pydantic_error(), _ExtractedErrorInfo, _ExtractedFieldErrorInfo, handle_pydantic_error(), TypedDict, Unpack (+118 more)

### Community 13 - "test_player_model.py"
Cohesion: 0.02
Nodes (87): Unit tests for Player SQLAlchemy model. Tests the Player model methods…, Test Player.get_inventory() handles empty inventory., Test Player.set_inventory() serializes to JSON., UUID fields in inventory entries should serialize to strings., Test Player can be instantiated with required fields., Test Player.get_status_effects() parses JSON status effects., Test Player.set_status_effects() serializes to JSON., Test Player.get_equipped_items() returns equipped items from _equipped_items… (+79 more)

### Community 14 - "ContainerServiceError"
Cohesion: 0.01
Nodes (273): AbstractContextManager, handle_close_container_exceptions(), handle_loot_all_exceptions(), handle_open_container_exceptions(), handle_transfer_items_exceptions(), Any, Exception, Request (+265 more)

### Community 15 - "players/__init__.py"
Cohesion: 0.04
Nodes (90): apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest, post (+82 more)

### Community 16 - "NPCCombatIntegrationService"
Cohesion: 0.01
Nodes (326): Combat messaging integration with real-time messaging system. This package…, CombatMessagingIntegration, Combat messaging integration with real-time messaging system. Re-exports from…, Integrates combat messaging with the real-time messaging system. This service…, NPCCombatDataProvider, Get player name for messaging. Args: player_id: ID of the player Returns:…, Get the current room ID for a player. Args: player_id: ID of the player (must…, Provides data retrieval and preparation for NPC combat. (+318 more)

### Community 17 - "BaseCommand"
Cohesion: 0.01
Nodes (246): AliasCommand, AliasesCommand, Alias command models for MythosMUD. This module provides command models for…, Command for creating or viewing command aliases., Command for listing all aliases., Command for removing an alias., UnaliasCommand, BaseCommand (+238 more)

### Community 18 - "test_security_validator.py"
Cohesion: 0.02
Nodes (189): field_validator, Validate alias name format using centralized validation., Validate command content for security using centralized validation., Validate alias name format using centralized validation., Communication command models for MythosMUD. This module provides command models…, Validate target player name format using centralized validation., Validate mute reason for security using centralized validation., Unit tests for security validation utilities. Tests the security validator… (+181 more)

### Community 19 - "TargetResolutionService"
Cohesion: 0.03
Nodes (77): Initialize the spell targeting service. Args: target_resolution_service:…, PersistenceProtocol, PlayerServiceProtocol, Player, Protocol, Room, UUID, Validate player exists and is in a room. Returns (room_id, error_result). (+69 more)

### Community 20 - "test_inventory_service_helpers.py"
Cohesion: 0.28
Nodes (8): Clear lazy singletons so each test gets a fresh init path. For unit tests only;…, reset_shared_inventory_services_for_tests(), fixture, Unit tests for inventory_service_helpers.get_shared_services., _request_with_persistence(), reset_shared_inventory_services_autouse(), test_get_shared_services_initializes_and_reuses_singletons(), test_get_shared_services_raises_without_async_persistence()

### Community 21 - "test_command_communication.py"
Cohesion: 0.03
Nodes (96): EmoteCommand, LocalCommand, MeCommand, PoseCommand, field_validator, Command for whispering to a specific player., Validate message content for security using centralized validation., Command for replying to the last whisper received. (+88 more)

### Community 22 - "connection_manager.py"
Cohesion: 0.04
Nodes (87): delegate_game_state_provider(), delegate_game_state_provider_sync(), delegate_message_broadcaster(), delegate_personal_message_sender(), delegate_personal_message_sender_sync(), delegate_room_event_handler(), Delegation helpers for connection manager. This module provides helper…, Generic delegate for game state provider methods. Args: game_state_provider:… (+79 more)

### Community 23 - "test_look_container.py"
Cohesion: 0.02
Nodes (184): _extract_container_metadata(), _find_container_in_room(), _find_container_in_room_or_equipped(), _find_container_via_inner_container(), _find_container_via_wearable_service(), _find_container_wearable(), _format_container_contents(), _format_container_display() (+176 more)

### Community 24 - "test_wearable_container_service.py"
Cohesion: 0.04
Nodes (74): asyncio, Unit tests for wearable container service. Tests the WearableContainerService…, Test handle_unequip_wearable_container returns None when no item_instance_id., Test handle_unequip_wearable_container preserves container., Test get_wearable_containers_for_player returns containers., Test get_wearable_containers_for_player returns empty list when no containers., Test get_wearable_containers_for_player handles errors gracefully., Test add_items_to_wearable_container adds items. (+66 more)

### Community 25 - "test_config_models.py"
Cohesion: 0.05
Nodes (47): _default_cors_origins(), _parse_env_list(), _parse_list_from_string(), Parse non-empty string as JSON list or CSV. Used by _parse_env_list., Parse a string from the environment as JSON list or CSV., Derive default CORS origins with environment taking precedence., DatabaseConfig, Any (+39 more)

### Community 26 - "test_npc_service.py"
Cohesion: 0.04
Nodes (87): _def_row(), _mock_result_mappings_all(), mock_session(), npc_service(), asyncio, fixture, Unit tests for NPC service. Tests the NPCService class., Test NPCService initialization. (+79 more)

### Community 27 - "api/monitoring.py"
Cohesion: 0.04
Nodes (113): _assemble_health_response(), force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_health_status(), get_memory_alerts() (+105 more)

### Community 28 - "test_look_npc.py"
Cohesion: 0.02
Nodes (165): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_description(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result() (+157 more)

### Community 29 - "test_admin_commands.py"
Cohesion: 0.05
Nodes (62): asyncio, Unit tests for admin command handlers. Tests the admin command handler…, Test handle_mute_command() with no target player., Test handle_mute_command() successful execution., Test handle_unmute_command() when user manager is not available., Test handle_unmute_command() with no target player., Test handle_unmute_command() successful execution., Test handle_unmute_command() succeeds when target was not muted (E2E cleanup… (+54 more)

### Community 30 - "_parse_jsonb_column"
Cohesion: 0.05
Nodes (45): _parse_jsonb_column(), Parse a JSONB column value from database. JSONB columns may be returned as: -…, Test parsing None JSONB column., Test parsing string JSONB column., Test parsing dict JSONB column., Test parsing empty string JSONB column., Test parsing list JSONB column., Test parsing invalid JSON string. (+37 more)

### Community 31 - "test_command_admin.py"
Cohesion: 0.03
Nodes (82): GotoCommand, NPCCommand, field_validator, Command for shutting down the server (admin only). Args can be: - Empty:…, Command for NPC administrative utilities with subcommands., Administrative command for summoning prototypes into the current room., Validate prototype ID format. Args: value: The prototype ID to validate…, Command for teleporting a player to the admin's location. (+74 more)

### Community 32 - "test_websocket_handler_core.py"
Cohesion: 0.03
Nodes (86): handle_websocket_message(), WebSocket, Handle a WebSocket message from a player. Args: websocket: The WebSocket…, Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), asyncio, Unit tests for core websocket handler functions. Tests core WebSocket handler…, Test _process_message processes message. (+78 more)

### Community 33 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (124): asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not…, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes. (+116 more)

### Community 34 - "inventory_commands.py"
Cohesion: 0.05
Nodes (65): Inventory and equipment command handlers for MythosMUD. Heavy handlers live in…, handle_pickup_command(), Move an item stack from room drops into the player's inventory., handle_unequip_command(), CommandResponse, Player, Unequip an item into the player's inventory., _unequip_persist_or_rollback() (+57 more)

### Community 35 - "test_inventory_helpers_extended.py"
Cohesion: 0.08
Nodes (37): ensure_item_instance_for_pickup(), Ensure item instance exists in database for picked up item., Resolve player from persistence and current user., resolve_player(), asyncio, Extended unit tests for inventory command helper functions. Tests additional…, Test _persist_player handles InventorySchemaValidationError., Test _persist_player handles general errors. (+29 more)

### Community 36 - "Room"
Cohesion: 0.02
Nodes (103): InstanceManager for MythosMUD. Manages instanced rooms: creates, stores, and…, Any, UUID, Add a player to the room without triggering an event. This method is used for…, Remove a player from the room without triggering an event. This method is used…, Remove a player from the room and trigger event. Args: player_id: The ID of the…, Add an object to the room and trigger event. Args: object_id: The ID of the…, Remove an object from the room and trigger event. Args: object_id: The ID of… (+95 more)

### Community 37 - "lifecycle_periodic.py"
Cohesion: 0.09
Nodes (26): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD. This module defines configuration settings for…, Configuration for NPC lifecycle maintenance. This class centralizes all timing…, Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…, Get a summary of all NPC configuration values. Returns: Dictionary containing…, Clean up old lifecycle records (delegates to lifecycle_periodic)., Perform periodic maintenance (delegates to lifecycle_periodic). (+18 more)

### Community 38 - "server/dependencies.py"
Cohesion: 0.01
Nodes (194): LevelUpHook, get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service() (+186 more)

### Community 39 - "ContainerComponent"
Cohesion: 0.01
Nodes (215): loot_all_items(), Request, Loot all eligible items from a container., _emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), Any (+207 more)

### Community 40 - "PlayerCombatService"
Cohesion: 0.01
Nodes (180): CombatCommandHandler, CombatCommandHandlerExtras, _NpcWithLife, Any, AppWithState, Protocol, Combat command handler class and shared helpers. Extracted from combat.py to…, Combat service for command modules. (+172 more)

### Community 41 - "lifespan_startup.py"
Cohesion: 0.04
Nodes (77): Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), subscribe_room_occupants_refresh(), _ensure_room_cache_before_npc_startup(), _get_item_prototype_count(), _get_item_prototype_entries(), initialize_chat_service() (+69 more)

### Community 42 - "server/schemas/__init__.py"
Cohesion: 0.01
Nodes (295): cleanup_admin_sessions(), get_admin_audit_log(), get_admin_sessions(), get, post, Request, Admin session and audit log endpoints under /admin/npc. Split out from…, Get active admin sessions. (+287 more)

### Community 43 - "coerce_int"
Cohesion: 0.07
Nodes (29): Get player stats as dictionary. Returns a MutableDict instance that…, Set player stats from dictionary. Accepts both plain dict and MutableDict…, Check if player is alive (DP > 0)., Check if player is mortally wounded (0 >= DP > -10). Returns: True if player…, Check if player is dead (DP <= -10). Returns: True if player has -10 DP or below, Get player's current health state. Returns: "alive" if DP > 0…, Get stats used for combat participant creation. Returns current_dp, max_dp, and…, Get player determination points (DP) as percentage. (+21 more)

### Community 44 - "NATSMessageHandler"
Cohesion: 0.02
Nodes (65): NATSMessageHandler, _not_configured_async(), Any, UUID, Compare two room IDs using canonical room ID resolution., Get player's current room ID from online players cache., Get player's current room ID from async persistence layer., Check if a player is currently in the specified room. (+57 more)

### Community 45 - "test_npc_startup_service.py"
Cohesion: 0.10
Nodes (19): Unit tests for NPC startup service. Tests the NPCStartupService class., Test _spawn_optional_npcs() spawns based on probability., Test _get_default_room_for_sub_zone() returns correct room for known sub-zone., Test _get_default_room_for_sub_zone() returns None for unknown sub-zone., Test _get_default_room_for_sub_zone() is case insensitive., Test get_npc_startup_service() returns service instance., Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute., Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center. (+11 more)

### Community 46 - "test_command_moderation.py"
Cohesion: 0.03
Nodes (79): AddAdminCommand, AdminCommand, MuteCommand, MuteGlobalCommand, field_validator, Command for administrative utilities with subcommands., Validate and normalize admin subcommand names., Command for muting a player. (+71 more)

### Community 47 - "BehaviorEngine"
Cohesion: 0.02
Nodes (121): BehaviorEngine, Any, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string…, Evaluate boolean conditions and variable lookups. Args: condition: Condition… (+113 more)

### Community 48 - "get_username_from_user"
Cohesion: 0.05
Nodes (67): _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), _load_follow_context(), Any, Follow commands for MythosMUD. Handlers for /follow, /unfollow, and /following.…, Handle /following - show who you follow and who follows you. (+59 more)

### Community 49 - "CombatParticipant"
Cohesion: 0.01
Nodes (299): get_current_tick(), Get the current game tick., CombatInstance, CombatParticipant, CombatResult, UUID, Check if participant can perform voluntary combat actions. Unconscious (DP <=…, Apply damage to this participant and determine resulting death states.… (+291 more)

### Community 50 - "test_container_websocket_events.py"
Cohesion: 0.09
Nodes (41): emit_container_closed(), emit_container_decayed(), emit_container_opened(), emit_container_opened_to_room(), emit_container_updated(), Any, ContainerComponent, datetime (+33 more)

### Community 51 - ".get_instance"
Cohesion: 0.01
Nodes (339): add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., main(), Load seed data and verify., close_db(), get_test_database_url() (+331 more)

### Community 52 - "CombatParticipantData"
Cohesion: 0.04
Nodes (47): _build_combat_instance(), _build_participant(), CombatInitializer, _compute_turn_order(), UUID, Combat initialization logic. Handles creation and setup of combat instances., Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…, Build CombatParticipant from CombatParticipantData. (+39 more)

### Community 53 - "test_command_factories.py"
Cohesion: 0.03
Nodes (69): Unit tests for command factories. Tests the CommandFactory class., Test create_go_command delegates to exploration factory., Test create_sit_command delegates to exploration factory., Test create_stand_command delegates to exploration factory., Test create_lie_command delegates to exploration factory., Test create_ground_command delegates to exploration factory., Test create_pickup_command delegates to inventory factory., Test create_drop_command delegates to inventory factory. (+61 more)

### Community 54 - "BaseEvent"
Cohesion: 0.03
Nodes (79): Distributed EventBus that uses NATS for cross-instance event distribution.…, Any, T, Task, Legacy wrapper for API compatibility during transition., Pure async event processing loop replacing the dangerous threading pattern., Separate async and sync subscribers for appropriate execution. Uses…, Execute sync subscribers sequentially with error isolation. Sync subscribers… (+71 more)

### Community 55 - "ExplorationService"
Cohesion: 0.04
Nodes (95): ExplorationService, Any, AsyncSession, UUID, Get room UUID by stable_id (hierarchical room ID). Args: stable_id:…, Mark room as explored using the provided session. Args: session: Database…, Get list of room IDs that a player has explored. Args: player_id: UUID of the…, Check if a player has explored a specific room. Args: player_id: UUID of the… (+87 more)

### Community 56 - "test_combat_schema.py"
Cohesion: 0.08
Nodes (46): Draft7Validator, add_default_combat_data_to_config(), add_default_combat_data_to_stats(), CombatSchemaValidationError, get_combat_stats_summary(), Any, Exception, Combat system JSON schema validation. This module provides JSON schema… (+38 more)

### Community 57 - "Stats"
Cohesion: 0.03
Nodes (73): computed_field, generate_random_stats(), Generate Stats with random attribute values. Factory function for creating…, Any, model_validator, Core character statistics with Lovecraftian horror elements., Initialize Stats with provided data. For random stat generation, use…, Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes… (+65 more)

### Community 58 - "test_command_combat.py"
Cohesion: 0.03
Nodes (75): AttackCommand, KickCommand, PunchCommand, field_validator, Command for attacking a target., Validate combat target name format using centralized validation., Command for punching a target., Validate combat target name format using centralized validation. (+67 more)

### Community 59 - "api/conftest.py"
Cohesion: 0.17
Nodes (15): mock_connection_manager(), mock_container(), mock_container_service(), mock_persistence(), mock_player(), mock_request(), mock_user(), fixture (+7 more)

### Community 60 - "_apply_exploration_filter_if_needed"
Cohesion: 0.17
Nodes (16): RoomDictList, _apply_exploration_filter_if_needed(), Any, Apply exploration filter to rooms if requested and user is not admin. Args:…, asyncio, fixture, Non-admin with player record gets filter_rooms_by_exploration(stable room rows)., If user has no linked player, exploration cannot run; unknown rooms list… (+8 more)

### Community 61 - "CombatAttackHandler"
Cohesion: 0.05
Nodes (33): get_app_instance(), Return the runtime app instance attached during lifespan startup. This provides…, Check if participant is alive enough to be in combat. For players: alive if DP…, CombatAttackHandler, Any, UUID, Apply damage to target and update combat state. Args: combat: Combat instance…, Validate attack and retrieve combat participants. Args: attacker_id: ID of the… (+25 more)

### Community 62 - "test_command_factories_utility.py"
Cohesion: 0.02
Nodes (97): Unit tests for utility command factories. Tests the UtilityCommandFactory class…, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+89 more)

### Community 63 - "magic_service_completion.py"
Cohesion: 0.12
Nodes (23): _is_heal_other_target(), MagicServiceCompletionMixin, Any, UUID, Casting completion flow for spellcasting. Mixin that handles completing a…, Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…, Parse target_id from casting state. Returns None if missing or invalid., Apply costs and queue spell for next combat round. Returns True if queued,… (+15 more)

### Community 64 - "LucidityFluxService"
Cohesion: 0.06
Nodes (39): FluxServiceConfig, lookup_profile(), normalize_environment_config(), period_label(), Any, datetime, Configuration and normalization for passive lucidity flux., Optional configuration for PassiveLucidityFluxService. All fields have defaults. (+31 more)

### Community 65 - ".create_look_command"
Cohesion: 0.07
Nodes (28): Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_look_command() creates LookCommand., Test create_look_command() creates LookCommand with target., Test create_look_command() with explicit player target type., Test create_look_command() with explicit NPC target type., Test create_look_command() with explicit item target type. (+20 more)

### Community 66 - "ui-v2/types.ts"
Cohesion: 0.05
Nodes (76): PanelManager(), PanelManagerProps, minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapPanelSection(), MinimapPanelSectionProps, PanelContainer, PanelContainerBody() (+68 more)

### Community 67 - "test_user_manager.py"
Cohesion: 0.02
Nodes (97): Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() successfully globally mutes a player., Test mute_global() fails when trying to mute admin. (+89 more)

### Community 68 - "test_quest_instance_repository.py"
Cohesion: 0.06
Nodes (58): QuestInstance, Per-character quest state: one row per player per quest., Any, datetime, UUID, QuestInstanceRepository, QuestInstance repository for quest subsystem. CRUD for quest_instances via…, Get the quest instance for this player and quest (any state). Returns None if… (+50 more)

### Community 69 - "PayloadOptimizer"
Cohesion: 0.22
Nodes (8): PayloadOptimizer, Any, Create an incremental update payload containing only changed fields. Args:…, Optimizes payloads for WebSocket transmission. Features: - Size limit…, Initialize the payload optimizer. Args: max_payload_size: Maximum payload size…, Calculate the size of a payload in bytes. Args: payload: The payload dictionary…, Compress a large payload using gzip compression. Args: payload: The payload…, Optimize a payload by applying size limits and compression if needed. Args:…

### Community 70 - "test_command_service.py"
Cohesion: 0.03
Nodes (71): MythosValidationError, Test handle_transfer_items_exceptions returns 400 for ValidationError., command_service(), mock_request(), mock_user(), asyncio, fixture, Unit tests for command service. Tests the CommandService class which handles… (+63 more)

### Community 71 - "test_connection_establishment.py"
Cohesion: 0.03
Nodes (106): _cleanup_dead_connections(), _cleanup_failed_connection(), establish_websocket_connection(), _find_dead_connections(), Any, UUID, WebSocket, Connection establishment management for connection manager. This module handles… (+98 more)

### Community 72 - "connection_manager_health_cleanup.py"
Cohesion: 0.05
Nodes (57): delegate_connection_cleaner(), delegate_connection_cleaner_sync(), delegate_error_handler(), delegate_health_monitor(), delegate_health_monitor_sync(), Any, Generic delegate for health monitor methods., Generic delegate for synchronous health monitor methods. (+49 more)

### Community 73 - "asyncio"
Cohesion: 0.09
Nodes (23): asyncio, Test resolve_player_name() when player is not found., Test create_player_with_stats() successful creation., Test validate_player_name() with name too long., Test create_player() successful creation., Test get_online_players() returns online players., Test damage_player() damages player., Test get_user_characters() returns user's characters. (+15 more)

### Community 74 - "CombatService"
Cohesion: 0.02
Nodes (143): _apply_taunt_and_maybe_broadcast(), AppWithState, Protocol, UUID, Taunt command flow: validation and execution. Extracted from combat.py to…, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Apply taunt and broadcast target switch if aggro changed. Returns error dict or… (+135 more)

### Community 75 - "test_combat_validator.py"
Cohesion: 0.02
Nodes (96): combat_validator(), fixture, Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_combat_command with target name too long., Test validate_combat_command when rate limited., Test validate_combat_command handles exceptions gracefully., Test validate_target_exists with exact match., Test validate_target_exists with case-insensitive match. (+88 more)

### Community 76 - "EldritchIcon.tsx"
Cohesion: 0.04
Nodes (61): ChatMessage, ChatMessageType, ChatPanelTest(), mockClick, mockCreateObjectURL, mockRevokeObjectURL, DraggablePanelResizeHandles(), DraggablePanelResizeHandlesProps (+53 more)

### Community 77 - "request_with_app_container"
Cohesion: 0.05
Nodes (63): Shared mock wiring for communication command unit tests., Return (request, container) with request.app.state.container wired. Typed…, request_with_app_container(), asyncio, Unit tests for local, global, and system chat command handlers., Test handle_global_command when player level is too low., Test handle_global_command successful execution., Test handle_system_command with no message. (+55 more)

### Community 78 - "test_room_renderer.py"
Cohesion: 0.04
Nodes (70): Unit tests for room_renderer utility functions. Tests the utility functions in…, Test clone_room_drops() returns empty list for None., Test format_room_drop_lines() formats room drops., Test format_room_drop_lines() returns empty message for empty drops., Test format_room_drop_lines() handles None., Test format_room_drop_lines() uses fallback for missing item_name., Test build_room_drop_summary() returns newline-separated summary., Test build_room_drop_summary() handles empty drops. (+62 more)

### Community 79 - "test_npc_models.py"
Cohesion: 0.04
Nodes (58): NPCRelationship, NPC relationship model. Defines relationships between different NPC types., String representation of the NPC relationship., Unit tests for NPC models. Tests the NPCDefinitionType enum and NPCDefinition,…, Test NPCDefinition.set_base_stats() serializes to JSON., Test NPCDefinition.get_behavior_config() parses JSON., Test NPCDefinition.set_behavior_config() serializes to JSON., Test NPCDefinition.get_ai_integration_stub() parses JSON. (+50 more)

### Community 80 - "time.py"
Cohesion: 0.01
Nodes (383): create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryThresholdMonitor, Any, Managed Task Cleanup Service - Runtime Detection for Memory Threshold…, Generate status report for diagnostic monitoring. Returns: Dictionary…, Runtime detection and cleanup of orphaned tasks based on memory thresholds.…, Create an instance of the MemoryThresholdMonitor with user-specified… (+375 more)

### Community 81 - "test_auth_utils.py"
Cohesion: 0.02
Nodes (123): PasswordHasher, create_hasher_with_params(), get_hash_info(), hash_password(), is_argon2_hash(), needs_rehash(), Validate password input before Argon2 hashing., Hash a plaintext password using Argon2id. This function provides superior… (+115 more)

### Community 82 - "Reporter"
Cohesion: 0.03
Nodes (46): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+38 more)

### Community 83 - "get_npc_instance_service"
Cohesion: 0.01
Nodes (331): _create_npc_services_on_app(), Create NPC spawning, lifecycle, population services and instance service.…, Get NPC instance from the spawning service. Public API., Get NPC instance from the spawning service., NPCBundle, NPC bundle: lifecycle manager, spawning service, population controller. Depends…, NPC services: lifecycle, spawning, population control., Initialize NPC services and load definitions. (+323 more)

### Community 84 - "test_websocket_handler_helpers_extended.py"
Cohesion: 0.05
Nodes (57): mock_connection_manager(), mock_validator(), mock_websocket(), asyncio, fixture, Extended unit tests for websocket handler helper functions. Tests additional…, Test _send_error_response() handles WebSocketDisconnect., Test _send_error_response() returns False for RuntimeError indicating… (+49 more)

### Community 85 - "test_status_commands.py"
Cohesion: 0.04
Nodes (90): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_profession_info(), _get_status_persistence(), handle_status_command() (+82 more)

### Community 86 - "WebSocketManager"
Cohesion: 0.22
Nodes (6): WebSocket connection manager with enhanced logging., Establish WebSocket connection with enhanced logging., Disconnect WebSocket with enhanced logging., Send message to specific client with enhanced logging., Broadcast message to all connected clients with enhanced logging., WebSocketManager

### Community 87 - "create_access_token"
Cohesion: 0.04
Nodes (57): create_access_token(), decode_access_token(), timedelta, Decode and validate a JWT access token., Create a JWT access token., Test decoding invalid access token returns None., Test decoding expired access token returns None., Test access token creation with custom secret key. (+49 more)

### Community 88 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (88): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+80 more)

### Community 89 - "map/types.ts"
Cohesion: 0.11
Nodes (21): defaultReactFlowOptions, getEdgeTypes(), getNodeTypes(), ExitEdge, ExitEdgeBody(), ExitEdgeLabels(), ExitEdgeProps, getEdgeStrokeStyle() (+13 more)

### Community 90 - "combat_service.py"
Cohesion: 0.01
Nodes (349): CombatEndedEvent, CombatStartedEvent, CombatTimeoutEvent, CombatTurnAdvancedEvent, NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent (+341 more)

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
Cohesion: 0.06
Nodes (42): asyncio, Unit tests for go command handler. Tests the go command for player movement., Test _setup_go_command corrects room ID mismatch., Test _validate_player_posture returns True for standing player., Test _validate_player_posture returns False for sitting player., Test _validate_player_posture returns False for lying player., Test _validate_player_posture handles player without get_stats., Test _validate_exit returns None when direction not in exits. (+34 more)

### Community 95 - "test_lucidity_recovery_commands.py"
Cohesion: 0.04
Nodes (94): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+86 more)

### Community 96 - "multiplayer.ts"
Cohesion: 0.10
Nodes (46): nudgeStandBothPlayers(), primeBothForCoLocate(), waitForLookReflected(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers() (+38 more)

### Community 97 - "test_nats_service.py"
Cohesion: 0.03
Nodes (86): asyncio, Unit tests for NATS service. Tests the NATSService class and NATSMetrics., Test NATSService initialization with NATSConfig., Test NATSService initialization with dict config., Test NATSService initializes connection pool structures., Test connect() successfully connects to NATS., Test connect() returns False when state machine blocks connection., Test connect() handles connection failure. (+78 more)

### Community 98 - "test_character_creation_service.py"
Cohesion: 0.03
Nodes (62): CharacterCreationService, Any, UUID, Validate character stats against class prerequisites. Args: stats: The stats…, Create a new character with specific stats. Args: name: The character's name…, Get information about all available character classes and their prerequisites.…, Service class for character creation and stats generation business operations., Get a description for a character class. (+54 more)

### Community 99 - "LoggedHTTPException"
Cohesion: 0.02
Nodes (148): apply_rate_limiting_for_close_container(), apply_rate_limiting_for_loot_all(), apply_rate_limiting_for_open_container(), apply_rate_limiting_for_transfer(), execute_transfer(), handle_container_service_error(), Request, UUID (+140 more)

### Community 100 - "Dependency Risk Analyzer"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 101 - "RealTimeEventHandler"
Cohesion: 0.04
Nodes (37): Any, UUID, Get the next sequence number for events., Subscribe to relevant game events., Delegate player entered event to specialized handler., Delegate player left event to specialized handler., Delegate NPC entered event to specialized handler., Delegate NPC left event to specialized handler. (+29 more)

### Community 102 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.06
Nodes (81): _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch(), filter_valid_items() (+73 more)

### Community 103 - "test_player_presence_tracker.py"
Cohesion: 0.02
Nodes (179): Disconnect grace period management for MythosMUD. This module handles the…, age_off_disconnected_sessions(), _cleanup_player_references(), _collect_disconnect_keys(), _get_session_maps_for_age_off(), handle_player_disconnect_broadcast(), _purge_expired_sessions_from_maps(), Player (+171 more)

### Community 104 - "test_player_death_service.py"
Cohesion: 0.03
Nodes (87): mock_event_bus(), mock_player(), mock_player_combat_service(), mock_session(), player_death_service(), player_death_service_no_dependencies(), asyncio, fixture (+79 more)

### Community 105 - "test_npc_utils.py"
Cohesion: 0.03
Nodes (75): Check if this NPC is required to spawn., extract_definition_id_from_npc(), extract_npc_metadata(), extract_room_id_from_npc(), get_zone_key_from_room_id(), Any, NPC Utility Functions. This module provides utility functions for extracting…, Extract room ID from NPC instance with fallback logic. Args: npc_instance: The… (+67 more)

### Community 106 - "test_metrics_endpoints.py"
Cohesion: 0.06
Nodes (79): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+71 more)

### Community 107 - "test_room_sync_service.py"
Cohesion: 0.03
Nodes (74): T, Clear room data cache. Args: room_id: Specific room ID to clear, or None to…, Enhanced room synchronization service. Provides improved event processing…, Process events with proper ordering to prevent race conditions. Args: event:…, RoomSyncService, mock_room_service(), asyncio, fixture (+66 more)

### Community 108 - "RoomLoader"
Cohesion: 0.03
Nodes (54): fixture, Create a temporary directory for testing., temp_dir(), Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path. (+46 more)

### Community 109 - "asyncio"
Cohesion: 0.11
Nodes (21): PartyChannelStrategy, Strategy for party channel broadcasting. Delivers only to current party members., asyncio, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() sends personal message., Test WhisperChannelStrategy.broadcast() handles missing target_player_id. (+13 more)

### Community 110 - "CircuitBreaker"
Cohesion: 0.05
Nodes (62): CircuitBreaker, CircuitState, Enum, timedelta, Circuit breaker pattern for NATS message processing. Implements three-state…, Circuit breaker states. - CLOSED: Normal operation, requests pass through -…, Get current circuit state. Returns: Current CircuitState AI: For monitoring and…, Manually reset circuit breaker to CLOSED state. Clears all counters and timers.… (+54 more)

### Community 111 - "CorpseOverlay.tsx"
Cohesion: 0.04
Nodes (68): BackpackTab(), BackpackTabProps, ContainerSplitPane(), ContainerSplitPaneProps, ContainerInventoryPaneProps, ContainerItemRow(), ContainerSplitPaneView(), ContainerSplitPaneViewModel (+60 more)

### Community 112 - "PlayerEnteredRoom"
Cohesion: 0.02
Nodes (118): _FollowTargetValue, PlayerEnteredRoom, Event fired when a player enters a room. This event is triggered when a player…, FollowService, _is_npc_follow_value(), Any, TypeGuard, UserManager (+110 more)

### Community 113 - "test_nats_broker.py"
Cohesion: 0.04
Nodes (74): asyncio, Unit tests for NATS message broker. Tests the NATSMessageBroker class., Test connect() passes TLS options to nats.connect when tls_enabled=True., Test disconnect() does nothing when no client., Test disconnect() successfully disconnects., Test disconnect() unsubscribes from all subscriptions., Test disconnect() handles unsubscribe errors gracefully., Test disconnect() raises MessageBrokerError on disconnect failure. (+66 more)

### Community 114 - "command.py"
Cohesion: 0.04
Nodes (84): Admin command models for MythosMUD. This module provides command models for…, CommandType, Direction, StrEnum, Base command models and enums for MythosMUD. This module provides the…, Valid directions for movement and looking., Valid command types for MythosMUD., ChannelCommand (+76 more)

### Community 115 - "UserManager"
Cohesion: 0.07
Nodes (33): UUID, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Get the mute data file path for a specific player., Update cache to mark load as failed., Convert mute_info datetime and UUID objects to JSON-serializable formats., Save player mutes to data dictionary for JSON serialization., Save channel mutes to data dictionary for JSON serialization. (+25 more)

### Community 116 - "test_look_player.py"
Cohesion: 0.04
Nodes (95): _get_visible_equipment(), Get visible equipment from player, excluding internal/hidden slots. Visible…, _apply_grace_period_labels(), _find_matching_players(), _format_player_look_display(), _get_players_in_room(), _handle_player_look(), _player_id_uuid() (+87 more)

### Community 117 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (86): _collect_rotatable_logs(), detect_environment(), ensure_log_directory(), BoundLogger, Path, Logging utilities for directory management, path resolution, and environment…, Resolve log_base path to absolute path relative to project root. Args:…, Collect non-empty log files eligible for rotation. (+78 more)

### Community 118 - "test_game.py"
Cohesion: 0.04
Nodes (58): broadcast_message(), get_game_status(), get_mythos_time(), get, post, Return the current Mythos calendar metadata for HUD initialization. In-memory…, Get current game status and connection information., Broadcast a message to all connected players (admin only). Requires superuser… (+50 more)

### Community 119 - "test_combat_monitoring_service.py"
Cohesion: 0.02
Nodes (93): Alert, AlertSeverity, AlertType, CombatMetrics, end_combat_monitoring(), get_combat_metrics(), get_combat_monitoring(), Enum (+85 more)

### Community 120 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.05
Nodes (73): _dispatch_player_event(), _format_liabilities(), LucidityChangeEventExtras, LiabilityStackEntry, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send rescue progress/status updates to either participant. (+65 more)

### Community 121 - "test_nats_message_handler_chat.py"
Cohesion: 0.12
Nodes (15): Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _convert_ids_to_uuids handles UUID objects., Test _should_echo_to_sender returns False for non-chat messages., Test _should_echo_to_sender returns False when message_id is None., Test _validate_chat_message_fields validates fields., Test _validate_chat_message_fields raises error when fields missing. (+7 more)

### Community 122 - "spell_effects.py"
Cohesion: 0.04
Nodes (69): NpcIntegrationStringIdPort, NpcLifecycleManagerPort, NpcSpellDamageTarget, PlayerPersistenceSpellPort, PlayerServiceHealPort, Protocol, UUID, Shared Protocol types for spell effect modules. Used by basedpyright to type… (+61 more)

### Community 123 - "GameTerminal.tsx"
Cohesion: 0.07
Nodes (47): buildHealthStatus(), ChatMessage, formatPosture(), GameTerminal(), Player, Room, HolidayBanner(), HolidayBannerProps (+39 more)

### Community 124 - "SchemaValidator"
Cohesion: 0.04
Nodes (35): Convert legacy string format exits to new object format internally. This allows…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in…, Validates room definitions against JSON schema. Supports both legacy string…, SchemaValidator, Tests for the schema validator module. Tests JSON schema validation, exit… (+27 more)

### Community 125 - "DeadLetterMessage"
Cohesion: 0.12
Nodes (16): DeadLetterMessage, Message stored in dead letter queue. Contains message data and failure context…, Test DeadLetterMessage.to_dict() converts to dictionary., Test list_messages() returns all messages., Test list_messages() respects limit parameter., Test replay_message() retrieves and removes message., Test delete_message() removes message file., Test cleanup_old_messages() removes old messages. (+8 more)

### Community 126 - "test_population_control.py"
Cohesion: 0.02
Nodes (138): Get population statistics for a given zone. Args: zone_key: Zone key in format…, PopulationStats, Any, Statistics for NPC population in a zone or sub-zone., Initialize population statistics. Args: zone_id: The zone identifier…, Add an NPC to the population statistics. Args: npc_type: Type of the NPC…, Remove an NPC from the population statistics. Args: npc_type: Type of the NPC…, Convert population statistics to dictionary. (+130 more)

### Community 127 - "LucidityService"
Cohesion: 0.04
Nodes (68): Failover callback that relocates catatonic players to the sanitarium., CatatoniaObserverProtocol, clamp_lucidity(), coerce_metadata_dict(), decode_liabilities(), encode_liabilities(), lucidity_event_source(), LucidityAdjustmentFinalizeContext (+60 more)

### Community 128 - "PathValidator"
Cohesion: 0.03
Nodes (60): option, Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Fix missing exits field. Returns True if fixed., Fix missing optional fields. Returns True if any fixed., Fix missing fields based on errors. Returns True if any fixed., Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer (+52 more)

### Community 129 - "test_websocket_helpers.py"
Cohesion: 0.05
Nodes (56): check_shutdown_and_reject(), convert_uuids_to_strings(), get_occupant_names(), is_client_disconnected_exception(), load_player_mute_data(), BaseException, WebSocket, Load player mute data when they connect. AI: Uses async version to avoid… (+48 more)

### Community 130 - ".__post_init__"
Cohesion: 0.03
Nodes (39): MythosHourTickEvent, NPCListened, NPCSpoke, PlayerMortallyWoundedEvent, QuestCompleted, Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type. (+31 more)

### Community 131 - "chatPanelRuntimeUtils.ts"
Cohesion: 0.08
Nodes (42): ChatExportDialog(), ChatExportDialogProps, collectFocusableElements(), filterMessagesForChannelView(), buildChatExportCSV(), buildChatExportCsvRow(), buildChatExportJSON(), ChatExportPayload (+34 more)

### Community 132 - "test_room_utils.py"
Cohesion: 0.07
Nodes (42): Unit tests for room_utils. Tests utility functions for room operations., Test get_subzone_local_channel_subject() generates subject., Test get_subzone_local_channel_subject() returns None for invalid room ID., Test extract_subzone_from_room_id() extracts subzone., Test extract_subzone_from_room_id() extracts different subzone., Test extract_subzone_from_room_id() returns None for invalid format., Test get_zone_from_room_id() extracts zone., Test get_zone_from_room_id() extracts different zone. (+34 more)

### Community 133 - "test_movement_service.py"
Cohesion: 0.05
Nodes (45): mock_event_bus(), mock_persistence(), movement_service(), asyncio, fixture, Unit tests for movement service. Tests the MovementService class., Test add_player_to_room() when player is not found., Test remove_player_from_room() successfully removes player. (+37 more)

### Community 134 - "test_alias_commands.py"
Cohesion: 0.06
Nodes (58): _extract_alias_params(), handle_alias_command(), Any, Extract alias_name and command from command_data. Returns (alias_name, command)., Handle the alias command for creating and viewing aliases. Args: command_data:…, mock_alias(), mock_alias_storage(), asyncio (+50 more)

### Community 135 - "WebSocketMessageValidator"
Cohesion: 0.04
Nodes (62): MessageValidationError, BaseModel, Exception, WebSocket message validation for MythosMUD. This module provides comprehensive…, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Validate message against Pydantic schema. Args: message: Parsed JSON message…, Raised when message validation fails. (+54 more)

### Community 136 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, get_skills_catalog returns list of skill dicts., get_player_skills for owned player returns list of skill dicts., get_player_skills for another user's player returns None., record_successful_skill_use delegates to repo.record_use with correct args., get_skills_used_this_level returns distinct skill_ids from repo., When roll > current value, update_value called with new value (gain 1 or 1d10)., roll_skill_check when player has no value for skill_id returns False. (+9 more)

### Community 137 - "RoomDataCache"
Cohesion: 0.05
Nodes (32): Manages room data caching and freshness validation., Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Clear room data cache. Args: room_id: Specific room ID to clear, or None to…, RoomDataCache, Unit tests for room data cache. Tests the RoomDataCache class for caching and…, Test clear_cache clears all rooms when room_id is None., Test clear_cache handles nonexistent room gracefully., Test get_cache_stats with empty cache. (+24 more)

### Community 138 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_player_data_for_respawn() returns None when player not found., Test get_player_data_for_respawn() handles errors., Test send_respawn_event_with_retry() is a no-op when connection manager is…, Test get_current_lucidity() returns lucidity from database., Test get_player_data_for_delirium_respawn() successfully retrieves player data., Test get_player_data_for_delirium_respawn() returns None when player not found., test_get_current_lucidity_found() (+5 more)

### Community 139 - "api/character_creation.py"
Cohesion: 0.03
Nodes (118): _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _check_shutdown_status(), _convert_stat_summary_to_stat_summary_model(), create_character_with_stats(), _dispatch_roll_stats(), _execute_create_character(), _prepare_create_character_request() (+110 more)

### Community 140 - "CombatPersistenceHandler"
Cohesion: 0.13
Nodes (14): CombatPersistenceHandler, Any, UUID, Synchronously persist player DP to database. This is the actual persistence…, Persist player DP to database in background (fire-and-forget). This method runs…, Handles combat-related persistence operations., Initialize the persistence handler. Args: combat_service: Reference to the…, Persist player DP to database in background (fire-and-forget). Public API… (+6 more)

### Community 141 - "catatonia_check.py"
Cohesion: 0.04
Nodes (61): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+53 more)

### Community 142 - "test_nats_message_handler_subzone_events.py"
Cohesion: 0.10
Nodes (19): Unit tests for NATS message handler subzone and event handling. Tests subzone…, Test get_event_subscription_count returns count., Test is_event_subscription_active checks subscription., Test _get_user_manager returns injected manager., Test _get_user_manager falls back to global manager., Test _get_event_handler_map delegates to event handler., Test _validate_event_message delegates to event handler., Test track_player_subzone_subscription handles player moving to different… (+11 more)

### Community 143 - "ScheduleService"
Cohesion: 0.03
Nodes (62): Provides schedule lookups for NPCs and environmental consumers., Get all schedule entries. Returns: list[ScheduleEntry]: List of all schedule…, Get the number of schedule entries. Returns: int: The count of schedule entries, ScheduleService, patch, Unit tests for schedule service. Tests the ScheduleService class for managing…, Test get_active_entries returns empty list when no matches., Test get_active_entries returns matching entries. (+54 more)

### Community 144 - "test_rest_command.py"
Cohesion: 0.04
Nodes (86): Check if player is resting or in login grace period, interrupt rest if needed.…, Check if player is resting or in login grace period, interrupt rest if needed., _begin_seated_rest_countdown(), cancel_rest_countdown(), _check_player_in_combat(), _check_rest_location(), _disconnect_player_intentionally(), _execute_rest_flow() (+78 more)

### Community 145 - "test_user_schemas.py"
Cohesion: 0.08
Nodes (34): Auth domain schemas: user and invite., Pydantic schemas for Invite model. This module defines Pydantic schemas for…, Pydantic schemas for User model. This module defines Pydantic schemas for user…, Base user schema with common fields., Schema for creating a new user., Schema for reading user data., Schema for updating user data., UserBase (+26 more)

### Community 146 - "ContainerService"
Cohesion: 0.08
Nodes (33): ContainerService, _filter_container_data(), _get_enum_value(), Any, ContainerComponent, ContainerLockState, InventoryStack, UUID (+25 more)

### Community 147 - "PlayerRespawnService"
Cohesion: 0.09
Nodes (28): PlayerRespawnService, AsyncSession, datetime, Player, UUID, Return current_dp as an int, defaulting to 0 for non-numeric values., Return (allowed, current_dp_int) for limbo movement gate checks., Publish delirium respawn event when event bus is available. (+20 more)

### Community 148 - "test_npc_combat_integration_class.py"
Cohesion: 0.04
Nodes (46): NPCAttacked, Event fired when an NPC attacks a target. This event is triggered when an NPC…, Initialize the event with proper type., Resolve attack_damage from behavior config with robust typing., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target., Attack a specific target., Handle attacking target action. (+38 more)

### Community 149 - "Spell"
Cohesion: 0.05
Nodes (45): UUID, Process a spell effect on a target. Args: spell: The spell being cast target:…, Route to the appropriate effect handler based on spell.effect_type., Process heal effect (normal heals and steal-life). Delegated to…, Process damage effect., Apply damage to a player target., Apply damage to an NPC target; publish events and sync combat participant., ADR-016: Add spell damage threat to NPC's hate list for the caster. No-op if… (+37 more)

### Community 150 - "AliasStorage"
Cohesion: 0.03
Nodes (143): AliasStorage, List all alias files in the storage directory., Manages player alias storage in JSON files. Each player's aliases are stored in…, handle_admin_command(), _handle_admin_status_command(), _handle_admin_time_command(), Any, Administrative commands for MythosMUD. This module contains the main admin… (+135 more)

### Community 151 - "TestHelperFunctions"
Cohesion: 0.03
Nodes (39): asyncio, Test _ensure_alias_storage returns None on error., Test _check_grace_period_block returns None when no connection manager., Test _check_grace_period_block returns None when not in grace period., Test _prepare_command_for_processing returns rate limit result., Test helper functions in command_handler_unified., Test _prepare_command_for_processing returns validation result., Test _prepare_command_for_processing returns empty result after cleaning. (+31 more)

### Community 152 - "StatsGenerator"
Cohesion: 0.05
Nodes (32): Any, Stats, Roll Size using formula: (2D6+6)*5 (range 40-90)., Roll stats using 3d6 method (scaled to 15-90 range)., Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)., Generate stats using a point-buy system (balanced, scaled to 1-100 range)., Check if stats meet the prerequisites for a given class. Args: stats: The…, Get a list of classes that the character qualifies for. Args: stats: The… (+24 more)

### Community 153 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.09
Nodes (48): _build_python_call_usage_map(), _call_target_name(), check_ai_guardrails(), _check_exports_and_tiny_functions(), _check_single_use_file(), _collect_code_texts(), _collect_python_public_defs_and_tiny(), _guardrail_scan_inputs() (+40 more)

### Community 154 - "websocket_helpers.py"
Cohesion: 0.06
Nodes (57): _AppStateForPlayerService, build_basic_player_data(), convert_schema_to_dict(), _ensure_player_in_room_occupancy(), _fetch_room_for_tracked_player(), get_player_and_room(), get_player_service_from_connection_manager(), get_player_stats_data() (+49 more)

### Community 155 - "test_connection_statistics.py"
Cohesion: 0.05
Nodes (51): Get session management statistics., Get detailed presence information for a player., Validate player presence and clean up any inconsistencies., Get presence tracking statistics., Get online player information by display name., get_online_player_by_display_name_impl(), get_player_presence_info_impl(), get_presence_statistics_impl() (+43 more)

### Community 156 - "test_player_schema_converter_weapon.py"
Cohesion: 0.07
Nodes (38): Item prototype registry for command modules., _inventory_item_with_weapon(), PlayerSchemaConverter, Any, Get stats, inventory, and status_effects from player, handling async methods., Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…, Get PositionState from position value, with fallback to STANDING., Create PlayerRead schema from player object. (+30 more)

### Community 157 - "test_active_lucidity_service.py"
Cohesion: 0.05
Nodes (59): active_lucidity_service(), mock_session(), asyncio, fixture, Unit tests for active lucidity service. Tests the ActiveLucidityService class…, Test apply_encounter_lucidity_loss() for acclimated encounter., Test apply_encounter_lucidity_loss() raises error for unknown category., Test apply_encounter_lucidity_loss() handles string player_id. (+51 more)

### Community 158 - "NPCDefinitionCRUDMixin"
Cohesion: 0.07
Nodes (27): NPCDefinitionCRUDMixin, Any, AsyncSession, Execute create_npc_definition stored procedure and return the created…, Validate create_npc_definition parameters. Raises ValueError if invalid., Log successful NPC definition creation., Validate NPC update parameters., Add a simple field to update_data if value is not None. (+19 more)

### Community 159 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages. These schemas define the structure and… (+55 more)

### Community 160 - "EventBus"
Cohesion: 0.01
Nodes (315): _JSONDict, EventBus, AbstractEventLoop, Event bus for MythosMUD. This module provides the EventBus class that…, Set the main event loop - now properly managed for async compatibility., Signal shutdown to async processing loop., Cancel the main processing task if it exists., Cancel all active tasks and wait for graceful shutdown. (+307 more)

### Community 161 - "test_room_subscription_manager_drops.py"
Cohesion: 0.20
Nodes (9): Unit tests for room subscription manager drop functions. Tests the room drop…, Test take_room_drop() with quantity larger than available., Test adjust_room_drop() successfully adjusts quantity., Test add_room_drop() handles negative quantity gracefully., Test take_room_drop() removes drop from room., test_add_room_drop_negative_quantity(), test_adjust_room_drop_success(), test_take_room_drop() (+1 more)

### Community 162 - "PlayerSavePreparer"
Cohesion: 0.13
Nodes (18): _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Player save/upsert helpers for PlayerRepository. Handles inventory validation,…, Validate and serialize inventory payload. Returns (inventory_json,… (+10 more)

### Community 163 - "test_validation.py"
Cohesion: 0.03
Nodes (64): custom_length_validator(), fixture, Unit tests for NATS Subject Validator. Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter. (+56 more)

### Community 164 - ".state"
Cohesion: 0.06
Nodes (64): _apply_grounding_adjustment(), _complete_ground_command(), _get_ground_services(), handle_ground_command(), handle_rescue_command(), _normalize_player_ids(), Any, UUID (+56 more)

### Community 165 - "ChatHistoryPanel.tsx"
Cohesion: 0.08
Nodes (34): EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW, isGloballyExcludedFromChannelView(), isVisibleInChannelView(), matchesChannelSelection(), resolveMessageChannelForFilter(), bumpUnreadCountForMessage(), canIncrementUnreadForChannel(), messageIsEligibleForUnreadCount() (+26 more)

### Community 166 - "CombatConfiguration"
Cohesion: 0.04
Nodes (50): CombatConfiguration, CombatConfigurationError, CombatConfigurationScope, CombatConfigurationService, get_combat_config(), get_combat_configuration(), is_combat_available(), Any (+42 more)

### Community 167 - "_asyncio_mark"
Cohesion: 0.10
Nodes (27): _asyncio_mark, _await_shutdown_result(), Test handle_shutdown_command() when player service is not available., Test handle_shutdown_command() when player is not found., Test handle_shutdown_command() when player lacks admin permission., Test handle_shutdown_command() with invalid parameters., Test handle_shutdown_command() with cancel action., Test handle_shutdown_command() with cancel when no active shutdown. (+19 more)

### Community 168 - "chat_message_senders.py"
Cohesion: 0.07
Nodes (62): RoomChatHistory, normalize_player_id(), Any, ChatMessage, UUID, Channel message senders (system, whisper, party, global)., Send a whisper message from one player to another. This function publishes the…, Normalize player identifiers to string form. (+54 more)

### Community 169 - "inventory_equip_command.py"
Cohesion: 0.09
Nodes (39): _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), normalize_equipped_items(), normalize_inventory_slots(), InventoryStack, Player, Find the equipped slot and item after equipping. (+31 more)

### Community 170 - "test_corpse_lifecycle_service.py"
Cohesion: 0.03
Nodes (78): asyncio, Unit tests for corpse lifecycle service. Tests the CorpseLifecycleService class., Test create_corpse_on_death() handles persistence errors., Test can_access_corpse() allows admin access., Test can_access_corpse() allows owner access., Test can_access_corpse() allows access when no owner., Test can_access_corpse() blocks access during grace period., Test can_access_corpse() allows access after grace period. (+70 more)

### Community 171 - "test_party_service.py"
Cohesion: 0.04
Nodes (49): Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves., Leader can disband the party., Non-leader cannot disband. (+41 more)

### Community 172 - "maps.py"
Cohesion: 0.06
Nodes (68): _apply_exploration_filter_if_needed(), _AsciiMapViewport, _build_ascii_map_response(), _build_ascii_minimap_response(), _CoordGenCtx, _ensure_coordinates_generated(), _filter_explored_rooms(), get_ascii_map() (+60 more)

### Community 173 - "test_quest_service.py"
Cohesion: 0.05
Nodes (63): _make_definition_row(), _make_turn_in_definition_row(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, Unit tests for QuestService. Covers: resolve_name_to_quest_id, start_quest,…, start_quest returns error when quest id not found. (+55 more)

### Community 174 - "test_async_persistence_room_cache.py"
Cohesion: 0.14
Nodes (13): Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test _generate_room_id_from_zone_data with None values., Test _parse_exits_json with invalid JSON string., Test _process_exits_for_room processes exits with direction., Test _process_exits_for_room skips exits without direction., Test _process_combined_rows processes rows with exits JSON., Test _process_exit_rows handles missing direction., test_generate_room_id_from_zone_data_none_values() (+5 more)

### Community 175 - "fixtures/integration/__init__.py"
Cohesion: 0.07
Nodes (44): FixtureRequest, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+36 more)

### Community 176 - "test_look_helpers.py"
Cohesion: 0.03
Nodes (87): _get_health_label(), _get_lucidity_label(), _get_wearable_container_service(), _parse_instance_number(), Any, Get descriptive lucidity label based on lucidity percentage. Args: stats:…, Get shared WearableContainerService instance, initializing it lazily if needed.…, Parse instance number from target string. Supports two formats: - "backpack-2"… (+79 more)

### Community 177 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (35): CatatoniaRegistry, datetime, UUID, In-memory registry tracking catatonic investigators., Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not… (+27 more)

### Community 178 - "mapUtils.ts"
Cohesion: 0.20
Nodes (20): useMapLayout(), useRoomMapData(), MapControls(), MapControlsProps, useRoomMapEditorData(), RoomMapViewer(), createMockNodes(), mockRooms (+12 more)

### Community 179 - "test_occupant_formatter.py"
Cohesion: 0.11
Nodes (17): Unit tests for occupant formatter. Tests the occupant_formatter module classes…, Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes player…, Test OccupantFormatter._process_string_occupant_for_update() adds valid string., Test OccupantFormatter.separate_occupants_by_type() separates dict NPCs., Test OccupantFormatter.separate_occupants_by_type() processes string occupants., Test OccupantFormatter.separate_occupants_by_type() handles mixed types., Test OccupantFormatter.separate_occupants_by_type() handles empty list. (+9 more)

### Community 180 - "admin_shutdown_command.py"
Cohesion: 0.10
Nodes (37): _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state(), countdown_loop(), _create_countdown_task() (+29 more)

### Community 181 - "test_connection_cleaner.py"
Cohesion: 0.09
Nodes (28): connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue(), mock_rate_limiter(), mock_room_manager() (+20 more)

### Community 182 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 183 - "test_container_persistence.py"
Cohesion: 0.05
Nodes (41): Unit tests for container_persistence package container persistence module.…, Test create_container with invalid capacity_slots., Test create_container with invalid lock_state., Test get_container when container doesn't exist., Test get_containers_by_entity_id with no containers., Test delete_container when container doesn't exist., Test get_container handles database errors., Test create_container handles case where no ID is returned. (+33 more)

### Community 184 - "useGameClientV2Container.ts"
Cohesion: 0.11
Nodes (34): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), performGameClientLogout(), deriveActiveEffectsForHeader(), buildGameClientV2ContainerReturn() (+26 more)

### Community 185 - "normalize_command"
Cohesion: 0.06
Nodes (28): clean_command_input(), normalize_command(), Clean and normalize command input by collapsing multiple spaces and stripping…, Normalize command input by removing optional slash prefix. Supports both…, Check if a single word command should be treated as an emote. This function…, should_treat_as_emote(), patch, Unit tests for command input processing. Tests command normalization, cleaning,… (+20 more)

### Community 186 - "GameClientV2.tsx"
Cohesion: 0.06
Nodes (34): calculateOccupantCount(), GameClientV2(), GameClientV2Content(), MainDockPanelId, MainDockSlotMeta, ChatHistoryPanel(), LocationPanel(), LocationPanelProps (+26 more)

### Community 187 - "ChatService"
Cohesion: 0.04
Nodes (37): ChatService, Any, UUID, Normalize player identifiers to string form., Send a say message to players in the same room. This method publishes the…, Send a local message to players in the same sub-zone. This method publishes the…, Send a global message to all players. This method publishes the global message…, Send a party (ephemeral group) chat message. Only current party members receive… (+29 more)

### Community 188 - "QuestService"
Cohesion: 0.05
Nodes (58): Persist player after spell mutations., Quest subsystem: service, goal progression, rewards., _build_collect_n_progress(), _call_add_item_to_inventory(), _collect_goal_prototype_id(), _collect_goal_required_count(), _consume_collect_goals_from_player(), _definition_completion_mode_error() (+50 more)

### Community 189 - "fixtures/unit/__init__.py"
Cohesion: 0.13
Nodes (17): MockerFixture, dummy_request(), fakerandom(), Any, fixture, Unit-tier fixtures with strict mocking and in-memory fakes., Provide deterministic random seed for unit tests., Provide a minimal request object for testing with container support. (+9 more)

### Community 190 - "quest_commands.py"
Cohesion: 0.09
Nodes (39): _collect_progress_sync(), Return quest_service.sync_collect_progress when it is callable., _active_npc_ids_in_room(), _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence() (+31 more)

### Community 191 - "MemoryProfiler"
Cohesion: 0.05
Nodes (46): BaseModel, Unit tests for memory profiler utilities. Tests the MemoryProfiler class…, Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test Pydantic model for memory profiling tests., Test MemoryProfiler.print_model_memory_usage() doesn't raise., Test MemoryProfiler initialization. (+38 more)

### Community 192 - "test_command_exploration.py"
Cohesion: 0.07
Nodes (36): GoCommand, LookCommand, field_validator, Command for looking around, in a specific direction, or at an NPC., Validate direction is one of the allowed values., Command for moving in a specific direction., Validate direction is one of the allowed values., Unit tests for exploration command models. Tests the LookCommand and GoCommand… (+28 more)

### Community 193 - "test_connection_initialization.py"
Cohesion: 0.08
Nodes (37): initialize_connection_cleaner(), initialize_connection_manager(), initialize_connection_maps(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging(), initialize_room_event_handler() (+29 more)

### Community 194 - "CorpseLifecycleService"
Cohesion: 0.09
Nodes (25): CorpseLifecycleService, _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Corpse lifecycle service for unified container system. As documented in the…, Create a corpse container when a player dies. (+17 more)

### Community 195 - "IdleMovementHandler"
Cohesion: 0.03
Nodes (91): _cfg_bool(), _cfg_float(), IdleMovementHandler, _npc_alive_and_active(), _npc_id_str(), _passes_movement_probability(), NPC Idle Movement Handler for MythosMUD. This module provides idle movement…, Core gating for idle movement (interval handled by scheduler). (+83 more)

### Community 196 - "_handle_admin_set_stat_command"
Cohesion: 0.07
Nodes (52): _get_app_or_error(), _handle_admin_set_stat_command(), _parse_set_stat_args(), _parse_value_from_args(), Any, Parse value from args[2] when value_input is None and args has at least 3…, Parse stat name, target player, and value from command data., Validate stat name and value inputs. (+44 more)

### Community 197 - "test_async_persistence_core.py"
Cohesion: 0.05
Nodes (54): asyncio, Unit tests for async persistence layer: init, close, player, user, room,…, Test get_players_by_user_id delegates to PlayerRepository., Test get_active_players_by_user_id delegates to PlayerRepository., Test get_user_by_username_case_insensitive with successful lookup., Test get_user_by_username_case_insensitive when user not found., Test get_user_by_username_case_insensitive with database error., Test save_player delegates to PlayerRepository. (+46 more)

### Community 198 - "eventHandlers/types.ts"
Cohesion: 0.07
Nodes (50): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), eventHandlers (+42 more)

### Community 199 - "MessageHandler"
Cohesion: 0.08
Nodes (22): Subscribe to a subject/topic with a message handler. Args: subject:…, Return the live NPC combat integration service for delegation. Prefer…, _resolve_npc_combat_service_raw(), FollowResponseMessageHandler, MessageHandler, PartyInviteResponseMessageHandler, ABC, Any (+14 more)

### Community 200 - "test_message_filtering.py"
Cohesion: 0.04
Nodes (49): message_filtering_helper(), mock_connection_manager(), asyncio, fixture, Unit tests for message filtering. Tests the MessageFilteringHelper class., Test should_apply_mute_check() returns True for sensitive channels., Test should_apply_mute_check() returns False for non-sensitive channels., Test compare_canonical_rooms() returns True for same rooms. (+41 more)

### Community 201 - "channels.ts"
Cohesion: 0.09
Nodes (32): ChannelActivityIndicators(), ChannelActivityIndicatorsProps, getActivityColor(), ChannelSelectorSection(), ChatHistoryToggle(), ChatStatistics(), ChatPanelHistorySearch(), ChatPanelHistorySearchProps (+24 more)

### Community 202 - "test_combat_persistence_handler_events.py"
Cohesion: 0.07
Nodes (38): asyncio, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully., Test _publish_player_dp_update_event_impl handles no NATS service., Test _publish_player_dp_update_event_impl with all optional parameters., Test _publish_player_dp_update_event_impl handles event bus publish error., Test _publish_player_dp_correction_event publishes correction event., Test _publish_player_dp_correction_event handles errors gracefully. (+30 more)

### Community 203 - "test_map_helpers.py"
Cohesion: 0.08
Nodes (36): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities. Extracted from… (+28 more)

### Community 204 - "test_inventory_helpers.py"
Cohesion: 0.03
Nodes (105): _equip_stack_from_inventory_index(), Equipment-related helper functions for inventory commands., Resolve slot from command data for unequip command., Deep-copy inventory stack at index and normalize slot_type., Resolve item index from command data for equip command., resolve_equip_item_index(), resolve_unequip_slot(), _try_resolve_unequip_by_search() (+97 more)

### Community 205 - "server/models/game.py"
Cohesion: 0.03
Nodes (95): Player schema conversion utilities. This module handles conversion of Player…, AttributeType, InventoryItem, Player, PositionState, BaseModel, StrEnum, Game-related models for MythosMUD. This module contains models specific to the… (+87 more)

### Community 206 - "MonitoringDashboard"
Cohesion: 0.05
Nodes (46): PerformanceStats, _initialize_enhanced_systems(), Initialize enhanced logging and monitoring systems. Returns: LogAggregator…, ExceptionStats, get_exception_tracker(), Get the global exception tracker instance. Returns: Global ExceptionTracker…, Statistics for exception tracking., Monitoring package for MythosMUD server. (+38 more)

### Community 207 - "EventHandler"
Cohesion: 0.06
Nodes (22): _as_event_data_dict(), EventHandler, Handler for NATS event messages., Initialize event handler. Args: connection_manager: ConnectionManager instance…, Get mapping of event types to their handler methods. Returns: Dictionary…, Validate that event message has required fields. Args: event_type: Event type…, Handle incoming event messages from NATS. Args: message_data: Event message…, Handle player_entered event. Args: data: Event data containing player and room… (+14 more)

### Community 208 - "useAsciiMapState.ts"
Cohesion: 0.06
Nodes (44): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+36 more)

### Community 209 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 210 - "MemoryMonitor"
Cohesion: 0.07
Nodes (16): ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor, MemoryMonitorOptions (+8 more)

### Community 211 - "fixtures/auth.ts"
Cohesion: 0.08
Nodes (34): clickLogout(), assertCommandChannelReady(), clickWithoutStability(), EnsurePlayableConnectionOptions, executeCommandTrusted(), executeCommandWithoutRecovery(), isPageUsable(), isUsernameLoginVisible() (+26 more)

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

### Community 219 - "test_player_preferences_service.py"
Cohesion: 0.06
Nodes (35): Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences with invalid ID., Test getting player preferences with database error., Test muting a channel successfully., Test checking if channel is muted (returns True)., Test checking if channel is muted (returns False)., Test deleting player preferences with database error. (+27 more)

### Community 220 - "commandStore.ts"
Cohesion: 0.16
Nodes (15): CommandActions, CommandAlias, CommandHistoryEntry, CommandSelectors, CommandState, CommandStore, CommandStoreGet, CommandStoreSet (+7 more)

### Community 221 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+21 more)

### Community 222 - "HolidayService"
Cohesion: 0.02
Nodes (113): _load_and_validate_holidays(), Load and validate holidays., Load and validate schedule files., _validate_schedule_files(), get_asyncpg_server_settings_for_database_url(), Build asyncpg ``server_settings`` so unqualified table names resolve like…, Record the schedule categories currently active for NPC routines., extract_observance_ids() (+105 more)

### Community 223 - "test_spell_effects.py"
Cohesion: 0.05
Nodes (58): mock_player_service(), mock_spell(), mock_target_match(), asyncio, fixture, Unit tests for spell effects. Tests the SpellEffects class., Test process_effect() routes to lucidity adjust handler., Test process_effect() routes to corruption adjust handler. (+50 more)

### Community 224 - "test_game_state_provider.py"
Cohesion: 0.05
Nodes (53): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for game state provider. Tests the GameStateProvider class. (+45 more)

### Community 225 - "CombatMonitoringService"
Cohesion: 0.04
Nodes (34): CombatMonitoringService, Any, Convert to dictionary., Comprehensive combat monitoring and alerting service. Tracks combat system…, Initialize the combat monitoring service., Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier…, Start monitoring a combat turn. Args: combat_id: Unique combat identifier (+26 more)

### Community 226 - "magic_service.py"
Cohesion: 0.03
Nodes (90): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+82 more)

### Community 227 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test get_room_occupants() returns occupants., Test get_room_occupants() returns empty list when no occupants., Test get_room_occupants() handles errors gracefully., Test get_room_subscribers() returns subscribers., test_get_room_occupants() (+5 more)

### Community 228 - "test_chat_service.py"
Cohesion: 0.05
Nodes (56): asyncio, Unit tests for chat service. Tests the ChatService class and ChatMessage class., Test send_say_message() when rate limited., Test send_say_message() when player is not in a room., Test send_local_message() with empty message., Test send_global_message() with empty message., Test send_emote_message() with empty action., Test send_whisper_message() with no target. (+48 more)

### Community 229 - "is_player_in_grace_period"
Cohesion: 0.04
Nodes (73): cancel_grace_period(), is_player_in_grace_period(), Any, UUID, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, Check if a player is currently in grace period. Args: player_id: The player's…, Start a grace period for a disconnected player. During the grace period, the…, start_grace_period() (+65 more)

### Community 230 - "deleteCharacterFlow.ts"
Cohesion: 0.05
Nodes (78): CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), extractErrorMessageFromResponseBody(), fetchCharactersList() (+70 more)

### Community 231 - "WebSocketRequestContext"
Cohesion: 0.08
Nodes (31): Any, Get the event bus from the request context., Creates FastAPI Request-like objects for WebSocket commands. This allows…, Initialize the WebSocket request context. Args: app_state: Real application…, Set the alias storage in the app state. Args: alias_storage: Alias storage…, Set the app state services in the request context. Note: This method is kept…, Get the persistence layer from the request context., WebSocketRequestContext (+23 more)

### Community 232 - "collect_inventory.py"
Cohesion: 0.07
Nodes (44): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+36 more)

### Community 233 - "ChatModeration"
Cohesion: 0.06
Nodes (32): ChatModeration, normalize_player_id(), PlayerServiceProtocol, Any, datetime, Protocol, UUID, Chat moderation utilities. This module provides moderation functionality… (+24 more)

### Community 234 - "resolve_weapon_attack_from_equipped"
Cohesion: 0.08
Nodes (34): Constants supporting item prototype validation. These enumerations anchor the…, Pydantic models for item prototype validation. This module defines the…, Prototype registry for managing item prototypes. This module provides the…, Any, NamedTuple, Weapon resolution helpers for combat. Resolves equipped main-hand items to…, Result of resolving an equipped item to a weapon attack. base_damage: Rolled…, Resolve equipped main-hand stack to weapon attack info, or None if unarmed. (+26 more)

### Community 235 - "EnvironmentalContainerLoader"
Cohesion: 0.17
Nodes (10): EnvironmentalContainerLoader, Any, ContainerComponent, ContainerLockState, UUID, migrate_room_container_to_postgresql., Load all environmental containers for a room from PostgreSQL. Args: room_id:…, Service for loading environmental containers from JSON and PostgreSQL. Handles… (+2 more)

### Community 236 - "rescue_service.py"
Cohesion: 0.16
Nodes (18): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+10 more)

### Community 237 - "chat_service.py"
Cohesion: 0.07
Nodes (36): ChatMessage, Any, UUID, Chat message model for MythosMUD. This module provides the ChatMessage class…, Represents a chat message with metadata., Convert message to dictionary for serialization., Log this chat message to the communications log., clear_player_pose() (+28 more)

### Community 238 - "Async Remediation Complete"
Cohesion: 0.25
Nodes (11): asyncio.to_thread Offloading, Async Audit 2025-12-03, Passive Lucidity Flux Blocking, Async Audit Executive Summary, Three-Phase Async Remediation Plan, Async Remediation Complete, Room Cache 60s TTL, Async Remediation Final Report (+3 more)

### Community 239 - "NPCCombatIntegrationBase"
Cohesion: 0.07
Nodes (25): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Apply combat effects to a target (player or NPC). Args: target_id: ID of the…, Convert target_id to UUID, accepting either string or UUID input., Apply combat effects to a player. (+17 more)

### Community 240 - "communication_commands_flows.py"
Cohesion: 0.11
Nodes (28): _chat_send_with_room_bundle(), _deliver_whisper_message(), flow_local_command(), flow_say_command(), flow_system_command(), flow_whisper_command(), _player_id_bundle(), Room/global/system/whisper/reply flows for communication command handlers.… (+20 more)

### Community 241 - "RoomDataValidator"
Cohesion: 0.06
Nodes (39): Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Check if occupant count matches the actual occupants list length. Args:…, Validates room data structure and content., Check for duplicate occupants in the room. Args: room_data: Room data to check…, Check if room has occupants but no name. Args: room_data: Room data to check…, Validate room data structure and content. Args: room_data: Room data to… (+31 more)

### Community 242 - "apiTypeGuards.ts"
Cohesion: 0.11
Nodes (46): ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertServerCharacterResponseArray(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString() (+38 more)

### Community 243 - "error_handling_middleware.py"
Cohesion: 0.06
Nodes (43): Response, add_error_handling_middleware(), ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Exception, FastAPI, Protocol (+35 more)

### Community 244 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.17
Nodes (17): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+9 more)

### Community 245 - "container_endpoints_basic.py"
Cohesion: 0.05
Nodes (60): _build_container_data_from_dict(), close_container(), _convert_container_dict_to_container_data(), _convert_datetime_to_iso(), _convert_inventory_list_to_inventory_stacks(), _convert_uuid_to_string(), open_container(), Any (+52 more)

### Community 246 - "LogAggregator"
Cohesion: 0.08
Nodes (24): LogAggregator, LogEntry, LogQueryFilter, Any, Path, Add a log entry to the aggregation system., Get filtered log entries., Get log aggregation statistics. Returns: Current log aggregation statistics (+16 more)

### Community 247 - "PlayerNameExtractor"
Cohesion: 0.02
Nodes (86): Utility functions for player event handlers. This module contains helper…, PlayerNameExtractor, Any, UUID, Player name extraction and validation utilities. This module provides utilities…, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:… (+78 more)

### Community 248 - "TestValidatorComponents"
Cohesion: 0.17
Nodes (7): Test path validator integration., Test reporter integration., Test the full validation pipeline., Test individual validator components., Test room loader integration., Test schema validator integration., TestValidatorComponents

### Community 249 - "_fetch_container_items"
Cohesion: 0.06
Nodes (36): _fetch_container_items(), Fetch container items directly from normalized tables. Queries…, Test _fetch_container_items with no items., Test _fetch_container_items with items., Test _fetch_container_items skips rows with missing item_instance_id., Test _fetch_container_items handles non-dictionary rows., Test _fetch_container_items parses string metadata., Test _fetch_container_items handles invalid JSON metadata. (+28 more)

### Community 250 - "useDraggablePanelInteractions.ts"
Cohesion: 0.08
Nodes (42): DraggablePanel(), DraggablePanelProps, isMouseEventOnHeader(), isPanelDragBlockedTarget(), PANEL_DRAG_BLOCK_SELECTORS, relativeSizeToAbsolute(), relativeToAbsolute(), DraggablePanelView() (+34 more)

### Community 251 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 252 - "test_nats_messages.py"
Cohesion: 0.07
Nodes (45): Realtime domain schemas: realtime API, NATS messages, WebSocket messages., BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, Pydantic schemas for NATS message validation. This module provides type-safe…, Validate an event message against the schema. Args: data: Message data… (+37 more)

### Community 253 - "test_command_factories_combat.py"
Cohesion: 0.06
Nodes (29): Unit tests for combat command factories. Tests the CombatCommandFactory class…, Test create_attack_command() creates AttackCommand., Test create_attack_command() allows None target (validation happens later)., Test create_punch_command() creates PunchCommand., Test create_punch_command() allows None target (validation happens later)., Test create_kick_command() creates KickCommand., Test create_kick_command() allows None target (validation happens later)., Test create_strike_command() creates StrikeCommand. (+21 more)

### Community 254 - "test_logout_commands.py"
Cohesion: 0.07
Nodes (38): asyncio, Unit tests for logout commands. Tests the logout and quit command handlers for…, Test _get_player_for_logout retrieves player from persistence when not in cache., Test _get_player_for_logout handles corrupted cache (coroutine instead of…, Test _get_player_for_logout handles persistence errors gracefully., Test _get_player_for_logout handles persistence returning coroutine., Test _update_and_save_player_last_active updates and saves player., Test _update_and_save_player_last_active handles None persistence. (+30 more)

### Community 255 - "test_player_occupant_processor.py"
Cohesion: 0.04
Nodes (59): PlayerOccupantProcessor, Any, UUID, Player occupant processing utilities. This module handles querying and…, Process players and convert to occupant information. Args: room_id: The room ID…, Processes player occupants for rooms., Initialize player occupant processor. Args: connection_manager:…, Ensure a player is included in the player ID strings list if specified. Args:… (+51 more)

### Community 256 - "test_command_helpers_functions.py"
Cohesion: 0.06
Nodes (39): Unit tests for command_helpers utility functions. Tests the utility functions…, Test validate_command_safety() returns True for safe commands., Test validate_command_safety() returns False for shell metacharacters., Test validate_command_safety() returns False for SQL injection attempts., Test validate_command_safety() returns False for Python injection attempts., Test validate_command_safety() returns False for format string injection., Test validate_command_safety() returns False for XSS attempts., Test get_command_help() returns help for specific command. (+31 more)

### Community 257 - "server/exceptions.py"
Cohesion: 0.01
Nodes (514): Composed, get_10_active_invites(), main(), Get 10 active invite codes from the database., F, Shared helper functions for player API endpoints., CreateItemInstanceInput, EnsureItemInstanceInput (+506 more)

### Community 258 - "game_tick_processing.py"
Cohesion: 0.05
Nodes (64): broadcast_tick_event(), cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _create_corpse_lifecycle_service(), game_tick_loop(), get_tick_interval(), _log_cleanup_results(), _process_all_status_effects() (+56 more)

### Community 259 - "GameLogPanel.tsx"
Cohesion: 0.14
Nodes (23): GameLogListMessage, GameLogMessagesList(), GameLogMessagesListProps, GameLogPanelProps, GameLogPanelFilterBar(), GameLogPanelFilterBarProps, GameLogPanelHeader(), GameLogPanelHeaderProps (+15 more)

### Community 260 - "health.ts"
Cohesion: 0.10
Nodes (29): formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, handlePlayerDeliriumRespawned(), handlePlayerDied(), handlePlayerDpUpdated(), handlePlayerEntered() (+21 more)

### Community 261 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 262 - "migration_examples.py"
Cohesion: 0.14
Nodes (12): migration_example_13(), migration_example_5(), migration_example_6(), migration_example_7(), migration_example_8(), migration_example_9(), Example 8: API logging migration., Example 9: WebSocket logging migration. (+4 more)

### Community 263 - "alias_storage.py"
Cohesion: 0.03
Nodes (134): Alias storage utilities for MythosMUD. As noted in the restricted archives of…, handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command., Handle NPC reaction trigger command. (+126 more)

### Community 264 - "RoomMapEditorRuntime.hooks.ts"
Cohesion: 0.11
Nodes (22): edgeTypes, nodeTypes, useMapEditing(), MapEditToolbar(), MapEditToolbarProps, buildModalCreateEdgeHandler(), buildModalPreviewHandler(), buildModalUpdateEdgeHandler() (+14 more)

### Community 265 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test get_adjacent_rooms() handles room with no exits., Test get_adjacent_rooms() handles target room not found., Test validate_room_exists() uses cache., Test validate_room_exists() falls back to persistence., Test get_room_occupants() handles Room object with get_players/get_npcs., Test get_room_occupants() falls back to persistence., Test validate_player_in_room() returns False when room not found. (+17 more)

### Community 266 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 267 - "ChatChannelLoggerMixin"
Cohesion: 0.10
Nodes (19): ChatChannelLoggerMixin, Any, Path, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper…, Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs. (+11 more)

### Community 268 - "executeCommand"
Cohesion: 0.12
Nodes (33): assertNpcSpawnVisible(), hasCombatMessage(), isInCombatStatus(), isInDeathVoid(), isWardBlockingCombat(), keepFirstCultistInstanceId(), resolveSpawnedCultistTarget(), retryUntilCombatStarted() (+25 more)

### Community 269 - ".get_player_aliases"
Cohesion: 0.07
Nodes (18): Any, Path, Save alias data to JSON file., Get all aliases for a player., Save aliases for a player., Add or update an alias for a player., Remove an alias for a player., Get a specific alias for a player. (+10 more)

### Community 270 - "test_communication_commands_flows.py"
Cohesion: 0.09
Nodes (44): flow_global_command(), flow_reply_command(), _global_player_bundle(), _message_from_command(), Handle the `global` command: server-wide chat when permitted., Resolve primary IDs for whisper; return error dict if self-whisper or missing…, Handle `reply`: whisper back to the last player who whispered to you., _room_player_bundle() (+36 more)

### Community 271 - "PlayerPreferencesService"
Cohesion: 0.15
Nodes (17): PlayerPreferencesService, Any, AsyncSession, UUID, Get preferences for a player. Args: session: Database session player_id: The…, Update a player's default channel. Args: session: Database session player_id:…, Mute a channel for a player. Args: session: Database session player_id: The…, Unmute a channel for a player. Args: session: Database session player_id: The… (+9 more)

### Community 272 - "FeatureFlagService"
Cohesion: 0.04
Nodes (47): Initialize the combat configuration service., FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature… (+39 more)

### Community 273 - "MemoryLeakMetricsCollector"
Cohesion: 0.04
Nodes (58): MemoryLeakMetricsCollector, Any, Collect event metrics from EventBus. Returns: Dictionary with event metrics, Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics, Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics, Collect NATS subscription metrics from NATSService. Returns: Dictionary with…, Unified metrics collector for memory leak detection. Aggregates metrics from…, Calculate growth rate for a single metric. Args: current: Current metrics… (+50 more)

### Community 274 - "Alias JSON Schema"
Cohesion: 0.20
Nodes (10): description, items, type, $ref, properties, aliases, version, description (+2 more)

### Community 275 - "AsciiMapRenderer"
Cohesion: 0.03
Nodes (63): AsciiMapRenderer, _ExitRowContext, Any, NamedTuple, ASCII map renderer for MythosMUD. This module provides server-side rendering of…, True if target room has a reverse exit back to from_room_id., Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits… (+55 more)

### Community 276 - "test_room_id_utils.py"
Cohesion: 0.07
Nodes (30): Check if NPC room IDs match target room IDs using fallback comparison. Args:…, Check if NPC room matches target room using normalized comparison. Args:…, Normalize room ID for comparison. Args: rid: Room ID to normalize Returns:…, Check if two normalized room IDs match. Args: id1: First normalized room ID…, Check if normalized NPC room IDs match normalized target room IDs. Args:…, Unit tests for room ID utilities. Tests the RoomIDUtils class for room ID…, Test RoomIDUtils initialization., Test get_canonical_room_id returns canonical ID. (+22 more)

### Community 277 - "test_admin_shutdown_command.py"
Cohesion: 0.09
Nodes (34): calculate_notification_times(), is_shutdown_pending(), Calculate notification times for countdown. Notifications occur: - Every 10…, Check if server shutdown is currently pending. Args: app: FastAPI application…, _AppWithoutState, _PendingCheckAppStub, _PendingCheckStateStub, Unit tests for admin shutdown command handler. Tests the shutdown command… (+26 more)

### Community 278 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 279 - "ExceptionTracker"
Cohesion: 0.08
Nodes (21): ExceptionRecord, ExceptionTracker, Any, Exception, Track an exception with full context information. Args: exception: The…, Get an exception record by ID. Args: exception_id: Unique exception ID Returns:…, Get all exceptions of a specific type. Args: exception_type: Exception type…, Get all exceptions for a specific user. Args: user_id: User ID Returns: List of… (+13 more)

### Community 280 - "Logging Compliance Checker"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 281 - "test_game_tick_processing_async.py"
Cohesion: 0.06
Nodes (50): _process_damage_over_time_effect(), _process_heal_over_time_effect(), _process_single_effect(), _process_single_player_mp_regeneration(), Any, Process a damage over time effect. Returns: True if effect was applied, False…, Process a heal over time effect. Returns: True if effect was applied, False…, Process a single status effect. Returns: Tuple of (updated_effect_dict or None… (+42 more)

### Community 282 - "GameClientV2ContainerView.tsx"
Cohesion: 0.08
Nodes (22): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, MapView(), MapViewBody() (+14 more)

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

### Community 287 - "test_health_service.py"
Cohesion: 0.02
Nodes (145): HealthStatus, ConnectionsComponent, DatabaseComponent, HealthComponents, HealthErrorResponse, HealthResponse, HealthStatus, BaseModel (+137 more)

### Community 288 - "PlayerRoomEventHandler"
Cohesion: 0.14
Nodes (14): PlayerRoomEventHandler, UUID, Subscribe player to room for receiving broadcasts. Args: player_id: The…, Send room name as a message to the Game Info panel. Args: player_id_uuid: The…, Prepare room data for client, removing occupant fields. Args: room: The room…, Send full room update to a player. Args: player_id: The player's ID (UUID or…, Handles room-related player events (entered, left, occupants)., Log occupants snapshot preparation and sending. Args: player_id_uuid: The… (+6 more)

### Community 289 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (49): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id. Args: room_drops: List of…, Unit tests for look item helper functions. Tests the helper functions in…, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items. (+41 more)

### Community 290 - "Any"
Cohesion: 0.13
Nodes (9): Any, Process room update with comprehensive validation. Args: room_data: Room data…, Invalidate stale room cache entry. Args: room_id: Room ID to invalidate…, Fetch fresh room data from room service. Args: room_id: Room ID to fetch…, Handle stale room data by requesting fresh data. Args: room_data: Stale room…, Process room transition with proper ordering and validation. Args:…, Get statistics about the room data cache. Returns: Dict[str, Any]: Cache…, Initialize the room synchronization service. Args: room_service: Optional… (+1 more)

### Community 291 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 292 - "SecurityHeadersMiddleware"
Cohesion: 0.14
Nodes (12): ASGIApp, Receive, Scope, Send, Pure ASGI middleware to add comprehensive security headers to all HTTP…, Initialize security headers middleware. Args: app: ASGI application instance, ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…, SecurityHeadersMiddleware (+4 more)

### Community 293 - "useRespawnHandlers.ts"
Cohesion: 0.16
Nodes (14): fetchSpy, apiErrorDetail(), appendChatError(), appendChatSystem(), applyDeathRespawnSuccess(), applyDeliriumRespawnSuccess(), postRespawn(), runDeathRespawn() (+6 more)

### Community 294 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 295 - "NATSMetrics"
Cohesion: 0.04
Nodes (41): NATSMetrics, Any, NATS metrics collection for MythosMUD. This module provides metrics collection…, NATS-specific metrics collection for monitoring and alerting., Record publish operation metrics., Record subscribe operation metrics., Record batch flush operation metrics., Update connection health score (0-100). (+33 more)

### Community 296 - "test_player_event_handlers.py"
Cohesion: 0.05
Nodes (51): mock_chat_logger(), mock_connection_manager(), mock_message_builder(), mock_name_extractor(), mock_occupant_manager(), mock_room_sync_service(), mock_task_registry(), player_event_handler() (+43 more)

### Community 297 - "go_command.py"
Cohesion: 0.10
Nodes (32): _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement(), handle_go_command(), _movement_combat_and_event_bus_from_go_app(), _movement_service_for_go_command(), Any, Go command for MythosMUD. This module handles the go command for player… (+24 more)

### Community 298 - "ansiToHtml.ts"
Cohesion: 0.06
Nodes (38): SafeHtml(), SafeHtmlProps, ChatMessage(), ChatMessageProps, formatTimestamp(), getFontSizeClass(), getMessageClass(), ChatMessagesList() (+30 more)

### Community 299 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 300 - "MessageFilteringHelper"
Cohesion: 0.08
Nodes (18): MessageFilteringHelper, Any, Extract information from chat event. Args: chat_event: Chat event dictionary…, Determine if mute check should be applied for a channel. Args: channel: Channel…, Compare two room IDs using canonical room ID resolution. Args: player_room_id:…, Get player's current room ID from online players cache. Args: player_id: Player…, Get player's current room ID from async persistence layer. Args: player_id:…, Helper class for message filtering operations. (+10 more)

### Community 301 - "test_command_base.py"
Cohesion: 0.06
Nodes (35): Unit tests for base command models and enums. Tests the Direction and…, Test CommandType enum contains combat commands., Test CommandType enum contains magic commands., Test CommandType enum values can be compared to strings., Test BaseCommand can be instantiated (though it's abstract)., Test BaseCommand rejects unknown fields (extra='forbid')., Test BaseCommand has correct model configuration., Test BaseCommand has __slots__ defined. (+27 more)

### Community 302 - "character-cleanup.ts"
Cohesion: 0.09
Nodes (25): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+17 more)

### Community 303 - "ConnectionManager"
Cohesion: 0.02
Nodes (160): get_async_persistence(), Get the global async persistence instance. DEPRECATED: Use…, PlayerRespawnedEvent, Event fired when a player respawns after death. This event is triggered when a…, ConnectionManager, Manages real-time connections for the game. This refactored version uses…, Check if a WebSocket ID is in the closed set., Mark a WebSocket ID as closed. (+152 more)

### Community 304 - "AI Executor Protocol"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 305 - "PlayerRepositoryProtocol"
Cohesion: 0.09
Nodes (18): PlayerRepositoryProtocol, datetime, Player, Protocol, UUID, Protocol for player persistence operations. Defines the contract used by…, Get the first active player for a user ID., Get all players (including deleted) for a user ID. (+10 more)

### Community 306 - "realtime/conftest.py"
Cohesion: 0.09
Nodes (32): mock_chat_logger(), mock_connection_manager(), mock_logger(), mock_message_builder(), mock_name_extractor(), mock_nats_service(), mock_occupant_manager(), mock_room_sync_service() (+24 more)

### Community 307 - "lifespan.py"
Cohesion: 0.03
Nodes (92): BaseUserManager, ID, Response model for system health check., Response model for system metrics., Response model for system monitoring summary., Response model for system alerts., SystemAlertsResponse, SystemHealthResponse (+84 more)

### Community 308 - "TestCombatMessagingService"
Cohesion: 0.07
Nodes (22): asyncio, fixture, Test get_death_message with custom template., Test get_combat_start_messages generates messages for all occupants., Test get_combat_start_messages with single occupant., Test get_combat_end_messages generates messages for all occupants., Test suite for CombatMessagingService class., Test get_combat_end_messages from winner perspective. (+14 more)

### Community 309 - "Hierarchical Schema Tests"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 310 - "format_metadata"
Cohesion: 0.09
Nodes (31): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+23 more)

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
Nodes (21): Unit tests for alias_graph utilities. Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+13 more)

### Community 318 - "test_spell.py"
Cohesion: 0.03
Nodes (71): Spell registry for managing the global spell database. This module provides an…, List all spells, optionally filtered by school. Args: school: Optional school…, Load all spells from the database into memory. This should be called during…, BaseModel, StrEnum, Spell data models for the magic system. This module contains Pydantic models…, Valid target types for spells., Valid range types for spells. (+63 more)

### Community 319 - "realtime/realtime.py"
Cohesion: 0.18
Nodes (22): ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD. This module defines…, Presence statistics for connection monitoring. This model represents aggregate…, Session statistics for connection monitoring. This model represents aggregate…, Error statistics for connection monitoring. This model represents aggregate…, SessionStatistics (+14 more)

### Community 321 - "test_command_player_state.py"
Cohesion: 0.06
Nodes (47): GroundCommand, LieCommand, LogoutCommand, field_validator, QuitCommand, Player state command models for MythosMUD. This module provides command models…, Command for quitting the game., Command for logging out of the game. (+39 more)

### Community 322 - "_check_grace_period_block"
Cohesion: 0.09
Nodes (25): _check_grace_period_block(), _get_grace_check_context(), UUID, Resolve player_id and connection_manager for grace period check. Returns None…, Check if player is in grace period and block commands. Players in grace period…, mock_request(), asyncio, fixture (+17 more)

### Community 323 - "Result"
Cohesion: 0.22
Nodes (6): database, Simulate database operations., Simulate database query., Simulate database execute., Container for subprocess result data (returncode, stdout, stderr)., Result

### Community 324 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 325 - "AsyncPersistenceLayer"
Cohesion: 0.02
Nodes (117): AsyncPersistenceLayer, Any, datetime, Player, Profession, UUID, Set the instance manager for instanced room lookup (instance-first)., Ensure room cache is loaded (lazy loading with lock). This method uses a lock… (+109 more)

### Community 326 - "PlayerPositionService"
Cohesion: 0.05
Nodes (59): PlayerPositionService, Any, Extract player information for response., Get current position from player stats., Update player position in persistence., Mutate persistence and in-memory tracking to reflect the requested position., Mirror posture changes into the live connection manager., Coordinate player posture transitions with persistence and live presence… (+51 more)

### Community 327 - "WearableContainerService"
Cohesion: 0.11
Nodes (24): _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Return existing equipment container ID for item instance if present., Create wearable container in persistence and return container_id payload., Handle equipping a wearable container item. Creates a container in PostgreSQL… (+16 more)

### Community 328 - "RoomService"
Cohesion: 0.03
Nodes (71): MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter…, _append_room_with_fallback_coords_if_needed(), _apply_minimap_fallback_coordinates(), _ensure_current_room_in_minimap_rooms(), generate_minimap_html(), Any (+63 more)

### Community 329 - "TestNPCCombatRewards"
Cohesion: 0.08
Nodes (20): asyncio, fixture, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class., Test award_xp_to_killer handles zero XP. (+12 more)

### Community 330 - "send_game_event"
Cohesion: 0.06
Nodes (48): MagicServiceHealingMixin, Any, UUID, Healing event notification for spellcasting. Mixin that sends player_dp_updated…, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or… (+40 more)

### Community 331 - "Container Looting Scenarios"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 332 - "websocket_handler_commands.py"
Cohesion: 0.02
Nodes (144): create_websocket_request_context(), Factory function to create a WebSocket request context. Args: app_state: Real…, _mirror_service_to_app_state(), Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state. Mutates…, resolve_and_setup_app_state_services(), _services_from_container() (+136 more)

### Community 333 - "StyleGuideSections.tsx"
Cohesion: 0.06
Nodes (46): ChannelSelectorSectionProps, Channel, ChannelSelector(), ChannelSelectorProps, useChannelSelectorState(), AllStats(), CommandsCount(), ConnectionStatus() (+38 more)

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
Cohesion: 0.07
Nodes (28): FakeHallucinationService, Any, UUID, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Select which type of fake hallucination to trigger (50/50 chance). Returns:…, Service for generating fake NPC tells and room text overlays. These…, Initialize the fake hallucination service., Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will… (+20 more)

### Community 342 - "WebSocket Handler Tests"
Cohesion: 0.09
Nodes (31): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test validating message with path traversal pattern., Test validating message with javascript: URL., Test validating message with event handler. (+23 more)

### Community 343 - "test_message_handler_factory.py"
Cohesion: 0.07
Nodes (42): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, MessageHandlerFactory, PingMessageHandler, Initialize the factory with registered handlers., Get a list of supported message types. Returns: List of supported message type…, Handler for command messages. (+34 more)

### Community 344 - "generate_sql.mjs"
Cohesion: 0.25
Nodes (8): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Static Data SQL Generation, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 345 - "player_effect_repository.py"
Cohesion: 0.06
Nodes (53): PlayerEffect, Base, Persistent player effect (status effect) with tick-based duration. Table:…, _add_effect_params(), AddEffectInput, _int_opt(), _opt_str(), PlayerEffectRepository (+45 more)

### Community 346 - "roomHandlers.ts"
Cohesion: 0.09
Nodes (37): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+29 more)

### Community 347 - "Enhanced Logging Migration Complete"
Cohesion: 0.67
Nodes (3): Enhanced Logging Implementation Complete, Enhanced Logging Implementation Summary, Enhanced Logging Migration Complete

### Community 350 - "gameStore.ts"
Cohesion: 0.05
Nodes (45): GameTerminalContainer(), GameTerminalPresentation(), GameTerminalPresentationProps, ChatPanel(), GameLogPanel(), Channel, ChannelSelectorProps, TerminalButtonProps (+37 more)

### Community 351 - "combat_attack.py"
Cohesion: 0.08
Nodes (39): _execute_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution. Extracted from combat.py to…, Resolve damage from equipped weapon or fall back to config unarmed damage., Execute combat action using the proper combat service., Handle attack commands (attack, punch, kick, etc.)., Validate target name, load player/room, check DP and no_combat. Returns… (+31 more)

### Community 352 - "appLazyScreens.tsx"
Cohesion: 0.09
Nodes (23): MotdContent(), MOTD_BUTTON_STYLE, MotdInterstitialScreen(), MotdInterstitialScreenProps, AppCreationFlowViews(), creationShell(), renderNameStep(), renderProfessionStep() (+15 more)

### Community 353 - "test_magic_commands.py"
Cohesion: 0.03
Nodes (101): MagicCommandHandler, Any, Resolve player and spell parameters for a cast; returns error message if…, Build the response payload for a cast result and send announcements., Build the final success message for a cast spell., If player is resting, cancel rest countdown so they can cast. Swallows errors…, Handle /spells command - list learned spells. Args: command_data: Command data…, Handle /spell command - show spell details. (+93 more)

### Community 354 - "container_persistence/container_persistence.py"
Cohesion: 0.14
Nodes (26): ContainerData, create_container(), delete_container(), get_container(), get_containers_by_entity_id(), get_containers_by_room_id(), Any, datetime (+18 more)

### Community 355 - "Test Coverage Gaps"
Cohesion: 0.67
Nodes (3): Disconnect Grace Period Rest Coverage, Test Coverage Gaps, Coverage Gap Priority Matrix

### Community 356 - "MovementMonitor"
Cohesion: 0.11
Nodes (15): MovementMonitor, Any, UUID, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms., Get comprehensive movement metrics., Get current alerts based on thresholds. (+7 more)

### Community 357 - "process_command_with_validation"
Cohesion: 0.08
Nodes (30): handle_expanded_command(), Any, CommandExecutionRequest, Handle command processing with alias expansion and loop detection. This…, _dispatch_parsed_command(), _handle_processing_error(), _handle_validation_error(), _log_security_sensitive_command() (+22 more)

### Community 358 - "test_event_publisher.py"
Cohesion: 0.07
Nodes (35): event_publisher(), mock_nats_service(), mock_subject_manager(), asyncio, fixture, Unit tests for event publisher. Tests the EventPublisher class., Test publish_game_tick_event() when NATS is not connected., Test get_next_sequence_number() returns and increments sequence. (+27 more)

### Community 359 - "useMythosAppActions.ts"
Cohesion: 0.07
Nodes (50): authSliceReducer(), creationSliceReducer(), INITIAL_AUTH_SLICE, INITIAL_CREATION_SLICE, PendingSkillsPayload, resolveNextState(), useAuthSliceSetters(), useCreationSliceSetters() (+42 more)

### Community 360 - "RoomCacheLoader"
Cohesion: 0.20
Nodes (5): Any, BaseException, Loads room data from the database and populates a room cache dict. Used by…, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 361 - "admin_setlucidity_command.py"
Cohesion: 0.13
Nodes (28): _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), _get_current_lcd(), _get_player_service_from_app(), _log_lucidity_success() (+20 more)

### Community 362 - "rate_overrides.py"
Cohesion: 0.12
Nodes (23): _async_load_lucidity_rate_overrides(), build_override_key(), extract_lucidity_rate(), load_lucidity_rate_overrides(), _LucidityRateLoadResult, _normalize_database_url(), _parse_special_rules_from_raw(), _parse_zone_stable_id() (+15 more)

### Community 363 - "Profession"
Cohesion: 0.07
Nodes (40): CharacterNameScreenProps, MechanicalEffect, Profession, ProfessionCard(), ProfessionCardProps, StatRequirement, ProfessionSelectionContentProps, ProfessionSelectionScreen() (+32 more)

### Community 364 - "Three-Column Game UI Layout"
Cohesion: 0.29
Nodes (7): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe

### Community 365 - "worktree-ops.py"
Cohesion: 0.22
Nodes (17): get_current_worktree(), get_project_root(), install_dependencies(), main(), Run linting (worktree-aware), Determine the project root based on current working directory, Run formatting (worktree-aware), Show worktree and project status (+9 more)

### Community 366 - "e2e-bootstrap.ts"
Cohesion: 0.15
Nodes (27): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+19 more)

### Community 367 - "test_invite_schemas.py"
Cohesion: 0.09
Nodes (29): InviteBase, InviteCreate, InviteRead, InviteUpdate, Base invite schema with common fields., Schema for creating a new invite., Schema for reading invite data., Schema for updating invite data. (+21 more)

### Community 368 - "MonitoringPanel.tsx"
Cohesion: 0.12
Nodes (23): ConnectionHealthStats(), DualConnectionStats(), formatNumber(), formatPercentage(), formatTime(), loadMonitoringSnapshot(), MonitoringData, MonitoringPanel() (+15 more)

### Community 369 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 370 - "test_message_broadcaster.py"
Cohesion: 0.08
Nodes (31): message_broadcaster(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for message broadcaster. Tests the MessageBroadcaster class., Test broadcast_global() excludes specified player., Test broadcast_global() when no players online. (+23 more)

### Community 371 - "test_postgres_adapter.py"
Cohesion: 0.14
Nodes (12): connect_postgres(), convert_sqlite_to_postgres_query(), Create a PostgreSQL connection. Args: database_url: PostgreSQL connection URL…, Convert legacy SQLite query syntax to PostgreSQL syntax. Note: This function is…, Unit tests for PostgreSQL adapter. Tests PostgresRow, PostgresConnection,…, Test utility functions., Test connect_postgres()., Test connect_postgres() with driver prefix. (+4 more)

### Community 372 - "_MagicServiceCore"
Cohesion: 0.08
Nodes (29): _MagicServiceCore, Any, UUID, Return (False, message) if not enough MP, else (True, '')., Return (False, message) if Mythos spell and not enough lucidity, else (True,…, Return (False, message) if player has not learned the spell, else (True, '')., Return (False, message) if spell requires materials and any are missing, else…, Check if a player can cast a spell. Args: player_id: Player ID spell: Spell to… (+21 more)

### Community 373 - "AuditLogger"
Cohesion: 0.07
Nodes (30): Unit tests for audit_logger utilities. Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries., test_audit_logger_get_recent_entries(), test_audit_logger_init() (+22 more)

### Community 374 - "command_handler_unified.py"
Cohesion: 0.06
Nodes (50): check_alias_safety(), Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:…, validate_expanded_command(), command_request_app_state(), CommandExecutionRequest, Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…, _check_all_command_blocks() (+42 more)

### Community 375 - "test_quest_definition_repository.py"
Cohesion: 0.11
Nodes (29): _make_session_context(), mock_quest_definition(), asyncio, fixture, quest_definition_repository(), Unit tests for QuestDefinitionRepository. Tests get_by_id, get_by_name, and…, Test get_by_id raises DatabaseError on DB failure., Test get_by_name returns definition when found by common name. (+21 more)

### Community 376 - "test_movement_monitor.py"
Cohesion: 0.04
Nodes (56): movement_monitor(), fixture, Unit tests for movement monitor. Tests the MovementMonitor class for monitoring…, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data., Test validate_room_integrity() detects duplicate players., Test validate_room_integrity() handles empty rooms dict. (+48 more)

### Community 377 - "bundles/game.py"
Cohesion: 0.05
Nodes (60): _check_holiday_coverage(), _get_calendar_paths(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message(), Namespace (+52 more)

### Community 378 - "shutdown_sequence.py"
Cohesion: 0.17
Nodes (20): Schedule a best-effort graceful process termination after a short delay. This…, schedule_process_termination(), _cancel_background_tasks(), _cleanup_connection_manager(), _despawn_all_npcs(), _disconnect_all_players(), _disconnect_nats_service(), execute_shutdown_sequence() (+12 more)

### Community 379 - "useRoomEditModal.ts"
Cohesion: 0.09
Nodes (14): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, RoomEditFormData, RoomEditModalForm(), RoomEditModalFormProps, RoomEditModalTabs() (+6 more)

### Community 380 - "subject_controller.py"
Cohesion: 0.10
Nodes (30): get_patterns(), get_subject_manager_dependency(), get_subject_statistics(), PatternsResponse, BaseModel, get, post, NATS Subject Management API Controller for MythosMUD. This module provides REST… (+22 more)

### Community 381 - "NATS Subject Manager Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 382 - "handle_whisper_command"
Cohesion: 0.07
Nodes (48): handle_whisper_command(), asyncio, Unit tests for whisper and reply communication command handlers., Test handle_whisper_command successful execution., Test handle_reply_command with no message., Test handle_reply_command when services are not available., Test handle_reply_command when no last whisper sender., Test handle_whisper_command with no target. (+40 more)

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
Cohesion: 0.11
Nodes (38): _ensure_connection_manager(), _extract_bearer_token(), get_connection_statistics(), get_player_connections(), handle_new_game_session(), _parse_subprotocol_token(), _parse_websocket_token(), Any (+30 more)

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
Nodes (41): autoprefixer, devDependencies, autoprefixer, cross-env, eslint-plugin-playwright, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals (+33 more)

### Community 391 - "TestCombatConfigurationService"
Cohesion: 0.05
Nodes (23): fixture, Test suite for CombatConfigurationService class., Create a mock config object., Create a CombatConfigurationService instance for testing., Test CombatConfigurationService initialization., Test get_combat_configuration returns configuration., Test get_combat_configuration caches configuration., Test get_combat_configuration_for_scope with global scope. (+15 more)

### Community 392 - "test_communication_commands_support.py"
Cohesion: 0.09
Nodes (36): _deliver_reply_to_last_whisper(), app_from_request(), AsyncPersistenceForPose, chat_result_map(), get_pose_persistence(), get_services_from_container(), message_id_from_result(), PlayerWithPose (+28 more)

### Community 393 - "test_quest_service_collect.py"
Cohesion: 0.13
Nodes (27): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in… (+19 more)

### Community 394 - "retry.py"
Cohesion: 0.08
Nodes (33): asyncio, Unit tests for retry utilities. Tests the retry decorator and retry logic., Test is_transient_error() identifies transient errors., Test is_transient_error() returns False for non-transient errors., Test retry_with_backoff() succeeds on first attempt., Test retry_with_backoff() retries on failure then succeeds., Test retry_with_backoff() with async function succeeds on first attempt., Test retry_with_backoff() with async function retries on failure then succeeds. (+25 more)

### Community 395 - "TaskRegistry"
Cohesion: 0.05
Nodes (35): HolidayResolver, Any, Task, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task…, Cancel specific task with logical timeout boundaries. Args: task: Task… (+27 more)

### Community 396 - "test_health_monitor.py"
Cohesion: 0.09
Nodes (29): health_monitor(), mock_cleanup_dead_websocket(), mock_is_websocket_open(), mock_performance_tracker(), mock_validate_token(), asyncio, fixture, Unit tests for health monitor. Tests the HealthMonitor class. (+21 more)

### Community 397 - "TestNPCCombatLifecycle"
Cohesion: 0.12
Nodes (13): asyncio, fixture, Test _despawn_npc handles NPC not in active_npcs., Test suite for NPCCombatLifecycle class., Create a mock persistence layer., Create a NPCCombatLifecycle instance for testing., Test NPCCombatLifecycle initialization., Test despawn_npc_safely successfully despawns NPC. (+5 more)

### Community 398 - "inventory_pickup_command.py"
Cohesion: 0.08
Nodes (48): _FloorPickupResolved, Parse numeric fields from object-typed JSON command payloads., Protocol, Shared types for inventory command handlers (Lizard: keep main module small)., Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, add_pickup_to_inventory(), prepare_extracted_stack() (+40 more)

### Community 399 - "Emote Schema Definition"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 401 - "CommandPanel.tsx"
Cohesion: 0.06
Nodes (28): CommandPanel(), CommandPanelProps, logCommandPanelConnectionDebug(), prepareCommandForSubmit(), prependChannelShortcut(), prependPartyPrefix(), STANDALONE_COMMANDS, useCommandPanelEffects() (+20 more)

### Community 402 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 404 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 405 - "test_room_occupant_manager.py"
Cohesion: 0.09
Nodes (29): mock_connection_manager(), occupant_manager(), asyncio, fixture, Unit tests for room occupant manager. Tests the RoomOccupantManager class for…, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test get_room_occupants handles get_players error. (+21 more)

### Community 406 - "LRUCache"
Cohesion: 0.04
Nodes (47): cached(), CacheService, Cache service for MythosMUD server. This module provides caching services that…, Decorator to cache function results. Args: cache_name: Name of the cache to use…, Main cache service that coordinates all caching operations. This service…, Initialize the cache service. Args: persistence: Persistence layer instance…, Preload frequently accessed data into caches. This method loads commonly used…, Caching module for MythosMUD server. This module provides comprehensive caching… (+39 more)

### Community 407 - "ValidationRule"
Cohesion: 0.06
Nodes (24): Path, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a sub-zone configuration against its schema. Args: config_data: Sub-…, Validate a zone configuration against its schema. Args: config_data: Zone…, Initialize the schema validator. Args: schema_path: Path to the JSON schema file, Load and cache the JSON schema., Validate a single room against the schema. Args: room_data: Room data to… (+16 more)

### Community 408 - "asyncio"
Cohesion: 0.05
Nodes (37): asyncio, Test creating player preferences with string UUID., Test creating player preferences when they already exist., Test getting player preferences successfully., Test updating default channel successfully., Test updating default channel with invalid channel name., Test muting system channel (should fail)., Test unmuting a channel successfully. (+29 more)

### Community 409 - "ValidationError"
Cohesion: 0.02
Nodes (117): create_validator(), Any, Path, Shared schema validator for room definition files. This module provides JSON…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a serialized alias bundle against the alias schema. Args: alias_data:…, Validate emote definition data against the emote schema. Args: emote_data:… (+109 more)

### Community 410 - "stateNormalization.ts"
Cohesion: 0.07
Nodes (37): ConnectionActions, ConnectionHealth, ConnectionMetadata, ConnectionSelectors, ConnectionState, ConnectionStore, createInitialState(), GameEvent (+29 more)

### Community 412 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 413 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 414 - "ZoneConfiguration"
Cohesion: 0.05
Nodes (53): Represents the configuration for a zone or sub-zone., Calculate effective spawn probability based on zone modifiers. Args:…, Check if a player can access this zone based on requirements. Args:…, ZoneConfiguration, Test get_zone_configuration() returns exact match., Test get_zone_configuration() falls back to zone-level config., Test get_zone_configuration() handles zone key without slash., Test _check_spawn_requirements_for_room() checks NPC definitions. (+45 more)

### Community 415 - "_str_id"
Cohesion: 0.13
Nodes (15): UUID, Create a new party with the given player as leader. Returns dict with success…, Add a player to a party. Fails if party does not exist or player is already in…, Remove expired pending invites and notify inviters., Send a command_response-style message to a single player., Create a pending party invite and send party_invite event to target. Target…, Normalize ID to string for dict keys and membership sets., Accept a party invite. Target is the player who accepted (the invitee). (+7 more)

### Community 416 - "NATSConnectionStateMachine"
Cohesion: 0.03
Nodes (90): ConnectionEvent, NATSConnectionStateMachine, Enum, Connection state machine for NATS messaging. Implements a robust state machine…, Initialize connection state machine. Args: connection_id: Unique identifier for…, Handler for connect transition. Resets reconnection counter and prepares for…, Handler for successful connection. Records connection time and increments…, Handler for disconnection. Increments disconnection counter. AI: Track… (+82 more)

### Community 417 - "LucidityRepository"
Cohesion: 0.10
Nodes (17): Delete an item from the cache. Args: key: The key to delete Returns: True if…, Get the number of rows affected., LucidityRepository, AsyncSession, datetime, UUID, Set or update cooldown for a player and action., Delete all cooldowns for a player matching an action code pattern. (+9 more)

### Community 418 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 419 - "teach_command.py"
Cohesion: 0.21
Nodes (15): _format_teach_result(), _get_teach_services(), handle_teach_command(), Any, Teach command handler for learning spells from NPC teachers. This module…, Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, _resolve_npc_teacher(), asyncio (+7 more)

### Community 420 - "format_player_entry"
Cohesion: 0.09
Nodes (23): format_player_entry(), Format a single player entry for the who command output. Args: player: Player…, Unit tests for who command helper functions. Tests the helper functions in…, Test filter_players_by_name() filters players by name., Test filter_players_by_name() returns empty list when no matches., Test filter_players_by_name() returns all players when filter is empty., Test format_player_location() formats valid room ID., Test format_player_entry() formats player entry. (+15 more)

### Community 421 - "api/player_respawn.py"
Cohesion: 0.13
Nodes (28): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Any, post, Request, ValidationError, Player respawn API endpoints. This module handles endpoints for respawning…, Respawn a delirious player at the Sanitarium with restored lucidity. This… (+20 more)

### Community 422 - "Advanced Chat Channels Specification"
Cohesion: 0.40
Nodes (5): Advanced Chat Channels Specification, Global Chat Channel, Local Chat Channel, Advanced Chat Channels Tasks, Whisper Chat Channel

### Community 423 - "test_chat_logger.py"
Cohesion: 0.08
Nodes (25): Unit tests for chat logger service. Tests the ChatLogger class for structured…, Test log_player_muted writes entry., Test log_player_unmuted writes entry., Test log_player_joined_room writes entry., Test log_rate_limit_violation writes entry., Test get_log_file_paths returns correct paths., Test get_log_stats returns statistics., Test log_whisper_channel_message writes entry. (+17 more)

### Community 424 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 425 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 426 - "testing_examples.py"
Cohesion: 0.14
Nodes (13): Test that sensitive data is properly sanitized in logs., Test database operation logging., Test logging correlation IDs., Test error logging functionality., Test performance logging functionality., Test API request logging in integration tests., request, test_api_request_logging() (+5 more)

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

### Community 433 - "InventorySchemaValidationError"
Cohesion: 0.12
Nodes (25): Shared schemas: base models, target resolution, inventory validation., _build_validator(), InventorySchemaValidationError, Any, Exception, Inventory JSON schema validation utilities. As recorded in the restricted…, Internal helper to construct a Draft7 validator instance., Validate a complete inventory payload against the canonical schema. Raises:… (+17 more)

### Community 434 - "CommandService"
Cohesion: 0.11
Nodes (16): CommandHandler, CommandService, Any, Main command processing service for MythosMUD. This service handles command…, Process a validated command with routing. Args: command_data: The validated…, Parse and validate command string. Returns: tuple of (parsed_command, cmd,…, Prepare command_data dictionary by merging parsed command fields. Returns:…, Extract non-private, non-callable attributes from parsed_command, excluding… (+8 more)

### Community 435 - "ConnectionCleaner"
Cohesion: 0.15
Nodes (12): ConnectionCleaner, Any, Extract player_id from connection metadata if present., Close stale WebSocket and remove from tracking. Handles None websocket…, Return set of online player IDs as strings (room._players uses string UUIDs)., Return players in room but not online. Empty if room has no get_players., Filter to players with zero WebSocket connections (or invalid UUIDs)., Remove ghost players from room and log. (+4 more)

### Community 436 - "projectorRoom.ts"
Cohesion: 0.09
Nodes (46): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), messageHandlers, ProjectorHandler, stateHandlers, appendMessage() (+38 more)

### Community 437 - "security.ts"
Cohesion: 0.04
Nodes (56): AppRouter(), MapPage, SkillsPage, RoomMapViewerProps, SetState, MapPage(), AuthenticatedMapProps, MapViewResolvedProps (+48 more)

### Community 438 - "generate_html_visualization.py"
Cohesion: 0.13
Nodes (22): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+14 more)

### Community 439 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 440 - "logout_commands.py"
Cohesion: 0.13
Nodes (26): _disconnect_player_connections(), _force_disconnect_player(), _get_app_services(), _get_player_for_logout(), handle_logout_command(), handle_quit_command(), _mark_quit_intentional(), _prepare_player_for_logout() (+18 more)

### Community 441 - "channel_broadcasting_strategies.py"
Cohesion: 0.19
Nodes (12): ChannelBroadcastingStrategy, GlobalChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for whisper channel broadcasting., Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy. Args: channel_type: Type of…, Abstract base class for channel broadcasting strategies. (+4 more)

### Community 442 - "Migration 019 Ready for Deployment"
Cohesion: 0.67
Nodes (3): Migration 019 Complete Summary, Migration 019 Ready for Deployment, Migration 019 Testing Guide

### Community 443 - "PlayerService"
Cohesion: 0.02
Nodes (191): create_player(), delete_character(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), _force_disconnect_character(), get_available_classes(), get_class_description() (+183 more)

### Community 444 - "test_flee_command.py"
Cohesion: 0.10
Nodes (36): flee_handler_deps(), _FleeCmdApp, _FleeCmdAppState, _FleeCmdRequest, FleeHandlerDeps, _GetCombatHandlerLoaderApp, _GetCombatHandlerLoaderAppState, _GetCombatHandlerLoaderContainer (+28 more)

### Community 445 - "factory.py"
Cohesion: 0.05
Nodes (49): main(), Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., _sanitize_token_examples(), Admin API module for MythosMUD. This module provides administrative API…, Container API endpoints for unified container system. As documented in the…, API module for MythosMUD. This module provides REST API endpoints for the…, get_all_professions() (+41 more)

### Community 447 - "asyncio"
Cohesion: 0.05
Nodes (37): asyncio, Test is_player_muted_async() returns True when player is muted., Test is_player_muted_async() returns False when player is not muted., Test add_admin() handles missing container., Test add_admin() handles missing persistence., Test add_admin() handles player not found., Test remove_admin() handles missing container., Test remove_admin() handles missing persistence. (+29 more)

### Community 448 - "test_combat_flee_handler.py"
Cohesion: 0.13
Nodes (26): execute_voluntary_flee(), _handle_failed_voluntary_flee(), Any, UUID, Execute voluntary flee for a combat participant (shared by /flee command and…, Roll for voluntary flee success (no side effects). Formula: base + (bonus *…, try_voluntary_flee_roll(), _make_participant() (+18 more)

### Community 449 - "websocket_handler.py"
Cohesion: 0.05
Nodes (61): get_message_validator(), Get the global message validator instance., handle_json_decode_error(), handle_message_loop_exception(), handle_websocket_disconnect(), handle_websocket_generic_exception(), handle_websocket_message_loop(), handle_websocket_runtime_error() (+53 more)

### Community 450 - "SkillAssignmentScreen.tsx"
Cohesion: 0.15
Nodes (24): buildCreateCharacterPayload(), CharacterNameScreen(), CreateCharacterPayload, getCreateCharacterErrorMessage(), OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, loadSkillsCatalog() (+16 more)

### Community 451 - "test_logout_commands_helpers.py"
Cohesion: 0.09
Nodes (25): _get_player_position_from_connection_manager(), Get player's current position from connection manager. Args:…, Unit tests for logout_commands helper functions. Tests helper functions in…, Test _sync_player_position() does nothing when position is None., Test _sync_player_position() does nothing when position matches., Test _get_player_position_from_connection_manager() returns position., Test _get_player_position_from_connection_manager() finds by display name., Test _get_player_position_from_connection_manager() returns None when no… (+17 more)

### Community 452 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 453 - "ApplicationContainer"
Cohesion: 0.02
Nodes (138): Audit and reclaim orphaned task candidates across the system. Returns: Number…, Proactively clean up orphaned tasks by cancelling leak prevention violations.…, Return count of currently tracked task references within the manager's…, Central namespace for tracked task lifecycle coordination preventing orphaned…, TrackedTaskManager, ChatBundle, Chat bundle: chat service. Depends on Core (config, persistence), Game…, Initialize chat service. (+130 more)

### Community 454 - "Process Scope NATS Scripts"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 455 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 456 - "canonical_room_id_impl"
Cohesion: 0.08
Nodes (24): Resolve a room id to the canonical Room.id value (public method)., Resolve a room id to the canonical Room.id value (compatibility method)., Remove a player from all room subscriptions and occupant lists (compatibility…, canonical_room_id_impl(), prune_player_from_all_rooms_impl(), Any, Resolve a room id to the canonical Room.id value. Args: room_id: The room ID to…, Remove a player from all room subscriptions and occupant lists. (+16 more)

### Community 457 - "zone_config_loader.py"
Cohesion: 0.13
Nodes (22): parse_zone_special_rules(), process_subzone_rows(), process_zone_rows(), Connection, Record, TypedDict, Zone Configuration Loader Module. This module handles loading zone and sub-zone…, Build and store one subzone configuration from a database row. (+14 more)

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

### Community 462 - "useRoomMapData.ts"
Cohesion: 0.13
Nodes (13): fetchSpy, buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), UseRoomMapDataOptions, UseRoomMapDataResult, RoomDetailsPanel() (+5 more)

### Community 463 - "RoomInfoPanel.tsx"
Cohesion: 0.13
Nodes (16): applyRoomDefaultFields(), DEV_FALLBACK_ROOM, fixOccupantCountMismatch(), formatDescription(), formatExitDirections(), formatLocationName(), KNOWN_LOCATION_PATTERNS, logRoomInfoRenderDebug() (+8 more)

### Community 464 - "CombatMessagingService"
Cohesion: 0.11
Nodes (14): CombatMessages, CombatMessagingBase, Base class with connection manager setup. Used by CombatMessagingIntegration., CombatMessagingService, Any, Generate combat start messages for all room occupants. Args: attacker_name:…, Generate combat end messages for all room occupants. Args: winner_name: Name of…, Generate thematic error messages for combat actions. Args: error_type: Type of… (+6 more)

### Community 465 - "._cleanup_player_mutes"
Cohesion: 0.12
Nodes (11): datetime, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired player mutes., Clean up expired channel mutes., Clean up expired global mutes., Clean up expired mutes from all storage. (+3 more)

### Community 466 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from…, Unit tests for connection utils. Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 467 - "_process_session_dp_decay_and_death"
Cohesion: 0.14
Nodes (19): _handle_player_death_threshold(), _player_in_active_combat(), _process_dead_players(), _process_mortally_wounded_player(), _process_mortally_wounded_players(), _process_mp_regeneration(), _process_passive_lucidity_flux(), _process_session_dp_decay_and_death() (+11 more)

### Community 468 - "Room"
Cohesion: 0.05
Nodes (59): GameTerminalProps, IncapacitatedBanner, IncapacitatedBannerProps, HallucinationTicker, HallucinationTickerProps, severityClass, computeLucidityBar(), formatChange() (+51 more)

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
Cohesion: 0.05
Nodes (64): NATSRetryHandler, Any, Exception, Calculate exponential backoff delay with jitter. Args: attempt: Current attempt…, Determine if a message should be retried. Args: message: Message that failed…, Retry a function with exponential backoff. Args: func: Async function to retry…, Get retry statistics. Returns: Dictionary with retry metrics AI: For monitoring…, Retry async function with exponential backoff. Attempts the function up to… (+56 more)

### Community 473 - "Logout Error Scenarios"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 474 - "Any"
Cohesion: 0.12
Nodes (12): Any, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:…, Get lifecycle manager for filtering fallback NPCs. Returns: Lifecycle manager…, Check if a single fallback NPC should be included. Args: npc_id: The NPC ID to…, Filter fallback NPCs to only include those in active_npcs and alive. Args:…, Get and validate NPC lifecycle manager. Args: room_id: The room ID for logging… (+4 more)

### Community 475 - "CacheManager"
Cohesion: 0.11
Nodes (11): CacheManager, Any, Get cache statistics. Returns: Dictionary containing cache statistics, String representation of the cache., Centralized cache manager for MythosMUD server. Manages multiple LRU caches for…, Initialize the cache manager., Initialize default caches with appropriate configurations., Get a cache by name. Args: name: The name of the cache Returns: The cache… (+3 more)

### Community 476 - "container_helpers_inventory_display.py"
Cohesion: 0.18
Nodes (15): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+7 more)

### Community 477 - "mock_container"
Cohesion: 0.11
Nodes (25): mock_connection_manager(), mock_container(), fixture, Create mock connection manager., Create mock container., _assign_container_get_instance(), Test _determine_spawn_room() uses NPC's room_id when available., Test _determine_spawn_room() uses sub_zone default when room_id not available. (+17 more)

### Community 478 - "static_data/package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 479 - "ActiveLucidityService"
Cohesion: 0.16
Nodes (14): ActiveLucidityService, AsyncSession, datetime, Handle active lucidity adjustments such as encounters and recovery actions., _EncounterCtx, Any, NamedTuple, Apply lucidity loss when a player engages an eldritch entity. Args: player_id:… (+6 more)

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
Nodes (19): minimum, type, additionalProperties, type, maxLength, minLength, type, properties (+11 more)

### Community 486 - "EdgeDetailsPanel.tsx"
Cohesion: 0.11
Nodes (15): buildEdgeFieldModel(), EdgeAdminActionsProps, EdgeDeleteConfirmProps, EdgeDetailRow(), EdgeDetailRowProps, EdgeDetailsFields(), EdgeDetailsFieldsProps, EdgeDetailsPanel() (+7 more)

### Community 487 - "E2E Multiplayer Findings"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 488 - "GameTerminalContext.test.tsx"
Cohesion: 0.16
Nodes (17): GameTerminalContext, GameTerminalContextType, GameTerminalProvider(), GameTerminalProviderProps, useConnectionState(), useGameActions(), useGameState(), useGameTerminalContext() (+9 more)

### Community 489 - "parse_last_active_datetime"
Cohesion: 0.10
Nodes (20): parse_last_active_datetime(), Parse last_active from string or datetime object to timezone-aware datetime.…, Test parse_last_active_datetime with None., Test parse_last_active_datetime with empty string., Test parse_last_active_datetime with string ending in Z., Test parse_last_active_datetime with string containing timezone., Test parse_last_active_datetime with string without timezone., Test parse_last_active_datetime with naive datetime. (+12 more)

### Community 490 - "PostgresConnection"
Cohesion: 0.08
Nodes (18): PostgresConnection, connection, Commit the current transaction., Rollback the current transaction., Close the connection., PostgreSQL connection wrapper for persistence layer operations., Test PostgresConnection initialization., Test PostgresConnection.execute(). (+10 more)

### Community 491 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, type, minLength, type, minLength, type, properties (+10 more)

### Community 492 - "inventory_command_helpers.py"
Cohesion: 0.09
Nodes (34): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any, Administrative summon command implementation. (+26 more)

### Community 493 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 494 - "Alertmanager Monitoring Stack"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 495 - "handle_emote_command"
Cohesion: 0.14
Nodes (22): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+14 more)

### Community 496 - "test_who_commands.py"
Cohesion: 0.10
Nodes (19): Unit tests for who commands., Test filtering players with no filter term., Test format_who_result with no players., Test format_who_result with no players and filter term., Test format_who_result with players., Test get_players_for_who without filter., Test get_players_for_who with filter., Test filtering players with exact match. (+11 more)

### Community 497 - "MessageBroadcaster"
Cohesion: 0.10
Nodes (22): SendPersonalMessage, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Convert string player IDs to UUIDs for message sending. Args: target_list: List…, Process results from batch message delivery. Args: delivery_results: Results…, Fallback to individual message sending if batch fails. Args: target_mapping:… (+14 more)

### Community 498 - "World Seed Loader"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 499 - "edgeModalLogic.ts"
Cohesion: 0.09
Nodes (30): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+22 more)

### Community 500 - "React Node Upgrade Analyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 501 - "NPCEventHandler"
Cohesion: 0.05
Nodes (43): NPCEventHandler, Any, Extract spawn_message from behavior_config. Args: behavior_config: The parsed…, Get the spawn message for an NPC from its behavior_config. If no custom spawn…, Get the name of an NPC by ID. Args: npc_id: The NPC ID Returns: NPC name or…, Determine the direction from one room to another by checking room exits. Args:…, Handles all NPC-related real-time events., Get the departure message for an NPC from its behavior_config. If no custom… (+35 more)

### Community 502 - "fastapi_integration.py"
Cohesion: 0.01
Nodes (180): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+172 more)

### Community 503 - "useWebSocketConnection.ts"
Cohesion: 0.17
Nodes (12): ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach(), wsConnectionBeforeEach() (+4 more)

### Community 504 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 505 - "RoomNodeData"
Cohesion: 0.23
Nodes (15): HistoryEntry, MapEditingChanges, UseMapEditingOptions, UseMapEditingResult, UseMapLayoutResult, ExitEdgeData, RoomNodeData, RoomMapData (+7 more)

### Community 506 - "Multiplayer Architecture Planning"
Cohesion: 0.25
Nodes (8): Performance Optimization Summary, Alias System Implementation Plan, Chat System Implementation Plan, Planning Completion Summary, Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 507 - "test_occupants.py"
Cohesion: 0.18
Nodes (18): _format_occupants_result(), _get_event_handler_for_test_occupants(), _get_room_id_for_test_occupants(), handle_npc_test_occupants_command(), Any, NPC test-occupants command for debugging occupant queries., Resolve application, player, room_id, and event handler for NPC test occupants…, Handle NPC test occupants command - manually trigger occupant query for… (+10 more)

### Community 508 - "room_validator/tests/conftest.py"
Cohesion: 0.15
Nodes (18): dead_end_room(), invalid_room_data(), fixture, Pytest configuration and fixtures for room validator tests. Provides test data…, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit. (+10 more)

### Community 509 - "Lint Remediation Prompt - AI-Optimized Version"
Cohesion: 0.12
Nodes (16): 🚨 AI ERROR HANDLING, 📋 AI EXECUTION CHECKLIST, 🎯 AI EXECUTION SUCCESS CRITERIA, 🎯 AI SUCCESS METRICS, 🔍 DEBUGGING GUIDE, 📝 DOCUMENTATION REQUIREMENTS, Example Documentation Format, For Large Codebases (+8 more)

### Community 510 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 511 - "useGameConnectionRefactored.ts"
Cohesion: 0.12
Nodes (17): useConnectionState(), UseConnectionStateResult, ConnectionContext, ConnectionEvent, connectionMachine, ConnectionMachineInput, ConnectionState, mockWebSocket (+9 more)

### Community 512 - "ADR-003 Dual Event Systems EventBus NATS"
Cohesion: 0.10
Nodes (22): FastAPI-Generated OpenAPI 3.1, API OpenAPI Specification, ADR-001 Layered Architecture Event-Driven, ADR-002 ApplicationContainer DI, ADR-003 Dual Event Systems EventBus NATS, In-Process EventBus, NATS Distributed Messaging, ADR-004 WebSocket-Only Realtime (+14 more)

### Community 513 - "MovementService"
Cohesion: 0.07
Nodes (29): MovementService, Any, Exception, Room, UUID, Validate movement parameters. Returns False if validation fails (same room),…, Resolve player by ID or name and return player object and resolved ID., Get and validate rooms for movement. (+21 more)

### Community 514 - "Linting Complexity Alignment"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 516 - "NPCSpawnRuleCRUDMixin"
Cohesion: 0.17
Nodes (13): Any, Map procedure result row to NPCSpawnRule model., _row_to_npc_spawn_rule(), NPCSpawnRuleCRUDMixin, Any, AsyncSession, Validate NPC definition existence and population counts for spawn rule creation., Execute create_spawn_rule stored procedure and return the created spawn rule. (+5 more)

### Community 517 - "GameBundle"
Cohesion: 0.04
Nodes (45): GameBundle, Any, datetime, Exception, Wire user_manager into follow_service and nats_message_handler when present., Set item prototype registry on player service when both are available., Create room and profession cache services; set to None on RuntimeError., Wire exploration, movement, follow, and party services. (+37 more)

### Community 518 - "test_security_headers.py"
Cohesion: 0.15
Nodes (16): asyncio, Unit tests for security headers middleware. Tests the SecurityHeadersMiddleware…, Test middleware error handling., Test _add_security_headers_to_response adds headers to Response., Test _add_security_headers_to_response includes subdomains in HSTS., Test dispatch method (backward compatibility)., Test dispatch method error handling., Test middleware passes through non-HTTP connections. (+8 more)

### Community 520 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 521 - "NPCCacheService"
Cohesion: 0.07
Nodes (20): bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…, NPCCacheService, Any, Initialize the room cache service. Args: persistence: Persistence layer instance (+12 more)

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
Cohesion: 0.15
Nodes (14): items, type, items, type, uniqueItems, minLength, type, effect_components (+6 more)

### Community 528 - "generate_sql.mjs"
Cohesion: 0.30
Nodes (15): ajv, __dirname, ensureDir(), __filename, generateEmotes(), generateHolidays(), generateNpcSchedules(), generateRooms() (+7 more)

### Community 529 - "PrototypeRegistry"
Cohesion: 0.18
Nodes (11): PrototypeRegistry, Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, In-memory registry for validated item prototypes., Load prototypes from a directory of JSON files., main() (+3 more)

### Community 530 - "_NPCCombatIntegrationDeps"
Cohesion: 0.14
Nodes (12): _NPCCombatIntegrationDeps, Protocol, UUID, Structured logging / observability trail when NPC-initiated combat begins., Start a new combat and process initial attack., Broadcast room occupants update to killer's room after NPC death. Swallows…, Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize…, Return combat service dependency. (+4 more)

### Community 531 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test filter_online_players with all players online., Test filter_online_players with some players offline., Test filter_online_players with players without last_active., Test handle_who_command when persistence is not available., Test handle_who_command when no players are found., Test handle_who_command successful execution., Test handle_who_command with filter term. (+11 more)

### Community 532 - "GameTickService"
Cohesion: 0.05
Nodes (32): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+24 more)

### Community 533 - "K"
Cohesion: 0.14
Nodes (10): K, Put an item into the cache. Args: key: The key to store value: The value to…, Get an item from the cache, or set it using a factory function if not found.…, Get all keys in the cache., Get all values in the cache., Get all key-value pairs in the cache., Check if a key exists in the cache., Get an item from the cache. Args: key: The key to look up Returns: The cached… (+2 more)

### Community 535 - "TestPathValidator"
Cohesion: 0.10
Nodes (12): fixture, Tests for path validator functionality. Validates room connectivity analysis…, Test detection of mismatched return paths across zones., Test suite for path validation functionality., Create a path validator instance., Sample rooms with zone transitions., Test detection of zone transitions in room connections., Test detection of broken zone transitions. (+4 more)

### Community 536 - "test_event_bus.py"
Cohesion: 0.03
Nodes (83): event_bus(), MockEventClass, asyncio, fixture, Unit tests for event bus. Tests the EventBus class., Test EventBus.publish() queues or processes event., Test EventBus.shutdown() stops processing., Test EventBus.set_main_loop() sets main loop. (+75 more)

### Community 537 - "server/tests/conftest.py"
Cohesion: 0.10
Nodes (28): Config, Item, _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables(), _get_db_name_from_url(), AbstractEventLoop (+20 more)

### Community 538 - "InventoryMutationGuard"
Cohesion: 0.02
Nodes (117): _AsyncPlayerGuardState, InventoryMutationGuard, _PlayerGuardState, Acquire sync mutation guard., Acquire async mutation guard., Get or create per-player guard state for sync contexts. Uses thread-safe…, Get or create per-player guard state for async contexts. Uses async lock to…, Clean up per-player guard state when no longer needed (sync context). Removes… (+109 more)

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

### Community 543 - "GameStateProvider"
Cohesion: 0.10
Nodes (23): GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send… (+15 more)

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

### Community 548 - "Any"
Cohesion: 0.14
Nodes (9): Any, Broadcast player entered message to room occupants. Args: message: The player…, Initialize room event handler. Args: connection_manager: ConnectionManager…, Process player entered event and return player name and normalized IDs. Args:…, Handle player entering a room with enhanced synchronization. Args: event: The…, Unsubscribe a player from a room. Args: player_id: The player's ID (UUID or…, Log player movement for AI processing. Args: player_id: The player's ID…, Broadcast player left message to room occupants. Args: message: The player left… (+1 more)

### Community 549 - "Test Server Remediation Prompt - Cursor Executable Version"
Cohesion: 0.14
Nodes (13): Best Practices, COMPLETION VERIFICATION, CRITICAL "DO NOT" INSTRUCTIONS, CRITICAL: EXECUTION REQUIREMENTS, DECISION TREE - START HERE, ERROR HANDLING PROTOCOL, MANDATORY PROGRESS TRACKING, MANDATORY VERIFICATION CHECKPOINTS (+5 more)

### Community 550 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 551 - "Chat Panel Separation Implementation Tasks"
Cohesion: 0.14
Nodes (13): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Functional Metrics, Overview, Phase Dependencies, Quality Metrics (+5 more)

### Community 552 - "HallucinationFrequencyService"
Cohesion: 0.19
Nodes (12): HallucinationFrequencyService, Any, AsyncSession, UUID, Check if hallucination should trigger on room entry (Uneasy tier). Args:…, Check if hallucination should trigger based on time (Fractured/Deranged tiers).…, Service for managing hallucination frequency checks based on player tier., Initialize the hallucination frequency service. (+4 more)

### Community 553 - "test_message_filtering_helpers.py"
Cohesion: 0.12
Nodes (16): message_filtering_helper(), mock_connection_manager(), fixture, Unit tests for message filtering helper functions. Tests the helper functions…, Create a mock connection manager., Create a MessageFilteringHelper instance., Test extract_chat_event_info() extracts event information., Test should_apply_mute_check() determines if mute check needed. (+8 more)

### Community 554 - "test_look_item.py"
Cohesion: 0.09
Nodes (27): _get_item_description_from_prototype(), Get item description from prototype registry. Returns: Formatted result string…, Unit tests for item look functionality. Tests the helper functions for looking…, Test finding item in equipped items by name., Test finding item in equipped items when not found., Test getting item description from prototype., Test getting item description when prototype registry is None., Test getting item description when prototype_id is missing. (+19 more)

### Community 555 - "ProfessionCacheService"
Cohesion: 0.18
Nodes (11): bench_profession_cache(), _FakePersistence, _get_empty_dict(), main(), Any, Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…, Helper function to return empty dict for mock methods., ProfessionCacheService (+3 more)

### Community 556 - "ChatLogger"
Cohesion: 0.07
Nodes (25): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+17 more)

### Community 557 - "test_combat_persistence_handler.py"
Cohesion: 0.09
Nodes (23): mock_combat_service(), mock_player(), persistence_handler(), fixture, Unit tests for combat persistence handler - core functionality. Tests…, Create mock combat service., Create CombatPersistenceHandler instance., Test CombatPersistenceHandler initialization. (+15 more)

### Community 558 - "test_command_magic.py"
Cohesion: 0.05
Nodes (54): CastCommand, LearnCommand, field_validator, Command for casting a spell., Validate spell name format., Validate target format., Command for viewing spell details., Validate spell name format. (+46 more)

### Community 559 - "test_invite.py"
Cohesion: 0.12
Nodes (15): Unit tests for the Invite model. Tests the Invite model methods including…, Test is_expired returns False for future expiry date., Test is_expired returns True for past expiry date., Test is_expired handles timezone-aware datetime., Test is_valid returns True for active, non-expired invite., Test is_valid returns False for expired invite., Test is_valid returns False for inactive and expired invite., Test use_invite marks invite as used and sets user_id. (+7 more)

### Community 560 - "test_lucidity_service.py"
Cohesion: 0.16
Nodes (15): mock_lucidity_record(), mock_session(), asyncio, fixture, Unit tests for lucidity service., Create a mock async session., Create a mock lucidity record., Test applying positive lucidity adjustment. (+7 more)

### Community 561 - "get_logger"
Cohesion: 0.00
Nodes (667): AttributeError, get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing), Base API router and common dependencies for MythosMUD server. This module…, Event subscription setup for application startup. Extracted from… (+659 more)

### Community 562 - "NATS Remediation Summary 2026-01-13"
Cohesion: 0.25
Nodes (8): NATS Error Handling Strategy, NATS Manual Acknowledgment Guide, NATS Manual Ack Pattern, NATS Medium Priority Remediation, NATS Critical Fixes Summary, NATS Remediation Summary 2026-01-13, NATS Subject Patterns, NATS Subject Naming Patterns

### Community 563 - "PartyService"
Cohesion: 0.12
Nodes (22): PartyUpdated, Event fired when party membership or leadership changes. Emitted by…, PartyService, Party service for MythosMUD. In-memory ephemeral party state: parties exist…, Send party_invite event to the target player only., In-memory party management: create, disband, add/remove/kick members, leader…, event_bus(), party_events() (+14 more)

### Community 564 - "test_database_config_helpers_asyncpg_settings.py"
Cohesion: 0.16
Nodes (15): clear_postgres_search_path(), fixture, MonkeyPatch, Unit tests for get_asyncpg_server_settings_for_database_url., Ensure POSTGRES_SEARCH_PATH does not leak between cases., Known env DBs must set search_path to the database name when env override is…, When POSTGRES_SEARCH_PATH matches the DB name, keep that search_path., Non-mythos_* URLs still honor POSTGRES_SEARCH_PATH. (+7 more)

### Community 565 - "generate_invites_db.py"
Cohesion: 0.19
Nodes (15): create_invite_in_db(), generate_invite_code(), generate_unique_codes(), get_existing_codes(), main(), parse_expires_date(), datetime, Generate a unique Mythos-themed invite code. (+7 more)

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

### Community 571 - "who_commands.py"
Cohesion: 0.21
Nodes (14): filter_online_players(), filter_players_by_name(), format_who_result(), get_players_for_who(), handle_who_command(), Any, Who command handlers and utilities for MythosMUD. This module contains the who…, Filter players to only those who are online (active within threshold). Args:… (+6 more)

### Community 572 - "messageHandlers.ts"
Cohesion: 0.16
Nodes (14): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+6 more)

### Community 573 - "_PlayerCombatClearing"
Cohesion: 0.14
Nodes (11): _PlayerCombatClearing, Protocol, _RandomChoiceSource, Minimal surface used by this service to publish respawn-related events., Deliver a respawn-related domain event to the game's event bus., Minimal surface used to clear combat state when a player respawns., Drop combat involvement for this player after respawn., Subset of random.Random / random module API used for liability picks. (+3 more)

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
Cohesion: 0.14
Nodes (11): Path, Fix self-references by adding proper flags. Args: room_database: Complete room…, Find the file for a room. Returns None if file doesn't exist., Create backup if requested., Initialize the room fixer. Args: base_path: Base directory for room files, Save fixed room if changes were made., Fix basic schema issues. Args: room_database: Complete room database…, Create a backup of a room file. Args: file_path: Path to the file to backup… (+3 more)

### Community 585 - "Configuration Files Reference"
Cohesion: 0.10
Nodes (22): Configuration File Tuples, Configuration Files Reference, .env.local Secrets Pattern, Container/Item Repository Async Migration Plan, SQLAlchemy Async Migration Option, Container System API, Container System API Reference, Container Item System (+14 more)

### Community 586 - "RoomBasedChannelStrategy"
Cohesion: 0.33
Nodes (5): Strategy for room-based channels (say, local, emote, pose)., Initialize room-based channel strategy. Args: channel_type: Type of room-based…, RoomBasedChannelStrategy, Test RoomBasedChannelStrategy.broadcast() handles missing room_id., test_room_based_channel_strategy_broadcast_no_room_id()

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

### Community 592 - "combat_loader.py"
Cohesion: 0.08
Nodes (34): Movement service for command modules., Player position service for command modules., format_combat_status(), get_combat_target(), Any, Produce a human-readable combat status string. This helper is retained for…, Resolve a combat target by name. The current implementation is intentionally…, _app_from_request() (+26 more)

### Community 593 - "test_event_publisher_helpers.py"
Cohesion: 0.14
Nodes (14): event_publisher(), mock_nats_service(), fixture, Unit tests for event publisher helper functions. Tests the helper functions in…, Create a mock NATS service., Create an EventPublisher instance., Test _create_event_message() creates event message., Test get_next_sequence_number() increments sequence. (+6 more)

### Community 594 - "StatisticsAggregator"
Cohesion: 0.05
Nodes (40): Any, UUID, Get comprehensive connection statistics. Args: player_websockets: Player to…, Analyze connection health distribution. Args: connection_metadata: Connection…, Aggregates statistics from connection management components. This class…, Analyze connection types. Args: connection_metadata: Connection metadata…, Analyze connection ages. Args: connection_metadata: Connection metadata now:…, Analyze session health. Args: connection_metadata: Connection metadata Returns:… (+32 more)

### Community 595 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 596 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 597 - "lucidityEventUtils.ts"
Cohesion: 0.31
Nodes (12): buildLucidityChangeMessage(), buildLucidityStatus(), createHallucinationEntry(), createHallucinationId(), createRescueState(), parseNumber(), resolveCurrentLucidity(), resolveCurrentRawValue() (+4 more)

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

### Community 602 - "Any"
Cohesion: 0.20
Nodes (8): Any, Disband a party. If by_player_id is given, only the leader may disband. If…, Safely schedule an async notification, handling cases where no event loop is…, Notify a player they have been removed from a party. Resolves leader name., Remove a player from a party (leave or internal remove). If leader leaves,…, Remove a member from the party. Only the leader may kick., Initialize empty party store. Optionally provide event_bus, connection_manager,…, Emit PartyUpdated event if event_bus is set.

### Community 603 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test handling item look when item is in room drops., Test handling item look when item is in inventory., Test handling item look when item is equipped., Test handling item look when item not found., Test handling item look with look_in flag skips equipped items., Test trying implicit lookup when item is in room drops., Test trying implicit lookup when item not found. (+17 more)

### Community 604 - "CoordinateValidator"
Cohesion: 0.21
Nodes (9): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Coordinate validation service for ASCII maps. This module provides conflict…, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:…, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate… (+1 more)

### Community 605 - "_find_item_in_inventory"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id. Args: inventory: List…, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 606 - "parse_shutdown_parameters"
Cohesion: 0.14
Nodes (14): parse_shutdown_parameters(), Parse shutdown command parameters. Args: command_data: Command data dictionary…, Test parse_shutdown_parameters() with no args defaults to 10 seconds., Test parse_shutdown_parameters() with cancel action., Test parse_shutdown_parameters() with seconds., Test parse_shutdown_parameters() with negative seconds., Test parse_shutdown_parameters() with zero seconds., Test parse_shutdown_parameters() with invalid string. (+6 more)

### Community 607 - "deque"
Cohesion: 0.08
Nodes (51): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+43 more)

### Community 608 - "test_command_processor.py"
Cohesion: 0.03
Nodes (76): command_processor(), fixture, Unit tests for command processor. Tests the CommandProcessor class which…, Test process_command_string handles KeyError., Test process_command_string handles RuntimeError., Test _extract_attributes extracts attributes correctly., Test _extract_attributes handles missing attributes., Test _is_combat_command returns True for attack command. (+68 more)

### Community 610 - "_clear_corrupted_cache_entry"
Cohesion: 0.14
Nodes (14): _clear_corrupted_cache_entry(), Clear a corrupted cache entry if it exists. Args: request: FastAPI request…, Test _clear_corrupted_cache_entry() clears cache entry., Test _clear_corrupted_cache_entry() handles None request., Test _clear_corrupted_cache_entry() handles request without state., test_clear_corrupted_cache_entry(), test_clear_corrupted_cache_entry_no_request(), test_clear_corrupted_cache_entry_no_state() (+6 more)

### Community 611 - "test_player_event_handlers_utils.py"
Cohesion: 0.12
Nodes (15): Unit tests for player event handler utilities. Tests the…, Test normalize_event_ids() with string IDs., Test process_dict_occupant() processes player occupant., Test build_occupants_snapshot_data() with empty list., Test count_occupants_by_type() with empty list., Test is_player_disconnecting() returns False when player is not disconnecting., Test is_player_disconnecting() handles invalid player_id., Test normalize_player_id() with None returns None without warning. (+7 more)

### Community 612 - "format_player_location"
Cohesion: 0.14
Nodes (14): format_player_location(), Format player location as Zone: Sub-zone: Room from room ID. Args: room_id:…, Test format_player_location() handles invalid room ID., test_format_player_location_invalid(), Test format_player_location() with short room ID format., Test format_player_location() with non-string input., Test formatting valid player location., Test formatting invalid player location. (+6 more)

### Community 613 - "SpellLearningService"
Cohesion: 0.20
Nodes (10): Any, UUID, Learn a spell for a player., Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…, Service for handling spell learning from various sources. Manages spell…, Learn a spell from a spellbook item. Args: player_id: Player ID…, Learn a spell from an NPC teacher. Args: player_id: Player ID npc_id: ID of the…, Learn a spell as a quest reward. Args: player_id: Player ID quest_id: ID of the… (+2 more)

### Community 614 - "Any"
Cohesion: 0.17
Nodes (7): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Check if new data is newer than old data for a specific key. Args: old_data:…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,…, Store room data in cache. Args: room_id: Room ID to store room_data: Room data…

### Community 615 - ".resolve_spell_target"
Cohesion: 0.22
Nodes (8): Any, UUID, Resolve the target for a spell cast. Args: player_id: ID of the player casting…, Get player object from persistence., Get the combat target for a player if they are in combat. Args: player_id:…, Resolve self-target spell. Returns (target_match, error_message)., Resolve area/all target spell. Returns (target_match, error_message)., Resolve entity/location target spell with explicit target. Returns…

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

### Community 622 - "fixture"
Cohesion: 0.09
Nodes (24): async_session_factory(), lucidity_service_factory(), mock_event_dispatcher(), mock_lucidity_service(), mock_persistence(), mock_session(), fixture, Create a mock persistence layer. (+16 more)

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

### Community 628 - "OccupantFormatter"
Cohesion: 0.12
Nodes (15): OccupantFormatter, Formats and separates occupants by type., Initialize occupant formatter., Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists., Test OccupantFormatter._process_player_name_for_update() skips UUID player name., Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict., Test OccupantFormatter.separate_occupants_by_type() separates dict players. (+7 more)

### Community 629 - "item_factory.py"
Cohesion: 0.11
Nodes (19): ItemInstance, initialize_components(), Any, Prepare component state metadata for a new item instance. This routine…, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError, Any (+11 more)

### Community 630 - "Movement Subsystem Design"
Cohesion: 0.20
Nodes (9): Architecture, Component interactions, Constraints, Developer guide, Key design decisions, Movement Subsystem Design, Overview, Related docs (+1 more)

### Community 631 - "load_test_10_players.spec.ts"
Cohesion: 0.22
Nodes (6): generateLoadTestCredential(), INVITE_CODES, PLAYER_CONFIGS, PlayerConfig, NOTE: This test is designed to be executed using Playwright MCP tools for, registerPlayer()

### Community 632 - "enum"
Cohesion: 0.20
Nodes (10): city, countryside, desert, mountains, swamp, tundra, zone_type, description (+2 more)

### Community 633 - "alias_schema.json"
Cohesion: 0.20
Nodes (9): version, additionalProperties, description, $id, aliases, required, $schema, title (+1 more)

### Community 634 - "properties"
Cohesion: 0.20
Nodes (10): properties, minLength, pattern, type, minLength, type, type, id (+2 more)

### Community 635 - "days"
Cohesion: 0.22
Nodes (10): items, items, minItems, type, items, type, pattern, type (+2 more)

### Community 636 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 637 - "player_repository_room.py"
Cohesion: 0.33
Nodes (9): Any, Player, Player room validation helpers for PlayerRepository. Validates and fixes…, Return True if room validation should be skipped (cache empty, instanced, or…, Validate player's current room and fix if invalid. Args: room_cache: Shared…, Validate and fix player room, persisting the fix if needed. Args: room_cache:…, should_skip_room_validation(), validate_and_fix_player_room() (+1 more)

### Community 638 - "Comprehensive System Audit"
Cohesion: 0.67
Nodes (3): CI/CD Enhanced Logging Validation, Comprehensive System Audit, Database Migration Guide

### Community 639 - "test_maps.py"
Cohesion: 0.17
Nodes (22): _MapRooms, _get_current_room_id(), _needs_coordinate_generation(), Check if rooms need coordinate generation. Args: rooms: List of room…, Get current room ID from query params or database. Returns room ID or None., _ensure_coords_stub(), mock_request(), mock_user_and_player() (+14 more)

### Community 640 - "._get_next_sequence"
Cohesion: 0.18
Nodes (8): Any, Build the room occupants update message. Args: room_id_str: Room ID as string…, Build a room update message. Args: room_id: The room ID room_data: The room…, Build a single authoritative room_state message (room metadata + occupants).…, Initialize the message builder. Args: sequence_counter: Callable that returns…, Get the next sequence number., Get the next sequence number (public API). Returns: The next sequence number…, Create a real-time message for player entering a room. Args: event: The…

### Community 641 - "test_exceptions.py"
Cohesion: 0.02
Nodes (90): Initialize the Pydantic error handler. Args: context: Optional error context…, ErrorContext, LoggedException, Any, Exception, Initialize MythosMUD error. Args: message: Technical error message context:…, Convert error to dictionary for API responses., Log validation errors at warning so expected user-input errors do not flood… (+82 more)

### Community 642 - "Security Implementation"
Cohesion: 0.29
Nodes (7): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection, SSE Authentication System

### Community 643 - "test_level_service.py"
Cohesion: 0.06
Nodes (53): level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level(), Unit tests for level curve (XP to level, level from total XP). Character… (+45 more)

### Community 644 - "RetryConfig"
Cohesion: 0.14
Nodes (11): Get current retry configuration. Returns: Current RetryConfig AI: Useful for…, Configuration for retry behavior. Defines retry parameters for handling…, Calculate delay for a given attempt number. Uses exponential backoff capped at…, Initialize retry handler. Args: max_retries: Maximum number of retry attempts…, RetryConfig, Test RetryConfig.calculate_delay() with base delay., Test RetryConfig.calculate_delay() respects max_delay., Test RetryConfig default values. (+3 more)

### Community 645 - "migrate_combat_data.py"
Cohesion: 0.23
Nodes (18): main(), migrate_npc_combat_data(), _migrate_one_npc(), _npc_has_combat_data(), _npc_has_full_combat_data(), Any, AsyncSession, Exception (+10 more)

### Community 647 - "validate_occupant_name"
Cohesion: 0.14
Nodes (14): _accumulate_valid_occupant_name(), Validate that a name is not a UUID string., Parse one occupant row: append display name or log when it looks like a UUID., validate_occupant_name(), Test validate_occupant_name() returns True for valid name., Test validate_occupant_name() returns False for UUID string., Test validate_occupant_name() returns False for empty string., Test validate_occupant_name() returns False for None. (+6 more)

### Community 648 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 649 - "test_player_event_handlers_room.py"
Cohesion: 0.17
Nodes (11): Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test _prepare_room_data() handles room without to_dict method., Test PlayerRoomEventHandler initialization., Test send_room_updates_to_entering_player() handles invalid player_id., Test _process_player_entered_event() returns None when room_id is None., Test handle_player_entered() handles errors., test_handle_player_entered_error_handling(), test_player_room_event_handler_init() (+3 more)

### Community 650 - ".dispatch"
Cohesion: 0.40
Nodes (4): Any, Request, Backward-compatible dispatch method for BaseHTTPMiddleware interface. This…, Add security headers to Response object (compatibility method).

### Community 651 - "PostgresRow"
Cohesion: 0.08
Nodes (17): PostgresRow, Any, Row-like object for PostgreSQL query results., Return the keys of the row dictionary. Returns: dict_keys: The keys of the row…, Execute a query and return a cursor. Args: query: SQL query with PostgreSQL %s…, Get a cursor from the underlying connection. This method provides direct access…, Test PostgresRow class., Test PostgresRow initialization. (+9 more)

### Community 652 - "TestValidateCommandBasics"
Cohesion: 0.20
Nodes (6): Test _validate_command_basics function., Test _validate_command_basics returns result for empty command., Test _validate_command_basics returns result for command too long., Test _validate_command_basics returns result for invalid command content., Test _validate_command_basics returns None for valid command., TestValidateCommandBasics

### Community 653 - "RateLimiter"
Cohesion: 0.10
Nodes (17): Any, RateLimiter, Remove timestamps older than the window size. Args: player_id: Player ID…, Check if a player is within rate limits for a channel. Args: player_id: Player…, Record a message for rate limiting. Args: player_id: Player ID channel: Channel…, Sliding window rate limiter for chat channels. Implements per-user, per-channel…, Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…, Reset rate limiting for a player. Args: player_id: Player ID channel: Specific… (+9 more)

### Community 654 - "validate_room_data"
Cohesion: 0.05
Nodes (37): patch, Unit tests for world loader utility functions. Tests room ID generation,…, Test get_room_environment() treats empty string as no environment., Test validate_room_data() function., Test validate_room_data() returns empty list when validation not available., Test validate_room_data() with provided validator., Test validate_room_data() creates validator when not provided., Test validate_room_data() returns validation errors. (+29 more)

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

### Community 661 - "persist_player"
Cohesion: 0.06
Nodes (54): _DropResolved, clone_inventory(), get_room_manager(), persist_player(), _player_uuid_for_quest_sync(), Player, UUID, Resolve player UUID for collect_n sync; None when missing. (+46 more)

### Community 662 - "test_inventory_commands_more_helpers.py"
Cohesion: 0.08
Nodes (32): asyncio, Unit tests for additional inventory_commands helper functions. Tests helper…, Test _clone_inventory() returns deep copy of inventory., Test _broadcast_room_event() calls broadcast_to_room., Test broadcast_room_event() passes exclude_player parameter., Test broadcast_room_event() handles None connection_manager., Test _broadcast_room_event() handles connection_manager without…, Test _broadcast_room_event() handles exceptions gracefully. (+24 more)

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
Cohesion: 0.22
Nodes (9): 2. Message Routing Logic, 3. State Management, 4. Event Handling, Command Routing Logic, Current Logic (in CommandPanel), New Logic Distribution, New State Structure, State Distribution (+1 more)

### Community 673 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 674 - "_PopulationLifecycleManager"
Cohesion: 0.15
Nodes (8): _PopulationLifecycleManager, Protocol, Initialize the NPC population controller. Args: event_bus: Event bus for…, Load zone and sub-zone configurations from PostgreSQL database., Subscribe to relevant game events., Lifecycle manager surface used by NPCPopulationController (avoids import cycle…, Clear all population statistics. This ensures a clean state when the server…, Spawn an NPC instance; returns (npc_id, None) or (None, failure_reason).

### Community 675 - "test_connection_event_helpers.py"
Cohesion: 0.14
Nodes (23): Any, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events., subscribe_to_room_events_impl(), unsubscribe_from_room_events_impl(), asyncio, Unit tests for connection event helpers. Tests the connection_event_helpers…, Test unsubscribe_from_room_events_impl() handles AttributeError. (+15 more)

### Community 676 - "skills_commands.py"
Cohesion: 0.24
Nodes (13): _format_skills_output(), _get_container_services(), handle_skills_command(), Any, UUID, Skills command handler (plan 10.7 V4). Returns the active character's skills as…, Get container, persistence, and skill_service from request, or None if…, Extract and validate player_id from player object, returning UUID or None. (+5 more)

### Community 677 - "party_commands.py"
Cohesion: 0.18
Nodes (19): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+11 more)

### Community 678 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 679 - "properties"
Cohesion: 0.22
Nodes (9): properties, description, pattern, type, created_at, updated_at, description, pattern (+1 more)

### Community 680 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 681 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 682 - "Protocol"
Cohesion: 0.15
Nodes (13): _AppStateForEventHandler, _AppStateWithNpcLifecycle, _AppWithState, _ContainerWithNpcLifecycle, _NpcOccupantDisplay, Protocol, Minimal app.state.container shape for resolving the real-time event handler., Minimal FastAPI/Starlette app shape for reading ``state``. (+5 more)

### Community 683 - "fixture"
Cohesion: 0.15
Nodes (13): catalog_with_own_language_and_mythos(), mock_persistence(), mock_player_skill_repo(), mock_skill_repo(), mock_skill_use_log_repo(), fixture, Mock PlayerSkillRepository., Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id). (+5 more)

### Community 684 - "Realtime Connection Compatibility"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 685 - "handle_channel_command"
Cohesion: 0.24
Nodes (11): _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting(), Any, Validate channel name. Returns error dict if invalid, None if valid., Handle the channel command for switching channels or setting default channel.…, Get persistence and player. Returns (persistence, player) or (None, None) if… (+3 more)

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

### Community 694 - "MockPersistence"
Cohesion: 0.22
Nodes (5): MockPersistence, Mock persistence layer with async methods., Mock async method that uses configured mock., Mock method that uses configured mock., Allow setting get_player_by_name and get_room_by_id to mocks.

### Community 695 - "enum"
Cohesion: 0.20
Nodes (10): artifact, consumable, container, currency, equipment, quest, enum, type (+2 more)

### Community 696 - "enum"
Cohesion: 0.25
Nodes (8): catholic, islamic, jewish, mythos, neo_pagan, tradition, enum, type

### Community 697 - "alias"
Cohesion: 0.25
Nodes (8): command, additionalProperties, description, required, type, $defs, alias, name

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

### Community 708 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_players_batch with empty list., Test _load_room_cache_async logs sample room IDs when rooms are loaded…, Test _load_room_cache_async handles table not found error., Test _load_room_cache_async raises other errors., Test _query_rooms_with_exits_async handles table not found error., Test _query_rooms_with_exits_async raises other errors., test_get_players_batch_empty_list() (+5 more)

### Community 709 - "test_combat_service.py"
Cohesion: 0.24
Nodes (19): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+11 more)

### Community 710 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

### Community 711 - "._create_grid_map"
Cohesion: 0.09
Nodes (12): Any, Extract street name from room ID. Args: room_id: Full room ID Returns: Street…, Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…, Render the mini-map as ASCII art with grid-based visualization. Args:…, Create a grid-based map visualization. Args: nodes: List of room nodes edges:…, Assign grid coordinates to rooms based on connectivity. Args: nodes: List of…, Get coordinates for the next room based on direction. Args: x: Current x…, Reverse a direction. Args: direction: Original direction Returns: Reversed… (+4 more)

### Community 712 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _build_room_objects logs debug info for specific room., Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., test_build_room_objects_debug_logging(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

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
Cohesion: 0.03
Nodes (60): mock_config(), fixture, rate_limiter(), Unit tests for rate limiter service. Tests the RateLimiter class which provides…, Test check_rate_limit returns True when within limits., Test check_rate_limit returns False when limit exceeded., Test check_rate_limit always returns True when disabled., Test check_rate_limit handles errors gracefully (fails open). (+52 more)

### Community 718 - "threading.py"
Cohesion: 0.04
Nodes (37): get_summary(), Any, Exception metrics tracking for monitoring. This module provides thread-safe…, Get a summary of exception counts. Returns: dict[str, Any]: Dictionary…, NPC subsystem for MythosMUD. This package provides the NPC (Non-Player…, Check if idle movement should be scheduled based on configuration and timing.…, Create a WANDER action message. Args: current_time: Current timestamp Returns:…, Queue a WANDER action via the thread manager. Args: wander_action: The wander… (+29 more)

### Community 719 - "._is_valid_name_for_occupant"
Cohesion: 0.24
Nodes (7): Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Check if a name is valid for use as an occupant name. Args: name: The name to…, Add a valid name to both target list and all occupants list. Args: name: The…, Process a player name and add to appropriate lists if valid. Args: player_name:…, Process an NPC name and add to appropriate lists if valid. Args: npc_name: The…

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
Cohesion: 0.07
Nodes (16): Lock, MetricsCollector, Any, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or…, Simple metrics collector for NATS message delivery. Thread-safe metrics… (+8 more)

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

### Community 732 - "MythosMUD"
Cohesion: 0.29
Nodes (5): Geography Overview, Engineering memory, MythosMUD, Sources, World

### Community 733 - "Chat Panel Separation Specification"
Cohesion: 0.29
Nodes (6): Chat Panel Separation Specification, Conclusion, Current Integration Points, Current State Analysis, Existing Structure, Overview

### Community 734 - "seed_e2e_users.py"
Cohesion: 0.23
Nodes (10): E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio., One row in users plus optional default character for login E2E. (+2 more)

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

### Community 750 - "bonus_tags"
Cohesion: 0.33
Nodes (6): items, type, uniqueItems, minLength, type, bonus_tags

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

### Community 757 - "player_combat_service.py"
Cohesion: 0.05
Nodes (53): check_combat_state(), check_player_posture(), extract_player_id(), Any, Room, UUID, Movement validation helpers for MovementService. Cohesive validation and room-…, Validate player is in the from_room, auto-adding if database matches. (+45 more)

### Community 758 - "get_help_content"
Cohesion: 0.13
Nodes (16): get_command_categories(), get_commands_by_category(), _get_general_help(), get_help_content(), Any, Help content and command documentation for MythosMUD. This module contains the…, Get help content for commands. Args: command_name: Optional specific command…, Get general help content with command categories. (+8 more)

### Community 759 - "items"
Cohesion: 0.33
Nodes (6): items, minItems, type, additionalProperties, properties, holidays

### Community 760 - "Quest System Features"
Cohesion: 0.40
Nodes (6): Quest Design Guidelines, Quest Design Principles, Quest System Features, Event-Driven Quest Progression, Quest Goal Types, Declarative YAML Quest Config

### Community 761 - "Testing Guide"
Cohesion: 0.29
Nodes (8): Quick Start E2E Tests, E2E Test Server Quick Start, Container-Based Test Fixtures, Test Modernization Plan, bcrypt PyO3 Fresh Session Limitation, Testing Guide, Pydantic Testing Patterns, Two-Tier Test Suite (make test)

### Community 762 - "._is_uuid_string"
Cohesion: 0.17
Nodes (10): Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Check if a string looks like a UUID. Args: value: The string to check Returns:…, Test OccupantFormatter._is_uuid_string() returns True for valid UUID., Test OccupantFormatter._is_uuid_string() returns False for invalid length., Test OccupantFormatter._is_uuid_string() returns False for wrong dash count., Test OccupantFormatter._is_uuid_string() returns False for invalid characters., test_occupant_formatter_is_uuid_string_invalid_chars(), test_occupant_formatter_is_uuid_string_invalid_dashes() (+2 more)

### Community 763 - "Any"
Cohesion: 0.11
Nodes (10): Any, Despawn an NPC instance. Args: npc_id: ID of the NPC to despawn reason: Reason…, Move an NPC instance to a different room. Args: npc_id: ID of the NPC to move…, Get all active NPC instances. Returns: List of NPC instance information, Get detailed stats for a specific NPC instance. Args: npc_id: ID of the NPC…, Get NPC population statistics. Returns: Dictionary with population statistics, Get NPC zone statistics. Returns: Dictionary with zone statistics, Get system-wide NPC statistics. Returns: Dictionary with system statistics (+2 more)

### Community 764 - "parse_json_field"
Cohesion: 0.17
Nodes (12): parse_json_field(), Parse a JSON field from database, handling both dict/list and string formats.…, Test parse_json_field() returns default when None., Test parse_json_field() parses JSON string., Test parse_json_field() returns dict as-is., Test parse_json_field() returns list as-is., Test parse_json_field() raises error on invalid JSON string., test_parse_json_field_dict() (+4 more)

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

### Community 775 - "name"
Cohesion: 0.33
Nodes (6): description, maxLength, minLength, pattern, type, name

### Community 776 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 777 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 778 - "._load_player_mutes_from_data"
Cohesion: 0.22
Nodes (5): Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory., Load channel mutes from JSON data into memory., Load global mutes from JSON data into memory.

### Community 779 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test unsubscribe_from_event_subjects handles partial success., Test cleanup_empty_subzone_subscriptions handles NATSError., Test _handle_player_attacked_event delegates to event handler., Test unsubscribe_from_subzone handles not subscribed case., Test _handle_event_message delegates to event handler. (+9 more)

### Community 780 - "CommandRequest"
Cohesion: 0.08
Nodes (23): CommandRequest, handle_command(), BaseModel, post, Request, Handle incoming HTTP command requests., Request model for command processing., asyncio (+15 more)

### Community 781 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test get_player_by_name returns None when player not found., Test get_player_by_id returns None when player not found., Test get_player_by_user_id returns None when no players., Test soft_delete_player successfully soft deletes player., Test delete_player successfully deletes player., Test delete_player returns False when player not found., Test update_player_last_active successfully updates timestamp. (+9 more)

### Community 782 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test _spawn_required_npcs() successfully spawns required NPCs., Test _spawn_required_npcs() handles spawn failures., Test _spawn_optional_npcs() skips NPCs with low probability., Test _spawn_optional_npcs() handles missing spawn room., Test spawn_npcs_on_startup() spawns optional NPCs., Arena pass is skipped when required/optional passes spawned nothing., One arena instance per definition_id present in required/optional spawned_npcs. (+11 more)

### Community 783 - "_occupation_slots_9"
Cohesion: 0.17
Nodes (12): _occupation_slots_9(), Valid 9 slots: one 70, two 60, three 50, three 40; 9 distinct skill_ids (no…, Personal interest with Cthulhu Mythos raises ValueError., personal_interest must have exactly 4 entries., occupation_slots with duplicate skill_id raises ValueError., personal_interest with duplicate skill_id raises ValueError., Occupation and personal interest sharing a skill_id raises ValueError., test_set_player_skills_cthulhu_mythos_in_personal_rejected() (+4 more)

### Community 784 - "UUID"
Cohesion: 0.02
Nodes (61): __getattr__(), Any, Player, UUID, Get the first WebSocket connection ID for a player (backward compatibility)., Check if a player has any WebSocket connections., Get the number of connections for a player by type., Subscribe a player to a room (compatibility method). (+53 more)

### Community 785 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

### Community 787 - "ItemPrototypeModel"
Cohesion: 0.14
Nodes (11): ItemPrototypeModel, BaseModel, field_validator, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validated representation of an item prototype definition. This model keeps the…, Validate that item_type is in the allowed list. Args: value: The item type to…, Validate that all flags are in the allowed list. Args: value: The list of flags… (+3 more)

### Community 788 - "spell_effects_status.py"
Cohesion: 0.11
Nodes (37): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+29 more)

### Community 790 - "test_metadata.py"
Cohesion: 0.11
Nodes (15): Shared SQLAlchemy metadata for MythosMUD models. This module provides the…, NPC Database metadata for MythosMUD. This module defines the SQLAlchemy…, Unit tests for metadata modules. Tests the shared SQLAlchemy metadata instances., Test that metadata is a MetaData instance., Test that npc_metadata is a MetaData instance., Test that metadata and npc_metadata are separate instances., Test that Base is a DeclarativeBase subclass., Test that Base has metadata attribute set to shared metadata. (+7 more)

### Community 791 - "alias_storage"
Cohesion: 0.12
Nodes (17): Get the alias storage from the request context., alias_storage(), fixture, Path, Create a temporary directory for alias storage., Create an AliasStorage instance with temporary directory., Create a sample alias for testing., Create another sample alias for testing. (+9 more)

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

### Community 796 - "Profession"
Cohesion: 0.03
Nodes (71): Profession, Any, Base, Check if given stats meet the profession requirements. Args: stats: Dictionary…, Check if profession is available for player selection., Get formatted text for displaying stat requirements. Returns: Formatted string…, Profession model for game data. Stores profession information including name,…, String representation of the profession. (+63 more)

### Community 797 - "test_player_event_handlers_respawn.py"
Cohesion: 0.17
Nodes (11): Unit tests for player respawn event handlers. Tests the…, Test send_respawn_event_with_retry() waits for connection to become available., Test PlayerRespawnEventHandler initialization., Test update_connection_manager_position() updates position., Test update_connection_manager_position() handles player not in online_players., Test update_connection_manager_position() handles missing online_players…, test_player_respawn_event_handler_init(), test_send_respawn_event_with_retry_waits_for_connection() (+3 more)

### Community 798 - "E 2 E Scenario Scenarios"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 799 - "test_command_helpers.py"
Cohesion: 0.23
Nodes (11): Unit tests for command helper utilities. Tests helper functions for command…, Test get_command_help with no command (general help)., Test get_command_help with specific command types., Test get_command_help with unknown command., Test get_command_help is case insensitive., test_get_command_help_case_insensitive(), test_get_command_help_no_command(), test_get_command_help_specific_commands() (+3 more)

### Community 800 - ".add_message"
Cohesion: 0.18
Nodes (6): Any, Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…, Check if a message is recent (within the specified age limit). Args: msg:…, Get message queue statistics. Returns: Dict[str, Any]: Statistics about the…, Add a message to a player's pending message queue. Args: player_id: The…, Get all pending messages for a player and clear the queue. Args: player_id: The…

### Community 801 - "wrap_third_party_exception"
Cohesion: 0.20
Nodes (11): create_logged_http_exception(), log_and_raise_http(), log_error_with_context(), Any, Exception, HTTPException, Log an error with structured context. Delegates to log_structured_error., Create an HTTPException with proper logging and return it. Delegates to… (+3 more)

### Community 802 - "test_metrics.py"
Cohesion: 0.03
Nodes (59): Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, Reset all metrics to zero., Performance metrics for NATS Subject Manager operations. Tracks validation…, Record a validation operation. Args: duration: Time taken in seconds success:…, Record a build operation. Args: duration: Time taken in seconds success:…, Record an error occurrence. Args: error_type: Type of error (pattern_not_found,… (+51 more)

### Community 803 - "RoomCacheService"
Cohesion: 0.18
Nodes (10): bench_room_cache(), _FakePersistence, main(), Any, Lightweight cache benchmark for CI artifacts. Measures miss vs. hit timings for…, Fake persistence layer providing async_get_room with simulated latency., Service for caching room data., Invalidate cached room data. Args: room_id: The room ID to invalidate (+2 more)

### Community 804 - "lifespan_shutdown.py"
Cohesion: 0.19
Nodes (16): FastAPI, Application shutdown logic. This module handles graceful shutdown of all…, Shutdown event bus and clean up all service subscriptions., Handle graceful shutdown of all services., Shutdown and persist mythos chronicle state., Shutdown NATS message handler if present., Shutdown connection manager if present., Shutdown mythos tick scheduler if present. (+8 more)

### Community 805 - "create_error_context"
Cohesion: 0.24
Nodes (9): create_error_context(), Any, Request, Create error context from request and user. Helper function to reduce…, Unit tests for server.api.player_helpers (error context helper)., When current_user is None, context gets metadata only., When current_user is set, user_id is populated and metadata merged., test_create_error_context_with_user_sets_user_id_and_metadata() (+1 more)

### Community 806 - "._connect_nats"
Cohesion: 0.22
Nodes (6): Any, BaseException, Raise RuntimeError when e2e requires live NATS; no-op for other environments., Convert connect failures into hard error (e2e) or soft log (other envs)., Handle connect() returning False; raise for e2e, soft-warn otherwise., Connect to NATS if enabled and not unit_test. Returns NATSService or None.…

### Community 807 - "Invite"
Cohesion: 0.11
Nodes (12): Get all unused invites., Invite, Base, Invite model for MythosMUD. This module defines the Invite model for managing…, Model for user registration invites., Check if the invite has expired. Handles naive timestamps as UTC., Check if the invite is valid (active and not expired)., Mark this invite as used by a specific user. (+4 more)

### Community 808 - "Audit Suppressions"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 809 - "Fix Markdown Line"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 810 - "Populate Npc Sample"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 811 - "NPCMovementIntegration"
Cohesion: 0.04
Nodes (39): _entity_id_for_quest_offer(), _make_on_npc_died(), _make_on_player_entered(), _make_on_player_left(), _parse_player_id(), Any, UUID, Quest event subscriptions: room entry (trigger start), room exit… (+31 more)

### Community 812 - "._error_callback"
Cohesion: 0.50
Nodes (3): Exception, Handle NATS errors. AI: Runs as fire-and-forget async task to prevent blocking…, Async handler for NATS connection errors.

### Community 813 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 814 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 815 - "extract_zone_name"
Cohesion: 0.20
Nodes (10): extract_zone_name(), Extract zone name from stable_id (format: 'plane/zone'). Args: stable_id: The…, Test extract_zone_name() extracts zone from stable_id., Test extract_zone_name() returns stable_id when no slash., Test extract_zone_name() extracts from first slash., Test extract_zone_name() handles empty string., test_extract_zone_name_empty(), test_extract_zone_name_multiple_slashes() (+2 more)

### Community 816 - "DecodeLiabilitiesFn"
Cohesion: 0.22
Nodes (8): DecodeLiabilitiesFn, EncodeLiabilitiesFn, LiabilityStackEntry, Protocol, Callable that parses liability JSON into normalized stack entries., Decode stored liability text (or empty state) into stack rows., Callable that serializes liability stack rows for persistence., Encode stack rows into JSON suitable for PlayerLucidity.liabilities.

### Community 817 - "NATSSubjectManager"
Cohesion: 0.05
Nodes (32): Initialize combat event publisher. Args: nats_service: NATS service instance…, NATSSubjectManager, Any, Build a NATS subject from a pattern and parameters. Args: pattern_name: Name of…, Ensure pattern exists in registry. Args: pattern_name: Name of the pattern to…, Ensure all required parameters are provided. Args: pattern_name: Name of the…, Format subject string from pattern and parameters. Args: pattern_name: Name of…, Ensure subject length is within limits. Args: subject: Subject string to… (+24 more)

### Community 818 - "Package Scripts Build"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 819 - ".call"
Cohesion: 0.22
Nodes (5): _CircuitBreakerResult, Execute function with circuit breaker protection. Args: func: Function to…, Handle successful operation., Handle failed operation., Check if circuit breaker should attempt reset.

### Community 820 - "Tsconfig Node"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 821 - "validate_shutdown_admin_permission"
Cohesion: 0.22
Nodes (8): Validate that a player has admin permissions for server shutdown. Args: player:…, validate_shutdown_admin_permission(), Test validate_shutdown_admin_permission() returns False when player is None., Test validate_shutdown_admin_permission() returns False when player is not…, Test validate_shutdown_admin_permission() returns True when player is admin., test_validate_shutdown_admin_permission_admin(), test_validate_shutdown_admin_permission_no_player(), test_validate_shutdown_admin_permission_not_admin()

### Community 822 - ".connect_websocket"
Cohesion: 0.22
Nodes (5): WebSocket, Check if a WebSocket is open., Safely close a WebSocket connection., Connect a WebSocket for a player., Get connection ID from a WebSocket instance.

### Community 823 - "chat_logger"
Cohesion: 0.22
Nodes (7): Initialize the rate limiter with configuration-based limits., Initialize the user manager. Args: data_dir: Directory for player-specific mute…, chat_logger(), fixture, Create a temporary directory for chat logs., Create a ChatLogger instance with temp directory., temp_log_dir()

### Community 824 - "test_player_repository.py"
Cohesion: 0.12
Nodes (15): Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes with room cache., Test PlayerRepository initializes with event bus., Test validate_and_fix_player_room returns False for valid room., Test validate_and_fix_player_room fixes invalid room., Test list_players returns empty list when no players., Test save_players successfully saves multiple players., Test PlayerRepository initializes correctly. (+7 more)

### Community 825 - "mock_utils"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_logger(), mock_utils(), player_respawn_event_handler(), fixture, Create a mock connection manager., Create a mock PlayerEventHandlerUtils., Create a mock logger. (+1 more)

### Community 826 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 827 - "ConnectionPanel.tsx"
Cohesion: 0.50
Nodes (3): ConnectionPanel(), ConnectionPanelProps, localStorageMock

### Community 828 - "global-teardown.ts"
Cohesion: 0.40
Nodes (3): __dirname, __filename, projectRoot

### Community 829 - "test_dead_letter_queue.py"
Cohesion: 0.12
Nodes (15): Unit tests for dead letter queue. Tests the DeadLetterQueue class and…, Test enqueue() creates DLQ file., Test dequeue() returns None when queue is empty., Test dequeue() removes file after reading., Test get_statistics() returns stats for empty queue., Test list_messages() handles file read errors., Test DeadLetterMessage.to_dict() handles None headers., Test DeadLetterQueue initialization with storage directory. (+7 more)

### Community 830 - "player_event_handler_utils"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), fixture, Create a mock connection manager., Create a mock name extractor., Create a mock logger. (+1 more)

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
Nodes (99): _create_config_instance(), _get_config_cached(), _get_config_test(), _is_test_mode(), Configuration module for MythosMUD server. This module provides type-safe,…, Reset the configuration cache. In test mode, this is a no-op since get_config()…, Detect if running in test environment. Uses multiple detection methods to…, Create a new AppConfig instance from current environment. This is a helper… (+91 more)

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

### Community 840 - "asyncio"
Cohesion: 0.22
Nodes (9): asyncio, Test get_player_info() returns None for invalid player_id., Test get_player_info() returns None when player not found., Test get_player_info() successfully retrieves player info., Test get_player_info() returns None when connection manager not available., test_get_player_info_invalid_player_id(), test_get_player_info_no_connection_manager(), test_get_player_info_player_not_found() (+1 more)

### Community 841 - "Middleware Command Rate"
Cohesion: 0.10
Nodes (12): CommandRateLimiter, Any, datetime, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate…, Remove timestamp data for players who haven't been active recently. Prevents… (+4 more)

### Community 842 - "fix_markdown_common_issues.py"
Cohesion: 0.22
Nodes (14): fix_emphasis_as_heading(), fix_first_line_heading(), fix_link_fragments(), fix_markdown_file(), generate_anchor(), main(), parse_markdownlint_output(), Path (+6 more)

### Community 843 - "applies_to"
Cohesion: 0.67
Nodes (3): minItems, type, applies_to

### Community 844 - "3. Simplified CommandPanel"
Cohesion: 0.40
Nodes (5): 3. Simplified CommandPanel, CommandPanel Layout Structure, Features to Keep, Features to Remove, Simplified CommandPanel Interface

### Community 845 - "Implementation Phases"
Cohesion: 0.40
Nodes (5): Implementation Phases, Phase 1: Core Separation, Phase 2: Enhanced Features, Phase 3: Polish and Optimization, Phase 4: Testing and Refinement

### Community 846 - "._generate_invite_code"
Cohesion: 0.25
Nodes (6): datetime, Generate a unique invite code., Test _generate_invite_code generates 12-character alphanumeric code., Test _generate_invite_code generates different codes on multiple calls., test_invite_generate_invite_code_format(), test_invite_generate_invite_code_uniqueness()

### Community 847 - "rest_countdown_task.py"
Cohesion: 0.24
Nodes (14): create_rest_countdown_task(), _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, Task, UUID, Rest countdown task implementation. This module contains the async task that… (+6 more)

### Community 848 - "command"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, command

### Community 849 - "Upgrade Implementation Plan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 850 - ".create_invite"
Cohesion: 0.25
Nodes (7): Create a new invite with the specified parameters., Test create_invite creates invite with creator user_id., Test create_invite creates invite with custom expiry days., Test create_invite creates invite with default parameters., test_invite_create_invite_defaults(), test_invite_create_invite_with_creator(), test_invite_create_invite_with_custom_expiry()

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

### Community 866 - "load_zone_configurations"
Cohesion: 0.25
Nodes (8): load_zone_configurations(), Load zone and sub-zone configurations from PostgreSQL database. Returns:…, Test load_zone_configurations() loads configurations., Test load_zone_configurations() merges zone and subzone configs., Test load_zone_configurations() raises RuntimeError on failure., test_load_zone_configurations_error(), test_load_zone_configurations_merges_zone_and_subzone(), test_load_zone_configurations_success()

### Community 867 - "2026_02_19_seed_quest_leave_the_tutorial.py"
Cohesion: 0.40
Nodes (4): downgrade(), Insert leave_the_tutorial quest and quest_offers row., Remove seed quest and its offer., upgrade()

### Community 868 - "test_command_validator.py"
Cohesion: 0.03
Nodes (95): Unit tests for command validator., Test validate_command_length returns True for valid length., Test validate_command_length returns False for too long command., Test validate_command_length with custom max_length., Test validate_command_format returns True for valid command., Test validate_command_format returns False for empty command., Test validate_command_format returns False for suspicious command., Test validate_command_format returns False for too long command. (+87 more)

### Community 869 - "2026_02_26_add_arena_zone_type.py"
Cohesion: 0.40
Nodes (4): downgrade(), Allow zone_type 'arena' in zones CHECK., Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)., upgrade()

### Community 870 - "rename_players_to_population.py"
Cohesion: 0.40
Nodes (4): downgrade(), Rename columns from min_players/max_players to min_population/max_population., Revert column names back to min_players/max_players., upgrade()

### Community 871 - "CorpseServiceError"
Cohesion: 0.25
Nodes (8): CorpseNotFoundError, CorpseServiceError, Base exception for corpse service operations., Raised when a corpse container is not found., Test CorpseServiceError exception., Test CorpseNotFoundError exception., test_corpse_not_found_error(), test_corpse_service_error()

### Community 872 - "DomainError"
Cohesion: 0.40
Nodes (4): DomainError, Exception, Domain-specific exceptions for MythosMUD. These exceptions represent business…, Base exception for all domain errors.

### Community 875 - "mock_connection_manager"
Cohesion: 0.25
Nodes (8): mock_connection_manager(), mock_room(), mock_websocket(), _passthrough_room_data(), fixture, Return room data unchanged for convert_room_players_uuids_to_names mocks., Create a mock WebSocket., Create a mock connection manager.

### Community 876 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 877 - "CircuitBreakerOpen"
Cohesion: 0.09
Nodes (17): CircuitBreakerOpen, Any, Exception, Handle successful function call. Updates state based on current circuit state:…, Handle failed function call. Updates state based on failure count: - Increments…, Check if enough time has passed to attempt circuit reset. Returns: True if…, Calculate seconds until circuit can attempt reset. Returns: Seconds until retry…, Transition circuit to new state. Args: new_state: State to transition to AI:… (+9 more)

### Community 878 - "8. Error Handling and Debugging"
Cohesion: 0.67
Nodes (3): 8. Error Handling and Debugging, Common Debug Commands, Test Debugging

### Community 879 - "UUID"
Cohesion: 0.17
Nodes (8): UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return True if websocket appears dead (should be cleaned up)., Return list of player IDs to check (single player or all)., Clean up dead connections for a single player., Clean up dead connections for a specific player or all players. Args:…

### Community 880 - "Real-Time Architecture"
Cohesion: 0.33
Nodes (6): Real-Time Architecture, WebSocket and NATS Realtime Stack, ConnectionManager Modular Split, ConnectionManager Refactoring Summary, Structured Concurrency Patterns, Structured Concurrency Task Tracking

### Community 882 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 883 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 884 - ".validate_timestamp"
Cohesion: 0.29
Nodes (4): field_validator, Validate timestamp is valid ISO format., Validate channel is a known chat channel., Validate event type is not empty.

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
Cohesion: 0.12
Nodes (11): Infrastructure layer for MythosMUD. This package contains abstractions for…, MessageBroker, Any, Protocol, Send a request and wait for a reply (request-reply pattern). Args: subject:…, Protocol defining the message broker interface. This abstract interface allows…, Connect to the message broker. Returns: bool: True if connection successful,…, Disconnect from the message broker. Closes all subscriptions and releases… (+3 more)

### Community 891 - "7. Common Test Failure Solutions"
Cohesion: 0.50
Nodes (4): 7. Common Test Failure Solutions, Authentication Test Issues, Database Connection Issues, WebSocket Test Issues

### Community 892 - "PostgresCursor"
Cohesion: 0.13
Nodes (11): PostgresCursor, cursor, PostgreSQL cursor wrapper for query result access., Test PostgresCursor class., Test PostgresCursor initialization., Test PostgresCursor.fetchone() with row., Test PostgresCursor.fetchone() with None., Test PostgresCursor.fetchall() with rows. (+3 more)

### Community 893 - ".get_room_occupants"
Cohesion: 0.33
Nodes (4): Any, UUID, Separate occupants into players, NPCs, and all occupants lists. Args:…, Get the list of occupants in a room. Args: room_id: The room ID…

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

### Community 903 - "_make_mock_row"
Cohesion: 0.13
Nodes (15): _make_mock_row(), UUID, Test get_player_by_name successfully retrieves player., Test list_players successfully retrieves players., Create a mock procedure result row for row_to_player., Test get_player_by_id successfully retrieves player., Test get_players_by_user_id successfully retrieves players., Test get_active_players_by_user_id successfully retrieves active players. (+7 more)

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

### Community 910 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test _broadcast_by_channel_type handles exceptions., Test _send_messages_to_players handles missing original_content., Test _send_messages_to_players adds tags from dampening., Test _send_messages_to_players handles invalid player_id., Test _apply_dampening_and_send_message handles blocked messages., Test _apply_dampening_and_send_message handles missing original_content., Test _get_player_lucidity_tier handles exceptions during processing. (+7 more)

### Community 911 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 912 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 913 - "test_initiate_shutdown_countdown_success"
Cohesion: 0.40
Nodes (6): _InitiateAppStub, _InitiateStateStub, Test initiate_shutdown_countdown() successfully initiates shutdown., Test initiate_shutdown_countdown() cancels existing shutdown., test_initiate_shutdown_countdown_success(), test_initiate_shutdown_countdown_supersedes()

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

### Community 920 - "SpellMaterialsService"
Cohesion: 0.19
Nodes (10): Any, UUID, Spell material handling service. This module handles checking and consuming…, Build final inventory with consumed materials removed. Args: inventory:…, Consume spell materials from player inventory. Args: player_id: Player ID…, Service for handling spell material requirements. Handles checking if players…, Check if player has all required materials. Args: player_id: Player ID spell:…, Process a single material requirement. Args: material: Material requirement… (+2 more)

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

### Community 938 - "DeadLetterQueue"
Cohesion: 0.14
Nodes (13): DeadLetterQueue, Clean up old DLQ messages. Args: max_age_days: Maximum age of messages to keep…, Store messages that fail after all retries. Implements file-based storage for…, Test DeadLetterQueue initialization without storage directory., Test dequeue() handles file read errors., Test get_statistics() returns stats with messages., Test list_messages() returns empty list when queue is empty., Test cleanup_old_messages() handles file errors. (+5 more)

### Community 939 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 941 - "test_player_service.py"
Cohesion: 0.09
Nodes (21): Unit tests for player service. Tests the PlayerService class., Test get_player_by_id() when player is not found., Test get_player_by_name() when player is found., Test create_player_with_stats() when character limit is reached., Test validate_player_name() when name already exists., Test search_players_by_name() returns matching players., Test apply_lucidity_loss() applies lucidity loss., Test gain_occult_knowledge() increases occult knowledge. (+13 more)

### Community 942 - "type"
Cohesion: 0.40
Nodes (5): integer, minimum, type, null, durability

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

### Community 948 - "ConnectionErrorHandler"
Cohesion: 0.18
Nodes (12): ConnectionErrorHandler, Any, UUID, Handle WebSocket-specific errors. Args: player_id: The player's ID…, Handle authentication-related errors. Args: player_id: The player's ID…, Handle security violations. Args: player_id: The player's ID violation_type:…, Attempt to recover from an error state for a player. Args: player_id: The…, Get error handling statistics. Args: online_players: Online players dictionary… (+4 more)

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

### Community 961 - ".is_active"
Cohesion: 0.40
Nodes (3): Check if the status effect is still active., Any, Initialize Invite with defaults.

### Community 962 - "NpcCombatServiceProtocol"
Cohesion: 0.40
Nodes (4): NpcCombatServiceProtocol, Protocol, Typed surface for npc_combat_service.handle_npc_attack_on_player., Handle an NPC attack against a player via the main combat service.

### Community 963 - "_EventBusPublishPort"
Cohesion: 0.40
Nodes (4): _EventBusPublishPort, Protocol, Minimal surface for publishing domain events from ConnectionManager.event_bus., Publish a single event to the in-process bus.

### Community 964 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 965 - "test_filter_other_players_adds_linkdead_indicator"
Cohesion: 0.40
Nodes (5): asyncio, Test _filter_other_players() adds (linkdead) indicator for grace period players., Test _filter_other_players() does not add (linkdead) when player not in grace…, test_filter_other_players_adds_linkdead_indicator(), test_filter_other_players_no_linkdead_when_not_in_grace_period()

### Community 966 - "MutableHeaders"
Cohesion: 0.15
Nodes (12): MutableHeaders, Add all security headers to the response., Test _add_security_headers adds all security headers., Test _add_security_headers sets correct HSTS value., Test _add_security_headers includes Permissions-Policy., Test _add_security_headers uses configured CSP policy., Test _add_security_headers uses configured referrer policy., test_add_security_headers() (+4 more)

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

### Community 977 - "TestGlobalFunctions"
Cohesion: 0.17
Nodes (7): Test suite for global convenience functions., Test get_feature_flags returns the global service instance., Test global is_combat_enabled function., Test global is_combat_logging_enabled function., Test global is_combat_monitoring_enabled function., Test refresh_feature_flags clears cache., TestGlobalFunctions

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

### Community 995 - "test_help_commands.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for help command handlers. Tests the help command functionality., Test handle_help_command() returns general help when no topic., Test handle_help_command() returns help for specific topic., Test handle_help_command() handles unknown topic., test_handle_help_command_no_topic(), test_handle_help_command_unknown_topic(), test_handle_help_command_with_topic()

### Community 997 - "corpse_service"
Cohesion: 0.40
Nodes (5): corpse_service(), mock_persistence(), fixture, Create a mock persistence layer., Create a CorpseLifecycleService instance.

### Community 998 - "Any"
Cohesion: 0.18
Nodes (6): Any, Retrieve and remove oldest message from DLQ (async version). Returns: Message…, Retrieve and remove oldest message from DLQ (sync version). Returns: Message…, Get DLQ statistics. Returns: Dictionary with DLQ metrics AI: For monitoring…, List messages in DLQ without removing them. Args: limit: Maximum number of…, Convert message to dictionary for JSON serialization.

### Community 999 - "plane"
Cohesion: 0.67
Nodes (3): minLength, type, plane

### Community 1000 - "AI Development Workflow"
Cohesion: 0.67
Nodes (3): AI Command Development Workflow, Cursor AI Tooling, AI Development Workflow

### Community 1001 - "Architecture Overview"
Cohesion: 0.67
Nodes (3): Architecture Overview, CircuitBreaker States, Integration Points

### Community 1002 - "Path"
Cohesion: 0.18
Nodes (6): Path, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve message for replay and remove from DLQ. Args: filepath: Path to DLQ…, Delete a message from DLQ without processing. Args: filepath: Path to DLQ file…, Initialize dead letter queue. Args: storage_dir: Optional directory to store…

### Community 1003 - "test_skills.py"
Cohesion: 0.13
Nodes (19): get_skills_catalog(), get, Request, Return the skills catalog (base values, allow_at_creation). Cthulhu Mythos is…, mock_request(), mock_skill_repository(), mock_user(), asyncio (+11 more)

### Community 1004 - "Cursor Skills Skill"
Cohesion: 0.13
Nodes (16): Tailwind CSS Anti-Pattern Remediation, Adapt Skill, Animate Skill, Arrange Skill, Audit Skill, Bolder Skill, Clarify Skill, Colorize Skill (+8 more)

### Community 1005 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1007 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test broadcast_player_entered_message() skips when room_id is None., Test send_room_update_to_player() successfully sends room update., Test query_room_occupants_snapshot() queries occupants., Test log_player_movement() skips when connection manager not available., Test log_player_movement() handles errors., test_broadcast_player_entered_message_no_room_id(), test_log_player_movement_error_handling() (+3 more)

### Community 1008 - "handle_explore_command"
Cohesion: 0.27
Nodes (9): handle_explore_command(), Any, Handle exploration requests by returning a simple message. This lightweight…, asyncio, Unit tests for exploration command handlers. Tests the exploration command…, Test handle_explore_command() explores area., Test handle_explore_command() handles missing persistence., test_handle_explore_command() (+1 more)

### Community 1009 - ".check_and_cleanup"
Cohesion: 0.20
Nodes (6): Return connection IDs that exceed max_connection_age., Clean up orphaned data that might accumulate over time. Args:…, Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops., Force immediate cleanup of all orphaned data. Args: cleanup_stats: Cleanup…, Periodically check for cleanup conditions and perform cleanup if needed. Args:…, _stale_prune_max_age_seconds()

### Community 1010 - "wearable_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), fixture, Create mock persistence layer., Create WearableContainerService instance., wearable_service()

### Community 1011 - "test_room_subscription_manager.py"
Cohesion: 0.20
Nodes (9): Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test add_room_occupant() adds occupant to existing room., Test add_room_occupant() handles errors gracefully., Test remove_room_occupant() handles errors gracefully., Test unsubscribe_from_room() removes room when last subscriber leaves., test_add_room_occupant_error_handling(), test_add_room_occupant_existing_room(), test_remove_room_occupant_error_handling() (+1 more)

### Community 1012 - "fix_markdown_file"
Cohesion: 0.36
Nodes (8): fix_markdown_file(), fix_multiple_blanks(), main(), parse_markdownlint_output(), Path, Fix multiple consecutive blank lines (MD012). Returns: (new_content,…, Parse markdownlint output to get files with MD012 issues., Fix multiple blank lines in a single markdown file. Returns: (changed,…

### Community 1015 - "Analyze Coverage Gaps"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and…, Write critical files below threshold section. (+7 more)

### Community 1016 - "Apply Arena Seed"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 1019 - "webhook"
Cohesion: 0.50
Nodes (4): post, Request, Receive and log alert webhooks, webhook()

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

### Community 1041 - "asyncio"
Cohesion: 0.22
Nodes (9): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success(), test_request_party_invite_creates_pending() (+1 more)

### Community 1042 - "fixture"
Cohesion: 0.22
Nodes (9): mock_persistence(), mock_room_cache(), fixture, Create a mock persistence layer., Create a mock room cache service., Create a RoomService instance with cache., Create a sample room dictionary., room_service_with_cache() (+1 more)

### Community 1050 - "asyncio"
Cohesion: 0.22
Nodes (9): asyncio, Test cleanup_orphaned_data() cleans up orphaned data., Test cleanup_dead_connections() cleans up dead connections., Test force_cleanup() performs forced cleanup., Test check_and_cleanup() performs cleanup check., test_check_and_cleanup(), test_cleanup_dead_connections(), test_cleanup_orphaned_data() (+1 more)

### Community 1051 - "test_damage_grace_period.py"
Cohesion: 0.11
Nodes (23): mock_combat(), mock_combat_service(), mock_connection_manager(), player_participant(), asyncio, fixture, Unit tests for damage blocking during login grace period. Tests that damage and…, Test that damage application fails open if grace period check errors. (+15 more)

### Community 1052 - "Security Infrastructure"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters). Args:…, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 1054 - "preferences_service"
Cohesion: 0.22
Nodes (9): mock_session(), preferences_service(), fixture, Create a PlayerPreferencesService instance., Create a mock async session., Create a sample player ID., Create sample player preferences., sample_player_id() (+1 more)

### Community 1056 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1058 - "description"
Cohesion: 0.67
Nodes (3): minLength, type, description

### Community 1065 - ".from_dict"
Cohesion: 0.25
Nodes (7): Reconstruct message from dictionary., Test DeadLetterMessage.from_dict() reconstructs message., Test DeadLetterMessage.from_dict() handles string timestamp., Test DeadLetterMessage.from_dict() handles datetime timestamp., test_dead_letter_message_from_dict(), test_dead_letter_message_from_dict_datetime_timestamp(), test_dead_letter_message_from_dict_string_timestamp()

### Community 1066 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 1067 - "test_error_logging.py"
Cohesion: 0.25
Nodes (7): Unit tests for error_logging utilities. Tests error logging helper functions., Test create_error_context() creates error context., Test create_error_context() can include metadata., Test error context to_dict() method., test_create_error_context(), test_create_error_context_with_metadata(), test_error_context_to_dict()

### Community 1069 - "monitoring_service"
Cohesion: 0.25
Nodes (8): mock_combat_config(), mock_config(), mock_feature_flags(), monitoring_service(), fixture, Create mock feature flags., Create mock combat config., Create CombatMonitoringService instance with mocked dependencies.

### Community 1070 - "_get_death_location_name"
Cohesion: 0.67
Nodes (3): _get_death_location_name(), Room, Extract death location name from room object or dict.

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
Nodes (6): PrototypeRegistryError, Exception, Get a prototype by ID. Args: prototype_id: The ID of the prototype to retrieve…, Raised when prototype registry lookups fail., When registry.get raises PrototypeRegistryError, returns None., test_resolve_weapon_attack_from_equipped_registry_error_returns_none()

### Community 1076 - "load_motd"
Cohesion: 0.23
Nodes (11): Unit tests for motd_loader utilities. Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+3 more)

### Community 1085 - "test_npc_event_handlers.py"
Cohesion: 0.03
Nodes (79): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers. Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON. (+71 more)

### Community 1086 - "fixture"
Cohesion: 0.29
Nodes (4): fixture, Create a mock psycopg2 connection., Create a mock psycopg2 cursor., Create a mock psycopg2 cursor.

### Community 1087 - "AGENTS.md agent instructions"
Cohesion: 0.08
Nodes (24): AGENTS.md agent instructions, COPPA compliance requirements, Obsidian LLM wiki permanent memory, One server only rule, PostgreSQL procedures/functions access, Server authority rule, CLAUDE.md agent router, Contributor Covenant Code of Conduct (+16 more)

### Community 1089 - "Architecture Decisions Adr"
Cohesion: 0.20
Nodes (10): ADR-013 Pydantic BaseSettings Configuration, ADR-014 NATS Circuit Breaker and DLQ, Dead Letter Queue, db/procedures Stored Functions, ADR-015 PostgreSQL Procedures Migration, ADR-016 Aggro Threat Management, Room-Based Combat Aggro, ADR-017 AST Console Pruning (+2 more)

### Community 1090 - "Fixture Optimization Complete"
Cohesion: 0.67
Nodes (3): E2E Testing Setup Status, Fixture Optimization Complete, Test Suite Post-Merge Refactoring

### Community 1093 - "Check No Production"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 1095 - "overrides"
Cohesion: 0.11
Nodes (18): overrides, @asyncapi/generator, @asyncapi/generator-components, @asyncapi/generator-helpers, @asyncapi/specs, fast-uri, flatted, glob (+10 more)

### Community 1097 - "Phase 2: Categorize and Prioritize Lint Issues"
Cohesion: 0.40
Nodes (5): 🔴 CRITICAL (Fix First - Blocking Issues), 🟡 HIGH PRIORITY (Fix Second - Core Functionality), 🔵 LOW PRIORITY (Fix Last - Polish), 🟢 MEDIUM PRIORITY (Fix Third - Enhancement), Phase 2: Categorize and Prioritize Lint Issues

### Community 1098 - "Cursor Workflows"
Cohesion: 0.22
Nodes (9): Cursor Agent CLI, Cursor CLI, Cursor Hooks, Cursor Lifecycle Hooks, Cursor Setup Guide, Cursor Subagents, Built-in Explore Bash Browser Subagents, Cursor Workflows (+1 more)

### Community 1099 - "database"
Cohesion: 0.33
Nodes (4): database, Simulate database operations., Simulate database execute., Simulate user creation.

### Community 1100 - "process_item"
Cohesion: 0.33
Nodes (6): migration_example_10(), migration_example_14(), process_item(), Example 10: Batch processing logging migration., Example 14: Logging in loops migration., Simulate item processing.

### Community 1101 - "SQLAlchemy Async Best Practices"
Cohesion: 1.00
Nodes (3): SQLAlchemy Async Best Practices, SQLAlchemy text() Async Usage, SQLAlchemy Code Review

### Community 1102 - "E 2 E Load Analyze"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 1103 - "risky_operation"
Cohesion: 0.33
Nodes (6): migration_example_11(), migration_example_3(), Example 11: Exception tracking migration., Simulate a risky operation., Example 3: Error logging migration., risky_operation()

### Community 1104 - "process_batch"
Cohesion: 0.33
Nodes (6): process_batch(), process_item(), Test batch operation logging., Simulate batch processing., Simulate item processing., test_batch_logging()

### Community 1111 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1116 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1117 - "WebSocket"
Cohesion: 0.33
Nodes (4): Test WebSocket logging in integration tests., Simulate WebSocket connection., test_websocket_logging(), WebSocket

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

### Community 1125 - "📊 LINT ISSUE CATEGORIZATION GUIDE"
Cohesion: 0.67
Nodes (3): 📊 LINT ISSUE CATEGORIZATION GUIDE, Python/Ruff Error Codes, React/ESLint Error Codes

### Community 1135 - "persistence_handler"
Cohesion: 0.33
Nodes (6): mock_combat_service(), mock_player(), persistence_handler(), fixture, Create mock combat service., Create CombatPersistenceHandler instance.

### Community 1140 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1141 - "test_nats_service_init_with_subject_manager"
Cohesion: 0.20
Nodes (6): Test NATSService initialization with None config., Test NATSService initialization with subject manager., Test NATSService initializes message batching structures., test_nats_service_init_message_batch(), test_nats_service_init_with_none(), test_nats_service_init_with_subject_manager()

### Community 1144 - "test_async_logging"
Cohesion: 0.40
Nodes (5): async_operation(), asyncio, Test logging in async functions., Simulate async operation., test_async_logging()

### Community 1145 - "Knip Entry Ignore Dependencies"
Cohesion: 0.08
Nodes (25): entry, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries, dependencies (+17 more)

### Community 1146 - "dependencies"
Cohesion: 0.08
Nodes (25): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-resizable, react-rnd (+17 more)

### Community 1150 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test _ensure_room_cache_loaded returns early when cache is already loaded., Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…, Test _ensure_room_cache_loaded handles DatabaseError gracefully., Test _ensure_room_cache_loaded handles OSError gracefully., Test _ensure_room_cache_loaded handles RuntimeError gracefully., test_ensure_room_cache_loaded_already_loaded(), test_ensure_room_cache_loaded_concurrent_load() (+3 more)

### Community 1151 - "client"
Cohesion: 0.40
Nodes (3): client, Simulate client POST request., Simulate client GET request.

### Community 1152 - "LoggingMiddleware"
Cohesion: 0.40
Nodes (4): LoggingMiddleware, Test logging in middleware., Simulate middleware processing., test_middleware_logging()

### Community 1153 - "WebSocketRateLimiter"
Cohesion: 0.40
Nodes (3): WebSocket rate limiter with enhanced logging., Check if client is within rate limit with enhanced logging., WebSocketRateLimiter

### Community 1157 - "shutdown_process_termination.py"
Cohesion: 0.20
Nodes (10): _find_uvicorn_processes(), Any, Process termination utilities for graceful server shutdown. This module handles…, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available., _terminate_child_processes() (+2 more)

### Community 1159 - "Mythosmud Obsidian Sources"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1163 - "registry_with_switchblade"
Cohesion: 0.40
Nodes (5): fixture, Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade)., PrototypeRegistry containing only the switchblade., registry_with_switchblade(), switchblade_prototype()

### Community 1164 - "player_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), player_service(), fixture, Create a mock persistence layer., Create a PlayerService instance.

### Community 1165 - "nats_broker"
Cohesion: 0.40
Nodes (5): nats_broker(), nats_config(), fixture, Create a NATSConfig instance., Create a NATSMessageBroker instance.

### Community 1166 - "player_repository"
Cohesion: 0.40
Nodes (5): mock_player(), player_repository(), fixture, Create a PlayerRepository instance., Create a mock player for save operations.

### Community 1167 - "persistence_handler"
Cohesion: 0.40
Nodes (5): mock_combat_service(), persistence_handler(), fixture, Create mock combat service., Create CombatPersistenceHandler instance.

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

### Community 1177 - "1. Component Refactoring"
Cohesion: 0.50
Nodes (4): 1. Component Refactoring, ChatPanel.tsx Enhancements (New Chat Input Panel), CommandPanel.tsx Simplifications, GameLogPanel.tsx (Renamed from ChatPanel.tsx)

### Community 1178 - "CombatAuditLogger"
Cohesion: 0.05
Nodes (59): CombatAttackDetails, CombatAuditLogger, CombatMonitoringAlert, CombatParties, CombatSecurityEvent, Any, datetime, Combat-specific audit logging and monitoring. This module provides specialized… (+51 more)

### Community 1186 - "migration_example_4"
Cohesion: 0.50
Nodes (4): expensive_operation(), migration_example_4(), Simulate an expensive operation., Example 4: Performance logging migration.

### Community 1187 - "test_mp_regeneration_service.py"
Cohesion: 0.04
Nodes (63): mock_player(), mock_player_service(), mp_regeneration_service(), asyncio, fixture, Unit tests for MP regeneration service. Tests the MPRegenerationService class…, Test process_tick_regeneration() accumulates fractional MP., Test _get_regen_multiplier() returns 1.0 for standing position. (+55 more)

### Community 1188 - "risky_operation"
Cohesion: 0.50
Nodes (4): Test logging error handling., Simulate risky operation that raises exception., risky_operation(), test_logging_error_handling()

### Community 1190 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 1197 - "Mythosmud Obsidian Readme"
Cohesion: 0.50
Nodes (4): LLM Wiki Vault Schema, Raw Sources Layer, Wiki Layer, Wiki Page Template

### Community 1200 - "mock_lifecycle_manager"
Cohesion: 0.50
Nodes (4): mock_lifecycle_manager(), mock_npc(), fixture, Create a mock lifecycle manager.

### Community 1217 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test broadcast_combat_death broadcasts death event., Test broadcast_combat_ended broadcasts combat ended event., Test broadcast_player_respawn broadcasts respawn message., Test broadcast_combat_attack sends personal message to attacker., Test broadcast_player_death handles personal message errors., Test broadcast_combat_start broadcasts combat start event., test_broadcast_combat_attack_with_attacker_id() (+5 more)

### Community 1220 - "E 2 E Scenarios Scenario"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1223 - "Grype Command Handle Result"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1224 - "Visualize Arkham Rooms"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1228 - "Validate Codacy Coverage"
Cohesion: 0.23
Nodes (12): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., test_cobertura_root_line_rate_parses(), test_lcov_aggregate_and_gate() (+4 more)

### Community 1230 - "mock_app"
Cohesion: 0.67
Nodes (3): mock_app(), fixture, Create a mock ASGI app.

### Community 1231 - "subscription_manager"
Cohesion: 0.67
Nodes (3): fixture, Create a RoomSubscriptionManager instance., subscription_manager()

### Community 1233 - "Player"
Cohesion: 0.00
Nodes (879): Reset the global async persistence instance for testing. DEPRECATED: Use…, reset_async_persistence(), Channel management commands for Advanced Chat Channels. This module provides…, PlayerCreationService, Any, Stats, UUID, Player creation service. This module handles player character creation… (+871 more)

### Community 1234 - "subscription_manager"
Cohesion: 0.67
Nodes (3): fixture, Create a RoomSubscriptionManager instance., subscription_manager()

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

### Community 1276 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 1277 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, properties, field1, field2, field3, zone (+3 more)

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

### Community 1355 - "Check Asyncio Run"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1356 - "Lucidity Migration"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1359 - "test_alias_storage.py"
Cohesion: 0.03
Nodes (65): Unit tests for alias storage utilities. Tests the AliasStorage class for…, Test _load_alias_data handles IO errors gracefully., Test _save_alias_data successfully saves data., Test _save_alias_data handles IO errors., Test get_player_aliases returns empty list for player with no aliases., Test get_player_aliases returns aliases from file., Test get_player_aliases correctly parses timestamp strings., Test add_alias adds a new alias. (+57 more)

### Community 1381 - "Testing Map Regression"
Cohesion: 0.67
Nodes (3): ASCII Map Context Preparation, ASCII Minimap Generation, Map Regression Tests Proposal

### Community 1391 - "Package Engines Node"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 1392 - "include"
Cohesion: 0.10
Nodes (19): compilerOptions, allowImportingTsExtensions, composite, noEmit, types, exclude, extends, include (+11 more)

### Community 1393 - "Vite Config Proxyauthorization"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1396 - "Cursor Hooks Trigger"
Cohesion: 0.31
Nodes (8): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Entry point: read hook payload from stdin, check edited-files state, and…

### Community 1414 - "Cursor Skills Mythosmud"
Cohesion: 0.67
Nodes (3): MythosMUD Server Runbook Skill, MythosMUD Worktree Workflow Skill, One Server Only Rule

### Community 1415 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 1422 - "Room Validator Toolkit"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1423 - "Room Toolkit Validator"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1426 - "Filter Static Dml"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after…, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1427 - "Fix Room References"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area. Args: base_path: Path to the…, save_room_file()

### Community 1428 - "Player Inventory Migration"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1430 - "Run Bug Prevention"
Cohesion: 0.53
Nodes (8): Invoke-ClientTest(), Invoke-IntegrationTest(), Invoke-ServerTest(), Show-TestSummary(), Test-Command(), Write-ColorOutput(), Write-Header(), Write-Section()

### Community 1433 - "test_logging_handlers.py"
Cohesion: 0.04
Nodes (69): _aggregator_formatter(), _aggregator_handler_class_for_windows(), create_aggregator_handler(), _make_exec_for_aggregator(), _open_aggregator_handler(), Any, Formatter, LogRecord (+61 more)

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

### Community 1561 - "Schemas Intersection Schema"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

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

### Community 1643 - "E 2 E Reset Players"
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

### Community 1744 - "TestPostgresConnectionPool"
Cohesion: 0.11
Nodes (17): is_postgres_url(), PostgresConnectionPool, Thread-safe PostgreSQL connection pool., Get or create a connection pool for the given database URL., Get a connection from the pool., Check if the database URL is PostgreSQL., patch, Test PostgresConnectionPool class. (+9 more)

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
- **3038 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `@codacy/codacy-mcp`, `@playwright/mcp` (+3033 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **599 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `MovementService`, `GameBundle`, `websocket_initial_state.py`, `User`, `is_player_in_login_grace_period`, `MythosMUDError`, `TargetMatch`, `ErrorType`, `player_connection_setup.py`, `ContainerServiceError`, `players/__init__.py`, `NPCCombatIntegrationService`, `PrototypeRegistry`, `BaseCommand`, `connection_manager.py`, `test_look_container.py`, `server/tests/conftest.py`, `api/monitoring.py`, `test_look_npc.py`, `optimized_security_validator.py`, `inventory_commands.py`, `debrief_command.py`, `Room`, `lifecycle_periodic.py`, `server/dependencies.py`, `ContainerComponent`, `PlayerCombatService`, `lifespan_startup.py`, `server/schemas/__init__.py`, `get_username_from_user`, `CombatParticipant`, `test_container_websocket_events.py`, `.get_instance`, `PartyService`, `CombatParticipantData`, `BaseEvent`, `who_commands.py`, `CombatAttackHandler`, `magic_service_completion.py`, `test_quest_instance_repository.py`, `test_connection_establishment.py`, `connection_manager_health_cleanup.py`, `_find_item_in_equipped`, `chat_nats_publisher.py`, `time.py`, `get_npc_instance_service`, `test_status_commands.py`, `Any`, `test_look_room.py`, `combat_service.py`, `NATSMessageBroker`, `CoordinateValidator`, `test_lucidity_recovery_commands.py`, `LoggedHTTPException`, `RealTimeEventHandler`, `test_player_presence_tracker.py`, `test_metrics_endpoints.py`, `CircuitBreaker`, `PlayerEnteredRoom`, `test_look_player.py`, `item_factory.py`, `OccupantFormatter`, `test_combat_monitoring_service.py`, `test_lucidity_event_dispatcher.py`, `spell_effects.py`, `LucidityService`, `test_exceptions.py`, `.__post_init__`, `shutdown_process_termination.py`, `migrate_combat_data.py`, `WebSocketMessageValidator`, `api/character_creation.py`, `catatonia_check.py`, `ScheduleService`, `test_rest_command.py`, `persist_player`, `AliasStorage`, `Spell`, `websocket_helpers.py`, `CombatAuditLogger`, `EventBus`, `.state`, `party_commands.py`, `skills_commands.py`, `CombatConfiguration`, `chat_message_senders.py`, `inventory_equip_command.py`, `maps.py`, `fixtures/integration/__init__.py`, `CatatoniaRegistry`, `admin_shutdown_command.py`, `QuestService`, `quest_commands.py`, `CorpseLifecycleService`, `IdleMovementHandler`, `test_map_helpers.py`, `test_inventory_helpers.py`, `server/models/game.py`, `MonitoringDashboard`, `threading.py`, `Player`, `test_connection_session_management.py`, `HolidayService`, `magic_service.py`, `ChatModeration`, `resolve_weapon_attack_from_equipped`, `rescue_service.py`, `chat_service.py`, `communication_commands_flows.py`, `error_handling_middleware.py`, `container_endpoints_basic.py`, `player_combat_service.py`, `get_help_content`, `PlayerNameExtractor`, `test_player_occupant_processor.py`, `server/exceptions.py`, `game_tick_processing.py`, `alias_storage.py`, `FeatureFlagService`, `AsciiMapRenderer`, `spell_effects_status.py`, `test_health_service.py`, `lifespan_shutdown.py`, `handle_read_command`, `go_command.py`, `NPCMovementIntegration`, `lifespan.py`, `format_metadata`, `Npc Lifecycle Respawn`, `test_spell.py`, `RoomService`, `send_game_event`, `websocket_handler_commands.py`, `Lucidity Migration`, `look_command.py`, `rest_countdown_task.py`, `hallucinations.py`, `player_effect_repository.py`, `combat_attack.py`, `container_persistence/container_persistence.py`, `MovementMonitor`, `admin_setlucidity_command.py`, `rate_overrides.py`, `command_handler_unified.py`, `bundles/game.py`, `shutdown_sequence.py`, `subject_controller.py`, `real_time.py`, `retry.py`, `TaskRegistry`, `inventory_pickup_command.py`, `Player Inventory Migration`, `LRUCache`, `SpellMaterialsService`, `ValidationError`, `NATSConnectionStateMachine`, `teach_command.py`, `api/player_respawn.py`, `logout_commands.py`, `channel_broadcasting_strategies.py`, `PlayerService`, `factory.py`, `websocket_handler.py`, `ApplicationContainer`, `zone_config_loader.py`, `inventory_command_helpers.py`, `handle_emote_command`, `NPCEventHandler`, `fastapi_integration.py`, `test_occupants.py`, `apply_communication_dampening`?**
  _High betweenness centrality (0.186) - this node is a cross-community bridge._
- **Why does `SchemaValidator` connect `ValidationError` to `PathValidator`, `alias_storage.py`, `Player`, `AliasStorage`, `SchemaValidator`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Why does `AliasStorage` connect `AliasStorage` to `server/exceptions.py`, `test_alias_commands.py`, `alias_storage.py`, `CommandRequest`, `.get_player_aliases`, `inventory_pickup_command.py`, `ContainerServiceError`, `test_rest_command.py`, `persist_player`, `test_admin_shutdown_command.py`, `TestHelperFunctions`, `alias_storage`, `ValidationError`, `inventory_commands.py`, `debrief_command.py`, `.state`, `party_commands.py`, `handle_read_command`, `skills_commands.py`, `PlayerCombatService`, `go_command.py`, `inventory_equip_command.py`, `teach_command.py`, `_asyncio_mark`, `handle_channel_command`, `get_username_from_user`, `get_logger`, `CommandService`, `admin_shutdown_command.py`, `logout_commands.py`, `handle_quest_command`, `quest_commands.py`, `_handle_admin_set_stat_command`, `PlayerPositionService`, `CombatService`, `websocket_handler_commands.py`, `look_command.py`, `test_alias_storage.py`, `combat_loader.py`, `Player`, `handle_system_command`, `handle_time_command`, `test_status_commands.py`, `test_alias_storage_creates_directory`, `test_lucidity_recovery_commands.py`, `test_magic_commands.py`, `magic_service.py`, `admin_setlucidity_command.py`, `inventory_command_helpers.py`, `handle_emote_command`, `handle_explore_command`, `command_handler_unified.py`, `test_occupants.py`, `handle_whisper_command`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 51 inferred relationships involving `LoggedHTTPException` (e.g. with `_AppStateWithLegacyConfig` and `_AppWithLegacyConfigState`) actually correct?**
  _`LoggedHTTPException` has 51 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `AliasStorage` (e.g. with `SchemaValidator` and `CommandRequest`) actually correct?**
  _`AliasStorage` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 42 inferred relationships involving `CombatService` (e.g. with `_FleeCommandHandlerLike` and `_PlayerForFlee`) actually correct?**
  _`CombatService` has 42 INFERRED edges - model-reasoned connections that need verification._