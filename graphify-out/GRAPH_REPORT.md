# Graph Report - MythosMUD  (2026-08-31)

## Corpus Check
- 3250 files · ~2,938,220 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 54430 nodes · 102187 edges · 2246 communities (1696 shown, 550 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 5830 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a3a96497`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- NPCCombatIntegrationService
- LucidityService
- PlayerRoomEventHandler
- NPCBase
- npc_database.py
- get_logger
- BaseCommand
- server/dependencies.py
- CommunicationCommandFactory
- ContainerComponent
- PlayerService
- TransferContainerRequest
- NPCDefinition
- CombatParticipant
- ConnectionManager
- sqlalchemy.md
- get_npc_instance_service
- test_security_validator.py
- MessageFilteringHelper
- ContainerData
- mythos_dev_ddl.sql
- Alias
- CombatService
- AsyncPersistenceLayer
- CommandFactory
- test_npc_utils.py
- LootAllRequest
- api/character_creation.py
- TargetMatch
- PlayerNameExtractor
- mock_lifecycle_manager
- ContainerServiceError
- test_container_bundles.py
- test_connection_session_management.py
- test_command_parser.py
- test_rest_command.py
- test_exploration_service.py
- test_connection_establishment.py
- NATSService
- ChatService
- ui-v2/types.ts
- factory.py
- FollowService
- server/models/game.py
- PlayerEnteredRoom
- test_inventory_helpers.py
- Communities (355 total, 223 thin omitted)
- inventory_equip_command.py
- server/exceptions.py
- TargetResolutionService
- handle_whisper_command
- is_player_in_login_grace_period
- test_connection_delegates.py
- ZoneConfiguration
- chat_service.py
- StandardizedErrorResponse
- MPRegenerationService
- SpellEffectType
- server/schemas/__init__.py
- command_handler_unified.py
- test_nats_message_handler.py
- config/models/__init__.py
- test_rescue_service.py
- admin_shutdown_command.py
- test_user_manager.py
- test_go_command.py
- UtilityCommandFactory
- test_users.py
- test_combat_flee_handler.py
- NATSError
- test_command_validator.py
- RoomLoader
- communication_commands_flows.py
- test_look_container.py
- test_player_respawn_service.py
- GameClientV2.tsx
- PopulationStats
- ApplicationContainer
- test_admin_commands.py
- test_combat_persistence_handler_events.py
- NATSConnectionStateMachine
- test_command_processor.py
- item_instance_persistence.py
- test_who_commands.py
- ExplorationService
- look_helpers.py
- ExplorationCommandFactory
- test_lucidity_event_dispatcher.py
- Any
- test_websocket_initial_state.py
- test_nats_service_pool.py
- sample_container
- ConnectionManager
- test_chat_npc_system.py
- api/player_effects.py
- catatonia_check.py
- CombatInstance
- test_auth_utils.py
- test_room_sync_service.py
- EventBus
- player_event_handlers_state.py
- admin_teleport_commands.py
- test_manager.py
- DistributedEventBus
- test_corpse_lifecycle_service.py
- test_combat_monitoring_service.py
- test_lifespan_startup.py
- get_session_maker
- InventoryService
- Stats
- test_room_renderer.py
- test_container_helpers_inventory_find.py
- test_websocket_room_updates.py
- test_real_time_helpers.py
- test_container_helpers_inventory_ops.py
- QuestService
- api/monitoring.py
- test_npc_models.py
- test_player_presence_tracker.py
- test_logging_utilities.py
- test_look_player.py
- UserManager
- EventHandler
- FeatureFlagService
- Reporter
- resolve_lazy_attr
- test_player_death_service.py
- test_connection_helpers_impl.py
- test_alias_commands.py
- test_character_creation_service.py
- test_quest_service.py
- DataProviderProtocol
- PlayerCombatService
- useMythosAppActions.ts
- mythos_e2e_ddl.sql
- test_metrics_endpoints.py
- test_status_commands.py
- mythos_unit_ddl.sql
- connection_manager_methods.py
- WebSocketMessageValidator
- test_magic_commands.py
- test_npc_service.py
- SchemaValidator
- ChatMessage
- manual_dependency_analysis.py
- ErrorType
- GameStateProvider
- format_message_content
- DeadLetterQueue
- test_websocket_handler_validation_errors.py
- admin_setstat_command.py
- migrate_combat_data.py
- pytest.md
- test_websocket_handler_app_state_connection.py
- websocket_handler_commands.py
- TaskRegistry
- talk_command.py
- NPCOccupantProcessor
- CombatConfiguration
- test_game_state_provider.py
- test_npc_event_handlers.py
- PlayerEventHandlerUtils
- lifespan_startup.py
- _parse_env_list
- room_service.py
- test_zone_config_loader.py
- test_lucidity_recovery_commands.py
- test_player_event_handlers_room_left.py
- NATSSubjectManager
- test_message_handlers.py
- test_admin_setlucidity_command.py
- test_combat_flee_helpers.py
- test_shutdown_sequence.py
- OccupantFormatter
- event_types.py
- server/services/__init__.py
- ValidationError
- test_party_service.py
- PlayerRespawnService
- test_nats_message_handler_chat.py
- waitForMessage
- test_logging_handlers.py
- NPCMovementIntegration
- IdleMovementHandler
- PassiveMobNPC
- test_player_disconnect_handlers.py
- middleware
- InventoryMutationGuard
- AppConfig
- test_communication_commands_flows.py
- test_connection_cleaner.py
- CombatAuditLogger
- test_wearable_container_service.py
- MemoryProfiler
- system_monitoring.py
- useGameClientV2Container.ts
- ContainerService
- websocket_handler.py
- logging_file_setup.py
- MovementService
- Room
- test_health_monitor.py
- test_player_event_handlers_room.py
- PlayerStateCommandFactory
- test_websocket_handler_coverage_gaps.py
- RoomEventHandler
- command_result_text
- ._calculate_percentile
- LogAggregator
- _is_predefined_emote
- ChatHistoryPanel.tsx
- Async Remediation Summary - December 3, 2025
- .state
- test_chat_validator.py
- PerformanceMonitor
- NPCCombatIntegration
- test_invite_schemas.py
- player.ts
- MonitoringDashboard
- websocket_helpers.py
- AliasStorage
- DatabaseError
- lifespan_protocols.py
- test_logout_commands.py
- test_aggressive_mob_npc.py
- CombatEventHandler
- build_event
- test_lifecycle_periodic.py
- test_error_handling_middleware.py
- _EventBusPublishPort
- CatatoniaRegistry
- GameClientV2Dock.test.tsx
- NPCCombatUUIDMapping
- InstanceManager
- CommandService
- .initialize
- validate_room_data
- _MagicServiceCore
- test_websocket_handler_json_error.py
- NATSMessageSubscriptionMixin
- security.ts
- RoomMapViewer.tsx
- fixtures/integration/__init__.py
- test_level_service.py
- InventorySchemaValidationError
- request_with_app_container
- test_websocket_messages.py
- ModerationCommandFactory
- devDependencies
- NATSMessageBroadcastMixin
- PlayerGuidFormatter
- eventHandlers/types.ts
- test_config_models.py
- handle_explore_command
- fixtures/auth.ts
- connection_establishment.py
- GameTickService
- useWebSocketConnection.ts
- testing_examples.py
- quality_fragmentation_ai_guardrails.py
- gen_arena_migration_sql.py
- PlayerStateEventHandler
- realtime/conftest.py
- CombatMonitoringService
- test_combat_service.py
- coerce_int
- systemHandlers.ts
- fastapi_integration.py
- ContainerLockState
- test_chat_nats_publisher.py
- NATSMetrics
- asyncio
- test_connection_establishment_ws.py
- test_look_room.py
- NPCCombatLucidity
- ExceptionTracker
- test_command_parser_helpers.py
- test_windows_safe_rotation.py
- test_communication_commands_channels.py
- PlayerPositionService
- utils/layout.ts
- MythosTimeEventConsumer
- MythosTickScheduler
- test_rate_overrides.py
- test_validation.py
- ResourceManager
- HealthStatus
- test_combat_handler.py
- error_logging.py
- MythosChronicle
- test_nats_service.py
- MemoryMonitor
- ✅ Phase 2 Async Persistence Migration - COMPLETE
- MythosMUD Test Suite Modernization Plan
- MemoryThresholdMonitor
- NPCCombatDataProvider
- validate_calendar.py
- CastingStateManager
- alias_schema.json
- test_party_commands.py
- PlayerDeathService
- TestRoomDataFixer
- PatternNotFoundError
- safe_run_static
- admin_summon_command.py
- test_inventory_display_helpers.py
- handle_read_command
- PlayerRepositoryProtocol
- AdminActionsLogger
- debrief_command.py
- test_nats_messages.py
- RoomMapEditorRuntime.tsx
- CoordinateGenerator
- SpellLearningService
- lucidity.py
- DialogueEditorPage.tsx
- game_tick_processing.py
- RoomDataValidator
- App.tsx
- Invite
- test_map_helpers.py
- test_pattern_matcher.py
- PlayerRespawnEventHandler
- test_player_occupant_processor.py
- verify_enhanced_logging_compliance.py
- projectorRoom.ts
- apiTypeGuards.ts
- mythos_mud_mapbuilder.py
- PrototypeRegistryError
- compare_linting_results.py
- .__post_init__
- PeriodicOrphanAuditor
- test_goto_helpers.py
- Any
- test_follow_commands.py
- collect_inventory.py
- test_shopkeeper_npc.py
- PydanticErrorHandler
- PlayerPreferencesService
- MemoryLeakMetricsCollector
- test_audit_logger.py
- Uplift Strategy
- Test Suite Optimization Roadmap
- Test Suite Refactoring Plan
- Test Value Distribution Chart
- LoggedHTTPException
- test_connection_statistics.py
- test_websocket_handler_core.py
- ScheduleCollection
- ChatLogger
- WebSocketRequestContext
- AsciiMapViewer.tsx
- revised-character-creation.spec.ts
- HealthService
- asyncio
- parse_shutdown_parameters
- test_npc_combat_handlers.py
- WebSocket Best Practices
- edgeModalLogic.ts
- vim Best Practices and Coding Standards
- Async Code Review - Post Phase 2 Migration
- FastAPI Code Review - Anti-Patterns and Best Practices
- E2E Test Suite AI Execution Improvements - Summary
- NPCCombatIntegrationBase
- DialogueDefinitionRepository
- ConnectionCleaner
- TestHierarchicalSchema
- service.py
- JsonMap
- properties
- properties
- properties
- log_and_raise_enhanced
- TrackedTaskManager
- test_admin_teleport_commands.py
- test_connection_disconnection_websockets.py
- SpellMaterialsService
- test_lint_raw_sql_in_python.py
- test_rest_and_grace_period.py
- retry.py
- TestCombatConfigurationService
- properties
- Any
- quest_commands.py
- NPCSpawnRule
- test_nats_service_health.py
- test_channel_commands.py
- test_quest_commands.py
- CORSConfig
- resolve_weapon_attack_from_equipped
- test_rate_limiter_utils.py
- MagicCommandHandler
- log_with_context
- TestEmitLootAllEvent
- 🧪 MythosMUD E2E Testing Strategy
- correct_patterns.py
- look_command.py
- test_game_tick_processing_async.py
- inventory_command_helpers.py
- player_connection_setup.py
- HolidayService
- StatsGenerator
- SubjectValidator
- Any
- test_message_broadcaster.py
- properties
- GameClientV2ContainerView.tsx
- Memory Leak Prevention System - Implementation Summary
- deprecated_patterns.py
- test_quality_fragmentation_guard.py
- NPCLifecycleRecord
- asyncio
- RoomCacheService
- transfer_all_items_from_container
- inventory_get_command.py
- ._cleanup_player_mutes
- _make_session_context
- disconnect_grace_period.py
- TestCombatMessagingService
- WebSocketRateLimiter
- follow_movement.py
- test_magic_service.py
- test_command_helpers_functions.py
- test_npc_event_handlers_helpers.py
- test_player_service.py
- test_room_subscription_manager_helpers.py
- test_admin_shutdown_command.py
- useRoomEditModal.ts
- multiplayer-browser-helpers.js
- Chat Panel Separation Implementation Tasks
- Async Persistence Migration Plan
- migration_examples.py
- test_game_tick_death.py
- MessageBroadcaster
- CombatCommandHandler
- generate_invites.py
- spell_effects_support.py
- test_connection_error_methods.py
- test_dependency_analysis.py
- AttributeError
- CombatCommandFactory
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)
- Phase 3, Task 3.2: NATS Subject Manager Usage Review
- Execution Steps
- properties
- properties
- ChatModeration
- EmoteService
- test_auth_rate_limit.py
- test_player_related_models.py
- PersonalMessageSender
- Any
- .load_room_data
- CharacterNameScreen.tsx
- required
- Async Persistence Migration Tracker
- PostgreSQL & SQL Audit Report
- LRUCache
- GameMechanicsService
- log_and_raise
- test_container_persistence_sql_injection.py
- TestNPCCombatRewards
- lint_optional_auth_no_guard.py
- 3. Common Patterns and Anti-patterns
- File-by-File Changes
- executeCommand
- enum
- AliasGraph
- test_npc_startup_service.py
- NPCThreadManager
- asyncio
- Stats
- test_player_preferences_service.py
- roomHandlers.ts
- authenticated.ts
- InventoryCommandFactory
- test_shutdown_process_termination.py
- ._build_player_attacked_event
- test_room_utils.py
- npc_config_parsing.py
- test_connection_event_helpers.py
- _make_session_context
- BehaviorEngine
- Test Pruning Candidates - Detailed List
- .get_upcoming_holidays
- FStringLoggingFixer
- Stop-MythosMudProjectProcessTree
- test_game_tick_processing.py
- test_chat_message_senders.py
- ItemPrototypeModel
- Any
- CombatMessagingService
- EventPublisher
- HolidayEntry
- containers.sql
- e2e-bootstrap.ts
- Chaosium CoC Catalog
- mythos_dev.players
- Phase 1: Core Separation
- test_magic_healing_events.py
- CommandRateLimiter
- test_event_publisher.py
- Phase 2: Enhanced Features
- subzone_schema.json
- Async Audit Executive Summary
- TEMPORAL_SYSTEM_RESEARCH.md
- test_room_write_procedures.py
- Prometheus Configuration
- load_world_seed.py
- validate.py
- ReactNodeUpgradeAnalyzer
- game_tick_death.py
- .validate_current_vs_max_stats
- run_flee_effect
- NPCCommunicationIntegration
- game_tick_protocols.py
- UserManagerProtocol
- test_combat_validator.py
- real_time.py
- test_optimized_security_validator.py
- MinimapRenderer
- scripts
- map/types.ts
- type
- P8 · Applied
- properties
- NATS Code Review - Branch: feature/sqlite-to-postgresql
- WebSocket Code Review - Branch: feature/sqlite-to-postgresql
- enum
- test_admin_commands_helpers.py
- test_container_helpers_inventory_display.py
- asyncio
- EventBusLifecycleMixin
- CharacterCreationService
- ComprehensiveLoggingMiddleware
- .create_combat_instance
- test_room_occupant_manager.py
- test_lint_container_get_instance.py
- InviteManager
- Async Remediation Final Report
- 🔴 CRITICAL ISSUES
- Test Suite Quality Audit - Executive Summary
- send_welcome_event
- test_inventory_command_prototype.py
- AsciiMapRenderer
- test_lifecycle_respawn.py
- MagicServiceCompletionMixin
- NPCStartupService
- GameConfig
- TestLogoutCommand
- test_chat_moderation.py
- ._handle_exception
- Bug Investigator Subagent
- EdgeDetailsPanel.tsx
- playerHandlers.ts
- Domain Model Anemic Anti-Pattern Audit
- ErrorMonitor
- verify_linting_parity.py
- players.sql
- CircuitBreaker
- validate_secure_path
- test_logging_processors.py
- test_lru_cache.py
- test_quest_service_collect.py
- test_combat_death_handler.py
- Argon2 Password Hashing Best Practices
- Pre-commit Hooks Best Practices
- debugLogger
- Communities (19 total, 4 thin omitted)
- properties
- Persistence Layer Refactoring - COMPLETE ✅
- enum
- LogAnalyzer
- test_look_item.py
- test_chat_pose_helpers.py
- MetricsCollector
- test_npc_threading_messages.py
- attach_compatibility_properties
- rooms.sql
- extract_player_name
- test_rate_limiter.py
- format_room_posture_message
- test_movement_monitor.py
- test_room_service.py
- Path
- PostgreSQL Best Practices
- Structured Logging with Structlog Best Practices
- Uvicorn ASGI Server Best Practices
- multiplayer-colocated.ts
- Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch
- test_load_world_seed.py
- test_emote_repository.py
- PrototypeRegistry
- schemas/unified_room_schema.json
- connection_cleanup_methods.py
- .claude/hooks/record_edited_file.py
- Vitest Best Practices
- dependencies
- messageHandlers.ts
- FeedbackManager
- .cursor/hooks/record_edited_file.py
- Migration Strategy
- ADR-012: python-statemachine for Backend Connection FSM
- Async Facades Implementation - COMPLETE ✅
- Feature Requirements Document: Random Stats Generator
- Migration 019: Complete Implementation Summary
- Persistence Layer Async Migration Plan
- Phase 4: Recommendations
- enum
- fix_fstring_logging.py
- TestRunner
- test_room_subscription_manager_npcs.py
- handle_emote_command
- test_behavior_engine.py
- ._get_room_uuid_by_stable_id
- .disconnect
- spell_repository.py
- npc_combat_grace.py
- Any
- send_system_message
- test_lint_optional_auth_no_guard.py
- ApplicationContainer Structure Analysis and Domain-Specific Split Proposal
- SchemaValidator
- get_cached_player
- ValidationRule
- SQLAlchemyAsyncLinter
- Test Suite Analyzer Subagent
- React Best Practices
- Frontend Design Skill
- Onboard Skill
- stateNormalization.ts
- multiplayer-browser-helpers.bundle.js
- compilerOptions
- Communities (10 total, 2 thin omitted)
- Dependency Upgrade Strategy Specification
- NATS Anti-Patterns and Best Practices Review
- ContainerLockMixin
- format_markdown_file
- migrate_rooms.py
- skills_commands.py
- handle_teach_command
- Player
- realtime/realtime.py
- test_mp_regeneration_service.py
- _handle_admin_set_stat_command
- Lint Remediation
- mythos_dev.rooms
- required
- test_player_repository_room.py
- TestNPCCombatLifecycle
- test_command_factories_inventory_helpers.py
- Color & Contrast
- MythosMUD Code Quality Targets for AI
- MythosMUD Database Placement
- MUD Disconnect Grace Period & Rest Command: Industry Comparison
- Code Review: Import Analysis and Anti-Patterns
- ContainerRepository and ItemRepository: Review and Full Async Migration Plan
- MythosMUD Dependency Upgrade Strategy - Implementation Summary
- Documentation Updates - ConnectionManager Refactoring
- Persistence Layer Refactoring Summary
- Phase 2 Async Persistence Migration - Status Update
- TEST_AUDIT_EXECUTIVE_SUMMARY.md
- compilerOptions
- Execution Steps
- Execution Steps
- generate_html_visualization.py
- verify_migration.py
- test_alias_expansion.py
- RoomCacheLoader
- error_handling_middleware.py
- CommunicationIntegrationProtocol
- MovementMonitor
- test_add_player_effect_generates_id
- test_retry.py
- .call
- repositories/__init__.py
- CircuitState
- apply_communication_dampening
- exploration.sql
- asyncio
- test_check_coverage_thresholds.py
- test_combat_persistence_handler.py
- npcs.sql
- Performance Profiler Subagent
- Security Auditor Subagent
- GitHub Actions Best Practices
- The Toolkit
- asyncio
- Complexity Refactoring Test Plan
- NATS Complete Remediation Summary
- SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch
- Execution Steps
- fix_suppression_alignment.py
- identify_critical_code.py
- Phase 3: Polish and Optimization
- NPCEventReaction
- test_security_utils.py
- Phase 4: Testing and Refinement
- .read_token
- Scenario 22: Invite-Only Registration Enforcement
- ContainerFactoryOptions
- get_room_environment
- overrides
- server/main.py
- ensurePlayableConnection
- compilerOptions
- test_channel_broadcasting_strategies.py
- compilerOptions
- Communities (11 total, 0 thin omitted)
- Communities (11 total, 0 thin omitted)
- DOCUMENTATION_AUDIT.md
- Asyncio Code Review - feature/sqlite-to-postgresql Branch
- Environment Contamination Audit Report
- Findings by Category
- NATS Medium-Priority Remediation Summary
- Pydantic Code Review - feature/sqlite-to-postgresql Branch
- Game Subsystem Design Documents Overview
- Execution Steps
- properties
- audit_suppressions.py
- fix_markdown_line_length.py
- populate_npc_sample_data.py
- generate_invites_db.py
- MemoryMonitor
- test_lucidity_command_disruption.py
- test_exploration_procedures.py
- asyncio
- reset_current_tick
- player_effect_repository.py
- TestPathValidator
- Design Critique
- useThemeContext.ts
- compilerOptions
- Communities (10 total, 0 thin omitted)
- properties
- properties
- Lizard Complexity Analysis Findings
- ConnectionManager Refactoring Summary
- Actionable Recommendations
- Phase 2: Qualitative Analysis Results
- Transaction Boundaries Audit
- LoggingPatternLinter
- logging_file_categories.py
- fixtures/unit/__init__.py
- required
- UpgradeImplementationPlan
- SpellTargetingService
- PartyService
- SpellEffects
- asyncio
- test_security_headers.py
- Any
- channel_broadcasting_strategies.py
- TestVerificationSqlUsersPlayers
- test_nats_message_handler_subzone_events.py
- optimized_validate_player_name
- static_data/package.json
- TypeScript Best Practices
- vite Best Practices
- Delight Techniques
- Frontend Aesthetics Guidelines
- Any
- compilerOptions
- test_command_factories_inventory.py
- Enhanced Logging Best Practices for MythosMUD
- Persistence Layer Extraction - COMPLETE ✅
- Test Coverage Summary: Disconnect Grace Period & Rest Command
- test_email_utils.py
- NPCCacheService
- ProfessionCacheService
- .create_put_command
- .create_get_command
- test_party_flow.py
- room_hierarchy_schema.json
- schedule_end_combat_if_npc_died_best_effort
- CoordinateValidator
- test_hallucination_services.py
- enum
- .create_equip_command
- fixtures/shared/__init__.py
- retry_with_backoff
- _GenerateOpenapiSpecModule
- room_validator/tests/conftest.py
- click Best Practices
- 2. Type Hinting Best Practices
- Animate Skill
- Polish Systematically
- overrides
- Migration 019 Ready for Deployment
- Gladiator Ring (Arena) Implementation Plan
- Python Model Updates Required for Migration 019
- Recommended Test Additions
- Critical Coverage Gaps
- Execution Steps
- properties
- fix_markdown_blanks_around_lists.py
- init_npc_database.py
- lint_raw_sql_in_python.py
- test_cancel_shutdown_countdown_no_active
- asyncio
- NATSRetryHandler
- asyncio
- ChatWhisperTracker
- enum
- .check_bidirectional_connections
- SQLAlchemy Best Practices (2.x Style)
- Introduce Color Strategically
- knip.json
- usePanelContext.ts
- commandStore.ts
- AggressiveMobNPC
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)
- applies_to
- Async Remediation Complete
- Execution Steps
- properties
- properties
- properties
- fix_file
- jackson_linter.py
- RoomFilenameMigrator
- CacheManager
- client/package.json
- test_occupants.py
- asyncio
- Party
- test_message_filtering.py
- test_player_repository.py
- test_player_spell_repository.py
- asyncio
- optimized_validate_security_comprehensive
- properties
- properties
- Codebase Explorer Subagent
- Pylint Best Practices
- Adapt Skill
- Improve Copy Systematically
- UX Writing
- saveMapChanges.ts
- message_handler_factory.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)
- Changes by document
- Memory Leak Audit Report
- Quick Start: Running E2E Tests
- test_ascii_map_renderer_grid.py
- _errors_len
- holiday.schema.json
- schedule.schema.json
- analyze_coverage_gaps.py
- _apply_arena_seed_patch.py
- pylint.py
- generate_sql.mjs
- fixture
- validate_admin_permission
- required
- NPCActionMessage
- UUID
- test_circuit_breaker.py
- required
- zone_schema.json
- PlayerChannelPreferences
- ._attack_target_impl
- _FakeMessageQueue
- test_metrics.py
- TestResolveExitTarget
- test_check_pr_issue_references.py
- combat_messaging/base.py
- RoomDataCache
- test_check_no_production_assert.py
- test_validate_codacy_coverage_gate.py
- optimized_sanitize_unicode_input
- pytest Best Practices
- Skill: Create a New Worktree for a Task
- TestHorizontalExitCharBetween
- MessageBatcher
- .create_lie_command
- server/tests/conftest.py
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)
- required
- npc_schedules.schema.json
- PARALLEL EXECUTION RESULTS (2025-11-05)
- fix_markdown_common_issues.py
- process_room_files
- validate_codacy_coverage_gate.py
- fixture
- ._format_mute_entry
- .connect_websocket
- ._get_vertical_exit_char
- Motion Design
- Profession
- mythos_dev.item_instances
- lock_state
- environment
- get_npc_name_from_instance
- is_safe_filename
- test_containers_procedures.py
- test_players_procedures.py
- required
- _StubPlayerRepo
- test_event_publisher_helpers.py
- properties
- check_no_production_assert.py
- Generate Comprehensive Report
- Interaction Design
- Spatial Design
- Typography
- Fix patterns by tier
- Optimize Skill
- Semgrep Configuration
- Test Server Remediation Prompt - Cursor Executable Version
- Arkham City (MOTD Zone)
- INDEX.md
- Claims by cluster
- P4 · Intent Sweep — Core Feature Issues
- P3 · Findings Verified Directly
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)
- Migration 019 Verification Report
- NATS Anti-Patterns Remediation Summary
- analyze_log_file
- find_fstring_logging_violations
- check_pr_issue_references.py
- lint_sql_guardrails.py
- CacheService
- ChatPoseManager
- environment
- FRD & Plan-Document Verification Register — 2026-08
- mp_regeneration_service
- normalize_path_from_url_or_path
- test_profession_service.py
- test_ascii_map_renderer_exits.py
- ._get_npc_display_name
- test_persistence_container_persistence.py
- UnknownChannelStrategy
- test_holiday_service.py
- test_websocket_handler_rate_limit.py
- SystemAdminChannelStrategy
- test_command_factories.py
- TestValidatorIntegration
- Improve Layout Systematically
- Distill Skill
- RoomBasedChannelStrategy
- handle_time_command
- ClientLogger
- Any
- Mypy Remediation
- P4 · Intent Sweep — FRD/SPEC Documents
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)
- required
- ADR-018: New Game Session vs Grace Reconnect
- Technical Implementation
- Critical Issues
- Easy Coverage Wins - Quick Analysis
- Entries
- Unique Pylint Findings Analysis
- Execution Timeline
- ._create_tracked_task
- main
- fix_markdown_code_block_style.py
- main
- SyntaxErrorFixer
- generate_openapi_spec.py
- safe_run
- test_follow_flow.py
- test_look_npc.py
- ._load_player_mutes_from_data
- TestGetContainer
- _FakeRoomManager
- .create_go_command
- optimized_comprehensive_sanitize_input
- required
- properties
- verify_npc_occupants.py
- asyncio
- test_async_persistence_room_cache.py
- .create_ground_command
- test_player_event_handlers_utils.py
- test_room_subscription_manager.py
- test_run_test_ci.py
- .create_follow_command
- test_room_environment_parity.py
- ScheduleEntry
- Commands
- Docker Best Practices
- Zustand Best Practices
- Amplify the Design
- Hardening Dimensions
- MythosMUD LLM Wiki (Obsidian)
- MapPerformanceMonitor
- PanelContextRuntime.tsx
- Lint Remediation
- mcp.json
- TRACK C · The interactive review — 8 decisions
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)
- bonus_tags
- Complexity Checking Alignment: Ruff C901 vs Pylint
- What They Measure
- Migration Guide: From Default Logging to Enhanced Logging
- Enhanced Logging Quick Reference
- PERSISTENCE_REFACTORING_COMPLETE.md
- Migration Roadmap
- Critical Insights
- Multi-Character Support System
- enum
- _collect_python_public_defs_and_tiny
- infrastructure/conftest.py
- lint_container_get_instance.py
- main
- main
- test_command_service.py
- inventory_unequip_command.py
- test_combat_grace_period.py
- SkillUseLog
- fixture
- connectionStore.ts
- event_publisher
- room_validator/schemas/unified_room_schema.json
- test_lucidity_procedures.py
- _ensure_connection_manager
- custom_length_validator
- test_monitoring_init.py
- .get_task_lifecycle_metrics
- load_motd
- main
- Codacy Rules
- Quieter Skill
- Typeset Skill
- test_combat_messaging_integration.py
- vite.userConfig.ts
- Client Test Remediation
- main
- Claims by cluster
- P3 · container-di + client + domain
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)
- Authoritative Environment DML
- AnyIO Code Review - Anti-Patterns and Issues
- ✅ Best Practices Compliance
- 🔍 Specific File Reviews
- CircuitBreaker Implementation Planning Document
- Ruff to Pylint Rule Mapping
- Test Timing Analysis - Optimization Targets
- Movement Subsystem Design
- CI Workflow
- items
- analyze_file
- check_and_apply_map_migrations.py
- main
- main
- items
- container
- holidays
- schedules
- intersection_schema.json
- room_schema.json
- capacity_slots
- .create_drop_command
- asyncio
- Teach Impeccable Skill
- Playwright Best Practices
- Responsive Design
- .create_supervised_task
- ._compute_player_context
- Cursor Subagents Overview
- REQUIRED TOOL USAGE PATTERN
- FAILURE PATTERN RECOGNITION
- P3 · realtime-connection + events-nats
- P7 · Rulings — complete
- Design ↔ Implementation Drift Audit — Final Summary
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)
- enum
- AnyIO vs Asyncio: High-Level Comparison and Decision Guide
- Asynchronous Code Audit - December 3, 2025
- Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES
- 📋 Test Coverage Breakdown
- `docs/**/*` files: Multiple rules
- 2. Model Updates Verified
- Findings
- Repository Details
- POSTGRESQL_AUDIT_REPORT_2026.md
- TEST_COVERAGE_DISCONNECT_GRACE_PERIOD_REST.md
- Implementation Phases
- Test Suite Quality Audit Report
- MythosMUD Testing Strategy (Greenfield Suite)
- Dialogue Content Tools (Content Creators)
- load_test_10_players.spec.ts
- emote_schema.json
- bench_cache_npc.py
- bench_cache_professions.py
- check_file
- test_cache_service.py
- initialize_components
- .__init__
- .on_enter_state
- lucidity_migration.py
- ensure_directory_exists
- test_calendar_procedures.py
- session_factory
- test_npcs_zone_config_procedures.py
- test_async_persistence_room_loading.py
- TestMinimapExplorationInvestigationDoc
- handle_system_command
- optimized_validate_action_content
- optimized_validate_alias_name
- gh-stack (MythosMUD)
- Workflows
- FastAPI Best Practices
- Dependency Upgrade
- tailwind Best Practices
- run-playwright-tests.js
- mythos_e2e Database
- P4 · Intent Sweep — Plan Documents
- holidays.schema.json
- Audit Coverage Boundary — 2026-08 Design Audit
- 🟡 HIGH PRIORITY ISSUES
- 🟢 MEDIUM PRIORITY IMPROVEMENTS
- Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE
- 🔴 Anti-Patterns Check (Critical)
- Coverage Improvement Summary - Plan 2 Execution
- Implementation Notes
- Ruff C901 McCabe Complexity
- Positive Findings ✅
- Detailed Implementation
- Specific File Reviews
- Python Code Coverage Status
- .get_combat_stats
- applies_to
- test_websocket_handler_validation.py
- analyze_idle_memory_samples.py
- bench_cache.py
- quality_fragmentation_graph.py
- _filter_lines
- fix_markdown_file
- fix_room_references
- run_bug_prevention_tests.ps1
- run_make_stages.py
- TestGetPlayerService
- ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List
- App Package Design
- Auth Package Design
- Models Package Design
- player_inventory_migration.py
- Schemas Package Design
- fixture
- Services Package Design
- test_utility_commands_whoami.py
- TestGetPlayerServiceForTesting
- fixture
- TestGetConnectionManager
- test_player_service_mutations.py
- test_room_subscription_manager_drops.py
- ADR-019: Player Effects System
- optimized_validate_target_player
- optimized_strip_ansi_codes
- Room Pathing Validator Implementation Spec
- validator.py CLI
- AGENTS.md
- gh-stack
- AuthRateLimitMiddleware
- Pydantic Best Practices
- MythosMUD Commit Messages
- worktree-plan-template.md
- Step 2: Ask UX-Focused Questions
- run-vitest.js
- usePerformanceMonitor.ts
- cli.sh
- Earth Plane
- C2 · REVISED — procedures-only is binding
- P3 · config-api
- P3 · persistence-db
- P5 · Adversarial Refutation
- emotes.schema.json
- 1. Enhanced ChatPanel (New Chat Input Panel)
- ✅ Verified Already Implemented
- Implementation Phases
- 3. REFACTOR Findings (935 findings)
- LOGGING_BEST_PRACTICES.md
- NumPy Code Review - MythosMUD Codebase
- Multiplayer Architecture Planning
- API Endpoints (Phase 2)
- PYDANTIC_CODE_REVIEW.md
- Top Time Consumers (>10 seconds)
- pyrightconfig.json
- enum
- main
- migrate_file
- generate_sql.mjs
- validate.mjs
- Server & Client Package Documentation Coverage
- TestGetAsyncPersistence
- TestGetPlayerRespawnService
- TestGetPlayerCombatService
- TestGetPlayerDeathService
- TestGetCombatService
- TestGetMagicService
- 1. Structured Concurrency: Entry Points and Task Management
- test_run_make_stages.py
- monitoring_service
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- optimized_validate_filter_name
- optimized_validate_help_topic
- TestGetSpellLearningService
- CRITICAL SERVER MANAGEMENT RULES
- Test Coverage Requirements
- gh-stack (MythosMUD)
- Git Workflow
- MythosMUD ADR Authoring
- MythosMUD Logging Standards
- MythosMUD Server Runbook
- MythosMUD Test Writing
- E2E Tests Playwright
- Event-Sourced Projector
- useGridLayout.ts
- Three-Column Game UI Layout
- Corrections · `docs/subsystems/` was missing from the corpus
- CRITICAL · WebSocket authentication bypass on `/ws`
- Design ↔ Implementation Drift Audit
- P0 · Previously-Known Deviations
- Decisions required
- ._generate_invite_code
- Chat Panel
- Aggro and Threat System Implementation Plan
- ✅ POSITIVE FINDINGS
- 🔴 CRITICAL ISSUES
- Easy Coverage Wins
- 1. CONVENTION Findings (260 findings)
- NATS Anti-Patterns Review 2026-01-13
- Migration Workflow (Per File)
- Methods Extracted
- Security Implementation
- 3.3 Value Distribution Calculation
- calculate_notification_times
- Attack Command Not Starting Combat
- Second NPC Combat And Linkdead Findings
- Multi-Word Spell Name Parsing Failure
- main
- TestGetNPCSpawningService
- NATSConfig
- Server Realtime Module
- TestGetNPCPopulationController
- TestGetChatService
- .validate_timestamp
- TestGetExitEntriesForRoom
- mythos_dev.npc_definitions
- items.sql
- enum
- TestGetPlayerServiceForTesting
- .create_sit_command
- _extract_bearer_token
- Thinking about stack structure
- Extract Skill
- MythosMUD Server Test Suite
- Common Test Failure Categories
- .create_stand_command
- description
- name
- Chat Panel Separation Specification
- 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage
- 📚 Documentation Created
- Implementation Details
- Core Logging Principles
- Performance Logging
- Common Mistakes and How to Fix Them
- Enhanced Logging Features
- Log Levels and Usage
- Common Patterns
- Enhanced Logging Migration Report
- Completed Fixes ✅
- NPC Startup Duplication Analysis
- ✨ Key Achievements
- PostgreSQL Procedures Migration - Audit Spreadsheet
- Real-Time Communication (WebSocket)
- Test Suite Analysis
- Modern Testing Patterns
- Test Modernization Checklist
- Phase 5: Strategic Additions (Week 5)
- packages/README.md
- Whisper Channel System
- NPC Occupants Verification Summary
- Combat Client Crash
- Respawn Death Screen Loop Limbo ID Mismatch
- NPC Combat Start Race Condition
- Round-Based Combat
- WebSocket-Only Migration
- item_prototype.schema.json
- description
- _run_dialogue_ddl
- check_file_for_logging_issues
- e2e_reset_players.py
- add_suppression_to_file
- description
- _ConnectionManagerUtilsModule
- test_chat_logger.py
- .create_unfollow_command
- _RaisesOnBool
- description
- PostgreSQL database names (MythosMUD)
- MythosMUD COPPA Checklist
- MythosLoginForm.tsx
- global-teardown.ts
- AI PR Reviewer Instructions
- 4. Common Fix Patterns
- DML Migrations
- Nameless Horrors - 2nd Edition (source summary)
- S. Petersen's Field Guide to Lovecraftian Horrors (source summary)
- name
- Advanced Chat Channels Specification
- UI/UX Considerations
- 3. Simplified CommandPanel
- Implementation Phases
- Magic and Spellcasting System
- Implementation Plan
- Lucidity Tiers
- Code Quality Improvements
- Common Conversion Patterns
- Gotchas & Solutions
- Four-Level Room Hierarchy
- Phase 1: Quantitative Analysis Results
- weather_patterns
- Summary: Test Quality Metrics
- Modular E2E Test Suite
- Playwright MCP Scenarios
- Local Channel System
- Container Contents Synchronization Bug
- F-String Logging Violations
- Quest System Gap
- items
- 7. Common Test Failure Solutions
- fix_file
- check_codacy_yaml
- HADS tooling (MythosMUD)
- snapshot_chaosium_graphify.ps1
- 2025_01_XX_convert_players_player_id_to_uuid.py
- 2025_11_21_convert_players_player_id_to_uuid.py
- 2025_11_25_normalize_container_schema.py
- 2025_11_25_remove_get_container_contents_json_procedure.py
- 2025_11_25_remove_items_json_column.py
- 2025_11_26_ensure_item_instance_foreign_keys.py
- 2026_02_09_add_player_effects_table.py
- 2026_02_18_add_player_skills_table.py
- 2026_02_18_add_profession_modifiers_columns.py
- 2026_02_19_add_quest_tables.py
- 2026_02_19_seed_quest_leave_the_tutorial.py
- 2026_02_26_add_arena_zone_type.py
- 2026_08_20_align_room_environment_enum.py
- rename_players_to_population.py
- get_alerts
- command_service
- _RoomPersistence
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- 2. Auto-Attack During Grace Period
- 3. Grace Period Visibility & Messaging
- 4. Rest/Quit Command During Combat
- 5. Rest Command Countdown Duration
- 6. Rest Location (Inn/Hotel) Behavior
- add_fastapi_users_columns.py
- 7. Reconnection During Grace Period
- 8. Grace Period After Intentional Disconnect
- 9. Command Blocking During Grace Period
- test_grype.py
- Recommendations Summary
- mythos_dev.users
- add_hashed_password_column.py
- user_manager
- day
- month
- Tiered Test Coverage Strategy
- add_used_by_user_id_column.py
- rename_invites_columns.py
- message-match.test.ts
- multiplayer-browser-helpers.d.ts
- 9. Test Maintenance Best Practices
- Geography Overview.md
- DML Migrations Apply Paths
- days
- Chaosium CoC Catalog.md
- effects
- A Cold Fire Within (source summary)
- Alone Against the Dark (source summary)
- Alone Against the Frost (source summary)
- Alone against the Tide (source summary)
- Berlin - The Wicked City (source summary)
- Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)
- Call of Cthulhu Keeper Tips (source summary)
- Call of Cthulhu Starter Set (source summary)
- Call of Cthulhu_ The Coloring Book (source summary)
- character_sheets (source summary)
- Cthulhu Dark Ages - 3rd Edition (source summary)
- Does Love Forgive_ (source summary)
- Doors to Darkness (source summary)
- Down Darker Trails (source summary)
- Gateways to Terror (source summary)
- Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)
- The Grand Grimoire of Cthulhu Mythos Magic (source summary)
- The Malleus Monstrorum Keeper Deck (source summary)
- duration_hours
- Migration Considerations
- Success Criteria
- Risk Assessment
- Testing Strategy
- Core Architectural Differences
- Real-World Impact for MythosMUD
- Detailed Feature Comparison
- Recommendation for MythosMUD
- 📚 REFERENCES AND RESOURCES
- 📊 METRICS AND SUCCESS CRITERIA
- 🚀 DEPLOYMENT STRATEGY
- end_hour
- Phase 2: Database Layer Integration
- Phase 3: Real-Time Communication Protection
- Phase 4: File System Operations
- Phase 6: Monitoring and Observability
- Future Enhancements
- Monitoring and Alerting
- Success Criteria
- Testing Strategy
- 🔬 Lessons Learned
- 🛠️ Technical Achievements
- 🚀 How to Run Remaining Tests
- WebSocket and SSE Dual Connections
- Context Management
- MythosMUD Product Requirements
- Test Execution
- rename_used_to_is_active.py
- Cursor Subagents Documentation
- Scenario Group Execution
- Main Foyer Starting Room
- Per-Recipient Whisper Rate Limiting
- Lucidity System Expansion Scenarios
- Container System
- Scenario 32 Disconnect Grace Period
- Catatonic Movement Prevention Bug
- Rooms List SQL ::uuid[] Parameter Conflict
- Vite Best-Practices Remediation
- duration_hours
- Shared JSON schemas
- apply_migration
- main
- _resolved_npm
- start_server.ps1
- verify_schema_match.sh script
- verify_tutorial_migrations.ps1
- start_hour
- exits
- validate_prototypes.py
- 1. Component Refactoring
- Executive Summary
- .codacy.yml
- eslint.config.js
- Client Security and Privacy Policies
- MythosMUD UI Component Library
- UUID
- mythosTheme.ts
- .validate_parameter_value
- Step-by-Step Remediation Process
- registry_with_switchblade
- Chaosium graphify snapshot - A Cold Fire Within
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
- Chaosium graphify snapshot - character_sheets
- Chaosium graphify snapshot - Cthulhu Dark Ages - 3rd Edition
- Chaosium graphify snapshot - Dead Light and Other Dark Turns
- Chaosium graphify snapshot - Does Love Forgive_
- Chaosium graphify snapshot - Doors to Darkness
- Chaosium graphify snapshot - Down Darker Trails
- Chaosium graphify snapshot - Gateways to Terror
- Chaosium graphify snapshot - Malleus Monstrorum - Cthulhu Mythos Bestiary
- Chaosium graphify snapshot - Mansions of Madness_ Vol 1 - Behind Closed Doors
- Chaosium graphify snapshot - Nameless Horrors - 2nd Edition
- Chaosium graphify snapshot - Petersen's Abominations
- Chaosium graphify snapshot - Pulp Cthulhu (7th edition Call of Cthulhu)
- Chaosium graphify snapshot - Reign of Terror
- Chaosium graphify snapshot - S. Petersen's Field Guide to Lovecraftian Horrors
- Chaosium graphify snapshot - The Grand Grimoire of Cthulhu Mythos Magic
- Chaosium graphify snapshot - The Malleus Monstrorum Keeper Deck
- Expansion Backlog (Raw)
- Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)
- Call of Cthulhu Investigator Handbook 7th Edition (source summary)
- Dead Light and Other Dark Turns (source summary)
- Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)
- Petersen's Abominations.md
- Paris (Reign of Terror).md
- test_websocket_handler_disconnect.py
- What Are They?
- Character Creation Revamp
- Comprehensive System Audit
- Architecture Overview
- Dead Code Cleanup Completion
- Single Session Per User
- 🎯 Next Steps
- Fixture Optimization Complete
- Test Warning Remediation
- Enhanced Logging Migration Complete
- Random Stats Generator Planning
- day
- Party System Reference
- Archive Directory README
- Structured Error Logging
- Test File Migration Mapping
- Who Command Enhancement
- 10 Concurrent Players Load Test
- Scenario 20 Logout Errors
- Scenario 34 Two Players Same Room Visibility
- E2E Session Report 2025-12-02
- Playwright MCP Primary Testing Tool
- Whisper NATS Subject Bug Fix
- Dependency Review Workflow
- Impeccable design context
- NPCs Not Updating On Player Movement
- Combat Messages Dual Panel Display
- Test Suite Stall After Performance Comparison
- Client Updates System Audit
- Cursor Rules as Canonical Config
- Logging Aggregator Verification
- Memory Leak Remediation
- Playwright DI Migration Validation
- Server Authority Remediation
- check_postgresql.sh
- remove_dir
- load_seed_data
- safe_print
- parse_lint_findings
- setup_postgresql_test_db.sh
- verify_e2e_users_seeded.py
- holiday
- month
- test_websocket_handler_helpers.py
- start_hour
- TestGetPlayerService
- plane
- zone
- long_description
- prototype_id
- short_description
- id
- plane
- rest_location
- sub_zone
- integration
- .use_invite
- zone
- PlayerStatsConfig
- test_create_admin_command
- rest_location
- sub_zone
- zone
- Test Suite Analyzer Agent
- black.md
- Vite Logo SVG
- message_filtering_helper
- subject_manager_no_cache
- ApplicationContainer
- playwright.runtime.config.ts
- deps/package.json
- wsl-bashrc-codacy.sh
- Mypy Remediation Skill
- MythosMUD Obsidian Index
- MythosMUD Worldbuilding Foundation (Raw)
- LLM Wiki Pattern.md
- player_service
- id
- .flee
- .sample_holidays
- test_validate_secure_path_path_traversal_commonpath
- Lucidity.md
- Migration 019 Testing Guide
- db/migrations/README.md
- Architecture Remediation Implementation Summary
- httpOnly Cookie Token Storage
- Combat Health Persistence Bug
- Paired YAML and Env Config Tuples
- React Node Upgrade Plan
- Environment Configuration Refactoring
- container_test_client Fixture
- Graceful Degradation Planning
- Item System Blueprint
- Pylint E0611 No Name in Module
- Mapped Diagnostic Context
- Migration Final Report
- Kingsport Yule Procession
- Two-Day Holiday Cap
- NATS JetStream
- Panel Layout Libraries Spec
- Structlog Implementation Plan
- MOTD Sacred Styling
- E2E Scenario Conversion
- CWE-209 Information Exposure
- ftfy Unicode Normalization
- Temporal NPC Schedules
- Updated Coverage Targets
- Hierarchical Test Structure
- Chat Messages Not Displayed to Sender (Bug #2)
- Mute Command Server Error (Bug #1)
- Playwright MCP core-tabs Capability
- Playwright MCP Timing Limitation
- Mandatory AI Execution Contract
- Room Subscription Timing Race
- AGENTS.md Authoritative Guidance
- Bug Report Issue Template
- Issue Template Config
- PR Coverage Thresholds
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
- Comprehensive planning document
- Deprecated get_async_persistence Global
- authoritative_schema.sql
- CoC Spells Proposal
- Convert E2E Scenarios to Playwright CLI
- Temporal System 4:1 Calendar Conversion
- Critical File Coverage Improvement
- Cursor Hooks Development Plan
- Eliminate Raw CRUD SQL
- Follow Command Feature
- 10-Second Login Grace Period
- Codacy 8100+ Remediation
- PostgreSQL Audit Remediation
- React Best-Practices Remediation
- Requests Best Practices Remediation
- app.state Global State Anti-Pattern
- schemas/__init__.py
- apply_container_migrations.py
- Incremental Upgrade Strategy (Report)
- High-Risk Major Package Updates
- ensure_codacy_coverage_reporter_ci.sh
- ensure_uv_ci.sh
- gen_arena_uuids.py
- generate_schema_from_dev.sh script
- install_ci_dependencies.sh
- _scan_dml_blank_before_terminator.py
- constants/__init__.py
- id
- ._handle_hunt_target
- ._handle_patrol_territory
- PlayerSearchService
- .is_expired
- .__init__
- server/game/magic/__init__.py
- TestGetProfessionService
- ._exit_is_bidirectional
- description
- name
- persistence/utils/__init__.py
- plane
- _UserWithGet
- zone
- server/structured_logging/__init__.py
- server/tests/__init__.py
- command_handler_unified/__init__.py
- exits
- plane
- unit/game/magic/__init__.py
- sub_zone
- zone
- description
- npc_spawn_modifier
- special_rules
- mythos_dev.dialogue_definitions
- mythos_e2e.dialogue_definitions
- mythos_unit.dialogue_definitions
- id
- plane
- Security Considerations
- enum
- 8. Error Handling and Debugging
- weight
- .validate_invite
- metadata
- .canonical_room_id
- party_service
- cross-env
- eslint-plugin-react-refresh
- globals
- _iter_exception_chain
- autoprefixer
- postcss
- @tailwindcss/postcss
- @types/node
- happy-dom
- markdownlint-cli
- @types/react-dom
- @playwright/test
- tailwindcss
- @vitest/coverage-v8
- _FakeClientState
- .get_unused_invites
- metrics
- .handle_npc_death
- @vitejs/plugin-react
- mythos_dev.emote_aliases
- mythos_dev.get_user_id_by_username_ci
- test_parse_command_string_success
- test_parse_command_string_with_subcommand
- test_parse_command_string_unexpected_error
- ._publish_attack_event
- create_professions_table.sql
- test_prepare_command_data_with_pipe_target
- test_build_room_objects_with_dict_attributes
- .ensure_unique_ids
- ._render_empty_map
- test_process_tick_regeneration_fractional_accumulation
- test_restore_mp_from_rest_at_max
- test_restore_mp_from_rest_calculates_max_from_power
- test_restore_mp_from_meditation_player_not_found
- test_process_tick_regeneration_sitting_position
- test_process_tick_regeneration_player_not_found
- test_process_tick_regeneration_at_max
- test_process_tick_regeneration_calculates_max_from_power
- test_validate_room_exists_cache_not_found
- test_get_user_by_username_case_insensitive_no_session
- unit/infrastructure/__init__.py
- test_get_professions_no_session
- test_get_players_batch_empty_list
- test_generate_room_id_from_zone_data_with_prefix
- test_generate_room_id_from_zone_data_needs_generation
- test_parse_exits_json_string_valid
- test_parse_exits_json_list
- test_load_room_cache_async_rooms_none
- test_parse_exits_json_other_type
- test_process_exits_for_room_multiple_exits
- test_process_combined_rows_no_exits
- test_extract_parsed_fields_with_pipe_target
- test_execute_command_handler_error
- test_process_command_parse_error
- test_process_command_no_handler
- test_process_room_rows_with_none_zone_stable_id
- test_get_available_commands
- test_unregister_command_handler
- test_process_exit_rows_with_partial_room_ids
- test_process_exit_rows_debug_logging
- test_build_room_objects_success
- test_process_room_rows_with_full_room_id
- test_build_room_objects_with_non_dict_attributes
- test_process_room_rows_with_none_stable_id
- test_load_room_cache_with_rooms_logs_sample_ids
- test_process_room_rows_empty_list
- test_process_exit_rows_empty_list
- test_process_exit_rows_multiple_exits_same_room
- test_process_exit_rows_zone_single_part
- test_build_room_objects_with_exits
- test_process_room_rows_with_partial_room_id
- test_build_room_objects_without_environment_in_attributes
- test_process_room_rows_with_none_attributes
- test_process_room_rows_zone_without_slash
- unit/middleware/__init__.py
- test_process_exit_rows_missing_zone
- test_process_exit_rows_missing_stable_id
- test_load_room_cache_async_warning_logging
- test_unregister_command_handler_nonexistent
- test_warmup_room_cache
- test_enrich_behavior_context_handles_no_current_room
- test_log_parsed_command_inspection
- test_process_validated_command_no_command_type
- test_enrich_behavior_context_sets_player_in_range_when_players_in_room
- test_create_spell_command
- test_apply_corruption
- _calculate_retry_delay
- unit/monitoring/__init__.py
- zones
- players
- npc_definitions
- test_gain_occult_knowledge
- unit/persistence/__init__.py
- test_damage_player
- test_get_user_characters
- test_soft_delete_character_success
- test_soft_delete_character_not_found
- test_soft_delete_character_wrong_user
- test_validate_player_name_whitespace
- test_delete_player_persistence_fails
- test_delete_player_success
- unit/realtime/integration/__init__.py
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- test_soft_delete_character_persistence_fails
- test_apply_lucidity_loss_player_not_found
- test_apply_corruption_player_not_found
- test_gain_occult_knowledge_player_not_found
- test_heal_player_player_not_found
- test_damage_player_player_not_found
- test_validate_player_name_too_short_one_char
- test_update_player_location_player_not_found
- test_get_room_persistence_returns_dict
- test_get_adjacent_rooms_success
- test_get_adjacent_rooms_source_not_found
- test_enrich_behavior_context_sets_false_when_no_players_in_room
- test_get_adjacent_rooms_null_exit
- test_get_local_chat_scope
- test_validate_room_exists_with_cache
- test_validate_room_exists_without_cache
- test_validate_exit_exists_success
- test_validate_exit_exists_invalid
- test_validate_exit_exists_from_room_not_found
- test_validate_exit_exists_no_exits
- test_get_room_occupants_with_cache_room_object
- test_get_room_occupants_cache_not_found
- test_validate_player_in_room_with_cache_true
- test_validate_player_in_room_cache_not_found
- test_get_room_exits_success
- test_get_room_exits_room_not_found
- test_get_room_exits_no_exits
- test_list_rooms_with_plane_zone
- test_list_rooms_with_sub_zone
- test_list_rooms_exclude_exits
- test_get_room_info_not_found
- test_room_service_init
- test_room_service_init_with_cache
- test_get_room_without_cache
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
- test_evaluate_condition_unknown
- test_get_applicable_rules_no_matching
- test_execute_applicable_rules_no_matching
- test_execute_applicable_rules_executes_highest_priority
- test_add_rule_missing_fields
- test_execute_applicable_rules_no_handler
- test_register_action_handler
- test_register_action_handler_overwrites
- test_state_direct_access
- test_execute_action_success
- test_evaluate_boolean_condition_false
- test_evaluate_boolean_condition_variable_false
- test_remove_rule_success
- test_remove_rule_not_found
- test_convert_room_uuids_to_names
- test_get_room_occupants
- test_get_player_not_found
- test_convert_room_uuids_to_names_no_player_ids
- test_convert_room_uuids_to_names_invalid_uuid
- test_get_room_occupants_empty_online_players
- test_get_room_occupants_with_online_players
- test_send_initial_game_state_no_player
- test_send_initial_game_state_send_fails
- test_convert_room_uuids_with_npcs
- test_get_room_data_with_conversion
- test_get_following_for_client
- test_get_quest_log_for_client
- test_get_players_batch
- test_circuit_breaker_init
- test_should_apply_mute_check_sensitive_channel
- test_should_apply_mute_check_non_sensitive_channel
- test_compare_canonical_rooms_same
- test_compare_canonical_rooms_different
- test_get_player_room_from_online_players
- test_get_player_room_from_online_players_not_found
- test_get_player_room_from_persistence_not_found
- test_is_player_in_room_false
- test_is_player_muted_by_receiver_not_muted
- test_get_user_manager_custom
- test_message_filtering_helper_init
- test_preload_receiver_mute_data
- test_collect_room_targets_with_canonical_id
- test_extract_chat_event_info
- test_record_build_stores_times
- unit/services/nats_subject_manager/__init__.py
- test_record_error_pattern_not_found
- test_record_error_missing_parameter
- test_record_error_validation_error
- test_record_error_unknown
- test_get_metrics_empty
- test_get_metrics_with_data
- test_get_metrics_calculates_percentiles
- test_subject_manager_metrics_init
- test_reset
- test_validation_times_maxlen
- test_build_times_maxlen
- test_record_validation_success
- test_record_validation_multiple
- test_record_build_success
- test_record_build_multiple
- test_spawn_required_npcs_success
- test_spawn_required_npcs_spawn_failure
- test_determine_spawn_room_room_id_not_found
- test_spawn_npcs_on_startup_with_optional_npcs
- test_create_sit_command
- test_create_aliases_command
- test_create_reply_command
- unit/structured_logging/__init__.py
- test_create_unequip_command
- test_create_mute_global_command
- test_create_punch_command
- test_create_teleport_command
- test_create_learn_command
- test_create_say_command
- test_create_pose_command
- unit/validators/__init__.py
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
- MythosMUD Database Placement Skill
- MythosMUD Server Runbook Skill
- POSTGRES_SEARCH_PATH for invites schema
- JSON Schema Validation
- room_validator/tests/__init__.py
- gh-stack Skill
- Codebase Explorer Agent
- Performance Profiler Agent
- Agent Routing
- Security Auditor Agent
- Argon2 Best Practices
- Black/Ruff Formatting Rule
- PostgreSQL Safety Rules
- PostgreSQL SQL Best Practices
- SQLAlchemy 2.x Best Practices
- Structlog Best Practices
- Tailwind CSS Best Practices
- Uvicorn Best Practices
- Explicit File Extensions
- Test Co-location
- Worktree Task Plan Template
- Vite HTML Entry
- Client Layer Layout
- Zustand Stores
- Codacy CLI Config
- MythosMUD Codacy Tool Suite
- Grype Local vs Trivy Codacy SCA
- Manually Managed codacy.yaml
- Codacy CLI via WSL on Windows
- Analysis Options
- Languages Config
- Semgrep Security Rules
- Contributor Covenant Code of Conduct
- Gladiator Ring (Arena)
- Client Test Remediation Skill
- Docker Best Practices Rule
- Authoritative DML Seed Data
- MythosMUD Local Data Directory
- MythosMUD Obsidian Log
- R'lyeh
- Mythos Magic
- Wiki Page Template
- mythos_dev mythos_unit mythos_e2e Databases
- generate_schema_from_dev.ps1
- Named Schema Per Database
- make verify-schema
- Owner and App Roles Per Environment
- AI Development Workflow
- Aggro and Threat System Design
- ADR-001: Layered Architecture with Event-Driven Components
- ADR-004: WebSocket-Only Real-Time Architecture
- ADR-005: Repository Pattern for Data Access
- ADR-006: PostgreSQL as Primary Datastore
- ADR-007: FastAPI with Async/Await
- ADR-008: React 18+ with TypeScript for Client
- ADR-009: Instanced Rooms
- ADR-010: Quest Subsystem Architecture
- ADR-016: Aggro and Threat Management System
- ADR-017: AST-Based Console Pruning in Client Production Build
- ADR-021: Character Display Name Validation
- Architecture Decision Records Index
- Admin Teleport Feature
- Argon2 Security Review
- Configuration Refactoring Complete
- datetime.utcnow Deprecation Fix
- Dependency Upgrade Report
- Dependency Upgrade Tasks
- Dependency Upgrade Implementation Plan
- Dual Connection Monitoring Guide
- Simultaneous WebSocket and SSE
- Dual Connection System Tasks
- Dual Connection Troubleshooting Guide
- .env and YAML Config Split
- player_lucidity Index Name Fix
- Players API Code Coverage Plan
- command_handler_v2
- Dual Command Processing Architecture
- Semgrep Windows UTF-8 Fix
- Legacy Test File Consolidation
- Test Migration Validation
- Test Refactoring Executive Summary
- Async Anti-Patterns Quick Reference
- CI Environment Alignment
- Client Layout Baseline
- Client message handling and GameState projection
- Client Typography and Layout Enhancement Specification
- Cursor Hooks
- Database Connection Pool Configuration
- Dead Code Definition and Tooling
- MythosMUD Deployment
- Fresh Session Test Execution Guide
- GitHub Actions Runner Parity Container
- NATS Error Handling Strategy
- NATS Manual Acknowledgment Guide
- PostgreSQL Standards for Contributors
- Quest Design Guidelines
- Quest System Features
- Room Environment Reference
- Item System Observability Runbook
- SQLAlchemy Async Best Practices
- Structured Concurrency Patterns
- Git Submodule Setup for MythosMUD
- Testing Guide for MythosMUD
- Map Regression Tests Proposal
- Pydantic Testing Patterns
- Troubleshooting Guide for MythosMUD
- Whisper Location Independence
- Per-Recipient Whisper Rate Limit
- Scenario 22 Administrative Summon
- Scenario 42 Quest Log Visible After Login
- Whisper System Investigation Report
- Whisper System Production-Ready
- Structured Logging Correct Patterns
- gh-stack Skill
- Codacy AI Instructions
- Documentation Issue Template
- Claude Code Workflow
- Claude Code Review Workflow
- PR Issue References Workflow
- Gladiator Ring Arena Plan
- Grype SCA exclude paths
- MythosMUD Code Quality for AI
- MythosMUD Full-Stack Feature
- MythosMUD Worktree Workflow
- NATS Whisper Subject Pattern
- mythosmud
- Click Best-Practices Remediation
- Code Practice Rules Reference Doc
- GitHub Actions Remediation
- Pydantic Anti-Patterns Remediation (3ee32154)
- Pytest Best-Practices Remediation
- Tailwind CSS Anti-Pattern Remediation
- finalize_build_touch Rebuild Trigger
- Persistence Repositories Overview
- GET /v1/monitoring/health
- Memory Leak Monitoring Endpoints
- PostgreSQL Player Persistence
- World Loading
- Enhanced Logging System Guide
- Adapt Skill
- Animate Skill
- Arrange Skill
- Audit Skill
- Bolder Skill
- Clarify Skill
- Colorize Skill
- Critique Skill
- Delight Skill
- Distill Skill
- Extract Skill
- MythosMUD Commit Messages Skill
- MythosMUD COPPA Checklist Skill
- MythosMUD OpenAPI Workflow Skill
- MythosMUD Test Writing Skill
- WebSocket Best Practices Compliance
- Worktree Plan Metadata
- GitHub Issues task tracking
- invites table
- Mythos-themed invite codes
- core/fixer.py
- jsonschema dependency

## God Nodes (most connected - your core abstractions)
1. `get_logger()` - 530 edges
2. `LoggedHTTPException` - 369 edges
3. `ValidationError` - 314 edges
4. `User` - 301 edges
5. `AliasStorage` - 264 edges
6. `DatabaseError` - 251 edges
7. `Player` - 231 edges
8. `EventBus` - 210 edges
9. `CombatParticipant` - 195 edges
10. `log_and_raise()` - 189 edges

## Surprising Connections (you probably didn't know these)
- `Arkham City Graph PNG` --semantically_similar_to--> `Simple Room Graph - Arkham City`  [INFERRED] [semantically similar]
  data/local/arkham_city_graph.png → data/local/simple_room_visualization.html
- `MythosMUD Code Quality AI Skill` --semantically_similar_to--> `Lizard Complexity Config`  [INFERRED] [semantically similar]
  .claude/skills/mythosmud-code-quality-ai/SKILL.md → .codacy/tools-configs/lizard.yaml
- `correct_async_logging()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/correct_patterns.py → server/structured_logging/logging_context.py
- `correct_async_logging()` --calls--> `clear_request_context()`  [INFERRED]
  docs/examples/logging/correct_patterns.py → server/structured_logging/logging_context.py
- `register_error_handlers()` --indirect_call--> `http_exception_handler()`  [INFERRED]
  server/middleware/error_handling_middleware.py → docs/examples/logging/fastapi_integration.py

## Import Cycles
- 2-file cycle: `client/src/components/map/useAsciiMap.ts -> client/src/components/map/useAsciiMapState.ts -> client/src/components/map/useAsciiMap.ts`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/realtime/connection_cleanup_methods.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_cleanup_methods.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- 4-file cycle: `server/realtime/connection_establishment.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_establishment.py`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`

## Hyperedges (group relationships)
- **Async Migration Strategy** — docs_archive_anyio_code_review, docs_archive_anyio_vs_asyncio_comparison, docs_archive_websocket_code_review [EXTRACTED 0.85]
- **Codacy Static Analysis Configuration** — codacy_cli_config, codacy_tools_configs_analysis_options, codacy_tools_configs_languages_config, github_instructions_codacy_instructions [EXTRACTED 0.90]
- **Connection Resilience & State Management** — docs_architecture_decisions_adr_011_xstate_frontend_fsm, docs_architecture_decisions_adr_012_python_statemachine_backend, docs_architecture_decisions_adr_014_nats_error_boundaries, docs_architecture_decisions_adr_018_new_game_session_replacement [EXTRACTED 0.90]
- **Express.js Security Audit Rules** — javascript_express_ssrf, javascript_express_xxe, javascript_express_object_deserialization, javascript_express_jwt_hardcoded_secret [EXTRACTED 0.90]
- **Java Security Audit Rules** — java_security_xpath_injection, java_security_unvalidated_redirect, java_security_weak_ssl, java_security_xss_response_writer, java_security_xxe_documentbuilderfactory, java_security_path_traversal, java_security_jms_deserialization, java_security_jackson_deserialization [EXTRACTED 0.90]
- **Agent Instruction Hierarchy** — agents_md, claude_md, user_rules_md [EXTRACTED 1.00]
- **Agent Instruction Stack** — agents_md, claude_md, user_rules_md, claude_agents_routing [EXTRACTED 1.00]
- **Lucidity hallucination effects group** — docs_archive_lucidity_system_lucidity_system, docs_archive_phantom_hostile_requirements_phantom_hostiles, docs_archive_reversed_compass_directions_requirements_reversed_compass [EXTRACTED 1.00]
- **December 2025 Async Remediation Document Set** — docs_archive_async_audit_executive_summary_async_audit_executive_summary, docs_archive_async_persistence_migration_tracker_async_persistence_migration_tracker, docs_archive_async_remediation_complete, docs_archive_async_remediation_final_report, docs_archive_async_remediation_summary_2025_12_03 [EXTRACTED 1.00]
- **Audit Workflow: Design ↔ Implementation Drift** — data_mythosmud_obsidian_design_audit_2026_08_18_p2_structural_claims, data_mythosmud_obsidian_design_audit_2026_08_18_p3_cluster_configapi, data_mythosmud_obsidian_design_audit_2026_08_18_p4_intent_core_issues, data_mythosmud_obsidian_design_audit_2026_08_18_p5_refutation, data_mythosmud_obsidian_design_audit_2026_08_18_p6_review_queue, data_mythosmud_obsidian_design_audit_2026_08_18_p7_rulings, data_mythosmud_obsidian_design_audit_2026_08_18_p8_applied [EXTRACTED 1.00]
- **Chaosium Source Catalog Group** — wiki_sources_nameless_horrors_2nd_edition, wiki_sources_petersens_abominations, wiki_sources_pulp_cthulhu, wiki_sources_reign_of_terror, wiki_sources_s_petersens_field_guide, data_mythosmud_obsidian_wiki_syntheses_chaosium_coc_catalog_chaosium_coc_catalog [EXTRACTED 1.00]
- **Client panel separation triad** — docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_chat_panel, docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_game_log_panel, docs_archive_advanced_chat_channels_spec_chat_panel_separation_documentation_commands_panel [EXTRACTED 1.00]
- **Uncoordinated NPC startup spawners** — docs_archive_npc_startup_duplication_analysis_npc_startup_service, docs_archive_npc_startup_duplication_analysis_npc_lifecycle_manager, docs_archive_npc_startup_duplication_analysis_npc_population_controller [EXTRACTED 1.00]
- **Container inventory synchronization cluster** — investigations_remediation_plans_2025_01_27_container_sync_remediation_container_sync_bug, investigations_sessions_2025_01_27_session_001_inventory_slot_calculation_bug_inventory_slot_bug, investigations_sessions_2025_01_27_session_001_inventory_slot_calculation_bug_dual_storage [EXTRACTED 1.00]
- **Enhanced logging f-string compliance cluster** — investigations_sessions_2025_01_28_session_enhanced_logging_compliance_audit_logging_audit, investigations_sessions_2025_01_28_session_fstring_violations_remediated_fstring_remediation, investigations_sessions_2025_01_28_session_pre_commit_hook_analysis_precommit_gaps, investigations_sessions_2025_01_28_session_pre_commit_hook_fix_ast_fstring_detector [EXTRACTED 1.00]
- **December 3 character and occupants UI cluster** — investigations_sessions_2025_12_03_final_summary_dec3_summary, investigations_sessions_2025_12_03_session_001_character_info_panel_character_info_stats, investigations_sessions_2025_12_03_session_002_room_occupants_display_occupants_duplicates [EXTRACTED 1.00]
- **Client Layout and Typography Specs** — docs_client_layout_baseline, docs_client_typography_layout_spec [EXTRACTED 1.00]
- **Codacy Remediation Campaign** — docs_archive_investigations_codacy_high_critical_baseline, docs_archive_investigations_codacy_high_critical_progress [EXTRACTED 1.00]
- **Command Development Framework** — docs_command_handler_patterns, docs_command_models_reference, docs_command_security_guide, docs_command_testing_guide [EXTRACTED 1.00]
- **MythosMUD Complexity Checking Strategy** — docs_archive_linting_complexity_alignment_ruff_c901, docs_archive_linting_complexity_alignment_pylint_r091x, docs_archive_linting_complexity_alignment_mccabe_cyclomatic_complexity, docs_archive_lizard_complexity_findings_ccn_threshold [EXTRACTED 1.00]
- **Cursor Tooling Suite** — docs_cursor_cli, docs_cursor_hooks, docs_cursor_setup_guide, docs_cursor_subagents, docs_cursor_workflows [EXTRACTED 1.00]
- **Database Architecture & Configuration** — docs_database_access_patterns, docs_database_pool_configuration [EXTRACTED 1.00]
- **Historical pre-authoritative DDL verification snapshots** — db_verification_ddl_status_historical_partial_status, db_verification_ddl_final_status_historical_final_status, db_verification_ddl_verification_summary_historical_summary [EXTRACTED 1.00]
- **Design Audit 2026-08-18** — design_audit_index, data_mythosmud_obsidian_design_audit_2026_08_18_critical_websocket_auth, data_mythosmud_obsidian_design_audit_2026_08_18_c2_revised_ruling, data_mythosmud_obsidian_design_audit_2026_08_18_corrections_corpus_gap, data_mythosmud_obsidian_design_audit_2026_08_18_p0_known_deviations, data_mythosmud_obsidian_design_audit_2026_08_18_p2_adr_claims [EXTRACTED 1.00]
- **Local server start/stop lifecycle scripts** — scripts_readme_start_server, scripts_readme_stop_server, scripts_readme_start_local, scripts_readme_port_54768 [EXTRACTED 1.00]
- **AI execution improvement documentation set** — e2e_tests_ai_execution_improvements_mandatory_execution_protocol, e2e_tests_ai_executor_quick_reference_seven_commandments, e2e_tests_execution_guards_max_step_attempts, e2e_tests_improvements_summary_infinite_loop_prevention [EXTRACTED 1.00]
- **Whisper Phase 3 NATS review artifacts** — e2e_tests_phase_3_complete_summary_phase_3_code_review, e2e_tests_phase_3_code_review_findings_nats_subject_manager, e2e_tests_phase_3_task_2_subject_manager_review_dual_path_subject_construction, e2e_tests_phase_3_task_3_documentation_review_nats_subject_patterns_doc [EXTRACTED 1.00]
- **Frontend Design System** — claude_skills_frontend_design_reference_color_and_contrast, claude_skills_frontend_design_reference_interaction_design, claude_skills_frontend_design_reference_motion_design, claude_skills_frontend_design_reference_responsive_design, claude_skills_frontend_design_reference_spatial_design, claude_skills_frontend_design_reference_typography, claude_skills_frontend_design_reference_ux_writing [EXTRACTED 1.00]
- **Frontend Tooling Stack** — claude_rules_vite_config, claude_rules_vitest_vitest_best_practices, claude_rules_zustand_best_practices [EXTRACTED 1.00]
- **Game Subsystem Design Documents** — docs_subsystems_subsystem_admin_commands_design, docs_subsystems_subsystem_combat_design, docs_subsystems_subsystem_emote_pose_design, docs_subsystems_subsystem_follow_design, docs_subsystems_subsystem_lucidity_design, docs_subsystems_subsystem_magic_design, docs_subsystems_subsystem_movement_design, docs_subsystems_subsystem_npc_design, docs_subsystems_subsystem_party_design, docs_subsystems_subsystem_rescue_design, docs_subsystems_subsystem_respawn_design, docs_subsystems_subsystem_rest_design, docs_subsystems_subsystem_skills_level_design, docs_subsystems_subsystem_status_effects_design, docs_subsystems_subsystem_who_design [EXTRACTED 1.00]
- **Design skills requiring teach-impeccable** — skills_teach_impeccable, skills_onboard, skills_optimize, skills_overdrive, skills_polish, skills_quieter, skills_typeset, skills_design_context_persistence [EXTRACTED 1.00]
- **Earth-plane major geography locations** — data_mythosmud_obsidian_raw_sources_mythosmud_worldbuilding_earth_plane, data_mythosmud_obsidian_raw_sources_geography_major_locations_arkham_city, data_mythosmud_obsidian_raw_sources_geography_major_locations_innsmouth, data_mythosmud_obsidian_raw_sources_geography_major_locations_rlyeh [EXTRACTED 1.00]
- **Effects and grace period cluster** — plans_effects_system_adr_and_implementation, plans_effects_system_implementation, plans_disconnect_grace_period_and_rest, plans_effects_login_warded [EXTRACTED 1.00]
- **Event projection and room handoff authority path** — client_src_components_ui_v2_eventlog_events_schema_event_projector, client_src_components_ui_v2_eventlog_events_schema_room_state, client_src_components_ui_v2_eventlog_handoffs_enter_room_rr [EXTRACTED 1.00]
- **Frontend-design reference docs** — skills_frontend_design_ref_color_and_contrast, skills_frontend_design_ref_interaction_design, skills_frontend_design_ref_motion_design, skills_frontend_design_ref_responsive_design, skills_frontend_design_ref_spatial_design, skills_frontend_design_ref_typography, skills_frontend_design_ref_ux_writing [EXTRACTED 1.00]
- **Memory leak metrics and remediation** — plans_memory_leak_metrics_collection, plans_memory_leak_remediation, plans_memory_closed_websockets_deque [EXTRACTED 1.00]
- **MOTD listed known zones** — data_local_motd_message_of_the_day, data_local_motd_arkham_city, data_local_motd_innsmouth, data_local_motd_katmandu [EXTRACTED 1.00]
- **Quest gap analysis to implementation** — plans_mud_subsystems_gap_analysis, plans_mud_quest_gap, plans_quest_subsystem_implementation, plans_quest_system [EXTRACTED 1.00]
- **Canonical seed path via authoritative DML** — data_spells_readme_spells_seed_deprecated, data_static_generated_sql_readme_world_and_emotes_sql, data_static_generated_sql_readme_static_seed_deprecated [EXTRACTED 1.00]
- **Knowledge Management Flow** — mythosmud_llm_wiki, chaosium_ingest_pipeline [EXTRACTED 1.00]
- **Alert evaluation and routing pipeline** — monitoring_prometheus_yml_prometheus_config, monitoring_mythos_alerts_yml_alert_rules, monitoring_alertmanager_yml_alertmanager_config [EXTRACTED 1.00]
- **Core monitoring stack services** — monitoring_docker_compose_prometheus, monitoring_docker_compose_alertmanager, monitoring_docker_compose_grafana [EXTRACTED 1.00]
- **MythosMUD Memory System** — mythosmud_llm_wiki, chaosium_ingest_pipeline [EXTRACTED 1.00]
- **MythosMUD Obsidian Vault** — data_mythosmud_obsidian_readme, data_mythosmud_obsidian_index, data_mythosmud_obsidian_log [EXTRACTED 1.00]
- **NATS 2026-01-13 Review and Remediation Cycle** — docs_archive_nats_anti_patterns_review_2026_01_13, docs_archive_nats_remediation_summary_2026_01_13_nats_anti_patterns_remediation_summary, docs_archive_nats_medium_priority_remediation_2026_01_13, docs_archive_nats_complete_remediation_summary_2026_01_13_nats_complete_remediation_summary [EXTRACTED 1.00]
- **Observability & Error Framework** — docs_enhanced_logging_guide, docs_error_handling_guide, docs_error_logging_implementation_guide, docs_memory_leak_metrics_usage_guide [EXTRACTED 1.00]
- **Persistence Async Repository Extraction** — docs_archive_persistence_extraction_complete_persistence_layer, docs_archive_persistence_refactoring_complete_seven_async_repositories, docs_archive_persistence_async_migration_plan_gradual_migration, docs_archive_persistence_extraction_complete_sync_to_async_delegation [EXTRACTED 1.00]
- **Persistence Three Access Paths** — docs_archive_asyncio_code_review_asyncpersistencelayer, docs_archive_asyncio_code_review_persistencelayer, docs_archive_facades_implementation_summary_playerrepository, docs_archive_facades_implementation_summary_complementary_facades [EXTRACTED 1.00]
- **Phase 2 Async Persistence Migration** — docs_archive_phase2_migration_complete, docs_archive_phase2_migration_status, docs_archive_phase2_migration_complete_asyncio_to_thread, docs_archive_asyncio_code_review_event_loop_blocking, docs_archive_phase2_migration_status_passive_lucidity_flux [EXTRACTED 1.00]
- **Migration 019 Schema and ORM Type Alignment** — docs_archive_postgresql_audit_report_2026_migration_019, docs_archive_postgresql_audit_report_2026_identity_ids, docs_archive_postgresql_audit_report_2026_varchar_vs_text, docs_archive_python_model_updates_required_integer_to_biginteger, docs_archive_python_model_updates_required_string_to_text [EXTRACTED 1.00]
- **Project Documentation Core** — readme_md, contributing_md, security_md, testing_md [EXTRACTED 1.00]
- **Python Quality & Linting Stack** — claude_rules_pylint_rule, claude_rules_mypy_rule, claude_rules_pytest_rule, pre_commit_config_yaml, bandit_yml [EXTRACTED 1.00]
- **WebSocket message accept-validate-route-broadcast pipeline** — server_realtime_readme_websocket_api, server_realtime_readme_connection_manager, server_realtime_readme_message_validator, server_realtime_readme_nats_message_handler, server_realtime_readme_room_broadcasts [EXTRACTED 1.00]
- **Room validator core modules** — tools_room_toolkit_room_validator_readme_room_loader, tools_room_toolkit_room_validator_readme_schema_validator, tools_room_toolkit_room_validator_readme_path_validator, tools_room_toolkit_room_validator_readme_reporter, tools_room_toolkit_room_validator_readme_fixer [EXTRACTED 1.00]
- **Multi-character scenario group 27-30** — e2e_tests_scenarios_scenario_27_character_selection_character_selection, e2e_tests_scenarios_scenario_28_multi_character_creation_multi_character_creation, e2e_tests_scenarios_scenario_29_character_deletion_character_soft_deletion, e2e_tests_scenarios_scenario_30_character_name_uniqueness_case_insensitive_name_uniqueness [EXTRACTED 1.00]
- **Skills scenario group 39-41** — e2e_tests_scenarios_scenario_39_skills_new_tab_skills_new_tab, e2e_tests_scenarios_scenario_40_skills_command_skills_slash_command, e2e_tests_scenarios_scenario_41_skills_after_creation_skills_after_creation [EXTRACTED 1.00]
- **Visibility and combat scenarios 34-36** — e2e_tests_scenarios_scenario_34_two_players_same_room_same_room_visibility, e2e_tests_scenarios_scenario_35_player_combat_player_combat, e2e_tests_scenarios_scenario_36_movement_visibility_movement_visibility [EXTRACTED 1.00]
- **Security Rule Definitions** — codacy_tools_configs_semgrep [EXTRACTED 1.00]
- **JSON validate generate merge seed pipeline** — scripts_static_data_readme_generate_sql_mjs, scripts_static_data_readme_ajv_validation, scripts_static_data_readme_world_emotes_sql, scripts_static_data_readme_canonical_dml_merge, scripts_static_data_readme_uuid_v5_namespace [EXTRACTED 1.00]
- **November 2025 Test Quality Audit Family** — docs_archive_test_audit_executive_summary, docs_archive_test_value_distribution, docs_archive_test_pruning_candidates, docs_archive_test_coverage_gaps, docs_archive_test_optimization_roadmap [EXTRACTED 1.00]
- **Chaosium Pack Synthesis** — data_mythosmud_obsidian_raw_chaosium_reign_of_terror_graph_report, data_mythosmud_obsidian_raw_chaosium_s_petersen_s_field_guide_to_lovecraftian_horrors_graph_report, data_mythosmud_obsidian_raw_chaosium_the_grand_grimoire_of_cthulhu_mythos_magic_graph_report, data_mythosmud_obsidian_raw_chaosium_the_malleus_monstrorum_keeper_deck_graph_report, wiki_concepts_graphify_code_graph [EXTRACTED]
- **Database Access Architecture** — db_procedures_readme, docs_database_access_patterns, docs_architecture_decisions_adr_015, data_mythosmud_obsidian_wiki_code_dml_migrations_apply_paths_dml_migrations_apply_paths [EXTRACTED]
- **Dependency Injection Governance** — docs_architecture_decisions_adr_002, docs_container_injection_audit, docs_database_access_patterns [EXTRACTED]
- **MythosMUD Quality Pipeline** — claude_skills_mythosmud_pre_commit_checklist_skill, claude_skills_mythosmud_code_quality_ai_skill, claude_skills_mypy_remediation_skill [EXTRACTED]
- **Combat start XP and second-NPC cluster** — investigations_sessions_2025_12_08_session_combat_start_failure_missing_await, investigations_sessions_2025_12_14_session_002_xp_award_error_investigation_xp_award_error, investigations_sessions_2026_02_04_combat_second_npc_and_linkdead_findings_second_npc_combat [INFERRED 0.75]
- **Explored rooms filtering and minimap cluster** — investigations_sessions_2025_12_07_session_sql_syntax_error_rooms_list_sql_cast_param, investigations_sessions_2026_01_04_session_minimap_explored_rooms_bug_minimap_explored [INFERRED 0.75]
- **GitHub security scanning suite** — github_workflows_codeql_codeql_workflow, github_workflows_dependency_review_dependency_review_workflow, github_workflows_scorecards_scorecard_workflow [INFERRED 0.75]
- **Chat and NATS migration linkage** — docs_archive_planning_redis_to_nats_migration_redis_to_nats, docs_archive_planning_redis_to_nats_migration_nats_service, docs_archive_planning_chat_system_chat_system_plan [INFERRED 0.85]
- **NPC occupants display investigation cluster** — investigations_sessions_2025_01_28_session_npc_display_final_fixes_npc_display_fixes, investigations_sessions_2025_01_28_session_npc_occupants_verification_summary_npc_occupants_verification, investigations_sessions_2025_01_29_session_001_npc_occupants_display_issue_dual_tracking, investigations_sessions_2025_01_30_session_001_npcs_not_updating_on_player_movement_npc_movement_update, investigations_sessions_2025_01_xx_session_npc_spawning_occupants_issue_npc_spawning_display, investigations_sessions_2025_01_xx_session_occupants_npc_display_flat_occupants_list [INFERRED 0.85]
- **Combat messaging and NATS failure cluster** — investigations_sessions_2025_11_19_session_001_nats_message_validation_failure_nats_event_data, investigations_sessions_2025_11_19_session_002_combat_client_crash_combat_client_crash, investigations_sessions_2025_11_19_session_002_combat_message_uuid_display_combat_uuid_display, investigations_sessions_2025_11_19_session_003_combat_messages_dual_panel_display_combat_dual_panel, investigations_sessions_2025_12_01_session_npc_death_messages_not_displaying_npc_death_messages [INFERRED 0.85]
- **Death limbo and respawn investigation cluster** — investigations_sessions_2025_11_19_session_005_respawn_death_screen_loop_limbo_room_id_mismatch, investigations_sessions_2025_11_20_respawn_persistence_bug_investigation_respawn_persistence, investigations_sessions_2025_11_20_session_002_death_posture_bugs_death_posture [INFERRED 0.85]
- **Contribution and triage templates** — github_issue_template_bug_report_bug_report_template, github_issue_template_documentation_documentation_template, github_issue_template_feature_request_feature_request_template, github_pull_request_template_pr_template [INFERRED 0.85]
- **Combat feature plans cluster** — plans_combat_round_system_refactor, plans_combat_bugs_investigation_and_fixes, plans_flee_command_and_effect, plans_first_weapon_switchblade [INFERRED 0.85]
- **WebSocket migration and client message pipeline** — plans_websocket_only_migration, plans_websocket_best_practices_remediation, plans_unify_client_message_handling, plans_websocket_only_architecture [INFERRED 0.85]
- **Dual connection documentation set** — docs_archive_dual_connection_api_reference_dual_connection_api, docs_archive_dual_connection_client_guide_dual_connection_client, docs_archive_dual_connection_deployment_guide_dual_connection_deploy, docs_archive_dual_connection_api_reference_websocket_sse_dual [INFERRED 0.95]
- **Enhanced logging documentation cluster** — docs_archive_implementation_complete_enhanced_logging_complete, docs_archive_logging_implementation_summary_enhanced_logging, docs_archive_logging_migration_complete_logging_migration [INFERRED 0.95]
- **Spell command and casting failure cluster** — investigations_sessions_2025_12_14_session_001_spell_commands_failure_spell_commands_missing, investigations_sessions_2025_12_14_session_002_spell_cast_failure_multiword_spell, investigations_sessions_2025_12_14_session_003_minor_heal_casting_delay_missing_async_heal, investigations_sessions_2025_12_14_session_004_heal_spell_casting_failure_session_boundary [INFERRED 0.95]
- **Command System Documentation Suite** — docs_command_handler_patterns, docs_command_models_reference, docs_command_security_guide, docs_command_testing_guide [INFERRED 0.95]

## Communities (2246 total, 550 thin omitted)

### Community 0 - "NPCCombatIntegrationService"
Cohesion: 0.01
Nodes (212): Check if participant is alive enough to be in combat. For players: alive if DP…, CombatResultCtx, NPCCombatHandlers, Any, NPC Combat Event Handlers. This module handles combat result processing and NPC…, Handle NPC death when combat ends, with defensive exception handling. Args:…, Handle NPC death and related effects., Check if a string is a valid UUID. (+204 more)

### Community 1 - "LucidityService"
Cohesion: 0.02
Nodes (135): PlayerLucidity, Authoritative lucidity state for a single investigator., AsyncSession, datetime, CatatoniaObserverProtocol, clamp_lucidity(), coerce_metadata_dict(), decode_liabilities() (+127 more)

### Community 2 - "PlayerRoomEventHandler"
Cohesion: 0.07
Nodes (33): OccupantSnap, _as_map(), _as_occupant_snap(), _NamedRoom, OccupantsUpdateFn, PlayerRoomEventHandler, JsonMap, Protocol (+25 more)

### Community 3 - "NPCBase"
Cohesion: 0.02
Nodes (117): NPC behavior system for MythosMUD. This module provides the core NPC behavior…, NPCBase, ABC, Get attribute from obj with default to avoid lazy-loading issues., Set npc_type, name, current_room, spawn_room_id from definition., Setup base behavior rules common to all NPCs., Return stats[key] as int, or default if missing/None., Return current_dp, max_dp, dexterity for CombatParticipantData. (+109 more)

### Community 4 - "npc_database.py"
Cohesion: 0.04
Nodes (69): get_postgres_connect_args(), Build connect_args for asyncpg: always a hung-transaction timeout, plus…, close_npc_db(), ensure_npc_database_directory(), get_npc_database_path(), get_npc_engine(), get_npc_session(), get_npc_session_maker() (+61 more)

### Community 5 - "get_logger"
Cohesion: 0.01
Nodes (328): Container API endpoints for unified container system. As documented in the…, Event subscription setup for application startup. Extracted from…, Managed Task Cleanup Service - Runtime Detection for Memory Threshold…, Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task…, # TODO: Improve graceful shutdown with early cancellation # pylint:…, Alias Expansion Logic for MythosMUD. This module handles alias resolution,…, Command Input Utilities for MythosMUD. This module provides utilities for…, Admin permission validation utilities for MythosMUD. This module provides… (+320 more)

### Community 6 - "BaseCommand"
Cohesion: 0.00
Nodes (889): RoomDictList, _apply_exploration_filter_if_needed(), _apply_room_exit_to_memory(), _apply_room_properties_to_memory(), _build_exit_attributes(), create_room_exit(), _create_room_link_in_db(), delete_room_exit() (+881 more)

### Community 7 - "server/dependencies.py"
Cohesion: 0.02
Nodes (128): get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service(), get_level_service() (+120 more)

### Community 8 - "CommunicationCommandFactory"
Cohesion: 0.05
Nodes (60): Unit tests for communication command factories. Tests the…, Test create_me_command() creates MeCommand., Test create_me_command() raises error with no args., Test create_pose_command() creates PoseCommand., Test create_pose_command() allows no args (sets pose to None)., Test create_channel_command() creates ChannelCommand., Test create_channel_command() handles 'default' action., Test create_channel_command() raises error with no args. (+52 more)

### Community 9 - "ContainerComponent"
Cohesion: 0.02
Nodes (128): ContainerComponent, ContainerSourceType, BaseModel, Check if container is locked or sealed., Check if container is unlocked., Check if container has available capacity., Check if container can hold this many items (e.g. when replacing contents)., Get number of used inventory slots. (+120 more)

### Community 10 - "PlayerService"
Cohesion: 0.02
Nodes (164): API module for MythosMUD. This module provides REST API endpoints for the…, Shared FastAPI APIRouter for player endpoints (avoids import cycles with route…, create_player(), delete_character(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), _force_disconnect_character() (+156 more)

### Community 11 - "TransferContainerRequest"
Cohesion: 0.03
Nodes (113): emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), ConnectionManager, UUID, WebSocket event emission helpers for container API endpoints. This module…, Emit WebSocket event for container closing. Args: connection_manager:… (+105 more)

### Community 12 - "NPCDefinition"
Cohesion: 0.04
Nodes (62): NPCDefinition, NPCDefinitionType, StrEnum, NPC database models for MythosMUD. This module defines the SQLAlchemy models…, Initialize NPCDefinition with defaults., String representation of the NPC definition., Check if this NPC can spawn given current population., Apply a default attribute value when SQLAlchemy leaves it unset or None. (+54 more)

### Community 13 - "CombatParticipant"
Cohesion: 0.01
Nodes (228): CombatAction, CombatParticipant, _get_default_damage(), Check if participant is mortally wounded (players only). For players: mortally…, Check if participant can perform voluntary combat actions. Unconscious (DP <=…, Apply damage to this participant and determine resulting death states.…, Get the participant whose turn it is., Get the default damage value from configuration. (+220 more)

### Community 14 - "ConnectionManager"
Cohesion: 0.02
Nodes (140): broadcast_global_event_impl(), broadcast_global_impl(), broadcast_room_event_impl(), broadcast_to_room_impl(), check_all_connections_health_impl(), check_connection_health_impl(), ConnectionManager, convert_room_players_uuids_to_names_impl() (+132 more)

### Community 15 - "sqlalchemy.md"
Cohesion: 0.01
Nodes (248): Shared SQLAlchemy metadata for MythosMUD models. This module provides the…, Base, DeclarativeBase, Shared SQLAlchemy DeclarativeBase for all models. This module provides a single…, Shared declarative base for all MythosMUD models. All models (User, Player,…, HolidayModel, NPCScheduleModel, Base (+240 more)

### Community 16 - "get_npc_instance_service"
Cohesion: 0.02
Nodes (168): Get NPC instance from the spawning service. Public API., Get NPC instance from the spawning service., handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command. (+160 more)

### Community 17 - "test_security_validator.py"
Cohesion: 0.01
Nodes (213): field_validator, Validate alias name format using centralized validation., Validate command content for security using centralized validation., Validate alias name format using centralized validation., field_validator, Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation. (+205 more)

### Community 18 - "MessageFilteringHelper"
Cohesion: 0.05
Nodes (34): MessageFilteringHelper, Any, Pre-load mute data for all potential receivers. Args: user_manager: UserManager…, Extract information from chat event. Args: chat_event: Chat event dictionary…, Determine if mute check should be applied for a channel. Args: channel: Channel…, Compare two room IDs using canonical room ID resolution. Args: player_room_id:…, Get player's current room ID from online players cache. Args: player_id: Player…, Get player's current room ID from async persistence layer. Args: player_id:… (+26 more)

### Community 19 - "ContainerData"
Cohesion: 0.02
Nodes (183): ContainerCreateParams, Shared parameters for container creation (sync DB and async repository paths)., Optional fields for creating a container row (beyond source_type)., ContainerData, ContainerDataCore, ContainerDataExtras, Container data class for persistence operations., Identity and placement fields for a container row. (+175 more)

### Community 20 - "mythos_dev_ddl.sql"
Cohesion: 0.02
Nodes (5): mythos_dev.aliases, mythos_dev.calendar_holidays, mythos_dev.calendar_npc_schedules, mythos_dev.id_map_users, mythos_dev.professions

### Community 21 - "Alias"
Cohesion: 0.01
Nodes (192): Alias, BaseModel, Alias model for command aliases. This module defines the Alias model for…, Alias model for command aliases. Stores player command aliases for quick access…, String representation of the alias., Check equality based on name and command., Hash based on name and command for use in sets/dicts., Update the updated_at timestamp to current time. (+184 more)

### Community 22 - "CombatService"
Cohesion: 0.01
Nodes (247): Return the combat service instance, or None if unavailable., CombatEndedEvent, CombatStartedEvent, CombatTargetSwitchEvent, NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent (+239 more)

### Community 23 - "AsyncPersistenceLayer"
Cohesion: 0.02
Nodes (121): AsyncPersistenceLayer, Any, datetime, Player, Profession, UUID, Set the instance manager for instanced room lookup (instance-first)., Ensure room cache is loaded (lazy loading with lock). This method uses a lock… (+113 more)

### Community 24 - "CommandFactory"
Cohesion: 0.01
Nodes (73): CommandFactory, Create StandCommand from arguments., Create LieCommand from arguments., Create GroundCommand from arguments., Create FollowCommand from arguments., Create UnfollowCommand from arguments., Create FollowingCommand from arguments., Create PartyCommand from arguments. (+65 more)

### Community 25 - "test_npc_utils.py"
Cohesion: 0.03
Nodes (103): Check if this NPC is required to spawn., despawn_npc_impl(), Any, NPC despawn logic for lifecycle. Extracted from lifecycle_manager to keep file…, Prefer live NPC room attrs, then lifecycle SPAWNED/left event room_id., Mutate room occupants or publish NPCLeftRoom; skip unknown rooms., Despawn an NPC instance. Args: manager: NPCLifecycleManager instance. npc_id:…, _remove_npc_from_room_on_despawn() (+95 more)

### Community 26 - "LootAllRequest"
Cohesion: 0.03
Nodes (91): _apply_inventory_stack_defaults(), _as_inventory_dicts(), _as_str_list(), _as_str_object_dict(), _build_container_data_from_dict(), _build_transfer_response(), _coerce_weapon_on_item(), _convert_container_dict_to_container_data() (+83 more)

### Community 27 - "api/character_creation.py"
Cohesion: 0.02
Nodes (197): _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _as_float(), _as_int(), _check_shutdown_status(), _convert_stat_summary_to_stat_summary_model(), create_character_with_stats(), _dispatch_roll_stats() (+189 more)

### Community 28 - "TargetMatch"
Cohesion: 0.03
Nodes (127): Resolve combat target using target resolution service. Public API., Validate target_result and resolve to a live NPC target_match., Resolve combat target using target resolution service., Resolve a typed target match for the given name in the current context., NpcIntegrationStringIdPort, NpcLifecycleManagerPort, NpcSpellDamageTarget, PlayerPersistenceSpellPort (+119 more)

### Community 29 - "PlayerNameExtractor"
Cohesion: 0.02
Nodes (85): PlayerNameExtractor, Any, UUID, Player name extraction and validation utilities. This module provides utilities…, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:…, Perform basic validation on player name (not None, is string, not empty). Args:… (+77 more)

### Community 30 - "mock_lifecycle_manager"
Cohesion: 0.50
Nodes (4): mock_lifecycle_manager(), mock_npc(), fixture, Create a mock lifecycle manager.

### Community 31 - "ContainerServiceError"
Cohesion: 0.04
Nodes (78): ContainerAccessMixin, UUID, Container access validation (ownership, proximity, roles, corpse grace). Mixin…, Return True if player inventory contains the required key item_id., Check if player can unlock the container. Args: container: Container to check…, Access checks for open containers and unlock eligibility., Verify that a container is open by the specified player with the given token.…, as_object_dict() (+70 more)

### Community 32 - "test_container_bundles.py"
Cohesion: 0.03
Nodes (121): ChatBundle, Chat bundle: chat service. Depends on Core (config, persistence), Game…, Initialize chat service., CombatBundle, Combat bundle: player combat, death, respawn, combat service, catatonia,…, Combat-related services., CoreBundle, Core bundle: config, database, tasks, event bus, persistence. First bundle in… (+113 more)

### Community 33 - "test_connection_session_management.py"
Cohesion: 0.06
Nodes (80): _cleanup_old_session_tracking(), _cleanup_player_data_for_session(), _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), handle_new_game_session_impl(), _is_websocket_connected(), Protocol, UUID (+72 more)

### Community 34 - "test_command_parser.py"
Cohesion: 0.02
Nodes (99): Smoke test for command parser., Test basic command parsing., Test command parsing with arguments., Test command parsing with pipes., test_parse_command_basic(), test_parse_command_with_args(), test_parse_command_with_pipes(), command_parser() (+91 more)

### Community 35 - "test_rest_command.py"
Cohesion: 0.04
Nodes (95): Check if player is resting or in login grace period, interrupt rest if needed.…, Check if player is resting or in login grace period, interrupt rest if needed., _begin_seated_rest_countdown(), cancel_rest_countdown(), _check_player_in_combat(), _check_rest_location(), _disconnect_player_intentionally(), _execute_rest_flow() (+87 more)

### Community 36 - "test_exploration_service.py"
Cohesion: 0.04
Nodes (81): _async_session_maker_mock(), exploration_service(), mock_database_manager(), asyncio, fixture, Unit tests for exploration service. Tests the ExplorationService class., Test mark_room_as_explored() returns False when room not found., Test mark_room_as_explored() raises DatabaseError on database failure. (+73 more)

### Community 37 - "test_connection_establishment.py"
Cohesion: 0.07
Nodes (59): _as_mgr(), _FakeEstablishmentManager, _make_manager(), _meta(), asyncio, ConnectionMetadata, UUID, Unit tests for connection establishment. Tests the connection_establishment… (+51 more)

### Community 38 - "NATSService"
Cohesion: 0.06
Nodes (67): NATSUnsubscribeError, Raised when unsubscribe operations fail., NATSService, Unsubscribe from a NATS subject. Args: subject: NATS subject name to…, NATS service for handling pub/sub operations and real-time messaging. This…, Check if NATS client is connected and healthy. Returns: True if connected and…, Get the number of active subscriptions. Returns: Number of active subscriptions, _assert_tracked_coro_closed() (+59 more)

### Community 39 - "ChatService"
Cohesion: 0.02
Nodes (106): ChatService, _publish_room_chat(), ChatMessage, UUID, _rate_limit_result(), Chat service for handling real-time communication between players. This service…, Normalize player identifiers to string form., Send a say message to players in the same room. This method publishes the… (+98 more)

### Community 40 - "ui-v2/types.ts"
Cohesion: 0.05
Nodes (79): PanelManager(), PanelManagerProps, minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapPanelSection(), MinimapPanelSectionProps, ExpandedPanelBody(), EXPANDED_RESIZE_EDGES (+71 more)

### Community 41 - "factory.py"
Cohesion: 0.08
Nodes (37): _apply_cors_env_overrides(), _configure_cors(), CORSConfigDict, CORSConfigOverrides, create_app(), _first_set_env(), _get_cors_config_from_app_config(), _get_default_cors_config() (+29 more)

### Community 42 - "FollowService"
Cohesion: 0.02
Nodes (127): FollowService, ConnectionManager, FollowTargetValue, UserManager, UUID, Follow service for MythosMUD. In-memory follow state: who is following whom…, Fire-and-forget; close coro if no running event loop (e.g. sync unit tests)., Send a command_response-style message to a single player. (+119 more)

### Community 43 - "server/models/game.py"
Cohesion: 0.02
Nodes (148): Item prototype registry for command modules., _apply_player_status_with_grace_check(), _apply_status_effect_to_player(), _grace_period_blocks_negative_status_effect(), _handle_player_status_effect(), _maybe_run_force_flee_effect(), _parse_status_effect_metadata(), Any (+140 more)

### Community 44 - "PlayerEnteredRoom"
Cohesion: 0.01
Nodes (298): ModuleType, _convert_value_for_json(), _convert_value_from_json(), _copy_public_event_attrs(), deserialize_event(), _event_class_from_payload(), _extract_event_fields(), _init_kwargs_from_event_data() (+290 more)

### Community 45 - "test_inventory_helpers.py"
Cohesion: 0.02
Nodes (134): _equip_stack_from_inventory_index(), _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), normalize_equipped_items(), normalize_inventory_slots(), InventoryStack, Equipment-related helper functions for inventory commands. (+126 more)

### Community 46 - "Communities (355 total, 223 thin omitted)"
Cohesion: 0.02
Nodes (133): Communities (355 total, 223 thin omitted), Community 0 - "Nyarlathotep Avatars", Community 100 - "Call Daoloth / Daoloth", Community 101 - "Call Nyogtha / Clutch of Nyogtha", Community 102 - "Call Saaitii / Saaitii", Community 103 - "Call Zu-Che-Quon / Enchant Bells of Horror", Community 104 - "Cast Out Shan / Shaggai", Community 105 - "Casting the Runes / Elder Sign" (+125 more)

### Community 47 - "inventory_equip_command.py"
Cohesion: 0.04
Nodes (86): _equip_build_work(), _equip_inventory_rollback_snapshot(), _equip_persist_or_rollback(), _equip_run_mutation(), _equip_success_payload(), _equip_target_slot_or_error(), _equip_try_inventory_swap(), EquipCommandInventoryStep (+78 more)

### Community 48 - "server/exceptions.py"
Cohesion: 0.02
Nodes (201): get_patterns(), get_subject_statistics(), PatternsResponse, BaseModel, get, post, NATS Subject Management API Controller for MythosMUD. This module provides REST…, Dependency to require admin permissions. Args: current_user: Current… (+193 more)

### Community 49 - "TargetResolutionService"
Cohesion: 0.02
Nodes (154): _format_teach_result(), _get_teach_services(), Any, Teach command handler for learning spells from NPC teachers. This module…, _resolve_npc_teacher(), BaseModel, Target metadata schema for MythosMUD. This module defines Pydantic models for…, Metadata about a target in target resolution. This model represents additional… (+146 more)

### Community 50 - "handle_whisper_command"
Cohesion: 0.07
Nodes (50): handle_reply_command(), handle_whisper_command(), Reply to last whisper sender., asyncio, Unit tests for whisper and reply communication command handlers., Test handle_whisper_command successful execution., Test handle_reply_command with no message., Test handle_reply_command when services are not available. (+42 more)

### Community 51 - "is_player_in_login_grace_period"
Cohesion: 0.04
Nodes (101): Get login grace period status for player., _as_grace(), cancel_login_grace_period(), _EffectPersistence, get_login_grace_period_remaining(), _grace_period_task(), _GraceApp, _GraceAppState (+93 more)

### Community 52 - "test_connection_delegates.py"
Cohesion: 0.03
Nodes (113): _async_callable(), cleanup_dead_websocket_impl(), _close_dead_websocket_if_open(), delegate_connection_cleaner(), delegate_game_state_provider(), delegate_game_state_provider_sync(), delegate_health_monitor(), delegate_health_monitor_sync() (+105 more)

### Community 53 - "ZoneConfiguration"
Cohesion: 0.03
Nodes (101): Determine if an NPC should spawn based on conditions. Args: definition: NPC…, _population_allows_spawn(), Any, Spawn Validator Module. This module provides logic for validating whether NPCs…, Determine if an NPC should spawn based on conditions. Args: definition: NPC…, Return False when zone population blocks this NPC definition., Evaluate one spawn rule; return True when probability roll succeeds., Return True when any spawn rule passes probability checks. (+93 more)

### Community 54 - "chat_service.py"
Cohesion: 0.04
Nodes (84): ChatResult, _append_channel_history(), _authorize_global_sender(), _authorize_system_sender(), ChatEmoteService, ChatLogger, ChatPlayerService, ChatPlayerView (+76 more)

### Community 55 - "StandardizedErrorResponse"
Cohesion: 0.04
Nodes (57): JSONResponse, post, Request, Receive and log alert webhooks, webhook(), _contains_file_path_in_exception(), _contains_sensitive_exception_pattern(), create_standardized_error_response() (+49 more)

### Community 56 - "MPRegenerationService"
Cohesion: 0.14
Nodes (14): MPRegenerationService, Any, UUID, Get MP regeneration multiplier based on player state. Args: stats: Player stats…, Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…, Restore MP from meditation (highly accelerated regeneration). Args: player_id:…, Restore MP from consuming an item. Args: player_id: Player ID amount: Amount of…, Service for managing MP regeneration. Handles passive regeneration over time… (+6 more)

### Community 57 - "SpellEffectType"
Cohesion: 0.04
Nodes (107): List all spells, optionally filtered by school. Args: school: Optional school…, Load all spells from the database into memory. This should be called during…, BaseModel, StrEnum, Spell data models for the magic system. This module contains Pydantic models…, Valid target types for spells., Valid range types for spells., Valid effect types for spells. (+99 more)

### Community 58 - "server/schemas/__init__.py"
Cohesion: 0.01
Nodes (360): create_dialogue_definition(), delete_dialogue_definition(), get_dialogue_definition(), list_dialogue_definitions(), delete, get, post, put (+352 more)

### Community 59 - "command_handler_unified.py"
Cohesion: 0.01
Nodes (158): clean_command_input(), normalize_command(), Clean and normalize command input by collapsing multiple spaces and stripping…, Normalize command input by removing optional slash prefix. Supports both…, Command Handler Package for MythosMUD. This package provides modular components…, _check_all_command_blocks(), _check_casting_state(), _check_grace_period_block() (+150 more)

### Community 60 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (128): asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not…, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes. (+120 more)

### Community 61 - "config/models/__init__.py"
Cohesion: 0.09
Nodes (23): Composite application configuration model., ChatConfig, BaseSettings, field_validator, Chat and time configuration models., Chat system configuration., Validate rate limits are reasonable., Temporal compression configuration for the MythosChronicle. (+15 more)

### Community 62 - "test_rescue_service.py"
Cohesion: 0.04
Nodes (75): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+67 more)

### Community 63 - "admin_shutdown_command.py"
Cohesion: 0.10
Nodes (39): _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state(), countdown_loop(), _create_countdown_task() (+31 more)

### Community 64 - "test_user_manager.py"
Cohesion: 0.02
Nodes (97): Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() successfully globally mutes a player., Test mute_global() fails when trying to mute admin. (+89 more)

### Community 65 - "test_go_command.py"
Cohesion: 0.05
Nodes (78): _cancel_rest_if_moving(), _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement(), handle_go_command(), _movement_combat_and_event_bus_from_go_app(), _movement_service_for_go_command(), Any (+70 more)

### Community 66 - "UtilityCommandFactory"
Cohesion: 0.03
Nodes (106): Unit tests for utility command factories. Tests the UtilityCommandFactory class…, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+98 more)

### Community 67 - "test_users.py"
Cohesion: 0.03
Nodes (118): AuthenticationBackend, Authentication module for MythosMUD. This package contains all authentication-…, JWT strategy that rejects tokens issued before the current server start., RestartInvalidatingJWTStrategy, get_auth_backend(), get_user_db(), get_user_manager(), get_username_auth_backend() (+110 more)

### Community 68 - "test_combat_flee_handler.py"
Cohesion: 0.07
Nodes (59): check_involuntary_flee(), _check_involuntary_flee_with_session(), execute_voluntary_flee(), _handle_failed_voluntary_flee(), _involuntary_flee_on_cooldown(), Any, UUID, Combat flee handler for involuntary and voluntary flee logic. Handles checking… (+51 more)

### Community 69 - "NATSError"
Cohesion: 0.02
Nodes (182): CombatResult, Result of a combat action., CombatDPSync, Any, Get persistence layer from application container. Args: player_id: Player ID…, Verify that player DP was successfully saved to database. Args: persistence:…, Log death threshold events based on DP changes. Args: current_dp: New current…, Update player DP and save to database. Args: persistence: Persistence layer… (+174 more)

### Community 70 - "test_command_validator.py"
Cohesion: 0.02
Nodes (137): _dispatch_parsed_command(), _handle_processing_error(), _handle_validation_error(), _log_security_sensitive_command(), _parse_command_line_or_client_error(), process_command_with_validation(), CommandExecutionRequest, Exception (+129 more)

### Community 71 - "RoomLoader"
Cohesion: 0.03
Nodes (75): option, fixture, Create a temporary directory for testing., temp_dir(), Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer (+67 more)

### Community 72 - "communication_commands_flows.py"
Cohesion: 0.06
Nodes (59): _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_global_command(), flow_local_command(), flow_reply_command(), flow_system_command(), flow_whisper_command(), _player_id_bundle() (+51 more)

### Community 73 - "test_look_container.py"
Cohesion: 0.02
Nodes (209): _as_map(), _as_map_list(), _as_uuid(), _container_name(), _ContainerPersistence, _extract_container_metadata(), _fetch_container(), _find_container_in_room() (+201 more)

### Community 74 - "test_player_respawn_service.py"
Cohesion: 0.03
Nodes (87): PositionState, Permitted posture states for a character., datetime, Player Respawn Service for managing player resurrection and limbo state. This…, Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE., _utc_now(), mock_event_bus(), mock_player_combat_service() (+79 more)

### Community 75 - "GameClientV2.tsx"
Cohesion: 0.04
Nodes (75): formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, computeLucidityBar(), formatChange(), LucidityChangeFooter(), LucidityMeter (+67 more)

### Community 76 - "PopulationStats"
Cohesion: 0.03
Nodes (66): Handle player entering a room., Handle player leaving a room., Update the current player count in game state., Get zone configuration for a given zone key. Args: zone_key: Zone key in format…, Get population statistics for a given zone. Args: zone_key: Zone key in format…, Check if NPCs need to be spawned for a specific room. Args: room_id: The room…, After lifecycle_manager.spawn_npc succeeds, update zone aggregates and log.…, Spawn an NPC instance using the lifecycle manager. Args: definition: NPC… (+58 more)

### Community 77 - "ApplicationContainer"
Cohesion: 0.03
Nodes (87): Raise if prerequisites for NATS combat are missing., Create CombatService with NATS and register it. Assumes NATS is connected., Start NATS message handler if available. Logs and swallows errors., Handle case when NATS is not connected. Raises in prod, sets combat_service to…, Initialize NATS-dependent combat service and start NATS message handler., Failover callback that relocates catatonic players to the sanitarium., Shutdown core services., Shutdown log aggregator. (+79 more)

### Community 78 - "test_admin_commands.py"
Cohesion: 0.03
Nodes (103): handle_admin_command(), _handle_admin_status_command(), _handle_admin_time_command(), Any, Expose current Mythos time metadata, active holidays, and freeze diagnostics., Entry point for general admin commands that expose subcommands like `admin…, Provide contextual status information about the caller's administrative…, _collect_mute_display_lines() (+95 more)

### Community 79 - "test_combat_persistence_handler_events.py"
Cohesion: 0.06
Nodes (43): mock_combat_service(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully., Test _publish_player_dp_update_event_impl handles no NATS service., Test _publish_player_dp_update_event_impl with all optional parameters. (+35 more)

### Community 80 - "NATSConnectionStateMachine"
Cohesion: 0.03
Nodes (92): ConnectionEvent, NATSConnectionStateMachine, Enum, Exception, Connection state machine for NATS messaging. Implements a robust state machine…, Initialize connection state machine. Args: connection_id: Unique identifier for…, Handler for connect transition. Resets reconnection counter and prepares for…, Handler for successful connection. Records connection time and increments… (+84 more)

### Community 81 - "test_command_processor.py"
Cohesion: 0.03
Nodes (71): command_processor(), fixture, Unit tests for command processor. Tests the CommandProcessor class which…, Test process_command_string handles KeyError., Test process_command_string handles RuntimeError., Test _extract_attributes extracts attributes correctly., Test _extract_attributes handles missing attributes., Test _is_combat_command returns True for attack command. (+63 more)

### Community 82 - "item_instance_persistence.py"
Cohesion: 0.05
Nodes (63): CreateItemInstanceInput, EnsureItemInstanceInput, TypedDict, Constants and shared types for async persistence layer. Extracted to keep…, Optional fields for create_item_instance. owner_type, owner_id, etc. with…, Optional fields for ensure_item_instance., Create a new item instance. Delegates to ItemRepository., create_item_instance_async() (+55 more)

### Community 83 - "test_who_commands.py"
Cohesion: 0.03
Nodes (110): Utility commands for MythosMUD. This module contains handlers for utility…, filter_online_players(), filter_players_by_name(), format_player_entry(), format_player_location(), format_who_result(), get_players_for_who(), handle_who_command() (+102 more)

### Community 84 - "ExplorationService"
Cohesion: 0.05
Nodes (106): _MapRooms, MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter…, _apply_exploration_filter_if_needed(), _AsciiMapViewport, _build_ascii_map_response(), _build_ascii_minimap_response() (+98 more)

### Community 85 - "look_helpers.py"
Cohesion: 0.04
Nodes (59): _AppWithState, _async_persistence_from_app(), _ContainerWithPersistence, _EquippedPlayer, _get_wearable_container_service(), _parse_instance_number(), Protocol, Helper functions for look command. This module contains utility functions used… (+51 more)

### Community 86 - "ExplorationCommandFactory"
Cohesion: 0.06
Nodes (52): Unit tests for exploration command factories. Tests the…, Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_following_command() creates FollowingCommand with no args., Test create_following_command() raises error with args., Test create_party_command() with no args returns status-only command., Test create_party_command() with invite and target. (+44 more)

### Community 87 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.05
Nodes (73): _dispatch_player_event(), _format_liabilities(), LucidityChangeEventExtras, LiabilityStackEntry, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send rescue progress/status updates to either participant. (+65 more)

### Community 88 - "Any"
Cohesion: 0.13
Nodes (12): Any, Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits…, Build exit lookup map from room data., Center viewport on the character's current room so the player is in the middle…, Render a single row of rooms with horizontal exits., Render an ASCII map as HTML. Args: rooms: List of room dictionaries with…, Return the horizontal exit character (—, >, or <) given east/west exit state,… (+4 more)

### Community 89 - "test_websocket_initial_state.py"
Cohesion: 0.02
Nodes (148): get_container_async_persistence(), Get the container-backed AsyncPersistenceLayer instance. Use for code that has…, convert_npc_ids_to_names(), enrich_room_data_with_occupant_names(), extract_occupant_names(), get_npc_name_from_lifecycle_manager(), merge_player_lists(), prepare_room_data_for_respawn() (+140 more)

### Community 90 - "test_nats_service_pool.py"
Cohesion: 0.08
Nodes (31): nats_config(), nats_service(), asyncio, fixture, Unit tests for NATSServicePoolMixin's exception-handling and retry branches.…, _cleanup_connection_pool's outer try/except tolerates a failure enumerating the…, publish_batch returns False (not raise) when subject validation rejects the…, publish_batch's outer handler catches an unexpected exception and returns False. (+23 more)

### Community 91 - "sample_container"
Cohesion: 0.29
Nodes (7): mock_prototype_registry(), fixture, Create a sample container., Create a sample equipped container item., Create a mock prototype registry., sample_container(), sample_equipped_container()

### Community 92 - "ConnectionManager"
Cohesion: 0.02
Nodes (97): ConnectionManager, Player, UUID, Check if a WebSocket ID is in the closed set., Mark a WebSocket ID as closed., Get the count of closed WebSocket IDs being tracked., Get the first WebSocket connection ID for a player (backward compatibility)., Check if a player has any WebSocket connections. (+89 more)

### Community 93 - "test_chat_npc_system.py"
Cohesion: 0.05
Nodes (66): _ChatDeliveryService, deliver_npc_room_speech(), deliver_personal_system(), npc_sender_id(), _on_npc_spoke(), Protocol, UUID, NPC and personal system chat delivery via ChatService (issue #146 MVP). #… (+58 more)

### Community 94 - "api/player_effects.py"
Cohesion: 0.04
Nodes (102): EffectHandler, apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest (+94 more)

### Community 95 - "catatonia_check.py"
Cohesion: 0.03
Nodes (71): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+63 more)

### Community 96 - "CombatInstance"
Cohesion: 0.01
Nodes (382): _apply_taunt_and_maybe_broadcast(), AppWithState, Protocol, UUID, Taunt command flow: validation and execution. Extracted from combat.py to…, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Apply taunt and broadcast target switch if aggro changed. Returns error dict or… (+374 more)

### Community 97 - "test_auth_utils.py"
Cohesion: 0.02
Nodes (195): PasswordHasher, E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio. (+187 more)

### Community 98 - "test_room_sync_service.py"
Cohesion: 0.03
Nodes (75): ChatLogger, ConnectionManager, Initialize the player event handler. Args: connection_manager:…, T, Clear room data cache. Args: room_id: Specific room ID to clear, or None to…, Enhanced room synchronization service. Provides improved event processing…, Process events with proper ordering to prevent race conditions. Args: event:…, RoomSyncService (+67 more)

### Community 99 - "EventBus"
Cohesion: 0.02
Nodes (186): EventBusMixinBase, Attrs/methods provided by EventBus when mixed in., Start the async consumer. Real impl is EventBusLifecycleMixin., Drain the event queue. Real impl is EventBusProcessingMixin., Drop tracked service handlers. Real impl is EventBus., EventBus, EventBusProcessingMixin, Exception (+178 more)

### Community 100 - "player_event_handlers_state.py"
Cohesion: 0.06
Nodes (49): _attach_dp_updated_posture_fields(), _decay_previous_position_before_lying(), _dispatch_player_dp_decay_payload(), _dispatch_player_dp_updated_payload(), _dp_player_update_payload(), _dp_posture_from_stats(), _maybe_attach_decay_posture_cross(), _player_snapshot_for_dp() (+41 more)

### Community 101 - "admin_teleport_commands.py"
Cohesion: 0.05
Nodes (83): Admin teleport command handlers for MythosMUD. This module provides handlers…, broadcast_teleport_effects(), get_online_player_by_display_name(), notify_player_of_teleport(), Any, Teleport utility functions for admin commands in MythosMUD. This module…, Notify a player that they are being teleported by an admin. Args:…, Get online player information by display name. Args: display_name: Display name… (+75 more)

### Community 102 - "test_manager.py"
Cohesion: 0.03
Nodes (75): Unit tests for NATS Subject Manager. Tests the NATSSubjectManager class., Test build_subject() raises SubjectValidationError for invalid parameter., Test build_subject() raises SubjectValidationError when subject too long., Test validate_subject() returns True for valid subject., Test validate_subject() returns False for invalid subject., Test validate_subject() accepts events.domain.{event_type} (distributed…, Test validate_subject() returns False for empty subject., Test validate_subject() uses cache for repeated validations. (+67 more)

### Community 103 - "DistributedEventBus"
Cohesion: 0.05
Nodes (40): DistributedEventBus, Any, Distributed EventBus that uses NATS for cross-instance event distribution.…, EventBus that distributes domain events via NATS for horizontal scaling. When…, Initialize distributed EventBus. Args: nats_service: NATS service for…, Set NATS service and start the bridge (call after NATS connects)., Publish event locally and to NATS when bridge is active., Shutdown EventBus and stop NATS bridge. (+32 more)

### Community 104 - "test_corpse_lifecycle_service.py"
Cohesion: 0.04
Nodes (72): CorpseNotFoundError, CorpseServiceError, _get_enum_value(), Corpse lifecycle service for unified container system. As documented in the…, Safely get enum value, handling both enum instances and string values. When…, Base exception for corpse service operations., Raised when a corpse container is not found., corpse_service() (+64 more)

### Community 105 - "test_combat_monitoring_service.py"
Cohesion: 0.03
Nodes (91): AlertSeverity, AlertType, CombatMetrics, end_combat_monitoring(), get_combat_metrics(), get_combat_monitoring(), Enum, Combat monitoring and alerting service for MythosMUD. This service provides… (+83 more)

### Community 106 - "test_lifespan_startup.py"
Cohesion: 0.06
Nodes (60): _get_item_prototype_count(), _get_item_prototype_entries(), initialize_container_and_legacy_services(), Initialize container and set up container reference on app.state. Services are…, Raise if prerequisites for NPC services are missing., Return raw entries from the item prototype registry, or None on error., Get count of item prototypes from registry., _validate_npc_services_prerequisites() (+52 more)

### Community 107 - "get_session_maker"
Cohesion: 0.05
Nodes (53): get_10_active_invites(), main(), Get 10 active invite codes from the database., get_session_maker(), Get the async session maker from DatabaseManager. Returns: async_sessionmaker:…, _coerce_row_stats(), _defaulted_numerics(), _defaulted_strings() (+45 more)

### Community 108 - "InventoryService"
Cohesion: 0.05
Nodes (55): AbstractContextManager, InnerContainer, InventoryCapacityError, InventoryService, InventoryServiceError, InventorySplitError, InventoryStackRequired, InventoryValidationError (+47 more)

### Community 109 - "Stats"
Cohesion: 0.04
Nodes (61): Core character statistics with Lovecraftian horror elements., Get the modifier for a given attribute (standard D&D-style calculation)., Check if the character is still mentally clear., Check if the character has significant corruption., Check if the character has lost their lucidity completely., Stats, Unit tests for Stats model methods. Tests Stats computed fields, methods, and…, Test max_magic_points() calculation with specific power. (+53 more)

### Community 110 - "test_room_renderer.py"
Cohesion: 0.04
Nodes (64): Unit tests for room_renderer utility functions. Tests the utility functions in…, Test clone_room_drops() returns empty list for None., Test format_room_drop_lines() formats room drops., Test format_room_drop_lines() returns empty message for empty drops., Test format_room_drop_lines() handles None., Test format_room_drop_lines() uses fallback for missing item_name., Test build_room_drop_summary() returns newline-separated summary., Test build_room_drop_summary() handles empty drops. (+56 more)

### Community 111 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (88): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+80 more)

### Community 112 - "test_websocket_room_updates.py"
Cohesion: 0.03
Nodes (126): _apply_grace_badges(), format_occupant_display_name(), _parse_occupant_player_id(), Any, UUID, Shared occupant display names for look text and Occupants panel events., Format an in-room player's Occupants/look name. Always list; grace badges only., connection_manager_from_running_app() (+118 more)

### Community 113 - "test_real_time_helpers.py"
Cohesion: 0.12
Nodes (27): handle_new_game_session(), post, Validate connection manager and accept WebSocket connection. Returns True if…, Handle a new game session for a player. This will disconnect existing…, Prefer the supplied manager; otherwise the container singleton. Static import…, Resolve player ID from a valid JWT. Path UUID is an identity check, not a…, resolve_connection_manager(), _resolve_player_id_from_path_or_token() (+19 more)

### Community 114 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.05
Nodes (86): object, _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch() (+78 more)

### Community 115 - "QuestService"
Cohesion: 0.04
Nodes (69): Persist player after spell mutations., Quest subsystem: service, goal progression, rewards., notify_quest_abandoned(), notify_quest_completed(), notify_quest_progress(), notify_quest_started(), UUID, Personal system chat when a quest becomes active. (+61 more)

### Community 116 - "api/monitoring.py"
Cohesion: 0.05
Nodes (103): force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_memory_alerts(), get_memory_leak_metrics(), get_memory_stats() (+95 more)

### Community 117 - "test_npc_models.py"
Cohesion: 0.03
Nodes (61): Base, NPCRelationship, DeclarativeBase, NPC relationship model. Defines relationships between different NPC types., String representation of the NPC relationship., SQLAlchemy declarative base for NPC database models., Unit tests for NPC models. Tests the NPCDefinitionType enum and NPCDefinition,…, Test NPCDefinition.set_base_stats() serializes to JSON. (+53 more)

### Community 118 - "test_player_presence_tracker.py"
Cohesion: 0.04
Nodes (91): _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _disconnect_during_rest_is_intentional(), _get_instance_manager_from_manager(), Any, UUID, Player presence tracking helper for connection manager. This module provides… (+83 more)

### Community 119 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (90): _collect_rotatable_logs(), detect_environment(), ensure_log_directory(), BoundLogger, Path, Logging utilities for directory management, path resolution, and environment…, Resolve log_base path to absolute path relative to project root. Args:…, Collect non-empty log files eligible for rotation. (+82 more)

### Community 120 - "test_look_player.py"
Cohesion: 0.03
Nodes (118): _get_health_label(), _get_lucidity_label(), _get_visible_equipment(), Get descriptive health label based on health percentage. Args: stats:…, Get descriptive lucidity label based on lucidity percentage. Args: stats:…, Get visible equipment from player, excluding internal/hidden slots. Visible…, _stat_number(), _apply_grace_period_labels() (+110 more)

### Community 121 - "UserManager"
Cohesion: 0.07
Nodes (34): UUID, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Add a player as an admin. Args: player_id: Player ID player_name: Player name…, Get the mute data file path for a specific player., Load channel mutes from JSON data into memory., Update cache to mark load as failed., Convert mute_info datetime and UUID objects to JSON-serializable formats. (+26 more)

### Community 122 - "EventHandler"
Cohesion: 0.05
Nodes (48): _as_event_data_dict(), EventHandler, _npc_died_broadcast_and_bridge(), _npc_died_ids_or_warn(), _participant_key_strings(), _publish_npc_died_to_event_bus(), ConnectionManager, Publish NPCDied to the in-process EventBus when configured on ConnectionManager. (+40 more)

### Community 123 - "FeatureFlagService"
Cohesion: 0.03
Nodes (54): Initialize the combat configuration service., FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature… (+46 more)

### Community 124 - "Reporter"
Cohesion: 0.03
Nodes (47): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+39 more)

### Community 125 - "resolve_lazy_attr"
Cohesion: 0.07
Nodes (37): broadcast_game_event(), _ConnectionManagerAPI, Protocol, UUID, Send a system notification to a player. Args: player_id: The player's ID…, Send a player status update to a player. Args: player_id: The player's ID…, Send room description to a player. Args: player_id: The player's ID room_data:…, Structural type for API helpers; avoids importing ConnectionManager. (+29 more)

### Community 126 - "test_player_death_service.py"
Cohesion: 0.03
Nodes (87): mock_event_bus(), mock_player(), mock_player_combat_service(), mock_session(), player_death_service(), player_death_service_no_dependencies(), asyncio, fixture (+79 more)

### Community 127 - "test_connection_helpers_impl.py"
Cohesion: 0.04
Nodes (86): broadcast_global_event_impl(), broadcast_room_event_impl(), convert_uuids_to_strings(), _optimize_payload(), Any, _queue_message_if_needed(), Queue message for later delivery if no active connections. Args: player_id: The…, Update final delivery status based on connection results. Args:… (+78 more)

### Community 128 - "test_alias_commands.py"
Cohesion: 0.05
Nodes (53): mock_alias(), mock_alias_storage(), asyncio, fixture, Unit tests for alias command handlers. Tests the alias, aliases, and unalias…, Test handle_alias_command creating alias from structured data., Test handle_alias_command with alias name too long., Test handle_alias_command with command too long. (+45 more)

### Community 129 - "test_character_creation_service.py"
Cohesion: 0.04
Nodes (50): character_creation_service(), mock_player_service(), fixture, Unit tests for character creation service. Tests the CharacterCreationService…, Test roll_character_stats() when required_class is not available., Test roll_character_stats() handles ValueError., Test validate_character_stats() with class_name., Test validate_character_stats() without class_name. (+42 more)

### Community 130 - "test_quest_service.py"
Cohesion: 0.06
Nodes (82): _DefinitionRow, _FullInventory, _InstanceStub, _make_definition_row(), _make_kill_definition_row(), _make_turn_in_definition_row(), _message(), mock_def_repo() (+74 more)

### Community 131 - "DataProviderProtocol"
Cohesion: 0.32
Nodes (6): DataProviderProtocol, _get_data_provider(), Protocol for room and NPC lookups used by combat helpers., Return current room id for a player id., Return NPC instance for a string NPC id., Safely fetch data provider from integration service.

### Community 132 - "PlayerCombatService"
Cohesion: 0.01
Nodes (223): Spell targeting service for resolving spell targets. This module handles target…, Initialize the spell targeting service. Args: target_resolution_service:…, check_combat_state(), check_player_posture(), extract_player_id(), Any, Room, UUID (+215 more)

### Community 133 - "useMythosAppActions.ts"
Cohesion: 0.03
Nodes (166): CharacterNameScreenProps, CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), extractErrorMessageFromResponseBody() (+158 more)

### Community 134 - "mythos_e2e_ddl.sql"
Cohesion: 0.09
Nodes (42): mythos_e2e.aliases, mythos_e2e.calendar_holidays, mythos_e2e.calendar_npc_schedules, mythos_e2e.container_contents, mythos_e2e.containers, mythos_e2e.dialogue_definitions, mythos_e2e.emote_aliases, mythos_e2e.emotes (+34 more)

### Community 135 - "test_metrics_endpoints.py"
Cohesion: 0.06
Nodes (79): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+71 more)

### Community 136 - "test_status_commands.py"
Cohesion: 0.04
Nodes (81): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_profession_info(), _get_status_persistence(), handle_status_command() (+73 more)

### Community 137 - "mythos_unit_ddl.sql"
Cohesion: 0.09
Nodes (42): mythos_unit.aliases, mythos_unit.calendar_holidays, mythos_unit.calendar_npc_schedules, mythos_unit.container_contents, mythos_unit.containers, mythos_unit.dialogue_definitions, mythos_unit.emote_aliases, mythos_unit.emotes (+34 more)

### Community 138 - "connection_manager_methods.py"
Cohesion: 0.01
Nodes (341): deque, initialize_connection_cleaner(), initialize_connection_state(), initialize_core_components(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging() (+333 more)

### Community 139 - "WebSocketMessageValidator"
Cohesion: 0.06
Nodes (53): MessageValidationError, BaseModel, Exception, WebSocket message validation for MythosMUD. This module provides comprehensive…, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Validate message against Pydantic schema. Args: message: Parsed JSON message…, Raised when message validation fails. (+45 more)

### Community 140 - "test_magic_commands.py"
Cohesion: 0.03
Nodes (84): handler(), mock_chat_service(), mock_magic_service(), mock_player(), mock_player_spell_repository(), mock_spell_learning_service(), mock_spell_registry(), MockEffectType (+76 more)

### Community 141 - "test_npc_service.py"
Cohesion: 0.04
Nodes (87): _def_row(), _mock_result_mappings_all(), mock_session(), npc_service(), asyncio, fixture, Unit tests for NPC service. Tests the NPCService class., Test NPCService initialization. (+79 more)

### Community 142 - "SchemaValidator"
Cohesion: 0.03
Nodes (45): Path, Convert legacy string format exits to new object format internally. This allows…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in… (+37 more)

### Community 143 - "ChatMessage"
Cohesion: 0.07
Nodes (37): ChatMessage, create_and_log_chat_message(), create_and_log_say_message(), Message creation and storage helpers for chat service., Create chat message and log it., Create say chat message and log it., Store message in room history with limit management., Store global message in history. (+29 more)

### Community 144 - "manual_dependency_analysis.py"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 145 - "ErrorType"
Cohesion: 0.02
Nodes (139): ErrorResponseDetailsInput, create_standard_error_response(), create_websocket_error_response(), ErrorContextDetail, ErrorMessages, ErrorResponseDetails, ErrorSeverity, ErrorType (+131 more)

### Community 146 - "GameStateProvider"
Cohesion: 0.06
Nodes (35): GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send… (+27 more)

### Community 147 - "format_message_content"
Cohesion: 0.05
Nodes (45): CircuitBreakerOpen, Exception, Exception raised when circuit breaker is open. Indicates the protected service…, format_message_content(), Format message content based on channel type and sender name. Args: channel:…, _ChatMessageFields, NATSMessageProcessingMixin, _optional_str() (+37 more)

### Community 148 - "DeadLetterQueue"
Cohesion: 0.04
Nodes (69): DeadLetterMessage, DeadLetterQueue, Any, Path, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve and remove oldest message from DLQ (async version). Returns: Message…, Retrieve and remove oldest message from DLQ (sync version). Returns: Message… (+61 more)

### Community 149 - "test_websocket_handler_validation_errors.py"
Cohesion: 0.04
Nodes (62): asyncio, Unit tests for WebSocket handler validation, rate limiting, and error paths.…, _validate_message should pass expected token from connection metadata into…, When metadata.token is missing, validate JWT from message and restore metadata., Test _send_error_response handles WebSocket disconnect., Test _send_error_response handles RuntimeError with disconnect message., Test _send_error_response handles RuntimeError with close message., Test _send_error_response handles other RuntimeError. (+54 more)

### Community 150 - "admin_setstat_command.py"
Cohesion: 0.05
Nodes (66): _apply_stat_change_and_build_result(), _execute_admin_set_stat(), _maybe_attach_dp_posture_message(), _mutate_player_stat(), _notify_player_stat_change(), UUID, Admin command to set player statistics. This module provides the handler for…, Apply DP or generic stat mutation; return previous posture when DP changes. (+58 more)

### Community 151 - "migrate_combat_data.py"
Cohesion: 0.05
Nodes (76): Draft7Validator, add_default_combat_data_to_config(), add_default_combat_data_to_stats(), CombatSchemaValidationError, get_combat_stats_summary(), Any, Exception, Combat system JSON schema validation. This module provides JSON schema… (+68 more)

### Community 152 - "pytest.md"
Cohesion: 0.01
Nodes (527): DependsParam, get_current_user(), Get current user with enhanced logging., get_connection_manager, get_current_active_user, _as_str_object_mapping(), _build_open_container_response(), close_container() (+519 more)

### Community 153 - "test_websocket_handler_app_state_connection.py"
Cohesion: 0.06
Nodes (48): _mirror_service_to_app_state(), WebSocket app.state / container service wiring for command processing.…, Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state. Mutates…, resolve_and_setup_app_state_services(), _services_from_container(), handle_websocket_connection() (+40 more)

### Community 154 - "websocket_handler_commands.py"
Cohesion: 0.09
Nodes (47): _attach_room_state_to_result(), _broadcast_command_room_if_needed(), handle_game_command(), _invoke_get_room_state_event(), parse_game_command_tokens(), process_websocket_command(), WebSocket, WebSocket game command processing (parse, unified handler, broadcast).… (+39 more)

### Community 155 - "TaskRegistry"
Cohesion: 0.09
Nodes (37): get_registry(), Centralized TaskRegistry for MythosMUD server task lifecycle management. This…, Cancel lifecycle/critical tasks first (Phase 1)., Cancel remaining active tasks (Phase 2)., Wait for task completion with timeout., Forcibly cancel any lingering tasks that didn't respond to graceful…, Clean up active collections after final shutdown., Gracefully shutdown all tracked tasks with timeout coordination. Implements… (+29 more)

### Community 156 - "talk_command.py"
Cohesion: 0.04
Nodes (73): _emit_prompt(), handle_talk_command(), UUID, talk / talk <n> command for NPC dialogue trees (#583)., Handle talk <npc> or talk <n> against same-room NPCs., Extract player UUID from player model., Join talk args into a single remainder string., Send personal system message for a node; return short command result. (+65 more)

### Community 157 - "NPCOccupantProcessor"
Cohesion: 0.03
Nodes (75): NPCOccupantProcessor, Any, NPC occupant processing utilities. This module handles querying and processing…, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Processes NPC occupants for rooms., Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:… (+67 more)

### Community 158 - "CombatConfiguration"
Cohesion: 0.04
Nodes (50): CombatConfiguration, CombatConfigurationError, CombatConfigurationScope, CombatConfigurationService, get_combat_config(), get_combat_configuration(), is_combat_available(), Any (+42 more)

### Community 159 - "test_game_state_provider.py"
Cohesion: 0.09
Nodes (21): Unit tests for game state provider. Tests the GameStateProvider class., Test get_npcs_batch() returns NPC names., Test get_npcs_batch() returns empty dict for empty input., Test get_npcs_batch() handles None in NPC IDs list., Test _get_fallback_player_data() uses get_stats when available., Test _get_fallback_player_data() parses JSON stats string., Test _get_player_name_with_grace_periods() returns name with grace indicators., Test get_npcs_batch() resolves names from active NPCs. (+13 more)

### Community 160 - "test_npc_event_handlers.py"
Cohesion: 0.03
Nodes (81): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers. Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON. (+73 more)

### Community 161 - "PlayerEventHandlerUtils"
Cohesion: 0.06
Nodes (33): BoundLogger, ConnectionManager, Initialize respawn event handler. Args: connection_manager: ConnectionManager…, PlayerEventHandlerUtils, Any, UUID, Extract occupant names from occupant information. Args: occupants_info: List of…, Add a valid name to the appropriate lists. Args: name: The name to validate and… (+25 more)

### Community 162 - "lifespan_startup.py"
Cohesion: 0.03
Nodes (109): _calculate_metrics_delta(), _cleanup_container_on_error(), _cleanup_dead_letter_queue_periodically(), _initialize_enhanced_systems(), lifespan(), _log_memory_metrics_periodically(), _persist_metrics_to_file(), _persist_mythos_state_on_error() (+101 more)

### Community 163 - "_parse_env_list"
Cohesion: 0.06
Nodes (37): _apply_url_fallback(), _default_cors_origins(), _parse_env_list(), _parse_list_from_string(), Any, Parse non-empty string as JSON list or CSV. Used by _parse_env_list., Parse a string from the environment as JSON list or CSV., Derive default CORS origins with environment taking precedence. (+29 more)

### Community 164 - "room_service.py"
Cohesion: 0.06
Nodes (43): _append_room_with_fallback_coords_if_needed(), _apply_minimap_fallback_coordinates(), _ensure_current_room_in_minimap_rooms(), generate_minimap_html(), Any, AsyncSession, UUID, Minimap orchestration for the map API. Extracted from maps.py so the router… (+35 more)

### Community 165 - "test_zone_config_loader.py"
Cohesion: 0.05
Nodes (79): async_load_zone_configurations(), extract_zone_name(), load_zone_configurations(), parse_json_field(), parse_zone_special_rules(), process_subzone_rows(), process_zone_rows(), Connection (+71 more)

### Community 166 - "test_lucidity_recovery_commands.py"
Cohesion: 0.02
Nodes (155): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+147 more)

### Community 167 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

### Community 168 - "NATSSubjectManager"
Cohesion: 0.03
Nodes (42): get_subject_manager_dependency(), Dependency function to inject NATSSubjectManager. Returns: Global…, _EventPersistence, _Named, _NatsPublish, Protocol, UUID, Initialize EventPublisher service. Args: nats_service: NATS service instance… (+34 more)

### Community 169 - "test_message_handlers.py"
Cohesion: 0.08
Nodes (48): handle_chat_message(), handle_client_error_report_message(), handle_command_message(), handle_follow_response_message(), handle_party_invite_response_message(), handle_ping_message(), Any, WebSocket (+40 more)

### Community 170 - "test_admin_setlucidity_command.py"
Cohesion: 0.06
Nodes (71): _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), _get_current_lcd(), _get_player_service_from_app(), _handle_admin_set_lucidity_command() (+63 more)

### Community 171 - "test_combat_flee_helpers.py"
Cohesion: 0.04
Nodes (76): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules. Keeps…, Application object with a ``state`` namespace (dynamic attributes)., _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id() (+68 more)

### Community 172 - "test_shutdown_sequence.py"
Cohesion: 0.10
Nodes (48): Schedule a best-effort graceful process termination after a short delay. This…, schedule_process_termination(), _cancel_background_tasks(), _cleanup_connection_manager(), _despawn_all_npcs(), _disconnect_all_players(), _disconnect_nats_service(), execute_shutdown_sequence() (+40 more)

### Community 173 - "OccupantFormatter"
Cohesion: 0.04
Nodes (65): OccupantFormatter, Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Formats and separates occupants by type., Initialize occupant formatter., Check if a string looks like a UUID. Args: value: The string to check Returns:… (+57 more)

### Community 174 - "event_types.py"
Cohesion: 0.01
Nodes (309): Async persistence layer for MythosMUD. This module provides an async version of…, Attribute stubs for EventBus mixins (mypy attr-defined). Mirrors…, Event dispatch and subscriber invocation for EventBus. Extracted to keep…, Event bus for MythosMUD. This module provides the EventBus class that…, _default_timestamp(), NPCAttacked, NPCDied, NPCEnteredRoom (+301 more)

### Community 175 - "server/services/__init__.py"
Cohesion: 0.03
Nodes (69): Services package for MythosMUD. This package contains various services for…, _DatabaseLoadResult, _fetch_schedule_entries(), _lower_string_list_from_row(), normalize_weekday_names(), Connection, datetime, Path (+61 more)

### Community 176 - "ValidationError"
Cohesion: 0.01
Nodes (379): MythosValidationError, add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., main(), Load seed data and verify., fetch_professions() (+371 more)

### Community 177 - "test_party_service.py"
Cohesion: 0.04
Nodes (49): Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves., Leader can disband the party., Non-leader cannot disband. (+41 more)

### Community 178 - "PlayerRespawnService"
Cohesion: 0.05
Nodes (42): _PlayerCombatClearing, PlayerRespawnService, AsyncSession, Player, Protocol, UUID, _RandomChoiceSource, Return current_dp as an int, defaulting to 0 for non-numeric values. (+34 more)

### Community 179 - "test_nats_message_handler_chat.py"
Cohesion: 0.03
Nodes (76): asyncio, Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _get_player_lucidity_tier returns default on error., Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_name…, Test _validate_chat_message_fields raises TypeError for invalid content type., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _extract_chat_message_fields handles whisper target_id. (+68 more)

### Community 180 - "waitForMessage"
Cohesion: 0.13
Nodes (29): prepCoLocatedContexts(), primeBothForCoLocate(), waitForLookReflected(), NOTE: The 'open' command does not exist yet., NOTE: The 'open' command does not exist yet., waitForMessage(), ensureE2eRuntimeReady(), ensureMultiplayerCoLocated() (+21 more)

### Community 181 - "test_logging_handlers.py"
Cohesion: 0.04
Nodes (65): _aggregator_handler_class_for_windows(), AsyncioConnLostWriteFilter, create_aggregator_handler(), _make_exec_for_aggregator(), Any, LogRecord, Path, RotatingFileHandler (+57 more)

### Community 182 - "NPCMovementIntegration"
Cohesion: 0.05
Nodes (45): Initialize the idle movement handler. Args: event_bus: Optional EventBus…, NPCMovementIntegration, Room, Get room objects and validate they exist. Args: npc_id: ID of the NPC…, Update room occupancy by removing NPC from source and adding to destination.…, Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…, Move an NPC to a different room with full integration. This method provides…, Get the current room ID for an NPC. Args: npc_id: ID of the NPC Returns:… (+37 more)

### Community 183 - "IdleMovementHandler"
Cohesion: 0.03
Nodes (87): _cfg_bool(), _cfg_float(), IdleMovementHandler, _npc_id_str(), _passes_movement_probability(), NPC Idle Movement Handler for MythosMUD. This module provides idle movement…, Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement. Checks multiple conditions: -… (+79 more)

### Community 184 - "PassiveMobNPC"
Cohesion: 0.04
Nodes (59): PassiveMobNPC, Check if idle movement should be scheduled based on configuration and timing.…, Create a WANDER action message. Args: current_time: Current timestamp Returns:…, Queue a WANDER action via the thread manager. Args: wander_action: The wander…, Schedule a WANDER action for idle movement if interval has elapsed. This method…, Respond to player interaction., Handle wandering action., Handle responding to greeting action. (+51 more)

### Community 185 - "test_player_disconnect_handlers.py"
Cohesion: 0.04
Nodes (75): age_off_disconnected_sessions(), _cleanup_player_references(), _collect_disconnect_keys(), _get_session_maps_for_age_off(), handle_player_disconnect_broadcast(), _purge_expired_sessions_from_maps(), Player, UUID (+67 more)

### Community 186 - "middleware"
Cohesion: 0.10
Nodes (32): CorrelationMiddleware, create_correlation_middleware(), create_websocket_correlation_middleware(), _get_header(), ASGIApp, Receive, Scope, Send (+24 more)

### Community 187 - "InventoryMutationGuard"
Cohesion: 0.02
Nodes (117): HolidayResolver, Lock, Initialize metrics collector. AI: Uses Lock for thread-safety in async context., _AsyncPlayerGuardState, InventoryMutationGuard, _PlayerGuardState, Acquire sync mutation guard., Acquire async mutation guard. (+109 more)

### Community 188 - "AppConfig"
Cohesion: 0.07
Nodes (38): AppConfig, Any, BaseSettings, model_validator, Composite application configuration. This is the main configuration class that…, Initialize configuration and set environment variables for legacy compatibility., Set environment variables for legacy code that reads them directly., Return first set CORS origins env var to reduce CCN in _sanitize. (+30 more)

### Community 189 - "test_communication_commands_flows.py"
Cohesion: 0.09
Nodes (45): _chat_send_with_room_bundle(), flow_say_command(), _global_player_bundle(), _message_from_command(), Handle the `say` command: broadcast speech to the current room., Resolve primary IDs for whisper; return error dict if self-whisper or missing…, _room_player_bundle(), _RoomChannelOutcomeConfig (+37 more)

### Community 190 - "test_connection_cleaner.py"
Cohesion: 0.06
Nodes (43): connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue(), mock_rate_limiter(), mock_room_manager() (+35 more)

### Community 191 - "CombatAuditLogger"
Cohesion: 0.05
Nodes (59): CombatAttackDetails, CombatAuditLogger, CombatMonitoringAlert, CombatParties, CombatSecurityEvent, Any, datetime, Combat-specific audit logging and monitoring. This module provides specialized… (+51 more)

### Community 192 - "test_wearable_container_service.py"
Cohesion: 0.02
Nodes (139): _filter_container_data(), _get_enum_value(), Any, UUID, Wearable container service for unified container system. As documented in the…, Return existing equipment container ID for item instance if present., Create wearable container in persistence and return container_id payload., Handle equipping a wearable container item. Creates a container in PostgreSQL… (+131 more)

### Community 193 - "MemoryProfiler"
Cohesion: 0.04
Nodes (58): OtherModel, BaseModel, Unit tests for memory profiler utilities. Tests the MemoryProfiler class…, Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test Pydantic model for memory profiling tests., Test MemoryProfiler.print_model_memory_usage() doesn't raise. (+50 more)

### Community 194 - "system_monitoring.py"
Cohesion: 0.05
Nodes (57): AlertResolveResponse, Response model for system health check., Response model for system metrics., Response model for system monitoring summary., Response model for system alerts., Response model for alert resolution., SystemAlertsResponse, SystemHealthResponse (+49 more)

### Community 195 - "useGameClientV2Container.ts"
Cohesion: 0.10
Nodes (38): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), forceLogoutFallback(), performGameClientLogout(), stillShowingGameClient() (+30 more)

### Community 196 - "ContainerService"
Cohesion: 0.08
Nodes (70): ContainerService, Service for managing container operations. Orchestrates open/close, transfer…, MutationDecision, Result of attempting to acquire a guarded mutation context., Test execute_transfer function., Test execute_transfer calls transfer_to_container for to_container direction., Test execute_transfer calls transfer_from_container for to_player direction., TestExecuteTransfer (+62 more)

### Community 197 - "websocket_handler.py"
Cohesion: 0.04
Nodes (86): Any, Convert alias to dictionary for JSON serialization., get_message_validator(), Get the global message validator instance., handle_json_decode_error(), handle_message_loop_exception(), handle_websocket_disconnect(), handle_websocket_generic_exception() (+78 more)

### Community 198 - "logging_file_setup.py"
Cohesion: 0.05
Nodes (77): Logger, Queue, QueueHandler, QueueListener, add_handler_to_loggers(), LoggerNameFilter, LogRecord, Filter that only allows logs from loggers matching specified prefixes. This… (+69 more)

### Community 199 - "MovementService"
Cohesion: 0.05
Nodes (36): MovementService, Any, Exception, Room, UUID, Validate movement parameters. Returns False if validation fails (same room),…, Resolve player by ID or name and return player object and resolved ID., Get and validate rooms for movement. (+28 more)

### Community 200 - "Room"
Cohesion: 0.03
Nodes (78): Any, UUID, Add a player to the room without triggering an event. This method is used for…, Remove a player from the room without triggering an event. This method is used…, Remove a player from the room and trigger event. Args: player_id: The ID of the…, Add an object to the room and trigger event. Args: object_id: The ID of the…, Remove an object from the room and trigger event. Args: object_id: The ID of…, Add an NPC to the room and trigger event. Args: npc_id: The ID of the NPC… (+70 more)

### Community 201 - "test_health_monitor.py"
Cohesion: 0.07
Nodes (35): health_monitor(), mock_cleanup_dead_websocket(), mock_is_websocket_open(), mock_performance_tracker(), mock_validate_token(), asyncio, fixture, Unit tests for health monitor. Tests the HealthMonitor class. (+27 more)

### Community 202 - "test_player_event_handlers_room.py"
Cohesion: 0.04
Nodes (70): asyncio, Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test broadcast_player_entered_message() skips when room_id is None., Test subscribe_player_to_room() successfully subscribes player., Test subscribe_player_to_room() handles invalid player_id., Test subscribe_player_to_room() handles subscription errors., Test _send_room_name_message() sends room name., Test _prepare_room_data() prepares room data with to_dict. (+62 more)

### Community 203 - "PlayerStateCommandFactory"
Cohesion: 0.04
Nodes (59): Unit tests for player state command factories. Tests the…, Test create_skills_command() raises error with args., Test create_journal_command() creates JournalCommand., Test create_journal_command() raises error with args., Test create_quests_command() creates QuestsCommand., Test create_quests_command() raises error with args., Test create_quest_command() with no args creates QuestCommand with empty list., Test create_status_command() creates StatusCommand. (+51 more)

### Community 204 - "test_websocket_handler_coverage_gaps.py"
Cohesion: 0.07
Nodes (42): asyncio, Unit tests to fill coverage gaps in websocket_handler.py. These tests target…, Test handle_game_command exception handling path (lines 472-480)., Test handle_game_command RuntimeError handling path (lines 472-480)., Test process_websocket_command resolves connection_manager from app when None…, Test handle_chat_message resolves connection_manager from app when None (lines…, Test handle_chat_message exception handling path (lines 666-674)., Test handle_chat_message RuntimeError handling path (lines 666-674). (+34 more)

### Community 205 - "RoomEventHandler"
Cohesion: 0.11
Nodes (24): Integration components for connection management. This package provides…, Any, UUID, Room event handling for connection management. This module provides integration…, Handle PlayerEnteredRoom events by broadcasting updated occupant count., Handle PlayerLeftRoom events by broadcasting updated occupant count., Handles room movement events and broadcasts occupant updates. This class…, Initialize the room event handler. Args: room_manager: RoomSubscriptionManager… (+16 more)

### Community 206 - "command_result_text"
Cohesion: 0.04
Nodes (91): Shared types for inventory command handlers (Lizard: keep main module small)., Resolve state and player, returning (persistence, connection_manager, player,…, Remove or update item quantity in player inventory after transfer., remove_item_from_inventory(), resolve_state_and_player(), Inventory and equipment command handlers for MythosMUD. Heavy handlers live in…, handle_pickup_command(), Move an item stack from room drops into the player's inventory. (+83 more)

### Community 207 - "._calculate_percentile"
Cohesion: 0.18
Nodes (9): Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, Test _calculate_percentile() returns 0 for empty list., Test _calculate_percentile() handles single value., Test _calculate_percentile() calculates percentile correctly., test_calculate_percentile_empty(), test_calculate_percentile_multiple_values() (+1 more)

### Community 208 - "LogAggregator"
Cohesion: 0.06
Nodes (50): LogEntry, aggregate_log_entry(), get_log_aggregator(), LogAggregator, LogEntry, LogQueryFilter, _optional_datetime_from_object(), _optional_str_from_object() (+42 more)

### Community 209 - "_is_predefined_emote"
Cohesion: 0.11
Nodes (18): _is_predefined_emote(), CommandExecutionRequest, Check if a command is a predefined emote alias. Args: command: The command to…, Check if a single word command should be treated as an emote. This function…, should_treat_as_emote(), _mock_request(), Unit tests for command input processing. Tests command normalization, cleaning,…, Test _is_predefined_emote() returns False when no request is available. (+10 more)

### Community 210 - "ChatHistoryPanel.tsx"
Cohesion: 0.03
Nodes (88): EldritchEffectsDemo(), EldritchEffectsDemoProps, mockAlert, ALWAYS_ACTIVE_EFFECTS, effectClass(), EffectOption, ELDRITCH_EFFECT_OPTIONS, hasEffect() (+80 more)

### Community 211 - "Async Remediation Summary - December 3, 2025"
Cohesion: 0.03
Nodes (67): 1. Fixed Event Loop Blocking in PassiveLucidityFluxService, 2. Removed asyncio.run() from Exploration Service, 3. Added Exception Handling for Database Engine Creation, Achieved, 🏆 Achievement Highlights, Adjusts spectacles with scholarly satisfaction, After, After Fixes (+59 more)

### Community 212 - ".state"
Cohesion: 0.06
Nodes (64): _apply_grounding_adjustment(), _complete_ground_command(), _get_ground_services(), handle_ground_command(), handle_rescue_command(), _normalize_player_ids(), Any, UUID (+56 more)

### Community 213 - "test_chat_validator.py"
Cohesion: 0.13
Nodes (26): _chat_passes_nats_validation(), Return True when message content and room access checks pass., contains_malicious_content(), Chat message validation utilities. This module provides validation functions…, Validate chat message before transmission. Args: chat_message: The chat message…, Validate sender has access to the room. Args: sender_id: ID of the message…, Check for malicious content patterns. Args: content: The message content to…, validate_chat_message() (+18 more)

### Community 214 - "PerformanceMonitor"
Cohesion: 0.05
Nodes (58): ExceptionStats, Statistics for exception tracking., __getattr__(), Any, Monitoring package for MythosMUD server., Lazy import for modules that require numpy., MonitoringSummary, Comprehensive monitoring dashboard for MythosMUD server. This module provides a… (+50 more)

### Community 215 - "NPCCombatIntegration"
Cohesion: 0.05
Nodes (77): NPCCombatIntegration, Integrates NPCs with the existing combat and game mechanics systems. Extends…, Get NPC stats or use defaults., integration(), asyncio, fixture, Unit tests for NPCCombatIntegrationBase helpers., test_apply_combat_effects_attribute_error_raises() (+69 more)

### Community 216 - "test_invite_schemas.py"
Cohesion: 0.05
Nodes (61): Auth domain schemas: user and invite., InviteBase, InviteCreate, InviteUpdate, Pydantic schemas for Invite model. This module defines Pydantic schemas for…, Base invite schema with common fields., Schema for creating a new invite., Schema for updating invite data. (+53 more)

### Community 217 - "player.ts"
Cohesion: 0.11
Nodes (31): locationIndicatesDeathVoid(), requiredAliveButDeadMessage(), assertLookVisibleInPanels(), lookAndStand(), prepAwForAdminSet(), prepNonAdminForSetAttempt(), runAdminSetWithRecovery(), assertNpcSpawnVisible() (+23 more)

### Community 218 - "MonitoringDashboard"
Cohesion: 0.06
Nodes (40): PerformanceStats, Alert, MonitoringDashboard, Any, Get overall system health status. Returns: Current system health status, Get comprehensive monitoring summary. Returns: Complete monitoring summary with…, Evaluate thresholds and record new alerts., Record a custom alert emitted by subsystems. Args: alert_type: Identifier for… (+32 more)

### Community 219 - "websocket_helpers.py"
Cohesion: 0.06
Nodes (54): _AppStateForPlayerService, build_basic_player_data(), _ensure_player_in_room_occupancy(), _fetch_room_for_tracked_player(), get_player_and_room(), get_player_service_from_connection_manager(), get_player_stats_data(), _get_tracked_player_from_connection_manager() (+46 more)

### Community 220 - "AliasStorage"
Cohesion: 0.02
Nodes (133): AliasPayload, AliasRecord, AliasStorage, _AliasValidatorCache, _apply_alias_timestamps(), _as_alias_payload(), _as_alias_record(), _empty_alias_payload() (+125 more)

### Community 221 - "DatabaseError"
Cohesion: 0.02
Nodes (148): get_npc_data_from_source(), get_npc_database_url(), main(), populate_database(), Populate a PostgreSQL database with NPC data. Args: target_url: PostgreSQL…, Main function to populate test NPC databases., Get NPC database URL for the specified environment. Args: environment:…, Extract NPC data from the source PostgreSQL database. Args: source_url:… (+140 more)

### Community 222 - "lifespan_protocols.py"
Cohesion: 0.07
Nodes (63): MemoryMonitor, _container_attr(), _legacy_container_attr(), lifespan_connection_manager(), lifespan_container(), lifespan_event_bus(), lifespan_memory_monitor(), lifespan_nats_handler() (+55 more)

### Community 223 - "test_logout_commands.py"
Cohesion: 0.04
Nodes (103): _clear_corrupted_cache_entry(), _disconnect_player_connections(), _force_disconnect_player(), _get_app_services(), _get_player_for_logout(), _get_player_position_from_connection_manager(), handle_logout_command(), handle_quit_command() (+95 more)

### Community 224 - "test_aggressive_mob_npc.py"
Cohesion: 0.25
Nodes (14): _make_aggro(), asyncio, Unit tests for AggressiveMobNPC. Regression test: aggressive mobs must have…, test_attack_target_error_returns_false(), test_attack_target_fallback_publishes_event(), test_attack_via_combat_integration_none_when_missing(), test_attack_via_create_task_with_running_loop(), test_attack_via_dropped_without_loop_or_bus() (+6 more)

### Community 225 - "CombatEventHandler"
Cohesion: 0.11
Nodes (28): CombatEventHandler, Any, UUID, Publish attack events and calculate XP reward. Args: current_participant:…, Calculate XP reward for defeating an NPC. Args: npc_id: ID of the defeated NPC…, Award XP to player for defeating an NPC. Args: current_participant: Attacking…, Publish combat ended event., Handles combat event publishing. (+20 more)

### Community 226 - "build_event"
Cohesion: 0.04
Nodes (68): create_rest_countdown_task(), _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, Task, UUID, Rest countdown task implementation. This module contains the async task that… (+60 more)

### Community 227 - "test_lifecycle_periodic.py"
Cohesion: 0.06
Nodes (53): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD. This module defines configuration settings for…, Configuration for NPC lifecycle maintenance. This class centralizes all timing…, Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…, Get a summary of all NPC configuration values. Returns: Dictionary containing…, Clean up old lifecycle records (delegates to lifecycle_periodic)., Perform periodic maintenance (delegates to lifecycle_periodic). (+45 more)

### Community 228 - "test_error_handling_middleware.py"
Cohesion: 0.14
Nodes (25): ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Read user id from a non-Mapping request.state.user (object with get and/or id).…, Pure ASGI middleware to handle all exceptions across FastAPI endpoints. This…, Initialize error handling middleware. Args: app: ASGI application instance…, _error_log_kwargs(), _http_scope() (+17 more)

### Community 229 - "_EventBusPublishPort"
Cohesion: 0.40
Nodes (4): _EventBusPublishPort, Protocol, Minimal surface for publishing domain events from ConnectionManager.event_bus., Publish a single event to the in-process bus.

### Community 230 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (34): CatatoniaRegistry, datetime, UUID, Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not…, asyncio (+26 more)

### Community 231 - "GameClientV2Dock.test.tsx"
Cohesion: 0.04
Nodes (38): ProfessionSelectionScreen(), fetchSpy, StatsRollingScreen(), mockFetch, RolledStatsInput, chatHistoryLayoutIdentity, chatHistoryLayoutState, defaultChatHistoryLayoutKey (+30 more)

### Community 232 - "NPCCombatUUIDMapping"
Cohesion: 0.04
Nodes (35): Return UUID mapping dependency for integration collaborators., NPCCombatUUIDMapping, UUID, NPC Combat UUID Mapping Management. This module handles UUID-to-string ID and…, Get the original string ID from a UUID. Args: uuid_id: The UUID to look up…, Get XP value for a UUID. Args: uuid_id: The UUID to look up Returns: XP value…, Manages UUID mappings for NPC combat., Initialize UUID mapping storage. (+27 more)

### Community 233 - "InstanceManager"
Cohesion: 0.05
Nodes (41): Wire exploration, movement, follow, and party services., Instance, InstanceManager, Room, UUID, Return template rooms matching instance_template_id., Clone template rooms into instance-scoped rooms with remapped exits., Extract stable_id from room - use room.id if it looks like a full path. (+33 more)

### Community 234 - "CommandService"
Cohesion: 0.09
Nodes (17): CommandHandler, CommandService, Command, Main command processing service for MythosMUD. This service handles command…, Initialize the command service., Process a validated command with routing. Args: command_data: The validated…, Parse and validate command string. Returns: tuple of (parsed_command, cmd,…, Prepare command_data dictionary by merging parsed command fields. Returns:… (+9 more)

### Community 235 - ".initialize"
Cohesion: 0.10
Nodes (12): Any, Exception, Wire user_manager into follow_service and nats_message_handler when present., Set item prototype registry on player service when both are available., Create room and profession cache services; set to None on RuntimeError., Create the emote repository/service and load predefined emotes once, at…, Initialize game services. Requires Core and Realtime., On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item… (+4 more)

### Community 236 - "validate_room_data"
Cohesion: 0.09
Nodes (23): patch, Unit tests for world loader utility functions. Tests room ID generation,…, Test validate_room_data() function., Test validate_room_data() returns empty list when validation not available., Test validate_room_data() with provided validator., Test validate_room_data() creates validator when not provided., Test validate_room_data() returns validation errors., Test validate_room_data() raises exception in strict mode with errors. (+15 more)

### Community 237 - "_MagicServiceCore"
Cohesion: 0.06
Nodes (34): _CombatTickState, _MagicServiceCore, _PlayerPersistence, JsonMap, Protocol, UUID, Load player and return normalized stats (MP/max_MP). Returns (player, stats) or…, Return (False, message) if not enough MP, else (True, ''). (+26 more)

### Community 238 - "test_websocket_handler_json_error.py"
Cohesion: 0.25
Nodes (7): mock_websocket(), asyncio, fixture, Unit tests for websocket handler JSON error handling. Tests the JSON decode…, Create a mock WebSocket., Test _handle_json_decode_error() sends error response., test_handle_json_decode_error()

### Community 239 - "NATSMessageSubscriptionMixin"
Cohesion: 0.05
Nodes (29): NATSMessageSubscriptionMixin, Any, Unsubscribe from local channel messages for a specific sub-zone. Args: subzone:…, Track a player's sub-zone subscription for local channels. Args: player_id:…, Mixin: room, subzone, and event NATS subscription lifecycle., Get list of players currently in a specific sub-zone. Args: subzone: Sub-zone…, Handle player movement between rooms and update sub-zone subscriptions. Args:…, Subscribe to chat messages for a specific room. Args: room_id: Room ID to… (+21 more)

### Community 240 - "security.ts"
Cohesion: 0.04
Nodes (44): SafeHtml(), SafeHtmlProps, useCommandHandlers(), UseCommandHandlersParams, fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler (+36 more)

### Community 241 - "RoomMapViewer.tsx"
Cohesion: 0.09
Nodes (39): fetchSpy, useMapLayout(), buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData(), UseRoomMapDataResult (+31 more)

### Community 242 - "fixtures/integration/__init__.py"
Cohesion: 0.13
Nodes (23): FixtureRequest, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+15 more)

### Community 243 - "test_level_service.py"
Cohesion: 0.05
Nodes (61): LevelUpHook, level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level() (+53 more)

### Community 244 - "InventorySchemaValidationError"
Cohesion: 0.06
Nodes (44): Initialize the player repository. Args: room_cache: Shared room cache for room…, _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Player save/upsert helpers for PlayerRepository. Handles inventory validation,… (+36 more)

### Community 245 - "request_with_app_container"
Cohesion: 0.09
Nodes (40): handle_me_command(), handle_pose_command(), handle_say_command(), Room-wide say; returns user-facing result dict., Set or clear persistent pose text., Shared mock wiring for communication command unit tests., Return (request, container) with request.app.state.container wired. Typed…, request_with_app_container() (+32 more)

### Community 246 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages. These schemas define the structure and… (+55 more)

### Community 247 - "ModerationCommandFactory"
Cohesion: 0.05
Nodes (58): Unit tests for moderation command factories. Tests the ModerationCommandFactory…, Test create_mute_global_command() with duration and reason., Test create_mute_global_command() with reason but no duration., Test create_unmute_global_command() creates UnmuteGlobalCommand., Test create_unmute_global_command() raises error with no args., Test create_unmute_global_command() raises error with multiple args., Test create_admin_command() creates AdminCommand., Test create_mute_command() creates MuteCommand. (+50 more)

### Community 248 - "devDependencies"
Cohesion: 0.05
Nodes (41): devDependencies, esbuild, eslint, @eslint/js, eslint-plugin-jsx-a11y, eslint-plugin-playwright, eslint-plugin-react-hooks, jsdom (+33 more)

### Community 249 - "NATSMessageBroadcastMixin"
Cohesion: 0.07
Nodes (23): NATSMessageBroadcastMixin, Any, UserManager, Determine if message should be echoed to sender. Args: channel: Channel type…, Echo message back to sender. Args: sender_id: Sender player ID chat_event: Chat…, Broadcast room-based messages with server-side filtering. This method ensures…, Mixin: room filtering, mute checks, dampening, and personal send., Return the user manager instance to use for mute lookups. #679: no module-level… (+15 more)

### Community 250 - "PlayerGuidFormatter"
Cohesion: 0.05
Nodes (54): _canonical_ip(), PlayerGuidFormatter, LogRecord, Player GUID Formatter for MythosMUD logging system. This module provides a…, Determine if a GUID is likely to be a player ID based on context. Args: guid:…, Get player name for GUID from in-memory data. Args: guid: The player GUID to…, Custom formatter that converts player GUIDs to "<name>: <GUID>" format. This…, Initialize the PlayerGuidFormatter. Args: player_service: Service for accessing… (+46 more)

### Community 251 - "eventHandlers/types.ts"
Cohesion: 0.06
Nodes (66): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), processGameEvent() (+58 more)

### Community 252 - "test_config_models.py"
Cohesion: 0.06
Nodes (35): DatabaseConfig, Any, BaseSettings, field_validator, model_validator, Server network configuration., Validate port is in valid range., Database configuration. (+27 more)

### Community 253 - "handle_explore_command"
Cohesion: 0.27
Nodes (9): handle_explore_command(), Any, Handle exploration requests by returning a simple message. This lightweight…, asyncio, Unit tests for exploration command handlers. Tests the exploration command…, Test handle_explore_command() explores area., Test handle_explore_command() handles missing persistence., test_handle_explore_command() (+1 more)

### Community 254 - "fixtures/auth.ts"
Cohesion: 0.07
Nodes (34): RoomSummary, STANDARD_DIRECTIONS, assertCommandChannelReady(), EnsurePlayableConnectionOptions, getLivePageForUsername(), getPageSessionCredentials(), isPageUsable(), isUsernameLoginVisible() (+26 more)

### Community 255 - "connection_establishment.py"
Cohesion: 0.11
Nodes (36): _bind_accepted_websocket(), _cleanup_dead_connections(), _cleanup_failed_connection(), establish_websocket_connection(), _EstablishmentConnectionManager, _find_dead_connections(), Player, Protocol (+28 more)

### Community 256 - "GameTickService"
Cohesion: 0.05
Nodes (32): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+24 more)

### Community 257 - "useWebSocketConnection.ts"
Cohesion: 0.17
Nodes (12): ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach(), wsConnectionBeforeEach() (+4 more)

### Community 258 - "testing_examples.py"
Cohesion: 0.04
Nodes (51): async_operation(), client, database, LoggingMiddleware, process_batch(), process_item(), asyncio, Test WebSocket logging in integration tests. (+43 more)

### Community 259 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.10
Nodes (52): check_ai_guardrails(), _check_single_use_file(), _collect_code_texts(), _guardrail_scan_inputs(), _is_single_use_small_file(), _process_added_file_checks(), build_context(), ChangedFile (+44 more)

### Community 260 - "gen_arena_migration_sql.py"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 261 - "PlayerStateEventHandler"
Cohesion: 0.05
Nodes (61): PlayerStateEventHandler, Handles player state update events (XP, DP, death, decay)., Handle player XP award events by sending updates to the client. Args: event:…, Handle player DP update events by sending updates to the client. Args: event:…, Handle player death events by sending death notification to the client. Args:…, Handle player DP decay events by sending decay notification to the client.…, mock_connection_manager(), mock_logger() (+53 more)

### Community 262 - "realtime/conftest.py"
Cohesion: 0.07
Nodes (36): Initialize utility functions and specialized handlers., PlayerRoomEventHandlerDeps, Constructor bundle so Lizard does not count eight service args., Initialize room event handler from a deps bundle., mock_chat_logger(), mock_connection_manager(), mock_logger(), mock_message_builder() (+28 more)

### Community 263 - "CombatMonitoringService"
Cohesion: 0.04
Nodes (36): Alert, CombatMonitoringService, Any, Convert to dictionary., Comprehensive combat monitoring and alerting service. Tracks combat system…, Initialize the combat monitoring service., Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier… (+28 more)

### Community 264 - "test_combat_service.py"
Cohesion: 0.07
Nodes (57): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+49 more)

### Community 265 - "coerce_int"
Cohesion: 0.16
Nodes (18): Coerce a JSONB stat value to int for DP and combat helpers., _stats_int(), parametrize, Unit tests for server.utils.int_coercion.coerce_int., JSONB stats use the same coercion as inventory command payloads., test_coerce_int_bool_before_int(), test_coerce_int_float(), test_coerce_int_float_inf_falls_back_to_default() (+10 more)

### Community 266 - "systemHandlers.ts"
Cohesion: 0.09
Nodes (42): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, appendDaypartChange(), appendHourChime() (+34 more)

### Community 267 - "fastapi_integration.py"
Cohesion: 0.05
Nodes (34): auth_service(), BackgroundTasks, create_player(), File, general_exception_handler(), get_player(), http_exception_handler(), list_players() (+26 more)

### Community 268 - "ContainerLockState"
Cohesion: 0.09
Nodes (27): ContainerLockState, StrEnum, Lock state for container instances., EnvironmentalContainerLoader, Any, UUID, Environmental container loader for unified container system. As documented in…, migrate_room_container_to_postgresql. (+19 more)

### Community 269 - "test_chat_nats_publisher.py"
Cohesion: 0.09
Nodes (53): _build_legacy_subject(), _build_nats_message_data(), build_nats_subject(), _build_standardized_subject(), _extract_subzone_from_room(), _log_nats_publish_error(), _log_nats_unexpected_error(), _nats_service_ready() (+45 more)

### Community 270 - "NATSMetrics"
Cohesion: 0.04
Nodes (35): NATSMetrics, Any, NATS-specific metrics collection for monitoring and alerting., Record publish operation metrics., Record subscribe operation metrics., Record batch flush operation metrics., Update connection health score (0-100)., Update connection pool utilization (0-1). (+27 more)

### Community 271 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test heal_player() heals player., Test apply_fear() when player not found., Test update_player_location() successfully updates location., Test apply_lucidity_loss() applies lucidity loss., Test apply_fear() applies fear., test_apply_fear(), test_apply_fear_player_not_found() (+3 more)

### Community 272 - "test_connection_establishment_ws.py"
Cohesion: 0.11
Nodes (36): _as_ws(), _FakeWebSocket, WebSocket, Test _find_dead_connections() returns empty list when all connections are…, Test _find_dead_connections() finds dead connections., Test _update_player_connection_list() keeps active connections., Test _register_new_connection() registers new connection., Test _register_new_connection() adds to existing player connections. (+28 more)

### Community 273 - "test_look_room.py"
Cohesion: 0.03
Nodes (111): _filter_other_players(), _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id() (+103 more)

### Community 274 - "NPCCombatLucidity"
Cohesion: 0.04
Nodes (52): Get base stats as dictionary., Return lucidity dependency for integration collaborators., _coerce_xp_mapping_value(), _NPCCombatIntegrationValidationDeps, Protocol, UUID, Validate that player and NPC are in the same room., End any active combat that includes this player when room validation fails. (+44 more)

### Community 275 - "ExceptionTracker"
Cohesion: 0.03
Nodes (67): auth_service, authenticate_websocket_connection(), chat_service, game_service, handle_chat_message(), handle_game_action(), handle_websocket_error(), handle_websocket_message() (+59 more)

### Community 276 - "test_command_parser_helpers.py"
Cohesion: 0.05
Nodes (37): Unit tests for command_parser helper methods. Tests the helper methods in…, Test _create_command_object() handles 'l' alias., Test _create_command_object() handles 'g' alias., Test _create_command_object() handles 'w' alias., Test _create_command_object() raises error for unsupported command., Test _create_command_object() handles PydanticValidationError., Test _create_command_object() handles ValueError., Test _normalize_command() removes leading slash. (+29 more)

### Community 277 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 278 - "test_communication_commands_channels.py"
Cohesion: 0.10
Nodes (34): handle_global_command(), handle_local_command(), handle_system_command(), Local channel message., Global channel message (level-gated in flow)., Admin-only system broadcast., asyncio, Unit tests for local, global, and system chat command handlers. (+26 more)

### Community 279 - "PlayerPositionService"
Cohesion: 0.04
Nodes (67): PlayerPositionService, PositionChangeResponse, PositionPlayer, TypedDict, Player posture coordination service for MythosMUD. As noted in the Pnakotic…, Validate and normalize position., Get player for position change. Returns: Tuple of (player, response_dict) if…, Copy player identity fields into the position-change response. (+59 more)

### Community 280 - "utils/layout.ts"
Cohesion: 0.10
Nodes (36): UseMapLayoutOptions, applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyLinkForces() (+28 more)

### Community 281 - "MythosTimeEventConsumer"
Cohesion: 0.12
Nodes (18): Construct holiday_service, schedule_service, and mythos_tick_scheduler.…, Initialize the Temporal context: holiday/schedule/tick-scheduler, then the…, MythosHourTickEvent, Event fired when the accelerated Mythos clock rolls over to a new hour., asyncio, fixture, Unit tests for MythosTimeEventConsumer hour tick handling., test_describe_state() (+10 more)

### Community 282 - "MythosTickScheduler"
Cohesion: 0.11
Nodes (27): mock_chronicle(), mock_event_bus(), mock_task_registry(), asyncio, fixture, Unit tests for MythosTickScheduler., scheduler(), test_emit_pending_ticks_initializes_last_hour() (+19 more)

### Community 283 - "test_rate_overrides.py"
Cohesion: 0.05
Nodes (69): get_asyncpg_server_settings_for_database_url(), Build asyncpg ``server_settings`` so unqualified table names resolve like…, _async_load_lucidity_rate_overrides(), build_override_key(), extract_lucidity_rate(), load_lucidity_rate_overrides(), _LucidityRateLoadResult, _normalize_database_url() (+61 more)

### Community 284 - "test_validation.py"
Cohesion: 0.03
Nodes (57): Unit tests for NATS Subject Validator. Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter., Test validate_parameter_value() raises error for empty parameter., Test validate_parameter_value() raises error for None parameter. (+49 more)

### Community 285 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 286 - "HealthStatus"
Cohesion: 0.04
Nodes (118): _assemble_health_response(), get_health_status(), Return aggregated health status for monitoring., ConnectionsComponent, DatabaseComponent, HealthComponents, HealthErrorResponse, HealthResponse (+110 more)

### Community 287 - "test_combat_handler.py"
Cohesion: 0.06
Nodes (56): _AppStatePersistence, _AppWithPersistence, _as_app_with_state(), _CmdType, _handler_with_persistence(), mock_persistence(), AppWithState, asyncio (+48 more)

### Community 288 - "error_logging.py"
Cohesion: 0.09
Nodes (33): Unit tests for error_logging wrapper utilities., Test create_error_context() creates error context., Test create_error_context() can include metadata., Test error context to_dict() method., test_create_context_from_request_none(), test_create_context_from_request_with_state(), test_create_context_from_websocket(), test_create_error_context() (+25 more)

### Community 289 - "MythosChronicle"
Cohesion: 0.05
Nodes (53): isolated_chronicle(), asyncio, fixture, Unit tests for TimeBundle container wiring., Calendar components and daypart helpers., Real/Mythos datetime conversion round-trips approximately., Advance and freeze update persisted state., Clock formatting includes Mythos suffix. (+45 more)

### Community 290 - "test_nats_service.py"
Cohesion: 0.03
Nodes (85): NATSRequestError, Raised when request/response operations fail., Send a request to a NATS subject and wait for a response. Args: subject: NATS…, asyncio, Unit tests for NATS service. Tests the NATSService class and NATSMetrics., Test NATSMetrics.record_batch_flush() records failed flush., Test NATSMetrics.update_connection_health() updates health score., Test NATSMetrics.update_connection_health() clamps values. (+77 more)

### Community 291 - "MemoryMonitor"
Cohesion: 0.06
Nodes (17): useGameClientV2MemoryMonitorEffect(), ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor (+9 more)

### Community 292 - "✅ Phase 2 Async Persistence Migration - COMPLETE"
Cohesion: 0.04
Nodes (53): 1. Eliminated Event Loop Blocking, 2. Consistent Async Patterns, 3. Proper Error Handling, 4. Resource Management, 5. Performance Optimization, 🏆 Achievement Summary, Additional Files Updated, Adjusts spectacles with profound satisfaction (+45 more)

### Community 293 - "MythosMUD Test Suite Modernization Plan"
Cohesion: 0.04
Nodes (53): Alternative: **GREENFIELD REWRITE**, Appendices, Appendix A: Test File Inventory, Appendix B: Direct app.state Access Locations, Appendix C: Fixture Audit, Backward Compatibility Strategy, Cons, Consolidation Opportunities (+45 more)

### Community 294 - "MemoryThresholdMonitor"
Cohesion: 0.06
Nodes (44): create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryThresholdMonitor, Any, Generate status report for diagnostic monitoring. Returns: Dictionary…, Runtime detection and cleanup of orphaned tasks based on memory thresholds.…, Create an instance of the MemoryThresholdMonitor with user-specified…, Factory function returning implementation conforming to Task 4.3 Specified… (+36 more)

### Community 295 - "NPCCombatDataProvider"
Cohesion: 0.03
Nodes (95): get_current_tick(), Shared game tick counter. Kept in a leaf module so combat services can read the…, Get the current game tick., _execute_combat_action(), _execute_phantom_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution. Extracted from combat.py to… (+87 more)

### Community 296 - "validate_calendar.py"
Cohesion: 0.20
Nodes (18): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+10 more)

### Community 297 - "CastingStateManager"
Cohesion: 0.09
Nodes (24): CastingStateManager, Any, UUID, Check if a player is currently casting. Args: player_id: Player ID to check…, Get the casting state for a player. Args: player_id: Player ID Returns:…, Complete and remove a casting state. Args: player_id: Player ID Returns:…, Interrupt and remove a casting state. Args: player_id: Player ID Returns:…, Update casting progress for a player. Args: player_id: Player ID current_tick:… (+16 more)

### Community 298 - "alias_schema.json"
Cohesion: 0.04
Nodes (51): command, version, additionalProperties, additionalProperties, description, properties, required, type (+43 more)

### Community 299 - "test_party_commands.py"
Cohesion: 0.08
Nodes (50): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+42 more)

### Community 300 - "PlayerDeathService"
Cohesion: 0.10
Nodes (21): Initialize combat services., Small types shared by CombatService wiring., PlayerDeathService, Any, AsyncSession, Player, UUID, Player Death Service for managing player mortality and DP decay. This service… (+13 more)

### Community 301 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+21 more)

### Community 302 - "PatternNotFoundError"
Cohesion: 0.09
Nodes (29): InvalidPatternError, MissingParameterError, NATSSubjectError, PatternNotFoundError, Exception, Base exception for NATS subject-related errors., Exception raised when a pattern name is not found in registry., Exception raised when required parameters are missing. (+21 more)

### Community 303 - "safe_run_static"
Cohesion: 0.07
Nodes (39): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+31 more)

### Community 304 - "admin_summon_command.py"
Cohesion: 0.08
Nodes (51): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), handle_summon_command(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any (+43 more)

### Community 305 - "test_inventory_display_helpers.py"
Cohesion: 0.07
Nodes (48): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+40 more)

### Community 306 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 307 - "PlayerRepositoryProtocol"
Cohesion: 0.07
Nodes (30): PlayerRepositoryProtocol, datetime, Player, Protocol, Room, UUID, List all cached rooms., Protocol for player persistence operations. Defines the contract used by… (+22 more)

### Community 308 - "AdminActionsLogger"
Cohesion: 0.08
Nodes (39): AdminActionsLogger, get_admin_actions_logger(), Any, datetime, Path, TypedDict, Log a general admin command action., Log permission check attempts. Args: player_name: Name of the player attempting… (+31 more)

### Community 309 - "debrief_command.py"
Cohesion: 0.08
Nodes (48): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+40 more)

### Community 310 - "test_nats_messages.py"
Cohesion: 0.07
Nodes (46): BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, Pydantic schemas for NATS message validation. This module provides type-safe…, Validate a chat message against the schema. Args: data: Message data dictionary…, Validate an event message against the schema. Args: data: Message data… (+38 more)

### Community 311 - "RoomMapEditorRuntime.tsx"
Cohesion: 0.07
Nodes (32): useMapEditing(), UseRoomMapDataOptions, MapEditToolbar(), MapEditToolbarProps, buildModalCreateEdgeHandler(), buildModalPreviewHandler(), buildModalUpdateEdgeHandler(), buildModalUpdateRoomHandler() (+24 more)

### Community 312 - "CoordinateGenerator"
Cohesion: 0.06
Nodes (27): Select, CoordinateGenerator, Any, AsyncSession, Coordinate generation service for ASCII maps. This module provides hierarchical…, Load rooms and their exits from database. Args: plane: Plane name zone: Zone…, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits. (+19 more)

### Community 313 - "SpellLearningService"
Cohesion: 0.12
Nodes (25): Any, UUID, Learn a spell for a player., Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…, Service for handling spell learning from various sources. Manages spell…, Learn a spell from a spellbook item. Args: player_id: Player ID…, Learn a spell from an NPC teacher. Args: player_id: Player ID npc_id: ID of the…, Learn a spell as a quest reward. Args: player_id: Player ID quest_id: ID of the… (+17 more)

### Community 314 - "lucidity.py"
Cohesion: 0.03
Nodes (119): LucidityActionCode, LucidityAdjustmentLog, LucidityCooldown, LucidityExposureState, Base, datetime, StrEnum, Lucidity tracking models drawn from the Pnakotic Manuscripts. (+111 more)

### Community 315 - "DialogueEditorPage.tsx"
Cohesion: 0.06
Nodes (42): baseUrl(), buildHeaders(), deleteDialogueDefinition(), DialogueDefinitionDto, DialogueNodeDto, DialogueOptionDto, DialogueTreeDto, listDialogueDefinitions() (+34 more)

### Community 316 - "game_tick_processing.py"
Cohesion: 0.13
Nodes (30): Game tick processing functions. This module handles all game tick processing…, _online_player_ids(), Return currently online player UUIDs, or empty if no connection manager., _TickConnectionManager, _handle_login_warded_expirations(), _process_all_status_effects(), _process_damage_over_time_effect(), _process_heal_over_time_effect() (+22 more)

### Community 317 - "RoomDataValidator"
Cohesion: 0.07
Nodes (39): Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Check if occupant count matches the actual occupants list length. Args:…, Validates room data structure and content., Check for duplicate occupants in the room. Args: room_data: Room data to check…, Check if room has occupants but no name. Args: room_data: Room data to check…, Validate room data structure and content. Args: room_data: Room data to… (+31 more)

### Community 318 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 319 - "Invite"
Cohesion: 0.08
Nodes (30): Invite, Base, Model for user registration invites., Mark this invite as used by a specific user., Create a new invite with the specified parameters., Unit tests for the Invite model. Tests the Invite model methods including…, Test create_invite creates invite with creator user_id., Test create_invite creates invite with custom expiry days. (+22 more)

### Community 320 - "test_map_helpers.py"
Cohesion: 0.08
Nodes (36): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities. Extracted from… (+28 more)

### Community 321 - "test_pattern_matcher.py"
Cohesion: 0.05
Nodes (37): Pattern matching utilities for NATS Subject Manager. This module provides…, pattern_matcher(), fixture, Unit tests for NATS Pattern Matcher. Tests the PatternMatcher class., Test _components_match_pattern() matches exact components., Test _components_match_pattern() matches placeholder components., Test _components_match_pattern() returns False for mismatch., Test _components_match_pattern() validates placeholder values. (+29 more)

### Community 322 - "PlayerRespawnEventHandler"
Cohesion: 0.03
Nodes (84): PlayerRespawnEventHandler, Player, Room, UUID, Get updated player data for respawn event. As documented in "Resurrection and…, Send respawn event with retry logic to handle temporary connection…, Build respawn player payload from connection-manager player when persistence…, Try connection-manager player lookup when persistence-based respawn data is… (+76 more)

### Community 323 - "test_player_occupant_processor.py"
Cohesion: 0.03
Nodes (71): PlayerOccupantProcessor, Any, UUID, Player occupant processing utilities. This module handles querying and…, Process players and convert to occupant information. Args: room_id: The room ID…, Processes player occupants for rooms., Initialize player occupant processor. Args: connection_manager:…, Ensure a player is included in the player ID strings list if specified. Args:… (+63 more)

### Community 324 - "verify_enhanced_logging_compliance.py"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 325 - "projectorRoom.ts"
Cohesion: 0.10
Nodes (43): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), messageHandlers, appendPostureGameInfoMessage(), mergePostureMessageIntoState(), ProjectorHandler (+35 more)

### Community 326 - "apiTypeGuards.ts"
Cohesion: 0.05
Nodes (78): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+70 more)

### Community 327 - "mythos_mud_mapbuilder.py"
Cohesion: 0.10
Nodes (46): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+38 more)

### Community 328 - "PrototypeRegistryError"
Cohesion: 0.08
Nodes (30): ItemInstance, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError, Any, Exception, PrototypeRegistry, Item factory for creating item instances from prototypes. This module provides… (+22 more)

### Community 329 - "compare_linting_results.py"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 330 - ".__post_init__"
Cohesion: 0.04
Nodes (39): Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), subscribe_room_occupants_refresh(), QuestCompleted, Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type. (+31 more)

### Community 331 - "PeriodicOrphanAuditor"
Cohesion: 0.07
Nodes (40): create_lifespan_memory_service(), PeriodicOrphanAuditor, Any, Core capability for granular investigation cycles. Repeated universal analysis…, Execute a single investigation loop synchronously producing operator summary.…, Stop the periodic orphan auditor background enforcement., Create a centralized memory operations coordinator instance targeted for…, Periodic background auditor that investigates orphanage patterns and memory… (+32 more)

### Community 332 - "test_goto_helpers.py"
Cohesion: 0.12
Nodes (43): execute_confirm_goto(), execute_goto_teleport(), log_goto_failure(), Any, Exception, Helper functions for goto command operations., Log failed goto action., Validate app context and get current player with admin permissions. Returns… (+35 more)

### Community 333 - "Any"
Cohesion: 0.16
Nodes (10): Any, ConnectionManager, Create a new party with the given player as leader. Returns dict with success…, Disband a party. If by_player_id is given, only the leader may disband. If…, Safely schedule an async notification, handling cases where no event loop is…, Notify a player they have been removed from a party. Resolves leader name., Remove a player from a party (leave or internal remove). If leader leaves,…, Remove a member from the party. Only the leader may kick. (+2 more)

### Community 334 - "test_follow_commands.py"
Cohesion: 0.10
Nodes (44): _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), _load_follow_context(), Any, Follow commands for MythosMUD. Handlers for /follow, /unfollow, and /following.…, Handle /following - show who you follow and who follows you. (+36 more)

### Community 335 - "collect_inventory.py"
Cohesion: 0.09
Nodes (41): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+33 more)

### Community 336 - "test_shopkeeper_npc.py"
Cohesion: 0.06
Nodes (35): Buy item from player., Calculate final price with markup., Handle greeting customer action., Handle restocking inventory action., Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., Shopkeeper NPC type with buy/sell functionality., Initialize shopkeeper NPC., Setup shopkeeper-specific behavior rules. (+27 more)

### Community 337 - "PydanticErrorHandler"
Cohesion: 0.11
Nodes (20): _ExtractedErrorInfo, _ExtractedFieldErrorInfo, TypedDict, ValidationError, PydanticErrorHandler, Handle a Pydantic ValidationError and convert it to a standardized response.…, Extract structured information from a Pydantic ValidationError. Args: error:…, Convert Pydantic error location to a readable field path. Args: location:… (+12 more)

### Community 338 - "PlayerPreferencesService"
Cohesion: 0.14
Nodes (18): PlayerPreferencesService, Any, AsyncSession, UUID, Player Preferences Service for Advanced Chat Channels. This module provides…, Get preferences for a player. Args: session: Database session player_id: The…, Update a player's default channel. Args: session: Database session player_id:…, Mute a channel for a player. Args: session: Database session player_id: The… (+10 more)

### Community 339 - "MemoryLeakMetricsCollector"
Cohesion: 0.03
Nodes (67): Initialize monitoring services. Depends on Core/Realtime/Game for injected deps., MemoryLeakMetricsCollector, Any, Memory leak metrics collector for MythosMUD. This module provides comprehensive…, Collect event metrics from EventBus. Returns: Dictionary with event metrics, Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics, Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics, Collect NATS subscription metrics from NATSService. Returns: Dictionary with… (+59 more)

### Community 340 - "test_audit_logger.py"
Cohesion: 0.07
Nodes (35): _logger(), Path, Unit tests for audit_logger utilities. Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries. (+27 more)

### Community 341 - "Uplift Strategy"
Cohesion: 0.04
Nodes (46): 0.1 Create Container Test Fixtures ✅, 0.2 Update conftest.py ✅, 1.1 Identify All Failing Tests ✅, 1.2 Fix Integration Test Fixtures ✅ **INFRASTRUCTURE COMPLETE**, 2.1 Categorize Unit Tests by Dependency Pattern, 2.2 Update Category B: Service Layer Tests, 2.3 Update Category C: Infrastructure Tests, 2.4 Update Category D: API Tests (+38 more)

### Community 342 - "Test Suite Optimization Roadmap"
Cohesion: 0.04
Nodes (46): After Month 1 (Pruning Phase), After Month 2 (Consolidation + Additions), After Month 3+ (Continuous Improvement), Guiding Principles, Implementation Timeline, Monitoring and Validation, Month 1: Pruning and Quick Wins, Month 2: Consolidation and Additions (+38 more)

### Community 343 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 344 - "Test Value Distribution Chart"
Cohesion: 0.04
Nodes (46): After Each Phase, After Phase 1-3: Pruning (Month 1), After Phase 4: Consolidation (Month 2), After Phase 5: Gap Filling (Month 2), Appendix: Quick Reference Commands, Automatic Rollback If, Before Starting Optimization, Capture Baseline (+38 more)

### Community 345 - "LoggedHTTPException"
Cohesion: 0.03
Nodes (174): CharacterInfo, get_container, IntegrityError, _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Any, post, Request (+166 more)

### Community 346 - "test_connection_statistics.py"
Cohesion: 0.06
Nodes (47): get_online_player_by_display_name_method(), Get online player information by display name., get_online_player_by_display_name_impl(), get_player_presence_info_impl(), get_presence_statistics_impl(), Any, Get online player information by display name., Get detailed presence information for a player. (+39 more)

### Community 347 - "test_websocket_handler_core.py"
Cohesion: 0.04
Nodes (71): handle_websocket_message(), WebSocket, Handle a WebSocket message from a player. Args: websocket: The WebSocket…, asyncio, Unit tests for core websocket handler functions. Tests core WebSocket handler…, Test _process_message processes message., Test _process_message returns True when rate limit exceeded., Test _validate_player_and_persistence validates successfully. (+63 more)

### Community 348 - "ScheduleCollection"
Cohesion: 0.10
Nodes (22): extract_observance_ids(), load_schedule_directory(), BaseModel, Path, Calendar ingestion schemas for MythosMUD. These models provide a typed wrapper…, Load holiday collection from JSON file., Wrapper around an array of schedule entries., Load schedule collection from a JSON file. Args: path: Path to the JSON file… (+14 more)

### Community 349 - "ChatLogger"
Cohesion: 0.07
Nodes (25): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+17 more)

### Community 350 - "WebSocketRequestContext"
Cohesion: 0.05
Nodes (48): command_request_app_state(), CommandExecutionRequest, HTTP Request or WebSocketRequestContext for unified command processing., Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…, create_websocket_request_context(), Any, Request context factory for WebSocket command processing. This module provides…, Get the event bus from the request context. (+40 more)

### Community 351 - "AsciiMapViewer.tsx"
Cohesion: 0.09
Nodes (28): AsciiMapViewer(), AsciiMapViewerProps, chooseMapView(), getMapClickHandler(), useAsciiMapViewerBindings(), createViewportKeyHandler(), VIEWPORT_BUTTON_CLASS, AsciiMapViewerContent() (+20 more)

### Community 352 - "revised-character-creation.spec.ts"
Cohesion: 0.09
Nodes (25): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+17 more)

### Community 353 - "HealthService"
Cohesion: 0.08
Nodes (23): HealthStatus, HealthService, Any, Create a standardized health check response dictionary. Args: status: Health…, Async database health check., check_database_health., Check connection manager health., Get server component health status. (+15 more)

### Community 354 - "asyncio"
Cohesion: 0.06
Nodes (31): asyncio, Test is_player_muted_async() returns True when player is muted., Test is_player_muted_async() returns False when player is not muted., Test add_admin() handles missing persistence (#679: injected, not via…, Test add_admin() handles player not found., Test remove_admin() handles missing persistence (#679: injected, not via…, Test remove_admin() handles player not found., Test is_admin() returns False when persistence not available (#679: injected). (+23 more)

### Community 355 - "parse_shutdown_parameters"
Cohesion: 0.14
Nodes (14): parse_shutdown_parameters(), Parse shutdown command parameters. Args: command_data: Command data dictionary…, Test parse_shutdown_parameters() with no args defaults to 10 seconds., Test parse_shutdown_parameters() with cancel action., Test parse_shutdown_parameters() with seconds., Test parse_shutdown_parameters() with negative seconds., Test parse_shutdown_parameters() with zero seconds., Test parse_shutdown_parameters() with invalid string. (+6 more)

### Community 356 - "test_npc_combat_handlers.py"
Cohesion: 0.07
Nodes (39): mock_combat_memory(), mock_combat_result(), mock_data_provider(), mock_lifecycle(), mock_messaging_integration(), mock_npc_instance(), mock_rewards(), npc_combat_handlers() (+31 more)

### Community 357 - "WebSocket Best Practices"
Cohesion: 0.05
Nodes (43): 1. Code Organization and Structure, 2. Common Patterns and Anti-patterns, 3. Performance Considerations, 4. Security Best Practices, 5. Testing Approaches, 6. Common Pitfalls and Gotchas, 7. Tooling and Environment, Anti-patterns (+35 more)

### Community 358 - "edgeModalLogic.ts"
Cohesion: 0.10
Nodes (30): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+22 more)

### Community 359 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 360 - "Async Code Review - Post Phase 2 Migration"
Cohesion: 0.05
Nodes (43): 1. Consistent Pattern Application, 2. Proper Async Propagation, 3. Exception Handling Preserved, 4. Resource Cleanup Maintained, 5. Proper Import Organization, 6. Documentation Added, After Migration, 🔍 Anti-Pattern Check (+35 more)

### Community 361 - "FastAPI Code Review - Anti-Patterns and Best Practices"
Cohesion: 0.05
Nodes (44): FastAPI Code Review, 10. ℹ️ **Dependency Injection Pattern**, 11. ℹ️ **API Versioning** (OPTIONAL - NOT REQUIRED FOR WEBAPP), 1. ✅ **Inconsistent Response Models** - **RESOLVED**, 1. Response Models (Critical Issue #1) ✅, 2. Dependency Injection (Critical Issue #3) ✅, 2. 🟡 **Fat Endpoints with Business Logic** - **IN PROGRESS**, 3. ✅ **Direct app.state Access Instead of Dependency Injection** - **RESOLVED** (+36 more)

### Community 362 - "E2E Test Suite AI Execution Improvements - Summary"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 363 - "NPCCombatIntegrationBase"
Cohesion: 0.07
Nodes (25): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Apply combat effects to a target (player or NPC). Args: target_id: ID of the…, Convert target_id to UUID, accepting either string or UUID input., Apply combat effects to a player. (+17 more)

### Community 364 - "DialogueDefinitionRepository"
Cohesion: 0.09
Nodes (36): DialogueDefinition, Base, NPC dialogue tree template: id (PK), definition JSONB, optional npc link., _as_dialogue_row(), _definition_dict(), DialogueDefinitionRepository, _DialogueRow, Protocol (+28 more)

### Community 365 - "ConnectionCleaner"
Cohesion: 0.08
Nodes (27): ConnectionCleaner, Any, UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return connection IDs that exceed max_connection_age., Extract player_id from connection metadata if present. (+19 more)

### Community 366 - "TestHierarchicalSchema"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 367 - "service.py"
Cohesion: 0.04
Nodes (75): PassiveLucidityFluxService, FluxServiceConfig, lookup_profile(), normalize_environment_config(), period_label(), Any, datetime, Configuration and normalization for passive lucidity flux. (+67 more)

### Community 368 - "JsonMap"
Cohesion: 0.08
Nodes (16): Msg, _as_json_map(), _NatsListenerClient, NatsMessageCallback, _NatsSubscribeFn, _NatsSubscription, JsonMap, Protocol (+8 more)

### Community 369 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, properties, field1, field2, field3, sub_zone (+3 more)

### Community 370 - "properties"
Cohesion: 0.17
Nodes (12): description, description, description, description, maxLength, minLength, type, properties (+4 more)

### Community 371 - "properties"
Cohesion: 0.11
Nodes (19): description, description, description, description, type, description, maxLength, minLength (+11 more)

### Community 372 - "log_and_raise_enhanced"
Cohesion: 0.03
Nodes (92): PlayerCreationService, Any, Stats, UUID, Player creation service. This module handles player character creation…, Create a new player character with specific stats. Args: name: The player's…, Service for player creation operations., Initialize with persistence layer, schema converter, and optional instance… (+84 more)

### Community 373 - "TrackedTaskManager"
Cohesion: 0.09
Nodes (30): get_global_tracked_manager(), memory_leak_prevention_channel_start_session(), patch_asyncio_create_task_with_tracking(), Global TrackedTaskManager for Memory Leak Prevention Infrastructure. This…, Audit and reclaim orphaned task candidates across the system. Returns: Number…, Proactively clean up orphaned tasks by cancelling leak prevention violations.…, Return count of currently tracked task references within the manager's…, Attach a TaskRegistry instance to this Tracker for shared coordination. Args:… (+22 more)

### Community 374 - "test_admin_teleport_commands.py"
Cohesion: 0.16
Nodes (42): handle_confirm_goto_command(), handle_confirm_teleport_command(), handle_goto_command(), handle_teleport_command(), Any, Handle the goto command for teleporting the admin to a player's location. Args:…, Handle the confirm teleport command for executing the actual teleportation.…, Handle the confirm goto command for executing the actual teleportation. Args:… (+34 more)

### Community 375 - "test_connection_disconnection_websockets.py"
Cohesion: 0.09
Nodes (29): mock_manager(), mock_safe_close_websocket(), asyncio, fixture, UUID, Unit tests for connection disconnection websocket functions. Tests the…, Test disconnect_connection_by_id_impl() disconnects websocket connection., Regression: e2e logout hit WebSocketDisconnect on close and aborted leave… (+21 more)

### Community 376 - "SpellMaterialsService"
Cohesion: 0.18
Nodes (10): Any, UUID, Build final inventory with consumed materials removed. Args: inventory:…, Consume spell materials from player inventory. Args: player_id: Player ID…, Service for handling spell material requirements. Handles checking if players…, Initialize the spell materials service. Args: player_service: Player service…, Check if player has all required materials. Args: player_id: Player ID spell:…, Process a single material requirement. Args: material: Material requirement… (+2 more)

### Community 377 - "test_lint_raw_sql_in_python.py"
Cohesion: 0.08
Nodes (33): _LintRawSqlModule, _load_script(), Protocol, Unit tests for scripts/lint_raw_sql_in_python.py. Verifies the detection logic…, Ordinary English sentence-case prose ('Select ... from ...') must not match --…, Under GITHUB_ACTIONS, an overdue entry renders as a ::warning:: annotation so…, A file with more raw-SQL sites than its allowlist entry expects fails -- a…, A file with fewer raw-SQL sites than its allowlist entry expects fails -- a… (+25 more)

### Community 378 - "test_rest_and_grace_period.py"
Cohesion: 0.07
Nodes (38): mock_app_with_services(), mock_connection_manager_full(), mock_persistence_full(), MockPersistenceFull, asyncio, fixture, Integration tests for rest command and disconnect grace period. Tests the…, Allow setting get_player_by_name and get_room_by_id to mocks. (+30 more)

### Community 379 - "retry.py"
Cohesion: 0.16
Nodes (19): _create_async_wrapper(), _create_sync_wrapper(), _is_asyncpg_transient(), _is_psycopg2_transient(), is_transient_error(), _is_wrapped_transient_message(), _log_retry_attempt(), _log_retry_failure() (+11 more)

### Community 380 - "TestCombatConfigurationService"
Cohesion: 0.05
Nodes (23): fixture, Test suite for CombatConfigurationService class., Create a mock config object., Create a CombatConfigurationService instance for testing., Test CombatConfigurationService initialization., Test get_combat_configuration returns configuration., Test get_combat_configuration caches configuration., Test get_combat_configuration_for_scope with global scope. (+15 more)

### Community 381 - "properties"
Cohesion: 0.14
Nodes (14): description, description, description, description, type, properties, field1, field2 (+6 more)

### Community 382 - "Any"
Cohesion: 0.10
Nodes (11): Any, Initialize the room cache service. Args: persistence: Persistence layer instance, Get room data with caching. Args: room_id: The room ID Returns: Room data…, Get room data with caching (synchronous version). Args: room_id: The room ID…, Initialize the NPC cache service. Args: npc_service: NPC service instance, Get NPC definitions with caching. Args: session: Database session Returns: List…, Get a specific NPC definition with caching. Args: session: Database session…, Get NPC spawn rules with caching. Args: session: Database session Returns: List… (+3 more)

### Community 383 - "quest_commands.py"
Cohesion: 0.06
Nodes (57): _active_npc_ids_in_room(), _emit_npc_lines_for_results(), _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence(), _get_quest_service() (+49 more)

### Community 384 - "NPCSpawnRule"
Cohesion: 0.05
Nodes (38): _JSONDict, _loads_json_dict(), NPCSpawnRule, Set base stats from dictionary., Get behavior configuration as dictionary., Set behavior configuration from dictionary., Get AI integration stub configuration as dictionary., Set AI integration stub configuration from dictionary. (+30 more)

### Community 385 - "test_nats_service_health.py"
Cohesion: 0.07
Nodes (37): nats_config(), nats_service(), asyncio, fixture, NATS health-check, batch flush, and subscription-lifecycle tests., Test _stop_health_monitoring() handles no task., Test publish_batch() adds message to batch., Test publish_batch() flushes when batch is full. (+29 more)

### Community 386 - "test_channel_commands.py"
Cohesion: 0.09
Nodes (40): _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting(), Any, Channel management commands for Advanced Chat Channels. This module provides…, Validate channel name. Returns error dict if invalid, None if valid., Handle the channel command for switching channels or setting default channel.… (+32 more)

### Community 387 - "test_quest_commands.py"
Cohesion: 0.09
Nodes (38): ExitStack, handle_quest_command(), Handle quest command subcommands: abandon, ask, turnin. Usage: quest abandon…, current_user(), _enter_quest_command_patches(), mock_request(), asyncio, fixture (+30 more)

### Community 388 - "CORSConfig"
Cohesion: 0.07
Nodes (30): CORSConfig, Any, BaseSettings, field_validator, model_validator, CORS (Cross-Origin Resource Sharing) configuration model., Parse comma-separated string into cleaned list., Parse comma separated strings or lists into a cleaned list of strings. (+22 more)

### Community 389 - "resolve_weapon_attack_from_equipped"
Cohesion: 0.08
Nodes (36): Pydantic models for item prototype validation. This module defines the…, Prototype registry for managing item prototypes. This module provides the…, _prototype_from_equipped_stack(), NamedTuple, PrototypeRegistry, Weapon resolution helpers for combat. Resolves equipped main-hand items to…, Result of resolving an equipped item to a weapon attack. base_damage: Rolled…, Resolve equipped main-hand stack to weapon attack info, or None if unarmed. (+28 more)

### Community 390 - "test_rate_limiter_utils.py"
Cohesion: 0.04
Nodes (52): fixture, rate_limiter(), Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…, Test get_rate_limit_info returns correct info with requests., Test get_rate_limit_info calculates reset time correctly., Test get_rate_limit_info calculates retry_after correctly., Test get_rate_limit_info filters out old requests., Test enforce_rate_limit allows request within limit. (+44 more)

### Community 391 - "MagicCommandHandler"
Cohesion: 0.10
Nodes (20): MagicCommandHandler, Any, Exception, Resolve player and spell parameters for a cast; returns error message if…, Build the response payload for a cast result and send announcements., Build the final success message for a cast spell., If player is resting, cancel rest countdown so they can cast. Swallows errors…, Handle /spells command - list learned spells. Args: command_data: Command data… (+12 more)

### Community 392 - "log_with_context"
Cohesion: 0.06
Nodes (36): correct_request_context(), Demonstrate correct request context binding., add_request_context(), websocket, WebSocket endpoint with enhanced logging., Background task for player update with enhanced logging., Add request context to all log entries using enhanced logging., update_player_background_task() (+28 more)

### Community 393 - "TestEmitLootAllEvent"
Cohesion: 0.10
Nodes (22): _assert_warning_once(), _diff_items_from_emit(), mock_connection_manager(), asyncio, ConnectionManager, fixture, Test emit_loot_all_event handles emission errors gracefully., Test emit_loot_all_event correctly calculates items_removed in diff. (+14 more)

### Community 394 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 395 - "correct_patterns.py"
Cohesion: 0.05
Nodes (35): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+27 more)

### Community 396 - "look_command.py"
Cohesion: 0.04
Nodes (90): _app_from_request(), _as_response(), _connection_manager_from_app(), _container_from_app(), _get_app_and_persistence(), _get_room_drops(), _handle_implicit_target_lookup(), handle_look_command() (+82 more)

### Community 397 - "test_game_tick_processing_async.py"
Cohesion: 0.07
Nodes (39): mock_app(), mock_container(), mock_player(), asyncio, fixture, Unit tests for game tick processing async functions. Tests the async game tick…, Test _process_single_effect() with damage_over_time effect., Test _process_single_effect() with heal_over_time effect. (+31 more)

### Community 398 - "inventory_command_helpers.py"
Cohesion: 0.02
Nodes (153): _DropResolved, _FloorPickupResolved, Parse numeric fields from object-typed JSON command payloads., Protocol, Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, add_pickup_to_inventory(), broadcast_room_event() (+145 more)

### Community 399 - "player_connection_setup.py"
Cohesion: 0.11
Nodes (38): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions. This module handles the setup tasks when a…, Broadcast a structured entry event to other occupants (excluding the newcomer).… (+30 more)

### Community 400 - "HolidayService"
Cohesion: 0.06
Nodes (33): HolidayCollection, Wrapper for the complete holiday JSON payload., HolidayService, Path, Load holidays from PostgreSQL database., Get the holiday collection. Returns: HolidayCollection: The loaded holiday…, Tracks active Mythos holidays and upcoming triggers., patch (+25 more)

### Community 401 - "StatsGenerator"
Cohesion: 0.13
Nodes (23): Character creation service for MythosMUD server. This module handles all…, generate_random_stats(), Stats Generator Service for MythosMUD. This module provides random stat…, Generate Stats with random attribute values. Factory function for creating…, Service for generating random character statistics., Initialize the stats generator., StatsGenerator, asyncio (+15 more)

### Community 402 - "SubjectValidator"
Cohesion: 0.07
Nodes (39): Custom exceptions for NATS Subject Manager. This module defines all exception…, Exception raised when subject validation fails., SubjectValidationError, NATS Subject Manager for MythosMUD. This module provides centralized subject…, Predefined subject patterns for MythosMUD chat system. This module contains all…, get_chat_subscription_patterns(), get_event_subscription_patterns(), get_subscription_pattern() (+31 more)

### Community 403 - "Any"
Cohesion: 0.07
Nodes (17): Any, AsyncSession, UUID, Get a list of rooms adjacent to the specified room. Args: room_id: The room's…, Get the scope of rooms for local chat (current room + adjacent rooms). Args:…, Validate that there's a valid exit from one room to another. Args:…, Get all occupants (players and NPCs) currently in a room using cached data.…, Get all exits from a room. Args: room_id: The ID of the room Returns: dict[str,… (+9 more)

### Community 404 - "test_message_broadcaster.py"
Cohesion: 0.07
Nodes (41): message_broadcaster(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for message broadcaster. Tests the MessageBroadcaster class., Test broadcast_global() excludes specified player., Test broadcast_global() when no players online. (+33 more)

### Community 405 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 406 - "GameClientV2ContainerView.tsx"
Cohesion: 0.07
Nodes (22): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, maxWidthClasses, ModalContainer() (+14 more)

### Community 407 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 408 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 409 - "test_quality_fragmentation_guard.py"
Cohesion: 0.10
Nodes (39): _build_python_call_usage_map(), _call_target_name(), Call, ChangedFile, Build a repo-wide call usage map from Python AST call sites., scan_changed_files(), _ChangedFile, _load_guard_module() (+31 more)

### Community 410 - "NPCLifecycleRecord"
Cohesion: 0.08
Nodes (15): Get room from persistence and handle errors., Clean up lifecycle record and active NPCs on spawn failure., Spawn an NPC instance. Thin wrapper around _spawn_npc_impl to keep public…, Internal implementation for spawning an NPC with full error handling., Handle failure when the spawning service cannot create an NPC instance., Handle logging and lifecycle updates for a failed spawn., Generate a unique NPC ID. Args: definition: NPC definition room_id: Room where…, Get lifecycle record for an NPC. Args: npc_id: ID of the NPC Returns: Lifecycle… (+7 more)

### Community 411 - "asyncio"
Cohesion: 0.07
Nodes (27): asyncio, Test _spawn_optional_npcs() spawns based on probability., Test _spawn_optional_npcs() skips NPCs with low probability., Test _determine_spawn_room() uses NPC's room_id when available., Test _determine_spawn_room() uses sub_zone default when room_id not available., Test _determine_spawn_room() uses fallback room when no other option., Test _determine_spawn_room() returns None when persistence not available., Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute. (+19 more)

### Community 412 - "RoomCacheService"
Cohesion: 0.15
Nodes (7): Service for caching room data., Invalidate cached room data. Args: room_id: The room ID to invalidate, Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload, RoomCacheService, Any, _RoomObj, TestRoomCacheService

### Community 413 - "transfer_all_items_from_container"
Cohesion: 0.13
Nodes (16): InventoryStack, Transfer all items from container to player, returning updated container and…, transfer_all_items_from_container(), asyncio, Test transfer_all_items_from_container function., Test transfer_all_items_from_container transfers all items., Test transfer_all_items_from_container stops on capacity error., Test transfer_all_items_from_container continues on transfer error. (+8 more)

### Community 414 - "inventory_get_command.py"
Cohesion: 0.13
Nodes (34): _container_transfer_messages(), _get_from_container_path(), _get_route_after_validation(), _get_transfer_out_of_container(), GetCommandRuntime, GetItemSpec, handle_get_command(), _handle_get_from_room() (+26 more)

### Community 415 - "._cleanup_player_mutes"
Cohesion: 0.12
Nodes (11): datetime, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired player mutes., Clean up expired channel mutes., Clean up expired global mutes., Clean up expired mutes from all storage. (+3 more)

### Community 416 - "_make_session_context"
Cohesion: 0.11
Nodes (27): _make_session_context(), asyncio, Test get_by_player_and_quest returns mapped instance when found., Test get_by_player_and_quest returns None when not found., Test get_by_player_and_quest accepts UUID for player_id., Test update_state_and_progress updates and commits., Test update_state_and_progress still calls procedure and commit when only…, Test list_active_by_player returns list of mapped active instances. (+19 more)

### Community 417 - "disconnect_grace_period.py"
Cohesion: 0.09
Nodes (37): cancel_grace_period(), is_player_in_grace_period(), Any, UUID, Disconnect grace period management for MythosMUD. This module handles the…, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, Check if a player is currently in grace period. Args: player_id: The player's…, Start a grace period for a disconnected player. During the grace period, the… (+29 more)

### Community 418 - "TestCombatMessagingService"
Cohesion: 0.07
Nodes (22): asyncio, fixture, Test get_death_message with custom template., Test get_combat_start_messages generates messages for all occupants., Test get_combat_start_messages with single occupant., Test get_combat_end_messages generates messages for all occupants., Test suite for CombatMessagingService class., Test get_combat_end_messages from winner perspective. (+14 more)

### Community 419 - "WebSocketRateLimiter"
Cohesion: 0.40
Nodes (3): WebSocket rate limiter with enhanced logging., Check if client is within rate limit with enhanced logging., WebSocketRateLimiter

### Community 420 - "follow_movement.py"
Cohesion: 0.12
Nodes (21): drop_follower(), ensure_follower_standing(), follower_already_in_room(), follower_needs_stand(), _FollowMovementHost, on_npc_entered_room(), on_player_entered_room(), propagate_follower_move() (+13 more)

### Community 421 - "test_magic_service.py"
Cohesion: 0.15
Nodes (38): CastingState, Represents an active spell casting state., MagicService, Public API: composition of completion, healing, and core spellcasting logic., _build_magic_service(), mock_player(), player_id(), Any (+30 more)

### Community 422 - "test_command_helpers_functions.py"
Cohesion: 0.05
Nodes (49): Unit tests for command_helpers utility functions. Tests the utility functions…, Test validate_command_safety() returns True for safe commands., Test validate_command_safety() returns False for shell metacharacters., Test validate_command_safety() returns False for SQL injection attempts., Test validate_command_safety() returns False for Python injection attempts., Test validate_command_safety() returns False for format string injection., Test validate_command_safety() returns False for XSS attempts., Test get_command_help() returns help for specific command. (+41 more)

### Community 423 - "test_npc_event_handlers_helpers.py"
Cohesion: 0.09
Nodes (25): mock_connection_manager(), mock_message_builder(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers helper functions. Tests the helper functions…, Test _determine_direction_from_rooms() determines direction., Test _determine_direction_from_rooms() returns None when direction not found. (+17 more)

### Community 424 - "test_player_service.py"
Cohesion: 0.06
Nodes (45): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service CRUD and lookup. Delete, location, mythos status,…, Test get_player_by_id() when player is not found., Test get_player_by_name() when player is found., Test get_player_by_name() when player is not found. (+37 more)

### Community 425 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 426 - "test_admin_shutdown_command.py"
Cohesion: 0.06
Nodes (50): _asyncio_mark, _AppWithoutState, _await_shutdown_result(), _InitiateAppStub, _InitiateStateStub, Unit tests for admin shutdown command handler. Tests the shutdown command…, Test handle_shutdown_command() when player service is not available., Test handle_shutdown_command() when player is not found. (+42 more)

### Community 427 - "useRoomEditModal.ts"
Cohesion: 0.07
Nodes (17): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, fieldBorderClass(), RoomEditDescriptionField(), RoomEditFormData, RoomEditModalForm() (+9 more)

### Community 428 - "multiplayer-browser-helpers.js"
Cohesion: 0.12
Nodes (33): buttonHasLoginSubmitLabel(), captureGameUiDiagnosticsInBrowser(), captureOccupantsSnapshotInBrowser(), coalesce(), computedStyleHidesElement(), elementShowsConnectedStatus(), elementTextIncludesGameInfo(), evaluateGameUiLoaded() (+25 more)

### Community 429 - "Chat Panel Separation Implementation Tasks"
Cohesion: 0.14
Nodes (13): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Functional Metrics, Overview, Phase Dependencies, Quality Metrics (+5 more)

### Community 430 - "Async Persistence Migration Plan"
Cohesion: 0.05
Nodes (37): 1.1 Find all PersistenceLayer usage, 1.2 Document call sites, 2.1 Update ApplicationContainer, 2.2 Update lifespan.py, 2.3 Migrate API endpoints, 2.4 Migrate services, 2.5 Migrate commands, 2.6 Update test fixtures (+29 more)

### Community 431 - "migration_examples.py"
Cohesion: 0.06
Nodes (36): expensive_operation(), migration_example_1(), migration_example_10(), migration_example_11(), migration_example_12(), migration_example_13(), migration_example_14(), migration_example_15() (+28 more)

### Community 432 - "test_game_tick_death.py"
Cohesion: 0.08
Nodes (40): cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _CorpseLike, _create_corpse_lifecycle_service(), _log_cleanup_results(), FastAPI, Protocol, Decayed corpse cleanup for the game tick loop. (+32 more)

### Community 433 - "MessageBroadcaster"
Cohesion: 0.09
Nodes (24): SendPersonalMessage, Messaging components for connection management. This package provides modular…, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Message broadcasting for connection management. This module provides room and…, Convert string player IDs to UUIDs for message sending. Args: target_list: List… (+16 more)

### Community 434 - "CombatCommandHandler"
Cohesion: 0.02
Nodes (123): CombatCommandHandler, CombatCommandHandlerExtras, _NpcWithLife, Any, AppWithState, ConnectionManager, Protocol, Combat command handler class and shared helpers. Extracted from combat.py to… (+115 more)

### Community 435 - "generate_invites.py"
Cohesion: 0.38
Nodes (6): generate_invite_code(), generate_unique_codes(), main(), Generate a unique Mythos-themed invite code., Generate a list of unique invite codes and store them in the database., Generate invite codes and store them in the database.

### Community 436 - "spell_effects_support.py"
Cohesion: 0.11
Nodes (33): apply_stat_modifications(), Apply stat modification dict to stats. Returns (updated stats, stat_changes,…, _apply_stat_modify_to_player(), _build_stat_modifications(), _create_object_for_player(), _create_object_for_room(), process_create_object_effect(), process_stat_modify_effect() (+25 more)

### Community 437 - "test_connection_error_methods.py"
Cohesion: 0.16
Nodes (25): delegate_error_handler(), Generic delegate for error handler methods. Args: error_handler: Error handler…, detect_and_handle_error_state_impl(), handle_authentication_error_impl(), handle_security_violation_impl(), handle_websocket_error_impl(), Any, UUID (+17 more)

### Community 438 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 439 - "AttributeError"
Cohesion: 0.06
Nodes (47): AttributeError, Test _create_player_occupant_info handles grace period check exceptions., test_create_player_occupant_info_grace_period_exception(), mock_combat_service(), mock_player(), persistence_handler(), asyncio, fixture (+39 more)

### Community 440 - "CombatCommandFactory"
Cohesion: 0.08
Nodes (32): Unit tests for combat command factories. Tests the CombatCommandFactory class…, Test create_attack_command() creates AttackCommand., Test create_attack_command() allows None target (validation happens later)., Test create_punch_command() creates PunchCommand., Test create_punch_command() allows None target (validation happens later)., Test create_kick_command() creates KickCommand., Test create_kick_command() allows None target (validation happens later)., Test create_strike_command() creates StrikeCommand. (+24 more)

### Community 441 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)"
Cohesion: 0.13
Nodes (15): Communities (10 total, 4 thin omitted), Community 0 - "Azathoth / Byakhee", Community 1 - "Call of Cthulhu / Chaosium Inc.", Community 2 - "Dimensional Shambler / Elder Thing", Community 3 - "Abhoth / Atlach-Nacha", Community 4 - "Deep One / Ghast", Community 5 - "Dark Young / Dark Young of Shub-Niggurath", Community Hubs (Navigation) (+7 more)

### Community 442 - "Phase 3, Task 3.2: NATS Subject Manager Usage Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 443 - "Execution Steps"
Cohesion: 0.05
Nodes (36): BEFORE EXECUTING THIS SCENARIO, YOU MUST, BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, CONFIRMATION CHECKLIST, EXECUTION AFFIRMATION (Type this before proceeding), 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER, Execution Steps, Expected Results (+28 more)

### Community 444 - "properties"
Cohesion: 0.12
Nodes (17): description, items, type, properties, default, description, type, type (+9 more)

### Community 445 - "properties"
Cohesion: 0.11
Nodes (19): integer, minimum, type, minimum, type, null, maxLength, minLength (+11 more)

### Community 446 - "ChatModeration"
Cohesion: 0.10
Nodes (20): ChatModeration, normalize_player_id(), UUID, Mute a specific channel for a player., Unmute a specific channel for a player., Check if a channel is muted for a player., Mute a specific player for another player., Unmute a specific player for another player. (+12 more)

### Community 447 - "EmoteService"
Cohesion: 0.07
Nodes (31): EmoteDefinition, EmoteService, _get_emote_validator(), TypedDict, Emote Service for handling predefined emote actions and their messages. This…, Check if a command is an emote alias. Args: command: The command to check…, Get the emote definition for a command. Args: command: The command (emote name…, Format emote messages for the player and room occupants. Args: command: The… (+23 more)

### Community 448 - "test_auth_rate_limit.py"
Cohesion: 0.11
Nodes (34): assert_auth_rate_limit_paths_registered(), _auth_bucket(), auth_client_key(), auth_rate_limit_response(), _collect_post_paths(), _HasPrefix, _HasRoutes, _IncludedRouterLike (+26 more)

### Community 449 - "test_player_related_models.py"
Cohesion: 0.09
Nodes (24): PlayerExploration, Base, Junction table tracking which rooms each player has explored., Unit tests for Player-related SQLAlchemy models. Tests…, Test PlayerInventory has correct table name., Test PlayerInventory __repr__ method., Test PlayerExploration can be instantiated with required fields., Test PlayerExploration has correct table name. (+16 more)

### Community 450 - "PersonalMessageSender"
Cohesion: 0.05
Nodes (55): PersonalMessageSender, Any, UUID, Send message to a single WebSocket connection. Returns True if successful., Queue message if no active connections., Send a personal message to a player via WebSocket. Args: player_id: The…, Get message delivery statistics for a player., Sends personal messages to individual players. This class provides: - Personal… (+47 more)

### Community 451 - "Any"
Cohesion: 0.11
Nodes (13): Any, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string…, Evaluate boolean conditions and variable lookups. Args: condition: Condition…, Evaluate a condition string against context. Args: condition: Condition string… (+5 more)

### Community 452 - ".load_room_data"
Cohesion: 0.06
Nodes (19): Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path., Validate or update room ID based on filename and location., Validate required fields are present., Add location fields if missing. (+11 more)

### Community 453 - "CharacterNameScreen.tsx"
Cohesion: 0.06
Nodes (41): buildCreateCharacterPayload(), CharacterNameScreen(), CreateCharacterPayload, getCreateCharacterErrorMessage(), OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, MotdContent() (+33 more)

### Community 454 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 455 - "Async Persistence Migration Tracker"
Cohesion: 0.06
Nodes (34): PassiveLucidityFluxService, 17-Second Game Tick Delay, Three-Phase Async Remediation, Room Cache TTL (60s), Async Persistence Migration Tracker, Current Status, Decision Tree, Files Requiring Migration (+26 more)

### Community 456 - "PostgreSQL & SQL Audit Report"
Cohesion: 0.06
Nodes (36): 10. Prioritized Fixes, 11. Summary Table, 1.1. Snake_case (GOOD), 1.2. Quoted Identifier, 1. Naming Conventions, 2.1. Uppercase SQL Keywords, 2. SQL Formatting (Keywords Lowercase), 3.1. Explicit Joins (GOOD) (+28 more)

### Community 457 - "LRUCache"
Cohesion: 0.08
Nodes (20): K, LRUCache, Put an item into the cache. Args: key: The key to store value: The value to…, Delete an item from the cache. Args: key: The key to delete Returns: True if…, Clear all items from the cache., Get the current number of items in the cache., Check if the cache is at maximum capacity., Get cache statistics. Returns: Dictionary containing cache statistics (+12 more)

### Community 458 - "GameMechanicsService"
Cohesion: 0.10
Nodes (25): GameMechanicsService, Game mechanics service for MythosMUD server. This module handles all game…, Heal a player's health., Damage a player's health., Award experience points to a player. CRITICAL FIX: This method prevents XP…, Service class for game mechanics operations., Initialize the game mechanics service with a persistence layer., Apply lucidity loss to a player. (+17 more)

### Community 459 - "log_and_raise"
Cohesion: 0.03
Nodes (139): _create_engine_or_raise(), Create async engine or raise a typed configuration/connection error., _coerce_row_quantity(), fetch_container_items(), _item_dict_from_contents_row(), _metadata_dict_from_cell(), parse_jsonb_column(), PsycopgConnection (+131 more)

### Community 460 - "test_container_persistence_sql_injection.py"
Cohesion: 0.17
Nodes (10): _create_mock_container_row(), UUID, Tests for SQL injection protection in container persistence operations. These…, Test that update_container uses parameterized queries, not string concatenation., Test that column names are hardcoded, not from user input., Create a complete mock container row with all required columns., Test SQL injection protection in container persistence., Test that SQL injection in lock_state is prevented. (+2 more)

### Community 461 - "TestNPCCombatRewards"
Cohesion: 0.08
Nodes (20): asyncio, fixture, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class., Test award_xp_to_killer handles zero XP. (+12 more)

### Community 462 - "lint_optional_auth_no_guard.py"
Cohesion: 0.10
Nodes (30): expr, AllowlistEntry, _auth_posture(), _body_has_direct_guard(), _called_helper_names(), _collect_files(), _dep_names_in_default(), _find_unguarded() (+22 more)

### Community 463 - "3. Common Patterns and Anti-patterns"
Cohesion: 0.09
Nodes (21): 1.1. Base Configuration, 1.2. TypeScript Integration (Type-Aware Linting), 1.3. Prettier Integration, 1. Core Configuration: Flat Config is Mandatory, 2. Code Organization and Structure, 3.1. Immutability (`prefer-const`), 3.2. Unused Variables (`no-unused-vars`), 3.3. Consistent Returns (`consistent-return`) (+13 more)

### Community 464 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 465 - "executeCommand"
Cohesion: 0.10
Nodes (35): expectWhoListingOnPage(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), ensureIthaquaInFoyer() (+27 more)

### Community 466 - "enum"
Cohesion: 0.11
Nodes (19): ACCESSORY, AMULET, BELT, CURSED, FEET, GLOW, HANDS, HEAD (+11 more)

### Community 467 - "AliasGraph"
Cohesion: 0.09
Nodes (21): Unit tests for alias_graph utilities. Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+13 more)

### Community 468 - "test_npc_startup_service.py"
Cohesion: 0.08
Nodes (24): npc_startup_service(), fixture, Unit tests for NPC startup service. Tests the NPCStartupService class., Test _get_default_room_for_sub_zone() returns correct room for known sub-zone., Test _get_default_room_for_sub_zone() returns None for unknown sub-zone., Test _get_default_room_for_sub_zone() is case insensitive., #679: NPCStartupService no longer reaches ApplicationContainer.get_instance()…, Test _spawn_optional_npcs() handles missing spawn room. (+16 more)

### Community 469 - "NPCThreadManager"
Cohesion: 0.04
Nodes (73): NPCThreadManager, Start a thread for a specific NPC. Args: npc_id: Unique identifier for the NPC…, Stop a specific NPC thread. Args: npc_id: Unique identifier for the NPC…, Internal method to stop an NPC thread., Restart a specific NPC thread. Args: npc_id: Unique identifier for the NPC…, Get list of active NPC thread IDs., Get NPC definition for a specific NPC., Worker function for individual NPC threads. This function runs in a separate… (+65 more)

### Community 470 - "asyncio"
Cohesion: 0.10
Nodes (21): asyncio, Test publish_game_tick_event() when NATS is not connected., Persistence lookup should replace Player_/Room_ fallbacks in event data., Legacy subject strings when subject_manager is unset., tick_number from additional_metadata should win over sequence., publish() returning False should surface as False from EventPublisher., Test publish_player_entered_event() successfully publishes., Test publish_player_entered_event() when NATS is not connected. (+13 more)

### Community 471 - "Stats"
Cohesion: 0.12
Nodes (13): Any, Stats, Roll Size using formula: (2D6+6)*5 (range 40-90)., Roll stats using 3d6 method (scaled to 15-90 range)., Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)., Generate stats using a point-buy system (balanced, scaled to 1-100 range)., Check if stats meet the prerequisites for a given class. Args: stats: The…, Get a list of classes that the character qualifies for. Args: stats: The… (+5 more)

### Community 472 - "test_player_preferences_service.py"
Cohesion: 0.02
Nodes (111): mock_session(), preferences_service(), asyncio, fixture, Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID. (+103 more)

### Community 473 - "roomHandlers.ts"
Cohesion: 0.05
Nodes (60): eventHandlers, buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata() (+52 more)

### Community 474 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 475 - "InventoryCommandFactory"
Cohesion: 0.10
Nodes (27): Test create_pickup_command() with numeric index., Test create_pickup_command() with quantity., test_create_pickup_command_with_index(), test_create_pickup_command_with_quantity(), Test create_pickup_command() creates PickupCommand., Test create_pickup_command() raises error with no args., Test create_pickup_command() raises error when quantity is zero., Test create_pickup_command() raises error when quantity is negative. (+19 more)

### Community 476 - "test_shutdown_process_termination.py"
Cohesion: 0.08
Nodes (24): _find_uvicorn_processes(), Any, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available., _terminate_child_processes(), _terminate_uvicorn_processes() (+16 more)

### Community 477 - "._build_player_attacked_event"
Cohesion: 0.11
Nodes (12): UUID, Resolve the player and UUID needed for DP update events., Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated., Publish the PlayerDPUpdated event to the event bus., Publish NPC-on-player attack as player_attacked to NATS so the client receives…, Resolve the combat event publisher used to send PlayerAttacked events to NATS., Resolve target UUID, player object, and stats needed for NATS attack event., Construct the PlayerAttackedEvent payload for NATS publication. (+4 more)

### Community 478 - "test_room_utils.py"
Cohesion: 0.04
Nodes (61): ChatChannelLoggerMixin, Any, Path, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper…, Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs. (+53 more)

### Community 479 - "npc_config_parsing.py"
Cohesion: 0.12
Nodes (22): Initialize the NPC base class., apply_dp_from_source(), apply_idle_movement_defaults(), _compute_max_dp(), get_combat_stats_dict(), normalize_determination_points(), parse_ai_config(), parse_behavior_config() (+14 more)

### Community 480 - "test_connection_event_helpers.py"
Cohesion: 0.14
Nodes (23): Any, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events., subscribe_to_room_events_impl(), unsubscribe_from_room_events_impl(), asyncio, Unit tests for connection event helpers. Tests the connection_event_helpers…, Test unsubscribe_from_room_events_impl() handles AttributeError. (+15 more)

### Community 481 - "_make_session_context"
Cohesion: 0.12
Nodes (23): _make_session_context(), asyncio, Test get_by_id raises DatabaseError on DB failure., Test get_by_name returns definition when found by common name., Test get_by_name returns None when not found., Test get_by_name raises DatabaseError on DB failure., Test list_quest_ids_offered_by returns quest IDs for entity (procedure returns…, Test list_quest_ids_offered_by returns empty list when no offers. (+15 more)

### Community 482 - "BehaviorEngine"
Cohesion: 0.09
Nodes (19): BehaviorEngine, Deterministic behavior engine for NPCs. This engine evaluates rules based on…, Initialize the behavior engine., Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…, Get the behavior engine for this NPC., Test _evaluate_equality() returns True for matching condition., Test _evaluate_numeric_comparison() raises ValueError for non-numeric values., Test get_applicable_rules() returns matching rules. (+11 more)

### Community 483 - "Test Pruning Candidates - Detailed List"
Cohesion: 0.06
Nodes (33): 1. Command Validation Tests, 2. Error Response Tests, 3. Permission Check Tests, Aggressive Estimate (Full Optimization), Category A: Infrastructure Tests Testing Framework Behavior, Category B: Coverage Tests Written for Metrics, Category C: Model Property Tests, Conclusion (+25 more)

### Community 484 - ".get_upcoming_holidays"
Cohesion: 0.10
Nodes (12): _ensure_utc(), datetime, Update the active holiday window for the provided Mythos timestamp., Return currently active holiday entries., Get active holidays and serialize them for API responses. This method…, Get upcoming holidays and serialize them for API responses. This method…, Convenience helper for formatted admin output., Return the next N holidays, wrapping around the calendar. (+4 more)

### Community 485 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 486 - "Stop-MythosMudProjectProcessTree"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 487 - "test_game_tick_processing.py"
Cohesion: 0.07
Nodes (37): process_combat_tick(), process_npc_maintenance(), Process NPC lifecycle maintenance (every 60 ticks = 1 minute)., Process combat auto-progression., Check if NPC maintenance should run on this tick. Args: tick_count: Current…, asyncio, Unit tests for game tick processing functions. Tests the game tick processing…, Test _validate_app_state_for_status_effects returns False when no… (+29 more)

### Community 488 - "test_chat_message_senders.py"
Cohesion: 0.27
Nodes (21): _attr(), _ctx(), _player(), asyncio, ChatMessage, Unit tests for chat message senders., MagicMock attributes are Any; getattr+cast is the typed access path., test_normalize_player_id() (+13 more)

### Community 489 - "ItemPrototypeModel"
Cohesion: 0.11
Nodes (22): Constants supporting item prototype validation. These enumerations anchor the…, ItemPrototypeModel, BaseModel, field_validator, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validated representation of an item prototype definition. This model keeps the…, Validate that item_type is in the allowed list. Args: value: The item type to… (+14 more)

### Community 490 - "Any"
Cohesion: 0.10
Nodes (16): Any, Task, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task…, Cancel specific task with logical timeout boundaries. Args: task: Task…, Metadata for tracked asyncio.Tasks. (+8 more)

### Community 491 - "CombatMessagingService"
Cohesion: 0.12
Nodes (12): CombatMessages, CombatMessagingService, Any, Generate combat start messages for all room occupants. Args: attacker_name:…, Generate combat end messages for all room occupants. Args: winner_name: Name of…, Generate thematic error messages for combat actions. Args: error_type: Type of…, Validate NPC message templates against the schema. Args: messages_data: NPC…, Service for generating combat messages. This service creates thematic,… (+4 more)

### Community 492 - "EventPublisher"
Cohesion: 0.18
Nodes (10): EventPublisher, JsonMap, Publish a player_entered event to NATS. Args: player_id: ID of the player who…, Publish a player_left event to NATS. Args: player_id: ID of the player who left…, Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…, Create a standardized event message structure. Args: event_type: Type of event…, Get the next sequence number for event ordering. Returns: Next sequence number, Reset the sequence number to 0. (+2 more)

### Community 493 - "HolidayEntry"
Cohesion: 0.14
Nodes (18): HolidayEntry, Create a mapping of holiday IDs to holiday entries. Returns: dict[str,…, Single holiday definition loaded from data/<env>/calendar/holidays.json., Unit tests for calendar schemas. Tests the Pydantic models in calendar.py…, Test HolidayCollection.id_map property., Test HolidayCollection.ensure_unique_ids() detects duplicates., Test HolidayEntry can be instantiated., Test HolidayEntry validates tradition. (+10 more)

### Community 494 - "containers.sql"
Cohesion: 0.13
Nodes (5): container_contents, schema_name.add_item_to_container(), schema_name.get_container_contents_json(), item_instances, item_prototypes

### Community 495 - "e2e-bootstrap.ts"
Cohesion: 0.15
Nodes (27): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+19 more)

### Community 496 - "Chaosium CoC Catalog"
Cohesion: 0.14
Nodes (14): Chaosium CoC Catalog, Creature / motif families (adaptation stubs), How to use, MythosMUD adaptation notes, Ongoing ops, Tier A (full or batch-promoted), Tier B (source-only), Tier C (+6 more)

### Community 497 - "mythos_dev.players"
Cohesion: 0.13
Nodes (16): mythos_dev.lucidity_adjustment_log, mythos_dev.lucidity_cooldowns, mythos_dev.lucidity_exposure_state, mythos_dev.player_channel_preferences, mythos_dev.player_effects, mythos_dev.player_inventories, mythos_dev.player_lucidity, mythos_dev.player_skills (+8 more)

### Community 498 - "Phase 1: Core Separation"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 1: Core Separation, Sub-tasks, Sub-tasks (+8 more)

### Community 499 - "test_magic_healing_events.py"
Cohesion: 0.09
Nodes (31): MagicServiceHealingMixin, Any, UUID, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or…, True if effect result indicates healing was applied (success, effect_applied,… (+23 more)

### Community 500 - "CommandRateLimiter"
Cohesion: 0.11
Nodes (21): CommandRateLimiter, Any, datetime, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate…, Remove timestamp data for players who haven't been active recently. Prevents… (+13 more)

### Community 501 - "test_event_publisher.py"
Cohesion: 0.10
Nodes (19): Unit tests for event publisher. Tests the EventPublisher class., Test get_next_sequence_number() returns and increments sequence., Test reset_sequence_number() resets sequence to 0., Test EventPublisher initialization without subject manager., Test EventPublisher initialization with initial sequence., Same persistence name resolution path for player_left., #679: async_persistence is injected at construction (no container lookup at all…, Test EventPublisher initialization. (+11 more)

### Community 502 - "Phase 2: Enhanced Features"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 2: Enhanced Features, Sub-tasks, Sub-tasks (+8 more)

### Community 503 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 504 - "Async Audit Executive Summary"
Cohesion: 0.06
Nodes (33): Alternative Approaches Considered, Async Audit Executive Summary, Benefit, Break-Even, Contact, Cost, Cost-Benefit Analysis, Critical Findings (+25 more)

### Community 505 - "TEMPORAL_SYSTEM_RESEARCH.md"
Cohesion: 0.07
Nodes (30): The Call of Cthulhu, Canonical and Derived Observances, Implementation Notes, Mythos Holiday Candidates, Narrative Flavor Seeds, Opportunities for Expansion, 1. Research Synthesis, 2. Mythos Time Model Draft (+22 more)

### Community 506 - "test_room_write_procedures.py"
Cohesion: 0.15
Nodes (30): async_sessionmaker, asyncio, AsyncSession, fixture, integration, Integration tests for the room-editor write procedures…, update_room_properties() with p_set_environment=TRUE and NULL clears the…, p_set_environment=FALSE leaves attributes.environment untouched, regardless of… (+22 more)

### Community 507 - "Prometheus Configuration"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 508 - "load_world_seed.py"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 509 - "validate.py"
Cohesion: 0.09
Nodes (33): demo(), BugBlock, check_bug_content(), _check_bugs(), check_loose_tags(), check_relative_links(), _check_required_structure(), _exit_code_for_errors() (+25 more)

### Community 510 - "ReactNodeUpgradeAnalyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 511 - "game_tick_death.py"
Cohesion: 0.13
Nodes (29): _handle_player_death_threshold(), _player_in_active_combat(), _process_dead_players(), process_dp_decay_and_death(), _process_mortally_wounded_player(), _process_mortally_wounded_players(), _process_mp_regeneration(), _process_passive_lucidity_flux() (+21 more)

### Community 512 - ".validate_current_vs_max_stats"
Cohesion: 0.11
Nodes (11): computed_field, Any, model_validator, Initialize Stats with provided data. For random stat generation, use…, Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes…, Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).…, Calculate max lucidity based on education. AI: This computed field uses the…, Calculate max determination points (DP) using formula: (CON + SIZ) / 5. AI:… (+3 more)

### Community 513 - "run_flee_effect"
Cohesion: 0.15
Nodes (28): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+20 more)

### Community 514 - "NPCCommunicationIntegration"
Cohesion: 0.10
Nodes (23): NPCCommunicationIntegration, Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…, Process a message to determine if the NPC should respond. Args: npc_id: ID of…, Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…, Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…, Integrates NPCs with the existing chat and whisper systems. This class provides…, Initialize the NPC communication integration. Args: event_bus: Optional…, Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the… (+15 more)

### Community 515 - "game_tick_protocols.py"
Cohesion: 0.11
Nodes (15): _app_container(), AsyncSession, FastAPI, Player, Protocol, UUID, Protocol stubs and container access for game tick processing., Return the DI container from app.state, or None if missing. (+7 more)

### Community 516 - "UserManagerProtocol"
Cohesion: 0.08
Nodes (11): Protocol for user manager., Mute a channel for a player., Unmute a channel for a player., Check if channel is muted., Mute a player for another player., Unmute a player for another player., Check if player is muted., Check if player is globally muted. (+3 more)

### Community 517 - "test_combat_validator.py"
Cohesion: 0.02
Nodes (96): combat_validator(), fixture, Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_combat_command with target name too long., Test validate_combat_command when rate limited., Test validate_combat_command handles exceptions gracefully., Test validate_target_exists with exact match., Test validate_target_exists with case-insensitive match. (+88 more)

### Community 518 - "real_time.py"
Cohesion: 0.12
Nodes (32): _invoke_handle_websocket_connection(), _parse_websocket_token(), Any, UUID, WebSocket, Real-time communication API endpoints for MythosMUD server. This module handles…, Parse token from WebSocket subprotocol (preferred) or query params (fallback).…, Return True only when anonymous player_id query fallback is explicitly enabled.… (+24 more)

### Community 519 - "test_optimized_security_validator.py"
Cohesion: 0.08
Nodes (35): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test benchmark function runs without errors., Test validating message with path traversal pattern., Test validating message with javascript: URL. (+27 more)

### Community 520 - "MinimapRenderer"
Cohesion: 0.09
Nodes (17): MinimapRenderer, Any, Mini-map renderer for room connectivity visualization. This module provides…, Renders room connectivity graphs in various visual formats. Implements the…, Extract street acronym from room ID. Args: room_id: Full room ID (e.g.,…, Extract street name from room ID. Args: room_id: Full room ID Returns: Street…, Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…, Render the mini-map as ASCII art with grid-based visualization. Args:… (+9 more)

### Community 521 - "scripts"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 522 - "map/types.ts"
Cohesion: 0.10
Nodes (32): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeBody(), ExitEdgeLabels() (+24 more)

### Community 523 - "type"
Cohesion: 0.13
Nodes (16): items, type, items, type, uniqueItems, minLength, type, effect_components (+8 more)

### Community 524 - "P8 · Applied"
Cohesion: 0.20
Nodes (9): Code changes — comment-only, explicitly authorised, Documentation changes — 33 files, Issues created — 14, Issues reopened — 12, New ADRs, Not done — deliberately, P8 · Applied, Security — filed privately, not publicly (+1 more)

### Community 525 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, minLength, type, type, minLength, type, properties (+10 more)

### Community 526 - "NATS Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (30): NATS Code Review, 10. **Inconsistent Error Handling**, 11. **Missing Input Validation**, 1. **Blocking Operations in Message Handlers** (Anti-pattern violation), 1. **Excellent Error Boundary Implementation**, 2. **Good Connection State Management**, 2. **Missing Message Acknowledgment** (Anti-pattern violation), 3. **Connection Pool Not Used by Default** (Inefficiency) (+22 more)

### Community 527 - "WebSocket Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (29): 10. **No Message Batching**, 11. **Missing Rate Limiting on WebSocket Messages**, 12. **Insufficient Authentication Validation**, 1. **Dependency Injection Pattern**, 1. **Event Loop Anti-Pattern in Connection Manager**, 2. **Missing Input Validation on Server Side**, 2. **Modern Async Patterns**, 3. **Error Boundaries** (+21 more)

### Community 528 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 529 - "test_admin_commands_helpers.py"
Cohesion: 0.09
Nodes (29): create_teleport_effect_message(), Create teleport effect message for visual display. Args: player_name: Name of…, asyncio, Unit tests for admin_commands helper functions. Tests helper functions in…, Test DIRECTION_OPPOSITES dictionary contains correct mappings., Test create_teleport_effect_message() for teleport departure., Test create_teleport_effect_message() for teleport departure with direction., Test create_teleport_effect_message() for teleport arrival. (+21 more)

### Community 530 - "test_container_helpers_inventory_display.py"
Cohesion: 0.12
Nodes (28): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+20 more)

### Community 531 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test get_players_batch() handles player not found., Test send_initial_game_state() sends initial state., Test convert_room_uuids_to_names() with empty room_data., Test convert_room_uuids_to_names() when player not found., Test _process_occupants_with_grace_periods() splits players and NPCs., Test _get_player_data_for_client() uses PlayerService when available., Test get_player() retrieves player from persistence. (+11 more)

### Community 532 - "EventBusLifecycleMixin"
Cohesion: 0.10
Nodes (17): EventBusLifecycleMixin, Exception, Task, Cancel leftover tasks after the grace wait, then give them a short drain., Cancel all active tasks and wait for graceful shutdown., Finalize shutdown by clearing tasks and logging., Stop pure async event processing gracefully., Unsubscribe every tracked service. No-op when none are registered. (+9 more)

### Community 533 - "CharacterCreationService"
Cohesion: 0.14
Nodes (12): CharacterCreationService, Any, UUID, Validate character stats against class prerequisites. Args: stats: The stats…, Create a new character with specific stats. Args: name: The character's name…, Get information about all available character classes and their prerequisites.…, Service class for character creation and stats generation business operations., Get a description for a character class. (+4 more)

### Community 534 - "ComprehensiveLoggingMiddleware"
Cohesion: 0.11
Nodes (22): ComprehensiveLoggingMiddleware, Any, ASGIApp, Exception, Receive, Request, Scope, Send (+14 more)

### Community 535 - ".create_combat_instance"
Cohesion: 0.07
Nodes (21): _build_participant(), _compute_turn_order(), UUID, Build CombatParticipant from CombatParticipantData., Return participant IDs sorted by dexterity (highest first)., Create and initialize a combat instance., Start a new combat instance between two participants., fixture (+13 more)

### Community 536 - "test_room_occupant_manager.py"
Cohesion: 0.09
Nodes (29): mock_connection_manager(), occupant_manager(), asyncio, fixture, Unit tests for room occupant manager. Tests the RoomOccupantManager class for…, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test get_room_occupants handles get_players error. (+21 more)

### Community 537 - "test_lint_container_get_instance.py"
Cohesion: 0.10
Nodes (26): _LintContainerGetInstanceModule, _load_script(), Protocol, Unit tests for scripts/lint_container_get_instance.py. Verifies the detection…, A file with more get_instance() calls than its allowlist entry expects fails --…, A file with fewer get_instance() calls than its allowlist entry expects fails…, An allowlist entry for a file with zero remaining hits (fully migrated) must…, A blank line inserted above the allowlisted site must not trip a violation --… (+18 more)

### Community 538 - "InviteManager"
Cohesion: 0.15
Nodes (24): InviteManager, Remove expired invites and return count of removed invites., Manages invite creation, validation, and tracking. Handles the invite-only…, mock_session(), asyncio, fixture, Unit tests for InviteManager (server.auth.invites)., use_invite reserves, captures, commits, then re-fetches the row (3 execute()… (+16 more)

### Community 539 - "Async Remediation Final Report"
Cohesion: 0.07
Nodes (29): 48 Sync Persistence Call Instances, Async Remediation Final Report, All async anti-patterns have been exorcised from the codebase, All Targets Met, API/Commands (2 files), Checklist, ✅ COMPLETE - ALL 48 INSTANCES MIGRATED, Core Infrastructure (2 files) (+21 more)

### Community 540 - "🔴 CRITICAL ISSUES"
Cohesion: 0.07
Nodes (28): 10. Use of `BETWEEN` with Integer Ranges, 11. Missing Indexes on Foreign Keys, 12. Inconsistent Constraint Naming, 13. Mixed Case in Table/Column Names, 14. Missing `UNIQUE` Constraints Where Appropriate, 15. Inconsistent Use of `NOT NULL` Constraints, 16. Missing Documentation for Complex Constraints, 1. Use of `serial`/`SERIAL` Instead of `bigint generated always as identity` (+20 more)

### Community 541 - "Test Suite Quality Audit - Executive Summary"
Cohesion: 0.07
Nodes (29): **25-30% (~1,250-1,500 tests) provide CRITICAL regression protection**, Answer to Original Question, Breakdown, By Category, CI/CD Time Saved, Commit to full 2-month optimization plan, Comparison to Industry Benchmarks, Created Documents (+21 more)

### Community 542 - "send_welcome_event"
Cohesion: 0.12
Nodes (15): AsyncPersistenceRoomLookup, cleanup_websocket_connection(), PlayerDisconnectService, PlayerMuteCleanup, Protocol, UUID, WebSocket, Send welcome event to the client. Returns: True if successful, False if… (+7 more)

### Community 543 - "test_inventory_command_prototype.py"
Cohesion: 0.12
Nodes (26): _first_normalized_wear_slot(), infer_equip_slot_from_prototype(), _inventory_prototype_id(), prototype_from_registry(), prototype_registry_from_request(), Prototype registry access and equip-slot inference for inventory items., Resolve prototype registry from FastAPI-style request (agent-readable…, Return the prototype object for ``prototype_id``, or None if missing or invalid. (+18 more)

### Community 544 - "AsciiMapRenderer"
Cohesion: 0.15
Nodes (11): AsciiMapRenderer, Renders ASCII maps from room coordinate data. Supports multiple map styles…, Initialize the ASCII map renderer., Tests for _vertical_exit_char_between (|, v, ^)., Bidirectional vertical exit renders as a vertical bar., One-way south exit renders as a lowercase 'v'., One-way north exit renders as a caret., When there are no vertical exits, the helper returns None. (+3 more)

### Community 545 - "test_lifecycle_respawn.py"
Cohesion: 0.18
Nodes (26): Process the respawn queue and spawn NPCs that are ready (delegates to…, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…, Process the respawn queue and spawn NPCs that are ready. Args: manager:… (+18 more)

### Community 546 - "MagicServiceCompletionMixin"
Cohesion: 0.19
Nodes (15): _is_heal_other_target(), MagicServiceCompletionMixin, Any, UUID, Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…, Parse target_id from casting state. Returns None if missing or invalid., Apply costs and queue spell for next combat round. Returns True if queued,…, Apply spell costs/effects, send completion message and healing event. (+7 more)

### Community 547 - "NPCStartupService"
Cohesion: 0.15
Nodes (14): _merge_phase_into_startup(), _new_spawn_results(), NPCStartupService, Any, NPC Startup Service for MythosMUD. This module provides automatic NPC spawning…, Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…, Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…, Second pass: spawn one instance per definition (that was spawned in… (+6 more)

### Community 548 - "GameConfig"
Cohesion: 0.12
Nodes (14): GameConfig, BaseSettings, field_validator, Game-specific configuration., Validate combat alert threshold., Validate combat performance threshold., Validate combat error threshold., Validate max connections is reasonable. (+6 more)

### Community 549 - "TestLogoutCommand"
Cohesion: 0.11
Nodes (17): Any, asyncio, fixture, Unit tests for the logout command handler., Test logout command when persistence is not available., Test logout command when persistence operations fail., Test cases for the logout command handler., Test logout command when connection cleanup fails. (+9 more)

### Community 550 - "test_chat_moderation.py"
Cohesion: 0.11
Nodes (20): moderation(), player_service(), asyncio, fixture, Unit tests for chat moderation operations., test_add_admin_returns_true(), test_get_mute_status_handles_internal_error(), test_get_mute_status_includes_player_name() (+12 more)

### Community 551 - "._handle_exception"
Cohesion: 0.16
Nodes (13): Exception, Receive, Request, Response, Scope, Send, ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…, Handle an exception and send a standardized error response. Args: scope: ASGI… (+5 more)

### Community 552 - "Bug Investigator Subagent"
Cohesion: 0.07
Nodes (27): Authentication/Login Issues, Best Practices, Bug Investigator Subagent, Capabilities, Chat/Communication Issues, Critical Requirements, Evidence Collection, Evidence Standards (+19 more)

### Community 553 - "EdgeDetailsPanel.tsx"
Cohesion: 0.11
Nodes (15): buildEdgeFieldModel(), EdgeAdminActionsProps, EdgeDeleteConfirmProps, EdgeDetailRow(), EdgeDetailRowProps, EdgeDetailsFields(), EdgeDetailsFieldsProps, EdgeDetailsPanel() (+7 more)

### Community 554 - "playerHandlers.ts"
Cohesion: 0.14
Nodes (23): handlePlayerDeliriumRespawned(), handlePlayerDied(), handlePlayerDpUpdated(), handlePlayerEntered(), handlePlayerEnteredGame(), handlePlayerLeft(), handlePlayerLeftGame(), handlePlayerRespawned() (+15 more)

### Community 555 - "Domain Model Anemic Anti-Pattern Audit"
Cohesion: 0.07
Nodes (27): 1. Already Addressed (Prior Work), 2.1 Player Death Service – DP Decay, 2.2 Combat Turn Processor – “Can Act” Checks, 2.3 Combat HP Sync – Death Threshold Logic, 2.4 Combat Persistence Handler – Same Patterns, 2.5 Player Respawn Service – Stats Restoration, 2. High Priority – Domain Logic in Services, 3.1 Wearable Container Service – Capacity Checks (+19 more)

### Community 556 - "ErrorMonitor"
Cohesion: 0.13
Nodes (17): ErrorMonitor, main(), Any, datetime, Path, Detect error trends over time. Returns trend analysis results., Check for alert conditions. Returns list of active alerts., Monitor errors continuously for a specified duration. Args: log_dir: Directory… (+9 more)

### Community 557 - "verify_linting_parity.py"
Cohesion: 0.15
Nodes (27): check_alignment(), _check_pylint_suppressions(), _check_ruff_suppressions(), find_suppressions(), _has_pylint_equivalent(), _has_ruff_equivalent(), main(), parse_pylint_suppression() (+19 more)

### Community 558 - "players.sql"
Cohesion: 0.12
Nodes (4): schema_name.get_user_id_by_username_ci(), schema_name.reserve_invite(), users, invites

### Community 559 - "CircuitBreaker"
Cohesion: 0.12
Nodes (15): CircuitBreaker, timedelta, Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…, Circuit breaker for NATS message processing. Implements Martin Fowler's circuit…, Initialize circuit breaker. Args: failure_threshold: Number of failures before…, Test _on_success() resets failure count in CLOSED state., Test _should_attempt_reset() returns True after timeout., Test _transition_to() updates state. (+7 more)

### Community 560 - "validate_secure_path"
Cohesion: 0.08
Nodes (24): Validate and sanitize a user-provided path to prevent path traversal attacks.…, validate_secure_path(), Test validate_secure_path detects when common_path != base_path (lines 59-66)., Test validate_secure_path with valid path., Test validate_secure_path handles different drives on Windows., Test validate_secure_path rejects path traversal with .., Test validate_secure_path rejects path traversal with ~, Test validate_secure_path with nested valid path. (+16 more)

### Community 561 - "test_logging_processors.py"
Cohesion: 0.04
Nodes (80): EventDict, configure_enhanced_structlog(), Configure enhanced Structlog with MDC, security, and performance features.…, add_correlation_id(), add_request_context(), _database_error_type(), _enhance_one_player_id(), enhance_player_ids() (+72 more)

### Community 562 - "test_lru_cache.py"
Cohesion: 0.07
Nodes (27): cache_with_ttl(), cache_without_ttl(), asyncio, fixture, Unit tests for LRU cache expiration and eviction. Tests the LRUCache class,…, Test that expired entry count is tracked in cache stats., Test that expiration rate is calculated in stats., Test that cache size stays within bounds after expiration cleanup. (+19 more)

### Community 563 - "test_quest_service_collect.py"
Cohesion: 0.13
Nodes (27): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in… (+19 more)

### Community 564 - "test_combat_death_handler.py"
Cohesion: 0.13
Nodes (22): combat(), combat_service(), handler(), npc_target(), player_target(), asyncio, fixture, patch (+14 more)

### Community 565 - "Argon2 Password Hashing Best Practices"
Cohesion: 0.07
Nodes (26): 1.1. Directory Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+18 more)

### Community 566 - "Pre-commit Hooks Best Practices"
Cohesion: 0.07
Nodes (26): 1.1. Configuration Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+18 more)

### Community 567 - "debugLogger"
Cohesion: 0.13
Nodes (5): debugLogger, LogConfig, LogEntry, LogLevel, mockConsole

### Community 568 - "Communities (19 total, 4 thin omitted)"
Cohesion: 0.07
Nodes (26): Ambiguous Edges - Review These, Communities (19 total, 4 thin omitted), Community 0 - "Yog-Sothoth Keeper Decks", Community 10 - "Tsathoggua Formless Spawn", Community 11 - "Ygolonac and Xiclotl", Community 12 - "Nyogtha Spawn", Community 13 - "Hastur Spawn", Community 14 - "Fthagghua Fire Vampires" (+18 more)

### Community 569 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 570 - "Persistence Layer Refactoring - COMPLETE ✅"
Cohesion: 0.07
Nodes (27): Backward Compatibility, 📈 Benefits, Code Created, 🎉 Conclusion, Directory Structure, Documentation Created, 📚 Documentation Index, 📊 Final Metrics (+19 more)

### Community 571 - "enum"
Cohesion: 0.29
Nodes (7): city, countryside, desert, mountains, swamp, tundra, enum

### Community 572 - "LogAnalyzer"
Cohesion: 0.12
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time. Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 573 - "test_look_item.py"
Cohesion: 0.02
Nodes (149): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _find_item_in_inventory(), _find_item_in_room_drops(), _get_item_description_from_prototype(), _handle_item_look(), Any (+141 more)

### Community 574 - "test_chat_pose_helpers.py"
Cohesion: 0.16
Nodes (25): clear_player_pose(), get_player_pose(), get_room_poses(), normalize_player_id(), Any, UUID, Pose management helpers for chat service., Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose… (+17 more)

### Community 575 - "MetricsCollector"
Cohesion: 0.09
Nodes (17): MetricsCollector, Any, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or…, Simple metrics collector for NATS message delivery. Thread-safe metrics…, Get concise metrics summary. Returns: High-level metrics summary AI: For quick… (+9 more)

### Community 576 - "test_npc_threading_messages.py"
Cohesion: 0.05
Nodes (35): NPCMessageQueue, Thread-safe message queue for NPC actions. This queue handles pending actions…, Initialize the NPC message queue. Args: max_messages_per_npc: Maximum number of…, Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…, Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…, Clear all pending messages for an NPC. Args: npc_id: The NPC's ID Returns:…, Get the number of pending messages for an NPC., Get the total number of pending messages across all NPCs. (+27 more)

### Community 577 - "attach_compatibility_properties"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 578 - "rooms.sql"
Cohesion: 0.15
Nodes (4): schema_name.create_room_link(), schema_name.delete_room_link(), schema_name.update_room_link(), rooms

### Community 579 - "extract_player_name"
Cohesion: 0.13
Nodes (25): extract_player_name(), _get_name_from_user(), get_player_position(), _is_uuid_string(), _is_valid_name(), Any, Player, UUID (+17 more)

### Community 580 - "test_rate_limiter.py"
Cohesion: 0.03
Nodes (78): Any, RateLimiter, Remove timestamps older than the window size. Args: player_id: Player ID…, Check if a player is within rate limits for a channel. Args: player_id: Player…, Record a message for rate limiting. Args: player_id: Player ID channel: Channel…, Sliding window rate limiter for chat channels. Implements per-user, per-channel…, Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…, Reset rate limiting for a player. Args: player_id: Player ID channel: Specific… (+70 more)

### Community 581 - "format_room_posture_message"
Cohesion: 0.16
Nodes (16): format_room_posture_message(), Create a descriptive room message for posture changes., Unit tests for position command helper functions. Tests helper functions in…, Test _format_room_posture_message() formats sitting message., Test _format_room_posture_message() formats lying message., Test _format_room_posture_message() formats standing from lying message., Test _format_room_posture_message() formats standing from sitting message., Test _format_room_posture_message() formats standing with no previous position. (+8 more)

### Community 582 - "test_movement_monitor.py"
Cohesion: 0.04
Nodes (56): movement_monitor(), fixture, Unit tests for movement monitor. Tests the MovementMonitor class for monitoring…, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data., Test validate_room_integrity() detects duplicate players., Test validate_room_integrity() handles empty rooms dict. (+48 more)

### Community 583 - "test_room_service.py"
Cohesion: 0.08
Nodes (23): Unit tests for room service. Tests the RoomService class for room-related…, Test get_room_by_name() returns None (not implemented)., Test list_rooms_in_zone() returns empty list (not implemented)., Test update_environment_state() updates environment state., Test get_environment_state() returns current environment state., Test describe_lighting() returns description for day., Test describe_lighting() returns description for night., Test describe_lighting() returns default for unknown daypart. (+15 more)

### Community 584 - "Path"
Cohesion: 0.10
Nodes (14): Path, Fix self-references by adding proper flags. Args: room_database: Complete room…, Find the file for a room. Returns None if file doesn't exist., Create backup if requested., Fix missing exits field. Returns True if fixed., Fix missing optional fields. Returns True if any fixed., Initialize the room fixer. Args: base_path: Base directory for room files, Fix missing fields based on errors. Returns True if any fixed. (+6 more)

### Community 585 - "PostgreSQL Best Practices"
Cohesion: 0.08
Nodes (25): 1.1. Naming Conventions, 1.2. Formatting, 1.3. Comments, 1. Code Organization and Structure, 2.1. Explicit JOINs, 2.2. Common Table Expressions (CTEs), 2.3. Avoid `NOT IN`, 2. Common Patterns and Anti-patterns (+17 more)

### Community 586 - "Structured Logging with Structlog Best Practices"
Cohesion: 0.08
Nodes (26): 1.1. Directory Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+18 more)

### Community 587 - "Uvicorn ASGI Server Best Practices"
Cohesion: 0.08
Nodes (25): 1.1. Directory Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+17 more)

### Community 588 - "multiplayer-colocated.ts"
Cohesion: 0.11
Nodes (26): forceLogoutPlayer(), assertNoRestDisconnectPollution(), executeCommandTrusted(), logoutPlayer(), Window, captureOccupantsSnapshot(), capturePresenceEvents(), EnsureMultiplayerCoLocatedOptions (+18 more)

### Community 589 - "Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.08
Nodes (26): 1. Deprecated `asyncio.get_event_loop()` Usage, 1. Proper Connection Pool Management, 2. Good Error Handling Patterns, 2. SQL Injection Risk in Field Name Construction, 3. Async/Await Usage, 3. Connection Pool Cleanup Verification, 4. Blocking Operations in Async Context, 4. Security Considerations (+18 more)

### Community 590 - "test_load_world_seed.py"
Cohesion: 0.12
Nodes (25): regression, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, CaptureFixture, fixture, MonkeyPatch, Protocol (+17 more)

### Community 591 - "test_emote_repository.py"
Cohesion: 0.13
Nodes (19): EmoteRepository, Any, Emote repository for async persistence operations. This module provides async…, Repository for predefined emote and emote-alias persistence operations., Initialize the emote repository., Get all predefined emotes from the database. Returns: list[dict]: Rows with…, Get all emote aliases joined to their owning emote's stable_id. Returns:…, _alias_row() (+11 more)

### Community 592 - "PrototypeRegistry"
Cohesion: 0.15
Nodes (20): PrototypeRegistry, Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, In-memory registry for validated item prototypes., Load prototypes from a directory of JSON files., _make_prototype() (+12 more)

### Community 593 - "schemas/unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 594 - "connection_cleanup_methods.py"
Cohesion: 0.07
Nodes (39): check_and_cleanup_impl(), cleanup_dead_connections_impl(), cleanup_ghost_players_impl(), cleanup_orphaned_data_impl(), force_cleanup_impl(), prune_stale_players_impl(), Any, UUID (+31 more)

### Community 595 - ".claude/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 596 - "Vitest Best Practices"
Cohesion: 0.08
Nodes (22): Vite Configuration, 1. Code Organization & Naming, 2. Test Structure & Isolation, 3. Asynchronous Testing with `vi.waitFor`, 4. Mocking Strategies, 5. DOM Environment & Component Testing, 6. Performance & Concurrent Tests, 7. Code Coverage (+14 more)

### Community 597 - "dependencies"
Cohesion: 0.09
Nodes (23): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-rnd, react-router-dom (+15 more)

### Community 598 - "messageHandlers.ts"
Cohesion: 0.08
Nodes (30): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+22 more)

### Community 599 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 600 - ".cursor/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 601 - "Migration Strategy"
Cohesion: 0.08
Nodes (24): Access Patterns, App.State to Dependency Injection Migration Plan, Current State Analysis, Dependencies, Dependency Injection Pattern, Estimated Effort, Implementation Guidelines, Migration Strategy (+16 more)

### Community 602 - "ADR-012: python-statemachine for Backend Connection FSM"
Cohesion: 0.08
Nodes (24): ADR-011: XState for Frontend Connection State Machine, 10. Related ADRs, 11. Changelog, 1. Overview, 2. Context and Problem Statement, 3. Decision Drivers, 4. Considered Options, 5. Decision Outcome (+16 more)

### Community 603 - "Async Facades Implementation - COMPLETE ✅"
Cohesion: 0.08
Nodes (25): (A) and (B) Relationship: **Complementary**, (A) AsyncPersistenceLayer Integration ✅, Async Facades Implementation - COMPLETE ✅, Async Tests, (B) Sync Shim - NOT NEEDED ⏭️, Benefits Achieved, Both facades are now operational, Conclusion (+17 more)

### Community 604 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 605 - "Migration 019: Complete Implementation Summary"
Cohesion: 0.08
Nodes (25): 1. Database Schema Updates ✅, 2. Python Model Updates ✅, 3. Migration Script Created ✅, 4. Testing Infrastructure ✅, Before Production, Conclusion, Created Files (5), Documentation Files (4) (+17 more)

### Community 606 - "Persistence Layer Async Migration Plan"
Cohesion: 0.08
Nodes (25): Aggressive Timeline (Focused Migration), Conclusion, Conservative Timeline (Gradual Migration), Decision Points, Emergency Rollback, Individual File Rollback, Metrics to Track, Migration Timeline (+17 more)

### Community 607 - "Phase 4: Recommendations"
Cohesion: 0.08
Nodes (25): 1. Prune Infrastructure Tests (Save ~3 minutes, Remove ~350 tests), 2. Consolidate Coverage Tests (Save ~1 minute, Reduce ~60 tests), 3. Parametrize Repetitive Tests (Save ~1 minute, Reduce ~300 tests), 4.1 Pruning Candidates (750 tests, ~5 minutes savings), 4.2 Consolidation Opportunities, 4.3 Coverage Gap Identification, 4.4 Optimization Recommendations, 4. Migrate Model Tests to Property-Based Testing (+17 more)

### Community 608 - "enum"
Cohesion: 0.20
Nodes (10): artifact, consumable, container, currency, equipment, quest, enum, type (+2 more)

### Community 609 - "fix_fstring_logging.py"
Cohesion: 0.12
Nodes (24): _build_structured_params(), _clean_message(), _create_replacement_for_fstring(), create_structured_log_message(), extract_variables_from_fstring(), fix_fstring_logging_in_file(), _handle_no_variables_case(), main() (+16 more)

### Community 610 - "TestRunner"
Cohesion: 0.11
Nodes (14): main(), Path, Verify test database configuration. Note: For PostgreSQL databases, schema is…, Build the pytest command with proper configuration. Args: test_paths: List of…, # NOTE: Test runner uses minimal structlog configuration for console output, Run the test suite with proper configuration. Args: test_paths: List of test…, Run integration tests only., Run all tests (unit, integration, but not E2E by default). (+6 more)

### Community 611 - "test_room_subscription_manager_npcs.py"
Cohesion: 0.09
Nodes (23): asyncio, fixture, Unit tests for room subscription manager NPC helpers. Tests NPC-related helpers…, Test get_room_occupants() includes NPCs from lifecycle manager., Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager…, Create a RoomSubscriptionManager instance., Test _get_npc_name_from_lifecycle_manager gets NPC name., Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found. (+15 more)

### Community 612 - "handle_emote_command"
Cohesion: 0.13
Nodes (24): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+16 more)

### Community 613 - "test_behavior_engine.py"
Cohesion: 0.07
Nodes (27): Unit tests for behavior engine. Tests the BehaviorEngine class., Test _evaluate_equality() handles boolean true., Test _evaluate_equality() handles boolean false., Test _evaluate_numeric_comparison() handles > operator., Test _evaluate_numeric_comparison() handles < operator., Test _evaluate_numeric_comparison() returns None for invalid format., Test evaluate_condition() handles >= operator., Test execute_applicable_rules() handles exceptions. (+19 more)

### Community 614 - "._get_room_uuid_by_stable_id"
Cohesion: 0.17
Nodes (10): Any, AsyncSession, UUID, Get room UUID by stable_id (hierarchical room ID). Args: stable_id:…, Mark room as explored using the provided session. Backed by…, Get list of room IDs that a player has explored. Args: player_id: UUID of the…, Check if a player has explored a specific room. Args: player_id: UUID of the…, Synchronous wrapper for mark_room_as_explored. This method is designed to be… (+2 more)

### Community 615 - ".disconnect"
Cohesion: 0.12
Nodes (9): Drain in-flight messages from all subscriptions., Close and unsubscribe from all subscriptions., Verify all subscriptions were cleaned up and log warnings if any remain., Close NATS connection and transition to disconnected state., Disconnect from NATS with graceful shutdown and message draining. AI: State…, Cancel all tracked background tasks for proper cleanup. AnyIO Pattern:…, Stop health check monitoring task., Get list of all active NATS subscription subjects. Returns: List of subject… (+1 more)

### Community 616 - "spell_repository.py"
Cohesion: 0.15
Nodes (17): Any, Spell repository for async persistence operations. This module provides async…, Get a spell by ID. Args: spell_id: Spell ID Returns: dict | None: Spell…, Map procedure result row to spell dict., Get all spells from the database. Returns: list[dict]: List of all spell…, _row_to_spell_dict(), _mock_session(), asyncio (+9 more)

### Community 617 - "npc_combat_grace.py"
Cohesion: 0.17
Nodes (17): get_app_instance(), Return the runtime app instance attached during lifespan startup. This provides…, _connection_manager_from_config_app(), is_npc_attack_on_player_blocked_by_login_grace_period(), is_player_attack_blocked_by_login_grace_period(), ConnectionManager, UUID, Login grace-period checks for NPC combat integration (extracted to keep service… (+9 more)

### Community 618 - "Any"
Cohesion: 0.13
Nodes (9): Any, Process room update with comprehensive validation. Args: room_data: Room data…, Invalidate stale room cache entry. Args: room_id: Room ID to invalidate…, Fetch fresh room data from room service. Args: room_id: Room ID to fetch…, Handle stale room data by requesting fresh data. Args: room_data: Stale room…, Process room transition with proper ordering and validation. Args:…, Get statistics about the room data cache. Returns: Dict[str, Any]: Cache…, Initialize the room synchronization service. Args: room_service: Optional… (+1 more)

### Community 619 - "send_system_message"
Cohesion: 0.18
Nodes (15): Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler system message functions. Tests the system…, Create a mock WebSocket., Test send_system_message() successfully sends message. (+7 more)

### Community 620 - "test_lint_optional_auth_no_guard.py"
Cohesion: 0.17
Nodes (20): _LintOptionalAuthModule, _load_script(), Path, Protocol, Unit tests for scripts/lint_optional_auth_no_guard.py. Verifies the detection…, Mirrors rooms.py's real shape: handler -> helper -> helper ->…, A route was fixed but the allowlist count wasn't lowered -- must fail, not pass…, Typed surface of the loaded script, for the parts these tests exercise. (+12 more)

### Community 621 - "ApplicationContainer Structure Analysis and Domain-Specific Split Proposal"
Cohesion: 0.09
Nodes (21): 1. Executive Summary, 2.1 Attribute Inventory by Domain, 2.2 Initialization Order and Dependencies, 2.3 Private Initializers and Helpers, 2.4 Public API and Consumers, 2. Current Structure Analysis, 3.1 Option A: Internal Bundles (Recommended), 3.2 Option B: Composed Sub-Containers (Alternative) (+13 more)

### Community 622 - "SchemaValidator"
Cohesion: 0.10
Nodes (18): create_validator(), Any, Path, Shared schema validator for room definition files. This module provides JSON…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a serialized alias bundle against the alias schema. Args: alias_data:…, Validate emote definition data against the emote schema. Args: emote_data:… (+10 more)

### Community 623 - "get_cached_player"
Cohesion: 0.13
Nodes (23): Unit tests for player_cache utilities. Tests the player caching functions for…, Test get_cached_player() returns None when no cache exists., Test cache_player() and get_cached_player() operations., Test get_cached_player() returns None for nonexistent key., Test cache_player() can cache multiple players., Test cache_player() overwrites existing entries., Test get_cached_player() handles missing state., Test cache_player() handles missing state gracefully. (+15 more)

### Community 624 - "ValidationRule"
Cohesion: 0.09
Nodes (15): ABC, Base validation rule class. This module defines the abstract base class for all…, Create a validation error for this rule. Args: room_id: Room ID where error…, Represents a validation error with metadata. As documented in the restricted…, Create a validation warning for this rule. Args: room_id: Room ID where warning…, Get information about this rule. Returns: Dictionary with rule information, Initialize a validation error. Args: rule_name: Name of the rule that generated…, Convert error to dictionary format. (+7 more)

### Community 625 - "SQLAlchemyAsyncLinter"
Cohesion: 0.11
Nodes (18): Await, lint_directory(), lint_file(), main(), Call, Import, ImportFrom, Path (+10 more)

### Community 626 - "Test Suite Analyzer Subagent"
Cohesion: 0.08
Nodes (23): Best Practices, Capabilities, Coverage Analysis, Coverage Gap Analysis, Coverage Requirements, Critical Files Requiring High Coverage, Critical Path Coverage, Example Scenarios (+15 more)

### Community 627 - "React Best Practices"
Cohesion: 0.08
Nodes (23): 1. Core React Principles: Purity & Rules of Hooks, 2. Code Organization & Naming, 3. Component Design & Patterns, 4. State Management, 5. Performance & Optimization, 6. Common Pitfalls, 7. Accessibility (A11y) & Testing, ❌ BAD: Class components / Mixed concerns (+15 more)

### Community 628 - "Frontend Design Skill"
Cohesion: 0.13
Nodes (13): Frontend Design Skill, Context Gathering Protocol, Design Direction, Implementation Principles, The AI Slop Test, Normalize Skill, Clean Up, Execute (+5 more)

### Community 629 - "Onboard Skill"
Cohesion: 0.08
Nodes (24): Onboard Skill, Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption (+16 more)

### Community 630 - "stateNormalization.ts"
Cohesion: 0.11
Nodes (26): createInitialState(), createSessionActions(), SessionActions, SessionSelectors, SessionState, SessionStore, touchActivity(), useSessionStore (+18 more)

### Community 631 - "multiplayer-browser-helpers.bundle.js"
Cohesion: 0.16
Nodes (20): buttonHasLoginSubmitLabel(), coalesce(), computedStyleHidesElement(), elementTextIncludesGameInfo(), fieldHasCommandPlaceholder(), getBodyInnerText(), hasCommandInputInBrowser(), hasGameInfoAnyMessageInBrowser() (+12 more)

### Community 632 - "compilerOptions"
Cohesion: 0.13
Nodes (14): compilerOptions, allowImportingTsExtensions, composite, noEmit, rootDir, typeRoots, types, exclude (+6 more)

### Community 633 - "Communities (10 total, 2 thin omitted)"
Cohesion: 0.12
Nodes (17): Communities (10 total, 2 thin omitted), Community 0 - "Azotottal (fallen angel beyond the stars) / Captain Louis Malon", Community 1 - "Charenton (Paris district / asylum) / Christophe Pressi — Soldat (Soldier), age 20", Community 2 - "Dreamlands / Fenalik's Mansion (Poissy)", Community 3 - "Reign of Terror / Call of Cthulhu 7th Edition", Community 4 - "Bastille / James Coquillat", Community 5 - "Azathoth / Celine Bessette", Community 6 - "Christophe Pressi / Comte Benoit" (+9 more)

### Community 634 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 635 - "NATS Anti-Patterns and Best Practices Review"
Cohesion: 0.08
Nodes (24): 10. **Missing Connection Health Monitoring in Broker** (Observability), 1. **Synchronous Operations in Non-Handler Context** (Low Priority), 2. **Event Handler Callbacks May Block** (Anti-pattern), 3. **Inconsistent Error Handling Patterns** (Code Quality), 4. **Missing Input Validation in Some Methods** (Security/Reliability), 5. **Subject Naming: Potential for Too Broad Wildcards** (Anti-pattern), 6. **Connection Pool Error Handling** (Resilience), 7. **Message Acknowledgment: Manual Ack Not Default** (Reliability) (+16 more)

### Community 636 - "ContainerLockMixin"
Cohesion: 0.23
Nodes (10): ContainerLockMixin, Player, UUID, Lock a container (LOCKED or SEALED). Requires ownership or admin., Unlock a container. Requires access and unlock eligibility (key/admin)., Lock/unlock container state persistence., Load container for lock/unlock ops, or raise ContainerNotFoundError., Load player for lock/unlock ops, or raise ValidationError. (+2 more)

### Community 637 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 638 - "migrate_rooms.py"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 639 - "skills_commands.py"
Cohesion: 0.14
Nodes (22): _format_skills_output(), _get_container_services(), handle_skills_command(), Any, UUID, Skills command handler (plan 10.7 V4). Returns the active character's skills as…, Get container, persistence, and skill_service from request, or None if…, Extract and validate player_id from player object, returning UUID or None. (+14 more)

### Community 640 - "handle_teach_command"
Cohesion: 0.24
Nodes (17): handle_teach_command(), Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, asyncio, patch, Unit tests for teach command handlers. Tests the teach command functionality., Test handle_teach_command() teaches spell to player., Test handle_teach_command() handles missing target., Test handle_teach_command() handles missing persistence. (+9 more)

### Community 641 - "Player"
Cohesion: 0.02
Nodes (150): _convert_legacy_stats_string(), Player, listens_for, Initialize Player instance., String representation of the player., Get player stats as dictionary. Returns a MutableDict instance that…, Set player stats from dictionary. Accepts both plain dict and MutableDict…, Get player inventory as list. Handles both JSON string (from database) and list… (+142 more)

### Community 642 - "realtime/realtime.py"
Cohesion: 0.13
Nodes (23): Realtime domain schemas: realtime API, NATS messages, WebSocket messages., ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD. This module defines…, Presence statistics for connection monitoring. This model represents aggregate…, Session statistics for connection monitoring. This model represents aggregate…, Error statistics for connection monitoring. This model represents aggregate… (+15 more)

### Community 643 - "test_mp_regeneration_service.py"
Cohesion: 0.12
Nodes (15): Unit tests for MP regeneration service. Tests the MPRegenerationService class…, Test _get_regen_multiplier() returns 1.0 for standing position., Test _get_regen_multiplier() returns REST multiplier for sitting., Test _get_regen_multiplier() returns enhanced REST multiplier for lying., Test _get_regen_multiplier() defaults to 1.0 when position not specified., Test restore_mp_from_meditation() restores more MP than rest., Test restore_mp_from_item() returns error when player not found., Test restore_mp_from_item() restores MP. (+7 more)

### Community 644 - "_handle_admin_set_stat_command"
Cohesion: 0.07
Nodes (48): _handle_admin_set_stat_command(), Handle admin set <stat_name> <target_player> <value>., _assert_stat_write_path(), asyncio, patch, Unit tests for admin setstat context failures, logging, and notify posture.…, Test handling when player service is not available., Test handling when persistence layer is not available. (+40 more)

### Community 645 - "Lint Remediation"
Cohesion: 0.14
Nodes (12): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — code quality, Lint Remediation — Reference, 🟢 Medium — style, Entry point (+4 more)

### Community 646 - "mythos_dev.rooms"
Cohesion: 0.16
Nodes (14): mythos_dev.count_coordinated_rooms(), mythos_dev.create_room_link(), mythos_dev.delete_room_link(), mythos_dev.get_room_id_by_stable_id(), mythos_dev.is_room_explored(), mythos_dev.player_exploration, mythos_dev.room_links, mythos_dev.rooms (+6 more)

### Community 647 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 648 - "test_player_repository_room.py"
Cohesion: 0.20
Nodes (20): Any, Player, Player room validation helpers for PlayerRepository. Validates and fixes…, Return True if room validation should be skipped (cache empty, instanced, or…, Validate player's current room and fix if invalid. Args: room_cache: Shared…, Validate and fix player room, persisting the fix if needed. Args: room_cache:…, should_skip_room_validation(), validate_and_fix_player_room() (+12 more)

### Community 649 - "TestNPCCombatLifecycle"
Cohesion: 0.11
Nodes (14): asyncio, fixture, Unit tests for NPC combat lifecycle. Tests the NPCCombatLifecycle class for…, Test _despawn_npc handles NPC not in active_npcs., Test suite for NPCCombatLifecycle class., Create a mock persistence layer., Create a NPCCombatLifecycle instance for testing., Test NPCCombatLifecycle initialization. (+6 more)

### Community 650 - "test_command_factories_inventory_helpers.py"
Cohesion: 0.10
Nodes (20): Unit tests for inventory command factory helper functions. Tests the helper…, Test create_equip_command() with item name and inferred slot., Test create_unequip_command() with slot., Test create_unequip_command() with item name., Test create_inventory_command() creates InventoryCommand., Test create_inventory_command() raises error with args., Test create_pickup_command() raises error for invalid quantity., Test create_pickup_command() raises error for invalid index. (+12 more)

### Community 651 - "Color & Contrast"
Cohesion: 0.13
Nodes (15): Alpha Is A Design Smell, Building Functional Palettes, Color & Contrast, Color Spaces: Use OKLCH, Contrast & Accessibility, Dangerous Color Combinations, Dark Mode Is Not Inverted Light Mode, Never Use Pure Gray or Pure Black (+7 more)

### Community 652 - "MythosMUD Code Quality Targets for AI"
Cohesion: 0.09
Nodes (23): MythosMUD Code Quality AI Skill, `__all__` for public modules, As You Touch, Client return types (TypeScript), Complexity policy, Docstrings (D), High Priority, Medium Priority (+15 more)

### Community 653 - "MythosMUD Database Placement"
Cohesion: 0.09
Nodes (23): Database Placement Skill, Allowed Paths Only, Data Types, Forbidden, MythosMUD Database Placement, PostgreSQL Access (Procedures and Functions), Reference, When Adding or Moving Persistence (+15 more)

### Community 654 - "MUD Disconnect Grace Period & Rest Command: Industry Comparison"
Cohesion: 0.33
Nodes (5): 11. Missing Features from Other MUDs, Executive Summary, Features We're NOT Implementing (but exist elsewhere), MUD Disconnect Grace Period & Rest Command: Industry Comparison, Questions for Discussion

### Community 655 - "Code Review: Import Analysis and Anti-Patterns"
Cohesion: 0.07
Nodes (28): F-String Logging Anti-Pattern, Code Review Import Analysis, 1. **Import Inconsistency in `server/persistence.py`**, 2. **Import Organization Pattern**, Additional Findings, Best Practices Analysis, Code Review: Import Analysis and Anti-Patterns, Conclusion (+20 more)

### Community 656 - "ContainerRepository and ItemRepository: Review and Full Async Migration Plan"
Cohesion: 0.09
Nodes (23): 1.1 Current Architecture, 1.2 Impact of Current Wrappers, 1.3 Recommendation, 1. Review Summary, 2.1 Functions to Migrate, 2.2 Callers, 2. Scope of Migration, 3. Migration Options (+15 more)

### Community 657 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 658 - "Documentation Updates - ConnectionManager Refactoring"
Cohesion: 0.09
Nodes (23): 1. **Accurate Reference Material**, ✅ 1. `REAL_TIME_ARCHITECTURE.md`, ✅ 2. `CONNECTION_MANAGER_ARCHITECTURE.md` (NEW), 2. **Reduced Confusion**, 3. **Better Onboarding**, ✅ 3. `WEBSOCKET_CODE_REVIEW.md`, ✅ 4. `DEVELOPMENT_AI.md`, 4. **Historical Record** (+15 more)

### Community 659 - "Persistence Layer Refactoring Summary"
Cohesion: 0.09
Nodes (23): Backward Compatibility, Benefits Achieved, Code Organization, Conclusion, Conservative Approach, Created, Existing Code (Unchanged), Files Created/Modified (+15 more)

### Community 660 - "Phase 2 Async Persistence Migration - Status Update"
Cohesion: 0.10
Nodes (19): Room Cache 60s TTL, adjusts spectacles and awaits instruction, Awaiting Your Direction, Professor Wolfshade, ✅ Completed Today, Critical Phase 1 Fixes (100% Complete), 🚦 Current Status, 🎯 Decision Point, 📊 Effort Analysis (+11 more)

### Community 661 - "TEST_AUDIT_EXECUTIVE_SUMMARY.md"
Cohesion: 0.10
Nodes (17): ConnectionCleaner, ConnectionManager Facade, MessageBroadcaster, PerformanceTracker, 25-30 Percent Critical Tests, Option B Quick Wins First, ApplicationContainer Lifecycle Gap, Domain Layer Coverage Gap (+9 more)

### Community 662 - "compilerOptions"
Cohesion: 0.09
Nodes (22): compilerOptions, baseUrl, lib, module, moduleResolution, noEmit, noFallthroughCasesInSwitch, noUnusedLocals (+14 more)

### Community 663 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 664 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 665 - "generate_html_visualization.py"
Cohesion: 0.13
Nodes (22): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+14 more)

### Community 666 - "verify_migration.py"
Cohesion: 0.15
Nodes (22): _check_foreign_keys(), _check_null_values(), _check_table_exists(), main(), _print_json_validation_results(), _print_sample_data(), _print_verification_summary(), Connection (+14 more)

### Community 667 - "test_alias_expansion.py"
Cohesion: 0.18
Nodes (18): check_alias_safety(), handle_expanded_command(), Any, CommandExecutionRequest, Handle command processing with alias expansion and loop detection. This…, Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:…, validate_expanded_command() (+10 more)

### Community 668 - "RoomCacheLoader"
Cohesion: 0.20
Nodes (5): Any, BaseException, Loads room data from the database and populates a room cache dict. Used by…, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 669 - "error_handling_middleware.py"
Cohesion: 0.23
Nodes (13): add_error_handling_middleware(), FastAPI, Protocol, Error handling middleware for FastAPI integration. This module provides…, Add error handling middleware to FastAPI application. Args: app: FastAPI…, Register error handlers for FastAPI application. This function registers…, Setup complete error handling for FastAPI application. This function sets up…, Narrowing for dynamic request.state.user shapes that expose .id (non-Mapping). (+5 more)

### Community 670 - "CommunicationIntegrationProtocol"
Cohesion: 0.14
Nodes (10): CombatIntegrationProtocol, CommunicationIntegrationProtocol, Protocol, Protocols for NPC combat and communication integration (used by NPCBase)., Handle NPC death in the combat integration layer., Protocol for communication integration (whisper, room message, handle player…, Send a private whisper from this NPC to a single player., Send a message from this NPC to all players in a room. (+2 more)

### Community 671 - "MovementMonitor"
Cohesion: 0.09
Nodes (20): MovementMonitor, Any, UUID, Movement monitoring and validation system for MythosMUD. This module provides…, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms., Get comprehensive movement metrics. (+12 more)

### Community 672 - "test_add_player_effect_generates_id"
Cohesion: 0.23
Nodes (14): async_sessionmaker, asyncio, AsyncSession, serial, Verify get_rooms_with_exits() (room cache data source) includes arena zone…, Call get_player_by_id() with non-existent UUID; verify return shape when empty., Call get_npc_system_statistics() and verify result columns., Call add_player_effect() and verify it returns a non-null UUID. This guards… (+6 more)

### Community 673 - "test_retry.py"
Cohesion: 0.14
Nodes (13): Unit tests for retry utilities. Tests the retry decorator and retry logic., Test is_transient_error() identifies transient errors., Test is_transient_error() returns False for non-transient errors., DatabaseError wrapping asyncpg closed-connection must still retry (e2e…, __cause__ ConnectionDoesNotExistError makes the outer wrapper transient., Test retry_with_backoff() succeeds on first attempt., Test retry_with_backoff() retries on failure then succeeds., test_is_transient_error_cause_chain_connection_closed() (+5 more)

### Community 674 - ".call"
Cohesion: 0.16
Nodes (8): Any, Handle successful function call. Updates state based on current circuit state:…, Handle failed function call. Updates state based on failure count: - Increments…, Check if enough time has passed to attempt circuit reset. Returns: True if…, Calculate seconds until circuit can attempt reset. Returns: Seconds until retry…, Transition circuit to new state. Args: new_state: State to transition to AI:…, Get circuit breaker statistics. Returns: Dictionary with circuit breaker…, Execute function through circuit breaker. Enforces circuit breaker logic: -…

### Community 675 - "repositories/__init__.py"
Cohesion: 0.06
Nodes (39): Initialize the async persistence layer. This facade delegates to focused async…, ExperienceRepository, Any, Player, UUID, Experience repository for async persistence operations. This module provides…, Update player experience points atomically. Args: player_id: Player UUID or…, Update a specific numeric field in player stats atomically. Args: player_id:… (+31 more)

### Community 676 - "CircuitState"
Cohesion: 0.13
Nodes (14): CircuitState, Enum, Circuit breaker states. - CLOSED: Normal operation, requests pass through -…, Get current circuit state. Returns: Current CircuitState AI: For monitoring and…, Test _should_attempt_reset() returns False when not OPEN., Test _time_until_retry() returns remaining time., Test _time_until_retry() returns 0 after timeout., Test get_state() returns current state. (+6 more)

### Community 677 - "apply_communication_dampening"
Cohesion: 0.17
Nodes (21): apply_communication_dampening(), _apply_receiver_effects(), _apply_sender_effects(), DampeningResult, _maybe_muffle_fractured_message(), _maybe_scramble_deranged_message(), TypedDict, Communication dampening utilities for lucidity system. Implements communication… (+13 more)

### Community 678 - "exploration.sql"
Cohesion: 0.17
Nodes (7): schema_name.count_coordinated_rooms(), schema_name.get_room_id_by_stable_id(), schema_name.is_room_explored(), rooms, subzones, zones, player_exploration

### Community 679 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test get_room() returns None when room not found in persistence., Test get_adjacent_rooms() handles room with no exits., Test get_adjacent_rooms() handles target room not found., Test get_local_chat_scope() returns empty list when source room not found., Test get_room_occupants() handles room dict., Test get_room_occupants() falls back to persistence., Test validate_player_in_room() returns False when player not in room. (+17 more)

### Community 680 - "test_check_coverage_thresholds.py"
Cohesion: 0.15
Nodes (20): _CheckCoverageThresholdsModule, _fully_covered(), _load_script(), Protocol, Unit tests for scripts/check_coverage_thresholds.py. Covers `check_thresholds`'…, A KNOWN_COVERAGE_DEBT entry lowers the blanket 70% normal-file floor (#677)., A file present in CRITICAL_FILES but absent from the coverage.xml data (e.g.…, Typed surface of the loaded script, for the parts these tests exercise. (+12 more)

### Community 681 - "test_combat_persistence_handler.py"
Cohesion: 0.09
Nodes (23): mock_combat_service(), mock_player(), persistence_handler(), fixture, Unit tests for combat persistence handler - core functionality. Tests…, Create mock combat service., Create CombatPersistenceHandler instance., Test CombatPersistenceHandler initialization. (+15 more)

### Community 682 - "npcs.sql"
Cohesion: 0.15
Nodes (3): schema_name.get_npc_system_statistics(), npc_definitions, npc_spawn_rules

### Community 683 - "Performance Profiler Subagent"
Cohesion: 0.10
Nodes (21): Bottleneck Identification, Capabilities, Code Performance Review, Database Performance, Database Query Optimization, Enhanced Logging Integration, Example Scenarios, Game Loop Performance (+13 more)

### Community 684 - "Security Auditor Subagent"
Cohesion: 0.09
Nodes (21): Authentication & Authorization, Authentication Security Review, Capabilities, COPPA Compliance, COPPA Compliance (Critical), COPPA Compliance Verification, Example Scenarios, Input Validation (+13 more)

### Community 685 - "GitHub Actions Best Practices"
Cohesion: 0.09
Nodes (21): 1.1 Use Reusable Workflows and Composite Actions, 1.2 Name Jobs and Steps Consistently, 1.3 Employ Matrix Strategies for Broad Testing, 1.4 Set Explicit Concurrency Groups, 1. Workflow Design & Code Organization, 2.1 Cache Dependencies, 2. Performance Considerations, 3.1 Run Linters, Formatters, and Static Analysis Early (+13 more)

### Community 686 - "The Toolkit"
Cohesion: 0.09
Nodes (22): Overdrive Skill, Animate complex properties, Assess What "Extraordinary" Means Here, For data-heavy interfaces, For functional UI, For performance-critical UI, For visual/marketing surfaces, Implement with Discipline (+14 more)

### Community 687 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test call() closes circuit from HALF_OPEN after success threshold., Test call() reopens circuit from HALF_OPEN on failure., Test call() executes successfully in CLOSED state., Test call() handles failure in CLOSED state., Test call() opens circuit after failure threshold., Test call() raises CircuitBreakerOpen when circuit is OPEN., Test call() transitions to HALF_OPEN after timeout. (+7 more)

### Community 688 - "Complexity Refactoring Test Plan"
Cohesion: 0.09
Nodes (22): 1. Application Startup & CORS (create_app), 2. WebSocket Connections, 3. Room Operations, 4. Container Operations, 5. Player Respawn, 6. Game Tick Processing, 7. Integration Tests, Complexity Refactoring Test Plan (+14 more)

### Community 689 - "NATS Complete Remediation Summary"
Cohesion: 0.09
Nodes (22): After Remediation, Backward Compatibility, Before Remediation, Complete Fix Summary, Conclusion, Configuration Options Added, Documentation Created, Enhanced Configuration Usage (+14 more)

### Community 690 - "SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.09
Nodes (21): 1. SQL Injection Vulnerability in `update_player_stat_field()` - ✅ FIXED, 2. Missing Eager Loading for Relationships, 3. Mixed Database Access Patterns, 4. F-String SQL Construction (Even with Constants), 5. Missing Indexes on Foreign Keys, 6. Long-Lived Sessions, 7. Connection Pool Configuration, 8. Transaction Boundaries (+13 more)

### Community 691 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 692 - "fix_suppression_alignment.py"
Cohesion: 0.16
Nodes (21): add_pylint_suppression(), add_ruff_suppression(), _apply_fixes_to_line(), fix_file(), _group_fixes_by_line(), main(), parse_alignment_report(), _parse_file_line_pattern() (+13 more)

### Community 693 - "identify_critical_code.py"
Cohesion: 0.15
Nodes (21): analyze_file(), analyze_function(), calculate_complexity(), calculate_priority(), check_file_keywords(), check_function_keywords(), main(), process_ast_functions() (+13 more)

### Community 694 - "Phase 3: Polish and Optimization"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 3: Polish and Optimization, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 695 - "NPCEventReaction"
Cohesion: 0.05
Nodes (43): NPCEventReaction, NPCEventReactionTemplates, Any, Register reactions for a specific NPC. Args: npc_id: The ID of the NPC…, Handle an incoming event and trigger appropriate NPC reactions. Args: event:…, Update stored NPC context used by reaction conditions (room, name, alive)., Get context information for an NPC. Args: npc_id: The ID of the NPC Returns:…, Get statistics about an NPC's reactions. Args: npc_id: The ID of the NPC… (+35 more)

### Community 696 - "test_security_utils.py"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory. Args: filename: The filename…, Unit tests for security utilities. Tests path validation and file security…, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 697 - "Phase 4: Testing and Refinement"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 4: Testing and Refinement, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 698 - ".read_token"
Cohesion: 0.40
Nodes (4): BaseUserManager, ID, Reads a JWT token, validating its signature, audience, and server epoch., UP

### Community 699 - "Scenario 22: Invite-Only Registration Enforcement"
Cohesion: 0.10
Nodes (19): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, ✅ EXECUTED - ALL STEPS PASSED, Execution Record, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview (+11 more)

### Community 700 - "ContainerFactoryOptions"
Cohesion: 0.07
Nodes (20): ContainerFactoryOptions, Any, datetime, field_validator, TypedDict, UUID, Validate that metadata does not contain personal information (COPPA…, Validate and convert source_type to enum. (+12 more)

### Community 701 - "get_room_environment"
Cohesion: 0.12
Nodes (14): Test get_room_environment() treats empty string as no environment., Test get_room_environment() function., Test get_room_environment() returns room-specific environment., Test get_room_environment() returns subzone environment when room doesn't have…, Test get_room_environment() returns zone environment when room and subzone…, Test get_room_environment() returns default 'outdoors' when no environment…, Test get_room_environment() prioritizes room environment over subzone and zone., Test get_room_environment() prioritizes subzone environment over zone. (+6 more)

### Community 702 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 703 - "server/main.py"
Cohesion: 0.18
Nodes (12): _create_get_app(), main(), Any, FastAPI, get, MythosMUD Server - Main Application Entry Point This module serves as the…, Root endpoint providing basic server information., Test endpoint to verify JWT authentication is working. (+4 more)

### Community 704 - "ensurePlayableConnection"
Cohesion: 0.17
Nodes (25): nudgeStandBothPlayers(), despawnArmitage(), DIALOGUE, ensureArmitagePresent(), listArmitageIds(), loginAdminPlayable(), ensurePlayableConnection(), executeCommandWithoutRecovery() (+17 more)

### Community 705 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 706 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.20
Nodes (13): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Unit tests for channel broadcasting strategies. Tests the…, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…, Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., Test ChannelBroadcastingStrategyFactory.get_strategy() returns…, Test ChannelBroadcastingStrategyFactory.register_strategy() registers new…, Test global channel_strategy_factory instance exists. (+5 more)

### Community 707 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 708 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "A Message of Art; And Some Fell on Stony Ground; Nameless Ho", Community 10 - "Stowell; Betty Considine (waitress); Wesley Frost (bank cler", Community 1 - "Handout: Amaranthine 1; Dunwich (Keeper Map); Dunwich Throug", Community 2 - "An Amaranthine Desire; Captain Louis Gerd; Dunwich (Suffolk)", Community 3 - "An Amaranthine Desire; Clare Boone; Dunwich, Suffolk, Englan", Community 4 - "A Message of Art; Evocations of the Inner God; Josephin Pela", Community 5 - "Church of Sunyata; Craig Steele; The Hungry Void" (+12 more)

### Community 709 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "Pandora's Box / Pandora Handout 10", Community 10 - "Chapter 6: Pulp Magic, Psychic Powers, and Weird S / Psychic Powers", Community 1 - "Disintegrator device / Handout: Disintegrator 1", Community 2 - "Chapter 1: The Pulps / Chapter 7: Running Pulp Games", Community 3 - "Avoiding Certain Death / Call of Cthulhu 7th Edition", Community 4 - "Cthulhu Mythos / Deep One", Community 5 - "Seekers of Eternal Wisdom / Handout: Pandora's Box 12" (+12 more)

### Community 710 - "DOCUMENTATION_AUDIT.md"
Cohesion: 0.15
Nodes (13): Audit date, Code as Source of Truth, Documentation vs. Code Accuracy Audit Log, Summary, CONNECTION_MANAGER_ARCHITECTURE.md, ConnectionManager Modular Architecture, Logging Best Practices Pointer, ENHANCED_LOGGING_GUIDE.md (+5 more)

### Community 711 - "Asyncio Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.10
Nodes (21): 1. Blocking Synchronous Operations in Async Methods, 2. asyncio.run() Called from Context with Existing Event Loop, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Event Loop Change Detection May Not Handle All Cases, 6. Synchronous Database Operations in Async Context, 7. Missing Transaction Management in Batch Operations, 8. Connection Pool Size Configuration (+13 more)

### Community 712 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 713 - "Findings by Category"
Cohesion: 0.10
Nodes (21): 1.1 Database Connection Pools, 1.2 WebSocket Connection Leaks, 1.3 NATS Connection and Subscription Leaks, 1. Connection Management Leaks, 2.1 EventBus Subscriber Leaks, 2.2 Client-Side Event Handler Leaks, 2. Event System Leaks, 3.1 Task Registry Leaks (+13 more)

### Community 714 - "NATS Medium-Priority Remediation Summary"
Cohesion: 0.10
Nodes (21): NATSMessageBroker, 1. Integrated Subject Manager into NATSMessageBroker, 2. Added Health Monitoring to NATSMessageBroker, 3. Documented Manual Acknowledgment Strategy, After Medium-Priority Fixes, Before Medium-Priority Fixes, Completed Medium-Priority Fixes ✅, Configuration Options (+13 more)

### Community 715 - "Pydantic Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.10
Nodes (21): ⚠️ Areas for Improvement, 🟡 Business Logic in Models - Stats.**init**, Code Quality Observations, Conclusion, Critical Issues, 🔴 CRITICAL: Security Vulnerability - `extra="allow"` in Stats Model, Executive Summary, 🟢 Field Validator Organization (+13 more)

### Community 716 - "Game Subsystem Design Documents Overview"
Cohesion: 0.16
Nodes (19): ADR-003: Dual Event Systems (EventBus + NATS), Distributed EventBus via NATS, Event Ownership Matrix, NATS Subject Pattern Management, Game Subsystem Design Documents Overview, Admin Commands Subsystem Design, Combat Subsystem Design, Emote / Pose Subsystem Design (+11 more)

### Community 717 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 718 - "properties"
Cohesion: 0.15
Nodes (13): minLength, type, maximum, minimum, type, minLength, type, type (+5 more)

### Community 719 - "audit_suppressions.py"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 720 - "fix_markdown_line_length.py"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 721 - "populate_npc_sample_data.py"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 722 - "generate_invites_db.py"
Cohesion: 0.17
Nodes (17): normalize_database_url(), Normalize database URL for asyncpg. Args: database_url: Original database URL…, create_invite_in_db(), generate_invite_code(), generate_unique_codes(), get_existing_codes(), main(), parse_expires_date() (+9 more)

### Community 723 - "MemoryMonitor"
Cohesion: 0.04
Nodes (76): AllocSiteSample, _append_sample_jsonl(), _as_int(), collect_idle_memory_sample(), ConnectionStatsSnapshot, _container_instance(), _event_bus_queue_depth(), idle_sampler_enabled() (+68 more)

### Community 724 - "test_lucidity_command_disruption.py"
Cohesion: 0.16
Nodes (19): can_perform_action(), get_misfire_message(), Command disruption utilities for lucidity system. Implements command misfires…, Check if a command should misfire based on tier and command type. Args:…, Get the misfire message for a failed command. Args: command_type: Type of…, Check if player should involuntarily flee. Args: tier: Current lucidity tier…, Check if player can perform actions (motor lock check). Args: tier: Current…, should_involuntary_flee() (+11 more)

### Community 725 - "test_exploration_procedures.py"
Cohesion: 0.25
Nodes (20): player_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/exploration.sql (#633). Replaces raw SQL…, A third room at the source room's exact coordinates conflicts with it -- one… (+12 more)

### Community 726 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test restore_mp_from_rest() returns error when player not found., Test restore_mp_from_rest() restores MP., Test restore_mp_from_meditation() returns message when MP already at max., Test restore_mp_from_meditation() restores MP., Test restore_mp_from_item() respects max_mp limit., Test restore_mp_from_item() uses magic_service if available., Test restore_mp_from_item() calculates max_mp from power if not present. (+11 more)

### Community 727 - "reset_current_tick"
Cohesion: 0.25
Nodes (8): Set the current game tick (game tick loop)., Reset the current tick for testing., reset_current_tick(), set_current_tick(), Test get_current_tick returns the current tick value., Test reset_current_tick resets the tick counter., test_get_current_tick(), test_reset_current_tick()

### Community 728 - "player_effect_repository.py"
Cohesion: 0.05
Nodes (53): _add_effect_params(), AddEffectInput, _int_opt(), _opt_str(), PlayerEffectRepository, Any, TypedDict, UUID (+45 more)

### Community 729 - "TestPathValidator"
Cohesion: 0.10
Nodes (12): fixture, Tests for path validator functionality. Validates room connectivity analysis…, Test detection of mismatched return paths across zones., Test suite for path validation functionality., Create a path validator instance., Sample rooms with zone transitions., Test detection of zone transitions in room connections., Test detection of broken zone transitions. (+4 more)

### Community 730 - "Design Critique"
Cohesion: 0.10
Nodes (20): Critique Skill, 10. Microcopy & Voice, 1. AI Slop Detection (CRITICAL), 2. Visual Hierarchy, 3. Information Architecture, 4. Emotional Resonance, 5. Discoverability & Affordance, 6. Composition & Balance (+12 more)

### Community 731 - "useThemeContext.ts"
Cohesion: 0.22
Nodes (17): useAccessibilityPreference(), useAnimationPreference(), useColorSchemePreference(), useCompactModePreference(), useDebugInfoPreference(), useFontSizePreference(), useTheme(), useThemePreference() (+9 more)

### Community 732 - "compilerOptions"
Cohesion: 0.04
Nodes (46): compilerOptions, allowImportingTsExtensions, baseUrl, isolatedModules, jsx, lib, module, moduleResolution (+38 more)

### Community 733 - "Communities (10 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (19): Communities (10 total, 0 thin omitted), Community 0 - "Hotel Hell", Community 1 - "Petersen's Abominations", Community 2 - "Hotel Hell", Community 3 - "Voice on the Phone", Community 4 - "Mohole", Community 5 - "Panacea", Community 6 - "Panacea" (+11 more)

### Community 734 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, properties, minLength, type, id, name, season (+4 more)

### Community 735 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, minLength, type, properties, minLength, type, type (+4 more)

### Community 736 - "Lizard Complexity Analysis Findings"
Cohesion: 0.10
Nodes (19): 1. `create_app` - CCN: 22, 2. `_load_rooms_with_coordinates` - CCN: 12, 3. `_parse_websocket_token` - CCN: 12, 4. `_ensure_coordinates_generated` - CCN: 11, 🔴 CRITICAL: Functions Exceeding Threshold (CCN > 10), Functions with CCN = 10, Functions with CCN = 9, Lizard Complexity Analysis Findings (+11 more)

### Community 737 - "ConnectionManager Refactoring Summary"
Cohesion: 0.10
Nodes (20): 1. Statistics & Monitoring (`realtime/monitoring/`), 2. Error Handling (`realtime/errors/`), 3. Health Monitoring (`realtime/monitoring/`), 4. Cleanup & Maintenance (`realtime/maintenance/`), 5. Game State Management (`realtime/integration/`), 6. Room Event Integration (`realtime/integration/`), 7. Message Broadcasting (`realtime/messaging/`), After (+12 more)

### Community 738 - "Actionable Recommendations"
Cohesion: 0.10
Nodes (20): **~25-30% provide CRITICAL coverage**, Actionable Recommendations, Add Missing Integration Tests (70 tests, 0% risk, 10 hours effort), Command, Critical Gap Action (Month 2), Files, High-Priority Action (Next 2 Weeks), Immediate (This Week) (+12 more)

### Community 739 - "Phase 2: Qualitative Analysis Results"
Cohesion: 0.07
Nodes (30): 2.1 Regression Test Audit (★★★★★ HIGH VALUE), 2.2 Integration Test Analysis (★★★★☆ HIGH-MEDIUM VALUE), 2.3 Coverage Test Review (★★☆☆☆ MEDIUM-LOW VALUE), 2.4 Unit Test Pattern Analysis (★★★☆☆ MIXED VALUE), 2.5 Infrastructure Test Review (★☆☆☆☆ LOW VALUE), 2.6 E2E Test Analysis (★★★★★ HIGH VALUE), 2.7 Security Test Analysis (★★★★★ HIGH VALUE), Assessment (+22 more)

### Community 740 - "Transaction Boundaries Audit"
Cohesion: 0.10
Nodes (20): ✅ AsyncPersistenceLayer (Async), Audit Date, Audited Operations, Current State: ✅ GOOD, Future Improvements, Multi-Step Operations, Notes, Pattern 1: Connection Context Manager (PersistenceLayer) (+12 more)

### Community 741 - "LoggingPatternLinter"
Cohesion: 0.11
Nodes (15): FormattedValue, lint_file(), LoggingPatternLinter, main(), Call, Import, ImportFrom, Path (+7 more)

### Community 742 - "logging_file_categories.py"
Cohesion: 0.12
Nodes (17): Formatter, _PlayerGuidFormatterType, create_formatter(), create_handler_for_category(), Path, RotatingFileHandler, Logger-name categories and per-category file handlers for enhanced logging. The…, Create formatter (with or without PlayerGuidFormatter). (+9 more)

### Community 743 - "fixtures/unit/__init__.py"
Cohesion: 0.13
Nodes (18): MockerFixture, dummy_request(), fakerandom(), Any, fixture, SimpleNamespace, Unit-tier fixtures with strict mocking and in-memory fakes., Provide deterministic random seed for unit tests. (+10 more)

### Community 744 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 745 - "UpgradeImplementationPlan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 746 - "SpellTargetingService"
Cohesion: 0.20
Nodes (11): Player, UUID, Resolve the target for a spell cast. Args: player_id: ID of the player casting…, Get player from persistence., Build a TargetMatch for a combat opponent, or None if unresolved., Get the combat target for a player if they are in combat. Args: player_id:…, Service for resolving spell targets. Handles target resolution based on spell…, Resolve self-target spell. Returns (target_match, error_message). (+3 more)

### Community 747 - "PartyService"
Cohesion: 0.14
Nodes (17): PartyService, UUID, Add a player to a party. Fails if party does not exist or player is already in…, Remove expired pending invites and notify inviters., Send a command_response-style message to a single player., Send party_invite event to the target player only., Create a pending party invite and send party_invite event to target. Target…, Normalize ID to string for dict keys and membership sets. (+9 more)

### Community 748 - "SpellEffects"
Cohesion: 0.02
Nodes (129): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+121 more)

### Community 749 - "asyncio"
Cohesion: 0.14
Nodes (14): asyncio, Test get_player_room_from_persistence() returns player room., Test is_player_in_room() returns True when player is in room., Test preload_receiver_mute_data() excludes sender from targets., test_check_player_mute_status_patched_and_emote(), test_filter_target_players_room_and_mute(), test_get_player_room_from_persistence(), test_get_player_room_from_persistence_mock_player() (+6 more)

### Community 750 - "test_security_headers.py"
Cohesion: 0.05
Nodes (49): MutableHeaders, Any, ASGIApp, Receive, Request, Scope, Send, Backward-compatible dispatch method for BaseHTTPMiddleware interface. This… (+41 more)

### Community 751 - "Any"
Cohesion: 0.17
Nodes (7): PlayerServiceProtocol, Any, Protocol, Protocol for player service., Resolve player name to player object., Get all mutes applied by a player., Get user management system statistics.

### Community 752 - "channel_broadcasting_strategies.py"
Cohesion: 0.21
Nodes (10): ChannelBroadcastingStrategy, GlobalChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for whisper channel broadcasting., Abstract base class for channel broadcasting strategies., Initialize the strategy factory., Register a new strategy for a channel type. Args: channel_type: Channel type to… (+2 more)

### Community 753 - "TestVerificationSqlUsersPlayers"
Cohesion: 0.10
Nodes (12): PostgreSQL-focused tests for verification and maintenance SQL scripts.…, Tests for db/verification/users_players.sql alignment with current schema., Verification SQL file must exist., Verification SQL must not reference staging tables or select obsolete columns., Verification SQL must use explicit join syntax for multi-table queries., Verification SQL must reference users and players tables., Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)., NPC name constraint script must exist. (+4 more)

### Community 754 - "test_nats_message_handler_subzone_events.py"
Cohesion: 0.04
Nodes (68): asyncio, Unit tests for NATS message handler subzone and event handling. Tests subzone…, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test subscribe_to_subzone raises error when subject manager unavailable., Test unsubscribe_from_event_subjects handles partial success., Test subscribe_to_event_subjects handles partial failure., Test get_event_subscription_count returns count. (+60 more)

### Community 755 - "optimized_validate_player_name"
Cohesion: 0.09
Nodes (22): Test validating empty player name., Test validating player name below min length., Test validating player name above max length., Test validating player name with spaces., Test validating valid player name., Test validating player name with underscore., Test validating player name with hyphen., Test validating player name with numbers. (+14 more)

### Community 756 - "static_data/package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 757 - "TypeScript Best Practices"
Cohesion: 0.11
Nodes (18): 1. Enable Strict Mode in `tsconfig.json`, 2. Define Clear Type Contracts, 3. Avoid `any` and Prefer `unknown` for Untyped Data, 4. Implement Robust Runtime Type Validation (Type Guards), 5. Prefer Union Types over Traditional Enums, 6. Use Generics for Reusable Components/Functions, 7. Enforce Consistent Code Organization, ❌ BAD: Numeric Enums (+10 more)

### Community 758 - "vite Best Practices"
Cohesion: 0.11
Nodes (18): 1. Code Organization and Structure, 2. Common Patterns and Anti-patterns, 3. Performance Considerations, 4. Common Pitfalls and Gotchas, 5. Testing Approaches, Audit Custom Plugins, Avoid Barrel Files, Embrace Native ES Modules (+10 more)

### Community 759 - "Delight Techniques"
Cohesion: 0.11
Nodes (19): Delight Skill, Appropriate to Context, Assess Delight Opportunities, Celebration Moments, Compound Over Time, Delight Amplifies, Never Blocks, Delight Principles, Delight Techniques (+11 more)

### Community 760 - "Frontend Aesthetics Guidelines"
Cohesion: 0.22
Nodes (9): Color & Theme, Frontend Aesthetics Guidelines, Interaction, Layout & Space, Motion, Responsive, Typography, UX Writing (+1 more)

### Community 761 - "Any"
Cohesion: 0.17
Nodes (7): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Check if new data is newer than old data for a specific key. Args: old_data:…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,…, Store room data in cache. Args: room_id: Room ID to store room_data: Room data…

### Community 762 - "compilerOptions"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 763 - "test_command_factories_inventory.py"
Cohesion: 0.14
Nodes (18): Unit tests for inventory command factories. Tests the InventoryCommandFactory…, Test create_unequip_command() raises error with empty args., Test create_unequip_command() raises error with whitespace only., Test create_unequip_command() handles known slot., Test create_unequip_command() handles unknown slot as search term., Test create_unequip_command() handles multi-word search term., Test create_unequip_command() handles all known slots., Test create_unequip_command() creates UnequipCommand. (+10 more)

### Community 764 - "Enhanced Logging Best Practices for MythosMUD"
Cohesion: 0.11
Nodes (19): Common Anti-Patterns, Conclusion, Configuration, 🚨 CRITICAL ANTI-PATTERNS - DO NOT USE, Custom Log Analysis, ✅ Do This Instead, ❌ Don't Do This, Enhanced Logging Best Practices for MythosMUD (+11 more)

### Community 765 - "Persistence Layer Extraction - COMPLETE ✅"
Cohesion: 0.11
Nodes (19): Architecture Changes, Benefits, Cleanup, Conclusion, File Size Reduction, Files Modified, Migration Path for Callers, Next Steps (+11 more)

### Community 766 - "Test Coverage Summary: Disconnect Grace Period & Rest Command"
Cohesion: 0.13
Nodes (19): Coverage Targets, Coverage Verification, Critical Files (90% Target), E2E Scenarios, E2E Test Scenarios, Expected Coverage Results, Grace Period System Tests, Integration Tests (+11 more)

### Community 767 - "test_email_utils.py"
Cohesion: 0.18
Nodes (17): generate_unique_bogus_email(), is_bogus_email(), AsyncSession, Email utilities for MythosMUD authentication. This module provides utilities…, Generate a unique bogus email address for a user. This function creates a bogus…, Check if an email address is a bogus email generated by our system. Args:…, Validate that a bogus email follows our expected format. Args: email: The email…, validate_bogus_email_format() (+9 more)

### Community 768 - "NPCCacheService"
Cohesion: 0.23
Nodes (8): NPCCacheService, Service for caching NPC definitions and spawn rules., Invalidate all NPC definition caches., Invalidate all NPC spawn rule caches., _NpcDef, asyncio, _SpawnRule, TestNPCCacheService

### Community 769 - "ProfessionCacheService"
Cohesion: 0.19
Nodes (7): ProfessionCacheService, Service for caching profession data., Initialize the profession cache service. Args: persistence: Persistence layer…, Invalidate all profession caches., _Profession, fixture, TestProfessionCacheService

### Community 770 - ".create_put_command"
Cohesion: 0.10
Nodes (19): Test create_put_command() handles optional 'in' keyword., Test create_put_command() with quantity., test_create_put_command_with_in(), test_create_put_command_with_quantity(), Test create_put_command() raises error with no args., Test create_put_command() raises error with only item., Test create_put_command() handles 'in' keyword., Test create_put_command() raises error when quantity is zero. (+11 more)

### Community 771 - ".create_get_command"
Cohesion: 0.10
Nodes (19): Test create_get_command() creates GetCommand., Test create_get_command() handles optional 'from' keyword., test_create_get_command(), test_create_get_command_with_from(), Test create_get_command() raises error with no args., Test create_get_command() with single arg returns get-from-room…, Test create_get_command() handles 'from' keyword., Test create_get_command() raises error when quantity is zero. (+11 more)

### Community 772 - "test_party_flow.py"
Cohesion: 0.18
Nodes (15): PartyUpdated, Event fired when party membership or leadership changes. Emitted by…, event_bus(), party_events(), party_service(), asyncio, fixture, Integration tests for party (ephemeral grouping) feature. Flow: Two players;… (+7 more)

### Community 773 - "room_hierarchy_schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, anyOf, description, description, exits, id, name, required (+3 more)

### Community 774 - "schedule_end_combat_if_npc_died_best_effort"
Cohesion: 0.31
Nodes (8): Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…, schedule_end_combat_if_npc_died_best_effort(), patch, Unit tests for best-effort NPC combat cleanup scheduling., When combat service is missing, scheduling is a no-op., Without a running asyncio loop, scheduling fails quietly (RuntimeError path)., test_schedule_end_combat_if_npc_died_no_running_loop(), test_schedule_end_combat_if_npc_died_no_service()

### Community 775 - "CoordinateValidator"
Cohesion: 0.14
Nodes (15): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Coordinate validation service for ASCII maps. This module provides conflict…, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate…, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:… (+7 more)

### Community 776 - "test_hallucination_services.py"
Cohesion: 0.03
Nodes (91): FakeHallucinationService, Any, UUID, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Select which type of fake hallucination to trigger (50/50 chance). Returns:…, Service for generating fake NPC tells and room text overlays. These…, Initialize the fake hallucination service., Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will… (+83 more)

### Community 777 - "enum"
Cohesion: 0.17
Nodes (12): default, description, enum, type, arena, indoors, intersection, outdoors (+4 more)

### Community 778 - ".create_equip_command"
Cohesion: 0.10
Nodes (19): Test create_equip_command() raises error when index is zero., Test create_equip_command() raises error when index is negative., Test create_equip_command() handles index with slot., Test create_equip_command() handles search term with slot., Test create_equip_command() raises error when search term is empty., Test create_equip_command() infers slot from known slots., Test create_equip_command() creates EquipCommand., Test create_equip_command() raises error with no args. (+11 more)

### Community 779 - "fixtures/shared/__init__.py"
Cohesion: 0.13
Nodes (15): fake_clock(), make_player_dict(), make_user_dict(), Any, fixture, Shared fixtures and builders for all test tiers., Create a user dictionary for testing., Create a player dictionary for testing. (+7 more)

### Community 780 - "retry_with_backoff"
Cohesion: 0.22
Nodes (10): F, asyncio, Test retry_with_backoff() with async function succeeds on first attempt., Test retry_with_backoff() with async function retries on failure then succeeds., Retry decorator must not treat wrapped closed-connection as final on attempt 1., test_retry_retries_wrapped_connection_closed_then_succeeds(), test_retry_with_backoff_async_failure_then_success(), test_retry_with_backoff_async_success() (+2 more)

### Community 781 - "_GenerateOpenapiSpecModule"
Cohesion: 0.19
Nodes (15): _GenerateOpenapiSpecModule, _load_script(), fixture, Protocol, Unit tests for scripts/generate_openapi_spec.py's tag-table generation logic.…, Typed surface of the loaded script, for the parts these tests exercise., Build a minimal OpenAPI-shaped dict: one operation per tag list in paths_tags., script() (+7 more)

### Community 782 - "room_validator/tests/conftest.py"
Cohesion: 0.15
Nodes (18): dead_end_room(), invalid_room_data(), fixture, Pytest configuration and fixtures for room validator tests. Provides test data…, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit. (+10 more)

### Community 783 - "click Best Practices"
Cohesion: 0.11
Nodes (18): 1. Code Organization & Structure, 2. Argument Parsing: Arguments vs. Options, 3. Output: `click.echo` and `click.secho`, 4. Type Hints, 5. Comprehensive Help Text & Examples, 6. Packaging with `pyproject.toml`, 7. Testing with `CliRunner`, ❌ BAD: Inconsistent Output (+10 more)

### Community 784 - "2. Type Hinting Best Practices"
Cohesion: 0.11
Nodes (17): 1.1. Centralized Configuration, 1.2. CI/CD & Pre-commit Hooks, 1.3. Incremental Adoption, 1. Configuration & Integration, 2.1. Prefer `object` over `Any`, 2.2. Use `TypeAlias` for Type Aliases, 2.3. Concrete vs. Abstract Types, 2.4. Shorthand Union Syntax (+9 more)

### Community 785 - "Animate Skill"
Cohesion: 0.11
Nodes (18): Animate Skill, Accessibility, Assess Animation Opportunities, CSS Animations, Delight Moments, Entrance Animations, Feedback & Guidance, Implement Animations (+10 more)

### Community 786 - "Polish Systematically"
Cohesion: 0.11
Nodes (18): Polish Skill, Code Quality, Color & Contrast, Content & Copy, Edge Cases & Error States, Final Verification, Forms & Inputs, Icons & Images (+10 more)

### Community 787 - "overrides"
Cohesion: 0.11
Nodes (18): overrides, @asyncapi/generator, @asyncapi/generator-components, @asyncapi/generator-helpers, @asyncapi/specs, fast-uri, flatted, glob (+10 more)

### Community 788 - "Migration 019 Ready for Deployment"
Cohesion: 0.12
Nodes (17): Migration 019 Complete Summary, 019_postgresql_anti_patterns_fixes.sql, Migration 019 Ready for Deployment, Application Script, Database Schema, Documentation, Files Ready, Implementation Complete (+9 more)

### Community 789 - "Gladiator Ring (Arena) Implementation Plan"
Cohesion: 0.11
Nodes (16): Gladiator Ring (Arena) — Implementation Todos, Phase 1: Schema and world data (Codebase Explorer for DML/schema pattern discovery) — DONE, Phase 2: Tutorial exit and respawn (main agent), Phase 3: NPC startup — also spawn in arena (main agent) — DONE, Phase 4: Tests and validation (main agent / Test Suite Analyzer) — DONE, Plan frontmatter todos (for Cursor plan file), Subagent usage, Todos (detailed) (+8 more)

### Community 790 - "Python Model Updates Required for Migration 019"
Cohesion: 0.11
Nodes (18): 1. Import BigInteger, 2. Files Requiring Updates, Impact Assessment, Integer → BigInteger, Low Risk Changes, No Breaking Changes Expected, Overview, Python Model Updates Required for Migration 019 (+10 more)

### Community 791 - "Recommended Test Additions"
Cohesion: 0.11
Nodes (18): 1. MessageBroker Integration Tests (15 tests, ~1 hour), 2. ApplicationContainer Lifecycle Tests (10 tests, ~1 hour), 3. Database Migration Tests (10 tests, ~1.5 hours), 4. WebSocket Edge Case Tests (15 tests, ~2 hours), 5. Error Recovery Tests (20 tests, ~3 hours), Additions, Coverage Gap Priority Matrix, If We Execute Full Recommendations (+10 more)

### Community 792 - "Critical Coverage Gaps"
Cohesion: 0.11
Nodes (18): Critical Coverage Gaps, Database Connection Loss, Gap 10: Configuration Edge Cases, Gap 1: Domain Layer (NEW ARCHITECTURE), Gap 2: Message Broker Abstraction, Gap 3: ApplicationContainer Lifecycle, Gap 4: Error Recovery Paths, Gap 5: Async/Await Pattern Verification (+10 more)

### Community 793 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 794 - "properties"
Cohesion: 0.20
Nodes (10): properties, minLength, pattern, type, minLength, type, type, id (+2 more)

### Community 795 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.17
Nodes (17): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+9 more)

### Community 796 - "init_npc_database.py"
Cohesion: 0.16
Nodes (17): _determine_database_init_flags(), get_npc_database_url(), get_npc_seed_data_from_postgresql(), init_database_schema(), _initialize_database_with_url(), main(), populate_npc_data(), _print_final_message() (+9 more)

### Community 797 - "lint_raw_sql_in_python.py"
Cohesion: 0.16
Nodes (17): AllowlistEntry, _collect_python_files(), _find_raw_sql_lines(), main(), _overdue_message(), Path, Guard against raw table CRUD SQL string literals inside Python source. Replaces…, Return line with a trailing '# ...' comment removed, so prose mentioning SQL… (+9 more)

### Community 798 - "test_cancel_shutdown_countdown_no_active"
Cohesion: 0.21
Nodes (13): _PendingCheckAppStub, _PendingCheckStateStub, Test is_shutdown_pending() returns True when shutdown is pending., Test is_shutdown_pending() returns False when shutdown is not pending., Test cancel_shutdown_countdown() when no shutdown is active., Test cancel_shutdown_countdown() successfully cancels shutdown., _ShutdownCancelAppStub, _ShutdownCancelStateStub (+5 more)

### Community 799 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., party_invite producer emits a build_event-shaped envelope., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success() (+3 more)

### Community 800 - "NATSRetryHandler"
Cohesion: 0.04
Nodes (75): NATSRetryHandler, Any, Exception, Calculate exponential backoff delay with jitter. Args: attempt: Current attempt…, Determine if a message should be retried. Args: message: Message that failed…, Retry a function with exponential backoff. Args: func: Async function to retry…, Get retry statistics. Returns: Dictionary with retry metrics AI: For monitoring…, Retry async function with exponential backoff. Attempts the function up to… (+67 more)

### Community 801 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_players_batch with actual players (UUID conversion)., Test _load_room_cache_async logs sample room IDs when rooms are loaded…, Test _load_room_cache_async handles table not found error., Test _load_room_cache_async raises other errors., Test _query_rooms_with_exits_async handles table not found error., Test _query_rooms_with_exits_async raises other errors., test_get_players_batch_with_players() (+5 more)

### Community 802 - "ChatWhisperTracker"
Cohesion: 0.17
Nodes (7): ChatWhisperTracker, Tracks last whisper senders for reply functionality., Initialize the whisper tracker., Store the last whisper sender for a player. Args: receiver_name: Name of the…, Get the last whisper sender for a player. Args: player_name: Name of the player…, Clear the last whisper sender for a player. Args: player_name: Name of the…, Get all whisper trackings (for testing/debugging). Returns: Dictionary mapping…

### Community 803 - "enum"
Cohesion: 0.18
Nodes (11): description, enum, type, arena, indoors, intersection, outdoors, street_paved (+3 more)

### Community 804 - ".check_bidirectional_connections"
Cohesion: 0.11
Nodes (9): Get the opposite direction for bidirectional checking., Find rooms with no exits (dead ends). Args: room_database: Dictionary mapping…, Find rooms that reference themselves in exits. Args: room_database: Dictionary…, Generate minimap graph data for visualization. Args: room_database: Dictionary…, Build adjacency graph from room database. Args: room_database: Dictionary…, Get target room ID from exit data., Check if exit is marked as one-way., Extract zone and sub_zone from room data. Args: room_id: Room identifier… (+1 more)

### Community 805 - "SQLAlchemy Best Practices (2.x Style)"
Cohesion: 0.12
Nodes (17): 1.1 Declarative Models with Type Annotations, 1.2 Mixins for Common Fields, 1. Code Organization and Data Modeling, 2.1 Context Manager for Sessions, 2.2 Explicit Transaction Blocks, 2. Session Management, 3.1 Use `select()` for All Queries, 3.2 Eager Loading Relationships (+9 more)

### Community 806 - "Introduce Color Strategically"
Cohesion: 0.12
Nodes (17): Colorize Skill, Accent Color Application, Accessibility, Assess Color Opportunity, Background & Surfaces, Balance & Refinement, Borders & Accents, Cohesion (+9 more)

### Community 807 - "knip.json"
Cohesion: 0.07
Nodes (27): entry, ignore, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries (+19 more)

### Community 808 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 809 - "commandStore.ts"
Cohesion: 0.16
Nodes (15): CommandActions, CommandAlias, CommandHistoryEntry, CommandSelectors, CommandState, CommandStore, CommandStoreGet, CommandStoreSet (+7 more)

### Community 810 - "AggressiveMobNPC"
Cohesion: 0.17
Nodes (11): AggressiveMobNPC, Aggressive mob NPC type with hunting and territorial behaviors., Get aggressive mob-specific behavior rules., _get_attack_damage coerces behavior_config attack_damage robustly., Non-digit attack_damage string in behavior_config falls back to 1., hunt_target appends each id once; repeated calls keep a single _targets entry., Warnings path: failure in _compute_player_context must not raise., test_enrich_behavior_context_swallows_compute_errors() (+3 more)

### Community 811 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)"
Cohesion: 0.12
Nodes (16): Communities (9 total, 4 thin omitted), Community 0 - "De Vermiis Mysteriis; Dust of Ibn-Ghazi", Community 1 - "Character Creation", Community 2 - "Alone Against the Flame", Community 3 - "Cover Art", Community 4 - "Azathoth; Banishment Chant (Latin)", Community Hubs (Navigation), Corpus Check (+8 more)

### Community 812 - "applies_to"
Cohesion: 0.28
Nodes (9): items, minItems, type, uniqueItems, items, items, minLength, type (+1 more)

### Community 813 - "Async Remediation Complete"
Cohesion: 0.12
Nodes (17): Async Remediation Complete, Adjusts spectacles with scholarly satisfaction, Critical Fixes Implemented (4 Code Changes), December 3, 2025, Documentation Created (5 Documents, ~2,500 lines), 📚 Key Documents, 🎓 Key Takeaway, Mission Accomplished (+9 more)

### Community 814 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 815 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 816 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 817 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 818 - "fix_file"
Cohesion: 0.18
Nodes (16): fix_blanks_around_fences(), fix_blanks_around_headings(), fix_blanks_around_lists(), fix_fence_language(), fix_file(), fix_line_length(), fix_trailing_punctuation_in_headings(), main() (+8 more)

### Community 819 - "jackson_linter.py"
Cohesion: 0.20
Nodes (16): collect_json_files(), _file_appears_binary_or_terminal_output(), _first_fallback_encoding_that_parses(), _is_vscode_jsonc_settings(), main(), Path, Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1…, VS Code allows JSON with Comments in settings.json; stdlib json cannot parse it. (+8 more)

### Community 820 - "RoomFilenameMigrator"
Cohesion: 0.19
Nodes (10): main(), Path, Update the room ID in the JSON file to match new naming schema., Execute the migration., Handles migration of room filenames from old to new schema., Initialize the migrator., Parse old filename format to extract components., Discover all room files that need migration. (+2 more)

### Community 821 - "CacheManager"
Cohesion: 0.14
Nodes (9): CacheManager, Any, Centralized cache manager for MythosMUD server. Manages multiple LRU caches for…, Initialize the cache manager., Initialize default caches with appropriate configurations., Get a cache by name. Args: name: The name of the cache Returns: The cache…, Create a new cache. Args: name: The name of the cache max_size: Maximum number…, Delete a cache. Args: name: The name of the cache to delete Returns: True if… (+1 more)

### Community 822 - "client/package.json"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 824 - "test_occupants.py"
Cohesion: 0.18
Nodes (18): _format_occupants_result(), _get_event_handler_for_test_occupants(), _get_room_id_for_test_occupants(), handle_npc_test_occupants_command(), Any, NPC test-occupants command for debugging occupant queries., Resolve application, player, room_id, and event handler for NPC test occupants…, Handle NPC test occupants command - manually trigger occupant query for… (+10 more)

### Community 825 - "asyncio"
Cohesion: 0.14
Nodes (17): PartyChannelStrategy, Strategy for party channel broadcasting. Delivers only to current party members., asyncio, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() sends personal message., Test WhisperChannelStrategy.broadcast() handles missing target_player_id. (+9 more)

### Community 826 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 827 - "test_message_filtering.py"
Cohesion: 0.17
Nodes (9): Unit tests for message filtering. Tests the MessageFilteringHelper class., Test is_player_muted_by_receiver() checks mute status., Test _get_user_manager() falls back to a fresh UserManager when none was…, Test collect_room_targets() returns subscribed players., Test collect_room_targets() returns empty set when no subscribers., test_collect_room_targets(), test_collect_room_targets_empty(), test_get_user_manager_global() (+1 more)

### Community 828 - "test_player_repository.py"
Cohesion: 0.04
Nodes (68): _make_mock_row(), mock_player(), player_repository(), asyncio, fixture, UUID, Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes with room cache. (+60 more)

### Community 829 - "test_player_spell_repository.py"
Cohesion: 0.12
Nodes (25): Any, UUID, Learn a new spell for a player. Args: player_id: Player ID spell_id: Spell ID…, Update mastery level for a player spell. Args: player_id: Player ID spell_id:…, Map procedure result row to PlayerSpell model., Record that a player cast a spell (increment times_cast, update last_cast_at).…, Get all spells learned by a player. Args: player_id: Player ID Returns:…, Get a specific player spell. Args: player_id: Player ID spell_id: Spell ID… (+17 more)

### Community 830 - "asyncio"
Cohesion: 0.13
Nodes (12): asyncio, Test _handle_special_command_routing function., Test _handle_special_command_routing handles alias management commands., Test _handle_special_command_routing returns error when alias storage…, Test _handle_special_command_routing converts single-word emotes., Test _process_alias_expansion function., Test _process_alias_expansion returns None when no alias storage., Test _process_alias_expansion returns None when alias not found. (+4 more)

### Community 831 - "optimized_validate_security_comprehensive"
Cohesion: 0.20
Nodes (10): Test comprehensive security validation of empty string., Test comprehensive security validation of valid text., Test comprehensive security validation with dangerous characters., Test comprehensive security validation with injection pattern., test_optimized_validate_security_comprehensive_dangerous_chars(), test_optimized_validate_security_comprehensive_empty(), test_optimized_validate_security_comprehensive_injection(), test_optimized_validate_security_comprehensive_valid() (+2 more)

### Community 832 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 833 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 834 - "Codebase Explorer Subagent"
Cohesion: 0.14
Nodes (15): Architecture Analysis, Best Practices, Capabilities, Codebase Explorer Subagent, Dependency Research, Example Scenarios, Finding All Implementations, Integration (+7 more)

### Community 835 - "Pylint Best Practices"
Cohesion: 0.12
Nodes (15): 1.1. Silence the Noise, Enable What Matters, 1.2. Filter by Confidence, 1. Configuration is King: `pyproject.toml`, 2.1. Docstrings for Everything, 2.2. Naming Conventions, 2.3. Manage Complexity, 2. Code Organization & Readability, 3.1. Specific Exception Handling (+7 more)

### Community 836 - "Adapt Skill"
Cohesion: 0.12
Nodes (16): Adapt Skill, Assess Adaptation Challenge, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Techniques, MANDATORY PREPARATION (+8 more)

### Community 837 - "Improve Copy Systematically"
Cohesion: 0.12
Nodes (16): Clarify Skill, Apply Clarity Principles, Assess Current Copy, Button & CTA Text, Confirmation Dialogs, Empty States, Error Messages, Form Labels & Instructions (+8 more)

### Community 838 - "UX Writing"
Cohesion: 0.12
Nodes (16): Avoid Redundant Copy, Confirmation Dialogs: Use Sparingly, Consistency: The Terminology Problem, Don't Blame the User, Empty States Are Opportunities, Error Message Templates, Error Messages: The Formula, Form Instructions (+8 more)

### Community 839 - "saveMapChanges.ts"
Cohesion: 0.31
Nodes (16): buildJsonHeaders(), createExit(), deleteExit(), ParsedEdgeId, parseEdgeId(), readErrorDetail(), recalculateCoordinates(), RecalculateCoordinatesResult (+8 more)

### Community 840 - "message_handler_factory.py"
Cohesion: 0.06
Nodes (51): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, MessageHandlerFactory, PartyInviteResponseMessageHandler, PingMessageHandler (+43 more)

### Community 841 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)"
Cohesion: 0.12
Nodes (15): Communities (17 total, 12 thin omitted), Community 0 - "Character and Skills", Community 1 - "Character and Skills (1)", Community 2 - "Core Rules", Community 3 - "Core Rules (3)", Community 4 - "Character Sheets", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 842 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (12 total, 7 thin omitted), Community 0 - "Call of Cthulhu (7th Edition); Chaosium Inc.", Community 1 - "APP; Characteristics", Community 2 - "Everett Scanlon; Gustavo Romero", Community 3 - "First Aid; Hit Points", Community 4 - "Formless Spawn of Tsathoggua; Rudolf Zimmer", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 843 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (5 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Bernard Corbitt; Randolph Tomaszewski", Community 2 - "Ramasekva; Yog-Sothoth", Community 3 - "Arthur Cornthwaite; Fitzgerald Manse", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions) (+7 more)

### Community 844 - "Changes by document"
Cohesion: 0.12
Nodes (16): Changes by document, CLAUDE.md, docs/COMMAND_MODELS_REFERENCE.md, docs/CONFIGURATION_FILES_REFERENCE.md, docs/CONTAINER_SYSTEM_API_REFERENCE.md, docs/DATABASE_ACCESS_PATTERNS.md, docs/E2E_TESTING_GUIDE.md, docs/EVENT_OWNERSHIP_MATRIX.md (+8 more)

### Community 845 - "Memory Leak Audit Report"
Cohesion: 0.12
Nodes (16): Audit Completion Summary, Audit Methodology, _closed_websockets Unbounded Set, Common Patterns Identified, EventBus Subscriber Leaks, Executive Summary, ✅ Good Patterns (No Leaks), High Priority Fixes (+8 more)

### Community 846 - "Quick Start: Running E2E Tests"
Cohesion: 0.12
Nodes (16): Expected Results, Method A: Use the E2E startup script (Simplest), Method B: Manual startup (More control), Next Actions, Prerequisites ✅, Problem: "element(s) not found" errors, Problem: Login failed (500), Problem: Server won't start (+8 more)

### Community 847 - "test_ascii_map_renderer_grid.py"
Cohesion: 0.17
Nodes (10): fixture, Unit tests for AsciiMapRenderer grid building. Guards against regressions in…, Return a fresh AsciiMapRenderer instance for each test., Tests for _build_grid player marker when multiple rooms share coordinates., Multiple rooms at same (x,y): cell keeps player marker even if player room is…, render_map covers empty map, styles, exits, and row rendering., renderer(), test_determine_map_style_and_symbols() (+2 more)

### Community 848 - "_errors_len"
Cohesion: 0.17
Nodes (12): _errors_len(), Test _spawn_required_npcs() handles missing spawn room., Narrow spawn/startup result dict for len(results['errors']) without propagating…, Test _spawn_required_npcs() handles exceptions during spawning., Test _spawn_optional_npcs() handles exceptions during spawning., Test spawn_npcs_on_startup() handles exceptions during session processing., Test spawn_npcs_on_startup() handles critical exceptions., test_spawn_npcs_on_startup_critical_exception() (+4 more)

### Community 849 - "holiday.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 850 - "schedule.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 851 - "analyze_coverage_gaps.py"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and…, Write critical files below threshold section. (+7 more)

### Community 852 - "_apply_arena_seed_patch.py"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 853 - "pylint.py"
Cohesion: 0.23
Nodes (13): _combined_output(), _CompletedProcessLike, is_pylint_startup_failure(), main(), Path, Protocol, Prefer current interpreter -m pylint (works under uv run --no-sync)., Fail fast before scanning if pylint cannot start (missing package, broken venv). (+5 more)

### Community 854 - "generate_sql.mjs"
Cohesion: 0.30
Nodes (15): ajv, __dirname, ensureDir(), __filename, generateEmotes(), generateHolidays(), generateNpcSchedules(), generateRooms() (+7 more)

### Community 855 - "fixture"
Cohesion: 0.18
Nodes (11): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), fixture, Create a mock room manager., Create a mock get_async_persistence callback. (+3 more)

### Community 856 - "validate_admin_permission"
Cohesion: 0.23
Nodes (14): Any, Validate that a player has admin permissions. Args: player: Player object to…, validate_admin_permission(), _BrokenAdminPlayer, mock_admin_logger(), asyncio, fixture, Unit tests for admin permission validation. (+6 more)

### Community 858 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 859 - "NPCActionMessage"
Cohesion: 0.15
Nodes (15): _float_field(), NPCActionMessage, NPCActionType, _optional_int_field(), _optional_str_field(), Enum, Convert message to JSON string., Create message from JSON string. (+7 more)

### Community 860 - "UUID"
Cohesion: 0.17
Nodes (9): Any, UUID, Broadcast party message to party members only, with dampening and mute checks., Send whisper message to specific player with communication dampening., Broadcast system/admin message; personal when target_player_id is set., Handle unknown channel type., Broadcast message according to channel strategy. Args: chat_event: WebSocket…, Broadcast room-based message with server-side filtering. (+1 more)

### Community 861 - "test_circuit_breaker.py"
Cohesion: 0.11
Nodes (17): Unit tests for circuit breaker. Tests the CircuitBreaker class and…, Test _on_success() increments success count in HALF_OPEN state., Test _on_failure() increments failure count., Test _on_failure() opens circuit at threshold., Test _on_failure() resets success count., Test _should_attempt_reset() returns False before timeout., Test _time_until_retry() returns 0 when not OPEN., Test CircuitBreaker initialization with defaults. (+9 more)

### Community 862 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 863 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 864 - "PlayerChannelPreferences"
Cohesion: 0.20
Nodes (10): PlayerChannelPreferences, Player channel preferences model for Advanced Chat Channels. Stores player…, Test PlayerChannelPreferences can be instantiated with required fields., Test PlayerChannelPreferences has correct default values., Test PlayerChannelPreferences can have muted channels., Test PlayerChannelPreferences __repr__ method., test_player_channel_preferences_creation(), test_player_channel_preferences_defaults() (+2 more)

### Community 865 - "._attack_target_impl"
Cohesion: 0.20
Nodes (5): Resolve attack_damage from behavior config with robust typing., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target., Attack a specific target., Handle attacking target action.

### Community 866 - "_FakeMessageQueue"
Cohesion: 0.20
Nodes (3): _FakeMessageQueue, _FakeRateLimiter, _FakeRoomManager

### Community 867 - "test_metrics.py"
Cohesion: 0.20
Nodes (9): Unit tests for NATS Subject Manager Metrics. Tests the SubjectManagerMetrics…, Test record_validation() records failed validation., Test record_validation() records cache hit., Test record_validation() stores validation times., Test record_build() records failed build., test_record_build_failure(), test_record_validation_cache_hit(), test_record_validation_failure() (+1 more)

### Community 868 - "TestResolveExitTarget"
Cohesion: 0.20
Nodes (6): Room without a reverse exit is not considered bidirectional., If the target room ID does not exist, the helper returns None., If the target room lacks map coordinates, the helper returns None., Tests for _resolve_exit_target., Room with a reverse exit is treated as bidirectional and returns its…, TestResolveExitTarget

### Community 870 - "combat_messaging/base.py"
Cohesion: 0.05
Nodes (39): CombatMessagingBase, HasConnectionManager, log_room_broadcast_result(), Any, Base integration with connection manager resolution., Base for mixins that require connection_manager. Satisfies mypy attr-defined…, Log a room broadcast's outcome -- error-level on any failed delivery, debug-…, Base class with connection manager setup. Used by CombatMessagingIntegration. (+31 more)

### Community 871 - "RoomDataCache"
Cohesion: 0.05
Nodes (32): Manages room data caching and freshness validation., Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Clear room data cache. Args: room_id: Specific room ID to clear, or None to…, RoomDataCache, Unit tests for room data cache. Tests the RoomDataCache class for caching and…, Test clear_cache clears all rooms when room_id is None., Test clear_cache handles nonexistent room gracefully., Test get_cache_stats with empty cache. (+24 more)

### Community 872 - "test_check_no_production_assert.py"
Cohesion: 0.18
Nodes (15): _load_checker(), _NoProductionAssertModule, Path, Protocol, Tests for scripts/check_no_production_assert.py., Verify no-production-assert hook targets server code and excludes tests., Public surface of check_no_production_assert loaded via importlib., test_find_assert_line_numbers_detects_assert() (+7 more)

### Community 873 - "test_validate_codacy_coverage_gate.py"
Cohesion: 0.18
Nodes (15): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., `coverage xml --cov=server` writes `<source>server</source>` and lists…, An empty/malformed Cobertura report (no <class> elements at all) must still be… (+7 more)

### Community 874 - "optimized_sanitize_unicode_input"
Cohesion: 0.20
Nodes (10): Test sanitizing empty string., Test sanitizing normal text (no changes expected)., Test sanitizing text with Unicode issues., test_optimized_sanitize_unicode_input_empty(), test_optimized_sanitize_unicode_input_normal_text(), test_optimized_sanitize_unicode_input_unicode(), _cached_ftfy_fix(), optimized_sanitize_unicode_input() (+2 more)

### Community 875 - "pytest Best Practices"
Cohesion: 0.13
Nodes (15): 1.1 Project Layout, 1.2 Test File Naming, 1.3 Test Naming Conventions, 1. Code Organization & Structure, 2.1 Single Assert Per Test, 2.2 Fixtures for Setup/Teardown & Dependency Injection, 2.3 Parameterization, 2.4 Markers (+7 more)

### Community 876 - "Skill: Create a New Worktree for a Task"
Cohesion: 0.13
Nodes (15): Worktree Workflow Skill, Canonical Layout (Summary), MythosMUD Worktree Workflow, Preconditions and Safety, Skill: Clean Up a Completed or Stale Worktree, Skill: Create a New Worktree for a Task, Step 1 — Gather Task Metadata, Step 2 — Derive Names and Paths (+7 more)

### Community 877 - "TestHorizontalExitCharBetween"
Cohesion: 0.20
Nodes (6): Tests for _horizontal_exit_char_between (em dash, >, <)., Bidirectional horizontal exit between two rooms uses an em dash., One-way east exit renders as a greater-than sign., One-way west exit renders as a less-than sign., When there are no horizontal exits, the helper returns None., TestHorizontalExitCharBetween

### Community 878 - "MessageBatcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 879 - ".create_lie_command"
Cohesion: 0.20
Nodes (9): Test create_lie_command() creates LieCommand., Test create_lie_command() with 'down' modifier., Test create_lie_command() raises error with invalid args., Test create_lie_command() raises error with multiple args., test_create_lie_command(), test_create_lie_command_with_down(), test_create_lie_command_with_invalid_args(), test_create_lie_command_with_multiple_args() (+1 more)

### Community 880 - "server/tests/conftest.py"
Cohesion: 0.06
Nodes (43): Config, Item, Reset the configuration cache. In test mode, this is a no-op since get_config()…, reset_config(), _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables() (+35 more)

### Community 881 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)"
Cohesion: 0.13
Nodes (14): Communities (8 total, 5 thin omitted), Community 0 - "Baron Arthur von Kleist; Pyotr Shabelsky-Bork", Community 1 - "The Demon-Großmann; Demonic Mutation Table", Community 2 - "Erwin Kern; Manfred Freiherr von Killinger", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11) (+6 more)

### Community 882 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Anna Konrad; Lucas Reston", Community 2 - "Does Love Forgive", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12) (+6 more)

### Community 883 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Pre-Generated Investigators", Community 1 - "Pre-Generated Investigators (1)", Community 2 - "Pre-Generated Investigators (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12) (+6 more)

### Community 884 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 885 - "npc_schedules.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 886 - "PARALLEL EXECUTION RESULTS (2025-11-05)"
Cohesion: 0.13
Nodes (15): After Parallelization, Before Parallelization, Benefits, Changes Implemented, Comprehensive Tests (Serial + Long-Running), Daily Development Tests (Parallel), Excluded from Fast Suite, FINAL METRICS (+7 more)

### Community 887 - "fix_markdown_common_issues.py"
Cohesion: 0.22
Nodes (14): fix_emphasis_as_heading(), fix_first_line_heading(), fix_link_fragments(), fix_markdown_file(), generate_anchor(), main(), parse_markdownlint_output(), Path (+6 more)

### Community 888 - "process_room_files"
Cohesion: 0.21
Nodes (14): load_room_file(), main(), process_room_files(), Path, Load a room file safely., Save a room file safely., Convert room ID to lowercase., Convert filename to lowercase. (+6 more)

### Community 889 - "validate_codacy_coverage_gate.py"
Cohesion: 0.25
Nodes (14): cobertura_has_server_sources(), cobertura_root_line_rate(), lcov_aggregate_hits(), main(), _parse_cobertura_xml(), Path, Parse Cobertura XML with defusedxml (lazy import: LCOV-only runs skip this…, Return root line-rate from Cobertura XML (0.0--1.0). (+6 more)

### Community 890 - "fixture"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Create a mock prototype registry., Create a sample room drop item., Create a sample inventory item., Create a sample equipped item., sample_equipped_item(), sample_inventory_item() (+1 more)

### Community 891 - "._format_mute_entry"
Cohesion: 0.22
Nodes (5): datetime, Format mute duration text with remaining time or expiration status., Format a single mute entry for display., Format a section of mutes (personal or global) for display., Get comprehensive mute status for a player. Args: player_id: Player ID to get…

### Community 892 - ".connect_websocket"
Cohesion: 0.22
Nodes (5): WebSocket, Check if a WebSocket is open., Safely close a WebSocket connection., Connect a WebSocket for a player., Get connection ID from a WebSocket instance.

### Community 893 - "._get_vertical_exit_char"
Cohesion: 0.22
Nodes (6): _ExitRowContext, NamedTuple, Render a single row of vertical exits between room rows., Viewport and style context for vertical exit row rendering., Return the vertical exit character (|, v, or ^) given south/north exit state,…, Get exit character to display between rows for vertical (north/south) exits.…

### Community 894 - "Motion Design"
Cohesion: 0.25
Nodes (8): Duration: The 100/300/500 Rule, Easing: Pick the Right Curve, Motion Design, Perceived Performance, Performance, Reduced Motion, Staggered Animations, The Only Two Properties You Should Animate

### Community 895 - "Profession"
Cohesion: 0.03
Nodes (99): Profession, Any, Base, Check if given stats meet the profession requirements. Args: stats: Dictionary…, Check if profession is available for player selection., Get formatted text for displaying stat requirements. Returns: Formatted string…, Profession model for game data. Stores profession information including name,…, String representation of the profession. (+91 more)

### Community 896 - "mythos_dev.item_instances"
Cohesion: 0.36
Nodes (8): mythos_dev.add_item_to_container(), mythos_dev.container_contents, mythos_dev.containers, mythos_dev.get_container_contents_json(), mythos_dev.item_component_states, mythos_dev.item_instance_exists(), mythos_dev.item_instances, mythos_dev.item_prototypes

### Community 898 - "lock_state"
Cohesion: 0.25
Nodes (8): locked, sealed, unlocked, default, description, enum, type, lock_state

### Community 899 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 900 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from…, Unit tests for connection utils. Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 901 - "is_safe_filename"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters). Args:…, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 902 - "test_containers_procedures.py"
Cohesion: 0.23
Nodes (14): container_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/containers.sql's update_container() return-…, Create one container row. Yields its container_instance_id. (+6 more)

### Community 903 - "test_players_procedures.py"
Cohesion: 0.23
Nodes (21): invite_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/players.sql's #633/#733 additions:…, A caller that captures twice for the same code (skipping a fresh reserve) gets… (+13 more)

### Community 904 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 906 - "test_event_publisher_helpers.py"
Cohesion: 0.14
Nodes (14): event_publisher(), mock_nats_service(), fixture, Unit tests for event publisher helper functions. Tests the helper functions in…, Create a mock NATS service., Create an EventPublisher instance., Test _create_event_message() creates event message., Test get_next_sequence_number() increments sequence. (+6 more)

### Community 907 - "properties"
Cohesion: 0.18
Nodes (11): description, type, description, type, description, minimum, type, combat_modifier (+3 more)

### Community 908 - "check_no_production_assert.py"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 909 - "Generate Comprehensive Report"
Cohesion: 0.14
Nodes (14): Audit Skill, Anti-Patterns Verdict, Critical Issues, Detailed Findings by Severity, Diagnostic Scan, Executive Summary, Generate Comprehensive Report, High-Severity Issues (+6 more)

### Community 910 - "Interaction Design"
Cohesion: 0.17
Nodes (12): Destructive Actions: Undo > Confirm, Focus Rings: Do Them Right, Form Design: The Non-Obvious, Gesture Discoverability, Interaction Design, Keyboard Navigation Patterns, Loading States, Modals: The Inert Approach (+4 more)

### Community 911 - "Spatial Design"
Cohesion: 0.14
Nodes (14): Cards Are Not Required, Container Queries, Depth & Elevation, Grid Systems, Hierarchy Through Multiple Dimensions, Name Tokens Semantically, Optical Adjustments, Spacing Systems (+6 more)

### Community 912 - "Typography"
Cohesion: 0.14
Nodes (14): Accessibility Considerations, Choosing Distinctive Fonts, Classic Typography Principles, Fluid Type, Font Selection & Pairing, Modern Web Typography, Modular Scale & Hierarchy, OpenType Features (+6 more)

### Community 913 - "Fix patterns by tier"
Cohesion: 0.13
Nodes (13): 🔴 Critical — import and name errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — type errors, 🔵 Low — type precision, 🟢 Medium — type refinement, Mypy Remediation — Reference (+5 more)

### Community 914 - "Optimize Skill"
Cohesion: 0.14
Nodes (14): Optimize Skill, Animation Performance, Assess Performance Issues, Core Web Vitals Optimization, Cumulative Layout Shift (CLS < 0.1), First Input Delay (FID < 100ms) / INP (< 200ms), Largest Contentful Paint (LCP < 2.5s), Loading Performance (+6 more)

### Community 915 - "Semgrep Configuration"
Cohesion: 0.14
Nodes (14): Semgrep Configuration, Java Jackson Deserialization Rule, Java JMS Deserialization Rule, Java Path Traversal Rule, Java Unvalidated Redirect Rule, Java Weak SSL Context Rule, Java XPath Injection Rule, Java XSS Response Writer Rule (+6 more)

### Community 916 - "Test Server Remediation Prompt - Cursor Executable Version"
Cohesion: 0.14
Nodes (13): Best Practices, COMPLETION VERIFICATION, CRITICAL "DO NOT" INSTRUCTIONS, CRITICAL: EXECUTION REQUIREMENTS, DECISION TREE - START HERE, ERROR HANDLING PROTOCOL, MANDATORY PROGRESS TRACKING, MANDATORY VERIFICATION CHECKPOINTS (+5 more)

### Community 917 - "Arkham City (MOTD Zone)"
Cohesion: 0.18
Nodes (14): Arkham City Graph PNG, Arkham City PDF Map, Arkham City (MOTD Zone), Welcome to the Dreamlands, Innsmouth (MOTD Zone), Katmandu, MythosMUD Message of the Day, The Yellow Sign (+6 more)

### Community 918 - "INDEX.md"
Cohesion: 0.16
Nodes (10): P6 · Review Queue (rebuilt), TRACK A · Code defects — not review material, TRACK B · Bulk confirmation, Documentation edits, Issues to reopen — **C7**, New ADRs (next free numbers, index updated in `decisions/README.md`), P8 · Action plan, Remediation plans to draft (not execute) (+2 more)

### Community 919 - "Claims by cluster"
Cohesion: 0.08
Nodes (21): Claims by cluster, config-api — API_OPENAPI_SPECIFICATION, container-di — BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES, container-di — CONTAINER_SYSTEM_ARCHITECTURE, Corpus correction, Design↔design contradictions (findings without needing code), domain — aggro-threat-system, events-nats — EVENT_OWNERSHIP_MATRIX, DISTRIBUTED_EVENTBUS_NATS, NATS_SUBJECT_PATTERNS (+13 more)

### Community 920 - "P4 · Intent Sweep — Core Feature Issues"
Cohesion: 0.13
Nodes (14): #17 · Party — one of three bullets built, #21 · Admin commands — "ban" was in the issue title and never built, #29 · Cultist faction and PvP — zero implementation, #30 · Branching quests and morality — two of three bullets absent, #62 · Tick-rate validation — not built, #9 · The xterm.js substitution — real, user-facing, unrecorded, CLOSED BUT NOT BUILT, Conforming, worth recording (+6 more)

### Community 921 - "P3 · Findings Verified Directly"
Cohesion: 0.14
Nodes (12): F-D3 · Inbound links to archived documents — DEVIATED (7 instances, one root cause), F-D5 · The DI system's architecture doc is archived, not live — DEVIATED, F-D6 · `docs/DEVELOPMENT_AI.md` is not valid text — DEVIATED, F-V1 · Sync PersistenceLayer removal — CONFORMS (reverses a P0 row), F-V2 · sqlite3 imports survive in migration scripts — STALE, P3 · Findings Verified Directly, A · Hard-coded metrics in documents, B · Migration scaffolding that outlived its migration (+4 more)

### Community 922 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (16 total, 14 thin omitted), Community 0 - "Open Mind Circle", Community 1 - "Campaign Materials", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 923 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (6 total, 4 thin omitted), Community 0 - "Solo Investigators", Community 1 - "Design & Authorship", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 924 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (4 total, 1 thin omitted), Community 0 - "Keeper Screen References", Community 1 - "Keeper Screen References (1)", Community 2 - "Keeper Screen References (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12) (+5 more)

### Community 925 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (3 total, 0 thin omitted), Community 0 - "Call of Cthulhu Stat Block; Chaosium Inc.", Community 1 - "Mythos Elements", Community 2 - "Mythos Elements (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12) (+5 more)

### Community 926 - "Migration 019 Verification Report"
Cohesion: 0.14
Nodes (14): Before Production Deployment, Conclusion, Documentation (3 files), Files Modified Summary, Low Risk ✅, Medium Risk ⚠️, Migration 019 Verification Report, Migration Scripts (1 file) (+6 more)

### Community 927 - "NATS Anti-Patterns Remediation Summary"
Cohesion: 0.14
Nodes (14): After Remediation, Backward Compatibility, Before Remediation, Code Quality Improvements, Configuration Options, Exception Hierarchy, Executive Summary, Impact Assessment (+6 more)

### Community 928 - "analyze_log_file"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 929 - "find_fstring_logging_violations"
Cohesion: 0.20
Nodes (11): find_fstring_logging_violations(), format_violation_report(), FStringLoggingDetector, main(), Call, Path, Main function to scan files and report violations., AST visitor to detect f-string logging violations. (+3 more)

### Community 930 - "check_pr_issue_references.py"
Cohesion: 0.20
Nodes (13): _extract_numbers(), find_bare_references(), _format_message(), get_open_issue_numbers(), main(), Warn when a PR references an open issue without a GitHub closing keyword. This…, Return issue numbers referenced in text that are NOT preceded by a closing…, Return every #NNN issue number appearing in text, as an int set. (+5 more)

### Community 931 - "lint_sql_guardrails.py"
Cohesion: 0.23
Nodes (13): check_not_in_subquery(), check_select_star(), _collect_sql_files(), main(), Path, Lightweight guardrails for hand-maintained PostgreSQL SQL. Warns on: - select *…, Return line with line comment removed (-- ...)., Return content with block comments /* ... */ removed (simple, no nested). (+5 more)

### Community 932 - "CacheService"
Cohesion: 0.21
Nodes (5): CacheService, Main cache service that coordinates all caching operations. This service…, Initialize the cache service. Args: persistence: Persistence layer instance…, Preload frequently accessed data into caches. This method loads commonly used…, TestCacheService

### Community 933 - "ChatPoseManager"
Cohesion: 0.18
Nodes (8): ChatPoseManager, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…, Get a player's current pose. Args: player_id: ID of the player Returns: Current…, Clear a player's pose. Args: player_id: ID of the player Returns: True if pose…, Get all poses (for testing/debugging). Returns: Dictionary mapping player IDs…

### Community 934 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 935 - "FRD & Plan-Document Verification Register — 2026-08"
Cohesion: 0.12
Nodes (17): 1. Purpose, 2.1 In corpus (17), 2.2 Candidates considered, excluded (delta, with reasons), 2. FRD corpus — reconstructed and enumerated, 3.1 Findings confirmed, refuted, or superseded since the original pass, 3.2 New verification — previously unrecorded, 3.3 Unverifiable — genuinely, with citation, 3. Claim verification (FRD sweep, re-run) (+9 more)

### Community 936 - "mp_regeneration_service"
Cohesion: 0.22
Nodes (9): mock_player(), mock_player_service(), mp_regeneration_service(), fixture, Create a mock player service., Create an MPRegenerationService instance., Create a sample player ID., Create a mock player. (+1 more)

### Community 937 - "normalize_path_from_url_or_path"
Cohesion: 0.25
Nodes (6): Path, Return and cache the repository root directory., Delegate to shared util. Kept for backward compatibility., normalize_path_from_url_or_path(), Path, Normalize an item database override into a filesystem path. DEPRECATED: Items…

### Community 938 - "test_profession_service.py"
Cohesion: 0.25
Nodes (13): persistence(), _profession(), asyncio, fixture, Unit tests for ProfessionService., service(), test_get_all_professions_dict(), test_get_profession_by_id_dict_found() (+5 more)

### Community 939 - "test_ascii_map_renderer_exits.py"
Cohesion: 0.22
Nodes (7): fixture, Unit tests for AsciiMapRenderer exit character and exit resolution. Guards…, Viewport bounds: return None when next cell is outside viewport., Returns None when the next horizontal cell lies at or beyond the viewport's…, Return a fresh AsciiMapRenderer instance for each test., renderer(), TestGetHorizontalExitCharViewportBounds

### Community 940 - "._get_npc_display_name"
Cohesion: 0.25
Nodes (4): Resolve NPC instance display name from lifecycle manager, or derive from npc_id., Best-effort lookup of NPC name from the lifecycle manager., Resolve the NPC lifecycle manager from the app state, if available., Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->…

### Community 941 - "test_persistence_container_persistence.py"
Cohesion: 0.14
Nodes (13): Unit tests for persistence.container_persistence module. This module tests the…, Test parsing None JSONB column., Test parsing string JSONB column., Test parsing dict JSONB column., Test parsing empty string JSONB column., Test parsing list JSONB column., Test parsing invalid JSON string., test_parse_jsonb_column_dict() (+5 more)

### Community 942 - "UnknownChannelStrategy"
Cohesion: 0.25
Nodes (6): Strategy for unknown channel types., Initialize unknown channel strategy. Args: channel_type: Unknown channel type, Get strategy for channel type. Args: channel_type: Type of channel to get…, UnknownChannelStrategy, Test UnknownChannelStrategy.broadcast() handles unknown channel., test_unknown_channel_strategy_broadcast()

### Community 943 - "test_holiday_service.py"
Cohesion: 0.11
Nodes (14): _holiday_entry_from_row(), _HolidayLoadResult, Record, TypedDict, Async helper to load holidays from PostgreSQL database., Normalize nullable PostgreSQL array columns to string values., Build a HolidayEntry from a calendar_holidays row., _string_list_from_row() (+6 more)

### Community 944 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 945 - "SystemAdminChannelStrategy"
Cohesion: 0.25
Nodes (7): Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy. Args: channel_type: Type of…, SystemAdminChannelStrategy, Test SystemAdminChannelStrategy.broadcast() broadcasts globally., Personal system messages deliver to target_player_id only., test_system_admin_channel_strategy_broadcast(), test_system_admin_channel_strategy_personal_target()

### Community 946 - "test_command_factories.py"
Cohesion: 0.02
Nodes (90): factory(), fixture, Unit tests for command factories. Tests the CommandFactory class., Test create_channel_command delegates to communication factory., Test create_go_command delegates to exploration factory., Test create_stand_command delegates to exploration factory., Test create_lie_command delegates to exploration factory., Test create_ground_command delegates to exploration factory. (+82 more)

### Community 947 - "TestValidatorIntegration"
Cohesion: 0.14
Nodes (8): Integration tests for the main validator., Test validator with valid room files., Test validator with invalid room files., Test validator JSON output format., Test validator zone filtering., Test that help text is properly displayed., Test schema-only validation flag., TestValidatorIntegration

### Community 948 - "Improve Layout Systematically"
Cohesion: 0.15
Nodes (13): Arrange Skill, Assess Current Layout, Break Card Grid Monotony, Choose the Right Layout Tool, Create Visual Rhythm, Establish a Spacing System, Improve Layout Systematically, Manage Depth & Elevation (+5 more)

### Community 949 - "Distill Skill"
Cohesion: 0.15
Nodes (13): Distill Skill, Assess Current State, Code Simplification, Content Simplification, Document Removed Complexity, Information Architecture, Interaction Simplification, Layout Simplification (+5 more)

### Community 950 - "RoomBasedChannelStrategy"
Cohesion: 0.25
Nodes (7): Strategy for room-based channels (say, local, emote, pose)., Initialize room-based channel strategy. Args: channel_type: Type of room-based…, RoomBasedChannelStrategy, Test RoomBasedChannelStrategy.broadcast() broadcasts to room., Test RoomBasedChannelStrategy.broadcast() handles missing room_id., test_room_based_channel_strategy_broadcast(), test_room_based_channel_strategy_broadcast_no_room_id()

### Community 951 - "handle_time_command"
Cohesion: 0.20
Nodes (15): handle_time_command(), Any, Handle the time command, exposing the current Mythos time and active holidays., asyncio, Unit tests for time command handlers. Tests the time command functionality., Test handle_time_command() handles holiday service errors., Test handle_time_command() handles missing holiday service., Test handle_time_command() returns time information. (+7 more)

### Community 953 - "Any"
Cohesion: 0.11
Nodes (14): Return the live NPC combat integration service for delegation. Prefer…, _resolve_npc_combat_service_raw(), Any, WebSocket, Get a handler for the specified message type. Args: message_type: The message…, Handle a WebSocket message using the appropriate handler. Args: websocket: The…, Handle a specific message type. Args: websocket: The WebSocket connection…, Handle command message type. (+6 more)

### Community 954 - "Mypy Remediation"
Cohesion: 0.15
Nodes (12): 🔴 Critical — import and name errors, Debugging when a fix doesn't take, Entry point, Error code table, Fix patterns by tier, Fix-verify loop, 🟡 High — type errors, 🔵 Low — type precision (+4 more)

### Community 955 - "P4 · Intent Sweep — FRD/SPEC Documents"
Cohesion: 0.15
Nodes (12): Correction to the core-issues sweep — verified directly, Corroborations from a second source, Deliberately superseded — and one of them is more interesting than a blanket ruling, HIGH · Phantom hostiles spawn but cannot be fought, HIGH · Reversed compass directions — never implemented, with a trap, MEDIUM · Admin teleport audit trail uses the wrong mechanism, MEDIUM · Room `environment` enum has drifted in production data, New undocumented items (+4 more)

### Community 956 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)"
Cohesion: 0.15
Nodes (12): Communities (4 total, 2 thin omitted), Community 0 - "Kingsport Setting", Community 1 - "Solo Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11), Hyperedges (group relationships) (+4 more)

### Community 957 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (3 total, 1 thin omitted), Community 0 - "Scenario Design", Community 1 - "Call of Cthulhu Roleplaying Game; Keeper Tips: C", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12), Hyperedges (group relationships) (+4 more)

### Community 958 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (17 total, 16 thin omitted), Community 0 - "Scenario Handouts", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12), Hyperedges (group relationships), Import Cycles (+4 more)

### Community 959 - "required"
Cohesion: 0.17
Nodes (12): $defs, scheduleEntry, applies_to, category, days, end_hour, id, name (+4 more)

### Community 960 - "ADR-018: New Game Session vs Grace Reconnect"
Cohesion: 0.15
Nodes (12): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. References, 8. Changelog (+4 more)

### Community 961 - "Technical Implementation"
Cohesion: 0.22
Nodes (9): 2. Message Routing Logic, 3. State Management, 4. Event Handling, Command Routing Logic, Current Logic (in CommandPanel), New Logic Distribution, New State Structure, State Distribution (+1 more)

### Community 962 - "Critical Issues"
Cohesion: 0.15
Nodes (13): 1. Entry Point Anti-Pattern: `asyncio.run()` Usage, 3.1 `asyncio.create_task()` Usage, 3.2 `asyncio.gather()` Usage, 3. Task Management Anti-Patterns, 4. Missing Explicit Dependency, 5.1 Uvicorn Integration, 5.2 Test Files, 5.3 Event Bus Queue Migration (+5 more)

### Community 963 - "Easy Coverage Wins - Quick Analysis"
Cohesion: 0.15
Nodes (13): Easy Coverage Wins - Quick Analysis, 🚀 Next Steps, Phase 1: Quick Wins (Tier 1 + Tier 2) ✅ COMPLETED, Phase 2: Medium Effort (Tier 3) ✅ COMPLETED, Phase 3: New Small Files (Tier 4) ✅ COMPLETED, Phase 4: Additional Realtime Files 🔄 IN PROGRESS, 📊 Recommended Priority Order, 🎉 Summary (+5 more)

### Community 964 - "Entries"
Cohesion: 0.15
Nodes (11): Codacy High/Critical Baseline – MythosMUD, Distribution notes, Example issue types, Summary (from Codacy UI snapshot), Top code patterns by issue count, 2026-02-24 — Wave 3 (Backend security) completed, 2026-02-24 — Wave 4 (Frontend security) verified, 2026-02-24 — Wave 5 (Complexity refactors) (+3 more)

### Community 965 - "Unique Pylint Findings Analysis"
Cohesion: 0.15
Nodes (13): Linting Complexity Alignment, 2.1 No Name in Module (E0611), 2. ERROR Findings (33 findings), 4.1 Unused Variable (W0612), 4.2 Unused Argument (W0613), 4. WARNINGS Findings (5 findings), Configure Ruff to Catch (Small subset), Executive Summary (+5 more)

### Community 966 - "Execution Timeline"
Cohesion: 0.15
Nodes (13): Execution Timeline, Month 1: Pruning Phase, Month 2: Consolidation + Gap Filling, Month 3+: Continuous Improvement, Ongoing Tasks, Week 1: Quick Wins, Week 2: Infrastructure Reduction, Week 3: Coverage Test Optimization (+5 more)

### Community 967 - "._create_tracked_task"
Cohesion: 0.07
Nodes (15): BaseException, Task, Async handler for NATS reconnection events., Check if connection attempt is allowed by state machine., Set up connection event handlers., Connect to NATS server with state machine tracking. Returns: True if connection…, Start periodic health check monitoring task., Periodic health check loop using ping/pong. (+7 more)

### Community 968 - "main"
Cohesion: 0.22
Nodes (12): analyze_connectivity(), generate_dot_file(), load_room_data(), main(), print_detailed_statistics(), print_room_listing(), Print a detailed listing of all rooms by subzone., Load all room and intersection data from the zone directory. (+4 more)

### Community 969 - "fix_markdown_code_block_style.py"
Cohesion: 0.24
Nodes (12): detect_code_language(), fix_code_block_style(), fix_markdown_file(), is_indented_code_line(), main(), parse_markdownlint_output(), Path, Parse markdownlint output to get files with MD046 issues. (+4 more)

### Community 970 - "main"
Cohesion: 0.22
Nodes (12): fix_md001_heading_increment(), fix_md013_line_length(), fix_md041_first_line_heading(), fix_md051_link_fragments(), main(), parse_errors(), Fix MD001: Heading levels should only increment by one level at a time., Parse markdownlint output file and extract errors. (+4 more)

### Community 971 - "SyntaxErrorFixer"
Cohesion: 0.22
Nodes (8): main(), Path, Process multiple files and return statistics., Main function to run the syntax error fixer., Tool to fix syntax errors introduced by automated f-string remediation., Fix malformed logger calls with broken syntax., Fix syntax errors in a specific file., SyntaxErrorFixer

### Community 972 - "generate_openapi_spec.py"
Cohesion: 0.22
Nodes (12): main(), Rewrite the generated tag table between its markers in the spec doc., Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., Tags actually declared by routes, in first-seen order. This is the authority., name -> description, from the spec's top-level tags block (OPENAPI_TAGS)., Build the markdown table, failing loudly if a route tag has no description., _render_tag_table() (+4 more)

### Community 973 - "safe_run"
Cohesion: 0.13
Nodes (25): main(), Run a psql command and return the result., Load all seed data files., run_psql_command(), _argv_char_len(), _build_guard_command(), _changed_files_between(), _git_executable() (+17 more)

### Community 974 - "test_follow_flow.py"
Cohesion: 0.17
Nodes (15): connection_manager(), event_bus(), follow_service(), movement_service(), asyncio, fixture, Integration tests for follow feature. Flow: Player A requests follow B; B…, Real EventBus for integration. (+7 more)

### Community 975 - "test_look_npc.py"
Cohesion: 0.02
Nodes (165): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_description(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result() (+157 more)

### Community 976 - "._load_player_mutes_from_data"
Cohesion: 0.29
Nodes (4): Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory., Load global mutes from JSON data into memory.

### Community 977 - "TestGetContainer"
Cohesion: 0.25
Nodes (5): Tests for get_container dependency function., Test get_container returns container when present., Test get_container raises RuntimeError when container not in app.state., Test get_container raises RuntimeError when app.state doesn't exist., TestGetContainer

### Community 979 - ".create_go_command"
Cohesion: 0.25
Nodes (7): Test create_go_command() creates GoCommand., Test create_go_command() raises error with no args., Test create_go_command() raises error with invalid direction., test_create_go_command(), test_create_go_command_invalid_direction(), test_create_go_command_no_args(), Create GoCommand from arguments.

### Community 980 - "optimized_comprehensive_sanitize_input"
Cohesion: 0.25
Nodes (8): Test comprehensive sanitization of empty string., Test comprehensive sanitization of normal text., Test that optimized comprehensive sanitization normalizes newlines to spaces., test_optimized_comprehensive_sanitize_input_empty(), test_optimized_comprehensive_sanitize_input_normal(), test_optimized_comprehensive_sanitize_input_normalizes_newlines(), optimized_comprehensive_sanitize_input(), Optimized comprehensive input sanitization. Args: text: Raw input text to…

### Community 981 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 982 - "properties"
Cohesion: 0.29
Nodes (7): description, type, properties, environment, zone_type, description, type

### Community 983 - "verify_npc_occupants.py"
Cohesion: 0.23
Nodes (12): _check_service_availability(), _collect_npcs_by_room(), _print_summary(), Any, Verification script to check NPCs in lifecycle manager and test occupant query…, Print verification summary. Args: npc_count: Total number of active NPCs…, Verify NPCs exist in lifecycle manager and test query logic., Check if NPC service, lifecycle manager, and active_npcs are available.… (+4 more)

### Community 984 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test _execute_command_handler successfully executes handler., Test process_command successfully processes command string., Test _execute_command_handler handles handler returning non-dict., Test process_validated_command successfully routes to handler., Test process_validated_command handles unknown command type., Test process_validated_command handles handler errors., Test process_validated_command handles logging errors gracefully. (+7 more)

### Community 985 - "test_async_persistence_room_cache.py"
Cohesion: 0.14
Nodes (13): Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test _generate_room_id_from_zone_data with None values., Test _parse_exits_json with invalid JSON string., Test _process_exits_for_room processes exits with direction., Test _process_exits_for_room skips exits without direction., Test _process_combined_rows processes rows with exits JSON., Test _process_exit_rows handles missing direction., test_generate_room_id_from_zone_data_none_values() (+5 more)

### Community 986 - ".create_ground_command"
Cohesion: 0.25
Nodes (7): Test create_ground_command() creates GroundCommand., Test create_ground_command() raises error with no args., Test create_ground_command() raises error with empty target., test_create_ground_command(), test_create_ground_command_empty_target(), test_create_ground_command_no_args(), Create GroundCommand from arguments.

### Community 987 - "test_player_event_handlers_utils.py"
Cohesion: 0.02
Nodes (91): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), asyncio, fixture, Unit tests for player event handler utilities. Tests the…, Test get_player_info() returns None for invalid player_id. (+83 more)

### Community 988 - "test_room_subscription_manager.py"
Cohesion: 0.04
Nodes (53): asyncio, fixture, Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test add_room_occupant() adds occupant., Test add_room_occupant() with multiple occupants., Test add_room_occupant() adds occupant to new room. (+45 more)

### Community 989 - "test_run_test_ci.py"
Cohesion: 0.15
Nodes (16): Regression tests for scripts/run_test_ci.py's coverage-combine sequence and the…, Run 1 (the main suite) must write to a COVERAGE_FILE distinct from the bare…, Run 1's safe_run_static call must pass env=env_unit, not the base env (which…, The `coverage combine` call's two data-file arguments must be coverage_unit and…, ci.yml's 'Check for excessive warnings' step re-runs the suite under -n auto;…, ci.yml's 'Run tests with coverage' step pipes through `tee`; without pipefail…, Run 1 must pass -n 0, overriding server/pytest.ini's default -n auto. pytest-…, ci.yml's 'Check for excessive warnings' step is CI-gating (a real crash now… (+8 more)

### Community 990 - ".create_follow_command"
Cohesion: 0.25
Nodes (7): Test create_follow_command() creates FollowCommand with target., Test create_follow_command() raises error with no args., Test create_follow_command() raises error with empty target., test_create_follow_command(), test_create_follow_command_empty_target(), test_create_follow_command_no_args(), Create FollowCommand from arguments.

### Community 991 - "test_room_environment_parity.py"
Cohesion: 0.19
Nodes (12): _environment_enum_from_schema(), _environment_options_from_room_edit_modal(), Path, Parity test for the room environment enum (#623). Guards against the exact…, Return the `environment` property's `enum` values from a room JSON schema., Return the non-empty `value`s of RoomEditModal.tsx's ENVIRONMENT_OPTIONS…, room_hierarchy_schema.json's environment enum must equal ROOM_ENVIRONMENTS., unified_room_schema.json's environment enum must equal ROOM_ENVIRONMENTS. (+4 more)

### Community 992 - "ScheduleEntry"
Cohesion: 0.08
Nodes (18): Record the schedule categories currently active for NPC routines., Any, field_validator, Single schedule block describing routine availability…, Validate schedule entry days are standard English weekday names (Sunday,…, Validate slug-formatted list entries. Args: value: Sequence of strings to…, Ensure the schedule window moves time forward like the Chronology Tablets…, Validate tradition value. Args: value: The tradition string to validate… (+10 more)

### Community 993 - "Commands"
Cohesion: 0.17
Nodes (12): Add a branch — `gh stack add`, Check out a stack — `gh stack checkout`, Commands, Initialize a stack — `gh stack init`, Link branches as a stack (no local tracking) — `gh stack link`, Navigate the stack, Push branches to remote — `gh stack push`, Rebase the stack — `gh stack rebase` (+4 more)

### Community 994 - "Docker Best Practices"
Cohesion: 0.17
Nodes (11): 10. Manage Secrets Securely with Docker Compose, 1. Optimize for Multi-Stage Builds, 2. Choose Minimal, Trusted Base Images, 3. Leverage `.dockerignore`, 4. Optimize Layer Caching, 5. Run as a Non-Root User, 6. Distinguish `ARG` and `ENV`, 7. Implement Health Checks (+3 more)

### Community 995 - "Zustand Best Practices"
Cohesion: 0.17
Nodes (11): 1. Typed Store Shape (TypeScript First), 2. Slice-Based Organization, 3. Naming Conventions, 4. Functional Updates to Prevent Stale Closures, 5. Selectors and Shallow Comparison for Performance, 6. Essential Middleware Usage, 7. Initializing Stores Outside Components, 8. Asynchronous Actions (+3 more)

### Community 996 - "Amplify the Design"
Cohesion: 0.17
Nodes (12): Bolder Skill, Amplify the Design, Assess Current State, Color Intensification, Composition Boldness, MANDATORY PREPARATION, Motion & Animation, Plan Amplification (+4 more)

### Community 997 - "Hardening Dimensions"
Cohesion: 0.17
Nodes (12): Harden Skill, Accessibility Resilience, Assess Hardening Needs, Edge Cases & Boundary Conditions, Error Handling, Hardening Dimensions, Input Validation & Sanitization, Internationalization (i18n) (+4 more)

### Community 998 - "MythosMUD LLM Wiki (Obsidian)"
Cohesion: 0.17
Nodes (12): LLM Wiki Skill, Chaosium ingest, Division of labor, Graphify sync, Ingest, Lint, MythosMUD LLM Wiki (Obsidian), Non-goals (+4 more)

### Community 999 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 1000 - "PanelContextRuntime.tsx"
Cohesion: 0.21
Nodes (9): defaultPanels, PanelContext, PanelContextType, PanelLayout, PanelPosition, PanelProvider(), PanelProviderProps, PanelSize (+1 more)

### Community 1001 - "Lint Remediation"
Cohesion: 0.17
Nodes (11): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Entry point, Error code table, Fix patterns by tier, Fix-verify loop, 🟡 High — code quality, Lint Remediation (+3 more)

### Community 1002 - "mcp.json"
Cohesion: 0.20
Nodes (11): codacy, context7, jcodemunch, playwright, JCODEMUNCH_MAX_FOLDER_FILES, npx, uvx, @codacy/codacy-mcp (+3 more)

### Community 1003 - "TRACK C · The interactive review — 8 decisions"
Cohesion: 0.17
Nodes (12): C1 · What are the ADRs *for*?, C2 · Who owns query construction?, C3 · Layer boundaries: enforce or amend?, C4 · Is `APPLICATION_CONTAINER_ANALYSIS.md` restored or left archived?, C5 · Four doc↔doc contradictions, C6 · Contract drift from one unrecorded decision, C7 · Closed-but-not-built — six features, C8 · Undocumented systems worth an ADR (+4 more)

### Community 1004 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)"
Cohesion: 0.17
Nodes (11): Communities (2 total, 1 thin omitted), Community 0 - "Expedition Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 1005 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (3 total, 2 thin omitted), Community 0 - "Player Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 1006 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (8 total, 7 thin omitted), Community 0 - "Character Sheets", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 1007 - "bonus_tags"
Cohesion: 0.33
Nodes (6): items, type, uniqueItems, minLength, type, bonus_tags

### Community 1008 - "Complexity Checking Alignment: Ruff C901 vs Pylint"
Cohesion: 0.17
Nodes (12): 1. Use Ruff for Cyclomatic Complexity ✅, 2. Suppress Pylint Complexity Metrics ✅, 3. Align Inline Suppressions, Complexity Checking Alignment: Ruff C901 vs Pylint, Conclusion, Current State Analysis, Example Comparison, Executive Summary (+4 more)

### Community 1009 - "What They Measure"
Cohesion: 0.17
Nodes (12): Configuration, Example, Pylint Complexity Metrics (R0911-R0915), R0911: Too Many Return Statements, R0912: Too Many Branches, R0913: Too Many Arguments, R0914: Too Many Local Variables, R0915: Too Many Statements (+4 more)

### Community 1010 - "Migration Guide: From Default Logging to Enhanced Logging"
Cohesion: 0.17
Nodes (12): 1. Update Import Statements, 2. Migrate Context Parameters, 3. Convert String Formatting to Structured Logging, 4. Add Rich Context to Error Messages, Issue 1: ImportError when using enhanced logging, Issue 2: TypeError with context parameter, Issue 3: Logs not appearing in files, Issue 4: Sensitive data appearing in logs (+4 more)

### Community 1011 - "Enhanced Logging Quick Reference"
Cohesion: 0.17
Nodes (12): Clear Context, Context Binding, 🚨 CRITICAL: DO NOT USE, Enhanced Logging Quick Reference, For complete documentation, see [ENHANCED_LOGGING_GUIDE.md](ENHANCED_LOGGING_GUIDE.md), Log Levels, ✅ MANDATORY: ALWAYS USE, One-page cheat sheet for MythosMUD enhanced logging patterns (+4 more)

### Community 1012 - "PERSISTENCE_REFACTORING_COMPLETE.md"
Cohesion: 0.18
Nodes (9): Persistence Async Migration Plan, Gradual File-by-File Async Migration, HealthRepository, Implementation Pattern, PersistenceLayer Sync Facade, PlayerRepository, Sync-to-Async Delegation, Seven Async Repositories (+1 more)

### Community 1013 - "Migration Roadmap"
Cohesion: 0.17
Nodes (12): Files to Migrate (11 total), Files to Migrate (2 total), Files to Migrate (6 total), Game Systems (3 files), Migration Roadmap, NPC Systems (7 files), Phase 2: API Endpoints (Priority 1) 🎯, Phase 3: Real-Time Handlers (Priority 2) 🚀 (+4 more)

### Community 1014 - "Critical Insights"
Cohesion: 0.17
Nodes (12): 1. Infrastructure Tests are the Main Optimization Target, 2. Regression Tests are 100% High-Value, 3. Coverage Tests Written for Metrics, Not Quality, 4. No Parametrized Tests (Major Opportunity), 5. Critical Gaps in New Architecture, Critical Insights, Example, Example Low-Value Test (+4 more)

### Community 1015 - "Multi-Character Support System"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1016 - "enum"
Cohesion: 0.25
Nodes (8): Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, enum

### Community 1017 - "_collect_python_public_defs_and_tiny"
Cohesion: 0.23
Nodes (12): _check_exports_and_tiny_functions(), _collect_python_public_defs_and_tiny(), _is_public_function_stmt(), _is_test_file_path(), _is_tiny_single_use(), AST, AsyncFunctionDef, FunctionDef (+4 more)

### Community 1018 - "infrastructure/conftest.py"
Cohesion: 0.33
Nodes (6): async_persistence_layer(), mock_event_bus(), fixture, Shared fixtures for unit tests in the infrastructure package., Create a mock event bus., Create an AsyncPersistenceLayer instance with skipped room cache.

### Community 1019 - "lint_container_get_instance.py"
Cohesion: 0.21
Nodes (11): AllowlistEntry, _collect_python_files(), _find_get_instance_lines(), main(), Path, Guard against new `ApplicationContainer.get_instance()` service-location debt…, Return 1-based line numbers of real `ApplicationContainer.get_instance()`…, Scan server/ for ApplicationContainer.get_instance() calls. Returns… (+3 more)

### Community 1020 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 1021 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1022 - "test_command_service.py"
Cohesion: 0.14
Nodes (13): Unit tests for command service. Tests the CommandService class which handles…, Test _prepare_command_data creates basic command_data dict., Test _extract_parsed_fields extracts basic fields., Test _extract_parsed_fields handles missing attributes gracefully., Test register_command_handler adds new handler., Test register_command_handler overwrites existing handler., Test _log_model_dump_result logs model dump., test_extract_parsed_fields_basic() (+5 more)

### Community 1023 - "inventory_unequip_command.py"
Cohesion: 0.11
Nodes (35): handle_wearable_container_on_unequip(), Player, Handle wearable container preservation when unequipping a container item., _ensure_shared_services_initialized(), get_shared_services(), Shared service initialization for inventory commands., Clear lazy singletons so each test gets a fresh init path. For unit tests only;…, Resolve async_persistence from the request and construct shared singletons. (+27 more)

### Community 1024 - "test_combat_grace_period.py"
Cohesion: 0.14
Nodes (17): mock_connection_manager(), mock_persistence(), mock_request(), asyncio, fixture, Unit tests for combat command blocking during login grace period. Tests that…, Test that attack commands work when player is not in grace period., Attack command returns incapacitated message when player has 0 to -9 DP (prone,… (+9 more)

### Community 1025 - "SkillUseLog"
Cohesion: 0.21
Nodes (10): Base, One recorded successful use of a skill by a character at a given level.…, SkillUseLog, Unit tests for SkillUseLog ORM model., SkillUseLog can be instantiated with required fields., SkillUseLog maps to the expected table., SkillUseLog __repr__ includes key identifiers., test_skill_use_log_creation() (+2 more)

### Community 1026 - "fixture"
Cohesion: 0.29
Nodes (7): fixture, Typed mock for RateLimiter.remove_player_data., Typed mock for MessageQueue.remove_player_messages., Typed mock for room_manager.remove_player_from_all_rooms., remove_player_data_mock(), remove_player_from_all_rooms_mock(), remove_player_messages_mock()

### Community 1027 - "connectionStore.ts"
Cohesion: 0.21
Nodes (11): ConnectionActions, ConnectionHealth, ConnectionMetadata, ConnectionSelectors, ConnectionState, ConnectionStore, createInitialState(), GameEvent (+3 more)

### Community 1028 - "event_publisher"
Cohesion: 0.29
Nodes (7): event_publisher(), mock_nats_service(), mock_subject_manager(), fixture, Create a mock NATS service., Create a mock subject manager., Create an EventPublisher instance.

### Community 1029 - "room_validator/schemas/unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 1030 - "test_lucidity_procedures.py"
Cohesion: 0.29
Nodes (11): async_sessionmaker, asyncio, AsyncSession, fixture, Integration test for db/procedures/lucidity.sql's get_lucidity_rate_overrides()…, A zone with special_rules set, and a subzone under it with special_rules NULL…, A zone with NO override, and a subzone under it WITH special_rules set. Yields…, subzone_with_override() (+3 more)

### Community 1031 - "_ensure_connection_manager"
Cohesion: 0.24
Nodes (11): _ensure_connection_manager(), get_connection_statistics(), get_player_connections(), get, Request, Get connection information for a player. Returns detailed connection metadata…, Get comprehensive connection statistics. Returns detailed statistics about all…, Ensure connection manager is available. Raises LoggedHTTPException with proper… (+3 more)

### Community 1032 - "custom_length_validator"
Cohesion: 0.29
Nodes (7): custom_length_validator(), fixture, Create SubjectValidator instance., Create SubjectValidator with strict validation., Create SubjectValidator with custom max length., strict_validator(), validator()

### Community 1033 - "test_monitoring_init.py"
Cohesion: 0.17
Nodes (11): Unit tests for server.monitoring lazy __getattr__ re-exports., Exception tracker symbols import without triggering numpy lazy paths., __getattr__ resolves MonitoringDashboard and get_monitoring_dashboard., __getattr__ resolves PerformanceStats and get_performance_monitor., Unknown attribute names raise AttributeError., Direct __getattr__ covers both branch returns for dashboard imports., test_monitoring_eager_imports(), test_monitoring_getattr_direct_call() (+3 more)

### Community 1036 - ".get_task_lifecycle_metrics"
Cohesion: 0.33
Nodes (3): Get count of active tasks., Get task breakdown by type., Get task lifecycle metrics including creation and completion rates.

### Community 1037 - "load_motd"
Cohesion: 0.23
Nodes (11): Unit tests for motd_loader utilities. Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+3 more)

### Community 1038 - "main"
Cohesion: 0.27
Nodes (10): _exit_empty(), _load_state(), main(), NoReturn, Path, Exit successfully with no decision (allow the stop)., Load and validate edited-files state. Returns None if missing or invalid., Write state via a same-directory temp file + os.replace. See… (+2 more)

### Community 1039 - "Codacy Rules"
Cohesion: 0.18
Nodes (10): After every response, Codacy Rules, CRITICAL: After ANY successful file edit, CRITICAL: Dependencies and Security Checks, General, Trying to call a tool that needs a `rootPath` parameter, Using any tool that accepts `provider`, `organization`, or `repository`, When `codacy_cli_analyze` fails because the Codacy CLI is not installed (+2 more)

### Community 1040 - "Quieter Skill"
Cohesion: 0.18
Nodes (11): Quieter Skill, Assess Current State, Color Refinement, Composition Refinement, MANDATORY PREPARATION, Motion Reduction, Plan Refinement, Refine the Design (+3 more)

### Community 1041 - "Typeset Skill"
Cohesion: 0.18
Nodes (11): Typeset Skill, Assess Current Typography, Establish Hierarchy, Fix Readability, Font Selection, Improve Typography Systematically, MANDATORY PREPARATION, Plan Typography Improvements (+3 more)

### Community 1042 - "test_combat_messaging_integration.py"
Cohesion: 0.05
Nodes (51): messaging_integration(), mock_connection_manager(), asyncio, fixture, Unit tests for combat messaging integration. Tests the…, Test broadcast_player_mortally_wounded broadcasts message., Test broadcast_player_died broadcasts death message., Test broadcast_player_mortally_wounded with attacker name. (+43 more)

### Community 1043 - "vite.userConfig.ts"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1044 - "Client Test Remediation"
Cohesion: 0.18
Nodes (10): Client Test Remediation, 🔴 Critical — TypeScript/rendering errors, Debugging when a fix doesn't take, Entry point, Fix patterns by tier, Fix-verify loop, 🟡 High — component issues, 🟢 Medium — hook/async issues (+2 more)

### Community 1045 - "main"
Cohesion: 0.27
Nodes (10): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Write state via a same-directory temp file + os.replace. See… (+2 more)

### Community 1046 - "Claims by cluster"
Cohesion: 0.18
Nodes (11): Claims by cluster, client — ADR-008, ADR-011, ADR-017, config-api — ADR-013, container-di / layering — ADR-001, ADR-002, ADR-007, domain — ADR-009, ADR-010, ADR-016, events-nats — ADR-003, ADR-014, P2 · ADR Claim Register, persistence-db — ADR-005, ADR-006, ADR-015 (+3 more)

### Community 1047 - "P3 · container-di + client + domain"
Cohesion: 0.18
Nodes (10): Further P0 reversals, H10 · ADR-011 declares completed work as "planned", H7 · The global-singleton leak grew rather than shrank, H8 · Twelve modules bypass the persistence facade — and the two docs disagree about whether that's allowed, H9 · ADR-008 styling claim is wholly counterfactual, Low / STALE, Medium, Notable CONFORMS (+2 more)

### Community 1048 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (1 total, 0 thin omitted), Community 0 - "Mythos Subjects", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1049 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (2 total, 2 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1050 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Ambiguous Edges - Review These, Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1051 - "Authoritative Environment DML"
Cohesion: 0.20
Nodes (11): Spells Seed Data (Deprecated), static_seed.sql (Deprecated), Generated World and Emotes SQL, DB Bootstrap Execution Order, Authoritative Environment DML, Removed Schema and Migration SQL, Legacy Schema Files Removed, Historical DDL Final Status (+3 more)

### Community 1052 - "AnyIO Code Review - Anti-Patterns and Issues"
Cohesion: 0.18
Nodes (9): AnyIO Code Review - Anti-Patterns and Issues, Executive Summary, High Priority (Entry Points), Low Priority (Complex Refactoring), Medium Priority (Core Primitives), Migration Priority, Notes, Recommendations (+1 more)

### Community 1053 - "✅ Best Practices Compliance"
Cohesion: 0.18
Nodes (11): 10. Exception Handling in Async Operations (asyncio.mdc Section 2.5), 1. Blocking the Event Loop (asyncio.mdc Section 2.3), 2. Async/Await Usage (anyio.mdc Section 2.2), 3. Method Signature Consistency (asyncio.mdc Section 2.1), 4. Error Handling (asyncio.mdc Section 2.5), 5. Resource Management (anyio.mdc Section 2.1), 6. Task Groups / Structured Concurrency (anyio.mdc Section 2.1), 7. Avoiding asyncio.run() in Library Code (asyncio.mdc Section 6.1) (+3 more)

### Community 1054 - "🔍 Specific File Reviews"
Cohesion: 0.18
Nodes (11): ✅ container_service.py, ✅ corpse_lifecycle_service.py, ✅ database.py, ✅ exploration_service.py, ✅ npc_combat_integration_service.py, ✅ passive_lucidity_flux_service.py, ✅ persistence.py, ✅ player_death_service.py (+3 more)

### Community 1055 - "CircuitBreaker Implementation Planning Document"
Cohesion: 0.18
Nodes (10): CircuitBreaker Implementation Planning Document, Configuration Schema, Dependencies, Gradual Rollback, Immediate Rollback, Objectives, Overview, Rollback Plan (+2 more)

### Community 1056 - "Ruff to Pylint Rule Mapping"
Cohesion: 0.18
Nodes (11): B008 - Function calls in argument defaults, C901 - Too complex (PRIMARY COMPLEXITY CHECKER), Category Mappings, Complexity Checking, E501 - Line too long, Global Ignores (pyproject.toml), Next Steps, Purpose (+3 more)

### Community 1057 - "Test Timing Analysis - Optimization Targets"
Cohesion: 0.18
Nodes (11): Test Timing Analysis, 1. **Mark Additional Slow Tests**, 2. **Investigate Heavy Setup Tests**, 3. **Verify Marker Application**, 4. **Target Time Budget (5-7 min = 300-420 seconds)**, Critical Finding: Tests Still Running Despite Markers, Next Actions, pytest-xdist Parallel Fast Suite (+3 more)

### Community 1058 - "Movement Subsystem Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Architecture, 3. Key design decisions, 4. Constraints, 5. Component interactions, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1059 - "CI Workflow"
Cohesion: 0.25
Nodes (11): CodeQL Configuration, CodeQL Test Credential Exclusions, CI Python Backend Job, CI Workflow, Codacy Coverage Finalize Job, CI React Client Job, step-security Harden Runner, mythos_unit CI Database Bootstrap (+3 more)

### Community 1060 - "items"
Cohesion: 0.33
Nodes (6): items, minItems, type, additionalProperties, properties, holidays

### Community 1061 - "analyze_file"
Cohesion: 0.22
Nodes (10): analyze_file(), check_comment_references_nonexistent_code(), extract_function_and_class_names(), main(), Any, Path, Analyze a single file for comment issues. Args: file_path: Path to file to…, Main entry point for comment analysis. (+2 more)

### Community 1062 - "check_and_apply_map_migrations.py"
Cohesion: 0.25
Nodes (10): apply_migration_013(), apply_migration_014(), check_migration_013(), check_migration_014(), main(), Main function to check and apply migrations., Check if migration 013 (map_x/map_y columns) has been applied., Check if migration 014 (player_exploration table) has been applied. (+2 more)

### Community 1063 - "main"
Cohesion: 0.29
Nodes (10): check_thresholds(), _ensure_coverage_xml_or_exit(), main(), parse_coverage_xml(), _print_results_and_exit(), Path, Check files against their thresholds. Returns hard-fail messages., Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't… (+2 more)

### Community 1064 - "main"
Cohesion: 0.25
Nodes (10): generate_simple_dot_file(), generate_simple_html_visualization(), load_room_data(), main(), print_simple_statistics(), Load all room and intersection data from the zone directory., Print simplified statistics about the room data., Main function to generate the simplified visualization. (+2 more)

### Community 1065 - "items"
Cohesion: 0.33
Nodes (6): additionalProperties, properties, schedules, items, minItems, type

### Community 1066 - "container"
Cohesion: 0.33
Nodes (6): enabled, additionalProperties, description, required, type, container

### Community 1067 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 1068 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 1069 - "intersection_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1070 - "room_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1071 - "capacity_slots"
Cohesion: 0.33
Nodes (6): default, description, maximum, minimum, type, capacity_slots

### Community 1072 - ".create_drop_command"
Cohesion: 0.15
Nodes (12): Test create_drop_command() with quantity., Test create_drop_command() raises error for invalid index., test_create_drop_command_invalid_index(), test_create_drop_command_with_quantity(), Test create_drop_command() raises error when index is not integer., Test create_drop_command() raises error when quantity is not integer., Test create_drop_command() creates DropCommand., Test create_drop_command() raises error with no args. (+4 more)

### Community 1073 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test _ensure_room_cache_loaded returns early when cache is already loaded., Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…, Test _ensure_room_cache_loaded handles DatabaseError gracefully., Test _ensure_room_cache_loaded handles OSError gracefully., Test _ensure_room_cache_loaded handles RuntimeError gracefully., test_ensure_room_cache_loaded_already_loaded(), test_ensure_room_cache_loaded_concurrent_load() (+3 more)

### Community 1074 - "Teach Impeccable Skill"
Cohesion: 0.24
Nodes (11): Aha Moment Onboarding, Core Web Vitals Performance, Design Context Persistence (.impeccable.md), Onboard Skill, Optimize Skill, Overdrive Skill, Overdrive Mode, Polish Skill (+3 more)

### Community 1075 - "Playwright Best Practices"
Cohesion: 0.20
Nodes (9): 1. Always Use `@playwright/test`, 2. Prioritize Robust Locators, 3. Embrace Web-First Assertions, 4. Implement the Page Object Model (POM), 5. Optimize Performance with Auth State & Route Blocking, 6. Mock APIs for Deterministic Tests, 7. Leverage CI/CD Features for Debugging, 8. Maintain Code Quality with Linters & Formatters (+1 more)

### Community 1076 - "Responsive Design"
Cohesion: 0.20
Nodes (10): Breakpoints: Content-Driven, Detect Input Method, Not Just Screen Size, Layout Adaptation Patterns, Mobile-First: Write It Right, Picture Element for Art Direction, Responsive Design, Responsive Images: Get It Right, Safe Areas: Handle the Notch (+2 more)

### Community 1077 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

### Community 1078 - "._compute_player_context"
Cohesion: 0.33
Nodes (3): Debug log for context enrichment (best-effort, must not fail)., Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…, Get player_in_range, enemy_nearby, and target_id from persistence. Returns…

### Community 1079 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 1080 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.18
Nodes (11): 10. Final Verification, 3. Systematic Investigation Approach, 5. Test Environment Setup, 6. Quality Assurance Checklist, Environment Variables, For Authentication Failures, For Database-Related Failures, For Game Logic Failures (+3 more)

### Community 1081 - "FAILURE PATTERN RECOGNITION"
Cohesion: 0.33
Nodes (6): A. Database-Related Failures, B. Authentication/Security Failures, C. WebSocket/Connection Failures, D. Game Logic Failures, E. Integration Test Failures, FAILURE PATTERN RECOGNITION

### Community 1082 - "P3 · realtime-connection + events-nats"
Cohesion: 0.20
Nodes (9): CONFORMS worth recording, H1 · DLQ automatic cleanup is not wired — unbounded disk growth, H2 · ADR-003 is self-contradictory about the EventBus being networked, H3 · ADR-003 quotes deprecated NATS subject forms as current, High risk — require P5 refutation before ruling, Low / STALE, Medium risk, Meta-finding (+1 more)

### Community 1083 - "P7 · Rulings — complete"
Cohesion: 0.20
Nodes (10): C1 · What are the ADRs for? — **Mark provenance, keep ADRs for new decisions**, C2 · Query construction — **Fix the guard now, defer the doc decision**, C3 · Layer boundaries — **Split three ways**, C4 · Container architecture doc — **Restore to `docs/` with a provenance note**, C5 · Doc↔doc contradictions — **In-place for ADR-003, cross-reference for ADR-004**, C6 · Contract drift — **Record `/v1` + fix all dependent paths**, C7 · Closed-but-not-built — **Reopen everything**, C8 · Undocumented systems — **ADR for WebSocket security + ui-v2; doc updates for the rest** (+2 more)

### Community 1084 - "Design ↔ Implementation Drift Audit — Final Summary"
Cohesion: 0.20
Nodes (10): Decisions made — do not re-litigate, Design ↔ Implementation Drift Audit — Final Summary, Do first — small, high value, Loose ends outside the tracker, Sequencing that matters, User-visible defects, Weight the evidence correctly, What the audit concluded (+2 more)

### Community 1085 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)"
Cohesion: 0.20
Nodes (9): Communities (1 total, 1 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12), Knowledge Gaps, Suggested Questions, Summary (+1 more)

### Community 1086 - "enum"
Cohesion: 0.29
Nodes (7): autumn, spring, summer, winter, season, enum, type

### Community 1087 - "AnyIO vs Asyncio: High-Level Comparison and Decision Guide"
Cohesion: 0.20
Nodes (10): Adjusts spectacles and peers at the codebase, anyio Cons ❌, anyio Pros ✅, AnyIO vs Asyncio: High-Level Comparison and Decision Guide, asyncio Cons ❌, asyncio Pros ✅, Decision Matrix, My Academic Opinion (Mythos Persona) (+2 more)

### Community 1088 - "Asynchronous Code Audit - December 3, 2025"
Cohesion: 0.14
Nodes (13): adjusts spectacles grimly, Asynchronous Code Audit - December 3, 2025, ✍️ AUDIT CONCLUSION, Audit Status**: ✅**COMPLETE, Blocking Risks, 📞 ESCALATION MATRIX, Executive Summary, Non-Blocking Risks (+5 more)

### Community 1089 - "Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES"
Cohesion: 0.20
Nodes (10): Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES, Phase 3: Medium Priority Improvements (Week 4) - POLISH, 📋 REMEDIATION PLAN, Task 1.1: Fix Synchronous Blocking in Passive Lucidity Flux Service, Task 1.2: Eliminate asyncio.run() from Library Code, Task 1.3: Ensure Connection Pool Cleanup, Task 1.4: Add Exception Handling to Pool Creation, Task 1.5: Fix Blocking Operations in NATS Message Handlers (+2 more)

### Community 1090 - "📋 Test Coverage Breakdown"
Cohesion: 0.20
Nodes (10): API Endpoints (Tests Created, Pending Fresh Session), Auth (Tests Created, Pending Fresh Session), Caching (100% Complete), Commands (Tests Created, Pending Fresh Session), Infrastructure (100% Complete), NPC System (Tests Created, Pending Fresh Session), Real-Time (100% Complete), 📋 Test Coverage Breakdown (+2 more)

### Community 1091 - "`docs/**/*` files: Multiple rules"
Cohesion: 0.20
Nodes (10): B904 - Broad except, `docs/**/*` files: Multiple rules, E402 - Module level import not at top, F811 - Redefined name, F821 - Undefined name, F841 - Unused variable, `__init__.py` files: F401 (unused import), Per-File Ignores (pyproject.toml) (+2 more)

### Community 1092 - "2. Model Updates Verified"
Cohesion: 0.20
Nodes (10): 1. Code Quality Checks, 2. Model Updates Verified, 3. Type Compatibility, 4. Database Schema Alignment, ✅ `server/models/lucidity.py`, ✅ `server/models/npc.py`, ✅ `server/models/player.py`, ✅ `server/models/player_spells.py` (+2 more)

### Community 1093 - "Findings"
Cohesion: 0.20
Nodes (10): Findings, 🟡 HIGH PRIORITY: Manual Statistical Calculations, Issue 1: Performance Monitor - Manual Statistics, Issue 2: Performance Tracker - Repeated Statistical Operations, Issue 3: Stats Generator - Manual Dice Rolling, Issue 4: Stats Summary - Manual Summation, Issue 5: Missing NumPy Type Hints, 🔵 LOW PRIORITY: Type Hints and Documentation (+2 more)

### Community 1094 - "Repository Details"
Cohesion: 0.20
Nodes (10): 1. PlayerRepository (439 lines), 2. RoomRepository (42 lines), 3. ProfessionRepository (74 lines), 4. HealthRepository (165 lines), 5. ExperienceRepository (203 lines), 6. ContainerRepository (80 lines), 7. ItemRepository (84 lines), Async Repository Structure (+2 more)

### Community 1095 - "POSTGRESQL_AUDIT_REPORT_2026.md"
Cohesion: 0.27
Nodes (8): bigint generated always as identity, Migration 019 PostgreSQL Anti-patterns Fixes, Schema Drift player_id uuid vs varchar, SELECT * Anti-pattern, varchar(n) Prefer text, players.current_room_id Index Gap, Integer to BigInteger Column Mapping, String(n) to Text Column Mapping

### Community 1096 - "TEST_COVERAGE_DISCONNECT_GRACE_PERIOD_REST.md"
Cohesion: 0.20
Nodes (9): Disconnect Grace Period, Zombie Linkdead State, Disconnect Grace Period and Rest Command, Rest Command, 30-Second Disconnect Grace Period, ADR-009 Effects System Architecture, LOGIN_WARDED Effect, Effects System ADR and Implementation (+1 more)

### Community 1097 - "Implementation Phases"
Cohesion: 0.20
Nodes (10): Deliverables, Implementation Phases, Phase 0: Foundation (Week 1) - 40 hours, Phase 1: Fix Failing Tests (Week 1-2) - 40 hours, Phase 2: Unit Test Modernization (Week 3-4) - 80 hours, Phase 2A: Service Layer Tests (Week 3), Phase 2B: Infrastructure Tests (Week 4), Phase 3: Test Pattern Modernization (Week 5) - 40 hours (+2 more)

### Community 1098 - "Test Suite Quality Audit Report"
Cohesion: 0.18
Nodes (10): ~25-30% (1,250-1,500 tests) provide CRITICAL protection, Answer to Your Question, Conclusion, Phase A: Quick Wins (1-2 hours effort), Phase B: Medium Effort (4-8 hours effort), Phase C: Strategic Enhancements (8-16 hours effort), Recommended Action, Specific Actionable Recommendations (+2 more)

### Community 1099 - "MythosMUD Testing Strategy (Greenfield Suite)"
Cohesion: 0.22
Nodes (9): Coverage policy, Fixtures/layout, Isolation rules, Logging and diagnostics, Markers, Mocking standards, MythosMUD Testing Strategy (Greenfield Suite), Tiers and commands (+1 more)

### Community 1100 - "Dialogue Content Tools (Content Creators)"
Cohesion: 0.20
Nodes (9): 1. Overview, 2. Open the editor, 3. Tree shape (nav-only), 4. Editor workflow, 5. Player verification, 6. Seed and API reference, 7. Related docs, AI READING INSTRUCTION (+1 more)

### Community 1101 - "load_test_10_players.spec.ts"
Cohesion: 0.22
Nodes (6): generateLoadTestCredential(), INVITE_CODES, PLAYER_CONFIGS, PlayerConfig, NOTE: This test is designed to be executed using Playwright MCP tools for, registerPlayer()

### Community 1102 - "emote_schema.json"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 1103 - "bench_cache_npc.py"
Cohesion: 0.31
Nodes (5): bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…

### Community 1104 - "bench_cache_professions.py"
Cohesion: 0.31
Nodes (7): bench_profession_cache(), _FakePersistence, _get_empty_dict(), main(), Any, Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…, Helper function to return empty dict for mock methods.

### Community 1105 - "check_file"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1106 - "test_cache_service.py"
Cohesion: 0.17
Nodes (14): cached(), Cache service for MythosMUD server. This module provides caching services that…, Decorator to cache function results. Args: cache_name: Name of the cache to use…, Caching module for MythosMUD server. This module provides comprehensive caching…, get_cache_manager(), LRU Cache implementation for MythosMUD server. This module provides thread-safe…, Get the global cache manager instance. Returns: The global cache manager…, Reset the global cache manager (for testing). (+6 more)

### Community 1107 - "initialize_components"
Cohesion: 0.29
Nodes (8): initialize_components(), Any, Component hook coordination for freshly minted item instances., Prepare component state metadata for a new item instance. This routine…, Unit tests for item component hooks., test_initialize_components_empty_prototype(), test_initialize_components_merges_overrides(), test_initialize_components_records_prototype_components()

### Community 1108 - ".__init__"
Cohesion: 0.20
Nodes (7): Check if the status effect is still active., Any, Initialize Invite with defaults., _npc_alive_and_active(), setter, Return True if NPC is alive (determination_points > 0)., Allow backward-compatible assignment (npc.is_alive = False).

### Community 1109 - ".on_enter_state"
Cohesion: 0.33
Nodes (4): Any, Called whenever state machine enters a new state. Logs state transitions for…, Get connection statistics. Returns: Dictionary with connection metrics AI: For…, State

### Community 1110 - "lucidity_migration.py"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1111 - "ensure_directory_exists"
Cohesion: 0.25
Nodes (8): ensure_directory_exists(), Ensure a directory exists and return its absolute path. Args: directory: The…, Test ensure_directory_exists with existing directory., Test ensure_directory_exists creates directory if it doesn't exist., Test ensure_directory_exists with relative path., test_ensure_directory_exists_creates(), test_ensure_directory_exists_existing(), test_ensure_directory_exists_relative_path()

### Community 1112 - "test_calendar_procedures.py"
Cohesion: 0.38
Nodes (9): holiday_row(), npc_schedule_row(), async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/calendar.sql (#633). Replace raw SQL…, test_get_calendar_holidays_includes_the_new_row() (+1 more)

### Community 1113 - "session_factory"
Cohesion: 0.14
Nodes (19): async_sessionmaker, Provide an async session factory for integration tests. CRITICAL: This fixture…, session_factory(), asyncio, serial, Test that we can create and read a User from the database. CRITICAL: This test…, test_db_connectivity_create_and_read_user(), emote_row() (+11 more)

### Community 1114 - "test_npcs_zone_config_procedures.py"
Cohesion: 0.31
Nodes (9): async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/npcs.sql's zone/subzone config read…, Create one zone and one subzone with unique stable_ids. Yields (zone_stable_id,…, test_get_subzone_configs_joins_parent_zone(), test_get_zone_configs_includes_the_zone() (+1 more)

### Community 1115 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _build_room_objects logs debug info for specific room., Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., test_build_room_objects_debug_logging(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

### Community 1116 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 1117 - "handle_system_command"
Cohesion: 0.24
Nodes (11): handle_system_command(), Any, Broadcast a system-level message via the chat service if available., asyncio, Unit tests for system command handlers. Tests the system command functionality., Test handle_system_command() broadcasts system message., Test handle_system_command() handles missing message., Test handle_system_command() handles missing chat service. (+3 more)

### Community 1118 - "optimized_validate_action_content"
Cohesion: 0.20
Nodes (10): Test validating empty action., Test validating valid action., Test validating action with dangerous characters., Test validating action with injection pattern., test_optimized_validate_action_content_dangerous_chars(), test_optimized_validate_action_content_empty(), test_optimized_validate_action_content_injection(), test_optimized_validate_action_content_valid() (+2 more)

### Community 1119 - "optimized_validate_alias_name"
Cohesion: 0.20
Nodes (10): Test validating empty alias name., Test validating valid alias name., Test validating alias name starting with number (invalid)., Test validating alias name with hyphen (invalid - aliases don't allow hyphens)., test_optimized_validate_alias_name_empty(), test_optimized_validate_alias_name_hyphen(), test_optimized_validate_alias_name_starts_with_number(), test_optimized_validate_alias_name_valid() (+2 more)

### Community 1120 - "gh-stack (MythosMUD)"
Cohesion: 0.22
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1121 - "Workflows"
Cohesion: 0.22
Nodes (9): End-to-end: create a stack from scratch, Handle rebase conflicts (agent workflow), Making mid-stack changes, Modify a mid-stack branch and sync, Parsing `--json` output, Restructure a stack (remove a branch, reorder, or rename), Routine sync after merges, Squash-merge recovery (+1 more)

### Community 1122 - "FastAPI Best Practices"
Cohesion: 0.22
Nodes (9): 1. Code Organization: Domain-Driven Modularity, 2. Type Hints: Mandatory Everywhere, 3. Dependency Injection: Decouple Components, 4. API Design: Versioning & Thin Endpoints, 5. Error Handling: Use `HTTPException`, 6. Performance: Async-First & Production Deployment, 7. Security: Environment Variables & Auth, 8. Logging: Structured & Centralized (+1 more)

### Community 1123 - "Dependency Upgrade"
Cohesion: 0.22
Nodes (7): Pre-commit Best Practices, Before starting, Dependency Upgrade, Never, Rollback, Upgrade procedure, Verify

### Community 1124 - "tailwind Best Practices"
Cohesion: 0.22
Nodes (8): 1. Design System Configuration, 2. Component Abstraction, 3. Class Ordering & Readability, 4. Mobile-First & Responsive Design, 5. Performance Optimization, 6. Accessibility, 7. Theming & Dark Mode, tailwind Best Practices

### Community 1125 - "run-playwright-tests.js"
Cohesion: 0.22
Nodes (7): clientRoot, __dirname, E2E_BACKEND_BASE_URL, env, __filename, playwright, testsDir

### Community 1126 - "mythos_e2e Database"
Cohesion: 0.25
Nodes (8): ArkanWolfshade E2E Account, Ithaqua E2E Account, mythos_e2e Database, Playwright Runtime E2E Suite, seed_e2e_users.py, start_e2e_test.ps1, pytest Markers unit integration e2e slow serial, Post-Scenario Cleanup

### Community 1127 - "P4 · Intent Sweep — Plan Documents"
Cohesion: 0.20
Nodes (9): Conforming — substantial features that check out, Correction to a prior audit finding, CRITICAL · The guard that was supposed to prevent raw SQL was never connected, HIGH · ADR-009 number collision — code cites a decision that does not exist, Meta-finding · plan status is unreliable in *both* directions, P4 · Intent Sweep — Plan Documents, PLAN CLAIMED COMPLETE, CODE ABSENT, PLANNED BUT NOT BUILT (+1 more)

### Community 1128 - "holidays.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 1129 - "Audit Coverage Boundary — 2026-08 Design Audit"
Cohesion: 0.11
Nodes (18): 1. Purpose, 2. Scope for the immediate next step: verifying #625–#628, 3. Enumeration method, 4.1 Documents — the audited 29, recovered from the audit's own claim registers, 4.2 Documents — the residual 74, conservative default, 4.3 Code — method fact, not a directory checklist, 4.4 `docs/subsystems/` — staleness, not conformance, 4.5 Security — a boundary issue #639 does not mention (+10 more)

### Community 1130 - "🟡 HIGH PRIORITY ISSUES"
Cohesion: 0.22
Nodes (9): 10. Loading All Players Instead of Active Only, 11. NATS Connection Pool Not Used by Default, 12. No TLS Configuration for NATS, 13. Event Loop Change Detection Edge Cases, 14. Missing Transaction Rollback on Critical Failures, 7. Missing Room Lookup Caching, 8. Incomplete Migration to Async Persistence, 9. Multiple Database Flushes Before Commit (+1 more)

### Community 1131 - "🟢 MEDIUM PRIORITY IMPROVEMENTS"
Cohesion: 0.13
Nodes (15): 15. Hardcoded Connection Pool Sizes, 16. Deprecated asyncio.get_event_loop() Usage, 17. Inconsistent Error Handling Patterns, 18. Memory Leak Risk in Metrics Collection, 19. Missing Message Acknowledgment in NATS, 20. Subject Naming Inconsistency, 21. No Connection Health Monitoring, 🟢 MEDIUM PRIORITY IMPROVEMENTS (+7 more)

### Community 1132 - "Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE"
Cohesion: 0.22
Nodes (9): Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE, Task 2.1: Add Room Lookup Caching, Task 2.2: Complete Async Persistence Migration, Task 2.3: Optimize Database Flush Operations, Task 2.4: Load Only Active Players, Task 2.5: Use NATS Connection Pool by Default, Task 2.6: Add TLS Configuration, Task 2.7: Improve Event Loop Change Detection (+1 more)

### Community 1133 - "🔴 Anti-Patterns Check (Critical)"
Cohesion: 0.22
Nodes (9): 1. Blocking the Event Loop?, 2. Missing `await` Keywords?, 3. Using `asyncio.run()` in Library Code?, 4. Mixing Sync and Async Code Incorrectly?, 5. Forgetting to Await Awaitable Objects?, 6. Not Handling Exceptions?, 7. Over-using Locks?, 8. Unstructured Concurrency? (+1 more)

### Community 1134 - "Coverage Improvement Summary - Plan 2 Execution"
Cohesion: 0.22
Nodes (9): 🏆 Achievement Highlights, ✅ COMPLETED & VERIFIED (6 modules), Coverage Improvement Summary - Plan 2 Execution, 📝 CREATED & READY (6 modules), 📚 Documentation Created, Executive Summary, 📊 Expected Final Results, 📞 Support (+1 more)

### Community 1135 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 1136 - "Ruff C901 McCabe Complexity"
Cohesion: 0.25
Nodes (9): Fat Endpoints, Service Layer Delegation, McCabe Cyclomatic Complexity, Pylint R0911-R0915 Complexity Metrics, Ruff C901 McCabe Complexity, Ruff-Pylint Rule Parity, Lizard CCN Threshold, create_app (+1 more)

### Community 1137 - "Positive Findings ✅"
Cohesion: 0.22
Nodes (9): 1. **Excellent Error Boundary Implementation**, 2. **Good Connection State Management**, 3. **Proper Async/Await Usage**, 4. **Subject Manager Pattern**, 5. **TLS Configuration Implemented**, 6. **Connection Pooling Implemented**, 7. **Message Acknowledgment Support**, 8. **Async Mute Data Loading** (+1 more)

### Community 1138 - "Detailed Implementation"
Cohesion: 0.22
Nodes (9): 1. Error Handling Standardization, 2. Message Validation, 3. Batch Flush Error Recovery, 4. Connection Pool Error Handling, 5. Subject Manager Integration, 6. Health Monitoring, 7. Acknowledgment Metrics, 8. Wildcard Validation (+1 more)

### Community 1139 - "Specific File Reviews"
Cohesion: 0.22
Nodes (9): `server/api/players.py`, `server/auth/endpoints.py`, `server/config/models.py`, `server/models/command.py`, `server/models/game.py`, `server/schemas/invite.py`, `server/schemas/player.py`, `server/schemas/user.py` (+1 more)

### Community 1140 - "Python Code Coverage Status"
Cohesion: 0.22
Nodes (8): Critical Files Below Threshold, Immediate Priority (Critical Files), Normal Files Below 70% Threshold, Priority Recommendations, Python Code Coverage Status, Secondary Priority (Normal Files), Showing top 50 files with largest coverage gaps, Summary

### Community 1141 - ".get_combat_stats"
Cohesion: 0.33
Nodes (3): Get combat stats for a player., Normalize NPC stats to include 'hp' for backward compatibility., Get combat-relevant stats for an entity. Args: entity_id: ID of the entity…

### Community 1142 - "applies_to"
Cohesion: 0.17
Nodes (13): items, minItems, type, items, minItems, type, items, type (+5 more)

### Community 1143 - "test_websocket_handler_validation.py"
Cohesion: 0.20
Nodes (11): mock_validator(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler message validation. Tests the message…, Create a mock WebSocket., Create a mock message validator., Test _validate_message() returns message when validation succeeds. (+3 more)

### Community 1144 - "analyze_idle_memory_samples.py"
Cohesion: 0.39
Nodes (8): analyze(), _append_slope_rows(), JsonSample, main(), Path, Analyze idle memory JSONL samples (warmup + measurement windows)., JSONL row with numeric fields used for slope analysis., _slope_per_hour()

### Community 1145 - "bench_cache.py"
Cohesion: 0.31
Nodes (6): bench_room_cache(), _FakePersistence, main(), Any, Lightweight cache benchmark for CI artifacts. Measures miss vs. hit timings for…, Fake persistence layer providing async_get_room with simulated latency.

### Community 1146 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 1147 - "_filter_lines"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after…, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1148 - "fix_markdown_file"
Cohesion: 0.36
Nodes (8): fix_markdown_file(), fix_multiple_blanks(), main(), parse_markdownlint_output(), Path, Fix multiple consecutive blank lines (MD012). Returns: (new_content,…, Parse markdownlint output to get files with MD012 issues., Fix multiple blank lines in a single markdown file. Returns: (changed,…

### Community 1149 - "fix_room_references"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area. Args: base_path: Path to the…, save_room_file()

### Community 1150 - "run_bug_prevention_tests.ps1"
Cohesion: 0.53
Nodes (8): Invoke-ClientTest(), Invoke-IntegrationTest(), Invoke-ServerTest(), Show-TestSummary(), Test-Command(), Write-ColorOutput(), Write-Header(), Write-Section()

### Community 1151 - "run_make_stages.py"
Cohesion: 0.33
Nodes (8): keep_going_requested(), main(), _print_fail(), Return True when Make was invoked with -k / --keep-going., Return a short failure reason, or None if the stage is OK., Run `make <stage>`, stream output, return (exit_code, captured_output)., run_stage(), stage_failed_from_output()

### Community 1152 - "TestGetPlayerService"
Cohesion: 0.33
Nodes (4): Test get_player_service raises RuntimeError when service is None., Tests for get_player_service dependency function., Test get_player_service returns service when present., TestGetPlayerService

### Community 1153 - "ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Methodology, 7. Related ADRs, 8. Related docs (+3 more)

### Community 1154 - "App Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1155 - "Auth Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1156 - "Models Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1157 - "player_inventory_migration.py"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1158 - "Schemas Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1159 - "fixture"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request object., Create a mock persistence layer., Create a mock connection manager. (+1 more)

### Community 1160 - "Services Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1161 - "test_utility_commands_whoami.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for utility command handlers. Tests the whoami command functionality., Test handle_whoami_command() returns player information., Test handle_whoami_command() handles missing persistence., Test handle_whoami_command() handles player not found., test_handle_whoami_command(), test_handle_whoami_command_no_persistence(), test_handle_whoami_command_player_not_found()

### Community 1162 - "TestGetPlayerServiceForTesting"
Cohesion: 0.33
Nodes (4): Tests for get_player_service_for_testing helper function., Test get_player_service_for_testing returns provided service., Test get_player_service_for_testing creates PlayerService when None provided., TestGetPlayerServiceForTesting

### Community 1163 - "fixture"
Cohesion: 0.18
Nodes (11): mock_persistence(), mock_room_cache(), fixture, Create a mock persistence layer., Create a mock room cache service., Create a RoomService instance., Create a RoomService instance with cache., Create a sample room dictionary. (+3 more)

### Community 1164 - "TestGetConnectionManager"
Cohesion: 0.33
Nodes (4): Tests for get_connection_manager dependency function., Test get_connection_manager returns service when present., Test get_connection_manager raises RuntimeError when service is None., TestGetConnectionManager

### Community 1165 - "test_player_service_mutations.py"
Cohesion: 0.20
Nodes (9): Unit tests for player service mutations. Covers delete, location update, mythos…, Test validate_player_name() with empty string., Test validate_player_name() with invalid characters., Test soft_delete_character() when character already deleted., Test delete_player() when player not found., test_delete_player_not_found(), test_soft_delete_character_already_deleted(), test_validate_player_name_empty() (+1 more)

### Community 1166 - "test_room_subscription_manager_drops.py"
Cohesion: 0.03
Nodes (64): fixture, Unit tests for room subscription manager drop functions. Tests the room drop…, Test adjust_room_drop() returns False for invalid index., Test list_room_drops() returns room drops., Test add_room_drop() adds drop to new room., Test add_room_drop() adds drop to existing room., Test take_room_drop() successfully takes drop., Test take_room_drop() with index out of range. (+56 more)

### Community 1167 - "ADR-019: Player Effects System"
Cohesion: 0.22
Nodes (9): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. Changelog, ADR-019: Player Effects System (+1 more)

### Community 1168 - "optimized_validate_target_player"
Cohesion: 0.25
Nodes (8): Test validating empty target player name., Test validating valid target player name., Test validating invalid target player name., test_optimized_validate_target_player_empty(), test_optimized_validate_target_player_invalid(), test_optimized_validate_target_player_valid(), optimized_validate_target_player(), Optimized validation for target player fields. Args: value: The target player…

### Community 1169 - "optimized_strip_ansi_codes"
Cohesion: 0.20
Nodes (10): Test stripping ANSI codes from empty string., Test stripping ANSI codes from text without ANSI., Test stripping ANSI codes from text with ANSI., test_optimized_strip_ansi_codes_empty(), test_optimized_strip_ansi_codes_no_ansi(), test_optimized_strip_ansi_codes_with_ansi(), _cached_strip_ansi(), optimized_strip_ansi_codes() (+2 more)

### Community 1170 - "Room Pathing Validator Implementation Spec"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1171 - "validator.py CLI"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1172 - "AGENTS.md"
Cohesion: 0.18
Nodes (7): Chaosium Ingest Pipeline, Bug Investigator Agent, MythosMUD — Claude pointer, basedpyright: no Any, MythosMUD LLM Wiki (Obsidian), One Server Only, Server Authority

### Community 1173 - "gh-stack"
Cohesion: 0.25
Nodes (8): Agent rules, Exit codes and error recovery, gh-stack, Known limitations, Output conventions, Prerequisites, Quick reference, When to use this skill

### Community 1174 - "AuthRateLimitMiddleware"
Cohesion: 0.25
Nodes (6): AuthRateLimitMiddleware, ASGIApp, Receive, Scope, Send, Pure ASGI middleware; HTTP POST login/register only.

### Community 1175 - "Pydantic Best Practices"
Cohesion: 0.25
Nodes (8): 1. Model Naming and Organization, 2. Strict Typing and Immutability, 3. Safe Default Values, 4. Custom Validation Logic, 5. Settings Management, 6. Editor Integration (VS Code / Pylance), 7. Common Pitfalls, Pydantic Best Practices

### Community 1176 - "MythosMUD Commit Messages"
Cohesion: 0.25
Nodes (8): GH Stack Skill, Commit Messages Skill, Examples, Format, MythosMUD Commit Messages, Rules, Template, Types

### Community 1177 - "worktree-plan-template.md"
Cohesion: 0.25
Nodes (7): Cleanup Checklist, Context, Design Notes, Metadata, Plan / Todos, Risks and Edge Cases, Testing

### Community 1178 - "Step 2: Ask UX-Focused Questions"
Cohesion: 0.25
Nodes (8): Teach Impeccable Skill, Accessibility & Inclusion, Aesthetic Preferences, Brand & Personality, Step 1: Explore the Codebase, Step 2: Ask UX-Focused Questions, Step 3: Write Design Context, Users & Purpose

### Community 1179 - "run-vitest.js"
Cohesion: 0.25
Nodes (7): args, clientRoot, __dirname, env, __filename, vitest, vitestBin

### Community 1180 - "usePerformanceMonitor.ts"
Cohesion: 0.29
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 1181 - "cli.sh"
Cohesion: 0.46
Nodes (7): download(), download_cli(), download_file(), get_latest_version(), get_version_from_yaml(), handle_rate_limit(), cli.sh script

### Community 1182 - "Earth Plane"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1183 - "C2 · REVISED — procedures-only is binding"
Cohesion: 0.25
Nodes (7): C2 · REVISED — procedures-only is binding, Consequence for enforcement (#618), Consequence for the code — migration backlog, Consequence for the documents, Known bounded exception, Status, The rule

### Community 1184 - "P3 · config-api"
Cohesion: 0.25
Nodes (7): CONFORMS worth recording, H11 · Config fail-fast is defeated at app construction, degrading to dev CORS, H12 · The `/v1` prefix exists in no design document, and every ADR endpoint path is wrong, H13 · The API specification document specifies no API, Medium / Low, P3 · config-api, Prior finding resolved

### Community 1185 - "P3 · persistence-db"
Cohesion: 0.25
Nodes (7): CONFORMS worth recording, H4 · D1 resolved — the code is a three-pattern hybrid no document describes, H5 · "Services never construct raw queries" is false at three layers, H6 · "Fully Async" is true of the class but not of the code, Medium, P3 · persistence-db, STALE — docs behind completed work

### Community 1186 - "P5 · Adversarial Refutation"
Cohesion: 0.25
Nodes (7): DOWNGRADED · F2 — config fail-fast → dev CORS (High → Low/Medium), DOWNGRADED · F5 — raw SQL at three layers (High → Medium), DOWNGRADED & REFRAMED · F4 — "12 modules bypass the facade" (High → Low), P5 · Adversarial Refutation, SURVIVES · F1 — DLQ never prunes (High, effort S), SURVIVES · F3 — deprecated global still called (High) — and it is worse than stated, What this pass changed

### Community 1187 - "emotes.schema.json"
Cohesion: 0.06
Nodes (31): additionalProperties, additionalProperties, properties, required, type, items, type, uniqueItems (+23 more)

### Community 1188 - "1. Enhanced ChatPanel (New Chat Input Panel)"
Cohesion: 0.25
Nodes (8): 1. Enhanced ChatPanel (New Chat Input Panel), 2. Renamed Game Log Panel (Formerly ChatPanel), ChatPanel Layout Structure, Enhanced ChatPanel Interface, Game Log Panel Layout Structure, New Features to Add, Proposed Changes, Purpose and Functionality

### Community 1189 - "✅ Verified Already Implemented"
Cohesion: 0.25
Nodes (8): 10. TLS Configuration, 4. Connection Pool Cleanup, 5. Mute Data Caching, 6. F-String Logging, 7. Database Flush Operations, 8. Active Player Filtering, 9. NATS Connection Pooling, ✅ Verified Already Implemented

### Community 1190 - "Implementation Phases"
Cohesion: 0.25
Nodes (8): 1.1 Enhance CircuitBreaker Class, 1.2 Create CircuitBreaker Manager, 1.3 Add Configuration Support, 5.1 Authentication Operations, 5.2 Rate Limiting Integration, Implementation Phases, Phase 1: Core Infrastructure Enhancement, Phase 5: Authentication and Security

### Community 1191 - "3. REFACTOR Findings (935 findings)"
Cohesion: 0.25
Nodes (8): 3.1 Too Many Instance Attributes (R0902), 3.2 Too Many Arguments (R0913, R0917), 3.3 Too Many Local Variables (R0914), 3.4 Too Many Statements (R0915), 3.5 Too Many Return Statements (R0911), 3.6 Too Many Public Methods (R0904), 3.7 No-Else-Return (R1705), 3. REFACTOR Findings (935 findings)

### Community 1192 - "LOGGING_BEST_PRACTICES.md"
Cohesion: 0.25
Nodes (6): enhanced_logging_config.get_logger, Structured Logging, measure_performance, NumPy Code Review, roll_4d6_drop_lowest, NumPy Vectorized Statistics

### Community 1193 - "NumPy Code Review - MythosMUD Codebase"
Cohesion: 0.25
Nodes (8): Code Quality Improvements Achieved, Completed Actions, Conclusion, Executive Summary, ✅ Implementation Status, NumPy Code Review - MythosMUD Codebase, Summary of Recommendations, Testing Considerations

### Community 1194 - "Multiplayer Architecture Planning"
Cohesion: 0.25
Nodes (8): Performance Optimization Summary, Alias System Implementation Plan, Chat System Implementation Plan, Planning Completion Summary, Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 1195 - "API Endpoints (Phase 2)"
Cohesion: 0.25
Nodes (8): API Endpoints (Phase 2), Detailed File Migration Instructions, `server/api/containers.py`, `server/api/players.py`, `server/api/rooms.py`, `server/services/combat_service.py`, `server/services/user_manager.py`, Services (Phase 4)

### Community 1196 - "PYDANTIC_CODE_REVIEW.md"
Cohesion: 0.25
Nodes (6): Parameterized Queries, Pydantic v2 ConfigDict, Pydantic __slots__ Performance, Stats extra=allow Security Risk, Deprecated asyncio.get_event_loop, jsonb_set Field Name f-string SQL

### Community 1197 - "Top Time Consumers (>10 seconds)"
Cohesion: 0.25
Nodes (8): Argon2 Password Tests (1.4+ seconds), Auth & Security Tests (21+ seconds setup each), Infrastructure Tests (3.5+ seconds), NATS Message Handler Tests (2-3 seconds), Performance Tests (still running despite slow marker), Rate Limiter Timing Tests (still running), SSE Handler Tests (60 seconds total), Top Time Consumers (>10 seconds)

### Community 1198 - "pyrightconfig.json"
Cohesion: 0.25
Nodes (7): extends, extraPaths, pythonVersion, venv, venvPath, ., ./pyproject.toml

### Community 1199 - "enum"
Cohesion: 0.25
Nodes (8): catholic, islamic, jewish, mythos, neo_pagan, tradition, enum, type

### Community 1200 - "main"
Cohesion: 0.36
Nodes (7): main(), cursor, Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial),…, Create quest_definitions, quest_instances, quest_offers tables and indexes., Insert leave_the_tutorial quest definition and room offer (idempotent)., _run_quest_ddl(), _seed_leave_the_tutorial()

### Community 1201 - "migrate_file"
Cohesion: 0.36
Nodes (7): main(), migrate_file(), MigrationResult, NamedTuple, Path, Result of a file migration., Migrate a single file to use async persistence patterns. Args: file_path: Path…

### Community 1202 - "generate_sql.mjs"
Cohesion: 0.25
Nodes (8): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Static Data SQL Generation, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 1203 - "validate.mjs"
Cohesion: 0.32
Nodes (7): ajv, __dirname, __filename, loadJson(), main(), root, validateFile()

### Community 1204 - "Server & Client Package Documentation Coverage"
Cohesion: 0.22
Nodes (9): 1. Overview, 2. Index, 3. Related documentation, 4. Changelog, AI READING INSTRUCTION, Documented (16), Provisional (2), Server & Client Package Documentation Coverage (+1 more)

### Community 1205 - "TestGetAsyncPersistence"
Cohesion: 0.33
Nodes (4): Tests for get_async_persistence dependency function., Test get_async_persistence returns service when present., Test get_async_persistence raises RuntimeError when service is None., TestGetAsyncPersistence

### Community 1206 - "TestGetPlayerRespawnService"
Cohesion: 0.33
Nodes (4): Tests for get_player_respawn_service dependency function., Test get_player_respawn_service returns service when present., Test get_player_respawn_service raises RuntimeError when service is None., TestGetPlayerRespawnService

### Community 1207 - "TestGetPlayerCombatService"
Cohesion: 0.33
Nodes (4): Tests for get_player_combat_service dependency function., Test get_player_combat_service returns service when present., Test get_player_combat_service raises RuntimeError when service is None., TestGetPlayerCombatService

### Community 1208 - "TestGetPlayerDeathService"
Cohesion: 0.33
Nodes (4): Tests for get_player_death_service dependency function., Test get_player_death_service returns service when present., Test get_player_death_service raises RuntimeError when service is None., TestGetPlayerDeathService

### Community 1209 - "TestGetCombatService"
Cohesion: 0.33
Nodes (4): Tests for get_combat_service dependency function., Test get_combat_service returns service when present., Test get_combat_service raises RuntimeError when service is None., TestGetCombatService

### Community 1210 - "TestGetMagicService"
Cohesion: 0.33
Nodes (4): Tests for get_magic_service dependency function., Test get_magic_service returns service when present., Test get_magic_service raises RuntimeError when service is None., TestGetMagicService

### Community 1211 - "1. Structured Concurrency: Entry Points and Task Management"
Cohesion: 0.29
Nodes (7): 1.1. Top-Level Entry Point, 1.2. Launching Concurrent Tasks, 1.3. Grouping Tasks, 1. Structured Concurrency: Entry Points and Task Management, 2.1. CPU-Bound Work, 2. Avoiding Blocking Operations, asyncio Best Practices

### Community 1212 - "test_run_make_stages.py"
Cohesion: 0.39
Nodes (6): _load_module(), Tests for scripts/run_make_stages.py fail-fast helpers., test_keep_going_requested(), test_stage_failed_from_output_nonzero(), test_stage_failed_from_output_ok(), test_stage_failed_from_output_traceback()

### Community 1213 - "monitoring_service"
Cohesion: 0.25
Nodes (8): mock_combat_config(), mock_config(), mock_feature_flags(), monitoring_service(), fixture, Create mock feature flags., Create mock combat config., Create CombatMonitoringService instance with mocked dependencies.

### Community 1214 - "optimized_validate_command_content"
Cohesion: 0.25
Nodes (8): Test validating empty command content., Test validating valid command content., Test validating command content with injection pattern., test_optimized_validate_command_content_empty(), test_optimized_validate_command_content_injection(), test_optimized_validate_command_content_valid(), optimized_validate_command_content(), Optimized validation for command content fields. Args: value: The command…

### Community 1215 - "optimized_validate_reason_content"
Cohesion: 0.25
Nodes (8): Test validating empty reason content., Test validating valid reason content., Test validating reason content with injection pattern., test_optimized_validate_reason_content_empty(), test_optimized_validate_reason_content_injection(), test_optimized_validate_reason_content_valid(), optimized_validate_reason_content(), Optimized validation for reason content fields. Args: value: The reason to…

### Community 1216 - "optimized_validate_pose_content"
Cohesion: 0.25
Nodes (8): Test validating empty pose content., Test validating valid pose content., Test validating pose content with injection pattern., test_optimized_validate_pose_content_empty(), test_optimized_validate_pose_content_injection(), test_optimized_validate_pose_content_valid(), optimized_validate_pose_content(), Optimized validation for pose content fields. Args: value: The pose to validate…

### Community 1217 - "optimized_validate_filter_name"
Cohesion: 0.25
Nodes (8): Test validating empty filter name., Test validating valid filter name., Test validating invalid filter name., test_optimized_validate_filter_name_empty(), test_optimized_validate_filter_name_invalid(), test_optimized_validate_filter_name_valid(), optimized_validate_filter_name(), Optimized validation for filter name fields. Args: value: The filter name to…

### Community 1218 - "optimized_validate_help_topic"
Cohesion: 0.25
Nodes (8): Test validating empty help topic., Test validating valid help topic., Test validating invalid help topic., test_optimized_validate_help_topic_empty(), test_optimized_validate_help_topic_invalid(), test_optimized_validate_help_topic_valid(), optimized_validate_help_topic(), Optimized validation for help topic fields. Args: value: The help topic to…

### Community 1219 - "TestGetSpellLearningService"
Cohesion: 0.33
Nodes (4): Tests for get_spell_learning_service dependency function., Test get_spell_learning_service returns service when present., Test get_spell_learning_service raises RuntimeError when service is None., TestGetSpellLearningService

### Community 1220 - "CRITICAL SERVER MANAGEMENT RULES"
Cohesion: 0.29
Nodes (7): Server Management, CRITICAL SERVER MANAGEMENT RULES, Implications, MANDATORY SERVER STARTUP PROCEDURE, ONE SERVER ONLY RULE, PRE-COMMAND CHECKLIST, Server Authority (Critical)

### Community 1221 - "Test Coverage Requirements"
Cohesion: 0.29
Nodes (6): Coverage Measurement, Forbidden Test Patterns, Minimum Coverage Standard, Required Test Patterns, Test Coverage Requirements, Test Quality Standards

### Community 1222 - "gh-stack (MythosMUD)"
Cohesion: 0.29
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1223 - "Git Workflow"
Cohesion: 0.29
Nodes (6): Branching, Commit messages, Git Workflow, History hygiene, Never, Repository hygiene

### Community 1224 - "MythosMUD ADR Authoring"
Cohesion: 0.29
Nodes (7): ADR Authoring Skill, Index Update, Location, MythosMUD ADR Authoring, Reference, Structure, Template

### Community 1225 - "MythosMUD Logging Standards"
Cohesion: 0.29
Nodes (7): Logging Standards Skill, Import, MythosMUD Logging Standards, Optional Helpers, Reference, Structured Logging, Summary

### Community 1226 - "MythosMUD Server Runbook"
Cohesion: 0.29
Nodes (7): Server Runbook Skill, Commands, Critical Rules, MythosMUD Server Runbook, ONE SERVER ONLY RULE, Pre-Start Checklist, Reference

### Community 1227 - "MythosMUD Test Writing"
Cohesion: 0.29
Nodes (7): MythosMUD Test Writing Skill, Coverage, How to Run Tests, MythosMUD Test Writing, Reference, Rules, Where Tests Live

### Community 1228 - "E2E Tests Playwright"
Cohesion: 0.33
Nodes (7): Playwright E2E Runtime Tests, E2E Tests Playwright, Runtime Auth Isolation, Playwright storageState Session Sharing, E2E Login Timeout Issue, authenticatedTest Fixture, E2E Timeout Analysis and Fixes

### Community 1229 - "Event-Sourced Projector"
Cohesion: 0.33
Nodes (7): Event-Sourced Projector, Client Event Schema, game_state Event, GameState, room_state Event, Critical State Handoffs, Enter-Room Request/Response

### Community 1230 - "useGridLayout.ts"
Cohesion: 0.33
Nodes (5): layoutConfig, PanelState, STORAGE_KEYS, useGridLayout(), UseGridLayoutReturn

### Community 1231 - "Three-Column Game UI Layout"
Cohesion: 0.29
Nodes (7): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe

### Community 1232 - "Corrections · `docs/subsystems/` was missing from the corpus"
Cohesion: 0.29
Nodes (7): Corrections · `docs/subsystems/` was missing from the corpus, `docs/subsystems/` — 15 documents, 2,497 lines, FINDING SHARPENED — the ADR-009 collision is real and now better characterised, FINDINGS WITHDRAWN, Open decision, The headline finding is REINFORCED, not weakened, What happened

### Community 1233 - "CRITICAL · WebSocket authentication bypass on `/ws`"
Cohesion: 0.29
Nodes (7): AGENT-REPORTED, NOT YET VERIFIED BY ME — `/ws/{player_id}`, CRITICAL · WebSocket authentication bypass on `/ws`, Documentation status, Issue #472 status, Recommended fix — one guard, not three, VERIFIED — anonymous WebSocket connection via query parameter, VERIFIED — CSRF validation fails open

### Community 1234 - "Design ↔ Implementation Drift Audit"
Cohesion: 0.29
Nodes (7): Correction · the "back-dated ADRs" evidence was wrong, Design ↔ Implementation Drift Audit, Headline finding · the design record was largely built from the code, Notes, P8 progress, Rulings — all 8 complete, Scope boundary

### Community 1235 - "P0 · Previously-Known Deviations"
Cohesion: 0.29
Nodes (7): ACCEPTED — do not re-report as new, Contradiction found in prior work, Corroboration of the P2 provenance finding, Deferred / residual (open by admission), P0 · Previously-Known Deviations, PLANNED-NOT-DONE — highest-value rows, REMEDIATED — expect CONFORMS; a deviation here is a regression

### Community 1236 - "Decisions required"
Cohesion: 0.25
Nodes (8): D · The design record was built from the code, Decisions required, E · Who owns query construction?, F · Layer boundaries: enforce or amend?, G · Doc ↔ doc contradictions, H · Contract/path drift, rooted in one unrecorded decision, I · Undocumented systems, J · Operational defects — recommend removing from this audit entirely

### Community 1237 - "._generate_invite_code"
Cohesion: 0.25
Nodes (6): datetime, Generate a unique invite code., Test _generate_invite_code generates 12-character alphanumeric code., Test _generate_invite_code generates different codes on multiple calls., test_invite_generate_invite_code_format(), test_invite_generate_invite_code_uniqueness()

### Community 1238 - "Chat Panel"
Cohesion: 0.29
Nodes (7): Chat Message Type Categorization Bug, Chat Panel, Commands Panel, Game Log Panel, Chat Message Routing Bug Fix, Room Description Routing Bug Fix, Bug Prevention Testing Strategy

### Community 1239 - "Aggro and Threat System Implementation Plan"
Cohesion: 0.29
Nodes (6): Aggro and Threat System Implementation Plan, Constants (locked), Integration with NPC static data (behavior_config / npc_type), Key Modules and Files, References, Status

### Community 1240 - "✅ POSITIVE FINDINGS"
Cohesion: 0.29
Nodes (7): 1. Excellent Error Boundary Implementation, 2. Proper Use of asyncio.gather with return_exceptions=True, 3. Task Tracking and Lifecycle Management, 4. Good Connection State Management, 5. Proper Async Context Managers, 6. Enhanced Structured Logging, ✅ POSITIVE FINDINGS

### Community 1241 - "🔴 CRITICAL ISSUES"
Cohesion: 0.29
Nodes (7): 1. Synchronous Blocking Operations in Async Context (CONFIRMED PERFORMANCE ISSUE), 2. asyncio.run() Called from Existing Event Loop Context, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Blocking Operations in NATS Message Handlers, 6. F-String Logging Destroying Structured Logging, 🔴 CRITICAL ISSUES

### Community 1242 - "Easy Coverage Wins"
Cohesion: 0.33
Nodes (7): Coverage Improvement Summary, bcrypt PyO3 Reimport Limitation, Easy Coverage Wins, Realtime Small-File Coverage Sweep, Python Code Coverage Status, analyze_coverage_gaps.py, 70% Coverage Threshold

### Community 1243 - "1. CONVENTION Findings (260 findings)"
Cohesion: 0.29
Nodes (7): 1.1 Missing Module Docstrings (C0114), 1.2 Invalid Name (C0103), 1.3 Too Many Lines in Module (C0302), 1.4 Use Implicit Booleaness (C1805, C1804), 1.5 Singleton Comparison (C0121), 1.6 Missing Function Docstring (C0116), 1. CONVENTION Findings (260 findings)

### Community 1244 - "NATS Anti-Patterns Review 2026-01-13"
Cohesion: 0.33
Nodes (7): NATS Anti-Patterns Review 2026-01-13, NATS Inconsistent Error Handling, NATSService, Blocking Operations in Message Handlers, NATS Exception Hierarchy, NATS Medium-Priority Remediation, NATS Batch Flush Recovery

### Community 1245 - "Migration Workflow (Per File)"
Cohesion: 0.29
Nodes (7): Migration Workflow (Per File), Step 1: Pre-Migration Assessment, Step 2: Create Async Repository Instances, Step 3: Convert Methods to Async, Step 4: Update All Callers, Step 5: Test Migration, Step 6: Validate Performance

### Community 1246 - "Methods Extracted"
Cohesion: 0.29
Nodes (7): Group 1: Player Operations (~800 lines → ~80 lines), Group 2: Health & XP Operations (~400 lines → ~40 lines), Group 3: Container Operations (~300 lines → ~30 lines), Group 4: Item Operations (~200 lines → ~20 lines), Group 5: Profession Operations (~100 lines → ~20 lines), Group 6: Room Operations (~100 lines → ~20 lines), Methods Extracted

### Community 1247 - "Security Implementation"
Cohesion: 0.29
Nodes (7): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection, SSE Authentication System

### Community 1248 - "3.3 Value Distribution Calculation"
Cohesion: 0.29
Nodes (7): 3.1 Scoring Criteria Matrix, 3.2 Category Scores, 3.3 Value Distribution Calculation, 🔴 CRITICAL VALUE TESTS (Score ≥75): **1,272 tests (25.6%)**, 🟡 IMPORTANT VALUE TESTS (Score 50-74): **2,943 tests (59.3%)**, 🟢 LOW VALUE TESTS (Score <50): **750 tests (15.1%)**, Phase 3: Test Value Scoring

### Community 1249 - "calculate_notification_times"
Cohesion: 0.25
Nodes (8): calculate_notification_times(), Calculate notification times for countdown. Notifications occur: - Every 10…, Test calculate_notification_times() for short countdown., Test calculate_notification_times() for long countdown., Test calculate_notification_times() returns sorted descending., test_calculate_notification_times_long(), test_calculate_notification_times_short(), test_calculate_notification_times_sorted()

### Community 1250 - "Attack Command Not Starting Combat"
Cohesion: 0.29
Nodes (7): Attack Command Not Starting Combat, CommandType Enum vs String Comparison, Target Resolution via Lifecycle Manager, NPC Dual Tracking System Issue, Stale Room.get_npcs After Persistence Reload, NPC Spawning vs Occupants Display Issue, Flattened Occupants Losing Player NPC Distinction

### Community 1251 - "Second NPC Combat And Linkdead Findings"
Cohesion: 0.29
Nodes (7): Coroutine Object Has No current_room_id, Combat Start Missing Await get_player_by_name, get_player_by_id vs async_get_player Mismatch, XP Award async_get_player Missing Method, Linkdead WebSocket Grace Period, Second NPC Combat And Linkdead Findings, Stale Queued Attack Target Validation

### Community 1252 - "Multi-Word Spell Name Parsing Failure"
Cohesion: 0.29
Nodes (7): Missing cast spell spells Pydantic Models, Spell Slash Commands Missing From Validation, create_cast_command First-Word-Only Parse, Multi-Word Spell Name Parsing Failure, Missing async_heal_player Method, record_spell_cast Cross-Session Object Use, Heal Spell SQLAlchemy Session Boundary Error

### Community 1253 - "main"
Cohesion: 0.38
Nodes (6): generate_html_visualization(), load_room_data(), main(), Load all room and intersection data from the zone directory., Main function to generate the HTML visualization., Generate an HTML visualization of the room network.

### Community 1254 - "TestGetNPCSpawningService"
Cohesion: 0.33
Nodes (4): Tests for get_npc_spawning_service dependency function., Test get_npc_spawning_service returns service when present., Test get_npc_spawning_service raises RuntimeError when service is None., TestGetNPCSpawningService

### Community 1255 - "NATSConfig"
Cohesion: 0.09
Nodes (22): NATSConfig, Any, BaseSettings, field_validator, NATS messaging configuration., Validate TLS file paths exist when TLS is enabled., Validate max payload is reasonable., Validate value is positive. (+14 more)

### Community 1256 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1257 - "TestGetNPCPopulationController"
Cohesion: 0.33
Nodes (4): Tests for get_npc_population_controller dependency function., Test get_npc_population_controller returns service when present., Test get_npc_population_controller raises RuntimeError when service is None., TestGetNPCPopulationController

### Community 1258 - "TestGetChatService"
Cohesion: 0.33
Nodes (4): Tests for get_chat_service dependency function., Test get_chat_service returns service when present., Test get_chat_service raises RuntimeError when service is None., TestGetChatService

### Community 1259 - ".validate_timestamp"
Cohesion: 0.29
Nodes (4): field_validator, Validate event type is not empty., Validate timestamp is valid ISO format., Validate channel is a known chat channel.

### Community 1260 - "TestGetExitEntriesForRoom"
Cohesion: 0.33
Nodes (4): Tests for _get_exit_entries_for_room., Valid exits for a room produce one entry with correct direction and coordinates., Exits whose targets are missing are skipped when building exit entries., TestGetExitEntriesForRoom

### Community 1261 - "mythos_dev.npc_definitions"
Cohesion: 0.50
Nodes (5): mythos_dev.dialogue_definitions, mythos_dev.get_npc_system_statistics(), mythos_dev.npc_definitions, mythos_dev.npc_relationships, mythos_dev.npc_spawn_rules

### Community 1263 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 1264 - "TestGetPlayerServiceForTesting"
Cohesion: 0.33
Nodes (4): Test get_player_service_for_testing() function., Test get_player_service_for_testing() with injected service., Test get_player_service_for_testing() creates mock when None., TestGetPlayerServiceForTesting

### Community 1265 - ".create_sit_command"
Cohesion: 0.33
Nodes (5): Test create_sit_command() creates SitCommand., Test create_sit_command() raises error with args., test_create_sit_command(), test_create_sit_command_with_args(), Create SitCommand from arguments.

### Community 1266 - "_extract_bearer_token"
Cohesion: 0.29
Nodes (7): _extract_bearer_token(), _parse_subprotocol_token(), Extract bearer token from parsed subprotocol parts. If 'bearer' marker is…, Parse token from WebSocket subprotocol header. Example formats: "bearer,…, test_extract_bearer_token_empty(), test_extract_bearer_token_last_part(), test_parse_subprotocol_token()

### Community 1267 - "Thinking about stack structure"
Cohesion: 0.33
Nodes (6): Branch naming, Dependency chain, One stack, one story, Staging changes deliberately, Thinking about stack structure, When to create a new branch

### Community 1268 - "Extract Skill"
Cohesion: 0.33
Nodes (6): Extract Skill, Discover, Document, Extract & Enrich, Migrate, Plan Extraction

### Community 1269 - "MythosMUD Server Test Suite"
Cohesion: 0.33
Nodes (6): Command Tests Relocated, server/tests/unit/commands/, Integration Test Tier, make test-server, MythosMUD Server Test Suite, Unit Test Tier

### Community 1270 - "Common Test Failure Categories"
Cohesion: 0.33
Nodes (6): 1. Database Test Failures, 2. Authentication Test Failures, 3. WebSocket Test Failures, 4. Game Logic Test Failures, 5. Integration Test Failures, Common Test Failure Categories

### Community 1271 - ".create_stand_command"
Cohesion: 0.33
Nodes (5): Test create_stand_command() creates StandCommand., Test create_stand_command() raises error with args., test_create_stand_command(), test_create_stand_command_with_args(), Create StandCommand from arguments.

### Community 1272 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1273 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1274 - "Chat Panel Separation Specification"
Cohesion: 0.29
Nodes (6): Chat Panel Separation Specification, Conclusion, Current Integration Points, Current State Analysis, Existing Structure, Overview

### Community 1275 - "2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage"
Cohesion: 0.33
Nodes (6): 2.1 `asyncio.sleep()` Usage, 2.2 `asyncio.Lock()` Usage, 2.3 `asyncio.Event()` Usage, 2.4 `asyncio.Queue()` Usage, 2.5 `asyncio.wait_for()` Usage, 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage

### Community 1276 - "📚 Documentation Created"
Cohesion: 0.33
Nodes (6): 1. Comprehensive Audit Report, 2. Executive Summary, 3. Developer Quick Reference, 4. Migration Tracker, 5. Test Suite, 📚 Documentation Created

### Community 1277 - "Implementation Details"
Cohesion: 0.33
Nodes (6): CircuitBreaker Manager, Database Operations, Enhanced CircuitBreaker Class, Implementation Details, Integration Examples, NATS Operations

### Community 1278 - "Core Logging Principles"
Cohesion: 0.33
Nodes (6): 1. **Structured Logging**, 2. **Context is Everything**, 3. **Security First**, 4. **Performance Aware**, 5. **Actionable Information**, Core Logging Principles

### Community 1279 - "Performance Logging"
Cohesion: 0.33
Nodes (6): API Request Logging, Basic Logging, Database Query Logging, Error Logging with Context, Performance Logging, Structured Logging Patterns

### Community 1280 - "Common Mistakes and How to Fix Them"
Cohesion: 0.33
Nodes (6): Common Mistakes and How to Fix Them, Mistake 1: Forgetting to Update Imports, Mistake 2: Using Deprecated Context Parameter, Mistake 3: String Formatting in Log Messages, Mistake 4: Missing Context in Error Logs, Mistake 5: Wrong Log Levels

### Community 1281 - "Enhanced Logging Features"
Cohesion: 0.33
Nodes (6): Correlation IDs, Enhanced Logging Features, Exception Tracking, MDC (Mapped Diagnostic Context), Performance Monitoring, Security Sanitization

### Community 1282 - "Log Levels and Usage"
Cohesion: 0.33
Nodes (6): CRITICAL, DEBUG, ERROR, INFO, Log Levels and Usage, WARNING

### Community 1283 - "Common Patterns"
Cohesion: 0.33
Nodes (6): API Requests, Common Patterns, Database Operations, Errors with Context, Performance Monitoring, User Actions

### Community 1284 - "Enhanced Logging Migration Report"
Cohesion: 0.33
Nodes (5): Enhanced Logging Features, Enhanced Logging Migration Report, Next Steps, Successfully Updated Files, Summary

### Community 1285 - "Completed Fixes ✅"
Cohesion: 0.33
Nodes (6): 1. Fixed Synchronous Operation in WebSocket Helpers, 2. Standardized Error Handling, 3. Added Message Validation to NATSMessageBroker, 4. Improved Batch Flush Error Recovery, 5. Improved Connection Pool Error Handling, Completed Fixes ✅

### Community 1286 - "NPC Startup Duplication Analysis"
Cohesion: 0.33
Nodes (6): NPC Duplication Bug Fix Plan, NPC Population Field Rename, NPC Lifecycle Manager, NPC Population Controller, NPC Startup Duplication Analysis, NPC Startup Service

### Community 1287 - "✨ Key Achievements"
Cohesion: 0.33
Nodes (6): 1. Modular Architecture, 2. Async Foundation, 3. Zero Breaking Changes, 4. Comprehensive Documentation, 5. Quality Maintained, ✨ Key Achievements

### Community 1288 - "PostgreSQL Procedures Migration - Audit Spreadsheet"
Cohesion: 0.33
Nodes (5): Audit Table, Domain Grouping Summary, Existing PostgreSQL Functions (Already in DDL), PostgreSQL Procedures Migration - Audit Spreadsheet, Scope

### Community 1289 - "Real-Time Communication (WebSocket)"
Cohesion: 0.33
Nodes (5): Authentication and Token in URL, Connection Grace Periods, Deprecated Endpoints, Production: HTTPS and WSS, Real-Time Communication (WebSocket)

### Community 1290 - "Test Suite Analysis"
Cohesion: 0.33
Nodes (6): Current Test Organization, Dependency Access Patterns, Pattern 1: Direct app.state Access (Broken - 445 instances), Pattern 2: Using Real Lifespan (Works - Limited), Pattern 3: Fixture-Based Mocking (Mixed), Test Suite Analysis

### Community 1291 - "Modern Testing Patterns"
Cohesion: 0.33
Nodes (6): Modern Testing Patterns, Pattern 1: Container-Based Fixtures, Pattern 2: Mock Container for Unit Tests, Pattern 3: Parametrized Integration Tests, Pattern 4: Fixture Factories, Pattern 5: Async Test Context Managers

### Community 1292 - "Test Modernization Checklist"
Cohesion: 0.33
Nodes (6): Phase 0: Foundation, Phase 1: Fix Failures, Phase 2: Modernize Units, Phase 3: Pattern Updates, Phase 4: New Coverage, Test Modernization Checklist

### Community 1293 - "Phase 5: Strategic Additions (Week 5)"
Cohesion: 0.33
Nodes (6): Phase 5: Strategic Additions (Week 5), Task 5.1: Add MessageBroker Integration Tests (3 hours), Task 5.2: Add ApplicationContainer Lifecycle Tests (2 hours), Task 5.3: Add Database Migration Tests (3 hours), Task 5.4: Add WebSocket Edge Case Tests (4 hours), Task 5.5: Add Error Recovery Tests (3 hours)

### Community 1294 - "packages/README.md"
Cohesion: 0.06
Nodes (39): UI-v2 Components, API OpenAPI/Swagger Specification, ADR-002: ApplicationContainer for Dependency Injection, ADR-022: ui-v2 Client Transition, Bounded Contexts and Service Boundaries, Command Handler Patterns, Command Models Reference, Command Security Guide (+31 more)

### Community 1295 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 1296 - "NPC Occupants Verification Summary"
Cohesion: 0.33
Nodes (6): NPC Display Final Fixes, room_update Overwriting NPC Data, asyncpg UUID replace AttributeError, Legacy Occupants Snapshot Format, NPC Occupants Verification Summary, Rooms API User Object AttributeError

### Community 1297 - "Combat Client Crash"
Cohesion: 0.33
Nodes (6): event_data vs data Field Name Mismatch, NATS Event Message Field Mismatch, Combat Client Crash, CombatMessaging Connection Manager Init Failure, Combat Disconnect At NPC Death, Passive Lucidity Flux Performance Degradation

### Community 1298 - "Respawn Death Screen Loop Limbo ID Mismatch"
Cohesion: 0.33
Nodes (6): limbo_death_void vs limbo_death_void_limbo_death_void, Respawn Death Screen Loop Limbo ID Mismatch, SQLAlchemy JSONB Mutation Detection, Respawn Persistence JSONB Mutation Failure, Death Threshold and Posture Bugs, HP -10 Limbo Transition Delay

### Community 1299 - "NPC Combat Start Race Condition"
Cohesion: 0.33
Nodes (6): NPC Combat Start Race Condition, Redundant NPC Instance Lookup Failure, NPCs Incorrectly Marked is_alive False, December 3 Final Investigation Summary, Character Info Panel Missing Stats Field, Room Occupants Duplicates and Missing Player

### Community 1300 - "Round-Based Combat"
Cohesion: 0.33
Nodes (6): Combat Action Queue, Combat Bugs Investigation and Fixes, Round-Based Combat, Combat Round System Refactor, First Weapon Switchblade, Flee Command and Effect

### Community 1301 - "WebSocket-Only Migration"
Cohesion: 0.33
Nodes (6): SSE Connection Removal, Unified Client Message Pipeline, Unify Client Message Handling, WebSocket Best-Practices Remediation, WebSocket-Only Architecture, WebSocket-Only Migration

### Community 1302 - "item_prototype.schema.json"
Cohesion: 0.40
Nodes (4): additionalProperties, $schema, title, type

### Community 1303 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1304 - "_run_dialogue_ddl"
Cohesion: 0.40
Nodes (5): main(), cursor, Create dialogue_definitions table if missing in the given schema., Connect via DATABASE_URL and ensure dialogue_definitions exists., _run_dialogue_ddl()

### Community 1305 - "check_file_for_logging_issues"
Cohesion: 0.47
Nodes (5): check_file_for_logging_issues(), main(), Path, Check a single file for logging consistency issues. Args: file_path: Path to…, Main function to check all service files for logging consistency.

### Community 1306 - "e2e_reset_players.py"
Cohesion: 0.47
Nodes (5): _load_default_respawn_room(), main(), Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the…, Entry point: run E2E player reset via anyio., _reset_e2e_players()

### Community 1307 - "add_suppression_to_file"
Cohesion: 0.47
Nodes (5): add_suppression_to_file(), main(), Path, Add suppression comment to a PowerShell file if it uses Write-Host and doesn't…, Process all PowerShell scripts in the scripts directory.

### Community 1308 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1309 - "_ConnectionManagerUtilsModule"
Cohesion: 0.40
Nodes (4): _ConnectionManagerUtilsModule, Protocol, Resolve the connection manager singleton (or optional candidate)., _WebSocketHandlerModule

### Community 1310 - "test_chat_logger.py"
Cohesion: 0.05
Nodes (37): Initialize chat service. Args: persistence: Database persistence layer…, Path, Initialize the user manager. Args: data_dir: Directory for player-specific mute…, chat_logger(), fixture, Unit tests for chat logger service. Tests the ChatLogger class for structured…, Test log_player_muted writes entry., Test log_player_unmuted writes entry. (+29 more)

### Community 1311 - ".create_unfollow_command"
Cohesion: 0.33
Nodes (5): Test create_unfollow_command() creates UnfollowCommand with no args., Test create_unfollow_command() raises error with args., test_create_unfollow_command(), test_create_unfollow_command_with_args(), Create UnfollowCommand from arguments.

### Community 1312 - "_RaisesOnBool"
Cohesion: 0.40
Nodes (4): _RaisesOnBool, Test double whose truthiness check raises, to exercise the broad except path., Test check_database_health handles errors gracefully., test_check_database_health_error()

### Community 1313 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1314 - "PostgreSQL database names (MythosMUD)"
Cohesion: 0.40
Nodes (4): CRITICAL: Which databases may be reset, Database placement (production vs test), Enforcement, PostgreSQL database names (MythosMUD)

### Community 1315 - "MythosMUD COPPA Checklist"
Cohesion: 0.40
Nodes (5): COPPA Checklist Skill, Checklist, Implementation, MythosMUD COPPA Checklist, Reference

### Community 1317 - "global-teardown.ts"
Cohesion: 0.40
Nodes (3): __dirname, __filename, projectRoot

### Community 1318 - "AI PR Reviewer Instructions"
Cohesion: 0.40
Nodes (5): AI PR Reviewer Instructions, COPPA and Security Review Mandates, Review Coverage Thresholds, player_id UUID Type Rule, Server Authority Review Rule

### Community 1319 - "4. Common Fix Patterns"
Cohesion: 0.40
Nodes (5): 4. Common Fix Patterns, Authentication Test Patterns, Database Test Patterns, Game Logic Test Patterns, WebSocket Test Patterns

### Community 1320 - "DML Migrations"
Cohesion: 0.40
Nodes (4): Dialogue definitions (#583), DML Migrations, Historical CSV files, Migration files

### Community 1321 - "Nameless Horrors - 2nd Edition (source summary)"
Cohesion: 0.50
Nodes (4): External live graph, For MythosMUD design, Key extractions pages, Nameless Horrors - 2nd Edition (source summary)

### Community 1322 - "S. Petersen's Field Guide to Lovecraftian Horrors (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extrated pages, S. Petersen's Field Guide to Lovecraftian Horrors (source summary)

### Community 1323 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1324 - "Advanced Chat Channels Specification"
Cohesion: 0.40
Nodes (5): Advanced Chat Channels Specification, Global Chat Channel, Local Chat Channel, Advanced Chat Channels Tasks, Whisper Chat Channel

### Community 1325 - "UI/UX Considerations"
Cohesion: 0.40
Nodes (5): 1. Visual Distinction, 2. Panel Positioning, 3. Responsive Design, 4. Accessibility, UI/UX Considerations

### Community 1326 - "3. Simplified CommandPanel"
Cohesion: 0.40
Nodes (5): 3. Simplified CommandPanel, CommandPanel Layout Structure, Features to Keep, Features to Remove, Simplified CommandPanel Interface

### Community 1327 - "Implementation Phases"
Cohesion: 0.40
Nodes (5): Implementation Phases, Phase 1: Core Separation, Phase 2: Enhanced Features, Phase 3: Polish and Optimization, Phase 4: Testing and Refinement

### Community 1328 - "Magic and Spellcasting System"
Cohesion: 0.40
Nodes (5): EffectList Pattern, Effects System Reference, Magic Points MP, Magic and Spellcasting System, Spell Registry

### Community 1329 - "Implementation Plan"
Cohesion: 0.40
Nodes (5): Implementation Plan, Step 1: Update `.pylintrc` ✅, Step 2: Refactor Ruff C901 Violations, Step 3: Document the Strategy, Step 4: Verify Alignment

### Community 1330 - "Lucidity Tiers"
Cohesion: 0.60
Nodes (5): Catatonic Rescue Window, Lucidity System (LCD), Lucidity Tiers, Phantom Hostiles, Reversed Compass Directions

### Community 1331 - "Code Quality Improvements"
Cohesion: 0.40
Nodes (5): Code Quality Improvements, Documentation, Exception Handling, Monitoring, Validation

### Community 1332 - "Common Conversion Patterns"
Cohesion: 0.40
Nodes (5): Common Conversion Patterns, Pattern 1: Simple Query, Pattern 2: Batch Operations, Pattern 3: Health Operations, Pattern 4: FastAPI Dependency Injection

### Community 1333 - "Gotchas & Solutions"
Cohesion: 0.40
Nodes (5): Gotcha 1: Async Propagation, Gotcha 2: Mixing Sync and Async, Gotcha 3: Transaction Management, Gotcha 4: Testing Async Code, Gotchas & Solutions

### Community 1334 - "Four-Level Room Hierarchy"
Cohesion: 0.40
Nodes (5): Environment Classification, Four-Level Room Hierarchy, Environment Inheritance, Room Hierarchy Implementation, Hierarchical World Loader

### Community 1335 - "Phase 1: Quantitative Analysis Results"
Cohesion: 0.40
Nodes (5): 1.1 Test Distribution by Category, 1.2 Largest Test Files (Splitting/Pruning Candidates), 1.3 Infrastructure Test Analysis, Files, Phase 1: Quantitative Analysis Results

### Community 1336 - "weather_patterns"
Cohesion: 0.40
Nodes (5): type, weather_patterns, description, items, type

### Community 1337 - "Summary: Test Quality Metrics"
Cohesion: 0.40
Nodes (5): By removing 15% of tests, we, Current State, Optimized State (After Pruning), Summary: Test Quality Metrics, Value Proposition

### Community 1338 - "Modular E2E Test Suite"
Cohesion: 0.40
Nodes (5): Modular E2E Test Suite, MULTIPLAYER_SCENARIOS_PLAYBOOK, E2E Validation Passed, AI Context Limit 20KB, E2E Test Suite README

### Community 1339 - "Playwright MCP Scenarios"
Cohesion: 0.40
Nodes (5): Automated Playwright CLI Tests, Hybrid E2E Testing Approach, Mandatory Execution Order, Playwright MCP Scenarios, Room Occupants Fix

### Community 1340 - "Local Channel System"
Cohesion: 0.40
Nodes (5): Local Channel Sub-Zone Routing, Scenario 10 Local Channel Movement, Scenario 11 Local Channel Errors, Scenario 12 Local Channel Integration, Local Channel System

### Community 1341 - "Container Contents Synchronization Bug"
Cohesion: 0.50
Nodes (5): Container Contents Synchronization Bug, Fail-Fast Container Error Philosophy, slot_type backpack Assignment, Dual Inventory Storage Architecture, Inventory Slot Calculation Bug

### Community 1342 - "F-String Logging Violations"
Cohesion: 0.40
Nodes (5): F-String Logging Violations, Enhanced Logging Compliance Audit, F-String Logging Remediation Complete, Pre-Commit F-String Hook Gaps, AST-Based F-String Logging Detector

### Community 1343 - "Quest System Gap"
Cohesion: 0.40
Nodes (5): Quest System Gap, MUD Subsystems Gap Analysis, Player Skills and Profession Modifiers, Quest Subsystem Implementation, Quest System

### Community 1344 - "items"
Cohesion: 0.40
Nodes (5): items, type, pattern, type, bonus_tags

### Community 1345 - "7. Common Test Failure Solutions"
Cohesion: 0.50
Nodes (4): 7. Common Test Failure Solutions, Authentication Test Issues, Database Connection Issues, WebSocket Test Issues

### Community 1346 - "fix_file"
Cohesion: 0.60
Nodes (4): fix_file(), main(), Path, Fix suppressions in a file. Returns: (number_fixed, list of changes)

### Community 1347 - "check_codacy_yaml"
Cohesion: 0.50
Nodes (4): check_codacy_yaml(), _content_is_valid(), Return (valid, list of reasons if invalid)., Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit.

### Community 1348 - "HADS tooling (MythosMUD)"
Cohesion: 0.40
Nodes (4): HADS tooling (MythosMUD), Policy, Source pin, Usage

### Community 1349 - "snapshot_chaosium_graphify.ps1"
Cohesion: 0.70
Nodes (4): Export-PackSnapshot(), Get-ChaosiumSlug(), Get-GraphCount(), Get-HonestyNote()

### Community 1351 - "2025_01_XX_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 1352 - "2025_11_21_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 1353 - "2025_11_25_normalize_container_schema.py"
Cohesion: 0.40
Nodes (4): downgrade(), Normalize container schema with proper relational structure., Revert to denormalized schema with items_json., upgrade()

### Community 1354 - "2025_11_25_remove_get_container_contents_json_procedure.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove deprecated stored procedure., Restore deprecated stored procedure., upgrade()

### Community 1355 - "2025_11_25_remove_items_json_column.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove items_json column from containers table., Restore items_json column (data will be empty)., upgrade()

### Community 1356 - "2025_11_26_ensure_item_instance_foreign_keys.py"
Cohesion: 0.40
Nodes (4): downgrade(), Ensure foreign key constraints exist for item_instances., This migration only ensures constraints exist - no downgrade needed., upgrade()

### Community 1357 - "2026_02_09_add_player_effects_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_effects table and indexes (ADR-019 effects system)., Drop player_effects table and indexes., upgrade()

### Community 1358 - "2026_02_18_add_player_skills_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_skills table if not exists (matches db/migrations/025)., Drop player_skills table., upgrade()

### Community 1359 - "2026_02_18_add_profession_modifiers_columns.py"
Cohesion: 0.40
Nodes (4): downgrade(), Add stat_modifiers and skill_modifiers columns to professions table., Remove stat_modifiers and skill_modifiers columns from professions table., upgrade()

### Community 1360 - "2026_02_19_add_quest_tables.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create quest_definitions, quest_instances, quest_offers tables., Drop quest tables (order matters for FKs)., upgrade()

### Community 1361 - "2026_02_19_seed_quest_leave_the_tutorial.py"
Cohesion: 0.40
Nodes (4): downgrade(), Insert leave_the_tutorial quest and quest_offers row., Remove seed quest and its offer., upgrade()

### Community 1362 - "2026_02_26_add_arena_zone_type.py"
Cohesion: 0.40
Nodes (4): downgrade(), Allow zone_type 'arena' in zones CHECK., Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)., upgrade()

### Community 1363 - "2026_08_20_align_room_environment_enum.py"
Cohesion: 0.40
Nodes (4): downgrade(), Fix the two one-off room rows, then widen/add the environment CHECKs., Restore the narrower zones/subzones CHECKs and drop the rooms CHECK. Does not…, upgrade()

### Community 1364 - "rename_players_to_population.py"
Cohesion: 0.40
Nodes (4): downgrade(), Rename columns from min_players/max_players to min_population/max_population., Revert column names back to min_players/max_players., upgrade()

### Community 1365 - "get_alerts"
Cohesion: 0.40
Nodes (5): get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing)

### Community 1366 - "command_service"
Cohesion: 0.29
Nodes (7): command_service(), mock_request(), mock_user(), fixture, Create a CommandService instance., Create a mock request object., Create a mock user object.

### Community 1367 - "_RoomPersistence"
Cohesion: 0.40
Nodes (4): Protocol, Protocol for persistence with get_room_by_id., Return the room object for the given room_id, or None if not found., _RoomPersistence

### Community 1368 - "10. Grace Period Persistence"
Cohesion: 0.50
Nodes (4): 10. Grace Period Persistence, Gap Analysis, Industry Practices, Our Plan

### Community 1369 - "1. Disconnect Grace Period Duration"
Cohesion: 0.50
Nodes (4): 1. Disconnect Grace Period Duration, Gap Analysis, Industry Practices, Our Plan

### Community 1370 - "2. Auto-Attack During Grace Period"
Cohesion: 0.50
Nodes (4): 2. Auto-Attack During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 1371 - "3. Grace Period Visibility & Messaging"
Cohesion: 0.50
Nodes (4): 3. Grace Period Visibility & Messaging, Gap Analysis, Industry Practices, Our Plan

### Community 1372 - "4. Rest/Quit Command During Combat"
Cohesion: 0.50
Nodes (4): 4. Rest/Quit Command During Combat, Gap Analysis, Industry Practices, Our Plan

### Community 1373 - "5. Rest Command Countdown Duration"
Cohesion: 0.50
Nodes (4): 5. Rest Command Countdown Duration, Gap Analysis, Industry Practices, Our Plan

### Community 1374 - "6. Rest Location (Inn/Hotel) Behavior"
Cohesion: 0.50
Nodes (4): 6. Rest Location (Inn/Hotel) Behavior, Gap Analysis, Industry Practices, Our Plan

### Community 1375 - "add_fastapi_users_columns.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add FastAPI Users columns. Args: database_url:…

### Community 1376 - "7. Reconnection During Grace Period"
Cohesion: 0.50
Nodes (4): 7. Reconnection During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 1377 - "8. Grace Period After Intentional Disconnect"
Cohesion: 0.50
Nodes (4): 8. Grace Period After Intentional Disconnect, Gap Analysis, Industry Practices, Our Plan

### Community 1378 - "9. Command Blocking During Grace Period"
Cohesion: 0.50
Nodes (4): 9. Command Blocking During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 1380 - "Recommendations Summary"
Cohesion: 0.50
Nodes (4): High Priority Decisions, Low Priority (Future Considerations), Medium Priority Enhancements, Recommendations Summary

### Community 1381 - "mythos_dev.users"
Cohesion: 0.40
Nodes (5): mythos_dev.id_map_players, mythos_dev.invites, mythos_dev.muting_rules, mythos_dev.reserve_invite(), mythos_dev.users

### Community 1382 - "add_hashed_password_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add hashed_password column. Args: database_url:…

### Community 1383 - "user_manager"
Cohesion: 0.40
Nodes (5): mock_data_dir(), fixture, Create a temporary data directory., Create a UserManager instance., user_manager()

### Community 1384 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 1385 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1386 - "Tiered Test Coverage Strategy"
Cohesion: 0.50
Nodes (4): Critical Code 90% Coverage, Global 70% Coverage Threshold, Tiered Test Coverage Strategy, Vitest Unit Tests

### Community 1387 - "add_used_by_user_id_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add used_by_user_id column. Args: database_url:…

### Community 1388 - "rename_invites_columns.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Apply the migration to rename columns. Args: database_url: PostgreSQL database…, Main entry point for the migration script.

### Community 1390 - "multiplayer-browser-helpers.d.ts"
Cohesion: 0.50
Nodes (3): GameUiDiagnostics, OccupantsSnapshot, PresenceEvent

### Community 1391 - "9. Test Maintenance Best Practices"
Cohesion: 0.50
Nodes (4): 9. Test Maintenance Best Practices, Performance Considerations, Test Data Management, Test Isolation

### Community 1392 - "Geography Overview.md"
Cohesion: 0.12
Nodes (12): Code Graph Entry, Live exploration (preferred for "how does X work?"), Synced community wiki (read-only dump), Chaosium pack graphs (external), Relationship to this vault, Geography and Major Locations (source summary), Geography Overview, Engineering memory (+4 more)

### Community 1393 - "DML Migrations Apply Paths"
Cohesion: 0.50
Nodes (3): Agent rule, DML Migrations Apply Paths, Facts

### Community 1394 - "days"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, days

### Community 1395 - "Chaosium CoC Catalog.md"
Cohesion: 0.15
Nodes (10): Evocations of the Inner God, The Hungry Void, Church of Sunyata, Dark Young of Shub-Niggurath, Flying Polyp, Fungi from Yuggoth, Ghoul, The Faceless Men (+2 more)

### Community 1396 - "effects"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, effects

### Community 1397 - "A Cold Fire Within (source summary)"
Cohesion: 0.50
Nodes (3): A Cold Fire Within (source summary), For MythosMUD design, Links

### Community 1398 - "Alone Against the Dark (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Dark (source summary), For MythosMUD design, Links

### Community 1399 - "Alone Against the Frost (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Frost (source summary), For MythosMUD design, Links

### Community 1400 - "Alone against the Tide (source summary)"
Cohesion: 0.50
Nodes (3): Alone against the Tide (source summary), For MythosMUD design, Links

### Community 1401 - "Berlin - The Wicked City (source summary)"
Cohesion: 0.50
Nodes (3): Berlin - The Wicked City (source summary), For MythosMUD design, Links

### Community 1402 - "Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary), For MythosMUD design, Links

### Community 1403 - "Call of Cthulhu Keeper Tips (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Keeper Tips (source summary), For MythosMUD design, Links

### Community 1404 - "Call of Cthulhu Starter Set (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Starter Set (source summary), For MythosMUD design, Links

### Community 1405 - "Call of Cthulhu_ The Coloring Book (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu_ The Coloring Book (source summary), For MythosMUD design, Links

### Community 1406 - "character_sheets (source summary)"
Cohesion: 0.50
Nodes (3): character_sheets (source summary), For MythosMUD design, Links

### Community 1407 - "Cthulhu Dark Ages - 3rd Edition (source summary)"
Cohesion: 0.50
Nodes (3): Cthulhu Dark Ages - 3rd Edition (source summary), For MythosMUD design, Links

### Community 1408 - "Does Love Forgive_ (source summary)"
Cohesion: 0.50
Nodes (3): Does Love Forgive_ (source summary), For MythosMUD design, Links

### Community 1409 - "Doors to Darkness (source summary)"
Cohesion: 0.50
Nodes (3): Doors to Darkness (source summary), For MythosMUD design, Links

### Community 1410 - "Down Darker Trails (source summary)"
Cohesion: 0.50
Nodes (3): Down Darker Trails (source summary), For MythosMUD design, Links

### Community 1411 - "Gateways to Terror (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Gateways to Terror (source summary), Links

### Community 1412 - "Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)

### Community 1413 - "The Grand Grimoire of Cthulhu Mythos Magic (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Grand Grimoire of Cthulhu Mythos Magic (source summary)

### Community 1414 - "The Malleus Monstrorum Keeper Deck (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Malleus Monstrorum Keeper Deck (source summary)

### Community 1415 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 1416 - "Migration Considerations"
Cohesion: 0.50
Nodes (4): Backward Compatibility, Data Migration, Migration Considerations, Performance Impact

### Community 1417 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Non-Functional Requirements, Success Criteria, User Experience Requirements

### Community 1418 - "Risk Assessment"
Cohesion: 0.50
Nodes (4): Implementation Risks, Risk Assessment, Technical Risks, User Experience Risks

### Community 1419 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Testing Strategy, Unit Tests, User Acceptance Tests

### Community 1420 - "Core Architectural Differences"
Cohesion: 0.50
Nodes (4): 1. **Structured Concurrency**, 2. **Backend Abstraction**, 3. **API Design Philosophy**, Core Architectural Differences

### Community 1421 - "Real-World Impact for MythosMUD"
Cohesion: 0.50
Nodes (4): Current Stack Compatibility, Migration Complexity, Performance Considerations, Real-World Impact for MythosMUD

### Community 1422 - "Detailed Feature Comparison"
Cohesion: 0.50
Nodes (4): Detailed Feature Comparison, Entry Points, Primitives, Task Management

### Community 1423 - "Recommendation for MythosMUD"
Cohesion: 0.50
Nodes (4): Option 1: Full Migration (Recommended for Long-Term), Option 2: Hybrid Approach (Pragmatic), Option 3: Stay with asyncio (Status Quo), Recommendation for MythosMUD

### Community 1424 - "📚 REFERENCES AND RESOURCES"
Cohesion: 0.50
Nodes (4): Best Practice Documents, External Resources, Investigation Reports, 📚 REFERENCES AND RESOURCES

### Community 1425 - "📊 METRICS AND SUCCESS CRITERIA"
Cohesion: 0.50
Nodes (4): Code Quality Metrics, 📊 METRICS AND SUCCESS CRITERIA, Performance Metrics, Test Coverage

### Community 1426 - "🚀 DEPLOYMENT STRATEGY"
Cohesion: 0.50
Nodes (4): 🚀 DEPLOYMENT STRATEGY, Monitoring Post-Deployment, Pre-Deployment Checklist, Rollback Plan

### Community 1427 - "end_hour"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 1428 - "Phase 2: Database Layer Integration"
Cohesion: 0.50
Nodes (4): 2.1 Persistence Layer Protection, 2.2 Database Connection Protection, 2.3 Configuration, Phase 2: Database Layer Integration

### Community 1429 - "Phase 3: Real-Time Communication Protection"
Cohesion: 0.50
Nodes (4): 3.1 NATS Integration, 3.2 WebSocket Protection, 3.3 Configuration, Phase 3: Real-Time Communication Protection

### Community 1430 - "Phase 4: File System Operations"
Cohesion: 0.50
Nodes (4): 4.1 Room Loading Protection, 4.2 Player Data File Operations, 4.3 Configuration, Phase 4: File System Operations

### Community 1431 - "Phase 6: Monitoring and Observability"
Cohesion: 0.50
Nodes (4): 6.1 Metrics Collection, 6.2 Health Check Endpoints, 6.3 Logging Integration, Phase 6: Monitoring and Observability

### Community 1432 - "Future Enhancements"
Cohesion: 0.50
Nodes (4): Advanced Features, Document metadata, Future Enhancements, Integration Opportunities

### Community 1433 - "Monitoring and Alerting"
Cohesion: 0.50
Nodes (4): Alerting Rules, Health Checks, Metrics to Monitor, Monitoring and Alerting

### Community 1434 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Monitoring Requirements, Performance Requirements, Success Criteria

### Community 1435 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Load Tests, Testing Strategy, Unit Tests

### Community 1436 - "🔬 Lessons Learned"
Cohesion: 0.50
Nodes (4): Challenges Encountered, 🔬 Lessons Learned, Solutions Applied, What Worked Well

### Community 1437 - "🛠️ Technical Achievements"
Cohesion: 0.50
Nodes (4): Code Quality, Performance, 🛠️ Technical Achievements, Test Organization

### Community 1438 - "🚀 How to Run Remaining Tests"
Cohesion: 0.50
Nodes (4): Docker-Based Testing (Zero bcrypt Issues), 🚀 How to Run Remaining Tests, Individual Module Testing (For Debugging), Quick Start (All Tests in One Fresh Session)

### Community 1439 - "WebSocket and SSE Dual Connections"
Cohesion: 0.50
Nodes (4): Dual Connection API Reference, WebSocket and SSE Dual Connections, Dual Connection Client Guide, Dual Connection Deployment Guide

### Community 1440 - "Context Management"
Cohesion: 0.50
Nodes (4): Context Management, Request Context, System Context, User Context

### Community 1441 - "MythosMUD Product Requirements"
Cohesion: 0.50
Nodes (4): Aggro System, Lucidity System, MythosMUD Product Requirements, Room-Based Combat

### Community 1442 - "Test Execution"
Cohesion: 0.50
Nodes (4): Run E2E Scenarios, Run Integration Tests, Run Unit Tests, Test Execution

### Community 1443 - "rename_used_to_is_active.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to rename used back to is_active. Args: database_url:…

### Community 1444 - "Cursor Subagents Documentation"
Cohesion: 0.50
Nodes (4): Cursor CLI Documentation, Cursor IDE Setup Guide, Cursor Subagents Documentation, Cursor Workflows Documentation

### Community 1445 - "Scenario Group Execution"
Cohesion: 0.50
Nodes (4): Scenario Group Execution, Local Channel Scenario Group (8-12), Logout Scenario Group (19-21), Whisper Channel Scenario Group (13-18)

### Community 1446 - "Main Foyer Starting Room"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 1447 - "Per-Recipient Whisper Rate Limiting"
Cohesion: 0.50
Nodes (4): Whisper System Remediation, Per-Recipient Whisper Rate Limiting, Global Whisper Rate Limit, Scenario 15 Rate Limiting Blocked

### Community 1448 - "Lucidity System Expansion Scenarios"
Cohesion: 0.67
Nodes (4): Lucidity System Expansion Scenarios, Catatonia Grounding Ritual Scenario, player_lucidity Ledger, Sanitarium Failover Escalation

### Community 1449 - "Container System"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 1450 - "Scenario 32 Disconnect Grace Period"
Cohesion: 0.50
Nodes (4): Scenario 32 Disconnect Grace Period, Linkdead Zombie State, Scenario 33 Rest Command, Scenario 35 Player Combat

### Community 1451 - "Catatonic Movement Prevention Bug"
Cohesion: 0.50
Nodes (4): Catatonic Movement Prevention Bug, WebSocket Go Command Unified Handler Bypass, current_room_id VARCHAR(50) Truncation, Movement Valid Exits Rejection Bug

### Community 1452 - "Rooms List SQL ::uuid[] Parameter Conflict"
Cohesion: 0.50
Nodes (4): asyncpg Colon Cast Parameter Parsing, Rooms List SQL ::uuid[] Parameter Conflict, Minimap Explored Rooms UUID vs stable_id, Explored Room UUIDs Treated As stable_ids

### Community 1453 - "Vite Best-Practices Remediation"
Cohesion: 0.50
Nodes (4): Test Suite Improvement, Vite Best-Practices Remediation, import.meta.env (Vite), Vitest Best-Practices Remediation

### Community 1454 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 1455 - "Shared JSON schemas"
Cohesion: 0.50
Nodes (4): alias_schema.json, emote_schema.json, Shared JSON schemas, unified_room_schema.json

### Community 1456 - "apply_migration"
Cohesion: 0.67
Nodes (3): apply_migration(), main(), Apply migration to a single database.

### Community 1457 - "main"
Cohesion: 0.67
Nodes (3): main(), Entry point: ensure collect_n quest seed and clear instances via anyio., _reset_collect_n_quest()

### Community 1459 - "_resolved_npm"
Cohesion: 0.67
Nodes (3): main(), Return absolute path to npm (prefer npm.cmd on Windows), or None if not found., _resolved_npm()

### Community 1460 - "start_server.ps1"
Cohesion: 0.50
Nodes (4): Default Server Port 54768, start_local.ps1, start_server.ps1, stop_server.ps1

### Community 1461 - "verify_schema_match.sh script"
Cohesion: 0.83
Nodes (3): find_pg_dump(), find_pg_isready(), verify_schema_match.sh script

### Community 1462 - "verify_tutorial_migrations.ps1"
Cohesion: 0.83
Nodes (3): Test-Migration08(), Test-Migration12(), Write-ColorOutput()

### Community 1463 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 1464 - "exits"
Cohesion: 0.50
Nodes (4): type, additionalProperties, type, exits

### Community 1465 - "validate_prototypes.py"
Cohesion: 0.50
Nodes (4): main(), parse_arguments(), Namespace, CLI entrypoint for validating MythosMUD item prototype definitions.

### Community 1466 - "1. Component Refactoring"
Cohesion: 0.50
Nodes (4): 1. Component Refactoring, ChatPanel.tsx Enhancements (New Chat Input Panel), CommandPanel.tsx Simplifications, GameLogPanel.tsx (Renamed from ChatPanel.tsx)

### Community 1467 - "Executive Summary"
Cohesion: 0.50
Nodes (4): Executive Summary, 🟡 IMPORTANT (Medium-Value):**~2,500-3,000 tests (50-60%) —**~15-18 minutes, Key Findings, Test Value Distribution

### Community 1470 - "Client Security and Privacy Policies"
Cohesion: 0.67
Nodes (3): Client Security and Privacy Policies, DOMPurify Sanitization, WebSocket Subprotocol Auth

### Community 1471 - "MythosMUD UI Component Library"
Cohesion: 0.67
Nodes (3): Mythos Terminal Theme Tokens, StatusPanel, MythosMUD UI Component Library

### Community 1472 - "UUID"
Cohesion: 0.40
Nodes (3): UUID, Publish a correction event when database persistence fails., Persist player DP to database in background (fire-and-forget). This method runs…

### Community 1474 - ".validate_parameter_value"
Cohesion: 0.50
Nodes (3): Any, Validate all parameters used in the pattern. Args: pattern: Pattern template…, Validate a parameter value. Args: param_name: Name of the parameter…

### Community 1475 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 1476 - "registry_with_switchblade"
Cohesion: 0.40
Nodes (5): fixture, Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade)., PrototypeRegistry containing only the switchblade., registry_with_switchblade(), switchblade_prototype()

### Community 1504 - "Expansion Backlog (Raw)"
Cohesion: 0.67
Nodes (3): Delta Green, Expansion Backlog (Raw), Things and Notes to Expand On

### Community 1505 - "Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition Keeper Screen Pack (source summary), For MythosMUD design, Links

### Community 1506 - "Call of Cthulhu Investigator Handbook 7th Edition (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Investigator Handbook 7th Edition (source summary), For MythosMUD design, Links

### Community 1507 - "Dead Light and Other Dark Turns (source summary)"
Cohesion: 0.50
Nodes (3): Dead Light and Other Dark Turns (source summary), For MythosMUD design, Links

### Community 1508 - "Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)

### Community 1509 - "Petersen's Abominations.md"
Cohesion: 0.13
Nodes (10): Chaosium catalog notes, Voice on the Phone, Dimensional Shambler, Key extrated pages, Petersen's Abominations (source summary), Hotel Hell, Mohole, Cosmic Horror (+2 more)

### Community 1510 - "Paris (Reign of Terror).md"
Cohesion: 0.18
Nodes (7): Dietrich Zann, Key extrated pages, Reign of Terror (source summary), Paris (Reign of Terror), Azotottal, Comte Fenalik, Reign of Terror

### Community 1511 - "test_websocket_handler_disconnect.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler disconnect handling. Tests the disconnect…, Test _handle_websocket_disconnect() returns True., Test _handle_websocket_disconnect() with no connection_id., test_handle_websocket_disconnect(), test_handle_websocket_disconnect_no_connection_id()

### Community 1512 - "What Are They?"
Cohesion: 0.67
Nodes (3): `anyio` (Third-Party Library), `asyncio` (Python Standard Library), What Are They?

### Community 1513 - "Character Creation Revamp"
Cohesion: 0.67
Nodes (3): Character Creation Revamp, CoC-Style Skills Allocation, Skill Use Tracking and Level-Up Improvement

### Community 1514 - "Comprehensive System Audit"
Cohesion: 0.67
Nodes (3): CI/CD Enhanced Logging Validation, Comprehensive System Audit, Database Migration Guide

### Community 1515 - "Architecture Overview"
Cohesion: 0.67
Nodes (3): Architecture Overview, CircuitBreaker States, Integration Points

### Community 1516 - "Dead Code Cleanup Completion"
Cohesion: 0.67
Nodes (3): Legacy Files Cleanup Summary, Dead Code Cleanup Completion, Dead Code Cleanup Planning

### Community 1517 - "Single Session Per User"
Cohesion: 0.67
Nodes (3): force_disconnect_player, Single Session Per User, Player Spawn Protection

### Community 1518 - "🎯 Next Steps"
Cohesion: 0.67
Nodes (3): Future Enhancements, Immediate Actions, 🎯 Next Steps

### Community 1519 - "Fixture Optimization Complete"
Cohesion: 0.67
Nodes (3): E2E Testing Setup Status, Fixture Optimization Complete, Test Suite Post-Merge Refactoring

### Community 1520 - "Test Warning Remediation"
Cohesion: 0.67
Nodes (3): Early Logging Initialization, datetime.utcnow Deprecation Fix, Test Warning Remediation

### Community 1521 - "Enhanced Logging Migration Complete"
Cohesion: 0.67
Nodes (3): Enhanced Logging Implementation Complete, Enhanced Logging Implementation Summary, Enhanced Logging Migration Complete

### Community 1522 - "Random Stats Generator Planning"
Cohesion: 0.67
Nodes (3): Pydantic Click Command Validation Integration, Random Stats Generator Technical Plan, Random Stats Generator Planning

### Community 1523 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 1524 - "Party System Reference"
Cohesion: 0.67
Nodes (3): Party Invite Command, Party System Reference, Ephemeral Grouping Party Planning

### Community 1525 - "Archive Directory README"
Cohesion: 0.67
Nodes (3): Archive Directory README, HADS Archive Exclusion, PLANNING.md Single Source of Truth

### Community 1526 - "Structured Error Logging"
Cohesion: 0.67
Nodes (3): Structured Error Logging, log_and_raise Utilities, Test/Production Environment Separation

### Community 1527 - "Test File Migration Mapping"
Cohesion: 0.67
Nodes (3): Test Suite Hierarchical Migration, Test File Migration Mapping, Test Suite Refactoring Deliverables

### Community 1528 - "Who Command Enhancement"
Cohesion: 0.67
Nodes (3): Who Command Name Filtering, Who Command Enhancement, Who Command Implementation Tasks

### Community 1529 - "10 Concurrent Players Load Test"
Cohesion: 0.67
Nodes (3): who Command Unawaited Coroutine Bug, 10 Concurrent Players Load Test, Load Test Suite

### Community 1530 - "Scenario 20 Logout Errors"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 1531 - "Scenario 34 Two Players Same Room Visibility"
Cohesion: 0.67
Nodes (3): Scenario 34 Two Players Same Room Visibility, Scenario 36 Movement Visibility, Scenario 37 Chat Message Ordering

### Community 1532 - "E2E Session Report 2025-12-02"
Cohesion: 0.67
Nodes (3): Admin Teleportation Display Bug, E2E Session Report 2025-12-02, Whisper Messages Not Received Bug

### Community 1533 - "Playwright MCP Primary Testing Tool"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 1534 - "Whisper NATS Subject Bug Fix"
Cohesion: 0.67
Nodes (3): chat.whisper.player Subject Segment, Whisper NATS Subject Bug Fix, Whisper Work Completed and Remaining

### Community 1535 - "Dependency Review Workflow"
Cohesion: 0.67
Nodes (3): Dependabot Dependency Updates, Dependency Review Workflow, UV Lock Dependency Snapshot Gate

### Community 1536 - "Impeccable design context"
Cohesion: 0.67
Nodes (3): Impeccable design context, Legibility under pressure, Dark terminal-first aesthetic

### Community 1537 - "NPCs Not Updating On Player Movement"
Cohesion: 0.67
Nodes (3): exclude_player Occupants Snapshot Pattern, NPCs Not Updating On Player Movement, Canonical Room ID NPC Matching Remediation

### Community 1538 - "Combat Messages Dual Panel Display"
Cohesion: 0.67
Nodes (3): Combat Turn Order UUID Display, Combat Messages Dual Panel Display, Missing NPC Death Message Handlers

### Community 1539 - "Test Suite Stall After Performance Comparison"
Cohesion: 0.67
Nodes (3): Docker Build mythos_unitql Typo, Test Suite Stall After Performance Comparison, thread.join Without Timeout Hang

### Community 1540 - "Client Updates System Audit"
Cohesion: 0.67
Nodes (3): Architecture Review Plan, Option C Replacement Client Updates, Client Updates System Audit

### Community 1541 - "Cursor Rules as Canonical Config"
Cohesion: 0.67
Nodes (3): Cursor-Centric AI Config, Cursor Rules as Canonical Config, GitHub Worktrees Cursor Setup

### Community 1542 - "Logging Aggregator Verification"
Cohesion: 0.67
Nodes (3): Logging Aggregator Verification, warnings.log and errors.log Aggregators, Structlog Anti-Pattern Remediation

### Community 1543 - "Memory Leak Remediation"
Cohesion: 0.67
Nodes (3): Closed WebSockets Deque Cap, Memory Leak Metrics Collection, Memory Leak Remediation

### Community 1544 - "Playwright DI Migration Validation"
Cohesion: 0.67
Nodes (3): Playwright Best-Practices Remediation, Playwright DI Migration Validation, E2E Harness Overhaul

### Community 1545 - "Server Authority Remediation"
Cohesion: 0.67
Nodes (3): game_state Room Replace (not Merge), Server Authority Remediation, Server Authority Rule

### Community 1554 - "holiday"
Cohesion: 0.50
Nodes (4): $defs, holiday, additionalProperties, type

### Community 1555 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1556 - "test_websocket_handler_helpers.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler helper functions. Tests the helper functions…, Test _is_websocket_disconnected() returns True for disconnection messages., Test _is_websocket_disconnected() returns False for other messages., test_is_websocket_disconnected_false(), test_is_websocket_disconnected_true()

### Community 1557 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 1558 - "TestGetPlayerService"
Cohesion: 0.33
Nodes (4): Test get_player_service() function., Test get_player_service() returns player service from container., Test get_player_service() raises error when service not initialized., TestGetPlayerService

### Community 1559 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1560 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1561 - "long_description"
Cohesion: 0.50
Nodes (4): maxLength, minLength, type, long_description

### Community 1562 - "prototype_id"
Cohesion: 0.50
Nodes (4): prototype_id, maxLength, minLength, type

### Community 1563 - "short_description"
Cohesion: 0.50
Nodes (4): short_description, maxLength, minLength, type

### Community 1564 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1565 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1566 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1567 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1568 - "integration"
Cohesion: 0.40
Nodes (5): integration(), mock_persistence(), fixture, Persistence mock with async get_player_by_id for integration tests., NPCCombatIntegration wired to the mock persistence layer.

### Community 1569 - ".use_invite"
Cohesion: 0.40
Nodes (3): UUID, Mark an invite as used by a specific user (atomic auth-and-capture). Uses the…, Get all invites used by a user.

### Community 1570 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1571 - "PlayerStatsConfig"
Cohesion: 0.20
Nodes (8): PlayerStatsConfig, Any, BaseSettings, field_validator, Default player statistics configuration., Validate stats are in valid range., Validate derived stats values., Convert to dictionary format expected by game code.

### Community 1573 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1574 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1575 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1579 - "message_filtering_helper"
Cohesion: 0.40
Nodes (5): message_filtering_helper(), mock_connection_manager(), fixture, Create a mock connection manager., Create a MessageFilteringHelper instance.

### Community 1580 - "subject_manager_no_cache"
Cohesion: 0.40
Nodes (5): fixture, Create NATSSubjectManager without metrics., Create NATSSubjectManager without cache., subject_manager_no_cache(), subject_manager_no_metrics()

### Community 1589 - "player_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), player_service(), fixture, Create a mock persistence layer., Create a PlayerService instance.

### Community 1590 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1592 - ".sample_holidays"
Cohesion: 0.40
Nodes (3): fixture, Create a mock chronicle for testing., Create sample holiday entries for testing.

### Community 1593 - "test_validate_secure_path_path_traversal_commonpath"
Cohesion: 0.33
Nodes (4): Test validate_secure_path normalizes backslashes., Test validate_secure_path detects path traversal via commonpath check., test_validate_secure_path_path_traversal_commonpath(), test_validate_secure_path_with_backslash()

### Community 1594 - "Lucidity.md"
Cohesion: 0.24
Nodes (5): Lucidity, Pandora's Box (Pulp campaign), Using Luck (Pulp), Key extrated pages, Pulp Sanity

### Community 1677 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 1680 - "PlayerSearchService"
Cohesion: 0.17
Nodes (8): PlayerSearchService, Any, Search for players by name with fuzzy matching. This method returns multiple…, Validate a player name for chat system use. This checks if the name is valid…, Service for player search and validation operations., Initialize with a reference to the player service for data access., Resolve a player name with fuzzy matching and case-insensitive search. This…, Get a list of currently online players. Note: This is a placeholder…

### Community 1684 - "TestGetProfessionService"
Cohesion: 0.50
Nodes (3): Tests for get_profession_service dependency function., Test get_profession_service creates service with persistence., TestGetProfessionService

### Community 1686 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1687 - "name"
Cohesion: 0.50
Nodes (4): description, minLength, type, name

### Community 1689 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1691 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1695 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 1696 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1698 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1699 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1700 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1701 - "npc_spawn_modifier"
Cohesion: 0.50
Nodes (4): description, minimum, type, npc_spawn_modifier

### Community 1702 - "special_rules"
Cohesion: 0.50
Nodes (4): special_rules, additionalProperties, description, type

### Community 1710 - "id"
Cohesion: 0.67
Nodes (3): minLength, type, id

### Community 1711 - "plane"
Cohesion: 0.67
Nodes (3): minLength, type, plane

### Community 1712 - "Security Considerations"
Cohesion: 0.67
Nodes (3): Data Sanitization, Security Considerations, Sensitive Data Protection

### Community 1713 - "enum"
Cohesion: 0.50
Nodes (4): enum, indoors, outdoors, underwater

### Community 1714 - "8. Error Handling and Debugging"
Cohesion: 0.67
Nodes (3): 8. Error Handling and Debugging, Common Debug Commands, Test Debugging

### Community 1715 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1717 - "metadata"
Cohesion: 0.67
Nodes (3): additionalProperties, type, metadata

### Community 1719 - "party_service"
Cohesion: 0.67
Nodes (3): party_service(), fixture, PartyService with no dependencies (in-memory only).

### Community 1723 - "_iter_exception_chain"
Cohesion: 0.67
Nodes (3): _iter_exception_chain(), BaseException, Walk __cause__/__context__ without looping.

### Community 1736 - "metrics"
Cohesion: 0.67
Nodes (3): metrics(), fixture, Create SubjectManagerMetrics instance.

## Knowledge Gaps
- **6249 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `JCODEMUNCH_MAX_FOLDER_FILES`, `@codacy/codacy-mcp` (+6244 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **550 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `NPCCombatIntegrationService`, `LucidityService`, `game_tick_protocols.py`, `npc_database.py`, `NPCBase`, `real_time.py`, `_ensure_connection_manager`, `BaseCommand`, `server/dependencies.py`, `PlayerService`, `TransferContainerRequest`, `game_tick_death.py`, `CombatParticipant`, `NPCDefinition`, `sqlalchemy.md`, `get_npc_instance_service`, `ContainerData`, `CombatService`, `test_npc_utils.py`, `LootAllRequest`, `api/character_creation.py`, `TargetMatch`, `PlayerNameExtractor`, `ContainerServiceError`, `test_container_bundles.py`, `test_lifecycle_respawn.py`, `test_rest_command.py`, `NPCStartupService`, `factory.py`, `FollowService`, `server/models/game.py`, `PlayerEnteredRoom`, `test_inventory_helpers.py`, `inventory_equip_command.py`, `server/exceptions.py`, `TargetResolutionService`, `is_player_in_login_grace_period`, `test_connection_delegates.py`, `ZoneConfiguration`, `chat_service.py`, `server/schemas/__init__.py`, `command_handler_unified.py`, `test_look_item.py`, `config/models/__init__.py`, `admin_shutdown_command.py`, `test_chat_pose_helpers.py`, `test_go_command.py`, `test_rescue_service.py`, `test_users.py`, `extract_player_name`, `test_combat_flee_handler.py`, `test_command_validator.py`, `NATSError`, `communication_commands_flows.py`, `test_look_container.py`, `test_player_respawn_service.py`, `test_admin_commands.py`, `test_emote_repository.py`, `NATSConnectionStateMachine`, `test_cache_service.py`, `test_who_commands.py`, `ExplorationService`, `look_helpers.py`, `initialize_components`, `item_instance_persistence.py`, `connection_cleanup_methods.py`, `test_websocket_initial_state.py`, `lucidity_migration.py`, `test_lucidity_event_dispatcher.py`, `test_chat_npc_system.py`, `api/player_effects.py`, `catatonia_check.py`, `CombatInstance`, `test_auth_utils.py`, `test_room_sync_service.py`, `EventBus`, `handle_emote_command`, `admin_teleport_commands.py`, `player_event_handlers_state.py`, `DistributedEventBus`, `spell_repository.py`, `test_combat_monitoring_service.py`, `test_corpse_lifecycle_service.py`, `npc_combat_grace.py`, `test_websocket_room_updates.py`, `test_real_time_helpers.py`, `QuestService`, `api/monitoring.py`, `test_player_presence_tracker.py`, `test_look_player.py`, `FeatureFlagService`, `skills_commands.py`, `Player`, `PlayerCombatService`, `player_inventory_migration.py`, `test_metrics_endpoints.py`, `test_status_commands.py`, `connection_manager_methods.py`, `WebSocketMessageValidator`, `ChatMessage`, `ErrorType`, `admin_setstat_command.py`, `migrate_combat_data.py`, `pytest.md`, `test_websocket_handler_app_state_connection.py`, `websocket_handler_commands.py`, `TaskRegistry`, `talk_command.py`, `error_handling_middleware.py`, `NPCOccupantProcessor`, `MovementMonitor`, `CombatConfiguration`, `lifespan_startup.py`, `repositories/__init__.py`, `room_service.py`, `test_zone_config_loader.py`, `test_lucidity_recovery_commands.py`, `apply_communication_dampening`, `test_admin_setlucidity_command.py`, `test_shutdown_sequence.py`, `OccupantFormatter`, `event_types.py`, `server/services/__init__.py`, `ValidationError`, `IdleMovementHandler`, `NPCEventReaction`, `test_player_disconnect_handlers.py`, `.read_token`, `middleware`, `InventoryMutationGuard`, `server/main.py`, `test_wearable_container_service.py`, `CombatAuditLogger`, `system_monitoring.py`, `websocket_handler.py`, `MovementService`, `Room`, `RoomEventHandler`, `command_result_text`, `LogAggregator`, `MemoryMonitor`, `.state`, `test_chat_validator.py`, `PerformanceMonitor`, `test_lucidity_command_disruption.py`, `player_effect_repository.py`, `websocket_helpers.py`, `AliasStorage`, `DatabaseError`, `lifespan_protocols.py`, `test_logout_commands.py`, `build_event`, `test_lifecycle_periodic.py`, `NPCCombatUUIDMapping`, `InstanceManager`, `SpellEffects`, `channel_broadcasting_strategies.py`, `fixtures/integration/__init__.py`, `InventorySchemaValidationError`, `test_email_utils.py`, `connection_establishment.py`, `CoordinateValidator`, `test_hallucination_services.py`, `ContainerLockState`, `test_chat_nats_publisher.py`, `test_look_room.py`, `NPCCombatLucidity`, `ExceptionTracker`, `PlayerPositionService`, `test_rate_overrides.py`, `HealthStatus`, `NPCCombatDataProvider`, `test_party_commands.py`, `PlayerDeathService`, `admin_summon_command.py`, `test_inventory_display_helpers.py`, `handle_read_command`, `debrief_command.py`, `test_occupants.py`, `CoordinateGenerator`, `game_tick_processing.py`, `test_map_helpers.py`, `test_player_occupant_processor.py`, `PrototypeRegistryError`, `message_handler_factory.py`, `test_goto_helpers.py`, `Any`, `test_follow_commands.py`, `PlayerPreferencesService`, `MemoryLeakMetricsCollector`, `LoggedHTTPException`, `NPCActionMessage`, `WebSocketRequestContext`, `add_fastapi_users_columns.py`, `add_hashed_password_column.py`, `combat_messaging/base.py`, `add_used_by_user_id_column.py`, `DialogueDefinitionRepository`, `rename_invites_columns.py`, `service.py`, `server/tests/conftest.py`, `log_and_raise_enhanced`, `TrackedTaskManager`, `retry.py`, `quest_commands.py`, `Profession`, `test_channel_commands.py`, `CORSConfig`, `resolve_weapon_attack_from_equipped`, `look_command.py`, `inventory_command_helpers.py`, `player_connection_setup.py`, `StatsGenerator`, `inventory_get_command.py`, `disconnect_grace_period.py`, `rename_used_to_is_active.py`, `test_game_tick_death.py`, `MessageBroadcaster`, `CombatCommandHandler`, `spell_effects_support.py`, `validate_prototypes.py`, `EmoteService`, `PersonalMessageSender`, `GameMechanicsService`, `log_and_raise`, `test_look_npc.py`, `npc_config_parsing.py`, `inventory_unequip_command.py`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Why does `RoomSubscriptionManager` connect `connection_manager_methods.py` to `test_connection_session_management.py`, `test_room_subscription_manager_npcs.py`, `get_logger`, `test_room_subscription_manager_helpers.py`, `test_room_subscription_manager.py`, `RoomEventHandler`, `ConnectionManager`, `test_room_subscription_manager_drops.py`, `MessageBroadcaster`, `ConnectionManager`, `connection_establishment.py`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `LoggedHTTPException` connect `LoggedHTTPException` to `real_time.py`, `test_metrics_endpoints.py`, `_ensure_connection_manager`, `BaseCommand`, `PlayerService`, `pytest.md`, `LootAllRequest`, `api/character_creation.py`, `InviteManager`, `error_handling_middleware.py`, `HealthStatus`, `.use_invite`, `server/exceptions.py`, `.validate_invite`, `StandardizedErrorResponse`, `server/schemas/__init__.py`, `system_monitoring.py`, `ExplorationService`, `api/player_effects.py`, `test_error_handling_middleware.py`, `test_real_time_helpers.py`, `api/monitoring.py`?**
  _High betweenness centrality (0.019) - this node is a cross-community bridge._
- **Are the 141 inferred relationships involving `LoggedHTTPException` (e.g. with `test_get_admin_sessions_error()` and `test_get_npc_population_stats_generic_error()`) actually correct?**
  _`LoggedHTTPException` has 141 INFERRED edges - model-reasoned connections that need verification._
- **Are the 192 inferred relationships involving `ValidationError` (e.g. with `fetch_user_by_username_case_insensitive()` and `load_database_url()`) actually correct?**
  _`ValidationError` has 192 INFERRED edges - model-reasoned connections that need verification._
- **Are the 81 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 81 INFERRED edges - model-reasoned connections that need verification._
- **Are the 73 inferred relationships involving `AliasStorage` (e.g. with `_handle_special_command_routing()` and `_prepare_command_for_processing()`) actually correct?**
  _`AliasStorage` has 73 INFERRED edges - model-reasoned connections that need verification._