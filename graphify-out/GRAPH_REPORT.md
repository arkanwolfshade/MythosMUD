# Graph Report - MythosMUD  (2026-08-26)

## Corpus Check
- 3268 files · ~2,952,382 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 54383 nodes · 101966 edges · 2133 communities (1685 shown, 448 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 5760 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `018019dd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- get_logger
- models/player.py
- PlayerLeftRoom
- NPCBase
- npc_database.py
- DatabaseError
- BaseCommand
- server/dependencies.py
- ValidationError
- ContainerComponent
- api/character_creation.py
- container_events.py
- test_security_validator.py
- CombatParticipant
- connection_manager_methods.py
- Player
- get_npc_instance_service
- players.py
- combat_turn_participant_actions.py
- test_container_persistence_async_helpers.py
- mythos_dev_ddl.sql
- AliasStorage
- test_combat_event_publisher.py
- AsyncPersistenceLayer
- CombatService
- inventory_command_helpers.py
- container_endpoints_basic.py
- roll_character_stats
- SpellEffects
- PlayerNameExtractor
- test_look_npc.py
- ContainerServiceError
- test_container_bundles.py
- test_connection_session_management.py
- get_username_from_user
- PlayerPositionService
- PlayerRoomEventHandler
- test_connection_establishment.py
- NATSService
- ChatService
- ui-v2/types.ts
- factory.py
- test_follow_service.py
- Stats
- test_command_inventory.py
- CommandFactory
- Communities (355 total, 223 thin omitted)
- server/services/__init__.py
- test_exceptions.py
- TargetResolutionService
- request_with_app_container
- is_player_in_login_grace_period
- NPCCombatDataProvider
- NPCDefinition
- chat_service.py
- test_npc_definitions_api.py
- lifespan_magic.py
- SpellEffectType
- test_admin_auth_service.py
- command_handler_unified.py
- test_nats_message_handler.py
- handle_transfer_items_exceptions
- RoomService
- test_admin_shutdown_command.py
- test_user_manager.py
- test_go_command.py
- test_command_factories_utility.py
- test_users.py
- CombatInstance
- combat_service.py
- test_command_validator.py
- RoomLoader
- communication_commands_flows.py
- test_look_container_helpers.py
- test_command_moderation.py
- eventHandlers/types.ts
- event_types.py
- ApplicationContainer
- test_admin_commands.py
- test_combat_persistence_handler_events.py
- NATSConnectionStateMachine
- StatusEffect
- item_instance_persistence_async.py
- format_player_entry
- User
- test_look_helpers.py
- ExplorationCommandFactory
- ContainerData
- Any
- test_websocket_initial_state.py
- NATSError
- test_look_container.py
- ConnectionManager
- test_chat_npc_system.py
- test_player_requests.py
- catatonia_check.py
- test_aggro_threat.py
- create_access_token
- test_room_sync_service.py
- EventBus
- rescue_commands.py
- test_containers.py
- NATSSubjectManager
- DistributedEventBus
- test_npc_utils.py
- test_combat_monitoring_service.py
- test_lifespan_startup.py
- command_result_text
- NPCCombatIntegrationService
- test_auth_utils.py
- PanelState
- test_container_helpers_inventory_find.py
- build_event
- real_time.py
- test_container_helpers_inventory_ops.py
- QuestService
- api/monitoring.py
- useMythosAppActions.ts
- test_player_presence_tracker.py
- test_logging_utilities.py
- test_look_player.py
- UserManager
- MythosMUDError
- FeatureFlagService
- Reporter
- PlayerService
- test_player_death_service.py
- test_connection_helpers_impl.py
- useRespawnHandlers.ts
- _as_mgr
- test_quest_service.py
- test_communication_commands_flows.py
- PlayerCombatService
- deleteCharacterFlow.ts
- mythos_e2e_ddl.sql
- test_metrics_endpoints.py
- test_status_commands.py
- mythos_unit_ddl.sql
- connection_manager.py
- WebSocketMessageValidator
- test_magic_commands.py
- test_npc_service.py
- SchemaValidator
- ChatMessage
- manual_dependency_analysis.py
- ErrorType
- GameStateProvider
- Any
- NATSRetryHandler
- test_websocket_handler_validation_errors.py
- test_nats_broker.py
- migrate_combat_data.py
- LoggedHTTPException
- ContainerRepository
- 1774539086359-useMythosAppState.ts
- TaskRegistry
- DialogueService
- RoomIDUtils
- CombatConfiguration
- test_game_state_provider.py
- test_npc_event_handlers.py
- chat_channel_message_senders.py
- lifespan_startup.py
- test_command_processor.py
- map_minimap.py
- test_zone_config_loader.py
- test_lucidity_recovery_commands.py
- test_quest_events.py
- test_communication_commands_say_me_pose.py
- test_message_handlers.py
- test_admin_setlucidity_command.py
- test_combat_flee_helpers.py
- test_shutdown_sequence.py
- OccupantFormatter
- NPCLifecycleManager
- ScheduleService
- test_database_helpers.py
- test_party_service.py
- PlayerRespawnService
- test_nats_message_handler_chat.py
- waitForMessage
- test_logging_handlers.py
- test_websocket_handler_helpers_extended.py
- IdleMovementHandler
- PassiveMobNPC
- test_player_disconnect_handlers.py
- middleware
- InventoryMutationGuard
- get_config
- test_websocket_handler_core.py
- test_lucidity_event_dispatcher.py
- CombatAuditLogger
- test_wearable_container_service.py
- MemoryProfiler
- system_monitoring.py
- useGameClientV2Container.ts
- ContainerService
- test_websocket_helpers.py
- logging_file_setup.py
- quest_service.py
- Room
- test_health_monitor.py
- test_player_event_handlers_room.py
- PlayerStateCommandFactory
- get_player_quests
- RoomEventHandler
- admin_mute_commands.py
- test_metrics.py
- LogAggregator
- test_room_renderer.py
- ChatHistoryPanel.tsx
- Async Remediation Summary - December 3, 2025
- test_rescue_commands.py
- chat_nats_publisher.py
- PerformanceMonitor
- NPCCombatIntegration
- test_invite_schemas.py
- player.ts
- MonitoringDashboard
- resolve_lazy_attr
- test_communication_commands_channels.py
- test_skill_service.py
- lifespan_protocols.py
- test_logout_commands.py
- AggressiveMobNPC
- CombatEventHandler
- container_query_helpers_async.py
- test_lifecycle_periodic.py
- test_error_handling_middleware.py
- EventHandler
- CatatoniaRegistry
- GameClientV2Dock.test.tsx
- NPCCombatUUIDMapping
- PhantomHostileService
- test_command_service.py
- ._init_player_quest_layer
- validate_room_data
- _MagicServiceCore
- websocket_handler.py
- asyncio
- security.ts
- RoomMapViewer.tsx
- session_factory
- test_level_service.py
- InventorySchemaValidationError
- NPCOccupantProcessor
- test_websocket_messages.py
- ModerationCommandFactory
- devDependencies
- StyleGuideSections.tsx
- PlayerGuidFormatter
- GameEvent
- Any
- .state
- fixtures/auth.ts
- dialogue_definitions_api.py
- GameTickService
- useGameConnectionRefactored.ts
- testing_examples.py
- quality_fragmentation_ai_guardrails.py
- gen_arena_migration_sql.py
- test_exceptions_comprehensive.py
- combat_taunt.py
- CombatMonitoringService
- test_combat_service.py
- test_rescue_service.py
- systemHandlers.ts
- http_exception_handler
- EnvironmentalContainerLoader
- test_chat_nats_publisher.py
- NATSServicePoolMixin
- test_player_service_mutations.py
- models/combat.py
- test_look_room.py
- HealthErrorResponse
- ExceptionTracker
- NPCCombatIntegrationReadApi
- test_windows_safe_rotation.py
- test_rate_limiter.py
- get_global_tracked_manager
- utils/layout.ts
- time_event_consumer.py
- test_connection_state_machine.py
- test_rate_overrides.py
- test_validation.py
- ResourceManager
- HealthStatus
- test_combat_handler.py
- health_service
- MythosTickScheduler
- utils/config.ts
- MemoryMonitor
- ✅ Phase 2 Async Persistence Migration - COMPLETE
- MythosMUD Test Suite Modernization Plan
- MemoryThresholdMonitor
- logout_commands.py
- field_validator
- item_instance_persistence.py
- alias_schema.json
- test_party_commands.py
- NATSMessageBroker
- TestRoomDataFixer
- Profession
- safe_run_static
- test_admin_summon_command.py
- test_inventory_display_helpers.py
- handle_read_command
- PlayerRepositoryProtocol
- AdminActionsLogger
- debrief_command.py
- test_nats_messages.py
- RoomMapEditorRuntime.tsx
- CoordinateGenerator
- SpellLearningService
- test_command_utility.py
- DialogueEditorPage.tsx
- useMythosAppState.ts
- RoomDataValidator
- App.tsx
- endpoints.py
- ConnectionCleaner
- test_pattern_matcher.py
- test_player_event_handlers_respawn.py
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
- _str_id
- Stats
- collect_inventory.py
- test_shopkeeper_npc.py
- StatisticsAggregator
- websocket_handler_commands.py
- test_memory_leak_metrics.py
- test_audit_logger.py
- Uplift Strategy
- Test Suite Optimization Roadmap
- Test Suite Refactoring Plan
- Test Value Distribution Chart
- api/player_respawn.py
- test_connection_statistics.py
- test_websocket_handler_coverage_gaps.py
- HolidayCollection
- ChatLogger
- test_calendar.py
- AsciiMapViewer.tsx
- revised-character-creation.spec.ts
- test_message_formatters.py
- CombatCommandHandler
- PlayerDeathService
- test_npc_combat_handlers.py
- WebSocket Best Practices
- edgeModalLogic.ts
- vim Best Practices and Coding Standards
- Async Code Review - Post Phase 2 Migration
- FastAPI Code Review - Anti-Patterns and Best Practices
- E2E Test Suite AI Execution Improvements - Summary
- NPCCombatIntegrationBase
- DialogueDefinitionRepository
- test_connection_cleaner.py
- TestHierarchicalSchema
- LucidityFluxService
- _track_player_presence
- properties
- properties
- properties
- _parse_stat_datetime
- TrackedTaskManager
- test_admin_teleport_commands.py
- test_status_commands_helpers.py
- SpellMaterialsService
- test_lint_raw_sql_in_python.py
- test_rest_and_grace_period.py
- retry.py
- TestCombatConfigurationService
- properties
- Any
- ErrorContext
- nats_broker.py
- test_users_current_user_logging.py
- get_async_session
- quest_commands.py
- CORSConfig
- resolve_weapon_attack_from_equipped
- test_rate_limiter_utils.py
- test_room_utils.py
- log_with_context
- maps.ts
- 🧪 MythosMUD E2E Testing Strategy
- correct_patterns.py
- look_command.py
- test_game_tick_processing_async.py
- inventory_pickup_command.py
- player_connection_setup.py
- HolidayService
- lucidity_trigger_handlers.py
- test_subscription_patterns.py
- _format_npc_description
- test_message_broadcaster.py
- properties
- GameClientV2ContainerView.tsx
- Memory Leak Prevention System - Implementation Summary
- deprecated_patterns.py
- test_quality_fragmentation_guard.py
- parse_last_active_datetime
- test_profession_repository.py
- RoomCacheService
- equipment_helpers.py
- test_skills.py
- ._cleanup_player_mutes
- pytest.md
- disconnect_grace_period.py
- TestCombatMessagingService
- WebSocketRateLimiter
- look_npc.py
- test_magic_service.py
- field_validator
- test_flee_command.py
- test_player_service.py
- test_room_subscription_manager_helpers.py
- test_command_parser_helpers.py
- useRoomEditModal.ts
- multiplayer-browser-helpers.js
- Chat Panel Separation Implementation Tasks
- Async Persistence Migration Plan
- migration_examples.py
- asyncio
- MessageBroadcaster
- combat_loader.py
- test_logout_commands_helpers.py
- spell_effects_support.py
- _parse_npc_stats_dict
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
- test_container_persistence_extended_crud.py
- PayloadOptimizer
- LoggedException
- .load_room_data
- CharacterNameScreen.tsx
- required
- Async Persistence Migration Tracker
- PostgreSQL & SQL Audit Report
- LRUCache
- GameMechanicsService
- test_container_persistence_extended_row_helpers.py
- test_container_persistence_sql_injection.py
- TestNPCCombatRewards
- test_metadata.py
- 3. Common Patterns and Anti-patterns
- File-by-File Changes
- MemoryLeakMetricsCollector
- enum
- test_combat_schema.py
- ConnectionErrorHandler
- NPCThreadManager
- test_event_publisher.py
- mock_connection_manager
- test_player_preferences_service.py
- roomHandlers.ts
- authenticated.ts
- ._execute_wander_movement
- AsciiMapRenderer
- test_who_commands.py
- ChatChannelLoggerMixin
- _find_item_in_equipped
- .create_cast_command
- create_hasher_with_params
- MotdInterstitialScreen.tsx
- Test Pruning Candidates - Detailed List
- test_passive_lucidity_flux_service.py
- FStringLoggingFixer
- Stop-MythosMudProjectProcessTree
- test_game_tick_processing.py
- processing.py
- ItemPrototypeModel
- who_commands.py
- PersonalMessageSender
- ._handle_exception
- test_npc_combat_integration_service_npc_aggro.py
- containers.sql
- e2e-bootstrap.ts
- Chaosium CoC Catalog
- mythos_dev.players
- Phase 1: Core Separation
- test_magic_healing_events.py
- CommandRateLimiter
- _NPCCombatIntegrationValidationDeps
- Phase 2: Enhanced Features
- subzone_schema.json
- Async Audit Executive Summary
- TEMPORAL_SYSTEM_RESEARCH.md
- async_sessionmaker
- Prometheus Configuration
- load_world_seed.py
- validate.py
- ReactNodeUpgradeAnalyzer
- game_tick_processing.py
- _find_item_in_inventory
- run_flee_effect
- NPCCommunicationIntegration
- combat_schema.py
- test_npc_combat_integration_service_player_attacks.py
- test_combat_validator.py
- CombatValidator
- test_optimized_security_validator.py
- MinimapRenderer
- scripts
- map/config.ts
- type
- P8 · Applied
- properties
- NATS Code Review - Branch: feature/sqlite-to-postgresql
- WebSocket Code Review - Branch: feature/sqlite-to-postgresql
- enum
- test_admin_commands_helpers.py
- test_container_helpers_inventory_display.py
- inventory_equip_command.py
- EventBusLifecycleMixin
- persistence/container_helpers.py
- ComprehensiveLoggingMiddleware
- CombatParticipantData
- test_room_occupant_manager.py
- test_lint_container_get_instance.py
- ContainerLockMixin
- Async Remediation Final Report
- 🔴 CRITICAL ISSUES
- Test Suite Quality Audit - Executive Summary
- test_inventory_mutation_guard_async.py
- test_inventory_command_prototype.py
- test_world_loader.py
- test_lifecycle_respawn.py
- UtilityCommandFactory
- NPCStartupService
- PlayerPreferencesService
- TestLogoutCommand
- test_chat_moderation.py
- test_inventory_mutation_guard.py
- Bug Investigator Subagent
- EdgeDetailsPanel.tsx
- playerHandlers.ts
- Domain Model Anemic Anti-Pattern Audit
- ErrorMonitor
- verify_linting_parity.py
- players.sql
- canonical_room_id_impl
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
- test_look_item_helpers.py
- test_chat_pose_helpers.py
- MetricsCollector
- test_npc_threading_messages.py
- attach_compatibility_properties
- rooms.sql
- extract_player_name
- RateLimiter
- test_time_bundle.py
- test_movement_monitor.py
- test_player_event_handlers_room_left.py
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
- create_app
- utility_commands.py
- BehaviorEngine
- error_handling_middleware.py
- .set_player_combat_service
- test_spell_repository.py
- npc_combat_grace.py
- UUID
- asyncio
- asyncio
- test_ascii_map_renderer_exits.py
- asyncio
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
- EventPublisher
- format_markdown_file
- migrate_rooms.py
- test_skills_commands.py
- handle_teach_command
- _lucidity_change_payload_with_liabilities
- realtime/realtime.py
- CombatDeathHandler
- _handle_admin_set_stat_command
- Lint Remediation
- mythos_dev.rooms
- required
- test_player_respawn_handlers.py
- _clear_corrupted_cache_entry
- test_npc_startup_service.py
- CommandProcessor
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
- _should_include_npc
- RoomCacheLoader
- format_player_location
- .send_message
- MovementMonitor
- test_add_player_effect_generates_id
- test_retry.py
- Lock
- ExperienceRepository
- Any
- apply_communication_dampening
- exploration.sql
- test_room_service.py
- test_check_coverage_thresholds.py
- CombatPersistenceHandler
- npcs.sql
- Performance Profiler Subagent
- Security Auditor Subagent
- GitHub Actions Best Practices
- The Toolkit
- mapPageRenderer.tsx
- Complexity Refactoring Test Plan
- NATS Complete Remediation Summary
- SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch
- Execution Steps
- fix_suppression_alignment.py
- identify_critical_code.py
- Phase 3: Polish and Optimization
- time.py
- test_security_utils.py
- Phase 4: Testing and Refinement
- status_commands.py
- ProfessionService
- ContainerFactoryOptions
- get_room_environment
- overrides
- designTokens.ts
- executeCommand
- compilerOptions
- asyncio
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
- field_validator
- MemoryMonitor
- test_lucidity_command_disruption.py
- test_exploration_procedures.py
- test_mp_regeneration_service.py
- get_current_tick
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
- strict_mocker
- required
- UpgradeImplementationPlan
- _add_profession_lines
- .accept_party_invite
- TargetMatch
- MessageBroker
- test_security_headers.py
- RoomRepository
- auth_rate_limit.py
- TestVerificationSqlUsersPlayers
- test_nats_message_handler_subzone_events.py
- optimized_validate_player_name
- static_data/package.json
- TypeScript Best Practices
- vite Best Practices
- Delight Techniques
- Frontend Aesthetics Guidelines
- resolve_connection_manager
- compilerOptions
- ADR-020: WebSocket Authentication and CSRF
- Enhanced Logging Best Practices for MythosMUD
- Persistence Layer Extraction - COMPLETE ✅
- Test Coverage Summary: Disconnect Grace Period & Rest Command
- test_email_utils.py
- NPCCacheService
- ProfessionCacheService
- .get_data_provider
- test_ascii_map_renderer_grid.py
- PartyService
- room_hierarchy_schema.json
- schedule_end_combat_if_npc_died_best_effort
- CoordinateValidator
- test_hallucination_services.py
- enum
- FakeHallucinationService
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
- ItemInstance
- asyncio
- test_nats_retry_handler.py
- is_player_in_grace_period
- PassiveFluxContext
- enum
- .check_bidirectional_connections
- SQLAlchemy Best Practices (2.x Style)
- Introduce Color Strategically
- rules
- usePanelContext.ts
- commandStore.ts
- setup.ts
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
- _get_lifecycle_manager
- asyncio
- Party
- ._load_player_mutes_from_data
- test_player_repository.py
- test_player_spell_repository.py
- _FakeMessageQueue
- optimized_validate_security_comprehensive
- properties
- properties
- Codebase Explorer Subagent
- Pylint Best Practices
- Adapt Skill
- Improve Copy Systematically
- UX Writing
- map/types.ts
- TestResolveExitTarget
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)
- Changes by document
- Memory Leak Audit Report
- Quick Start: Running E2E Tests
- ._resolve_context_async
- TestHorizontalExitCharBetween
- holiday.schema.json
- schedule.schema.json
- analyze_coverage_gaps.py
- _apply_arena_seed_patch.py
- pylint.py
- generate_sql.mjs
- .create_lie_command
- validate_admin_permission
- required
- NPCActionMessage
- UUID
- CircuitBreaker
- required
- zone_schema.json
- populate_test_npc_databases.py
- api/conftest.py
- ._connect_nats
- .optimize_payload
- add_default_combat_data_to_config
- test_check_pr_issue_references.py
- test_combat_messaging_integration.py
- RoomDataCache
- test_check_no_production_assert.py
- test_validate_codacy_coverage_gate.py
- optimized_sanitize_unicode_input
- pytest Best Practices
- Skill: Create a New Worktree for a Task
- RoomInfo.tsx
- MessageBatcher
- ._get_vertical_exit_char
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
- format_combat_status
- test_look_item.py
- rest_countdown_task.py
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
- Decisions required
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
- test_channel_broadcasting_strategies.py
- _EventPersistence
- normalize_path_from_url_or_path
- test_profession_service.py
- RateLimiter
- connection_state_machine.py
- test_persistence_container_persistence.py
- .check_and_cleanup
- ._filter_active_players
- test_websocket_handler_rate_limit.py
- .validate_room_consistency
- test_command_factories.py
- TestValidatorIntegration
- Improve Layout Systematically
- Distill Skill
- .create_go_command
- .create_ground_command
- ClientLogger
- .create_follow_command
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
- .create_alias_command
- main
- fix_markdown_code_block_style.py
- main
- SyntaxErrorFixer
- generate_openapi_spec.py
- run_quality_fragmentation_guard.py
- .create_learn_command
- test_look_npc_helpers.py
- _utc_now
- .create_unalias_command
- player_repository_mappers.py
- channel_broadcasting_strategies.py
- optimized_comprehensive_sanitize_input
- required
- properties
- verify_npc_occupants.py
- logger.test.ts
- test_async_persistence_room_cache.py
- player_service
- test_player_event_handlers_utils.py
- test_room_subscription_manager.py
- test_run_test_ci.py
- test_combat_service_npc_in_combat.py
- test_room_environment_parity.py
- _RoomBroadcaster
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
- grype.py
- lint_container_get_instance.py
- main
- main
- .validate_alias_name_field
- handle_unequip_command
- mock_connection_manager
- SkillUseLog
- quest_service
- message_broadcaster
- .generate_fake_npc_tell
- room_validator/schemas/unified_room_schema.json
- subzone_with_override
- MagicPointsMeter.tsx
- test_game_enums.py
- test_monitoring_init.py
- _errors_len
- load_motd
- main
- Codacy Rules
- Quieter Skill
- Typeset Skill
- GridLayoutManager.tsx
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
- .create_supervised_task
- asyncio
- Teach Impeccable Skill
- Playwright Best Practices
- Responsive Design
- ConfigurationError
- .format
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
- holiday_row
- test_emotes_procedures.py
- test_npcs_zone_config_procedures.py
- test_async_persistence_room_loading.py
- TestMinimapExplorationInvestigationDoc
- add_default_combat_data_to_stats
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
- .check_duplicate_occupants
- days
- mock_persistence
- analyze_idle_memory_samples.py
- bench_cache.py
- quality_fragmentation_graph.py
- _filter_lines
- fix_markdown_file
- fix_room_references
- run_bug_prevention_tests.ps1
- run_make_stages.py
- mock_persistence
- test_inventory_service_helpers.py
- TestValidateUserForOpenContainer
- TestValidateUserForTransfer
- TestValidateUserForCloseContainer
- player_inventory_migration.py
- TestValidateUserForLootAll
- fixture
- TestGetRoomService
- test_utility_commands_whoami.py
- TestGetPlayerDeathService
- TestGetMagicService
- TestGetSpellLearningService
- TestGetMPRegenerationService
- test_room_subscription_manager_drops.py
- TestGetNPCSpawningService
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
- TestGetNPCPopulationController
- UnknownChannelStrategy
- SystemAdminChannelStrategy
- RoomBasedChannelStrategy
- TestGetMythosTimeConsumer
- test_event_publisher_init_with_initial_sequence
- _FakeEstablishmentManager
- .create_sit_command
- test_run_make_stages.py
- monitoring_service
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- optimized_validate_filter_name
- optimized_validate_help_topic
- .create_stand_command
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
- .create_unfollow_command
- .create_goto_command
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
- .create_shutdown_command
- Attack Command Not Starting Combat
- Second NPC Combat And Linkdead Findings
- Multi-Word Spell Name Parsing Failure
- main
- .create_spells_command
- .create_aliases_command
- Server Realtime Module
- .create_help_command
- .create_npc_command
- .validate_timestamp
- 3. Systematic Investigation Approach
- mythos_dev.npc_definitions
- items.sql
- enum
- WebSocket
- mock_event_bus
- event_publisher
- Thinking about stack structure
- Extract Skill
- MythosMUD Server Test Suite
- Common Test Failure Categories
- WebSocket
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
- Enhanced Logging System Implementation Guide
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
- ._get_player_mute_file
- mock_container
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
- DomainError
- ._error_callback
- test_command_player_state.py
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- 2. Auto-Attack During Grace Period
- 3. Grace Period Visibility & Messaging
- 4. Rest/Quit Command During Combat
- 5. Rest Command Countdown Duration
- 6. Rest Location (Inn/Hotel) Behavior
- nats_broker
- 7. Reconnection During Grace Period
- 8. Grace Period After Intentional Disconnect
- 9. Command Blocking During Grace Period
- test_grype.py
- Recommendations Summary
- mythos_dev.users
- rate_limiter
- user_manager
- day
- month
- Tiered Test Coverage Strategy
- chatPanelTestHelpers.ts
- VirtualizedMessageList.tsx
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
- Bounded Contexts and Service Boundaries
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
- setup_jwt_secret
- 1. Component Refactoring
- Executive Summary
- .codacy.yml
- eslint.config.js
- Client Security and Privacy Policies
- MythosMUD UI Component Library
- LoginGracePeriodBanner.tsx
- mythosTheme.ts
- Step-by-Step Remediation Process
- .__init__
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
- ADR-002: ApplicationContainer for Dependency Injection
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
- end_hour
- start_hour
- id
- plane
- zone
- long_description
- prototype_id
- short_description
- id
- plane
- rest_location
- sub_zone
- mock_send_game_event
- npc_startup_service
- zone
- plane
- test_create_admin_command
- rest_location
- sub_zone
- zone
- Test Suite Analyzer Agent
- black.md
- Vite Logo SVG
- chatPanelTestSetup.tsx
- UI-v2 Components
- ApplicationContainer
- playwright.runtime.config.ts
- deps/package.json
- wsl-bashrc-codacy.sh
- Mypy Remediation Skill
- MythosMUD Obsidian Index
- MythosMUD Worldbuilding Foundation (Raw)
- LLM Wiki Pattern.md
- ._exit_is_bidirectional
- .start
- .check_empty_room_with_occupants
- TestGetContainerService
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
- entities/__init__.py
- domain/events/__init__.py
- domain/__init__.py
- domain/repositories/__init__.py
- domain/services/__init__.py
- value_objects/__init__.py
- server/game/magic/__init__.py
- _UserWithGet
- mock_connection_manager
- description
- name
- persistence/utils/__init__.py
- plane
- sub_zone
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
- applies_to
- metadata
- weight
- .__init__
- .validate_direction
- .on_connection_failed
- _MigrationArgs
- _format_liabilities
- _FakeClientState
- mock_connection_manager
- _iter_exception_chain
- autoprefixer
- eslint
- @eslint/js
- eslint-plugin-jsx-a11y
- happy-dom
- markdownlint-cli
- patch-package
- @playwright/test
- tailwindcss
- @testing-library/dom
- @testing-library/react
- @testing-library/user-event
- typescript
- vite
- @vitejs/plugin-react
- mythos_dev.emote_aliases
- mythos_dev.get_user_id_by_username_ci
- .save_player
- .add_item_to_inventory
- server/realtime/maintenance/__init__.py
- .__init__
- create_professions_table.sql
- ._render_empty_map
- test_build_room_objects_with_dict_attributes
- test_disconnect_from_connected
- test_disconnect_from_degraded
- test_degrade
- test_recover
- test_close_circuit
- test_can_attempt_connection_connected
- test_can_attempt_connection_circuit_open
- test_can_attempt_connection_reconnecting
- test_should_open_circuit_at_threshold
- test_should_open_circuit_over_threshold
- test_get_stats
- test_get_stats_with_error
- unit/infrastructure/__init__.py
- test_get_stats_no_error
- test_reconnect_attempts_increment
- test_nats_connection_state_machine_init
- test_total_disconnections_increment
- test_last_connected_time_set
- test_on_enter_state_logs
- test_invalid_transition_raises_error
- test_connect_transition
- test_connected_successfully_from_connecting
- test_connection_failed_from_connecting
- test_determine_spawn_room_room_id_not_found
- test_spawn_npcs_on_startup_with_optional_npcs
- test_check_rate_limit_disabled
- test_record_message_cleanup_old
- test_record_message_error_handling
- test_get_player_stats
- test_get_player_stats_empty
- test_process_exit_rows_with_partial_room_ids
- test_process_exit_rows_debug_logging
- test_build_room_objects_success
- test_process_room_rows_with_full_room_id
- test_build_room_objects_with_non_dict_attributes
- test_reset_player_limits_specific_channel
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
- test_reset_player_limits_all_channels
- test_get_system_stats
- test_is_player_rate_limited_true
- test_get_remaining_messages_zero
- test_get_remaining_messages_error_handling
- test_set_limit
- test_get_limit_existing
- test_get_limit_default
- test_cleanup_old_entries
- test_create_spell_command
- test_create_teleport_command_too_many_args
- _calculate_retry_delay
- unit/monitoring/__init__.py
- zones
- players
- npc_definitions
- unit/persistence/__init__.py
- unit/realtime/integration/__init__.py
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- unit/services/nats_subject_manager/__init__.py
- unit/structured_logging/__init__.py
- test_create_sit_command
- test_create_unequip_command
- test_create_mute_global_command
- test_create_punch_command
- test_create_aliases_command
- test_create_teleport_command
- test_create_learn_command
- test_create_say_command
- test_create_pose_command
- test_create_reply_command
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
- API OpenAPI/Swagger Specification
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
- Distributed EventBus via NATS
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
- Configuration Files Reference
- Cursor Hooks
- Database Connection Pool Configuration
- Dead Code Definition and Tooling
- MythosMUD Deployment
- Event Subscription Cleanup Patterns
- Fresh Session Test Execution Guide
- GitHub Actions Runner Parity Container
- NATS Error Handling Strategy
- NATS Manual Acknowledgment Guide
- Persistence Layer Async Migration Guide
- Persistence Repository Architecture
- MythosMUD Player Command Developer's Guide
- PostgreSQL Standards for Contributors
- Pre-commit Logging Validation
- Quest Design Guidelines
- Quest System Features
- Real-Time Architecture
- Room Environment Reference
- Item System Observability Runbook
- Security: Environment Variables
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
2. `LoggedHTTPException` - 360 edges
3. `ValidationError` - 314 edges
4. `User` - 298 edges
5. `AliasStorage` - 264 edges
6. `DatabaseError` - 251 edges
7. `Player` - 232 edges
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
- 3-file cycle: `server/realtime/connection_cleanup_methods.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_cleanup_methods.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- 4-file cycle: `server/realtime/connection_establishment.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_establishment.py`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
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

## Communities (2133 total, 448 thin omitted)

### Community 0 - "get_logger"
Cohesion: 0.01
Nodes (340): get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing), create_validator(), Any, Path (+332 more)

### Community 1 - "models/player.py"
Cohesion: 0.01
Nodes (513): Player schema conversion utilities. This module handles conversion of Player…, Alias model for command aliases. This module defines the Alias model for…, Base, DeclarativeBase, Shared SQLAlchemy DeclarativeBase for all models. This module provides a single…, Shared declarative base for all MythosMUD models. All models (User, Player,…, SQLAlchemy models for calendar data (holidays and NPC schedules)., Dialogue subsystem model: dialogue_definitions (NPC talk trees, #583). (+505 more)

### Community 2 - "PlayerLeftRoom"
Cohesion: 0.01
Nodes (407): ModuleType, _convert_value_for_json(), _convert_value_from_json(), _copy_public_event_attrs(), deserialize_event(), _event_class_from_payload(), _extract_event_fields(), _init_kwargs_from_event_data() (+399 more)

### Community 3 - "NPCBase"
Cohesion: 0.02
Nodes (108): NPC behavior system for MythosMUD. This module provides the core NPC behavior…, NPCBase, ABC, Get behavior configuration., Get AI integration configuration., Remove item from NPC inventory., Get specific item from inventory., Update determination points after taking damage; return new DP. (+100 more)

### Community 4 - "npc_database.py"
Cohesion: 0.04
Nodes (68): Shutdown core services., close_npc_db(), ensure_npc_database_directory(), get_npc_database_path(), get_npc_engine(), get_npc_session(), get_npc_session_maker(), init_npc_db() (+60 more)

### Community 5 - "DatabaseError"
Cohesion: 0.01
Nodes (441): get_10_active_invites(), main(), Get 10 active invite codes from the database., fetch_professions(), fetch_user_by_username_case_insensitive(), Profession, Direct async SQL queries used by AsyncPersistenceLayer. Extracted to keep…, Get a user by username (case-insensitive). MULTI-CHARACTER: Usernames are… (+433 more)

### Community 6 - "BaseCommand"
Cohesion: 0.01
Nodes (527): _apply_room_exit_to_memory(), _apply_room_properties_to_memory(), _build_exit_attributes(), create_room_exit(), _create_room_link_in_db(), delete_room_exit(), _delete_room_link_in_db(), AsyncSession (+519 more)

### Community 7 - "server/dependencies.py"
Cohesion: 0.02
Nodes (156): get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service(), get_level_service() (+148 more)

### Community 8 - "ValidationError"
Cohesion: 0.01
Nodes (340): MythosValidationError, Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.…, create_error_context(), Unpack, Data validation errors (e.g. empty local/whisper message). Log at warning, not…, Create an error context with the given parameters. Args: **kwargs: Context…, ValidationError, PlayerCreationService (+332 more)

### Community 9 - "ContainerComponent"
Cohesion: 0.02
Nodes (203): ContainerComponent, ContainerLockState, ContainerSourceType, Any, BaseModel, field_validator, StrEnum, Validate that metadata does not contain personal information (COPPA… (+195 more)

### Community 10 - "api/character_creation.py"
Cohesion: 0.03
Nodes (102): _apply_stat_modifiers(), _check_shutdown_status(), create_character_with_stats(), _execute_create_character(), _prepare_create_character_request(), Request, Character creation and stats generation API endpoints. This module handles…, Apply profession stat_modifiers to a stats dict; returns new dict. Plan 4.4. (+94 more)

### Community 11 - "container_events.py"
Cohesion: 0.03
Nodes (126): emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), ConnectionManager, UUID, WebSocket event emission helpers for container API endpoints. This module…, Emit WebSocket event for container closing. Args: connection_manager:… (+118 more)

### Community 12 - "test_security_validator.py"
Cohesion: 0.01
Nodes (203): Process a validated command with routing. Args: command_data: The validated…, Validate mute reason for security using centralized validation., Unit tests for security validation utilities. Tests the security validator…, Test that comprehensive sanitization removes null bytes., Test that comprehensive sanitization removes control characters., Test that comprehensive sanitization normalizes newlines to spaces., Test that comprehensive sanitization preserves tabs., Test that comprehensive sanitization removes zero-width characters. (+195 more)

### Community 13 - "CombatParticipant"
Cohesion: 0.03
Nodes (111): CombatAction, CombatParticipant, Check if participant is mortally wounded (players only). For players: mortally…, Check if participant can perform voluntary combat actions. Unconscious (DP <=…, Apply damage to this participant and determine resulting death states.…, Represents a combat action., Represents a participant in combat., Check if participant is dead. For players: dead if DP <= -10 For NPCs: dead if… (+103 more)

### Community 14 - "connection_manager_methods.py"
Cohesion: 0.01
Nodes (259): _async_callable(), cleanup_dead_websocket_impl(), _close_dead_websocket_if_open(), delegate_game_state_provider(), delegate_game_state_provider_sync(), delegate_health_monitor(), delegate_health_monitor_sync(), delegate_message_broadcaster() (+251 more)

### Community 15 - "Player"
Cohesion: 0.01
Nodes (190): _convert_legacy_stats_string(), Player, listens_for, Initialize Player instance., String representation of the player., Get player stats as dictionary. Returns a MutableDict instance that…, Set player stats from dictionary. Accepts both plain dict and MutableDict…, Get player inventory as list. Handles both JSON string (from database) and list… (+182 more)

### Community 16 - "get_npc_instance_service"
Cohesion: 0.02
Nodes (180): handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command., Handle NPC reaction trigger command., Handle NPC behavior stop command. (+172 more)

### Community 17 - "players.py"
Cohesion: 0.07
Nodes (80): create_player(), delete_character(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), _force_disconnect_character(), get_available_classes(), get_class_description() (+72 more)

### Community 18 - "combat_turn_participant_actions.py"
Cohesion: 0.05
Nodes (53): get_npc_current_target(), Return current target participant_id for this NPC, or None., _apply_physical_strength_bonus(), _attacker_stats_dict_from_full_player(), _execute_npc_attack(), _execute_player_attack(), _get_combat_container_services(), _get_target_stats_for_damage() (+45 more)

### Community 19 - "test_container_persistence_async_helpers.py"
Cohesion: 0.08
Nodes (60): Validate lock_state parameter. Args: lock_state: Lock state to validate Raises:…, validate_lock_state(), _build_item_dict(), _call_create_container_procedure(), _container_data_from_row(), create_container_async(), delete_container_async(), fetch_container_items_async() (+52 more)

### Community 20 - "mythos_dev_ddl.sql"
Cohesion: 0.02
Nodes (5): mythos_dev.aliases, mythos_dev.calendar_holidays, mythos_dev.calendar_npc_schedules, mythos_dev.id_map_users, mythos_dev.professions

### Community 21 - "AliasStorage"
Cohesion: 0.01
Nodes (397): AliasPayload, AliasRecord, AliasStorage, _AliasValidatorCache, _apply_alias_timestamps(), _as_alias_payload(), _as_alias_record(), _empty_alias_payload() (+389 more)

### Community 22 - "test_combat_event_publisher.py"
Cohesion: 0.03
Nodes (124): CombatEndedEvent, CombatStartedEvent, CombatTargetSwitchEvent, NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent, Combat-specific events for the MUD. This module defines combat-related events… (+116 more)

### Community 23 - "AsyncPersistenceLayer"
Cohesion: 0.01
Nodes (315): AsyncPersistenceLayer, Any, datetime, Player, Profession, UUID, Async persistence layer for MythosMUD. This module provides an async version of…, Set the instance manager for instanced room lookup (instance-first). (+307 more)

### Community 24 - "CombatService"
Cohesion: 0.02
Nodes (116): Create CombatService with NATS and register it. Assumes NATS is connected., Internal helpers for spell_effects.py (coercion, combat room lookup). Keeps the…, CombatService, DataProviderProtocol, _fallback_find_combat_id_for_npc(), find_participant_uuid_by_string_id(), get_combat_by_participant(), get_combat_id_for_npc() (+108 more)

### Community 25 - "inventory_command_helpers.py"
Cohesion: 0.02
Nodes (152): broadcast_room_event(), _collect_progress_sync(), ensure_item_instance_for_pickup(), persist_player(), _player_uuid_for_quest_sync(), prepare_extracted_stack(), Player, UUID (+144 more)

### Community 26 - "container_endpoints_basic.py"
Cohesion: 0.02
Nodes (180): _apply_inventory_stack_defaults(), _as_inventory_dicts(), _as_str_list(), _as_str_object_dict(), _as_str_object_mapping(), _build_container_data_from_dict(), _build_open_container_response(), _build_transfer_response() (+172 more)

### Community 27 - "roll_character_stats"
Cohesion: 0.04
Nodes (72): get_current_user(), Get current user with enhanced logging., _apply_rate_limiting_for_stats_roll(), _as_float(), _as_int(), _convert_stat_summary_to_stat_summary_model(), _dispatch_roll_stats(), Depends (+64 more)

### Community 28 - "SpellEffects"
Cohesion: 0.02
Nodes (174): NpcIntegrationStringIdPort, NpcLifecycleManagerPort, NpcSpellDamageTarget, PlayerPersistenceSpellPort, PlayerServiceHealPort, Protocol, UUID, Shared Protocol types for spell effect modules. Used by basedpyright to type… (+166 more)

### Community 29 - "PlayerNameExtractor"
Cohesion: 0.02
Nodes (84): PlayerNameExtractor, Any, UUID, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:…, Perform basic validation on player name (not None, is string, not empty). Args:…, Utility class for extracting and validating player names. CRITICAL: NEVER uses… (+76 more)

### Community 30 - "test_look_npc.py"
Cohesion: 0.08
Nodes (25): mock_lifecycle_manager(), mock_npc(), fixture, Unit tests for NPC look functionality. Tests the helper functions for looking…, Test formatting other stats when none present., Test formatting lifecycle information., Test formatting lifecycle information when not present., Test finding matching NPCs successfully. (+17 more)

### Community 31 - "ContainerServiceError"
Cohesion: 0.03
Nodes (90): Container component model for the unified container system. As documented in…, ContainerAccessMixin, UUID, Container access validation (ownership, proximity, roles, corpse grace). Mixin…, Deny non-owner corpse access during (or without) a timed grace period., Validate corpse grace period access rules., Validate that player has access to the container. Checks proximity, ownership,…, Return True if player inventory contains the required key item_id. (+82 more)

### Community 32 - "test_container_bundles.py"
Cohesion: 0.03
Nodes (109): ChatBundle, Chat bundle: chat service. Depends on Core (config, persistence), Game…, CombatBundle, Combat bundle: player combat, death, respawn, combat service, catatonia,…, Combat-related services., CoreBundle, Core bundle: config, database, tasks, event bus, persistence. First bundle in…, Core infrastructure: config, database, tasks, event bus, persistence. (+101 more)

### Community 33 - "test_connection_session_management.py"
Cohesion: 0.06
Nodes (81): _cleanup_old_session_tracking(), _cleanup_player_data_for_session(), _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), handle_new_game_session_impl(), _is_websocket_connected(), Protocol, UUID (+73 more)

### Community 34 - "get_username_from_user"
Cohesion: 0.01
Nodes (381): handle_add_admin_command(), handle_mute_global_command(), handle_unmute_global_command(), Handle the mute_global command for global muting. Args: command_data: Command…, Handle the unmute_global command for removing global mute. Args: command_data:…, Handle the add_admin command for adding administrators. Args: command_data:…, _execute_combat_action(), _execute_phantom_combat_action() (+373 more)

### Community 35 - "PlayerPositionService"
Cohesion: 0.02
Nodes (161): Check if player is resting or in login grace period, interrupt rest if needed.…, Check if player is resting or in login grace period, interrupt rest if needed., _begin_seated_rest_countdown(), cancel_rest_countdown(), _check_player_in_combat(), _check_rest_location(), _disconnect_player_intentionally(), _execute_rest_flow() (+153 more)

### Community 36 - "PlayerRoomEventHandler"
Cohesion: 0.04
Nodes (60): OccupantSnap, _as_map(), _as_occupant_snap(), PlayerRoomEventHandler, JsonMap, UUID, Handles room-related player events (entered, left, occupants)., Initialize room event handler from a deps bundle. (+52 more)

### Community 37 - "test_connection_establishment.py"
Cohesion: 0.05
Nodes (70): _bind_accepted_websocket(), _cleanup_dead_connections(), _cleanup_failed_connection(), _EstablishmentConnectionManager, _find_dead_connections(), Player, Protocol, UUID (+62 more)

### Community 38 - "NATSService"
Cohesion: 0.01
Nodes (199): Msg, NATSConfig, Any, BaseSettings, field_validator, NATS messaging configuration., Validate TLS file paths exist when TLS is enabled., Validate max payload is reasonable. (+191 more)

### Community 39 - "ChatService"
Cohesion: 0.02
Nodes (108): ChatService, _publish_room_chat(), ChatMessage, UUID, _rate_limit_result(), Chat service for handling real-time communication between players. This service…, Normalize player identifiers to string form., Send a say message to players in the same room. This method publishes the… (+100 more)

### Community 40 - "ui-v2/types.ts"
Cohesion: 0.03
Nodes (80): PanelManager(), PanelManagerProps, calculateOccupantCount(), GameClientV2(), GameClientV2Content(), MainDockPanelId, MainDockSlotMeta, GameClientV2AuxiliaryPanels() (+72 more)

### Community 41 - "factory.py"
Cohesion: 0.05
Nodes (56): Admin API module for MythosMUD. This module provides administrative API…, Container API endpoints for unified container system. As documented in the…, API module for MythosMUD. This module provides REST API endpoints for the…, Shared FastAPI APIRouter for player endpoints (avoids import cycles with route…, get_all_professions(), get_profession_by_id(), get, Request (+48 more)

### Community 42 - "test_follow_service.py"
Cohesion: 0.02
Nodes (139): _FollowTargetValue, Wire exploration, movement, follow, and party services., NPCEnteredRoom, Event fired when an NPC enters a room. This event is triggered when an NPC…, FollowService, _is_npc_follow_value(), Any, ConnectionManager (+131 more)

### Community 43 - "Stats"
Cohesion: 0.02
Nodes (157): computed_field, CharacterCreationService, Any, UUID, Character creation service for MythosMUD server. This module handles all…, Validate character stats against class prerequisites. Args: stats: The stats…, Create a new character with specific stats. Args: name: The character's name…, Get information about all available character classes and their prerequisites.… (+149 more)

### Community 44 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (125): EquipCommand, PickupCommand, field_validator, model_validator, Strip and validate search term., Ensure either index or search_term is provided., Validate target slot value. Args: value: The target slot value to validate (can…, Command for unequipping an item back to inventory. (+117 more)

### Community 45 - "CommandFactory"
Cohesion: 0.01
Nodes (73): CommandFactory, Create StandCommand from arguments., Create LieCommand from arguments., Create GroundCommand from arguments., Create FollowCommand from arguments., Create UnfollowCommand from arguments., Create FollowingCommand from arguments., Create PartyCommand from arguments. (+65 more)

### Community 46 - "Communities (355 total, 223 thin omitted)"
Cohesion: 0.02
Nodes (133): Communities (355 total, 223 thin omitted), Community 0 - "Nyarlathotep Avatars", Community 100 - "Call Daoloth / Daoloth", Community 101 - "Call Nyogtha / Clutch of Nyogtha", Community 102 - "Call Saaitii / Saaitii", Community 103 - "Call Zu-Che-Quon / Enchant Bells of Horror", Community 104 - "Cast Out Shan / Shaggai", Community 105 - "Casting the Runes / Elder Sign" (+125 more)

### Community 47 - "server/services/__init__.py"
Cohesion: 0.03
Nodes (111): AbstractContextManager, _ensure_shared_services_initialized(), Shared service initialization for inventory commands., Resolve async_persistence from the request and construct shared singletons., Unequip command: move an equipped item back to inventory., _clone_equipped(), _clone_inventory(), EquipmentCapacityError (+103 more)

### Community 48 - "test_exceptions.py"
Cohesion: 0.05
Nodes (41): GameLogicError, Game mechanics and logic errors., Resource not found errors., ResourceNotFoundError, Test GameLogicError can be instantiated., Test ResourceNotFoundError can be instantiated., test_game_logic_error(), test_resource_not_found_error() (+33 more)

### Community 49 - "TargetResolutionService"
Cohesion: 0.06
Nodes (32): Initialize the spell targeting service. Args: target_resolution_service:…, PersistenceProtocol, PlayerServiceProtocol, Player, Protocol, Room, UUID, Validate player exists and is in a room. Returns (room_id, error_result). (+24 more)

### Community 50 - "request_with_app_container"
Cohesion: 0.06
Nodes (53): handle_reply_command(), handle_whisper_command(), Reply to last whisper sender., Shared mock wiring for communication command unit tests., Return (request, container) with request.app.state.container wired. Typed…, request_with_app_container(), asyncio, Unit tests for whisper and reply communication command handlers. (+45 more)

### Community 51 - "is_player_in_login_grace_period"
Cohesion: 0.03
Nodes (124): Game state provision for connection management. This module provides…, Get login grace period status for player., _as_grace(), cancel_login_grace_period(), _EffectPersistence, get_login_grace_period_remaining(), _grace_period_task(), _GraceApp (+116 more)

### Community 52 - "NPCCombatDataProvider"
Cohesion: 0.05
Nodes (43): NPCCombatDataProvider, Any, UUID, NPC Combat Data Provider. This module provides data retrieval and preparation…, Get player name for messaging. Args: player_id: ID of the player Returns:…, Get the current room ID for a player. Args: player_id: ID of the player (must…, Get player combat participant data from persistence. Args: player_id: ID of the…, Get NPC combat participant data from NPC instance. Args: npc_instance: NPC… (+35 more)

### Community 53 - "NPCDefinition"
Cohesion: 0.01
Nodes (389): _JSONDict, Base, _loads_json_dict(), NPCDefinition, NPCDefinitionType, NPCRelationship, NPCSpawnRule, DeclarativeBase (+381 more)

### Community 54 - "chat_service.py"
Cohesion: 0.04
Nodes (62): ChatEmoteService, ChatLogger, ChatPlayerService, ChatRateLimiter, ChatUserManager, Protocol, Return True if command is a predefined emote alias., Return (self_message, other_message) for a predefined emote command. (+54 more)

### Community 55 - "test_npc_definitions_api.py"
Cohesion: 0.08
Nodes (58): create_npc_definition(), delete_npc_definition(), get_npc_definition(), get_npc_definitions(), AsyncSession, delete, get, post (+50 more)

### Community 56 - "lifespan_magic.py"
Cohesion: 0.05
Nodes (43): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+35 more)

### Community 57 - "SpellEffectType"
Cohesion: 0.04
Nodes (118): Load all spells from the database into memory. This should be called during…, BaseModel, StrEnum, Spell data models for the magic system. This module contains Pydantic models…, Valid target types for spells., Valid range types for spells., Valid effect types for spells., Material component required for casting a spell. (+110 more)

### Community 58 - "test_admin_auth_service.py"
Cohesion: 0.02
Nodes (116): AdminAction, AdminAuthService, AdminRole, AdminSession, Any, Request, Represents an admin session., Service for admin authentication and authorization. (+108 more)

### Community 59 - "command_handler_unified.py"
Cohesion: 0.01
Nodes (245): command_request_app_state(), CommandExecutionRequest, HTTP Request or WebSocketRequestContext for unified command processing., Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…, clean_command_input(), _is_predefined_emote(), normalize_command(), CommandExecutionRequest (+237 more)

### Community 60 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (128): asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not…, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes. (+120 more)

### Community 61 - "handle_transfer_items_exceptions"
Cohesion: 0.02
Nodes (66): handle_close_container_exceptions(), handle_loot_all_exceptions(), handle_open_container_exceptions(), handle_transfer_items_exceptions(), Any, Exception, Request, UUID (+58 more)

### Community 62 - "RoomService"
Cohesion: 0.03
Nodes (89): RoomDictList, _apply_exploration_filter_if_needed(), get_room(), _invalidate_room_cache(), list_rooms(), Any, BaseModel, get (+81 more)

### Community 63 - "test_admin_shutdown_command.py"
Cohesion: 0.03
Nodes (124): _asyncio_mark, _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), calculate_notification_times(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state() (+116 more)

### Community 64 - "test_user_manager.py"
Cohesion: 0.02
Nodes (97): Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() successfully globally mutes a player., Test mute_global() fails when trying to mute admin. (+89 more)

### Community 65 - "test_go_command.py"
Cohesion: 0.05
Nodes (78): _cancel_rest_if_moving(), _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement(), handle_go_command(), _movement_combat_and_event_bus_from_go_app(), _movement_service_for_go_command(), Any (+70 more)

### Community 66 - "test_command_factories_utility.py"
Cohesion: 0.11
Nodes (22): Unit tests for utility command factories. Tests the UtilityCommandFactory class…, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+14 more)

### Community 67 - "test_users.py"
Cohesion: 0.02
Nodes (144): AuthenticationBackend, BaseUserManager, ID, Authentication module for MythosMUD. This package contains all authentication-…, Custom JWT strategy that invalidates tokens after server restart. Tokens must…, JWT strategy that rejects tokens issued before the current server start., Reads a JWT token, validating its signature, audience, and server epoch., RestartInvalidatingJWTStrategy (+136 more)

### Community 68 - "CombatInstance"
Cohesion: 0.03
Nodes (101): CombatInstance, UUID, Represents an active combat instance., Get the participant whose turn it is., Advance to the next round - all participants act each round. In round-based…, Check if combat should end. CRITICAL: Combat should NOT end when a player is…, Get all participants that are not dead (includes mortally wounded players at 0…, Update the last activity tick and datetime. (+93 more)

### Community 69 - "combat_service.py"
Cohesion: 0.03
Nodes (130): CombatResult, Result of a combat action., clear_aggro_for_combat(), Clear all aggro state for this combat (call on combat end)., CombatDPSync, Any, UUID, Get persistence layer from application container. Args: player_id: Player ID… (+122 more)

### Community 70 - "test_command_validator.py"
Cohesion: 0.03
Nodes (109): Unit tests for command validator., Test validate_command_length returns True for valid length., Test validate_command_length returns False for too long command., Test validate_command_length with custom max_length., Test validate_command_format returns True for valid command., Test validate_command_format returns False for empty command., Test validate_command_format returns False for suspicious command., Test validate_command_format returns False for too long command. (+101 more)

### Community 71 - "RoomLoader"
Cohesion: 0.03
Nodes (75): option, fixture, Create a temporary directory for testing., temp_dir(), Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer (+67 more)

### Community 72 - "communication_commands_flows.py"
Cohesion: 0.06
Nodes (57): _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_global_command(), flow_reply_command(), flow_system_command(), flow_whisper_command(), _player_id_bundle(), Room/global/system/whisper/reply flows for communication command handlers.… (+49 more)

### Community 73 - "test_look_container_helpers.py"
Cohesion: 0.03
Nodes (118): _as_map(), _as_map_list(), _as_uuid(), _container_name(), _ContainerPersistence, _extract_container_metadata(), _fetch_container(), _find_container_in_room() (+110 more)

### Community 74 - "test_command_moderation.py"
Cohesion: 0.04
Nodes (68): AddAdminCommand, AdminCommand, MuteCommand, MutesCommand, field_validator, Moderation command models for MythosMUD. This module provides command models…, Command for showing current mute status., Command for administrative utilities with subcommands. (+60 more)

### Community 75 - "eventHandlers/types.ts"
Cohesion: 0.04
Nodes (81): formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, IncapacitatedBanner, IncapacitatedBannerProps, HallucinationTicker, HallucinationTickerProps (+73 more)

### Community 76 - "event_types.py"
Cohesion: 0.03
Nodes (117): 1.1. Top-Level Entry Point, 1.2. Launching Concurrent Tasks, 1.3. Grouping Tasks, 1. Structured Concurrency: Entry Points and Task Management, 2.1. CPU-Bound Work, 2. Avoiding Blocking Operations, asyncio Best Practices, EventBusMixinBase (+109 more)

### Community 77 - "ApplicationContainer"
Cohesion: 0.03
Nodes (90): Raise if prerequisites for NATS combat are missing., Start NATS message handler if available. Logs and swallows errors., Handle case when NATS is not connected. Raises in prod, sets combat_service to…, Initialize NATS-dependent combat service and start NATS message handler., Failover callback that relocates catatonic players to the sanitarium., Shutdown log aggregator., Shutdown NATS-related services., Dependency Injection Container for MythosMUD. Re-exports ApplicationContainer… (+82 more)

### Community 78 - "test_admin_commands.py"
Cohesion: 0.05
Nodes (62): asyncio, Unit tests for admin command handlers. Tests the admin command handler…, Test handle_mute_command() with no target player., Test handle_mute_command() successful execution., Test handle_unmute_command() when user manager is not available., Test handle_unmute_command() with no target player., Test handle_unmute_command() successful execution., Test handle_unmute_command() succeeds when target was not muted (E2E cleanup… (+54 more)

### Community 79 - "test_combat_persistence_handler_events.py"
Cohesion: 0.06
Nodes (43): mock_combat_service(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully., Test _publish_player_dp_update_event_impl handles no NATS service., Test _publish_player_dp_update_event_impl with all optional parameters. (+35 more)

### Community 80 - "NATSConnectionStateMachine"
Cohesion: 0.08
Nodes (14): NATSConnectionStateMachine, Initialize connection state machine. Args: connection_id: Unique identifier for…, Handler for connect transition. Resets reconnection counter and prepares for…, Handler for successful connection. Records connection time and increments…, Handler for disconnection. Increments disconnection counter. AI: Track…, Handler for starting reconnection. Checks if circuit breaker should be…, Handler for circuit breaker opening. Logs circuit open event for alerting. AI:…, Handler for circuit breaker closing. Resets failure counters. AI: Circuit… (+6 more)

### Community 81 - "StatusEffect"
Cohesion: 0.02
Nodes (107): Item prototype registry for command modules., _inventory_item_with_weapon(), PlayerSchemaConverter, Any, Get stats, inventory, and status_effects from player, handling async methods., Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…, Get PositionState from position value, with fallback to STANDING., Create PlayerRead schema from player object. (+99 more)

### Community 82 - "item_instance_persistence_async.py"
Cohesion: 0.08
Nodes (40): CreateItemInstanceInput, EnsureItemInstanceInput, TypedDict, Constants and shared types for async persistence layer. Extracted to keep…, Optional fields for create_item_instance. owner_type, owner_id, etc. with…, Optional fields for ensure_item_instance., Create a new item instance. Delegates to ItemRepository., create_item_instance_async() (+32 more)

### Community 83 - "format_player_entry"
Cohesion: 0.09
Nodes (23): format_player_entry(), Format a single player entry for the who command output. Args: player: Player…, Unit tests for who command helper functions. Tests the helper functions in…, Test filter_players_by_name() filters players by name., Test filter_players_by_name() returns empty list when no matches., Test filter_players_by_name() returns all players when filter is empty., Test format_player_location() formats valid room ID., Test format_player_entry() formats player entry. (+15 more)

### Community 84 - "User"
Cohesion: 0.02
Nodes (232): _MapRooms, MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter…, _apply_exploration_filter_if_needed(), _AsciiMapViewport, _build_ascii_map_response(), _build_ascii_minimap_response() (+224 more)

### Community 85 - "test_look_helpers.py"
Cohesion: 0.03
Nodes (103): _AppWithState, _async_persistence_from_app(), _ContainerWithPersistence, _EquippedPlayer, _get_health_label(), _get_lucidity_label(), _get_visible_equipment(), _get_wearable_container_service() (+95 more)

### Community 86 - "ExplorationCommandFactory"
Cohesion: 0.06
Nodes (52): Unit tests for exploration command factories. Tests the…, Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_following_command() creates FollowingCommand with no args., Test create_following_command() raises error with args., Test create_party_command() with no args returns status-only command., Test create_party_command() with invite and target. (+44 more)

### Community 87 - "ContainerData"
Cohesion: 0.04
Nodes (71): ContainerData, ContainerDataCore, ContainerDataExtras, Container data class for persistence operations., Identity and placement fields for a container row., Optional payload and timestamps for a container row., Data class for container information., Convert container data to dictionary. Returns dictionary with model field names… (+63 more)

### Community 88 - "Any"
Cohesion: 0.13
Nodes (12): Any, Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits…, Build exit lookup map from room data., Center viewport on the character's current room so the player is in the middle…, Render a single row of rooms with horizontal exits., Render an ASCII map as HTML. Args: rooms: List of room dictionaries with…, Return the horizontal exit character (—, >, or <) given east/west exit state,… (+4 more)

### Community 89 - "test_websocket_initial_state.py"
Cohesion: 0.03
Nodes (103): add_npc_occupants_to_list(), _AppStateForEventHandler, _AppStateWithNpcLifecycle, _AppWithState, check_and_send_death_notification(), _ContainerWithNpcLifecycle, _get_death_location_name(), get_event_handler_for_initial_state() (+95 more)

### Community 90 - "NATSError"
Cohesion: 0.02
Nodes (144): NATSConnectionError, NATSError, NATSHealthCheckError, NATSPublishError, NATSRequestError, NATSSubscribeError, Exception, NATS-specific exception hierarchy for standardized error handling. This module… (+136 more)

### Community 91 - "test_look_container.py"
Cohesion: 0.03
Nodes (101): ContainerLookArgs, _get_container_description(), _handle_container_look(), CommandResponse, NamedTuple, Get container description from prototype registry., Handle looking at a specific container., Arguments for looking at a container. (+93 more)

### Community 92 - "ConnectionManager"
Cohesion: 0.02
Nodes (125): Initialize real-time services. Requires CoreBundle attributes on container., delegate_error_handler(), Generic delegate for error handler methods. Args: error_handler: Error handler…, detect_and_handle_error_state_impl(), handle_authentication_error_impl(), handle_security_violation_impl(), handle_websocket_error_impl(), Any (+117 more)

### Community 93 - "test_chat_npc_system.py"
Cohesion: 0.05
Nodes (70): Initialize chat service., NPCSpoke, Event fired when an NPC speaks. This event is triggered when an NPC…, _ChatDeliveryService, deliver_npc_room_speech(), deliver_personal_system(), npc_sender_id(), _on_npc_spoke() (+62 more)

### Community 94 - "test_player_requests.py"
Cohesion: 0.04
Nodes (93): apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest, post (+85 more)

### Community 95 - "catatonia_check.py"
Cohesion: 0.03
Nodes (67): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+59 more)

### Community 96 - "test_aggro_threat.py"
Cohesion: 0.05
Nodes (85): add_damage_threat(), add_heal_threat(), _aggression_scale(), apply_stealth_wipe(), apply_taunt(), _get_aggro_config(), get_or_create_hate_list(), on_player_entered_stealth() (+77 more)

### Community 97 - "create_access_token"
Cohesion: 0.04
Nodes (59): create_access_token(), decode_access_token(), timedelta, Decode and validate a JWT access token., Create a JWT access token., Test decoding invalid access token returns None., Test decoding expired access token returns None., Test access token creation with custom secret key. (+51 more)

### Community 98 - "test_room_sync_service.py"
Cohesion: 0.04
Nodes (65): mock_room_service(), asyncio, fixture, Unit tests for room sync service. Tests the RoomSyncService class for room…, Test _process_room_update_with_validation() processes valid room data., Test _process_room_update_with_validation() fixes invalid room data., Test _process_room_update_with_validation() handles stale data., Test _process_room_update_with_validation() handles errors gracefully. (+57 more)

### Community 99 - "EventBus"
Cohesion: 0.02
Nodes (171): EventBus, Invoke one subscriber in test mode (direct call or create_task)., Process subscribers synchronously when tests have no running EventBus loop., Publish an event to the pure asyncio event bus. Args: event: The event to…, AbstractEventLoop, T, TypedDict, Set the main event loop - now properly managed for async compatibility. (+163 more)

### Community 100 - "rescue_commands.py"
Cohesion: 0.05
Nodes (67): _broadcast_posture_change(), _build_posture_change_event(), _format_room_posture_message(), _get_position_command_services(), handle_lie_command(), _handle_position_change(), handle_stand_command(), Request (+59 more)

### Community 101 - "test_containers.py"
Cohesion: 0.05
Nodes (51): get_connection_manager, close_container(), open_container(), APIRouter, ConnectionManager, Depends, Request, Open a container; returns container data and mutation_token (rate limited). (+43 more)

### Community 102 - "NATSSubjectManager"
Cohesion: 0.01
Nodes (205): get_patterns(), get_subject_manager_dependency(), get_subject_statistics(), PatternsResponse, BaseModel, get, post, NATS Subject Management API Controller for MythosMUD. This module provides REST… (+197 more)

### Community 103 - "DistributedEventBus"
Cohesion: 0.05
Nodes (50): DistributedEventBus, Any, Distributed EventBus that uses NATS for cross-instance event distribution.…, EventBus that distributes domain events via NATS for horizontal scaling. When…, Initialize distributed EventBus. Args: nats_service: NATS service for…, Set NATS service and start the bridge (call after NATS connects)., Publish event locally and to NATS when bridge is active., Shutdown EventBus and stop NATS bridge. (+42 more)

### Community 104 - "test_npc_utils.py"
Cohesion: 0.03
Nodes (81): Check if this NPC is required to spawn., Prefer live NPC room attrs, then lifecycle SPAWNED/left event room_id., _resolve_despawn_room_id(), extract_definition_id_from_npc(), extract_npc_metadata(), extract_room_id_from_lifecycle_record(), extract_room_id_from_npc(), get_zone_key_from_room_id() (+73 more)

### Community 105 - "test_combat_monitoring_service.py"
Cohesion: 0.03
Nodes (91): AlertSeverity, AlertType, CombatMetrics, end_combat_monitoring(), get_combat_metrics(), get_combat_monitoring(), Enum, Combat monitoring and alerting service for MythosMUD. This service provides… (+83 more)

### Community 106 - "test_lifespan_startup.py"
Cohesion: 0.05
Nodes (68): _get_item_prototype_count(), _get_item_prototype_entries(), initialize_chat_service(), initialize_combat_services(), initialize_container_and_legacy_services(), initialize_mythos_time_consumer(), initialize_npc_services(), Initialize container and set up container reference on app.state. Services are… (+60 more)

### Community 107 - "command_result_text"
Cohesion: 0.07
Nodes (58): Remove or update item quantity in player inventory after transfer., remove_item_from_inventory(), handle_put_command(), _put_resolve_container_id(), _put_run_validated(), _put_transfer_finish(), PutCommandRuntime, PutValidatedWork (+50 more)

### Community 108 - "NPCCombatIntegrationService"
Cohesion: 0.03
Nodes (94): NPCCombatIntegrationService, ConnectionManager, UUID, Return combat messaging integration for room broadcasts (e.g. aggro switches)., Return combat service dependency for integration collaborators., Return NPC data provider dependency for integration collaborators., Return rewards dependency for integration collaborators., Return lucidity dependency for integration collaborators. (+86 more)

### Community 109 - "test_auth_utils.py"
Cohesion: 0.03
Nodes (113): E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio., One row in users plus optional default character for login E2E. (+105 more)

### Community 110 - "PanelState"
Cohesion: 0.09
Nodes (45): mergePanelMetadataFromDefault(), resolveInitialPanelLayout(), applyOptionalContentMinHeight(), clampDimensionsToViewport(), clampPanelLayoutToViewport(), clampSinglePanel(), clampTopLeftWithinBounds(), layoutFitsViewport() (+37 more)

### Community 111 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (90): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+82 more)

### Community 112 - "build_event"
Cohesion: 0.01
Nodes (197): build_event(), _get_next_global_sequence(), Protocol, UUID, Event envelope utilities for MythosMUD real-time messages. Provides a single,…, Minimal typing for connection_manager passed to build_event (sequence_counter…, Custom JSON encoder that handles UUID objects., Thread-safe global sequence number generation (fallback when no… (+189 more)

### Community 113 - "real_time.py"
Cohesion: 0.05
Nodes (81): _ensure_connection_manager(), _extract_bearer_token(), get_connection_statistics(), get_player_connections(), handle_new_game_session(), _invoke_handle_websocket_connection(), _parse_subprotocol_token(), _parse_websocket_token() (+73 more)

### Community 114 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.05
Nodes (85): object, _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch(), filter_valid_items() (+77 more)

### Community 115 - "QuestService"
Cohesion: 0.06
Nodes (46): _build_collect_n_progress(), _call_add_item_to_inventory(), _definition_completion_mode_error(), _goals_met(), _has_collect_n_goals(), _parse_definition(), Any, UUID (+38 more)

### Community 116 - "api/monitoring.py"
Cohesion: 0.06
Nodes (88): _assemble_health_response(), force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_health_status(), get_memory_alerts() (+80 more)

### Community 117 - "useMythosAppActions.ts"
Cohesion: 0.08
Nodes (46): postSelectCharacter(), executeDeleteCharacterUi(), nextStepForDeleteResult(), isGracePeriodServerUnavailableError(), tryStartLoginGracePeriod(), runSelectCharacterFlow(), selectCharacterNetworkErrorMessage(), SelectCharacterResult (+38 more)

### Community 118 - "test_player_presence_tracker.py"
Cohesion: 0.04
Nodes (91): _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _disconnect_during_rest_is_intentional(), _get_instance_manager_from_manager(), Any, UUID, Player presence tracking helper for connection manager. This module provides… (+83 more)

### Community 119 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (90): _collect_rotatable_logs(), detect_environment(), ensure_log_directory(), BoundLogger, Path, Logging utilities for directory management, path resolution, and environment…, Resolve log_base path to absolute path relative to project root. Args:…, Collect non-empty log files eligible for rotation. (+82 more)

### Community 120 - "test_look_player.py"
Cohesion: 0.04
Nodes (94): _apply_grace_period_labels(), _find_matching_players(), _format_player_look_display(), _get_players_in_room(), _handle_player_look(), _player_id_uuid(), Any, UUID (+86 more)

### Community 121 - "UserManager"
Cohesion: 0.07
Nodes (32): UUID, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Add a player as an admin. Args: player_id: Player ID player_name: Player name…, Update cache to mark load as failed., Convert mute_info datetime and UUID objects to JSON-serializable formats., Save player mutes to data dictionary for JSON serialization., Save channel mutes to data dictionary for JSON serialization. (+24 more)

### Community 122 - "MythosMUDError"
Cohesion: 0.11
Nodes (16): MythosMUDError, Log the error with structured context., Convert error to dictionary for API responses., Base exception for all MythosMUD errors. Provides structured error handling…, Test MythosMUDError can be instantiated., test_mythosmud_error(), Test MythosMUDError with custom context., Test MythosMUDError with additional details. (+8 more)

### Community 123 - "FeatureFlagService"
Cohesion: 0.03
Nodes (54): Initialize the combat configuration service., FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature… (+46 more)

### Community 124 - "Reporter"
Cohesion: 0.03
Nodes (47): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+39 more)

### Community 125 - "PlayerService"
Cohesion: 0.03
Nodes (81): CastingStateManager, Any, UUID, Casting state manager for tracking active spell castings. This module manages…, Check if a player is currently casting. Args: player_id: Player ID to check…, Get the casting state for a player. Args: player_id: Player ID Returns:…, Complete and remove a casting state. Args: player_id: Player ID Returns:…, Interrupt and remove a casting state. Args: player_id: Player ID Returns:… (+73 more)

### Community 126 - "test_player_death_service.py"
Cohesion: 0.03
Nodes (87): mock_event_bus(), mock_player(), mock_player_combat_service(), mock_session(), player_death_service(), player_death_service_no_dependencies(), asyncio, fixture (+79 more)

### Community 127 - "test_connection_helpers_impl.py"
Cohesion: 0.03
Nodes (91): broadcast_global_event_impl(), broadcast_room_event_impl(), convert_uuids_to_strings(), handle_new_login_impl(), mark_player_seen_impl(), _optimize_payload(), Any, _queue_message_if_needed() (+83 more)

### Community 128 - "useRespawnHandlers.ts"
Cohesion: 0.13
Nodes (28): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), fetchSpy (+20 more)

### Community 129 - "_as_mgr"
Cohesion: 0.10
Nodes (50): establish_websocket_connection(), Establish a new WebSocket connection. Args: websocket: The WebSocket connection…, _as_mgr(), _as_ws(), _FakeWebSocket, _make_manager(), WebSocket, Test _find_dead_connections() returns empty list when player not found. (+42 more)

### Community 130 - "test_quest_service.py"
Cohesion: 0.07
Nodes (75): _DefinitionRow, _FullInventory, _InstanceStub, _make_definition_row(), _make_kill_definition_row(), _make_turn_in_definition_row(), _message(), _MockDefRepo (+67 more)

### Community 131 - "test_communication_commands_flows.py"
Cohesion: 0.08
Nodes (47): _chat_send_with_room_bundle(), flow_local_command(), flow_say_command(), _global_player_bundle(), _message_from_command(), Handle the `say` command: broadcast speech to the current room., Handle the `local` command: room-only speech (not global)., Resolve primary IDs for whisper; return error dict if self-whisper or missing… (+39 more)

### Community 132 - "PlayerCombatService"
Cohesion: 0.03
Nodes (92): Set the player combat service for the connection manager., PlayerCombatService, PlayerCombatState, UUID, Attach NPC combat integration for UUID/XP mapping (post-construction wiring)., Track a player's combat state. Args: player_id: ID of the player player_name:…, Get a player's combat state. Args: player_id: ID of the player Returns:…, Clear a player's combat state. Args: player_id: ID of the player (+84 more)

### Community 133 - "deleteCharacterFlow.ts"
Cohesion: 0.07
Nodes (59): CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), extractErrorMessageFromResponseBody(), fetchCharactersList() (+51 more)

### Community 134 - "mythos_e2e_ddl.sql"
Cohesion: 0.09
Nodes (42): mythos_e2e.aliases, mythos_e2e.calendar_holidays, mythos_e2e.calendar_npc_schedules, mythos_e2e.container_contents, mythos_e2e.containers, mythos_e2e.dialogue_definitions, mythos_e2e.emote_aliases, mythos_e2e.emotes (+34 more)

### Community 135 - "test_metrics_endpoints.py"
Cohesion: 0.06
Nodes (79): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+71 more)

### Community 136 - "test_status_commands.py"
Cohesion: 0.08
Nodes (36): _get_profession_info(), Get profession information for a player. Args: player: Player object…, asyncio, Unit tests for status command handlers. Tests handlers for status and whoami…, Test _get_combat_status returns False when no combat service., Test _get_combat_status returns False when no app., Test _get_combat_status returns True when player is in combat., Test _get_combat_status returns False when player is not in combat. (+28 more)

### Community 137 - "mythos_unit_ddl.sql"
Cohesion: 0.09
Nodes (42): mythos_unit.aliases, mythos_unit.calendar_holidays, mythos_unit.calendar_npc_schedules, mythos_unit.container_contents, mythos_unit.containers, mythos_unit.dialogue_definitions, mythos_unit.emote_aliases, mythos_unit.emotes (+34 more)

### Community 138 - "connection_manager.py"
Cohesion: 0.01
Nodes (390): deque, _apply_disconnect_side_effects(), _cleanup_connection_tracking(), _cleanup_fully_disconnected_player(), _cleanup_player_data(), _cleanup_room_subscriptions(), cleanup_websocket_disconnect(), _close_and_untrack_websockets() (+382 more)

### Community 139 - "WebSocketMessageValidator"
Cohesion: 0.04
Nodes (80): MessageValidationError, BaseModel, Exception, WebSocket message validation for MythosMUD. This module provides comprehensive…, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Validate message against Pydantic schema. Args: message: Parsed JSON message…, Raised when message validation fails. (+72 more)

### Community 140 - "test_magic_commands.py"
Cohesion: 0.03
Nodes (115): handle_cast_command(), handle_learn_command(), handle_spell_command(), handle_spells_command(), handle_stop_command(), MagicCommandHandler, Any, Exception (+107 more)

### Community 141 - "test_npc_service.py"
Cohesion: 0.04
Nodes (87): _def_row(), _mock_result_mappings_all(), mock_session(), npc_service(), asyncio, fixture, Unit tests for NPC service. Tests the NPCService class., Test NPCService initialization. (+79 more)

### Community 142 - "SchemaValidator"
Cohesion: 0.03
Nodes (45): Path, Convert legacy string format exits to new object format internally. This allows…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in… (+37 more)

### Community 143 - "ChatMessage"
Cohesion: 0.10
Nodes (40): ChatMessage, Any, Represents a chat message with metadata., Convert message to dictionary for serialization., Log this chat message to the communications log., _attr(), _ctx(), _player() (+32 more)

### Community 144 - "manual_dependency_analysis.py"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 145 - "ErrorType"
Cohesion: 0.02
Nodes (154): JSONResponse, ErrorResponseDetailsInput, post, Request, Receive and log alert webhooks, webhook(), Error handlers package for MythosMUD. This package provides specialized error…, convert_pydantic_error() (+146 more)

### Community 146 - "GameStateProvider"
Cohesion: 0.09
Nodes (26): GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send… (+18 more)

### Community 147 - "Any"
Cohesion: 0.06
Nodes (21): Any, Retrieve current room drops as a defensive copy for callers. Args: room_id: The…, Append an item stack to the room drop ledger. Args: room_id: The room receiving…, Remove quantity of a drop entry, returning the removed stack. Args: room_id:…, Adjust quantity for an existing drop entry; removing entry when zero. Args:…, Add a player as an occupant of a room. Args: player_id: The player's ID…, Remove a player as an occupant of a room. Args: player_id: The player's ID…, Get online player occupants from room_occupants and room_subscriptions. Uses… (+13 more)

### Community 148 - "NATSRetryHandler"
Cohesion: 0.01
Nodes (234): Any, Attach event publisher and message handler when NATS is available., DeadLetterQueue, Any, Path, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve and remove oldest message from DLQ (async version). Returns: Message… (+226 more)

### Community 149 - "test_websocket_handler_validation_errors.py"
Cohesion: 0.04
Nodes (62): asyncio, Unit tests for WebSocket handler validation, rate limiting, and error paths.…, _validate_message should pass expected token from connection metadata into…, When metadata.token is missing, validate JWT from message and restore metadata., Test _send_error_response handles WebSocket disconnect., Test _send_error_response handles RuntimeError with disconnect message., Test _send_error_response handles RuntimeError with close message., Test _send_error_response handles other RuntimeError. (+54 more)

### Community 150 - "test_nats_broker.py"
Cohesion: 0.03
Nodes (77): asyncio, Unit tests for NATS message broker. Tests the NATSMessageBroker class., Test connect() passes TLS options to nats.connect when tls_enabled=True., Test disconnect() does nothing when no client., Test disconnect() successfully disconnects., Test disconnect() unsubscribes from all subscriptions., Test disconnect() handles unsubscribe errors gracefully., Test disconnect() raises MessageBrokerError on disconnect failure. (+69 more)

### Community 151 - "migrate_combat_data.py"
Cohesion: 0.14
Nodes (27): main(), migrate_npc_combat_data(), _migrate_one_npc(), MigrationResults, _npc_has_combat_data(), _npc_has_full_combat_data(), _omit_keys(), _present_keys() (+19 more)

### Community 152 - "LoggedHTTPException"
Cohesion: 0.01
Nodes (292): cleanup_admin_sessions(), get_admin_audit_log(), get_admin_sessions(), get, post, Request, Admin session and audit log endpoints under /admin/npc. Split out from…, Get active admin sessions. (+284 more)

### Community 153 - "ContainerRepository"
Cohesion: 0.10
Nodes (31): _container_data_to_dict(), ContainerRepository, Any, ContainerData, datetime, UUID, Update a container (async)., Get decayed containers (async). (+23 more)

### Community 154 - "1774539086359-useMythosAppState.ts"
Cohesion: 0.13
Nodes (26): AuthSlice, authSliceReducer(), creationSliceReducer(), INITIAL_AUTH_SLICE, INITIAL_CREATION_SLICE, PendingSkillsPayload, resolveNextState(), useAuthSliceSetters() (+18 more)

### Community 155 - "TaskRegistry"
Cohesion: 0.05
Nodes (56): get_registry(), Any, Task, Centralized TaskRegistry for MythosMUD server task lifecycle management. This…, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task… (+48 more)

### Community 156 - "DialogueService"
Cohesion: 0.06
Nodes (45): DialogueCursor, DialoguePrompt, DialogueService, format_dialogue_prompt(), UUID, In-memory dialogue session service for classic MUD talk (#583). Loads trees by…, Load and validate a dialogue tree, or clear cursor and return fade text., Return an error string if option_index is out of range for node. (+37 more)

### Community 157 - "RoomIDUtils"
Cohesion: 0.07
Nodes (35): Any, Check if NPC room IDs match target room IDs using fallback comparison. Args:…, Check if NPC room matches target room using normalized comparison. Args:…, Utilities for room ID normalization and comparison., Initialize room ID utilities. Args: connection_manager: ConnectionManager…, Get canonical room ID for consistent comparison. Args: room_id: The room ID…, Normalize room ID for comparison. Args: rid: Room ID to normalize Returns:…, Check if two normalized room IDs match. Args: id1: First normalized room ID… (+27 more)

### Community 158 - "CombatConfiguration"
Cohesion: 0.04
Nodes (50): CombatConfiguration, CombatConfigurationError, CombatConfigurationScope, CombatConfigurationService, get_combat_config(), get_combat_configuration(), is_combat_available(), Any (+42 more)

### Community 159 - "test_game_state_provider.py"
Cohesion: 0.03
Nodes (79): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for game state provider. Tests the GameStateProvider class. (+71 more)

### Community 160 - "test_npc_event_handlers.py"
Cohesion: 0.03
Nodes (81): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers. Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON. (+73 more)

### Community 161 - "chat_channel_message_senders.py"
Cohesion: 0.13
Nodes (36): ChatResult, _append_channel_history(), _authorize_global_sender(), _authorize_system_sender(), ChatPlayerView, ChatSendServices, _load_whisper_participants(), _log_and_store_system_message() (+28 more)

### Community 162 - "lifespan_startup.py"
Cohesion: 0.06
Nodes (66): _calculate_metrics_delta(), _cleanup_container_on_error(), _cleanup_dead_letter_queue_periodically(), _initialize_enhanced_systems(), lifespan(), _log_memory_metrics_periodically(), _persist_metrics_to_file(), _persist_mythos_state_on_error() (+58 more)

### Community 163 - "test_command_processor.py"
Cohesion: 0.03
Nodes (57): Unit tests for command processor. Tests the CommandProcessor class which…, Test process_command_string handles KeyError., Test process_command_string handles RuntimeError., Test _extract_attributes extracts attributes correctly., Test _extract_attributes handles missing attributes., Test _is_combat_command returns True for attack command., Test _is_combat_command returns True for punch command., Test _is_combat_command returns True for kick command. (+49 more)

### Community 164 - "map_minimap.py"
Cohesion: 0.04
Nodes (78): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities. Extracted from… (+70 more)

### Community 165 - "test_zone_config_loader.py"
Cohesion: 0.05
Nodes (76): async_load_zone_configurations(), extract_zone_name(), parse_json_field(), parse_zone_special_rules(), process_subzone_rows(), process_zone_rows(), Connection, Record (+68 more)

### Community 166 - "test_lucidity_recovery_commands.py"
Cohesion: 0.02
Nodes (188): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+180 more)

### Community 167 - "test_quest_events.py"
Cohesion: 0.08
Nodes (37): _entity_id_for_quest_offer(), _make_on_npc_died(), _make_on_player_entered(), _make_on_player_left(), _parse_player_id(), Any, UUID, Quest event subscriptions: room entry (trigger start), room exit… (+29 more)

### Community 168 - "test_communication_commands_say_me_pose.py"
Cohesion: 0.09
Nodes (37): handle_me_command(), handle_pose_command(), handle_say_command(), Room-wide say; returns user-facing result dict., Set or clear persistent pose text., asyncio, Unit tests for say, me, and pose communication command handlers., Test handle_me_command with no action. (+29 more)

### Community 169 - "test_message_handlers.py"
Cohesion: 0.03
Nodes (111): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, MessageHandlerFactory, PartyInviteResponseMessageHandler, PingMessageHandler (+103 more)

### Community 170 - "test_admin_setlucidity_command.py"
Cohesion: 0.03
Nodes (138): Admin permission validation utilities for MythosMUD. This module provides…, _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), _get_current_lcd(), _get_player_service_from_app() (+130 more)

### Community 171 - "test_combat_flee_helpers.py"
Cohesion: 0.05
Nodes (62): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules. Keeps…, Application object with a ``state`` namespace (dynamic attributes)., _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id() (+54 more)

### Community 172 - "test_shutdown_sequence.py"
Cohesion: 0.05
Nodes (73): _find_uvicorn_processes(), Any, Process termination utilities for graceful server shutdown. This module handles…, Schedule a best-effort graceful process termination after a short delay. This…, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available. (+65 more)

### Community 173 - "OccupantFormatter"
Cohesion: 0.04
Nodes (64): OccupantFormatter, Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Formats and separates occupants by type., Check if a string looks like a UUID. Args: value: The string to check Returns:…, Check if a name is valid for use as an occupant name. Args: name: The name to… (+56 more)

### Community 174 - "NPCLifecycleManager"
Cohesion: 0.01
Nodes (159): _create_npc_services_on_app(), Create NPC spawning, lifecycle, population services and instance service.…, Add an NPC to the room and trigger event. Args: npc_id: The ID of the NPC…, NPCLifecycleManager, Protocol, Initialize the NPC lifecycle manager. Args: event_bus: Event bus for publishing…, Record the death of an NPC to suppress respawning for 30 seconds. Args: npc_id:…, Check if an NPC is currently under death suppression. Args: npc_id: ID of the… (+151 more)

### Community 175 - "ScheduleService"
Cohesion: 0.03
Nodes (69): Construct holiday_service, schedule_service, and mythos_tick_scheduler.…, _DatabaseLoadResult, _fetch_schedule_entries(), _lower_string_list_from_row(), normalize_weekday_names(), Connection, datetime, Path (+61 more)

### Community 176 - "test_database_helpers.py"
Cohesion: 0.03
Nodes (112): normalize_database_url(), Set test override database URL., Normalize database URL for asyncpg. Args: database_url: Original database URL…, set_test_database_url(), _get_database_url_state(), close_db(), ensure_database_directory(), get_async_session() (+104 more)

### Community 177 - "test_party_service.py"
Cohesion: 0.04
Nodes (49): Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves., Leader can disband the party., Non-leader cannot disband. (+41 more)

### Community 178 - "PlayerRespawnService"
Cohesion: 0.07
Nodes (34): _PlayerCombatClearing, PlayerRespawnService, AsyncSession, datetime, Player, Protocol, UUID, Return current_dp as an int, defaulting to 0 for non-numeric values. (+26 more)

### Community 179 - "test_nats_message_handler_chat.py"
Cohesion: 0.03
Nodes (76): asyncio, Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _get_player_lucidity_tier returns default on error., Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_name…, Test _validate_chat_message_fields raises TypeError for invalid content type., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _extract_chat_message_fields handles whisper target_id. (+68 more)

### Community 180 - "waitForMessage"
Cohesion: 0.12
Nodes (35): primeBothForCoLocate(), waitForLookReflected(), executeUnmuteAndWaitForAck(), primeBothForCoLocate(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), NOTE: The 'open' command does not exist yet. (+27 more)

### Community 181 - "test_logging_handlers.py"
Cohesion: 0.04
Nodes (65): _aggregator_handler_class_for_windows(), AsyncioConnLostWriteFilter, create_aggregator_handler(), _make_exec_for_aggregator(), Any, LogRecord, Path, RotatingFileHandler (+57 more)

### Community 182 - "test_websocket_handler_helpers_extended.py"
Cohesion: 0.05
Nodes (57): mock_connection_manager(), mock_validator(), mock_websocket(), asyncio, fixture, Extended unit tests for websocket handler helper functions. Tests additional…, Test _send_error_response() handles WebSocketDisconnect., Test _send_error_response() returns False for RuntimeError indicating… (+49 more)

### Community 183 - "IdleMovementHandler"
Cohesion: 0.03
Nodes (81): _cfg_bool(), _cfg_float(), IdleMovementHandler, _npc_id_str(), _passes_movement_probability(), Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement. Checks multiple conditions: -…, Check if NPC is in combat via UUID lookup. Args: npc_id: NPC ID (string or… (+73 more)

### Community 184 - "PassiveMobNPC"
Cohesion: 0.05
Nodes (58): PassiveMobNPC, Check if idle movement should be scheduled based on configuration and timing.…, Create a WANDER action message. Args: current_time: Current timestamp Returns:…, Queue a WANDER action via the thread manager. Args: wander_action: The wander…, Schedule a WANDER action for idle movement if interval has elapsed. This method…, Respond to player interaction., Handle wandering action., Handle responding to greeting action. (+50 more)

### Community 185 - "test_player_disconnect_handlers.py"
Cohesion: 0.04
Nodes (71): age_off_disconnected_sessions(), _cleanup_player_references(), _collect_disconnect_keys(), _get_session_maps_for_age_off(), handle_player_disconnect_broadcast(), _purge_expired_sessions_from_maps(), Player, UUID (+63 more)

### Community 186 - "middleware"
Cohesion: 0.10
Nodes (32): CorrelationMiddleware, create_correlation_middleware(), create_websocket_correlation_middleware(), _get_header(), ASGIApp, Receive, Scope, Send (+24 more)

### Community 187 - "InventoryMutationGuard"
Cohesion: 0.03
Nodes (73): _AsyncPlayerGuardState, InventoryMutationGuard, _PlayerGuardState, Acquire sync mutation guard., Acquire async mutation guard., Get or create per-player guard state for sync contexts. Uses thread-safe…, Get or create per-player guard state for async contexts. Uses async lock to…, Clean up per-player guard state when no longer needed (sync context). Removes… (+65 more)

### Community 188 - "get_config"
Cohesion: 0.04
Nodes (63): main(), Load seed data and verify., get_config(), _is_test_mode(), Reset the configuration cache. In test mode, this is a no-op since get_config()…, Detect if running in test environment. Uses multiple detection methods to…, Get application configuration (singleton in production, fresh in tests). In…, reset_config() (+55 more)

### Community 189 - "test_websocket_handler_core.py"
Cohesion: 0.03
Nodes (86): handle_websocket_message(), WebSocket, Handle a WebSocket message from a player. Args: websocket: The WebSocket…, Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), asyncio, Unit tests for core websocket handler functions. Tests core WebSocket handler…, Test _process_message processes message. (+78 more)

### Community 190 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.08
Nodes (50): _dispatch_player_event(), LucidityChangeEventExtras, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send rescue progress/status updates to either participant., Send an event to a specific player, swallowing transport errors in headless…, Optional lucidity change event fields (reduces send_lucidity_change_event… (+42 more)

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
Cohesion: 0.03
Nodes (84): AlertResolveResponse, AlertsResponse, CacheMetricsResponse, DualConnectionStatsResponse, EventBusMetricsResponse, MemoryAlertsResponse, MemoryLeakMetricsResponse, MemoryStatsResponse (+76 more)

### Community 195 - "useGameClientV2Container.ts"
Cohesion: 0.11
Nodes (36): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), forceLogoutFallback(), performGameClientLogout(), stillShowingGameClient() (+28 more)

### Community 196 - "ContainerService"
Cohesion: 0.07
Nodes (80): ContainerService, Service for managing container operations. Orchestrates open/close, transfer…, MutationDecision, Result of attempting to acquire a guarded mutation context., asyncio, Test get_player_id_from_user raises exception when player not found., Test execute_transfer function., Test execute_transfer calls transfer_to_container for to_container direction. (+72 more)

### Community 197 - "test_websocket_helpers.py"
Cohesion: 0.02
Nodes (136): get_container_async_persistence(), Get the container-backed AsyncPersistenceLayer instance. Use for code that has…, Prepare room data with NPC and player names for a respawn event., _accumulate_valid_occupant_name(), _AppStateForPlayerService, build_basic_player_data(), check_shutdown_and_reject(), convert_schema_to_dict() (+128 more)

### Community 198 - "logging_file_setup.py"
Cohesion: 0.05
Nodes (77): Logger, Queue, QueueHandler, QueueListener, add_handler_to_loggers(), LoggerNameFilter, LogRecord, Filter that only allows logs from loggers matching specified prefixes. This… (+69 more)

### Community 199 - "quest_service.py"
Cohesion: 0.09
Nodes (35): Schedule personal system chat from sync or async callers., schedule_personal_system(), Quest subsystem: service, goal progression, rewards., _as_int(), _goal_is_met(), notify_quest_abandoned(), notify_quest_completed(), notify_quest_progress() (+27 more)

### Community 200 - "Room"
Cohesion: 0.01
Nodes (171): ObjectAddedToRoom, ObjectRemovedFromRoom, Event fired when an object is removed from a room. This event is triggered when…, Event fired when an object is added to a room. This event is triggered when an…, Events module for MythosMUD. This module provides the event system for tracking…, Instance, InstanceManager, Room (+163 more)

### Community 201 - "test_health_monitor.py"
Cohesion: 0.07
Nodes (35): health_monitor(), mock_cleanup_dead_websocket(), mock_is_websocket_open(), mock_performance_tracker(), mock_validate_token(), asyncio, fixture, Unit tests for health monitor. Tests the HealthMonitor class. (+27 more)

### Community 202 - "test_player_event_handlers_room.py"
Cohesion: 0.04
Nodes (70): asyncio, Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test broadcast_player_entered_message() skips when room_id is None., Test subscribe_player_to_room() successfully subscribes player., Test subscribe_player_to_room() handles invalid player_id., Test subscribe_player_to_room() handles subscription errors., Test _send_room_name_message() sends room name., Test _prepare_room_data() prepares room data with to_dict. (+62 more)

### Community 203 - "PlayerStateCommandFactory"
Cohesion: 0.04
Nodes (59): Unit tests for player state command factories. Tests the…, Test create_skills_command() raises error with args., Test create_journal_command() creates JournalCommand., Test create_journal_command() raises error with args., Test create_quests_command() creates QuestsCommand., Test create_quests_command() raises error with args., Test create_quest_command() with no args creates QuestCommand with empty list., Test create_status_command() creates StatusCommand. (+51 more)

### Community 204 - "get_player_quests"
Cohesion: 0.09
Nodes (33): get_player_quests(), Get quest log for a character. Requires ownership (403 if not owner)., Quest subsystem schemas: definition, progress, API responses., BaseModel, QuestGoalSchema, QuestLogEntryResponse, QuestLogResponse, QuestRewardSchema (+25 more)

### Community 205 - "RoomEventHandler"
Cohesion: 0.11
Nodes (24): Integration components for connection management. This package provides…, Any, UUID, Room event handling for connection management. This module provides integration…, Handle PlayerEnteredRoom events by broadcasting updated occupant count., Handle PlayerLeftRoom events by broadcasting updated occupant count., Handles room movement events and broadcasts occupant updates. This class…, Initialize the room event handler. Args: room_manager: RoomSubscriptionManager… (+16 more)

### Community 206 - "admin_mute_commands.py"
Cohesion: 0.10
Nodes (34): _collect_mute_display_lines(), _extract_mute_target(), _format_mute_line(), handle_mute_command(), handle_mutes_command(), handle_unmute_command(), _mute_command_app(), _mute_display_target() (+26 more)

### Community 207 - "test_metrics.py"
Cohesion: 0.04
Nodes (53): Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, metrics(), fixture, Unit tests for NATS Subject Manager Metrics. Tests the SubjectManagerMetrics…, Test record_build() stores build times., Test record_error() records pattern_not_found error. (+45 more)

### Community 208 - "LogAggregator"
Cohesion: 0.06
Nodes (48): LogEntry, aggregate_log_entry(), get_log_aggregator(), LogAggregator, LogEntry, LogQueryFilter, _optional_datetime_from_object(), _optional_str_from_object() (+40 more)

### Community 209 - "test_room_renderer.py"
Cohesion: 0.04
Nodes (53): Test format_room_drop_lines() formats room drops., Test format_room_drop_lines() returns empty message for empty drops., Test format_room_drop_lines() handles None., Test format_room_drop_lines() uses fallback for missing item_name., test_format_room_drop_lines(), test_format_room_drop_lines_empty(), test_format_room_drop_lines_fallback_name(), test_format_room_drop_lines_none() (+45 more)

### Community 210 - "ChatHistoryPanel.tsx"
Cohesion: 0.03
Nodes (78): EldritchEffectsDemo(), EldritchEffectsDemoProps, mockAlert, ALWAYS_ACTIVE_EFFECTS, effectClass(), EffectOption, ELDRITCH_EFFECT_OPTIONS, hasEffect() (+70 more)

### Community 211 - "Async Remediation Summary - December 3, 2025"
Cohesion: 0.03
Nodes (67): 1. Fixed Event Loop Blocking in PassiveLucidityFluxService, 2. Removed asyncio.run() from Exploration Service, 3. Added Exception Handling for Database Engine Creation, Achieved, 🏆 Achievement Highlights, Adjusts spectacles with scholarly satisfaction, After, After Fixes (+59 more)

### Community 212 - "test_rescue_commands.py"
Cohesion: 0.09
Nodes (39): handle_rescue_command(), Delegate rescue handling to the RescueService for testable, real logic., asyncio, patch, Unit tests for rescue command handlers. Tests the rescue command functionality., Test handle_ground_command() handles missing target., Test handle_ground_command() handles rescuer not found., Test handle_ground_command() handles target not found. (+31 more)

### Community 213 - "chat_nats_publisher.py"
Cohesion: 0.09
Nodes (34): UUID, Chat message model for MythosMUD. This module provides the ChatMessage class…, _chat_passes_nats_validation(), _log_nats_publish_error(), _log_nats_unexpected_error(), Exception, Chat NATS publishing utilities. This module provides NATS subject building and…, Return True when message content and room access checks pass. (+26 more)

### Community 214 - "PerformanceMonitor"
Cohesion: 0.05
Nodes (48): Initialize the monitoring dashboard. Args: memory_leak_collector: Optional pre-…, ExportMetrics, get_performance_monitor(), get_performance_stats(), measure_performance(), peek_performance_monitor(), PerformanceMetric, PerformanceMonitor (+40 more)

### Community 215 - "NPCCombatIntegration"
Cohesion: 0.03
Nodes (114): NPCAttacked, Event fired when an NPC attacks a target. This event is triggered when an NPC…, Protocol, Aggressive mob NPC type for MythosMUD. This module provides the…, Protocol for persistence with get_room_by_id., Return the room object for the given room_id, or None if not found., _RoomPersistence, Return the live NPC combat integration service for delegation. Prefer… (+106 more)

### Community 216 - "test_invite_schemas.py"
Cohesion: 0.03
Nodes (91): get_current_active_user, create_invite(), CurrentUserInfo, get_current_user_info(), list_invites(), Depends, get, TypedDict (+83 more)

### Community 217 - "player.ts"
Cohesion: 0.11
Nodes (31): locationIndicatesDeathVoid(), requiredAliveButDeadMessage(), assertLookVisibleInPanels(), lookAndStand(), prepAwForAdminSet(), prepNonAdminForSetAttempt(), runAdminSetWithRecovery(), assertNpcSpawnVisible() (+23 more)

### Community 218 - "MonitoringDashboard"
Cohesion: 0.06
Nodes (39): PerformanceStats, Alert, MonitoringDashboard, Any, Get overall system health status. Returns: Current system health status, Get comprehensive monitoring summary. Returns: Complete monitoring summary with…, Evaluate thresholds and record new alerts., Record a custom alert emitted by subsystems. Args: alert_type: Identifier for… (+31 more)

### Community 219 - "resolve_lazy_attr"
Cohesion: 0.07
Nodes (34): _ConnectionManagerAPI, Protocol, UUID, Send a system notification to a player. Args: player_id: The player's ID…, Send a player status update to a player. Args: player_id: The player's ID…, Send room description to a player. Args: player_id: The player's ID room_data:…, Structural type for API helpers; avoids importing ConnectionManager., Resolve manager without importing ConnectionManager (import cycle). (+26 more)

### Community 220 - "test_communication_commands_channels.py"
Cohesion: 0.10
Nodes (34): handle_global_command(), handle_local_command(), handle_system_command(), Local channel message., Global channel message (level-gated in flow)., Admin-only system broadcast., asyncio, Unit tests for local, global, and system chat command handlers. (+26 more)

### Community 221 - "test_skill_service.py"
Cohesion: 0.05
Nodes (63): catalog_with_own_language_and_mythos(), mock_persistence(), mock_player_skill_repo(), mock_skill_repo(), mock_skill_use_log_repo(), _occupation_slots_9(), _personal_interest_4(), asyncio (+55 more)

### Community 222 - "lifespan_protocols.py"
Cohesion: 0.07
Nodes (63): MemoryMonitor, _container_attr(), _legacy_container_attr(), lifespan_connection_manager(), lifespan_container(), lifespan_event_bus(), lifespan_memory_monitor(), lifespan_nats_handler() (+55 more)

### Community 223 - "test_logout_commands.py"
Cohesion: 0.08
Nodes (40): _get_player_for_logout(), Get player for logout, handling cache corruption and persistence fallback.…, asyncio, Unit tests for logout commands. Tests the logout and quit command handlers for…, Test _get_player_for_logout retrieves player from persistence when not in cache., Test _get_player_for_logout handles corrupted cache (coroutine instead of…, Test _get_player_for_logout handles persistence errors gracefully., Test _get_player_for_logout handles persistence returning coroutine. (+32 more)

### Community 224 - "AggressiveMobNPC"
Cohesion: 0.04
Nodes (48): Get list of player IDs currently in the room. Returns: List of player IDs in…, AggressiveMobNPC, Debug log for context enrichment (best-effort, must not fail)., Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…, Hunt a specific target., Resolve attack_damage from behavior config with robust typing., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target. (+40 more)

### Community 225 - "CombatEventHandler"
Cohesion: 0.11
Nodes (28): CombatEventHandler, Any, UUID, Publish attack events and calculate XP reward. Args: current_participant:…, Calculate XP reward for defeating an NPC. Args: npc_id: ID of the defeated NPC…, Award XP to player for defeating an NPC. Args: current_participant: Attacking…, Publish combat ended event., Handles combat event publishing. (+20 more)

### Community 226 - "container_query_helpers_async.py"
Cohesion: 0.14
Nodes (28): Shared parameters for container creation (sync DB and async repository paths)., _build_container_data_from_row_async(), get_containers_by_entity_id_async(), get_containers_by_room_id_async(), get_decayed_containers_async(), _parse_jsonb(), Any, AsyncSession (+20 more)

### Community 227 - "test_lifecycle_periodic.py"
Cohesion: 0.06
Nodes (54): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD. This module defines configuration settings for…, Configuration for NPC lifecycle maintenance. This class centralizes all timing…, Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…, Check if NPC maintenance should run on this tick. Args: tick_count: Current…, Get a summary of all NPC configuration values. Returns: Dictionary containing…, Clean up old lifecycle records (delegates to lifecycle_periodic). (+46 more)

### Community 228 - "test_error_handling_middleware.py"
Cohesion: 0.14
Nodes (25): ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Read user id from a non-Mapping request.state.user (object with get and/or id).…, Pure ASGI middleware to handle all exceptions across FastAPI endpoints. This…, Initialize error handling middleware. Args: app: ASGI application instance…, _error_log_kwargs(), _http_scope() (+17 more)

### Community 229 - "EventHandler"
Cohesion: 0.05
Nodes (53): _as_event_data_dict(), _EventBusPublishPort, EventHandler, _npc_died_broadcast_and_bridge(), _npc_died_ids_or_warn(), _participant_key_strings(), _publish_npc_died_to_event_bus(), ConnectionManager (+45 more)

### Community 230 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (35): CatatoniaRegistry, datetime, UUID, In-memory registry tracking catatonic investigators., Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not… (+27 more)

### Community 231 - "GameClientV2Dock.test.tsx"
Cohesion: 0.07
Nodes (28): fetchSpy, chatHistoryLayoutIdentity, chatHistoryLayoutState, defaultChatHistoryLayoutKey, dockTest, mockPanelRecord(), mockPanelRecordCore(), mockPanelRecordFlags() (+20 more)

### Community 232 - "NPCCombatUUIDMapping"
Cohesion: 0.05
Nodes (34): Return UUID mapping dependency for integration collaborators., NPCCombatUUIDMapping, UUID, Get the original string ID from a UUID. Args: uuid_id: The UUID to look up…, Get XP value for a UUID. Args: uuid_id: The UUID to look up Returns: XP value…, Manages UUID mappings for NPC combat., Initialize UUID mapping storage., Check if a string is a valid UUID. Args: uuid_string: String to check Returns:… (+26 more)

### Community 233 - "PhantomHostileService"
Cohesion: 0.07
Nodes (25): PhantomHostileService, Any, UUID, Return the full data dict for one phantom, or None if it's gone (#625)., Find one of the player's active phantoms by (case-insensitive) name, scoped to…, Remove a phantom hostile from tracking. Args: player_id: Player UUID…, Get list of active phantom IDs for a player. Args: player_id: Player UUID…, Clear all phantom hostiles for a player. Args: player_id: Player UUID (+17 more)

### Community 234 - "test_command_service.py"
Cohesion: 0.03
Nodes (75): CommandHandler, CommandService, Command, Main command processing service for MythosMUD. This service handles command…, Initialize the command service., Parse and validate command string. Returns: tuple of (parsed_command, cmd,…, Prepare command_data dictionary by merging parsed command fields. Returns:…, Extract non-private, non-callable attributes from parsed_command, excluding… (+67 more)

### Community 235 - "._init_player_quest_layer"
Cohesion: 0.07
Nodes (19): Any, Exception, Wire user_manager into follow_service and nats_message_handler when present., Set item prototype registry on player service when both are available., Create room and profession cache services; set to None on RuntimeError., Wire player/room/user, container, skill, level, and quest services., Create the emote repository/service and load predefined emotes once, at…, Initialize game services. Requires Core and Realtime. (+11 more)

### Community 236 - "validate_room_data"
Cohesion: 0.14
Nodes (12): patch, Test validate_room_data() returns empty list when validation not available., Test validate_room_data() with provided validator., Test validate_room_data() creates validator when not provided., Test validate_room_data() returns validation errors., Test validate_room_data() raises exception in strict mode with errors., Test validate_room_data() returns empty list when validator creation fails., Test validate_room_data() handles validation exception. (+4 more)

### Community 237 - "_MagicServiceCore"
Cohesion: 0.08
Nodes (28): _CombatTickState, _MagicServiceCore, _PlayerPersistence, JsonMap, Protocol, UUID, Load player and return normalized stats (MP/max_MP). Returns (player, stats) or…, Return (False, message) if not enough MP, else (True, ''). (+20 more)

### Community 238 - "websocket_handler.py"
Cohesion: 0.06
Nodes (48): get_message_validator(), Get the global message validator instance., handle_json_decode_error(), handle_message_loop_exception(), handle_websocket_disconnect(), handle_websocket_generic_exception(), handle_websocket_message_loop(), handle_websocket_runtime_error() (+40 more)

### Community 239 - "asyncio"
Cohesion: 0.06
Nodes (31): asyncio, Test is_player_muted_async() returns True when player is muted., Test is_player_muted_async() returns False when player is not muted., Test add_admin() handles missing persistence (#679: injected, not via…, Test add_admin() handles player not found., Test remove_admin() handles missing persistence (#679: injected, not via…, Test remove_admin() handles player not found., Test is_admin() returns False when persistence not available (#679: injected). (+23 more)

### Community 240 - "security.ts"
Cohesion: 0.07
Nodes (22): SafeHtml(), SafeHtmlProps, collectWindowCandidates(), COMMAND_PROBE_CONFIG, DOMPurifyInstance, getDomPurify(), INCOMING_HTML_PROBE_CONFIG, resetDomPurifyClientForTests() (+14 more)

### Community 241 - "RoomMapViewer.tsx"
Cohesion: 0.09
Nodes (39): fetchSpy, useMapLayout(), buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData(), UseRoomMapDataResult (+31 more)

### Community 242 - "session_factory"
Cohesion: 0.12
Nodes (26): FixtureRequest, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+18 more)

### Community 243 - "test_level_service.py"
Cohesion: 0.05
Nodes (56): level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level(), UUID (+48 more)

### Community 244 - "InventorySchemaValidationError"
Cohesion: 0.06
Nodes (47): Initialize the player repository. Args: room_cache: Shared room cache for room…, _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Validate and serialize inventory payload. Returns (inventory_json,… (+39 more)

### Community 245 - "NPCOccupantProcessor"
Cohesion: 0.11
Nodes (23): NPCOccupantProcessor, NPC occupant processing utilities. This module handles querying and processing…, Processes NPC occupants for rooms., Get lifecycle manager for filtering fallback NPCs. Returns: Lifecycle manager…, Check if a single fallback NPC should be included. Args: npc_id: The NPC ID to…, Filter fallback NPCs to only include those in active_npcs and alive. Args:…, Room ID normalization and comparison utilities. This module provides utilities…, Initialize the room occupant manager. Args: connection_manager:… (+15 more)

### Community 246 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages. These schemas define the structure and… (+55 more)

### Community 247 - "ModerationCommandFactory"
Cohesion: 0.05
Nodes (58): Unit tests for moderation command factories. Tests the ModerationCommandFactory…, Test create_mute_global_command() with duration and reason., Test create_mute_global_command() with reason but no duration., Test create_unmute_global_command() creates UnmuteGlobalCommand., Test create_unmute_global_command() raises error with no args., Test create_unmute_global_command() raises error with multiple args., Test create_admin_command() creates AdminCommand., Test create_mute_command() creates MuteCommand. (+50 more)

### Community 248 - "devDependencies"
Cohesion: 0.05
Nodes (41): devDependencies, cross-env, esbuild, eslint-plugin-playwright, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals, jsdom (+33 more)

### Community 249 - "StyleGuideSections.tsx"
Cohesion: 0.06
Nodes (47): buildPanelClasses(), CONTENT_PADDING, HEADER_PADDING, MythosPanel(), MythosPanelProps, SIZE_CLASSES, VARIANT_CLASSES, AllStats() (+39 more)

### Community 250 - "PlayerGuidFormatter"
Cohesion: 0.06
Nodes (50): PlayerGuidFormatter, Player GUID Formatter for MythosMUD logging system. This module provides a…, Determine if a GUID is likely to be a player ID based on context. Args: guid:…, Get player name for GUID from in-memory data. Args: guid: The player GUID to…, Custom formatter that converts player GUIDs to "<name>: <GUID>" format. This…, Initialize the PlayerGuidFormatter. Args: player_service: Service for accessing…, formatter(), mock_player_service() (+42 more)

### Community 251 - "GameEvent"
Cohesion: 0.18
Nodes (13): GameEvent, EventStore, IEventStore, ensureSelfListedInRoomPlayers(), HANDLERS, projectEvent(), projectState(), getInitialGameState() (+5 more)

### Community 252 - "Any"
Cohesion: 0.10
Nodes (15): Any, UUID, Raise ValueError if any skill_id appears in both occupation and personal…, Build skill_key -> total modifier from profession skill_modifiers (supports…, Compute final skill_id -> value: base + profession mod, then occupation…, Validate skills allocation without persisting. Raises ValueError if invalid.…, Set all skills for a character at creation. Validates occupation_slots (9…, Return list of {skill_id, skill_key, skill_name, value} for the player. If the… (+7 more)

### Community 253 - ".state"
Cohesion: 0.14
Nodes (16): _app_state_container_service(), handle_explore_command(), Any, Handle exploration requests by returning a simple message. This lightweight…, FastAPI/Starlette application (or duck-typed equivalent)., _get_ground_services(), Get persistence and registry from request. Returns (persistence, registry)., Current FSM state as a single State. Uses python-statemachine 3.x configuration… (+8 more)

### Community 254 - "fixtures/auth.ts"
Cohesion: 0.06
Nodes (45): RoomSummary, STANDARD_DIRECTIONS, assertCommandChannelReady(), clickWithoutStability(), EnsurePlayableConnectionOptions, getLivePageForUsername(), getPageSessionCredentials(), isPageUsable() (+37 more)

### Community 255 - "dialogue_definitions_api.py"
Cohesion: 0.09
Nodes (44): create_dialogue_definition(), delete_dialogue_definition(), get_dialogue_definition(), list_dialogue_definitions(), delete, get, post, put (+36 more)

### Community 256 - "GameTickService"
Cohesion: 0.06
Nodes (30): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+22 more)

### Community 257 - "useGameConnectionRefactored.ts"
Cohesion: 0.07
Nodes (29): ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach(), wsConnectionBeforeEach() (+21 more)

### Community 258 - "testing_examples.py"
Cohesion: 0.04
Nodes (51): async_operation(), client, database, LoggingMiddleware, process_batch(), process_item(), asyncio, Test WebSocket logging in integration tests. (+43 more)

### Community 259 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.10
Nodes (52): check_ai_guardrails(), _check_single_use_file(), _collect_code_texts(), _guardrail_scan_inputs(), _is_single_use_small_file(), _process_added_file_checks(), build_context(), ChangedFile (+44 more)

### Community 260 - "gen_arena_migration_sql.py"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 261 - "test_exceptions_comprehensive.py"
Cohesion: 0.06
Nodes (34): handle_exception(), NetworkError, Exception, Network and communication errors., Convert a generic exception to a MythosMUD error. Args: exc: The original…, Comprehensive unit tests for exceptions module. Tests exception classes,…, Test MythosMUDError.to_dict() converts to dictionary., Test AuthenticationError can be instantiated. (+26 more)

### Community 262 - "combat_taunt.py"
Cohesion: 0.06
Nodes (51): _apply_taunt_and_maybe_broadcast(), AppWithState, Protocol, UUID, Taunt command flow: validation and execution. Extracted from combat.py to…, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Apply taunt and broadcast target switch if aggro changed. Returns error dict or… (+43 more)

### Community 263 - "CombatMonitoringService"
Cohesion: 0.04
Nodes (36): Alert, CombatMonitoringService, Any, Convert to dictionary., Comprehensive combat monitoring and alerting service. Tracks combat system…, Initialize the combat monitoring service., Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier… (+28 more)

### Community 264 - "test_combat_service.py"
Cohesion: 0.07
Nodes (57): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+49 more)

### Community 265 - "test_rescue_service.py"
Cohesion: 0.04
Nodes (73): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+65 more)

### Community 266 - "systemHandlers.ts"
Cohesion: 0.08
Nodes (42): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, appendDaypartChange(), appendHourChime() (+34 more)

### Community 267 - "http_exception_handler"
Cohesion: 0.10
Nodes (22): create_player(), general_exception_handler(), get_player(), http_exception_handler(), list_players(), log_api_requests(), Exception, get (+14 more)

### Community 268 - "EnvironmentalContainerLoader"
Cohesion: 0.12
Nodes (20): EnvironmentalContainerLoader, Any, UUID, Environmental container loader for unified container system. As documented in…, migrate_room_container_to_postgresql., Load all environmental containers for a room from PostgreSQL. Args: room_id:…, Service for loading environmental containers from JSON and PostgreSQL. Handles…, Initialize the environmental container loader. Args: persistence: Persistence… (+12 more)

### Community 269 - "test_chat_nats_publisher.py"
Cohesion: 0.10
Nodes (47): _build_legacy_subject(), _build_nats_message_data(), build_nats_subject(), _build_standardized_subject(), _extract_subzone_from_room(), _nats_service_ready(), publish_chat_message_to_nats(), Any (+39 more)

### Community 270 - "NATSServicePoolMixin"
Cohesion: 0.05
Nodes (33): configure_nats_tls(), nats_connect(), _NatsConnectFn, NatsConnectOptions, Client, Protocol, TypedDict, Apply TLS settings from NATS config onto connect options. (+25 more)

### Community 271 - "test_player_service_mutations.py"
Cohesion: 0.05
Nodes (61): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service mutations. Covers delete, location update, mythos…, Test apply_corruption() applies corruption., Test gain_occult_knowledge() increases occult knowledge., Test heal_player() heals player. (+53 more)

### Community 272 - "models/combat.py"
Cohesion: 0.01
Nodes (188): CombatParticipantType, CombatStatus, _get_default_damage(), Enum, Combat system models for in-memory state management. This module defines the…, Get the default damage value from configuration., Status of a combat instance., Type of combat participant. (+180 more)

### Community 273 - "test_look_room.py"
Cohesion: 0.03
Nodes (111): _filter_other_players(), _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id() (+103 more)

### Community 274 - "HealthErrorResponse"
Cohesion: 0.25
Nodes (8): HealthErrorResponse, Error response for health check failures., Test HealthErrorResponse can be created with required fields., Test HealthErrorResponse rejects unknown fields., Test HealthErrorResponse is frozen (immutable)., test_health_error_response_creation(), test_health_error_response_frozen(), test_health_error_response_rejects_extra_fields()

### Community 275 - "ExceptionTracker"
Cohesion: 0.03
Nodes (86): auth_service(), BackgroundTasks, File, oauth2_scheme, Update player with background task and enhanced logging., Background task for player update with enhanced logging., Simulate auth service., update_player_background() (+78 more)

### Community 276 - "NPCCombatIntegrationReadApi"
Cohesion: 0.08
Nodes (21): EventBusPublish, lifecycle_lookup_id(), NPCCombatIntegrationReadApi, NPCCombatRewardsLike, original_string_id_for_npc(), PlayerXpLike, Protocol, UUID (+13 more)

### Community 277 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 278 - "test_rate_limiter.py"
Cohesion: 0.08
Nodes (25): Unit tests for rate limiter service. Tests the RateLimiter class which provides…, Test check_rate_limit returns True when within limits., Test check_rate_limit returns False when limit exceeded., Test check_rate_limit handles errors gracefully (fails open)., Test record_message adds timestamp to window., Test reset_player_limits handles nonexistent player., Test get_system_stats handles no active players., Test is_player_rate_limited returns False when not rate limited. (+17 more)

### Community 279 - "get_global_tracked_manager"
Cohesion: 0.10
Nodes (20): create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), Managed Task Cleanup Service - Runtime Detection for Memory Threshold…, Create an instance of the MemoryThresholdMonitor with user-specified…, Factory function returning implementation conforming to Task 4.3 Specified…, Any, Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task…, Execute a single investigation loop synchronously producing operator summary.… (+12 more)

### Community 280 - "utils/layout.ts"
Cohesion: 0.10
Nodes (36): UseMapLayoutOptions, applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyLinkForces() (+28 more)

### Community 281 - "time_event_consumer.py"
Cohesion: 0.13
Nodes (18): Initialize the Temporal context: holiday/schedule/tick-scheduler, then the…, MythosHourTickEvent, Event fired when the accelerated Mythos clock rolls over to a new hour., asyncio, fixture, Unit tests for MythosTimeEventConsumer hour tick handling., test_describe_state(), test_handle_tick_updates_room_and_broadcasts() (+10 more)

### Community 282 - "test_connection_state_machine.py"
Cohesion: 0.08
Nodes (25): Unit tests for connection state machine. Tests the NATSConnectionStateMachine…, Test start_reconnect() transition from disconnected to reconnecting., Test open_circuit() transition from reconnecting to circuit_open., Test can_attempt_connection() returns True when disconnected., Test can_attempt_connection() returns True when connecting., Test should_open_circuit() returns False when under threshold., Test get_stats() handles None connected time., Test reconnect_attempts resets on successful connection. (+17 more)

### Community 283 - "test_rate_overrides.py"
Cohesion: 0.05
Nodes (69): get_asyncpg_server_settings_for_database_url(), Build asyncpg ``server_settings`` so unqualified table names resolve like…, _async_load_lucidity_rate_overrides(), build_override_key(), extract_lucidity_rate(), load_lucidity_rate_overrides(), _LucidityRateLoadResult, _normalize_database_url() (+61 more)

### Community 284 - "test_validation.py"
Cohesion: 0.03
Nodes (64): custom_length_validator(), fixture, Unit tests for NATS Subject Validator. Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter. (+56 more)

### Community 285 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 286 - "HealthStatus"
Cohesion: 0.03
Nodes (124): HealthStatus, ConnectionsComponent, DatabaseComponent, HealthComponents, HealthResponse, HealthStatus, BaseModel, StrEnum (+116 more)

### Community 287 - "test_combat_handler.py"
Cohesion: 0.07
Nodes (54): _AppStatePersistence, _AppWithPersistence, _as_app_with_state(), _CmdType, _handler_with_persistence(), mock_persistence(), AppWithState, asyncio (+46 more)

### Community 288 - "health_service"
Cohesion: 0.40
Nodes (5): health_service(), mock_connection_manager(), fixture, Create a mock connection manager., Create a HealthService instance.

### Community 289 - "MythosTickScheduler"
Cohesion: 0.04
Nodes (62): HolidayResolver, Any, Initialize configuration and set environment variables for legacy compatibility., mock_chronicle(), mock_event_bus(), mock_task_registry(), asyncio, fixture (+54 more)

### Community 290 - "utils/config.ts"
Cohesion: 0.11
Nodes (18): AppRouter(), DialogueEditorPage, MapPage, SkillsPage, AppCreationFlowViews(), creationShell(), renderNameStep(), renderProfessionStep() (+10 more)

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
Cohesion: 0.07
Nodes (40): MemoryThresholdMonitor, Any, Generate status report for diagnostic monitoring. Returns: Dictionary…, Runtime detection and cleanup of orphaned tasks based on memory thresholds.…, Runtime monitor for detecting memory threshold violations requiring cleanup.…, Initialize the memory threshold monitoring service. Args: memory_threshold_mb:…, Get current memory usage in bytes for this process., Get count of active tasks in the current event loop. (+32 more)

### Community 295 - "logout_commands.py"
Cohesion: 0.14
Nodes (24): _disconnect_player_connections(), _force_disconnect_player(), _get_app_services(), handle_logout_command(), handle_quit_command(), _mark_quit_intentional(), _prepare_player_for_logout(), Any (+16 more)

### Community 296 - "field_validator"
Cohesion: 0.22
Nodes (5): field_validator, Validate spell name format., Validate target format., Validate spell name format., Validate spell name format.

### Community 297 - "item_instance_persistence.py"
Cohesion: 0.15
Nodes (23): create_item_instance(), ensure_item_instance(), _execute_item_instance_upsert(), get_item_instance(), _handle_item_instance_db_error(), item_instance_exists(), _item_instance_row_values(), Any (+15 more)

### Community 298 - "alias_schema.json"
Cohesion: 0.04
Nodes (51): command, version, additionalProperties, additionalProperties, description, properties, required, type (+43 more)

### Community 299 - "test_party_commands.py"
Cohesion: 0.08
Nodes (49): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+41 more)

### Community 300 - "NATSMessageBroker"
Cohesion: 0.09
Nodes (19): PublishError, Exception raised when publishing message fails., NATSMessageBroker, Any, Connect to NATS server. Returns: bool: True if connection successful, False…, Check if connected to NATS and healthy. Returns: bool: True if connected and…, Publish message to NATS subject., Subscribe to NATS subject with message handler. (+11 more)

### Community 301 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+21 more)

### Community 302 - "Profession"
Cohesion: 0.05
Nodes (50): CharacterNameScreenProps, CreateCharacterPayload, MechanicalEffect, Profession, ProfessionCard(), ProfessionCardProps, StatRequirement, ProfessionSelectionContentProps (+42 more)

### Community 303 - "safe_run_static"
Cohesion: 0.07
Nodes (41): get_project_root(), Determine the project root based on current working directory, main(), Run a psql command and return the result., Load all seed data files., run_psql_command(), Read process output in background thread., read_output() (+33 more)

### Community 304 - "test_admin_summon_command.py"
Cohesion: 0.07
Nodes (48): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any, Persist item instance to DB. Logs and continues on failure (room drop still… (+40 more)

### Community 305 - "test_inventory_display_helpers.py"
Cohesion: 0.07
Nodes (48): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+40 more)

### Community 306 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 307 - "PlayerRepositoryProtocol"
Cohesion: 0.07
Nodes (31): PlayerRepositoryProtocol, datetime, Player, Protocol, Room, UUID, Repository protocols for MythosMUD persistence layer. Explicit typing.Protocol…, List all cached rooms. (+23 more)

### Community 308 - "AdminActionsLogger"
Cohesion: 0.08
Nodes (37): AdminActionsLogger, Any, datetime, Path, TypedDict, Log a general admin command action., Log permission check attempts. Args: player_name: Name of the player attempting…, Optional fields for teleport action logging. (+29 more)

### Community 309 - "debrief_command.py"
Cohesion: 0.08
Nodes (48): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+40 more)

### Community 310 - "test_nats_messages.py"
Cohesion: 0.07
Nodes (46): BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, Pydantic schemas for NATS message validation. This module provides type-safe…, Validate a chat message against the schema. Args: data: Message data dictionary…, Validate an event message against the schema. Args: data: Message data… (+38 more)

### Community 311 - "RoomMapEditorRuntime.tsx"
Cohesion: 0.07
Nodes (29): UseRoomMapDataOptions, MapEditToolbar(), MapEditToolbarProps, buildModalCreateEdgeHandler(), buildModalPreviewHandler(), buildModalUpdateEdgeHandler(), buildModalUpdateRoomHandler(), buildPreviewEdge() (+21 more)

### Community 312 - "CoordinateGenerator"
Cohesion: 0.06
Nodes (27): Select, CoordinateGenerator, Any, AsyncSession, Coordinate generation service for ASCII maps. This module provides hierarchical…, Load rooms and their exits from database. Args: plane: Plane name zone: Zone…, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits. (+19 more)

### Community 313 - "SpellLearningService"
Cohesion: 0.10
Nodes (29): Any, UUID, Spell learning service for handling spell acquisition. This module provides…, Learn a spell for a player., Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…, Service for handling spell learning from various sources. Manages spell…, Learn a spell from a spellbook item. Args: player_id: Player ID…, # TODO: Integrate with item system to get spellbook data # pylint:… (+21 more)

### Community 314 - "test_command_utility.py"
Cohesion: 0.07
Nodes (34): HelpCommand, field_validator, Command for getting help on commands., Validate help topic format using centralized validation., Command for listing online players., Validate filter name format using centralized validation., WhoCommand, Unit tests for utility command models. Tests the utility command models and… (+26 more)

### Community 315 - "DialogueEditorPage.tsx"
Cohesion: 0.16
Nodes (18): baseUrl(), buildHeaders(), deleteDialogueDefinition(), DialogueDefinitionDto, DialogueNodeDto, DialogueOptionDto, DialogueTreeDto, listDialogueDefinitions() (+10 more)

### Community 316 - "useMythosAppState.ts"
Cohesion: 0.15
Nodes (20): AppActions, AppState, buildActionViewModel(), buildMythosAppViewModel(), buildStateViewModel(), hoisted, useMythosApp(), AuthSlice (+12 more)

### Community 317 - "RoomDataValidator"
Cohesion: 0.13
Nodes (22): Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validates room data structure and content., Validate room data structure and content. Args: room_data: Room data to…, Validate that all required fields are present. Args: room_data: Room data to…, Validate field types. Args: room_data: Room data to validate Returns:…, RoomDataValidator, Unit tests for room_data_validator. Tests the RoomDataValidator class methods. (+14 more)

### Community 318 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 319 - "endpoints.py"
Cohesion: 0.02
Nodes (178): CharacterInfo, get_container, IntegrityError, _authenticate_user_credentials(), _check_shutdown_status(), _check_username_exists(), _create_user_object(), _ensure_user_email() (+170 more)

### Community 320 - "ConnectionCleaner"
Cohesion: 0.15
Nodes (13): ConnectionCleaner, Any, Return connection IDs that exceed max_connection_age., Extract player_id from connection metadata if present., Close stale WebSocket and remove from tracking. Handles None websocket…, Clean up orphaned data that might accumulate over time. Args:…, Return set of online player IDs as strings (room._players uses string UUIDs)., Return players in room but not online. Empty if room has no get_players. (+5 more)

### Community 321 - "test_pattern_matcher.py"
Cohesion: 0.06
Nodes (36): pattern_matcher(), fixture, Unit tests for NATS Pattern Matcher. Tests the PatternMatcher class., Test _components_match_pattern() matches exact components., Test _components_match_pattern() matches placeholder components., Test _components_match_pattern() returns False for mismatch., Test _components_match_pattern() validates placeholder values., Test _components_match_pattern() disallows underscores in strict mode. (+28 more)

### Community 322 - "test_player_event_handlers_respawn.py"
Cohesion: 0.02
Nodes (103): _append_unique_valid_occupant(), _ensure_respawned_player_in_lists(), _is_npc_occupant_row(), _occupant_str_field(), PlayerRespawnEventHandler, BoundLogger, ConnectionManager, Player (+95 more)

### Community 323 - "test_player_occupant_processor.py"
Cohesion: 0.05
Nodes (47): mock_connection_manager(), mock_name_extractor(), processor(), asyncio, fixture, Unit tests for player occupant processor. Tests the PlayerOccupantProcessor…, Test _convert_player_ids_to_uuids handles mixed string and UUID types., Test _convert_player_ids_to_uuids handles UUID objects. (+39 more)

### Community 324 - "verify_enhanced_logging_compliance.py"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 325 - "projectorRoom.ts"
Cohesion: 0.09
Nodes (45): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), ProjectorHandler, stateHandlers, appendMessage(), appendMovementMessage() (+37 more)

### Community 326 - "apiTypeGuards.ts"
Cohesion: 0.11
Nodes (45): ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertServerCharacterResponseArray(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString() (+37 more)

### Community 327 - "mythos_mud_mapbuilder.py"
Cohesion: 0.10
Nodes (46): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+38 more)

### Community 328 - "PrototypeRegistryError"
Cohesion: 0.09
Nodes (29): ItemInstance, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError, Any, Exception, PrototypeRegistry, Item factory for creating item instances from prototypes. This module provides… (+21 more)

### Community 329 - "compare_linting_results.py"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 330 - ".__post_init__"
Cohesion: 0.04
Nodes (37): Event subscription setup for application startup. Extracted from…, Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), subscribe_room_occupants_refresh(), QuestCompleted, Initialize the event with proper type., Initialize the event with proper type. (+29 more)

### Community 331 - "PeriodicOrphanAuditor"
Cohesion: 0.08
Nodes (37): create_lifespan_memory_service(), PeriodicOrphanAuditor, Core capability for granular investigation cycles. Repeated universal analysis…, Stop the periodic orphan auditor background enforcement., Create a centralized memory operations coordinator instance targeted for…, Periodic background auditor that investigates orphanage patterns and memory…, Start the background auditing scheduler responsible for identifying orphan…, Primary background cycle consuming auditor implementation. Executes periodic… (+29 more)

### Community 332 - "test_goto_helpers.py"
Cohesion: 0.12
Nodes (43): execute_confirm_goto(), execute_goto_teleport(), log_goto_failure(), Any, Exception, Helper functions for goto command operations., Log failed goto action., Validate app context and get current player with admin permissions. Returns… (+35 more)

### Community 333 - "_str_id"
Cohesion: 0.11
Nodes (19): Any, ConnectionManager, UUID, Create a new party with the given player as leader. Returns dict with success…, Disband a party. If by_player_id is given, only the leader may disband. If…, Add a player to a party. Fails if party does not exist or player is already in…, Safely schedule an async notification, handling cases where no event loop is…, Notify a player they have been removed from a party. Resolves leader name. (+11 more)

### Community 334 - "Stats"
Cohesion: 0.12
Nodes (13): Any, Stats, Roll Size using formula: (2D6+6)*5 (range 40-90)., Roll stats using 3d6 method (scaled to 15-90 range)., Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)., Generate stats using a point-buy system (balanced, scaled to 1-100 range)., Check if stats meet the prerequisites for a given class. Args: stats: The…, Get a list of classes that the character qualifies for. Args: stats: The… (+5 more)

### Community 335 - "collect_inventory.py"
Cohesion: 0.08
Nodes (43): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+35 more)

### Community 336 - "test_shopkeeper_npc.py"
Cohesion: 0.06
Nodes (35): Buy item from player., Calculate final price with markup., Handle greeting customer action., Handle restocking inventory action., Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., Shopkeeper NPC type with buy/sell functionality., Initialize shopkeeper NPC., Setup shopkeeper-specific behavior rules. (+27 more)

### Community 337 - "StatisticsAggregator"
Cohesion: 0.04
Nodes (51): MemoryStatsSnapshot, TypedDict, UUID, Assemble memory stats from a snapshot dict (keeps call sites param-stable)., Count active connections not tied to any online player., Build the connections subsection of memory stats., Build the sessions subsection of memory stats., Expose memory monitor configuration knobs for stats payload. (+43 more)

### Community 338 - "websocket_handler_commands.py"
Cohesion: 0.08
Nodes (50): connection_manager_from_running_app(), _MainModule, Protocol, Read the running FastAPI app without a static import of server.main. A static…, Return app.state.container.connection_manager, or None if unavailable., _attach_room_state_to_result(), _broadcast_command_room_if_needed(), handle_game_command() (+42 more)

### Community 339 - "test_memory_leak_metrics.py"
Cohesion: 0.05
Nodes (42): collector(), fixture, Unit tests for memory leak metrics collector. Tests the…, Test collection of cache metrics., Test collection of task metrics., Test collection of NATS metrics., Create a MemoryLeakMetricsCollector instance., Test collection of all metrics. (+34 more)

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

### Community 345 - "api/player_respawn.py"
Cohesion: 0.14
Nodes (28): Any, post, Request, Player respawn API endpoints. This module handles endpoints for respawning…, Respawn a delirious player at the Sanitarium with restored lucidity. This…, Respawn a dead player at their respawn location with full DP. This endpoint…, Execute a respawn service call inside a DB session with shared error handling., respawn_player() (+20 more)

### Community 346 - "test_connection_statistics.py"
Cohesion: 0.06
Nodes (48): Get session management statistics., Get presence tracking statistics., get_online_player_by_display_name_impl(), get_player_presence_info_impl(), get_presence_statistics_impl(), get_session_stats_impl(), Any, Get online player information by display name. (+40 more)

### Community 347 - "test_websocket_handler_coverage_gaps.py"
Cohesion: 0.03
Nodes (92): _mirror_service_to_app_state(), WebSocket app.state / container service wiring for command processing.…, Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state. Mutates…, resolve_and_setup_app_state_services(), _services_from_container(), handle_chat_message() (+84 more)

### Community 348 - "HolidayCollection"
Cohesion: 0.04
Nodes (79): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+71 more)

### Community 349 - "ChatLogger"
Cohesion: 0.03
Nodes (59): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+51 more)

### Community 350 - "test_calendar.py"
Cohesion: 0.12
Nodes (23): HolidayModel, NPCScheduleModel, Base, Mythos holidays tracker., Unit tests for calendar models. Tests the HolidayModel and NPCScheduleModel…, Test NPCScheduleModel can have optional notes., Test NPCScheduleModel has correct table name., Test NPCScheduleModel __repr__ method. (+15 more)

### Community 351 - "AsciiMapViewer.tsx"
Cohesion: 0.08
Nodes (29): AsciiMapEditorProps, AsciiMapViewer(), AsciiMapViewerProps, chooseMapView(), getMapClickHandler(), useAsciiMapViewerBindings(), createViewportKeyHandler(), VIEWPORT_BUTTON_CLASS (+21 more)

### Community 352 - "revised-character-creation.spec.ts"
Cohesion: 0.08
Nodes (26): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+18 more)

### Community 353 - "test_message_formatters.py"
Cohesion: 0.08
Nodes (23): Unit tests for message formatters. Tests the message_formatters module…, Test format_message_content() formats 'say' channel messages., Test format_message_content() formats 'local' channel messages., Test format_message_content() formats 'global' channel messages., Test format_message_content() formats 'emote' channel messages., Test format_message_content() formats 'pose' channel messages., Test format_message_content() formats 'whisper' channel messages (default)., Test format_message_content() formats 'whisper' for recipient as 'X whispers to… (+15 more)

### Community 354 - "CombatCommandHandler"
Cohesion: 0.05
Nodes (29): CombatCommandHandler, AppWithState, ConnectionManager, Combat service for command modules., Movement service for command modules., Player position service for command modules., Extract command type and target name from command_data. Public API., Validate that target name is provided. Public API. (+21 more)

### Community 355 - "PlayerDeathService"
Cohesion: 0.08
Nodes (29): Initialize combat services., PlayerDeathService, Any, AsyncSession, Player, UUID, Process DP decay for a single mortally wounded player. Decreases player DP by…, Ensure player posture is set to lying when dead. Args: player: Player object to… (+21 more)

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
Cohesion: 0.18
Nodes (20): _definition_dict(), DialogueDefinitionRepository, Coerce JSONB definition cell to a plain string-keyed dict., Repository for dialogue_definitions via stored procedures., _mock_session_with_rows(), asyncio, fixture, Unit tests for DialogueDefinitionRepository. (+12 more)

### Community 365 - "test_connection_cleaner.py"
Cohesion: 0.08
Nodes (30): connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue(), mock_rate_limiter(), mock_room_manager() (+22 more)

### Community 366 - "TestHierarchicalSchema"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 367 - "LucidityFluxService"
Cohesion: 0.13
Nodes (13): LucidityFluxService, PlayerFluxCtx, AsyncSession, Player, Build room cache for all players., Process a single player's passive flux., Evaluate passive LCD flux for the current tick., Snapshot of scheduler state for ops and tests. (+5 more)

### Community 368 - "_track_player_presence"
Cohesion: 0.11
Nodes (23): Get player and setup room subscription. Args: player_id: The player's ID…, Track player presence and broadcast connection message. Args: player_id: The…, _setup_player_and_room(), _track_player_presence(), asyncio, Test _cleanup_dead_connections() handles empty list., Test _setup_player_and_room() successfully sets up player and room., Test _setup_player_and_room() returns False when player not found. (+15 more)

### Community 369 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, properties, field1, field2, field3, sub_zone (+3 more)

### Community 370 - "properties"
Cohesion: 0.17
Nodes (12): description, description, description, description, maxLength, minLength, type, properties (+4 more)

### Community 371 - "properties"
Cohesion: 0.13
Nodes (15): description, description, description, description, type, description, maxLength, minLength (+7 more)

### Community 372 - "_parse_stat_datetime"
Cohesion: 0.09
Nodes (22): _parse_stat_datetime(), Parse datetime value from various formats and return formatted string., Test _parse_stat_datetime() handles datetime object., Test _parse_stat_datetime() handles timestamp., Test _parse_stat_datetime() handles ISO string., Test _parse_stat_datetime() returns 'Unknown' for None., Test _parse_stat_datetime() returns string representation for invalid input., test_parse_stat_datetime_from_datetime() (+14 more)

### Community 373 - "TrackedTaskManager"
Cohesion: 0.12
Nodes (21): patch_asyncio_create_task_with_tracking(), Audit and reclaim orphaned task candidates across the system. Returns: Number…, Proactively clean up orphaned tasks by cancelling leak prevention violations.…, Return count of currently tracked task references within the manager's…, Attach a TaskRegistry instance to this Tracker for shared coordination. Args:…, Central namespace for tracked task lifecycle coordination preventing orphaned…, Replace asyncio.create_task with a tracked alternative throughout the…, Initialize the TrackedTaskManager. Args: task_registry: Optional TaskRegistry… (+13 more)

### Community 374 - "test_admin_teleport_commands.py"
Cohesion: 0.16
Nodes (42): handle_confirm_goto_command(), handle_confirm_teleport_command(), handle_goto_command(), handle_teleport_command(), Any, Handle the goto command for teleporting the admin to a player's location. Args:…, Handle the confirm teleport command for executing the actual teleportation.…, Handle the confirm goto command for executing the actual teleportation. Args:… (+34 more)

### Community 375 - "test_status_commands_helpers.py"
Cohesion: 0.10
Nodes (21): _add_additional_stats_lines(), Add additional stats lines to status lines if they have non-zero values. Args:…, Unit tests for status_commands helper functions. Tests helper functions in…, Test _add_additional_stats_lines() ignores zero values., Test _build_base_status_lines() builds status lines., Test _build_base_status_lines() shows combat status., Test _build_base_status_lines() formats position correctly., Test _add_additional_stats_lines() adds additional stats. (+13 more)

### Community 376 - "SpellMaterialsService"
Cohesion: 0.16
Nodes (11): Any, UUID, Spell material handling service. This module handles checking and consuming…, Build final inventory with consumed materials removed. Args: inventory:…, Consume spell materials from player inventory. Args: player_id: Player ID…, Service for handling spell material requirements. Handles checking if players…, Initialize the spell materials service. Args: player_service: Player service…, Check if player has all required materials. Args: player_id: Player ID spell:… (+3 more)

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
Cohesion: 0.20
Nodes (10): description, description, description, description, type, properties, field1, field2 (+2 more)

### Community 382 - "Any"
Cohesion: 0.10
Nodes (11): Any, Initialize the room cache service. Args: persistence: Persistence layer instance, Get room data with caching. Args: room_id: The room ID Returns: Room data…, Get room data with caching (synchronous version). Args: room_id: The room ID…, Initialize the NPC cache service. Args: npc_service: NPC service instance, Get NPC definitions with caching. Args: session: Database session Returns: List…, Get a specific NPC definition with caching. Args: session: Database session…, Get NPC spawn rules with caching. Args: session: Database session Returns: List… (+3 more)

### Community 383 - "ErrorContext"
Cohesion: 0.16
Nodes (9): Initialize the Pydantic error handler. Args: context: Optional error context…, ErrorContext, Any, Initialize MythosMUD error. Args: message: Technical error message context:…, Log validation errors at warning so expected user-input errors do not flood…, Contextual information for error handling. Provides structured context for…, Initialize LoggedHTTPException. Args: status_code: HTTP status code detail:…, Convert context to dictionary for logging. (+1 more)

### Community 384 - "nats_broker.py"
Cohesion: 0.14
Nodes (16): MessageBrokerConnectionError, MessageBrokerError, Exception, Message Broker abstraction for MythosMUD. This module defines the MessageBroker…, Base exception for message broker errors., Exception raised when connection to message broker fails., Exception raised when subscribing to subject fails., Exception raised when unsubscribing from subject fails. (+8 more)

### Community 385 - "test_users_current_user_logging.py"
Cohesion: 0.17
Nodes (19): DependsParam, get_current_user_with_logging(), Enhanced get_current_user with detailed logging., asyncio, Unit tests for get_current_user_with_logging wrapper., Test _get_current_user_with_logging when HTTPException is raised., Test _get_current_user_with_logging with successful authentication., Test _get_current_user_with_logging when generic Exception is raised. (+11 more)

### Community 386 - "get_async_session"
Cohesion: 0.07
Nodes (47): add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting() (+39 more)

### Community 387 - "quest_commands.py"
Cohesion: 0.03
Nodes (109): ExitStack, _active_npc_ids_in_room(), _emit_npc_lines_for_results(), _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence() (+101 more)

### Community 388 - "CORSConfig"
Cohesion: 0.08
Nodes (29): CORSConfig, Any, BaseSettings, field_validator, model_validator, Parse comma-separated string into cleaned list., Parse comma separated strings or lists into a cleaned list of strings., Parse allowed origins from various input formats. (+21 more)

### Community 389 - "resolve_weapon_attack_from_equipped"
Cohesion: 0.08
Nodes (39): _prototype_from_equipped_stack(), NamedTuple, PrototypeRegistry, Weapon resolution helpers for combat. Resolves equipped main-hand items to…, Result of resolving an equipped item to a weapon attack. base_damage: Rolled…, Resolve equipped main-hand stack to weapon attack info, or None if unarmed., resolve_weapon_attack_from_equipped(), _roll_weapon_attack() (+31 more)

### Community 390 - "test_rate_limiter_utils.py"
Cohesion: 0.05
Nodes (41): Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…, Test get_rate_limit_info returns correct info with requests., Test get_rate_limit_info calculates reset time correctly., Test get_rate_limit_info calculates retry_after correctly., Test get_rate_limit_info filters out old requests., Test enforce_rate_limit allows request within limit., Test enforce_rate_limit raises RateLimitError when limit exceeded., Test enforce_rate_limit includes retry_after in error. (+33 more)

### Community 391 - "test_room_utils.py"
Cohesion: 0.07
Nodes (42): Unit tests for room_utils. Tests utility functions for room operations., Test get_subzone_local_channel_subject() generates subject., Test get_subzone_local_channel_subject() returns None for invalid room ID., Test extract_subzone_from_room_id() extracts subzone., Test extract_subzone_from_room_id() extracts different subzone., Test extract_subzone_from_room_id() returns None for invalid format., Test get_zone_from_room_id() extracts zone., Test get_zone_from_room_id() extracts different zone. (+34 more)

### Community 392 - "log_with_context"
Cohesion: 0.06
Nodes (36): correct_request_context(), Demonstrate correct request context binding., add_request_context(), process_websocket_message(), websocket, WebSocket endpoint with enhanced logging., Add request context to all log entries using enhanced logging., Simulate WebSocket message processing. (+28 more)

### Community 393 - "maps.ts"
Cohesion: 0.09
Nodes (32): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+24 more)

### Community 394 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 395 - "correct_patterns.py"
Cohesion: 0.05
Nodes (35): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+27 more)

### Community 396 - "look_command.py"
Cohesion: 0.06
Nodes (76): _app_from_request(), _as_response(), _connection_manager_from_app(), _container_from_app(), _get_app_and_persistence(), _get_room_drops(), _handle_implicit_target_lookup(), handle_look_command() (+68 more)

### Community 397 - "test_game_tick_processing_async.py"
Cohesion: 0.07
Nodes (39): mock_app(), mock_container(), mock_player(), asyncio, fixture, Unit tests for game tick processing async functions. Tests the async game tick…, Test _process_single_effect() with damage_over_time effect., Test _process_single_effect() with heal_over_time effect. (+31 more)

### Community 398 - "inventory_pickup_command.py"
Cohesion: 0.05
Nodes (82): _DropResolved, _FloorPickupResolved, Parse numeric fields from object-typed JSON command payloads., Protocol, Shared types for inventory command handlers (Lizard: keep main module small)., Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, add_pickup_to_inventory() (+74 more)

### Community 399 - "player_connection_setup.py"
Cohesion: 0.11
Nodes (38): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions. This module handles the setup tasks when a…, Broadcast a structured entry event to other occupants (excluding the newcomer).… (+30 more)

### Community 400 - "HolidayService"
Cohesion: 0.03
Nodes (59): _ensure_utc(), _holiday_entry_from_row(), _HolidayLoadResult, HolidayService, datetime, Path, Record, TypedDict (+51 more)

### Community 401 - "lucidity_trigger_handlers.py"
Cohesion: 0.09
Nodes (38): CatatoniaObserverProtocol, datetime, Protocol, UUID, Handle a player returning from catatonia., Handle a player requiring sanitarium failover., Return False to suppress failover (debounce); True allows failover handling., Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE. (+30 more)

### Community 402 - "test_subscription_patterns.py"
Cohesion: 0.11
Nodes (26): get_chat_subscription_patterns(), get_event_subscription_patterns(), get_subscription_pattern(), Any, Convert a pattern template into a subscription pattern with wildcards. Args:…, Get all chat-related subscription patterns. Args: patterns: Dictionary of…, Get all event-related subscription patterns. Args: patterns: Dictionary of…, Unit tests for NATS Subscription Patterns. Tests the subscription pattern… (+18 more)

### Community 403 - "_format_npc_description"
Cohesion: 0.10
Nodes (20): _format_npc_description(), Format NPC description with fallback., Test _format_npc_description() returns description from definition., Test _format_npc_description() uses fallback when description is empty., Test _format_npc_description() uses alternative attributes., test_format_npc_description(), test_format_npc_description_fallback(), test_format_npc_description_no_description() (+12 more)

### Community 404 - "test_message_broadcaster.py"
Cohesion: 0.08
Nodes (34): asyncio, Unit tests for message broadcaster. Tests the MessageBroadcaster class., Test broadcast_global() excludes specified player., Test broadcast_global() when no players online., Test broadcast_room_event() broadcasts room event., Test broadcast_to_room() records invalid subscriber IDs., Test broadcast_to_room() falls back when batch gather fails., Test broadcast_global() falls back when batch gather fails. (+26 more)

### Community 405 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 406 - "GameClientV2ContainerView.tsx"
Cohesion: 0.08
Nodes (21): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, maxWidthClasses, ModalContainer() (+13 more)

### Community 407 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 408 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 409 - "test_quality_fragmentation_guard.py"
Cohesion: 0.10
Nodes (39): _build_python_call_usage_map(), _call_target_name(), Call, ChangedFile, Build a repo-wide call usage map from Python AST call sites., scan_changed_files(), _ChangedFile, _load_guard_module() (+31 more)

### Community 410 - "parse_last_active_datetime"
Cohesion: 0.10
Nodes (20): parse_last_active_datetime(), Parse last_active from string or datetime object to timezone-aware datetime.…, Test parse_last_active_datetime with None., Test parse_last_active_datetime with empty string., Test parse_last_active_datetime with string ending in Z., Test parse_last_active_datetime with string containing timezone., Test parse_last_active_datetime with string without timezone., Test parse_last_active_datetime with naive datetime. (+12 more)

### Community 411 - "test_profession_repository.py"
Cohesion: 0.17
Nodes (19): _bool_or_default(), Any, Return value as str or a default if falsy., Return text value or default if falsy., Return bool(value) when not None, otherwise default., _str_or_default(), _text_or_default(), _mock_session() (+11 more)

### Community 412 - "RoomCacheService"
Cohesion: 0.15
Nodes (7): Service for caching room data., Invalidate cached room data. Args: room_id: The room ID to invalidate, Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload, RoomCacheService, Any, _RoomObj, TestRoomCacheService

### Community 413 - "equipment_helpers.py"
Cohesion: 0.05
Nodes (62): _equip_stack_from_inventory_index(), _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), handle_wearable_container_on_unequip(), InventoryStack, Player, Equipment-related helper functions for inventory commands. (+54 more)

### Community 414 - "test_skills.py"
Cohesion: 0.13
Nodes (18): PlayerSkillEntry, PlayerSkillsResponse, BaseModel, Skill catalog API response schemas. Used by GET /v1/skills (or equivalent) for…, Response model for skills catalog list., Single player skill (character creation revamp 4.3)., Response for GET /v1/api/players/{player_id}/skills., SkillListResponse (+10 more)

### Community 415 - "._cleanup_player_mutes"
Cohesion: 0.12
Nodes (11): datetime, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired player mutes., Clean up expired channel mutes., Clean up expired global mutes., Clean up expired mutes from all storage. (+3 more)

### Community 416 - "pytest.md"
Cohesion: 0.03
Nodes (116): Base, QuestDefinition, QuestInstance, QuestOffer, Quest subsystem models: quest_definitions, quest_instances, quest_offers. Maps…, Quest template: id (PK), definition JSONB, timestamps., Per-character quest state: one row per player per quest., Junction: links a quest to an NPC or room that offers it. (+108 more)

### Community 417 - "disconnect_grace_period.py"
Cohesion: 0.09
Nodes (34): cancel_grace_period(), Any, UUID, Disconnect grace period management for MythosMUD. This module handles the…, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, Start a grace period for a disconnected player. During the grace period, the…, start_grace_period(), mock_manager() (+26 more)

### Community 418 - "TestCombatMessagingService"
Cohesion: 0.05
Nodes (34): CombatMessages, CombatMessagingService, Any, Generate combat start messages for all room occupants. Args: attacker_name:…, Generate combat end messages for all room occupants. Args: winner_name: Name of…, Generate thematic error messages for combat actions. Args: error_type: Type of…, Validate NPC message templates against the schema. Args: messages_data: NPC…, Service for generating combat messages. This service creates thematic,… (+26 more)

### Community 419 - "WebSocketRateLimiter"
Cohesion: 0.40
Nodes (3): WebSocket rate limiter with enhanced logging., Check if client is within rate limit with enhanced logging., WebSocketRateLimiter

### Community 420 - "look_npc.py"
Cohesion: 0.19
Nodes (18): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result(), Any (+10 more)

### Community 421 - "test_magic_service.py"
Cohesion: 0.15
Nodes (38): CastingState, Represents an active spell casting state., MagicService, Public API: composition of completion, healing, and core spellcasting logic., _build_magic_service(), mock_player(), player_id(), Any (+30 more)

### Community 422 - "field_validator"
Cohesion: 0.11
Nodes (10): field_validator, Validate target player name format using centralized validation., Validate message content for security using centralized validation., Validate message content for security using centralized validation., Validate message content for security using centralized validation., Validate message content for security using centralized validation., Validate system message content for security using centralized validation., Validate emote action for security using centralized validation. (+2 more)

### Community 423 - "test_flee_command.py"
Cohesion: 0.09
Nodes (38): flee_handler_deps(), _FleeCmdApp, _FleeCmdAppState, _FleeCmdRequest, FleeHandlerDeps, _GetCombatHandlerLoaderApp, _GetCombatHandlerLoaderAppState, _GetCombatHandlerLoaderContainer (+30 more)

### Community 424 - "test_player_service.py"
Cohesion: 0.06
Nodes (45): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service CRUD and lookup. Delete, location, mythos status,…, Test get_player_by_id() when player is not found., Test get_player_by_name() when player is found., Test get_player_by_name() when player is not found. (+37 more)

### Community 425 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 426 - "test_command_parser_helpers.py"
Cohesion: 0.05
Nodes (40): command_parser(), fixture, Unit tests for command_parser helper methods. Tests the helper methods in…, Test _create_command_object() handles 'l' alias., Test _create_command_object() handles 'g' alias., Test _create_command_object() handles 'w' alias., Test _create_command_object() raises error for unsupported command., Test _create_command_object() handles PydanticValidationError. (+32 more)

### Community 427 - "useRoomEditModal.ts"
Cohesion: 0.07
Nodes (16): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, fieldBorderClass(), RoomEditDescriptionField(), RoomEditFormData, RoomEditModalForm() (+8 more)

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

### Community 432 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test filter_online_players with all players online., Test filter_online_players with some players offline., Test filter_online_players with players without last_active., Test handle_who_command when persistence is not available., Test handle_who_command when no players are found., Test handle_who_command successful execution., Test handle_who_command with filter term. (+11 more)

### Community 433 - "MessageBroadcaster"
Cohesion: 0.10
Nodes (22): Messaging components for connection management. This package provides modular…, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Message broadcasting for connection management. This module provides room and…, Convert string player IDs to UUIDs for message sending. Args: target_list: List…, Process results from batch message delivery. Args: delivery_results: Results… (+14 more)

### Community 434 - "combat_loader.py"
Cohesion: 0.13
Nodes (35): CombatCommandHandlerExtras, Optional services from the app container (keeps…, _app_from_request(), get_combat_command_handler(), handle_attack_command(), handle_flee_command(), handle_kick_command(), handle_punch_command() (+27 more)

### Community 435 - "test_logout_commands_helpers.py"
Cohesion: 0.09
Nodes (25): _get_player_position_from_connection_manager(), Get player's current position from connection manager. Args:…, Unit tests for logout_commands helper functions. Tests helper functions in…, Test _sync_player_position() does nothing when position is None., Test _sync_player_position() does nothing when position matches., Test _get_player_position_from_connection_manager() returns position., Test _get_player_position_from_connection_manager() finds by display name., Test _get_player_position_from_connection_manager() returns None when no… (+17 more)

### Community 436 - "spell_effects_support.py"
Cohesion: 0.11
Nodes (34): apply_stat_modifications(), Stat modification helpers for spell effects. This module contains utility…, Apply stat modification dict to stats. Returns (updated stats, stat_changes,…, _apply_stat_modify_to_player(), _build_stat_modifications(), _create_object_for_player(), _create_object_for_room(), process_create_object_effect() (+26 more)

### Community 437 - "_parse_npc_stats_dict"
Cohesion: 0.11
Nodes (18): _parse_npc_stats_dict(), Parse NPC stats dictionary, handling both dict and JSON string formats., Test _parse_npc_stats_dict() handles dict input., Test _parse_npc_stats_dict() parses JSON string., Test _parse_npc_stats_dict() returns empty dict for invalid JSON., Test _parse_npc_stats_dict() returns empty dict for other types., test_parse_npc_stats_dict_from_dict(), test_parse_npc_stats_dict_from_json_string() (+10 more)

### Community 438 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 439 - "AttributeError"
Cohesion: 0.06
Nodes (47): AttributeError, Test create_access_token handles AttributeError., test_create_access_token_attribute_error(), Test _extract_parsed_fields handles missing attributes gracefully., test_extract_parsed_fields_handles_missing_attributes(), Test _create_player_occupant_info handles grace period check exceptions., test_create_player_occupant_info_grace_period_exception(), mock_combat_service() (+39 more)

### Community 440 - "CombatCommandFactory"
Cohesion: 0.08
Nodes (31): Unit tests for combat command factories. Tests the CombatCommandFactory class…, Test create_attack_command() creates AttackCommand., Test create_attack_command() allows None target (validation happens later)., Test create_punch_command() creates PunchCommand., Test create_punch_command() allows None target (validation happens later)., Test create_kick_command() creates KickCommand., Test create_kick_command() allows None target (validation happens later)., Test create_strike_command() creates StrikeCommand. (+23 more)

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
Cohesion: 0.04
Nodes (44): ChatModeration, normalize_player_id(), PlayerServiceProtocol, Any, datetime, Protocol, UUID, Chat moderation utilities. This module provides moderation functionality… (+36 more)

### Community 447 - "EmoteService"
Cohesion: 0.08
Nodes (28): EmoteDefinition, EmoteService, TypedDict, Check if a command is an emote alias. Args: command: The command to check…, Get the emote definition for a command. Args: command: The command (emote name…, Format emote messages for the player and room occupants. Args: command: The…, Get a list of all available emotes and their aliases. Returns: Dict mapping…, Reload predefined emote definitions from the database. (+20 more)

### Community 448 - "test_auth_rate_limit.py"
Cohesion: 0.16
Nodes (22): _auth_bucket(), auth_client_key(), auth_rate_limit_response(), is_auth_rate_limited_path(), Request, Return 429 when an auth POST exceeds the limiter; otherwise None., Return True if path is an unauthenticated auth POST covered by the limiter., Key the limiter by client IP. Default uses the TCP peer (request.client.host).… (+14 more)

### Community 449 - "test_container_persistence_extended_crud.py"
Cohesion: 0.04
Nodes (52): ContainerCreateParams, Optional fields for creating a container row (beyond source_type)., create_container(), Persist a new container row, optionally seed contents, return hydrated data or…, Unit tests for container persistence: CRUD, queries, and UUID conversion paths.…, Test get_container returns None when container not found., Test get_container handles database errors., Test get_containers_by_room_id successfully retrieves containers. (+44 more)

### Community 450 - "PayloadOptimizer"
Cohesion: 0.12
Nodes (24): get_payload_optimizer(), PayloadOptimizer, Payload optimization for WebSocket messages. This module provides utilities for…, Optimizes payloads for WebSocket transmission. Features: - Size limit…, Get the global payload optimizer instance., Initialize the payload optimizer. Args: max_payload_size: Maximum payload size…, _CompareExplodes, optimizer() (+16 more)

### Community 451 - "LoggedException"
Cohesion: 0.11
Nodes (17): LoggedException, Marker base class indicating an exception has already produced a log entry., Return True if this exception instance has already been logged., Test LoggedException can be instantiated., Test LoggedException.mark_logged() marks as logged., Test LoggedException can be created with already_logged=True., test_logged_exception(), test_logged_exception_already_logged() (+9 more)

### Community 452 - ".load_room_data"
Cohesion: 0.06
Nodes (19): Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path., Validate or update room ID based on filename and location., Validate required fields are present., Add location fields if missing. (+11 more)

### Community 453 - "CharacterNameScreen.tsx"
Cohesion: 0.11
Nodes (30): buildCreateCharacterPayload(), CharacterNameScreen(), getCreateCharacterErrorMessage(), OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, loadSkillsCatalog(), MIN_TOUCH_TARGET_STYLE (+22 more)

### Community 454 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 455 - "Async Persistence Migration Tracker"
Cohesion: 0.07
Nodes (33): PassiveLucidityFluxService, 17-Second Game Tick Delay, Three-Phase Async Remediation, Room Cache TTL (60s), Async Persistence Migration Tracker, Current Status, Decision Tree, Files Requiring Migration (+25 more)

### Community 456 - "PostgreSQL & SQL Audit Report"
Cohesion: 0.06
Nodes (36): 10. Prioritized Fixes, 11. Summary Table, 1.1. Snake_case (GOOD), 1.2. Quoted Identifier, 1. Naming Conventions, 2.1. Uppercase SQL Keywords, 2. SQL Formatting (Keywords Lowercase), 3.1. Explicit Joins (GOOD) (+28 more)

### Community 457 - "LRUCache"
Cohesion: 0.08
Nodes (20): K, LRUCache, Put an item into the cache. Args: key: The key to store value: The value to…, Delete an item from the cache. Args: key: The key to delete Returns: True if…, Clear all items from the cache., Get the current number of items in the cache., Check if the cache is at maximum capacity., Get cache statistics. Returns: Dictionary containing cache statistics (+12 more)

### Community 458 - "GameMechanicsService"
Cohesion: 0.11
Nodes (24): GameMechanicsService, Heal a player's health., Damage a player's health., Award experience points to a player. CRITICAL FIX: This method prevents XP…, Service class for game mechanics operations., Initialize the game mechanics service with a persistence layer., Apply lucidity loss to a player., Apply fear to a player. (+16 more)

### Community 459 - "test_container_persistence_extended_row_helpers.py"
Cohesion: 0.08
Nodes (60): parse_jsonb_column(), Parse a JSONB column value from database. JSONB columns may be returned as: -…, _after_container_insert(), _allowed_roles_from_row(), _as_opt_datetime(), _as_opt_str(), _as_opt_uuid(), _as_uuid() (+52 more)

### Community 460 - "test_container_persistence_sql_injection.py"
Cohesion: 0.17
Nodes (10): _create_mock_container_row(), UUID, Tests for SQL injection protection in container persistence operations. These…, Test that update_container uses parameterized queries, not string concatenation., Test that column names are hardcoded, not from user input., Create a complete mock container row with all required columns., Test SQL injection protection in container persistence., Test that SQL injection in lock_state is prevented. (+2 more)

### Community 461 - "TestNPCCombatRewards"
Cohesion: 0.08
Nodes (20): asyncio, fixture, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class., Test award_xp_to_killer handles zero XP. (+12 more)

### Community 462 - "test_metadata.py"
Cohesion: 0.11
Nodes (15): Shared SQLAlchemy metadata for MythosMUD models. This module provides the…, NPC Database metadata for MythosMUD. This module defines the SQLAlchemy…, Unit tests for metadata modules. Tests the shared SQLAlchemy metadata instances., Test that metadata is a MetaData instance., Test that npc_metadata is a MetaData instance., Test that metadata and npc_metadata are separate instances., Test that Base is a DeclarativeBase subclass., Test that Base has metadata attribute set to shared metadata. (+7 more)

### Community 463 - "3. Common Patterns and Anti-patterns"
Cohesion: 0.09
Nodes (21): 1.1. Base Configuration, 1.2. TypeScript Integration (Type-Aware Linting), 1.3. Prettier Integration, 1. Core Configuration: Flat Config is Mandatory, 2. Code Organization and Structure, 3.1. Immutability (`prefer-const`), 3.2. Unused Variables (`no-unused-vars`), 3.3. Consistent Returns (`consistent-return`) (+13 more)

### Community 464 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 465 - "MemoryLeakMetricsCollector"
Cohesion: 0.07
Nodes (24): Initialize monitoring services. Depends on Core/Realtime/Game for injected deps., MemoryLeakMetricsCollector, Any, Collect event metrics from EventBus. Returns: Dictionary with event metrics, Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics, Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics, Collect NATS subscription metrics from NATSService. Returns: Dictionary with…, Unified metrics collector for memory leak detection. Aggregates metrics from… (+16 more)

### Community 466 - "enum"
Cohesion: 0.11
Nodes (19): ACCESSORY, AMULET, BELT, CURSED, FEET, GLOW, HANDS, HEAD (+11 more)

### Community 467 - "test_combat_schema.py"
Cohesion: 0.13
Nodes (17): Validate base_stats combat data against schema. Args: data: Base stats…, validate_base_stats_combat_data(), Unit tests for combat_schema validation functions. Tests the validation…, Test validate_npc_combat_data() validates NPC definition., Test validate_base_stats_combat_data() accepts valid data., Test validate_base_stats_combat_data() raises error for missing required fields., Test validate_base_stats_combat_data() raises error for invalid type., Test validate_behavior_config_combat_data() accepts valid data. (+9 more)

### Community 468 - "ConnectionErrorHandler"
Cohesion: 0.11
Nodes (27): ConnectionErrorHandler, Any, UUID, Error handling for connection management. This module provides comprehensive…, Handle WebSocket-specific errors. Args: player_id: The player's ID…, Handle authentication-related errors. Args: player_id: The player's ID…, Handle security violations. Args: player_id: The player's ID violation_type:…, Attempt to recover from an error state for a player. Args: player_id: The… (+19 more)

### Community 469 - "NPCThreadManager"
Cohesion: 0.05
Nodes (62): NPCThreadManager, Get list of active NPC thread IDs., Get NPC definition for a specific NPC., Parse NPC behavior config from instance attribute (dict or JSON string)., Manages NPC threads and their lifecycle. This class handles the creation,…, Start the NPC thread manager. Returns: bool: True if started successfully,…, asyncio, Unit tests for NPCThreadManager/NPCCommunicationBridge branches that… (+54 more)

### Community 470 - "test_event_publisher.py"
Cohesion: 0.08
Nodes (32): asyncio, Unit tests for event publisher. Tests the EventPublisher class., Test publish_game_tick_event() when NATS is not connected., Test get_next_sequence_number() returns and increments sequence., Test reset_sequence_number() resets sequence to 0., Persistence lookup should replace Player_/Room_ fallbacks in event data., Same persistence name resolution path for player_left., Legacy subject strings when subject_manager is unset. (+24 more)

### Community 471 - "mock_connection_manager"
Cohesion: 0.67
Nodes (3): mock_connection_manager(), fixture, Create a mock ConnectionManager for testing.

### Community 472 - "test_player_preferences_service.py"
Cohesion: 0.02
Nodes (111): mock_session(), preferences_service(), asyncio, fixture, Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID. (+103 more)

### Community 473 - "roomHandlers.ts"
Cohesion: 0.12
Nodes (32): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+24 more)

### Community 474 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 475 - "._execute_wander_movement"
Cohesion: 0.09
Nodes (11): Start a thread for a specific NPC. Args: npc_id: Unique identifier for the NPC…, Stop a specific NPC thread. Args: npc_id: Unique identifier for the NPC…, Internal method to stop an NPC thread., Restart a specific NPC thread. Args: npc_id: Unique identifier for the NPC…, Worker function for individual NPC threads. This function runs in a separate…, Process a message for an NPC., Resolve active NPC instance and definition for a WANDER action., Run idle movement for a resolved wander NPC. (+3 more)

### Community 476 - "AsciiMapRenderer"
Cohesion: 0.15
Nodes (11): AsciiMapRenderer, Renders ASCII maps from room coordinate data. Supports multiple map styles…, Initialize the ASCII map renderer., Tests for _vertical_exit_char_between (|, v, ^)., Bidirectional vertical exit renders as a vertical bar., One-way south exit renders as a lowercase 'v'., One-way north exit renders as a caret., When there are no vertical exits, the helper returns None. (+3 more)

### Community 477 - "test_who_commands.py"
Cohesion: 0.11
Nodes (17): Unit tests for who commands., Test filtering players with no filter term., Test format_who_result with no players., Test format_who_result with no players and filter term., Test format_who_result with players., Test format_who_result with players and filter term., Test get_players_for_who without filter., Test get_players_for_who with filter. (+9 more)

### Community 478 - "ChatChannelLoggerMixin"
Cohesion: 0.10
Nodes (19): ChatChannelLoggerMixin, Any, Path, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper…, Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs. (+11 more)

### Community 479 - "_find_item_in_equipped"
Cohesion: 0.11
Nodes (24): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _handle_item_look(), Any, Item look functionality for MythosMUD. This module handles looking at items,…, Find an item in equipped items by name or prototype_id. Args: equipped:…, Check if item found in a location and return formatted result. (+16 more)

### Community 480 - ".create_cast_command"
Cohesion: 0.11
Nodes (16): Test create_cast_command() with 'heal' and no target invokes heal_self., Test /cast heal self -> heal_self, no target., Test /cast heal me -> heal_self, no target., Test create_cast_command() raises error with no args., Test create_cast_command() with two args: first=spell, rest=target., Test /cast heal <target> (target not self/me) -> heal_other with target., Test /cast heal other <target> -> heal_other with target., test_create_cast_command() (+8 more)

### Community 481 - "create_hasher_with_params"
Cohesion: 0.12
Nodes (17): PasswordHasher, create_hasher_with_params(), Create a PasswordHasher with custom parameters., Test that create_hasher_with_params logs warning for low time_cost., Test that create_hasher_with_params logs warning for low memory_cost., Test creating hasher with valid parameters., Test creating hasher with invalid time_cost., Test creating hasher with invalid memory_cost. (+9 more)

### Community 482 - "MotdInterstitialScreen.tsx"
Cohesion: 0.21
Nodes (5): MotdContent(), MOTD_BUTTON_STYLE, MotdInterstitialScreen(), MotdInterstitialScreenProps, MotdInterstitialScreen

### Community 483 - "Test Pruning Candidates - Detailed List"
Cohesion: 0.06
Nodes (33): 1. Command Validation Tests, 2. Error Response Tests, 3. Permission Check Tests, Aggressive Estimate (Full Optimization), Category A: Infrastructure Tests Testing Framework Behavior, Category B: Coverage Tests Written for Metrics, Category C: Model Property Tests, Conclusion (+25 more)

### Community 484 - "test_passive_lucidity_flux_service.py"
Cohesion: 0.15
Nodes (27): PassiveLucidityFluxService, _make_service(), asyncio, Unit tests for PassiveLucidityFluxService., test_apply_adaptive_resistance_positive_flux_unchanged(), test_apply_adaptive_resistance_reduces_negative_flux(), test_apply_residual_accumulates_and_emits_delta(), test_apply_residual_negative_delta() (+19 more)

### Community 485 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 486 - "Stop-MythosMudProjectProcessTree"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 487 - "test_game_tick_processing.py"
Cohesion: 0.04
Nodes (79): cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _CorpseLike, _create_corpse_lifecycle_service(), _log_cleanup_results(), FastAPI, Protocol, Create CorpseLifecycleService or None if persistence is unavailable. (+71 more)

### Community 488 - "processing.py"
Cohesion: 0.04
Nodes (76): check_alias_safety(), handle_expanded_command(), Any, CommandExecutionRequest, Alias Expansion Logic for MythosMUD. This module handles alias resolution,…, Handle command processing with alias expansion and loop detection. This…, Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:… (+68 more)

### Community 489 - "ItemPrototypeModel"
Cohesion: 0.10
Nodes (23): Constants supporting item prototype validation. These enumerations anchor the…, ItemPrototypeModel, BaseModel, field_validator, Pydantic models for item prototype validation. This module defines the…, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validated representation of an item prototype definition. This model keeps the… (+15 more)

### Community 490 - "who_commands.py"
Cohesion: 0.18
Nodes (16): filter_online_players(), filter_players_by_name(), format_who_result(), get_players_for_who(), handle_who_command(), Any, Who command handlers and utilities for MythosMUD. This module contains the who…, Filter players to only those who are online (active within threshold). Args:… (+8 more)

### Community 491 - "PersonalMessageSender"
Cohesion: 0.19
Nodes (19): PersonalMessageSender, Personal message delivery for connection management. This module provides…, Sends personal messages to individual players. This class provides: - Personal…, asyncio, fixture, LogCaptureFixture, Unit tests for PersonalMessageSender., E2E teardown: send after client drop must not warn. (+11 more)

### Community 492 - "._handle_exception"
Cohesion: 0.16
Nodes (13): Exception, Receive, Request, Response, Scope, Send, ASGI application interface. Args: scope: ASGI connection scope receive: ASGI…, Handle an exception and send a standardized error response. Args: scope: ASGI… (+5 more)

### Community 493 - "test_npc_combat_integration_service_npc_aggro.py"
Cohesion: 0.08
Nodes (33): mock_async_persistence(), mock_combat_service(), mock_connection_manager(), mock_messaging_integration(), asyncio, Unit tests for NPC combat integration service - NPC-initiated aggro combat…, Test handle_npc_attack_on_player returns False when NPC instance cannot be…, Test handle_npc_attack_on_player returns False when NPC is dead. (+25 more)

### Community 494 - "containers.sql"
Cohesion: 0.13
Nodes (5): container_contents, schema_name.add_item_to_container(), schema_name.get_container_contents_json(), item_instances, item_prototypes

### Community 495 - "e2e-bootstrap.ts"
Cohesion: 0.14
Nodes (28): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+20 more)

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
Nodes (32): MagicServiceHealingMixin, Any, UUID, Healing event notification for spellcasting. Mixin that sends player_dp_updated…, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or… (+24 more)

### Community 500 - "CommandRateLimiter"
Cohesion: 0.11
Nodes (21): CommandRateLimiter, Any, datetime, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate…, Remove timestamp data for players who haven't been active recently. Prevents… (+13 more)

### Community 501 - "_NPCCombatIntegrationValidationDeps"
Cohesion: 0.13
Nodes (14): _coerce_xp_mapping_value(), _NPCCombatIntegrationValidationDeps, Protocol, UUID, End any active combat that includes this player when room validation fails., Convert string IDs to UUIDs and set up XP mappings., Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,…, Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1). (+6 more)

### Community 502 - "Phase 2: Enhanced Features"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 2: Enhanced Features, Sub-tasks, Sub-tasks (+8 more)

### Community 503 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 504 - "Async Audit Executive Summary"
Cohesion: 0.06
Nodes (31): Alternative Approaches Considered, Async Audit Executive Summary, Benefit, Break-Even, Contact, Cost, Cost-Benefit Analysis, Critical Findings (+23 more)

### Community 505 - "TEMPORAL_SYSTEM_RESEARCH.md"
Cohesion: 0.07
Nodes (30): The Call of Cthulhu, Canonical and Derived Observances, Implementation Notes, Mythos Holiday Candidates, Narrative Flavor Seeds, Opportunities for Expansion, 1. Research Synthesis, 2. Mythos Time Model Draft (+22 more)

### Community 506 - "async_sessionmaker"
Cohesion: 0.15
Nodes (29): async_sessionmaker, asyncio, AsyncSession, fixture, integration, update_room_properties() with p_set_environment=TRUE and NULL clears the…, p_set_environment=FALSE leaves attributes.environment untouched, regardless of…, update_room_properties() on a nonexistent stable_id returns FALSE, no exception. (+21 more)

### Community 507 - "Prometheus Configuration"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 508 - "load_world_seed.py"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 509 - "validate.py"
Cohesion: 0.10
Nodes (30): BugBlock, check_bug_content(), _check_bugs(), check_loose_tags(), _check_required_structure(), _exit_code_for_errors(), find_bug_blocks(), find_first_content_section() (+22 more)

### Community 510 - "ReactNodeUpgradeAnalyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 511 - "game_tick_processing.py"
Cohesion: 0.05
Nodes (75): _handle_player_death_threshold(), _player_in_active_combat(), _process_dead_players(), process_dp_decay_and_death(), _process_mortally_wounded_player(), _process_mortally_wounded_players(), _process_mp_regeneration(), _process_passive_lucidity_flux() (+67 more)

### Community 512 - "_find_item_in_inventory"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id. Args: inventory: List…, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 513 - "run_flee_effect"
Cohesion: 0.15
Nodes (28): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+20 more)

### Community 514 - "NPCCommunicationIntegration"
Cohesion: 0.10
Nodes (23): NPCCommunicationIntegration, Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…, Process a message to determine if the NPC should respond. Args: npc_id: ID of…, Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…, Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…, Integrates NPCs with the existing chat and whisper systems. This class provides…, Initialize the NPC communication integration. Args: event_bus: Optional…, Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the… (+15 more)

### Community 515 - "combat_schema.py"
Cohesion: 0.23
Nodes (14): Draft7Validator, CombatSchemaValidationError, Exception, Combat system JSON schema validation. This module provides JSON schema…, Raised when combat data fails schema validation., Validate behavior_config combat data against schema. Args: data: Behavior…, Validate combat message templates. Args: messages: Combat messages dictionary…, Validate that message templates contain required variables. Args: messages:… (+6 more)

### Community 516 - "test_npc_combat_integration_service_player_attacks.py"
Cohesion: 0.09
Nodes (30): asyncio, Unit tests for NPC combat integration service - player-initiated combat paths., Test handle_player_attack_on_npc returns False when NPC not found., Test handle_player_attack_on_npc handles exceptions gracefully., Test _setup_combat_uuids_and_mappings handles ValueError., Test _setup_combat_uuids_and_mappings with valid UUID., Test store_npc_xp_mapping_for_mixin when NPC definition is not found., Test store_npc_xp_mapping_for_mixin when base_stats is not a dict. (+22 more)

### Community 517 - "test_combat_validator.py"
Cohesion: 0.02
Nodes (87): Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_combat_command with target name too long., Test validate_combat_command when rate limited., Test validate_combat_command handles exceptions gracefully., Test validate_target_exists with exact match., Test validate_target_exists with case-insensitive match., Test validate_target_exists with partial match., Test validate_target_exists with no match. (+79 more)

### Community 518 - "CombatValidator"
Cohesion: 0.06
Nodes (28): combat_validator(), fixture, Create a CombatValidator instance., When party_service is None, validate_can_attack_target allows attack., When both players are in same party, validate_can_attack_target blocks attack., When players are not in same party, validate_can_attack_target allows attack., test_validate_can_attack_target_different_party_allows(), test_validate_can_attack_target_no_party_service_allows() (+20 more)

### Community 519 - "test_optimized_security_validator.py"
Cohesion: 0.08
Nodes (35): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test benchmark function runs without errors., Test validating message with path traversal pattern., Test validating message with javascript: URL. (+27 more)

### Community 520 - "MinimapRenderer"
Cohesion: 0.09
Nodes (17): MinimapRenderer, Any, Mini-map renderer for room connectivity visualization. This module provides…, Renders room connectivity graphs in various visual formats. Implements the…, Extract street acronym from room ID. Args: room_id: Full room ID (e.g.,…, Extract street name from room ID. Args: room_id: Full room ID Returns: Street…, Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…, Render the mini-map as ASCII art with grid-based visualization. Args:… (+9 more)

### Community 521 - "scripts"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 522 - "map/config.ts"
Cohesion: 0.13
Nodes (19): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeBody(), ExitEdgeLabels() (+11 more)

### Community 523 - "type"
Cohesion: 0.13
Nodes (16): items, type, items, type, uniqueItems, minLength, type, effect_components (+8 more)

### Community 524 - "P8 · Applied"
Cohesion: 0.07
Nodes (28): Code changes — comment-only, explicitly authorised, Documentation changes — 33 files, Issues created — 14, Issues reopened — 12, New ADRs, Not done — deliberately, P8 · Applied, Security — filed privately, not publicly (+20 more)

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
Cohesion: 0.07
Nodes (48): broadcast_teleport_effects(), create_teleport_effect_message(), get_online_player_by_display_name(), notify_player_of_teleport(), Any, Notify a player that they are being teleported by an admin. Args:…, Get online player information by display name. Args: display_name: Display name…, Create teleport effect message for visual display. Args: player_name: Name of… (+40 more)

### Community 530 - "test_container_helpers_inventory_display.py"
Cohesion: 0.12
Nodes (28): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+20 more)

### Community 531 - "inventory_equip_command.py"
Cohesion: 0.08
Nodes (54): normalize_equipped_items(), normalize_inventory_slots(), Normalize slot_type in inventory list in-place., Normalize slot names and slot_type in equipped items., _equip_build_work(), _equip_inventory_rollback_snapshot(), _equip_persist_or_rollback(), _equip_run_mutation() (+46 more)

### Community 532 - "EventBusLifecycleMixin"
Cohesion: 0.10
Nodes (17): EventBusLifecycleMixin, Exception, Task, Cancel leftover tasks after the grace wait, then give them a short drain., Cancel all active tasks and wait for graceful shutdown., Finalize shutdown by clearing tasks and logging., Stop pure async event processing gracefully., Unsubscribe every tracked service. No-op when none are registered. (+9 more)

### Community 533 - "persistence/container_helpers.py"
Cohesion: 0.18
Nodes (15): _coerce_row_quantity(), fetch_container_items(), _item_dict_from_contents_row(), _metadata_dict_from_cell(), PsycopgConnection, PsycopgCursor, UUID, Helper functions for container persistence operations. (+7 more)

### Community 534 - "ComprehensiveLoggingMiddleware"
Cohesion: 0.10
Nodes (23): ComprehensiveLoggingMiddleware, Any, ASGIApp, Exception, Receive, Request, Scope, Send (+15 more)

### Community 535 - "CombatParticipantData"
Cohesion: 0.05
Nodes (40): _build_combat_instance(), _build_participant(), CombatInitializer, _compute_turn_order(), UUID, Combat initialization logic. Handles creation and setup of combat instances., Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…, Build CombatParticipant from CombatParticipantData. (+32 more)

### Community 536 - "test_room_occupant_manager.py"
Cohesion: 0.09
Nodes (29): mock_connection_manager(), occupant_manager(), asyncio, fixture, Unit tests for room occupant manager. Tests the RoomOccupantManager class for…, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test get_room_occupants handles get_players error. (+21 more)

### Community 537 - "test_lint_container_get_instance.py"
Cohesion: 0.10
Nodes (26): _LintContainerGetInstanceModule, _load_script(), Protocol, Unit tests for scripts/lint_container_get_instance.py. Verifies the detection…, A file with more get_instance() calls than its allowlist entry expects fails --…, A file with fewer get_instance() calls than its allowlist entry expects fails…, An allowlist entry for a file with zero remaining hits (fully migrated) must…, A blank line inserted above the allowlisted site must not trip a violation --… (+18 more)

### Community 538 - "ContainerLockMixin"
Cohesion: 0.23
Nodes (10): ContainerLockMixin, Player, UUID, Lock a container (LOCKED or SEALED). Requires ownership or admin., Unlock a container. Requires access and unlock eligibility (key/admin)., Lock/unlock container state persistence., Load container for lock/unlock ops, or raise ContainerNotFoundError., Load player for lock/unlock ops, or raise ValidationError. (+2 more)

### Community 539 - "Async Remediation Final Report"
Cohesion: 0.07
Nodes (29): 48 Sync Persistence Call Instances, Async Remediation Final Report, All async anti-patterns have been exorcised from the codebase, All Targets Met, API/Commands (2 files), Checklist, ✅ COMPLETE - ALL 48 INSTANCES MIGRATED, Core Infrastructure (2 files) (+21 more)

### Community 540 - "🔴 CRITICAL ISSUES"
Cohesion: 0.07
Nodes (28): 10. Use of `BETWEEN` with Integer Ranges, 11. Missing Indexes on Foreign Keys, 12. Inconsistent Constraint Naming, 13. Mixed Case in Table/Column Names, 14. Missing `UNIQUE` Constraints Where Appropriate, 15. Inconsistent Use of `NOT NULL` Constraints, 16. Missing Documentation for Complex Constraints, 1. Use of `serial`/`SERIAL` Instead of `bigint generated always as identity` (+20 more)

### Community 541 - "Test Suite Quality Audit - Executive Summary"
Cohesion: 0.07
Nodes (29): **25-30% (~1,250-1,500 tests) provide CRITICAL regression protection**, Answer to Original Question, Breakdown, By Category, CI/CD Time Saved, Commit to full 2-month optimization plan, Comparison to Industry Benchmarks, Created Documents (+21 more)

### Community 542 - "test_inventory_mutation_guard_async.py"
Cohesion: 0.17
Nodes (15): guard(), asyncio, fixture, Unit tests for inventory mutation guard - asynchronous acquire operations.…, Test acquire_async serializes concurrent mutations for same player., Create an InventoryMutationGuard instance., Test acquire_async enforces max_tokens limit., Test acquire_async allows token reuse after expiry. (+7 more)

### Community 543 - "test_inventory_command_prototype.py"
Cohesion: 0.12
Nodes (26): _first_normalized_wear_slot(), infer_equip_slot_from_prototype(), _inventory_prototype_id(), prototype_from_registry(), prototype_registry_from_request(), Prototype registry access and equip-slot inference for inventory items., Resolve prototype registry from FastAPI-style request (agent-readable…, Return the prototype object for ``prototype_id``, or None if missing or invalid. (+18 more)

### Community 544 - "test_world_loader.py"
Cohesion: 0.16
Nodes (11): Unit tests for world loader utility functions. Tests room ID generation,…, Test validate_room_data() function., Test generate_room_id() function., Test generate_room_id() with basic components., Test generate_room_id() handles components with underscores., Test generate_room_id() with empty components., Test generate_room_id() preserves special characters in components., TestGenerateRoomId (+3 more)

### Community 545 - "test_lifecycle_respawn.py"
Cohesion: 0.18
Nodes (26): Process the respawn queue and spawn NPCs that are ready (delegates to…, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…, Process the respawn queue and spawn NPCs that are ready. Args: manager:… (+18 more)

### Community 546 - "UtilityCommandFactory"
Cohesion: 0.15
Nodes (15): Test create_teleport_command() raises error with no args., Test create_teleport_command() with direction., Test create_teleport_command() raises error with invalid direction., Test create_spell_command() creates SpellCommand., Test create_spell_command() raises error with no args., Test create_spell_command() with multi-word spell name., test_create_spell_command(), test_create_spell_command_multi_word() (+7 more)

### Community 547 - "NPCStartupService"
Cohesion: 0.15
Nodes (14): _merge_phase_into_startup(), _new_spawn_results(), NPCStartupService, Any, NPC Startup Service for MythosMUD. This module provides automatic NPC spawning…, Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…, Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…, Second pass: spawn one instance per definition (that was spawned in… (+6 more)

### Community 548 - "PlayerPreferencesService"
Cohesion: 0.15
Nodes (17): PlayerPreferencesService, Any, AsyncSession, UUID, Get preferences for a player. Args: session: Database session player_id: The…, Update a player's default channel. Args: session: Database session player_id:…, Mute a channel for a player. Args: session: Database session player_id: The…, Unmute a channel for a player. Args: session: Database session player_id: The… (+9 more)

### Community 549 - "TestLogoutCommand"
Cohesion: 0.11
Nodes (17): Any, asyncio, fixture, Unit tests for the logout command handler., Test logout command when persistence is not available., Test logout command when persistence operations fail., Test cases for the logout command handler., Test logout command when connection cleanup fails. (+9 more)

### Community 550 - "test_chat_moderation.py"
Cohesion: 0.11
Nodes (20): moderation(), player_service(), asyncio, fixture, Unit tests for chat moderation operations., test_add_admin_returns_true(), test_get_mute_status_handles_internal_error(), test_get_mute_status_includes_player_name() (+12 more)

### Community 551 - "test_inventory_mutation_guard.py"
Cohesion: 0.07
Nodes (29): guard(), asyncio, fixture, Unit tests for inventory mutation guard - core functionality. Tests…, Test acquire_async without token allows mutation., Test acquire_async with unique token allows mutation., Test acquire_async with duplicate token suppresses mutation., Test acquire_async allows same token for different players. (+21 more)

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

### Community 559 - "canonical_room_id_impl"
Cohesion: 0.09
Nodes (30): canonical_room_id_public_impl(), Resolve a room id to the canonical Room.id value (public method)., canonical_room_id_impl(), prune_player_from_all_rooms_impl(), Any, Resolve a room id to the canonical Room.id value. Args: room_id: The room ID to…, Ensure room_occupants only contains currently online players., Remove a player from all room subscriptions and occupant lists. (+22 more)

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
Cohesion: 0.20
Nodes (10): city, countryside, desert, mountains, swamp, tundra, zone_type, description (+2 more)

### Community 572 - "LogAnalyzer"
Cohesion: 0.12
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time. Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 573 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (49): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id. Args: room_drops: List of…, Unit tests for look item helper functions. Tests the helper functions in…, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items. (+41 more)

### Community 574 - "test_chat_pose_helpers.py"
Cohesion: 0.16
Nodes (25): clear_player_pose(), get_player_pose(), get_room_poses(), normalize_player_id(), Any, UUID, Pose management helpers for chat service., Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose… (+17 more)

### Community 575 - "MetricsCollector"
Cohesion: 0.08
Nodes (18): MetricsCollector, Any, Metrics collection for NATS message delivery. Collects and exposes metrics for…, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or…, Simple metrics collector for NATS message delivery. Thread-safe metrics… (+10 more)

### Community 576 - "test_npc_threading_messages.py"
Cohesion: 0.06
Nodes (33): NPCMessageQueue, Thread-safe message queue for NPC actions. This queue handles pending actions…, Initialize the NPC message queue. Args: max_messages_per_npc: Maximum number of…, Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…, Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…, Clear all pending messages for an NPC. Args: npc_id: The NPC's ID Returns:…, Get the number of pending messages for an NPC., Get the total number of pending messages across all NPCs. (+25 more)

### Community 577 - "attach_compatibility_properties"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 578 - "rooms.sql"
Cohesion: 0.15
Nodes (4): schema_name.create_room_link(), schema_name.delete_room_link(), schema_name.update_room_link(), rooms

### Community 579 - "extract_player_name"
Cohesion: 0.13
Nodes (25): extract_player_name(), _get_name_from_user(), get_player_position(), _is_uuid_string(), _is_valid_name(), Any, Player, UUID (+17 more)

### Community 580 - "RateLimiter"
Cohesion: 0.09
Nodes (18): Any, RateLimiter, Remove timestamps older than the window size. Args: player_id: Player ID…, Check if a player is within rate limits for a channel. Args: player_id: Player…, Record a message for rate limiting. Args: player_id: Player ID channel: Channel…, Sliding window rate limiter for chat channels. Implements per-user, per-channel…, Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…, Reset rate limiting for a player. Args: player_id: Player ID channel: Specific… (+10 more)

### Community 581 - "test_time_bundle.py"
Cohesion: 0.08
Nodes (28): isolated_chronicle(), asyncio, fixture, Unit tests for TimeBundle container wiring., Calendar components and daypart helpers., Real/Mythos datetime conversion round-trips approximately., Advance and freeze update persisted state., Clock formatting includes Mythos suffix. (+20 more)

### Community 582 - "test_movement_monitor.py"
Cohesion: 0.03
Nodes (58): movement_monitor(), fixture, Unit tests for movement monitor. Tests the MovementMonitor class for monitoring…, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data., Test validate_room_integrity() detects duplicate players., Test validate_room_integrity() handles empty rooms dict. (+50 more)

### Community 583 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

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
Cohesion: 0.15
Nodes (24): ensureIthaquaInFoyer(), leaveEasternHallwayWest(), pageShowsEasternHallway(), prepareLocalIsolationPair(), primeBothForCoLocate(), returnAwToFoyerIfInHallway(), softCommand(), waitForLookReflected() (+16 more)

### Community 589 - "Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.08
Nodes (26): 1. Deprecated `asyncio.get_event_loop()` Usage, 1. Proper Connection Pool Management, 2. Good Error Handling Patterns, 2. SQL Injection Risk in Field Name Construction, 3. Async/Await Usage, 3. Connection Pool Cleanup Verification, 4. Blocking Operations in Async Context, 4. Security Considerations (+18 more)

### Community 590 - "test_load_world_seed.py"
Cohesion: 0.12
Nodes (25): regression, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, CaptureFixture, fixture, MonkeyPatch, Protocol (+17 more)

### Community 591 - "test_emote_repository.py"
Cohesion: 0.27
Nodes (12): _alias_row(), _emote_row(), _mock_session(), asyncio, fixture, Unit tests for EmoteRepository (#624)., repo(), test_get_emote_aliases() (+4 more)

### Community 592 - "PrototypeRegistry"
Cohesion: 0.15
Nodes (20): PrototypeRegistry, Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, In-memory registry for validated item prototypes., Load prototypes from a directory of JSON files., _make_prototype() (+12 more)

### Community 593 - "schemas/unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 594 - "connection_cleanup_methods.py"
Cohesion: 0.07
Nodes (41): check_and_cleanup_impl(), cleanup_dead_connections_impl(), cleanup_ghost_players_impl(), cleanup_orphaned_data_impl(), force_cleanup_impl(), prune_stale_players_impl(), Any, UUID (+33 more)

### Community 595 - ".claude/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 596 - "Vitest Best Practices"
Cohesion: 0.08
Nodes (22): Vite Configuration, 1. Code Organization & Naming, 2. Test Structure & Isolation, 3. Asynchronous Testing with `vi.waitFor`, 4. Mocking Strategies, 5. DOM Environment & Component Testing, 6. Performance & Concurrent Tests, 7. Code Coverage (+14 more)

### Community 597 - "dependencies"
Cohesion: 0.08
Nodes (25): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-resizable, react-rnd (+17 more)

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

### Community 611 - "create_app"
Cohesion: 0.11
Nodes (23): create_app(), FastAPI, Mount all versioned API routers under /v1., Create and configure the FastAPI application. This function sets up the FastAPI…, _register_v1_routers(), _create_get_app(), main(), Any (+15 more)

### Community 612 - "utility_commands.py"
Cohesion: 0.08
Nodes (40): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+32 more)

### Community 613 - "BehaviorEngine"
Cohesion: 0.02
Nodes (122): BehaviorEngine, Any, Behavior engine for NPCs. This module provides the deterministic behavior…, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string… (+114 more)

### Community 614 - "error_handling_middleware.py"
Cohesion: 0.23
Nodes (13): add_error_handling_middleware(), FastAPI, Protocol, Error handling middleware for FastAPI integration. This module provides…, Add error handling middleware to FastAPI application. Args: app: FastAPI…, Register error handlers for FastAPI application. This function registers…, Setup complete error handling for FastAPI application. This function sets up…, Narrowing for dynamic request.state.user shapes that expose .id (non-Mapping). (+5 more)

### Community 616 - "test_spell_repository.py"
Cohesion: 0.23
Nodes (13): Any, Map procedure result row to spell dict., Get all spells from the database. Returns: list[dict]: List of all spell…, _row_to_spell_dict(), _mock_session(), asyncio, Unit tests for SpellRepository., _spell_row() (+5 more)

### Community 617 - "npc_combat_grace.py"
Cohesion: 0.17
Nodes (17): get_app_instance(), Return the runtime app instance attached during lifespan startup. This provides…, _connection_manager_from_config_app(), is_npc_attack_on_player_blocked_by_login_grace_period(), is_player_attack_blocked_by_login_grace_period(), ConnectionManager, UUID, Login grace-period checks for NPC combat integration (extracted to keep service… (+9 more)

### Community 618 - "UUID"
Cohesion: 0.17
Nodes (8): UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return True if websocket appears dead (should be cleaned up)., Return list of player IDs to check (single player or all)., Clean up dead connections for a single player., Clean up dead connections for a specific player or all players. Args:…

### Community 619 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test handling item look when item is in room drops., Test handling item look when item is in inventory., Test handling item look when item is equipped., Test handling item look when item not found., Test handling item look with look_in flag skips equipped items., Test trying implicit lookup when item is in room drops., Test trying implicit lookup when item not found. (+17 more)

### Community 620 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test formatting NPC stats for admin successfully., Test formatting NPC stats for admin when NPC ID missing., Test formatting single NPC result successfully., Test formatting single NPC result with admin stats., Test trying implicit NPC lookup successfully., Test trying implicit NPC lookup when no NPCs in room., Test trying implicit NPC lookup with multiple matches. (+7 more)

### Community 621 - "test_ascii_map_renderer_exits.py"
Cohesion: 0.13
Nodes (11): fixture, Unit tests for AsciiMapRenderer exit character and exit resolution. Guards…, Tests for _get_exit_entries_for_room., Valid exits for a room produce one entry with correct direction and coordinates., Exits whose targets are missing are skipped when building exit entries., Viewport bounds: return None when next cell is outside viewport., Returns None when the next horizontal cell lies at or beyond the viewport's…, Return a fresh AsciiMapRenderer instance for each test. (+3 more)

### Community 622 - "asyncio"
Cohesion: 0.07
Nodes (27): asyncio, Test _spawn_required_npcs() successfully spawns required NPCs., Test _spawn_required_npcs() handles spawn failures., Test _spawn_optional_npcs() spawns based on probability., Test _determine_spawn_room() uses NPC's room_id when available., Test _determine_spawn_room() uses sub_zone default when room_id not available., Test _spawn_optional_npcs() handles missing spawn room., Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute. (+19 more)

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
Cohesion: 0.07
Nodes (28): Alpha Is A Design Smell, Building Functional Palettes, Color & Contrast, Color Spaces: Use OKLCH, Contrast & Accessibility, Dangerous Color Combinations, Dark Mode Is Not Inverted Light Mode, Never Use Pure Gray or Pure Black (+20 more)

### Community 629 - "Onboard Skill"
Cohesion: 0.08
Nodes (24): Onboard Skill, Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption (+16 more)

### Community 630 - "stateNormalization.ts"
Cohesion: 0.07
Nodes (37): ConnectionActions, ConnectionHealth, ConnectionMetadata, ConnectionSelectors, ConnectionState, ConnectionStore, createInitialState(), GameEvent (+29 more)

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

### Community 636 - "EventPublisher"
Cohesion: 0.16
Nodes (12): EventPublisher, JsonMap, Publish a player_entered event to NATS. Args: player_id: ID of the player who…, Publish a player_left event to NATS. Args: player_id: ID of the player who left…, Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…, Create a standardized event message structure. Args: event_type: Type of event…, Get the next sequence number for event ordering. Returns: Next sequence number, Reset the sequence number to 0. (+4 more)

### Community 637 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 638 - "migrate_rooms.py"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 639 - "test_skills_commands.py"
Cohesion: 0.22
Nodes (10): _get_container_services(), Get container, persistence, and skill_service from request, or None if…, asyncio, Unit tests for skills command helpers., test_get_container_services_missing(), test_get_container_services_ok(), test_handle_skills_command_no_services(), test_handle_skills_command_success() (+2 more)

### Community 640 - "handle_teach_command"
Cohesion: 0.18
Nodes (22): _format_teach_result(), _get_teach_services(), handle_teach_command(), Any, Teach command handler for learning spells from NPC teachers. This module…, Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, _resolve_npc_teacher(), asyncio (+14 more)

### Community 641 - "_lucidity_change_payload_with_liabilities"
Cohesion: 0.13
Nodes (15): _lucidity_change_payload_with_liabilities(), LiabilityStackEntry, Test liability formatting skips entries with empty code., Dispatch a lucidity change event and return the payload., Test liability formatting with empty input via send_lucidity_change_event., Test liability formatting with a single liability., Test liability formatting with multiple stacks., Test liability formatting with multiple entries. (+7 more)

### Community 642 - "realtime/realtime.py"
Cohesion: 0.14
Nodes (19): Realtime domain schemas: realtime API, NATS messages, WebSocket messages., ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD. This module defines…, Presence statistics for connection monitoring. This model represents aggregate…, Error statistics for connection monitoring. This model represents aggregate…, ConnectionStatisticsResponse (+11 more)

### Community 643 - "CombatDeathHandler"
Cohesion: 0.04
Nodes (41): CombatAttackHandler, Any, UUID, Apply damage to target and update combat state. Args: combat: Combat instance…, Validate attack and retrieve combat participants. Args: attacker_id: ID of the…, Handles combat attack processing and damage application., Initialize the attack handler. Args: combat_service: Reference to the parent…, Validate that attack is allowed. (+33 more)

### Community 644 - "_handle_admin_set_stat_command"
Cohesion: 0.05
Nodes (72): _AdminSetStatApplyContext, _AdminSetStatLogContext, _apply_stat_change_and_build_result(), _build_set_stat_error_response(), _calculate_stat_warnings(), _get_app_or_error(), _handle_admin_set_stat_command(), _log_admin_set_stat() (+64 more)

### Community 645 - "Lint Remediation"
Cohesion: 0.14
Nodes (12): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — code quality, Lint Remediation — Reference, 🟢 Medium — style, Entry point (+4 more)

### Community 646 - "mythos_dev.rooms"
Cohesion: 0.16
Nodes (14): mythos_dev.count_coordinated_rooms(), mythos_dev.create_room_link(), mythos_dev.delete_room_link(), mythos_dev.get_room_id_by_stable_id(), mythos_dev.is_room_explored(), mythos_dev.player_exploration, mythos_dev.room_links, mythos_dev.rooms (+6 more)

### Community 647 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 648 - "test_player_respawn_handlers.py"
Cohesion: 0.31
Nodes (13): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), ValidationError, Convert ValidationError to appropriate HTTPException for respawn. Args: e:…, Convert ValidationError to appropriate HTTPException for delirium respawn.…, test_handle_delirium_validation_generic_500(), test_handle_delirium_validation_lucidity_keyword(), test_handle_delirium_validation_must_be_delirious() (+5 more)

### Community 649 - "_clear_corrupted_cache_entry"
Cohesion: 0.14
Nodes (14): _clear_corrupted_cache_entry(), Clear a corrupted cache entry if it exists. Args: request: FastAPI request…, Test _clear_corrupted_cache_entry() clears cache entry., Test _clear_corrupted_cache_entry() handles None request., Test _clear_corrupted_cache_entry() handles request without state., test_clear_corrupted_cache_entry(), test_clear_corrupted_cache_entry_no_request(), test_clear_corrupted_cache_entry_no_state() (+6 more)

### Community 650 - "test_npc_startup_service.py"
Cohesion: 0.08
Nodes (25): Unit tests for NPC startup service. Tests the NPCStartupService class., Test _spawn_optional_npcs() skips NPCs with low probability., Test _determine_spawn_room() uses fallback room when no other option., Test _determine_spawn_room() returns None when persistence not available., Test _get_default_room_for_sub_zone() returns correct room for known sub-zone., Test _get_default_room_for_sub_zone() returns None for unknown sub-zone., Test _get_default_room_for_sub_zone() is case insensitive., #679: NPCStartupService no longer reaches ApplicationContainer.get_instance()… (+17 more)

### Community 651 - "CommandProcessor"
Cohesion: 0.10
Nodes (17): command_processor(), fixture, Create a CommandProcessor instance., Test get_command_processor returns global instance., Test process_command_string handles Pydantic validation errors., test_get_command_processor(), test_process_command_string_pydantic_validation_error(), CommandProcessor (+9 more)

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
Cohesion: 0.09
Nodes (23): 1. **Import Inconsistency in `server/persistence.py`**, 2. **Import Organization Pattern**, Additional Findings, Best Practices Analysis, Code Review: Import Analysis and Anti-Patterns, Conclusion, Configuration Files, Container Files (+15 more)

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
Cohesion: 0.09
Nodes (21): asyncio.to_thread Persistence Pattern, Room Cache 60s TTL, adjusts spectacles and awaits instruction, Awaiting Your Direction, Professor Wolfshade, ✅ Completed Today, Critical Phase 1 Fixes (100% Complete), 🚦 Current Status, 🎯 Decision Point (+13 more)

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

### Community 667 - "_should_include_npc"
Cohesion: 0.14
Nodes (14): Check if an NPC should be included in the results (has name and is alive)., _should_include_npc(), Test _should_include_npc() returns True for valid NPC., Test _should_include_npc() returns False when no name., Test _should_include_npc() returns False when not alive., test_should_include_npc(), test_should_include_npc_no_name(), test_should_include_npc_not_alive() (+6 more)

### Community 668 - "RoomCacheLoader"
Cohesion: 0.20
Nodes (5): Any, BaseException, Loads room data from the database and populates a room cache dict. Used by…, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 669 - "format_player_location"
Cohesion: 0.14
Nodes (14): format_player_location(), Format player location as Zone: Sub-zone: Room from room ID. Args: room_id:…, Test format_player_location() handles invalid room ID., test_format_player_location_invalid(), Test format_player_location() with short room ID format., Test format_player_location() with non-string input., Test formatting valid player location., Test formatting invalid player location. (+6 more)

### Community 670 - ".send_message"
Cohesion: 0.23
Nodes (8): Any, UUID, Send message to a single WebSocket connection. Returns True if successful., Queue message if no active connections., Send a personal message to a player via WebSocket. Args: player_id: The…, Get message delivery statistics for a player., Initialize the personal message sender. Args: message_queue: MessageQueue…, Prepare and optimize the payload for sending.

### Community 671 - "MovementMonitor"
Cohesion: 0.11
Nodes (15): MovementMonitor, Any, UUID, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms., Get comprehensive movement metrics., Get current alerts based on thresholds. (+7 more)

### Community 672 - "test_add_player_effect_generates_id"
Cohesion: 0.23
Nodes (14): async_sessionmaker, asyncio, AsyncSession, serial, Verify get_rooms_with_exits() (room cache data source) includes arena zone…, Call get_player_by_id() with non-existent UUID; verify return shape when empty., Call get_npc_system_statistics() and verify result columns., Call add_player_effect() and verify it returns a non-null UUID. This guards… (+6 more)

### Community 673 - "test_retry.py"
Cohesion: 0.14
Nodes (13): Unit tests for retry utilities. Tests the retry decorator and retry logic., Test is_transient_error() identifies transient errors., Test is_transient_error() returns False for non-transient errors., DatabaseError wrapping asyncpg closed-connection must still retry (e2e…, __cause__ ConnectionDoesNotExistError makes the outer wrapper transient., Test retry_with_backoff() succeeds on first attempt., Test retry_with_backoff() retries on failure then succeeds., test_is_transient_error_cause_chain_connection_closed() (+5 more)

### Community 674 - "Lock"
Cohesion: 0.22
Nodes (5): Lock, Initialize metrics collector. AI: Uses Lock for thread-safety in async context., Initialize the communication bridge., Initialize the NPC thread manager., Get or create the async lock (lazy initialization).

### Community 675 - "ExperienceRepository"
Cohesion: 0.18
Nodes (19): Initialize the async persistence layer. This facade delegates to focused async…, ExperienceRepository, Player, Repository for player experience and stats persistence operations. Handles XP…, Award experience points to a player atomically. Args: player: Player to award…, asyncio, fixture, Unit tests for ExperienceRepository. (+11 more)

### Community 676 - "Any"
Cohesion: 0.14
Nodes (10): Any, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:…, Get and validate NPC lifecycle manager. Args: room_id: The room ID for logging…, Get fallback NPCs from room.get_npcs() if lifecycle manager query fails. Args:…, Process NPC IDs and convert to occupant information. Args: npc_ids: List of NPC… (+2 more)

### Community 677 - "apply_communication_dampening"
Cohesion: 0.17
Nodes (21): apply_communication_dampening(), _apply_receiver_effects(), _apply_sender_effects(), DampeningResult, _maybe_muffle_fractured_message(), _maybe_scramble_deranged_message(), TypedDict, Communication dampening utilities for lucidity system. Implements communication… (+13 more)

### Community 678 - "exploration.sql"
Cohesion: 0.17
Nodes (7): schema_name.count_coordinated_rooms(), schema_name.get_room_id_by_stable_id(), schema_name.is_room_explored(), rooms, subzones, zones, player_exploration

### Community 679 - "test_room_service.py"
Cohesion: 0.02
Nodes (111): mock_persistence(), mock_room_cache(), asyncio, fixture, Unit tests for room service. Tests the RoomService class for room-related…, Test get_room() returns None when room not found in persistence., Test get_room() handles dict from persistence., Test get_room_by_name() returns None (not implemented). (+103 more)

### Community 680 - "test_check_coverage_thresholds.py"
Cohesion: 0.15
Nodes (20): _CheckCoverageThresholdsModule, _fully_covered(), _load_script(), Protocol, Unit tests for scripts/check_coverage_thresholds.py. Covers `check_thresholds`'…, A KNOWN_COVERAGE_DEBT entry lowers the blanket 70% normal-file floor (#677)., A file present in CRITICAL_FILES but absent from the coverage.xml data (e.g.…, Typed surface of the loaded script, for the parts these tests exercise. (+12 more)

### Community 681 - "CombatPersistenceHandler"
Cohesion: 0.05
Nodes (39): CombatPersistenceHandler, Any, UUID, Combat persistence handling logic. Handles player DP persistence, verification,…, # NOTE: The game tick loop will also check for dead players, but this provides…, Synchronously persist player DP to database. This is the actual persistence…, Persist player DP to database in background (fire-and-forget). This method runs…, Handles combat-related persistence operations. (+31 more)

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

### Community 687 - "mapPageRenderer.tsx"
Cohesion: 0.13
Nodes (22): RoomDetailsPanelProps, RoomMapViewerProps, LocationPanelProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView(), renderMapPageState() (+14 more)

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

### Community 695 - "time.py"
Cohesion: 0.02
Nodes (119): Time bundle: the Temporal bounded context…, NPCListened, NPCTookDamage, PlayerEnteredRoom, Event fired when an NPC takes damage. This event is triggered when an NPC…, Event fired when an NPC receives a message. This event is triggered when an NPC…, Event fired when a player enters a room. This event is triggered when a player…, get_summary() (+111 more)

### Community 696 - "test_security_utils.py"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory. Args: filename: The filename…, Unit tests for security utilities. Tests path validation and file security…, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 697 - "Phase 4: Testing and Refinement"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 4: Testing and Refinement, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 698 - "status_commands.py"
Cohesion: 0.28
Nodes (12): _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_status_persistence(), handle_status_command(), handle_whoami_command(), Any, Status command handlers for MythosMUD. This module contains handlers for status… (+4 more)

### Community 699 - "ProfessionService"
Cohesion: 0.21
Nodes (8): ProfessionService, Any, Service class for profession-related business operations., Initialize the profession service with a persistence layer., Convert a Profession model to a dictionary for API responses. Args: profession:…, Get all available professions as dictionaries. Returns: list[dict[str, Any]]:…, Get a profession by ID as a dictionary. Args: profession_id: Profession ID…, Validate that a profession exists and return it. This method encapsulates the…

### Community 700 - "ContainerFactoryOptions"
Cohesion: 0.18
Nodes (9): ContainerFactoryOptions, datetime, TypedDict, UUID, Check if container has decayed (for corpse containers)., Factory method to create an environmental container., Factory method to create a wearable equipment container., Factory method to create a corpse container. (+1 more)

### Community 701 - "get_room_environment"
Cohesion: 0.12
Nodes (14): Test get_room_environment() treats empty string as no environment., Test get_room_environment() function., Test get_room_environment() returns room-specific environment., Test get_room_environment() returns subzone environment when room doesn't have…, Test get_room_environment() returns zone environment when room and subzone…, Test get_room_environment() returns default 'outdoors' when no environment…, Test get_room_environment() prioritizes room environment over subzone and zone., Test get_room_environment() prioritizes subzone environment over zone. (+6 more)

### Community 702 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 703 - "designTokens.ts"
Cohesion: 0.15
Nodes (19): animations, borderRadius, breakpoints, buildClasses, ButtonVariant, colors, ColorVariant, ComponentSize (+11 more)

### Community 704 - "executeCommand"
Cohesion: 0.09
Nodes (45): expectWhoListingOnPage(), nudgeStandBothPlayers(), nudgeStandBothPlayers(), nudgeStandBothPlayers(), nudgeStandBothPlayers(), assertNeitherPlayerInVoid(), attemptEastHop(), bringFrontAndAssertPlayerBanner() (+37 more)

### Community 705 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 706 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test cleanup_orphaned_data() cleans up orphaned data., Test cleanup_dead_connections() cleans up dead websocket connections., Test cleanup_orphaned_data() closes stale active connections., Test check_and_cleanup() no-ops when memory monitor does not request cleanup., Test force_cleanup() performs forced cleanup., Test check_and_cleanup() performs cleanup check., test_check_and_cleanup() (+5 more)

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
Cohesion: 0.10
Nodes (19): F-String Logging Anti-Pattern, Code Review Import Analysis, isort Import Grouping, Relative vs Absolute Import Policy, Audit date, Code as Source of Truth, Documentation vs. Code Accuracy Audit Log, Summary (+11 more)

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
Nodes (20): Command Handler Patterns, Command Models Reference, Command Security Guide, Command Testing Guide, NATS Subject Pattern Management, Game Subsystem Design Documents Overview, Admin Commands Subsystem Design, Combat Subsystem Design (+12 more)

### Community 717 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 718 - "properties"
Cohesion: 0.15
Nodes (13): minLength, type, minLength, pattern, type, minLength, type, type (+5 more)

### Community 719 - "audit_suppressions.py"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 720 - "fix_markdown_line_length.py"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 721 - "populate_npc_sample_data.py"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 722 - "field_validator"
Cohesion: 0.18
Nodes (6): field_validator, Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation.

### Community 723 - "MemoryMonitor"
Cohesion: 0.04
Nodes (79): Return the live singleton without constructing one., AllocSiteSample, _append_sample_jsonl(), _as_int(), collect_idle_memory_sample(), ConnectionStatsSnapshot, _container_instance(), _event_bus_queue_depth() (+71 more)

### Community 724 - "test_lucidity_command_disruption.py"
Cohesion: 0.16
Nodes (19): can_perform_action(), get_misfire_message(), Command disruption utilities for lucidity system. Implements command misfires…, Check if a command should misfire based on tier and command type. Args:…, Get the misfire message for a failed command. Args: command_type: Type of…, Check if player should involuntarily flee. Args: tier: Current lucidity tier…, Check if player can perform actions (motor lock check). Args: tier: Current…, should_involuntary_flee() (+11 more)

### Community 725 - "test_exploration_procedures.py"
Cohesion: 0.25
Nodes (20): player_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/exploration.sql (#633). Replaces raw SQL…, A third room at the source room's exact coordinates conflicts with it -- one… (+12 more)

### Community 726 - "test_mp_regeneration_service.py"
Cohesion: 0.03
Nodes (76): MPRegenerationService, Any, UUID, MP regeneration service for passive and active magic point recovery. This…, Get MP regeneration multiplier based on player state. Args: stats: Player stats…, # TODO: Check status effects for meditation when status effect system supports…, Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…, # NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per… (+68 more)

### Community 727 - "get_current_tick"
Cohesion: 0.21
Nodes (11): get_current_tick(), Shared game tick counter. Kept in a leaf module so combat services can read the…, Get the current game tick., Set the current game tick (game tick loop)., Reset the current tick for testing., reset_current_tick(), set_current_tick(), Test get_current_tick returns the current tick value. (+3 more)

### Community 728 - "player_effect_repository.py"
Cohesion: 0.05
Nodes (51): _add_effect_params(), AddEffectInput, _int_opt(), _opt_str(), PlayerEffectRepository, Any, TypedDict, UUID (+43 more)

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
Cohesion: 0.18
Nodes (12): Formatter, _PlayerGuidFormatterType, create_formatter(), create_handler_for_category(), Path, RotatingFileHandler, Logger-name categories and per-category file handlers for enhanced logging. The…, Create formatter (with or without PlayerGuidFormatter). (+4 more)

### Community 743 - "strict_mocker"
Cohesion: 0.28
Nodes (8): MockerFixture, Any, fixture, Strict mocking helpers for unit tests. Provides fixtures and helpers that…, Return a patch helper that enables autospec by default. Usage: patched_fn =…, Convenience helper for direct calls with autospec=True by default., strict_mocker(), strict_patch()

### Community 744 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 745 - "UpgradeImplementationPlan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 746 - "_add_profession_lines"
Cohesion: 0.17
Nodes (12): _add_profession_lines(), Add profession information lines to status lines. Args: status_lines: List of…, Test _add_profession_lines() adds profession information., Test _add_profession_lines() does nothing when no profession., test_add_profession_lines(), test_add_profession_lines_no_profession(), Test _add_profession_lines adds profession info when available., Test _add_profession_lines does nothing when no profession name. (+4 more)

### Community 747 - ".accept_party_invite"
Cohesion: 0.20
Nodes (6): Remove expired pending invites and notify inviters., Send a command_response-style message to a single player., Send party_invite event to the target player only., Create a pending party invite and send party_invite event to target. Target…, Accept a party invite. Target is the player who accepted (the invitee)., Decline a party invite.

### Community 748 - "TargetMatch"
Cohesion: 0.04
Nodes (94): Resolve a typed target match for the given name in the current context., Get spell from registry by ID or name., Validate spell can be cast and resolve target., Handle instant cast (casting_time == 0)., Start delayed cast (casting_time > 0)., Resolve spell from registry and validate casting/target. Returns (spell,…, Run instant cast or start delayed cast; send healing event for instant heal…, _coerce_effect_int() (+86 more)

### Community 749 - "MessageBroker"
Cohesion: 0.11
Nodes (12): Infrastructure layer for MythosMUD. This package contains abstractions for…, MessageBroker, Any, Protocol, Send a request and wait for a reply (request-reply pattern). Args: subject:…, Protocol defining the message broker interface. This abstract interface allows…, Connect to the message broker. Returns: bool: True if connection successful,…, Disconnect from the message broker. Closes all subscriptions and releases… (+4 more)

### Community 750 - "test_security_headers.py"
Cohesion: 0.05
Nodes (49): MutableHeaders, Any, ASGIApp, Receive, Request, Scope, Send, Backward-compatible dispatch method for BaseHTTPMiddleware interface. This… (+41 more)

### Community 751 - "RoomRepository"
Cohesion: 0.13
Nodes (13): Room repository for async persistence operations. This module provides async…, Repository for room persistence operations. Handles room caching and retrieval.…, Initialize the room repository. Args: room_cache: Shared room cache dictionary, Get a room by ID from cache. Args: room_id: Room identifier Returns: Room |…, List all cached rooms. Returns: list[Room]: List of all rooms Note: This is…, Save a room to the cache. Args: room: Room object to save Note: Rooms are…, Save multiple rooms to the cache. Args: rooms: List of room objects to save…, RoomRepository (+5 more)

### Community 752 - "auth_rate_limit.py"
Cohesion: 0.24
Nodes (11): assert_auth_rate_limit_paths_registered(), _collect_post_paths(), _HasPrefix, _HasRoutes, _IncludedRouterLike, _join_route_path(), FastAPI, Protocol (+3 more)

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

### Community 761 - "resolve_connection_manager"
Cohesion: 0.21
Nodes (11): Typed wrapper; utils stays free of ConnectionManager imports (import cycles)., resolve_connection_manager(), _coerce_connection_manager(), _ensure_async_compat(), _make_async_compat_wrapper(), Utility functions and module-level code for ConnectionManager. This module…, Pass-through for container values; typing lives at call sites., Wrap a sync or async callable so callers can always await it. (+3 more)

### Community 762 - "compilerOptions"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 763 - "ADR-020: WebSocket Authentication and CSRF"
Cohesion: 0.15
Nodes (11): PostgreSQL Procedures and Functions README, ADR-003: Dual Event Systems (EventBus + NATS), ADR-015: PostgreSQL Procedures and Functions for Data Access, ADR-020: WebSocket Authentication and CSRF, 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered (+3 more)

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

### Community 770 - ".get_data_provider"
Cohesion: 0.17
Nodes (8): Validate that player and NPC are in the same room., Log when a player targets an NPC that exists but is not alive., Return data provider dependency., Validate NPC instance (lookup when missing). Return instance or None., _warn_attacked_dead_npc(), Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Test is_valid_room_id() validates room ID format., test_is_valid_room_id()

### Community 771 - "test_ascii_map_renderer_grid.py"
Cohesion: 0.17
Nodes (10): fixture, Unit tests for AsciiMapRenderer grid building. Guards against regressions in…, Return a fresh AsciiMapRenderer instance for each test., Tests for _build_grid player marker when multiple rooms share coordinates., Multiple rooms at same (x,y): cell keeps player marker even if player room is…, render_map covers empty map, styles, exits, and row rendering., renderer(), test_determine_map_style_and_symbols() (+2 more)

### Community 772 - "PartyService"
Cohesion: 0.14
Nodes (21): PartyUpdated, Event fired when party membership or leadership changes. Emitted by…, PartyService, Party service for MythosMUD. In-memory ephemeral party state: parties exist…, In-memory party management: create, disband, add/remove/kick members, leader…, event_bus(), party_events(), party_service() (+13 more)

### Community 773 - "room_hierarchy_schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, anyOf, description, description, exits, id, name, required (+3 more)

### Community 774 - "schedule_end_combat_if_npc_died_best_effort"
Cohesion: 0.31
Nodes (8): Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…, schedule_end_combat_if_npc_died_best_effort(), patch, Unit tests for best-effort NPC combat cleanup scheduling., When combat service is missing, scheduling is a no-op., Without a running asyncio loop, scheduling fails quietly (RuntimeError path)., test_schedule_end_combat_if_npc_died_no_running_loop(), test_schedule_end_combat_if_npc_died_no_service()

### Community 775 - "CoordinateValidator"
Cohesion: 0.14
Nodes (14): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate…, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:…, _zone_pattern() (+6 more)

### Community 776 - "test_hallucination_services.py"
Cohesion: 0.09
Nodes (31): HallucinationFrequencyService, Any, AsyncSession, UUID, Check if hallucination should trigger on room entry (Uneasy tier). Args:…, Check if hallucination should trigger based on time (Fractured/Deranged tiers).…, Service for managing hallucination frequency checks based on player tier., Initialize the hallucination frequency service. (+23 more)

### Community 777 - "enum"
Cohesion: 0.17
Nodes (12): default, description, enum, type, arena, indoors, intersection, outdoors (+4 more)

### Community 778 - "FakeHallucinationService"
Cohesion: 0.10
Nodes (29): FakeHallucinationService, Select which type of fake hallucination to trigger (50/50 chance). Returns:…, Service for generating fake NPC tells and room text overlays. These…, Initialize the fake hallucination service., Send a hallucination event to a player., send_hallucination_event(), handle_fake_hallucination(), handle_hallucination_triggers() (+21 more)

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

### Community 798 - "ItemInstance"
Cohesion: 0.24
Nodes (8): ItemInstance, Any, Item instance model for runtime item representation. This module defines the…, Runtime representation of an item created from a prototype., Convert the instance into an inventory stack payload understood by legacy…, Unit tests for ItemInstance model., test_item_instance_to_inventory_stack_includes_optional_fields(), test_item_instance_to_inventory_stack_minimal()

### Community 799 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., party_invite producer emits a build_event-shaped envelope., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success() (+3 more)

### Community 800 - "test_nats_retry_handler.py"
Cohesion: 0.04
Nodes (67): Exception, Determine if a message should be retried. Args: message: Message that failed…, Message that can be retried with tracking metadata. Stores message data along…, Get current retry configuration. Returns: Current RetryConfig AI: Useful for…, Configuration for retry behavior. Defines retry parameters for handling…, Calculate delay for a given attempt number. Uses exponential backoff capped at…, Initialize retry handler. Args: max_retries: Maximum number of retry attempts…, RetryableMessage (+59 more)

### Community 801 - "is_player_in_grace_period"
Cohesion: 0.11
Nodes (22): is_player_in_grace_period(), Check if a player is currently in grace period. Args: player_id: The player's…, _apply_grace_badges(), format_occupant_display_name(), _parse_occupant_player_id(), Any, UUID, Shared occupant display names for look text and Occupants panel events. (+14 more)

### Community 802 - "PassiveFluxContext"
Cohesion: 0.13
Nodes (16): FluxServiceConfig, lookup_profile(), period_label(), datetime, Configuration and normalization for passive lucidity flux., Optional configuration for PassiveLucidityFluxService. All fields have defaults., Return a coarse period label used for environment profiles., Look up flux value from profile by period. (+8 more)

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

### Community 807 - "rules"
Cohesion: 0.08
Nodes (25): entry, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries, dependencies (+17 more)

### Community 808 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 809 - "commandStore.ts"
Cohesion: 0.16
Nodes (15): CommandActions, CommandAlias, CommandHistoryEntry, CommandSelectors, CommandState, CommandStore, CommandStoreGet, CommandStoreSet (+7 more)

### Community 810 - "setup.ts"
Cohesion: 0.16
Nodes (6): createDomPurifyTestWindow(), installDomPurifyTestWindow(), defaultFetchMock, installLocalStorageShim(), isUsableStorage(), peekExistingLocalStorage()

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

### Community 824 - "_get_lifecycle_manager"
Cohesion: 0.20
Nodes (10): _get_lifecycle_manager(), _get_npcs_in_room(), Get the lifecycle manager from the NPC instance service., Get list of NPC names in a room from lifecycle manager., Test getting lifecycle manager successfully., Test getting lifecycle manager when service not available., Test getting lifecycle manager when lifecycle_manager not available., test_get_lifecycle_manager_no_lifecycle_manager() (+2 more)

### Community 825 - "asyncio"
Cohesion: 0.14
Nodes (17): PartyChannelStrategy, Strategy for party channel broadcasting. Delivers only to current party members., asyncio, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() sends personal message., Test WhisperChannelStrategy.broadcast() handles missing target_player_id. (+9 more)

### Community 826 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 827 - "._load_player_mutes_from_data"
Cohesion: 0.22
Nodes (5): Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory., Load channel mutes from JSON data into memory., Load global mutes from JSON data into memory.

### Community 828 - "test_player_repository.py"
Cohesion: 0.04
Nodes (68): _make_mock_row(), mock_player(), player_repository(), asyncio, fixture, UUID, Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes with room cache. (+60 more)

### Community 829 - "test_player_spell_repository.py"
Cohesion: 0.33
Nodes (14): _mock_session_with_rows(), asyncio, Unit tests for PlayerSpellRepository., _spell_row(), test_get_player_spell_found(), test_get_player_spell_missing(), test_get_player_spells(), test_get_player_spells_db_error() (+6 more)

### Community 830 - "_FakeMessageQueue"
Cohesion: 0.20
Nodes (3): _FakeMessageQueue, _FakeRateLimiter, _FakeRoomManager

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

### Community 839 - "map/types.ts"
Cohesion: 0.14
Nodes (29): HistoryEntry, MapEditingChanges, useMapEditing(), UseMapEditingOptions, UseMapEditingResult, UseMapLayoutResult, useRoomMapEditorEditing(), ExitEdge (+21 more)

### Community 840 - "TestResolveExitTarget"
Cohesion: 0.20
Nodes (6): Room without a reverse exit is not considered bidirectional., If the target room ID does not exist, the helper returns None., If the target room lacks map coordinates, the helper returns None., Tests for _resolve_exit_target., Room with a reverse exit is treated as bidirectional and returns its…, TestResolveExitTarget

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

### Community 847 - "._resolve_context_async"
Cohesion: 0.21
Nodes (11): _as_float(), _as_str_attr(), FluxRoom, _profile_map(), datetime, Protocol, Look up base_flux and profile_source from room overrides. Returns (base_flux,…, Resolve environmental context for passive flux evaluation using cached room. (+3 more)

### Community 848 - "TestHorizontalExitCharBetween"
Cohesion: 0.20
Nodes (6): Tests for _horizontal_exit_char_between (em dash, >, <)., Bidirectional horizontal exit between two rooms uses an em dash., One-way east exit renders as a greater-than sign., One-way west exit renders as a less-than sign., When there are no horizontal exits, the helper returns None., TestHorizontalExitCharBetween

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

### Community 855 - ".create_lie_command"
Cohesion: 0.20
Nodes (9): Test create_lie_command() creates LieCommand., Test create_lie_command() with 'down' modifier., Test create_lie_command() raises error with invalid args., Test create_lie_command() raises error with multiple args., test_create_lie_command(), test_create_lie_command_with_down(), test_create_lie_command_with_invalid_args(), test_create_lie_command_with_multiple_args() (+1 more)

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

### Community 861 - "CircuitBreaker"
Cohesion: 0.04
Nodes (75): CircuitBreaker, CircuitBreakerOpen, CircuitState, Any, Enum, Exception, timedelta, Circuit breaker pattern for NATS message processing. Implements three-state… (+67 more)

### Community 862 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 863 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 864 - "populate_test_npc_databases.py"
Cohesion: 0.31
Nodes (8): get_npc_data_from_source(), get_npc_database_url(), main(), populate_database(), Populate a PostgreSQL database with NPC data. Args: target_url: PostgreSQL…, Main function to populate test NPC databases., Get NPC database URL for the specified environment. Args: environment:…, Extract NPC data from the source PostgreSQL database. Args: source_url:…

### Community 865 - "api/conftest.py"
Cohesion: 0.17
Nodes (15): mock_connection_manager(), mock_container(), mock_container_service(), mock_persistence(), mock_player(), mock_request(), mock_user(), fixture (+7 more)

### Community 866 - "._connect_nats"
Cohesion: 0.25
Nodes (5): BaseException, Raise RuntimeError when e2e requires live NATS; no-op for other environments., Convert connect failures into hard error (e2e) or soft log (other envs)., Handle connect() returning False; raise for e2e, soft-warn otherwise., Connect to NATS if enabled and not unit_test. Returns NATSService or None.…

### Community 867 - ".optimize_payload"
Cohesion: 0.28
Nodes (5): Any, Create an incremental update payload containing only changed fields. Args:…, Calculate the size of a payload in bytes. Args: payload: The payload dictionary…, Compress a large payload using gzip compression. Args: payload: The payload…, Optimize a payload by applying size limits and compression if needed. Args:…

### Community 868 - "add_default_combat_data_to_config"
Cohesion: 0.22
Nodes (9): add_default_combat_data_to_config(), get_combat_stats_summary(), Any, Add default combat data to behavior_config if not present. Args: config:…, Get a summary of combat stats for an NPC definition. Args: npc_definition:…, Test add_default_combat_data_to_config() adds defaults., Test get_combat_stats_summary() returns summary., test_add_default_combat_data_to_config() (+1 more)

### Community 870 - "test_combat_messaging_integration.py"
Cohesion: 0.04
Nodes (57): messaging_integration(), mock_connection_manager(), asyncio, fixture, Unit tests for combat messaging integration. Tests the…, Test broadcast_player_mortally_wounded broadcasts message., Test broadcast_player_died broadcasts death message., Test broadcast_player_mortally_wounded with attacker name. (+49 more)

### Community 871 - "RoomDataCache"
Cohesion: 0.04
Nodes (39): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Manages room data caching and freshness validation., Check if new data is newer than old data for a specific key. Args: old_data:…, Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,… (+31 more)

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

### Community 877 - "RoomInfo.tsx"
Cohesion: 0.29
Nodes (13): CompleteRoomInfo(), DebugInfo(), RoomDescription(), RoomEntities(), RoomExits(), RoomInfo(), RoomInfoContext, RoomInfoContextType (+5 more)

### Community 878 - "MessageBatcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 879 - "._get_vertical_exit_char"
Cohesion: 0.22
Nodes (6): _ExitRowContext, NamedTuple, Render a single row of vertical exits between room rows., Viewport and style context for vertical exit row rendering., Return the vertical exit character (|, v, or ^) given south/north exit state,…, Get exit character to display between rows for vertical (north/south) exits.…

### Community 880 - "server/tests/conftest.py"
Cohesion: 0.10
Nodes (28): Config, Item, _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables(), _get_db_name_from_url(), AbstractEventLoop (+20 more)

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

### Community 891 - "format_combat_status"
Cohesion: 0.16
Nodes (14): format_combat_status(), get_combat_target(), Any, Produce a human-readable combat status string. This helper is retained for…, Resolve a combat target by name. The current implementation is intentionally…, Unit tests for combat command helper functions. Tests helper functions in…, Test format_combat_status() formats combat status., Test format_combat_status() handles player not in combat. (+6 more)

### Community 892 - "test_look_item.py"
Cohesion: 0.09
Nodes (27): _get_item_description_from_prototype(), Get item description from prototype registry. Returns: Formatted result string…, Unit tests for item look functionality. Tests the helper functions for looking…, Test finding item in equipped items by name., Test finding item in equipped items when not found., Test getting item description from prototype., Test getting item description when prototype registry is None., Test getting item description when prototype_id is missing. (+19 more)

### Community 893 - "rest_countdown_task.py"
Cohesion: 0.24
Nodes (14): create_rest_countdown_task(), _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, Task, UUID, Rest countdown task implementation. This module contains the async task that… (+6 more)

### Community 894 - "Motion Design"
Cohesion: 0.25
Nodes (8): Duration: The 100/300/500 Rule, Easing: Pick the Right Curve, Motion Design, Perceived Performance, Performance, Reduced Motion, Staggered Animations, The Only Two Properties You Should Animate

### Community 895 - "Profession"
Cohesion: 0.03
Nodes (71): Profession, Any, Base, Check if given stats meet the profession requirements. Args: stats: Dictionary…, Check if profession is available for player selection., Get formatted text for displaying stat requirements. Returns: Formatted string…, Profession model for game data. Stores profession information including name,…, String representation of the profession. (+63 more)

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
Cohesion: 0.30
Nodes (14): invite_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/players.sql's #633 additions:…, Create one user with a mixed-case username. Yields (user_id, username). (+6 more)

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
Cohesion: 0.13
Nodes (14): Cards Are Not Required, Container Queries, Depth & Elevation, Grid Systems, Hierarchy Through Multiple Dimensions, Name Tokens Semantically, Optical Adjustments, Spacing Systems (+6 more)

### Community 912 - "Typography"
Cohesion: 0.13
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
Cohesion: 0.15
Nodes (12): Claims by cluster, config-api — API_OPENAPI_SPECIFICATION, container-di — BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES, container-di — CONTAINER_SYSTEM_ARCHITECTURE, Corpus correction, Design↔design contradictions (findings without needing code), domain — aggro-threat-system, events-nats — EVENT_OWNERSHIP_MATRIX, DISTRIBUTED_EVENTBUS_NATS, NATS_SUBJECT_PATTERNS (+4 more)

### Community 920 - "P4 · Intent Sweep — Core Feature Issues"
Cohesion: 0.13
Nodes (14): #17 · Party — one of three bullets built, #21 · Admin commands — "ban" was in the issue title and never built, #29 · Cultist faction and PvP — zero implementation, #30 · Branching quests and morality — two of three bullets absent, #62 · Tick-rate validation — not built, #9 · The xterm.js substitution — real, user-facing, unrecorded, CLOSED BUT NOT BUILT, Conforming, worth recording (+6 more)

### Community 921 - "Decisions required"
Cohesion: 0.09
Nodes (20): F-D3 · Inbound links to archived documents — DEVIATED (7 instances, one root cause), F-D5 · The DI system's architecture doc is archived, not live — DEVIATED, F-D6 · `docs/DEVELOPMENT_AI.md` is not valid text — DEVIATED, F-V1 · Sync PersistenceLayer removal — CONFORMS (reverses a P0 row), F-V2 · sqlite3 imports survive in migration scripts — STALE, P3 · Findings Verified Directly, A · Hard-coded metrics in documents, B · Migration scaffolding that outlived its migration (+12 more)

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
Cohesion: 0.07
Nodes (17): ChatPoseManager, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…, Get a player's current pose. Args: player_id: ID of the player Returns: Current…, Clear a player's pose. Args: player_id: ID of the player Returns: True if pose…, Get all poses (for testing/debugging). Returns: Dictionary mapping player IDs… (+9 more)

### Community 934 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 935 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.20
Nodes (13): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Unit tests for channel broadcasting strategies. Tests the…, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…, Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., Test ChannelBroadcastingStrategyFactory.get_strategy() returns…, Test ChannelBroadcastingStrategyFactory.register_strategy() registers new…, Test global channel_strategy_factory instance exists. (+5 more)

### Community 936 - "_EventPersistence"
Cohesion: 0.24
Nodes (6): _EventPersistence, _Named, _NatsPublish, Protocol, UUID, Initialize EventPublisher service. Args: nats_service: NATS service instance…

### Community 937 - "normalize_path_from_url_or_path"
Cohesion: 0.25
Nodes (6): Path, Return and cache the repository root directory., Delegate to shared util. Kept for backward compatibility., normalize_path_from_url_or_path(), Path, Normalize an item database override into a filesystem path. DEPRECATED: Items…

### Community 938 - "test_profession_service.py"
Cohesion: 0.25
Nodes (13): persistence(), _profession(), asyncio, fixture, Unit tests for ProfessionService., service(), test_get_all_professions_dict(), test_get_profession_by_id_dict_found() (+5 more)

### Community 939 - "RateLimiter"
Cohesion: 0.13
Nodes (12): test_auth_rate_limit_response_returns_429_when_exceeded(), fixture, rate_limiter(), Create a RateLimiter instance for testing., Utility modules for MythosMUD server. This package contains various utility…, Any, RateLimiter, Enforce rate limiting for a user. Args: user_id: The user's ID Raises:… (+4 more)

### Community 940 - "connection_state_machine.py"
Cohesion: 0.29
Nodes (7): ConnectionEvent, Enum, Connection state machine for NATS messaging. Implements a robust state machine…, Events that trigger state transitions. AI: Explicit events make the FSM…, Test ConnectionEvent enum values., test_connection_event_enum(), StateMachine

### Community 941 - "test_persistence_container_persistence.py"
Cohesion: 0.14
Nodes (13): Unit tests for persistence.container_persistence module. This module tests the…, Test parsing None JSONB column., Test parsing string JSONB column., Test parsing dict JSONB column., Test parsing empty string JSONB column., Test parsing list JSONB column., Test parsing invalid JSON string., test_parse_jsonb_column_dict() (+5 more)

### Community 942 - ".check_and_cleanup"
Cohesion: 0.25
Nodes (6): Stale-prune threshold (seconds). Higher in e2e/local to avoid mid-run drops., Force immediate cleanup of all orphaned data. Args: cleanup_stats: Cleanup…, Periodically check for cleanup conditions and perform cleanup if needed. Args:…, _stale_prune_max_age_seconds(), Test _stale_prune_max_age_seconds uses longer threshold in local env., test_stale_prune_max_age_local()

### Community 943 - "._filter_active_players"
Cohesion: 0.29
Nodes (4): Parse last_active from various formats., Normalize datetime to timezone-aware UTC., Check if player is active based on last_active and created_at., Filter players to only those active in the last 5 minutes.

### Community 944 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 945 - ".validate_room_consistency"
Cohesion: 0.25
Nodes (6): Check if occupant count matches the actual occupants list length. Args:…, Validate room data consistency. Args: room_data: Room data to validate for…, Test validate_room_consistency() validates room consistency., Test check_occupant_count_consistency() detects mismatches., test_check_occupant_count_consistency(), test_validate_room_consistency()

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

### Community 950 - ".create_go_command"
Cohesion: 0.25
Nodes (7): Test create_go_command() creates GoCommand., Test create_go_command() raises error with no args., Test create_go_command() raises error with invalid direction., test_create_go_command(), test_create_go_command_invalid_direction(), test_create_go_command_no_args(), Create GoCommand from arguments.

### Community 951 - ".create_ground_command"
Cohesion: 0.25
Nodes (7): Test create_ground_command() creates GroundCommand., Test create_ground_command() raises error with no args., Test create_ground_command() raises error with empty target., test_create_ground_command(), test_create_ground_command_empty_target(), test_create_ground_command_no_args(), Create GroundCommand from arguments.

### Community 953 - ".create_follow_command"
Cohesion: 0.25
Nodes (7): Test create_follow_command() creates FollowCommand with target., Test create_follow_command() raises error with no args., Test create_follow_command() raises error with empty target., test_create_follow_command(), test_create_follow_command_empty_target(), test_create_follow_command_no_args(), Create FollowCommand from arguments.

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

### Community 967 - ".create_alias_command"
Cohesion: 0.25
Nodes (7): Test create_alias_command() creates AliasCommand., Test create_alias_command() raises error with no args., Test create_alias_command() with only alias name., test_create_alias_command(), test_create_alias_command_no_args(), test_create_alias_command_no_command(), Create AliasCommand from arguments.

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

### Community 973 - "run_quality_fragmentation_guard.py"
Cohesion: 0.31
Nodes (12): _argv_char_len(), _build_guard_command(), _changed_files_between(), _git_executable(), _is_graphify_path(), _local_changed_files(), main(), Path (+4 more)

### Community 974 - ".create_learn_command"
Cohesion: 0.25
Nodes (7): Test create_learn_command() creates LearnCommand., Test create_learn_command() raises error with no args., Test create_learn_command() with multi-word spell name., test_create_learn_command(), test_create_learn_command_multi_word(), test_create_learn_command_no_args(), Create LearnCommand from arguments.

### Community 975 - "test_look_npc_helpers.py"
Cohesion: 0.08
Nodes (27): _get_npc_room_id(), Get the room ID from an NPC instance, checking both current_room and…, Unit tests for look_npc helper functions. Tests the helper functions in…, Test _format_other_stats() returns empty list when no other stats., Test _format_lifecycle_info() formats lifecycle information., Test _format_lifecycle_info() returns empty list when no lifecycle_state., Test _get_npc_room_id() returns current_room_id when available., Test _get_npc_room_id() returns current_room when current_room_id is None. (+19 more)

### Community 976 - "_utc_now"
Cohesion: 0.21
Nodes (12): datetime, Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE…, _utc_now(), Unit tests for lucidity model utility functions. Tests the _utc_now utility…, Test _utc_now returns a datetime object., Test _utc_now returns naive datetime (tzinfo=None)., Test _utc_now returns time close to current UTC time., Test _utc_now returns different times on subsequent calls. (+4 more)

### Community 977 - ".create_unalias_command"
Cohesion: 0.25
Nodes (7): Test create_unalias_command() creates UnaliasCommand., Test create_unalias_command() raises error with no args., Test create_unalias_command() raises error with multiple args., test_create_unalias_command(), test_create_unalias_command_multiple_args(), test_create_unalias_command_no_args(), Create UnaliasCommand from arguments.

### Community 978 - "player_repository_mappers.py"
Cohesion: 0.19
Nodes (12): _coerce_row_stats(), _defaulted_numerics(), _defaulted_strings(), InventoryPayload, _parse_equipped_safely(), Any, Row-to-player mapping utilities for PlayerRepository. Maps procedure result…, Type hint for inventory payload structure. (+4 more)

### Community 979 - "channel_broadcasting_strategies.py"
Cohesion: 0.21
Nodes (10): ChannelBroadcastingStrategy, GlobalChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for whisper channel broadcasting., Abstract base class for channel broadcasting strategies., Initialize the strategy factory., Register a new strategy for a channel type. Args: channel_type: Channel type to… (+2 more)

### Community 980 - "optimized_comprehensive_sanitize_input"
Cohesion: 0.25
Nodes (8): Test comprehensive sanitization of empty string., Test comprehensive sanitization of normal text., Test that optimized comprehensive sanitization normalizes newlines to spaces., test_optimized_comprehensive_sanitize_input_empty(), test_optimized_comprehensive_sanitize_input_normal(), test_optimized_comprehensive_sanitize_input_normalizes_newlines(), optimized_comprehensive_sanitize_input(), Optimized comprehensive input sanitization. Args: text: Raw input text to…

### Community 981 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 982 - "properties"
Cohesion: 0.25
Nodes (8): description, enum, type, indoors, outdoors, underwater, properties, environment

### Community 983 - "verify_npc_occupants.py"
Cohesion: 0.23
Nodes (12): _check_service_availability(), _collect_npcs_by_room(), _print_summary(), Any, Verification script to check NPCs in lifecycle manager and test occupant query…, Print verification summary. Args: npc_count: Total number of active NPCs…, Verify NPCs exist in lifecycle manager and test query logic., Check if NPC service, lifecycle manager, and active_npcs are available.… (+4 more)

### Community 984 - "logger.test.ts"
Cohesion: 0.29
Nodes (6): mockAppendChild, mockClick, mockConsole, mockCreateElement, mockCreateObjectURL, mockRemoveChild

### Community 985 - "test_async_persistence_room_cache.py"
Cohesion: 0.04
Nodes (60): asyncio, Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test get_user_by_username_case_insensitive when no session is yielded., Test get_professions when no session is yielded., Test get_players_batch with empty list., Test get_players_batch with actual players (UUID conversion)., Test _generate_room_id_from_zone_data when stable_id already has full path., Test _generate_room_id_from_zone_data when room ID needs generation. (+52 more)

### Community 987 - "test_player_event_handlers_utils.py"
Cohesion: 0.02
Nodes (91): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), asyncio, fixture, Unit tests for player event handler utilities. Tests the…, Test get_player_info() returns None for invalid player_id. (+83 more)

### Community 988 - "test_room_subscription_manager.py"
Cohesion: 0.04
Nodes (53): asyncio, fixture, Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test add_room_occupant() adds occupant., Test add_room_occupant() with multiple occupants., Test add_room_occupant() adds occupant to new room. (+45 more)

### Community 989 - "test_run_test_ci.py"
Cohesion: 0.19
Nodes (12): Regression tests for scripts/run_test_ci.py's coverage-combine sequence and the…, Run 1 (the main suite) must write to a COVERAGE_FILE distinct from the bare…, Run 1's safe_run_static call must pass env=env_unit, not the base env (which…, The `coverage combine` call's two data-file arguments must be coverage_unit and…, ci.yml's 'Check for excessive warnings' step re-runs the suite under -n auto;…, ci.yml's 'Run tests with coverage' step pipes through `tee`; without pipefail…, _script_source(), test_combine_call_never_targets_the_bare_coverage_file() (+4 more)

### Community 990 - "test_combat_service_npc_in_combat.py"
Cohesion: 0.15
Nodes (12): combat_service(), fixture, Unit tests for CombatService.is_npc_in_combat_sync. Tests the NPC-in-combat…, Create CombatService with mocked dependencies so is_npc_in_combat_sync can be…, Test is_npc_in_combat_sync returns False when NPC is not in any combat., Test is_npc_in_combat_sync returns True when NPC UUID is in _npc_combats., Test is_npc_in_combat_sync returns False for non-UUID string when no mapping., Test is_npc_in_combat_sync returns True when integration service maps string id… (+4 more)

### Community 991 - "test_room_environment_parity.py"
Cohesion: 0.19
Nodes (12): _environment_enum_from_schema(), _environment_options_from_room_edit_modal(), Path, Parity test for the room environment enum (#623). Guards against the exact…, Return the `environment` property's `enum` values from a room JSON schema., Return the non-empty `value`s of RoomEditModal.tsx's ENVIRONMENT_OPTIONS…, room_hierarchy_schema.json's environment enum must equal ROOM_ENVIRONMENTS., unified_room_schema.json's environment enum must equal ROOM_ENVIRONMENTS. (+4 more)

### Community 992 - "_RoomBroadcaster"
Cohesion: 0.29
Nodes (6): _EventSequence, Protocol, Sequence counter surface used by build_event., Connection manager surface used to fan out posture events., Send event to occupants of room_id., _RoomBroadcaster

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

### Community 1018 - "grype.py"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1019 - "lint_container_get_instance.py"
Cohesion: 0.21
Nodes (11): AllowlistEntry, _collect_python_files(), _find_get_instance_lines(), main(), Path, Guard against new `ApplicationContainer.get_instance()` service-location debt…, Return 1-based line numbers of real `ApplicationContainer.get_instance()`…, Scan server/ for ApplicationContainer.get_instance() calls. Returns… (+3 more)

### Community 1020 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 1021 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1022 - ".validate_alias_name_field"
Cohesion: 0.29
Nodes (4): field_validator, Validate alias name format using centralized validation., Validate command content for security using centralized validation., Validate alias name format using centralized validation.

### Community 1023 - "handle_unequip_command"
Cohesion: 0.29
Nodes (16): handle_unequip_command(), CommandResponse, Player, Unequip an item into the player's inventory., _unequip_persist_or_rollback(), _unequip_run_mutation(), _unequip_success_payload(), _mutation_cm() (+8 more)

### Community 1024 - "mock_connection_manager"
Cohesion: 0.29
Nodes (7): mock_connection_manager(), mock_persistence(), mock_request(), fixture, Create a mock ConnectionManager., Create a mock persistence layer., Create a mock FastAPI request.

### Community 1025 - "SkillUseLog"
Cohesion: 0.21
Nodes (10): Base, One recorded successful use of a skill by a character at a given level.…, SkillUseLog, Unit tests for SkillUseLog ORM model., SkillUseLog can be instantiated with required fields., SkillUseLog maps to the expected table., SkillUseLog __repr__ includes key identifiers., test_skill_use_log_creation() (+2 more)

### Community 1026 - "quest_service"
Cohesion: 0.29
Nodes (7): mock_def_repo(), mock_instance_repo(), fixture, quest_service(), QuestService with mocked repos., Mock QuestDefinitionRepository., Mock QuestInstanceRepository.

### Community 1027 - "message_broadcaster"
Cohesion: 0.29
Nodes (7): message_broadcaster(), mock_room_manager(), mock_send_personal_message(), fixture, Create a mock room manager., Create a mock send_personal_message callback., Create a MessageBroadcaster instance.

### Community 1028 - ".generate_fake_npc_tell"
Cohesion: 0.40
Nodes (4): Any, UUID, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will…

### Community 1029 - "room_validator/schemas/unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 1030 - "subzone_with_override"
Cohesion: 0.31
Nodes (10): async_sessionmaker, asyncio, AsyncSession, fixture, A zone with special_rules set, and a subzone under it with special_rules NULL…, A zone with NO override, and a subzone under it WITH special_rules set. Yields…, subzone_with_override(), test_get_lucidity_rate_overrides_includes_subzone_row() (+2 more)

### Community 1031 - "MagicPointsMeter.tsx"
Cohesion: 0.53
Nodes (4): formatDelta(), MagicPointsMeter, MagicPointsMeterProps, MagicPointsStatus

### Community 1032 - "test_game_enums.py"
Cohesion: 0.14
Nodes (13): Unit tests for game model enums. Tests AttributeType, StatusEffectType, and…, Test PositionState enum contains all expected states., Test AttributeType enum contains expected values., Test AttributeType enum contains all expected types., Test StatusEffectType enum contains expected values., Test StatusEffectType enum contains all expected types., Test PositionState enum contains expected values., test_attribute_type_enum_all_types() (+5 more)

### Community 1033 - "test_monitoring_init.py"
Cohesion: 0.17
Nodes (11): Unit tests for server.monitoring lazy __getattr__ re-exports., Exception tracker symbols import without triggering numpy lazy paths., __getattr__ resolves MonitoringDashboard and get_monitoring_dashboard., __getattr__ resolves PerformanceStats and get_performance_monitor., Unknown attribute names raise AttributeError., Direct __getattr__ covers both branch returns for dashboard imports., test_monitoring_eager_imports(), test_monitoring_getattr_direct_call() (+3 more)

### Community 1036 - "_errors_len"
Cohesion: 0.17
Nodes (12): _errors_len(), Test _spawn_required_npcs() handles missing spawn room., Narrow spawn/startup result dict for len(results['errors']) without propagating…, Test _spawn_required_npcs() handles exceptions during spawning., Test _spawn_optional_npcs() handles exceptions during spawning., Test spawn_npcs_on_startup() handles exceptions during session processing., Test spawn_npcs_on_startup() handles critical exceptions., test_spawn_npcs_on_startup_critical_exception() (+4 more)

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

### Community 1042 - "GridLayoutManager.tsx"
Cohesion: 0.20
Nodes (5): GridLayoutManager(), GridLayoutManagerProps, layoutConfig, PanelComponent, ResponsiveGridLayout

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

### Community 1072 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

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

### Community 1077 - "ConfigurationError"
Cohesion: 0.33
Nodes (6): ConfigurationError, Configuration and setup errors., Test ConfigurationError can be instantiated., test_configuration_error(), Test ConfigurationError initialization., test_configuration_error_initialization()

### Community 1078 - ".format"
Cohesion: 0.33
Nodes (4): _canonical_ip(), LogRecord, Format a log record with enhanced player GUID display. Args: record: The log…, Convert player GUIDs in message to enhanced format. Args: message: The log…

### Community 1079 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 1080 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.22
Nodes (9): 10. Final Verification, 5. Test Environment Setup, 6. Quality Assurance Checklist, 8. Error Handling and Debugging, Common Debug Commands, Environment Variables, REQUIRED TOOL USAGE PATTERN, Test Configuration (+1 more)

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
Cohesion: 0.36
Nodes (7): initialize_components(), Any, Prepare component state metadata for a new item instance. This routine…, Unit tests for item component hooks., test_initialize_components_empty_prototype(), test_initialize_components_merges_overrides(), test_initialize_components_records_prototype_components()

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

### Community 1112 - "holiday_row"
Cohesion: 0.43
Nodes (8): holiday_row(), npc_schedule_row(), async_sessionmaker, asyncio, AsyncSession, fixture, test_get_calendar_holidays_includes_the_new_row(), test_get_calendar_npc_schedules_includes_the_new_row()

### Community 1113 - "test_emotes_procedures.py"
Cohesion: 0.31
Nodes (9): emote_row(), async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/emotes.sql (#633). Replace raw SQL…, Create one emote with one alias. Yields (stable_id, alias)., test_get_emote_aliases_joins_owning_emote() (+1 more)

### Community 1114 - "test_npcs_zone_config_procedures.py"
Cohesion: 0.31
Nodes (9): async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/npcs.sql's zone/subzone config read…, Create one zone and one subzone with unique stable_ids. Yields (zone_stable_id,…, test_get_subzone_configs_joins_parent_zone(), test_get_zone_configs_includes_the_zone() (+1 more)

### Community 1115 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _build_room_objects logs debug info for specific room., Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., test_build_room_objects_debug_logging(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

### Community 1116 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 1117 - "add_default_combat_data_to_stats"
Cohesion: 0.33
Nodes (6): add_default_combat_data_to_stats(), Add default combat data to base_stats if not present. Args: stats: Base stats…, Test add_default_combat_data_to_stats() preserves existing values., Test add_default_combat_data_to_stats() adds defaults., test_add_default_combat_data_to_stats(), test_add_default_combat_data_to_stats_preserves_existing()

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

### Community 1141 - ".check_duplicate_occupants"
Cohesion: 0.33
Nodes (5): Check for duplicate occupants in the room. Args: room_data: Room data to check…, Test check_duplicate_occupants() detects duplicates., Test check_duplicate_occupants() passes when no duplicates., test_check_duplicate_occupants(), test_check_duplicate_occupants_no_duplicates()

### Community 1142 - "days"
Cohesion: 0.22
Nodes (10): items, items, minItems, type, items, type, pattern, type (+2 more)

### Community 1143 - "mock_persistence"
Cohesion: 0.33
Nodes (6): mock_persistence(), mock_request(), mock_user(), fixture, Create a mock request object., Create a mock persistence layer.

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

### Community 1152 - "mock_persistence"
Cohesion: 0.33
Nodes (6): mock_persistence(), mock_request(), mock_user(), fixture, Create a mock request object., Create a mock persistence layer.

### Community 1153 - "test_inventory_service_helpers.py"
Cohesion: 0.28
Nodes (8): Clear lazy singletons so each test gets a fresh init path. For unit tests only;…, reset_shared_inventory_services_for_tests(), fixture, Unit tests for inventory_service_helpers.get_shared_services., _request_with_persistence(), reset_shared_inventory_services_autouse(), test_get_shared_services_initializes_and_reuses_singletons(), test_get_shared_services_raises_without_async_persistence()

### Community 1154 - "TestValidateUserForOpenContainer"
Cohesion: 0.33
Nodes (4): Test validate_user_for_open_container function., Test validate_user_for_open_container passes with valid user., Test validate_user_for_open_container raises exception for None user., TestValidateUserForOpenContainer

### Community 1155 - "TestValidateUserForTransfer"
Cohesion: 0.33
Nodes (4): Test validate_user_for_transfer function., Test validate_user_for_transfer passes with valid user., Test validate_user_for_transfer raises exception for None user., TestValidateUserForTransfer

### Community 1156 - "TestValidateUserForCloseContainer"
Cohesion: 0.33
Nodes (4): Test validate_user_for_close_container function., Test validate_user_for_close_container passes with valid user., Test validate_user_for_close_container raises exception for None user., TestValidateUserForCloseContainer

### Community 1157 - "player_inventory_migration.py"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1158 - "TestValidateUserForLootAll"
Cohesion: 0.33
Nodes (4): Test validate_user_for_loot_all function., Test validate_user_for_loot_all passes with valid user., Test validate_user_for_loot_all raises exception for None user., TestValidateUserForLootAll

### Community 1159 - "fixture"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request object., Create a mock persistence layer., Create a mock connection manager. (+1 more)

### Community 1160 - "TestGetRoomService"
Cohesion: 0.33
Nodes (4): Tests for get_room_service dependency function., Test get_room_service returns service when present., Test get_room_service raises RuntimeError when service is None., TestGetRoomService

### Community 1161 - "test_utility_commands_whoami.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for utility command handlers. Tests the whoami command functionality., Test handle_whoami_command() returns player information., Test handle_whoami_command() handles missing persistence., Test handle_whoami_command() handles player not found., test_handle_whoami_command(), test_handle_whoami_command_no_persistence(), test_handle_whoami_command_player_not_found()

### Community 1162 - "TestGetPlayerDeathService"
Cohesion: 0.33
Nodes (4): Tests for get_player_death_service dependency function., Test get_player_death_service returns service when present., Test get_player_death_service raises RuntimeError when service is None., TestGetPlayerDeathService

### Community 1163 - "TestGetMagicService"
Cohesion: 0.33
Nodes (4): Tests for get_magic_service dependency function., Test get_magic_service returns service when present., Test get_magic_service raises RuntimeError when service is None., TestGetMagicService

### Community 1164 - "TestGetSpellLearningService"
Cohesion: 0.33
Nodes (4): Tests for get_spell_learning_service dependency function., Test get_spell_learning_service returns service when present., Test get_spell_learning_service raises RuntimeError when service is None., TestGetSpellLearningService

### Community 1165 - "TestGetMPRegenerationService"
Cohesion: 0.33
Nodes (4): Tests for get_mp_regeneration_service dependency function., Test get_mp_regeneration_service returns service when present., Test get_mp_regeneration_service raises RuntimeError when service is None., TestGetMPRegenerationService

### Community 1166 - "test_room_subscription_manager_drops.py"
Cohesion: 0.03
Nodes (64): fixture, Unit tests for room subscription manager drop functions. Tests the room drop…, Test adjust_room_drop() returns False for invalid index., Test list_room_drops() returns room drops., Test add_room_drop() adds drop to new room., Test add_room_drop() adds drop to existing room., Test take_room_drop() successfully takes drop., Test take_room_drop() with index out of range. (+56 more)

### Community 1167 - "TestGetNPCSpawningService"
Cohesion: 0.33
Nodes (4): Tests for get_npc_spawning_service dependency function., Test get_npc_spawning_service returns service when present., Test get_npc_spawning_service raises RuntimeError when service is None., TestGetNPCSpawningService

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

### Community 1204 - "TestGetNPCPopulationController"
Cohesion: 0.33
Nodes (4): Tests for get_npc_population_controller dependency function., Test get_npc_population_controller returns service when present., Test get_npc_population_controller raises RuntimeError when service is None., TestGetNPCPopulationController

### Community 1205 - "UnknownChannelStrategy"
Cohesion: 0.25
Nodes (6): Strategy for unknown channel types., Initialize unknown channel strategy. Args: channel_type: Unknown channel type, Get strategy for channel type. Args: channel_type: Type of channel to get…, UnknownChannelStrategy, Test UnknownChannelStrategy.broadcast() handles unknown channel., test_unknown_channel_strategy_broadcast()

### Community 1206 - "SystemAdminChannelStrategy"
Cohesion: 0.25
Nodes (7): Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy. Args: channel_type: Type of…, SystemAdminChannelStrategy, Test SystemAdminChannelStrategy.broadcast() broadcasts globally., Personal system messages deliver to target_player_id only., test_system_admin_channel_strategy_broadcast(), test_system_admin_channel_strategy_personal_target()

### Community 1207 - "RoomBasedChannelStrategy"
Cohesion: 0.25
Nodes (7): Strategy for room-based channels (say, local, emote, pose)., Initialize room-based channel strategy. Args: channel_type: Type of room-based…, RoomBasedChannelStrategy, Test RoomBasedChannelStrategy.broadcast() broadcasts to room., Test RoomBasedChannelStrategy.broadcast() handles missing room_id., test_room_based_channel_strategy_broadcast(), test_room_based_channel_strategy_broadcast_no_room_id()

### Community 1208 - "TestGetMythosTimeConsumer"
Cohesion: 0.33
Nodes (4): Tests for get_mythos_time_consumer dependency function., Test get_mythos_time_consumer returns service when present., Test get_mythos_time_consumer raises RuntimeError when service is None., TestGetMythosTimeConsumer

### Community 1209 - "test_event_publisher_init_with_initial_sequence"
Cohesion: 0.20
Nodes (6): Test EventPublisher initialization with initial sequence., #679: async_persistence is injected at construction (no container lookup at all…, Test EventPublisher initialization., test_event_publisher_init(), test_event_publisher_init_with_initial_sequence(), test_get_async_persistence_returns_none_when_unset()

### Community 1210 - "_FakeEstablishmentManager"
Cohesion: 0.20
Nodes (4): _FakeEstablishmentManager, _FakePerformanceTracker, _FakeRoomManager, Typed stand-in for ConnectionManager; MagicMock attributes are Any.

### Community 1211 - ".create_sit_command"
Cohesion: 0.33
Nodes (5): Test create_sit_command() creates SitCommand., Test create_sit_command() raises error with args., test_create_sit_command(), test_create_sit_command_with_args(), Create SitCommand from arguments.

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

### Community 1219 - ".create_stand_command"
Cohesion: 0.33
Nodes (5): Test create_stand_command() creates StandCommand., Test create_stand_command() raises error with args., test_create_stand_command(), test_create_stand_command_with_args(), Create StandCommand from arguments.

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

### Community 1236 - ".create_unfollow_command"
Cohesion: 0.33
Nodes (5): Test create_unfollow_command() creates UnfollowCommand with no args., Test create_unfollow_command() raises error with args., test_create_unfollow_command(), test_create_unfollow_command_with_args(), Create UnfollowCommand from arguments.

### Community 1237 - ".create_goto_command"
Cohesion: 0.33
Nodes (5): Test create_goto_command() creates GotoCommand., Test create_goto_command() raises error with no args., test_create_goto_command(), test_create_goto_command_no_args(), Create GotoCommand from arguments.

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

### Community 1249 - ".create_shutdown_command"
Cohesion: 0.33
Nodes (5): Test create_shutdown_command() creates ShutdownCommand., Test create_shutdown_command() with args., test_create_shutdown_command(), test_create_shutdown_command_with_args(), Create ShutdownCommand from arguments. Args can be: - Empty: Default 10 second…

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

### Community 1254 - ".create_spells_command"
Cohesion: 0.33
Nodes (5): Test create_spells_command() creates SpellsCommand., Test create_spells_command() raises error with args., test_create_spells_command(), test_create_spells_command_with_args(), Create SpellsCommand from arguments.

### Community 1255 - ".create_aliases_command"
Cohesion: 0.33
Nodes (5): Test create_aliases_command() creates AliasesCommand., Test create_aliases_command() raises error with args., test_create_aliases_command(), test_create_aliases_command_with_args(), Create AliasesCommand from arguments.

### Community 1256 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1257 - ".create_help_command"
Cohesion: 0.33
Nodes (5): Test create_help_command() creates HelpCommand., Test create_help_command() creates HelpCommand with no topic., test_create_help_command(), test_create_help_command_no_args(), Create HelpCommand from arguments.

### Community 1258 - ".create_npc_command"
Cohesion: 0.33
Nodes (5): Test create_npc_command() with no args., Test create_npc_command() with subcommand., test_create_npc_command_no_args(), test_create_npc_command_with_subcommand(), Create NPCCommand from arguments.

### Community 1259 - ".validate_timestamp"
Cohesion: 0.29
Nodes (4): field_validator, Validate event type is not empty., Validate timestamp is valid ISO format., Validate channel is a known chat channel.

### Community 1260 - "3. Systematic Investigation Approach"
Cohesion: 0.40
Nodes (5): 3. Systematic Investigation Approach, For Authentication Failures, For Database-Related Failures, For Game Logic Failures, For WebSocket Failures

### Community 1261 - "mythos_dev.npc_definitions"
Cohesion: 0.50
Nodes (5): mythos_dev.dialogue_definitions, mythos_dev.get_npc_system_statistics(), mythos_dev.npc_definitions, mythos_dev.npc_relationships, mythos_dev.npc_spawn_rules

### Community 1263 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 1265 - "mock_event_bus"
Cohesion: 0.40
Nodes (5): mock_event_bus(), mock_persistence(), fixture, Create a mock persistence layer., Create a mock event bus.

### Community 1266 - "event_publisher"
Cohesion: 0.29
Nodes (7): event_publisher(), mock_nats_service(), mock_subject_manager(), fixture, Create a mock NATS service., Create a mock subject manager., Create an EventPublisher instance.

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

### Community 1294 - "Enhanced Logging System Implementation Guide"
Cohesion: 0.40
Nodes (6): MythosMUD Development Environment Setup, MythosMUD AI Agent Development Guide, E2E Testing Guide, Enhanced Logging System Implementation Guide, Error Handling Guide, Error Logging Implementation Guide

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

### Community 1310 - "._get_player_mute_file"
Cohesion: 0.40
Nodes (3): Path, Get the mute data file path for a specific player., Initialize the user manager. Args: data_dir: Directory for player-specific mute…

### Community 1311 - "mock_container"
Cohesion: 0.40
Nodes (5): mock_container(), mock_request(), fixture, Create a mock FastAPI Request with app.state.container., Get the container from mock_request.

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
Nodes (4): downgrade(), Create player_effects table and indexes (ADR-009 effects system)., Drop player_effects table and indexes., upgrade()

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

### Community 1365 - "DomainError"
Cohesion: 0.40
Nodes (4): DomainError, Exception, Domain-specific exceptions for MythosMUD. These exceptions represent business…, Base exception for all domain errors.

### Community 1366 - "._error_callback"
Cohesion: 0.50
Nodes (3): Exception, Handle NATS errors. AI: Runs as fire-and-forget async task to prevent blocking…, Async handler for NATS connection errors.

### Community 1367 - "test_command_player_state.py"
Cohesion: 0.06
Nodes (47): GroundCommand, LieCommand, LogoutCommand, field_validator, QuitCommand, Player state command models for MythosMUD. This module provides command models…, Command for quitting the game., Command for logging out of the game. (+39 more)

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

### Community 1375 - "nats_broker"
Cohesion: 0.40
Nodes (5): nats_broker(), nats_config(), fixture, Create a NATSConfig instance., Create a NATSMessageBroker instance.

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
Cohesion: 0.50
Nodes (4): mythos_dev.id_map_players, mythos_dev.invites, mythos_dev.muting_rules, mythos_dev.users

### Community 1382 - "rate_limiter"
Cohesion: 0.40
Nodes (5): mock_config(), fixture, rate_limiter(), Create a mock config with chat rate limits., Create a RateLimiter instance with mocked config.

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

### Community 1443 - "Bounded Contexts and Service Boundaries"
Cohesion: 0.50
Nodes (4): Bounded Contexts and Service Boundaries, ConnectionManager Modular Architecture, Container System API Reference, Container System Architecture

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

### Community 1465 - "setup_jwt_secret"
Cohesion: 0.50
Nodes (4): fixture, MonkeyPatch, Set JWT secret for tests., setup_jwt_secret()

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

### Community 1475 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 1476 - ".__init__"
Cohesion: 0.50
Nodes (3): LevelUpHook, Any, Initialize the level service. Args: async_persistence: Async persistence for…

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

### Community 1511 - "ADR-002: ApplicationContainer for Dependency Injection"
Cohesion: 1.00
Nodes (3): ADR-002: ApplicationContainer for Dependency Injection, Container Injection Audit, Database Access Patterns

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

### Community 1556 - "end_hour"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 1557 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 1558 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

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

### Community 1568 - "mock_send_game_event"
Cohesion: 0.67
Nodes (3): mock_send_game_event(), fixture, Create a mock send_game_event function.

### Community 1569 - "npc_startup_service"
Cohesion: 0.67
Nodes (3): npc_startup_service(), fixture, Create an NPCStartupService instance.

### Community 1570 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1571 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1573 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1574 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1575 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1591 - ".check_empty_room_with_occupants"
Cohesion: 0.50
Nodes (3): Check if room has occupants but no name. Args: room_data: Room data to check…, Test check_empty_room_with_occupants() detects empty room with occupants., test_check_empty_room_with_occupants()

### Community 1592 - "TestGetContainerService"
Cohesion: 0.50
Nodes (3): Test get_container_service function., Test get_container_service returns ContainerService instance., TestGetContainerService

### Community 1593 - "test_validate_secure_path_path_traversal_commonpath"
Cohesion: 0.33
Nodes (4): Test validate_secure_path normalizes backslashes., Test validate_secure_path detects path traversal via commonpath check., test_validate_secure_path_path_traversal_commonpath(), test_validate_secure_path_with_backslash()

### Community 1594 - "Lucidity.md"
Cohesion: 0.24
Nodes (5): Lucidity, Pandora's Box (Pulp campaign), Using Luck (Pulp), Key extrated pages, Pulp Sanity

### Community 1685 - "mock_connection_manager"
Cohesion: 0.50
Nodes (4): mock_connection_manager(), mock_player(), fixture, Create mock connection manager.

### Community 1686 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1687 - "name"
Cohesion: 0.50
Nodes (4): description, minLength, type, name

### Community 1689 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1690 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

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

### Community 1713 - "applies_to"
Cohesion: 0.67
Nodes (3): minItems, type, applies_to

### Community 1714 - "metadata"
Cohesion: 0.67
Nodes (3): additionalProperties, type, metadata

### Community 1715 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1719 - "_MigrationArgs"
Cohesion: 0.67
Nodes (3): _MigrationArgs, Protocol, argparse namespace for this script.

### Community 1720 - "_format_liabilities"
Cohesion: 0.67
Nodes (3): _format_liabilities(), LiabilityStackEntry, Flatten liability entries into human-readable strings for the client.

### Community 1722 - "mock_connection_manager"
Cohesion: 0.67
Nodes (3): mock_connection_manager(), fixture, Create a mock ConnectionManager.

### Community 1723 - "_iter_exception_chain"
Cohesion: 0.67
Nodes (3): _iter_exception_chain(), BaseException, Walk __cause__/__context__ without looping.

## Knowledge Gaps
- **6194 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `JCODEMUNCH_MAX_FOLDER_FILES`, `@codacy/codacy-mcp` (+6189 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **448 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `models/player.py`, `PlayerLeftRoom`, `NPCBase`, `npc_database.py`, `DatabaseError`, `server/dependencies.py`, `ValidationError`, `ContainerComponent`, `api/character_creation.py`, `container_events.py`, `CombatParticipant`, `connection_manager_methods.py`, `get_npc_instance_service`, `players.py`, `combat_turn_participant_actions.py`, `inventory_equip_command.py`, `test_container_persistence_async_helpers.py`, `AliasStorage`, `ComprehensiveLoggingMiddleware`, `AsyncPersistenceLayer`, `persistence/container_helpers.py`, `inventory_command_helpers.py`, `container_endpoints_basic.py`, `test_combat_event_publisher.py`, `SpellEffects`, `PlayerNameExtractor`, `CombatParticipantData`, `ContainerServiceError`, `test_container_bundles.py`, `test_lifecycle_respawn.py`, `get_username_from_user`, `PlayerPositionService`, `test_connection_session_management.py`, `test_connection_establishment.py`, `NATSService`, `NPCStartupService`, `factory.py`, `test_follow_service.py`, `Stats`, `server/services/__init__.py`, `is_player_in_login_grace_period`, `NPCCombatDataProvider`, `NPCDefinition`, `chat_service.py`, `test_npc_definitions_api.py`, `lifespan_magic.py`, `command_handler_unified.py`, `handle_transfer_items_exceptions`, `RoomService`, `test_admin_shutdown_command.py`, `test_chat_pose_helpers.py`, `test_go_command.py`, `MetricsCollector`, `test_users.py`, `extract_player_name`, `CombatInstance`, `combat_service.py`, `communication_commands_flows.py`, `test_look_container_helpers.py`, `event_types.py`, `test_cache_service.py`, `item_instance_persistence_async.py`, `User`, `test_look_helpers.py`, `connection_cleanup_methods.py`, `ContainerData`, `lucidity_migration.py`, `test_websocket_initial_state.py`, `test_chat_npc_system.py`, `test_player_requests.py`, `catatonia_check.py`, `test_aggro_threat.py`, `EventBus`, `utility_commands.py`, `rescue_commands.py`, `NATSSubjectManager`, `DistributedEventBus`, `create_app`, `error_handling_middleware.py`, `BehaviorEngine`, `command_result_text`, `test_combat_monitoring_service.py`, `test_auth_utils.py`, `npc_combat_grace.py`, `build_event`, `real_time.py`, `api/monitoring.py`, `test_player_presence_tracker.py`, `test_look_player.py`, `FeatureFlagService`, `PlayerService`, `test_connection_helpers_impl.py`, `handle_teach_command`, `_handle_admin_set_stat_command`, `player_inventory_migration.py`, `test_metrics_endpoints.py`, `connection_manager.py`, `WebSocketMessageValidator`, `test_magic_commands.py`, `ErrorType`, `NATSRetryHandler`, `migrate_combat_data.py`, `LoggedHTTPException`, `ContainerRepository`, `TaskRegistry`, `DialogueService`, `CombatConfiguration`, `MovementMonitor`, `chat_channel_message_senders.py`, `lifespan_startup.py`, `ExperienceRepository`, `map_minimap.py`, `test_zone_config_loader.py`, `test_lucidity_recovery_commands.py`, `test_quest_events.py`, `Any`, `test_message_handlers.py`, `test_admin_setlucidity_command.py`, `CombatPersistenceHandler`, `test_shutdown_sequence.py`, `apply_communication_dampening`, `NPCLifecycleManager`, `ScheduleService`, `test_database_helpers.py`, `time.py`, `test_player_disconnect_handlers.py`, `status_commands.py`, `middleware`, `test_lucidity_event_dispatcher.py`, `CombatAuditLogger`, `test_wearable_container_service.py`, `system_monitoring.py`, `test_websocket_helpers.py`, `quest_service.py`, `Room`, `RoomEventHandler`, `admin_mute_commands.py`, `LogAggregator`, `.__init__`, `MemoryMonitor`, `test_lucidity_command_disruption.py`, `chat_nats_publisher.py`, `test_mp_regeneration_service.py`, `PerformanceMonitor`, `NPCCombatIntegration`, `player_effect_repository.py`, `lifespan_protocols.py`, `container_query_helpers_async.py`, `test_lifecycle_periodic.py`, `EventHandler`, `CatatoniaRegistry`, `TargetMatch`, `websocket_handler.py`, `RoomRepository`, `session_factory`, `InventorySchemaValidationError`, `NPCOccupantProcessor`, `test_email_utils.py`, `dialogue_definitions_api.py`, `PartyService`, `test_rescue_service.py`, `FakeHallucinationService`, `EnvironmentalContainerLoader`, `models/combat.py`, `test_look_room.py`, `ExceptionTracker`, `get_global_tracked_manager`, `time_event_consumer.py`, `test_rate_overrides.py`, `HealthStatus`, `is_player_in_grace_period`, `MythosTickScheduler`, `logout_commands.py`, `item_instance_persistence.py`, `NATSMessageBroker`, `test_inventory_display_helpers.py`, `handle_read_command`, `debrief_command.py`, `CoordinateGenerator`, `SpellLearningService`, `endpoints.py`, `PrototypeRegistryError`, `.__post_init__`, `test_goto_helpers.py`, `_str_id`, `websocket_handler_commands.py`, `api/player_respawn.py`, `NPCActionMessage`, `test_websocket_handler_coverage_gaps.py`, `CircuitBreaker`, `DialogueDefinitionRepository`, `server/tests/conftest.py`, `SpellMaterialsService`, `retry.py`, `rest_countdown_task.py`, `ErrorContext`, `nats_broker.py`, `get_async_session`, `quest_commands.py`, `resolve_weapon_attack_from_equipped`, `look_command.py`, `inventory_pickup_command.py`, `player_connection_setup.py`, `HolidayService`, `lucidity_trigger_handlers.py`, `equipment_helpers.py`, `pytest.md`, `disconnect_grace_period.py`, `look_npc.py`, `ChatPoseManager`, `connection_state_machine.py`, `MessageBroadcaster`, `spell_effects_support.py`, `ChatModeration`, `PayloadOptimizer`, `test_container_persistence_extended_row_helpers.py`, `channel_broadcasting_strategies.py`, `ConnectionErrorHandler`, `_find_item_in_equipped`, `processing.py`, `who_commands.py`, `PersonalMessageSender`, `test_magic_healing_events.py`, `game_tick_processing.py`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Why does `DatabaseError` connect `DatabaseError` to `models/player.py`, `_as_mgr`, `_handle_admin_set_stat_command`, `test_exceptions_comprehensive.py`, `ValidationError`, `connection_manager.py`, `test_npc_service.py`, `connection_manager_methods.py`, `Player`, `player_connection_setup.py`, `players.py`, `ErrorType`, `test_container_persistence_async_helpers.py`, `test_player_service_mutations.py`, `AliasStorage`, `persistence/container_helpers.py`, `AsyncPersistenceLayer`, `time_event_consumer.py`, `test_profession_repository.py`, `RoomCacheLoader`, `SpellEffects`, `pytest.md`, `test_connection_session_management.py`, `test_retry.py`, `ExperienceRepository`, `PlayerPositionService`, `test_connection_establishment.py`, `item_instance_persistence.py`, `test_admin_setlucidity_command.py`, `test_shutdown_sequence.py`, `canonical_room_id_impl`, `test_admin_summon_command.py`, `test_logging_processors.py`, `asyncio`, `test_exceptions.py`, `NPCDefinition`, `lifespan_magic.py`, `test_player_repository.py`, `test_player_spell_repository.py`, `RoomService`, `ConnectionCleaner`, `test_go_command.py`, `test_container_persistence_extended_crud.py`, `extract_player_name`, `combat_service.py`, `test_container_persistence_extended_row_helpers.py`, `event_types.py`, `admin_mute_commands.py`, `test_admin_commands.py`, `test_emote_repository.py`, `item_instance_persistence_async.py`, `User`, `NPCCombatIntegration`, `ContainerData`, `player_effect_repository.py`, `test_async_persistence_room_loading.py`, `populate_test_npc_databases.py`, `container_query_helpers_async.py`, `rescue_commands.py`, `test_spell_repository.py`, `PersonalMessageSender`, `DialogueDefinitionRepository`, `test_player_presence_tracker.py`, `MythosMUDError`, `test_connection_helpers_impl.py`, `ErrorContext`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Why does `Profession` connect `Profession` to `models/player.py`, `DatabaseError`, `AsyncPersistenceLayer`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._
- **Are the 136 inferred relationships involving `LoggedHTTPException` (e.g. with `test_get_admin_sessions_error()` and `test_get_npc_population_stats_generic_error()`) actually correct?**
  _`LoggedHTTPException` has 136 INFERRED edges - model-reasoned connections that need verification._
- **Are the 192 inferred relationships involving `ValidationError` (e.g. with `fetch_user_by_username_case_insensitive()` and `load_database_url()`) actually correct?**
  _`ValidationError` has 192 INFERRED edges - model-reasoned connections that need verification._
- **Are the 81 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 81 INFERRED edges - model-reasoned connections that need verification._
- **Are the 73 inferred relationships involving `AliasStorage` (e.g. with `_handle_special_command_routing()` and `_prepare_command_for_processing()`) actually correct?**
  _`AliasStorage` has 73 INFERRED edges - model-reasoned connections that need verification._