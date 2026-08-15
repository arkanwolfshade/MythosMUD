# Graph Report - MythosMUD  (2026-08-14)

## Corpus Check
- 3308 files · ~2,954,894 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 53601 nodes · 100724 edges · 2776 communities (1862 shown, 914 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 7361 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7c8e0440`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ConnectionManager
- test_player_respawn_service.py
- TestPlayerNameExtractor
- SpellEffects
- UUID
- BaseCommand
- test_admin_auth_service.py
- test_follow_service.py
- test_connection_delegates.py
- test_auth_utils.py
- test_websocket_handler_app_state_connection.py
- test_exceptions.py
- CombatParticipant
- .get_instance
- test_invite_schemas.py
- CatatoniaRegistry
- NPCCombatIntegrationService
- api/character_creation.py
- test_occupant_formatter.py
- test_container_persistence_async_helpers.py
- GameConfig
- fixtures/unit/__init__.py
- connection_manager_methods.py
- test_admin_shutdown_command.py
- test_nats_message_handler.py
- inventory_item_matching.py
- test_security_validator.py
- ApplicationContainer
- NPCDefinitionCRUDMixin
- TargetMatch
- LoggedHTTPException
- Communities (355 total, 223 thin omitted)
- pydantic.md
- test_command_inventory.py
- test_combat.py
- test_user_manager.py
- test_player_position_service.py
- test_event_publisher_helpers.py
- test_nats_service.py
- NPCMovementIntegration
- LootAllRequest
- test_command_communication.py
- test_connection_cleaner.py
- test_command_processing.py
- test_manager.py
- UtilityCommandFactory
- legacy_error_sanitization.py
- test_container_websocket_events.py
- test_command_factories.py
- MinimapRenderer
- api/monitoring.py
- is_player_in_login_grace_period
- test_dead_letter_queue.py
- NATSConnectionStateMachine
- test_who_commands.py
- test_command_parser.py
- CombatService
- pytest.md
- Stats
- command_handler_unified.py
- _JSONDict
- ContainerComponent
- WebSocket Best Practices
- test_message_queue.py
- Any
- submitAuth.ts
- test_exploration_service.py
- NATSService
- catatonia_check.py
- chat_service.py
- test_database_helpers.py
- ExplorationCommandFactory
- patch
- test_nats_message_handler_subzone_events.py
- HealthStatus
- ChatWhisperTracker
- test_websocket_helpers.py
- _MagicServiceCore
- RoomLoader
- CombatMonitoringService
- Alias
- security.ts
- test_command_validator.py
- test_player_presence_tracker.py
- test_container_helpers_inventory_ops.py
- test_look_player.py
- test_websocket_handler_json_error.py
- test_health_service.py
- TargetResolutionService
- test_logging_utilities.py
- test_lifespan_helpers.py
- ChatService
- npc_admin_mgmt_api.py
- test_combat_monitoring_service.py
- test_npc_combat_integration_service.py
- CorpseOverlay.tsx
- QuestService
- test_npc_definitions_api.py
- test_connection_establishment.py
- _def_row
- test_container_helpers_inventory_find.py
- test_look_room.py
- NATSMetrics
- EldritchIcon.tsx
- CorpseLifecycleService
- Reporter
- executeCommand
- test_database_init.py
- test_rate_limiter_utils.py
- test_websocket_helpers_player.py
- SubjectValidator
- test_inventory_equip_command.py
- combat_service_npc.py
- NPCCommunicationIntegration
- test_rest_command.py
- UserManager
- SchemaValidator
- GameClientV2.tsx
- test_status_commands.py
- TestCombatConfigurationService
- real_time.py
- EventBus
- test_quest_service.py
- test_combat_validator.py
- test_alias_storage.py
- useMythosAppActions.ts
- test_quest_commands.py
- test_websocket_handler_core.py
- test_logging_processors.py
- test_lucidity_recovery_commands.py
- test_channel_broadcasting_strategies.py
- _format_room_posture_message
- test_command_moderation.py
- NATSRetryHandler
- _utc_now
- chat_channel_message_senders.py
- get_logger
- get_username_from_user
- test_nats_broker.py
- .load_room_data
- test_validation.py
- test_chat_service.py
- SpellEffectType
- test_lifecycle_periodic.py
- test_debrief_command.py
- item_instance_persistence_async.py
- log_with_context
- persistence/container_persistence.py
- server/schemas/__init__.py
- test_connection_session_management.py
- test_player_combat_service.py
- useRespawnHandlers.ts
- test_active_lucidity_service.py
- test_player_disconnect_handlers.py
- test_websocket_handler_helpers_extended.py
- quest_commands.py
- test_aggro_threat.py
- test_combat_service.py
- test_combat_attack_handler.py
- test_admin_commands.py
- ContainerService
- test_player_service.py
- test_combat_handler.py
- test_admin_setlucidity_command.py
- RoomIDUtils
- HealthService
- RoomService
- get_admin_auth_service
- test_go_command.py
- coerce_int
- PlayerRoomEventHandler
- CombatAuditLogger
- CombatInstance
- test_logging_handlers.py
- test_alias_commands.py
- test_combat_flee_helpers.py
- MonitoringDashboard
- test_lucidity_event_dispatcher.py
- MagicServiceHealingMixin
- test_room_renderer.py
- test_level_service.py
- test_party_service.py
- LRUCache
- MemoryMonitor
- test_hallucination_services.py
- monitoring_models.py
- test_metrics.py
- test_player_event_handlers_utils.py
- fixtures/auth.ts
- test_websocket_handler_coverage_gaps.py
- realtime/realtime.py
- server/persistence/__init__.py
- ChatHistoryPanel.tsx
- .__post_init__
- test_config_init.py
- test_logout_commands.py
- ExceptionTracker
- test_combat_messaging_integration.py
- test_target_resolution_service.py
- manual_dependency_analysis.py
- middleware
- communication_commands_flows.py
- test_nats_messages.py
- test_player_schema_converter_weapon.py
- test_character_creation_service.py
- Player
- test_connection_helpers_impl.py
- NATSMessageSubscriptionMixin
- test_room_subscription_manager_drops.py
- test_command_admin.py
- test_communication_commands_flows.py
- dialogue_definitions_api.py
- test_player_occupant_processor.py
- LogAggregator
- test_mp_regeneration_service.py
- test_admin_setstat_command.py
- ui-v2/types.ts
- test_command_alias.py
- SpellLearningService
- test_inventory_helpers_extended.py
- NPCCombatUUIDMapping
- MythosChronicle
- roomHandlers.ts
- Argon2 Password Hashing Best Practices
- test_websocket_messages.py
- TauntCommandHandler
- ContainerRepository
- Pre-commit Hooks Best Practices
- devDependencies
- useGameClientV2ContainerRefsAndBootstrap.ts
- test_game_tick_processing.py
- PlayerStateCommandFactory
- RoomDataCache
- PlayerGuidFormatter
- test_player_model.py
- errorHandler.ts
- Any
- test_player_service_mutations.py
- GameTickService
- TestMonitoringEndpoints
- gameStore.ts
- logging_file_setup.py
- gen_arena_migration_sql.py
- AdminActionsLogger
- look_command.py
- PrototypeRegistryError
- PostgreSQL Best Practices
- IdleMovementHandler
- useAsciiMapState.ts
- resolve_weapon_attack_from_equipped
- test_security_headers.py
- test_command_magic.py
- Structured Logging with Structlog Best Practices
- Uvicorn ASGI Server Best Practices
- CommunicationCommandFactory
- PartyService
- test_movement_service.py
- test_windows_safe_rotation.py
- test_movement_monitor.py
- test_rate_limiter.py
- CharacterSelectionScreen.tsx
- communication_commands.py
- test_chat_nats_publisher.py
- UUID
- NPCCombatLucidity
- asyncio
- ResourceManager
- testing_examples.py
- PlayerNameExtractor
- message_handler_factory.py
- test_container_persistence_extended_parse.py
- test_look_item.py
- nats_service.py
- chatPanelRuntimeUtils.ts
- apiTypeGuards.ts
- MemoryMonitor
- ScheduleEntry
- react Best Practices
- test_rest_and_grace_period.py
- ModerationCommandFactory
- lucidity.ts
- MagicServiceCompletionMixin
- alias_schema.json
- test_zone_configuration.py
- TestRoomDataFixer
- test_connection_statistics.py
- test_admin_commands_helpers.py
- WebSocketMessageValidator
- test_inventory_display_helpers.py
- handle_read_command
- NATSSubscribeError
- test_admin_summon_command.py
- test_memory_leak_metrics.py
- container_endpoints_basic.py
- edgeModalLogic.ts
- test_command_parser_helpers.py
- test_config_model_helpers.py
- RoomEventHandler
- test_pattern_matcher.py
- admin_shutdown_command.py
- test_npc_event_handlers_helpers.py
- StyleGuideSections.tsx
- npc_database.py
- test_npc_combat_handlers.py
- Any
- test_goto_helpers.py
- github-actions Best Practices
- RoomDataValidator
- NPCCombatIntegration
- App.tsx
- useDraggablePanelInteractions.ts
- fixtures/integration/__init__.py
- TestHolidayService
- PassiveMobNPC
- canonical_room_id_impl
- TargetResolutionResult
- collect_inventory.py
- deleteCharacterFlow.ts
- NATSMessageBroadcastMixin
- verify_enhanced_logging_compliance.py
- projectorRoom.ts
- character-cleanup.ts
- deque
- TestNPCCombatLifecycle
- compare_linting_results.py
- 3. Common Patterns and Anti-patterns
- NATSSubjectManager
- handle_whisper_command
- CoordinateGenerator
- Test Suite Refactoring Plan
- HolidayCollection
- test_chat_npc_system.py
- test_chat_logger.py
- test_room_utils.py
- HealthRepository
- HolidayEntry
- ChatLogger
- _find_item_in_equipped
- test_audit_logger.py
- ContainerTransferFromMixin
- test_look_container.py
- GameLogPanel.tsx
- RoomMapEditorRuntime.hooks.ts
- types/mythosTime.ts
- TypeScript Best Practices
- setup.ts
- asyncio
- spell_effect_types.py
- vite Best Practices
- ConnectionCleaner
- Lint Remediation
- vim Best Practices and Coding Standards
- E2E Test Suite AI Execution Improvements - Summary
- test_connection_event_helpers.py
- connection_cleanup_methods.py
- click Best Practices
- _find_item_in_inventory
- 2. Type Hinting Best Practices
- DistributedEventBus
- MythosPanel.tsx
- useGameTerminal.ts
- GameStateProvider
- test_admin_teleport_commands.py
- connection_manager_health_cleanup.py
- PerformanceMonitor
- WearableContainerService
- ConnectionErrorHandler
- .check_bidirectional_connections
- SQLAlchemy Best Practices (2.x Style)
- Uplift Strategy
- test_quest_instance_repository.py
- CastingStateManager
- PydanticErrorHandler
- NPCCombatIntegrationBase
- DialogueDefinitionRepository
- test_look_helpers.py
- TestHierarchicalSchema
- GameClientV2ContainerView.tsx
- utils/layout.ts
- player.ts
- FastAPI Code Review - Anti-Patterns and Best Practices
- 🧪 MythosMUD E2E Testing Strategy
- subject_controller.py
- Any
- combat_attack.py
- NPCCacheService
- test_magic_service.py
- NPCCombatDataProvider
- test_player_related_models.py
- test_async_persistence_core.py
- pylint Best Practices
- test_message_broadcaster.py
- TestNPCCombatRewards
- Memory Leak Prevention System - Implementation Summary
- deprecated_patterns.py
- TaskRegistry
- useMythosAppState.ts
- TestCombatMessagingService
- Phase 1: Core Separation
- MythosMUD Test Writing
- test_connection_initialization.py
- NATSPublishError
- Phase 2: Enhanced Features
- CombatCommandHandler
- log_exception_once
- player_connection_setup.py
- CommandPanel.tsx
- WebSocketRequestContext
- test_command_helpers.py
- test_room_subscription_manager_helpers.py
- UUID
- schemas/unified_room_schema.json
- Chat Panel Separation Implementation Tasks
- Async Persistence Migration Plan
- test_combat_persistence_handler.py
- NATSMessageBroker
- test_lucidity_repository.py
- test_population_stats.py
- test_message_handlers.py
- test_container_persistence.py
- test_health_monitor.py
- test_dependency_analysis.py
- test_combat_persistence_handler_persistence.py
- PlayerRespawnWrapper
- test_lucidity_trigger_handlers.py
- useRoomEditModal.ts
- NATS Complete Remediation Summary
- PostgreSQL & SQL Audit Report
- Critical Coverage Gaps
- Phase 3, Task 3.2: NATS Subject Manager Usage Review
- Execution Steps
- properties
- enum
- properties
- test_game_tick_processing_async.py
- ValidationError
- RoomCacheService
- pytest Best Practices
- MemoryProfiler
- authenticated.ts
- fastapi_integration.py
- migration_examples.py
- InventoryMutationGuard
- properties
- safe_run_static
- NATSConfig
- CombatCommandFactory
- ChatMessage
- test_npc_threading_messages.py
- PostgresConnection
- Fix patterns by tier
- game_tick_processing.py
- stateNormalization.ts
- File-by-File Changes
- Coverage Improvement Summary - Plan 2 Execution
- Memory Leak Audit Report
- CacheManager
- ProfessionCacheService
- test_inventory_get_command.py
- MovementMonitor
- test_player_preferences_service.py
- Lint Remediation
- logger.ts
- NATS Anti-Patterns and Best Practices Review
- Persistence Layer Refactoring - COMPLETE ✅
- Persistence Layer Refactoring Summary
- Test Pruning Candidates - Detailed List
- required
- test_lucidity_command_disruption.py
- Path
- StatusEffect
- panelReducerHandlers.ts
- DialogueService
- PlayerRepositoryProtocol
- TestPostgresConnectionPool
- .to_dict
- e2e-bootstrap.ts
- MemoryThresholdMonitor
- properties
- FStringLoggingFixer
- Stop-MythosMudProjectProcessTree
- spell_effects_status.py
- test_statistics_aggregator.py
- container_query_helpers_async.py
- Client Test Remediation
- Phase 3: Polish and Optimization
- Phase 4: Testing and Refinement
- PlayerPreferencesService
- disconnect_grace_period.py
- performance.test.tsx
- multiplayer-browser-helpers.js
- Client Test Remediation
- Async Audit Executive Summary
- PARALLEL EXECUTION RESULTS (2025-11-05)
- _collect_python_public_defs_and_tiny
- TestLogoutCommand
- test_admin_permission_utils.py
- ChatModeration
- test_npc_combat_integration_service_player_attacks.py
- test_combat_persistence_handler_events.py
- PickupTestWiring
- test_party_commands.py
- properties
- Pydantic Code Review - feature/sqlite-to-postgresql Branch
- test_passive_lucidity_flux_service.py
- Prometheus Configuration
- PeriodicOrphanAuditor
- test_item.py
- load_world_seed.py
- validate.py
- ReactNodeUpgradeAnalyzer
- UUID
- UserManagerProtocol
- NPCStartupService
- _NPCCombatIntegrationValidationDeps
- PatternNotFoundError
- test_shutdown_sequence.py
- test_room_occupant_manager.py
- docker Best Practices
- test_inventory_mutation_guard.py
- RoomInfoPanel.tsx
- test_combat_service_modules.py
- test_optimized_security_validator.py
- properties
- Any
- scripts
- RoomMapEditorRuntime.tsx
- container_query_helpers.py
- ensurePlayableConnection
- test_channel_commands.py
- AnyIO vs Asyncio: High-Level Comparison and Decision Guide
- Complexity Checking Alignment: Ruff C901 vs Pylint
- WebSocket Code Review - Branch: feature/sqlite-to-postgresql
- LucidityFluxService
- properties
- CORSConfig
- test_chat_pose_helpers.py
- test_quest_definition_repository.py
- test_chat_moderation.py
- NPCCombatIntegrationReadApi
- equipment_helpers.py
- MythosMUD Database Placement
- debugLogger
- test_logger
- AnyIO Code Review - Anti-Patterns and Issues
- 🎯 Async Remediation - Final Report
- NATS Code Review - Branch: feature/sqlite-to-postgresql
- Persistence Layer Extraction - COMPLETE ✅
- 🔴 CRITICAL ISSUES
- asyncio
- log_and_raise
- Protocol
- get_shared_services
- OccupantFormatter
- extract_player_name
- RateLimiter
- Bug Investigator Subagent
- MonitoringPanel.tsx
- asyncio
- .create_combat_instance
- 3. REFACTOR Findings (935 findings)
- ErrorMonitor
- verify_linting_parity.py
- MythosTickScheduler
- test_connection_manager_api.py
- test_npc_spawn_rules_api.py
- InventorySchemaValidationError
- test_security_utils.py
- test_shutdown_process_termination.py
- handle_command
- .perform_recovery_action
- NPCOccupantProcessor
- SkillUseLog
- test_quest_service_collect.py
- NPCActionMessage
- .create_instance
- AliasGraph
- .change_position
- Communities (19 total, 4 thin omitted)
- properties
- Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch
- test_error_handling_middleware.py
- LogAnalyzer
- test_look_item_helpers.py
- test_npc_combat_integration_service_npc_aggro.py
- test_lru_cache.py
- attach_compatibility_properties
- room_hierarchy_schema.json
- test_combat_death_handler.py
- Codacy Rules
- test_player_event_handlers_room_left.py
- GameTerminal.tsx
- Migration Strategy
- Async Facades Implementation - COMPLETE ✅
- Migration 019: Complete Implementation Summary
- CombatEventHandler
- test_load_world_seed.py
- ._build_player_attacked_event
- Vitest Best Practices
- zustand Best Practices
- test_time_bundle.py
- asyncio
- test_behavior_engine.py
- channel_broadcasting_strategies.py
- test_quality_fragmentation_guard.py
- dependencies
- normalize_environment
- messageHandlers.ts
- FeedbackManager
- Feature Requirements Document: Random Stats Generator
- Migration 019 Verification Report
- Phase 4: Recommendations
- test_retry.py
- send_system_message
- LucidityRepository
- fix_fstring_logging.py
- TestRunner
- SkillAssignmentScreen.tsx
- establish_websocket_connection
- seed_e2e_users.py
- client/package.json
- Playwright Best Practices
- test_inventory_mutation_guard_internal.py
- StatisticsAggregator
- designTokens.ts
- test_event_bus.py
- Recommended Test Additions
- test_async_persistence_room_loading.py
- AggressiveMobNPC
- get_cached_player
- cached
- ValidationRule
- SQLAlchemyAsyncLinter
- Test Suite Analyzer Subagent
- Onboard Skill
- utils/config.ts
- test_database_config_helpers_asyncpg_settings.py
- properties
- ContainerRepository and ItemRepository: Review and Full Async Migration Plan
- Dependency Upgrade Strategy Specification
- Documentation Updates - ConnectionManager Refactoring
- Domain Model Anemic Anti-Pattern Audit
- Test Coverage Summary: Disconnect Grace Period & Rest Command
- format_markdown_file
- migrate_rooms.py
- handle_emote_command
- MessageBroadcaster
- EnvironmentalContainerLoader
- InviteManager
- PlayerOccupantProcessor
- PostgresRow
- .rescue
- ItemPrototypeModel
- ChatPanel
- _NPCCombatIntegrationDeps
- enum
- test_shopkeeper_npc.py
- EventPublisher
- CombatDeathHandler
- PanelState
- .claude/hooks/record_edited_file.py
- EdgeDetailsPanel.tsx
- .cursor/hooks/record_edited_file.py
- MUD Disconnect Grace Period & Rest Command: Industry Comparison
- test_npc_event_handlers.py
- Code Review: Import Analysis and Anti-Patterns
- MythosMUD Dependency Upgrade Strategy - Implementation Summary
- compilerOptions
- Execution Steps
- Execution Steps
- generate_html_visualization.py
- verify_migration.py
- test_emote.py
- RoomCacheLoader
- GameTerminalContext.test.tsx
- MockPersistence
- PlayerInventory
- tailwind Best Practices
- ChannelBroadcastingStrategyFactory
- async_load_zone_configurations
- required
- required
- CombatBroadcastMixin
- Net Impact Summary
- MemoryLeakMetricsCollector
- delegate_error_handler
- asyncio
- Performance Profiler Subagent
- Security Auditor Subagent
- The Toolkit
- test_profession_repository.py
- UUID
- compilerOptions
- include
- ADR-012: python-statemachine for Backend Connection FSM
- Asyncio Code Review - feature/sqlite-to-postgresql Branch
- Ruff to Pylint Rule Mapping
- SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch
- MythosMUD Test Suite Modernization Plan
- Execution Steps
- monitoring_service
- quality_fragmentation_ai_guardrails.py
- fix_suppression_alignment.py
- identify_critical_code.py
- test_postgres_adapter.py
- UnknownChannelStrategy
- command_result_text
- RoomRepository
- get_summary
- PostgresCursor
- handle_unequip_command
- test_users.py
- test_player_repository_room.py
- fixture
- talk_command.py
- 1. Structured Concurrency: Entry Points and Task Management
- asyncio
- _get_proper_data_dir
- test_game_state_provider.py
- get_room_environment
- TestErrorHandlers
- overrides
- mock_persistence
- test_logging_file_setup.py
- compilerOptions
- compilerOptions
- Communities (11 total, 0 thin omitted)
- Communities (11 total, 0 thin omitted)
- 🎯 Test Categories
- Environment Contamination Audit Report
- NATS Anti-Patterns Remediation Summary
- ConnectionManager Refactoring Summary
- Execution Steps
- PersonalMessageSender
- properties
- audit_suppressions.py
- fix_markdown_line_length.py
- populate_npc_sample_data.py
- pydantic Best Practices
- worktree-plan-template.md
- lock_state
- MetricsCollector
- npc_combat_grace.py
- test_look_container_helpers.py
- test_lifespan_shutdown.py
- environment
- Path
- TestPathValidator
- Design Critique
- useThemeContext.ts
- multiplayer-browser-helpers.bundle.js
- compilerOptions
- verify_password
- Communities (10 total, 0 thin omitted)
- properties
- properties
- ApplicationContainer Structure Analysis and Domain-Specific Split Proposal
- Changes by document
- Lizard Complexity Analysis Findings
- NATS Medium-Priority Remediation Summary
- 2. Mythos Time Model Draft
- Phase 2: Qualitative Analysis Results
- LoggingPatternLinter
- required
- UpgradeImplementationPlan
- environment
- validate_secure_path
- test_container_persistence_crud.py
- MessageBroker
- CommandRateLimiter
- ComprehensiveLoggingMiddleware
- test_event_publisher.py
- SystemAdminChannelStrategy
- test_chat_validator.py
- handle_skills_command
- test_room_service.py
- test_room_subscription_manager_npcs.py
- UUID
- TestVerificationSqlUsersPlayers
- PayloadOptimizer
- _RoomPersistence
- subzone_schema.json
- static_data/package.json
- Delight Techniques
- Frontend Design Skill
- ContainerLockMixin
- compilerOptions
- asyncio
- Enhanced Logging Quick Reference
- NumPy Code Review - MythosMUD Codebase
- Python Model Updates Required for Migration 019
- Transaction Boundaries Audit
- asyncio
- enum
- test_container_persistence_sql_injection.py
- CombatConfiguration
- Any
- test_inventory_helpers.py
- channels.ts
- CoordinateValidator
- fixtures/shared/__init__.py
- optimized_comprehensive_sanitize_input
- required
- CRITICAL SERVER MANAGEMENT RULES
- Test Coverage Requirements
- zone_schema.json
- properties
- room_validator/tests/conftest.py
- Dependency Upgrade
- Animate Skill
- Polish Systematically
- overrides
- ContainerTransferToMixin
- Communities (10 total, 2 thin omitted)
- Git Workflow
- Gladiator Ring (Arena) Implementation Plan
- Game Subsystem Design Documents
- Execution Steps
- properties
- bench_cache_professions.py
- fix_markdown_blanks_around_lists.py
- init_npc_database.py
- ._create_tracked_task
- TestCommandNormalization
- asyncio
- Path
- CombatValidator
- HealthMonitor
- persistence/container_helpers.py
- enum
- properties
- _FakeClientState
- CircuitBreaker
- items
- container
- holidays
- schedules
- Introduce Color Strategically
- UX Writing
- rules
- usePanelContext.ts
- hash_password
- whisper-movement.spec.ts
- intersection_schema.json
- room_schema.json
- create_app
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)
- Cosmic Horror.md
- applies_to
- ADR-003 Dual Event Systems EventBus NATS
- ✅ Async Remediation Complete
- Phase 2 Async Persistence Migration - Status Update
- Quick Start: Running E2E Tests
- Execution Steps
- CircuitBreaker
- properties
- properties
- properties
- fix_file
- jackson_linter.py
- RoomFilenameMigrator
- rest_countdown_task.py
- test_zone_config_loader.py
- match_inventory_item_by_name
- test_party_flow.py
- TestFeatureFlagService
- SessionManager
- MythosMUDError
- AttributeError
- PrototypeRegistry
- test_instance_manager.py
- Any
- test_player_spell_repository.py
- test_time_commands.py
- test_nats_message_handler_chat.py
- optimized_validate_security_comprehensive
- properties
- properties
- CommunicationIntegrationProtocol
- Codebase Explorer Subagent
- Adapt Skill
- Improve Copy Systematically
- Color & Contrast
- AlertType
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)
- Async Persistence Migration Tracker
- Migration 019: Ready for Deployment
- .connection_manager
- ExperienceRepository
- Frontend Design Skill
- holiday.schema.json
- schedule.schema.json
- analyze_coverage_gaps.py
- _apply_arena_seed_patch.py
- test_command_service.py
- generate_sql.mjs
- PostgreSQL database names (MythosMUD)
- enum
- MockEventClass
- test_alias_expansion.py
- description
- .get_player_aliases
- name
- item_prototype.schema.json
- description
- test_invite.py
- description
- test_message_builders.py
- CommandService
- test_inventory_command_prototype.py
- test_profession_service.py
- test_lifecycle_respawn.py
- PhantomHostileService
- TestValidatorIntegration
- LoggingConfig
- test_check_no_production_assert.py
- fixture
- asyncio
- Spatial Design
- Typography
- MythosMUD Code Quality Targets for AI
- Skill: Create a New Worktree for a Task
- RoomInfo.tsx
- MessageBatcher
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)
- required
- npc_schedules.schema.json
- .get_instance
- fix_markdown_common_issues.py
- process_room_files
- validate_codacy_coverage_gate.py
- description
- handle_teach_command
- TestValidateRoomData
- test_message_filtering_helpers.py
- test_aggressive_mob_npc.py
- test_argon2_utils.py
- AsciiMapRenderer
- name
- weather_patterns
- Stats
- convert_uuids_to_strings
- test_npc_population_api.py
- 7. Common Test Failure Solutions
- PlayerStateService
- Player
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- _StubPlayerRepo
- 2. Auto-Attack During Grace Period
- 3. Grace Period Visibility & Messaging
- test_config_models.py
- TrackedTaskManager
- 4. Rest/Quit Command During Combat
- Any
- test_websocket_handler_error_handling.py
- 5. Rest Command Countdown Duration
- 6. Rest Location (Inn/Hotel) Behavior
- .disconnect
- test_skill_service.py
- asyncio
- handle_explore_command
- 7. Reconnection During Grace Period
- optimized_security_validator.py
- check_no_production_assert.py
- Generate Comprehensive Report
- Optimize Skill
- Test Server Remediation Prompt - Cursor Executable Version
- Arkham City (MOTD Zone)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)
- Easy Coverage Wins - Quick Analysis
- Test Suite Quality Audit - Executive Summary
- Test Value Distribution Chart
- analyze_log_file
- type
- find_fstring_logging_violations
- lint_sql_guardrails.py
- test_cache_service.py
- test_load_room_cache_async_rooms_none
- ._get_room_uuid_by_stable_id
- 8. Grace Period After Intentional Disconnect
- 9. Command Blocking During Grace Period
- Recommendations Summary
- duration_hours
- is_safe_filename
- days
- effects
- run_flee_effect
- end_hour
- test_player_repository.py
- start_hour
- zone_config_loader.py
- ._ensure_room_cache_loaded
- _make_mock_row
- _find_container_wearable
- test_ascii_map_renderer_exits.py
- _parse_env_list
- exits
- test_magic_commands.py
- 💡 Recommendations
- optimized_validate_player_name
- Improve Layout Systematically
- Distill Skill
- Interaction Design
- Missing Test Scenarios
- MythosMUD Full-Stack Feature Skill
- Next Steps
- ClientLogger
- _format_container_display
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)
- Geography Overview.md
- required
- Technical Implementation
- Execution Timeline
- main
- fix_markdown_code_block_style.py
- main
- SyntaxErrorFixer
- run_quality_fragmentation_guard.py
- _check_grace_period_block
- day
- get_npc_name_from_instance
- correct_patterns.py
- holiday
- ._compose_memory_stats
- FeatureFlagService
- .get_upcoming_holidays
- assert_event_envelope
- get_database_path
- month
- Any
- generate_invites_db.py
- test_persistence_container_persistence.py
- .error
- UUID
- test_combat_loader.py
- Any
- fixture
- test_validate_codacy_coverage_gate.py
- feature_flag_service.py
- room_validator/schemas/unified_room_schema.json
- Commands
- Amplify the Design
- Hardening Dimensions
- MythosMUD LLM Wiki (Obsidian)
- plane
- MapPerformanceMonitor
- PanelContextRuntime.tsx
- mcp.json
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)
- bonus_tags
- Async Remediation Summary - December 3, 2025
- Migration Guide: From Default Logging to Enhanced Logging
- Migration Roadmap
- Enhanced Logging Guide
- Critical Insights
- Actionable Recommendations
- Movement Subsystem Design
- Multi-Character Support System
- .call
- enum
- required
- required
- grype.py
- main
- main
- position_commands.py
- test_websocket_handler_rate_limit.py
- long_description
- look_container.py
- prototype_id
- short_description
- id
- plane
- rest_location
- test_monitoring_init.py
- zone
- TestEmoteDetection
- handle_system_command
- test_player_event_handlers_utils_grace_period.py
- test_player_event_handlers_room.py
- test_process_exit_rows_with_partial_room_ids
- test_process_exit_rows_debug_logging
- test_schedule_service.py
- load_motd
- reset_config
- sub_zone
- zone
- Responsive Design
- Quieter Skill
- Typeset Skill
- mythos_e2e Database
- GridLayoutManager.tsx
- test_build_room_objects_success
- vite.userConfig.ts
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)
- Authoritative Environment DML
- ADR-018: New Game Session vs Grace Reconnect
- Async Code Review - Post Phase 2 Migration
- ✅ Best Practices Compliance
- 🔍 Specific File Reviews
- CircuitBreaker Implementation Planning Document
- CI Workflow
- analyze_file
- check_and_apply_map_migrations.py
- main
- .validate_database_url
- main
- test_process_room_rows_with_full_room_id
- test_build_room_objects_with_non_dict_attributes
- test_load_room_cache_with_rooms_logs_sample_ids
- test_process_room_rows_empty_list
- test_inventory_mutation_guard_sync.py
- test_process_exit_rows_multiple_exits_same_room
- SpellMaterial
- test_process_exit_rows_zone_single_part
- items
- description
- test_process_room_rows_with_partial_room_id
- .get_alias_file_path
- test_async_persistence_room_cache.py
- test_build_room_objects_without_environment_in_attributes
- exits
- test_process_room_rows_with_none_attributes
- test_process_room_rows_zone_without_slash
- name
- UUID
- Teach Impeccable Skill
- Dependency Upgrade Report
- plane
- _occupation_slots_9
- Cursor Subagents Overview
- exits
- Mypy Remediation
- REQUIRED TOOL USAGE PATTERN
- FAILURE PATTERN RECOGNITION
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)
- Chaosium CoC Catalog
- enum
- Architecture Decision Records Index
- Asynchronous Code Audit - December 3, 2025
- Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES
- Enhanced Logging Best Practices for MythosMUD
- Appendices
- Implementation Phases
- Summary: Test Quality Metrics
- MythosMUD Testing Strategy (Greenfield Suite)
- Dialogue Content Tools (Content Creators)
- load_test_10_players.spec.ts
- enum
- plane
- emote_schema.json
- bench_cache_npc.py
- check_file
- .__init__
- zone
- RetryConfig
- lucidity_migration.py
- _personal_interest_4
- asyncio
- npc_spawn_modifier
- event_publisher
- special_rules
- factory
- ChatChannelLoggerMixin
- TestMinimapExplorationInvestigationDoc
- plane
- 📈 Success Metrics
- _EventPersistence
- optimized_validate_action_content
- optimized_validate_alias_name
- optimized_sanitize_unicode_input
- asyncio
- gh-stack (MythosMUD)
- Workflows
- Security Considerations
- test_websocket_handler_validation.py
- main
- Motion Design
- run-playwright-tests.js
- Final Recommendation
- main
- holidays.schema.json
- 🟡 HIGH PRIORITY ISSUES
- 🟢 MEDIUM PRIORITY IMPROVEMENTS
- Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE
- 🔴 Anti-Patterns Check (Critical)
- Implementation Notes
- Persistence Layer Async Migration Plan
- **~25-30% provide CRITICAL coverage**
- Cursor Workflows
- test_ascii_map_renderer_grid.py
- enum
- CombatMetrics
- days
- weight
- bench_cache.py
- quality_fragmentation_graph.py
- _filter_lines
- fix_markdown_file
- fix_room_references
- config.py
- run_bug_prevention_tests.ps1
- run_make_stages.py
- capacity_slots
- .validate_current_vs_max_stats
- apply_communication_dampening
- ._connect_nats
- player_inventory_migration.py
- asyncio
- TestResolveExitTarget
- TestHorizontalExitCharBetween
- asyncio
- test_utility_commands_whoami.py
- FastAPI Best Practices
- test_quest_start_by_trigger_then_abandon
- TestCheckRateLimit
- ModalContainer.tsx
- handle_admin_command
- RoomMapEditor
- agent-routing.md
- ._attack_target_impl
- optimized_validate_target_player
- black.md
- Room Pathing Validator Implementation Spec
- validator.py CLI
- gh-stack
- MythosMUD Commit Messages
- Step 2: Ask UX-Focused Questions
- run-vitest.js
- usePerformanceMonitor.ts
- cli.sh
- Earth Plane
- emotes.schema.json
- 1. Enhanced ChatPanel (New Chat Input Panel)
- ✅ Verified Already Implemented
- Implementation Phases
- Multiplayer Architecture Planning
- API Endpoints (Phase 2)
- ✅ Phase 2 Async Persistence Migration - COMPLETE
- Python Code Coverage Status
- pyrightconfig.json
- enum
- main
- migrate_file
- apply_migration
- generate_sql.mjs
- validate.mjs
- Invite
- asyncio
- test_emote_service.py
- happy-dom
- markdownlint-cli
- .render_map
- PlayerCreationService
- fixture
- DatabaseManager
- ._check_dict_condition
- test_run_make_stages.py
- verify_npc_occupants.py
- patch-package
- @playwright/test
- tailwindcss
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- optimized_validate_filter_name
- optimized_validate_help_topic
- @testing-library/dom
- gh-stack (MythosMUD)
- MythosMUD ADR Authoring
- MythosMUD Logging Standards
- MythosMUD Server Runbook
- useGridLayout.ts
- mapPageRenderer.tsx
- Three-Column Game UI Layout
- @testing-library/react
- @testing-library/user-event
- Chat Panel
- Aggro and Threat System Implementation Plan
- ✅ POSITIVE FINDINGS
- 🔴 CRITICAL ISSUES
- ✅ Positive Findings
- 🚫 Anti-Patterns NOT Found (Good!)
- 📞 Next Steps
- Entries
- Migration Workflow (Per File)
- Security Implementation
- Recommended Decision
- 3.3 Value Distribution Calculation
- Projected Optimization Impact
- Command Handler Patterns
- AsyncPersistenceLayer Pattern
- Respawn Subsystem
- Attack Command Not Starting Combat
- Second NPC Combat And Linkdead Findings
- Multi-Word Spell Name Parsing Failure
- typescript
- Disconnect Grace Period and Rest Command
- main
- vite
- Server Realtime Module
- test_websocket_room_updates.py
- Critical Discovery & Fix
- BehaviorEngine
- Phase 1: Fix Failing Integration Tests (Week 1-2) 🚧 **IN PROGRESS**
- CombatConfigurationService
- Files Affected
- Category D: API Endpoint Tests (App State)
- Files to Update
- Phase 3: Modernize Test Patterns (Week 5)
- AFTER
- websocket_integration.py
- Thinking about stack structure
- Files to Update
- Extract Skill
- codacy.yaml Tool Manifest
- MythosMUD Server Test Suite
- _run_dialogue_ddl
- New Tests to Add
- Common Test Failure Categories
- Azotottal.md
- Any
- Chat Panel Separation Specification
- 🔍 Anti-Pattern Check
- 📚 Documentation Created
- Implementation Details
- Summary (from Codacy UI snapshot)
- Core Logging Principles
- Performance Logging
- Common Mistakes and How to Fix Them
- Enhanced Logging Features
- Log Levels and Usage
- Enhanced Logging Migration Report
- Mythos Holiday Candidates
- NPC Startup Duplication Analysis
- 💡 Key Improvements
- PostgreSQL Procedures Migration - Audit Spreadsheet
- Real-Time Communication (WebSocket)
- Implementation Approach Decision
- Backward Compatibility Strategy
- Test Suite Analysis
- Modern Testing Patterns
- Test Modernization Checklist
- Testing Requirements
- Test Suite Optimization Roadmap
- Phase 5: Strategic Additions (Week 5)
- Measurement and Validation
- Quest System Features
- Testing Guide
- Whisper Channel System
- NPC Occupants Verification Summary
- Combat Client Crash
- Respawn Death Screen Loop Limbo ID Mismatch
- NPC Combat Start Race Condition
- Round-Based Combat
- WebSocket-Only Migration
- .broadcast_player_mortally_wounded
- asyncio
- check_file_for_logging_issues
- test_profession.py
- e2e_reset_players.py
- add_suppression_to_file
- .shutdown_all
- _get_container_description
- ._compute_player_context
- .process_tick_regeneration
- get_engine
- reset_database
- test_message_filtering.py
- .__init__
- Enhanced Structured Logging System
- test_player_event_handlers_respawn.py
- .select_exit
- UUID
- asyncio
- is_argon2_hash
- Party
- extract_zone_name
- NATSRequestError
- test_async_persistence_delegates.py
- _EmptyClientState
- get_async_session
- usePlayerStatusEffects.ts
- populate_test_npc_databases.py
- RoomBasedChannelStrategy
- stop_health_checks_impl
- .optimize_payload
- test_inventory_mutation_guard_error_handling.py
- test_error_logging.py
- Protocol
- lucidity_communication_dampening.py
- zone
- TestValidateCommandBasics
- ensure_directory_exists
- Any
- _default_cors_origins
- AGENTS.md
- test_combat_grace_period.py
- JsonMap
- _FakeClientState
- MythosMUD COPPA Checklist
- ConnectionPanel.tsx
- MythosLoginForm.tsx
- global-teardown.ts
- AI PR Reviewer Instructions
- generate_invites.py
- asyncio
- 4. Common Fix Patterns
- DML Migrations
- Nameless Horrors - 2nd Edition (source summary)
- S. Petersen's Field Guide to Lovecraftian Horrors (source summary)
- mock_utils
- Advanced Chat Channels Specification
- UI/UX Considerations
- 3. Simplified CommandPanel
- Implementation Phases
- 🎓 Best Practice Examples to Share
- Magic and Spellcasting System
- Lucidity Tiers
- Common Conversion Patterns
- Gotchas & Solutions
- 🎭 Closing Remarks
- Four-Level Room Hierarchy
- Financial Impact (If You're Tracking Dev Time)
- Phase 1: Quick Wins (Week 1)
- Phase 2: Infrastructure Test Reduction (Week 2)
- Phase 4: Test Consolidation (Week 4)
- Phase 6: Long-Term Optimizations (Ongoing)
- Phase 1: Quantitative Analysis Results
- Test Suite Quality Audit Report
- asyncio
- Risk Assessment and Mitigation
- Configuration Files Reference
- Modular E2E Test Suite
- Playwright MCP Scenarios
- Local Channel System
- Container Contents Synchronization Bug
- F-String Logging Violations
- player_event_handler_utils
- asyncio
- Quest System Gap
- CharacterCreationService
- items
- mock_player
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
- rename_players_to_population.py
- wearable_service
- DomainError
- preferences_service
- @vitejs/plugin-react
- .__init__
- reset_async_persistence
- RoomRepositoryProtocol
- needs_rehash
- PlayerCombatState
- test_inventory_mutation_guard_async.py
- .ensure_url_set
- ._build_exit_lookup
- _mock_result_mappings_all
- ._generate_invite_code
- .validate_invite
- Any
- test_validate_secure_path_path_traversal_commonpath
- normalize_path_from_url_or_path
- Testing Logging
- server/dependencies.py
- convert_uuids_to_strings_impl
- sub_zone
- get_next_sequence_impl
- .create_invite
- test_grype.py
- .check_player_mute_status
- _validate_tls_files_and_maybe_update_url
- Any
- ._generate_alert
- .is_player_in_room
- ._send_messages_to_players
- fixture
- test_realtime_bundle_nats.py
- MythosMUD Pre-Commit Checklist Skill
- Claude Pointer (.claude/CLAUDE.md)
- ._handle_hunt_target
- ._handle_patrol_territory
- .__init__
- Tiered Test Coverage Strategy
- VirtualizedMessageList.tsx
- message-match.test.ts
- .__init__
- fake_hallucination_service.py
- test_look_npc.py
- 9. Test Maintenance Best Practices
- LLM Wiki Vault Schema
- Code Graph Entry
- DML Migrations Apply Paths
- Graphify Code Graph
- Church of Sunyata.md
- Dark Young of Shub-Niggurath.md
- Dimensional Shambler.md
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
- day
- Aggro and Threat System Design
- Migration Considerations
- Success Criteria
- Risk Assessment
- Testing Strategy
- 📚 REFERENCES AND RESOURCES
- 📊 METRICS AND SUCCESS CRITERIA
- 🚀 DEPLOYMENT STRATEGY
- @eslint/js
- 🔧 Code Changes Made
- 🏆 Achievement Highlights
- 🎭 Closing Remarks
- 🎯 Performance Improvements
- 💰 ROI Analysis
- 📚 Deliverables
- 🚀 Deployment Readiness
- Phase 2: Database Layer Integration
- Phase 3: Real-Time Communication Protection
- Phase 4: File System Operations
- Phase 6: Monitoring and Observability
- Future Enhancements
- Monitoring and Alerting
- Success Criteria
- Testing Strategy
- WebSocket and SSE Dual Connections
- Context Management
- 🚨 CRITICAL ANTI-PATTERNS - DO NOT USE
- Rollback Procedures
- Success Metrics
- 🚀 Deployment Readiness
- 🎓 Lessons Learned
- 📚 Changes by Category
- 🚦 Next Steps
- ✅ Verification Results
- MythosMUD Product Requirements
- Files to Update
- test_npc_models.py
- Net Impact Projection
- Implementation Timeline
- Phase 3: Coverage Test Optimization (Week 3)
- Appendix: Quick Reference Commands
- Detailed Category Value Breakdown
- Time Distribution Analysis
- Container System API Reference
- Event Ownership Matrix
- Logging Best Practices
- Persistence Repository Layer
- Real-Time Architecture
- Scenario Group Execution
- ChatPoseManager
- Main Foyer Starting Room
- Per-Recipient Whisper Rate Limiting
- Lucidity System Expansion Scenarios
- Container System
- Scenario 32 Disconnect Grace Period
- Whisper System Investigation Report
- Catatonic Movement Prevention Bug
- Rooms List SQL ::uuid[] Parameter Conflict
- Vite Best-Practices Remediation
- duration_hours
- is_websocket_open_impl
- Shared JSON schemas
- apply_migration
- main
- _resolved_npm
- start_server.ps1
- verify_schema_match.sh
- verify_tutorial_migrations.ps1
- test_rescue_service.py
- DeadLetterMessage
- .create_go_command
- .create_ground_command
- _RoomBroadcaster
- test_config.py
- command_service
- idle_movement_handler
- fixture
- test_npc_service.py
- Exception
- Profession
- test_create_channel_command
- Any
- eslint.config.js
- Client Security and Privacy Policies
- PlayerPanel.tsx
- RoomPanel.tsx
- MythosMUD UI Component Library
- LoginGracePeriodBanner.tsx
- mythosTheme.ts
- multiplayer-browser-helpers.d.ts
- get_online_players_impl
- Step-by-Step Remediation Process
- test_create_go_command
- MythosMUD Worldbuilding Source
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
- Petersen's Abominations (source summary)
- Reign of Terror (source summary)
- AI Development Workflow
- 📈 Performance Impact Assessment
- 🎯 Code Quality Assessment
- 🎯 Final Verdict
- 🎓 Technical Debt Reduced
- 🎯 Audit Compliance Score
- 🎓 Key Learnings
- 🔍 Testing Strategy
- test_create_stand_command
- 🎯 Success Criteria - Status
- 🚨 Risk Assessment
- Character Creation Revamp
- Comprehensive System Audit
- Architecture Overview
- Dead Code Cleanup Completion
- Single Session Per User
- Fixture Optimization Complete
- Test Warning Remediation
- Enhanced Logging Migration Complete
- Random Stats Generator Planning
- validate_websocket_message
- Log Rotation and Management
- Log Analysis and Monitoring
- Party System Reference
- Decision Points
- Monitoring & Validation
- Testing Strategy
- 📊 Final Results
- 📈 Performance Impact
- 🎯 Async Compliance Score
- 🧪 Testing Status
- 🔧 Changes Summary
- ._build_connection_stats
- Test File Migration Mapping
- Optimization Strategy Overview
- Monitoring and Validation
- Success Criteria
- Visual Test Value Distribution
- Who Command Enhancement
- Bounded Contexts and Service Boundaries
- GameState Event Projection
- Truly Dead Code
- E2E Testing Guide
- NATS Subject Patterns
- Ground Command
- Rest Subsystem
- LevelService
- Map Regression Tests Proposal
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
- .get_task_lifecycle_metrics
- eslint-plugin-jsx-a11y
- .create_supervised_task
- Any
- Any
- test_create_equip_command
- test_create_unequip_command
- get_hash_info
- test_create_mute_command
- asyncio
- .validate_combat_command
- test_create_unmute_command
- Profession
- MythosMUD Server Runbook Skill
- Bandit configuration
- Test Suite Analyzer Agent
- test_create_mute_global_command
- test_create_unmute_global_command
- mark_player_seen_impl
- test_create_admin_command
- Vite Logo SVG
- ApplicationContainer
- playwright.runtime.config.ts
- deps/package.json
- wsl-bashrc-codacy.sh
- LLM Wiki Pattern.md
- Dietrich Zann.md
- Flying Polyp.md
- Fungi from Yuggoth.md
- Ghoul.md
- Geography and Major Locations.md
- Pulp Cthulhu (7th edition Call of Cthulhu) (source summary)
- Hotel Hell.md
- Mohole.md
- db/migrations/README.md
- Procedures as CRUD Boundary
- InstanceManager
- Architecture Remediation Implementation Summary
- httpOnly Cookie Token Storage
- Combat Health Persistence Bug
- Paired YAML and Env Config Tuples
- React Node Upgrade Plan
- Environment Configuration Refactoring
- container_test_client Fixture
- Graceful Degradation Planning
- Item System Blueprint
- Migration Final Report
- Panel Layout Libraries Spec
- Structlog Implementation Plan
- MOTD Sacred Styling
- players.current_room_id Index Gap
- E2E Scenario Conversion
- CWE-209 Information Exposure
- ftfy Unicode Normalization
- Temporal NPC Schedules
- Updated Coverage Targets
- Hierarchical Test Structure
- CI Environment Alignment
- Client Layout Baseline
- Realtime Messaging Subsystem
- Mid-Run Disconnect Reasons
- bcrypt Fresh Session Isolation
- GitHub Actions Runner Parity Container
- Memory Leak Metrics Usage Guide
- NATS Manual Acknowledgment Guide
- Player Command Pipeline
- Pre-commit Logging Validation
- Python Coverage Targets
- SQLAlchemy Async Best Practices
- Git Submodule Setup
- Online via last_active Threshold
- Error Monitoring Scripts
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
- Limbo Arena Zone
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
- TestNATSError
- test_create_mutes_command
- test_get_room_persistence_not_found
- test_get_room_persistence_returns_dict
- test_get_adjacent_rooms_success
- test_create_time_command
- test_get_adjacent_rooms_source_not_found
- AsyncPersistenceLayer
- persistence/utils/__init__.py
- test_create_whoami_command
- test_get_adjacent_rooms_null_exit
- test_create_quit_command
- test_create_logout_command
- test_get_local_chat_scope
- test_get_local_chat_scope_source_not_found
- TestGracefulDegradation
- test_validate_room_exists_cache_not_found
- test_validate_exit_exists_success
- test_validate_exit_exists_invalid
- test_validate_exit_exists_from_room_not_found
- EventHandler
- test_create_strike_command
- test_validate_exit_exists_no_exits
- test_get_room_occupants_with_cache_dict
- server/structured_logging/__init__.py
- server/tests/__init__.py
- command_handler_unified/__init__.py
- test_create_unalias_command
- .create_stand_command
- test_create_help_command
- _format_container_contents
- test_create_npc_command
- .create_unfollow_command
- ._execute_command_handler
- test_create_spawn_command
- test_create_summon_command
- test_get_room_occupants_cache_not_found
- spell_effects.py
- test_create_teleport_command
- .validate_rate_limits
- unit/container_persistence/__init__.py
- test_combat_configuration_service.py
- test_get_players_batch_with_players
- test_create_goto_command
- test_validate_player_in_room_with_cache_true
- test_validate_player_in_room_with_cache_false
- test_command_factory_has_create_methods
- test_validate_player_in_room_cache_dict
- test_create_cast_command
- get_alerts
- test_get_room_exits_success
- test_get_room_exits_no_exits
- test_create_learn_command
- test_list_rooms_exclude_exits
- test_get_room_info_success
- unit/game/magic/__init__.py
- test_command_factory_create_existing_command
- test_get_room_info_not_found
- test_command_factory_create_nonexistent_command
- test_room_service_init
- test_create_local_command
- asyncio
- month
- test_create_emote_command
- test_create_me_command
- .validate_derived_stats
- test_create_whisper_command
- esbuild
- test_room_service_init_with_cache
- test_get_room_without_cache
- ._error_callback
- _AppStateWithLegacyConfig
- id
- test_save_player_success
- test_save_player_with_bool_is_admin
- test_save_player_database_error
- test_list_players_database_error
- TestGlobalFunctions
- sub_zone
- test_get_player_by_user_id_success
- test_soft_delete_player_not_found
- test_get_players_batch_success
- get_session_connections_impl
- Any
- WearableContainerServiceError
- .add_message
- .get_active_sessions
- .get_combat_settings_summary
- nats_broker
- _PlayerCombatClearing
- fixture
- fixture
- message_filtering_helper
- MonkeyPatch
- server/tests/conftest.py
- messaging_integration
- Success Metrics
- Executive Summary
- unit/infrastructure/__init__.py
- _FakeMessageQueue
- test_create_lie_command
- test_create_ground_command
- test_create_pickup_command
- test_create_get_command
- test_create_add_admin_command
- test_create_status_command
- test_command_factory_init
- test_create_who_command
- test_create_rest_command
- test_create_punch_command
- test_create_shutdown_command
- test_create_spell_command
- test_create_spells_command
- test_create_say_command
- webhook
- test_create_system_command
- test_create_pose_command
- test_room_subscription_manager.py
- _spawn_rule_row
- rest_location
- .get_memory_status_report
- process_zone_rows
- convert_schema_to_dict
- CircuitBreakerOpen
- Path
- convert_room_players_uuids_to_names_impl
- .__init__
- get_combat_monitoring
- sub_zone
- test_help_commands.py
- description
- Enum
- unit/middleware/__init__.py
- unit/monitoring/__init__.py
- id
- test_skill_use_log_repository.py
- npc_service
- applies_to
- initialize_components
- .to_dict
- .__del__
- .__init__
- get_commands_by_category
- .from_dict
- event_bus
- renderer
- mock_connection_manager
- eslint
- ._get_vertical_exit_char
- test_handle_cast_command_success
- test_event_bus_set_main_loop
- test_event_bus_publish_no_subscribers
- occupant_display.py
- test_enrich_behavior_context_swallows_compute_errors
- test_enrich_behavior_context_sets_false_when_no_players_in_room
- test_evaluate_equality_false
- test_evaluate_inequality_false
- test_evaluate_numeric_comparison_greater_equal
- test_evaluate_numeric_comparison_false
- test_evaluate_condition_inequality
- test_evaluate_condition_greater_than
- test_room_class.py
- _FakeEstablishmentManager
- test_connection_rate_limiter.py
- test_get_applicable_rules_priority_order
- ._handle_nats_message_impl
- .check_player_connection_health
- unit/persistence/__init__.py
- unit/realtime/integration/__init__.py
- test_event_bus_publish_multiple_subscribers
- test_subscribe_invalid_event_type
- .auto_progression_enabled
- test_execute_applicable_rules_executes_highest_priority
- movement_service
- fixture
- test_add_rule_missing_fields
- test_execute_applicable_rules_no_handler
- ._background_audit_cycle
- test_register_action_handler
- test_state_direct_access
- test_execute_action_success
- test_auth
- .cleanup_empty_subzone_subscriptions
- .handle_player_movement
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- .__init__
- test_evaluate_condition_handles_exception
- test_ensure_processing_started
- test_convert_room_uuids_to_names
- test_websocket_handler_disconnect.py
- test_websocket_handler_helpers.py
- metadata
- test_event_bus_init
- test_validate_player_room_membership_db_mismatch
- test_unsubscribe_all_for_service
- .get_decayed_containers
- test_unsubscribe_all_for_service_nonexistent
- test_create_container_with_kwargs
- test_apply_dampening_and_send_message_exception
- test_unsubscribe_all_for_service_partial_cleanup
- test_get_subscriber_stats
- test_event_bus_get_subscriber_count
- test_build_room_objects_debug_logging
- test_get_players_batch_empty
- get_npcs_batch_impl
- test_remove_player_from_room_success
- handle_player_entered_room_impl
- periodic_health_check_impl
- _EventBusPublishPort
- test_remove_player_from_room_room_not_found
- pytest_asyncio_loop_factories
- test_get_room_players_room_not_found
- test_validate_player_location_true
- test_validate_movement_allows_ghost_in_destination
- .service
- test_validate_move_params_same_room
- .__call__
- start_hour
- test_move_player_success
- ._flush_memory_indexes_cache
- _set_default_if_missing
- test_resolve_player_by_name
- test_remove_player_invalid_params
- test_check_combat_state_blocks_when_in_combat
- test_validate_exit_found
- test_is_shutdown_pending_no_state
- test_move_player_player_not_found
- test_validate_movement_combat_blocks
- test_mark_room_explored_with_service
- test_asyncio_run_guardrails.py
- id
- test_validate_movement_player_already_in_target
- 8. Error Handling and Debugging
- test_move_player_empty_player_id
- .force_single_audit_cycle
- _NpcWithLife
- test_move_player_same_room
- test_generate_room_id_from_zone_data_with_prefix
- test_generate_room_id_from_zone_data_needs_generation
- test_parse_exits_json_string_valid
- test_add_room_occupant_error_handling
- test_parse_exits_json_list
- test_create_spawn_rule_invalid_min_population
- test_move_player_invalid_to_room
- test_parse_exits_json_other_type
- test_process_exits_for_room_multiple_exits
- .__init__
- test_process_combined_rows_no_exits
- test_add_player_to_room_success
- test_process_room_rows_with_none_zone_stable_id
- test_process_room_rows_with_none_stable_id
- test_process_exit_rows_missing_zone
- test_process_exit_rows_missing_stable_id
- test_load_room_cache_async_warning_logging
- test_warmup_room_cache
- test_async_heal_player_delegates
- test_damage_player_delegates
- unit/services/nats_subject_manager/__init__.py
- test_async_damage_player_delegates
- test_create_container_with_params
- monitor
- auditor
- test_get_container_delegates
- test_get_containers_by_room_id_delegates
- subscription_manager
- subscription_manager
- test_get_containers_by_entity_id_delegates
- combat_validator
- .__init__
- .stop_audit_scheduler
- ._handle_combat_started_event
- test_update_container_delegates
- ._handle_event_message
- ._handle_game_tick_event
- ._handle_npc_attacked_event
- ._handle_npc_died_event
- ._handle_player_entered_event
- .unsubscribe_from_room
- test_process_exit_rows_empty_list
- test_get_decayed_containers_delegates
- test_handle_cast_command_cast_failure
- test_delete_container_delegates
- Dependency Upgrade Tasks
- Dependency Upgrade Implementation Plan
- test_create_item_instance_delegates
- unit/structured_logging/__init__.py
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
- MythosMUD LLM Wiki Skill
- POSTGRES_SEARCH_PATH for invites schema
- JSON Schema Validation
- room_validator/tests/__init__.py
- Codebase Explorer Agent
- Performance Profiler Agent
- Security Auditor Agent
- Vite HTML Entry
- Client Layer Layout
- Zustand Stores
- Codacy CLI via WSL on Windows
- Contributor Covenant Code of Conduct
- test_handle_spells_command_no_player
- test_handle_spells_command_no_spells
- Docker Best Practices Rule
- Authoritative DML Seed Data
- MythosMUD Local Data Directory
- MythosMUD Wiki Index
- R'lyeh
- Mythos Magic
- MythosMUD Obsidian Vault
- mythos_dev mythos_unit mythos_e2e Databases
- test_handle_spells_command_with_spells
- apply_procedures.ps1
- Container Functions Moved from DDL
- generate_schema_from_dev.ps1
- make verify-schema
- Owner and App Roles Per Environment
- Admin Teleport Feature
- Argon2 Security Review
- Configuration Refactoring Complete
- datetime.utcnow Deprecation Fix
- Dual Connection Monitoring Guide
- Simultaneous WebSocket and SSE
- Dual Connection System Tasks
- Dual Connection Troubleshooting Guide
- Players API Code Coverage Plan
- command_handler_v2
- Dual Command Processing Architecture
- PLANNING.md Single Source of Truth
- Semgrep Windows UTF-8 Fix
- Legacy Test File Consolidation
- Test Migration Validation
- Test Refactoring Executive Summary
- asyncio.run Anti-Pattern
- asyncio.to_thread Offloading
- ConnectionManager Modular Architecture
- Migration 019 Testing Guide
- Persistence Async Migration Guide
- Security Environment Variables
- Whisper Location Independence
- Per-Recipient Whisper Rate Limit
- Scenario 22 Administrative Summon
- Scenario 42 Quest Log Visible After Login
- Whisper System Production-Ready
- Structured Logging Correct Patterns
- test_handle_spell_command_no_player
- test_handle_spell_command_spell_not_found
- Documentation Issue Template
- Grype SCA exclude paths
- test_handle_spell_command_success
- NATS Whisper Subject Pattern
- test_handle_learn_command_no_player
- mythosmud
- Click Best-Practices Remediation
- Code Practice Rules Reference Doc
- GitHub Actions Remediation
- Pydantic Anti-Patterns Remediation (3ee32154)
- Pytest Best-Practices Remediation
- test_handle_learn_command_success
- finalize_build_touch Rebuild Trigger
- no-direct-table-crud-in-python-sql rule
- no-select-star-in-python-sql rule
- test_handle_learn_command_with_corruption
- test_handle_stop_command_no_player
- test_announce_spell_cast_no_player_id
- test_handle_spell_command_wrapper_success
- test_handle_learn_command_wrapper_success
- test_handle_stop_command_wrapper_success
- test_ensure_item_instance_delegates
- test_get_player_by_user_id_delegates
- test_dequeue_removes_file
- test_get_players_batch_empty_list
- test_build_room_objects_with_dict_attributes
- test_npc_definition_set_base_stats
- test_npc_definition_get_behavior_config
- test_npc_definition_set_behavior_config
- test_npc_definition_get_ai_integration_stub
- test_npc_definition_set_ai_integration_stub
- test_npc_definition_is_required
- test_npc_definition_type_enum_values
- test_npc_definition_can_spawn
- test_npc_definition_table_name
- test_npc_definition_repr
- test_npc_spawn_rule_creation
- test_npc_spawn_rule_get_spawn_conditions
- test_npc_spawn_rule_set_spawn_conditions
- HealthRepository
- RoomRepository
- GET /v1/monitoring/health
- PostgreSQL Player Persistence
- World Loading
- test_npc_definition_type_enum_all_types
- test_npc_spawn_rule_can_spawn_with_population
- test_npc_spawn_rule_check_spawn_conditions
- test_npc_spawn_rule_check_spawn_conditions_multiple
- test_npc_spawn_rule_table_name
- test_npc_spawn_rule_repr
- test_npc_relationship_table_name
- test_npc_relationship_repr
- test_npc_relationship_different_types
- test_npc_definition_get_base_stats
- test_npc_definition_get_base_stats_empty
- test_get_player_by_name_database_error
- test_convert_room_uuids_to_names_invalid_uuid
- test_enqueue_creates_file
- test_list_messages_handles_read_error
- test_delete_message
- test_should_apply_mute_check_sensitive_channel
- test_should_apply_mute_check_non_sensitive_channel
- test_compare_canonical_rooms_same
- test_compare_canonical_rooms_different
- test_get_player_room_from_online_players
- test_get_player_room_from_online_players_not_found
- test_get_player_room_from_persistence_not_found
- test_get_professions_no_session
- test_is_player_in_room_false
- test_is_player_muted_by_receiver_not_muted
- test_get_user_manager_custom
- test_message_filtering_helper_init
- test_preload_receiver_mute_data
- test_collect_room_targets_with_canonical_id
- test_extract_chat_event_info
- test_get_player_data_for_respawn_no_connection_manager
- WebSocket Best Practices Compliance
- Worktree Plan Metadata
- GitHub Issues task tracking
- invites table
- Mythos-themed invite codes
- core/fixer.py
- jsonschema dependency
- test_get_player_data_for_respawn_no_persistence
- test_send_respawn_event_with_retry_success
- test_send_respawn_event_with_retry_timeout
- test_handle_player_respawned_success
- test_handle_player_respawned_error_handling
- test_get_current_lucidity_found
- test_build_chat_event
- test_get_player_data_for_delirium_respawn_no_connection_manager
- test_get_player_data_for_delirium_respawn_error_handling
- test_handle_player_delirium_respawned_error_handling
- test_prepare_room_data_for_respawn_no_connection_manager
- test_get_player_data_for_respawn_no_get_stats
- test_get_player_data_for_respawn_success
- test_subscribe_player_to_room_success
- test_subscribe_player_to_room_invalid_id
- test_subscribe_player_to_room_error
- test_player_get_inventory_empty
- test_player_set_inventory
- test_player_set_inventory_serializes_uuid_values
- test_player_get_status_effects
- test_player_set_status_effects
- test_player_get_equipped_items
- test_player_get_equipped_items_empty
- test_player_add_experience
- test_player_add_experience_zero
- test_player_is_alive
- test_player_is_mortally_wounded
- test_player_defaults
- test_player_is_dead
- test_player_is_dead_false
- test_player_is_mortally_wounded_uses_stats_int_coercion
- test_player_is_dead_uses_stats_int_nan_default
- test_player_get_health_state
- test_player_is_admin_user
- test_player_is_admin_user_false
- test_player_set_admin_status
- test_player_get_stats
- test_player_set_admin_status_false
- test_player_get_health_percentage
- test_player_get_health_percentage_full
- test_player_get_combat_stats
- test_player_get_combat_stats_defaults
- test_player_get_health_percentage_zero
- test_player_apply_dp_decay_reduces_dp
- test_player_apply_dp_decay_caps_at_negative_10
- test_player_apply_dp_decay_changes_posture_when_crossing_zero
- test_player_restore_to_full_health
- test_player_apply_dp_change_updates_dp
- test_player_get_stats_default
- test_player_apply_dp_change_became_dead
- test_player_table_name
- test_player_repr
- test_player_set_stats
- test_player_get_inventory
- test_profession_get_mechanical_effects_invalid_json
- test_profession_get_mechanical_effects_empty_string
- test_profession_get_mechanical_effects_none
- test_profession_set_mechanical_effects
- test_profession_repr
- test_profession_set_mechanical_effects_empty_dict
- test_profession_meets_stat_requirements_all_met
- test_profession_meets_stat_requirements_one_not_met
- test_profession_meets_stat_requirements_multiple_not_met
- test_profession_meets_stat_requirements_empty_requirements
- test_profession_meets_stat_requirements_invalid_json
- test_profession_meets_stat_requirements_extra_stats
- test_profession_is_available_for_selection_false
- test_profession_get_requirement_display_text_no_requirements
- test_profession_get_requirement_display_text_multiple_requirements
- test_profession_get_stat_requirements_empty_string
- test_profession_get_stat_requirements_none
- test_profession_set_stat_requirements
- test_profession_set_stat_requirements_empty_dict
- test_room_remove_player_silently
- test_room_player_left
- test_room_object_added
- test_room_object_removed
- test_room_npc_entered
- test_room_npc_left
- test_room_init
- test_room_get_players
- test_room_get_npcs
- test_room_has_player_false
- test_room_has_object
- test_room_has_npc
- test_room_get_occupant_count
- test_room_is_empty
- test_room_is_empty_false
- test_room_get_containers
- test_room_to_dict
- test_room_str
- test_room_repr
- test_room_player_entered
- test_room_player_entered_string_id
- test_room_player_entered_empty_id
- test_room_add_player_silently
- test_send_room_name_message
- test_evaluate_equality_string
- test_prepare_room_data_with_to_dict
- test_behavior_engine_init
- test_evaluate_equality_not_equality
- test_evaluate_equality_invalid_format
- test_evaluate_inequality_true
- test_evaluate_inequality_not_inequality
- test_send_room_update_to_player_no_connection_manager
- test_evaluate_numeric_comparison_less_equal
- test_add_rule_success
- test_send_room_update_to_player_room_not_found
- test_evaluate_condition_equality
- test_evaluate_condition_less_than
- test_wearable_container_service.py
- test_evaluate_condition_less_equal
- test_evaluate_condition_unknown
- test_get_applicable_rules_no_matching
- test_execute_applicable_rules_no_matching
- test_send_room_update_to_player_error_handling
- test_register_action_handler_overwrites
- test_build_room_occupants_message
- test_send_occupants_snapshot_to_player_success
- test_send_occupants_snapshot_to_player_string_id
- test_evaluate_boolean_condition_false
- test_send_occupants_snapshot_to_player_no_connection_manager
- test_evaluate_boolean_condition_variable_false
- test_send_occupants_snapshot_to_player_error_handling
- test_remove_rule_success
- test_remove_rule_not_found
- test_send_room_updates_to_entering_player_success
- test_log_player_movement_joined
- test_get_room_occupants
- test_get_player_not_found
- test_convert_room_uuids_to_names_no_player_ids
- test_send_room_updates_to_entering_player_error_handling
- test_get_room_occupants_empty_online_players
- test_get_room_occupants_with_online_players
- test_send_initial_game_state_no_player
- test_send_initial_game_state_send_fails
- test_convert_room_uuids_with_npcs
- test_handle_player_delirium_respawned_success
- test_get_following_for_client
- test_get_quest_log_for_client
- test_get_players_batch
- test_process_player_entered_event_success
- test_health_monitor_init_custom_intervals
- test_rate_limiter_get_rate_limit_info_no_attempts
- test_rate_limiter_cleanup_old_attempts
- test_rate_limiter_init_defaults
- test_rate_limiter_cleanup_old_attempts_removes_empty
- test_rate_limiter_cleanup_old_attempts_error
- test_rate_limiter_cleanup_large_structures
- test_rate_limiter_cleanup_large_structures_error
- test_rate_limiter_remove_player_data
- test_rate_limiter_remove_player_data_not_present
- test_rate_limiter_remove_player_data_error
- test_rate_limiter_init_custom
- test_rate_limiter_get_stats
- test_rate_limiter_get_stats_empty
- test_rate_limiter_get_stats_error
- test_rate_limiter_check_message_rate_limit_first
- test_rate_limiter_check_message_rate_limit_within_limit
- test_rate_limiter_check_message_rate_limit_exceeded
- test_rate_limiter_get_message_rate_limit_info
- test_rate_limiter_get_message_rate_limit_info_no_attempts
- test_rate_limiter_check_rate_limit_first_attempt
- test_rate_limiter_remove_connection_message_data
- test_rate_limiter_remove_connection_message_data_not_present
- test_rate_limiter_cleanup_old_message_attempts
- test_rate_limiter_check_rate_limit_within_limit
- test_rate_limiter_check_rate_limit_exceeded
- test_rate_limiter_check_rate_limit_old_attempts_removed
- test_process_player_entered_event_no_player_info
- test_dequeue_returns_oldest_message
- test_handle_player_entered_success
- test_list_messages_returns_all
- test_handle_player_entered_no_connection_manager
- test_handle_player_entered_no_player_info
- test_cleanup_old_messages
- test_log_player_movement_left
- test_log_player_movement_no_room
- test_broadcast_player_entered_message
- test_normalize_event_ids_both_provided
- test_normalize_event_ids_none_values
- test_extract_name_from_occupant_dict_with_player_name
- test_extract_name_from_occupant_dict_with_npc_name
- test_extract_name_from_occupant_dict_with_name
- test_extract_name_from_occupant_string
- test_extract_name_from_occupant_invalid_type
- test_extract_occupant_names_valid_names
- test_extract_occupant_names_invalid_names
- test_extract_occupant_names_empty_list
- test_extract_occupant_names_none
- test_get_player_lucidity_tier_default
- test_validate_chat_message_fields_sender_name_type_error
- test_validate_chat_message_fields_content_type_error
- test_extract_chat_message_fields_whisper_target_id
- test_extract_chat_message_fields_system_target_id
- test_process_message_with_retry_failure
- test_broadcast_by_channel_type_exception
- test_send_messages_to_players_no_original_content
- test_send_messages_to_players_with_tags
- test_should_echo_to_sender_not_echo_channel
- test_should_echo_to_sender_not_chat_message
- test_validate_chat_message_fields
- test_should_echo_to_sender_no_targets_not_notified
- test_should_echo_to_sender_no_targets_already_notified
- test_add_valid_name_to_lists_player
- test_broadcast_to_room_with_filtering_exception
- test_get_player_lucidity_tier_exception_in_processing
- test_add_valid_name_to_lists_npc
- test_convert_ids_to_uuids
- test_convert_ids_to_uuids_none_target
- test_format_message_for_receiver
- test_subscribe_to_subzone_no_subject_manager
- test_subscribe_to_event_subjects_partial_failure
- test_unsubscribe_from_subzone_decrease_count
- test_handle_player_movement_old_subzone_none
- test_add_room_occupant_new_room
- test_handle_player_movement_error
- test_subscribe_to_subzone_subscribe_failure
- test_unsubscribe_from_subzone_unsubscribe_failure
- test_handle_combat_started_event
- test_handle_combat_ended_event
- test_handle_npc_attacked_event
- test_handle_npc_took_damage_event
- test_handle_npc_died_event
- test_handle_player_movement_different_subzone
- test_handle_player_movement_same_subzone
- test_handle_player_movement_exception
- test_add_valid_name_to_lists_invalid_name
- test_add_valid_name_to_lists_none_name
- test_process_dict_occupant_with_npc_name
- test_process_dict_occupant_with_name
- test_process_dict_occupant_invalid_name
- test_build_occupants_snapshot_data_mixed
- test_build_occupants_snapshot_data_none
- test_count_occupants_by_type_mixed
- test_is_player_disconnecting_true
- test_is_player_disconnecting_string_id
- test_is_player_disconnecting_no_connection_manager
- test_is_player_disconnecting_no_disconnecting_players_attr
- test_player_event_handler_utils_init
- test_normalize_player_id_uuid
- test_normalize_player_id_string
- test_normalize_player_id_invalid_string
- test_player_name_utils.py
- .test_extract_initial_player_name_with_getattr
- .test_extract_initial_player_name_none
- .test_try_player_username_invalid_uuid
- .test_try_player_username_none
- .test_get_name_from_user_object_display_name
- .test_get_name_from_user_object_none
- .test_try_user_object_name_no_user_attr
- .test_try_user_object_name_user_none
- .test_try_user_object_name_exception_handling
- .test_validate_name_basic_valid
- .test_validate_name_basic_none
- .test_validate_name_basic_empty_string
- .test_check_uuid_pattern_match_valid
- .test_is_uuid_string_invalid_length
- .test_log_uuid_validation_failure_critical
- .test_log_uuid_validation_failure_warning_string
- .test_validate_name_not_uuid_valid
- .test_validate_name_not_uuid_matches_player_id
- .test_extract_and_validate_player_name_fallback_user_object
- .test_extract_and_validate_player_name_invalid_uuid
- .test_is_uuid_string_invalid_characters
- .test_is_valid_name_valid_string
- .test_is_valid_name_none
- .test_is_valid_name_not_string
- .test_is_valid_name_string_valid
- .test_extract_initial_player_name_with_name_attr
- test_rescue_no_persistence
- test_rescue_target_not_found
- test_rescue_not_catatonic
- test_rescue_success
- test_rescue_with_player_name
- test_rescue_delta_calculation
- test_create_put_command
- test_rescue_metadata_includes_rescuer
- test_rescue_handles_uuid_objects
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
- test_add_room_drop
- test_add_room_drop_invalid_quantity
- test_take_room_drop_all
- test_take_room_drop_invalid_index
- test_adjust_room_drop
- test_adjust_room_drop_remove
- sample_target
- test_add_room_occupant_multiple
- sample_lucidity_record
- test_remove_room_occupant
- test_remove_room_occupant_not_occupant
- test_remove_room_occupant_removes_empty_room
- test_room_subscription_manager_init
- test_set_async_persistence
- test_subscribe_to_room
- test_subscribe_to_room_multiple_players
- test_unsubscribe_from_room
- test_unsubscribe_from_room_not_subscribed
- test_subscribe_to_room_error
- test_unsubscribe_from_room_error
- .test_is_combat_monitoring_enabled_true
- .test_clear_cache
- .test_check_combat_availability_enabled
- .test_check_combat_availability_invalid_requirements
- test_update_npc_definition_invalid_type
- test_update_npc_definition_invalid_probability
- test_list_alias_files_with_files
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

## God Nodes (most connected - your core abstractions)
1. `get_logger()` - 527 edges
2. `LoggedHTTPException` - 358 edges
3. `ValidationError` - 337 edges
4. `User` - 293 edges
5. `AliasStorage` - 264 edges
6. `DatabaseError` - 264 edges
7. `ConnectionManager` - 257 edges
8. `Player` - 229 edges
9. `log_and_raise()` - 196 edges
10. `CombatParticipant` - 194 edges

## Surprising Connections (you probably didn't know these)
- `Arkham City Graph PNG` --semantically_similar_to--> `Simple Room Graph - Arkham City`  [INFERRED] [semantically similar]
  data/local/arkham_city_graph.png → data/local/simple_room_visualization.html
- `correct_async_logging()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/correct_patterns.py → server/structured_logging/logging_context.py
- `correct_async_logging()` --calls--> `clear_request_context()`  [INFERRED]
  docs/examples/logging/correct_patterns.py → server/structured_logging/logging_context.py
- `websocket_endpoint()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py
- `websocket_endpoint()` --calls--> `clear_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py

## Import Cycles
- 2-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 2-file cycle: `client/src/components/map/useAsciiMap.ts -> client/src/components/map/useAsciiMapState.ts -> client/src/components/map/useAsciiMap.ts`
- 3-file cycle: `server/realtime/connection_cleanup_methods.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_cleanup_methods.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 3-file cycle: `client/src/components/panels/chatPanelChannelFilter.ts -> client/src/components/panels/chatPanelChannelVisibility.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelChannelFilter.ts`
- 3-file cycle: `client/src/components/panels/chatPanelRuntimeUtils.ts -> client/src/components/panels/chatPanelUnreadCounts.ts -> client/src/components/panels/chatPanelUnreadBump.ts -> client/src/components/panels/chatPanelRuntimeUtils.ts`
- 4-file cycle: `server/realtime/connection_establishment.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_establishment.py`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`

## Hyperedges (group relationships)
- **Agent Orchestration Framework** — agents_md, claude_md, user_rules_md, claude_agents_bug_investigator_md, claude_agents_codebase_explorer_md, claude_agents_performance_profiler_md, claude_agents_security_auditor_md, claude_agents_test_analyzer_md [EXTRACTED 1.00]
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
- **Frontend Design System Skills** — claude_skills_frontend_design_skill, claude_skills_teach_impeccable_skill, claude_skills_audit_skill, claude_skills_critique_skill, claude_skills_normalize_skill, claude_skills_polish_skill [EXTRACTED 1.00]
- **Design skills depend on frontend-design** — skills_frontend_design, skills_adapt, skills_animate, skills_arrange, skills_bolder, skills_clarify, skills_colorize, skills_critique, skills_delight, skills_distill, skills_extract [EXTRACTED 1.00]
- **Design skills requiring teach-impeccable** — skills_teach_impeccable, skills_onboard, skills_optimize, skills_overdrive, skills_polish, skills_quieter, skills_typeset, skills_design_context_persistence [EXTRACTED 1.00]
- **Earth-plane major geography locations** — data_mythosmud_obsidian_raw_sources_mythosmud_worldbuilding_earth_plane, data_mythosmud_obsidian_raw_sources_geography_major_locations_arkham_city, data_mythosmud_obsidian_raw_sources_geography_major_locations_innsmouth, data_mythosmud_obsidian_raw_sources_geography_major_locations_rlyeh [EXTRACTED 1.00]
- **Effects and grace period cluster** — plans_effects_system_adr_and_implementation, plans_effects_system_implementation, plans_disconnect_grace_period_and_rest, plans_effects_login_warded [EXTRACTED 1.00]
- **Event projection and room handoff authority path** — client_src_components_ui_v2_eventlog_events_schema_event_projector, client_src_components_ui_v2_eventlog_events_schema_room_state, client_src_components_ui_v2_eventlog_handoffs_enter_room_rr [EXTRACTED 1.00]
- **Frontend-design reference docs** — skills_frontend_design_ref_color_and_contrast, skills_frontend_design_ref_interaction_design, skills_frontend_design_ref_motion_design, skills_frontend_design_ref_responsive_design, skills_frontend_design_ref_spatial_design, skills_frontend_design_ref_typography, skills_frontend_design_ref_ux_writing [EXTRACTED 1.00]
- **Memory leak metrics and remediation** — plans_memory_leak_metrics_collection, plans_memory_leak_remediation, plans_memory_closed_websockets_deque [EXTRACTED 1.00]
- **MOTD listed known zones** — data_local_motd_message_of_the_day, data_local_motd_arkham_city, data_local_motd_innsmouth, data_local_motd_katmandu [EXTRACTED 1.00]
- **Quest gap analysis to implementation** — plans_mud_subsystems_gap_analysis, plans_mud_quest_gap, plans_quest_subsystem_implementation, plans_quest_system [EXTRACTED 1.00]
- **Canonical seed path via authoritative DML** — data_spells_readme_spells_seed_deprecated, data_static_generated_sql_readme_world_and_emotes_sql, data_static_generated_sql_readme_static_seed_deprecated [EXTRACTED 1.00]
- **Alert evaluation and routing pipeline** — monitoring_prometheus_yml_prometheus_config, monitoring_mythos_alerts_yml_alert_rules, monitoring_alertmanager_yml_alertmanager_config [EXTRACTED 1.00]
- **Core monitoring stack services** — monitoring_docker_compose_prometheus, monitoring_docker_compose_alertmanager, monitoring_docker_compose_grafana [EXTRACTED 1.00]
- **MythosMUD Development Workflow** — claude_skills_mythosmud_worktree_workflow_skill, claude_skills_gh_stack_skill, claude_skills_mythosmud_commit_messages_skill, claude_skills_mythosmud_pre_commit_checklist_skill [EXTRACTED 1.00]
- **MythosMUD Quality & Compliance** — claude_skills_mythosmud_code_quality_ai_skill, claude_skills_mythosmud_logging_standards_skill, claude_skills_mythosmud_coppa_checklist_skill, claude_skills_mythosmud_database_placement_skill [EXTRACTED 1.00]
- **Project Documentation Core** — readme_md, contributing_md, security_md, testing_md [EXTRACTED 1.00]
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
- **Dual connection documentation set** — docs_archive_dual_connection_api_reference_dual_connection_api, docs_archive_dual_connection_client_guide_dual_connection_client, docs_archive_dual_connection_deployment_guide_dual_connection_deploy, docs_archive_dual_connection_api_reference_websocket_sse_dual [INFERRED 0.95]
- **Enhanced logging documentation cluster** — docs_archive_implementation_complete_enhanced_logging_complete, docs_archive_logging_implementation_summary_enhanced_logging, docs_archive_logging_migration_complete_logging_migration [INFERRED 0.95]
- **Spell command and casting failure cluster** — investigations_sessions_2025_12_14_session_001_spell_commands_failure_spell_commands_missing, investigations_sessions_2025_12_14_session_002_spell_cast_failure_multiword_spell, investigations_sessions_2025_12_14_session_003_minor_heal_casting_delay_missing_async_heal, investigations_sessions_2025_12_14_session_004_heal_spell_casting_failure_session_boundary [INFERRED 0.95]
- **Logging and error handling guides** — docs_enhanced_logging_guide_doc, docs_error_handling_guide_doc, docs_error_logging_implementation_guide_doc [INFERRED 0.95]

## Communities (2776 total, 914 thin omitted)

### Community 0 - "ConnectionManager"
Cohesion: 0.00
Nodes (1087): ModuleType, emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), ContainerComponent, UUID, WebSocket event emission helpers for container API endpoints. This module… (+1079 more)

### Community 1 - "test_player_respawn_service.py"
Cohesion: 0.01
Nodes (234): Shared spawn / respawn room identifiers used by gameplay and E2E seed scripts.…, Initialize combat services., AttributeType, PositionState, StrEnum, Game-related models for MythosMUD. This module contains models specific to the…, Weapon statistics for items that can be used as weapons. This model represents…, Core attribute types for the character system . (+226 more)

### Community 2 - "TestPlayerNameExtractor"
Cohesion: 0.03
Nodes (35): Test _try_player_username with valid username., Test _try_player_username with getattr fallback., Test suite for PlayerNameExtractor class., Test _get_name_from_user_object with username., Test _get_name_from_user_object with getattr fallback., Test PlayerNameExtractor initialization., Test _try_user_object_name with user attribute., Test _try_fallback_name_sources with valid current name. (+27 more)

### Community 3 - "SpellEffects"
Cohesion: 0.03
Nodes (100): _initialize_spell_effects(), Initialize SpellEffects and attach to app.state., Optional deps for SpellEffects beyond player_service., Engine for processing spell effects with mastery modifiers., Initialize the spell effects engine., Connection manager for login grace period checks., Movement service for flee effect., SpellEffects (+92 more)

### Community 4 - "UUID"
Cohesion: 0.03
Nodes (35): Player, UUID, Get the first WebSocket connection ID for a player (backward compatibility)., Check if a player has any WebSocket connections., Get the number of connections for a player by type., Subscribe a player to a room (compatibility method)., Unsubscribe a player from a room (compatibility method)., Disconnect a specific WebSocket connection for a player. (+27 more)

### Community 5 - "BaseCommand"
Cohesion: 0.01
Nodes (289): BaseCommand, CommandType, BaseModel, Base command models and enums for MythosMUD. This module provides the…, Base class for all MythosMUD commands. Provides common validation and security…, Valid command types for MythosMUD., ChannelCommand, Channel management command models for MythosMUD. This module provides command… (+281 more)

### Community 6 - "test_admin_auth_service.py"
Cohesion: 0.02
Nodes (109): AdminAction, AdminAuthService, AdminRole, AdminSession, Request, Represents an admin session., Service for admin authentication and authorization., Initialize the admin auth service. (+101 more)

### Community 7 - "test_follow_service.py"
Cohesion: 0.02
Nodes (126): _FollowTargetValue, FollowService, _is_npc_follow_value(), Any, TypeGuard, UserManager, UUID, Follow service for MythosMUD. In-memory follow state: who is following whom… (+118 more)

### Community 8 - "test_connection_delegates.py"
Cohesion: 0.03
Nodes (117): _async_callable(), cleanup_dead_websocket_impl(), _close_dead_websocket_if_open(), delegate_connection_cleaner_sync(), delegate_game_state_provider(), delegate_game_state_provider_sync(), delegate_health_monitor(), delegate_health_monitor_sync() (+109 more)

### Community 9 - "test_auth_utils.py"
Cohesion: 0.03
Nodes (98): create_access_token(), hash_password(), timedelta, Hash a plaintext password using Argon2id. This function provides superior…, Verify a plaintext password against a hash. This function safely handles both…, Create a JWT access token., verify_password(), fixture (+90 more)

### Community 10 - "test_websocket_handler_app_state_connection.py"
Cohesion: 0.06
Nodes (47): _mirror_service_to_app_state(), Read player_service and user_manager from app_state.container., Copy container service onto app.state if missing., Resolve player_service and user_manager from container or app.state. Mutates…, resolve_and_setup_app_state_services(), _services_from_container(), handle_websocket_connection(), UUID (+39 more)

### Community 11 - "test_exceptions.py"
Cohesion: 0.03
Nodes (81): Initialize the Pydantic error handler. Args: context: Optional error context…, ErrorContext, LoggedException, Any, Exception, Initialize MythosMUD error. Args: message: Technical error message context:…, Convert error to dictionary for API responses., Log validation errors at warning so expected user-input errors do not flood… (+73 more)

### Community 12 - "CombatParticipant"
Cohesion: 0.03
Nodes (117): CombatAction, CombatParticipant, Check if participant can perform voluntary combat actions. Unconscious (DP <=…, Apply damage to this participant and determine resulting death states.…, Represents a combat action., Represents a participant in combat., Check if participant is dead. For players: dead if DP <= -10 For NPCs: dead if…, Check if participant is mortally wounded (players only). For players: mortally… (+109 more)

### Community 13 - ".get_instance"
Cohesion: 0.04
Nodes (98): Get the singleton instance., Reset singleton for testing., asyncio, Unit tests for database error handling and edge cases. Tests error paths,…, Test _initialize_database converts postgresql:// to postgresql+asyncpg://., Test _initialize_database keeps postgresql+asyncpg:// URL as-is., Test _initialize_database uses NullPool for test URLs., Test _initialize_database uses pool config for production URLs. (+90 more)

### Community 14 - "test_invite_schemas.py"
Cohesion: 0.05
Nodes (61): Auth domain schemas: user and invite., InviteBase, InviteCreate, InviteUpdate, Pydantic schemas for Invite model. This module defines Pydantic schemas for…, Base invite schema with common fields., Schema for creating a new invite., Schema for updating invite data. (+53 more)

### Community 15 - "CatatoniaRegistry"
Cohesion: 0.05
Nodes (35): CatatoniaRegistry, datetime, UUID, In-memory registry tracking catatonic investigators., Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks., Return True if we should trigger sanitarium failover for this player (not… (+27 more)

### Community 16 - "NPCCombatIntegrationService"
Cohesion: 0.03
Nodes (59): NPCCombatHandlers, Any, Handle NPC death when combat ends, with defensive exception handling. Args:…, Handle NPC death and related effects., Check if a string is a valid UUID., Handles combat result processing and NPC death operations., Initialize the combat handlers. Args: data_provider: NPC combat data provider…, NPCCombatIntegrationService (+51 more)

### Community 17 - "api/character_creation.py"
Cohesion: 0.02
Nodes (140): get_current_user(), Get current user with enhanced logging., _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _as_float(), _as_int(), _check_shutdown_status(), _convert_stat_summary_to_stat_summary_model() (+132 more)

### Community 18 - "test_occupant_formatter.py"
Cohesion: 0.04
Nodes (45): Unit tests for occupant formatter. Tests the occupant_formatter module classes…, Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists., Test OccupantFormatter._process_player_name_for_update() adds valid player name., Test OccupantFormatter.__init__() initializes formatter., Test OccupantFormatter._process_player_name_for_update() skips UUID player name., Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name., Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes player… (+37 more)

### Community 19 - "test_container_persistence_async_helpers.py"
Cohesion: 0.08
Nodes (62): ContainerDataExtras, Optional payload and timestamps for a container row., parse_jsonb_column(), Parse a JSONB column value from database. JSONB columns may be returned as: -…, _build_item_dict(), _call_create_container_procedure(), _container_data_from_row(), create_container_async() (+54 more)

### Community 20 - "GameConfig"
Cohesion: 0.14
Nodes (12): GameConfig, BaseSettings, field_validator, Game-specific configuration., Validate combat alert threshold., Validate combat performance threshold., Validate combat error threshold., Validate max connections is reasonable. (+4 more)

### Community 21 - "fixtures/unit/__init__.py"
Cohesion: 0.13
Nodes (18): MockerFixture, dummy_request(), fakerandom(), Any, fixture, SimpleNamespace, Unit-tier fixtures with strict mocking and in-memory fakes., Provide deterministic random seed for unit tests. (+10 more)

### Community 22 - "connection_manager_methods.py"
Cohesion: 0.02
Nodes (117): broadcast_room_event_impl(), broadcast_to_room_impl(), check_all_connections_health_impl(), check_connection_health_impl(), disconnect_websocket_connection_impl(), get_active_connection_count_impl(), get_connection_count_impl(), get_connection_health_stats_impl() (+109 more)

### Community 23 - "test_admin_shutdown_command.py"
Cohesion: 0.04
Nodes (77): _asyncio_mark, _await_shutdown_result(), _InitiateAppStub, _InitiateStateStub, _PendingCheckAppStub, _PendingCheckStateStub, Unit tests for admin shutdown command handler. Tests the shutdown command…, Test handle_shutdown_command() when player service is not available. (+69 more)

### Community 24 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (124): asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not…, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes. (+116 more)

### Community 25 - "inventory_item_matching.py"
Cohesion: 0.07
Nodes (35): build_drop_candidates(), build_equipped_candidates(), build_inventory_candidates(), clean_item_value(), extract_item_identifier(), match_equipped_item_by_name(), match_prefix_drop(), match_substring_drop() (+27 more)

### Community 26 - "test_security_validator.py"
Cohesion: 0.01
Nodes (212): field_validator, Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., Validate combat target name format using centralized validation., field_validator, Validate target player name format using centralized validation. (+204 more)

### Community 27 - "ApplicationContainer"
Cohesion: 0.01
Nodes (396): Decayed corpse cleanup for the game tick loop., _log_memory_metrics_periodically(), Application lifecycle management for MythosMUD server. This module handles…, Log memory leak metrics periodically. Args: collector:…, Perform application startup and return initialized container. Args: app:…, _startup_application(), _create_npc_services_on_app(), _ensure_room_cache_before_npc_startup() (+388 more)

### Community 28 - "NPCDefinitionCRUDMixin"
Cohesion: 0.05
Nodes (45): NPCDefinitionCRUDMixin, Any, AsyncSession, Execute create_npc_definition stored procedure and return the created…, Validate create_npc_definition parameters. Raises ValueError if invalid., Log successful NPC definition creation., Validate NPC update parameters., Add a simple field to update_data if value is not None. (+37 more)

### Community 29 - "TargetMatch"
Cohesion: 0.03
Nodes (100): Resolve a typed target match for the given name in the current context., NpcSpellDamageTarget, SpellEffects engine surface for spell_effects_heal (no import cycle with…, Minimal NPC surface for spell damage, steal-life, and NATS publish helpers., True if the NPC is still alive (structural typing stub for pyright)., Apply damage; return True if the instance accepted the hit., Current combat stats (e.g. current_dp, max_dp) for events and UI sync., SpellEffectsEngineHealPort (+92 more)

### Community 30 - "LoggedHTTPException"
Cohesion: 0.02
Nodes (201): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Any, post, Request, ValidationError, Respawn a delirious player at the Sanitarium with restored lucidity. This…, Respawn a dead player at their respawn location with full DP. This endpoint… (+193 more)

### Community 31 - "Communities (355 total, 223 thin omitted)"
Cohesion: 0.02
Nodes (133): Communities (355 total, 223 thin omitted), Community 0 - "Nyarlathotep Avatars", Community 100 - "Call Daoloth / Daoloth", Community 101 - "Call Nyogtha / Clutch of Nyogtha", Community 102 - "Call Saaitii / Saaitii", Community 103 - "Call Zu-Che-Quon / Enchant Bells of Horror", Community 104 - "Cast Out Shan / Shaggai", Community 105 - "Casting the Runes / Elder Sign" (+125 more)

### Community 32 - "pydantic.md"
Cohesion: 0.03
Nodes (116): apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest, post (+108 more)

### Community 33 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (134): DropCommand, EquipCommand, GetCommand, InventoryCommand, PickupCommand, PutCommand, field_validator, model_validator (+126 more)

### Community 34 - "test_combat.py"
Cohesion: 0.02
Nodes (103): Unit tests for combat models. Tests the combat system models including enums,…, Test is_alive returns True for player with negative DP above -10., Test is_alive returns False for player with DP at -10 threshold., Test is_alive returns False for player with DP below -10., Test is_alive returns False for inactive player even with positive DP., Test is_alive returns True for NPC with positive DP., Test is_alive returns False for NPC with 0 DP., Test is_alive returns False for NPC with negative DP. (+95 more)

### Community 35 - "test_user_manager.py"
Cohesion: 0.02
Nodes (139): mock_data_dir(), asyncio, fixture, Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel. (+131 more)

### Community 36 - "test_player_position_service.py"
Cohesion: 0.05
Nodes (46): asyncio, Unit tests for player position service. Tests the PlayerPositionService for…, Test change_position raises ValueError for invalid position., Test change_position returns error when no persistence., Test change_position returns error when player not found., Test change_position returns already message when already in position., Test PlayerPositionService initialization., Test change_position successfully changes position. (+38 more)

### Community 37 - "test_event_publisher_helpers.py"
Cohesion: 0.14
Nodes (14): event_publisher(), mock_nats_service(), fixture, Unit tests for event publisher helper functions. Tests the helper functions in…, Create a mock NATS service., Create an EventPublisher instance., Test _create_event_message() creates event message., Test get_next_sequence_number() increments sequence. (+6 more)

### Community 38 - "test_nats_service.py"
Cohesion: 0.03
Nodes (90): asyncio, Unit tests for NATS service. Tests the NATSService class and NATSMetrics., Test NATSService initialization with dict config., Test NATSService initialization with None config., Test NATSService initialization with subject manager., Test NATSService initializes connection pool structures., Test NATSService initializes message batching structures., Test connect() successfully connects to NATS. (+82 more)

### Community 39 - "NPCMovementIntegration"
Cohesion: 0.05
Nodes (44): NPCMovementIntegration, Room, Get room objects and validate they exist. Args: npc_id: ID of the NPC…, Update room occupancy by removing NPC from source and adding to destination.…, Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…, Move an NPC to a different room with full integration. This method provides…, Get the current room ID for an NPC. Args: npc_id: ID of the NPC Returns:…, Get list of NPC IDs in a room. Args: room_id: ID of the room Returns:… (+36 more)

### Community 40 - "LootAllRequest"
Cohesion: 0.04
Nodes (81): _audit_loot_all(), _build_loot_all_response(), loot_all_items(), Any, APIRouter, Request, Container loot-all endpoint. Handles the convenience action to transfer all…, Register loot-all endpoint to the router. (+73 more)

### Community 41 - "test_command_communication.py"
Cohesion: 0.03
Nodes (88): EmoteCommand, LocalCommand, MeCommand, PoseCommand, Communication command models for MythosMUD. This module provides command models…, Command for whispering to a specific player., Command for replying to the last whisper received., Command for saying something to other players in the room. (+80 more)

### Community 42 - "test_connection_cleaner.py"
Cohesion: 0.06
Nodes (45): connection_cleaner(), mock_cleanup_dead_websocket(), mock_get_async_persistence(), mock_has_websocket_connection(), mock_memory_monitor(), mock_message_queue(), mock_rate_limiter(), mock_room_manager() (+37 more)

### Community 43 - "test_command_processing.py"
Cohesion: 0.10
Nodes (30): _dispatch_parsed_command(), _handle_processing_error(), _handle_validation_error(), _log_security_sensitive_command(), _parse_command_line_or_client_error(), process_command_with_validation(), CommandExecutionRequest, Exception (+22 more)

### Community 44 - "test_manager.py"
Cohesion: 0.02
Nodes (82): fixture, Unit tests for NATS Subject Manager. Tests the NATSSubjectManager class., Test build_subject() raises SubjectValidationError for invalid parameter., Test build_subject() raises SubjectValidationError when subject too long., Test validate_subject() returns True for valid subject., Test validate_subject() returns False for invalid subject., Test validate_subject() accepts events.domain.{event_type} (distributed…, Test validate_subject() returns False for empty subject. (+74 more)

### Community 45 - "UtilityCommandFactory"
Cohesion: 0.03
Nodes (106): Unit tests for utility command factories. Tests the UtilityCommandFactory class…, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+98 more)

### Community 46 - "legacy_error_sanitization.py"
Cohesion: 0.05
Nodes (44): _collect_safe_context_fields(), _contains_sensitive_detail_pattern(), is_safe_detail_key(), Sanitization helpers for legacy MythosMUD error responses. Extracted from…, Sanitize dictionary detail values, keeping only safe keys., Sanitize each element in a list detail value., Return detail dict entries that use safe keys with sanitized values., Sanitize a detail value to prevent information exposure. Uses bleach for HTML… (+36 more)

### Community 47 - "test_container_websocket_events.py"
Cohesion: 0.09
Nodes (41): emit_container_closed(), emit_container_decayed(), emit_container_opened(), emit_container_opened_to_room(), emit_container_updated(), Any, ContainerComponent, datetime (+33 more)

### Community 48 - "test_command_factories.py"
Cohesion: 0.14
Nodes (13): Unit tests for command factories. Tests the CommandFactory class., Test create_sit_command delegates to exploration factory., Test create_drop_command delegates to inventory factory., Test create_kick_command delegates to combat factory., Test create_alias_command delegates to utility factory., Test create_aliases_command delegates to utility factory., Test create_reply_command delegates to communication factory., test_create_alias_command() (+5 more)

### Community 49 - "MinimapRenderer"
Cohesion: 0.09
Nodes (17): MinimapRenderer, Any, Mini-map renderer for room connectivity visualization. This module provides…, Renders room connectivity graphs in various visual formats. Implements the…, Extract street acronym from room ID. Args: room_id: Full room ID (e.g.,…, Extract street name from room ID. Args: room_id: Full room ID Returns: Street…, Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…, Render the mini-map as ASCII art with grid-based visualization. Args:… (+9 more)

### Community 50 - "api/monitoring.py"
Cohesion: 0.06
Nodes (79): _assemble_health_response(), force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_health_status(), get_memory_alerts() (+71 more)

### Community 51 - "is_player_in_login_grace_period"
Cohesion: 0.03
Nodes (116): Get login grace period status for player., _as_grace(), cancel_login_grace_period(), _EffectPersistence, get_login_grace_period_remaining(), _grace_period_task(), _GraceApp, _GraceAppState (+108 more)

### Community 52 - "test_dead_letter_queue.py"
Cohesion: 0.11
Nodes (17): Unit tests for dead letter queue. Tests the DeadLetterQueue class and…, Test DeadLetterQueue initialization without storage directory., Test dequeue() returns None when queue is empty., Test dequeue() handles file read errors., Test get_statistics() returns stats for empty queue., Test list_messages() returns empty list when queue is empty., Test replay_message() retrieves and removes message., Test cleanup_old_messages() handles file errors. (+9 more)

### Community 53 - "NATSConnectionStateMachine"
Cohesion: 0.02
Nodes (96): ConnectionEvent, NATSConnectionStateMachine, Any, Enum, Exception, Connection state machine for NATS messaging. Implements a robust state machine…, Initialize connection state machine. Args: connection_id: Unique identifier for…, Called whenever state machine enters a new state. Logs state transitions for… (+88 more)

### Community 54 - "test_who_commands.py"
Cohesion: 0.03
Nodes (110): Utility commands for MythosMUD. This module contains handlers for utility…, filter_online_players(), filter_players_by_name(), format_player_entry(), format_player_location(), format_who_result(), get_players_for_who(), handle_who_command() (+102 more)

### Community 55 - "test_command_parser.py"
Cohesion: 0.01
Nodes (149): Smoke test for command parser., Test basic command parsing., Test command parsing with arguments., Test command parsing with pipes., test_parse_command_basic(), test_parse_command_with_args(), test_parse_command_with_pipes(), command_parser() (+141 more)

### Community 56 - "CombatService"
Cohesion: 0.01
Nodes (442): get_current_tick(), Shared game tick counter. Kept in a leaf module so combat services can read the…, Get the current game tick., Create CombatService with NATS and register it. Assumes NATS is connected., CombatEndedEvent, CombatStartedEvent, CombatTimeoutEvent, CombatTurnAdvancedEvent (+434 more)

### Community 57 - "pytest.md"
Cohesion: 0.01
Nodes (417): CharacterInfo, DependsParam, get_container, get_current_active_user, IntegrityError, _MapRooms, broadcast_message(), get_game_status() (+409 more)

### Community 58 - "Stats"
Cohesion: 0.03
Nodes (87): Character creation service for MythosMUD server. This module handles all…, generate_random_stats(), Generate Stats with random attribute values. Factory function for creating…, Service for generating random character statistics., Initialize the stats generator., StatsGenerator, Core character statistics with Lovecraftian horror elements., Get the modifier for a given attribute (standard D&D-style calculation). (+79 more)

### Community 59 - "command_handler_unified.py"
Cohesion: 0.03
Nodes (84): normalize_command(), Normalize command input by removing optional slash prefix. Supports both…, _check_all_command_blocks(), _check_casting_state(), _check_rate_limit(), _ensure_alias_storage(), _get_casting_block_result(), get_help_content() (+76 more)

### Community 60 - "_JSONDict"
Cohesion: 0.09
Nodes (14): _JSONDict, _loads_json_dict(), Get base stats as dictionary., Set base stats from dictionary., Get behavior configuration as dictionary., Set behavior configuration from dictionary., Get AI integration stub configuration as dictionary., Set AI integration stub configuration from dictionary. (+6 more)

### Community 61 - "ContainerComponent"
Cohesion: 0.01
Nodes (332): _equip_build_work(), _equip_inventory_rollback_snapshot(), EquipCommandInventoryStep, Equip command: move an item from inventory to an equipment slot., Inventory indices, slot choice, and rollback snapshot for equip., _ensure_shared_services_initialized(), Shared service initialization for inventory commands., Resolve async_persistence from the request and construct shared singletons. (+324 more)

### Community 62 - "WebSocket Best Practices"
Cohesion: 0.05
Nodes (43): 1. Code Organization and Structure, 2. Common Patterns and Anti-patterns, 3. Performance Considerations, 4. Security Best Practices, 5. Testing Approaches, 6. Common Pitfalls and Gotchas, 7. Tooling and Environment, Anti-patterns (+35 more)

### Community 63 - "test_message_queue.py"
Cohesion: 0.03
Nodes (57): Unit tests for message queue. Tests the message_queue module classes and…, Test MessageQueue.get_messages() retrieves and clears messages., Test MessageQueue.get_messages() returns empty list for player with no messages., Test MessageQueue.get_messages() handles errors., Test MessageQueue.__init__() with default values., Test MessageQueue.has_messages() returns True when player has messages., Test MessageQueue.has_messages() returns False when player has no messages., Test MessageQueue.has_messages() returns False for empty list. (+49 more)

### Community 64 - "Any"
Cohesion: 0.21
Nodes (7): Any, Render a single row of rooms with horizontal exits., Return the horizontal exit character (—, >, or <) given east/west exit state,…, Get exit character to display after a room for horizontal (east/west) exits.…, Determine map style from room data. Args: rooms: List of room dictionaries…, Build a coordinate grid from room data. Args: rooms: List of room dictionaries…, Get ASCII symbol for a room. Args: room: Room dictionary map_style: Current map…

### Community 65 - "submitAuth.ts"
Cohesion: 0.24
Nodes (14): AuthSessionSetters, persistTokensAndApplySession(), SetBool, SetChars, SetStep, toCharacterInfoFromLogin(), AuthSuccessPayload, SanitizedCredentials (+6 more)

### Community 66 - "test_exploration_service.py"
Cohesion: 0.04
Nodes (83): _async_session_maker_mock(), exploration_service(), mock_database_manager(), asyncio, fixture, Unit tests for exploration service. Tests the ExplorationService class., Test mark_room_as_explored() returns False when room not found., Test mark_room_as_explored() raises DatabaseError on database failure. (+75 more)

### Community 67 - "NATSService"
Cohesion: 0.06
Nodes (66): NATSUnsubscribeError, Raised when unsubscribe operations fail., NATSService, NATS service for handling pub/sub operations and real-time messaging. This…, Unsubscribe from a NATS subject. Args: subject: NATS subject name to…, Check if NATS client is connected and healthy. Returns: True if connected and…, Get the number of active subscriptions. Returns: Number of active subscriptions, _assert_tracked_coro_closed() (+58 more)

### Community 68 - "catatonia_check.py"
Cohesion: 0.04
Nodes (60): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+52 more)

### Community 69 - "chat_service.py"
Cohesion: 0.03
Nodes (99): ChatLogger, ChatPlayerService, ChatRateLimiter, ChatUserManager, Protocol, Player lookup used by channel senders., Mute and admin checks used by channel senders., Return True if the player has admin chat privileges. (+91 more)

### Community 70 - "test_database_helpers.py"
Cohesion: 0.05
Nodes (67): close_db(), ensure_database_directory(), get_async_session(), get_database_path(), get_session_maker(), init_db(), async_sessionmaker, AsyncSession (+59 more)

### Community 71 - "ExplorationCommandFactory"
Cohesion: 0.04
Nodes (73): Unit tests for exploration command factories. Tests the…, Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_sit_command() creates SitCommand., Test create_sit_command() raises error with args., Test create_lie_command() creates LieCommand., Test create_lie_command() with 'down' modifier. (+65 more)

### Community 72 - "patch"
Cohesion: 0.05
Nodes (32): asyncio, patch, Test get_npc_engine() uses NullPool for test databases., Test NPC session maker functions., Test get_npc_session_maker() returns session maker., Test NPC session management., Test get_npc_session() yields session., Test get_npc_session() rolls back on error during yield. (+24 more)

### Community 73 - "test_nats_message_handler_subzone_events.py"
Cohesion: 0.10
Nodes (19): Unit tests for NATS message handler subzone and event handling. Tests subzone…, Test get_event_subscription_count returns count., Test is_event_subscription_active checks subscription., Test _get_user_manager returns injected manager., Test _get_user_manager falls back to global manager., Test _get_event_handler_map delegates to event handler., Test _validate_event_message delegates to event handler., Test track_player_subzone_subscription handles player moving to different… (+11 more)

### Community 74 - "HealthStatus"
Cohesion: 0.06
Nodes (63): ConnectionsComponent, DatabaseComponent, HealthErrorResponse, HealthStatus, BaseModel, StrEnum, Health monitoring models for MythosMUD. This module contains Pydantic models…, Error response for health check failures. (+55 more)

### Community 75 - "ChatWhisperTracker"
Cohesion: 0.10
Nodes (14): Initialize chat service. Args: persistence: Database persistence layer…, ChatWhisperTracker, Tracks last whisper senders for reply functionality., Initialize the whisper tracker., Store the last whisper sender for a player. Args: receiver_name: Name of the…, Get the last whisper sender for a player. Args: player_name: Name of the player…, Clear the last whisper sender for a player. Args: player_name: Name of the…, Get all whisper trackings (for testing/debugging). Returns: Dictionary mapping… (+6 more)

### Community 76 - "test_websocket_helpers.py"
Cohesion: 0.04
Nodes (57): is_client_disconnected_exception(), load_player_mute_data(), BaseException, Load player mute data when they connect. AI: Uses async version to avoid…, True if the exception indicates the client disconnected (tab close, navigate…, asyncio, LogCaptureFixture, Unit tests for WebSocket helpers. Tests the websocket_helpers module functions.… (+49 more)

### Community 77 - "_MagicServiceCore"
Cohesion: 0.06
Nodes (34): _CombatTickState, _MagicServiceCore, _PlayerPersistence, JsonMap, Protocol, UUID, Load player and return normalized stats (MP/max_MP). Returns (player, stats) or…, Return (False, message) if not enough MP, else (True, ''). (+26 more)

### Community 78 - "RoomLoader"
Cohesion: 0.03
Nodes (75): option, fixture, Create a temporary directory for testing., temp_dir(), Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer (+67 more)

### Community 79 - "CombatMonitoringService"
Cohesion: 0.08
Nodes (17): CombatMonitoringService, Comprehensive combat monitoring and alerting service. Tracks combat system…, Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier…, Start monitoring a combat turn. Args: combat_id: Unique combat identifier, End monitoring a combat turn. Args: combat_id: Unique combat identifier, Record a combat error. Args: error_type: Type of error (validation, timeout,…, Resolve an alert. Args: alert_id: Alert identifier Returns: bool: True if alert… (+9 more)

### Community 80 - "Alias"
Cohesion: 0.04
Nodes (63): Alias, BaseModel, Alias model for command aliases. Stores player command aliases for quick access…, String representation of the alias., Check equality based on name and command., Hash based on name and command for use in sets/dicts., Update the updated_at timestamp to current time., Check if the alias name conflicts with a reserved command. (+55 more)

### Community 81 - "security.ts"
Cohesion: 0.08
Nodes (25): SafeHtml(), SafeHtmlProps, fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler, collectWindowCandidates(), COMMAND_PROBE_CONFIG (+17 more)

### Community 82 - "test_command_validator.py"
Cohesion: 0.03
Nodes (104): Unit tests for command validator., Test validate_command_length returns True for valid length., Test validate_command_length returns False for too long command., Test validate_command_length with custom max_length., Test validate_command_format returns True for valid command., Test validate_command_format returns False for empty command., Test validate_command_format returns False for suspicious command., Test validate_command_format returns False for too long command. (+96 more)

### Community 83 - "test_player_presence_tracker.py"
Cohesion: 0.04
Nodes (91): _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _disconnect_during_rest_is_intentional(), _get_instance_manager_from_manager(), Any, UUID, Player presence tracking helper for connection manager. This module provides… (+83 more)

### Community 84 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.06
Nodes (83): object, _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch() (+75 more)

### Community 85 - "test_look_player.py"
Cohesion: 0.04
Nodes (86): _get_visible_equipment(), Get visible equipment from player, excluding internal/hidden slots. Visible…, _apply_grace_period_labels(), _find_matching_players(), _format_player_look_display(), _get_players_in_room(), _handle_player_look(), _player_id_uuid() (+78 more)

### Community 86 - "test_websocket_handler_json_error.py"
Cohesion: 0.25
Nodes (7): mock_websocket(), asyncio, fixture, Unit tests for websocket handler JSON error handling. Tests the JSON decode…, Create a mock WebSocket., Test _handle_json_decode_error() sends error response., test_handle_json_decode_error()

### Community 87 - "test_health_service.py"
Cohesion: 0.04
Nodes (57): get_health_service(), Get the global health service instance. Args: connection_manager: Optional…, health_service(), mock_connection_manager(), fixture, patch, Unit tests for health service. Tests the health monitoring service for system…, Test check_database_health returns degraded status. (+49 more)

### Community 88 - "TargetResolutionService"
Cohesion: 0.06
Nodes (31): PersistenceProtocol, PlayerServiceProtocol, Player, Protocol, Room, UUID, Validate player exists and is in a room. Returns (room_id, error_result)., Clean target name and extract disambiguation suffix. Returns (clean_target,… (+23 more)

### Community 89 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (90): _collect_rotatable_logs(), detect_environment(), ensure_log_directory(), BoundLogger, Path, Logging utilities for directory management, path resolution, and environment…, Resolve log_base path to absolute path relative to project root. Args:…, Collect non-empty log files eligible for rotation. (+82 more)

### Community 90 - "test_lifespan_helpers.py"
Cohesion: 0.12
Nodes (29): _calculate_metrics_delta(), _cleanup_container_on_error(), _initialize_enhanced_systems(), lifespan(), _persist_metrics_to_file(), _persist_mythos_state_on_error(), Any, FastAPI (+21 more)

### Community 91 - "ChatService"
Cohesion: 0.04
Nodes (35): ChatService, UUID, Chat service for handling real-time communication between players. This service…, Send a local message to players in the same sub-zone. This method publishes the…, Send a global message to all players. This method publishes the global message…, Send a party (ephemeral group) chat message. Only current party members receive…, Send a system message to all players. This method publishes the system message…, Publish a say-shaped room message from an NPC (no player lookup). (+27 more)

### Community 92 - "npc_admin_mgmt_api.py"
Cohesion: 0.07
Nodes (47): cleanup_admin_sessions(), get_admin_audit_log(), get_admin_sessions(), get, post, Request, Admin session and audit log endpoints under /admin/npc. Split out from…, Get active admin sessions. (+39 more)

### Community 93 - "test_combat_monitoring_service.py"
Cohesion: 0.04
Nodes (47): Unit tests for combat monitoring service. Tests the CombatMonitoringService…, Test end_combat_monitoring with failed combat., Test end_combat_monitoring when combat not found., Test start_turn_monitoring tracks turn., Test end_turn_monitoring updates metrics., Test end_turn_monitoring when turn not found., Test record_combat_error with validation error., Test record_combat_error with timeout error. (+39 more)

### Community 94 - "test_npc_combat_integration_service.py"
Cohesion: 0.04
Nodes (75): integration_service(), asyncio, MonkeyPatch, Unit tests for NPC combat integration service. Tests the…, Test init sets NPC combat integration reference on shared PlayerCombatService., Test init creates CombatService when combat_service is None., Test integration service has combat service with config., Test auto_progression_enabled is set on combat service. (+67 more)

### Community 95 - "CorpseOverlay.tsx"
Cohesion: 0.04
Nodes (71): BackpackTab(), BackpackTabProps, ContainerSplitPane(), ContainerSplitPaneProps, ContainerInventoryPaneProps, ContainerItemRow(), ContainerSplitPaneView(), ContainerSplitPaneViewModel (+63 more)

### Community 96 - "QuestService"
Cohesion: 0.04
Nodes (83): Schedule personal system chat from sync or async callers., schedule_personal_system(), Persist player after spell mutations., Quest subsystem: service, goal progression, rewards., _as_int(), _goal_is_met(), notify_quest_abandoned(), notify_quest_completed() (+75 more)

### Community 97 - "test_npc_definitions_api.py"
Cohesion: 0.09
Nodes (55): create_npc_definition(), delete_npc_definition(), get_npc_definition(), get_npc_definitions(), AsyncSession, delete, get, post (+47 more)

### Community 98 - "test_connection_establishment.py"
Cohesion: 0.06
Nodes (87): _as_mgr(), _as_ws(), _FakeWebSocket, _make_manager(), _meta(), _player_with_room(), asyncio, ConnectionMetadata (+79 more)

### Community 99 - "_def_row"
Cohesion: 0.11
Nodes (18): _def_row(), Test get_npc_definition_by_name() matches case-insensitively., Test get_npc_definition_by_name() returns None when not found., Test create_npc_definition() successfully creates definition., Test create_npc_definition() handles base_stats., Test delete_npc_definition() successfully deletes definition., Test create_spawn_rule() raises ValueError when max < min., Test get_npc_definitions_by_type() filters by type. (+10 more)

### Community 100 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (87): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+79 more)

### Community 101 - "test_look_room.py"
Cohesion: 0.03
Nodes (102): _filter_other_players(), _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id() (+94 more)

### Community 102 - "NATSMetrics"
Cohesion: 0.04
Nodes (42): NATSMetrics, Any, NATS-specific metrics collection for monitoring and alerting., Record publish operation metrics., Record subscribe operation metrics., Record batch flush operation metrics., Update connection health score (0-100)., Update connection pool utilization (0-1). (+34 more)

### Community 103 - "EldritchIcon.tsx"
Cohesion: 0.04
Nodes (56): ChatMessage, ChatMessageType, ChatPanelTest(), mockClick, mockCreateObjectURL, mockRevokeObjectURL, DraggablePanelResizeHandles(), DraggablePanelResizeHandlesProps (+48 more)

### Community 104 - "CorpseLifecycleService"
Cohesion: 0.08
Nodes (29): CorpseLifecycleService, _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Create a corpse container when a player dies., True if player may access corpse (owner/admin always; others after grace). (+21 more)

### Community 105 - "Reporter"
Cohesion: 0.03
Nodes (47): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+39 more)

### Community 106 - "executeCommand"
Cohesion: 0.10
Nodes (50): expectWhoListingOnPage(), primeBothForCoLocate(), waitForLookReflected(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers() (+42 more)

### Community 107 - "test_database_init.py"
Cohesion: 0.04
Nodes (48): Reset the database connection state (for testing). This resets the…, reset_database(), fixture, Reset database state before each test., Test reset_database resets module-level _database_url., reset_db_state(), test_reset_database_resets_module_url(), fixture (+40 more)

### Community 108 - "test_rate_limiter_utils.py"
Cohesion: 0.04
Nodes (45): fixture, rate_limiter(), Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…, Test get_rate_limit_info calculates reset time correctly., Test get_rate_limit_info calculates retry_after correctly., Test get_rate_limit_info filters out old requests., Test enforce_rate_limit allows request within limit., Test enforce_rate_limit raises RateLimitError when limit exceeded. (+37 more)

### Community 109 - "test_websocket_helpers_player.py"
Cohesion: 0.07
Nodes (40): build_basic_player_data(), get_player_service_from_connection_manager(), get_player_stats_data(), Extract player service from connection manager using container pattern., Get and normalize player stats data., Build basic player data dictionary., asyncio, Unit tests for WebSocket helpers (player-related). Tests… (+32 more)

### Community 110 - "SubjectValidator"
Cohesion: 0.06
Nodes (44): Custom exceptions for NATS Subject Manager. This module defines all exception…, Exception raised when subject validation fails., SubjectValidationError, NATS Subject Manager for MythosMUD. This package provides centralized subject…, NATS Subject Manager for MythosMUD. This module provides centralized subject…, Performance metrics for NATS Subject Manager operations. This module provides…, Predefined subject patterns for MythosMUD chat system. This module contains all…, get_chat_subscription_patterns() (+36 more)

### Community 111 - "test_inventory_equip_command.py"
Cohesion: 0.14
Nodes (32): _equip_persist_or_rollback(), _equip_run_mutation(), _equip_success_payload(), _equip_target_slot_or_error(), _equip_try_inventory_swap(), EquipCommandRuntime, EquipCommandWork, handle_equip_command() (+24 more)

### Community 112 - "combat_service_npc.py"
Cohesion: 0.06
Nodes (58): DataProviderProtocol, _fallback_find_combat_id_for_npc(), find_participant_uuid_by_string_id(), get_combat_by_participant(), get_combat_id_for_npc(), get_combat_id_for_npc_via_mapping(), _get_data_provider(), _get_uuid_mapping() (+50 more)

### Community 113 - "NPCCommunicationIntegration"
Cohesion: 0.10
Nodes (23): NPCCommunicationIntegration, Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…, Process a message to determine if the NPC should respond. Args: npc_id: ID of…, Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…, Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…, Integrates NPCs with the existing chat and whisper systems. This class provides…, Initialize the NPC communication integration. Args: event_bus: Optional…, Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the… (+15 more)

### Community 114 - "test_rest_command.py"
Cohesion: 0.05
Nodes (65): _check_player_in_combat(), _check_rest_location(), handle_rest_command(), Handle /rest command for clean disconnection. Usage: /rest Behavior: - If in…, Check if a player is currently in combat. Args: player_id: The player's ID app:…, Check if the current room is a rest location (inn/hotel/motel). Args: room_id:…, mock_app(), mock_connection_manager() (+57 more)

### Community 115 - "UserManager"
Cohesion: 0.05
Nodes (49): datetime, UUID, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired player mutes. (+41 more)

### Community 116 - "SchemaValidator"
Cohesion: 0.03
Nodes (45): Path, Convert legacy string format exits to new object format internally. This allows…, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in… (+37 more)

### Community 117 - "GameClientV2.tsx"
Cohesion: 0.06
Nodes (38): calculateOccupantCount(), GameClientV2(), GameClientV2Content(), MainDockPanelId, MainDockSlotMeta, GameClientV2AuxiliaryPanels(), renderCharacterInfoPanel(), renderCommandHistoryPanel() (+30 more)

### Community 118 - "test_status_commands.py"
Cohesion: 0.04
Nodes (81): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_profession_info(), _get_status_persistence(), handle_status_command() (+73 more)

### Community 119 - "TestCombatConfigurationService"
Cohesion: 0.05
Nodes (20): Test suite for CombatConfigurationService class., Test CombatConfigurationService initialization., Test get_combat_configuration returns configuration., Test get_combat_configuration caches configuration., Test get_combat_configuration_for_scope with global scope., Test get_combat_configuration_for_scope with room scope., Test get_combat_configuration_for_scope with player scope., Test get_combat_configuration_for_scope with temporary scope. (+12 more)

### Community 120 - "real_time.py"
Cohesion: 0.07
Nodes (60): _ensure_connection_manager(), _extract_bearer_token(), handle_new_game_session(), _parse_subprotocol_token(), _parse_websocket_token(), Any, post, UUID (+52 more)

### Community 121 - "EventBus"
Cohesion: 0.00
Nodes (746): HolidayResolver, EventBus, AbstractEventLoop, Any, T, Task, Event bus for MythosMUD. This module provides the EventBus class that…, Set the main event loop - now properly managed for async compatibility. (+738 more)

### Community 122 - "test_quest_service.py"
Cohesion: 0.06
Nodes (82): _DefinitionRow, _FullInventory, _InstanceStub, _make_definition_row(), _make_kill_definition_row(), _make_turn_in_definition_row(), _message(), mock_def_repo() (+74 more)

### Community 123 - "test_combat_validator.py"
Cohesion: 0.06
Nodes (33): Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_combat_command with target name too long., Test validate_target_exists with case-insensitive match., Test validate_target_exists with empty target name., Test validate_target_alive when target is dead., Test validate_combat_state when in combat and combat required., Test validate_combat_state when in combat but combat not required., Test validate_combat_state when not in combat and combat not required. (+25 more)

### Community 124 - "test_alias_storage.py"
Cohesion: 0.02
Nodes (89): Unit tests for alias storage utilities. Tests the AliasStorage class for…, Open path is absolute str under realpath(storage_dir)., Test _load_alias_data returns default structure for nonexistent file., Test _load_alias_data loads existing alias file., Test _load_alias_data handles invalid JSON gracefully., Test _save_alias_data successfully saves data., Test get_player_aliases returns empty list for player with no aliases., Test get_player_aliases returns aliases from file. (+81 more)

### Community 125 - "useMythosAppActions.ts"
Cohesion: 0.10
Nodes (40): postSelectCharacter(), runAfterCharacterCreatedFlow(), isGracePeriodServerUnavailableError(), tryStartLoginGracePeriod(), runSelectCharacterFlow(), selectCharacterNetworkErrorMessage(), SelectCharacterResult, CONNECTION_ERROR_SUBSTRINGS (+32 more)

### Community 126 - "test_quest_commands.py"
Cohesion: 0.09
Nodes (38): ExitStack, handle_quest_command(), Handle quest command subcommands: abandon, ask, turnin. Usage: quest abandon…, current_user(), _enter_quest_command_patches(), mock_request(), asyncio, fixture (+30 more)

### Community 127 - "test_websocket_handler_core.py"
Cohesion: 0.03
Nodes (115): _attach_room_state_to_result(), handle_game_command(), _invoke_get_room_state_event(), parse_game_command_tokens(), process_websocket_command(), WebSocket, Handle a game command from a player. Args: websocket: The WebSocket connection…, Return get_room_state_event(player_id, room_id) coroutine factory, or None if… (+107 more)

### Community 128 - "test_logging_processors.py"
Cohesion: 0.04
Nodes (80): EventDict, configure_enhanced_structlog(), Configure enhanced Structlog with MDC, security, and performance features.…, add_correlation_id(), add_request_context(), _database_error_type(), _enhance_one_player_id(), enhance_player_ids() (+72 more)

### Community 129 - "test_lucidity_recovery_commands.py"
Cohesion: 0.05
Nodes (75): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+67 more)

### Community 130 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.11
Nodes (24): asyncio, Unit tests for channel broadcasting strategies. Tests the…, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() sends personal message., Test WhisperChannelStrategy.broadcast() handles missing target_player_id., Test SystemAdminChannelStrategy.broadcast() broadcasts globally. (+16 more)

### Community 131 - "_format_room_posture_message"
Cohesion: 0.17
Nodes (15): _format_room_posture_message(), Create a descriptive room message for posture changes., Unit tests for position command helper functions. Tests helper functions in…, Test _format_room_posture_message() formats sitting message., Test _format_room_posture_message() formats lying message., Test _format_room_posture_message() formats standing from lying message., Test _format_room_posture_message() formats standing from sitting message., Test _format_room_posture_message() formats standing with no previous position. (+7 more)

### Community 132 - "test_command_moderation.py"
Cohesion: 0.03
Nodes (81): AddAdminCommand, AdminCommand, MuteCommand, MuteGlobalCommand, MutesCommand, field_validator, Moderation command models for MythosMUD. This module provides command models…, Command for showing current mute status. (+73 more)

### Community 133 - "NATSRetryHandler"
Cohesion: 0.05
Nodes (64): NATSRetryHandler, Any, Exception, Calculate exponential backoff delay with jitter. Args: attempt: Current attempt…, Determine if a message should be retried. Args: message: Message that failed…, Retry a function with exponential backoff. Args: func: Async function to retry…, Get retry statistics. Returns: Dictionary with retry metrics AI: For monitoring…, Retry async function with exponential backoff. Attempts the function up to… (+56 more)

### Community 134 - "_utc_now"
Cohesion: 0.21
Nodes (12): datetime, Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE…, _utc_now(), Unit tests for lucidity model utility functions. Tests the _utc_now utility…, Test _utc_now returns a datetime object., Test _utc_now returns naive datetime (tzinfo=None)., Test _utc_now returns time close to current UTC time., Test _utc_now returns different times on subsequent calls. (+4 more)

### Community 135 - "chat_channel_message_senders.py"
Cohesion: 0.14
Nodes (34): ChatResult, _append_channel_history(), _authorize_global_sender(), _authorize_system_sender(), ChatPlayerView, ChatSendServices, _load_whisper_participants(), _log_and_store_system_message() (+26 more)

### Community 136 - "get_logger"
Cohesion: 0.00
Nodes (1011): _DropResolved, _FloorPickupResolved, create_validator(), Shared schema validator for room definition files. This module provides JSON…, Check if a room ID follows the unified naming schema. Args: room_id: Room ID to…, Create a schema validator with the specified schema. Args: schema_name: Name of…, Validates room definitions against JSON schema. This validator can be used by…, SchemaValidator (+1003 more)

### Community 137 - "get_username_from_user"
Cohesion: 0.07
Nodes (52): _get_ground_services(), handle_ground_command(), _normalize_player_ids(), Any, Get persistence and registry from request. Returns (persistence, registry)., Attempt to ground a catatonic ally back to 1 LCD., Validate ground command context and get rescuer. Returns (rescuer, error_dict)., Validate ground target and check same room. Returns (target, error_dict). (+44 more)

### Community 138 - "test_nats_broker.py"
Cohesion: 0.03
Nodes (77): asyncio, Unit tests for NATS message broker. Tests the NATSMessageBroker class., Test connect() passes TLS options to nats.connect when tls_enabled=True., Test disconnect() does nothing when no client., Test disconnect() successfully disconnects., Test disconnect() unsubscribes from all subscriptions., Test disconnect() handles unsubscribe errors gracefully., Test disconnect() raises MessageBrokerError on disconnect failure. (+69 more)

### Community 139 - ".load_room_data"
Cohesion: 0.06
Nodes (19): Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path., Validate or update room ID based on filename and location., Validate required fields are present., Add location fields if missing. (+11 more)

### Community 140 - "test_validation.py"
Cohesion: 0.03
Nodes (64): custom_length_validator(), fixture, Unit tests for NATS Subject Validator. Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter. (+56 more)

### Community 141 - "test_chat_service.py"
Cohesion: 0.03
Nodes (78): asyncio, Unit tests for chat service. Tests the ChatService class and ChatMessage class., Test send_say_message() when rate limited., Test send_say_message() when player is not in a room., Test send_local_message() with empty message., Test send_global_message() with empty message., Test ChatMessage initialization., Test send_emote_message() with empty action. (+70 more)

### Community 142 - "SpellEffectType"
Cohesion: 0.04
Nodes (113): List all spells, optionally filtered by school. Args: school: Optional school…, StrEnum, Spell data models for the magic system. This module contains Pydantic models…, Valid target types for spells., Valid range types for spells., Valid effect types for spells., SpellEffectType, SpellRangeType (+105 more)

### Community 143 - "test_lifecycle_periodic.py"
Cohesion: 0.06
Nodes (54): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD. This module defines configuration settings for…, Configuration for NPC lifecycle maintenance. This class centralizes all timing…, Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…, Check if NPC maintenance should run on this tick. Args: tick_count: Current…, Get a summary of all NPC configuration values. Returns: Dictionary containing…, Clean up old lifecycle records (delegates to lifecycle_periodic). (+46 more)

### Community 144 - "test_debrief_command.py"
Cohesion: 0.07
Nodes (47): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+39 more)

### Community 145 - "item_instance_persistence_async.py"
Cohesion: 0.08
Nodes (41): CreateItemInstanceInput, EnsureItemInstanceInput, TypedDict, Constants and shared types for async persistence layer. Extracted to keep…, Optional fields for create_item_instance. owner_type, owner_id, etc. with…, Optional fields for ensure_item_instance., Create a new item instance. Delegates to ItemRepository., create_item_instance_async() (+33 more)

### Community 146 - "log_with_context"
Cohesion: 0.07
Nodes (31): correct_request_context(), Demonstrate correct request context binding., add_request_context(), Add request context to all log entries using enhanced logging., WebSocket connection manager with enhanced logging., Establish WebSocket connection with enhanced logging., Disconnect WebSocket with enhanced logging., Send message to specific client with enhanced logging. (+23 more)

### Community 147 - "persistence/container_persistence.py"
Cohesion: 0.04
Nodes (107): ContainerData, ContainerDataCore, Container data class for persistence operations., Identity and placement fields for a container row., Data class for container information., Convert container data to dictionary. Returns dictionary with model field names…, Validate lock_state parameter. Args: lock_state: Lock state to validate Raises:…, validate_lock_state() (+99 more)

### Community 148 - "server/schemas/__init__.py"
Cohesion: 0.06
Nodes (80): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+72 more)

### Community 149 - "test_connection_session_management.py"
Cohesion: 0.06
Nodes (77): _cleanup_old_session_tracking(), _cleanup_player_data_for_session(), _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), handle_new_game_session_impl(), _is_websocket_connected(), Protocol, UUID (+69 more)

### Community 150 - "test_player_combat_service.py"
Cohesion: 0.06
Nodes (48): asyncio, Unit tests for player combat service. Tests the PlayerCombatService class for…, Test clear_player_combat_state clears state., Test is_player_in_combat_sync returns False when not in combat., Test is_player_in_combat checks combat state., Test get_players_in_combat returns list of players., Test handle_combat_start tracks combat state., Test handle_combat_end clears combat states. (+40 more)

### Community 151 - "useRespawnHandlers.ts"
Cohesion: 0.09
Nodes (38): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), formatNpcAttackedLine() (+30 more)

### Community 152 - "test_active_lucidity_service.py"
Cohesion: 0.05
Nodes (59): active_lucidity_service(), mock_session(), asyncio, fixture, Unit tests for active lucidity service. Tests the ActiveLucidityService class…, Test apply_encounter_lucidity_loss() for acclimated encounter., Test apply_encounter_lucidity_loss() raises error for unknown category., Test apply_encounter_lucidity_loss() handles string player_id. (+51 more)

### Community 153 - "test_player_disconnect_handlers.py"
Cohesion: 0.06
Nodes (42): _collect_disconnect_keys(), Player, Collect all keys (UUID and string) that need to be removed for player…, mock_connection_manager(), mock_player(), fixture, Unit tests for player disconnect handlers. Tests the player disconnect handling…, Test _collect_disconnect_keys collects user_id when available. (+34 more)

### Community 154 - "test_websocket_handler_helpers_extended.py"
Cohesion: 0.05
Nodes (57): mock_connection_manager(), mock_validator(), mock_websocket(), asyncio, fixture, Extended unit tests for websocket handler helper functions. Tests additional…, Test _send_error_response() handles WebSocketDisconnect., Test _send_error_response() returns False for RuntimeError indicating… (+49 more)

### Community 155 - "quest_commands.py"
Cohesion: 0.08
Nodes (45): _active_npc_ids_in_room(), _emit_npc_lines_for_results(), _format_goal_line(), _format_one_quest_entry(), _format_quest_action_results(), _format_quest_log(), _get_container_and_persistence(), _get_quest_service() (+37 more)

### Community 156 - "test_aggro_threat.py"
Cohesion: 0.05
Nodes (91): _apply_taunt_and_maybe_broadcast(), Apply taunt and broadcast target switch if aggro changed. Returns error dict or…, add_damage_threat(), add_heal_threat(), _aggression_scale(), apply_stealth_wipe(), apply_taunt(), clear_aggro_for_combat() (+83 more)

### Community 157 - "test_combat_service.py"
Cohesion: 0.07
Nodes (57): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+49 more)

### Community 158 - "test_combat_attack_handler.py"
Cohesion: 0.03
Nodes (71): CombatAttackHandler, Any, UUID, Apply damage to target and update combat state. Args: combat: Combat instance…, Validate attack and retrieve combat participants. Args: attacker_id: ID of the…, Handles combat attack processing and damage application., Initialize the attack handler. Args: combat_service: Reference to the parent…, Validate that attack is allowed. (+63 more)

### Community 159 - "test_admin_commands.py"
Cohesion: 0.05
Nodes (66): handle_mute_command(), handle_unmute_command(), Handle the mute command for muting other players. Args: command_data: Command…, Handle the unmute command for unmuting other players. Args: command_data:…, asyncio, Unit tests for admin command handlers. Tests the admin command handler…, Test handle_mute_command() with no target player., Test handle_mute_command() successful execution. (+58 more)

### Community 160 - "ContainerService"
Cohesion: 0.08
Nodes (61): AbstractContextManager, ContainerService, Service for managing container operations. Orchestrates open/close, transfer…, MutationDecision, Result of attempting to acquire a guarded mutation context., UUID, Acquire a guarded mutation context for the given player. Args: player_id: The…, _container() (+53 more)

### Community 161 - "test_player_service.py"
Cohesion: 0.06
Nodes (45): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service CRUD and lookup. Delete, location, mythos status,…, Test get_player_by_id() when player is not found., Test get_player_by_name() when player is found., Test get_player_by_name() when player is not found. (+37 more)

### Community 162 - "test_combat_handler.py"
Cohesion: 0.07
Nodes (52): _AppStatePersistence, _AppWithPersistence, _as_app_with_state(), _CmdType, _handler_with_persistence(), mock_persistence(), AppWithState, asyncio (+44 more)

### Community 163 - "test_admin_setlucidity_command.py"
Cohesion: 0.06
Nodes (70): _apply_lucidity_change(), _check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), _get_current_lcd(), _get_player_service_from_app(), _handle_admin_set_lucidity_command() (+62 more)

### Community 164 - "RoomIDUtils"
Cohesion: 0.07
Nodes (35): Any, Check if NPC room IDs match target room IDs using fallback comparison. Args:…, Check if NPC room matches target room using normalized comparison. Args:…, Utilities for room ID normalization and comparison., Initialize room ID utilities. Args: connection_manager: ConnectionManager…, Get canonical room ID for consistent comparison. Args: room_id: The room ID…, Normalize room ID for comparison. Args: rid: Room ID to normalize Returns:…, Check if two normalized room IDs match. Args: id1: First normalized room ID… (+27 more)

### Community 165 - "HealthService"
Cohesion: 0.09
Nodes (23): HealthStatus, HealthComponents, Health status for all system components., HealthService, Any, Async database health check., check_database_health., Check connection manager health. (+15 more)

### Community 166 - "RoomService"
Cohesion: 0.02
Nodes (148): RoomDictList, build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession (+140 more)

### Community 167 - "get_admin_auth_service"
Cohesion: 0.11
Nodes (39): despawn_npc_instance(), get_npc_instances(), get_npc_stats(), move_npc_instance(), Any, delete, get, NPCSpawnRequest (+31 more)

### Community 168 - "test_go_command.py"
Cohesion: 0.05
Nodes (78): _cancel_rest_if_moving(), _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement(), handle_go_command(), _movement_combat_and_event_bus_from_go_app(), _movement_service_for_go_command(), Any (+70 more)

### Community 169 - "coerce_int"
Cohesion: 0.08
Nodes (28): Get player stats as dictionary. Returns a MutableDict instance that…, Set player stats from dictionary. Accepts both plain dict and MutableDict…, Check if player is alive (DP > 0)., Check if player is mortally wounded (0 >= DP > -10). Returns: True if player…, Check if player is dead (DP <= -10). Returns: True if player has -10 DP or below, Get player's current health state. Returns: "alive" if DP > 0…, Get stats used for combat participant creation. Returns current_dp, max_dp, and…, Get player determination points (DP) as percentage. (+20 more)

### Community 170 - "PlayerRoomEventHandler"
Cohesion: 0.08
Nodes (28): OccupantSnap, _as_map(), _as_occupant_snap(), PlayerRoomEventHandler, JsonMap, UUID, Handles room-related player events (entered, left, occupants)., Initialize room event handler from a deps bundle. (+20 more)

### Community 171 - "CombatAuditLogger"
Cohesion: 0.05
Nodes (59): CombatAttackDetails, CombatAuditLogger, CombatMonitoringAlert, CombatParties, CombatSecurityEvent, Any, datetime, Combat-specific audit logging and monitoring. This module provides specialized… (+51 more)

### Community 172 - "CombatInstance"
Cohesion: 0.04
Nodes (80): CombatInstance, UUID, Represents an active combat instance., Get the participant whose turn it is., Advance to the next round - all participants act each round. In round-based…, Check if combat should end. CRITICAL: Combat should NOT end when a player is…, Get all participants that are not dead (includes mortally wounded players at 0…, Update the last activity tick and datetime. (+72 more)

### Community 173 - "test_logging_handlers.py"
Cohesion: 0.04
Nodes (65): _aggregator_handler_class_for_windows(), AsyncioConnLostWriteFilter, create_aggregator_handler(), _make_exec_for_aggregator(), Any, LogRecord, Path, RotatingFileHandler (+57 more)

### Community 174 - "test_alias_commands.py"
Cohesion: 0.06
Nodes (58): _extract_alias_params(), handle_alias_command(), Any, Extract alias_name and command from command_data. Returns (alias_name, command)., Handle the alias command for creating and viewing aliases. Args: command_data:…, mock_alias(), mock_alias_storage(), asyncio (+50 more)

### Community 175 - "test_combat_flee_helpers.py"
Cohesion: 0.05
Nodes (62): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules. Keeps…, Application object with a ``state`` namespace (dynamic attributes)., _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id() (+54 more)

### Community 176 - "MonitoringDashboard"
Cohesion: 0.06
Nodes (41): PerformanceStats, Alert, MonitoringDashboard, MonitoringSummary, Any, Get comprehensive monitoring summary. Returns: Complete monitoring summary with…, Evaluate thresholds and record new alerts., Record a custom alert emitted by subsystems. Args: alert_type: Identifier for… (+33 more)

### Community 177 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.05
Nodes (56): _lucidity_change_payload_with_liabilities(), mock_send_game_event(), asyncio, fixture, LiabilityStackEntry, Unit tests for lucidity event dispatcher. Tests the lucidity event broadcasting…, Test liability formatting skips entries with empty code., Test send_lucidity_change_event with basic parameters. (+48 more)

### Community 178 - "MagicServiceHealingMixin"
Cohesion: 0.23
Nodes (10): MagicServiceHealingMixin, Any, UUID, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or…, True if effect result indicates healing was applied (success, effect_applied,… (+2 more)

### Community 179 - "test_room_renderer.py"
Cohesion: 0.04
Nodes (69): Unit tests for room_renderer utility functions. Tests the utility functions in…, Test clone_room_drops() returns empty list for None., Test format_room_drop_lines() formats room drops., Test format_room_drop_lines() returns empty message for empty drops., Test format_room_drop_lines() handles None., Test format_room_drop_lines() uses fallback for missing item_name., Test build_room_drop_summary() returns newline-separated summary., Test build_room_drop_summary() handles empty drops. (+61 more)

### Community 180 - "test_level_service.py"
Cohesion: 0.05
Nodes (56): level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level(), UUID (+48 more)

### Community 181 - "test_party_service.py"
Cohesion: 0.04
Nodes (52): party_service(), fixture, Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves. (+44 more)

### Community 182 - "LRUCache"
Cohesion: 0.08
Nodes (20): K, LRUCache, Put an item into the cache. Args: key: The key to store value: The value to…, Delete an item from the cache. Args: key: The key to delete Returns: True if…, Clear all items from the cache., Get the current number of items in the cache., Check if the cache is at maximum capacity., Get cache statistics. Returns: Dictionary containing cache statistics (+12 more)

### Community 183 - "MemoryMonitor"
Cohesion: 0.08
Nodes (29): _max_connection_age_seconds(), MemoryMonitor, Any, Get memory-related alerts based on current usage and connection statistics.…, Update the last cleanup time to the current time., Force garbage collection to free memory., Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops., Monitor memory usage and trigger cleanup when needed. This class provides… (+21 more)

### Community 184 - "test_hallucination_services.py"
Cohesion: 0.06
Nodes (43): HallucinationFrequencyService, Any, AsyncSession, UUID, Check if hallucination should trigger on room entry (Uneasy tier). Args:…, Check if hallucination should trigger based on time (Fractured/Deranged tiers).…, Service for managing hallucination frequency checks based on player tier., Initialize the hallucination frequency service. (+35 more)

### Community 185 - "monitoring_models.py"
Cohesion: 0.07
Nodes (40): AlertResolveResponse, AlertsResponse, CacheMetricsResponse, ConnectionHealthStatsResponse, DualConnectionStatsResponse, EventBusMetricsResponse, IntegrityResponse, MemoryAlertsResponse (+32 more)

### Community 186 - "test_metrics.py"
Cohesion: 0.03
Nodes (60): Initialize NATS Subject Manager. Args: enable_cache: Enable validation result…, Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, Reset all metrics to zero., Performance metrics for NATS Subject Manager operations. Tracks validation…, Record a validation operation. Args: duration: Time taken in seconds success:…, Record a build operation. Args: duration: Time taken in seconds success:… (+52 more)

### Community 187 - "test_player_event_handlers_utils.py"
Cohesion: 0.12
Nodes (15): Unit tests for player event handler utilities. Tests the…, Test normalize_event_ids() with string IDs., Test process_dict_occupant() processes player occupant., Test build_occupants_snapshot_data() with empty list., Test count_occupants_by_type() with empty list., Test is_player_disconnecting() returns False when player is not disconnecting., Test is_player_disconnecting() handles invalid player_id., Test normalize_player_id() with None returns None without warning. (+7 more)

### Community 188 - "fixtures/auth.ts"
Cohesion: 0.06
Nodes (55): forceLogoutPlayer(), assertCommandChannelReady(), assertNoRestDisconnectPollution(), assertNotStuckOnLogin(), clickWithoutStability(), EnsurePlayableConnectionOptions, executeCommandTrusted(), getLivePageForUsername() (+47 more)

### Community 189 - "test_websocket_handler_coverage_gaps.py"
Cohesion: 0.07
Nodes (42): asyncio, Unit tests to fill coverage gaps in websocket_handler.py. These tests target…, Test handle_game_command exception handling path (lines 472-480)., Test handle_game_command RuntimeError handling path (lines 472-480)., Test process_websocket_command resolves connection_manager from app when None…, Test handle_chat_message resolves connection_manager from app when None (lines…, Test handle_chat_message exception handling path (lines 666-674)., Test handle_chat_message RuntimeError handling path (lines 666-674). (+34 more)

### Community 190 - "realtime/realtime.py"
Cohesion: 0.10
Nodes (30): get_connection_statistics(), get_player_connections(), get, Request, Get connection information for a player. Returns detailed connection metadata…, Get comprehensive connection statistics. Returns detailed statistics about all…, Realtime domain schemas: realtime API, NATS messages, WebSocket messages., ErrorStatistics (+22 more)

### Community 191 - "server/persistence/__init__.py"
Cohesion: 0.13
Nodes (25): Persistence package for MythosMUD. This package contains persistence utilities…, # NOTE: PersistenceLayer and get_persistence removed - all code now uses…, # NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from…, create_item_instance(), ensure_item_instance(), _execute_item_instance_upsert(), get_item_instance(), _handle_item_instance_db_error() (+17 more)

### Community 192 - "ChatHistoryPanel.tsx"
Cohesion: 0.08
Nodes (30): ChatMessage(), ChatMessageProps, formatTimestamp(), getFontSizeClass(), getMessageClass(), ChatMessagesList(), ChatMessagesListProps, ChatHistoryMessageBody() (+22 more)

### Community 193 - ".__post_init__"
Cohesion: 0.03
Nodes (73): Event subscription setup for application startup. Extracted from…, Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), subscribe_room_occupants_refresh(), QuestCompleted, Initialize the event with proper type., Initialize the event with proper type. (+65 more)

### Community 194 - "test_config_init.py"
Cohesion: 0.17
Nodes (11): Unit tests for config module initialization., Test that get_config() returns fresh instances in test mode., Test that config has server configuration., Test that config has database configuration., Test that config has game configuration., Test that get_config() returns an AppConfig object., test_get_config_fresh_instances_in_test_mode(), test_get_config_has_database_config() (+3 more)

### Community 195 - "test_logout_commands.py"
Cohesion: 0.03
Nodes (112): _clear_corrupted_cache_entry(), _disconnect_player_connections(), _force_disconnect_player(), _get_app_services(), _get_player_for_logout(), _get_player_position_from_connection_manager(), handle_logout_command(), handle_quit_command() (+104 more)

### Community 196 - "ExceptionTracker"
Cohesion: 0.05
Nodes (45): ExceptionContextTrackInput, ExceptionRecord, ExceptionStats, ExceptionTracker, ExceptionTrackInput, get_exception_tracker(), Any, Exception (+37 more)

### Community 197 - "test_combat_messaging_integration.py"
Cohesion: 0.05
Nodes (56): asyncio, Unit tests for combat messaging integration. Tests the…, Test broadcast_combat_attack handles personal message errors gracefully., Test broadcast_combat_death broadcasts death event., Test broadcast_combat_ended broadcasts combat ended event., Test broadcast_combat_end broadcasts combat end event., Test broadcast_combat_error sends error to player., Test broadcast_player_mortally_wounded broadcasts message. (+48 more)

### Community 198 - "test_target_resolution_service.py"
Cohesion: 0.04
Nodes (72): BaseModel, Metadata about a target in target resolution. This model represents additional…, TargetMetadata, mock_persistence(), mock_player_service(), asyncio, fixture, Unit tests for target resolution service. Tests the TargetResolutionService… (+64 more)

### Community 199 - "manual_dependency_analysis.py"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 200 - "middleware"
Cohesion: 0.10
Nodes (32): CorrelationMiddleware, create_correlation_middleware(), create_websocket_correlation_middleware(), _get_header(), ASGIApp, Receive, Scope, Send (+24 more)

### Community 201 - "communication_commands_flows.py"
Cohesion: 0.06
Nodes (54): _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_global_command(), flow_reply_command(), flow_system_command(), flow_whisper_command(), _player_id_bundle(), Room/global/system/whisper/reply flows for communication command handlers.… (+46 more)

### Community 202 - "test_nats_messages.py"
Cohesion: 0.06
Nodes (50): BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, field_validator, Pydantic schemas for NATS message validation. This module provides type-safe…, Validate event type is not empty. (+42 more)

### Community 203 - "test_player_schema_converter_weapon.py"
Cohesion: 0.07
Nodes (38): Item prototype registry for command modules., _inventory_item_with_weapon(), PlayerSchemaConverter, Any, Get stats, inventory, and status_effects from player, handling async methods., Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…, Get PositionState from position value, with fallback to STANDING., Create PlayerRead schema from player object. (+30 more)

### Community 204 - "test_character_creation_service.py"
Cohesion: 0.04
Nodes (52): character_creation_service(), mock_player_service(), fixture, Unit tests for character creation service. Tests the CharacterCreationService…, Test roll_character_stats() when required_class is not available., Test roll_character_stats() handles ValueError., Test validate_character_stats() with class_name., Test validate_character_stats() without class_name. (+44 more)

### Community 205 - "Player"
Cohesion: 0.01
Nodes (404): _apply_grounding_adjustment(), _complete_ground_command(), handle_rescue_command(), UUID, Rescue commands for stabilising catatonic investigators., Apply lucidity adjustment for grounding. Returns result., Send failure events for grounding ritual., Send success events for grounding ritual. (+396 more)

### Community 206 - "test_connection_helpers_impl.py"
Cohesion: 0.08
Nodes (36): broadcast_global_event_impl(), _optimize_payload(), Any, _queue_message_if_needed(), Queue message for later delivery if no active connections. Args: player_id: The…, Update final delivery status based on connection results. Args:…, Send a personal message to a player via WebSocket (deprecated implementation).…, Broadcast a global event to all connected players. (+28 more)

### Community 207 - "NATSMessageSubscriptionMixin"
Cohesion: 0.12
Nodes (9): NATSMessageSubscriptionMixin, Mixin: room, subzone, and event NATS subscription lifecycle., Subscribe to chat messages for a specific room. Args: room_id: Room ID to…, Subscribe to all event-related NATS subjects using standardized patterns.…, Unsubscribe from all event-related NATS subjects using standardized patterns.…, Get the number of active event subscriptions. Returns: Number of active event…, Check if a specific event subscription is active. Args: subject: NATS subject…, Get the number of active subscriptions. (+1 more)

### Community 208 - "test_room_subscription_manager_drops.py"
Cohesion: 0.20
Nodes (9): Unit tests for room subscription manager drop functions. Tests the room drop…, Test take_room_drop() with quantity larger than available., Test adjust_room_drop() successfully adjusts quantity., Test add_room_drop() handles negative quantity gracefully., Test take_room_drop() removes drop from room., test_add_room_drop_negative_quantity(), test_adjust_room_drop_success(), test_take_room_drop() (+1 more)

### Community 209 - "test_command_admin.py"
Cohesion: 0.02
Nodes (125): GotoCommand, NPCCommand, field_validator, Admin command models for MythosMUD. This module provides command models for…, Command for shutting down the server (admin only). Args can be: - Empty:…, Command for NPC administrative utilities with subcommands., Administrative command for summoning prototypes into the current room., Validate prototype ID format. Args: value: The prototype ID to validate… (+117 more)

### Community 210 - "test_communication_commands_flows.py"
Cohesion: 0.08
Nodes (47): _chat_send_with_room_bundle(), flow_local_command(), flow_say_command(), _global_player_bundle(), _message_from_command(), Handle the `say` command: broadcast speech to the current room., Handle the `local` command: room-only speech (not global)., Resolve primary IDs for whisper; return error dict if self-whisper or missing… (+39 more)

### Community 211 - "dialogue_definitions_api.py"
Cohesion: 0.09
Nodes (44): create_dialogue_definition(), delete_dialogue_definition(), get_dialogue_definition(), list_dialogue_definitions(), delete, get, post, put (+36 more)

### Community 212 - "test_player_occupant_processor.py"
Cohesion: 0.05
Nodes (47): mock_connection_manager(), mock_name_extractor(), processor(), asyncio, fixture, Unit tests for player occupant processor. Tests the PlayerOccupantProcessor…, Test _convert_player_ids_to_uuids handles mixed string and UUID types., Test _convert_player_ids_to_uuids handles UUID objects. (+39 more)

### Community 213 - "LogAggregator"
Cohesion: 0.07
Nodes (39): LogEntry, aggregate_log_entry(), LogAggregator, LogEntry, LogQueryFilter, Any, Path, Add a log entry to the aggregation system. (+31 more)

### Community 214 - "test_mp_regeneration_service.py"
Cohesion: 0.04
Nodes (63): mock_player(), mock_player_service(), mp_regeneration_service(), asyncio, fixture, Unit tests for MP regeneration service. Tests the MPRegenerationService class…, Test process_tick_regeneration() accumulates fractional MP., Test _get_regen_multiplier() returns 1.0 for standing position. (+55 more)

### Community 215 - "test_admin_setstat_command.py"
Cohesion: 0.07
Nodes (39): asyncio, patch, Unit tests for admin set stat command handler. Tests the admin set command…, Test invalid stat name handling., Test successful setting of STR stat., Test invalid value (non-integer) handling., Test value out of range (warn but allow)., Test DP above maximum (warn but allow). (+31 more)

### Community 216 - "ui-v2/types.ts"
Cohesion: 0.06
Nodes (61): GameTerminalProps, eventHandlers, processGameEvent(), hoisted, EventHandlerContext, GameEvent, GameStateUpdates, EventStore (+53 more)

### Community 217 - "test_command_alias.py"
Cohesion: 0.07
Nodes (38): AliasCommand, AliasesCommand, field_validator, Alias command models for MythosMUD. This module provides command models for…, Command for creating or viewing command aliases., Validate alias name format using centralized validation., Validate command content for security using centralized validation., Command for listing all aliases. (+30 more)

### Community 218 - "SpellLearningService"
Cohesion: 0.12
Nodes (25): Any, UUID, Learn a spell for a player., Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…, Service for handling spell learning from various sources. Manages spell…, Learn a spell from a spellbook item. Args: player_id: Player ID…, Learn a spell from an NPC teacher. Args: player_id: Player ID npc_id: ID of the…, Learn a spell as a quest reward. Args: player_id: Player ID quest_id: ID of the… (+17 more)

### Community 219 - "test_inventory_helpers_extended.py"
Cohesion: 0.08
Nodes (35): ensure_item_instance_for_pickup(), Ensure item instance exists in database for picked up item., asyncio, Extended unit tests for inventory command helper functions. Tests additional…, Test _persist_player handles InventorySchemaValidationError., Test _persist_player handles general errors., Test _resolve_player when persistence is None., Test _resolve_player when username resolution fails. (+27 more)

### Community 220 - "NPCCombatUUIDMapping"
Cohesion: 0.05
Nodes (34): Return UUID mapping dependency for integration collaborators., NPCCombatUUIDMapping, UUID, Get the original string ID from a UUID. Args: uuid_id: The UUID to look up…, Get XP value for a UUID. Args: uuid_id: The UUID to look up Returns: XP value…, Manages UUID mappings for NPC combat., Initialize UUID mapping storage., Check if a string is a valid UUID. Args: uuid_string: String to check Returns:… (+26 more)

### Community 221 - "MythosChronicle"
Cohesion: 0.08
Nodes (27): ChronicleState, _ensure_utc(), MythosChronicle, datetime, Get the current Mythos datetime. Returns: datetime: The current Mythos datetime, Format the clock display string. Args: mythos_dt: Optional Mythos datetime to…, Authoritative converter between real and Mythos time., Return the singleton chronicle instance. (+19 more)

### Community 222 - "roomHandlers.ts"
Cohesion: 0.12
Nodes (32): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+24 more)

### Community 223 - "Argon2 Password Hashing Best Practices"
Cohesion: 0.07
Nodes (26): 1.1. Directory Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+18 more)

### Community 224 - "test_websocket_messages.py"
Cohesion: 0.05
Nodes (63): BaseWebSocketMessage, ChatMessage, ChatMessageData, CommandMessage, CommandMessageData, PingMessage, BaseModel, Pydantic schemas for WebSocket messages. These schemas define the structure and… (+55 more)

### Community 225 - "TauntCommandHandler"
Cohesion: 0.06
Nodes (46): AppWithState, Protocol, UUID, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Handle taunt command: draw NPC aggro (ADR-016). Room-local only., Minimal handler surface for taunt (avoids importing CombatCommandHandler:…, Return the combat service instance, or None if unavailable. (+38 more)

### Community 226 - "ContainerRepository"
Cohesion: 0.10
Nodes (31): Shared parameters for container creation (sync DB and async repository paths)., _container_data_to_dict(), ContainerRepository, Any, ContainerData, UUID, Update a container (async)., Get decayed containers (async). (+23 more)

### Community 227 - "Pre-commit Hooks Best Practices"
Cohesion: 0.07
Nodes (26): 1.1. Configuration Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+18 more)

### Community 228 - "devDependencies"
Cohesion: 0.05
Nodes (41): autoprefixer, devDependencies, autoprefixer, cross-env, eslint-plugin-playwright, eslint-plugin-react-hooks, eslint-plugin-react-refresh, globals (+33 more)

### Community 229 - "useGameClientV2ContainerRefsAndBootstrap.ts"
Cohesion: 0.09
Nodes (42): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), forceLogoutFallback(), performGameClientLogout(), stillShowingGameClient() (+34 more)

### Community 230 - "test_game_tick_processing.py"
Cohesion: 0.05
Nodes (68): cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _CorpseLike, _create_corpse_lifecycle_service(), _log_cleanup_results(), FastAPI, Protocol, Create CorpseLifecycleService or None if persistence is unavailable. (+60 more)

### Community 231 - "PlayerStateCommandFactory"
Cohesion: 0.04
Nodes (60): Unit tests for player state command factories. Tests the…, Test create_skills_command() raises error with args., Test create_journal_command() creates JournalCommand., Test create_journal_command() raises error with args., Test create_quests_command() creates QuestsCommand., Test create_quests_command() raises error with args., Test create_quest_command() with no args creates QuestCommand with empty list., Test create_status_command() creates StatusCommand. (+52 more)

### Community 232 - "RoomDataCache"
Cohesion: 0.05
Nodes (32): Manages room data caching and freshness validation., Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Clear room data cache. Args: room_id: Specific room ID to clear, or None to…, RoomDataCache, Unit tests for room data cache. Tests the RoomDataCache class for caching and…, Test clear_cache clears all rooms when room_id is None., Test clear_cache handles nonexistent room gracefully., Test get_cache_stats with empty cache. (+24 more)

### Community 233 - "PlayerGuidFormatter"
Cohesion: 0.05
Nodes (53): PlayerGuidFormatter, LogRecord, Player GUID Formatter for MythosMUD logging system. This module provides a…, Determine if a GUID is likely to be a player ID based on context. Args: guid:…, Get player name for GUID from in-memory data. Args: guid: The player GUID to…, Custom formatter that converts player GUIDs to "<name>: <GUID>" format. This…, Initialize the PlayerGuidFormatter. Args: player_service: Service for accessing…, Format a log record with enhanced player GUID display. Args: record: The log… (+45 more)

### Community 234 - "test_player_model.py"
Cohesion: 0.17
Nodes (11): Unit tests for Player SQLAlchemy model. Tests the Player model methods…, Test Player can be instantiated with required fields., Test Player.set_equipped_items() updates equipped items in stats., Test Player.is_alive() returns False when current_dp <= 0., Test Player.is_mortally_wounded() returns False when current_dp >= 0., Test Player.apply_dp_change detects crossing to mortally wounded (0 >= DP >…, test_player_apply_dp_change_became_mortally_wounded(), test_player_creation() (+3 more)

### Community 235 - "errorHandler.ts"
Cohesion: 0.15
Nodes (30): buildCreateCharacterPayload(), CharacterNameScreen(), getCreateCharacterErrorMessage(), extractErrorMessageFromResponseBody(), errorMessageFromApiBody(), messageFromCreationRefreshHttpError(), parseRefreshFailure(), isObject() (+22 more)

### Community 236 - "Any"
Cohesion: 0.06
Nodes (21): Any, Retrieve current room drops as a defensive copy for callers. Args: room_id: The…, Append an item stack to the room drop ledger. Args: room_id: The room receiving…, Remove quantity of a drop entry, returning the removed stack. Args: room_id:…, Adjust quantity for an existing drop entry; removing entry when zero. Args:…, Add a player as an occupant of a room. Args: player_id: The player's ID…, Remove a player as an occupant of a room. Args: player_id: The player's ID…, Get online player occupants from room_occupants and room_subscriptions. Uses… (+13 more)

### Community 237 - "test_player_service_mutations.py"
Cohesion: 0.05
Nodes (61): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service mutations. Covers delete, location update, mythos…, Test apply_corruption() applies corruption., Test gain_occult_knowledge() increases occult knowledge., Test heal_player() heals player. (+53 more)

### Community 238 - "GameTickService"
Cohesion: 0.05
Nodes (32): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+24 more)

### Community 239 - "TestMonitoringEndpoints"
Cohesion: 0.07
Nodes (22): asyncio, fixture, Test health check endpoint returns system health., Test health check endpoint handles errors., Test metrics endpoint returns monitoring data., Test metrics endpoint handles errors., Test monitoring summary endpoint returns summary data., Test lifespan() context manager. (+14 more)

### Community 240 - "gameStore.ts"
Cohesion: 0.10
Nodes (36): fetchSpy, useMapLayout(), buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData(), UseRoomMapDataResult (+28 more)

### Community 241 - "logging_file_setup.py"
Cohesion: 0.06
Nodes (51): Formatter, Logger, _PlayerGuidFormatterType, Queue, _add_handler_to_loggers(), _CategoryHandlerConfig, _ConsoleHandlerConfig, _convert_max_size_to_bytes() (+43 more)

### Community 242 - "gen_arena_migration_sql.py"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 243 - "AdminActionsLogger"
Cohesion: 0.08
Nodes (37): AdminActionsLogger, Any, datetime, Path, TypedDict, Log a general admin command action., Log permission check attempts. Args: player_name: Name of the player attempting…, Optional fields for teleport action logging. (+29 more)

### Community 244 - "look_command.py"
Cohesion: 0.05
Nodes (78): _app_from_request(), _as_response(), _connection_manager_from_app(), _container_from_app(), _get_app_and_persistence(), _get_room_drops(), _handle_implicit_target_lookup(), handle_look_command() (+70 more)

### Community 245 - "PrototypeRegistryError"
Cohesion: 0.07
Nodes (35): ItemInstance, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError, Any, Exception, PrototypeRegistry, Item factory for creating item instances from prototypes. This module provides… (+27 more)

### Community 246 - "PostgreSQL Best Practices"
Cohesion: 0.08
Nodes (25): 1.1. Naming Conventions, 1.2. Formatting, 1.3. Comments, 1. Code Organization and Structure, 2.1. Explicit JOINs, 2.2. Common Table Expressions (CTEs), 2.3. Avoid `NOT IN`, 2. Common Patterns and Anti-patterns (+17 more)

### Community 247 - "IdleMovementHandler"
Cohesion: 0.04
Nodes (73): _cfg_float(), IdleMovementHandler, _npc_id_str(), _passes_movement_probability(), Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement. Checks multiple conditions: -…, Check if NPC is in combat via UUID lookup. Args: npc_id: NPC ID (string or…, Check if NPC is in combat via string ID mapping. Args: npc_id: NPC ID as string… (+65 more)

### Community 248 - "useAsciiMapState.ts"
Cohesion: 0.06
Nodes (44): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+36 more)

### Community 249 - "resolve_weapon_attack_from_equipped"
Cohesion: 0.07
Nodes (40): Pydantic models for item prototype validation. This module defines the…, _prototype_from_equipped_stack(), NamedTuple, PrototypeRegistry, Weapon resolution helpers for combat. Resolves equipped main-hand items to…, Result of resolving an equipped item to a weapon attack. base_damage: Rolled…, Resolve equipped main-hand stack to weapon attack info, or None if unarmed., resolve_weapon_attack_from_equipped() (+32 more)

### Community 250 - "test_security_headers.py"
Cohesion: 0.05
Nodes (49): MutableHeaders, Any, ASGIApp, Receive, Request, Scope, Send, Backward-compatible dispatch method for BaseHTTPMiddleware interface. This… (+41 more)

### Community 251 - "test_command_magic.py"
Cohesion: 0.05
Nodes (57): CastCommand, LearnCommand, field_validator, Magic command models for MythosMUD. This module provides command models for…, Command for casting a spell., Validate spell name format., Validate target format., Command for viewing spell details. (+49 more)

### Community 252 - "Structured Logging with Structlog Best Practices"
Cohesion: 0.08
Nodes (26): 1.1. Directory Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+18 more)

### Community 253 - "Uvicorn ASGI Server Best Practices"
Cohesion: 0.08
Nodes (25): 1.1. Directory Structure, 1.2. File Naming Conventions, 1.3. Module Organization, 1. Code Organization and Structure, 2.1. Design Patterns, 2.2. Recommended Approaches, 2.3. Anti-patterns, 2. Common Patterns and Anti-patterns (+17 more)

### Community 254 - "CommunicationCommandFactory"
Cohesion: 0.05
Nodes (60): Unit tests for communication command factories. Tests the…, Test create_me_command() creates MeCommand., Test create_me_command() raises error with no args., Test create_pose_command() creates PoseCommand., Test create_pose_command() allows no args (sets pose to None)., Test create_channel_command() creates ChannelCommand., Test create_channel_command() handles 'default' action., Test create_channel_command() raises error with no args. (+52 more)

### Community 255 - "PartyService"
Cohesion: 0.11
Nodes (25): PartyService, Any, UUID, Create a new party with the given player as leader. Returns dict with success…, Disband a party. If by_player_id is given, only the leader may disband. If…, Add a player to a party. Fails if party does not exist or player is already in…, Remove expired pending invites and notify inviters., Send a command_response-style message to a single player. (+17 more)

### Community 256 - "test_movement_service.py"
Cohesion: 0.09
Nodes (21): Unit tests for movement service. Tests the MovementService class., Test get_room_players() returns list of player IDs., Test validate_player_location() returns False when player is not in room., Test validate_player_location() returns False when room is not found., Test set_player_combat_service updates combat service reference., Test check_combat_state allows movement when no combat service., Test check_player_posture blocks non-standing posture., Test validate_exit returns False when room has no exits. (+13 more)

### Community 257 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 258 - "test_movement_monitor.py"
Cohesion: 0.03
Nodes (60): Reset the global movement monitor (useful for testing)., reset_movement_monitor(), movement_monitor(), fixture, Unit tests for movement monitor. Tests the MovementMonitor class for monitoring…, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data. (+52 more)

### Community 259 - "test_rate_limiter.py"
Cohesion: 0.03
Nodes (60): mock_config(), fixture, rate_limiter(), Unit tests for rate limiter service. Tests the RateLimiter class which provides…, Test check_rate_limit returns True when within limits., Test check_rate_limit returns False when limit exceeded., Test check_rate_limit always returns True when disabled., Test check_rate_limit handles errors gracefully (fails open). (+52 more)

### Community 260 - "CharacterSelectionScreen.tsx"
Cohesion: 0.08
Nodes (20): CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreen(), CharacterSelectionScreenProps, extractCharactersFetchErrorMessage(), fetchCharactersList(), formatCharacterDate() (+12 more)

### Community 261 - "communication_commands.py"
Cohesion: 0.05
Nodes (77): handle_global_command(), handle_local_command(), handle_me_command(), handle_pose_command(), handle_say_command(), handle_system_command(), Communication commands for MythosMUD. Handlers delegate heavy logic to…, Local channel message. (+69 more)

### Community 262 - "test_chat_nats_publisher.py"
Cohesion: 0.08
Nodes (52): _build_legacy_subject(), _build_nats_message_data(), build_nats_subject(), _build_standardized_subject(), _extract_subzone_from_room(), _log_nats_publish_error(), _log_nats_unexpected_error(), _nats_service_ready() (+44 more)

### Community 263 - "UUID"
Cohesion: 0.11
Nodes (17): AsyncSession, Player, UUID, Return current_dp as an int, defaulting to 0 for non-numeric values., Return (allowed, current_dp_int) for limbo movement gate checks., Clear combat state for a respawning player, logging and swallowing DB errors., Publish standard respawn event when event bus is available., Restore full health and move player to respawn_room; return (old_dp, max_dp,… (+9 more)

### Community 264 - "NPCCombatLucidity"
Cohesion: 0.06
Nodes (32): ActiveLucidityService, Handle active lucidity adjustments such as encounters and recovery actions., _EncounterCtx, NPCCombatLucidity, Any, NamedTuple, Apply lucidity loss when a player engages an eldritch entity. Args: player_id:…, Determine encounter category based on NPC definition metadata. Args:… (+24 more)

### Community 265 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test get_player_by_id returns None when player not found., Test get_player_by_user_id returns None when no players., Test save_players successfully saves multiple players., Test soft_delete_player successfully soft deletes player., Test delete_player successfully deletes player., Test delete_player returns False when player not found., Test update_player_last_active successfully updates timestamp. (+9 more)

### Community 266 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 267 - "testing_examples.py"
Cohesion: 0.04
Nodes (51): async_operation(), client, database, LoggingMiddleware, process_batch(), process_item(), asyncio, Test WebSocket logging in integration tests. (+43 more)

### Community 268 - "PlayerNameExtractor"
Cohesion: 0.10
Nodes (22): PlayerNameExtractor, Any, UUID, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:…, Perform basic validation on player name (not None, is string, not empty). Args:…, Utility class for extracting and validating player names. CRITICAL: NEVER uses… (+14 more)

### Community 269 - "message_handler_factory.py"
Cohesion: 0.06
Nodes (53): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, MessageHandlerFactory, PartyInviteResponseMessageHandler, PingMessageHandler (+45 more)

### Community 270 - "test_container_persistence_extended_parse.py"
Cohesion: 0.05
Nodes (39): Unit tests for container persistence: JSONB parsing, item fetch, and…, Test _fetch_container_items with no items., Test _fetch_container_items skips rows with missing item_instance_id., Test _fetch_container_items handles non-dictionary rows., Test _fetch_container_items parses string metadata., Test _fetch_container_items handles invalid JSON metadata., Test _fetch_container_items handles non-dict metadata., Test parsing empty list JSONB column. (+31 more)

### Community 271 - "test_look_item.py"
Cohesion: 0.09
Nodes (27): _get_item_description_from_prototype(), Get item description from prototype registry. Returns: Formatted result string…, Unit tests for item look functionality. Tests the helper functions for looking…, Test finding item in equipped items by name., Test finding item in equipped items when not found., Test getting item description from prototype., Test getting item description when prototype registry is None., Test getting item description when prototype_id is missing. (+19 more)

### Community 272 - "nats_service.py"
Cohesion: 0.06
Nodes (24): Msg, NATS metrics collection for MythosMUD. This module provides metrics collection…, _as_json_map(), _nats_connect(), _NatsConnectFn, NatsConnectOptions, _NatsListenerClient, NatsMessageCallback (+16 more)

### Community 273 - "chatPanelRuntimeUtils.ts"
Cohesion: 0.05
Nodes (67): ChatExportDialog(), ChatExportDialogProps, collectFocusableElements(), filterMessagesForChannelView(), EXCLUDED_MESSAGE_TYPES_FOR_CHANNEL_VIEW, isGloballyExcludedFromChannelView(), isVisibleInChannelView(), matchesChannelSelection() (+59 more)

### Community 274 - "apiTypeGuards.ts"
Cohesion: 0.11
Nodes (46): ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertServerCharacterResponseArray(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString() (+38 more)

### Community 275 - "MemoryMonitor"
Cohesion: 0.06
Nodes (17): useGameClientV2MemoryMonitorEffect(), ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor (+9 more)

### Community 276 - "ScheduleEntry"
Cohesion: 0.04
Nodes (33): Record the schedule categories currently active for NPC routines., Any, field_validator, Single schedule block describing routine availability…, Validate schedule entry days are standard English weekday names (Sunday,…, Validate slug-formatted list entries. Args: value: Sequence of strings to…, Ensure the schedule window moves time forward like the Chronology Tablets…, Validate tradition value. Args: value: The tradition string to validate… (+25 more)

### Community 277 - "react Best Practices"
Cohesion: 0.08
Nodes (23): 1. Core React Principles: Purity & Rules of Hooks, 2. Code Organization & Naming, 3. Component Design & Patterns, 4. State Management, 5. Performance & Optimization, 6. Common Pitfalls, 7. Accessibility (A11y) & Testing, ❌ BAD: Class components / Mixed concerns (+15 more)

### Community 278 - "test_rest_and_grace_period.py"
Cohesion: 0.06
Nodes (46): is_player_in_grace_period(), Check if a player is currently in grace period. Args: player_id: The player's…, mock_app_with_services(), mock_connection_manager_full(), mock_persistence_full(), MockPersistenceFull, asyncio, fixture (+38 more)

### Community 279 - "ModerationCommandFactory"
Cohesion: 0.05
Nodes (58): Unit tests for moderation command factories. Tests the ModerationCommandFactory…, Test create_mute_global_command() with duration and reason., Test create_mute_global_command() with reason but no duration., Test create_unmute_global_command() creates UnmuteGlobalCommand., Test create_unmute_global_command() raises error with no args., Test create_unmute_global_command() raises error with multiple args., Test create_admin_command() creates AdminCommand., Test create_mute_command() creates MuteCommand. (+50 more)

### Community 280 - "lucidity.ts"
Cohesion: 0.10
Nodes (27): IncapacitatedBanner, IncapacitatedBannerProps, HallucinationTicker, HallucinationTickerProps, severityClass, RescueStatusBanner, RescueStatusBannerProps, statusStyles (+19 more)

### Community 281 - "MagicServiceCompletionMixin"
Cohesion: 0.19
Nodes (15): _is_heal_other_target(), MagicServiceCompletionMixin, Any, UUID, Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…, Parse target_id from casting state. Returns None if missing or invalid., Apply costs and queue spell for next combat round. Returns True if queued,…, Apply spell costs/effects, send completion message and healing event. (+7 more)

### Community 282 - "alias_schema.json"
Cohesion: 0.04
Nodes (51): command, version, additionalProperties, additionalProperties, description, properties, required, type (+43 more)

### Community 283 - "test_zone_configuration.py"
Cohesion: 0.05
Nodes (41): Unit tests for zone configuration. Tests the ZoneConfiguration class., Test get_effective_spawn_probability() when already at 1.0., Test can_access() returns True when no requirements., Test can_access() returns True when requirements are met., Test can_access() returns True when at least one requirement is met., Test ZoneConfiguration initialization with minimal data., Test can_access() returns False when requirements not met., Test can_access() returns False when player has no requirements. (+33 more)

### Community 284 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (28): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+20 more)

### Community 285 - "test_connection_statistics.py"
Cohesion: 0.05
Nodes (52): get_online_player_by_display_name_method(), Get online player information by display name., Get session management statistics., Get presence tracking statistics., Get online player information by display name., get_online_player_by_display_name_impl(), get_player_presence_info_impl(), get_presence_statistics_impl() (+44 more)

### Community 286 - "test_admin_commands_helpers.py"
Cohesion: 0.07
Nodes (48): broadcast_teleport_effects(), create_teleport_effect_message(), get_online_player_by_display_name(), notify_player_of_teleport(), Any, Notify a player that they are being teleported by an admin. Args:…, Get online player information by display name. Args: display_name: Display name…, Create teleport effect message for visual display. Args: player_name: Name of… (+40 more)

### Community 287 - "WebSocketMessageValidator"
Cohesion: 0.03
Nodes (112): MessageValidationError, BaseModel, Exception, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Validate message against Pydantic schema. Args: message: Parsed JSON message…, Raised when message validation fails., Return the first string CSRF token from known keys, or None if absent. (+104 more)

### Community 288 - "test_inventory_display_helpers.py"
Cohesion: 0.09
Nodes (40): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+32 more)

### Community 289 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 290 - "NATSSubscribeError"
Cohesion: 0.06
Nodes (32): NATSConnectionError, NATSHealthCheckError, NATSSubscribeError, Raised when NATS connection operations fail., Raised when subscription operations fail., Raised when health check operations fail., Subscribe to a NATS subject and register a callback for incoming messages.…, Unit tests for NATS exception classes. Tests the NATS exception hierarchy for… (+24 more)

### Community 291 - "test_admin_summon_command.py"
Cohesion: 0.08
Nodes (48): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), handle_summon_command(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any (+40 more)

### Community 292 - "test_memory_leak_metrics.py"
Cohesion: 0.05
Nodes (42): collector(), fixture, Unit tests for memory leak metrics collector. Tests the…, Test collection of cache metrics., Test collection of task metrics., Test collection of NATS metrics., Test collection of all metrics., Test calculation of growth rates. (+34 more)

### Community 293 - "container_endpoints_basic.py"
Cohesion: 0.01
Nodes (304): get_async_persistence, get_connection_manager, _apply_inventory_stack_defaults(), _as_inventory_dicts(), _as_str_list(), _as_str_object_dict(), _as_str_object_mapping(), _build_container_data_from_dict() (+296 more)

### Community 294 - "edgeModalLogic.ts"
Cohesion: 0.09
Nodes (30): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+22 more)

### Community 295 - "test_command_parser_helpers.py"
Cohesion: 0.06
Nodes (30): command_parser(), fixture, Unit tests for command_parser helper methods. Tests the helper methods in…, Test _create_command_object() handles 'l' alias., Test _create_command_object() handles 'g' alias., Test _create_command_object() handles 'w' alias., Create a CommandParser instance., Test _normalize_command() removes leading slash. (+22 more)

### Community 296 - "test_config_model_helpers.py"
Cohesion: 0.31
Nodes (8): _apply_url_fallback(), If url is missing, set it from npc_url in data or from DATABASE_* env vars.…, MonkeyPatch, Unit tests for server.config.models._helpers., test_apply_url_fallback_from_database_env(), test_apply_url_fallback_from_npc_url(), test_apply_url_fallback_keeps_existing_url(), test_default_cors_origins_from_env()

### Community 297 - "RoomEventHandler"
Cohesion: 0.12
Nodes (22): Any, UUID, Handle PlayerEnteredRoom events by broadcasting updated occupant count., Handle PlayerLeftRoom events by broadcasting updated occupant count., Handles room movement events and broadcasts occupant updates. This class…, Initialize the room event handler. Args: room_manager: RoomSubscriptionManager…, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events. (+14 more)

### Community 298 - "test_pattern_matcher.py"
Cohesion: 0.05
Nodes (43): PatternMatcher, Any, Pattern matching utilities for NATS Subject Manager. This module provides…, Matcher for validating subjects against registered patterns., Initialize pattern matcher. Args: strict_validation: Enable strict validation…, Check if subject matches any registered pattern. Args: subject: Subject string…, Check if subject components match a pattern. Args: components: Subject…, pattern_matcher() (+35 more)

### Community 299 - "admin_shutdown_command.py"
Cohesion: 0.09
Nodes (43): _broadcast_shutdown_cancellation(), broadcast_shutdown_notification(), calculate_notification_times(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), cancel_shutdown_countdown(), _clear_shutdown_state(), countdown_loop() (+35 more)

### Community 300 - "test_npc_event_handlers_helpers.py"
Cohesion: 0.09
Nodes (25): mock_connection_manager(), mock_message_builder(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers helper functions. Tests the helper functions…, Test _determine_direction_from_rooms() determines direction., Test _determine_direction_from_rooms() returns None when direction not found. (+17 more)

### Community 301 - "StyleGuideSections.tsx"
Cohesion: 0.06
Nodes (45): Channel, ChannelSelector(), ChannelSelectorProps, useChannelSelectorState(), AllStats(), CommandsCount(), ConnectionStatus(), CORE_ATTRIBUTES (+37 more)

### Community 302 - "npc_database.py"
Cohesion: 0.02
Nodes (162): Draft7Validator, get_asyncpg_server_settings_for_database_url(), get_postgres_connect_args(), get_test_database_url(), load_database_url(), normalize_database_url(), Database configuration helper functions. This module provides utility functions…, Build connect_args for asyncpg when POSTGRES_SEARCH_PATH is set. Used so unit… (+154 more)

### Community 303 - "test_npc_combat_handlers.py"
Cohesion: 0.06
Nodes (42): CombatResultCtx, Bundle for handle_combat_result (lizard PARAM)., Handle combat result, broadcast, and NPC death., mock_combat_memory(), mock_combat_result(), mock_data_provider(), mock_lifecycle(), mock_messaging_integration() (+34 more)

### Community 304 - "Any"
Cohesion: 0.11
Nodes (10): Any, Initialize the room cache service. Args: persistence: Persistence layer instance, Get room data with caching. Args: room_id: The room ID Returns: Room data…, Get room data with caching (synchronous version). Args: room_id: The room ID…, Initialize the NPC cache service. Args: npc_service: NPC service instance, Get NPC definitions with caching. Args: session: Database session Returns: List…, Get a specific NPC definition with caching. Args: session: Database session…, Get NPC spawn rules with caching. Args: session: Database session Returns: List… (+2 more)

### Community 305 - "test_goto_helpers.py"
Cohesion: 0.12
Nodes (43): execute_confirm_goto(), execute_goto_teleport(), log_goto_failure(), Any, Exception, Helper functions for goto command operations., Log failed goto action., Validate app context and get current player with admin permissions. Returns… (+35 more)

### Community 306 - "github-actions Best Practices"
Cohesion: 0.09
Nodes (21): 1.1 Use Reusable Workflows and Composite Actions, 1.2 Name Jobs and Steps Consistently, 1.3 Employ Matrix Strategies for Broad Testing, 1.4 Set Explicit Concurrency Groups, 1. Workflow Design & Code Organization, 2.1 Cache Dependencies, 2. Performance Considerations, 3.1 Run Linters, Formatters, and Static Analysis Early (+13 more)

### Community 307 - "RoomDataValidator"
Cohesion: 0.07
Nodes (39): Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Check if occupant count matches the actual occupants list length. Args:…, Validates room data structure and content., Check for duplicate occupants in the room. Args: room_data: Room data to check…, Check if room has occupants but no name. Args: room_data: Room data to check…, Validate room data structure and content. Args: room_data: Room data to… (+31 more)

### Community 308 - "NPCCombatIntegration"
Cohesion: 0.04
Nodes (88): NPCCombatIntegration, Publish NPC attack event to event bus., Integrates NPCs with the existing combat and game mechanics systems. Extends…, Handle NPC death and related effects. Args: npc_id: ID of the dead NPC room_id:…, Get NPC stats or use defaults., Resolve NPC instance display name from lifecycle manager, or derive from npc_id., Best-effort lookup of NPC name from the lifecycle manager., Resolve the NPC lifecycle manager from the app state, if available. (+80 more)

### Community 309 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 310 - "useDraggablePanelInteractions.ts"
Cohesion: 0.09
Nodes (41): DraggablePanel(), DraggablePanelProps, isMouseEventOnHeader(), isPanelDragBlockedTarget(), PANEL_DRAG_BLOCK_SELECTORS, relativeSizeToAbsolute(), relativeToAbsolute(), applyDragMove() (+33 more)

### Community 311 - "fixtures/integration/__init__.py"
Cohesion: 0.08
Nodes (43): FixtureRequest, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+35 more)

### Community 312 - "TestHolidayService"
Cohesion: 0.04
Nodes (33): _holiday_entry_from_row(), Record, Normalize nullable PostgreSQL array columns to string values., Build a HolidayEntry from a calendar_holidays row., _string_list_from_row(), asyncio, fixture, MonkeyPatch (+25 more)

### Community 313 - "PassiveMobNPC"
Cohesion: 0.06
Nodes (52): PassiveMobNPC, Respond to player interaction., Handle responding to greeting action., Handle fleeing action., Passive mob NPC type with wandering and response behaviors., Setup passive mob-specific behavior rules., Get passive mob-specific behavior rules., asyncio (+44 more)

### Community 314 - "canonical_room_id_impl"
Cohesion: 0.07
Nodes (32): Resolve a room id to the canonical Room.id value (public method)., Resolve a room id to the canonical Room.id value (compatibility method)., Ensure room_occupants only contains currently online players (compatibility…, Remove a player from all room subscriptions and occupant lists (compatibility…, canonical_room_id_impl(), prune_player_from_all_rooms_impl(), Any, Resolve a room id to the canonical Room.id value. Args: room_id: The room ID to… (+24 more)

### Community 315 - "TargetResolutionResult"
Cohesion: 0.05
Nodes (70): _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), _load_follow_context(), Any, Follow commands for MythosMUD. Handlers for /follow, /unfollow, and /following.…, Handle /following - show who you follow and who follows you. (+62 more)

### Community 316 - "collect_inventory.py"
Cohesion: 0.08
Nodes (43): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+35 more)

### Community 317 - "deleteCharacterFlow.ts"
Cohesion: 0.09
Nodes (39): AuthSlice, authSliceReducer(), CreationSlice, creationSliceReducer(), INITIAL_AUTH_SLICE, INITIAL_CREATION_SLICE, PendingSkillsPayload, resolveNextState() (+31 more)

### Community 318 - "NATSMessageBroadcastMixin"
Cohesion: 0.09
Nodes (19): NATSMessageBroadcastMixin, Any, UserManager, Determine if message should be echoed to sender. Args: channel: Channel type…, Echo message back to sender. Args: sender_id: Sender player ID chat_event: Chat…, Broadcast room-based messages with server-side filtering. This method ensures…, Mixin: room filtering, mute checks, dampening, and personal send., Return the user manager instance to use for mute lookups. (+11 more)

### Community 319 - "verify_enhanced_logging_compliance.py"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 320 - "projectorRoom.ts"
Cohesion: 0.16
Nodes (28): attachOccupants(), coalesceCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), deriveRoomFromGameState(), deriveRoomFromOccupantsWithoutExisting(), deriveRoomFromRoomOccupants() (+20 more)

### Community 321 - "character-cleanup.ts"
Cohesion: 0.10
Nodes (25): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), loginAsIthaqua(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation() (+17 more)

### Community 322 - "deque"
Cohesion: 0.07
Nodes (51): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+43 more)

### Community 323 - "TestNPCCombatLifecycle"
Cohesion: 0.11
Nodes (14): asyncio, fixture, Unit tests for NPC combat lifecycle. Tests the NPCCombatLifecycle class for…, Test _despawn_npc handles NPC not in active_npcs., Test suite for NPCCombatLifecycle class., Create a mock persistence layer., Create a NPCCombatLifecycle instance for testing., Test NPCCombatLifecycle initialization. (+6 more)

### Community 324 - "compare_linting_results.py"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 325 - "3. Common Patterns and Anti-patterns"
Cohesion: 0.10
Nodes (20): 1.1. Base Configuration, 1.2. TypeScript Integration (Type-Aware Linting), 1.3. Prettier Integration, 1. Core Configuration: Flat Config is Mandatory, 2. Code Organization and Structure, 3.1. Immutability (`prefer-const`), 3.2. Unused Variables (`no-unused-vars`), 3.3. Consistent Returns (`consistent-return`) (+12 more)

### Community 326 - "NATSSubjectManager"
Cohesion: 0.07
Nodes (21): get_subject_manager_dependency(), Dependency function to inject NATSSubjectManager. Returns: Global…, Initialize combat event publisher. Args: nats_service: NATS service instance…, NATSSubjectManager, Any, Build a NATS subject from a pattern and parameters. Args: pattern_name: Name of…, Ensure pattern exists in registry. Args: pattern_name: Name of the pattern to…, Ensure all required parameters are provided. Args: pattern_name: Name of the… (+13 more)

### Community 327 - "handle_whisper_command"
Cohesion: 0.07
Nodes (50): handle_reply_command(), handle_whisper_command(), Reply to last whisper sender., asyncio, Unit tests for whisper and reply communication command handlers., Test handle_whisper_command successful execution., Test handle_reply_command with no message., Test handle_reply_command when services are not available. (+42 more)

### Community 328 - "CoordinateGenerator"
Cohesion: 0.07
Nodes (24): CoordinateGenerator, Any, AsyncSession, Load rooms and their exits from database. Args: plane: Plane name zone: Zone…, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits., Assign coordinates using BFS starting from origin., Detect conflicts (multiple rooms at same x,y coordinates). (+16 more)

### Community 329 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 330 - "HolidayCollection"
Cohesion: 0.12
Nodes (26): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+18 more)

### Community 331 - "test_chat_npc_system.py"
Cohesion: 0.08
Nodes (35): deliver_personal_system(), UUID, Deliver personal system chat using the wired ChatService, if any., Clear one-shot NPCSpoke subscription guard (unit tests only)., Send a system-channel message to one player (whisper subject)., reset_npc_spoke_subscription_for_tests(), send_personal_system_message(), _mock_chat_service() (+27 more)

### Community 332 - "test_chat_logger.py"
Cohesion: 0.06
Nodes (29): Unit tests for chat logger service. Tests the ChatLogger class for structured…, Test log_player_muted writes entry., Test log_player_unmuted writes entry., Test log_player_joined_room writes entry., Test log_rate_limit_violation writes entry., Test get_log_file_paths returns correct paths., Test get_log_stats returns statistics., Test log_whisper_channel_message writes entry. (+21 more)

### Community 333 - "test_room_utils.py"
Cohesion: 0.07
Nodes (37): Unit tests for room_utils. Tests utility functions for room operations., Test get_subzone_local_channel_subject() generates subject., Test get_subzone_local_channel_subject() returns None for invalid room ID., Test extract_subzone_from_room_id() extracts subzone., Test extract_subzone_from_room_id() extracts different subzone., Test extract_subzone_from_room_id() returns None for invalid format., Test get_zone_from_room_id() extracts zone., Test get_zone_from_room_id() extracts different zone. (+29 more)

### Community 334 - "HealthRepository"
Cohesion: 0.08
Nodes (35): HealthRepository, Exception, Player, UUID, Log critical damage persistence failure., Execute atomic health update via update_player_health procedure., Damage a player and persist health changes atomically. Args: player: Player to…, Heal a player and persist health changes atomically. (+27 more)

### Community 335 - "HolidayEntry"
Cohesion: 0.06
Nodes (40): extract_observance_ids(), HolidayEntry, BaseModel, Calendar ingestion schemas for MythosMUD. These models provide a typed wrapper…, Create a mapping of holiday IDs to holiday entries. Returns: dict[str,…, Wrapper around an array of schedule entries., Load schedule collection from a JSON file. Args: path: Path to the JSON file…, Normalize document observance names into snake_case ids. (+32 more)

### Community 336 - "ChatLogger"
Cohesion: 0.07
Nodes (23): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+15 more)

### Community 337 - "_find_item_in_equipped"
Cohesion: 0.11
Nodes (24): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _handle_item_look(), Any, Item look functionality for MythosMUD. This module handles looking at items,…, Find an item in equipped items by name or prototype_id. Args: equipped:…, Check if item found in a location and return formatted result. (+16 more)

### Community 338 - "test_audit_logger.py"
Cohesion: 0.07
Nodes (35): _logger(), Path, Unit tests for audit_logger utilities. Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries. (+27 more)

### Community 339 - "ContainerTransferFromMixin"
Cohesion: 0.19
Nodes (15): ContainerTransferFromMixin, ContainerComponent, InventoryStack, Player, UUID, Persist container changes and log audit trail., Mutation-guarded body: remove stack, add to player, persist, audit., Transfer items from container to player inventory. (+7 more)

### Community 340 - "test_look_container.py"
Cohesion: 0.08
Nodes (42): ContainerLookArgs, _find_container_in_room_or_equipped(), _find_container_via_inner_container(), _handle_container_look(), NamedTuple, Find container via inner_container_id from item., Find container in room or equipped items. Returns: tuple: (container_found,…, Handle looking at a specific container. (+34 more)

### Community 341 - "GameLogPanel.tsx"
Cohesion: 0.09
Nodes (31): GameTerminalPresentation(), GameTerminalPresentationProps, GameLogListMessage, GameLogMessagesList(), GameLogMessagesListProps, GameLogPanel(), GameLogPanelProps, GameLogPanelFilterBar() (+23 more)

### Community 342 - "RoomMapEditorRuntime.hooks.ts"
Cohesion: 0.13
Nodes (29): HistoryEntry, MapEditingChanges, useMapEditing(), UseMapEditingOptions, UseMapEditingResult, UseMapLayoutResult, buildModalCreateEdgeHandler(), buildModalPreviewHandler() (+21 more)

### Community 343 - "types/mythosTime.ts"
Cohesion: 0.10
Nodes (32): HolidayBanner(), HolidayBannerProps, MythosTimeHud(), MythosTimeHudProps, TRADITION_COLORS, mythosState, appendDaypartChange(), appendHourChime() (+24 more)

### Community 344 - "TypeScript Best Practices"
Cohesion: 0.11
Nodes (18): 1. Enable Strict Mode in `tsconfig.json`, 2. Define Clear Type Contracts, 3. Avoid `any` and Prefer `unknown` for Untyped Data, 4. Implement Robust Runtime Type Validation (Type Guards), 5. Prefer Union Types over Traditional Enums, 6. Use Generics for Reusable Components/Functions, 7. Enforce Consistent Code Organization, ❌ BAD: Numeric Enums (+10 more)

### Community 345 - "setup.ts"
Cohesion: 0.16
Nodes (6): createDomPurifyTestWindow(), installDomPurifyTestWindow(), defaultFetchMock, installLocalStorageShim(), isUsableStorage(), peekExistingLocalStorage()

### Community 346 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test handling item look when item is in room drops., Test handling item look when item is in inventory., Test handling item look when item is equipped., Test handling item look when item not found., Test handling item look with look_in flag skips equipped items., Test trying implicit lookup when item is in room drops., Test trying implicit lookup when item not found. (+17 more)

### Community 347 - "spell_effect_types.py"
Cohesion: 0.07
Nodes (26): NpcIntegrationStringIdPort, NpcLifecycleManagerPort, PlayerPersistenceSpellPort, PlayerServiceHealPort, Protocol, UUID, Shared Protocol types for spell effect modules. Used by basedpyright to type…, Apply healing to a player by id. (+18 more)

### Community 348 - "vite Best Practices"
Cohesion: 0.11
Nodes (18): 1. Code Organization and Structure, 2. Common Patterns and Anti-patterns, 3. Performance Considerations, 4. Common Pitfalls and Gotchas, 5. Testing Approaches, Audit Custom Plugins, Avoid Barrel Files, Embrace Native ES Modules (+10 more)

### Community 349 - "ConnectionCleaner"
Cohesion: 0.08
Nodes (26): ConnectionCleaner, Any, UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return connection IDs that exceed max_connection_age., Extract player_id from connection metadata if present. (+18 more)

### Community 350 - "Lint Remediation"
Cohesion: 0.17
Nodes (11): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Entry point, Error code table, Fix patterns by tier, Fix-verify loop, 🟡 High — code quality, Lint Remediation (+3 more)

### Community 351 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 352 - "E2E Test Suite AI Execution Improvements - Summary"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 353 - "test_connection_event_helpers.py"
Cohesion: 0.11
Nodes (26): Any, Subscribe to room movement events for occupant broadcasting., Unsubscribe from room movement events., subscribe_to_room_events_impl(), unsubscribe_from_room_events_impl(), Unsubscribe from room movement events., unsubscribe_from_room_events_impl(), Unsubscribe from room movement events. (+18 more)

### Community 354 - "connection_cleanup_methods.py"
Cohesion: 0.08
Nodes (35): check_and_cleanup_impl(), cleanup_dead_connections_impl(), cleanup_ghost_players_impl(), cleanup_orphaned_data_impl(), force_cleanup_impl(), prune_stale_players_impl(), Any, UUID (+27 more)

### Community 355 - "click Best Practices"
Cohesion: 0.11
Nodes (18): 1. Code Organization & Structure, 2. Argument Parsing: Arguments vs. Options, 3. Output: `click.echo` and `click.secho`, 4. Type Hints, 5. Comprehensive Help Text & Examples, 6. Packaging with `pyproject.toml`, 7. Testing with `CliRunner`, ❌ BAD: Inconsistent Output (+10 more)

### Community 356 - "_find_item_in_inventory"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id. Args: inventory: List…, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 357 - "2. Type Hinting Best Practices"
Cohesion: 0.11
Nodes (17): 1.1. Centralized Configuration, 1.2. CI/CD & Pre-commit Hooks, 1.3. Incremental Adoption, 1. Configuration & Integration, 2.1. Prefer `object` over `Any`, 2.2. Use `TypeAlias` for Type Aliases, 2.3. Concrete vs. Abstract Types, 2.4. Shorthand Union Syntax (+9 more)

### Community 358 - "DistributedEventBus"
Cohesion: 0.09
Nodes (28): DistributedEventBus, Any, EventBus that distributes domain events via NATS for horizontal scaling. When…, Initialize distributed EventBus. Args: nats_service: NATS service for…, Set NATS service and start the bridge (call after NATS connects)., Publish event locally and to NATS when bridge is active., Shutdown EventBus and stop NATS bridge., distributed_bus() (+20 more)

### Community 359 - "MythosPanel.tsx"
Cohesion: 0.10
Nodes (27): appendCommands(), CommandCategories(), CommandPanelTest(), COMMAND_CATEGORIES, DEFAULT_COMMAND_HISTORY, EXAMPLES, FEATURES, MOVEMENT_COMMANDS (+19 more)

### Community 360 - "useGameTerminal.ts"
Cohesion: 0.05
Nodes (53): GameTerminalContainer(), createDefaultGameTerminalState(), useGameTerminalMock, applyTestCommandHistoryCap(), CHANNEL_TYPE_MAP, ChatMessageLike, GameTerminalState, mockCommandState (+45 more)

### Community 361 - "GameStateProvider"
Cohesion: 0.09
Nodes (26): GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send… (+18 more)

### Community 362 - "test_admin_teleport_commands.py"
Cohesion: 0.16
Nodes (42): handle_confirm_goto_command(), handle_confirm_teleport_command(), handle_goto_command(), handle_teleport_command(), Any, Handle the goto command for teleporting the admin to a player's location. Args:…, Handle the confirm teleport command for executing the actual teleportation.…, Handle the confirm goto command for executing the actual teleportation. Args:… (+34 more)

### Community 363 - "connection_manager_health_cleanup.py"
Cohesion: 0.09
Nodes (38): delegate_connection_cleaner(), Generic delegate for connection cleaner methods. Args: connection_cleaner:…, check_and_cleanup_impl(), check_connection_health_impl(), cleanup_dead_connections_impl(), cleanup_ghost_players_impl(), cleanup_orphaned_data_impl(), detect_and_handle_error_state_impl() (+30 more)

### Community 364 - "PerformanceMonitor"
Cohesion: 0.06
Nodes (44): __getattr__(), Any, Lazy import for modules that require numpy., Initialize the monitoring dashboard., get_performance_monitor(), get_performance_stats(), measure_performance(), PerformanceMetric (+36 more)

### Community 365 - "WearableContainerService"
Cohesion: 0.11
Nodes (24): _filter_container_data(), _get_enum_value(), Any, ContainerComponent, UUID, Return existing equipment container ID for item instance if present., Create wearable container in persistence and return container_id payload., Handle equipping a wearable container item. Creates a container in PostgreSQL… (+16 more)

### Community 366 - "ConnectionErrorHandler"
Cohesion: 0.11
Nodes (26): ConnectionErrorHandler, Any, UUID, Handle WebSocket-specific errors. Args: player_id: The player's ID…, Handle authentication-related errors. Args: player_id: The player's ID…, Handle security violations. Args: player_id: The player's ID violation_type:…, Attempt to recover from an error state for a player. Args: player_id: The…, Get error handling statistics. Args: online_players: Online players dictionary… (+18 more)

### Community 367 - ".check_bidirectional_connections"
Cohesion: 0.11
Nodes (9): Get the opposite direction for bidirectional checking., Find rooms with no exits (dead ends). Args: room_database: Dictionary mapping…, Find rooms that reference themselves in exits. Args: room_database: Dictionary…, Generate minimap graph data for visualization. Args: room_database: Dictionary…, Build adjacency graph from room database. Args: room_database: Dictionary…, Get target room ID from exit data., Check if exit is marked as one-way., Extract zone and sub_zone from room data. Args: room_id: Room identifier… (+1 more)

### Community 368 - "SQLAlchemy Best Practices (2.x Style)"
Cohesion: 0.12
Nodes (17): 1.1 Declarative Models with Type Annotations, 1.2 Mixins for Common Fields, 1. Code Organization and Data Modeling, 2.1 Context Manager for Sessions, 2.2 Explicit Transaction Blocks, 2. Session Management, 3.1 Use `select()` for All Queries, 3.2 Eager Loading Relationships (+9 more)

### Community 369 - "Uplift Strategy"
Cohesion: 0.04
Nodes (49): 0.2 Update conftest.py ✅, 2.1 Categorize Unit Tests by Dependency Pattern, 4.1 Test ApplicationContainer Itself, Actions, AFTER, AFTER, AFTER, AFTER (+41 more)

### Community 370 - "test_quest_instance_repository.py"
Cohesion: 0.07
Nodes (49): QuestInstance, Per-character quest state: one row per player per quest., Any, datetime, UUID, QuestInstanceRepository, Get the quest instance for this player and quest (any state). Returns None if…, Update an instance's state and/or progress. Pass only fields to change. (+41 more)

### Community 371 - "CastingStateManager"
Cohesion: 0.09
Nodes (24): CastingStateManager, Any, UUID, Check if a player is currently casting. Args: player_id: Player ID to check…, Get the casting state for a player. Args: player_id: Player ID Returns:…, Complete and remove a casting state. Args: player_id: Player ID Returns:…, Interrupt and remove a casting state. Args: player_id: Player ID Returns:…, Update casting progress for a player. Args: player_id: Player ID current_tick:… (+16 more)

### Community 372 - "PydanticErrorHandler"
Cohesion: 0.05
Nodes (43): MythosValidationError, convert_pydantic_error(), _ExtractedErrorInfo, _ExtractedFieldErrorInfo, handle_pydantic_error(), TypedDict, Unpack, ValidationError (+35 more)

### Community 373 - "NPCCombatIntegrationBase"
Cohesion: 0.06
Nodes (27): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Apply combat effects to a target (player or NPC). Args: target_id: ID of the…, Convert target_id to UUID, accepting either string or UUID input., Apply combat effects to a player. (+19 more)

### Community 374 - "DialogueDefinitionRepository"
Cohesion: 0.18
Nodes (20): _definition_dict(), DialogueDefinitionRepository, Coerce JSONB definition cell to a plain string-keyed dict., Repository for dialogue_definitions via stored procedures., _mock_session_with_rows(), asyncio, fixture, Unit tests for DialogueDefinitionRepository. (+12 more)

### Community 375 - "test_look_helpers.py"
Cohesion: 0.03
Nodes (87): _get_health_label(), _get_lucidity_label(), _get_wearable_container_service(), _parse_instance_number(), Any, Get descriptive lucidity label based on lucidity percentage. Args: stats:…, Get shared WearableContainerService instance, initializing it lazily if needed.…, Parse instance number from target string. Supports two formats: - "backpack-2"… (+79 more)

### Community 376 - "TestHierarchicalSchema"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 377 - "GameClientV2ContainerView.tsx"
Cohesion: 0.10
Nodes (17): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, TabbedInterfaceOverlay(), TabbedInterfaceOverlayProps (+9 more)

### Community 378 - "utils/layout.ts"
Cohesion: 0.10
Nodes (36): UseMapLayoutOptions, applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyLinkForces() (+28 more)

### Community 379 - "player.ts"
Cohesion: 0.11
Nodes (33): locationIndicatesDeathVoid(), requiredAliveButDeadMessage(), assertLookVisibleInPanels(), lookAndStand(), prepAwForAdminSet(), prepNonAdminForSetAttempt(), runAdminSetWithRecovery(), assertNpcSpawnVisible() (+25 more)

### Community 380 - "FastAPI Code Review - Anti-Patterns and Best Practices"
Cohesion: 0.05
Nodes (40): 10. ℹ️ **Dependency Injection Pattern**, 11. ℹ️ **API Versioning** (OPTIONAL - NOT REQUIRED FOR WEBAPP), 1. ✅ **Inconsistent Response Models** - **RESOLVED**, 1. Response Models (Critical Issue #1) ✅, 2. Dependency Injection (Critical Issue #3) ✅, 2. 🟡 **Fat Endpoints with Business Logic** - **IN PROGRESS**, 3. ✅ **Direct app.state Access Instead of Dependency Injection** - **RESOLVED**, 3. Error Handling (Medium Issue #7) ✅ (+32 more)

### Community 381 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 382 - "subject_controller.py"
Cohesion: 0.10
Nodes (41): get_patterns(), get_subject_statistics(), PatternsResponse, BaseModel, get, post, NATS Subject Management API Controller for MythosMUD. This module provides REST…, Dependency to require admin permissions. Args: current_user: Current… (+33 more)

### Community 383 - "Any"
Cohesion: 0.07
Nodes (17): Any, AsyncSession, UUID, Get a list of rooms adjacent to the specified room. Args: room_id: The room's…, Get the scope of rooms for local chat (current room + adjacent rooms). Args:…, Validate that there's a valid exit from one room to another. Args:…, Get all occupants (players and NPCs) currently in a room using cached data.…, Get all exits from a room. Args: room_id: The ID of the room Returns: dict[str,… (+9 more)

### Community 384 - "combat_attack.py"
Cohesion: 0.08
Nodes (39): _execute_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution. Extracted from combat.py to…, Resolve damage from equipped weapon or fall back to config unarmed damage., Execute combat action using the proper combat service., Handle attack commands (attack, punch, kick, etc.)., Validate target name, load player/room, check DP and no_combat. Returns… (+31 more)

### Community 385 - "NPCCacheService"
Cohesion: 0.23
Nodes (8): NPCCacheService, Service for caching NPC definitions and spawn rules., Invalidate all NPC definition caches., Invalidate all NPC spawn rule caches., _NpcDef, asyncio, _SpawnRule, TestNPCCacheService

### Community 386 - "test_magic_service.py"
Cohesion: 0.15
Nodes (39): CastingState, Represents an active spell casting state., MagicService, Public API: composition of completion, healing, and core spellcasting logic., _build_magic_service(), magic_service(), mock_player(), player_id() (+31 more)

### Community 387 - "NPCCombatDataProvider"
Cohesion: 0.09
Nodes (27): NPCCombatDataProvider, Any, UUID, Get player name for messaging. Args: player_id: ID of the player Returns:…, Get the current room ID for a player. Args: player_id: ID of the player (must…, Get player combat participant data from persistence. Args: player_id: ID of the…, Get NPC combat participant data from NPC instance. Args: npc_instance: NPC…, Provides data retrieval and preparation for NPC combat. (+19 more)

### Community 388 - "test_player_related_models.py"
Cohesion: 0.07
Nodes (34): PlayerChannelPreferences, PlayerExploration, Base, Player channel preferences model for Advanced Chat Channels. Stores player…, Junction table tracking which rooms each player has explored., Unit tests for Player-related SQLAlchemy models. Tests…, Test PlayerInventory has correct table name., Test PlayerInventory __repr__ method. (+26 more)

### Community 389 - "test_async_persistence_core.py"
Cohesion: 0.04
Nodes (60): asyncio, Unit tests for async persistence layer: init, close, player, user, room,…, Test get_players_by_user_id delegates to PlayerRepository., Test get_active_players_by_user_id delegates to PlayerRepository., Test get_user_by_username_case_insensitive with successful lookup., Test get_user_by_username_case_insensitive when user not found., Test get_user_by_username_case_insensitive with database error., Test save_player delegates to PlayerRepository. (+52 more)

### Community 390 - "pylint Best Practices"
Cohesion: 0.12
Nodes (15): 1.1. Silence the Noise, Enable What Matters, 1.2. Filter by Confidence, 1. Configuration is King: `pyproject.toml`, 2.1. Docstrings for Everything, 2.2. Naming Conventions, 2.3. Manage Complexity, 2. Code Organization & Readability, 3.1. Specific Exception Handling (+7 more)

### Community 391 - "test_message_broadcaster.py"
Cohesion: 0.07
Nodes (41): message_broadcaster(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for message broadcaster. Tests the MessageBroadcaster class., Test broadcast_global() excludes specified player., Test broadcast_global() when no players online. (+33 more)

### Community 392 - "TestNPCCombatRewards"
Cohesion: 0.07
Nodes (21): asyncio, fixture, Unit tests for NPC combat rewards. Tests the NPCCombatRewards class for XP…, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class. (+13 more)

### Community 393 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 394 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 395 - "TaskRegistry"
Cohesion: 0.15
Nodes (29): get_registry(), Centralized TaskRegistry for MythosMUD server task lifecycle management. This…, Convenience function for registering tasks with global registry., Access the global TaskRegistry., Centralized asyncio task registry for lifecycle-tracking with timeout…, Initialize TaskRegistry with empty task collections., register_task(), TaskRegistry (+21 more)

### Community 396 - "useMythosAppState.ts"
Cohesion: 0.12
Nodes (21): MythosAppViewModel, AppActions, AppState, buildActionViewModel(), buildMythosAppViewModel(), buildStateViewModel(), hoisted, useMythosApp() (+13 more)

### Community 397 - "TestCombatMessagingService"
Cohesion: 0.05
Nodes (34): CombatMessages, CombatMessagingService, Any, Generate combat start messages for all room occupants. Args: attacker_name:…, Generate combat end messages for all room occupants. Args: winner_name: Name of…, Generate thematic error messages for combat actions. Args: error_type: Type of…, Validate NPC message templates against the schema. Args: messages_data: NPC…, Service for generating combat messages. This service creates thematic,… (+26 more)

### Community 398 - "Phase 1: Core Separation"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 1: Core Separation, Sub-tasks, Sub-tasks (+8 more)

### Community 399 - "MythosMUD Test Writing"
Cohesion: 0.29
Nodes (7): Test Writing Skill, Coverage, How to Run Tests, MythosMUD Test Writing, Reference, Rules, Where Tests Live

### Community 400 - "test_connection_initialization.py"
Cohesion: 0.09
Nodes (33): initialize_connection_cleaner(), initialize_connection_state(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging(), initialize_room_event_handler(), Any (+25 more)

### Community 401 - "NATSPublishError"
Cohesion: 0.08
Nodes (23): NATS, NATSPublishError, Raised when message publishing fails., NATSServicePoolMixin, Any, NATS connection pool and batch publishing (extracted from nats_service)., Get connection from pool. Raises: NATSPublishError: If no connection is…, Return connection to pool. (+15 more)

### Community 402 - "Phase 2: Enhanced Features"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 2: Enhanced Features, Sub-tasks, Sub-tasks (+8 more)

### Community 403 - "CombatCommandHandler"
Cohesion: 0.03
Nodes (70): CombatCommandHandler, Any, AppWithState, Combat service for command modules., Movement service for command modules., Player position service for command modules., Check if player is resting or in login grace period, interrupt rest if needed.…, Extract command type and target name from command_data. Public API. (+62 more)

### Community 404 - "log_exception_once"
Cohesion: 0.08
Nodes (25): Any, AsyncSession, Player, UUID, Ensure player posture is set to lying when dead. Args: player: Player object to…, Clear player combat state when they die. BUGFIX #244: As documented in…, Get room name for death location display. Args: death_location: Room ID where…, Publish player died event if event bus is available. Args: player_id: ID of the… (+17 more)

### Community 405 - "player_connection_setup.py"
Cohesion: 0.11
Nodes (38): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions. This module handles the setup tasks when a…, Broadcast a structured entry event to other occupants (excluding the newcomer).… (+30 more)

### Community 406 - "CommandPanel.tsx"
Cohesion: 0.10
Nodes (19): CommandPanel(), CommandPanelProps, logCommandPanelConnectionDebug(), useCommandPanelEffects(), applyChannelPrefix(), prepareCommandForSubmit(), prependChannelShortcut(), prependPartyPrefix() (+11 more)

### Community 407 - "WebSocketRequestContext"
Cohesion: 0.06
Nodes (45): command_request_app_state(), CommandExecutionRequest, Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…, create_websocket_request_context(), Any, Get the event bus from the request context., Factory function to create a WebSocket request context. Args: app_state: Real…, Creates FastAPI Request-like objects for WebSocket commands. This allows… (+37 more)

### Community 408 - "test_command_helpers.py"
Cohesion: 0.04
Nodes (68): Unit tests for command_helpers utility functions. Tests the utility functions…, Test validate_command_safety() returns True for safe commands., Test validate_command_safety() returns False for shell metacharacters., Test validate_command_safety() returns False for SQL injection attempts., Test validate_command_safety() returns False for Python injection attempts., Test validate_command_safety() returns False for format string injection., Test validate_command_safety() returns False for XSS attempts., Test get_command_help() returns help for specific command. (+60 more)

### Community 409 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 410 - "UUID"
Cohesion: 0.17
Nodes (9): Any, UUID, Broadcast party message to party members only, with dampening and mute checks., Send whisper message to specific player with communication dampening., Broadcast system/admin message; personal when target_player_id is set., Handle unknown channel type., Broadcast message according to channel strategy. Args: chat_event: WebSocket…, Broadcast room-based message with server-side filtering. (+1 more)

### Community 411 - "schemas/unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 412 - "Chat Panel Separation Implementation Tasks"
Cohesion: 0.20
Nodes (9): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Overview, Phase Dependencies, Risk Mitigation, Technical Risks (+1 more)

### Community 413 - "Async Persistence Migration Plan"
Cohesion: 0.05
Nodes (37): 1.1 Find all PersistenceLayer usage, 1.2 Document call sites, 2.1 Update ApplicationContainer, 2.2 Update lifespan.py, 2.3 Migrate API endpoints, 2.4 Migrate services, 2.5 Migrate commands, 2.6 Update test fixtures (+29 more)

### Community 414 - "test_combat_persistence_handler.py"
Cohesion: 0.09
Nodes (23): mock_combat_service(), mock_player(), persistence_handler(), fixture, Unit tests for combat persistence handler - core functionality. Tests…, Create mock combat service., Create CombatPersistenceHandler instance., Test CombatPersistenceHandler initialization. (+15 more)

### Community 415 - "NATSMessageBroker"
Cohesion: 0.07
Nodes (34): MessageBrokerConnectionError, MessageBrokerError, PublishError, Exception, Message Broker abstraction for MythosMUD. This module defines the MessageBroker…, Base exception for message broker errors., Exception raised when connection to message broker fails., Exception raised when publishing message fails. (+26 more)

### Community 416 - "test_lucidity_repository.py"
Cohesion: 0.11
Nodes (33): mock_session(), _MockAsyncSession, asyncio, fixture, Unit tests for LucidityRepository., increment_exposure_state creates record when absent., increment_exposure_state bumps count on existing record., get_cooldown returns cooldown record. (+25 more)

### Community 417 - "test_population_stats.py"
Cohesion: 0.05
Nodes (39): Unit tests for population statistics. Tests the PopulationStats class., Test remove_npc() removes optional NPC., Test remove_npc() decrements count when multiple exist., Test remove_npc() handles removal when NPC not found., Test PopulationStats initialization., Test remove_npc() prevents negative counts., Test remove_npc() handles None definition_id., Test remove_npc() updates last_updated timestamp. (+31 more)

### Community 418 - "test_message_handlers.py"
Cohesion: 0.07
Nodes (44): handle_chat_message(), handle_client_error_report_message(), handle_command_message(), handle_ping_message(), Any, WebSocket, Handle client_error_report: log client-reported errors to errors.log (via…, Handle command message type. (+36 more)

### Community 419 - "test_container_persistence.py"
Cohesion: 0.05
Nodes (37): Unit tests for container_persistence helpers and fetch_container_items. Tests…, Test fetch_container_items with items., Test fetch_container_items skips rows with missing item_instance_id., Test fetch_container_items handles non-dictionary rows., Test fetch_container_items parses string metadata., Test fetch_container_items handles invalid JSON metadata., Test fetch_container_items handles non-dict metadata., Test parsing None JSONB column. (+29 more)

### Community 420 - "test_health_monitor.py"
Cohesion: 0.11
Nodes (22): asyncio, Unit tests for health monitor. Tests the HealthMonitor class., Test check_all_connections_health() checks all connections., Test start_periodic_checks() starts periodic checks., Test stop_periodic_checks() stops periodic checks., Test HealthMonitor initialization., Test check_player_connection_health() returns health status., Test check_player_connection_health() when player has no websockets. (+14 more)

### Community 421 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 422 - "test_combat_persistence_handler_persistence.py"
Cohesion: 0.07
Nodes (38): mock_combat_service(), mock_player(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - persistence operations. Tests…, Test _persist_player_dp_sync calls _verify_player_save., Test _persist_player_dp_sync handles save_player error. (+30 more)

### Community 423 - "PlayerRespawnWrapper"
Cohesion: 0.19
Nodes (15): PlayerRespawnWrapper, Any, Respawn a delirious player by user ID. This method handles the complete…, Wrapper service for player respawn operations., Initialize with a persistence layer., Respawn a dead player by user ID. This method handles the complete respawn…, _dead_player(), asyncio (+7 more)

### Community 424 - "test_lucidity_trigger_handlers.py"
Cohesion: 0.26
Nodes (16): handle_delirium_trigger(), Handle delirium respawn threshold (LCD crosses -10); debounced., lucidity_record(), player_id(), asyncio, fixture, UUID, Unit tests for lucidity trigger handlers. (+8 more)

### Community 425 - "useRoomEditModal.ts"
Cohesion: 0.07
Nodes (19): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, fieldBorderClass(), RoomEditDescriptionField(), RoomEditFormData, RoomEditModalForm() (+11 more)

### Community 426 - "NATS Complete Remediation Summary"
Cohesion: 0.05
Nodes (36): 1. Error Handling Standardization, 2. Message Validation, 3. Batch Flush Error Recovery, 4. Connection Pool Error Handling, 5. Subject Manager Integration, 6. Health Monitoring, 7. Acknowledgment Metrics, 8. Wildcard Validation (+28 more)

### Community 427 - "PostgreSQL & SQL Audit Report"
Cohesion: 0.05
Nodes (36): 10. Prioritized Fixes, 11. Summary Table, 1.1. Snake_case (GOOD), 1.2. Quoted Identifier, 1. Naming Conventions, 2.1. Uppercase SQL Keywords, 2. SQL Formatting (Keywords Lowercase), 3.1. Explicit Joins (GOOD) (+28 more)

### Community 428 - "Critical Coverage Gaps"
Cohesion: 0.06
Nodes (32): Critical Coverage Gaps, Gap 10: Configuration Edge Cases, Gap 1: Domain Layer (NEW ARCHITECTURE), Gap 2: Message Broker Abstraction, Gap 3: ApplicationContainer Lifecycle, Gap 4: Error Recovery Paths, Gap 5: Async/Await Pattern Verification, Gap 6: Rate Limiting and Throttling (+24 more)

### Community 429 - "Phase 3, Task 3.2: NATS Subject Manager Usage Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 430 - "Execution Steps"
Cohesion: 0.05
Nodes (36): BEFORE EXECUTING THIS SCENARIO, YOU MUST, BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, CONFIRMATION CHECKLIST, EXECUTION AFFIRMATION (Type this before proceeding), 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER, Execution Steps, Expected Results (+28 more)

### Community 431 - "properties"
Cohesion: 0.12
Nodes (17): description, items, type, properties, default, description, type, type (+9 more)

### Community 432 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 433 - "properties"
Cohesion: 0.17
Nodes (12): description, description, description, description, maxLength, minLength, type, properties (+4 more)

### Community 434 - "test_game_tick_processing_async.py"
Cohesion: 0.07
Nodes (41): _process_heal_over_time_effect(), Process a heal over time effect. Returns: True if effect was applied, False…, mock_app(), mock_container(), mock_player(), asyncio, fixture, Unit tests for game tick processing async functions. Tests the async game tick… (+33 more)

### Community 435 - "ValidationError"
Cohesion: 0.02
Nodes (165): Data validation errors (e.g. empty local/whisper message). Log at warning, not…, ValidationError, Validate that a profession exists and return it. This method encapsulates the…, Test ValidationError can be instantiated., test_validation_error(), Unit tests for inventory command factory helper functions. Tests the helper…, Test create_equip_command() with item name and inferred slot., Test create_unequip_command() with slot. (+157 more)

### Community 436 - "RoomCacheService"
Cohesion: 0.15
Nodes (7): Service for caching room data., Invalidate cached room data. Args: room_id: The room ID to invalidate, Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload, RoomCacheService, Any, _RoomObj, TestRoomCacheService

### Community 437 - "pytest Best Practices"
Cohesion: 0.13
Nodes (15): 1.1 Project Layout, 1.2 Test File Naming, 1.3 Test Naming Conventions, 1. Code Organization & Structure, 2.1 Single Assert Per Test, 2.2 Fixtures for Setup/Teardown & Dependency Injection, 2.3 Parameterization, 2.4 Markers (+7 more)

### Community 438 - "MemoryProfiler"
Cohesion: 0.04
Nodes (58): OtherModel, BaseModel, Unit tests for memory profiler utilities. Tests the MemoryProfiler class…, Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test Pydantic model for memory profiling tests., Test MemoryProfiler.print_model_memory_usage() doesn't raise. (+50 more)

### Community 439 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 440 - "fastapi_integration.py"
Cohesion: 0.05
Nodes (38): auth_service(), BackgroundTasks, create_player(), File, general_exception_handler(), get_player(), http_exception_handler(), list_players() (+30 more)

### Community 441 - "migration_examples.py"
Cohesion: 0.06
Nodes (36): expensive_operation(), migration_example_1(), migration_example_10(), migration_example_11(), migration_example_12(), migration_example_13(), migration_example_14(), migration_example_15() (+28 more)

### Community 442 - "InventoryMutationGuard"
Cohesion: 0.09
Nodes (18): _AsyncPlayerGuardState, InventoryMutationGuard, _PlayerGuardState, Acquire sync mutation guard., Acquire async mutation guard., Get or create per-player guard state for sync contexts. Uses thread-safe…, Get or create per-player guard state for async contexts. Uses async lock to…, Clean up per-player guard state when no longer needed (sync context). Removes… (+10 more)

### Community 443 - "properties"
Cohesion: 0.11
Nodes (19): description, description, description, description, type, description, maxLength, minLength (+11 more)

### Community 444 - "safe_run_static"
Cohesion: 0.05
Nodes (52): get_project_root(), Determine the project root based on current working directory, main(), Run a psql command and return the result., Load all seed data files., run_psql_command(), _combined_output(), _CompletedProcessLike (+44 more)

### Community 445 - "NATSConfig"
Cohesion: 0.11
Nodes (15): NATSConfig, Any, BaseSettings, field_validator, NATS messaging configuration., Validate TLS file paths exist when TLS is enabled., Validate max payload is reasonable., Validate value is positive. (+7 more)

### Community 446 - "CombatCommandFactory"
Cohesion: 0.08
Nodes (31): Unit tests for combat command factories. Tests the CombatCommandFactory class…, Test create_attack_command() creates AttackCommand., Test create_attack_command() allows None target (validation happens later)., Test create_punch_command() creates PunchCommand., Test create_punch_command() allows None target (validation happens later)., Test create_kick_command() creates KickCommand., Test create_kick_command() allows None target (validation happens later)., Test create_strike_command() creates StrikeCommand. (+23 more)

### Community 447 - "ChatMessage"
Cohesion: 0.12
Nodes (34): ChatMessage, Store global message in history., store_global_message_in_history(), Any, UUID, Represents a chat message with metadata., Convert message to dictionary for serialization., Log this chat message to the communications log. (+26 more)

### Community 448 - "test_npc_threading_messages.py"
Cohesion: 0.06
Nodes (34): Lock, Initialize metrics collector. AI: Uses Lock for thread-safety in async context., NPCCommunicationBridge, NPCMessageQueue, Initialize the NPC message queue. Args: max_messages_per_npc: Maximum number of…, Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…, Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…, Clear all pending messages for an NPC. Args: npc_id: The NPC's ID Returns:… (+26 more)

### Community 449 - "PostgresConnection"
Cohesion: 0.08
Nodes (18): PostgresConnection, connection, Commit the current transaction., Rollback the current transaction., Close the connection., PostgreSQL connection wrapper for persistence layer operations., Test PostgresConnection initialization., Test PostgresConnection.execute(). (+10 more)

### Community 450 - "Fix patterns by tier"
Cohesion: 0.13
Nodes (13): 🔴 Critical — import and name errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — type errors, 🔵 Low — type precision, 🟢 Medium — type refinement, Mypy Remediation — Reference (+5 more)

### Community 451 - "game_tick_processing.py"
Cohesion: 0.08
Nodes (55): Set the current game tick (game tick loop)., Reset the current tick for testing., reset_current_tick(), set_current_tick(), _app_container(), broadcast_tick_event(), game_tick_loop(), get_tick_interval() (+47 more)

### Community 452 - "stateNormalization.ts"
Cohesion: 0.16
Nodes (18): createEntityMap(), denormalizeGameData(), Entity, EntityMap, extractEntities(), GameData, getEntitiesByIds(), getEntitiesByType() (+10 more)

### Community 453 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 454 - "Coverage Improvement Summary - Plan 2 Execution"
Cohesion: 0.06
Nodes (34): 🏆 Achievement Highlights, API Endpoints (Tests Created, Pending Fresh Session), Auth (Tests Created, Pending Fresh Session), Caching (100% Complete), Challenges Encountered, Code Quality, Commands (Tests Created, Pending Fresh Session), ✅ COMPLETED & VERIFIED (6 modules) (+26 more)

### Community 455 - "Memory Leak Audit Report"
Cohesion: 0.06
Nodes (34): 1.1 Database Connection Pools, 1.2 WebSocket Connection Leaks, 1.3 NATS Connection and Subscription Leaks, 1. Connection Management Leaks, 2.1 EventBus Subscriber Leaks, 2.2 Client-Side Event Handler Leaks, 2. Event System Leaks, 3.1 Task Registry Leaks (+26 more)

### Community 456 - "CacheManager"
Cohesion: 0.14
Nodes (9): CacheManager, Any, Centralized cache manager for MythosMUD server. Manages multiple LRU caches for…, Initialize the cache manager., Initialize default caches with appropriate configurations., Get a cache by name. Args: name: The name of the cache Returns: The cache…, Create a new cache. Args: name: The name of the cache max_size: Maximum number…, Delete a cache. Args: name: The name of the cache to delete Returns: True if… (+1 more)

### Community 457 - "ProfessionCacheService"
Cohesion: 0.17
Nodes (7): ProfessionCacheService, Service for caching profession data., Initialize the profession cache service. Args: persistence: Persistence layer…, Get a specific profession by ID with caching. Args: profession_id: The…, Invalidate all profession caches., Create room and profession cache services; set to None on RuntimeError., TestProfessionCacheService

### Community 458 - "test_inventory_get_command.py"
Cohesion: 0.16
Nodes (29): _container_transfer_messages(), _get_from_container_path(), _get_route_after_validation(), _get_transfer_out_of_container(), GetCommandRuntime, GetItemSpec, handle_get_command(), _handle_get_from_room() (+21 more)

### Community 459 - "MovementMonitor"
Cohesion: 0.11
Nodes (15): MovementMonitor, Any, UUID, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms., Get comprehensive movement metrics., Get current alerts based on thresholds. (+7 more)

### Community 460 - "test_player_preferences_service.py"
Cohesion: 0.03
Nodes (102): asyncio, Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID., Test creating player preferences when they already exist., Test creating player preferences with invalid ID., Test creating player preferences with integrity error. (+94 more)

### Community 461 - "Lint Remediation"
Cohesion: 0.14
Nodes (12): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — code quality, Lint Remediation — Reference, 🟢 Medium — style, Entry point (+4 more)

### Community 462 - "logger.ts"
Cohesion: 0.06
Nodes (38): ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach(), wsConnectionBeforeEach() (+30 more)

### Community 463 - "NATS Anti-Patterns and Best Practices Review"
Cohesion: 0.06
Nodes (33): 10. **Missing Connection Health Monitoring in Broker** (Observability), 1. **Excellent Error Boundary Implementation**, 1. **Synchronous Operations in Non-Handler Context** (Low Priority), 2. **Event Handler Callbacks May Block** (Anti-pattern), 2. **Good Connection State Management**, 3. **Inconsistent Error Handling Patterns** (Code Quality), 3. **Proper Async/Await Usage**, 4. **Missing Input Validation in Some Methods** (Security/Reliability) (+25 more)

### Community 464 - "Persistence Layer Refactoring - COMPLETE ✅"
Cohesion: 0.06
Nodes (33): 1. Modular Architecture, 2. Async Foundation, 3. Zero Breaking Changes, 4. Comprehensive Documentation, 5. Quality Maintained, Backward Compatibility, 📈 Benefits, Code Created (+25 more)

### Community 465 - "Persistence Layer Refactoring Summary"
Cohesion: 0.06
Nodes (33): 1. PlayerRepository (439 lines), 2. RoomRepository (42 lines), 3. ProfessionRepository (74 lines), 4. HealthRepository (165 lines), 5. ExperienceRepository (203 lines), 6. ContainerRepository (80 lines), 7. ItemRepository (84 lines), Async Repository Structure (+25 more)

### Community 466 - "Test Pruning Candidates - Detailed List"
Cohesion: 0.06
Nodes (35): 1. Command Validation Tests, 2. Error Response Tests, 3. Permission Check Tests, Aggressive Estimate (Full Optimization), Category A: Infrastructure Tests Testing Framework Behavior, Category B: Coverage Tests Written for Metrics, Category C: Model Property Tests, Conclusion (+27 more)

### Community 467 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 468 - "test_lucidity_command_disruption.py"
Cohesion: 0.16
Nodes (19): can_perform_action(), get_misfire_message(), Command disruption utilities for lucidity system. Implements command misfires…, Check if a command should misfire based on tier and command type. Args:…, Get the misfire message for a failed command. Args: command_type: Type of…, Check if player should involuntarily flee. Args: tier: Current lucidity tier…, Check if player can perform actions (motor lock check). Args: tier: Current…, should_involuntary_flee() (+11 more)

### Community 469 - "Path"
Cohesion: 0.10
Nodes (14): Any, Path, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper…, Get the whisper channel log file path. Returns: Path to the whisper channel log…, Get the system channel log file path. Returns: Path to the system channel log… (+6 more)

### Community 470 - "StatusEffect"
Cohesion: 0.04
Nodes (68): InventoryItem, Player, BaseModel, Represents an item in a player's inventory., Pydantic Player model for game logic and validation. This is separate from the…, Add an item to the player's inventory. Args: item_id: Unique identifier for the…, Remove an item from the player's inventory. Args: item_id: Unique identifier…, Add a status effect to the player. Args: effect: StatusEffect to add (+60 more)

### Community 471 - "panelReducerHandlers.ts"
Cohesion: 0.16
Nodes (27): savePanelLayout(), PanelAction, panelActionHandlers, PanelReducerHandler, computeMinimizedDockPosition(), getDefaultViewport(), getMinimizedPanelIds(), MINIMIZED_BAR_HEIGHT (+19 more)

### Community 472 - "DialogueService"
Cohesion: 0.06
Nodes (47): DialogueCursor, DialoguePrompt, DialogueService, format_dialogue_prompt(), get_dialogue_service(), UUID, In-memory dialogue session service for classic MUD talk (#583). Loads trees by…, Load and validate a dialogue tree, or clear cursor and return fade text. (+39 more)

### Community 473 - "PlayerRepositoryProtocol"
Cohesion: 0.11
Nodes (19): PlayerRepositoryProtocol, datetime, Player, UUID, Protocol for player persistence operations. Defines the contract used by…, Get the first active player for a user ID., Get all players (including deleted) for a user ID., Get active (non-deleted) players for a user ID. (+11 more)

### Community 474 - "TestPostgresConnectionPool"
Cohesion: 0.11
Nodes (17): is_postgres_url(), PostgresConnectionPool, Thread-safe PostgreSQL connection pool., Get or create a connection pool for the given database URL., Get a connection from the pool., Check if the database URL is PostgreSQL., patch, Test PostgresConnectionPool class. (+9 more)

### Community 475 - ".to_dict"
Cohesion: 0.17
Nodes (7): Any, Get list of object IDs currently in the room. Returns: List of object IDs in…, Get list of NPC IDs currently in the room. Returns: List of NPC IDs in the room, Get the total number of occupants in the room. Returns: Total count of players,…, Check if the room has no occupants. Returns: True if the room is empty, False…, Get list of containers in this room. Returns: List of container data…, Convert the room to a dictionary representation. Returns: Dictionary containing…

### Community 476 - "e2e-bootstrap.ts"
Cohesion: 0.15
Nodes (27): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+19 more)

### Community 477 - "MemoryThresholdMonitor"
Cohesion: 0.10
Nodes (34): create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryThresholdMonitor, Create an instance of the MemoryThresholdMonitor with user-specified…, Factory function returning implementation conforming to Task 4.3 Specified…, Runtime monitor for detecting memory threshold violations requiring cleanup.…, asyncio, Unit tests for memory threshold monitoring and managed task cleanup. (+26 more)

### Community 478 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 479 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 480 - "Stop-MythosMudProjectProcessTree"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 481 - "spell_effects_status.py"
Cohesion: 0.09
Nodes (35): _apply_player_status_with_grace_check(), _apply_status_effect_to_player(), _grace_period_blocks_negative_status_effect(), _handle_player_status_effect(), _maybe_run_force_flee_effect(), _parse_status_effect_metadata(), Any, UUID (+27 more)

### Community 482 - "test_statistics_aggregator.py"
Cohesion: 0.10
Nodes (24): mock_memory_monitor(), mock_message_queue(), mock_performance_tracker(), mock_rate_limiter(), mock_room_manager(), fixture, Unit tests for statistics aggregator. Tests the StatisticsAggregator class., Test get_connection_stats() returns connection statistics. (+16 more)

### Community 483 - "container_query_helpers_async.py"
Cohesion: 0.14
Nodes (28): _build_container_data_from_row_async(), get_containers_by_entity_id_async(), get_containers_by_room_id_async(), get_decayed_containers_async(), _parse_jsonb(), Any, AsyncSession, ContainerData (+20 more)

### Community 484 - "Client Test Remediation"
Cohesion: 0.15
Nodes (11): Client Test Remediation — Reference, 🔴 Critical — TypeScript/rendering errors, Debugging when a fix doesn't take, Fix patterns by tier, 🟡 High — component issues, 🟢 Medium — hook/async issues, Client Test Remediation, Entry point (+3 more)

### Community 485 - "Phase 3: Polish and Optimization"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 3: Polish and Optimization, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 486 - "Phase 4: Testing and Refinement"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 4: Testing and Refinement, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 487 - "PlayerPreferencesService"
Cohesion: 0.15
Nodes (17): PlayerPreferencesService, Any, AsyncSession, UUID, Get preferences for a player. Args: session: Database session player_id: The…, Update a player's default channel. Args: session: Database session player_id:…, Mute a channel for a player. Args: session: Database session player_id: The…, Unmute a channel for a player. Args: session: Database session player_id: The… (+9 more)

### Community 488 - "disconnect_grace_period.py"
Cohesion: 0.06
Nodes (56): cancel_grace_period(), Any, UUID, Disconnect grace period management for MythosMUD. This module handles the…, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, Start a grace period for a disconnected player. During the grace period, the…, start_grace_period(), _cleanup_player_references() (+48 more)

### Community 489 - "performance.test.tsx"
Cohesion: 0.12
Nodes (13): Channel, ChannelSelectorProps, MemoryUsageDisplayProps, PerformanceChartProps, TerminalButtonProps, TerminalInputProps, ExtendedPerformance, PerformanceMemory (+5 more)

### Community 490 - "multiplayer-browser-helpers.js"
Cohesion: 0.15
Nodes (29): buttonHasLoginSubmitLabel(), captureGameUiDiagnosticsInBrowser(), captureOccupantsSnapshotInBrowser(), computedStyleHidesElement(), elementShowsConnectedStatus(), elementTextIncludesGameInfo(), evaluateGameUiLoaded(), fieldHasCommandPlaceholder() (+21 more)

### Community 491 - "Client Test Remediation"
Cohesion: 0.18
Nodes (10): Client Test Remediation, 🔴 Critical — TypeScript/rendering errors, Debugging when a fix doesn't take, Entry point, Fix patterns by tier, Fix-verify loop, 🟡 High — component issues, 🟢 Medium — hook/async issues (+2 more)

### Community 492 - "Async Audit Executive Summary"
Cohesion: 0.06
Nodes (31): Alternative Approaches Considered, Async Audit Executive Summary, Benefit, Break-Even, Contact, Cost, Cost-Benefit Analysis, Critical Findings (+23 more)

### Community 493 - "PARALLEL EXECUTION RESULTS (2025-11-05)"
Cohesion: 0.06
Nodes (31): 1. **Mark Additional Slow Tests**, 2. **Investigate Heavy Setup Tests**, 3. **Verify Marker Application**, 4. **Target Time Budget (5-7 min = 300-420 seconds)**, After Parallelization, Argon2 Password Tests (1.4+ seconds), Auth & Security Tests (21+ seconds setup each), Before Parallelization (+23 more)

### Community 494 - "_collect_python_public_defs_and_tiny"
Cohesion: 0.23
Nodes (12): _check_exports_and_tiny_functions(), _collect_python_public_defs_and_tiny(), _is_public_function_stmt(), _is_test_file_path(), _is_tiny_single_use(), AST, AsyncFunctionDef, FunctionDef (+4 more)

### Community 495 - "TestLogoutCommand"
Cohesion: 0.11
Nodes (17): Any, asyncio, fixture, Unit tests for the logout command handler., Test logout command when persistence is not available., Test logout command when persistence operations fail., Test cases for the logout command handler., Test logout command when connection cleanup fails. (+9 more)

### Community 496 - "test_admin_permission_utils.py"
Cohesion: 0.27
Nodes (11): _BrokenAdminPlayer, mock_admin_logger(), asyncio, fixture, Unit tests for admin permission validation., test_validate_admin_permission_attribute_error(), test_validate_admin_permission_granted(), test_validate_admin_permission_is_admin_false() (+3 more)

### Community 497 - "ChatModeration"
Cohesion: 0.07
Nodes (26): ChatModeration, normalize_player_id(), datetime, UUID, Mute a specific channel for a player., Unmute a specific channel for a player., Check if a channel is muted for a player., Mute a specific player for another player. (+18 more)

### Community 498 - "test_npc_combat_integration_service_player_attacks.py"
Cohesion: 0.09
Nodes (30): asyncio, Unit tests for NPC combat integration service - player-initiated combat paths., Test handle_player_attack_on_npc returns False when NPC not found., Test handle_player_attack_on_npc handles exceptions gracefully., Test _setup_combat_uuids_and_mappings handles ValueError., Test _setup_combat_uuids_and_mappings with valid UUID., Test store_npc_xp_mapping_for_mixin when NPC definition is not found., Test store_npc_xp_mapping_for_mixin when base_stats is not a dict. (+22 more)

### Community 499 - "test_combat_persistence_handler_events.py"
Cohesion: 0.06
Nodes (43): mock_combat_service(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully., Test _publish_player_dp_update_event_impl handles no NATS service., Test _publish_player_dp_update_event_impl with all optional parameters. (+35 more)

### Community 500 - "PickupTestWiring"
Cohesion: 0.12
Nodes (26): handle_pickup_command(), Move an item stack from room drops into the player's inventory., inventory_has_named_item(), PickupTestWiring, Shared helpers for inventory command unit tests., True if inv is a sequence of dict rows containing item_name == name., Single sword stack as returned by list_room_drops / take_room_drop., Standard app.state wiring for handle_pickup_command tests (typed mock surface… (+18 more)

### Community 501 - "test_party_commands.py"
Cohesion: 0.08
Nodes (50): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+42 more)

### Community 502 - "properties"
Cohesion: 0.14
Nodes (14): description, description, description, description, type, properties, field1, field2 (+6 more)

### Community 503 - "Pydantic Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.06
Nodes (30): ⚠️ Areas for Improvement, 🟡 Business Logic in Models - Stats.**init**, Code Quality Observations, Conclusion, Critical Issues, 🔴 CRITICAL: Security Vulnerability - `extra="allow"` in Stats Model, Executive Summary, 🟢 Field Validator Organization (+22 more)

### Community 504 - "test_passive_lucidity_flux_service.py"
Cohesion: 0.10
Nodes (36): PassiveLucidityFluxService, FluxServiceConfig, Optional configuration for PassiveLucidityFluxService. All fields have defaults., Passive lucidity flux service package., CachedRoom, PassiveFluxContext, Data models for passive lucidity flux., Cached room entry with timestamp for TTL management. (+28 more)

### Community 505 - "Prometheus Configuration"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 506 - "PeriodicOrphanAuditor"
Cohesion: 0.12
Nodes (30): create_lifespan_memory_service(), PeriodicOrphanAuditor, Create a centralized memory operations coordinator instance targeted for…, Periodic background auditor that investigates orphanage patterns and memory…, asyncio, Unit tests for periodic orphan auditing and lifespan memory coordination., No orphans and no threshold breach skips cleanup., Audit cycle errors are logged without propagating. (+22 more)

### Community 507 - "test_item.py"
Cohesion: 0.07
Nodes (36): ItemComponentState, ItemInstance, Base, Idempotently apply a runtime-only flag override., Per-instance persisted state for modular item components., Convenience helper for composing uniqueness checks in higher layers., Runtime representation of an item spawned from a prototype., Unit tests for item models. Tests the ItemPrototype, ItemInstance, and… (+28 more)

### Community 508 - "load_world_seed.py"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 509 - "validate.py"
Cohesion: 0.10
Nodes (30): BugBlock, check_bug_content(), _check_bugs(), check_loose_tags(), _check_required_structure(), _exit_code_for_errors(), find_bug_blocks(), find_first_content_section() (+22 more)

### Community 510 - "ReactNodeUpgradeAnalyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 511 - "UUID"
Cohesion: 0.06
Nodes (19): UUID, Publish an npc_took_damage event for non-combat damage., Publish an npc_died event when non-combat damage kills an NPC., Return combat_id if this NPC is in combat, else None., End combat if the given NPC is in combat (e.g. steal-life kill)., Return the active combat for combat_id, or None if not found., Return combat_id if a participant is in combat, else None., Return combat_id if an NPC UUID is in combat, else None. (+11 more)

### Community 512 - "UserManagerProtocol"
Cohesion: 0.06
Nodes (17): PlayerServiceProtocol, Any, Protocol, Protocol for player service., Resolve player name to player object., Get user management system statistics., Protocol for user manager., Mute a channel for a player. (+9 more)

### Community 513 - "NPCStartupService"
Cohesion: 0.05
Nodes (79): NPCStartupService, Get a default room for a given sub-zone. Args: sub_zone_id: Sub-zone identifier…, Service for automatic NPC spawning during server startup. This service…, Initialize the NPC startup service., mock_container(), Create mock container., _assign_container_get_instance(), _errors_len() (+71 more)

### Community 514 - "_NPCCombatIntegrationValidationDeps"
Cohesion: 0.09
Nodes (19): _coerce_xp_mapping_value(), _NPCCombatIntegrationValidationDeps, Protocol, UUID, Validate that player and NPC are in the same room., End any active combat that includes this player when room validation fails., Convert string IDs to UUIDs and set up XP mappings., Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,… (+11 more)

### Community 515 - "PatternNotFoundError"
Cohesion: 0.09
Nodes (27): MissingParameterError, NATSSubjectError, PatternNotFoundError, Exception, Base exception for NATS subject-related errors., Exception raised when a pattern name is not found in registry., Exception raised when required parameters are missing., Get a subscription pattern with wildcards for NATS subscriptions. This method… (+19 more)

### Community 516 - "test_shutdown_sequence.py"
Cohesion: 0.10
Nodes (46): _cancel_background_tasks(), _cleanup_connection_manager(), _despawn_all_npcs(), _disconnect_all_players(), _disconnect_nats_service(), execute_shutdown_sequence(), _persist_all_players(), Any (+38 more)

### Community 517 - "test_room_occupant_manager.py"
Cohesion: 0.09
Nodes (29): mock_connection_manager(), occupant_manager(), asyncio, fixture, Unit tests for room occupant manager. Tests the RoomOccupantManager class for…, Test get_room_occupants with ensure_player_included., Test get_room_occupants returns both players and NPCs., Test get_room_occupants handles get_players error. (+21 more)

### Community 518 - "docker Best Practices"
Cohesion: 0.17
Nodes (11): 10. Manage Secrets Securely with Docker Compose, 1. Optimize for Multi-Stage Builds, 2. Choose Minimal, Trusted Base Images, 3. Leverage `.dockerignore`, 4. Optimize Layer Caching, 5. Run as a Non-Root User, 6. Distinguish `ARG` and `ENV`, 7. Implement Health Checks (+3 more)

### Community 519 - "test_inventory_mutation_guard.py"
Cohesion: 0.07
Nodes (29): guard(), asyncio, fixture, Unit tests for inventory mutation guard - core functionality. Tests…, Test acquire_async without token allows mutation., Test acquire_async with unique token allows mutation., Test acquire_async with duplicate token suppresses mutation., Test acquire_async allows same token for different players. (+21 more)

### Community 520 - "RoomInfoPanel.tsx"
Cohesion: 0.13
Nodes (16): applyRoomDefaultFields(), DEV_FALLBACK_ROOM, fixOccupantCountMismatch(), formatDescription(), formatExitDirections(), formatLocationName(), KNOWN_LOCATION_PATTERNS, logRoomInfoRenderDebug() (+8 more)

### Community 521 - "test_combat_service_modules.py"
Cohesion: 0.05
Nodes (79): CombatDPSync, Any, Get persistence layer from application container. Args: player_id: Player ID…, Verify that player DP was successfully saved to database. Args: persistence:…, Log death threshold events based on DP changes. Args: current_dp: New current…, Update player DP and save to database. Args: persistence: Persistence layer…, Synchronously persist player DP to database. This is the actual persistence…, Handles DP synchronization for combat operations. (+71 more)

### Community 522 - "test_optimized_security_validator.py"
Cohesion: 0.09
Nodes (31): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test validating message with path traversal pattern., Test validating message with javascript: URL., Test validating message with event handler. (+23 more)

### Community 523 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, properties, field1, field2, field3, zone (+3 more)

### Community 524 - "Any"
Cohesion: 0.09
Nodes (18): Any, Task, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task…, Cancel specific task with logical timeout boundaries. Args: task: Task…, Metadata for tracked asyncio.Tasks. (+10 more)

### Community 525 - "scripts"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 526 - "RoomMapEditorRuntime.tsx"
Cohesion: 0.06
Nodes (36): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeBody(), ExitEdgeLabels() (+28 more)

### Community 527 - "container_query_helpers.py"
Cohesion: 0.09
Nodes (29): _build_container_data_from_row(), get_containers_by_entity_id(), get_containers_by_room_id(), get_decayed_containers(), Any, ContainerData, datetime, UUID (+21 more)

### Community 528 - "ensurePlayableConnection"
Cohesion: 0.17
Nodes (24): nudgeStandBothPlayers(), despawnArmitage(), DIALOGUE, ensureArmitagePresent(), listArmitageIds(), loginAdminPlayable(), ensurePlayableConnection(), executeCommandWithoutRecovery() (+16 more)

### Community 529 - "test_channel_commands.py"
Cohesion: 0.09
Nodes (39): _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting(), Any, Validate channel name. Returns error dict if invalid, None if valid., Handle the channel command for switching channels or setting default channel.…, Get persistence and player. Returns (persistence, player) or (None, None) if… (+31 more)

### Community 530 - "AnyIO vs Asyncio: High-Level Comparison and Decision Guide"
Cohesion: 0.07
Nodes (29): 1. **Structured Concurrency**, 2. **Backend Abstraction**, 3. **API Design Philosophy**, Adjusts spectacles and peers at the codebase, anyio Cons ❌, anyio Pros ✅, `anyio` (Third-Party Library), AnyIO vs Asyncio: High-Level Comparison and Decision Guide (+21 more)

### Community 531 - "Complexity Checking Alignment: Ruff C901 vs Pylint"
Cohesion: 0.06
Nodes (30): 1. Use Ruff for Cyclomatic Complexity ✅, 2. Suppress Pylint Complexity Metrics ✅, 3. Align Inline Suppressions, Complexity Checking Alignment: Ruff C901 vs Pylint, Conclusion, Configuration, Configuration, Current State Analysis (+22 more)

### Community 532 - "WebSocket Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (29): 10. **No Message Batching**, 11. **Missing Rate Limiting on WebSocket Messages**, 12. **Insufficient Authentication Validation**, 1. **Dependency Injection Pattern**, 1. **Event Loop Anti-Pattern in Connection Manager**, 2. **Missing Input Validation on Server Side**, 2. **Modern Async Patterns**, 3. **Error Boundaries** (+21 more)

### Community 533 - "LucidityFluxService"
Cohesion: 0.10
Nodes (19): LucidityFluxService, PlayerFluxCtx, AsyncSession, datetime, Player, Build room cache for all players., Process a single player's passive flux., Evaluate passive LCD flux for the current tick. (+11 more)

### Community 534 - "properties"
Cohesion: 0.11
Nodes (19): integer, minimum, type, minimum, type, null, maxLength, minLength (+11 more)

### Community 535 - "CORSConfig"
Cohesion: 0.08
Nodes (29): CORSConfig, Any, BaseSettings, field_validator, model_validator, Parse comma-separated string into cleaned list., Parse comma separated strings or lists into a cleaned list of strings., Parse allowed origins from various input formats. (+21 more)

### Community 536 - "test_chat_pose_helpers.py"
Cohesion: 0.16
Nodes (24): clear_player_pose(), get_player_pose(), get_room_poses(), normalize_player_id(), Any, UUID, Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose…, Get all poses for players in a room. Args: room_id: ID of the room… (+16 more)

### Community 537 - "test_quest_definition_repository.py"
Cohesion: 0.11
Nodes (29): _make_session_context(), mock_quest_definition(), asyncio, fixture, quest_definition_repository(), Unit tests for QuestDefinitionRepository. Tests get_by_id, get_by_name, and…, Test get_by_id raises DatabaseError on DB failure., Test get_by_name returns definition when found by common name. (+21 more)

### Community 538 - "test_chat_moderation.py"
Cohesion: 0.11
Nodes (20): moderation(), player_service(), asyncio, fixture, Unit tests for chat moderation operations., test_add_admin_returns_true(), test_get_mute_status_handles_internal_error(), test_get_mute_status_includes_player_name() (+12 more)

### Community 539 - "NPCCombatIntegrationReadApi"
Cohesion: 0.09
Nodes (20): lifecycle_lookup_id(), NPCCombatIntegrationReadApi, NPCCombatRewardsLike, original_string_id_for_npc(), PersistenceWithNpcLifecycleManager, PlayerXpLike, Protocol, UUID (+12 more)

### Community 540 - "equipment_helpers.py"
Cohesion: 0.09
Nodes (44): _equip_stack_from_inventory_index(), _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), handle_wearable_container_on_unequip(), normalize_equipped_items(), normalize_inventory_slots(), InventoryStack (+36 more)

### Community 541 - "MythosMUD Database Placement"
Cohesion: 0.07
Nodes (29): Database Placement Skill, Allowed Paths Only, Data Types, Forbidden, MythosMUD Database Placement, PostgreSQL Access (Procedures and Functions), Reference, When Adding or Moving Persistence (+21 more)

### Community 542 - "debugLogger"
Cohesion: 0.13
Nodes (5): debugLogger, LogConfig, LogEntry, LogLevel, mockConsole

### Community 543 - "test_logger"
Cohesion: 0.25
Nodes (8): deterministic_random_seed(), ensure_test_environment_variables(), BoundLogger, fixture, Set deterministic random seed for reproducible tests., Provide a logger for tests., Ensure critical environment variables are set before each test. Some tests may…, test_logger()

### Community 544 - "AnyIO Code Review - Anti-Patterns and Issues"
Cohesion: 0.07
Nodes (28): 1. Entry Point Anti-Pattern: `asyncio.run()` Usage, 2.1 `asyncio.sleep()` Usage, 2.2 `asyncio.Lock()` Usage, 2.3 `asyncio.Event()` Usage, 2.4 `asyncio.Queue()` Usage, 2.5 `asyncio.wait_for()` Usage, 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage, 3.1 `asyncio.create_task()` Usage (+20 more)

### Community 545 - "🎯 Async Remediation - Final Report"
Cohesion: 0.07
Nodes (28): All async anti-patterns have been exorcised from the codebase, All Targets Met, API/Commands (2 files), 🎯 Async Remediation - Final Report, Checklist, ✅ COMPLETE - ALL 48 INSTANCES MIGRATED, Core Infrastructure (2 files), 📚 Documentation Delivered (+20 more)

### Community 546 - "NATS Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (28): 10. **Inconsistent Error Handling**, 11. **Missing Input Validation**, 1. **Blocking Operations in Message Handlers** (Anti-pattern violation), 1. **Excellent Error Boundary Implementation**, 2. **Good Connection State Management**, 2. **Missing Message Acknowledgment** (Anti-pattern violation), 3. **Connection Pool Not Used by Default** (Inefficiency), 3. **Proper Async/Await Usage** (+20 more)

### Community 547 - "Persistence Layer Extraction - COMPLETE ✅"
Cohesion: 0.07
Nodes (28): Architecture Changes, Benefits, Cleanup, Conclusion, File Size Reduction, Files Modified, Group 1: Player Operations (~800 lines → ~80 lines), Group 2: Health & XP Operations (~400 lines → ~40 lines) (+20 more)

### Community 548 - "🔴 CRITICAL ISSUES"
Cohesion: 0.07
Nodes (28): 10. Use of `BETWEEN` with Integer Ranges, 11. Missing Indexes on Foreign Keys, 12. Inconsistent Constraint Naming, 13. Mixed Case in Table/Column Names, 14. Missing `UNIQUE` Constraints Where Appropriate, 15. Inconsistent Use of `NOT NULL` Constraints, 16. Missing Documentation for Complex Constraints, 1. Use of `serial`/`SERIAL` Instead of `bigint generated always as identity` (+20 more)

### Community 549 - "asyncio"
Cohesion: 0.14
Nodes (14): asyncio, Test get_player_room_from_persistence() returns player room., Test is_player_in_room() returns True when player is in room., Test preload_receiver_mute_data() excludes sender from targets., test_check_player_mute_status_patched_and_emote(), test_filter_target_players_room_and_mute(), test_get_player_room_from_persistence(), test_get_player_room_from_persistence_mock_player() (+6 more)

### Community 550 - "log_and_raise"
Cohesion: 0.01
Nodes (230): get_10_active_invites(), main(), Get 10 active invite codes from the database., F, Initialize the async persistence layer. This facade delegates to focused async…, get_session_maker(), Get the async session maker from DatabaseManager. Returns: async_sessionmaker:…, get_skill_repository() (+222 more)

### Community 551 - "Protocol"
Cohesion: 0.13
Nodes (10): Protocol, UUID, _TickCombatService, _TickConnectionManager, _TickDeathService, _TickEventBus, _TickMagicService, _TickMpRegen (+2 more)

### Community 552 - "get_shared_services"
Cohesion: 0.08
Nodes (38): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+30 more)

### Community 553 - "OccupantFormatter"
Cohesion: 0.12
Nodes (20): OccupantFormatter, Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Formats and separates occupants by type., Initialize occupant formatter., Check if a string looks like a UUID. Args: value: The string to check Returns:… (+12 more)

### Community 554 - "extract_player_name"
Cohesion: 0.13
Nodes (25): extract_player_name(), _get_name_from_user(), get_player_position(), _is_uuid_string(), _is_valid_name(), Any, Player, UUID (+17 more)

### Community 555 - "RateLimiter"
Cohesion: 0.10
Nodes (17): Any, RateLimiter, Remove timestamps older than the window size. Args: player_id: Player ID…, Check if a player is within rate limits for a channel. Args: player_id: Player…, Record a message for rate limiting. Args: player_id: Player ID channel: Channel…, Sliding window rate limiter for chat channels. Implements per-user, per-channel…, Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…, Reset rate limiting for a player. Args: player_id: Player ID channel: Specific… (+9 more)

### Community 556 - "Bug Investigator Subagent"
Cohesion: 0.07
Nodes (27): Authentication/Login Issues, Best Practices, Bug Investigator Subagent, Capabilities, Chat/Communication Issues, Critical Requirements, Evidence Collection, Evidence Standards (+19 more)

### Community 557 - "MonitoringPanel.tsx"
Cohesion: 0.12
Nodes (23): ConnectionHealthStats(), DualConnectionStats(), formatNumber(), formatPercentage(), formatTime(), loadMonitoringSnapshot(), MonitoringData, MonitoringPanel() (+15 more)

### Community 558 - "asyncio"
Cohesion: 0.11
Nodes (21): _make_effect(), asyncio, get_active_effects_for_player returns only effects with remaining_ticks > 0…, has_effect returns True when player has active effect of type., has_effect returns False when no active effect of type., get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick)., get_effect_remaining_ticks returns None when no matching effect., expire_effects_for_tick returns (player_id, effect_type) and deletes rows via… (+13 more)

### Community 559 - ".create_combat_instance"
Cohesion: 0.09
Nodes (17): _build_combat_instance(), Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…, Create and initialize a combat instance., fixture, Test create_combat_instance orders turns when target has higher dexterity., Test create_combat_instance handles equal dexterity., Test create_combat_instance with auto-progression disabled., Test create_combat_instance with different turn interval. (+9 more)

### Community 560 - "3. REFACTOR Findings (935 findings)"
Cohesion: 0.07
Nodes (27): 1.1 Missing Module Docstrings (C0114), 1.2 Invalid Name (C0103), 1.3 Too Many Lines in Module (C0302), 1.4 Use Implicit Booleaness (C1805, C1804), 1.5 Singleton Comparison (C0121), 1.6 Missing Function Docstring (C0116), 1. CONVENTION Findings (260 findings), 2.1 No Name in Module (E0611) (+19 more)

### Community 561 - "ErrorMonitor"
Cohesion: 0.13
Nodes (17): ErrorMonitor, main(), Any, datetime, Path, Detect error trends over time. Returns trend analysis results., Check for alert conditions. Returns list of active alerts., Monitor errors continuously for a specified duration. Args: log_dir: Directory… (+9 more)

### Community 562 - "verify_linting_parity.py"
Cohesion: 0.15
Nodes (27): check_alignment(), _check_pylint_suppressions(), _check_ruff_suppressions(), find_suppressions(), _has_pylint_equivalent(), _has_ruff_equivalent(), main(), parse_pylint_suppression() (+19 more)

### Community 563 - "MythosTickScheduler"
Cohesion: 0.11
Nodes (27): mock_chronicle(), mock_event_bus(), mock_task_registry(), asyncio, fixture, Unit tests for MythosTickScheduler., scheduler(), test_emit_pending_ticks_initializes_last_hour() (+19 more)

### Community 564 - "test_connection_manager_api.py"
Cohesion: 0.26
Nodes (11): mock_manager(), asyncio, fixture, Unit tests for server.realtime.connection_manager_api., test_broadcast_game_event(), test_require_manager_raises_when_missing(), test_send_game_event_with_uuid(), test_send_player_status_update() (+3 more)

### Community 565 - "test_npc_spawn_rules_api.py"
Cohesion: 0.13
Nodes (26): NPCSpawnRuleResponse, Model for NPC spawn rule responses., Create response from ORM object., create_npc_spawn_rule(), delete_npc_spawn_rule(), get_npc_spawn_rules(), AsyncSession, delete (+18 more)

### Community 566 - "InventorySchemaValidationError"
Cohesion: 0.13
Nodes (25): Shared schemas: base models, target resolution, inventory validation., _build_validator(), InventorySchemaValidationError, Any, Exception, Inventory JSON schema validation utilities. As recorded in the restricted…, Internal helper to construct a Draft7 validator instance., Validate a complete inventory payload against the canonical schema. Raises:… (+17 more)

### Community 567 - "test_security_utils.py"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory. Args: filename: The filename…, Unit tests for security utilities. Tests path validation and file security…, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 568 - "test_shutdown_process_termination.py"
Cohesion: 0.08
Nodes (26): _find_uvicorn_processes(), Any, Schedule a best-effort graceful process termination after a short delay. This…, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available., schedule_process_termination() (+18 more)

### Community 569 - "handle_command"
Cohesion: 0.08
Nodes (23): CommandRequest, handle_command(), BaseModel, post, Request, Handle incoming HTTP command requests., Request model for command processing., asyncio (+15 more)

### Community 570 - ".perform_recovery_action"
Cohesion: 0.32
Nodes (5): Any, UUID, Perform a recovery action and enforce cooldowns., Fetch the cooldown record for a recovery action., Apply LCD loss for a Mythos encounter.

### Community 571 - "NPCOccupantProcessor"
Cohesion: 0.07
Nodes (32): NPCOccupantProcessor, Any, NPC occupant processing utilities. This module handles querying and processing…, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Processes NPC occupants for rooms., Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:… (+24 more)

### Community 572 - "SkillUseLog"
Cohesion: 0.21
Nodes (10): Base, One recorded successful use of a skill by a character at a given level.…, SkillUseLog, Unit tests for SkillUseLog ORM model., SkillUseLog can be instantiated with required fields., SkillUseLog maps to the expected table., SkillUseLog __repr__ includes key identifiers., test_skill_use_log_creation() (+2 more)

### Community 573 - "test_quest_service_collect.py"
Cohesion: 0.13
Nodes (27): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in… (+19 more)

### Community 574 - "NPCActionMessage"
Cohesion: 0.09
Nodes (18): Check if idle movement should be scheduled based on configuration and timing.…, Create a WANDER action message. Args: current_time: Current timestamp Returns:…, Queue a WANDER action via the thread manager. Args: wander_action: The wander…, Schedule a WANDER action for idle movement if interval has elapsed. This method…, Handle wandering action., Perform wandering behavior using idle movement system., NPCActionMessage, NPCActionType (+10 more)

### Community 575 - ".create_instance"
Cohesion: 0.12
Nodes (12): Instance, Room, UUID, Return template rooms matching instance_template_id., Clone template rooms into instance-scoped rooms with remapped exits., Extract stable_id from room - use room.id if it looks like a full path., Remap exit targets: same-instance rooms use instance IDs, outside exits use…, Extract stable_id from a room ID (may be full path or short form). (+4 more)

### Community 576 - "AliasGraph"
Cohesion: 0.09
Nodes (22): Unit tests for alias_graph utilities. Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+14 more)

### Community 577 - ".change_position"
Cohesion: 0.09
Nodes (16): PositionChangeResponse, Player, TypedDict, Validate and normalize position., Get player for position change. Returns: Tuple of (player, response_dict) if…, Copy player identity fields into the position-change response., Load player stats, returning {} when loading fails., Get current position from player stats. (+8 more)

### Community 578 - "Communities (19 total, 4 thin omitted)"
Cohesion: 0.07
Nodes (26): Ambiguous Edges - Review These, Communities (19 total, 4 thin omitted), Community 0 - "Yog-Sothoth Keeper Decks", Community 10 - "Tsathoggua Formless Spawn", Community 11 - "Ygolonac and Xiclotl", Community 12 - "Nyogtha Spawn", Community 13 - "Hastur Spawn", Community 14 - "Fthagghua Fire Vampires" (+18 more)

### Community 579 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 580 - "Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.07
Nodes (26): 1. Deprecated `asyncio.get_event_loop()` Usage, 1. Proper Connection Pool Management, 2. Good Error Handling Patterns, 2. SQL Injection Risk in Field Name Construction, 3. Async/Await Usage, 3. Connection Pool Cleanup Verification, 4. Blocking Operations in Async Context, 4. Security Considerations (+18 more)

### Community 581 - "test_error_handling_middleware.py"
Cohesion: 0.06
Nodes (53): add_error_handling_middleware(), ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Exception, FastAPI, Protocol, Receive (+45 more)

### Community 582 - "LogAnalyzer"
Cohesion: 0.12
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time. Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 583 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (49): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id. Args: room_drops: List of…, Unit tests for look item helper functions. Tests the helper functions in…, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items. (+41 more)

### Community 584 - "test_npc_combat_integration_service_npc_aggro.py"
Cohesion: 0.08
Nodes (33): mock_async_persistence(), mock_combat_service(), mock_connection_manager(), mock_messaging_integration(), asyncio, Unit tests for NPC combat integration service - NPC-initiated aggro combat…, Test handle_npc_attack_on_player returns False when NPC instance cannot be…, Test handle_npc_attack_on_player returns False when NPC is dead. (+25 more)

### Community 585 - "test_lru_cache.py"
Cohesion: 0.07
Nodes (27): cache_with_ttl(), cache_without_ttl(), asyncio, fixture, Unit tests for LRU cache expiration and eviction. Tests the LRUCache class,…, Test that expired entry count is tracked in cache stats., Test that expiration rate is calculated in stats., Test that cache size stays within bounds after expiration cleanup. (+19 more)

### Community 586 - "attach_compatibility_properties"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 587 - "room_hierarchy_schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, anyOf, description, description, exits, id, name, required (+3 more)

### Community 588 - "test_combat_death_handler.py"
Cohesion: 0.13
Nodes (22): combat(), combat_service(), handler(), npc_target(), player_target(), asyncio, fixture, patch (+14 more)

### Community 589 - "Codacy Rules"
Cohesion: 0.18
Nodes (10): After every response, Codacy Rules, CRITICAL: After ANY successful file edit, CRITICAL: Dependencies and Security Checks, General, Trying to call a tool that needs a `rootPath` parameter, Using any tool that accepts `provider`, `organization`, or `repository`, When `codacy_cli_analyze` fails because the Codacy CLI is not installed (+2 more)

### Community 590 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

### Community 591 - "GameTerminal.tsx"
Cohesion: 0.04
Nodes (57): buildHealthStatus(), ChatMessage, formatPosture(), GameTerminal(), Player, Room, formatDelta(), HealthMeter (+49 more)

### Community 592 - "Migration Strategy"
Cohesion: 0.08
Nodes (25): Access Patterns, App.State to Dependency Injection Migration Plan, Current State Analysis, Dependencies, Dependency Injection Pattern, Estimated Effort, Implementation Guidelines, Migration Strategy (+17 more)

### Community 593 - "Async Facades Implementation - COMPLETE ✅"
Cohesion: 0.08
Nodes (25): (A) and (B) Relationship: **Complementary**, (A) AsyncPersistenceLayer Integration ✅, Async Facades Implementation - COMPLETE ✅, Async Tests, (B) Sync Shim - NOT NEEDED ⏭️, Benefits Achieved, Both facades are now operational, Conclusion (+17 more)

### Community 594 - "Migration 019: Complete Implementation Summary"
Cohesion: 0.08
Nodes (25): 1. Database Schema Updates ✅, 2. Python Model Updates ✅, 3. Migration Script Created ✅, 4. Testing Infrastructure ✅, Before Production, Conclusion, Created Files (5), Documentation Files (4) (+17 more)

### Community 595 - "CombatEventHandler"
Cohesion: 0.12
Nodes (23): CombatEventHandler, Any, UUID, Publish attack events and calculate XP reward. Args: current_participant:…, Calculate XP reward for defeating an NPC. Args: npc_id: ID of the defeated NPC…, Award XP to player for defeating an NPC. Args: current_participant: Attacking…, Publish combat ended event., Handles combat event publishing. (+15 more)

### Community 596 - "test_load_world_seed.py"
Cohesion: 0.12
Nodes (25): regression, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, CaptureFixture, fixture, MonkeyPatch, Protocol (+17 more)

### Community 597 - "._build_player_attacked_event"
Cohesion: 0.06
Nodes (22): CombatEventPublisherProtocol, NpcCombatServiceProtocol, Protocol, Publish a PlayerAttackedEvent to the combat event stream., Typed surface for npc_combat_service.handle_npc_attack_on_player., Handle an NPC attack against a player via the main combat service., Combat event publisher (avoids importing CombatEventPublisher)., UUID (+14 more)

### Community 598 - "Vitest Best Practices"
Cohesion: 0.18
Nodes (10): 1. Code Organization & Naming, 2. Test Structure & Isolation, 3. Asynchronous Testing with `vi.waitFor`, 4. Mocking Strategies, 5. DOM Environment & Component Testing, 6. Performance & Concurrent Tests, 7. Code Coverage, Function Mocking (+2 more)

### Community 599 - "zustand Best Practices"
Cohesion: 0.18
Nodes (10): 1. Typed Store Shape (TypeScript First), 2. Slice-Based Organization, 3. Naming Conventions, 4. Functional Updates to Prevent Stale Closures, 5. Selectors and Shallow Comparison for Performance, 6. Essential Middleware Usage, 7. Initializing Stores Outside Components, 8. Asynchronous Actions (+2 more)

### Community 600 - "test_time_bundle.py"
Cohesion: 0.08
Nodes (26): isolated_chronicle(), asyncio, fixture, Unit tests for TimeBundle container wiring., Advance and freeze update persisted state., Clock formatting includes Mythos suffix., get_mythos_chronicle returns the same instance., advance_mythos rejects negative hours. (+18 more)

### Community 601 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_player_data_for_respawn() returns None when player not found., Test get_player_data_for_respawn() handles errors., Test send_respawn_event_with_retry() is a no-op when connection manager is…, Test get_current_lucidity() returns default when record not found., Test get_player_data_for_delirium_respawn() successfully retrieves player data., Test get_player_data_for_delirium_respawn() returns None when player not found., test_get_current_lucidity_not_found() (+5 more)

### Community 602 - "test_behavior_engine.py"
Cohesion: 0.07
Nodes (29): Unit tests for behavior engine. Tests the BehaviorEngine class., Test _evaluate_equality() returns True for matching condition., Test _evaluate_equality() handles boolean true., Test _evaluate_numeric_comparison() handles > operator., Test _evaluate_numeric_comparison() raises ValueError for non-numeric values., Test evaluate_condition() handles >= operator., Test get_applicable_rules() returns matching rules., Test execute_applicable_rules() handles exceptions. (+21 more)

### Community 603 - "channel_broadcasting_strategies.py"
Cohesion: 0.23
Nodes (11): ChannelBroadcastingStrategy, GlobalChannelStrategy, PartyChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for party channel broadcasting. Delivers only to current party members., Strategy for whisper channel broadcasting., Abstract base class for channel broadcasting strategies. (+3 more)

### Community 604 - "test_quality_fragmentation_guard.py"
Cohesion: 0.12
Nodes (35): _build_python_call_usage_map(), _call_target_name(), Call, ChangedFile, Build a repo-wide call usage map from Python AST call sites., scan_changed_files(), _ChangedFile, _load_guard_module() (+27 more)

### Community 605 - "dependencies"
Cohesion: 0.08
Nodes (25): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-resizable, react-rnd (+17 more)

### Community 606 - "normalize_environment"
Cohesion: 0.12
Nodes (22): Path, Load holidays from PostgreSQL database., Path, Unit tests for project_paths utilities. Tests path resolution functions., Test get_project_root() returns project root path., Test normalize_environment() normalizes environment names., Test get_environment_data_dir() returns data directory., Test get_calendar_paths_for_environment() returns calendar paths. (+14 more)

### Community 607 - "messageHandlers.ts"
Cohesion: 0.16
Nodes (14): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+6 more)

### Community 608 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 609 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 610 - "Migration 019 Verification Report"
Cohesion: 0.08
Nodes (24): 1. Code Quality Checks, 2. Model Updates Verified, 3. Type Compatibility, 4. Database Schema Alignment, Before Production Deployment, Conclusion, Documentation (3 files), Files Modified Summary (+16 more)

### Community 611 - "Phase 4: Recommendations"
Cohesion: 0.08
Nodes (25): 1. Prune Infrastructure Tests (Save ~3 minutes, Remove ~350 tests), 2. Consolidate Coverage Tests (Save ~1 minute, Reduce ~60 tests), 3. Parametrize Repetitive Tests (Save ~1 minute, Reduce ~300 tests), 4.1 Pruning Candidates (750 tests, ~5 minutes savings), 4.2 Consolidation Opportunities, 4.3 Coverage Gap Identification, 4.4 Optimization Recommendations, 4. Migrate Model Tests to Property-Based Testing (+17 more)

### Community 612 - "test_retry.py"
Cohesion: 0.09
Nodes (25): asyncio, Unit tests for retry utilities. Tests the retry decorator and retry logic., Test retry_with_backoff() with async function succeeds on first attempt., Test is_transient_error() identifies transient errors., Test retry_with_backoff() with async function retries on failure then succeeds., Test is_transient_error() returns False for non-transient errors., DatabaseError wrapping asyncpg closed-connection must still retry (e2e…, __cause__ ConnectionDoesNotExistError makes the outer wrapper transient. (+17 more)

### Community 613 - "send_system_message"
Cohesion: 0.18
Nodes (15): Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler system message functions. Tests the system…, Create a mock WebSocket., Test send_system_message() successfully sends message. (+7 more)

### Community 614 - "LucidityRepository"
Cohesion: 0.11
Nodes (17): LucidityRepository, AsyncSession, datetime, UUID, Set or update cooldown for a player and action., Delete all cooldowns for a player matching an action code pattern., Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE., Data-access helpers for lucidity persistence. (+9 more)

### Community 615 - "fix_fstring_logging.py"
Cohesion: 0.12
Nodes (24): _build_structured_params(), _clean_message(), _create_replacement_for_fstring(), create_structured_log_message(), extract_variables_from_fstring(), fix_fstring_logging_in_file(), _handle_no_variables_case(), main() (+16 more)

### Community 616 - "TestRunner"
Cohesion: 0.12
Nodes (13): main(), Path, Verify test database configuration. Note: For PostgreSQL databases, schema is…, Build the pytest command with proper configuration. Args: test_paths: List of…, Run the test suite with proper configuration. Args: test_paths: List of test…, Run integration tests only., Run all tests (unit, integration, but not E2E by default)., Generate coverage report only. (+5 more)

### Community 617 - "SkillAssignmentScreen.tsx"
Cohesion: 0.18
Nodes (20): OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, loadSkillsCatalog(), MIN_TOUCH_TARGET_STYLE, OCCUPATION_VALUES, renderErrorState(), renderLoadingState() (+12 more)

### Community 618 - "establish_websocket_connection"
Cohesion: 0.10
Nodes (33): _cleanup_dead_connections(), _cleanup_failed_connection(), establish_websocket_connection(), _EstablishmentConnectionManager, _find_dead_connections(), Player, Protocol, UUID (+25 more)

### Community 619 - "seed_e2e_users.py"
Cohesion: 0.29
Nodes (9): E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio., One row in users plus optional default character for login E2E. (+1 more)

### Community 620 - "client/package.json"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 621 - "Playwright Best Practices"
Cohesion: 0.20
Nodes (9): 1. Always Use `@playwright/test`, 2. Prioritize Robust Locators, 3. Embrace Web-First Assertions, 4. Implement the Page Object Model (POM), 5. Optimize Performance with Auth State & Route Blocking, 6. Mock APIs for Deterministic Tests, 7. Leverage CI/CD Features for Debugging, 8. Maintain Code Quality with Linters & Formatters (+1 more)

### Community 622 - "test_inventory_mutation_guard_internal.py"
Cohesion: 0.09
Nodes (25): guard(), asyncio, fixture, Unit tests for inventory mutation guard - internal helper methods. Tests…, Test _cleanup_async_state removes empty state., Test _prune_tokens_async removes expired tokens., Test _prune_tokens_async with token_ttl=0 doesn't prune., Test _enforce_limit_async removes oldest tokens when limit exceeded. (+17 more)

### Community 623 - "StatisticsAggregator"
Cohesion: 0.12
Nodes (12): Analyze connection health distribution. Args: connection_metadata: Connection…, Analyze connection types. Args: connection_metadata: Connection metadata…, Analyze connection ages. Args: connection_metadata: Connection metadata now:…, Analyze session health. Args: connection_metadata: Connection metadata Returns:…, Calculate session health percentages. Args: session_health: Session health…, Build health trends statistics. Args: connection_ages: List of connection ages…, Build connection health statistics response. Args: total_connections: Total…, Aggregates statistics from connection management components. This class… (+4 more)

### Community 624 - "designTokens.ts"
Cohesion: 0.15
Nodes (19): animations, borderRadius, breakpoints, buildClasses, ButtonVariant, colors, ColorVariant, ComponentSize (+11 more)

### Community 625 - "test_event_bus.py"
Cohesion: 0.07
Nodes (27): Unit tests for event bus. Tests the EventBus class., Test EventBus.unsubscribe() with multiple handlers., Test EventBus.get_all_subscriber_counts() with no subscribers., Test EventBus.get_all_subscriber_counts() with multiple event types., Test subscribe() raises error for non-callable handler., Test unsubscribe() raises error for invalid event type., Test publish() raises error for invalid event., Test EventBus.subscribe() with service_id for tracking. (+19 more)

### Community 626 - "Recommended Test Additions"
Cohesion: 0.20
Nodes (10): 1. MessageBroker Integration Tests (15 tests, ~1 hour), 2. ApplicationContainer Lifecycle Tests (10 tests, ~1 hour), 3. Database Migration Tests (10 tests, ~1.5 hours), 4. WebSocket Edge Case Tests (15 tests, ~2 hours), 5. Error Recovery Tests (20 tests, ~3 hours), Immediate Priority (Add First), Recommended Test Additions, Secondary Priority (Add Second) (+2 more)

### Community 627 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., Test _build_room_objects includes exits in room data., test_build_room_objects_with_exits(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

### Community 628 - "AggressiveMobNPC"
Cohesion: 0.12
Nodes (15): AggressiveMobNPC, Flee from current situation., Aggressive mob NPC type with hunting and territorial behaviors., Handle fleeing action., Get aggressive mob-specific behavior rules., _enrich_behavior_context sets False when current_room is None., _get_attack_damage coerces behavior_config attack_damage robustly., Non-digit attack_damage string in behavior_config falls back to 1. (+7 more)

### Community 629 - "get_cached_player"
Cohesion: 0.13
Nodes (23): Unit tests for player_cache utilities. Tests the player caching functions for…, Test get_cached_player() returns None when no cache exists., Test cache_player() and get_cached_player() operations., Test get_cached_player() returns None for nonexistent key., Test cache_player() can cache multiple players., Test cache_player() overwrites existing entries., Test get_cached_player() handles missing state., Test cache_player() handles missing state gracefully. (+15 more)

### Community 630 - "cached"
Cohesion: 0.33
Nodes (5): cached(), Decorator to cache function results. Args: cache_name: Name of the cache to use…, Keep players cache truthy; empty LRUCache is bool-false via __len__., _seed_players_cache(), TestCachedDecorator

### Community 631 - "ValidationRule"
Cohesion: 0.09
Nodes (15): ABC, Base validation rule class. This module defines the abstract base class for all…, Create a validation error for this rule. Args: room_id: Room ID where error…, Represents a validation error with metadata. As documented in the restricted…, Create a validation warning for this rule. Args: room_id: Room ID where warning…, Get information about this rule. Returns: Dictionary with rule information, Initialize a validation error. Args: rule_name: Name of the rule that generated…, Convert error to dictionary format. (+7 more)

### Community 632 - "SQLAlchemyAsyncLinter"
Cohesion: 0.11
Nodes (18): Await, lint_directory(), lint_file(), main(), Call, Import, ImportFrom, Path (+10 more)

### Community 633 - "Test Suite Analyzer Subagent"
Cohesion: 0.08
Nodes (23): Best Practices, Capabilities, Coverage Analysis, Coverage Gap Analysis, Coverage Requirements, Critical Files Requiring High Coverage, Critical Path Coverage, Example Scenarios (+15 more)

### Community 634 - "Onboard Skill"
Cohesion: 0.08
Nodes (24): Onboard Skill, Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption (+16 more)

### Community 635 - "utils/config.ts"
Cohesion: 0.06
Nodes (42): baseUrl(), buildHeaders(), deleteDialogueDefinition(), DialogueDefinitionDto, DialogueNodeDto, DialogueOptionDto, DialogueTreeDto, listDialogueDefinitions() (+34 more)

### Community 636 - "test_database_config_helpers_asyncpg_settings.py"
Cohesion: 0.16
Nodes (15): clear_postgres_search_path(), fixture, MonkeyPatch, Unit tests for get_asyncpg_server_settings_for_database_url., Ensure POSTGRES_SEARCH_PATH does not leak between cases., Known env DBs must set search_path to the database name when env override is…, When POSTGRES_SEARCH_PATH matches the DB name, keep that search_path., Non-mythos_* URLs still honor POSTGRES_SEARCH_PATH. (+7 more)

### Community 637 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, minLength, type, type, minLength, type, properties (+10 more)

### Community 638 - "ContainerRepository and ItemRepository: Review and Full Async Migration Plan"
Cohesion: 0.08
Nodes (23): 1.1 Current Architecture, 1.2 Impact of Current Wrappers, 1.3 Recommendation, 1. Review Summary, 2.1 Functions to Migrate, 2.2 Callers, 2. Scope of Migration, 3. Migration Options (+15 more)

### Community 639 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 640 - "Documentation Updates - ConnectionManager Refactoring"
Cohesion: 0.08
Nodes (23): 1. **Accurate Reference Material**, ✅ 1. `REAL_TIME_ARCHITECTURE.md`, ✅ 2. `CONNECTION_MANAGER_ARCHITECTURE.md` (NEW), 2. **Reduced Confusion**, 3. **Better Onboarding**, ✅ 3. `WEBSOCKET_CODE_REVIEW.md`, ✅ 4. `DEVELOPMENT_AI.md`, 4. **Historical Record** (+15 more)

### Community 641 - "Domain Model Anemic Anti-Pattern Audit"
Cohesion: 0.08
Nodes (23): 1. Already Addressed (Prior Work), 2.1 Player Death Service – DP Decay, 2.2 Combat Turn Processor – “Can Act” Checks, 2.3 Combat HP Sync – Death Threshold Logic, 2.4 Combat Persistence Handler – Same Patterns, 2.5 Player Respawn Service – Stats Restoration, 2. High Priority – Domain Logic in Services, 3.1 Wearable Container Service – Capacity Checks (+15 more)

### Community 642 - "Test Coverage Summary: Disconnect Grace Period & Rest Command"
Cohesion: 0.07
Nodes (27): Coverage Targets, Coverage Verification, Critical Files (90% Target), E2E Scenarios, E2E Test Scenarios, E2E Test Scenarios, Expected Coverage Results, Grace Period System Tests (+19 more)

### Community 643 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 644 - "migrate_rooms.py"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 645 - "handle_emote_command"
Cohesion: 0.14
Nodes (22): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+14 more)

### Community 646 - "MessageBroadcaster"
Cohesion: 0.09
Nodes (24): SendPersonalMessage, Messaging components for connection management. This package provides modular…, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Message broadcasting for connection management. This module provides room and…, Convert string player IDs to UUIDs for message sending. Args: target_list: List… (+16 more)

### Community 647 - "EnvironmentalContainerLoader"
Cohesion: 0.12
Nodes (21): EnvironmentalContainerLoader, Any, ContainerComponent, ContainerLockState, UUID, migrate_room_container_to_postgresql., Load all environmental containers for a room from PostgreSQL. Args: room_id:…, Service for loading environmental containers from JSON and PostgreSQL. Handles… (+13 more)

### Community 648 - "InviteManager"
Cohesion: 0.17
Nodes (22): get_invite_manager(), InviteManager, AsyncSession, Remove expired invites and return count of removed invites., Get invite manager dependency., Manages invite creation, validation, and tracking. Handles the invite-only…, mock_session(), asyncio (+14 more)

### Community 649 - "PlayerOccupantProcessor"
Cohesion: 0.12
Nodes (18): PlayerOccupantProcessor, Any, UUID, Process players and convert to occupant information. Args: room_id: The room ID…, Processes player occupants for rooms., Initialize player occupant processor. Args: connection_manager:…, Ensure a player is included in the player ID strings list if specified. Args:…, Convert player ID strings to UUIDs for batch loading. Args: player_id_strings:… (+10 more)

### Community 650 - "PostgresRow"
Cohesion: 0.08
Nodes (17): PostgresRow, Any, Row-like object for PostgreSQL query results., Return the keys of the row dictionary. Returns: dict_keys: The keys of the row…, Execute a query and return a cursor. Args: query: SQL query with PostgreSQL %s…, Get a cursor from the underlying connection. This method provides direct access…, Test PostgresRow class., Test PostgresRow initialization. (+9 more)

### Community 651 - ".rescue"
Cohesion: 0.16
Nodes (15): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+7 more)

### Community 652 - "ItemPrototypeModel"
Cohesion: 0.11
Nodes (22): Constants supporting item prototype validation. These enumerations anchor the…, ItemPrototypeModel, BaseModel, field_validator, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validated representation of an item prototype definition. This model keeps the…, Validate that item_type is in the allowed list. Args: value: The item type to… (+14 more)

### Community 653 - "ChatPanel"
Cohesion: 0.16
Nodes (12): ChatPanel(), Channel, ChannelSelectorProps, TerminalButtonProps, TerminalInputProps, Channel, ChannelSelectorProps, TerminalButtonProps (+4 more)

### Community 654 - "_NPCCombatIntegrationDeps"
Cohesion: 0.13
Nodes (15): NPCCombatIntegrationCombatMixin, _NPCCombatIntegrationDeps, Protocol, UUID, Structured logging / observability trail when NPC-initiated combat begins., Process combat attack, starting new combat or continuing existing one., Start a new combat and process initial attack., Broadcast room occupants update to killer's room after NPC death. Swallows… (+7 more)

### Community 655 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 656 - "test_shopkeeper_npc.py"
Cohesion: 0.06
Nodes (35): Buy item from player., Calculate final price with markup., Handle greeting customer action., Handle restocking inventory action., Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., Shopkeeper NPC type with buy/sell functionality., Initialize shopkeeper NPC., Setup shopkeeper-specific behavior rules. (+27 more)

### Community 657 - "EventPublisher"
Cohesion: 0.18
Nodes (10): EventPublisher, JsonMap, Publish a player_entered event to NATS. Args: player_id: ID of the player who…, Publish a player_left event to NATS. Args: player_id: ID of the player who left…, Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…, Create a standardized event message structure. Args: event_type: Type of event…, Get the next sequence number for event ordering. Returns: Next sequence number, Reset the sequence number to 0. (+2 more)

### Community 658 - "CombatDeathHandler"
Cohesion: 0.08
Nodes (20): CombatDeathHandler, _CombatServiceDeps, _NPCCombatIntegrationLike, Protocol, UUID, Create corpse container when player dies., Best-effort connection diagnostics before publishing NPC death event., Resolve UUID participant id to canonical NPC string id when mapping exists. (+12 more)

### Community 659 - "PanelState"
Cohesion: 0.05
Nodes (48): PanelManager(), PanelManagerProps, minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapPanelSection(), MinimapPanelSectionProps, PanelContainer, PanelContainerProps (+40 more)

### Community 660 - ".claude/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 661 - "EdgeDetailsPanel.tsx"
Cohesion: 0.11
Nodes (15): buildEdgeFieldModel(), EdgeAdminActionsProps, EdgeDeleteConfirmProps, EdgeDetailRow(), EdgeDetailRowProps, EdgeDetailsFields(), EdgeDetailsFieldsProps, EdgeDetailsPanel() (+7 more)

### Community 662 - ".cursor/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 663 - "MUD Disconnect Grace Period & Rest Command: Industry Comparison"
Cohesion: 0.33
Nodes (5): 11. Missing Features from Other MUDs, Executive Summary, Features We're NOT Implementing (but exist elsewhere), MUD Disconnect Grace Period & Rest Command: Industry Comparison, Questions for Discussion

### Community 664 - "test_npc_event_handlers.py"
Cohesion: 0.03
Nodes (81): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers. Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON. (+73 more)

### Community 665 - "Code Review: Import Analysis and Anti-Patterns"
Cohesion: 0.08
Nodes (23): 1. **Import Inconsistency in `server/persistence.py`**, 2. **Import Organization Pattern**, Additional Findings, Best Practices Analysis, Code Review: Import Analysis and Anti-Patterns, Conclusion, Configuration Files, Container Files (+15 more)

### Community 666 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 667 - "compilerOptions"
Cohesion: 0.09
Nodes (22): compilerOptions, baseUrl, lib, module, moduleResolution, noEmit, noFallthroughCasesInSwitch, noUnusedLocals (+14 more)

### Community 668 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 669 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 670 - "generate_html_visualization.py"
Cohesion: 0.13
Nodes (22): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+14 more)

### Community 671 - "verify_migration.py"
Cohesion: 0.15
Nodes (22): _check_foreign_keys(), _check_null_values(), _check_table_exists(), main(), _print_json_validation_results(), _print_sample_data(), _print_verification_summary(), Connection (+14 more)

### Community 672 - "test_emote.py"
Cohesion: 0.10
Nodes (22): Emote, Base, Predefined emote definitions., Unit tests for emote models. Tests the Emote and EmoteAlias SQLAlchemy models., Test EmoteAlias aliases are case sensitive., Test Emote can be instantiated with required fields., Test Emote has correct table name., Test Emote __repr__ method. (+14 more)

### Community 673 - "RoomCacheLoader"
Cohesion: 0.20
Nodes (5): Any, BaseException, Loads room data from the database and populates a room cache dict. Used by…, Load rooms from PostgreSQL and update the room cache., RoomCacheLoader

### Community 674 - "GameTerminalContext.test.tsx"
Cohesion: 0.16
Nodes (17): GameTerminalContext, GameTerminalContextType, GameTerminalProvider(), GameTerminalProviderProps, useConnectionState(), useGameActions(), useGameState(), useGameTerminalContext() (+9 more)

### Community 675 - "MockPersistence"
Cohesion: 0.18
Nodes (7): mock_persistence(), MockPersistence, Mock persistence layer with async methods., Mock async method that uses configured mock., Mock method that uses configured mock., Allow setting get_player_by_name and get_room_by_id to mocks., Create a mock persistence layer.

### Community 676 - "PlayerInventory"
Cohesion: 0.12
Nodes (20): PlayerInventory, Player inventory model for persistent storage of items. This matches the…, _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player (+12 more)

### Community 677 - "tailwind Best Practices"
Cohesion: 0.22
Nodes (8): 1. Design System Configuration, 2. Component Abstraction, 3. Class Ordering & Readability, 4. Mobile-First & Responsive Design, 5. Performance Optimization, 6. Accessibility, 7. Theming & Dark Mode, tailwind Best Practices

### Community 678 - "ChannelBroadcastingStrategyFactory"
Cohesion: 0.20
Nodes (9): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Register a new strategy for a channel type. Args: channel_type: Channel type to…, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…, Test ChannelBroadcastingStrategyFactory.register_strategy() registers new…, Test global channel_strategy_factory instance exists., test_channel_broadcasting_strategy_factory_init(), test_channel_broadcasting_strategy_factory_register_strategy() (+1 more)

### Community 679 - "async_load_zone_configurations"
Cohesion: 0.16
Nodes (21): async_load_zone_configurations(), Async helper to load zone configurations from PostgreSQL database., _empty_zone_load_result(), asyncio, MonkeyPatch, Test process_subzone_rows() processes subzone rows., Test process_subzone_rows() handles empty result., Test async_load_zone_configurations() loads configurations successfully. (+13 more)

### Community 680 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 681 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 682 - "CombatBroadcastMixin"
Cohesion: 0.13
Nodes (13): CombatBroadcastMixin, Any, Broadcast combat start message to all players in the room., Mixin for combat-related broadcast methods. Requires connection_manager on self., Broadcast combat attack to room. Excludes attacker from broadcast; sends them a…, Broadcast NPC death message to all players in the room., Build perspective-specific attack messages., Broadcast combat end message to all players in the room. (+5 more)

### Community 683 - "Net Impact Summary"
Cohesion: 0.22
Nodes (8): Additions, Coverage Gap Priority Matrix, If We Execute Full Recommendations, Net Impact Summary, Net Result, Removals, Test Coverage Gaps Report, "The goal is not comprehensive coverage of all code, but comprehensive protection of all user value."

### Community 684 - "MemoryLeakMetricsCollector"
Cohesion: 0.12
Nodes (16): MemoryLeakMetricsCollector, Any, Collect event metrics from EventBus. Returns: Dictionary with event metrics, Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics, Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics, Collect NATS subscription metrics from NATSService. Returns: Dictionary with…, Unified metrics collector for memory leak detection. Aggregates metrics from…, Calculate growth rate for a single metric. Args: current: Current metrics… (+8 more)

### Community 685 - "delegate_error_handler"
Cohesion: 0.16
Nodes (25): delegate_error_handler(), Generic delegate for error handler methods. Args: error_handler: Error handler…, detect_and_handle_error_state_impl(), handle_authentication_error_impl(), handle_security_violation_impl(), handle_websocket_error_impl(), Any, UUID (+17 more)

### Community 686 - "asyncio"
Cohesion: 0.09
Nodes (23): asyncio, Test _execute_command_handler successfully executes handler., Test _execute_command_handler handles handler errors., Test process_command successfully processes command string., Test process_command handles parse errors., Test process_command handles missing handler., Test _execute_command_handler handles handler returning non-dict., Test process_validated_command successfully routes to handler. (+15 more)

### Community 687 - "Performance Profiler Subagent"
Cohesion: 0.10
Nodes (21): Bottleneck Identification, Capabilities, Code Performance Review, Database Performance, Database Query Optimization, Enhanced Logging Integration, Example Scenarios, Game Loop Performance (+13 more)

### Community 688 - "Security Auditor Subagent"
Cohesion: 0.09
Nodes (21): Authentication & Authorization, Authentication Security Review, Capabilities, COPPA Compliance, COPPA Compliance (Critical), COPPA Compliance Verification, Example Scenarios, Input Validation (+13 more)

### Community 689 - "The Toolkit"
Cohesion: 0.09
Nodes (22): Overdrive Skill, Animate complex properties, Assess What "Extraordinary" Means Here, For data-heavy interfaces, For functional UI, For performance-critical UI, For visual/marketing surfaces, Implement with Discipline (+14 more)

### Community 690 - "test_profession_repository.py"
Cohesion: 0.17
Nodes (19): _bool_or_default(), Any, Return value as str or a default if falsy., Return text value or default if falsy., Return bool(value) when not None, otherwise default., _str_or_default(), _text_or_default(), _mock_session() (+11 more)

### Community 691 - "UUID"
Cohesion: 0.10
Nodes (13): UUID, Track a player's combat state. Args: player_id: ID of the player player_name:…, Clear a player's combat state. Args: player_id: ID of the player, Synchronously check if a player is currently in combat. This is the preferred…, Check if a player is currently in combat. Args: player_id: ID of the player…, Get all players currently in combat. Returns: List of player IDs currently in…, Handle combat start for a player. Args: player_id: ID of the player…, Handle combat end by clearing all players in the combat. Args: combat_id: ID of… (+5 more)

### Community 692 - "compilerOptions"
Cohesion: 0.15
Nodes (12): compilerOptions, allowImportingTsExtensions, composite, noEmit, rootDir, types, exclude, extends (+4 more)

### Community 693 - "include"
Cohesion: 0.11
Nodes (17): compilerOptions, noEmit, types, exclude, extends, include, node, src/**/*.spec.ts (+9 more)

### Community 694 - "ADR-012: python-statemachine for Backend Connection FSM"
Cohesion: 0.09
Nodes (21): 10. Related ADRs, 11. Changelog, 1. Overview, 2. Context and Problem Statement, 3. Decision Drivers, 4. Considered Options, 5. Decision Outcome, 6. Implementation Details (+13 more)

### Community 695 - "Asyncio Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.09
Nodes (21): 1. Blocking Synchronous Operations in Async Methods, 2. asyncio.run() Called from Context with Existing Event Loop, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Event Loop Change Detection May Not Handle All Cases, 6. Synchronous Database Operations in Async Context, 7. Missing Transaction Management in Batch Operations, 8. Connection Pool Size Configuration (+13 more)

### Community 696 - "Ruff to Pylint Rule Mapping"
Cohesion: 0.09
Nodes (21): B008 - Function calls in argument defaults, B904 - Broad except, C901 - Too complex (PRIMARY COMPLEXITY CHECKER), Category Mappings, Complexity Checking, `docs/**/*` files: Multiple rules, E402 - Module level import not at top, E501 - Line too long (+13 more)

### Community 697 - "SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.09
Nodes (21): 1. SQL Injection Vulnerability in `update_player_stat_field()` - ✅ FIXED, 2. Missing Eager Loading for Relationships, 3. Mixed Database Access Patterns, 4. F-String SQL Construction (Even with Constants), 5. Missing Indexes on Foreign Keys, 6. Long-Lived Sessions, 7. Connection Pool Configuration, 8. Transaction Boundaries (+13 more)

### Community 698 - "MythosMUD Test Suite Modernization Plan"
Cohesion: 0.09
Nodes (21): Current State, Decision Framework: Uplift vs Greenfield Rewrite, Executive Summary, Goal, Greenfield Only If, Key Files, Known Risks, MythosMUD Test Suite Modernization Plan (+13 more)

### Community 699 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 700 - "monitoring_service"
Cohesion: 0.25
Nodes (8): mock_combat_config(), mock_config(), mock_feature_flags(), monitoring_service(), fixture, Create mock feature flags., Create mock combat config., Create CombatMonitoringService instance with mocked dependencies.

### Community 701 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.10
Nodes (52): check_ai_guardrails(), _check_single_use_file(), _collect_code_texts(), _guardrail_scan_inputs(), _is_single_use_small_file(), _process_added_file_checks(), build_context(), ChangedFile (+44 more)

### Community 702 - "fix_suppression_alignment.py"
Cohesion: 0.16
Nodes (21): add_pylint_suppression(), add_ruff_suppression(), _apply_fixes_to_line(), fix_file(), _group_fixes_by_line(), main(), parse_alignment_report(), _parse_file_line_pattern() (+13 more)

### Community 703 - "identify_critical_code.py"
Cohesion: 0.15
Nodes (21): analyze_file(), analyze_function(), calculate_complexity(), calculate_priority(), check_file_keywords(), check_function_keywords(), main(), process_ast_functions() (+13 more)

### Community 704 - "test_postgres_adapter.py"
Cohesion: 0.14
Nodes (12): connect_postgres(), convert_sqlite_to_postgres_query(), Create a PostgreSQL connection. Args: database_url: PostgreSQL connection URL…, Convert legacy SQLite query syntax to PostgreSQL syntax. Note: This function is…, Unit tests for PostgreSQL adapter. Tests PostgresRow, PostgresConnection,…, Test utility functions., Test connect_postgres()., Test connect_postgres() with driver prefix. (+4 more)

### Community 705 - "UnknownChannelStrategy"
Cohesion: 0.25
Nodes (6): Strategy for unknown channel types., Initialize unknown channel strategy. Args: channel_type: Unknown channel type, Get strategy for channel type. Args: channel_type: Type of channel to get…, UnknownChannelStrategy, Test ChannelBroadcastingStrategyFactory.get_strategy() returns…, test_channel_broadcasting_strategy_factory_get_strategy_unknown()

### Community 706 - "command_result_text"
Cohesion: 0.07
Nodes (58): handle_put_command(), _put_resolve_container_id(), _put_run_validated(), _put_transfer_finish(), PutCommandRuntime, PutValidatedWork, CommandResponse, Player (+50 more)

### Community 707 - "RoomRepository"
Cohesion: 0.14
Nodes (12): Repository for room persistence operations. Handles room caching and retrieval.…, Initialize the room repository. Args: room_cache: Shared room cache dictionary, Get a room by ID from cache. Args: room_id: Room identifier Returns: Room |…, List all cached rooms. Returns: list[Room]: List of all rooms Note: This is…, Save a room to the cache. Args: room: Room object to save Note: Rooms are…, Save multiple rooms to the cache. Args: rooms: List of room objects to save…, RoomRepository, Unit tests for RoomRepository. (+4 more)

### Community 708 - "get_summary"
Cohesion: 0.67
Nodes (3): get_summary(), Any, Get a summary of exception counts. Returns: dict[str, Any]: Dictionary…

### Community 709 - "PostgresCursor"
Cohesion: 0.12
Nodes (12): PostgresCursor, cursor, PostgreSQL cursor wrapper for query result access., Get the number of rows affected., Test PostgresCursor class., Test PostgresCursor initialization., Test PostgresCursor.fetchone() with row., Test PostgresCursor.fetchone() with None. (+4 more)

### Community 710 - "handle_unequip_command"
Cohesion: 0.29
Nodes (16): handle_unequip_command(), CommandResponse, Player, Unequip an item into the player's inventory., _unequip_persist_or_rollback(), _unequip_run_mutation(), _unequip_success_payload(), _mutation_cm() (+8 more)

### Community 711 - "test_users.py"
Cohesion: 0.02
Nodes (137): AuthenticationBackend, BaseUserManager, ID, generate_unique_bogus_email(), is_bogus_email(), AsyncSession, Email utilities for MythosMUD authentication. This module provides utilities…, Generate a unique bogus email address for a user. This function creates a bogus… (+129 more)

### Community 712 - "test_player_repository_room.py"
Cohesion: 0.20
Nodes (20): Any, Player, Player room validation helpers for PlayerRepository. Validates and fixes…, Return True if room validation should be skipped (cache empty, instanced, or…, Validate player's current room and fix if invalid. Args: room_cache: Shared…, Validate and fix player room, persisting the fix if needed. Args: room_cache:…, should_skip_room_validation(), validate_and_fix_player_room() (+12 more)

### Community 713 - "fixture"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Create a mock prototype registry., Create a sample room drop item., Create a sample inventory item., Create a sample equipped item., sample_equipped_item(), sample_inventory_item() (+1 more)

### Community 714 - "talk_command.py"
Cohesion: 0.13
Nodes (26): _emit_prompt(), handle_talk_command(), UUID, talk / talk <n> command for NPC dialogue trees (#583)., Handle talk <npc> or talk <n> against same-room NPCs., Extract player UUID from player model., Join talk args into a single remainder string., Send personal system message for a node; return short command result. (+18 more)

### Community 715 - "1. Structured Concurrency: Entry Points and Task Management"
Cohesion: 0.29
Nodes (7): 1.1. Top-Level Entry Point, 1.2. Launching Concurrent Tasks, 1.3. Grouping Tasks, 1. Structured Concurrency: Entry Points and Task Management, 2.1. CPU-Bound Work, 2. Avoiding Blocking Operations, asyncio Best Practices

### Community 716 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test get_adjacent_rooms() handles room with no exits., Test get_adjacent_rooms() handles target room not found., Test validate_room_exists() uses cache., Test validate_room_exists() falls back to persistence., Test get_room_occupants() handles Room object with get_players/get_npcs., Test get_room_occupants() falls back to persistence., Test validate_player_in_room() returns False when room not found. (+17 more)

### Community 717 - "_get_proper_data_dir"
Cohesion: 0.40
Nodes (4): _get_proper_data_dir(), Path, Get the proper environment-aware data directory for user management. Uses…, Initialize the user manager. Args: data_dir: Directory for player-specific mute…

### Community 718 - "test_game_state_provider.py"
Cohesion: 0.09
Nodes (21): Unit tests for game state provider. Tests the GameStateProvider class., Test get_npcs_batch() returns NPC names., Test get_npcs_batch() returns empty dict for empty input., Test get_npcs_batch() handles None in NPC IDs list., Test _get_fallback_player_data() uses get_stats when available., Test _get_fallback_player_data() parses JSON stats string., Test _get_player_name_with_grace_periods() returns name with grace indicators., Test get_npcs_batch() resolves names from active NPCs. (+13 more)

### Community 719 - "get_room_environment"
Cohesion: 0.12
Nodes (14): Test get_room_environment() treats empty string as no environment., Test get_room_environment() function., Test get_room_environment() returns room-specific environment., Test get_room_environment() returns subzone environment when room doesn't have…, Test get_room_environment() returns zone environment when room and subzone…, Test get_room_environment() returns default 'outdoors' when no environment…, Test get_room_environment() prioritizes room environment over subzone and zone., Test get_room_environment() prioritizes subzone environment over zone. (+6 more)

### Community 720 - "TestErrorHandlers"
Cohesion: 0.10
Nodes (16): asyncio, Test error handler functions., Test mythos_exception_handler., Test mythos_exception_handler with debug enabled., Test mythos_exception_handler sets request_id in context., Test general_exception_handler., Test logged_http_exception_handler for 401., Test logged_http_exception_handler for 404. (+8 more)

### Community 721 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 722 - "mock_persistence"
Cohesion: 0.29
Nodes (7): mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request with app state and container., Create a mock persistence., Create a mock player.

### Community 723 - "test_logging_file_setup.py"
Cohesion: 0.13
Nodes (23): QueueListener, get_queue_listener(), Return the global QueueListener if running (for tests and shutdown). Returns:…, Stop the global QueueListener and reset state (for tests and shutdown). Allows…, stop_queue_listener(), default_log_config(), fixture, Unit tests for logging file setup. Verifies aggregator handlers attached to… (+15 more)

### Community 724 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 725 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 726 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "A Message of Art; And Some Fell on Stony Ground; Nameless Ho", Community 10 - "Stowell; Betty Considine (waitress); Wesley Frost (bank cler", Community 1 - "Handout: Amaranthine 1; Dunwich (Keeper Map); Dunwich Throug", Community 2 - "An Amaranthine Desire; Captain Louis Gerd; Dunwich (Suffolk)", Community 3 - "An Amaranthine Desire; Clare Boone; Dunwich, Suffolk, Englan", Community 4 - "A Message of Art; Evocations of the Inner God; Josephin Pela", Community 5 - "Church of Sunyata; Craig Steele; The Hungry Void" (+12 more)

### Community 727 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "Pandora's Box / Pandora Handout 10", Community 10 - "Chapter 6: Pulp Magic, Psychic Powers, and Weird S / Psychic Powers", Community 1 - "Disintegrator device / Handout: Disintegrator 1", Community 2 - "Chapter 1: The Pulps / Chapter 7: Running Pulp Games", Community 3 - "Avoiding Certain Death / Call of Cthulhu 7th Edition", Community 4 - "Cthulhu Mythos / Deep One", Community 5 - "Seekers of Eternal Wisdom / Handout: Pandora's Box 12" (+12 more)

### Community 728 - "🎯 Test Categories"
Cohesion: 0.10
Nodes (20): 1. Application Startup & CORS (create_app), 2. WebSocket Connections, 3. Room Operations, 4. Container Operations, 5. Player Respawn, 6. Game Tick Processing, 7. Integration Tests, Complexity Refactoring Test Plan (+12 more)

### Community 729 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 730 - "NATS Anti-Patterns Remediation Summary"
Cohesion: 0.10
Nodes (20): 1. Fixed Synchronous Operation in WebSocket Helpers, 2. Standardized Error Handling, 3. Added Message Validation to NATSMessageBroker, 4. Improved Batch Flush Error Recovery, 5. Improved Connection Pool Error Handling, After Remediation, Backward Compatibility, Before Remediation (+12 more)

### Community 731 - "ConnectionManager Refactoring Summary"
Cohesion: 0.10
Nodes (20): 1. Statistics & Monitoring (`realtime/monitoring/`), 2. Error Handling (`realtime/errors/`), 3. Health Monitoring (`realtime/monitoring/`), 4. Cleanup & Maintenance (`realtime/maintenance/`), 5. Game State Management (`realtime/integration/`), 6. Room Event Integration (`realtime/integration/`), 7. Message Broadcasting (`realtime/messaging/`), After (+12 more)

### Community 732 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 733 - "PersonalMessageSender"
Cohesion: 0.12
Nodes (26): PersonalMessageSender, Any, UUID, Send message to a single WebSocket connection. Returns True if successful., Queue message if no active connections., Send a personal message to a player via WebSocket. Args: player_id: The…, Get message delivery statistics for a player., Sends personal messages to individual players. This class provides: - Personal… (+18 more)

### Community 734 - "properties"
Cohesion: 0.15
Nodes (13): minLength, type, maximum, minimum, type, minLength, type, type (+5 more)

### Community 735 - "audit_suppressions.py"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 736 - "fix_markdown_line_length.py"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 737 - "populate_npc_sample_data.py"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 738 - "pydantic Best Practices"
Cohesion: 0.25
Nodes (8): 1. Model Naming and Organization, 2. Strict Typing and Immutability, 3. Safe Default Values, 4. Custom Validation Logic, 5. Settings Management, 6. Editor Integration (VS Code / Pylance), 7. Common Pitfalls, pydantic Best Practices

### Community 739 - "worktree-plan-template.md"
Cohesion: 0.25
Nodes (7): Cleanup Checklist, Context, Design Notes, Metadata, Plan / Todos, Risks and Edge Cases, Testing

### Community 740 - "lock_state"
Cohesion: 0.25
Nodes (8): locked, sealed, unlocked, default, description, enum, type, lock_state

### Community 741 - "MetricsCollector"
Cohesion: 0.09
Nodes (17): MetricsCollector, Any, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or…, Simple metrics collector for NATS message delivery. Thread-safe metrics…, Get concise metrics summary. Returns: High-level metrics summary AI: For quick… (+9 more)

### Community 742 - "npc_combat_grace.py"
Cohesion: 0.14
Nodes (18): get_app_instance(), Return the runtime app instance attached during lifespan startup. This provides…, _connection_manager_from_config_app(), is_npc_attack_on_player_blocked_by_login_grace_period(), is_player_attack_blocked_by_login_grace_period(), UUID, Login grace-period checks for NPC combat integration (extracted to keep service…, Resolve connection_manager from the public config app accessor. Uses getattr on… (+10 more)

### Community 743 - "test_look_container_helpers.py"
Cohesion: 0.05
Nodes (44): asyncio, Unit tests for look container helper functions. Tests the helper functions in…, Test _find_container_in_room() with instance number out of range., Test _find_container_in_room() with instance number zero., Test _find_container_via_inner_container() when item has no inner_container., Test _find_container_via_inner_container() with invalid UUID., Test _find_container_via_inner_container() when persistence has no…, Test _matches_item_instance_id() returns True when IDs match. (+36 more)

### Community 744 - "test_lifespan_shutdown.py"
Cohesion: 0.13
Nodes (36): FastAPI, Application shutdown logic. This module handles graceful shutdown of all…, Shutdown event bus and clean up all service subscriptions., Handle graceful shutdown of all services., Shutdown and persist mythos chronicle state., Shutdown NATS message handler if present., Shutdown connection manager if present., Shutdown mythos tick scheduler if present. (+28 more)

### Community 745 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 746 - "Path"
Cohesion: 0.10
Nodes (14): Path, Fix self-references by adding proper flags. Args: room_database: Complete room…, Find the file for a room. Returns None if file doesn't exist., Create backup if requested., Fix missing exits field. Returns True if fixed., Fix missing optional fields. Returns True if any fixed., Initialize the room fixer. Args: base_path: Base directory for room files, Fix missing fields based on errors. Returns True if any fixed. (+6 more)

### Community 747 - "TestPathValidator"
Cohesion: 0.10
Nodes (12): fixture, Tests for path validator functionality. Validates room connectivity analysis…, Test detection of mismatched return paths across zones., Test suite for path validation functionality., Create a path validator instance., Sample rooms with zone transitions., Test detection of zone transitions in room connections., Test detection of broken zone transitions. (+4 more)

### Community 748 - "Design Critique"
Cohesion: 0.10
Nodes (20): Critique Skill, 10. Microcopy & Voice, 1. AI Slop Detection (CRITICAL), 2. Visual Hierarchy, 3. Information Architecture, 4. Emotional Resonance, 5. Discoverability & Affordance, 6. Composition & Balance (+12 more)

### Community 749 - "useThemeContext.ts"
Cohesion: 0.22
Nodes (17): useAccessibilityPreference(), useAnimationPreference(), useColorSchemePreference(), useCompactModePreference(), useDebugInfoPreference(), useFontSizePreference(), useTheme(), useThemePreference() (+9 more)

### Community 750 - "multiplayer-browser-helpers.bundle.js"
Cohesion: 0.20
Nodes (17): buttonHasLoginSubmitLabel(), computedStyleHidesElement(), elementTextIncludesGameInfo(), fieldHasCommandPlaceholder(), getBodyInnerText(), hasCommandInputInBrowser(), hasGameInfoAnyMessageInBrowser(), hasGameInfoPanelInBrowser() (+9 more)

### Community 751 - "compilerOptions"
Cohesion: 0.04
Nodes (48): compilerOptions, allowImportingTsExtensions, baseUrl, isolatedModules, jsx, lib, module, moduleResolution (+40 more)

### Community 752 - "verify_password"
Cohesion: 0.09
Nodes (21): Verify a plaintext password against an Argon2 hash. This function verifies…, verify_password(), Verify password using Argon2 instead of bcrypt., Test verifying password with non-string password returns False., Test verifying password with non-string hash returns False., Test verifying password with empty hash returns False., Test verify_password handles VerificationError., Test successful password verification. (+13 more)

### Community 753 - "Communities (10 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (19): Communities (10 total, 0 thin omitted), Community 0 - "Hotel Hell", Community 1 - "Petersen's Abominations", Community 2 - "Hotel Hell", Community 3 - "Voice on the Phone", Community 4 - "Mohole", Community 5 - "Panacea", Community 6 - "Panacea" (+11 more)

### Community 754 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, properties, minLength, type, id, name, season (+4 more)

### Community 755 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, minLength, type, properties, minLength, type, type (+4 more)

### Community 756 - "ApplicationContainer Structure Analysis and Domain-Specific Split Proposal"
Cohesion: 0.10
Nodes (19): 1. Executive Summary, 2.1 Attribute Inventory by Domain, 2.2 Initialization Order and Dependencies, 2.3 Private Initializers and Helpers, 2.4 Public API and Consumers, 2. Current Structure Analysis, 3.1 Option A: Internal Bundles (Recommended), 3.2 Option B: Composed Sub-Containers (Alternative) (+11 more)

### Community 757 - "Changes by document"
Cohesion: 0.10
Nodes (19): Audit date, Changes by document, CLAUDE.md, docs/COMMAND_MODELS_REFERENCE.md, docs/CONFIGURATION_FILES_REFERENCE.md, docs/CONTAINER_SYSTEM_API_REFERENCE.md, docs/DATABASE_ACCESS_PATTERNS.md, docs/E2E_TESTING_GUIDE.md (+11 more)

### Community 758 - "Lizard Complexity Analysis Findings"
Cohesion: 0.10
Nodes (19): 1. `create_app` - CCN: 22, 2. `_load_rooms_with_coordinates` - CCN: 12, 3. `_parse_websocket_token` - CCN: 12, 4. `_ensure_coordinates_generated` - CCN: 11, 🔴 CRITICAL: Functions Exceeding Threshold (CCN > 10), Functions with CCN = 10, Functions with CCN = 9, Lizard Complexity Analysis Findings (+11 more)

### Community 759 - "NATS Medium-Priority Remediation Summary"
Cohesion: 0.10
Nodes (20): 1. Integrated Subject Manager into NATSMessageBroker, 2. Added Health Monitoring to NATSMessageBroker, 3. Documented Manual Acknowledgment Strategy, After Medium-Priority Fixes, Before Medium-Priority Fixes, Completed Medium-Priority Fixes ✅, Configuration Options, Event Callback Improvements (+12 more)

### Community 760 - "2. Mythos Time Model Draft"
Cohesion: 0.10
Nodes (19): 1. Research Synthesis, 2. Mythos Time Model Draft, 3. Implementation Blueprint, 4. Client HUD Implementation, Calendar structure, Chronicle bootstrap, Configuration & persistence, Core services (+11 more)

### Community 761 - "Phase 2: Qualitative Analysis Results"
Cohesion: 0.07
Nodes (30): 2.1 Regression Test Audit (★★★★★ HIGH VALUE), 2.2 Integration Test Analysis (★★★★☆ HIGH-MEDIUM VALUE), 2.3 Coverage Test Review (★★☆☆☆ MEDIUM-LOW VALUE), 2.4 Unit Test Pattern Analysis (★★★☆☆ MIXED VALUE), 2.5 Infrastructure Test Review (★☆☆☆☆ LOW VALUE), 2.6 E2E Test Analysis (★★★★★ HIGH VALUE), 2.7 Security Test Analysis (★★★★★ HIGH VALUE), Assessment (+22 more)

### Community 762 - "LoggingPatternLinter"
Cohesion: 0.11
Nodes (15): FormattedValue, lint_file(), LoggingPatternLinter, main(), Call, Import, ImportFrom, Path (+7 more)

### Community 763 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 764 - "UpgradeImplementationPlan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 765 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 766 - "validate_secure_path"
Cohesion: 0.08
Nodes (24): Validate and sanitize a user-provided path to prevent path traversal attacks.…, validate_secure_path(), Test validate_secure_path detects when common_path != base_path (lines 59-66)., Test validate_secure_path with valid path., Test validate_secure_path handles different drives on Windows., Test validate_secure_path rejects path traversal with .., Test validate_secure_path rejects path traversal with ~, Test validate_secure_path with nested valid path. (+16 more)

### Community 767 - "test_container_persistence_crud.py"
Cohesion: 0.03
Nodes (131): ContainerData, Container data class for the unified container system., Data class for container information., Convert container data to dictionary for ContainerComponent., allowed_roles_from_row(), as_opt_datetime(), as_opt_str(), as_opt_uuid() (+123 more)

### Community 768 - "MessageBroker"
Cohesion: 0.11
Nodes (12): Infrastructure layer for MythosMUD. This package contains abstractions for…, MessageBroker, Any, Protocol, Send a request and wait for a reply (request-reply pattern). Args: subject:…, Protocol defining the message broker interface. This abstract interface allows…, Connect to the message broker. Returns: bool: True if connection successful,…, Disconnect from the message broker. Closes all subscriptions and releases… (+4 more)

### Community 769 - "CommandRateLimiter"
Cohesion: 0.10
Nodes (22): CommandRateLimiter, Any, datetime, Per-player command rate limiting. Prevents command flooding and denial-of-…, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate… (+14 more)

### Community 770 - "ComprehensiveLoggingMiddleware"
Cohesion: 0.11
Nodes (22): ComprehensiveLoggingMiddleware, Any, ASGIApp, Exception, Receive, Request, Scope, Send (+14 more)

### Community 771 - "test_event_publisher.py"
Cohesion: 0.06
Nodes (40): asyncio, Unit tests for event publisher. Tests the EventPublisher class., Test publish_game_tick_event() when NATS is not connected., Test get_next_sequence_number() returns and increments sequence., Test reset_sequence_number() resets sequence to 0., Test EventPublisher initialization without subject manager., Test EventPublisher initialization with initial sequence., Persistence lookup should replace Player_/Room_ fallbacks in event data. (+32 more)

### Community 772 - "SystemAdminChannelStrategy"
Cohesion: 0.33
Nodes (5): Strategy for system/admin channel broadcasting., Initialize system/admin channel strategy. Args: channel_type: Type of…, SystemAdminChannelStrategy, Personal system messages deliver to target_player_id only., test_system_admin_channel_strategy_personal_target()

### Community 773 - "test_chat_validator.py"
Cohesion: 0.14
Nodes (25): _chat_passes_nats_validation(), Return True when message content and room access checks pass., contains_malicious_content(), Validate chat message before transmission. Args: chat_message: The chat message…, Validate sender has access to the room. Args: sender_id: ID of the message…, Check for malicious content patterns. Args: content: The message content to…, validate_chat_message(), validate_room_access() (+17 more)

### Community 774 - "handle_skills_command"
Cohesion: 0.14
Nodes (21): _format_skills_output(), _get_container_services(), handle_skills_command(), Any, UUID, Get container, persistence, and skill_service from request, or None if…, Extract and validate player_id from player object, returning UUID or None., Resolve user_id from current_user (auth user) or fallback to player.user_id. (+13 more)

### Community 775 - "test_room_service.py"
Cohesion: 0.08
Nodes (23): Unit tests for room service. Tests the RoomService class for room-related…, Test get_room_by_name() returns None (not implemented)., Test list_rooms_in_zone() returns empty list (not implemented)., Test update_environment_state() updates environment state., Test get_environment_state() returns current environment state., Test describe_lighting() returns description for day., Test describe_lighting() returns description for night., Test describe_lighting() returns default for unknown daypart. (+15 more)

### Community 776 - "test_room_subscription_manager_npcs.py"
Cohesion: 0.09
Nodes (23): asyncio, fixture, Unit tests for room subscription manager NPC helpers. Tests NPC-related helpers…, Test get_room_occupants() includes NPCs from lifecycle manager., Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager…, Create a RoomSubscriptionManager instance., Test _get_npc_name_from_lifecycle_manager gets NPC name., Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found. (+15 more)

### Community 777 - "UUID"
Cohesion: 0.28
Nodes (5): UUID, Count active connections not tied to any online player., Build the connections subsection of memory stats., Build the sessions subsection of memory stats., Return numerator/denominator, or 0 when denominator is empty.

### Community 778 - "TestVerificationSqlUsersPlayers"
Cohesion: 0.10
Nodes (12): PostgreSQL-focused tests for verification and maintenance SQL scripts.…, Tests for db/verification/users_players.sql alignment with current schema., Verification SQL file must exist., Verification SQL must not reference staging tables or select obsolete columns., Verification SQL must use explicit join syntax for multi-table queries., Verification SQL must reference users and players tables., Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)., NPC name constraint script must exist. (+4 more)

### Community 779 - "PayloadOptimizer"
Cohesion: 0.12
Nodes (24): get_payload_optimizer(), PayloadOptimizer, Payload optimization for WebSocket messages. This module provides utilities for…, Optimizes payloads for WebSocket transmission. Features: - Size limit…, Get the global payload optimizer instance., Initialize the payload optimizer. Args: max_payload_size: Maximum payload size…, _CompareExplodes, optimizer() (+16 more)

### Community 780 - "_RoomPersistence"
Cohesion: 0.40
Nodes (4): Protocol, Protocol for persistence with get_room_by_id., Return the room object for the given room_id, or None if not found., _RoomPersistence

### Community 781 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 782 - "static_data/package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 783 - "Delight Techniques"
Cohesion: 0.11
Nodes (19): Delight Skill, Appropriate to Context, Assess Delight Opportunities, Celebration Moments, Compound Over Time, Delight Amplifies, Never Blocks, Delight Principles, Delight Techniques (+11 more)

### Community 784 - "Frontend Design Skill"
Cohesion: 0.11
Nodes (19): Frontend Design Skill, Color & Theme, Context Gathering Protocol, Design Direction, Frontend Aesthetics Guidelines, Implementation Principles, Interaction, Layout & Space (+11 more)

### Community 785 - "ContainerLockMixin"
Cohesion: 0.21
Nodes (11): ContainerLockMixin, ContainerComponent, ContainerLockState, Player, UUID, Lock a container (LOCKED or SEALED). Requires ownership or admin., Unlock a container. Requires access and unlock eligibility (key/admin)., Lock/unlock container state persistence. (+3 more)

### Community 786 - "compilerOptions"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 787 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test NPCService initialization., Test get_npc_definitions() handles database errors., Test get_npc_definition() returns definition when found., Test create_npc_definition() raises ValueError for invalid probability., Test create_npc_definition() raises ValueError for invalid max population., Test update_npc_definition() successfully updates definition., Test get_system_statistics() handles database errors. (+7 more)

### Community 788 - "Enhanced Logging Quick Reference"
Cohesion: 0.11
Nodes (18): API Requests, Clear Context, Common Patterns, Context Binding, 🚨 CRITICAL: DO NOT USE, Database Operations, Enhanced Logging Quick Reference, Errors with Context (+10 more)

### Community 789 - "NumPy Code Review - MythosMUD Codebase"
Cohesion: 0.11
Nodes (18): Code Quality Improvements Achieved, Completed Actions, Conclusion, Executive Summary, Findings, 🟡 HIGH PRIORITY: Manual Statistical Calculations, ✅ Implementation Status, Issue 1: Performance Monitor - Manual Statistics (+10 more)

### Community 790 - "Python Model Updates Required for Migration 019"
Cohesion: 0.11
Nodes (18): 1. Import BigInteger, 2. Files Requiring Updates, Impact Assessment, Integer → BigInteger, Low Risk Changes, No Breaking Changes Expected, Overview, Python Model Updates Required for Migration 019 (+10 more)

### Community 791 - "Transaction Boundaries Audit"
Cohesion: 0.11
Nodes (18): ✅ AsyncPersistenceLayer (Async), Audit Date, Audited Operations, Current State: ✅ GOOD, Future Improvements, Multi-Step Operations, Notes, Pattern 1: Connection Context Manager (PersistenceLayer) (+10 more)

### Community 792 - "asyncio"
Cohesion: 0.09
Nodes (22): asyncio, Test EventBus.publish() queues or processes event., Test EventBus.shutdown() stops processing., Test EventBus.shutdown() is idempotent., Test _stop_processing() when not running., Test EventBus.shutdown() automatically cleans up all service subscriptions., Test multiple services subscribing to the same event type., Test that service shutdown removes all subscribers for that service. This test… (+14 more)

### Community 793 - "enum"
Cohesion: 0.11
Nodes (19): ACCESSORY, AMULET, BELT, CURSED, FEET, GLOW, HANDS, HEAD (+11 more)

### Community 794 - "test_container_persistence_sql_injection.py"
Cohesion: 0.17
Nodes (10): _create_mock_container_row(), UUID, Tests for SQL injection protection in container persistence operations. These…, Test that update_container uses parameterized queries, not string concatenation., Test that column names are hardcoded, not from user input., Create a complete mock container row with all required columns., Test SQL injection protection in container persistence., Test that SQL injection in lock_state is prevented. (+2 more)

### Community 795 - "CombatConfiguration"
Cohesion: 0.09
Nodes (17): CombatConfiguration, Combat configuration data class., Validate configuration and return list of errors., Test validate catches XP multiplier too high., Test validate catches alert threshold out of range., Test validate catches max participants out of range., Test suite for CombatConfiguration dataclass., Test CombatConfiguration initialization with defaults. (+9 more)

### Community 796 - "Any"
Cohesion: 0.11
Nodes (12): Any, Path, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a serialized alias bundle against the alias schema. Args: alias_data:…, Validate emote definition data against the emote schema. Args: emote_data:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data… (+4 more)

### Community 797 - "test_inventory_helpers.py"
Cohesion: 0.06
Nodes (39): match_room_drop_by_name(), Resolve a room drop index using Lovecraftian-grade fuzzy matching heuristics.…, Unit tests for inventory command helper functions. Tests helper functions used…, Test _format_metadata with None., Test format_metadata with empty dict., Test format_metadata with simple metadata., Test _normalize_slot_name with None., Test format_metadata with complex metadata. (+31 more)

### Community 798 - "channels.ts"
Cohesion: 0.10
Nodes (31): ChannelActivityIndicators(), ChannelActivityIndicatorsProps, getActivityColor(), ChannelSelectorSection(), ChannelSelectorSectionProps, ChatStatistics(), ChatStatisticsProps, ChatPanelRefactored() (+23 more)

### Community 799 - "CoordinateValidator"
Cohesion: 0.14
Nodes (14): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:…, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate…, _zone_pattern() (+6 more)

### Community 800 - "fixtures/shared/__init__.py"
Cohesion: 0.13
Nodes (15): fake_clock(), make_player_dict(), make_user_dict(), Any, fixture, Shared fixtures and builders for all test tiers., Create a user dictionary for testing., Create a player dictionary for testing. (+7 more)

### Community 801 - "optimized_comprehensive_sanitize_input"
Cohesion: 0.25
Nodes (8): Test comprehensive sanitization of empty string., Test comprehensive sanitization of normal text., Test that optimized comprehensive sanitization normalizes newlines to spaces., test_optimized_comprehensive_sanitize_input_empty(), test_optimized_comprehensive_sanitize_input_normal(), test_optimized_comprehensive_sanitize_input_normalizes_newlines(), optimized_comprehensive_sanitize_input(), Optimized comprehensive input sanitization. Args: text: Raw input text to…

### Community 802 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 803 - "CRITICAL SERVER MANAGEMENT RULES"
Cohesion: 0.29
Nodes (6): CRITICAL SERVER MANAGEMENT RULES, Implications, MANDATORY SERVER STARTUP PROCEDURE, ONE SERVER ONLY RULE, PRE-COMMAND CHECKLIST, Server Authority (Critical)

### Community 804 - "Test Coverage Requirements"
Cohesion: 0.29
Nodes (6): Coverage Measurement, Forbidden Test Patterns, Minimum Coverage Standard, Required Test Patterns, Test Coverage Requirements, Test Quality Standards

### Community 805 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 806 - "properties"
Cohesion: 0.18
Nodes (11): description, type, description, type, description, minimum, type, combat_modifier (+3 more)

### Community 807 - "room_validator/tests/conftest.py"
Cohesion: 0.15
Nodes (18): dead_end_room(), invalid_room_data(), fixture, Pytest configuration and fixtures for room validator tests. Provides test data…, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit. (+10 more)

### Community 808 - "Dependency Upgrade"
Cohesion: 0.29
Nodes (6): Before starting, Dependency Upgrade, Never, Rollback, Upgrade procedure, Verify

### Community 809 - "Animate Skill"
Cohesion: 0.11
Nodes (18): Animate Skill, Accessibility, Assess Animation Opportunities, CSS Animations, Delight Moments, Entrance Animations, Feedback & Guidance, Implement Animations (+10 more)

### Community 810 - "Polish Systematically"
Cohesion: 0.11
Nodes (18): Polish Skill, Code Quality, Color & Contrast, Content & Copy, Edge Cases & Error States, Final Verification, Forms & Inputs, Icons & Images (+10 more)

### Community 811 - "overrides"
Cohesion: 0.11
Nodes (18): overrides, @asyncapi/generator, @asyncapi/generator-components, @asyncapi/generator-helpers, @asyncapi/specs, fast-uri, flatted, glob (+10 more)

### Community 812 - "ContainerTransferToMixin"
Cohesion: 0.20
Nodes (14): ContainerTransferToMixin, ContainerComponent, InventoryStack, Player, UUID, Best-effort audit log for transfer-to-container (must not fail the transfer)., Add a stack via InventoryService; map capacity failures to…, Load player or raise ValidationError for transfer ops. (+6 more)

### Community 813 - "Communities (10 total, 2 thin omitted)"
Cohesion: 0.11
Nodes (17): Communities (10 total, 2 thin omitted), Community 0 - "Azotottal (fallen angel beyond the stars) / Captain Louis Malon", Community 1 - "Charenton (Paris district / asylum) / Christophe Pressi — Soldat (Soldier), age 20", Community 2 - "Dreamlands / Fenalik's Mansion (Poissy)", Community 3 - "Reign of Terror / Call of Cthulhu 7th Edition", Community 4 - "Bastille / James Coquillat", Community 5 - "Azathoth / Celine Bessette", Community 6 - "Christophe Pressi / Comte Benoit" (+9 more)

### Community 814 - "Git Workflow"
Cohesion: 0.29
Nodes (6): Branching, Commit messages, Git Workflow, History hygiene, Never, Repository hygiene

### Community 815 - "Gladiator Ring (Arena) Implementation Plan"
Cohesion: 0.11
Nodes (16): Gladiator Ring (Arena) — Implementation Todos, Phase 1: Schema and world data (Codebase Explorer for DML/schema pattern discovery) — DONE, Phase 2: Tutorial exit and respawn (main agent), Phase 3: NPC startup — also spawn in arena (main agent) — DONE, Phase 4: Tests and validation (main agent / Test Suite Analyzer) — DONE, Plan frontmatter todos (for Cursor plan file), Subagent usage, Todos (detailed) (+8 more)

### Community 816 - "Game Subsystem Design Documents"
Cohesion: 0.13
Nodes (18): Linkdead Grace Period, Gunicorn + Uvicorn Production, HTTPS and WSS Requirement, Disconnect Grace Period (linkdead), Login Grace Period (warded), WebSocket JWT in URL Query String, Item System Observability Runbook, Game Subsystem Design Documents (+10 more)

### Community 817 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 818 - "properties"
Cohesion: 0.20
Nodes (10): properties, minLength, pattern, type, minLength, type, type, id (+2 more)

### Community 819 - "bench_cache_professions.py"
Cohesion: 0.31
Nodes (7): bench_profession_cache(), _FakePersistence, _get_empty_dict(), main(), Any, Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…, Helper function to return empty dict for mock methods.

### Community 820 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.17
Nodes (17): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+9 more)

### Community 821 - "init_npc_database.py"
Cohesion: 0.16
Nodes (17): _determine_database_init_flags(), get_npc_database_url(), get_npc_seed_data_from_postgresql(), init_database_schema(), _initialize_database_with_url(), main(), populate_npc_data(), _print_final_message() (+9 more)

### Community 822 - "._create_tracked_task"
Cohesion: 0.10
Nodes (12): BaseException, Task, Handle NATS connection errors with state machine tracking. AI: Errors may…, Async handler for NATS connection errors., Handle NATS disconnection events with state machine tracking. AI: Disconnection…, Async handler for NATS disconnection events., Handle NATS reconnection events with state machine tracking. AI: Successful…, Async handler for NATS reconnection events. (+4 more)

### Community 823 - "TestCommandNormalization"
Cohesion: 0.09
Nodes (12): Test command normalization functions., Test clean_command_input() with normal command., Test clean_command_input() collapses multiple spaces., Test clean_command_input() strips leading/trailing whitespace., Test clean_command_input() handles tabs., Test normalize_command() with no slash prefix., Test normalize_command() removes slash prefix., Test normalize_command() with empty string. (+4 more)

### Community 824 - "asyncio"
Cohesion: 0.12
Nodes (21): Send event to all active websockets for a player. Args: player_id: The player's…, _send_to_websockets(), asyncio, Test handle_new_login_impl() handles new login., New login must cancel /rest countdown so it cannot kill the new session., Test broadcast_room_event_impl() broadcasts room event., Test _send_to_websockets() handles websocket errors., Test _send_to_websockets() handles None websocket. (+13 more)

### Community 825 - "Path"
Cohesion: 0.07
Nodes (27): Get the alias storage from the request context., alias_storage(), fixture, Path, Load/save re-check before open: attack names never open files outside storage., Create a temporary directory for alias storage., Create an AliasStorage instance with temporary directory., Create a sample alias for testing. (+19 more)

### Community 826 - "CombatValidator"
Cohesion: 0.08
Nodes (18): When party_service is None, validate_can_attack_target allows attack., When both players are in same party, validate_can_attack_target blocks attack., When players are not in same party, validate_can_attack_target allows attack., test_validate_can_attack_target_different_party_allows(), test_validate_can_attack_target_no_party_service_allows(), test_validate_can_attack_target_same_party_blocks(), CombatValidator, Enhanced combat command validator with thematic error messages. Provides… (+10 more)

### Community 827 - "HealthMonitor"
Cohesion: 0.14
Nodes (13): HealthMonitor, UUID, Find player_id for cleanup when metadata is missing., Check if connection is stale based on timeout., Check if WebSocket is actually open., Validate token and update last validation time if needed., Process health check for a single connection., Clean up stale connections. (+5 more)

### Community 828 - "persistence/container_helpers.py"
Cohesion: 0.14
Nodes (19): Composed, build_update_query(), _coerce_row_quantity(), fetch_container_items(), _item_dict_from_contents_row(), _metadata_dict_from_cell(), datetime, PsycopgConnection (+11 more)

### Community 829 - "enum"
Cohesion: 0.29
Nodes (7): description, enum, type, indoors, outdoors, underwater, environment

### Community 830 - "properties"
Cohesion: 0.25
Nodes (8): description, enum, type, indoors, outdoors, underwater, properties, environment

### Community 832 - "CircuitBreaker"
Cohesion: 0.10
Nodes (15): _CircuitBreakerResult, CircuitBreaker, Simple circuit breaker pattern implementation. Provides fault tolerance for…, Execute function with circuit breaker protection. Args: func: Function to…, Handle successful operation., Handle failed operation., Check if circuit breaker should attempt reset., Test CircuitBreaker class. (+7 more)

### Community 833 - "items"
Cohesion: 0.33
Nodes (6): additionalProperties, properties, schedules, items, minItems, type

### Community 834 - "container"
Cohesion: 0.33
Nodes (6): enabled, additionalProperties, description, required, type, container

### Community 835 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 836 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 837 - "Introduce Color Strategically"
Cohesion: 0.12
Nodes (17): Colorize Skill, Accent Color Application, Accessibility, Assess Color Opportunity, Background & Surfaces, Balance & Refinement, Borders & Accents, Cohesion (+9 more)

### Community 838 - "UX Writing"
Cohesion: 0.12
Nodes (16): Avoid Redundant Copy, Confirmation Dialogs: Use Sparingly, Consistency: The Terminology Problem, Don't Blame the User, Empty States Are Opportunities, Error Message Templates, Error Messages: The Formula, Form Instructions (+8 more)

### Community 839 - "rules"
Cohesion: 0.08
Nodes (25): entry, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries, dependencies (+17 more)

### Community 840 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 841 - "hash_password"
Cohesion: 0.10
Nodes (19): hash_password(), Validate password input before Argon2 hashing., Hash a plaintext password using Argon2id. This function provides superior…, _validate_password_for_hashing(), Hash password using Argon2 instead of bcrypt., Test hashing password with non-string type raises AuthenticationError., Test successful password hashing., Test hash_password handles HashingError. (+11 more)

### Community 842 - "whisper-movement.spec.ts"
Cohesion: 0.19
Nodes (14): assertNeitherPlayerInVoid(), attemptEastHop(), bringFrontAndAssertPlayerBanner(), deliverWhisperAcrossRooms(), focusCommandInput(), hopEastUntilHallway(), lookAndWaitForUi(), moveAwToEasternHallway() (+6 more)

### Community 843 - "intersection_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 844 - "room_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 845 - "create_app"
Cohesion: 0.17
Nodes (14): main(), Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., _sanitize_token_examples(), create_app(), FastAPI, Mount all versioned API routers under /v1., Create and configure the FastAPI application. This function sets up the FastAPI… (+6 more)

### Community 846 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)"
Cohesion: 0.12
Nodes (16): Communities (9 total, 4 thin omitted), Community 0 - "De Vermiis Mysteriis; Dust of Ibn-Ghazi", Community 1 - "Character Creation", Community 2 - "Alone Against the Flame", Community 3 - "Cover Art", Community 4 - "Azathoth; Banishment Chant (Latin)", Community Hubs (Navigation), Corpus Check (+8 more)

### Community 847 - "Cosmic Horror.md"
Cohesion: 0.13
Nodes (9): Chaosium catalog notes, Cosmic Horror, Evocations of the Inner God, Lucidity, Pandora's Box (Pulp campaign), Pulp Sanity, The Hungry Void, Using Luck (Pulp) (+1 more)

### Community 848 - "applies_to"
Cohesion: 0.28
Nodes (9): items, minItems, type, uniqueItems, items, items, minLength, type (+1 more)

### Community 849 - "ADR-003 Dual Event Systems EventBus NATS"
Cohesion: 0.13
Nodes (17): FastAPI-Generated OpenAPI 3.1, API OpenAPI Specification, ADR-001 Layered Architecture Event-Driven, ADR-002 ApplicationContainer DI, ADR-003 Dual Event Systems EventBus NATS, In-Process EventBus, NATS Distributed Messaging, ADR-004 WebSocket-Only Realtime (+9 more)

### Community 850 - "✅ Async Remediation Complete"
Cohesion: 0.12
Nodes (16): Adjusts spectacles with scholarly satisfaction, ✅ Async Remediation Complete, Critical Fixes Implemented (4 Code Changes), December 3, 2025, Documentation Created (5 Documents, ~2,500 lines), 📚 Key Documents, 🎓 Key Takeaway, Mission Accomplished (+8 more)

### Community 851 - "Phase 2 Async Persistence Migration - Status Update"
Cohesion: 0.12
Nodes (16): adjusts spectacles and awaits instruction, Awaiting Your Direction, Professor Wolfshade, ✅ Completed Today, Critical Phase 1 Fixes (100% Complete), 🚦 Current Status, 🎯 Decision Point, 📊 Effort Analysis, My Recommendation (+8 more)

### Community 852 - "Quick Start: Running E2E Tests"
Cohesion: 0.12
Nodes (16): Expected Results, Method A: Use the E2E startup script (Simplest), Method B: Manual startup (More control), Next Actions, Prerequisites ✅, Problem: "element(s) not found" errors, Problem: Login failed (500), Problem: Server won't start (+8 more)

### Community 853 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 854 - "CircuitBreaker"
Cohesion: 0.06
Nodes (60): CircuitBreaker, CircuitState, Enum, Circuit breaker pattern for NATS message processing. Implements three-state…, Circuit breaker states. - CLOSED: Normal operation, requests pass through -…, Get current circuit state. Returns: Current CircuitState AI: For monitoring and…, Manually reset circuit breaker to CLOSED state. Clears all counters and timers.…, Circuit breaker for NATS message processing. Implements Martin Fowler's circuit… (+52 more)

### Community 855 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 856 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 857 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 858 - "fix_file"
Cohesion: 0.18
Nodes (16): fix_blanks_around_fences(), fix_blanks_around_headings(), fix_blanks_around_lists(), fix_fence_language(), fix_file(), fix_line_length(), fix_trailing_punctuation_in_headings(), main() (+8 more)

### Community 859 - "jackson_linter.py"
Cohesion: 0.20
Nodes (16): collect_json_files(), _file_appears_binary_or_terminal_output(), _first_fallback_encoding_that_parses(), _is_vscode_jsonc_settings(), main(), Path, Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1…, VS Code allows JSON with Comments in settings.json; stdlib json cannot parse it. (+8 more)

### Community 860 - "RoomFilenameMigrator"
Cohesion: 0.19
Nodes (10): main(), Path, Update the room ID in the JSON file to match new naming schema., Execute the migration., Handles migration of room filenames from old to new schema., Initialize the migrator., Parse old filename format to extract components., Discover all room files that need migration. (+2 more)

### Community 861 - "rest_countdown_task.py"
Cohesion: 0.24
Nodes (14): create_rest_countdown_task(), _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, Task, UUID, Rest countdown task implementation. This module contains the async task that… (+6 more)

### Community 862 - "test_zone_config_loader.py"
Cohesion: 0.13
Nodes (19): parse_json_field(), Parse a JSON field from database, handling both dict/list and string formats.…, Unit tests for zone configuration loader. Tests the zone_config_loader module…, Test load_zone_configurations() loads configurations., Test load_zone_configurations() merges zone and subzone configs., Test parse_json_field() returns default when None., Test load_zone_configurations() raises RuntimeError on failure., Test parse_json_field() parses JSON string. (+11 more)

### Community 863 - "match_inventory_item_by_name"
Cohesion: 0.08
Nodes (27): match_exact_drop(), match_inventory_item_by_name(), Resolve an inventory index from a fuzzy name search. Human scholars: this…, Match by exact identifier (item_name, item_id, or prototype_id)., Unit tests for inventory command helper functions. Tests the helper functions…, Test match_room_drop_by_name() finds exact match., Test match_room_drop_by_name() returns None when not found., Test match_inventory_item_by_name() finds exact match. (+19 more)

### Community 864 - "test_party_flow.py"
Cohesion: 0.19
Nodes (13): event_bus(), party_events(), party_service(), asyncio, fixture, Integration tests for party (ephemeral grouping) feature. Flow: Two players;…, When leader leaves, party is disbanded and disbanded event is emitted., Real EventBus for integration. (+5 more)

### Community 865 - "TestFeatureFlagService"
Cohesion: 0.08
Nodes (13): Test is_combat_monitoring_enabled returns False when disabled., Test get_combat_configuration returns all combat settings., Test validate_combat_requirements returns True with valid configuration., Test suite for FeatureFlagService class., Test validate_combat_requirements returns False with invalid tick interval., Test FeatureFlagService initialization., Test get_feature_status returns complete feature status., Test check_combat_availability returns False when combat is disabled. (+5 more)

### Community 867 - "MythosMUDError"
Cohesion: 0.02
Nodes (219): JSONResponse, Error handlers package for MythosMUD. This package provides specialized error…, Pydantic error handler for consistent error processing. This module provides a…, _contains_file_path_in_exception(), _contains_sensitive_exception_pattern(), create_standardized_error_response(), handle_api_error(), Any (+211 more)

### Community 868 - "AttributeError"
Cohesion: 0.05
Nodes (40): AttributeError, Test _create_player_occupant_info handles grace period check exceptions., test_create_player_occupant_info_grace_period_exception(), Test get_npc_instances() handles exception from get_stats., test_get_npc_instances_get_stats_exception(), asyncio, Test _process_room_update_with_validation() processes valid room data., Test _process_room_update_with_validation() fixes invalid room data. (+32 more)

### Community 869 - "PrototypeRegistry"
Cohesion: 0.15
Nodes (20): PrototypeRegistry, Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, In-memory registry for validated item prototypes., Load prototypes from a directory of JSON files., _make_prototype() (+12 more)

### Community 870 - "test_instance_manager.py"
Cohesion: 0.09
Nodes (22): instance_manager(), fixture, Unit tests for InstanceManager. Tests instance creation, destruction, room…, Test get_exit_room_id returns fixed exit room., Test get_room_by_id returns None for non-instance room IDs., Test get_room_by_id returns room when room is in an instance., Create tutorial bedroom template room., Room cache with tutorial template. (+14 more)

### Community 871 - "Any"
Cohesion: 0.11
Nodes (13): Any, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string…, Evaluate boolean conditions and variable lookups. Args: condition: Condition…, Evaluate a condition string against context. Args: condition: Condition string… (+5 more)

### Community 872 - "test_player_spell_repository.py"
Cohesion: 0.27
Nodes (16): _mock_session_with_rows(), asyncio, fixture, Unit tests for PlayerSpellRepository., repo(), _spell_row(), test_get_player_spell_found(), test_get_player_spell_missing() (+8 more)

### Community 873 - "test_time_commands.py"
Cohesion: 0.21
Nodes (12): asyncio, Unit tests for time command handlers. Tests the time command functionality., Test handle_time_command() handles holiday service errors., Test handle_time_command() handles missing holiday service., Test handle_time_command() returns time information., Test handle_time_command() includes active holidays., Test handle_time_command() handles no active holidays., test_handle_time_command_holiday_service_error() (+4 more)

### Community 874 - "test_nats_message_handler_chat.py"
Cohesion: 0.11
Nodes (17): Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _extract_chat_message_fields extracts fields., Chat WebSocket event carries speaker_kind for client pass-through., Test _convert_ids_to_uuids handles UUID objects., Test _should_echo_to_sender returns False when message_id is None., Test _should_echo_to_sender returns True when targets exist. (+9 more)

### Community 875 - "optimized_validate_security_comprehensive"
Cohesion: 0.20
Nodes (10): Test comprehensive security validation of empty string., Test comprehensive security validation of valid text., Test comprehensive security validation with dangerous characters., Test comprehensive security validation with injection pattern., test_optimized_validate_security_comprehensive_dangerous_chars(), test_optimized_validate_security_comprehensive_empty(), test_optimized_validate_security_comprehensive_injection(), test_optimized_validate_security_comprehensive_valid() (+2 more)

### Community 876 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 877 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 878 - "CommunicationIntegrationProtocol"
Cohesion: 0.14
Nodes (10): CombatIntegrationProtocol, CommunicationIntegrationProtocol, Protocol, Protocols for NPC combat and communication integration (used by NPCBase)., Handle NPC death in the combat integration layer., Protocol for communication integration (whisper, room message, handle player…, Send a private whisper from this NPC to a single player., Send a message from this NPC to all players in a room. (+2 more)

### Community 879 - "Codebase Explorer Subagent"
Cohesion: 0.14
Nodes (15): Architecture Analysis, Best Practices, Capabilities, Codebase Explorer Subagent, Dependency Research, Example Scenarios, Finding All Implementations, Integration (+7 more)

### Community 880 - "Adapt Skill"
Cohesion: 0.12
Nodes (16): Adapt Skill, Assess Adaptation Challenge, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Techniques, MANDATORY PREPARATION (+8 more)

### Community 881 - "Improve Copy Systematically"
Cohesion: 0.12
Nodes (16): Clarify Skill, Apply Clarity Principles, Assess Current Copy, Button & CTA Text, Confirmation Dialogs, Empty States, Error Messages, Form Labels & Instructions (+8 more)

### Community 882 - "Color & Contrast"
Cohesion: 0.12
Nodes (15): Alpha Is A Design Smell, Building Functional Palettes, Color & Contrast, Color Spaces: Use OKLCH, Contrast & Accessibility, Dangerous Color Combinations, Dark Mode Is Not Inverted Light Mode, Never Use Pure Gray or Pure Black (+7 more)

### Community 883 - "AlertType"
Cohesion: 0.10
Nodes (25): AlertSeverity, AlertType, Enum, Alert severity levels., Alert types for combat monitoring., Test get_active_alerts returns unresolved alerts., Test get_all_alerts returns all alerts., Test resolve_alert resolves an alert. (+17 more)

### Community 884 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)"
Cohesion: 0.12
Nodes (15): Communities (17 total, 12 thin omitted), Community 0 - "Character and Skills", Community 1 - "Character and Skills (1)", Community 2 - "Core Rules", Community 3 - "Core Rules (3)", Community 4 - "Character Sheets", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 885 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (12 total, 7 thin omitted), Community 0 - "Call of Cthulhu (7th Edition); Chaosium Inc.", Community 1 - "APP; Characteristics", Community 2 - "Everett Scanlon; Gustavo Romero", Community 3 - "First Aid; Hit Points", Community 4 - "Formless Spawn of Tsathoggua; Rudolf Zimmer", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 886 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (5 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Bernard Corbitt; Randolph Tomaszewski", Community 2 - "Ramasekva; Yog-Sothoth", Community 3 - "Arthur Cornthwaite; Fitzgerald Manse", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions) (+7 more)

### Community 887 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (10 total, 4 thin omitted), Community 0 - "Azathoth / Byakhee", Community 1 - "Call of Cthulhu / Chaosium Inc.", Community 2 - "Dimensional Shambler / Elder Thing", Community 3 - "Abhoth / Atlach-Nacha", Community 4 - "Deep One / Ghast", Community 5 - "Dark Young / Dark Young of Shub-Niggurath", Community Hubs (Navigation) (+7 more)

### Community 888 - "Async Persistence Migration Tracker"
Cohesion: 0.12
Nodes (15): Async Persistence Migration Tracker, Current Status, Decision Tree, Files Requiring Migration, Migration Pattern, Migration Strategy, Overview, Phase 1: High Priority (✅ COMPLETE) (+7 more)

### Community 889 - "Migration 019: Ready for Deployment"
Cohesion: 0.12
Nodes (15): Application Script, Database Schema, Documentation, Files Ready, Implementation Complete, Migration 019: Ready for Deployment, Migration Script, Next Action (+7 more)

### Community 890 - ".connection_manager"
Cohesion: 0.12
Nodes (14): Check connection state before publishing combat ended event., CombatMessagingBase, Any, setter, Base class with connection manager setup. Used by CombatMessagingIntegration., Lazily resolve the connection manager from the application container., Return the connection manager, resolving it from the application container if…, Explicitly set the connection manager (primarily used in tests). (+6 more)

### Community 891 - "ExperienceRepository"
Cohesion: 0.06
Nodes (45): GameMechanicsService, Any, Heal a player's health., Damage a player's health., Award experience points to a player. CRITICAL FIX: This method prevents XP…, Service class for game mechanics operations., Initialize the game mechanics service with a persistence layer., Apply lucidity loss to a player. (+37 more)

### Community 892 - "Frontend Design Skill"
Cohesion: 0.13
Nodes (16): Tailwind CSS Anti-Pattern Remediation, Adapt Skill, Animate Skill, Arrange Skill, Audit Skill, Bolder Skill, Clarify Skill, Colorize Skill (+8 more)

### Community 893 - "holiday.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 894 - "schedule.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 895 - "analyze_coverage_gaps.py"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and…, Write critical files below threshold section. (+7 more)

### Community 896 - "_apply_arena_seed_patch.py"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 897 - "test_command_service.py"
Cohesion: 0.06
Nodes (31): Unit tests for command service. Tests the CommandService class which handles…, Test _parse_command_string successfully parses command., Test _parse_command_string handles subcommands., Test _parse_command_string handles unexpected errors., Test _prepare_command_data creates basic command_data dict., Test _prepare_command_data includes pipe_target if present., Test _extract_parsed_fields extracts basic fields., Test _extract_parsed_fields includes pipe_target. (+23 more)

### Community 898 - "generate_sql.mjs"
Cohesion: 0.30
Nodes (15): ajv, __dirname, ensureDir(), __filename, generateEmotes(), generateHolidays(), generateNpcSchedules(), generateRooms() (+7 more)

### Community 899 - "PostgreSQL database names (MythosMUD)"
Cohesion: 0.40
Nodes (4): CRITICAL: Which databases may be reset, Database placement (production vs test), Enforcement, PostgreSQL database names (MythosMUD)

### Community 900 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 901 - "MockEventClass"
Cohesion: 0.10
Nodes (20): MockEventClass, Test EventBus.inject() delivers event to subscribers (used by distributed…, Mock event class for testing., Test _handle_event_async() when no subscribers., Test _handle_event_async() handles sync subscriber errors., Test _handle_event_async() handles async subscriber errors., Test _handle_task_result_async() with successful task., Test _handle_task_result_async() with task that raises error. (+12 more)

### Community 902 - "test_alias_expansion.py"
Cohesion: 0.18
Nodes (18): check_alias_safety(), handle_expanded_command(), Any, CommandExecutionRequest, Handle command processing with alias expansion and loop detection. This…, Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:…, validate_expanded_command() (+10 more)

### Community 903 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 904 - ".get_player_aliases"
Cohesion: 0.09
Nodes (14): AliasRecord, _apply_alias_timestamps(), _as_alias_record(), Get all aliases for a player., Save aliases for a player., Add or update an alias for a player., Remove an alias for a player., Get a specific alias for a player. (+6 more)

### Community 905 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 906 - "item_prototype.schema.json"
Cohesion: 0.40
Nodes (4): additionalProperties, $schema, title, type

### Community 907 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 908 - "test_invite.py"
Cohesion: 0.10
Nodes (19): Unit tests for the Invite model. Tests the Invite model methods including…, Test is_expired returns False for future expiry date., Test __repr__ returns expected string format., Test is_expired returns True for past expiry date., Test is_expired handles timezone-aware datetime., Test is_valid returns True for active, non-expired invite., Test is_valid returns False for inactive invite., Test is_valid returns False for expired invite. (+11 more)

### Community 909 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 910 - "test_message_builders.py"
Cohesion: 0.14
Nodes (18): _builder(), Unit tests for MessageBuilder., Sequence counter callable is invoked., Non-callable sequence counter returns 0., Player entered message includes ids and player name., Player left message includes ids and player name., NPC movement messages cover direction and movement type branches., Occupants update includes structured and legacy fields. (+10 more)

### Community 911 - "CommandService"
Cohesion: 0.13
Nodes (13): CommandService, Command, Main command processing service for MythosMUD. This service handles command…, Initialize the command service., Parse and validate command string. Returns: tuple of (parsed_command, cmd,…, Prepare command_data dictionary by merging parsed command fields. Returns:…, Extract non-private, non-callable attributes from parsed_command, excluding…, Extract fields from parsed_command using model_dump or fallback method.… (+5 more)

### Community 912 - "test_inventory_command_prototype.py"
Cohesion: 0.12
Nodes (26): _first_normalized_wear_slot(), infer_equip_slot_from_prototype(), _inventory_prototype_id(), prototype_from_registry(), prototype_registry_from_request(), Prototype registry access and equip-slot inference for inventory items., Resolve prototype registry from FastAPI-style request (agent-readable…, Return the prototype object for ``prototype_id``, or None if missing or invalid. (+18 more)

### Community 913 - "test_profession_service.py"
Cohesion: 0.25
Nodes (13): persistence(), _profession(), asyncio, fixture, Unit tests for ProfessionService., service(), test_get_all_professions_dict(), test_get_profession_by_id_dict_found() (+5 more)

### Community 914 - "test_lifecycle_respawn.py"
Cohesion: 0.18
Nodes (26): Process the respawn queue and spawn NPCs that are ready (delegates to…, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…, Process the respawn queue and spawn NPCs that are ready. Args: manager:… (+18 more)

### Community 915 - "PhantomHostileService"
Cohesion: 0.07
Nodes (35): FakeHallucinationService, Select which type of fake hallucination to trigger (50/50 chance). Returns:…, Service for generating fake NPC tells and room text overlays. These…, Initialize the fake hallucination service., Send a hallucination event to a player., send_hallucination_event(), handle_fake_hallucination(), handle_hallucination_triggers() (+27 more)

### Community 916 - "TestValidatorIntegration"
Cohesion: 0.14
Nodes (8): Integration tests for the main validator., Test validator with valid room files., Test validator with invalid room files., Test validator JSON output format., Test validator zone filtering., Test that help text is properly displayed., Test schema-only validation flag., TestValidatorIntegration

### Community 917 - "LoggingConfig"
Cohesion: 0.18
Nodes (8): LoggingConfig, Any, BaseSettings, field_validator, Validate admin password strength (production only)., Logging configuration., Validate logging environment., Convert to legacy logging config dict format for backward compatibility.…

### Community 918 - "test_check_no_production_assert.py"
Cohesion: 0.18
Nodes (15): _load_checker(), _NoProductionAssertModule, Path, Protocol, Tests for scripts/check_no_production_assert.py., Verify no-production-assert hook targets server code and excludes tests., Public surface of check_no_production_assert loaded via importlib., test_find_assert_line_numbers_detects_assert() (+7 more)

### Community 919 - "fixture"
Cohesion: 0.12
Nodes (17): async_session_factory(), lucidity_service_factory(), mock_event_dispatcher(), mock_lucidity_service(), mock_persistence(), mock_session(), fixture, Create a mock persistence layer. (+9 more)

### Community 920 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test get_room_occupants() returns occupants., Test get_room_occupants() returns empty list when no occupants., Test get_room_occupants() handles errors gracefully., Test get_room_subscribers() returns subscribers., test_get_room_occupants() (+5 more)

### Community 921 - "Spatial Design"
Cohesion: 0.13
Nodes (14): Cards Are Not Required, Container Queries, Depth & Elevation, Grid Systems, Hierarchy Through Multiple Dimensions, Name Tokens Semantically, Optical Adjustments, Spacing Systems (+6 more)

### Community 922 - "Typography"
Cohesion: 0.13
Nodes (14): Accessibility Considerations, Choosing Distinctive Fonts, Classic Typography Principles, Fluid Type, Font Selection & Pairing, Modern Web Typography, Modular Scale & Hierarchy, OpenType Features (+6 more)

### Community 923 - "MythosMUD Code Quality Targets for AI"
Cohesion: 0.13
Nodes (15): Code Quality AI Skill, `__all__` for public modules, As You Touch, Client return types (TypeScript), Complexity policy, Docstrings (D), High Priority, Medium Priority (+7 more)

### Community 924 - "Skill: Create a New Worktree for a Task"
Cohesion: 0.13
Nodes (15): Worktree Workflow Skill, Canonical Layout (Summary), MythosMUD Worktree Workflow, Preconditions and Safety, Skill: Clean Up a Completed or Stale Worktree, Skill: Create a New Worktree for a Task, Step 1 — Gather Task Metadata, Step 2 — Derive Names and Paths (+7 more)

### Community 925 - "RoomInfo.tsx"
Cohesion: 0.29
Nodes (13): CompleteRoomInfo(), DebugInfo(), RoomDescription(), RoomEntities(), RoomExits(), RoomInfo(), RoomInfoContext, RoomInfoContextType (+5 more)

### Community 926 - "MessageBatcher"
Cohesion: 0.24
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 927 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)"
Cohesion: 0.13
Nodes (14): Communities (8 total, 5 thin omitted), Community 0 - "Baron Arthur von Kleist; Pyotr Shabelsky-Bork", Community 1 - "The Demon-Großmann; Demonic Mutation Table", Community 2 - "Erwin Kern; Manfred Freiherr von Killinger", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11) (+6 more)

### Community 928 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Anna Konrad; Lucas Reston", Community 2 - "Does Love Forgive", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12) (+6 more)

### Community 929 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Pre-Generated Investigators", Community 1 - "Pre-Generated Investigators (1)", Community 2 - "Pre-Generated Investigators (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12) (+6 more)

### Community 930 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 931 - "npc_schedules.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 932 - ".get_instance"
Cohesion: 0.16
Nodes (10): Get the singleton container instance., _merge_phase_into_startup(), _new_spawn_results(), Any, Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…, Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…, Second pass: spawn one instance per definition (that was spawned in…, Determine the appropriate room for spawning an NPC. Args: npc_def: NPC… (+2 more)

### Community 933 - "fix_markdown_common_issues.py"
Cohesion: 0.22
Nodes (14): fix_emphasis_as_heading(), fix_first_line_heading(), fix_link_fragments(), fix_markdown_file(), generate_anchor(), main(), parse_markdownlint_output(), Path (+6 more)

### Community 934 - "process_room_files"
Cohesion: 0.21
Nodes (14): load_room_file(), main(), process_room_files(), Path, Load a room file safely., Save a room file safely., Convert room ID to lowercase., Convert filename to lowercase. (+6 more)

### Community 935 - "validate_codacy_coverage_gate.py"
Cohesion: 0.25
Nodes (14): cobertura_has_server_sources(), cobertura_root_line_rate(), lcov_aggregate_hits(), main(), _parse_cobertura_xml(), Path, Parse Cobertura XML with defusedxml (lazy import: LCOV-only runs skip this…, Return root line-rate from Cobertura XML (0.0--1.0). (+6 more)

### Community 936 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 937 - "handle_teach_command"
Cohesion: 0.19
Nodes (21): _format_teach_result(), _get_teach_services(), handle_teach_command(), Any, Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, _resolve_npc_teacher(), asyncio, patch (+13 more)

### Community 938 - "TestValidateRoomData"
Cohesion: 0.15
Nodes (11): patch, Test validate_room_data() function., Test validate_room_data() returns empty list when validation not available., Test validate_room_data() with provided validator., Test validate_room_data() creates validator when not provided., Test validate_room_data() returns validation errors., Test validate_room_data() raises exception in strict mode with errors., Test validate_room_data() returns empty list when validator creation fails. (+3 more)

### Community 939 - "test_message_filtering_helpers.py"
Cohesion: 0.12
Nodes (16): message_filtering_helper(), mock_connection_manager(), fixture, Unit tests for message filtering helper functions. Tests the helper functions…, Create a mock connection manager., Create a MessageFilteringHelper instance., Test extract_chat_event_info() extracts event information., Test should_apply_mute_check() determines if mute check needed. (+8 more)

### Community 940 - "test_aggressive_mob_npc.py"
Cohesion: 0.25
Nodes (14): _make_aggro(), asyncio, Unit tests for AggressiveMobNPC. Regression test: aggressive mobs must have…, test_attack_target_error_returns_false(), test_attack_target_fallback_publishes_event(), test_attack_via_combat_integration_none_when_missing(), test_attack_via_create_task_with_running_loop(), test_attack_via_dropped_without_loop_or_bus() (+6 more)

### Community 941 - "test_argon2_utils.py"
Cohesion: 0.15
Nodes (18): PasswordHasher, create_hasher_with_params(), Create a PasswordHasher with custom parameters., Unit tests for Argon2 password hashing utilities., Test that create_hasher_with_params logs warning for low time_cost., Test that create_hasher_with_params logs warning for low memory_cost., Test creating hasher with valid parameters., Test creating hasher with invalid time_cost. (+10 more)

### Community 942 - "AsciiMapRenderer"
Cohesion: 0.14
Nodes (12): AsciiMapRenderer, Renders ASCII maps from room coordinate data. Supports multiple map styles…, Initialize the ASCII map renderer., Tests for _vertical_exit_char_between (|, v, ^)., Bidirectional vertical exit renders as a vertical bar., One-way south exit renders as a lowercase 'v'., One-way north exit renders as a caret., When there are no vertical exits, the helper returns None. (+4 more)

### Community 943 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 944 - "weather_patterns"
Cohesion: 0.40
Nodes (5): type, weather_patterns, description, items, type

### Community 945 - "Stats"
Cohesion: 0.12
Nodes (13): Any, Stats, Roll Size using formula: (2D6+6)*5 (range 40-90)., Roll stats using 3d6 method (scaled to 15-90 range)., Roll stats using 4d6 drop lowest method (more generous, scaled to 15-90 range)., Generate stats using a point-buy system (balanced, scaled to 1-100 range)., Check if stats meet the prerequisites for a given class. Args: stats: The…, Get a list of classes that the character qualifies for. Args: stats: The… (+5 more)

### Community 946 - "convert_uuids_to_strings"
Cohesion: 0.11
Nodes (23): convert_uuids_to_strings(), Recursively convert UUID objects to strings for JSON serialization. Args: obj:…, Test convert_uuids_to_strings() converts UUIDs in dict., Test convert_uuids_to_strings() converts UUIDs in list., Test convert_uuids_to_strings() converts UUID object., Test convert_uuids_to_strings() converts UUIDs in nested structures., test_convert_uuids_to_strings_dict(), test_convert_uuids_to_strings_list() (+15 more)

### Community 947 - "test_npc_population_api.py"
Cohesion: 0.20
Nodes (17): get_npc_population_stats(), get_npc_system_status(), get_npc_zone_stats(), get, Request, Get NPC population statistics., Get NPC zone statistics., Get NPC system status. (+9 more)

### Community 948 - "7. Common Test Failure Solutions"
Cohesion: 0.50
Nodes (4): 7. Common Test Failure Solutions, Authentication Test Issues, Database Connection Issues, WebSocket Test Issues

### Community 949 - "PlayerStateService"
Cohesion: 0.18
Nodes (11): PlayerStateService, Any, UUID, Gain occult knowledge (with lucidity loss). Args: player_id: The player's ID…, Heal a player's health. Args: player_id: The player's ID (UUID) amount: Amount…, Service for managing player state modifications., Damage a player's health. Args: player_id: The player's ID (UUID) amount:…, Initialize with a persistence layer. (+3 more)

### Community 950 - "Player"
Cohesion: 0.09
Nodes (12): Player, Save a player. Delegates to PlayerRepository., Save multiple players in a single transaction. Delegates to PlayerRepository., Validate and fix player room if needed. Delegates to PlayerRepository., Apply lucidity loss to a player. Delegates to ExperienceRepository., Apply fear to a player. Delegates to ExperienceRepository., Apply corruption to a player. Delegates to ExperienceRepository., Award experience to a player atomically. Delegates to ExperienceRepository. (+4 more)

### Community 951 - "10. Grace Period Persistence"
Cohesion: 0.50
Nodes (4): 10. Grace Period Persistence, Gap Analysis, Industry Practices, Our Plan

### Community 952 - "1. Disconnect Grace Period Duration"
Cohesion: 0.50
Nodes (4): 1. Disconnect Grace Period Duration, Gap Analysis, Industry Practices, Our Plan

### Community 953 - "_StubPlayerRepo"
Cohesion: 0.14
Nodes (4): UUID, _StubPlayerRepo, Retry decorator must not treat wrapped closed-connection as final on attempt 1., test_retry_retries_wrapped_connection_closed_then_succeeds()

### Community 954 - "2. Auto-Attack During Grace Period"
Cohesion: 0.50
Nodes (4): 2. Auto-Attack During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 955 - "3. Grace Period Visibility & Messaging"
Cohesion: 0.50
Nodes (4): 3. Grace Period Visibility & Messaging, Gap Analysis, Industry Practices, Our Plan

### Community 956 - "test_config_models.py"
Cohesion: 0.11
Nodes (20): BaseSettings, Server network configuration., ServerConfig, Unit tests for configuration models., Test DatabaseConfig pool config validation with positive values., Test DatabaseConfig pool config validation with invalid value., Test ServerConfig default host., Test ServerConfig port validation with valid port. (+12 more)

### Community 957 - "TrackedTaskManager"
Cohesion: 0.09
Nodes (27): memory_leak_prevention_channel_start_session(), patch_asyncio_create_task_with_tracking(), Audit and reclaim orphaned task candidates across the system. Returns: Number…, Proactively clean up orphaned tasks by cancelling leak prevention violations.…, Return count of currently tracked task references within the manager's…, Attach a TaskRegistry instance to this Tracker for shared coordination. Args:…, Central namespace for tracked task lifecycle coordination preventing orphaned…, Reset the global tracked manager for testing. (+19 more)

### Community 958 - "4. Rest/Quit Command During Combat"
Cohesion: 0.50
Nodes (4): 4. Rest/Quit Command During Combat, Gap Analysis, Industry Practices, Our Plan

### Community 959 - "Any"
Cohesion: 0.09
Nodes (12): Any, Set the instance manager for instanced room lookup (instance-first)., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests. (+4 more)

### Community 960 - "test_websocket_handler_error_handling.py"
Cohesion: 0.15
Nodes (13): mock_websocket(), asyncio, fixture, Unit tests for websocket handler error handling. Tests the error handling…, Create a mock WebSocket., Test _send_error_response() successfully sends error., Test _send_error_response() handles WebSocket disconnection., Test _handle_runtime_error() detects WebSocket disconnection. (+5 more)

### Community 961 - "5. Rest Command Countdown Duration"
Cohesion: 0.50
Nodes (4): 5. Rest Command Countdown Duration, Gap Analysis, Industry Practices, Our Plan

### Community 962 - "6. Rest Location (Inn/Hotel) Behavior"
Cohesion: 0.50
Nodes (4): 6. Rest Location (Inn/Hotel) Behavior, Gap Analysis, Industry Practices, Our Plan

### Community 963 - ".disconnect"
Cohesion: 0.12
Nodes (9): Drain in-flight messages from all subscriptions., Close and unsubscribe from all subscriptions., Verify all subscriptions were cleaned up and log warnings if any remain., Close NATS connection and transition to disconnected state., Disconnect from NATS with graceful shutdown and message draining. AI: State…, Cancel all tracked background tasks for proper cleanup. AnyIO Pattern:…, Stop health check monitoring task., Get list of all active NATS subscription subjects. Returns: List of subject… (+1 more)

### Community 964 - "test_skill_service.py"
Cohesion: 0.10
Nodes (28): asyncio, Unit tests for SkillService (get_skills_catalog, set_player_skills,…, get_skills_catalog returns list of skill dicts., get_player_skills for owned player returns list of skill dicts., get_player_skills for another user's player returns None., record_successful_skill_use delegates to repo.record_use with correct args., get_skills_used_this_level returns distinct skill_ids from repo., run_improvement_rolls with new_level 1 does nothing (previous level 0). (+20 more)

### Community 965 - "asyncio"
Cohesion: 0.13
Nodes (12): asyncio, Test _handle_special_command_routing function., Test _handle_special_command_routing handles alias management commands., Test _handle_special_command_routing returns error when alias storage…, Test _handle_special_command_routing converts single-word emotes., Test _process_alias_expansion function., Test _process_alias_expansion returns None when no alias storage., Test _process_alias_expansion returns None when alias not found. (+4 more)

### Community 966 - "handle_explore_command"
Cohesion: 0.27
Nodes (9): handle_explore_command(), Any, Handle exploration requests by returning a simple message. This lightweight…, asyncio, Unit tests for exploration command handlers. Tests the exploration command…, Test handle_explore_command() explores area., Test handle_explore_command() handles missing persistence., test_handle_explore_command() (+1 more)

### Community 967 - "7. Reconnection During Grace Period"
Cohesion: 0.50
Nodes (4): 7. Reconnection During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 968 - "optimized_security_validator.py"
Cohesion: 0.13
Nodes (15): Test benchmark function runs without errors., Test stripping ANSI codes from empty string., Test stripping ANSI codes from text without ANSI., Test stripping ANSI codes from text with ANSI., test_benchmark_validation_performance(), test_optimized_strip_ansi_codes_empty(), test_optimized_strip_ansi_codes_no_ansi(), test_optimized_strip_ansi_codes_with_ansi() (+7 more)

### Community 969 - "check_no_production_assert.py"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 970 - "Generate Comprehensive Report"
Cohesion: 0.14
Nodes (14): Audit Skill, Anti-Patterns Verdict, Critical Issues, Detailed Findings by Severity, Diagnostic Scan, Executive Summary, Generate Comprehensive Report, High-Severity Issues (+6 more)

### Community 971 - "Optimize Skill"
Cohesion: 0.14
Nodes (14): Optimize Skill, Animation Performance, Assess Performance Issues, Core Web Vitals Optimization, Cumulative Layout Shift (CLS < 0.1), First Input Delay (FID < 100ms) / INP (< 200ms), Largest Contentful Paint (LCP < 2.5s), Loading Performance (+6 more)

### Community 972 - "Test Server Remediation Prompt - Cursor Executable Version"
Cohesion: 0.14
Nodes (13): Best Practices, COMPLETION VERIFICATION, CRITICAL "DO NOT" INSTRUCTIONS, CRITICAL: EXECUTION REQUIREMENTS, DECISION TREE - START HERE, ERROR HANDLING PROTOCOL, MANDATORY PROGRESS TRACKING, MANDATORY VERIFICATION CHECKPOINTS (+5 more)

### Community 973 - "Arkham City (MOTD Zone)"
Cohesion: 0.18
Nodes (14): Arkham City Graph PNG, Arkham City PDF Map, Arkham City (MOTD Zone), Welcome to the Dreamlands, Innsmouth (MOTD Zone), Katmandu, MythosMUD Message of the Day, The Yellow Sign (+6 more)

### Community 974 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (16 total, 14 thin omitted), Community 0 - "Open Mind Circle", Community 1 - "Campaign Materials", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 975 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (6 total, 4 thin omitted), Community 0 - "Solo Investigators", Community 1 - "Design & Authorship", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 976 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (4 total, 1 thin omitted), Community 0 - "Keeper Screen References", Community 1 - "Keeper Screen References (1)", Community 2 - "Keeper Screen References (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12) (+5 more)

### Community 977 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (3 total, 0 thin omitted), Community 0 - "Call of Cthulhu Stat Block; Chaosium Inc.", Community 1 - "Mythos Elements", Community 2 - "Mythos Elements (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12) (+5 more)

### Community 978 - "Easy Coverage Wins - Quick Analysis"
Cohesion: 0.14
Nodes (13): Easy Coverage Wins - Quick Analysis, 🚀 Next Steps, Phase 1: Quick Wins (Tier 1 + Tier 2) ✅ COMPLETED, Phase 2: Medium Effort (Tier 3) ✅ COMPLETED, Phase 3: New Small Files (Tier 4) ✅ COMPLETED, Phase 4: Additional Realtime Files 🔄 IN PROGRESS, 📊 Recommended Priority Order, 🎉 Summary (+5 more)

### Community 979 - "Test Suite Quality Audit - Executive Summary"
Cohesion: 0.13
Nodes (15): **25-30% (~1,250-1,500 tests) provide CRITICAL regression protection**, Answer to Original Question, Breakdown, By Category, Comparison to Industry Benchmarks, Created Documents, Deliverables Summary, Key Findings (+7 more)

### Community 980 - "Test Value Distribution Chart"
Cohesion: 0.14
Nodes (13): Coverage vs Value Analysis, Declare Success When, Efficiency = Value per Second of Execution, Interpretation, Success Celebration Criteria, Target Quadrants, Test Execution Time Efficiency, Test Maintenance Burden (+5 more)

### Community 981 - "analyze_log_file"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 982 - "type"
Cohesion: 0.13
Nodes (16): items, type, items, type, uniqueItems, minLength, type, effect_components (+8 more)

### Community 983 - "find_fstring_logging_violations"
Cohesion: 0.20
Nodes (11): find_fstring_logging_violations(), format_violation_report(), FStringLoggingDetector, main(), Call, Path, Main function to scan files and report violations., AST visitor to detect f-string logging violations. (+3 more)

### Community 984 - "lint_sql_guardrails.py"
Cohesion: 0.23
Nodes (13): check_not_in_subquery(), check_select_star(), _collect_sql_files(), main(), Path, Lightweight guardrails for hand-maintained PostgreSQL SQL. Warns on: - select *…, Return line with line comment removed (-- ...)., Return content with block comments /* ... */ removed (simple, no nested). (+5 more)

### Community 985 - "test_cache_service.py"
Cohesion: 0.11
Nodes (16): CacheService, Cache service for MythosMUD server. This module provides caching services that…, Main cache service that coordinates all caching operations. This service…, Initialize the cache service. Args: persistence: Persistence layer instance…, Preload frequently accessed data into caches. This method loads commonly used…, Caching module for MythosMUD server. This module provides comprehensive caching…, get_cache_manager(), LRU Cache implementation for MythosMUD server. This module provides thread-safe… (+8 more)

### Community 987 - "._get_room_uuid_by_stable_id"
Cohesion: 0.17
Nodes (10): Any, AsyncSession, UUID, Get room UUID by stable_id (hierarchical room ID). Args: stable_id:…, Mark room as explored using the provided session. Args: session: Database…, Get list of room IDs that a player has explored. Args: player_id: UUID of the…, Check if a player has explored a specific room. Args: player_id: UUID of the…, Synchronous wrapper for mark_room_as_explored. This method is designed to be… (+2 more)

### Community 988 - "8. Grace Period After Intentional Disconnect"
Cohesion: 0.50
Nodes (4): 8. Grace Period After Intentional Disconnect, Gap Analysis, Industry Practices, Our Plan

### Community 989 - "9. Command Blocking During Grace Period"
Cohesion: 0.50
Nodes (4): 9. Command Blocking During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 990 - "Recommendations Summary"
Cohesion: 0.50
Nodes (4): High Priority Decisions, Low Priority (Future Considerations), Medium Priority Enhancements, Recommendations Summary

### Community 991 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 992 - "is_safe_filename"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters). Args:…, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 993 - "days"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, days

### Community 994 - "effects"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, effects

### Community 995 - "run_flee_effect"
Cohesion: 0.15
Nodes (28): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+20 more)

### Community 996 - "end_hour"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 997 - "test_player_repository.py"
Cohesion: 0.12
Nodes (15): Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes with room cache., Test PlayerRepository initializes with event bus., Test validate_and_fix_player_room returns False for valid room., Test validate_and_fix_player_room fixes invalid room., Test get_player_by_name returns None when player not found., Test list_players returns empty list when no players., Test PlayerRepository initializes correctly. (+7 more)

### Community 998 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 999 - "zone_config_loader.py"
Cohesion: 0.15
Nodes (18): parse_zone_special_rules(), process_subzone_rows(), Connection, Record, TypedDict, Zone Configuration Loader Module. This module handles loading zone and sub-zone…, Build and store one subzone configuration from a database row., Process subzone rows from database and populate subzone configurations. Args:… (+10 more)

### Community 1000 - "._ensure_room_cache_loaded"
Cohesion: 0.09
Nodes (11): Ensure room cache is loaded (lazy loading with lock). This method uses a lock…, Load rooms from PostgreSQL via RoomCacheLoader., Get a player by name. Delegates to PlayerRepository., Get a player by ID. Delegates to PlayerRepository., Get all players (including deleted) for a user ID. Delegates to…, Get active (non-deleted) players for a user ID. Delegates to PlayerRepository., Get the first active player by user ID (backward compatibility). Delegates to…, List all players. Delegates to PlayerRepository. (+3 more)

### Community 1001 - "_make_mock_row"
Cohesion: 0.13
Nodes (15): _make_mock_row(), UUID, Test get_player_by_name successfully retrieves player., Test list_players successfully retrieves players., Create a mock procedure result row for row_to_player., Test get_player_by_id successfully retrieves player., Test get_players_by_user_id successfully retrieves players., Test get_active_players_by_user_id successfully retrieves active players. (+7 more)

### Community 1002 - "_find_container_wearable"
Cohesion: 0.08
Nodes (24): _find_container_wearable(), Find a wearable container in equipped items by name or prototype_id. This…, Test _find_container_wearable() with empty dict., Test _find_container_wearable() with no matching containers., Test _find_container_wearable() with multiple matches (ambiguous)., Test _find_container_wearable() with instance number., Test _find_container_wearable() with instance number out of range., Test _find_container_wearable() finds wearable container. (+16 more)

### Community 1003 - "test_ascii_map_renderer_exits.py"
Cohesion: 0.17
Nodes (8): Unit tests for AsciiMapRenderer exit character and exit resolution. Guards…, Tests for _get_exit_entries_for_room., Valid exits for a room produce one entry with correct direction and coordinates., Exits whose targets are missing are skipped when building exit entries., Viewport bounds: return None when next cell is outside viewport., Returns None when the next horizontal cell lies at or beyond the viewport's…, TestGetExitEntriesForRoom, TestGetHorizontalExitCharViewportBounds

### Community 1004 - "_parse_env_list"
Cohesion: 0.14
Nodes (14): _parse_env_list(), _parse_list_from_string(), Parse non-empty string as JSON list or CSV. Used by _parse_env_list., Parse a string from the environment as JSON list or CSV., test_parse_env_list_empty_and_none(), test_parse_list_from_string_json_and_csv(), Test parsing None as env list., Test parsing empty string as env list. (+6 more)

### Community 1005 - "exits"
Cohesion: 0.50
Nodes (4): type, additionalProperties, type, exits

### Community 1006 - "test_magic_commands.py"
Cohesion: 0.17
Nodes (11): Unit tests for magic commands. Tests the /cast, /spells, /spell, /learn, and…, Test cast command when no spell name is provided., Test spell command when no spell name is provided., Test spell command when player has mastery., Test stop command success., Test announce spell cast when chat service raises an error., test_announce_spell_cast_chat_error(), test_handle_cast_command_no_spell_name() (+3 more)

### Community 1007 - "💡 Recommendations"
Cohesion: 0.50
Nodes (4): Immediate, Medium-Term (Next 2-3 Weeks), 💡 Recommendations, Short-Term (This Week)

### Community 1008 - "optimized_validate_player_name"
Cohesion: 0.12
Nodes (16): Test validating empty player name., Test validating valid player name., Test validating player name with underscore., Test validating player name with hyphen., Test validating player name with numbers., Test validating player name starting with number (invalid)., Test validating player name with special characters (invalid)., test_optimized_validate_player_name_empty() (+8 more)

### Community 1009 - "Improve Layout Systematically"
Cohesion: 0.15
Nodes (13): Arrange Skill, Assess Current Layout, Break Card Grid Monotony, Choose the Right Layout Tool, Create Visual Rhythm, Establish a Spacing System, Improve Layout Systematically, Manage Depth & Elevation (+5 more)

### Community 1010 - "Distill Skill"
Cohesion: 0.15
Nodes (13): Distill Skill, Assess Current State, Code Simplification, Content Simplification, Document Removed Complexity, Information Architecture, Interaction Simplification, Layout Simplification (+5 more)

### Community 1011 - "Interaction Design"
Cohesion: 0.15
Nodes (12): Destructive Actions: Undo > Confirm, Focus Rings: Do Them Right, Form Design: The Non-Obvious, Gesture Discoverability, Interaction Design, Keyboard Navigation Patterns, Loading States, Modals: The Inert Approach (+4 more)

### Community 1012 - "Missing Test Scenarios"
Cohesion: 0.50
Nodes (4): Database Connection Loss, Missing Test Scenarios, NATS Unavailability, Room Data Corruption

### Community 1013 - "MythosMUD Full-Stack Feature Skill"
Cohesion: 0.18
Nodes (13): Event-Sourced Projector, Client Event Schema, game_state Event, GameState, room_state Event, Critical State Handoffs, Enter-Room Request/Response, MythosMUD COPPA Checklist Skill (+5 more)

### Community 1014 - "Next Steps"
Cohesion: 0.50
Nodes (4): Immediate (This Session), Medium Term (Weeks 2-6), Next Steps, Short Term (Week 1)

### Community 1016 - "_format_container_display"
Cohesion: 0.09
Nodes (22): _format_container_display(), Format the complete container display text., Test _format_container_display() with locked container., Test _format_container_display() with sealed container., Test _format_container_display() with look_in flag., Test _format_container_display() with target_type container., test_format_container_display_locked(), test_format_container_display_sealed() (+14 more)

### Community 1017 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)"
Cohesion: 0.15
Nodes (12): Communities (4 total, 2 thin omitted), Community 0 - "Kingsport Setting", Community 1 - "Solo Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11), Hyperedges (group relationships) (+4 more)

### Community 1018 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (3 total, 1 thin omitted), Community 0 - "Scenario Design", Community 1 - "Call of Cthulhu Roleplaying Game; Keeper Tips: C", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12), Hyperedges (group relationships) (+4 more)

### Community 1019 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (17 total, 16 thin omitted), Community 0 - "Scenario Handouts", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12), Hyperedges (group relationships), Import Cycles (+4 more)

### Community 1020 - "Geography Overview.md"
Cohesion: 0.15
Nodes (8): Bleak Prospect, Dreamlands, Geography Overview, Engineering memory, MythosMUD, Sources, World, Paris (Reign of Terror)

### Community 1021 - "required"
Cohesion: 0.17
Nodes (12): $defs, scheduleEntry, applies_to, category, days, end_hour, id, name (+4 more)

### Community 1022 - "Technical Implementation"
Cohesion: 0.15
Nodes (13): 1. Component Refactoring, 2. Message Routing Logic, 3. State Management, 4. Event Handling, ChatPanel.tsx Enhancements (New Chat Input Panel), Command Routing Logic, CommandPanel.tsx Simplifications, Current Logic (in CommandPanel) (+5 more)

### Community 1023 - "Execution Timeline"
Cohesion: 0.15
Nodes (13): Execution Timeline, Month 1: Pruning Phase, Month 2: Consolidation + Gap Filling, Month 3+: Continuous Improvement, Ongoing Tasks, Week 1: Quick Wins, Week 2: Infrastructure Reduction, Week 3: Coverage Test Optimization (+5 more)

### Community 1024 - "main"
Cohesion: 0.22
Nodes (12): analyze_connectivity(), generate_dot_file(), load_room_data(), main(), print_detailed_statistics(), print_room_listing(), Print a detailed listing of all rooms by subzone., Load all room and intersection data from the zone directory. (+4 more)

### Community 1025 - "fix_markdown_code_block_style.py"
Cohesion: 0.24
Nodes (12): detect_code_language(), fix_code_block_style(), fix_markdown_file(), is_indented_code_line(), main(), parse_markdownlint_output(), Path, Parse markdownlint output to get files with MD046 issues. (+4 more)

### Community 1026 - "main"
Cohesion: 0.22
Nodes (12): fix_md001_heading_increment(), fix_md013_line_length(), fix_md041_first_line_heading(), fix_md051_link_fragments(), main(), parse_errors(), Fix MD001: Heading levels should only increment by one level at a time., Parse markdownlint output file and extract errors. (+4 more)

### Community 1027 - "SyntaxErrorFixer"
Cohesion: 0.22
Nodes (8): main(), Path, Process multiple files and return statistics., Main function to run the syntax error fixer., Tool to fix syntax errors introduced by automated f-string remediation., Fix malformed logger calls with broken syntax., Fix syntax errors in a specific file., SyntaxErrorFixer

### Community 1028 - "run_quality_fragmentation_guard.py"
Cohesion: 0.31
Nodes (12): _argv_char_len(), _build_guard_command(), _changed_files_between(), _git_executable(), _is_graphify_path(), _local_changed_files(), main(), Path (+4 more)

### Community 1029 - "_check_grace_period_block"
Cohesion: 0.09
Nodes (25): _check_grace_period_block(), _get_grace_check_context(), UUID, Resolve player_id and connection_manager for grace period check. Returns None…, Check if player is in grace period and block commands. Players in grace period…, mock_request(), asyncio, fixture (+17 more)

### Community 1030 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 1031 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from…, Unit tests for connection utils. Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 1032 - "correct_patterns.py"
Cohesion: 0.05
Nodes (35): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+27 more)

### Community 1033 - "holiday"
Cohesion: 0.50
Nodes (4): $defs, holiday, additionalProperties, type

### Community 1034 - "._compose_memory_stats"
Cohesion: 0.25
Nodes (6): MemoryStatsSnapshot, TypedDict, Assemble memory stats from a snapshot dict (keeps call sites param-stable)., Expose memory monitor configuration knobs for stats payload., Connection-manager snapshot consumed by get_memory_stats., Get comprehensive memory and connection statistics. Args: snap: Connection-…

### Community 1035 - "FeatureFlagService"
Cohesion: 0.09
Nodes (12): FeatureFlagService, Clear the feature flag cache. This should be called when configuration changes…, Centralized feature flag service for MythosMUD. Provides type-safe access to…, Initialize the feature flag service., Check if combat system is enabled. Returns: bool: True if combat is enabled,…, Check if combat logging is enabled. Returns: bool: True if combat logging is…, Check if combat monitoring is enabled. Returns: bool: True if combat monitoring…, Test validate_combat_requirements returns True when combat is disabled. (+4 more)

### Community 1036 - ".get_upcoming_holidays"
Cohesion: 0.10
Nodes (12): _ensure_utc(), datetime, Update the active holiday window for the provided Mythos timestamp., Return currently active holiday entries., Get active holidays and serialize them for API responses. This method…, Get upcoming holidays and serialize them for API responses. This method…, Convenience helper for formatted admin output., Return the next N holidays, wrapping around the calendar. (+4 more)

### Community 1037 - "assert_event_envelope"
Cohesion: 0.11
Nodes (17): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., party_invite producer emits a build_event-shaped envelope., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success() (+9 more)

### Community 1038 - "get_database_path"
Cohesion: 0.13
Nodes (14): get_database_path(), Path, Get the database file path. DEPRECATED: PostgreSQL does not use file paths.…, Get the database file path (deprecated for PostgreSQL). Returns: Path | None:…, Test get_database_path returns None for PostgreSQL., Test get_database_path raises for None URL., test_get_database_path_none_url(), test_get_database_path_postgresql() (+6 more)

### Community 1039 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1040 - "Any"
Cohesion: 0.17
Nodes (9): Any, WebSocket, Handle a specific message type. Args: websocket: The WebSocket connection…, Handle command message type., Handle chat message type., Handle ping message type., Handle follow_response message type., Handle party_invite_response message type. (+1 more)

### Community 1041 - "generate_invites_db.py"
Cohesion: 0.19
Nodes (15): create_invite_in_db(), generate_invite_code(), generate_unique_codes(), get_existing_codes(), main(), parse_expires_date(), datetime, Generate a unique Mythos-themed invite code. (+7 more)

### Community 1042 - "test_persistence_container_persistence.py"
Cohesion: 0.14
Nodes (13): Unit tests for persistence.container_persistence module. This module tests the…, Test parsing None JSONB column., Test parsing string JSONB column., Test parsing dict JSONB column., Test parsing empty string JSONB column., Test parsing list JSONB column., Test parsing invalid JSON string., test_parse_jsonb_column_dict() (+5 more)

### Community 1043 - ".error"
Cohesion: 0.14
Nodes (9): Any, Build legacy dict entries for game config., Build legacy nats nested dict., Build legacy chat nested dict., Build legacy cors nested dict., Initialize configuration and set environment variables for legacy compatibility., Return first set CORS origins env var to reduce CCN in _sanitize., Normalize environment variables so nested configs can parse them reliably. (+1 more)

### Community 1044 - "UUID"
Cohesion: 0.10
Nodes (10): UUID, Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository., Delete a player. Delegates to PlayerRepository., Add a player effect. Returns effect id., Remove a player effect by id., Get active effects for a player (remaining_ticks > 0). Returns list of…, Return True if player has an active effect of the given type., Return remaining ticks for the effect, or None. (+2 more)

### Community 1045 - "test_combat_loader.py"
Cohesion: 0.08
Nodes (46): format_combat_status(), get_combat_target(), Any, Produce a human-readable combat status string. This helper is retained for…, Resolve a combat target by name. The current implementation is intentionally…, _app_from_request(), get_combat_command_handler(), handle_attack_command() (+38 more)

### Community 1046 - "Any"
Cohesion: 0.13
Nodes (8): Any, Initialize the player service with a persistence layer and optional combat…, Heal a player's health. Args: player_id: The player's ID (UUID) amount: Amount…, Damage a player's health. Args: player_id: The player's ID (UUID) amount:…, Respawn a dead player by user ID. This method handles the complete respawn…, Respawn a delirious player by user ID. This method handles the complete…, Set the item prototype registry on the schema converter (e.g. after item…, Convert a player object to PlayerRead schema. This is a public method that…

### Community 1047 - "fixture"
Cohesion: 0.15
Nodes (13): catalog_with_own_language_and_mythos(), mock_persistence(), mock_player_skill_repo(), mock_skill_repo(), mock_skill_use_log_repo(), fixture, Mock PlayerSkillRepository., Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id). (+5 more)

### Community 1048 - "test_validate_codacy_coverage_gate.py"
Cohesion: 0.23
Nodes (12): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., test_cobertura_root_line_rate_parses(), test_lcov_aggregate_and_gate() (+4 more)

### Community 1049 - "feature_flag_service.py"
Cohesion: 0.15
Nodes (15): is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature…, Validate that all combat requirements are met. Returns: bool: True if combat…, Get status of all feature flags. Returns: Dict[str, Dict[str, Any]]: Status of…, Check if combat is available for a specific player or globally. Args:… (+7 more)

### Community 1050 - "room_validator/schemas/unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 1051 - "Commands"
Cohesion: 0.17
Nodes (12): Add a branch — `gh stack add`, Check out a stack — `gh stack checkout`, Commands, Initialize a stack — `gh stack init`, Link branches as a stack (no local tracking) — `gh stack link`, Navigate the stack, Push branches to remote — `gh stack push`, Rebase the stack — `gh stack rebase` (+4 more)

### Community 1052 - "Amplify the Design"
Cohesion: 0.17
Nodes (12): Bolder Skill, Amplify the Design, Assess Current State, Color Intensification, Composition Boldness, MANDATORY PREPARATION, Motion & Animation, Plan Amplification (+4 more)

### Community 1053 - "Hardening Dimensions"
Cohesion: 0.17
Nodes (12): Harden Skill, Accessibility Resilience, Assess Hardening Needs, Edge Cases & Boundary Conditions, Error Handling, Hardening Dimensions, Input Validation & Sanitization, Internationalization (i18n) (+4 more)

### Community 1054 - "MythosMUD LLM Wiki (Obsidian)"
Cohesion: 0.17
Nodes (12): LLM Wiki Skill, Chaosium ingest, Division of labor, Graphify sync, Ingest, Lint, MythosMUD LLM Wiki (Obsidian), Non-goals (+4 more)

### Community 1055 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1056 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 1057 - "PanelContextRuntime.tsx"
Cohesion: 0.21
Nodes (9): defaultPanels, PanelContext, PanelContextType, PanelLayout, PanelPosition, PanelProvider(), PanelProviderProps, PanelSize (+1 more)

### Community 1058 - "mcp.json"
Cohesion: 0.20
Nodes (11): codacy, context7, jcodemunch, playwright, JCODEMUNCH_MAX_FOLDER_FILES, npx, uvx, @codacy/codacy-mcp (+3 more)

### Community 1059 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)"
Cohesion: 0.17
Nodes (11): Communities (2 total, 1 thin omitted), Community 0 - "Expedition Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 1060 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (3 total, 2 thin omitted), Community 0 - "Player Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 1061 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (8 total, 7 thin omitted), Community 0 - "Character Sheets", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 1062 - "bonus_tags"
Cohesion: 0.33
Nodes (6): items, type, uniqueItems, minLength, type, bonus_tags

### Community 1063 - "Async Remediation Summary - December 3, 2025"
Cohesion: 0.17
Nodes (11): Async Remediation Summary - December 3, 2025, Executive Summary, 📝 Git Commit Message, Issues Addressed (12 of 12), New Tests Created, Phase 2: Async Persistence Migration (2-3 weeks), 📋 Remaining Work, 📊 Remediation Results (+3 more)

### Community 1064 - "Migration Guide: From Default Logging to Enhanced Logging"
Cohesion: 0.17
Nodes (12): 1. Update Import Statements, 2. Migrate Context Parameters, 3. Convert String Formatting to Structured Logging, 4. Add Rich Context to Error Messages, Issue 1: ImportError when using enhanced logging, Issue 2: TypeError with context parameter, Issue 3: Logs not appearing in files, Issue 4: Sensitive data appearing in logs (+4 more)

### Community 1065 - "Migration Roadmap"
Cohesion: 0.17
Nodes (12): Files to Migrate (11 total), Files to Migrate (2 total), Files to Migrate (6 total), Game Systems (3 files), Migration Roadmap, NPC Systems (7 files), Phase 2: API Endpoints (Priority 1) 🎯, Phase 3: Real-Time Handlers (Priority 2) 🚀 (+4 more)

### Community 1066 - "Enhanced Logging Guide"
Cohesion: 0.18
Nodes (12): Structured Error Logging, log_and_raise Utilities, Test/Production Environment Separation, AI Agent Development Guide, AI Enhanced Logging Mandate, Enhanced Logging Guide, MDC Request Context Binding, measure_performance Span (+4 more)

### Community 1067 - "Critical Insights"
Cohesion: 0.13
Nodes (15): 1. Infrastructure Tests are the Main Optimization Target, 2. Regression Tests are 100% High-Value, 3. Coverage Tests Written for Metrics, Not Quality, 4. No Parametrized Tests (Major Opportunity), 5. Critical Gaps in New Architecture, Critical Insights, Example, Example Low-Value Test (+7 more)

### Community 1068 - "Actionable Recommendations"
Cohesion: 0.15
Nodes (13): Actionable Recommendations, Add Missing Integration Tests (70 tests, 0% risk, 10 hours effort), Command, Critical Gap Action (Month 2), Files, High-Priority Action (Next 2 Weeks), Immediate Action (This Week), Parametrize Repetitive Tests (170 → 50, 0% risk, 8 hours effort) (+5 more)

### Community 1069 - "Movement Subsystem Design"
Cohesion: 0.17
Nodes (11): 1. Overview, 2. Architecture, 3. Key design decisions, 4. Constraints, 5. Component interactions, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1070 - "Multi-Character Support System"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1071 - ".call"
Cohesion: 0.16
Nodes (8): Any, Handle successful function call. Updates state based on current circuit state:…, Handle failed function call. Updates state based on failure count: - Increments…, Check if enough time has passed to attempt circuit reset. Returns: True if…, Calculate seconds until circuit can attempt reset. Returns: Seconds until retry…, Transition circuit to new state. Args: new_state: State to transition to AI:…, Get circuit breaker statistics. Returns: Dictionary with circuit breaker…, Execute function through circuit breaker. Enforces circuit breaker logic: -…

### Community 1072 - "enum"
Cohesion: 0.25
Nodes (8): Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, enum

### Community 1073 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 1074 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 1075 - "grype.py"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1076 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 1077 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1078 - "position_commands.py"
Cohesion: 0.11
Nodes (30): _broadcast_posture_change(), _build_posture_change_event(), _get_position_command_services(), handle_lie_command(), _handle_position_change(), handle_sit_command(), handle_stand_command(), Request (+22 more)

### Community 1079 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 1080 - "long_description"
Cohesion: 0.50
Nodes (4): maxLength, minLength, type, long_description

### Community 1081 - "look_container.py"
Cohesion: 0.10
Nodes (36): _as_map(), _as_map_list(), _as_uuid(), _container_name(), _ContainerPersistence, _extract_container_metadata(), _fetch_container(), _find_container_in_room() (+28 more)

### Community 1082 - "prototype_id"
Cohesion: 0.50
Nodes (4): prototype_id, maxLength, minLength, type

### Community 1083 - "short_description"
Cohesion: 0.50
Nodes (4): short_description, maxLength, minLength, type

### Community 1084 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1085 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1086 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1087 - "test_monitoring_init.py"
Cohesion: 0.17
Nodes (11): Unit tests for server.monitoring lazy __getattr__ re-exports., Exception tracker symbols import without triggering numpy lazy paths., __getattr__ resolves MonitoringDashboard and get_monitoring_dashboard., __getattr__ resolves PerformanceStats and get_performance_monitor., Unknown attribute names raise AttributeError., Direct __getattr__ covers both branch returns for dashboard imports., test_monitoring_eager_imports(), test_monitoring_getattr_direct_call() (+3 more)

### Community 1088 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1089 - "TestEmoteDetection"
Cohesion: 0.17
Nodes (9): patch, Test should_treat_as_emote() returns False for system commands., Test should_treat_as_emote() returns False for unknown words., Test should_treat_as_emote() returns True for predefined emotes., Test emote detection functions., Test _is_predefined_emote() returns True for predefined emote., Test _is_predefined_emote() returns False for non-emote., Test _is_predefined_emote() handles errors gracefully. (+1 more)

### Community 1090 - "handle_system_command"
Cohesion: 0.24
Nodes (11): handle_system_command(), Any, Broadcast a system-level message via the chat service if available., asyncio, Unit tests for system command handlers. Tests the system command functionality., Test handle_system_command() broadcasts system message., Test handle_system_command() handles missing message., Test handle_system_command() handles missing chat service. (+3 more)

### Community 1091 - "test_player_event_handlers_utils_grace_period.py"
Cohesion: 0.14
Nodes (14): mock_logger(), mock_name_extractor(), fixture, Unit tests for player event handlers utils grace period integration. Tests the…, Create a mock PlayerNameExtractor., Create a mock logger., Test is_player_in_grace_period() returns True when player is in grace period., Test is_player_in_grace_period() returns False when player is not in grace… (+6 more)

### Community 1092 - "test_player_event_handlers_room.py"
Cohesion: 0.17
Nodes (11): Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test broadcast_player_entered_message() skips when room_id is None., Test _prepare_room_data() handles room without to_dict method., Test PlayerRoomEventHandler initialization., Test _process_player_entered_event() returns None when room_id is None., Test log_player_movement() skips when connection manager not available., test_broadcast_player_entered_message_no_room_id(), test_log_player_movement_no_connection_manager() (+3 more)

### Community 1095 - "test_schedule_service.py"
Cohesion: 0.07
Nodes (27): _DatabaseLoadResult, _fetch_schedule_entries(), _lower_string_list_from_row(), normalize_weekday_names(), Connection, Record, TypedDict, Load and normalize schedule rows from PostgreSQL. (+19 more)

### Community 1096 - "load_motd"
Cohesion: 0.23
Nodes (11): Unit tests for motd_loader utilities. Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+3 more)

### Community 1097 - "reset_config"
Cohesion: 0.25
Nodes (8): Reset the configuration cache. In test mode, this is a no-op since get_config()…, reset_config(), Reset config singleton before and after each test. In test mode, get_config()…, reset_config_singleton(), Test that reset_config() works in test mode., test_reset_config_in_test_mode(), Test that reset_config() clears global state., test_reset_config_clears_state()

### Community 1098 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1099 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1100 - "Responsive Design"
Cohesion: 0.18
Nodes (10): Breakpoints: Content-Driven, Detect Input Method, Not Just Screen Size, Layout Adaptation Patterns, Mobile-First: Write It Right, Picture Element for Art Direction, Responsive Design, Responsive Images: Get It Right, Safe Areas: Handle the Notch (+2 more)

### Community 1101 - "Quieter Skill"
Cohesion: 0.18
Nodes (11): Quieter Skill, Assess Current State, Color Refinement, Composition Refinement, MANDATORY PREPARATION, Motion Reduction, Plan Refinement, Refine the Design (+3 more)

### Community 1102 - "Typeset Skill"
Cohesion: 0.18
Nodes (11): Typeset Skill, Assess Current Typography, Establish Hierarchy, Fix Readability, Font Selection, Improve Typography Systematically, MANDATORY PREPARATION, Plan Typography Improvements (+3 more)

### Community 1103 - "mythos_e2e Database"
Cohesion: 0.20
Nodes (11): Playwright E2E Runtime Tests, ArkanWolfshade E2E Account, E2E Tests Playwright, Ithaqua E2E Account, mythos_e2e Database, Runtime Auth Isolation, Playwright storageState Session Sharing, E2E Login Timeout Issue (+3 more)

### Community 1104 - "GridLayoutManager.tsx"
Cohesion: 0.20
Nodes (5): GridLayoutManager(), GridLayoutManagerProps, layoutConfig, PanelComponent, ResponsiveGridLayout

### Community 1106 - "vite.userConfig.ts"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1107 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (1 total, 0 thin omitted), Community 0 - "Mythos Subjects", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1108 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (2 total, 2 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1109 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Ambiguous Edges - Review These, Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1110 - "Authoritative Environment DML"
Cohesion: 0.20
Nodes (11): Spells Seed Data (Deprecated), static_seed.sql (Deprecated), Generated World and Emotes SQL, DB Bootstrap Execution Order, Authoritative Environment DML, Removed Schema and Migration SQL, Legacy Schema Files Removed, Historical DDL Final Status (+3 more)

### Community 1111 - "ADR-018: New Game Session vs Grace Reconnect"
Cohesion: 0.18
Nodes (10): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. References, 8. Changelog (+2 more)

### Community 1112 - "Async Code Review - Post Phase 2 Migration"
Cohesion: 0.18
Nodes (10): anyio.mdc Compliance, Async Code Review - Post Phase 2 Migration, asyncio.mdc Compliance, 📋 Checklist Against Best Practices, 📊 Compliance Scorecard, 📝 Conclusion, Executive Summary, 🟡 Minor Recommendations (Not Blocking) (+2 more)

### Community 1113 - "✅ Best Practices Compliance"
Cohesion: 0.18
Nodes (11): 10. Exception Handling in Async Operations (asyncio.mdc Section 2.5), 1. Blocking the Event Loop (asyncio.mdc Section 2.3), 2. Async/Await Usage (anyio.mdc Section 2.2), 3. Method Signature Consistency (asyncio.mdc Section 2.1), 4. Error Handling (asyncio.mdc Section 2.5), 5. Resource Management (anyio.mdc Section 2.1), 6. Task Groups / Structured Concurrency (anyio.mdc Section 2.1), 7. Avoiding asyncio.run() in Library Code (asyncio.mdc Section 6.1) (+3 more)

### Community 1114 - "🔍 Specific File Reviews"
Cohesion: 0.18
Nodes (11): ✅ container_service.py, ✅ corpse_lifecycle_service.py, ✅ database.py, ✅ exploration_service.py, ✅ npc_combat_integration_service.py, ✅ passive_lucidity_flux_service.py, ✅ persistence.py, ✅ player_death_service.py (+3 more)

### Community 1115 - "CircuitBreaker Implementation Planning Document"
Cohesion: 0.18
Nodes (10): CircuitBreaker Implementation Planning Document, Configuration Schema, Dependencies, Gradual Rollback, Immediate Rollback, Objectives, Overview, Rollback Plan (+2 more)

### Community 1116 - "CI Workflow"
Cohesion: 0.25
Nodes (11): CodeQL Configuration, CodeQL Test Credential Exclusions, CI Python Backend Job, CI Workflow, Codacy Coverage Finalize Job, CI React Client Job, step-security Harden Runner, mythos_unit CI Database Bootstrap (+3 more)

### Community 1117 - "analyze_file"
Cohesion: 0.22
Nodes (10): analyze_file(), check_comment_references_nonexistent_code(), extract_function_and_class_names(), main(), Any, Path, Analyze a single file for comment issues. Args: file_path: Path to file to…, Main entry point for comment analysis. (+2 more)

### Community 1118 - "check_and_apply_map_migrations.py"
Cohesion: 0.25
Nodes (10): apply_migration_013(), apply_migration_014(), check_migration_013(), check_migration_014(), main(), Main function to check and apply migrations., Check if migration 013 (map_x/map_y columns) has been applied., Check if migration 014 (player_exploration table) has been applied. (+2 more)

### Community 1119 - "main"
Cohesion: 0.29
Nodes (10): check_thresholds(), _ensure_coverage_xml_or_exit(), main(), parse_coverage_xml(), _print_results_and_exit(), Path, Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't…, Print coverage results and exit with appropriate code. (+2 more)

### Community 1120 - ".validate_database_url"
Cohesion: 0.29
Nodes (4): field_validator, Validate port is in valid range., Validate database URL format - PostgreSQL only., Validate pool configuration values are positive.

### Community 1121 - "main"
Cohesion: 0.25
Nodes (10): generate_simple_dot_file(), generate_simple_html_visualization(), load_room_data(), main(), print_simple_statistics(), Load all room and intersection data from the zone directory., Print simplified statistics about the room data., Main function to generate the simplified visualization. (+2 more)

### Community 1126 - "test_inventory_mutation_guard_sync.py"
Cohesion: 0.13
Nodes (14): guard(), fixture, Unit tests for inventory mutation guard - synchronous acquire operations. Tests…, Create an InventoryMutationGuard instance., Test acquire serializes mutations per player., Test acquire allows token reuse after expiry., Test acquire with token_ttl=0 (no expiry)., Test acquire enforces max_tokens limit. (+6 more)

### Community 1128 - "SpellMaterial"
Cohesion: 0.08
Nodes (36): Any, UUID, Build final inventory with consumed materials removed. Args: inventory:…, Consume spell materials from player inventory. Args: player_id: Player ID…, Service for handling spell material requirements. Handles checking if players…, Check if player has all required materials. Args: player_id: Player ID spell:…, Process a single material requirement. Args: material: Material requirement…, Consume a material item. Args: item: Inventory item material_id: Material ID… (+28 more)

### Community 1130 - "items"
Cohesion: 0.33
Nodes (6): items, minItems, type, additionalProperties, properties, holidays

### Community 1131 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1133 - ".get_alias_file_path"
Cohesion: 0.15
Nodes (12): AliasPayload, _as_alias_payload(), _empty_alias_payload(), Path, Get the file path for a player's aliases. Human: reject path separators /…, Absolute str path for open(); re-checks containment at the open site. Human:…, Load alias data from JSON file., Save alias data to JSON file. (+4 more)

### Community 1134 - "test_async_persistence_room_cache.py"
Cohesion: 0.14
Nodes (13): Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test _generate_room_id_from_zone_data with None values., Test _parse_exits_json with invalid JSON string., Test _process_exits_for_room processes exits with direction., Test _process_exits_for_room skips exits without direction., Test _process_combined_rows processes rows with exits JSON., Test _process_exit_rows handles missing direction., test_generate_room_id_from_zone_data_none_values() (+5 more)

### Community 1136 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 1139 - "name"
Cohesion: 0.50
Nodes (4): description, minLength, type, name

### Community 1140 - "UUID"
Cohesion: 0.11
Nodes (11): Stats, UUID, Create a new player character with specific stats. Args: name: The player's…, Get a player by their ID. Args: player_id: The player's ID (UUID) Returns:…, Get all active characters for a user. MULTI-CHARACTER: Returns list of active…, Validate that a character exists, belongs to the user, and is not deleted.…, Apply lucidity loss to a player. Args: player_id: The player's ID (UUID)…, Apply fear to a player. Args: player_id: The player's ID (UUID) amount: Amount… (+3 more)

### Community 1141 - "Teach Impeccable Skill"
Cohesion: 0.24
Nodes (11): Aha Moment Onboarding, Core Web Vitals Performance, Design Context Persistence (.impeccable.md), Onboard Skill, Optimize Skill, Overdrive Skill, Overdrive Mode, Polish Skill (+3 more)

### Community 1143 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1144 - "_occupation_slots_9"
Cohesion: 0.17
Nodes (12): _occupation_slots_9(), Valid 9 slots: one 70, two 60, three 50, three 40; 9 distinct skill_ids (no…, When Own Language is not in occupation or personal, its value is stats_for_edu., Personal interest with Cthulhu Mythos raises ValueError., personal_interest must have exactly 4 entries., personal_interest with duplicate skill_id raises ValueError., Occupation and personal interest sharing a skill_id raises ValueError., test_set_player_skills_cthulhu_mythos_in_personal_rejected() (+4 more)

### Community 1145 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 1146 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 1147 - "Mypy Remediation"
Cohesion: 0.15
Nodes (12): 🔴 Critical — import and name errors, Debugging when a fix doesn't take, Entry point, Error code table, Fix patterns by tier, Fix-verify loop, 🟡 High — type errors, 🔵 Low — type precision (+4 more)

### Community 1148 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.18
Nodes (11): 10. Final Verification, 3. Systematic Investigation Approach, 5. Test Environment Setup, 6. Quality Assurance Checklist, Environment Variables, For Authentication Failures, For Database-Related Failures, For Game Logic Failures (+3 more)

### Community 1149 - "FAILURE PATTERN RECOGNITION"
Cohesion: 0.33
Nodes (6): A. Database-Related Failures, B. Authentication/Security Failures, C. WebSocket/Connection Failures, D. Game Logic Failures, E. Integration Test Failures, FAILURE PATTERN RECOGNITION

### Community 1150 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)"
Cohesion: 0.20
Nodes (9): Communities (1 total, 1 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12), Knowledge Gaps, Suggested Questions, Summary (+1 more)

### Community 1151 - "Chaosium CoC Catalog"
Cohesion: 0.20
Nodes (9): Chaosium CoC Catalog, Creature / motif families (adaptation stubs), How to use, MythosMUD adaptation notes, Ongoing ops, Tier A (full or batch-promoted), Tier B (source-only), Tier C (+1 more)

### Community 1152 - "enum"
Cohesion: 0.29
Nodes (7): autumn, spring, summer, winter, season, enum, type

### Community 1153 - "Architecture Decision Records Index"
Cohesion: 0.20
Nodes (10): ADR-013 Pydantic BaseSettings Configuration, ADR-014 NATS Circuit Breaker and DLQ, Dead Letter Queue, db/procedures Stored Functions, ADR-015 PostgreSQL Procedures Migration, ADR-016 Aggro Threat Management, Room-Based Combat Aggro, ADR-017 AST Console Pruning (+2 more)

### Community 1154 - "Asynchronous Code Audit - December 3, 2025"
Cohesion: 0.14
Nodes (13): adjusts spectacles grimly, Asynchronous Code Audit - December 3, 2025, ✍️ AUDIT CONCLUSION, Audit Status**: ✅**COMPLETE, Blocking Risks, 📞 ESCALATION MATRIX, Executive Summary, Non-Blocking Risks (+5 more)

### Community 1155 - "Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES"
Cohesion: 0.20
Nodes (10): Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES, Phase 3: Medium Priority Improvements (Week 4) - POLISH, 📋 REMEDIATION PLAN, Task 1.1: Fix Synchronous Blocking in Passive Lucidity Flux Service, Task 1.2: Eliminate asyncio.run() from Library Code, Task 1.3: Ensure Connection Pool Cleanup, Task 1.4: Add Exception Handling to Pool Creation, Task 1.5: Fix Blocking Operations in NATS Message Handlers (+2 more)

### Community 1156 - "Enhanced Logging Best Practices for MythosMUD"
Cohesion: 0.18
Nodes (10): Basic Logging, Common Anti-Patterns, Conclusion, ✅ Do This Instead, ❌ Don't Do This, Enhanced Logging Best Practices for MythosMUD, Error Logging with Context, Overview (+2 more)

### Community 1157 - "Appendices"
Cohesion: 0.20
Nodes (10): Appendices, Appendix A: Test File Inventory, Appendix B: Direct app.state Access Locations, Appendix C: Fixture Audit, Consolidation Opportunities, Current Fixture Categories, High Priority (Integration Tests), Low Priority (Other) (+2 more)

### Community 1158 - "Implementation Phases"
Cohesion: 0.12
Nodes (17): Deliverables, Deliverables, Deliverables, Deliverables, Deliverables, Implementation Phases, Phase 0: Foundation (Week 1) - 40 hours, Phase 1: Fix Failing Tests (Week 1-2) - 40 hours (+9 more)

### Community 1159 - "Summary: Test Quality Metrics"
Cohesion: 0.40
Nodes (5): By removing 15% of tests, we, Current State, Optimized State (After Pruning), Summary: Test Quality Metrics, Value Proposition

### Community 1160 - "MythosMUD Testing Strategy (Greenfield Suite)"
Cohesion: 0.20
Nodes (9): Coverage policy, Fixtures/layout, Isolation rules, Logging and diagnostics, Markers, Mocking standards, MythosMUD Testing Strategy (Greenfield Suite), Tiers and commands (+1 more)

### Community 1161 - "Dialogue Content Tools (Content Creators)"
Cohesion: 0.20
Nodes (9): 1. Overview, 2. Open the editor, 3. Tree shape (nav-only), 4. Editor workflow, 5. Player verification, 6. Seed and API reference, 7. Related docs, AI READING INSTRUCTION (+1 more)

### Community 1162 - "load_test_10_players.spec.ts"
Cohesion: 0.22
Nodes (6): generateLoadTestCredential(), INVITE_CODES, PLAYER_CONFIGS, PlayerConfig, NOTE: This test is designed to be executed using Playwright MCP tools for, registerPlayer()

### Community 1163 - "enum"
Cohesion: 0.20
Nodes (10): city, countryside, desert, mountains, swamp, tundra, zone_type, description (+2 more)

### Community 1164 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1165 - "emote_schema.json"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 1166 - "bench_cache_npc.py"
Cohesion: 0.31
Nodes (5): bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…

### Community 1167 - "check_file"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1168 - ".__init__"
Cohesion: 0.20
Nodes (7): Check if the status effect is still active., Any, Initialize Invite with defaults., _npc_alive_and_active(), setter, Return True if NPC is alive (determination_points > 0)., Allow backward-compatible assignment (npc.is_alive = False).

### Community 1169 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1170 - "RetryConfig"
Cohesion: 0.14
Nodes (11): Get current retry configuration. Returns: Current RetryConfig AI: Useful for…, Configuration for retry behavior. Defines retry parameters for handling…, Calculate delay for a given attempt number. Uses exponential backoff capped at…, Initialize retry handler. Args: max_retries: Maximum number of retry attempts…, RetryConfig, Test RetryConfig.calculate_delay() with base delay., Test RetryConfig.calculate_delay() respects max_delay., Test RetryConfig default values. (+3 more)

### Community 1171 - "lucidity_migration.py"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1172 - "_personal_interest_4"
Cohesion: 0.17
Nodes (12): _personal_interest_4(), Four personal interest (skill_ids only); distinct and no overlap with…, set_player_skills with valid occupation and personal calls delete then…, Occupation slot with Cthulhu Mythos (allow_at_creation=False) raises ValueError., occupation_slots not length 9 raises ValueError., occupation_slots with wrong value set (e.g. two 70s) raises ValueError., occupation_slots with duplicate skill_id raises ValueError., test_set_player_skills_cthulhu_mythos_in_occupation_rejected() (+4 more)

### Community 1173 - "asyncio"
Cohesion: 0.05
Nodes (43): asyncio, Test spawn_npc_instance() successfully spawns NPC., Test spawn_npc_instance() raises ValueError when definition not found., Test spawn_npc_instance() raises RuntimeError when spawn fails., Test despawn_npc_instance() successfully despawns NPC., Test despawn_npc_instance() is idempotent when NPC not found., Test despawn_npc_instance() raises RuntimeError when despawn fails., Test move_npc_instance() successfully moves NPC. (+35 more)

### Community 1174 - "npc_spawn_modifier"
Cohesion: 0.50
Nodes (4): description, minimum, type, npc_spawn_modifier

### Community 1175 - "event_publisher"
Cohesion: 0.29
Nodes (7): event_publisher(), mock_nats_service(), mock_subject_manager(), fixture, Create a mock NATS service., Create a mock subject manager., Create an EventPublisher instance.

### Community 1176 - "special_rules"
Cohesion: 0.50
Nodes (4): special_rules, additionalProperties, description, type

### Community 1177 - "factory"
Cohesion: 0.67
Nodes (3): factory(), fixture, Create a CommandFactory instance.

### Community 1178 - "ChatChannelLoggerMixin"
Cohesion: 0.16
Nodes (10): ChatChannelLoggerMixin, Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs., Get the local channel log file path for a specific sub-zone. Args: subzone:…, Clean up old local channel log files. Args: days_to_keep: Number of days of…, Log a local channel message to sub-zone specific file. Args: message_data:…, extract_subzone_from_room_id(), get_subzone_local_channel_subject(), Room utility functions for MythosMUD. This module provides utility functions… (+2 more)

### Community 1179 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 1180 - "plane"
Cohesion: 0.67
Nodes (3): minLength, type, plane

### Community 1181 - "📈 Success Metrics"
Cohesion: 0.67
Nodes (3): Achieved, 📈 Success Metrics, To Verify (After Deployment)

### Community 1182 - "_EventPersistence"
Cohesion: 0.22
Nodes (6): _EventPersistence, _Named, _NatsPublish, Protocol, UUID, Initialize EventPublisher service. Args: nats_service: NATS service instance…

### Community 1183 - "optimized_validate_action_content"
Cohesion: 0.20
Nodes (10): Test validating empty action., Test validating valid action., Test validating action with dangerous characters., Test validating action with injection pattern., test_optimized_validate_action_content_dangerous_chars(), test_optimized_validate_action_content_empty(), test_optimized_validate_action_content_injection(), test_optimized_validate_action_content_valid() (+2 more)

### Community 1184 - "optimized_validate_alias_name"
Cohesion: 0.20
Nodes (10): Test validating empty alias name., Test validating valid alias name., Test validating alias name starting with number (invalid)., Test validating alias name with hyphen (invalid - aliases don't allow hyphens)., test_optimized_validate_alias_name_empty(), test_optimized_validate_alias_name_hyphen(), test_optimized_validate_alias_name_starts_with_number(), test_optimized_validate_alias_name_valid() (+2 more)

### Community 1185 - "optimized_sanitize_unicode_input"
Cohesion: 0.20
Nodes (10): Test sanitizing empty string., Test sanitizing normal text (no changes expected)., Test sanitizing text with Unicode issues., test_optimized_sanitize_unicode_input_empty(), test_optimized_sanitize_unicode_input_normal_text(), test_optimized_sanitize_unicode_input_unicode(), _cached_ftfy_fix(), optimized_sanitize_unicode_input() (+2 more)

### Community 1186 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test _ensure_room_cache_loaded returns early when cache is already loaded., Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…, Test _ensure_room_cache_loaded handles DatabaseError gracefully., Test _ensure_room_cache_loaded handles OSError gracefully., Test _ensure_room_cache_loaded handles RuntimeError gracefully., test_ensure_room_cache_loaded_already_loaded(), test_ensure_room_cache_loaded_concurrent_load() (+3 more)

### Community 1187 - "gh-stack (MythosMUD)"
Cohesion: 0.22
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1188 - "Workflows"
Cohesion: 0.22
Nodes (9): End-to-end: create a stack from scratch, Handle rebase conflicts (agent workflow), Making mid-stack changes, Modify a mid-stack branch and sync, Parsing `--json` output, Restructure a stack (remove a branch, reorder, or rename), Routine sync after merges, Squash-merge recovery (+1 more)

### Community 1189 - "Security Considerations"
Cohesion: 0.67
Nodes (3): Data Sanitization, Security Considerations, Sensitive Data Protection

### Community 1190 - "test_websocket_handler_validation.py"
Cohesion: 0.20
Nodes (11): mock_validator(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler message validation. Tests the message…, Create a mock WebSocket., Create a mock message validator., Test _validate_message() returns message when validation succeeds. (+3 more)

### Community 1191 - "main"
Cohesion: 0.27
Nodes (10): _exit_empty(), _load_state(), main(), NoReturn, Path, Exit successfully with no decision (allow the stop)., Load and validate edited-files state. Returns None if missing or invalid., Write state via a same-directory temp file + os.replace. See… (+2 more)

### Community 1192 - "Motion Design"
Cohesion: 0.22
Nodes (8): Duration: The 100/300/500 Rule, Easing: Pick the Right Curve, Motion Design, Perceived Performance, Performance, Reduced Motion, Staggered Animations, The Only Two Properties You Should Animate

### Community 1193 - "run-playwright-tests.js"
Cohesion: 0.22
Nodes (7): clientRoot, __dirname, E2E_BACKEND_BASE_URL, env, __filename, playwright, testsDir

### Community 1194 - "Final Recommendation"
Cohesion: 0.67
Nodes (3): Final Recommendation, Start with Option B (Quick Wins) Immediately, Then Proceed to Option A (Full Optimization)

### Community 1195 - "main"
Cohesion: 0.27
Nodes (10): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Write state via a same-directory temp file + os.replace. See… (+2 more)

### Community 1196 - "holidays.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 1197 - "🟡 HIGH PRIORITY ISSUES"
Cohesion: 0.22
Nodes (9): 10. Loading All Players Instead of Active Only, 11. NATS Connection Pool Not Used by Default, 12. No TLS Configuration for NATS, 13. Event Loop Change Detection Edge Cases, 14. Missing Transaction Rollback on Critical Failures, 7. Missing Room Lookup Caching, 8. Incomplete Migration to Async Persistence, 9. Multiple Database Flushes Before Commit (+1 more)

### Community 1198 - "🟢 MEDIUM PRIORITY IMPROVEMENTS"
Cohesion: 0.13
Nodes (15): 15. Hardcoded Connection Pool Sizes, 16. Deprecated asyncio.get_event_loop() Usage, 17. Inconsistent Error Handling Patterns, 18. Memory Leak Risk in Metrics Collection, 19. Missing Message Acknowledgment in NATS, 20. Subject Naming Inconsistency, 21. No Connection Health Monitoring, 🟢 MEDIUM PRIORITY IMPROVEMENTS (+7 more)

### Community 1199 - "Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE"
Cohesion: 0.22
Nodes (9): Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE, Task 2.1: Add Room Lookup Caching, Task 2.2: Complete Async Persistence Migration, Task 2.3: Optimize Database Flush Operations, Task 2.4: Load Only Active Players, Task 2.5: Use NATS Connection Pool by Default, Task 2.6: Add TLS Configuration, Task 2.7: Improve Event Loop Change Detection (+1 more)

### Community 1200 - "🔴 Anti-Patterns Check (Critical)"
Cohesion: 0.22
Nodes (9): 1. Blocking the Event Loop?, 2. Missing `await` Keywords?, 3. Using `asyncio.run()` in Library Code?, 4. Mixing Sync and Async Code Incorrectly?, 5. Forgetting to Await Awaitable Objects?, 6. Not Handling Exceptions?, 7. Over-using Locks?, 8. Unstructured Concurrency? (+1 more)

### Community 1201 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 1202 - "Persistence Layer Async Migration Plan"
Cohesion: 0.22
Nodes (8): Aggressive Timeline (Focused Migration), Conclusion, Conservative Timeline (Gradual Migration), Migration Timeline, Persistence Layer Async Migration Plan, Phase 1: Foundation Complete ✅, References, Total Migration Effort

### Community 1203 - "**~25-30% provide CRITICAL coverage**"
Cohesion: 0.22
Nodes (8): **~25-30% provide CRITICAL coverage**, Immediate (This Week), Medium-Term (Next Month), Next Steps, Quick Reference, Short-Term (This Month), Specifically, The other 70-75%

### Community 1204 - "Cursor Workflows"
Cohesion: 0.22
Nodes (9): Cursor Agent CLI, Cursor CLI, Cursor Hooks, Cursor Lifecycle Hooks, Cursor Setup Guide, Cursor Subagents, Built-in Explore Bash Browser Subagents, Cursor Workflows (+1 more)

### Community 1205 - "test_ascii_map_renderer_grid.py"
Cohesion: 0.18
Nodes (9): fixture, Unit tests for AsciiMapRenderer grid building. Guards against regressions in…, Return a fresh AsciiMapRenderer instance for each test., Tests for _build_grid player marker when multiple rooms share coordinates., Multiple rooms at same (x,y): cell keeps player marker even if player room is…, render_map covers empty map, styles, exits, and row rendering., renderer(), test_render_map_empty_and_connected_rooms() (+1 more)

### Community 1206 - "enum"
Cohesion: 0.20
Nodes (10): artifact, consumable, container, currency, equipment, quest, enum, type (+2 more)

### Community 1207 - "CombatMetrics"
Cohesion: 0.15
Nodes (12): CombatMetrics, get_combat_metrics(), Get current combat metrics. Returns: CombatMetrics: Current metrics, Combat system metrics., Save current metrics as a snapshot., Convenience function to get current combat metrics. Returns: CombatMetrics:…, Test get_current_metrics returns metrics., Test get_combat_metrics returns metrics. (+4 more)

### Community 1208 - "days"
Cohesion: 0.22
Nodes (10): items, items, minItems, type, items, type, pattern, type (+2 more)

### Community 1209 - "weight"
Cohesion: 0.67
Nodes (3): weight, minimum, type

### Community 1210 - "bench_cache.py"
Cohesion: 0.31
Nodes (6): bench_room_cache(), _FakePersistence, main(), Any, Lightweight cache benchmark for CI artifacts. Measures miss vs. hit timings for…, Fake persistence layer providing async_get_room with simulated latency.

### Community 1211 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 1212 - "_filter_lines"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after…, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1213 - "fix_markdown_file"
Cohesion: 0.36
Nodes (8): fix_markdown_file(), fix_multiple_blanks(), main(), parse_markdownlint_output(), Path, Fix multiple consecutive blank lines (MD012). Returns: (new_content,…, Parse markdownlint output to get files with MD012 issues., Fix multiple blank lines in a single markdown file. Returns: (changed,…

### Community 1214 - "fix_room_references"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area. Args: base_path: Path to the…, save_room_file()

### Community 1215 - "config.py"
Cohesion: 0.16
Nodes (15): lookup_profile(), period_label(), datetime, Configuration and normalization for passive lucidity flux., Return a coarse period label used for environment profiles., Look up flux value from profile by period., _as_float(), _as_str_attr() (+7 more)

### Community 1216 - "run_bug_prevention_tests.ps1"
Cohesion: 0.53
Nodes (8): Invoke-ClientTest(), Invoke-IntegrationTest(), Invoke-ServerTest(), Show-TestSummary(), Test-Command(), Write-ColorOutput(), Write-Header(), Write-Section()

### Community 1217 - "run_make_stages.py"
Cohesion: 0.33
Nodes (8): keep_going_requested(), main(), _print_fail(), Return True when Make was invoked with -k / --keep-going., Return a short failure reason, or None if the stage is OK., Run `make <stage>`, stream output, return (exit_code, captured_output)., run_stage(), stage_failed_from_output()

### Community 1218 - "capacity_slots"
Cohesion: 0.33
Nodes (6): default, description, maximum, minimum, type, capacity_slots

### Community 1219 - ".validate_current_vs_max_stats"
Cohesion: 0.11
Nodes (11): computed_field, Any, model_validator, Initialize Stats with provided data. For random stat generation, use…, Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes…, Calculate max magic points (MP) using formula: 20% of Power (ceiling rounded).…, Calculate max lucidity based on education. AI: This computed field uses the…, Calculate max determination points (DP) using formula: (CON + SIZ) / 5. AI:… (+3 more)

### Community 1220 - "apply_communication_dampening"
Cohesion: 0.25
Nodes (13): apply_communication_dampening(), Check if shout should be blocked based on tier., Apply communication dampening based on lucidity tiers. Args: message: Original…, should_block_shout(), patch, Unit tests for lucidity communication dampening., test_deranged_incoming_scrambles_words(), test_deranged_shout_blocked() (+5 more)

### Community 1221 - "._connect_nats"
Cohesion: 0.22
Nodes (6): Any, BaseException, Raise RuntimeError when e2e requires live NATS; no-op for other environments., Convert connect failures into hard error (e2e) or soft log (other envs)., Handle connect() returning False; raise for e2e, soft-warn otherwise., Connect to NATS if enabled and not unit_test. Returns NATSService or None.…

### Community 1222 - "player_inventory_migration.py"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1223 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test add_player_to_room() when room is not found., Test add_player_to_room() when player is not found., Test get_player_room() returns player's room., Test get_player_room() when player is not found., Test _validate_movement returns True for valid movement., Test _validate_movement returns False when destination room missing., Test move_player returns False when validation fails. (+11 more)

### Community 1224 - "TestResolveExitTarget"
Cohesion: 0.20
Nodes (6): Room without a reverse exit is not considered bidirectional., If the target room ID does not exist, the helper returns None., If the target room lacks map coordinates, the helper returns None., Tests for _resolve_exit_target., Room with a reverse exit is treated as bidirectional and returns its…, TestResolveExitTarget

### Community 1225 - "TestHorizontalExitCharBetween"
Cohesion: 0.20
Nodes (6): Tests for _horizontal_exit_char_between (em dash, >, <)., Bidirectional horizontal exit between two rooms uses an em dash., One-way east exit renders as a greater-than sign., One-way west exit renders as a less-than sign., When there are no horizontal exits, the helper returns None., TestHorizontalExitCharBetween

### Community 1226 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test get_players_batch() handles player not found., Test send_initial_game_state() sends initial state., Test convert_room_uuids_to_names() with empty room_data., Test convert_room_uuids_to_names() when player not found., Test _get_room_data_with_conversion() loads room and converts UUIDs., Test _process_occupants_with_grace_periods() splits players and NPCs., Test _get_player_data_for_client() uses PlayerService when available. (+11 more)

### Community 1227 - "test_utility_commands_whoami.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for utility command handlers. Tests the whoami command functionality., Test handle_whoami_command() returns player information., Test handle_whoami_command() handles missing persistence., Test handle_whoami_command() handles player not found., test_handle_whoami_command(), test_handle_whoami_command_no_persistence(), test_handle_whoami_command_player_not_found()

### Community 1228 - "FastAPI Best Practices"
Cohesion: 0.22
Nodes (9): 1. Code Organization: Domain-Driven Modularity, 2. Type Hints: Mandatory Everywhere, 3. Dependency Injection: Decouple Components, 4. API Design: Versioning & Thin Endpoints, 5. Error Handling: Use `HTTPException`, 6. Performance: Async-First & Production Deployment, 7. Security: Environment Variables & Auth, 8. Logging: Structured & Centralized (+1 more)

### Community 1229 - "test_quest_start_by_trigger_then_abandon"
Cohesion: 0.31
Nodes (9): integration, _make_shared_session_factory(), asyncio, serial, Integration: start leave_the_tutorial, get_quest_log shows it, abandon, log…, Start quest via start_quest_by_trigger(room), then abandon. Verifies trigger-…, Return a callable that behaves like a session maker but always yields the same…, test_quest_start_by_trigger_then_abandon() (+1 more)

### Community 1230 - "TestCheckRateLimit"
Cohesion: 0.33
Nodes (4): Test _check_rate_limit function., Test _check_rate_limit returns None when allowed., Test _check_rate_limit returns result when blocked., TestCheckRateLimit

### Community 1231 - "ModalContainer.tsx"
Cohesion: 0.24
Nodes (5): maxWidthClasses, ModalContainer(), ModalContainerProps, renderOpenModal(), useModalEscapeKey()

### Community 1232 - "handle_admin_command"
Cohesion: 0.32
Nodes (7): handle_admin_command(), _handle_admin_status_command(), _handle_admin_time_command(), Any, Expose current Mythos time metadata, active holidays, and freeze diagnostics., Entry point for general admin commands that expose subcommands like `admin…, Provide contextual status information about the caller's administrative…

### Community 1233 - "RoomMapEditor"
Cohesion: 0.28
Nodes (4): UseRoomMapDataOptions, useRoomMapEditorSelection(), RoomMapEditor(), useRoomMapDataMock

### Community 1235 - "._attack_target_impl"
Cohesion: 0.20
Nodes (5): Resolve attack_damage from behavior config with robust typing., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target., Attack a specific target., Handle attacking target action.

### Community 1236 - "optimized_validate_target_player"
Cohesion: 0.25
Nodes (8): Test validating empty target player name., Test validating valid target player name., Test validating invalid target player name., test_optimized_validate_target_player_empty(), test_optimized_validate_target_player_invalid(), test_optimized_validate_target_player_valid(), optimized_validate_target_player(), Optimized validation for target player fields. Args: value: The target player…

### Community 1238 - "Room Pathing Validator Implementation Spec"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1239 - "validator.py CLI"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1240 - "gh-stack"
Cohesion: 0.25
Nodes (8): Agent rules, Exit codes and error recovery, gh-stack, Known limitations, Output conventions, Prerequisites, Quick reference, When to use this skill

### Community 1241 - "MythosMUD Commit Messages"
Cohesion: 0.25
Nodes (8): GH Stack Skill, Commit Messages Skill, Examples, Format, MythosMUD Commit Messages, Rules, Template, Types

### Community 1242 - "Step 2: Ask UX-Focused Questions"
Cohesion: 0.25
Nodes (8): Teach Impeccable Skill, Accessibility & Inclusion, Aesthetic Preferences, Brand & Personality, Step 1: Explore the Codebase, Step 2: Ask UX-Focused Questions, Step 3: Write Design Context, Users & Purpose

### Community 1243 - "run-vitest.js"
Cohesion: 0.25
Nodes (7): args, clientRoot, __dirname, env, __filename, vitest, vitestBin

### Community 1244 - "usePerformanceMonitor.ts"
Cohesion: 0.29
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 1245 - "cli.sh"
Cohesion: 0.39
Nodes (6): download(), download_cli(), download_file(), get_latest_version(), handle_rate_limit(), cli.sh script

### Community 1246 - "Earth Plane"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1247 - "emotes.schema.json"
Cohesion: 0.06
Nodes (31): additionalProperties, additionalProperties, properties, required, type, items, type, uniqueItems (+23 more)

### Community 1248 - "1. Enhanced ChatPanel (New Chat Input Panel)"
Cohesion: 0.25
Nodes (8): 1. Enhanced ChatPanel (New Chat Input Panel), 2. Renamed Game Log Panel (Formerly ChatPanel), ChatPanel Layout Structure, Enhanced ChatPanel Interface, Game Log Panel Layout Structure, New Features to Add, Proposed Changes, Purpose and Functionality

### Community 1249 - "✅ Verified Already Implemented"
Cohesion: 0.25
Nodes (8): 10. TLS Configuration, 4. Connection Pool Cleanup, 5. Mute Data Caching, 6. F-String Logging, 7. Database Flush Operations, 8. Active Player Filtering, 9. NATS Connection Pooling, ✅ Verified Already Implemented

### Community 1250 - "Implementation Phases"
Cohesion: 0.25
Nodes (8): 1.1 Enhance CircuitBreaker Class, 1.2 Create CircuitBreaker Manager, 1.3 Add Configuration Support, 5.1 Authentication Operations, 5.2 Rate Limiting Integration, Implementation Phases, Phase 1: Core Infrastructure Enhancement, Phase 5: Authentication and Security

### Community 1251 - "Multiplayer Architecture Planning"
Cohesion: 0.25
Nodes (8): Performance Optimization Summary, Alias System Implementation Plan, Chat System Implementation Plan, Planning Completion Summary, Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 1252 - "API Endpoints (Phase 2)"
Cohesion: 0.25
Nodes (8): API Endpoints (Phase 2), Detailed File Migration Instructions, `server/api/containers.py`, `server/api/players.py`, `server/api/rooms.py`, `server/services/combat_service.py`, `server/services/user_manager.py`, Services (Phase 4)

### Community 1253 - "✅ Phase 2 Async Persistence Migration - COMPLETE"
Cohesion: 0.25
Nodes (7): 🏆 Achievement Summary, 📝 Git Commit Message, 📋 Migration Checklist, 🎯 Mission Accomplished, Phase 1 + Phase 2 Complete, ✅ Phase 2 Async Persistence Migration - COMPLETE, Status**: ✅**100% COMPLETE

### Community 1254 - "Python Code Coverage Status"
Cohesion: 0.22
Nodes (8): Critical Files Below Threshold, Immediate Priority (Critical Files), Normal Files Below 70% Threshold, Priority Recommendations, Python Code Coverage Status, Secondary Priority (Normal Files), Showing top 50 files with largest coverage gaps, Summary

### Community 1255 - "pyrightconfig.json"
Cohesion: 0.25
Nodes (7): extends, extraPaths, pythonVersion, venv, venvPath, ., ./pyproject.toml

### Community 1256 - "enum"
Cohesion: 0.25
Nodes (8): catholic, islamic, jewish, mythos, neo_pagan, tradition, enum, type

### Community 1257 - "main"
Cohesion: 0.36
Nodes (7): main(), cursor, Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial),…, Create quest_definitions, quest_instances, quest_offers tables and indexes., Insert leave_the_tutorial quest definition and room offer (idempotent)., _run_quest_ddl(), _seed_leave_the_tutorial()

### Community 1258 - "migrate_file"
Cohesion: 0.36
Nodes (7): main(), migrate_file(), MigrationResult, NamedTuple, Path, Result of a file migration., Migrate a single file to use async persistence patterns. Args: file_path: Path…

### Community 1259 - "apply_migration"
Cohesion: 0.36
Nodes (7): apply_migration(), check_schema(), main(), Cursor, Path, Check current schema of npc_spawn_rules table, Apply the migration to rename columns

### Community 1260 - "generate_sql.mjs"
Cohesion: 0.25
Nodes (8): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Static Data SQL Generation, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 1261 - "validate.mjs"
Cohesion: 0.32
Nodes (7): ajv, __dirname, __filename, loadJson(), main(), root, validateFile()

### Community 1262 - "Invite"
Cohesion: 0.17
Nodes (7): Get all unused invites., Invite, Base, Model for user registration invites., Check if the invite has expired. Handles naive timestamps as UTC., Check if the invite is valid (active and not expired)., Mark this invite as used by a specific user.

### Community 1263 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_user_by_username_case_insensitive when no session is yielded., Test _load_room_cache_async logs sample room IDs when rooms are loaded…, Test _load_room_cache_async handles table not found error., Test _load_room_cache_async raises other errors., Test _query_rooms_with_exits_async handles table not found error., Test _query_rooms_with_exits_async raises other errors., test_get_user_by_username_case_insensitive_no_session() (+5 more)

### Community 1264 - "test_emote_service.py"
Cohesion: 0.26
Nodes (12): EmoteDefinition, Public emote payload returned by EmoteService lookups., Unit tests for EmoteService lookup and formatting., _service_with_emotes(), test_emote_service_init_loads_via_mock(), test_format_emote_messages(), test_format_emote_messages_unknown_raises(), test_is_emote_alias_and_get_definition() (+4 more)

### Community 1267 - ".render_map"
Cohesion: 0.20
Nodes (7): _ExitRowContext, NamedTuple, Center viewport on the character's current room so the player is in the middle…, Render a single row of vertical exits between room rows., Viewport and style context for vertical exit row rendering., Render an ASCII map as HTML. Args: rooms: List of room dictionaries with…, Render an empty map. Args: width: Viewport width height: Viewport height…

### Community 1268 - "PlayerCreationService"
Cohesion: 0.21
Nodes (9): PlayerCreationService, Any, Stats, UUID, Create a new player character with specific stats. Args: name: The player's…, Service for player creation operations., Initialize with persistence layer, schema converter, and optional instance…, Resolve starting room and tutorial instance ID. For tutorial players, returns… (+1 more)

### Community 1269 - "fixture"
Cohesion: 0.22
Nodes (9): mock_persistence(), mock_room_cache(), fixture, Create a mock persistence layer., Create a mock room cache service., Create a RoomService instance with cache., Create a sample room dictionary., room_service_with_cache() (+1 more)

### Community 1270 - "DatabaseManager"
Cohesion: 0.07
Nodes (30): DatabaseManager, get_database_url(), Get the database URL, initializing if necessary. Returns: str | None: The…, Thread-safe singleton for database management. Manages database engine, session…, Initialize the database manager., Get the database URL, initializing if necessary. Returns: str: The database URL…, Close database connections., Test get_database_url returns URL from DatabaseManager. (+22 more)

### Community 1271 - "._check_dict_condition"
Cohesion: 0.12
Nodes (8): Check if missing key condition is acceptable. Returns: True if condition…, Check list condition. Returns: True if condition passes, False if fails, None…, True if numeric game_value is strictly below bound., True if numeric game_value is strictly above bound., Check dict (range) condition., Check simple value condition. Returns: True if condition passes, False if…, Return False if this condition value blocks spawning; True otherwise., Evaluate one key from spawn_conditions; False means spawn blocked.

### Community 1272 - "test_run_make_stages.py"
Cohesion: 0.39
Nodes (6): _load_module(), Tests for scripts/run_make_stages.py fail-fast helpers., test_keep_going_requested(), test_stage_failed_from_output_nonzero(), test_stage_failed_from_output_ok(), test_stage_failed_from_output_traceback()

### Community 1273 - "verify_npc_occupants.py"
Cohesion: 0.23
Nodes (12): _check_service_availability(), _collect_npcs_by_room(), _print_summary(), Any, Verification script to check NPCs in lifecycle manager and test occupant query…, Print verification summary. Args: npc_count: Total number of active NPCs…, Verify NPCs exist in lifecycle manager and test query logic., Check if NPC service, lifecycle manager, and active_npcs are available.… (+4 more)

### Community 1277 - "optimized_validate_command_content"
Cohesion: 0.25
Nodes (8): Test validating empty command content., Test validating valid command content., Test validating command content with injection pattern., test_optimized_validate_command_content_empty(), test_optimized_validate_command_content_injection(), test_optimized_validate_command_content_valid(), optimized_validate_command_content(), Optimized validation for command content fields. Args: value: The command…

### Community 1278 - "optimized_validate_reason_content"
Cohesion: 0.25
Nodes (8): Test validating empty reason content., Test validating valid reason content., Test validating reason content with injection pattern., test_optimized_validate_reason_content_empty(), test_optimized_validate_reason_content_injection(), test_optimized_validate_reason_content_valid(), optimized_validate_reason_content(), Optimized validation for reason content fields. Args: value: The reason to…

### Community 1279 - "optimized_validate_pose_content"
Cohesion: 0.25
Nodes (8): Test validating empty pose content., Test validating valid pose content., Test validating pose content with injection pattern., test_optimized_validate_pose_content_empty(), test_optimized_validate_pose_content_injection(), test_optimized_validate_pose_content_valid(), optimized_validate_pose_content(), Optimized validation for pose content fields. Args: value: The pose to validate…

### Community 1280 - "optimized_validate_filter_name"
Cohesion: 0.25
Nodes (8): Test validating empty filter name., Test validating valid filter name., Test validating invalid filter name., test_optimized_validate_filter_name_empty(), test_optimized_validate_filter_name_invalid(), test_optimized_validate_filter_name_valid(), optimized_validate_filter_name(), Optimized validation for filter name fields. Args: value: The filter name to…

### Community 1281 - "optimized_validate_help_topic"
Cohesion: 0.25
Nodes (8): Test validating empty help topic., Test validating valid help topic., Test validating invalid help topic., test_optimized_validate_help_topic_empty(), test_optimized_validate_help_topic_invalid(), test_optimized_validate_help_topic_valid(), optimized_validate_help_topic(), Optimized validation for help topic fields. Args: value: The help topic to…

### Community 1283 - "gh-stack (MythosMUD)"
Cohesion: 0.29
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1284 - "MythosMUD ADR Authoring"
Cohesion: 0.29
Nodes (7): ADR Authoring Skill, Index Update, Location, MythosMUD ADR Authoring, Reference, Structure, Template

### Community 1285 - "MythosMUD Logging Standards"
Cohesion: 0.29
Nodes (7): Logging Standards Skill, Import, MythosMUD Logging Standards, Optional Helpers, Reference, Structured Logging, Summary

### Community 1286 - "MythosMUD Server Runbook"
Cohesion: 0.29
Nodes (7): Server Runbook Skill, Commands, Critical Rules, MythosMUD Server Runbook, ONE SERVER ONLY RULE, Pre-Start Checklist, Reference

### Community 1287 - "useGridLayout.ts"
Cohesion: 0.33
Nodes (5): layoutConfig, PanelState, STORAGE_KEYS, useGridLayout(), UseGridLayoutReturn

### Community 1288 - "mapPageRenderer.tsx"
Cohesion: 0.17
Nodes (16): RoomMapViewerProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView(), renderMapPageState(), renderStatusGate(), resolveMapViewProps() (+8 more)

### Community 1289 - "Three-Column Game UI Layout"
Cohesion: 0.29
Nodes (7): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe

### Community 1292 - "Chat Panel"
Cohesion: 0.29
Nodes (7): Chat Message Type Categorization Bug, Chat Panel, Commands Panel, Game Log Panel, Chat Message Routing Bug Fix, Room Description Routing Bug Fix, Bug Prevention Testing Strategy

### Community 1293 - "Aggro and Threat System Implementation Plan"
Cohesion: 0.29
Nodes (6): Aggro and Threat System Implementation Plan, Constants (locked), Integration with NPC static data (behavior_config / npc_type), Key Modules and Files, References, Status

### Community 1294 - "✅ POSITIVE FINDINGS"
Cohesion: 0.29
Nodes (7): 1. Excellent Error Boundary Implementation, 2. Proper Use of asyncio.gather with return_exceptions=True, 3. Task Tracking and Lifecycle Management, 4. Good Connection State Management, 5. Proper Async Context Managers, 6. Enhanced Structured Logging, ✅ POSITIVE FINDINGS

### Community 1295 - "🔴 CRITICAL ISSUES"
Cohesion: 0.29
Nodes (7): 1. Synchronous Blocking Operations in Async Context (CONFIRMED PERFORMANCE ISSUE), 2. asyncio.run() Called from Existing Event Loop Context, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Blocking Operations in NATS Message Handlers, 6. F-String Logging Destroying Structured Logging, 🔴 CRITICAL ISSUES

### Community 1296 - "✅ Positive Findings"
Cohesion: 0.29
Nodes (7): 1. Consistent Pattern Application, 2. Proper Async Propagation, 3. Exception Handling Preserved, 4. Resource Cleanup Maintained, 5. Proper Import Organization, 6. Documentation Added, ✅ Positive Findings

### Community 1297 - "🚫 Anti-Patterns NOT Found (Good!)"
Cohesion: 0.29
Nodes (7): 🚫 Anti-Patterns NOT Found (Good!), ❌ Calling async without await, ❌ Creating tasks without tracking, ❌ Global state issues, ❌ Nested event loops, ❌ Not closing resources, ❌ Using time.sleep() in async functions

### Community 1298 - "📞 Next Steps"
Cohesion: 0.50
Nodes (4): Immediate (Today), Medium-Term (Next Sprint), 📞 Next Steps, Short-Term (This Week)

### Community 1299 - "Entries"
Cohesion: 0.29
Nodes (6): 2026-02-24 — Wave 3 (Backend security) completed, 2026-02-24 — Wave 4 (Frontend security) verified, 2026-02-24 — Wave 5 (Complexity refactors), 2026-02-24 — Wave 6 (Metrics and hardening), Codacy High/Critical Remediation Progress, Entries

### Community 1300 - "Migration Workflow (Per File)"
Cohesion: 0.29
Nodes (7): Migration Workflow (Per File), Step 1: Pre-Migration Assessment, Step 2: Create Async Repository Instances, Step 3: Convert Methods to Async, Step 4: Update All Callers, Step 5: Test Migration, Step 6: Validate Performance

### Community 1301 - "Security Implementation"
Cohesion: 0.29
Nodes (7): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection, SSE Authentication System

### Community 1302 - "Recommended Decision"
Cohesion: 0.29
Nodes (7): Commit to full 2-month optimization plan, Implement gap filling only (skip pruning), Implement only Phase 1 (Quick Wins), Option A: Full Optimization (Recommended), Option B: Quick Wins Only, Option C: Strategic Focus, Recommended Decision

### Community 1303 - "3.3 Value Distribution Calculation"
Cohesion: 0.29
Nodes (7): 3.1 Scoring Criteria Matrix, 3.2 Category Scores, 3.3 Value Distribution Calculation, 🔴 CRITICAL VALUE TESTS (Score ≥75): **1,272 tests (25.6%)**, 🟡 IMPORTANT VALUE TESTS (Score 50-74): **2,943 tests (59.3%)**, 🟢 LOW VALUE TESTS (Score <50): **750 tests (15.1%)**, Phase 3: Test Value Scoring

### Community 1304 - "Projected Optimization Impact"
Cohesion: 0.29
Nodes (7): After Phase 1-3: Pruning (Month 1), After Phase 4: Consolidation (Month 2), After Phase 5: Gap Filling (Month 2), Current State (Baseline), Final State Comparison, Net Benefit, Projected Optimization Impact

### Community 1305 - "Command Handler Patterns"
Cohesion: 0.29
Nodes (7): Command Handler Patterns, Command Models Reference, Pydantic Command Models, Command Security Guide, Command Role-Based Access Control, Command Testing Guide, Command Test-Driven Development

### Community 1306 - "AsyncPersistenceLayer Pattern"
Cohesion: 0.38
Nodes (7): AsyncPersistenceLayer Pattern, Database Access Patterns, Eager Loading Best Practices, SQLAlchemy ORM Pattern, AsyncPG Connection Pool, Database Pool Configuration, SQLAlchemy Connection Pool

### Community 1307 - "Respawn Subsystem"
Cohesion: 0.33
Nodes (7): Limbo Room Death State, PlayerRespawnService, Respawn Subsystem, Determination Points (DP), Incapacitation (DP 0 to -9), no_death Rooms (ADR-009), Status Effects Subsystem

### Community 1308 - "Attack Command Not Starting Combat"
Cohesion: 0.29
Nodes (7): Attack Command Not Starting Combat, CommandType Enum vs String Comparison, Target Resolution via Lifecycle Manager, NPC Dual Tracking System Issue, Stale Room.get_npcs After Persistence Reload, NPC Spawning vs Occupants Display Issue, Flattened Occupants Losing Player NPC Distinction

### Community 1309 - "Second NPC Combat And Linkdead Findings"
Cohesion: 0.29
Nodes (7): Coroutine Object Has No current_room_id, Combat Start Missing Await get_player_by_name, get_player_by_id vs async_get_player Mismatch, XP Award async_get_player Missing Method, Linkdead WebSocket Grace Period, Second NPC Combat And Linkdead Findings, Stale Queued Attack Target Validation

### Community 1310 - "Multi-Word Spell Name Parsing Failure"
Cohesion: 0.29
Nodes (7): Missing cast spell spells Pydantic Models, Spell Slash Commands Missing From Validation, create_cast_command First-Word-Only Parse, Multi-Word Spell Name Parsing Failure, Missing async_heal_player Method, record_spell_cast Cross-Session Object Use, Heal Spell SQLAlchemy Session Boundary Error

### Community 1312 - "Disconnect Grace Period and Rest Command"
Cohesion: 0.29
Nodes (7): Disconnect Grace Period and Rest Command, Rest Command, 30-Second Disconnect Grace Period, ADR-009 Effects System Architecture, LOGIN_WARDED Effect, Effects System ADR and Implementation, Effects System Implementation

### Community 1313 - "main"
Cohesion: 0.38
Nodes (6): generate_html_visualization(), load_room_data(), main(), Load all room and intersection data from the zone directory., Main function to generate the HTML visualization., Generate an HTML visualization of the room network.

### Community 1315 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1316 - "test_websocket_room_updates.py"
Cohesion: 0.05
Nodes (56): Update player's room subscription and current room., update_player_room_subscription(), mock_connection_manager(), mock_room(), asyncio, fixture, Unit tests for WebSocket room updates. Tests the websocket_room_updates module…, Test get_player_occupants() returns empty list when no occupants. (+48 more)

### Community 1318 - "BehaviorEngine"
Cohesion: 0.12
Nodes (13): BehaviorEngine, Deterministic behavior engine for NPCs. This engine evaluates rules based on…, Initialize the behavior engine., Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…, Get the behavior engine for this NPC., Test _evaluate_equality() handles boolean false., Test _evaluate_numeric_comparison() handles < operator., Test _evaluate_numeric_comparison() returns None for invalid format. (+5 more)

### Community 1320 - "CombatConfigurationService"
Cohesion: 0.14
Nodes (11): CombatConfigurationService, get_combat_configuration(), Get current combat configuration. Returns: CombatConfiguration: Current combat…, Get combat configuration for a specific scope. Args: scope: Configuration scope…, Clear all configuration overrides., Validate combat configuration. Args: config: Optional configuration to validate…, Check if combat is available for a specific player/room. Args: player_id:…, Refresh configuration from source. (+3 more)

### Community 1326 - "websocket_integration.py"
Cohesion: 0.05
Nodes (31): Client, WebSocket, auth_service, authenticate_websocket_connection(), chat_service, game_service, handle_chat_message(), handle_game_action() (+23 more)

### Community 1327 - "Thinking about stack structure"
Cohesion: 0.33
Nodes (6): Branch naming, Dependency chain, One stack, one story, Staging changes deliberately, Thinking about stack structure, When to create a new branch

### Community 1329 - "Extract Skill"
Cohesion: 0.33
Nodes (6): Extract Skill, Discover, Document, Extract & Enrich, Migrate, Plan Extraction

### Community 1330 - "codacy.yaml Tool Manifest"
Cohesion: 0.33
Nodes (6): codacy.yaml Tool Manifest, Lizard Complexity Tool Pin, Trivy Codacy Tool Pin, MythosMUD Codacy Tool Suite, Grype Local vs Trivy Codacy SCA, Manually Managed codacy.yaml

### Community 1331 - "MythosMUD Server Test Suite"
Cohesion: 0.33
Nodes (6): Command Tests Relocated, server/tests/unit/commands/, Integration Test Tier, make test-server, MythosMUD Server Test Suite, Unit Test Tier

### Community 1332 - "_run_dialogue_ddl"
Cohesion: 0.40
Nodes (5): main(), cursor, Create dialogue_definitions table if missing in the given schema., Connect via DATABASE_URL and ensure dialogue_definitions exists., _run_dialogue_ddl()

### Community 1334 - "Common Test Failure Categories"
Cohesion: 0.33
Nodes (6): 1. Database Test Failures, 2. Authentication Test Failures, 3. WebSocket Test Failures, 4. Game Logic Test Failures, 5. Integration Test Failures, Common Test Failure Categories

### Community 1335 - "Azotottal.md"
Cohesion: 0.33
Nodes (3): Azotottal, Comte Fenalik, The Old Gods (nameless patrons)

### Community 1336 - "Any"
Cohesion: 0.12
Nodes (20): _get_event_handler_for_test_occupants(), _get_room_id_for_test_occupants(), Any, Resolve application, player, room_id, and event handler for NPC test occupants…, Get room_id from args or current room. Returns (room_id, error_result)., Get event handler from app.state. Returns (event_handler, error_result)., Resolve application and player object for NPC test occupants command., Resolve room_id and event handler for NPC test occupants command. (+12 more)

### Community 1337 - "Chat Panel Separation Specification"
Cohesion: 0.29
Nodes (6): Chat Panel Separation Specification, Conclusion, Current Integration Points, Current State Analysis, Existing Structure, Overview

### Community 1338 - "🔍 Anti-Pattern Check"
Cohesion: 0.33
Nodes (6): 🔍 Anti-Pattern Check, ❌ Blocking Calls in Async Functions?, ❌ Ignoring Exceptions?, ❌ Long-Running Coroutines?, ❌ Missing `await` Keywords?, ❌ Unstructured Concurrency?

### Community 1339 - "📚 Documentation Created"
Cohesion: 0.33
Nodes (6): 1. Comprehensive Audit Report, 2. Executive Summary, 3. Developer Quick Reference, 4. Migration Tracker, 5. Test Suite, 📚 Documentation Created

### Community 1340 - "Implementation Details"
Cohesion: 0.33
Nodes (6): CircuitBreaker Manager, Database Operations, Enhanced CircuitBreaker Class, Implementation Details, Integration Examples, NATS Operations

### Community 1341 - "Summary (from Codacy UI snapshot)"
Cohesion: 0.33
Nodes (5): Codacy High/Critical Baseline – MythosMUD, Distribution notes, Example issue types, Summary (from Codacy UI snapshot), Top code patterns by issue count

### Community 1342 - "Core Logging Principles"
Cohesion: 0.33
Nodes (6): 1. **Structured Logging**, 2. **Context is Everything**, 3. **Security First**, 4. **Performance Aware**, 5. **Actionable Information**, Core Logging Principles

### Community 1343 - "Performance Logging"
Cohesion: 0.67
Nodes (3): API Request Logging, Database Query Logging, Performance Logging

### Community 1344 - "Common Mistakes and How to Fix Them"
Cohesion: 0.33
Nodes (6): Common Mistakes and How to Fix Them, Mistake 1: Forgetting to Update Imports, Mistake 2: Using Deprecated Context Parameter, Mistake 3: String Formatting in Log Messages, Mistake 4: Missing Context in Error Logs, Mistake 5: Wrong Log Levels

### Community 1345 - "Enhanced Logging Features"
Cohesion: 0.33
Nodes (6): Correlation IDs, Enhanced Logging Features, Exception Tracking, MDC (Mapped Diagnostic Context), Performance Monitoring, Security Sanitization

### Community 1346 - "Log Levels and Usage"
Cohesion: 0.33
Nodes (6): CRITICAL, DEBUG, ERROR, INFO, Log Levels and Usage, WARNING

### Community 1347 - "Enhanced Logging Migration Report"
Cohesion: 0.33
Nodes (5): Enhanced Logging Features, Enhanced Logging Migration Report, Next Steps, Successfully Updated Files, Summary

### Community 1348 - "Mythos Holiday Candidates"
Cohesion: 0.33
Nodes (5): Canonical and Derived Observances, Implementation Notes, Mythos Holiday Candidates, Narrative Flavor Seeds, Opportunities for Expansion

### Community 1349 - "NPC Startup Duplication Analysis"
Cohesion: 0.33
Nodes (6): NPC Duplication Bug Fix Plan, NPC Population Field Rename, NPC Lifecycle Manager, NPC Population Controller, NPC Startup Duplication Analysis, NPC Startup Service

### Community 1350 - "💡 Key Improvements"
Cohesion: 0.33
Nodes (6): 1. Eliminated Event Loop Blocking, 2. Consistent Async Patterns, 3. Proper Error Handling, 4. Resource Management, 5. Performance Optimization, 💡 Key Improvements

### Community 1351 - "PostgreSQL Procedures Migration - Audit Spreadsheet"
Cohesion: 0.33
Nodes (5): Audit Table, Domain Grouping Summary, Existing PostgreSQL Functions (Already in DDL), PostgreSQL Procedures Migration - Audit Spreadsheet, Scope

### Community 1352 - "Real-Time Communication (WebSocket)"
Cohesion: 0.33
Nodes (5): Authentication and Token in URL, Connection Grace Periods, Deprecated Endpoints, Production: HTTPS and WSS, Real-Time Communication (WebSocket)

### Community 1353 - "Implementation Approach Decision"
Cohesion: 0.33
Nodes (6): Alternative: **GREENFIELD REWRITE**, Cons, Implementation Approach Decision, Pros, Recommended: **PHASED UPLIFT**, Would Choose If

### Community 1354 - "Backward Compatibility Strategy"
Cohesion: 0.33
Nodes (6): Backward Compatibility Strategy, Layer 1: New Tests (Use Container), Layer 2: Updated Tests (Hybrid), Layer 3: Legacy Tests (Unchanged), Migration Flags, Three-Layer Compatibility

### Community 1355 - "Test Suite Analysis"
Cohesion: 0.33
Nodes (6): Current Test Organization, Dependency Access Patterns, Pattern 1: Direct app.state Access (Broken - 445 instances), Pattern 2: Using Real Lifespan (Works - Limited), Pattern 3: Fixture-Based Mocking (Mixed), Test Suite Analysis

### Community 1356 - "Modern Testing Patterns"
Cohesion: 0.33
Nodes (6): Modern Testing Patterns, Pattern 1: Container-Based Fixtures, Pattern 2: Mock Container for Unit Tests, Pattern 3: Parametrized Integration Tests, Pattern 4: Fixture Factories, Pattern 5: Async Test Context Managers

### Community 1357 - "Test Modernization Checklist"
Cohesion: 0.33
Nodes (6): Phase 0: Foundation, Phase 1: Fix Failures, Phase 2: Modernize Units, Phase 3: Pattern Updates, Phase 4: New Coverage, Test Modernization Checklist

### Community 1358 - "Testing Requirements"
Cohesion: 0.33
Nodes (6): Phase 0 Testing, Phase 1 Testing, Phase 2 Testing, Phase 3 Testing, Phase 4 Testing, Testing Requirements

### Community 1359 - "Test Suite Optimization Roadmap"
Cohesion: 0.33
Nodes (5): Recommended Execution Order, Risk Mitigation Strategy, Rollback Plan, Safety Measures, Test Suite Optimization Roadmap

### Community 1360 - "Phase 5: Strategic Additions (Week 5)"
Cohesion: 0.33
Nodes (6): Phase 5: Strategic Additions (Week 5), Task 5.1: Add MessageBroker Integration Tests (3 hours), Task 5.2: Add ApplicationContainer Lifecycle Tests (2 hours), Task 5.3: Add Database Migration Tests (3 hours), Task 5.4: Add WebSocket Edge Case Tests (4 hours), Task 5.5: Add Error Recovery Tests (3 hours)

### Community 1361 - "Measurement and Validation"
Cohesion: 0.33
Nodes (6): After Each Phase, Before Starting Optimization, Capture Baseline, Measurement and Validation, Verify Metrics, Weekly Dashboard

### Community 1362 - "Quest System Features"
Cohesion: 0.40
Nodes (6): Quest Design Guidelines, Quest Design Principles, Quest System Features, Event-Driven Quest Progression, Quest Goal Types, Declarative YAML Quest Config

### Community 1363 - "Testing Guide"
Cohesion: 0.40
Nodes (6): Quick Start E2E Tests, E2E Test Server Quick Start, bcrypt PyO3 Fresh Session Limitation, Testing Guide, Pydantic Testing Patterns, Two-Tier Test Suite (make test)

### Community 1364 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 1365 - "NPC Occupants Verification Summary"
Cohesion: 0.33
Nodes (6): NPC Display Final Fixes, room_update Overwriting NPC Data, asyncpg UUID replace AttributeError, Legacy Occupants Snapshot Format, NPC Occupants Verification Summary, Rooms API User Object AttributeError

### Community 1366 - "Combat Client Crash"
Cohesion: 0.33
Nodes (6): event_data vs data Field Name Mismatch, NATS Event Message Field Mismatch, Combat Client Crash, CombatMessaging Connection Manager Init Failure, Combat Disconnect At NPC Death, Passive Lucidity Flux Performance Degradation

### Community 1367 - "Respawn Death Screen Loop Limbo ID Mismatch"
Cohesion: 0.33
Nodes (6): limbo_death_void vs limbo_death_void_limbo_death_void, Respawn Death Screen Loop Limbo ID Mismatch, SQLAlchemy JSONB Mutation Detection, Respawn Persistence JSONB Mutation Failure, Death Threshold and Posture Bugs, HP -10 Limbo Transition Delay

### Community 1368 - "NPC Combat Start Race Condition"
Cohesion: 0.33
Nodes (6): NPC Combat Start Race Condition, Redundant NPC Instance Lookup Failure, NPCs Incorrectly Marked is_alive False, December 3 Final Investigation Summary, Character Info Panel Missing Stats Field, Room Occupants Duplicates and Missing Player

### Community 1369 - "Round-Based Combat"
Cohesion: 0.33
Nodes (6): Combat Action Queue, Combat Bugs Investigation and Fixes, Round-Based Combat, Combat Round System Refactor, First Weapon Switchblade, Flee Command and Effect

### Community 1370 - "WebSocket-Only Migration"
Cohesion: 0.33
Nodes (6): SSE Connection Removal, Unified Client Message Pipeline, Unify Client Message Handling, WebSocket Best-Practices Remediation, WebSocket-Only Architecture, WebSocket-Only Migration

### Community 1371 - ".broadcast_player_mortally_wounded"
Cohesion: 0.17
Nodes (7): Any, Broadcast player respawn message to all players in the room., Send DP decay message to a specific mortally wounded player., Build personal and room messages for mortally wounded broadcast., Send mortally wounded personal message. Logs warning on failure., Broadcast player mortally wounded to room. Sends personal message to wounded…, Broadcast player death message to all players in the room.

### Community 1372 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test rescue() returns error when rescuer is not found., Test rescue() sets delta to 1 when delta is zero or negative., Test rescue() handles errors during lucidity adjustment., Test rescue() handles event dispatcher errors gracefully., Test rescue() dispatches events for both target and rescuer., Test rescue() handles player_id as UUID strings., test_rescue_apply_lucidity_error() (+5 more)

### Community 1373 - "check_file_for_logging_issues"
Cohesion: 0.47
Nodes (5): check_file_for_logging_issues(), main(), Path, Check a single file for logging consistency issues. Args: file_path: Path to…, Main function to check all service files for logging consistency.

### Community 1374 - "test_profession.py"
Cohesion: 0.11
Nodes (17): Unit tests for the Profession model. Tests the Profession model methods…, Test meets_stat_requirements returns True when stats exactly match requirements., Test meets_stat_requirements returns False when required stat is missing., Test is_available_for_selection returns True when is_available is True., Test get_requirement_display_text formats single requirement correctly., Test get_stat_requirements returns dict for valid JSON., Test get_requirement_display_text capitalizes stat names., Test get_stat_requirements returns empty dict for invalid JSON. (+9 more)

### Community 1375 - "e2e_reset_players.py"
Cohesion: 0.47
Nodes (5): _load_default_respawn_room(), main(), Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the…, Entry point: run E2E player reset via anyio., _reset_e2e_players()

### Community 1376 - "add_suppression_to_file"
Cohesion: 0.47
Nodes (5): add_suppression_to_file(), main(), Path, Add suppression comment to a PowerShell file if it uses Write-Host and doesn't…, Process all PowerShell scripts in the scripts directory.

### Community 1377 - ".shutdown_all"
Cohesion: 0.17
Nodes (6): Cancel lifecycle/critical tasks first (Phase 1)., Cancel remaining active tasks (Phase 2)., Wait for task completion with timeout., Forcibly cancel any lingering tasks that didn't respond to graceful…, Clean up active collections after final shutdown., Gracefully shutdown all tracked tasks with timeout coordination. Implements…

### Community 1378 - "_get_container_description"
Cohesion: 0.17
Nodes (12): _get_container_description(), Get container description from prototype registry., Test getting container description from equipped item., Test getting container description from container metadata., Test getting container description when registry is None., Test getting container description when prototype_id is missing., Test getting container description handles prototype errors., test_get_container_description_from_container_metadata() (+4 more)

### Community 1379 - "._compute_player_context"
Cohesion: 0.25
Nodes (4): Get list of player IDs currently in the room. Returns: List of player IDs in…, Debug log for context enrichment (best-effort, must not fail)., Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…, Get player_in_range, enemy_nearby, and target_id from persistence. Returns…

### Community 1380 - ".process_tick_regeneration"
Cohesion: 0.23
Nodes (7): Any, UUID, Get MP regeneration multiplier based on player state. Args: stats: Player stats…, Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…, Restore MP from meditation (highly accelerated regeneration). Args: player_id:…, Restore MP from consuming an item. Args: player_id: Player ID amount: Amount of…, Process MP regeneration for a player on a game tick. Args: player_id: Player ID…

### Community 1381 - "get_engine"
Cohesion: 0.29
Nodes (7): get_engine(), AsyncEngine, Get the database engine, initializing if necessary. Returns: AsyncEngine: The…, Test get_engine returns engine from DatabaseManager., Test get_engine raises ValidationError when database cannot be initialized., test_get_engine(), test_get_engine_raises_validation_error()

### Community 1382 - "reset_database"
Cohesion: 0.29
Nodes (7): Reset database state for testing. This function resets the DatabaseManager…, reset_database(), fixture, Reset database state before each test., Test reset_database resets DatabaseManager singleton and module state., reset_db(), test_reset_database()

### Community 1383 - "test_message_filtering.py"
Cohesion: 0.17
Nodes (9): Unit tests for message filtering. Tests the MessageFilteringHelper class., Test is_player_muted_by_receiver() checks mute status., Test _get_user_manager() returns global user manager when custom not set., Test collect_room_targets() returns subscribed players., Test collect_room_targets() returns empty set when no subscribers., test_collect_room_targets(), test_collect_room_targets_empty(), test_get_user_manager_global() (+1 more)

### Community 1384 - ".__init__"
Cohesion: 0.38
Nodes (4): Any, Initialize LucidityAdjustmentLog with defaults., Initialize LucidityExposureState with defaults., Initialize PlayerLucidity with defaults.

### Community 1385 - "Enhanced Structured Logging System"
Cohesion: 0.40
Nodes (6): bind_request_context, Dual Logging (warnings/errors aggregators), Enhanced Structured Logging System, F-String Logging Anti-Pattern, get_logger, sanitize_sensitive_data Processor

### Community 1386 - "test_player_event_handlers_respawn.py"
Cohesion: 0.17
Nodes (11): Unit tests for player respawn event handlers. Tests the…, Test send_respawn_event_with_retry() waits for connection to become available., Test PlayerRespawnEventHandler initialization., Test update_connection_manager_position() updates position., Test update_connection_manager_position() handles player not in online_players., Test update_connection_manager_position() handles missing online_players…, test_player_respawn_event_handler_init(), test_send_respawn_event_with_retry_waits_for_connection() (+3 more)

### Community 1387 - ".select_exit"
Cohesion: 0.18
Nodes (6): _cfg_bool(), Calculate weight for an exit based on distance from spawn. Args:…, Calculate weights for all exits. Args: valid_exits: Dictionary of direction ->…, Select exit based on weighted probabilities. Args: exit_weights: List of…, Select an exit using weighted random selection favoring exits closer to spawn…, Calculate approximate distance between two rooms. This is a simplified distance…

### Community 1388 - "UUID"
Cohesion: 0.20
Nodes (6): UUID, Check if a player is currently disconnecting. Args: player_id: The player's ID…, Check if a player is currently in grace period after disconnect. Args:…, Normalize player ID to UUID format. Args: player_id: The player's ID (UUID or…, Get player information and name (async version). Args: player_id: The player's…, Normalize event IDs to strings for comparison and logging. Args: player_id: The…

### Community 1389 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test send_room_update_to_player() successfully sends room update., Test query_room_occupants_snapshot() queries occupants., Test send_room_updates_to_entering_player() handles invalid player_id., Test handle_player_entered() handles errors., Test log_player_movement() handles errors., test_handle_player_entered_error_handling(), test_log_player_movement_error_handling() (+3 more)

### Community 1390 - "is_argon2_hash"
Cohesion: 0.20
Nodes (10): is_argon2_hash(), Check if a given string is an Argon2 hash., Test is_argon2_hash with valid Argon2 hash., Test is_argon2_hash with invalid hash., Test is_argon2_hash with None., Test is_argon2_hash with non-string type., test_is_argon2_hash_invalid(), test_is_argon2_hash_non_string() (+2 more)

### Community 1391 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 1392 - "extract_zone_name"
Cohesion: 0.20
Nodes (10): extract_zone_name(), Extract zone name from stable_id (format: 'plane/zone'). Args: stable_id: The…, Test extract_zone_name() extracts zone from stable_id., Test extract_zone_name() returns stable_id when no slash., Test extract_zone_name() extracts from first slash., Test extract_zone_name() handles empty string., test_extract_zone_name_empty(), test_extract_zone_name_multiple_slashes() (+2 more)

### Community 1393 - "NATSRequestError"
Cohesion: 0.29
Nodes (4): NATSRequestError, Exception, Raised when request/response operations fail., Send a request to a NATS subject and wait for a response. Args: subject: NATS…

### Community 1394 - "test_async_persistence_delegates.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: health, container, item, singleton,…, Test validate_and_fix_player_room delegates to PlayerRepository., Test item_instance_exists delegates to ItemRepository., Test PLAYER_COLUMNS constant is defined., Test PROFESSION_COLUMNS constant is defined., test_item_instance_exists_delegates(), test_player_columns_constant(), test_profession_columns_constant() (+1 more)

### Community 1396 - "get_async_session"
Cohesion: 0.05
Nodes (55): add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., fetch_professions(), fetch_user_by_username_case_insensitive(), Profession, Get a user by username (case-insensitive). MULTI-CHARACTER: Usernames are… (+47 more)

### Community 1397 - "usePlayerStatusEffects.ts"
Cohesion: 0.39
Nodes (8): currentDpOf(), getCurrentLucidity(), markPlayerDead(), PlayerStatusSetters, skipDeadInRespawnRoom(), syncDeathState(), syncDeliriumState(), usePlayerStatusEffects()

### Community 1398 - "populate_test_npc_databases.py"
Cohesion: 0.31
Nodes (8): get_npc_data_from_source(), get_npc_database_url(), main(), populate_database(), Populate a PostgreSQL database with NPC data. Args: target_url: PostgreSQL…, Main function to populate test NPC databases., Get NPC database URL for the specified environment. Args: environment:…, Extract NPC data from the source PostgreSQL database. Args: source_url:…

### Community 1399 - "RoomBasedChannelStrategy"
Cohesion: 0.33
Nodes (5): Strategy for room-based channels (say, local, emote, pose)., Initialize room-based channel strategy. Args: channel_type: Type of room-based…, RoomBasedChannelStrategy, Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., test_channel_broadcasting_strategy_factory_get_strategy_known()

### Community 1400 - "stop_health_checks_impl"
Cohesion: 0.40
Nodes (4): Stop the periodic health check task., stop_health_checks_impl(), Stop the periodic health check task., test_stop_health_checks_impl()

### Community 1401 - ".optimize_payload"
Cohesion: 0.28
Nodes (5): Any, Create an incremental update payload containing only changed fields. Args:…, Calculate the size of a payload in bytes. Args: payload: The payload dictionary…, Compress a large payload using gzip compression. Args: payload: The payload…, Optimize a payload by applying size limits and compression if needed. Args:…

### Community 1402 - "test_inventory_mutation_guard_error_handling.py"
Cohesion: 0.13
Nodes (17): guard(), asyncio, fixture, Unit tests for inventory mutation guard - error handling and monitoring. Tests…, Test acquire_async handles record_custom_alert with message parameter., Test acquire handles TypeError from record_custom_alert and uses fallback., Test acquire_async handles TypeError from record_custom_alert and uses fallback., Create an InventoryMutationGuard instance. (+9 more)

### Community 1403 - "test_error_logging.py"
Cohesion: 0.05
Nodes (46): create_error_context(), Any, Request, Create error context from request and user. Helper function to reduce…, Unit tests for server.api.player_helpers (error context helper)., When current_user is None, context gets metadata only., When current_user is set, user_id is populated and metadata merged., test_create_error_context_with_user_sets_user_id_and_metadata() (+38 more)

### Community 1404 - "Protocol"
Cohesion: 0.22
Nodes (9): _HasId, _HasIsAdmin, _HasIsSuperuser, _HasUsername, Protocol, Narrowing for user shapes that expose is_superuser., Narrowing for user shapes that expose is_admin., Narrowing for user shapes that expose username. (+1 more)

### Community 1405 - "lucidity_communication_dampening.py"
Cohesion: 0.39
Nodes (8): _apply_receiver_effects(), _apply_sender_effects(), DampeningResult, _maybe_muffle_fractured_message(), _maybe_scramble_deranged_message(), TypedDict, Communication dampening utilities for lucidity system. Implements communication…, Filtered chat payload after lucidity-tier effects.

### Community 1406 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1407 - "TestValidateCommandBasics"
Cohesion: 0.20
Nodes (6): Test _validate_command_basics function., Test _validate_command_basics returns result for empty command., Test _validate_command_basics returns result for command too long., Test _validate_command_basics returns result for invalid command content., Test _validate_command_basics returns None for valid command., TestValidateCommandBasics

### Community 1408 - "ensure_directory_exists"
Cohesion: 0.25
Nodes (8): ensure_directory_exists(), Ensure a directory exists and return its absolute path. Args: directory: The…, Test ensure_directory_exists with existing directory., Test ensure_directory_exists creates directory if it doesn't exist., Test ensure_directory_exists with relative path., test_ensure_directory_exists_creates(), test_ensure_directory_exists_existing(), test_ensure_directory_exists_relative_path()

### Community 1409 - "Any"
Cohesion: 0.13
Nodes (9): Any, Process room update with comprehensive validation. Args: room_data: Room data…, Invalidate stale room cache entry. Args: room_id: Room ID to invalidate…, Fetch fresh room data from room service. Args: room_id: Room ID to fetch…, Handle stale room data by requesting fresh data. Args: room_data: Stale room…, Process room transition with proper ordering and validation. Args:…, Get statistics about the room data cache. Returns: Dict[str, Any]: Cache…, Initialize the room synchronization service. Args: room_service: Optional… (+1 more)

### Community 1410 - "_default_cors_origins"
Cohesion: 0.29
Nodes (7): _default_cors_origins(), Derive default CORS origins with environment taking precedence., test_default_cors_origins_fallback(), Test default CORS origins when no env vars set., Test default CORS origins with env var set., test_default_cors_origins_no_env(), test_default_cors_origins_with_env()

### Community 1412 - "test_combat_grace_period.py"
Cohesion: 0.14
Nodes (17): mock_connection_manager(), mock_persistence(), mock_request(), asyncio, fixture, Unit tests for combat command blocking during login grace period. Tests that…, Test that attack commands work when player is not in grace period., Attack command returns incapacitated message when player has 0 to -9 DP (prone,… (+9 more)

### Community 1413 - "JsonMap"
Cohesion: 0.09
Nodes (24): mock_prototype_registry(), fixture, JsonMap, Test finding container in room with instance number., Test finding container in room with invalid instance number., Test formatting container display with basic info., Test formatting container display with target_type container., Create a sample container. (+16 more)

### Community 1415 - "MythosMUD COPPA Checklist"
Cohesion: 0.40
Nodes (5): COPPA Checklist Skill, Checklist, Implementation, MythosMUD COPPA Checklist, Reference

### Community 1416 - "ConnectionPanel.tsx"
Cohesion: 0.50
Nodes (3): ConnectionPanel(), ConnectionPanelProps, localStorageMock

### Community 1418 - "global-teardown.ts"
Cohesion: 0.40
Nodes (3): __dirname, __filename, projectRoot

### Community 1419 - "AI PR Reviewer Instructions"
Cohesion: 0.40
Nodes (5): AI PR Reviewer Instructions, COPPA and Security Review Mandates, Review Coverage Thresholds, player_id UUID Type Rule, Server Authority Review Rule

### Community 1420 - "generate_invites.py"
Cohesion: 0.38
Nodes (6): generate_invite_code(), generate_unique_codes(), main(), Generate a unique Mythos-themed invite code., Generate a list of unique invite codes and store them in the database., Generate invite codes and store them in the database.

### Community 1421 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test _send_messages_to_players skips blocked messages., Test _send_messages_to_players handles invalid player_id., Test _echo_message_to_sender echoes message., Test _echo_message_to_sender handles exceptions., Test _apply_dampening_and_send_message handles blocked messages., Test _apply_dampening_and_send_message handles missing original_content., Test _get_player_lucidity_tier handles UUID objects. (+9 more)

### Community 1422 - "4. Common Fix Patterns"
Cohesion: 0.40
Nodes (5): 4. Common Fix Patterns, Authentication Test Patterns, Database Test Patterns, Game Logic Test Patterns, WebSocket Test Patterns

### Community 1423 - "DML Migrations"
Cohesion: 0.40
Nodes (4): Dialogue definitions (#583), DML Migrations, Historical CSV files, Migration files

### Community 1424 - "Nameless Horrors - 2nd Edition (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extractions pages, Nameless Horrors - 2nd Edition (source summary)

### Community 1425 - "S. Petersen's Field Guide to Lovecraftian Horrors (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extrated pages, S. Petersen's Field Guide to Lovecraftian Horrors (source summary)

### Community 1426 - "mock_utils"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_logger(), mock_utils(), player_respawn_event_handler(), fixture, Create a mock connection manager., Create a mock PlayerEventHandlerUtils., Create a mock logger. (+1 more)

### Community 1427 - "Advanced Chat Channels Specification"
Cohesion: 0.40
Nodes (5): Advanced Chat Channels Specification, Global Chat Channel, Local Chat Channel, Advanced Chat Channels Tasks, Whisper Chat Channel

### Community 1428 - "UI/UX Considerations"
Cohesion: 0.40
Nodes (5): 1. Visual Distinction, 2. Panel Positioning, 3. Responsive Design, 4. Accessibility, UI/UX Considerations

### Community 1429 - "3. Simplified CommandPanel"
Cohesion: 0.40
Nodes (5): 3. Simplified CommandPanel, CommandPanel Layout Structure, Features to Keep, Features to Remove, Simplified CommandPanel Interface

### Community 1430 - "Implementation Phases"
Cohesion: 0.40
Nodes (5): Implementation Phases, Phase 1: Core Separation, Phase 2: Enhanced Features, Phase 3: Polish and Optimization, Phase 4: Testing and Refinement

### Community 1431 - "🎓 Best Practice Examples to Share"
Cohesion: 0.40
Nodes (4): 🎓 Best Practice Examples to Share, Example 1: Proper Blocking Operation Offloading, Example 2: Caching with TTL, Example 3: Exception Handling for Connection Failures

### Community 1432 - "Magic and Spellcasting System"
Cohesion: 0.40
Nodes (5): EffectList Pattern, Effects System Reference, Magic Points MP, Magic and Spellcasting System, Spell Registry

### Community 1433 - "Lucidity Tiers"
Cohesion: 0.60
Nodes (5): Catatonic Rescue Window, Lucidity System (LCD), Lucidity Tiers, Phantom Hostiles, Reversed Compass Directions

### Community 1434 - "Common Conversion Patterns"
Cohesion: 0.40
Nodes (5): Common Conversion Patterns, Pattern 1: Simple Query, Pattern 2: Batch Operations, Pattern 3: Health Operations, Pattern 4: FastAPI Dependency Injection

### Community 1435 - "Gotchas & Solutions"
Cohesion: 0.40
Nodes (5): Gotcha 1: Async Propagation, Gotcha 2: Mixing Sync and Async, Gotcha 3: Transaction Management, Gotcha 4: Testing Async Code, Gotchas & Solutions

### Community 1436 - "🎭 Closing Remarks"
Cohesion: 0.40
Nodes (5): Adjusts spectacles with profound satisfaction, 🎭 Closing Remarks, December 3, 2025, Status**: ✅**PHASE 2 COMPLETE - READY FOR TESTING, "The last synchronous operation has been banished to the thread pool, where it belongs."

### Community 1437 - "Four-Level Room Hierarchy"
Cohesion: 0.40
Nodes (5): Environment Classification, Four-Level Room Hierarchy, Environment Inheritance, Room Hierarchy Implementation, Hierarchical World Loader

### Community 1438 - "Financial Impact (If You're Tracking Dev Time)"
Cohesion: 0.40
Nodes (5): CI/CD Time Saved, Developer Time Saved, Financial Impact (If You're Tracking Dev Time), Maintenance Time Saved, Time Savings Calculation

### Community 1439 - "Phase 1: Quick Wins (Week 1)"
Cohesion: 0.40
Nodes (5): Phase 1: Quick Wins (Week 1), Task 1.1: Remove Placeholder Tests (30 minutes), Task 1.2: Remove Trivial Type Assertions (1 hour), Task 1.3: Remove Duplicate Tests (30 minutes), Task 1.4: Delete Empty Test File (5 minutes)

### Community 1440 - "Phase 2: Infrastructure Test Reduction (Week 2)"
Cohesion: 0.40
Nodes (5): Phase 2: Infrastructure Test Reduction (Week 2), Task 2.1: Reduce Dependency Injection Tests (2 hours), Task 2.2: Consolidate Dependency Injection Test Files (2 hours), Task 2.3: Reduce App Factory Tests (1 hour), Task 2.4: Review Lifespan Tests (1 hour)

### Community 1441 - "Phase 4: Test Consolidation (Week 4)"
Cohesion: 0.40
Nodes (5): Phase 4: Test Consolidation (Week 4), Task 4.1: Parametrize Command Validation Tests (4 hours), Task 4.2: Parametrize Error Response Tests (3 hours), Task 4.3: Parametrize Permission Tests (2 hours), Task 4.4: Consolidate Similar Integration Tests (3 hours)

### Community 1442 - "Phase 6: Long-Term Optimizations (Ongoing)"
Cohesion: 0.40
Nodes (5): Phase 6: Long-Term Optimizations (Ongoing), Task 6.1: Establish Test Quality Gates, Task 6.2: Monthly Test Quality Review, Task 6.3: Performance Optimization, Task 6.4: Parallel Test Execution (Investigation)

### Community 1443 - "Phase 1: Quantitative Analysis Results"
Cohesion: 0.40
Nodes (5): 1.1 Test Distribution by Category, 1.2 Largest Test Files (Splitting/Pruning Candidates), 1.3 Infrastructure Test Analysis, Files, Phase 1: Quantitative Analysis Results

### Community 1444 - "Test Suite Quality Audit Report"
Cohesion: 0.18
Nodes (10): ~25-30% (1,250-1,500 tests) provide CRITICAL protection, Answer to Your Question, Conclusion, Phase A: Quick Wins (1-2 hours effort), Phase B: Medium Effort (4-8 hours effort), Phase C: Strategic Enhancements (8-16 hours effort), Recommended Action, Specific Actionable Recommendations (+2 more)

### Community 1445 - "asyncio"
Cohesion: 0.11
Nodes (19): asyncio, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test unsubscribe_from_event_subjects handles partial success., Test handle_player_movement handles None new_subzone., Test cleanup_empty_subzone_subscriptions handles NATSError., Test _handle_player_attacked_event delegates to event handler., Test unsubscribe_from_subzone handles not subscribed case. (+11 more)

### Community 1446 - "Risk Assessment and Mitigation"
Cohesion: 0.40
Nodes (5): Automatic Rollback If, Review and Reconsider If, Risk Assessment and Mitigation, Risks by Phase, Rollback Triggers

### Community 1447 - "Configuration Files Reference"
Cohesion: 0.40
Nodes (5): Configuration File Tuples, Configuration Files Reference, .env.local Secrets Pattern, COPPA Compliance Checklist, Development Environment Setup

### Community 1448 - "Modular E2E Test Suite"
Cohesion: 0.40
Nodes (5): Modular E2E Test Suite, MULTIPLAYER_SCENARIOS_PLAYBOOK, E2E Validation Passed, AI Context Limit 20KB, E2E Test Suite README

### Community 1449 - "Playwright MCP Scenarios"
Cohesion: 0.40
Nodes (5): Automated Playwright CLI Tests, Hybrid E2E Testing Approach, Mandatory Execution Order, Playwright MCP Scenarios, Room Occupants Fix

### Community 1450 - "Local Channel System"
Cohesion: 0.40
Nodes (5): Local Channel Sub-Zone Routing, Scenario 10 Local Channel Movement, Scenario 11 Local Channel Errors, Scenario 12 Local Channel Integration, Local Channel System

### Community 1451 - "Container Contents Synchronization Bug"
Cohesion: 0.50
Nodes (5): Container Contents Synchronization Bug, Fail-Fast Container Error Philosophy, slot_type backpack Assignment, Dual Inventory Storage Architecture, Inventory Slot Calculation Bug

### Community 1452 - "F-String Logging Violations"
Cohesion: 0.40
Nodes (5): F-String Logging Violations, Enhanced Logging Compliance Audit, F-String Logging Remediation Complete, Pre-Commit F-String Hook Gaps, AST-Based F-String Logging Detector

### Community 1453 - "player_event_handler_utils"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), fixture, Create a mock connection manager., Create a mock name extractor., Create a mock logger. (+1 more)

### Community 1454 - "asyncio"
Cohesion: 0.22
Nodes (9): asyncio, Test get_player_info() returns None for invalid player_id., Test get_player_info() returns None when player not found., Test get_player_info() successfully retrieves player info., Test get_player_info() returns None when connection manager not available., test_get_player_info_invalid_player_id(), test_get_player_info_no_connection_manager(), test_get_player_info_player_not_found() (+1 more)

### Community 1455 - "Quest System Gap"
Cohesion: 0.40
Nodes (5): Quest System Gap, MUD Subsystems Gap Analysis, Player Skills and Profession Modifiers, Quest Subsystem Implementation, Quest System

### Community 1456 - "CharacterCreationService"
Cohesion: 0.17
Nodes (10): CharacterCreationService, Any, UUID, Validate character stats against class prerequisites. Args: stats: The stats…, Create a new character with specific stats. Args: name: The character's name…, Get information about all available character classes and their prerequisites.…, Service class for character creation and stats generation business operations., Get a description for a character class. (+2 more)

### Community 1457 - "items"
Cohesion: 0.40
Nodes (5): items, type, pattern, type, bonus_tags

### Community 1458 - "mock_player"
Cohesion: 0.40
Nodes (5): mock_player(), player_repository(), fixture, Create a PlayerRepository instance., Create a mock player for save operations.

### Community 1459 - "fix_file"
Cohesion: 0.60
Nodes (4): fix_file(), main(), Path, Fix suppressions in a file. Returns: (number_fixed, list of changes)

### Community 1460 - "check_codacy_yaml"
Cohesion: 0.50
Nodes (4): check_codacy_yaml(), _content_is_valid(), Return (valid, list of reasons if invalid)., Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit.

### Community 1461 - "HADS tooling (MythosMUD)"
Cohesion: 0.40
Nodes (4): HADS tooling (MythosMUD), Policy, Source pin, Usage

### Community 1462 - "snapshot_chaosium_graphify.ps1"
Cohesion: 0.70
Nodes (4): Export-PackSnapshot(), Get-ChaosiumSlug(), Get-GraphCount(), Get-HonestyNote()

### Community 1464 - "2025_01_XX_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 1465 - "2025_11_21_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 1466 - "2025_11_25_normalize_container_schema.py"
Cohesion: 0.40
Nodes (4): downgrade(), Normalize container schema with proper relational structure., Revert to denormalized schema with items_json., upgrade()

### Community 1467 - "2025_11_25_remove_get_container_contents_json_procedure.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove deprecated stored procedure., Restore deprecated stored procedure., upgrade()

### Community 1468 - "2025_11_25_remove_items_json_column.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove items_json column from containers table., Restore items_json column (data will be empty)., upgrade()

### Community 1469 - "2025_11_26_ensure_item_instance_foreign_keys.py"
Cohesion: 0.40
Nodes (4): downgrade(), Ensure foreign key constraints exist for item_instances., This migration only ensures constraints exist - no downgrade needed., upgrade()

### Community 1470 - "2026_02_09_add_player_effects_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_effects table and indexes (ADR-009 effects system)., Drop player_effects table and indexes., upgrade()

### Community 1471 - "2026_02_18_add_player_skills_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_skills table if not exists (matches db/migrations/025)., Drop player_skills table., upgrade()

### Community 1472 - "2026_02_18_add_profession_modifiers_columns.py"
Cohesion: 0.40
Nodes (4): downgrade(), Add stat_modifiers and skill_modifiers columns to professions table., Remove stat_modifiers and skill_modifiers columns from professions table., upgrade()

### Community 1473 - "2026_02_19_add_quest_tables.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create quest_definitions, quest_instances, quest_offers tables., Drop quest tables (order matters for FKs)., upgrade()

### Community 1474 - "2026_02_19_seed_quest_leave_the_tutorial.py"
Cohesion: 0.40
Nodes (4): downgrade(), Insert leave_the_tutorial quest and quest_offers row., Remove seed quest and its offer., upgrade()

### Community 1475 - "2026_02_26_add_arena_zone_type.py"
Cohesion: 0.40
Nodes (4): downgrade(), Allow zone_type 'arena' in zones CHECK., Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)., upgrade()

### Community 1476 - "rename_players_to_population.py"
Cohesion: 0.40
Nodes (4): downgrade(), Rename columns from min_players/max_players to min_population/max_population., Revert column names back to min_players/max_players., upgrade()

### Community 1477 - "wearable_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), fixture, Create mock persistence layer., Create WearableContainerService instance., wearable_service()

### Community 1478 - "DomainError"
Cohesion: 0.40
Nodes (4): DomainError, Exception, Domain-specific exceptions for MythosMUD. These exceptions represent business…, Base exception for all domain errors.

### Community 1479 - "preferences_service"
Cohesion: 0.22
Nodes (9): mock_session(), preferences_service(), fixture, Create a PlayerPreferencesService instance., Create a mock async session., Create a sample player ID., Create sample player preferences., sample_player_id() (+1 more)

### Community 1481 - ".__init__"
Cohesion: 0.50
Nodes (3): LevelUpHook, Any, Initialize the level service. Args: async_persistence: Async persistence for…

### Community 1482 - "reset_async_persistence"
Cohesion: 0.25
Nodes (8): Reset the global async persistence instance for testing. DEPRECATED: Use…, reset_async_persistence(), Test get_async_persistence creates singleton instance., Test get_async_persistence returns same instance on multiple calls., Test reset_async_persistence resets the singleton., test_get_async_persistence_creates_instance(), test_get_async_persistence_returns_same_instance(), test_reset_async_persistence()

### Community 1483 - "RoomRepositoryProtocol"
Cohesion: 0.15
Nodes (11): Protocol, Room, List all cached rooms., Protocol for room persistence operations. Defines the contract used by…, Get a room by ID from cache., RoomRepositoryProtocol, asyncio, Runtime checks for persistence repository protocols. (+3 more)

### Community 1484 - "needs_rehash"
Cohesion: 0.25
Nodes (8): needs_rehash(), Check if a hash needs to be rehashed due to parameter changes., Test needs_rehash with valid hash that doesn't need rehashing., Test needs_rehash with invalid hash returns True., Test needs_rehash handles errors and returns True., test_needs_rehash_error_handling(), test_needs_rehash_invalid_hash(), test_needs_rehash_valid_hash()

### Community 1485 - "PlayerCombatState"
Cohesion: 0.12
Nodes (14): PlayerCombatState, Get a player's combat state. Args: player_id: ID of the player Returns:…, Represents a player's combat state., Initialize last_activity if not provided., Test is_player_in_combat_sync returns True when in combat., Test cleanup_stale_combat_states cleans up stale states., Test handle_combat_end clears player combat state., Test PlayerCombatState.__post_init__ sets last_activity. (+6 more)

### Community 1486 - "test_inventory_mutation_guard_async.py"
Cohesion: 0.17
Nodes (15): guard(), asyncio, fixture, Unit tests for inventory mutation guard - asynchronous acquire operations.…, Test acquire_async serializes concurrent mutations for same player., Create an InventoryMutationGuard instance., Test acquire_async enforces max_tokens limit., Test acquire_async allows token reuse after expiry. (+7 more)

### Community 1487 - ".ensure_url_set"
Cohesion: 0.50
Nodes (3): Any, model_validator, Ensure url is set - use npc_url as fallback if url is missing. This handles…

### Community 1488 - "._build_exit_lookup"
Cohesion: 0.20
Nodes (5): True if target room has a reverse exit back to from_room_id., Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits…, Build exit lookup map from room data., Get reverse direction for checking bidirectional exits. Args: direction: Exit…

### Community 1489 - "_mock_result_mappings_all"
Cohesion: 0.12
Nodes (16): _mock_result_mappings_all(), Build mock result such that result.mappings().all() returns rows., Test get_npc_definitions() successfully retrieves definitions., Test get_npc_definitions() returns empty list when no definitions., Test get_npc_definition_by_name() returns definition when found., Test update_npc_definition() returns None when not found., Test get_spawn_rule() returns None when not found., Test create_spawn_rule() raises ValueError when definition not found. (+8 more)

### Community 1490 - "._generate_invite_code"
Cohesion: 0.25
Nodes (6): datetime, Generate a unique invite code., Test _generate_invite_code generates 12-character alphanumeric code., Test _generate_invite_code generates different codes on multiple calls., test_invite_generate_invite_code_format(), test_invite_generate_invite_code_uniqueness()

### Community 1491 - ".validate_invite"
Cohesion: 0.25
Nodes (5): Request, UUID, Mark an invite as used by a specific user., Get all invites used by a user., Validate an invite code.

### Community 1492 - "Any"
Cohesion: 0.13
Nodes (8): Any, Set profession stat requirements from dictionary., Get profession mechanical effects as dictionary., Set profession mechanical effects from dictionary., Get stat modifiers as list of {stat, value}., Set stat modifiers from list of {stat, value}., Get skill modifiers as list of {skill_key, value}., Set skill modifiers from list of {skill_key, value}.

### Community 1493 - "test_validate_secure_path_path_traversal_commonpath"
Cohesion: 0.33
Nodes (4): Test validate_secure_path normalizes backslashes., Test validate_secure_path detects path traversal via commonpath check., test_validate_secure_path_path_traversal_commonpath(), test_validate_secure_path_with_backslash()

### Community 1494 - "normalize_path_from_url_or_path"
Cohesion: 0.25
Nodes (6): Path, Return and cache the repository root directory., Delegate to shared util. Kept for backward compatibility., normalize_path_from_url_or_path(), Path, Normalize an item database override into a filesystem path. DEPRECATED: Items…

### Community 1495 - "Testing Logging"
Cohesion: 0.67
Nodes (3): Integration Tests, Testing Logging, Unit Tests for Logging

### Community 1496 - "server/dependencies.py"
Cohesion: 0.01
Nodes (207): get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container(), get_exploration_service(), get_level_service() (+199 more)

### Community 1497 - "convert_uuids_to_strings_impl"
Cohesion: 0.40
Nodes (4): convert_uuids_to_strings_impl(), Recursively convert UUID objects to strings for JSON serialization., Recursively convert UUID objects to strings for JSON serialization., test_convert_uuids_to_strings_impl()

### Community 1498 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1499 - "get_next_sequence_impl"
Cohesion: 0.40
Nodes (4): get_next_sequence_impl(), Get the next sequence number for events., Get the next sequence number for events. Returns: int: The next sequence number, test_get_next_sequence_impl()

### Community 1500 - ".create_invite"
Cohesion: 0.25
Nodes (7): Create a new invite with the specified parameters., Test create_invite creates invite with creator user_id., Test create_invite creates invite with custom expiry days., Test create_invite creates invite with default parameters., test_invite_create_invite_defaults(), test_invite_create_invite_with_creator(), test_invite_create_invite_with_custom_expiry()

### Community 1502 - ".check_player_mute_status"
Cohesion: 0.14
Nodes (8): Any, Extract information from chat event. Args: chat_event: Chat event dictionary…, Determine if mute check should be applied for a channel. Args: channel: Channel…, Initialize message filtering helper. Args: connection_manager:…, Check if a receiving player has muted the sender using a provided UserManager…, Check if a player has muted the sender. Args: user_manager: UserManager…, Filter target players based on room location and mute status. Args: targets:…, Check if a receiving player has muted the sender.

### Community 1503 - "_validate_tls_files_and_maybe_update_url"
Cohesion: 0.25
Nodes (8): Any, When TLS is enabled, validate cert/key (and optional CA) exist and update url…, _validate_tls_files_and_maybe_update_url(), model_validator, Validate TLS configuration is complete when enabled., Path, test_validate_tls_files_missing_cert_raises(), test_validate_tls_updates_url_scheme()

### Community 1504 - "Any"
Cohesion: 0.15
Nodes (8): Any, Extract occupant names from occupant information. Args: occupants_info: List of…, Add a valid name to the appropriate lists. Args: name: The name to validate and…, Process a dictionary occupant and add to appropriate lists. Args: occ:…, Build structured occupants data from snapshot. Args: occupants_snapshot: List…, Initialize utility functions. Args: connection_manager: ConnectionManager…, Count NPCs and players in occupants snapshot. Args: occupants_snapshot: List of…, Extract name from a single occupant entry. Args: occ: Occupant information…

### Community 1505 - "._generate_alert"
Cohesion: 0.13
Nodes (8): Alert, Convert to dictionary., Update resource usage metrics. Args: memory_mb: Memory usage in MB cpu_percent:…, Add alert callback function. Args: callback: Function to call when alert is…, Remove alert callback function. Args: callback: Function to remove, Check resource usage thresholds., Check if performance threshold has been exceeded., Generate and dispatch an alert.

### Community 1506 - ".is_player_in_room"
Cohesion: 0.25
Nodes (4): Compare two room IDs using canonical room ID resolution. Args: player_room_id:…, Get player's current room ID from online players cache. Args: player_id: Player…, Get player's current room ID from async persistence layer. Args: player_id:…, Check if a player is currently in the specified room. Args: player_id: Player…

### Community 1507 - "._send_messages_to_players"
Cohesion: 0.29
Nodes (4): Format message content for a receiver (after dampening applied). For whisper…, Apply communication dampening and send message to a single receiver. Helper…, Get a player's current lucidity tier from database. Args: player_id: Player ID…, Send messages to filtered target players, applying communication dampening per…

### Community 1508 - "fixture"
Cohesion: 0.13
Nodes (15): handler(), mock_chat_service(), mock_magic_service(), mock_player(), mock_player_spell_repository(), mock_spell_learning_service(), mock_spell_registry(), fixture (+7 more)

### Community 1509 - "test_realtime_bundle_nats.py"
Cohesion: 0.19
Nodes (14): _config(), Any, asyncio, RealtimeBundle NATS connect policy: e2e hard-fails; soft fail only for non-e2e., e2e_test must not soft-mock missing NATS (avoids silent chat failures in…, e2e_test hard-fails when NATS connect times out (e.g. TLS mismatch)., Non-e2e local may soft-continue without NATS when connect fails., unit_test combat path still soft-mocks unavailable NATS. (+6 more)

### Community 1510 - "MythosMUD Pre-Commit Checklist Skill"
Cohesion: 0.40
Nodes (5): Definition of Done Checklist, MythosMUD Code Quality AI Skill, MythosMUD Commit Messages Skill, MythosMUD Pre-Commit Checklist Skill, MythosMUD Test Writing Skill

### Community 1511 - "Claude Pointer (.claude/CLAUDE.md)"
Cohesion: 0.67
Nodes (4): AGENTS.md Authoritative Reference, Cursor Rules (.cursor/rules/), Claude Pointer (.claude/CLAUDE.md), Root CLAUDE.md Router Stub

### Community 1515 - "Tiered Test Coverage Strategy"
Cohesion: 0.50
Nodes (4): Critical Code 90% Coverage, Global 70% Coverage Threshold, Tiered Test Coverage Strategy, Vitest Unit Tests

### Community 1518 - ".__init__"
Cohesion: 0.25
Nodes (5): Any, UUID, Separate occupants into players, NPCs, and all occupants lists. Args:…, Initialize the room occupant manager. Args: connection_manager:…, Get the list of occupants in a room. Args: room_id: The room ID…

### Community 1519 - "fake_hallucination_service.py"
Cohesion: 0.29
Nodes (5): Any, UUID, Fake hallucination service for MythosMUD. Implements fake NPC tells and room…, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will…

### Community 1520 - "test_look_npc.py"
Cohesion: 0.02
Nodes (169): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_description(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result() (+161 more)

### Community 1521 - "9. Test Maintenance Best Practices"
Cohesion: 0.50
Nodes (4): 9. Test Maintenance Best Practices, Performance Considerations, Test Data Management, Test Isolation

### Community 1522 - "LLM Wiki Vault Schema"
Cohesion: 0.50
Nodes (4): LLM Wiki Vault Schema, Raw Sources Layer, Wiki Layer, Wiki Page Template

### Community 1523 - "Code Graph Entry"
Cohesion: 0.50
Nodes (3): Code Graph Entry, Live exploration (preferred for "how does X work?"), Synced community wiki (read-only dump)

### Community 1524 - "DML Migrations Apply Paths"
Cohesion: 0.50
Nodes (3): Agent rule, DML Migrations Apply Paths, Facts

### Community 1525 - "Graphify Code Graph"
Cohesion: 0.50
Nodes (3): Chaosium pack graphs (external), Graphify Code Graph, Relationship to this vault

### Community 1529 - "A Cold Fire Within (source summary)"
Cohesion: 0.50
Nodes (3): A Cold Fire Within (source summary), For MythosMUD design, Links

### Community 1530 - "Alone Against the Dark (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Dark (source summary), For MythosMUD design, Links

### Community 1531 - "Alone Against the Frost (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Frost (source summary), For MythosMUD design, Links

### Community 1532 - "Alone against the Tide (source summary)"
Cohesion: 0.50
Nodes (3): Alone against the Tide (source summary), For MythosMUD design, Links

### Community 1533 - "Berlin - The Wicked City (source summary)"
Cohesion: 0.50
Nodes (3): Berlin - The Wicked City (source summary), For MythosMUD design, Links

### Community 1534 - "Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary), For MythosMUD design, Links

### Community 1535 - "Call of Cthulhu Keeper Tips (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Keeper Tips (source summary), For MythosMUD design, Links

### Community 1536 - "Call of Cthulhu Starter Set (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Starter Set (source summary), For MythosMUD design, Links

### Community 1537 - "Call of Cthulhu_ The Coloring Book (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu_ The Coloring Book (source summary), For MythosMUD design, Links

### Community 1538 - "character_sheets (source summary)"
Cohesion: 0.50
Nodes (3): character_sheets (source summary), For MythosMUD design, Links

### Community 1539 - "Cthulhu Dark Ages - 3rd Edition (source summary)"
Cohesion: 0.50
Nodes (3): Cthulhu Dark Ages - 3rd Edition (source summary), For MythosMUD design, Links

### Community 1540 - "Does Love Forgive_ (source summary)"
Cohesion: 0.50
Nodes (3): Does Love Forgive_ (source summary), For MythosMUD design, Links

### Community 1541 - "Doors to Darkness (source summary)"
Cohesion: 0.50
Nodes (3): Doors to Darkness (source summary), For MythosMUD design, Links

### Community 1542 - "Down Darker Trails (source summary)"
Cohesion: 0.50
Nodes (3): Down Darker Trails (source summary), For MythosMUD design, Links

### Community 1543 - "Gateways to Terror (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Gateways to Terror (source summary), Links

### Community 1544 - "Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)

### Community 1545 - "The Grand Grimoire of Cthulhu Mythos Magic (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Grand Grimoire of Cthulhu Mythos Magic (source summary)

### Community 1546 - "The Malleus Monstrorum Keeper Deck (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Malleus Monstrorum Keeper Deck (source summary)

### Community 1547 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 1548 - "Aggro and Threat System Design"
Cohesion: 0.50
Nodes (4): Aggro and Threat System Design, Hate List, Aggro Stability Margin, UpdateAggro

### Community 1549 - "Migration Considerations"
Cohesion: 0.50
Nodes (4): Backward Compatibility, Data Migration, Migration Considerations, Performance Impact

### Community 1550 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Non-Functional Requirements, Success Criteria, User Experience Requirements

### Community 1551 - "Risk Assessment"
Cohesion: 0.50
Nodes (4): Implementation Risks, Risk Assessment, Technical Risks, User Experience Risks

### Community 1552 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Testing Strategy, Unit Tests, User Acceptance Tests

### Community 1553 - "📚 REFERENCES AND RESOURCES"
Cohesion: 0.50
Nodes (4): Best Practice Documents, External Resources, Investigation Reports, 📚 REFERENCES AND RESOURCES

### Community 1554 - "📊 METRICS AND SUCCESS CRITERIA"
Cohesion: 0.50
Nodes (4): Code Quality Metrics, 📊 METRICS AND SUCCESS CRITERIA, Performance Metrics, Test Coverage

### Community 1555 - "🚀 DEPLOYMENT STRATEGY"
Cohesion: 0.50
Nodes (4): 🚀 DEPLOYMENT STRATEGY, Monitoring Post-Deployment, Pre-Deployment Checklist, Rollback Plan

### Community 1557 - "🔧 Code Changes Made"
Cohesion: 0.50
Nodes (4): 1. Fixed Event Loop Blocking in PassiveLucidityFluxService, 2. Removed asyncio.run() from Exploration Service, 3. Added Exception Handling for Database Engine Creation, 🔧 Code Changes Made

### Community 1558 - "🏆 Achievement Highlights"
Cohesion: 0.50
Nodes (4): 🏆 Achievement Highlights, Code Quality, Critical Fixes (Phase 1), Performance Optimizations

### Community 1559 - "🎭 Closing Remarks"
Cohesion: 0.50
Nodes (4): Adjusts spectacles with scholarly satisfaction, 🎭 Closing Remarks, "In the house of the event loop, all operations must flow as one.", Status**: ✅**REMEDIATION COMPLETE

### Community 1560 - "🎯 Performance Improvements"
Cohesion: 0.50
Nodes (4): After Fixes, Before Fixes, 🎯 Performance Improvements, Room Cache Performance

### Community 1561 - "💰 ROI Analysis"
Cohesion: 0.50
Nodes (4): Break-Even, Investment, Return, 💰 ROI Analysis

### Community 1562 - "📚 Deliverables"
Cohesion: 0.50
Nodes (4): Code Changes (4 files modified), 📚 Deliverables, Documentation (5 files, ~2,500 lines), Tests (1 file, 250+ lines)

### Community 1563 - "🚀 Deployment Readiness"
Cohesion: 0.50
Nodes (4): Critical Blockers - RESOLVED, 🚀 Deployment Readiness, Phase 2 Recommendation, Production Ready Status

### Community 1564 - "Phase 2: Database Layer Integration"
Cohesion: 0.50
Nodes (4): 2.1 Persistence Layer Protection, 2.2 Database Connection Protection, 2.3 Configuration, Phase 2: Database Layer Integration

### Community 1565 - "Phase 3: Real-Time Communication Protection"
Cohesion: 0.50
Nodes (4): 3.1 NATS Integration, 3.2 WebSocket Protection, 3.3 Configuration, Phase 3: Real-Time Communication Protection

### Community 1566 - "Phase 4: File System Operations"
Cohesion: 0.50
Nodes (4): 4.1 Room Loading Protection, 4.2 Player Data File Operations, 4.3 Configuration, Phase 4: File System Operations

### Community 1567 - "Phase 6: Monitoring and Observability"
Cohesion: 0.50
Nodes (4): 6.1 Metrics Collection, 6.2 Health Check Endpoints, 6.3 Logging Integration, Phase 6: Monitoring and Observability

### Community 1568 - "Future Enhancements"
Cohesion: 0.50
Nodes (4): Advanced Features, Document metadata, Future Enhancements, Integration Opportunities

### Community 1569 - "Monitoring and Alerting"
Cohesion: 0.50
Nodes (4): Alerting Rules, Health Checks, Metrics to Monitor, Monitoring and Alerting

### Community 1570 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Monitoring Requirements, Performance Requirements, Success Criteria

### Community 1571 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Load Tests, Testing Strategy, Unit Tests

### Community 1572 - "WebSocket and SSE Dual Connections"
Cohesion: 0.50
Nodes (4): Dual Connection API Reference, WebSocket and SSE Dual Connections, Dual Connection Client Guide, Dual Connection Deployment Guide

### Community 1573 - "Context Management"
Cohesion: 0.50
Nodes (4): Context Management, Request Context, System Context, User Context

### Community 1574 - "🚨 CRITICAL ANTI-PATTERNS - DO NOT USE"
Cohesion: 0.50
Nodes (4): 🚨 CRITICAL ANTI-PATTERNS - DO NOT USE, ❌ FORBIDDEN IMPORT PATTERNS, ❌ FORBIDDEN LOGGING PATTERNS, ✅ MANDATORY CORRECT PATTERNS

### Community 1575 - "Rollback Procedures"
Cohesion: 0.50
Nodes (4): Emergency Rollback, Individual File Rollback, Phase Rollback, Rollback Procedures

### Community 1576 - "Success Metrics"
Cohesion: 0.50
Nodes (4): Overall Migration Metrics, Per-File Metrics, Per-Phase Metrics, Success Metrics

### Community 1577 - "🚀 Deployment Readiness"
Cohesion: 0.50
Nodes (4): Async Compliance, Code Quality, 🚀 Deployment Readiness, Remaining Work

### Community 1578 - "🎓 Lessons Learned"
Cohesion: 0.50
Nodes (4): Best Practices Reinforced, Challenges Encountered, 🎓 Lessons Learned, What Worked Well

### Community 1579 - "📚 Changes by Category"
Cohesion: 0.50
Nodes (4): 📚 Changes by Category, Combat/Death (2 files), Core Layer (4 files), Service Layer (8 files)

### Community 1580 - "🚦 Next Steps"
Cohesion: 0.50
Nodes (4): Immediate (Today), 🚦 Next Steps, Production Deployment, This Week

### Community 1581 - "✅ Verification Results"
Cohesion: 0.50
Nodes (4): Linting, Result**: ✅**ALL CHECKS PASSED, Test Results, ✅ Verification Results

### Community 1582 - "MythosMUD Product Requirements"
Cohesion: 0.50
Nodes (4): Aggro System, Lucidity System, MythosMUD Product Requirements, Room-Based Combat

### Community 1584 - "test_npc_models.py"
Cohesion: 0.25
Nodes (7): Unit tests for NPC models. Tests the NPCDefinitionType enum and NPCDefinition,…, Test NPCRelationship can be instantiated with required fields., Test NPCDefinition can be instantiated with required fields., Test NPCDefinition has correct default values., test_npc_definition_creation(), test_npc_definition_defaults(), test_npc_relationship_creation()

### Community 1585 - "Net Impact Projection"
Cohesion: 0.50
Nodes (4): After Month 1 (Pruning Phase), After Month 2 (Consolidation + Additions), After Month 3+ (Continuous Improvement), Net Impact Projection

### Community 1586 - "Implementation Timeline"
Cohesion: 0.50
Nodes (4): Implementation Timeline, Month 1: Pruning and Quick Wins, Month 2: Consolidation and Additions, Month 3+: Continuous Improvement

### Community 1587 - "Phase 3: Coverage Test Optimization (Week 3)"
Cohesion: 0.50
Nodes (4): Phase 3: Coverage Test Optimization (Week 3), Task 3.1: Reduce Command Handler Coverage Tests (3 hours), Task 3.2: Reduce Error Logging Coverage Tests (2 hours), Task 3.3: Merge Coverage Tests into Domain Tests (3 hours)

### Community 1588 - "Appendix: Quick Reference Commands"
Cohesion: 0.50
Nodes (4): Appendix: Quick Reference Commands, Test Analysis Commands, Test Removal Workflow, "The optimization of tests is not destruction, but refinement — removing the dross to reveal the gold beneath."

### Community 1589 - "Detailed Category Value Breakdown"
Cohesion: 0.50
Nodes (4): 🔴 CRITICAL VALUE TESTS (1,272 tests = 25.6%), Detailed Category Value Breakdown, 🟡 IMPORTANT VALUE TESTS (2,943 tests = 59.3%), 🟢 LOW VALUE TESTS (750 tests = 15.1%)

### Community 1590 - "Time Distribution Analysis"
Cohesion: 0.50
Nodes (4): Current Time Allocation, Highest Impact (Remove), Optimization Targets, Time Distribution Analysis

### Community 1591 - "Container System API Reference"
Cohesion: 0.50
Nodes (4): Container System API, Container System API Reference, Container Item System, Container System Architecture

### Community 1592 - "Event Ownership Matrix"
Cohesion: 0.50
Nodes (4): Event Ownership Matrix, Event Publishing Layers, Event Subscription Cleanup Patterns, Event Subscription service_id Tracking

### Community 1593 - "Logging Best Practices"
Cohesion: 0.67
Nodes (4): Logging Best Practices, Structured Key-Value Logging, Logging Quick Reference, Forbidden Logging Patterns

### Community 1594 - "Persistence Repository Layer"
Cohesion: 0.50
Nodes (4): Persistence Repository Architecture, Persistence Repository Layer, PostgreSQL Contributor Guide, PostgreSQL Stored Procedures Pattern

### Community 1595 - "Real-Time Architecture"
Cohesion: 0.50
Nodes (4): Real-Time Architecture, WebSocket and NATS Realtime Stack, Structured Concurrency Patterns, Structured Concurrency Task Tracking

### Community 1596 - "Scenario Group Execution"
Cohesion: 0.50
Nodes (4): Scenario Group Execution, Local Channel Scenario Group (8-12), Logout Scenario Group (19-21), Whisper Channel Scenario Group (13-18)

### Community 1597 - "ChatPoseManager"
Cohesion: 0.18
Nodes (8): ChatPoseManager, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…, Get a player's current pose. Args: player_id: ID of the player Returns: Current…, Clear a player's pose. Args: player_id: ID of the player Returns: True if pose…, Get all poses (for testing/debugging). Returns: Dictionary mapping player IDs…

### Community 1598 - "Main Foyer Starting Room"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 1599 - "Per-Recipient Whisper Rate Limiting"
Cohesion: 0.50
Nodes (4): Whisper System Remediation, Per-Recipient Whisper Rate Limiting, Global Whisper Rate Limit, Scenario 15 Rate Limiting Blocked

### Community 1600 - "Lucidity System Expansion Scenarios"
Cohesion: 0.67
Nodes (4): Lucidity System Expansion Scenarios, Catatonia Grounding Ritual Scenario, player_lucidity Ledger, Sanitarium Failover Escalation

### Community 1601 - "Container System"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 1602 - "Scenario 32 Disconnect Grace Period"
Cohesion: 0.50
Nodes (4): Scenario 32 Disconnect Grace Period, Linkdead Zombie State, Scenario 33 Rest Command, Scenario 35 Player Combat

### Community 1604 - "Catatonic Movement Prevention Bug"
Cohesion: 0.50
Nodes (4): Catatonic Movement Prevention Bug, WebSocket Go Command Unified Handler Bypass, current_room_id VARCHAR(50) Truncation, Movement Valid Exits Rejection Bug

### Community 1605 - "Rooms List SQL ::uuid[] Parameter Conflict"
Cohesion: 0.50
Nodes (4): asyncpg Colon Cast Parameter Parsing, Rooms List SQL ::uuid[] Parameter Conflict, Minimap Explored Rooms UUID vs stable_id, Explored Room UUIDs Treated As stable_ids

### Community 1606 - "Vite Best-Practices Remediation"
Cohesion: 0.50
Nodes (4): Test Suite Improvement, Vite Best-Practices Remediation, import.meta.env (Vite), Vitest Best-Practices Remediation

### Community 1607 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 1608 - "is_websocket_open_impl"
Cohesion: 0.15
Nodes (11): get_connection_id_from_websocket_impl(), is_websocket_open_impl(), WebSocket, Get connection ID from a WebSocket instance., Check if a WebSocket is open., WebSocket, Check if a WebSocket is open., Connect a WebSocket for a player. (+3 more)

### Community 1609 - "Shared JSON schemas"
Cohesion: 0.50
Nodes (4): alias_schema.json, emote_schema.json, Shared JSON schemas, unified_room_schema.json

### Community 1610 - "apply_migration"
Cohesion: 0.67
Nodes (3): apply_migration(), main(), Apply migration to a single database.

### Community 1611 - "main"
Cohesion: 0.67
Nodes (3): main(), Entry point: ensure collect_n quest seed and clear instances via anyio., _reset_collect_n_quest()

### Community 1613 - "_resolved_npm"
Cohesion: 0.67
Nodes (3): main(), Return absolute path to npm (prefer npm.cmd on Windows), or None if not found., _resolved_npm()

### Community 1614 - "start_server.ps1"
Cohesion: 0.50
Nodes (4): Default Server Port 54768, start_local.ps1, start_server.ps1, stop_server.ps1

### Community 1616 - "verify_tutorial_migrations.ps1"
Cohesion: 0.83
Nodes (3): Test-Migration08(), Test-Migration12(), Write-ColorOutput()

### Community 1617 - "test_rescue_service.py"
Cohesion: 0.25
Nodes (7): Unit tests for rescue service. Tests the RescueService class for performing…, Test rescue() returns error when rescuer and target are in different rooms., Test rescue() returns error when lucidity record is not found., Test rescue() includes location_id in lucidity adjustment., test_rescue_different_rooms(), test_rescue_lucidity_record_not_found(), test_rescue_metadata_includes_location()

### Community 1618 - "DeadLetterMessage"
Cohesion: 0.14
Nodes (14): DeadLetterMessage, Message stored in dead letter queue. Contains message data and failure context…, Test enqueue() writes correct message data., Test DeadLetterMessage.to_dict() converts to dictionary., Test get_statistics() returns stats with messages., Test list_messages() respects limit parameter., Test DeadLetterMessage.to_dict() handles None headers., Test cleanup_old_messages() returns 0 when no old messages. (+6 more)

### Community 1619 - ".create_go_command"
Cohesion: 0.25
Nodes (7): Test create_go_command() creates GoCommand., Test create_go_command() raises error with no args., Test create_go_command() raises error with invalid direction., test_create_go_command(), test_create_go_command_invalid_direction(), test_create_go_command_no_args(), Create GoCommand from arguments.

### Community 1620 - ".create_ground_command"
Cohesion: 0.25
Nodes (7): Test create_ground_command() creates GroundCommand., Test create_ground_command() raises error with no args., Test create_ground_command() raises error with empty target., test_create_ground_command(), test_create_ground_command_empty_target(), test_create_ground_command_no_args(), Create GroundCommand from arguments.

### Community 1621 - "_RoomBroadcaster"
Cohesion: 0.29
Nodes (6): _EventSequence, Protocol, Sequence counter surface used by build_event., Connection manager surface used to fan out posture events., Send event to occupants of room_id., _RoomBroadcaster

### Community 1622 - "test_config.py"
Cohesion: 0.17
Nodes (11): Unit tests for configuration system., Test that get_config() returns fresh instances in test mode., Test that config has server configuration., Test that config has database configuration., Test that config has game configuration., Test that get_config() returns an AppConfig object., test_get_config_has_database_config(), test_get_config_has_game_config() (+3 more)

### Community 1623 - "command_service"
Cohesion: 0.29
Nodes (7): command_service(), mock_request(), mock_user(), fixture, Create a CommandService instance., Create a mock request object., Create a mock user object.

### Community 1624 - "idle_movement_handler"
Cohesion: 0.29
Nodes (7): idle_movement_handler(), mock_event_bus(), mock_persistence(), fixture, Create a mock persistence layer., Create a mock event bus., Create an IdleMovementHandler instance.

### Community 1625 - "fixture"
Cohesion: 0.29
Nodes (4): fixture, Create a mock psycopg2 connection., Create a mock psycopg2 cursor., Create a mock psycopg2 cursor.

### Community 1626 - "test_npc_service.py"
Cohesion: 0.14
Nodes (13): Unit tests for NPC service. Tests the NPCService class., Test get_npc_definition() returns None when not found., Test get_npc_definition() handles errors., Test create_npc_definition() raises ValueError for invalid type., Test delete_npc_definition() returns False when not found., Test get_spawn_rules() handles database errors., Test delete_spawn_rule() returns False when not found., test_create_npc_definition_invalid_type() (+5 more)

### Community 1627 - "Exception"
Cohesion: 0.15
Nodes (14): _create_async_wrapper(), _create_sync_wrapper(), _is_psycopg2_transient(), _is_wrapped_transient_message(), _log_retry_attempt(), _log_retry_failure(), Any, Exception (+6 more)

### Community 1628 - "Profession"
Cohesion: 0.18
Nodes (8): Profession, Base, Check if given stats meet the profession requirements. Args: stats: Dictionary…, Check if profession is available for player selection., Get formatted text for displaying stat requirements. Returns: Formatted string…, Profession model for game data. Stores profession information including name,…, String representation of the profession., Get profession stat requirements as dictionary.

### Community 1630 - "Any"
Cohesion: 0.15
Nodes (7): Any, Get mapping of event types to their handler methods., Validate that event message has required fields., Handle player_left event., Handle combat_ended event., Handle player_attacked event., Handle npc_took_damage event.

### Community 1632 - "Client Security and Privacy Policies"
Cohesion: 0.67
Nodes (3): Client Security and Privacy Policies, DOMPurify Sanitization, WebSocket Subprotocol Auth

### Community 1635 - "MythosMUD UI Component Library"
Cohesion: 0.67
Nodes (3): Mythos Terminal Theme Tokens, StatusPanel, MythosMUD UI Component Library

### Community 1640 - "get_online_players_impl"
Cohesion: 0.40
Nodes (4): get_online_players_impl(), Get list of online players., Get list of online players., test_get_online_players_impl_with_data()

### Community 1641 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 1643 - "MythosMUD Worldbuilding Source"
Cohesion: 0.67
Nodes (3): MythosMUD Wiki Log, MythosMUD Worldbuilding Foundation (Raw), MythosMUD Worldbuilding Source

### Community 1671 - "Expansion Backlog (Raw)"
Cohesion: 0.67
Nodes (3): Delta Green, Expansion Backlog (Raw), Things and Notes to Expand On

### Community 1672 - "Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition Keeper Screen Pack (source summary), For MythosMUD design, Links

### Community 1673 - "Call of Cthulhu Investigator Handbook 7th Edition (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Investigator Handbook 7th Edition (source summary), For MythosMUD design, Links

### Community 1674 - "Dead Light and Other Dark Turns (source summary)"
Cohesion: 0.50
Nodes (3): Dead Light and Other Dark Turns (source summary), For MythosMUD design, Links

### Community 1675 - "Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)

### Community 1678 - "AI Development Workflow"
Cohesion: 0.67
Nodes (3): AI Command Development Workflow, Cursor AI Tooling, AI Development Workflow

### Community 1679 - "📈 Performance Impact Assessment"
Cohesion: 0.67
Nodes (3): After Migration, Before Migration, 📈 Performance Impact Assessment

### Community 1680 - "🎯 Code Quality Assessment"
Cohesion: 0.67
Nodes (3): Areas for Future Enhancement (Not Blocking), 🎯 Code Quality Assessment, Strengths

### Community 1681 - "🎯 Final Verdict"
Cohesion: 0.67
Nodes (3): Code Quality: ✅ EXCELLENT (A), 🎯 Final Verdict, Recommendations for Deployment

### Community 1682 - "🎓 Technical Debt Reduced"
Cohesion: 0.67
Nodes (3): After, Before, 🎓 Technical Debt Reduced

### Community 1683 - "🎯 Audit Compliance Score"
Cohesion: 0.67
Nodes (3): After Remediation, 🎯 Audit Compliance Score, Before Remediation

### Community 1684 - "🎓 Key Learnings"
Cohesion: 0.67
Nodes (3): Best Practices Reinforced, 🎓 Key Learnings, What We Found

### Community 1685 - "🔍 Testing Strategy"
Cohesion: 0.67
Nodes (3): Immediate Testing (This Session), Performance Testing (After Deployment), 🔍 Testing Strategy

### Community 1687 - "🎯 Success Criteria - Status"
Cohesion: 0.67
Nodes (3): Phase 1 (Critical) - ✅ COMPLETE, Phase 2 (Performance) - 📋 PLANNED, 🎯 Success Criteria - Status

### Community 1688 - "🚨 Risk Assessment"
Cohesion: 0.67
Nodes (3): Remaining Risks, 🚨 Risk Assessment, Risks Eliminated

### Community 1689 - "Character Creation Revamp"
Cohesion: 0.67
Nodes (3): Character Creation Revamp, CoC-Style Skills Allocation, Skill Use Tracking and Level-Up Improvement

### Community 1690 - "Comprehensive System Audit"
Cohesion: 0.67
Nodes (3): CI/CD Enhanced Logging Validation, Comprehensive System Audit, Database Migration Guide

### Community 1691 - "Architecture Overview"
Cohesion: 0.67
Nodes (3): Architecture Overview, CircuitBreaker States, Integration Points

### Community 1692 - "Dead Code Cleanup Completion"
Cohesion: 0.67
Nodes (3): Legacy Files Cleanup Summary, Dead Code Cleanup Completion, Dead Code Cleanup Planning

### Community 1693 - "Single Session Per User"
Cohesion: 0.67
Nodes (3): force_disconnect_player, Single Session Per User, Player Spawn Protection

### Community 1694 - "Fixture Optimization Complete"
Cohesion: 0.67
Nodes (3): E2E Testing Setup Status, Fixture Optimization Complete, Test Suite Post-Merge Refactoring

### Community 1695 - "Test Warning Remediation"
Cohesion: 0.67
Nodes (3): Early Logging Initialization, datetime.utcnow Deprecation Fix, Test Warning Remediation

### Community 1696 - "Enhanced Logging Migration Complete"
Cohesion: 0.67
Nodes (3): Enhanced Logging Implementation Complete, Enhanced Logging Implementation Summary, Enhanced Logging Migration Complete

### Community 1697 - "Random Stats Generator Planning"
Cohesion: 0.67
Nodes (3): Pydantic Click Command Validation Integration, Random Stats Generator Technical Plan, Random Stats Generator Planning

### Community 1698 - "validate_websocket_message"
Cohesion: 0.18
Nodes (13): extract_csrf_token_from_raw(), get_connection_csrf_context(), WebSocket, Persist a validated message JWT on connection metadata after reconnect edge…, Validate csrfToken from the message body and optionally heal connection…, Resolve the CSRF/JWT token used for message validation. Prefer connection…, Validate message and send error response if validation fails. Returns:…, Parse outer JSON once to read csrfToken/csrf_token when metadata lacks a stored… (+5 more)

### Community 1699 - "Log Rotation and Management"
Cohesion: 0.67
Nodes (3): Configuration, Log Cleanup, Log Rotation and Management

### Community 1700 - "Log Analysis and Monitoring"
Cohesion: 0.67
Nodes (3): Custom Log Analysis, Log Analysis and Monitoring, Using Our Log Analysis Tools

### Community 1701 - "Party System Reference"
Cohesion: 0.67
Nodes (3): Party Invite Command, Party System Reference, Ephemeral Grouping Party Planning

### Community 1702 - "Decision Points"
Cohesion: 0.67
Nodes (3): Decision Points, When NOT to Migrate, When TO Migrate

### Community 1703 - "Monitoring & Validation"
Cohesion: 0.67
Nodes (3): Metrics to Track, Monitoring & Validation, Performance Validation

### Community 1704 - "Testing Strategy"
Cohesion: 0.67
Nodes (3): Per-File Testing, Regression Testing, Testing Strategy

### Community 1705 - "📊 Final Results"
Cohesion: 0.67
Nodes (3): Additional Files Updated, Files Migrated (12 of 12 - 100%), 📊 Final Results

### Community 1706 - "📈 Performance Impact"
Cohesion: 0.67
Nodes (3): After Migration, Before Migration, 📈 Performance Impact

### Community 1707 - "🎯 Async Compliance Score"
Cohesion: 0.67
Nodes (3): 🎯 Async Compliance Score, Final Score: 100%, Overall Compliance**: 🟢**A+ (100%)

### Community 1708 - "🧪 Testing Status"
Cohesion: 0.67
Nodes (3): Automated Tests, Manual Testing Required, 🧪 Testing Status

### Community 1709 - "🔧 Changes Summary"
Cohesion: 0.67
Nodes (3): 🔧 Changes Summary, Methods Made Async, Pattern Applied (48 times)

### Community 1710 - "._build_connection_stats"
Cohesion: 0.25
Nodes (4): Count how many sessions have each connection-count size., Return (avg, max, min) connection ages; zeros when the list is empty., Compose connection statistics payload (extracted to keep get_connection_stats…, Get comprehensive connection statistics. Args: player_websockets: Player to…

### Community 1711 - "Test File Migration Mapping"
Cohesion: 0.67
Nodes (3): Test Suite Hierarchical Migration, Test File Migration Mapping, Test Suite Refactoring Deliverables

### Community 1712 - "Optimization Strategy Overview"
Cohesion: 0.67
Nodes (3): Guiding Principles, Optimization Strategy Overview, Success Metrics

### Community 1713 - "Monitoring and Validation"
Cohesion: 0.67
Nodes (3): Monitoring and Validation, Monthly Review Questions, Weekly Metrics

### Community 1714 - "Success Criteria"
Cohesion: 0.67
Nodes (3): Qualitative Goals, Quantitative Goals, Success Criteria

### Community 1715 - "Visual Test Value Distribution"
Cohesion: 0.67
Nodes (3): Overall Test Suite Composition (4,965 Tests), Test Count by Category, Visual Test Value Distribution

### Community 1716 - "Who Command Enhancement"
Cohesion: 0.67
Nodes (3): Who Command Name Filtering, Who Command Enhancement, Who Command Implementation Tasks

### Community 1717 - "Bounded Contexts and Service Boundaries"
Cohesion: 0.67
Nodes (3): Bounded Contexts, Bounded Contexts and Service Boundaries, Service Boundaries

### Community 1718 - "GameState Event Projection"
Cohesion: 0.67
Nodes (3): Client EventStore, GameState Event Projection, Server Authority over Client State

### Community 1719 - "Truly Dead Code"
Cohesion: 0.67
Nodes (3): Knip Client Dead Code Tooling, Truly Dead Code, Vulture Allowlist

### Community 1720 - "E2E Testing Guide"
Cohesion: 1.00
Nodes (3): E2E Testing Guide, Playwright CLI E2E Tests, Playwright MCP Multiplayer Scenarios

### Community 1721 - "NATS Subject Patterns"
Cohesion: 0.67
Nodes (3): NATS Error Handling Strategy, NATS Subject Patterns, NATS Subject Naming Patterns

### Community 1722 - "Ground Command"
Cohesion: 0.67
Nodes (3): Catatonic Rescue Target, Ground Command, Rescue Subsystem

### Community 1723 - "Rest Subsystem"
Cohesion: 0.67
Nodes (3): Rest Countdown Disconnect, Rest Location Instant Disconnect, Rest Subsystem

### Community 1724 - "LevelService"
Cohesion: 1.00
Nodes (3): LevelService, SkillService, Skills / Level Subsystem

### Community 1725 - "Map Regression Tests Proposal"
Cohesion: 0.67
Nodes (3): ASCII Map Context Preparation, ASCII Minimap Generation, Map Regression Tests Proposal

### Community 1726 - "10 Concurrent Players Load Test"
Cohesion: 0.67
Nodes (3): who Command Unawaited Coroutine Bug, 10 Concurrent Players Load Test, Load Test Suite

### Community 1727 - "Scenario 20 Logout Errors"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 1728 - "Scenario 34 Two Players Same Room Visibility"
Cohesion: 0.67
Nodes (3): Scenario 34 Two Players Same Room Visibility, Scenario 36 Movement Visibility, Scenario 37 Chat Message Ordering

### Community 1729 - "E2E Session Report 2025-12-02"
Cohesion: 0.67
Nodes (3): Admin Teleportation Display Bug, E2E Session Report 2025-12-02, Whisper Messages Not Received Bug

### Community 1730 - "Playwright MCP Primary Testing Tool"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 1731 - "Whisper NATS Subject Bug Fix"
Cohesion: 0.67
Nodes (3): chat.whisper.player Subject Segment, Whisper NATS Subject Bug Fix, Whisper Work Completed and Remaining

### Community 1732 - "Dependency Review Workflow"
Cohesion: 0.67
Nodes (3): Dependabot Dependency Updates, Dependency Review Workflow, UV Lock Dependency Snapshot Gate

### Community 1733 - "Impeccable design context"
Cohesion: 0.67
Nodes (3): Impeccable design context, Legibility under pressure, Dark terminal-first aesthetic

### Community 1734 - "NPCs Not Updating On Player Movement"
Cohesion: 0.67
Nodes (3): exclude_player Occupants Snapshot Pattern, NPCs Not Updating On Player Movement, Canonical Room ID NPC Matching Remediation

### Community 1735 - "Combat Messages Dual Panel Display"
Cohesion: 0.67
Nodes (3): Combat Turn Order UUID Display, Combat Messages Dual Panel Display, Missing NPC Death Message Handlers

### Community 1736 - "Test Suite Stall After Performance Comparison"
Cohesion: 0.67
Nodes (3): Docker Build mythos_unitql Typo, Test Suite Stall After Performance Comparison, thread.join Without Timeout Hang

### Community 1737 - "Client Updates System Audit"
Cohesion: 0.67
Nodes (3): Architecture Review Plan, Option C Replacement Client Updates, Client Updates System Audit

### Community 1738 - "Cursor Rules as Canonical Config"
Cohesion: 0.67
Nodes (3): Cursor-Centric AI Config, Cursor Rules as Canonical Config, GitHub Worktrees Cursor Setup

### Community 1739 - "Logging Aggregator Verification"
Cohesion: 0.67
Nodes (3): Logging Aggregator Verification, warnings.log and errors.log Aggregators, Structlog Anti-Pattern Remediation

### Community 1740 - "Memory Leak Remediation"
Cohesion: 0.67
Nodes (3): Closed WebSockets Deque Cap, Memory Leak Metrics Collection, Memory Leak Remediation

### Community 1741 - "Playwright DI Migration Validation"
Cohesion: 0.67
Nodes (3): Playwright Best-Practices Remediation, Playwright DI Migration Validation, E2E Harness Overhaul

### Community 1742 - "Server Authority Remediation"
Cohesion: 0.67
Nodes (3): game_state Room Replace (not Merge), Server Authority Remediation, Server Authority Rule

### Community 1751 - ".get_task_lifecycle_metrics"
Cohesion: 0.33
Nodes (3): Get count of active tasks., Get task breakdown by type., Get task lifecycle metrics including creation and completion rates.

### Community 1753 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

### Community 1754 - "Any"
Cohesion: 0.15
Nodes (8): Any, Get metrics history. Args: limit: Optional limit on number of records Returns:…, Get active alerts. Returns: List[Dict[str, Any]]: Active alerts, Get all alerts. Returns: List[Dict[str, Any]]: All alerts, Get monitoring summary. Returns: Dict[str, Any]]: Monitoring summary, Convenience function to record combat error. Args: error_type: Type of error…, Convert to dictionary., record_combat_error()

### Community 1755 - "Any"
Cohesion: 0.17
Nodes (7): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Check if new data is newer than old data for a specific key. Args: old_data:…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,…, Store room data in cache. Args: room_id: Room ID to store room_data: Room data…

### Community 1758 - "get_hash_info"
Cohesion: 0.33
Nodes (6): get_hash_info(), Extract parameters from an Argon2 hash string., Test get_hash_info with valid Argon2 hash., Test get_hash_info with invalid hash returns None., test_get_hash_info_invalid(), test_get_hash_info_valid()

### Community 1760 - "asyncio"
Cohesion: 0.15
Nodes (13): asyncio, Test get_decayed_containers with None time., Test soft_delete_player delegates to PlayerRepository., Test apply_lucidity_loss delegates to ExperienceRepository., Test apply_fear delegates to ExperienceRepository., Test apply_corruption delegates to ExperienceRepository., Test heal_player delegates to HealthRepository., test_apply_corruption_delegates() (+5 more)

### Community 1761 - ".validate_combat_command"
Cohesion: 0.17
Nodes (7): Any, Initialize the combat validator. Args: party_service: Optional PartyService for…, Validate a combat command with thematic error messages. Args: command_data: The…, Check if target name is valid., Check for suspicious patterns in target name., Check if player is rate limited., Get a thematic combat status message.

### Community 1763 - "Profession"
Cohesion: 0.06
Nodes (41): CharacterNameScreenProps, CreateCharacterPayload, MechanicalEffect, Profession, ProfessionCard(), ProfessionCardProps, StatRequirement, ProfessionSelectionContentProps (+33 more)

### Community 1764 - "MythosMUD Server Runbook Skill"
Cohesion: 0.67
Nodes (3): MythosMUD Server Runbook Skill, MythosMUD Worktree Workflow Skill, One Server Only Rule

### Community 1769 - "mark_player_seen_impl"
Cohesion: 0.33
Nodes (5): mark_player_seen_impl(), Update last-seen timestamp for a player and all their connections., Update last-seen timestamp for a player and all their connections., Test mark_player_seen_impl() marks player as seen., test_mark_player_seen_impl()

### Community 1886 - "TestNATSError"
Cohesion: 0.33
Nodes (4): Test suite for NATSError base class., Test NATSError can be created with a message., Test NATSError inherits from Exception., TestNATSError

### Community 1901 - "TestGracefulDegradation"
Cohesion: 0.33
Nodes (4): Test graceful_degradation context manager., Test graceful_degradation with successful operation., Test graceful_degradation catches exceptions., TestGracefulDegradation

### Community 1906 - "EventHandler"
Cohesion: 0.06
Nodes (41): _as_event_data_dict(), EventHandler, _npc_died_ids_or_warn(), _participant_key_strings(), Handler for NATS event messages., Initialize event handler. Args: connection_manager: ConnectionManager instance…, Get mapping of event types to their handler methods. Returns: Dictionary…, Validate that event message has required fields. Args: event_type: Event type… (+33 more)

### Community 1914 - ".create_stand_command"
Cohesion: 0.33
Nodes (5): Test create_stand_command() creates StandCommand., Test create_stand_command() raises error with args., test_create_stand_command(), test_create_stand_command_with_args(), Create StandCommand from arguments.

### Community 1916 - "_format_container_contents"
Cohesion: 0.17
Nodes (12): _format_container_contents(), Format container contents as list of lines., Test _format_container_contents() with empty list., Test _format_container_contents() with items having quantity., test_format_container_contents_empty(), test_format_container_contents_with_quantity(), Test formatting container contents with items., Test formatting container contents when empty. (+4 more)

### Community 1918 - ".create_unfollow_command"
Cohesion: 0.33
Nodes (5): Test create_unfollow_command() creates UnfollowCommand with no args., Test create_unfollow_command() raises error with args., test_create_unfollow_command(), test_create_unfollow_command_with_args(), Create UnfollowCommand from arguments.

### Community 1919 - "._execute_command_handler"
Cohesion: 0.40
Nodes (3): CommandHandler, Execute command handler with error handling. Returns: dict: Command result, Register a new command handler. Args: command: Command name handler: Handler…

### Community 1923 - "spell_effects.py"
Cohesion: 0.08
Nodes (44): coerce_effect_float_times_mastery_as_int(), combat_room_id_for_npc_spell(), Internal helpers for spell_effects.py (coercion, combat room lookup). Keeps the…, Coerce to float first, then apply mastery (lucidity-style deltas)., Active combat room_id for an NPC, if any., Spell effects processing engine. This module handles applying spell effects to…, apply_stat_modifications(), Stat modification helpers for spell effects. This module contains utility… (+36 more)

### Community 1925 - ".validate_rate_limits"
Cohesion: 0.40
Nodes (3): field_validator, Validate rate limits are reasonable., Ensure we never divide by zero or run the chronicle backward.

### Community 1927 - "test_combat_configuration_service.py"
Cohesion: 0.20
Nodes (9): CombatConfigurationError, CombatConfigurationScope, Enum, Exception, Update combat configuration. Args: updates: Dictionary of configuration updates…, Clear configuration override for a specific scope. Args: scope: Configuration…, Exception raised for combat configuration errors., Scope for combat configuration changes. (+1 more)

### Community 1935 - "get_alerts"
Cohesion: 0.40
Nodes (5): get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing)

### Community 1947 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, Test cast command when player is not found., Cast command returns incapacitated message when player has 0 to -9 DP (prone,…, Test cast command with target., Test learn command when spell learning service is not available., Test learn command when no spell name is provided., Test announce spell cast when chat service is not available., Test handle_cast_command wrapper when magic service is not available. (+9 more)

### Community 1948 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1951 - ".validate_derived_stats"
Cohesion: 0.40
Nodes (3): field_validator, Validate stats are in valid range., Validate derived stats values.

### Community 1956 - "._error_callback"
Cohesion: 0.50
Nodes (3): Exception, Handle NATS errors. AI: Runs as fire-and-forget async task to prevent blocking…, Async handler for NATS connection errors.

### Community 1957 - "_AppStateWithLegacyConfig"
Cohesion: 0.40
Nodes (5): _AppStateWithLegacyConfig, _AppWithLegacyConfigState, Protocol, Minimal app.state shape for legacy error-handler debug config., Minimal FastAPI app shape for reading legacy config from state.

### Community 1958 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 1963 - "TestGlobalFunctions"
Cohesion: 0.17
Nodes (7): Test suite for global convenience functions., Test get_feature_flags returns the global service instance., Test global is_combat_enabled function., Test global is_combat_logging_enabled function., Test global is_combat_monitoring_enabled function., Test refresh_feature_flags clears cache., TestGlobalFunctions

### Community 1964 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1968 - "get_session_connections_impl"
Cohesion: 0.40
Nodes (4): get_session_connections_impl(), Get all connection IDs for a session., Get all connection IDs for a session., test_get_session_connections_impl()

### Community 1969 - "Any"
Cohesion: 0.18
Nodes (6): Any, Retrieve and remove oldest message from DLQ (async version). Returns: Message…, Retrieve and remove oldest message from DLQ (sync version). Returns: Message…, Get DLQ statistics. Returns: Dictionary with DLQ metrics AI: For monitoring…, List messages in DLQ without removing them. Args: limit: Maximum number of…, Convert message to dictionary for JSON serialization.

### Community 1970 - "WearableContainerServiceError"
Cohesion: 0.07
Nodes (28): Base exception for wearable container service operations., WearableContainerServiceError, Test add_items_to_wearable_container raises error when container not found., Test add_items_to_wearable_container raises error when capacity exceeded., Test handle_container_overflow raises error when player not found., Test handle_equip_wearable_container handles container creation error., Test add_items_to_wearable_container raises error when container belongs to…, Test add_items_to_wearable_container raises error when container is not… (+20 more)

### Community 1971 - ".add_message"
Cohesion: 0.18
Nodes (6): Any, Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…, Check if a message is recent (within the specified age limit). Args: msg:…, Get message queue statistics. Returns: Dict[str, Any]: Statistics about the…, Add a message to a player's pending message queue. Args: player_id: The…, Get all pending messages for a player and clear the queue. Args: player_id: The…

### Community 1972 - ".get_active_sessions"
Cohesion: 0.40
Nodes (3): Any, Get list of active admin sessions. Returns: List of active session information, Get audit log entries. Args: limit: Maximum number of entries to return…

### Community 1973 - ".get_combat_settings_summary"
Cohesion: 0.20
Nodes (6): Any, Get all active configuration overrides. Returns: Dict[str, Dict[str, Any]]:…, Get summary of combat settings for monitoring. Returns: Dict[str, Any]: Combat…, Convert to dictionary., Create from dictionary., Test from_dict creates configuration from dictionary.

### Community 1974 - "nats_broker"
Cohesion: 0.40
Nodes (5): nats_broker(), nats_config(), fixture, Create a NATSConfig instance., Create a NATSMessageBroker instance.

### Community 1975 - "_PlayerCombatClearing"
Cohesion: 0.20
Nodes (8): _PlayerCombatClearing, Protocol, Minimal surface used by this service to publish respawn-related events., Deliver a respawn-related domain event to the game's event bus., Minimal surface used to clear combat state when a player respawns., Drop combat involvement for this player after respawn., Initialize the player respawn service. Args: event_bus: Optional event bus for…, _RespawnEventPublisher

### Community 1976 - "fixture"
Cohesion: 0.18
Nodes (11): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), fixture, Create a mock room manager., Create a mock get_async_persistence callback. (+3 more)

### Community 1977 - "fixture"
Cohesion: 0.18
Nodes (11): health_monitor(), mock_cleanup_dead_websocket(), mock_is_websocket_open(), mock_performance_tracker(), mock_validate_token(), fixture, Create a mock is_websocket_open callback., Create a mock validate_token callback. (+3 more)

### Community 1978 - "message_filtering_helper"
Cohesion: 0.40
Nodes (5): message_filtering_helper(), mock_connection_manager(), fixture, Create a mock connection manager., Create a MessageFilteringHelper instance.

### Community 1979 - "MonkeyPatch"
Cohesion: 0.18
Nodes (11): MonkeyPatch, Test _load_alias_data handles IO errors gracefully., Test _save_alias_data handles IO errors., Test delete_player_aliases handles IO errors., Test backup_aliases handles IO errors., Test AliasStorage initialization with ALIASES_DIR environment variable., test_alias_storage_init_with_env_var(), test_backup_aliases_io_error() (+3 more)

### Community 1980 - "server/tests/conftest.py"
Cohesion: 0.20
Nodes (13): Config, Item, _apply_path_based_markers(), _get_db_name_from_url(), pytest_collection_modifyitems(), Test configuration and fixtures for MythosMUD greenfield test suite. This…, True when the collected test file lives under a unit/integration/e2e directory., Append @group to pytest Item nodeid for xdist --dist loadgroup scheduling.… (+5 more)

### Community 1981 - "messaging_integration"
Cohesion: 0.40
Nodes (5): messaging_integration(), mock_connection_manager(), fixture, Create mock connection manager., Create CombatMessagingIntegration instance.

### Community 1982 - "Success Metrics"
Cohesion: 0.50
Nodes (4): Functional Metrics, Quality Metrics, Success Metrics, Timeline Metrics

### Community 1983 - "Executive Summary"
Cohesion: 0.50
Nodes (4): Executive Summary, 🟡 IMPORTANT (Medium-Value):**~2,500-3,000 tests (50-60%) —**~15-18 minutes, Key Findings, Test Value Distribution

### Community 1985 - "_FakeMessageQueue"
Cohesion: 0.20
Nodes (3): _FakeMessageQueue, _FakeRateLimiter, _FakeRoomManager

### Community 2000 - "webhook"
Cohesion: 0.50
Nodes (4): post, Request, Receive and log alert webhooks, webhook()

### Community 2003 - "test_room_subscription_manager.py"
Cohesion: 0.20
Nodes (9): Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test add_room_occupant() adds occupant., Test add_room_occupant() adds occupant to existing room., Test remove_room_occupant() handles errors gracefully., Test unsubscribe_from_room() removes room when last subscriber leaves., test_add_room_occupant(), test_add_room_occupant_existing_room(), test_remove_room_occupant_error_handling() (+1 more)

### Community 2004 - "_spawn_rule_row"
Cohesion: 0.20
Nodes (10): Test get_spawn_rules() successfully retrieves rules., Test get_spawn_rule() returns rule when found., Test create_spawn_rule() successfully creates rule., Test delete_spawn_rule() successfully deletes rule., Build procedure result row for NPCSpawnRule., _spawn_rule_row(), test_create_spawn_rule_success(), test_delete_spawn_rule_success() (+2 more)

### Community 2005 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 2006 - ".get_memory_status_report"
Cohesion: 0.22
Nodes (5): Any, Generate status report for diagnostic monitoring. Returns: Dictionary…, Runtime detection and cleanup of orphaned tasks based on memory thresholds.…, Get current memory usage in bytes for this process., Get count of active tasks in the current event loop.

### Community 2007 - "process_zone_rows"
Cohesion: 0.25
Nodes (8): process_zone_rows(), Process zone rows from database and populate zone configurations. Args: conn:…, Test process_zone_rows() handles empty result., Test process_zone_rows() parses JSON string fields., Test process_zone_rows() processes zone rows., test_process_zone_rows(), test_process_zone_rows_empty(), test_process_zone_rows_json_strings()

### Community 2008 - "convert_schema_to_dict"
Cohesion: 0.22
Nodes (8): Any, Convert alias to dictionary for JSON serialization., convert_schema_to_dict(), Convert Pydantic schema to dictionary., Test convert_schema_to_dict() uses model_dump() when available., Test convert_schema_to_dict() uses dict() when model_dump() not available., test_convert_schema_to_dict_with_dict(), test_convert_schema_to_dict_with_model_dump()

### Community 2009 - "CircuitBreakerOpen"
Cohesion: 0.22
Nodes (9): CircuitBreakerOpen, Exception, Exception raised when circuit breaker is open. Indicates the protected service…, Test CircuitBreakerOpen exception., test_circuit_breaker_open_exception(), Test _handle_nats_message() handles circuit breaker open., Test _handle_nats_message uses 'unknown' as default message_id when missing., test_handle_nats_message_circuit_breaker_open() (+1 more)

### Community 2010 - "Path"
Cohesion: 0.22
Nodes (5): Path, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve message for replay and remove from DLQ. Args: filepath: Path to DLQ…, Delete a message from DLQ without processing. Args: filepath: Path to DLQ file…

### Community 2011 - "convert_room_players_uuids_to_names_impl"
Cohesion: 0.50
Nodes (3): convert_room_players_uuids_to_names_impl(), Convert player UUIDs and NPC IDs in room_data to names., Convert player UUIDs and NPC IDs in room_data to names.

### Community 2013 - "get_combat_monitoring"
Cohesion: 0.50
Nodes (4): get_combat_monitoring(), Get the global combat monitoring service instance. Returns:…, Test get_combat_monitoring returns global instance., test_get_combat_monitoring()

### Community 2014 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 2015 - "test_help_commands.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for help command handlers. Tests the help command functionality., Test handle_help_command() returns general help when no topic., Test handle_help_command() returns help for specific topic., Test handle_help_command() handles unknown topic., test_handle_help_command_no_topic(), test_handle_help_command_unknown_topic(), test_handle_help_command_with_topic()

### Community 2016 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 2017 - "Enum"
Cohesion: 0.22
Nodes (9): MockEffectType, MockRangeType, MockSchool, MockTargetType, Enum, Mock spell school enum., Mock target type enum., Mock range type enum. (+1 more)

### Community 2020 - "id"
Cohesion: 0.67
Nodes (3): minLength, type, id

### Community 2021 - "test_skill_use_log_repository.py"
Cohesion: 0.33
Nodes (8): _mock_session(), asyncio, fixture, Unit tests for SkillUseLogRepository., repo(), test_get_skill_ids_used_at_level(), test_record_use(), test_record_use_db_error()

### Community 2022 - "npc_service"
Cohesion: 0.22
Nodes (9): mock_session(), npc_service(), fixture, Create a mock AsyncSession., Create NPCService instance., Create a sample NPC definition., Create a sample spawn rule., sample_npc_definition() (+1 more)

### Community 2023 - "applies_to"
Cohesion: 0.67
Nodes (3): minItems, type, applies_to

### Community 2024 - "initialize_components"
Cohesion: 0.36
Nodes (7): initialize_components(), Any, Prepare component state metadata for a new item instance. This routine…, Unit tests for item component hooks., test_initialize_components_empty_prototype(), test_initialize_components_merges_overrides(), test_initialize_components_records_prototype_components()

### Community 2028 - "get_commands_by_category"
Cohesion: 0.67
Nodes (3): get_commands_by_category(), Any, Get all commands in a specific category.

### Community 2029 - ".from_dict"
Cohesion: 0.25
Nodes (7): Reconstruct message from dictionary., Test DeadLetterMessage.from_dict() reconstructs message., Test DeadLetterMessage.from_dict() handles string timestamp., Test DeadLetterMessage.from_dict() handles datetime timestamp., test_dead_letter_message_from_dict(), test_dead_letter_message_from_dict_datetime_timestamp(), test_dead_letter_message_from_dict_string_timestamp()

### Community 2030 - "event_bus"
Cohesion: 0.67
Nodes (3): event_bus(), fixture, Create an EventBus instance.

### Community 2031 - "renderer"
Cohesion: 0.67
Nodes (3): fixture, Return a fresh AsciiMapRenderer instance for each test., renderer()

### Community 2032 - "mock_connection_manager"
Cohesion: 0.67
Nodes (3): mock_connection_manager(), fixture, Create mock connection manager.

### Community 2038 - "occupant_display.py"
Cohesion: 0.46
Nodes (7): _apply_grace_badges(), format_occupant_display_name(), _parse_occupant_player_id(), Any, UUID, Shared occupant display names for look text and Occupants panel events., Format an in-room player's Occupants/look name. Always list; grace badges only.

### Community 2047 - "test_room_class.py"
Cohesion: 0.25
Nodes (7): Unit tests for Room class. Tests the Room class methods for managing room…, Test Room.get_objects() returns list of object IDs., Test Room.has_player() returns True if player in room., Test Room initialization with minimal data., test_room_get_objects(), test_room_has_player(), test_room_init_defaults()

### Community 2048 - "_FakeEstablishmentManager"
Cohesion: 0.20
Nodes (4): _FakeEstablishmentManager, _FakePerformanceTracker, _FakeRoomManager, Typed stand-in for ConnectionManager; MagicMock attributes are Any.

### Community 2049 - "test_connection_rate_limiter.py"
Cohesion: 0.25
Nodes (7): Unit tests for rate limiter. Tests the rate_limiter module classes and…, Test RateLimiter.cleanup_old_message_attempts() removes empty entries., Test RateLimiter.cleanup_old_message_attempts() handles errors., Test RateLimiter.get_rate_limit_info() returns correct info., test_rate_limiter_cleanup_old_message_attempts_error(), test_rate_limiter_cleanup_old_message_attempts_removes_empty(), test_rate_limiter_get_rate_limit_info()

### Community 2051 - "._handle_nats_message_impl"
Cohesion: 0.33
Nodes (4): Any, Initialize the NATS EventBus bridge. Args: event_bus: Local EventBus instance…, Process a NATS message - deserialize and inject into local EventBus. Public for…, Handle message received from NATS - deserialize and inject into local EventBus.

### Community 2052 - ".check_player_connection_health"
Cohesion: 0.29
Nodes (4): Any, Stop the periodic health check task. This should be called during application…, Wait for a task to be cancelled, with timeout., Check the health of all connections for a player. Args: player_id: The player's…

### Community 2057 - ".auto_progression_enabled"
Cohesion: 0.29
Nodes (5): setter, Return whether auto-progression is enabled., Enable or disable combat auto-progression., Return the turn interval in seconds., Set the turn interval in seconds.

### Community 2059 - "movement_service"
Cohesion: 0.29
Nodes (7): mock_event_bus(), mock_persistence(), movement_service(), fixture, Create a mock persistence layer., Create a mock event bus., Create a MovementService instance.

### Community 2060 - "fixture"
Cohesion: 0.29
Nodes (7): mock_event_bus(), mock_npc_service(), mock_persistence(), fixture, Create mock persistence layer., Create mock event bus., Create mock NPC combat integration service (no _rewards so XP uses fallback…

### Community 2063 - "._background_audit_cycle"
Cohesion: 0.33
Nodes (3): Core capability for granular investigation cycles. Repeated universal analysis…, Start the background auditing scheduler responsible for identifying orphan…, Primary background cycle consuming auditor implementation. Executes periodic…

### Community 2067 - "test_auth"
Cohesion: 0.33
Nodes (6): Any, get, Root endpoint providing basic server information., Test endpoint to verify JWT authentication is working., read_root(), test_auth()

### Community 2068 - ".cleanup_empty_subzone_subscriptions"
Cohesion: 0.33
Nodes (3): Unsubscribe from local channel messages for a specific sub-zone. Args: subzone:…, Get list of players currently in a specific sub-zone. Args: subzone: Sub-zone…, Clean up sub-zone subscriptions that have no active players.

### Community 2069 - ".handle_player_movement"
Cohesion: 0.33
Nodes (3): Track a player's sub-zone subscription for local channels. Args: player_id:…, Handle player movement between rooms and update sub-zone subscriptions. Args:…, Subscribe to local channel messages for a specific sub-zone. Args: subzone:…

### Community 2073 - ".__init__"
Cohesion: 0.33
Nodes (5): normalize_environment_config(), Any, Normalize environment config to validated structure., load_lucidity_rate_overrides(), Load lucidity rate overrides from PostgreSQL zones/subzones tables.

### Community 2077 - "test_websocket_handler_disconnect.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler disconnect handling. Tests the disconnect…, Test _handle_websocket_disconnect() returns True., Test _handle_websocket_disconnect() with no connection_id., test_handle_websocket_disconnect(), test_handle_websocket_disconnect_no_connection_id()

### Community 2078 - "test_websocket_handler_helpers.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler helper functions. Tests the helper functions…, Test _is_websocket_disconnected() returns True for disconnection messages., Test _is_websocket_disconnected() returns False for other messages., test_is_websocket_disconnected_false(), test_is_websocket_disconnected_true()

### Community 2079 - "metadata"
Cohesion: 0.67
Nodes (3): additionalProperties, type, metadata

### Community 2083 - ".get_decayed_containers"
Cohesion: 0.40
Nodes (3): datetime, Update the last_active timestamp for a player. Delegates to PlayerRepository., Get decayed containers.

### Community 2092 - "get_npcs_batch_impl"
Cohesion: 0.40
Nodes (4): get_npcs_batch_impl(), Get NPC names for multiple NPCs in a batch operation., Get NPC names for multiple NPCs in a batch operation., test_get_npcs_batch_impl()

### Community 2094 - "handle_player_entered_room_impl"
Cohesion: 0.40
Nodes (4): handle_player_entered_room_impl(), Handle PlayerEnteredRoom events by broadcasting updated occupant count., Handle PlayerEnteredRoom events by broadcasting updated occupant count., test_handle_player_entered_room_impl()

### Community 2095 - "periodic_health_check_impl"
Cohesion: 0.40
Nodes (4): periodic_health_check_impl(), Periodic health check task that runs continuously., Periodic health check task that runs continuously., test_periodic_health_check_impl()

### Community 2096 - "_EventBusPublishPort"
Cohesion: 0.40
Nodes (4): _EventBusPublishPort, Protocol, Minimal surface for publishing domain events from ConnectionManager.event_bus., Publish a single event to the in-process bus.

### Community 2098 - "pytest_asyncio_loop_factories"
Cohesion: 0.50
Nodes (5): _create_test_event_loop(), AbstractEventLoop, pytest_asyncio_loop_factories(), Create an event loop suitable for MythosMUD tests. CRITICAL: On Windows,…, Register platform-appropriate loop factories for pytest-asyncio (Python 3.14+…

### Community 2102 - ".service"
Cohesion: 0.40
Nodes (3): fixture, Create a mock config object., Create a CombatConfigurationService instance for testing.

### Community 2104 - ".__call__"
Cohesion: 0.40
Nodes (3): LiabilityStackEntry, Decode stored liability text (or empty state) into stack rows., Encode stack rows into JSON suitable for PlayerLucidity.liabilities.

### Community 2105 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 2108 - "_set_default_if_missing"
Cohesion: 0.50
Nodes (3): Initialize NPCDefinition with defaults., Apply a default attribute value when SQLAlchemy leaves it unset or None., _set_default_if_missing()

### Community 2113 - "test_is_shutdown_pending_no_state"
Cohesion: 0.50
Nodes (4): _AppWithoutState, Test is_shutdown_pending() returns False when app has no state., App double with no state attribute (is_shutdown_pending must return False)., test_is_shutdown_pending_no_state()

### Community 2117 - "test_asyncio_run_guardrails.py"
Cohesion: 0.50
Nodes (3): Test that server library code does not use asyncio.run() (AnyIO best practice).…, Assert server/ has no asyncio.run() in library code (use anyio.run() at entry…, test_no_asyncio_run_in_server_library_code()

### Community 2118 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 2120 - "8. Error Handling and Debugging"
Cohesion: 0.67
Nodes (3): 8. Error Handling and Debugging, Common Debug Commands, Test Debugging

### Community 2123 - "_NpcWithLife"
Cohesion: 0.67
Nodes (3): _NpcWithLife, Protocol, NPC instance shape for alive check before accepting an attack target.

### Community 2148 - "monitor"
Cohesion: 0.67
Nodes (3): monitor(), fixture, Monitor with tiny thresholds for easy triggering in tests.

### Community 2149 - "auditor"
Cohesion: 0.67
Nodes (3): auditor(), fixture, Auditor with short interval and auto cleanup enabled.

### Community 2152 - "subscription_manager"
Cohesion: 0.67
Nodes (3): fixture, Create a RoomSubscriptionManager instance., subscription_manager()

### Community 2153 - "subscription_manager"
Cohesion: 0.67
Nodes (3): fixture, Create a RoomSubscriptionManager instance., subscription_manager()

### Community 2155 - "combat_validator"
Cohesion: 0.67
Nodes (3): combat_validator(), fixture, Create a CombatValidator instance.

### Community 2533 - "test_wearable_container_service.py"
Cohesion: 0.03
Nodes (82): asyncio, Unit tests for wearable container service. Tests the WearableContainerService…, Test handle_unequip_wearable_container returns None when no item_instance_id., Test handle_unequip_wearable_container preserves container., Test handle_unequip_wearable_container returns None when container not found., Test get_wearable_containers_for_player returns containers., Test get_wearable_containers_for_player returns empty list when no containers., Test get_wearable_containers_for_player handles errors gracefully. (+74 more)

## Knowledge Gaps
- **6141 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `JCODEMUNCH_MAX_FOLDER_FILES`, `@codacy/codacy-mcp` (+6136 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **914 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `ConnectionManager`, `test_player_respawn_service.py`, `test_shutdown_sequence.py`, `test_follow_service.py`, `test_connection_delegates.py`, `test_exceptions.py`, `container_query_helpers.py`, `CatatoniaRegistry`, `api/character_creation.py`, `test_container_persistence_async_helpers.py`, `connection_manager_methods.py`, `feature_flag_service.py`, `ApplicationContainer`, `equipment_helpers.py`, `TargetMatch`, `LoggedHTTPException`, `test_logger`, `pydantic.md`, `log_and_raise`, `LootAllRequest`, `OccupantFormatter`, `extract_player_name`, `test_container_websocket_events.py`, `api/monitoring.py`, `is_player_in_login_grace_period`, `NATSConnectionStateMachine`, `position_commands.py`, `test_who_commands.py`, `CombatService`, `pytest.md`, `look_container.py`, `command_handler_unified.py`, `Stats`, `ContainerComponent`, `NPCOccupantProcessor`, `catatonia_check.py`, `chat_service.py`, `test_error_handling_middleware.py`, `HealthStatus`, `test_player_presence_tracker.py`, `test_look_player.py`, `channel_broadcasting_strategies.py`, `npc_admin_mgmt_api.py`, `QuestService`, `test_npc_definitions_api.py`, `test_look_room.py`, `test_status_commands.py`, `real_time.py`, `EventBus`, `test_lucidity_recovery_commands.py`, `handle_emote_command`, `MessageBroadcaster`, `chat_channel_message_senders.py`, `PlayerOccupantProcessor`, `test_lifecycle_periodic.py`, `item_instance_persistence_async.py`, `persistence/container_persistence.py`, `server/schemas/__init__.py`, `lucidity_migration.py`, `quest_commands.py`, `test_aggro_threat.py`, `RoomService`, `get_admin_auth_service`, `test_go_command.py`, `CombatAuditLogger`, `CombatInstance`, `realtime/realtime.py`, `.__post_init__`, `test_logout_commands.py`, `ExceptionTracker`, `RoomRepository`, `player_inventory_migration.py`, `test_users.py`, `middleware`, `communication_commands_flows.py`, `talk_command.py`, `Player`, `dialogue_definitions_api.py`, `ContainerRepository`, `npc_combat_grace.py`, `test_lifespan_shutdown.py`, `look_command.py`, `PrototypeRegistryError`, `resolve_weapon_attack_from_equipped`, `test_container_persistence_crud.py`, `CommandRateLimiter`, `communication_commands.py`, `PayloadOptimizer`, `PlayerNameExtractor`, `message_handler_factory.py`, `nats_service.py`, `test_inventory_display_helpers.py`, `handle_read_command`, `container_endpoints_basic.py`, `admin_shutdown_command.py`, `npc_database.py`, `test_goto_helpers.py`, `fixtures/integration/__init__.py`, `TargetResolutionResult`, `persistence/container_helpers.py`, `HealthRepository`, `_find_item_in_equipped`, `CircuitBreaker`, `rest_countdown_task.py`, `connection_cleanup_methods.py`, `MythosMUDError`, `connection_manager_health_cleanup.py`, `PerformanceMonitor`, `test_quest_instance_repository.py`, `DialogueDefinitionRepository`, `ExperienceRepository`, `lucidity_communication_dampening.py`, `subject_controller.py`, `combat_attack.py`, `spell_effects.py`, `TaskRegistry`, `NATSPublishError`, `test_lifecycle_respawn.py`, `PhantomHostileService`, `player_connection_setup.py`, `NATSMessageBroker`, `server/tests/conftest.py`, `NATSConfig`, `game_tick_processing.py`, `optimized_security_validator.py`, `MovementMonitor`, `test_lucidity_command_disruption.py`, `server/dependencies.py`, `test_cache_service.py`, `DialogueService`, `spell_effects_status.py`, `container_query_helpers_async.py`, `zone_config_loader.py`, `disconnect_grace_period.py`, `.__init__`, `fake_hallucination_service.py`, `test_look_npc.py`, `test_party_commands.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `RoomIDUtils` connect `RoomIDUtils` to `ConnectionManager`, `NPCOccupantProcessor`, `.__init__`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Why does `ValidationError` connect `ValidationError` to `ConnectionManager`, `test_command_service.py`, `test_movement_service.py`, `EnvironmentalContainerLoader`, `get_logger`, `test_exceptions.py`, `.get_instance`, `get_database_path`, `api/character_creation.py`, `item_instance_persistence_async.py`, `persistence/container_persistence.py`, `test_container_persistence_async_helpers.py`, `test_profession_service.py`, `test_error_logging.py`, `ModerationCommandFactory`, `test_command_helpers.py`, `LoggedHTTPException`, `pydantic.md`, `test_player_service.py`, `ContainerService`, `container_endpoints_basic.py`, `log_and_raise`, `PlayerRespawnWrapper`, `test_go_command.py`, `test_command_parser_helpers.py`, `TestValidateRoomData`, `test_command_processing.py`, `UtilityCommandFactory`, `npc_database.py`, `.create_unfollow_command`, `NPCCombatIntegration`, `test_command_parser.py`, `Stats`, `persistence/container_helpers.py`, `ContainerComponent`, `test_remove_player_invalid_params`, `server/persistence/__init__.py`, `test_database_helpers.py`, `asyncio`, `patch`, `test_move_player_empty_player_id`, `ExplorationCommandFactory`, `test_character_creation_service.py`, `Player`, `TestErrorHandlers`, `test_move_player_invalid_to_room`, `.create_go_command`, `.create_ground_command`, `test_inventory_helpers_extended.py`, `MythosMUDError`, `get_engine`, `PlayerStateCommandFactory`, `test_player_service_mutations.py`, `test_emote_service.py`, `get_async_session`, `PydanticErrorHandler`, `DatabaseManager`, `EventBus`, `.create_stand_command`, `ExperienceRepository`, `CommunicationCommandFactory`, `test_container_persistence_crud.py`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Are the 137 inferred relationships involving `LoggedHTTPException` (e.g. with `logged_http_exception_handler()` and `register_error_handlers()`) actually correct?**
  _`LoggedHTTPException` has 137 INFERRED edges - model-reasoned connections that need verification._
- **Are the 223 inferred relationships involving `ValidationError` (e.g. with `fetch_user_by_username_case_insensitive()` and `load_database_url()`) actually correct?**
  _`ValidationError` has 223 INFERRED edges - model-reasoned connections that need verification._
- **Are the 90 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 90 INFERRED edges - model-reasoned connections that need verification._
- **Are the 79 inferred relationships involving `AliasStorage` (e.g. with `_ensure_alias_storage()` and `_handle_special_command_routing()`) actually correct?**
  _`AliasStorage` has 79 INFERRED edges - model-reasoned connections that need verification._