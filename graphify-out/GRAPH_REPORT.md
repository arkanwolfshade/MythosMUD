# Graph Report - MythosMUD  (2026-09-15)

## Corpus Check
- 3431 files · ~3,590,413 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 56496 nodes · 105916 edges · 2300 communities (1766 shown, 534 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 6144 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7132bdf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- get_logger
- Invite
- test_users.py
- LootAllRequest
- Player
- UtilityCommandFactory
- server/dependencies.py
- test_npc_combat_integration_service.py
- ChatService
- server/services/__init__.py
- Room
- NATSService
- test_spell_effects.py
- NPCPopulationController
- test_security_validator.py
- Profession
- CombatTurnProcessor
- SecureBaseModel
- JsonMap
- LoggedHTTPException
- NPCDefinition
- ContainerTransferFromMixin
- test_rescue_service.py
- AliasStorage
- ContainerComponent
- api/character_creation.py
- test_combat_event_publisher.py
- HolidayService
- .auto_progression_enabled
- MemoryMonitor
- players.py
- EventBus
- get_npc_instance_service
- test_zone_config_loader.py
- InventoryMutationGuard
- InventoryCommandFactory
- test_combat_monitoring_service.py
- DatabaseManager
- ConnectionManager
- PlayerNameExtractor
- test_quest_instance_repository.py
- test_communication_commands_flows.py
- connection_manager_methods.py
- AsyncPersistenceLayer
- PlayerService
- useRespawnHandlers.ts
- test_lifespan_startup.py
- test_target_resolution_service.py
- ui-v2/types.ts
- test_corpse_lifecycle_service.py
- test_container_bundles.py
- Communities (355 total, 223 thin omitted)
- test_magic_commands.py
- test_command_parser.py
- HolidayCollection
- BaseCommand
- ChatHistoryPanel.tsx
- test_admin_auth_service.py
- test_look_container.py
- test_command_inventory.py
- NPCCombatIntegration
- test_nats_message_handler.py
- CommandValidator
- MythosTickScheduler
- inventory_equip_command.py
- SpellEffectType
- test_command_communication.py
- PanelState
- CombatService
- ._initialize_item_services
- CombatConfiguration
- magic_service_completion.py
- CORSConfig
- CombatInstance
- asyncio
- RoomLoader
- test_websocket_initial_state.py
- test_container_persistence_extended_parse.py
- ChatLogger
- test_admin_commands.py
- test_real_time_helpers.py
- test_passive_lucidity_flux_service.py
- PlayerRespawnEventHandler
- test_who_commands.py
- test_connection_delegates.py
- mythos_dev_ddl.sql
- test_look_room.py
- ExplorationCommandFactory
- test_rest_command.py
- NATSServicePoolMixin
- AsciiMapRenderer
- test_player_presence_tracker.py
- look_helpers.py
- NPCOccupantProcessor
- ContainerService
- chat_service.py
- system_monitoring.py
- WebSocketMessageValidator
- CombatParticipant
- npc_database.py
- test_chat_npc_system.py
- cleanse_command.py
- test_movement_service.py
- test_player_preferences_service.py
- maps.py
- test_combat_service_modules.py
- TestScheduleService
- seed_e2e_users.py
- .to_dict
- SubjectValidator
- test_npc_utils.py
- Alias
- server/schemas/__init__.py
- request_with_app_container
- is_player_in_login_grace_period
- test_logging_utilities.py
- test_command_combat.py
- CombatMonitoringService
- container_events.py
- PlayerPositionService
- test_population_control.py
- rooms.py
- test_container_helpers_inventory_find.py
- NPCDefinitionCRUDMixin
- test_user_manager.py
- Reporter
- logoutHandler.ts
- test_manager.py
- test_look_player.py
- NPCCombatIntegrationService
- test_combat_persistence_handler_events.py
- test_container_helpers_inventory_ops.py
- TestHelperFunctions
- test_combat_handler.py
- IdleMovementHandler
- connection_manager.py
- test_rest_and_grace_period.py
- test_aggro_threat.py
- test_rate_limiter.py
- look_command.py
- ApplicationContainer
- mythos_e2e_ddl.sql
- test_websocket_handler_validation_errors.py
- FeatureFlagService
- test_player_event_handlers_utils.py
- TargetType
- test_logout_commands.py
- test_player_combat_service.py
- mythos_unit_ddl.sql
- test_connection_helpers_impl.py
- test_metrics_endpoints.py
- test_look_npc.py
- test_status_commands.py
- AppConfig
- test_quest_service.py
- test_logging_processors.py
- test_npc_service.py
- SchemaValidator
- manual_dependency_analysis.py
- api/monitoring.py
- admin_teleport_commands.py
- FollowService
- player.ts
- admin_setstat_command.py
- ChatModeration
- QuestService
- test_combat_schema.py
- deleteCharacterFlow.ts
- test_go_command.py
- test_lifecycle_periodic.py
- get_hallucinated_exits
- TaskRegistry
- test_game_state_provider.py
- MemoryLeakMetricsCollector
- test_message_queue.py
- NATSError
- container_persistence.py
- PopulationStats
- ExplorationService
- logging_file_setup.py
- dialogue_definitions_api.py
- CreateItemInstanceInput
- catatonia_check.py
- test_combat_flee_helpers.py
- test_shutdown_sequence.py
- player_presence_tracker.py
- useGameConnectionRefactored.ts
- test_player_event_handlers_room.py
- ContainerLockState
- test_party_service.py
- PerformanceMonitor
- executeCommand
- test_logging_handlers.py
- test_admin_setlucidity_command.py
- test_occupant_formatter.py
- RoomDataCache
- RoomDataValidator
- test_error_handling_middleware.py
- test_lucidity_recovery_commands.py
- test_hallucination_services.py
- test_lucidity_event_dispatcher.py
- PlayerStateCommandFactory
- GameConfig
- apiTypeGuards.ts
- ZoneConfiguration
- CombatAuditLogger
- MemoryProfiler
- test_alias_commands.py
- build_event
- test_room_sync_service.py
- LogAggregator
- admin_hallucinate_command.py
- test_enhanced_logging_config.py
- exception_metrics.py
- test_nats_message_handler_subzone_events.py
- game_state_provider.py
- inventory_command_helpers.py
- test_character_creation_service.py
- api/game.py
- test_async_persistence_core.py
- maps.ts
- Async Remediation Summary - December 3, 2025
- test_player_respawn_service.py
- TestCombatConfigurationService
- NPCThreadManager
- test_npc_startup_service.py
- lifespan_protocols.py
- compare_linting_results.py
- AsyncPersistenceRoomFacade
- CatatoniaRegistry
- test_metrics.py
- .resolve_target
- RoomMapViewer.tsx
- PlayerEventHandlerUtils
- HealthStatus
- PlayerRepositoryProtocol
- test_mp_regeneration_service.py
- ExceptionTracker
- catalog_commands.py
- DeadLetterQueue
- UserManager
- test_event_handler.py
- TargetMatch
- test_command_moderation.py
- NPCMovementIntegration
- test_player_service_mutations.py
- test_admin_commands_helpers.py
- useGameClientV2Container.ts
- test_level_service.py
- NATSRetryHandler
- LucidityService
- fixtures/auth.ts
- TestCombatMessagingService
- MonitoringDashboard
- TauntCommandHandler
- test_container_persistence_async_helpers.py
- test_inventory_display_helpers.py
- websocket_handler.py
- test_active_lucidity_service.py
- InstanceManager
- collect_inventory.py
- GameTickService
- devDependencies
- gen_arena_migration_sql.py
- .state
- useMythosAppActions.ts
- test_combat_service.py
- get_username_from_user
- test_command_processor.py
- NPCLifecycleManager
- get_item_catalog
- _prepare_command_for_processing
- test_rate_overrides.py
- send_game_event
- PlayerGuidFormatter
- projectorRoom.ts
- test_command_validator.py
- RoomService
- GameStateProvider
- player_event_handlers_respawn_room.py
- combat_turn_participant_actions.py
- test_windows_safe_rotation.py
- test_movement_monitor.py
- MemoryMonitor
- map_minimap.py
- NATSMessageSubscriptionMixin
- websocket_handler_commands.py
- test_nats_messages.py
- NPCCombatLucidity
- test_chat_logger.py
- test_player_respawn_api.py
- ResourceManager
- DialogueDefinitionRepository
- testing_examples.py
- test_party_commands.py
- StatusEffect
- test_npc_combat_handlers.py
- test_room_subscription_manager.py
- rescue_commands.py
- Any
- ✅ Phase 2 Async Persistence Migration - COMPLETE
- MythosMUD Test Suite Modernization Plan
- test_magic_service.py
- test_admin_summon_command.py
- test_command_magic.py
- npc_config_parsing.py
- AdminActionsLogger
- CharacterNameScreen.tsx
- alias_schema.json
- get_cached_player
- EmoteService
- websocket_helpers.py
- TestRoomDataFixer
- connection_cleanup_methods.py
- AliasGraph
- test_validation.py
- handle_read_command
- event_types.py
- retry.py
- debrief_command.py
- passive_lucidity_flux/service.py
- test_pattern_matcher.py
- should_spawn_npc
- test_combat_persistence_handler_persistence.py
- CoordinateGenerator
- command_guards.py
- combat_attack.py
- command_handler_unified.py
- App.tsx
- migrate_combat_data.py
- mock_app
- talk_command.py
- test_npc_threading_messages.py
- ConnectionCleaner
- test_player_occupant_processor.py
- verify_enhanced_logging_compliance.py
- CombatPersistenceHandler
- quality_fragmentation_lizard.py
- _str_id
- NPCCombatUUIDMapping
- test_shopkeeper_npc.py
- ContainerRepository
- test_audit_logger.py
- Uplift Strategy
- Test Suite Optimization Roadmap
- Test Suite Refactoring Plan
- Test Value Distribution Chart
- catalog_dml.py
- _handle_admin_set_stat_command
- TargetResolutionResult
- test_chat_nats_publisher.py
- fastapi_integration.py
- format_player_entry
- map/types.ts
- test_rooms_api.py
- test_map_helpers.py
- test_npc_spawn_rules_api.py
- CharacterInfoPanel.tsx
- mock_container
- test_passive_corruption_flux_rate_overrides.py
- vim Best Practices and Coding Standards
- Async Code Review - Post Phase 2 Migration
- FastAPI Code Review - Anti-Patterns and Best Practices
- E2E Test Suite AI Execution Improvements - Summary
- test_inventory_equip_command.py
- test_room_utils.py
- .create_combat_instance
- test_player_service.py
- WearableContainerService
- get_room_environment
- TestHierarchicalSchema
- RoomNodeData
- messageHandlers.ts
- mythos_e2e.players
- mythos_unit.players
- properties
- properties
- properties
- test_admin_teleport_commands.py
- .check_player_mute_status
- test_lucidity_models.py
- test_websocket_handler_coverage_gaps.py
- properties
- test_channel_commands.py
- NATSSubjectManager
- test_lint_pyright_suppressions.py
- test_rate_limiter_utils.py
- GameClientV2ContainerView.tsx
- utils/layout.ts
- 🧪 MythosMUD E2E Testing Strategy
- CorruptionRepository
- npcs/catalog_dml.py
- test_item.py
- player_connection_setup.py
- SkillRepository
- test_container_persistence_extended_crud.py
- test_message_broadcaster.py
- properties
- Memory Leak Prevention System - Implementation Summary
- deprecated_patterns.py
- test_player_requests.py
- SpellLearningService
- test_item_catalog.py
- PlayerDPUpdated
- npc_combat_integration_service.py
- test_websocket_handler_helpers.py
- test_config_models.py
- handle_quest_command
- LRUCache
- TrackedTaskManager
- PrototypeRegistry
- PlayerDeathService
- test_time_bundle.py
- ._build_player_attacked_event
- test_flee_command.py
- test_room_subscription_manager_helpers.py
- test_player_death_service.py
- useRoomEditModal.ts
- multiplayer-browser-helpers.js
- Chat Panel Separation Implementation Tasks
- Async Persistence Migration Plan
- migration_examples.py
- MessageBroadcaster
- passive_corruption_flux/service.py
- quest_commands.py
- test_catalog_commands.py
- test_dependency_analysis.py
- TestNPCCombatRewards
- TestEmitLootAllEvent
- asyncio
- RoomMapEditorRuntime.tsx
- Async Persistence Migration Tracker
- Phase 3, Task 3.2: NATS Subject Manager Usage Review
- Execution Steps
- properties
- TestValidatorComponents
- PayloadOptimizer
- lint_pyright_suppressions.py
- PydanticErrorHandler
- test_npc_event_handlers.py
- ChatPoseManager
- revised-character-creation.spec.ts
- authenticated.ts
- required
- Audit Coverage Boundary — 2026-08 Design Audit
- PostgreSQL & SQL Audit Report
- test_quality_fragmentation_guard.py
- PeriodicOrphanAuditor
- RoomCacheService
- admin_shutdown_command.py
- magic_healing_events.py
- websocket_integration.py
- NPCStartupService
- stateNormalization.ts
- File-by-File Changes
- validate.py
- test_game_tick_death.py
- Any
- LucidityTierCache
- ExperienceRepository
- test_inventory_get_command.py
- ConnectionErrorHandler
- test_player_event_handlers_room_left.py
- RateLimiter
- roomHandlers.ts
- e2e-bootstrap.ts
- multiplayer-colocated.ts
- FakeSenderRegistry
- ChatChannelLoggerMixin
- start_grace_period
- _find_item_in_equipped
- test_connection_state_machine.py
- Frontend Design Skill
- Async Audit Executive Summary
- Test Pruning Candidates - Detailed List
- ItemFactory
- FStringLoggingFixer
- combat_loader.py
- test_command_processing.py
- InventorySchemaValidationError
- GameMechanicsService
- MovementMonitor
- Profession
- PersonalMessageSender
- EventPublisher
- directionHallucination.ts
- CommandRateLimiter
- test_lifecycle_respawn.py
- test_inventory_mutation_guard_internal.py
- test_inventory_helpers_extended.py
- asyncio
- lint_optional_auth_no_guard.py
- CommandService
- Does Love Forgive_ (source summary)
- TEMPORAL_SYSTEM_RESEARCH.md
- Prometheus Configuration
- load_world_seed.py
- ReactNodeUpgradeAnalyzer
- MemoryThresholdMonitor
- _find_item_in_inventory
- DistributedEventBus
- test_item_prototype_models.py
- NPCCommunicationIntegration
- test_connection_establishment.py
- test_room_write_procedures.py
- ADR-025: Corruption as a Global Perceptual Filter, Not Per-Message Styling
- Any
- test_optimized_security_validator.py
- PathValidator
- scripts
- properties
- NATS Code Review - Branch: feature/sqlite-to-postgresql
- WebSocket Code Review - Branch: feature/sqlite-to-postgresql
- enum
- CombatEventHandler
- container_helpers_inventory_display.py
- zone_config_loader.py
- EventBusLifecycleMixin
- ContainerData
- get_help_content
- properties
- convert_uuids_to_strings
- test_lint_container_get_instance.py
- Async Remediation Final Report
- 🔴 CRITICAL ISSUES
- Test Suite Quality Audit - Executive Summary
- test_inventory_command_prototype.py
- properties
- PassiveMobNPC
- NATSConnectionStateMachine
- test_lifespan_event_subscriptions.py
- handle_logout_command
- test_chat_moderation.py
- test_lint_raw_sql_in_python.py
- Bug Investigator Subagent
- Code Review: Import Analysis and Anti-Patterns
- Domain Model Anemic Anti-Pattern Audit
- session_factory
- test_connection_room_utils.py
- zone_schema.json
- ErrorMonitor
- verify_linting_parity.py
- handle_skills_command
- test_npc_combat_integration_service_player_attacks.py
- RoomEventHandler
- validate_secure_path
- test_quest_service_collect.py
- test_combat_death_handler.py
- server/tests/conftest.py
- test_emote.py
- CorruptionService
- debugLogger
- Communities (19 total, 4 thin omitted)
- properties
- packages/README.md
- Persistence Layer Refactoring - COMPLETE ✅
- enum
- LogAnalyzer
- quality_fragmentation_ai_guardrails.py
- safe_run_static
- _NPCCombatIntegrationValidationDeps
- ._create_grid_map
- test_look_item_helpers.py
- MetricsCollector
- attach_compatibility_properties
- test_passive_corruption_flux_service.py
- extract_player_name
- test_health_monitor.py
- test_connection_session_management.py
- waitForMessage
- Path
- test_report_any_baseline.py
- test_support_helpers.py
- Dream Messaging Subsystem Design
- Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch
- .get_stats
- test_load_world_seed.py
- handle_emote_command
- test_chat_validator.py
- .load_from_path
- PlayerEffectRepository
- test_audit_suppressions.py
- _asyncio_mark
- .claude/hooks/record_edited_file.py
- Client Test Remediation
- FeedbackManager
- .cursor/hooks/record_edited_file.py
- Migration Strategy
- Async Facades Implementation - COMPLETE ✅
- Feature Requirements Document: Random Stats Generator
- Migration 019: Complete Implementation Summary
- Persistence Layer Async Migration Plan
- Phase 4: Recommendations
- fix_fstring_logging.py
- Stop-MythosMudProjectProcessTree
- TestRunner
- ._bind_event_type
- test_chat_pose_helpers.py
- BehaviorEngine
- test_channel_broadcasting_strategies.py
- PerformanceTester
- asyncio
- active_lucidity_service.py
- StatisticsAggregator
- test_command_factories_inventory_helpers.py
- ValidationRule
- test_request_schema_security.py
- SQLAlchemyAsyncLinter
- Test Suite Analyzer Subagent
- properties
- Onboard Skill
- DialogueEditorPage.tsx
- multiplayer-browser-helpers.bundle.js
- compilerOptions
- Dependency Upgrade Strategy Specification
- NATS Anti-Patterns and Best Practices Review
- format_markdown_file
- migrate_rooms.py
- handle_teach_command
- ContainerTransferToMixin
- _validate_command_basics
- test_inventory_mutation_guard.py
- playerHandlers.ts
- lifespan.py
- test_room_subscription_manager_npcs.py
- properties
- security.ts
- ADR-012: python-statemachine for Backend Connection FSM
- MythosMUD Code Quality Targets for AI
- MythosMUD Database Placement
- dependencies
- EdgeDetailsPanel.tsx
- MUD Disconnect Grace Period & Rest Command: Industry Comparison
- Chaosium CoC Catalog.md
- ApplicationContainer Structure Analysis and Domain-Specific Split Proposal
- ContainerRepository and ItemRepository: Review and Full Async Migration Plan
- MythosMUD Dependency Upgrade Strategy - Implementation Summary
- Documentation Updates - ConnectionManager Refactoring
- Persistence Layer Refactoring Summary
- TEST_AUDIT_EXECUTIVE_SUMMARY.md
- compilerOptions
- Execution Steps
- Execution Steps
- test_command_factories_inventory.py
- generate_html_visualization.py
- lint_container_get_instance.py
- verify_migration.py
- NPCCacheService
- realtime/realtime.py
- bind_request_context
- .create_put_command
- apply_communication_dampening
- test_room_service.py
- useMythosAppState.ts
- test_check_coverage_thresholds.py
- test_lint_optional_auth_no_guard.py
- Performance Profiler Subagent
- Security Auditor Subagent
- Lint Remediation Skill
- get_session_maker
- The Toolkit
- GameClientV2Dock.test.tsx
- Communities (10 total, 2 thin omitted)
- Game Subsystem Design Documents Overview
- Complexity Refactoring Test Plan
- NATS Complete Remediation Summary
- SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch
- Execution Steps
- fix_suppression_alignment.py
- identify_critical_code.py
- test_auth_rate_limit.py
- real_time.py
- Phase 1: Core Separation
- Phase 2: Enhanced Features
- test_player_repository_room.py
- .create_get_command
- MPRegenerationService
- test_security_utils.py
- test_players_procedures.py
- asyncio
- test_wearable_container_service.py
- overrides
- compilerOptions
- compilerOptions
- Communities (11 total, 0 thin omitted)
- Communities (11 total, 0 thin omitted)
- Asyncio Code Review - feature/sqlite-to-postgresql Branch
- Environment Contamination Audit Report
- Findings by Category
- NATS Medium-Priority Remediation Summary
- Phase 2 Async Persistence Migration - Status Update
- Pydantic Code Review - feature/sqlite-to-postgresql Branch
- Execution Steps
- TestNPCCombatLifecycle
- properties
- audit_suppressions.py
- fix_markdown_line_length.py
- populate_npc_sample_data.py
- .create_equip_command
- schemas/unified_room_schema.json
- properties
- test_lucidity_command_disruption.py
- test_exploration_procedures.py
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
- Scenario 22: Invite-Only Registration Enforcement
- LoggingPatternLinter
- required
- UpgradeImplementationPlan
- test_admin_shutdown_command.py
- properties
- NPCActionMessage
- NpcBaseStats
- .validate_entity_id
- schedule_end_combat_if_npc_died_best_effort
- NPCSpawnRuleCRUDMixin
- test_lru_cache.py
- TestVerificationSqlUsersPlayers
- utils/config.ts
- required
- optimized_validate_player_name
- subzone_schema.json
- static_data/package.json
- test_metadata.py
- submitAuth.ts
- Delight Techniques
- knip.json
- compilerOptions
- Enhanced Logging Best Practices for MythosMUD
- Persistence Layer Extraction - COMPLETE ✅
- Test Coverage Summary: Disconnect Grace Period & Rest Command
- enum
- test_email_utils.py
- properties
- ADR-027: NPC Catalog Base Stats Contracts
- parse_json_field
- ._damage_player_inner
- handle_unequip_command
- test_corruption_reactions.py
- Any
- fixtures/shared/__init__.py
- test_command_service.py
- _GenerateOpenapiSpecModule
- room_validator/tests/conftest.py
- coerce_int
- .build_subject
- Animate Skill
- Polish Systematically
- overrides
- Enhanced Logging Quick Reference
- Migration 019 Ready for Deployment
- Gladiator Ring (Arena) Implementation Plan
- Python Model Updates Required for Migration 019
- Recommended Test Additions
- Critical Coverage Gaps
- Execution Steps
- properties
- properties
- fix_markdown_blanks_around_lists.py
- init_npc_database.py
- test_profession_repository.py
- validate_admin_permission
- PartyService
- _make_mock_row
- Phase 3: Polish and Optimization
- test_player_spell_repository.py
- Phase 4: Testing and Refinement
- test_chat_message_senders.py
- Introduce Color Strategically
- saveMapChanges.ts
- usePanelContext.ts
- commandStore.ts
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)
- Petersen's Abominations.md
- Geography Overview.md
- Chaosium CoC Catalog
- players.sql
- applies_to
- Async Remediation Complete
- Execution Steps
- properties
- properties
- properties
- fix_file
- jackson_linter.py
- RoomFilenameMigrator
- game_tick_processing.py
- get_cache_manager
- ProfessionCacheService
- CacheManager
- test_occupants.py
- handle_time_command
- _ensure_alias_storage
- PlayerSchemaConverter
- command_service.py
- npc_combat_grace.py
- ._cleanup_player_mutes
- CoordinateValidator
- asyncio
- test_nats_message_handler_chat.py
- test_analyze_idle_memory_samples.py
- test_run_test_ci.py
- properties
- properties
- Codebase Explorer Subagent
- .accept_party_invite
- Adapt Skill
- Improve Copy Systematically
- UX Writing
- whisper-movement.spec.ts
- containers.sql
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)
- mythos_dev.players
- Changes by document
- Memory Leak Audit Report
- Quick Start: Running E2E Tests
- holiday.schema.json
- schedule.schema.json
- type
- analyze_coverage_gaps.py
- _apply_arena_seed_patch.py
- pylint.py
- generate_sql.mjs
- SpellMaterialsService
- UUID
- get_npc_name_from_instance
- bundles/game.py
- ContainerLockMixin
- command_result_text
- test_security_headers.py
- test_follow_flow.py
- CircuitBreaker
- test_check_pr_issue_references.py
- test_combat_messaging_integration.py
- test_player_repository.py
- test_check_no_production_assert.py
- HallucinationRng
- test_validate_codacy_coverage_gate.py
- ADR-018: New Game Session vs Grace Reconnect
- test_logging_file_categories.py
- Spatial Design
- Typography
- Fix patterns by tier
- Skill: Create a New Worktree for a Task
- MessageBatcher
- RateLimiter
- P4 · Intent Sweep — Core Feature Issues
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)
- rooms.sql
- required
- npc_schedules.schema.json
- DOCUMENTATION_AUDIT.md
- PARALLEL EXECUTION RESULTS (2025-11-05)
- Result
- fix_markdown_common_issues.py
- process_room_files
- validate_codacy_coverage_gate.py
- ProcessedRoomData
- test_look_item.py
- rest_countdown_task.py
- room_hierarchy_schema.json
- factory.py
- enum
- TestValidateRoomData
- Any
- Corruption Subsystem Design
- channel_broadcasting_strategies.py
- ADR-026: Item Catalog Metadata Contracts
- test_aggressive_mob_npc.py
- CorruptionTierCache
- asyncio
- is_safe_filename
- test_update_container_found_returns_the_id
- enum
- client/package.json
- event_publisher.py
- ADR-024: Server-Authoritative Perceived Reality for Hallucinations
- test_lint_imports.py
- update_container
- optimized_security_validator.py
- properties
- check_no_production_assert.py
- Generate Comprehensive Report
- Lint Remediation
- Optimize Skill
- Semgrep Configuration
- Test Server Remediation Prompt - Cursor Executable Version
- INDEX.md
- Decisions required
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)
- mythos_dev.rooms
- Migration 019 Verification Report
- NATS Anti-Patterns Remediation Summary
- analyze_log_file
- find_fstring_logging_violations
- check_pr_issue_references.py
- lint_raw_sql_in_python.py
- lint_sql_guardrails.py
- fixture
- RoomCacheLoader
- ChannelBroadcastingStrategyFactory
- handle_explore_command
- AsciiMapViewer.tsx
- event_handler.py
- Party
- test_get_npc_system_statistics_return_shape
- test_profession_service.py
- CacheService
- test_persistence_container_persistence.py
- ItemCatalogService
- test_websocket_handler_rate_limit.py
- asyncio
- test_command_factories.py
- AggressiveMobNPC
- Improve Layout Systematically
- Distill Skill
- MotdInterstitialScreen.tsx
- connectionStore.ts
- ClientLogger
- Mypy Remediation
- Claims by cluster
- P4 · Intent Sweep — FRD/SPEC Documents
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)
- exploration.sql
- npcs.sql
- required
- Technical Implementation
- Critical Issues
- Easy Coverage Wins - Quick Analysis
- Entries
- Unique Pylint Findings Analysis
- Migration Guide: From Default Logging to Enhanced Logging
- Execution Timeline
- ._is_valid_name_for_occupant
- analyze_idle_memory_samples.py
- main
- fix_markdown_code_block_style.py
- main
- SyntaxErrorFixer
- fixture
- lint_imports.py
- .create_drop_command
- catalogMetadata
- parse_shutdown_parameters
- .load
- _utc_now
- api/conftest.py
- fetch_container_items
- _weapon_from_prototype_registry
- ._is_uuid_string
- test_skill_service.py
- _occupation_slots_9
- required
- _personal_interest_4
- test_room_environment_parity.py
- Commands
- Dependency Upgrade
- required
- mapPageRenderer.tsx
- Amplify the Design
- Interaction Design
- Hardening Dimensions
- MythosMUD LLM Wiki (Obsidian)
- generate_room_id
- MapPerformanceMonitor
- PanelContextRuntime.tsx
- properties
- Lint Remediation
- mcp.json
- TRACK C · The interactive review — 8 decisions
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)
- bonus_tags
- ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List
- Complexity Checking Alignment: Ruff C901 vs Pylint
- What They Measure
- PERSISTENCE_REFACTORING_COMPLETE.md
- Migration Roadmap
- Critical Insights
- Multi-Character Support System
- enum
- grype.py
- main
- main
- PlayerRespawnWrapper
- mythos_e2e.rooms
- SkillUseLog
- fixture
- subzone_with_override
- test_monitoring_init.py
- mythos_unit.rooms
- field_validator
- skill
- load_motd
- main
- Codacy Rules
- Quieter Skill
- Typeset Skill
- PlayerServiceHealPort
- vite.userConfig.ts
- Client Test Remediation
- main
- Arkham City (MOTD Zone)
- Claims by cluster
- P3 · container-di + client + domain
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)
- AnyIO Code Review - Anti-Patterns and Issues
- ✅ Best Practices Compliance
- 🔍 Specific File Reviews
- CircuitBreaker Implementation Planning Document
- Ruff to Pylint Rule Mapping
- Test Timing Analysis - Optimization Targets
- App Package Design
- Auth Package Design
- Middleware Package Design
- apply_stat_modifications
- Schemas Package Design
- Services Package Design
- Movement Subsystem Design
- analyze_file
- main
- main
- main
- damage_expr_to_min_max
- Cult Chat Seam Design
- test_lucidity_round_trip.py
- test_spell_effects_support.py
- lock_state
- environment
- npc_base_stats.schema.json
- required
- environment
- fixture
- test_async_persistence_room_cache.py
- asyncio
- ._attack_target_impl
- Teach Impeccable Skill
- ADR-019: Player Effects System
- _ScalarResult
- Responsive Design
- ._get_npc_display_name
- Cursor Subagents Overview
- REQUIRED TOOL USAGE PATTERN
- FAILURE PATTERN RECOGNITION
- P3 · realtime-connection + events-nats
- P4 · Intent Sweep — Plan Documents
- P7 · Rulings — complete
- P8 · Applied
- Design ↔ Implementation Drift Audit — Final Summary
- Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)
- Lucidity.md
- enum
- Chat Panel Separation Specification
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
- Conclusion
- MythosMUD Testing Strategy (Greenfield Suite)
- Dialogue Content Tools (Content Creators)
- load_test_10_players.spec.ts
- emote_schema.json
- bench_cache_npc.py
- bench_cache_professions.py
- check_file
- populate_test_npc_databases.py
- .__init__
- properties
- Any
- lucidity_migration.py
- ensure_directory_exists
- test_calendar_procedures.py
- emote_row
- zone_and_subzone
- test_async_persistence_room_loading.py
- TestMinimapExplorationInvestigationDoc
- test_skill_use_log_repository.py
- local-channel-isolation.spec.ts
- test_combat_validator.py
- optimized_validate_action_content
- optimized_validate_alias_name
- optimized_sanitize_unicode_input
- optimized_validate_security_comprehensive
- gh-stack (MythosMUD)
- Workflows
- test_db_connectivity_create_and_read_user
- run_quality_fragmentation_guard.py
- Frontend Aesthetics Guidelines
- run-playwright-tests.js
- mythos_e2e Database
- holidays.schema.json
- 🟡 HIGH PRIORITY ISSUES
- 🟢 MEDIUM PRIORITY IMPROVEMENTS
- Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE
- async_persistence_room_loader.py
- Coverage Improvement Summary - Plan 2 Execution
- Implementation Notes
- Ruff C901 McCabe Complexity
- Positive Findings ✅
- Detailed Implementation
- Specific File Reviews
- Python Code Coverage Status
- Server & Client Package Documentation Coverage
- monitoring_service
- enum
- applies_to
- validate_shutdown_admin_permission
- bench_cache.py
- HealthErrorResponse
- _filter_lines
- fix_markdown_file
- fix_room_references
- run_bug_prevention_tests.ps1
- run_make_stages.py
- load_zone_configurations
- required
- connection_state_machine.py
- logger.test.ts
- verify_npc_occupants.py
- NPC catalog pipeline (private `data/` submodule)
- player_inventory_migration.py
- strict_mocker
- fixture
- test_utility_commands_whoami.py
- get_config
- test_spell_effects_internal.py
- room_validator/schemas/unified_room_schema.json
- test_room_subscription_manager_drops.py
- test_websocket_handler_disconnect.py
- properties
- _RealtimeConnectionManager
- optimized_validate_target_player
- Room Pathing Validator Implementation Spec
- validator.py CLI
- gh-stack
- items
- Motion Design
- MythosMUD Commit Messages
- worktree-plan-template.md
- Step 2: Ask UX-Focused Questions
- run-vitest.js
- usePerformanceMonitor.ts
- mock_persistence
- cli.sh
- Earth Plane
- C2 · REVISED — procedures-only is binding
- P3 · config-api
- P3 · persistence-db
- P5 · Adversarial Refutation
- Paris (Reign of Terror).md
- Authoritative Environment DML
- mythos_dev.item_instances
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
- Common Mistakes and How to Fix Them
- validate.mjs
- calculate_notification_times
- Log Levels and Usage
- AuthRateLimitMiddleware
- UnknownChannelStrategy
- mock_zone_config
- CorruptionTier
- test_websocket_handler_json_error.py
- test_run_make_stages.py
- Common Patterns
- optimized_validate_command_content
- optimized_validate_reason_content
- optimized_validate_pose_content
- optimized_validate_filter_name
- optimized_validate_help_topic
- optimized_comprehensive_sanitize_input
- ADR-001: Layered Architecture with Event-Driven Components
- container
- Server Management
- Test Coverage
- Skill
- Skill
- Skill
- Skill
- Skill
- Skill
- Readme
- useGridLayout.ts
- CatalogPage.tsx
- Wireframe
- Corrections Corpus Gap
- Critical Websocket Auth
- Index
- P0 Known Deviations
- holidays
- schedules
- Chat Panel Separation Documentation
- Aggro Threat Implementation Plan
- Async Audit 2025 12 03
- Async Audit 2025 12 03
- Python Coverage Status
- Linting Pylint Unique Findings
- Nats Anti Patterns Review 2026
- Persistence Async Migration Plan
- Persistence Extraction Complete
- Planning Users Db
- Test Suite Quality Audit Report
- Attack Command Not Starting Combat
- Second NPC Combat And Linkdead Findings
- Multi-Word Spell Name Parsing Failure
- main
- intersection_schema.json
- Server Realtime Module
- room_schema.json
- 🔍 Anti-Pattern Check
- Models Package Design
- _ensure_connection_manager
- .create_supervised_task
- _AsyncPersistenceRoomFacadeBase
- broadcast_shutdown_notification
- Thinking about stack structure
- .claude/CLAUDE.md
- Extract Skill
- MythosMUD Server Test Suite
- Common Test Failure Categories
- P3 · Findings Verified Directly
- P8 · Action plan
- ._compute_player_context
- 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage
- 📚 Documentation Created
- Implementation Details
- Core Logging Principles
- Performance Logging
- Enhanced Logging Features
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
- Whisper Channel System
- NPC Occupants Verification Summary
- Combat Client Crash
- Respawn Death Screen Loop Limbo ID Mismatch
- NPC Combat Start Race Condition
- mark_player_seen_impl
- Round-Based Combat
- WebSocket-Only Migration
- .on_enter_state
- _get_enum_value
- _run_dialogue_ddl
- check_file_for_logging_issues
- e2e_reset_players.py
- add_suppression_to_file
- test_initiate_shutdown_countdown_success
- 3. Anti-patterns and Semantic Problems
- create_error_context
- auth_rate_limit.py
- User
- damage_expr
- name
- player_repository
- _PlayerLookupPersistence
- _SessionCM
- rate_limiter
- wearable_service
- Database
- Skill
- Mythosloginform
- Global Teardown
- Review
- Server Test Remediation
- DML Migrations
- S. Petersen's Field Guide to Lovecraftian Horrors (source summary)
- mythos_dev.npc_definitions
- websocket_handler_connection.py
- items.sql
- month
- Advanced Chat Channels Specification
- UI/UX Considerations
- 3. Simplified CommandPanel
- Implementation Phases
- Magic and Spellcasting System
- Implementation Plan
- Specific Actionable Recommendations
- Lucidity Tiers
- Code Quality Improvements
- Common Conversion Patterns
- Gotchas & Solutions
- Four-Level Room Hierarchy
- Phase 1: Quantitative Analysis Results
- attacks
- Summary: Test Quality Metrics
- Modular E2E Test Suite
- Playwright MCP Scenarios
- Local Channel System
- Container Contents Synchronization Bug
- F-String Logging Violations
- Quest System Gap
- items
- determination_points
- fix_file
- check_codacy_yaml
- HADS tooling (MythosMUD)
- max_dp
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
- xp_value
- .generate_fake_npc_tell
- EventHandler
- enabled
- ._load_player_mutes_from_data
- plane
- .flee
- ._handle_patrol_territory
- .__init__
- charisma
- dexterity
- Test Grype
- messaging_integration
- user_manager
- intelligence
- AGENTS.md
- CONTRIBUTING.md
- Tiered Test Coverage Strategy
- message-match.test.ts
- multiplayer-browser-helpers.d.ts
- 9. Test Maintenance Best Practices
- DML Migrations Apply Paths
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
- Doors to Darkness (source summary)
- Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)
- The Grand Grimoire of Cthulhu Mythos Magic (source summary)
- duration_hours
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
- magic_points
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
- power
- MythosMUD Product Requirements
- Test Execution
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
- .on_connection_failed
- test_room_write_request_schemas_reject_unknown_field
- factory
- quality_fragmentation_graph.py
- Shared JSON schemas
- apply_migration
- main
- _resolved_npm
- start_server.ps1
- verify_schema_match.sh script
- verify_tutorial_migrations.ps1
- esbuild
- enum
- description
- name
- item_prototype.schema.json
- test_auth_utils.py
- description
- eslint.config.js
- Client Security and Privacy Policies
- MythosMUD UI Component Library
- mythosTheme.ts
- Step-by-Step Remediation Process
- 8. Error Handling and Debugging
- mythos_dev.dialogue_definitions
- mythos_e2e.dialogue_definitions
- mythos_unit.dialogue_definitions
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
- description
- report_any_baseline.py
- server/game/npcs/__init__.py
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
- CodeQL Configuration
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
- test_get_adjacent_rooms_null_exit
- check_postgresql.sh
- remove_dir
- load_seed_data
- safe_print
- parse_lint_findings
- setup_postgresql_test_db.sh
- verify_e2e_users_seeded.py
- test_build_room_objects_success
- test_enrich_behavior_context_handles_no_current_room
- test_get_attack_damage_from_behavior_config
- test_enrich_behavior_context_sets_player_in_range_when_players_in_room
- test_enrich_behavior_context_sets_false_when_no_players_in_room
- test_validate_player_in_room_cache_not_found
- test_save_player_with_bool_is_admin
- mythos_e2e.item_instances
- test_list_players_empty
- mythos_unit.item_instances
- normalize_path_from_url_or_path
- test_save_players_success
- description
- name
- weather_patterns
- 7. Common Test Failure Solutions
- 10. Grace Period Persistence
- 1. Disconnect Grace Period Duration
- 2. Auto-Attack During Grace Period
- Vite Logo SVG
- Critical State Handoffs
- ApplicationContainer
- playwright.runtime.config.ts
- deps/package.json
- wsl-bashrc-codacy.sh
- Mypy Remediation Skill
- MythosMUD Worldbuilding Foundation (Raw)
- LLM Wiki Pattern.md
- db/migrations/README.md
- mythos_dev.emote_aliases
- mythos_dev.get_user_id_by_username_ci
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
- MythosMUD Development Environment Setup
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
- One Server Only
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
- 3. Grace Period Visibility & Messaging
- 4. Rest/Quit Command During Combat
- 5. Rest Command Countdown Duration
- constants/__init__.py
- server/game/magic/__init__.py
- 6. Rest Location (Inn/Hotel) Behavior
- 7. Reconnection During Grace Period
- 8. Grace Period After Intentional Disconnect
- persistence/utils/__init__.py
- create_professions_table.sql
- server/structured_logging/__init__.py
- server/tests/__init__.py
- command_handler_unified/__init__.py
- unit/game/magic/__init__.py
- 9. Command Blocking During Grace Period
- test_get_room_persistence_returns_dict
- test_get_adjacent_rooms_success
- test_get_adjacent_rooms_source_not_found
- Recommendations Summary
- Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)
- Call of Cthulhu Investigator Handbook 7th Edition (source summary)
- test_validate_room_exists_with_cache
- test_validate_room_exists_cache_not_found
- test_validate_room_exists_without_cache
- test_validate_exit_exists_success
- test_validate_exit_exists_invalid
- test_validate_exit_exists_from_room_not_found
- test_validate_exit_exists_no_exits
- test_get_room_occupants_with_cache_room_object
- Dead Light and Other Dark Turns (source summary)
- test_validate_player_in_room_with_cache_true
- Down Darker Trails (source summary)
- test_get_room_exits_room_not_found
- test_get_room_exits_no_exits
- test_list_rooms_exclude_exits
- test_get_room_info_not_found
- test_room_service_init
- Gateways to Terror (source summary)
- test_get_room_without_cache
- infrastructure/__init__.py
- test_delete_player_success
- test_update_player_last_active_success
- test_disconnect_from_connected
- Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)
- test_disconnect_from_degraded
- Nameless Horrors - 2nd Edition (source summary)
- test_degrade
- test_recover
- The Malleus Monstrorum Keeper Deck (source summary)
- corruption_adjustment_log.sql
- test_close_circuit
- day
- test_can_attempt_connection_connected
- test_can_attempt_connection_circuit_open
- test_can_attempt_connection_reconnecting
- days
- effects
- test_process_exit_rows_with_partial_room_ids
- test_process_exit_rows_debug_logging
- _ExecuteResult
- test_process_room_rows_with_full_room_id
- test_build_room_objects_with_non_dict_attributes
- test_load_room_cache_with_rooms_logs_sample_ids
- test_process_room_rows_empty_list
- test_process_exit_rows_empty_list
- test_process_exit_rows_multiple_exits_same_room
- test_process_exit_rows_zone_single_part
- test_build_room_objects_with_exits
- test_process_room_rows_with_partial_room_id
- test_build_room_objects_with_dict_attributes
- test_build_room_objects_without_environment_in_attributes
- test_process_room_rows_with_none_attributes
- test_process_room_rows_zone_without_slash
- unit/middleware/__init__.py
- end_hour
- start_hour
- exits
- test_should_open_circuit_at_threshold
- Migration Considerations
- test_should_open_circuit_over_threshold
- day
- holiday
- month
- test_get_stats
- id
- plane
- sub_zone
- zone
- id
- plane
- rest_location
- sub_zone
- zone
- test_run_quality_fragmentation_guard.py
- Item catalog pipeline (private `data/` submodule)
- sub_zone
- zone
- _extract_bearer_token
- unit/monitoring/__init__.py
- test_get_stats_with_error
- test_get_stats_no_error
- test_reconnect_attempts_increment
- test_nats_connection_state_machine_init
- test_total_disconnections_increment
- test_validate_secure_path_path_traversal_commonpath
- items
- test_asyncio_run_guardrails.py
- description
- name
- plane
- sub_zone
- zone
- exits
- plane
- sub_zone
- zone
- description
- test_last_connected_time_set
- npc_spawn_modifier
- special_rules
- test_on_enter_state_logs
- plane
- test_invalid_transition_raises_error
- test_connect_transition
- properties
- test_connected_successfully_from_connecting
- test_connection_failed_from_connecting
- test_occupant_formatter_process_player_name_for_update_valid
- test_occupant_formatter_init
- test_occupant_formatter_process_dict_occupant_for_update_fallback_name
- test_occupant_formatter_process_string_occupant_for_update_uuid
- unit/persistence/__init__.py
- eslint
- @eslint/js
- globals
- happy-dom
- jsdom
- @playwright/test
- postcss
- @testing-library/dom
- unit/realtime/integration/__init__.py
- unit/realtime/maintenance/__init__.py
- unit/realtime/messaging/__init__.py
- unit/realtime/monitoring/__init__.py
- @testing-library/jest-dom
- @testing-library/react
- test_occupant_formatter_separate_occupants_by_type_dict_npcs
- test_occupant_formatter_separate_occupants_by_type_none
- @types/jsdom
- test_occupant_formatter_is_valid_name_for_occupant_uuid
- @types/react
- test_occupant_formatter_is_valid_name_for_occupant_none
- vite
- test_occupant_formatter_is_valid_name_for_occupant_non_string
- test_get_mortally_wounded_players_handles_error
- test_ensure_player_posture_lying_already_lying
- mythos_e2e.npc_definitions
- @vitejs/plugin-react
- @vitest/coverage-v8
- mythos_unit.npc_definitions
- get_alerts
- test_clear_player_combat_state_success
- snapshot_source_pack_graphify.ps1
- 2026_09_11_add_account_sanctions_table.py
- test_handle_player_death_with_killer_info
- _RoomPersistence
- test_check_rate_limit_disabled
- test_record_message_cleanup_old
- add_used_by_user_id_column.py
- test_record_message_error_handling
- test_get_player_stats
- quest_seed_data
- test_get_player_stats_empty
- test_reset_player_limits_specific_channel
- health_service
- _RaisesOnBool
- Context Management
- start_hour
- test_reset_player_limits_all_channels
- test_get_system_stats
- test_is_player_rate_limited_true
- test_get_remaining_messages_zero
- test_get_remaining_messages_error_handling
- resolve_connection_manager
- test_set_limit
- test_get_limit_existing
- test_get_limit_default
- test_cleanup_old_entries
- test_handle_unequip_wearable_container_preserves
- test_get_wearable_containers_for_player
- mythos_dev.quest_definitions
- mythos_e2e.quest_definitions
- mythos_unit.quest_definitions
- test_update_wearable_container_items
- test_handle_container_overflow
- id
- Security Considerations
- apply_account_sanctions_migration.py
- websocket_player_id_fallback_allowed
- test_handle_equip_wearable_container_creation_error
- test_handle_unequip_wearable_container_with_allowed_roles
- test_update_wearable_container_items_not_found
- test_update_wearable_container_items_capacity_exceeded
- test_filter_container_data
- test_handle_unequip_wearable_container_no_allowed_roles
- test_handle_container_overflow_partial_spill
- test_handle_container_overflow_no_spilled_items
- test_handle_container_overflow_room_id_empty_string
- generated/README.md
- rename_maps/README.md
- mythos_e2e.emote_aliases
- mythos_e2e.get_user_id_by_username_ci
- mythos_unit.emote_aliases
- mythos_unit.get_user_id_by_username_ci
- test_update_wearable_container_items_wrong_source_type
- test_get_local_chat_scope
- test_get_room_occupants_cache_not_found
- test_get_room_exits_success
- test_list_rooms_with_plane_zone
- unit/services/nats_subject_manager/__init__.py
- test_broadcast_player_mortally_wounded
- test_list_rooms_with_sub_zone
- test_connection_manager_lazy_load_called
- test_create_reply_command
- test_room_service_init_with_cache
- test_broadcast_player_death_personal_message_error
- test_send_dp_decay_message
- test_create_channel_command
- test_create_go_command
- test_messaging_integration_init_no_connection_manager
- test_create_sit_command
- test_create_stand_command
- test_create_lie_command
- test_create_ground_command
- test_create_drop_command
- test_create_put_command
- test_create_get_command
- test_create_equip_command
- test_create_unequip_command
- test_create_mute_command
- test_create_mute_global_command
- test_create_unmute_global_command
- test_create_add_admin_command
- test_create_admin_command
- test_create_mutes_command
- OccupantFormatter
- test_create_status_command
- test_broadcast_player_mortally_wounded_with_attacker
- unit/structured_logging/__init__.py
- test_broadcast_player_mortally_wounded_no_attacker
- test_broadcast_player_mortally_wounded_personal_message_error
- test_broadcast_combat_target_switch
- test_resolve_connection_manager_from_container
- test_resolve_connection_manager_from_container_error
- players
- test_create_time_command
- test_create_quit_command
- test_create_logout_command
- test_create_rest_command
- test_command_factory_init
- test_create_cleanse_command
- test_create_punch_command
- test_create_strike_command
- test_create_alias_command
- test_create_aliases_command
- test_create_unalias_command
- test_create_help_command
- test_create_npc_command
- test_create_spawn_command
- test_create_summon_command
- test_create_teleport_command
- test_create_goto_command
- test_create_cast_command
- test_create_spell_command
- test_create_spells_command
- test_create_learn_command
- test_command_factory_has_create_methods
- test_command_factory_create_existing_command
- test_command_factory_create_nonexistent_command
- test_create_say_command
- test_create_system_command
- test_create_emote_command
- test_create_me_command
- test_create_pose_command
- test_create_whisper_command
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
- ADR-008: React 18+ with TypeScript for Client
- ADR-010: Quest Subsystem Architecture
- ADR-013: Pydantic BaseSettings for Configuration Management
- ADR-014: Circuit Breaker + Dead Letter Queue for NATS
- ADR-016: Aggro and Threat Management System
- ADR-017: AST-Based Console Pruning
- ADR-021: Character Display Name Validation
- ADR-022: ui-v2 Client Transition
- ADR-023: Package Ownership and Fan-Out
- gh-stack Skill
- Codebase Explorer Agent
- Performance Profiler Agent
- Agent Routing
- Security Auditor Agent
- PostgreSQL Safety Rules
- Worktree Task Plan Template
- Event Schema
- Vite HTML Entry
- Client Layer Layout
- Zustand Stores
- UI-v2 Components
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
- MythosMUD Obsidian README
- Wiki Page Template
- mythos_dev mythos_unit mythos_e2e Databases
- zones
- PostgreSQL Procedures and Functions README
- generate_schema_from_dev.ps1
- Named Schema Per Database
- make verify-schema
- Owner and App Roles Per Environment
- AI Development Workflow
- Aggro and Threat System Design
- ADR-009: Instanced Rooms
- 1. Overview
- 2. Context
- 3. Decision
- 4. Alternatives Considered
- 5. Consequences
- AI READING INSTRUCTION
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
- Migration 019 Testing Guide
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
- OpenSSF Scorecard Workflow
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
- Server Authority
- Persistence Repositories Overview
- GET /v1/monitoring/health
- Memory Leak Monitoring Endpoints
- PostgreSQL Player Persistence
- World Loading
- npc_definitions
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
1. `get_logger()` - 542 edges
2. `LoggedHTTPException` - 374 edges
3. `ValidationError` - 318 edges
4. `User` - 310 edges
5. `AliasStorage` - 271 edges
6. `DatabaseError` - 253 edges
7. `Player` - 240 edges
8. `EventBus` - 224 edges
9. `CombatParticipant` - 219 edges
10. `log_and_raise()` - 191 edges

## Surprising Connections (you probably didn't know these)
- `Arkham City Graph PNG` --semantically_similar_to--> `Simple Room Graph - Arkham City`  [INFERRED] [semantically similar]
  data/local/arkham_city_graph.png → data/local/simple_room_visualization.html
- `MythosMUD Code Quality AI Skill` --semantically_similar_to--> `Lizard Complexity Config`  [INFERRED] [semantically similar]
  .claude/skills/mythosmud-code-quality-ai/SKILL.md → .codacy/tools-configs/lizard.yaml
- `register_error_handlers()` --indirect_call--> `http_exception_handler()`  [INFERRED]
  server/middleware/error_handling_middleware.py → docs/examples/logging/fastapi_integration.py
- `websocket_endpoint()` --calls--> `bind_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py
- `websocket_endpoint()` --calls--> `clear_request_context()`  [INFERRED]
  docs/examples/logging/fastapi_integration.py → server/structured_logging/logging_context.py

## Import Cycles
- 2-file cycle: `client/src/components/map/useAsciiMap.ts -> client/src/components/map/useAsciiMapState.ts -> client/src/components/map/useAsciiMap.ts`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_combat_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/npc_combat_integration_service.py -> server/services/npc_combat_integration_validation_mixin.py -> server/services/combat_service.py`
- 3-file cycle: `server/services/combat_service.py -> server/services/combat_turn_processor.py -> server/services/combat_turn_participant_actions.py -> server/services/combat_service.py`
- 3-file cycle: `server/realtime/connection_cleanup_methods.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_cleanup_methods.py`
- 3-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 3-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 3-file cycle: `server/config/models/security_logging.py -> server/structured_logging/enhanced_logging_config.py -> server/structured_logging/logging_file_setup.py -> server/config/models/security_logging.py`
- 4-file cycle: `server/realtime/connection_establishment.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_establishment.py`
- 4-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 4-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`
- 5-file cycle: `server/realtime/connection_initialization.py -> server/realtime/integration/game_state_provider.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py -> server/realtime/connection_initialization.py`
- 5-file cycle: `server/realtime/connection_manager.py -> server/realtime/player_presence_tracker.py -> server/realtime/player_connection_setup.py -> server/realtime/disconnect_grace_period.py -> server/realtime/player_disconnect_handlers.py -> server/realtime/connection_manager.py`
- 5-file cycle: `client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts -> client/tests/e2e/runtime/fixtures/multiplayer-ready.ts -> client/tests/e2e/runtime/fixtures/multiplayer-contexts.ts -> client/tests/e2e/runtime/fixtures/player.ts -> client/tests/e2e/runtime/fixtures/multiplayer.ts -> client/tests/e2e/runtime/fixtures/multiplayer-colocated.ts`

## Hyperedges (group relationships)
- **Async Migration Strategy** — docs_archive_anyio_code_review, docs_archive_anyio_vs_asyncio_comparison, docs_archive_websocket_code_review [EXTRACTED 0.85]
- **Codacy Static Analysis Configuration** — codacy_cli_config, codacy_tools_configs_analysis_options, codacy_tools_configs_languages_config, github_instructions_codacy_instructions [EXTRACTED 0.90]
- **Connection Resilience & State Management** — docs_architecture_decisions_adr_012_python_statemachine_backend, docs_architecture_decisions_adr_018_new_game_session_replacement [EXTRACTED 0.90]
- **Express.js Security Audit Rules** — javascript_express_ssrf, javascript_express_xxe, javascript_express_object_deserialization, javascript_express_jwt_hardcoded_secret [EXTRACTED 0.90]
- **Java Security Audit Rules** — java_security_xpath_injection, java_security_unvalidated_redirect, java_security_weak_ssl, java_security_xss_response_writer, java_security_xxe_documentbuilderfactory, java_security_path_traversal, java_security_jms_deserialization, java_security_jackson_deserialization [EXTRACTED 0.90]
- **Persistence Layer Architecture** — docs_database_access_patterns, docs_persistence_repository_architecture, docs_postgresql_contributor_guide [EXTRACTED 0.90]
- **Real-Time Communication Flow** — adr_003, adr_004, adr_011, adr_012, adr_014, adr_020 [EXTRACTED 0.90]
- **Real-Time Messaging System** — docs_real_time_architecture, docs_connection_manager_architecture, docs_nats_subject_patterns, docs_event_ownership_matrix [EXTRACTED 0.95]
- **Lucidity hallucination effects group** — docs_archive_lucidity_system_lucidity_system, docs_archive_phantom_hostile_requirements_phantom_hostiles, docs_archive_reversed_compass_directions_requirements_reversed_compass [EXTRACTED 1.00]
- **December 2025 Async Remediation Document Set** — docs_archive_async_audit_executive_summary_async_audit_executive_summary, docs_archive_async_persistence_migration_tracker_async_persistence_migration_tracker, docs_archive_async_remediation_complete, docs_archive_async_remediation_final_report, docs_archive_async_remediation_summary_2025_12_03 [EXTRACTED 1.00]
- **2026-08 Design Audit & Verification** — docs_architecture_audit_coverage_boundary_2026_08, docs_architecture_frd_plan_verification_register_2026_08, docs_architecture_api_openapi_specification [EXTRACTED 1.00]
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
- **Game Subsystem Design Documents** — docs_subsystems_subsystem_admin_commands_design, docs_subsystems_subsystem_combat_design, docs_subsystems_subsystem_emote_pose_design, docs_subsystems_subsystem_follow_design, docs_subsystems_subsystem_lucidity_design, docs_subsystems_subsystem_magic_design, docs_subsystems_subsystem_movement_design, docs_subsystems_subsystem_npc_design, docs_subsystems_subsystem_party_design, docs_subsystems_subsystem_rescue_design, docs_subsystems_subsystem_respawn_design, docs_subsystems_subsystem_rest_design, docs_subsystems_subsystem_skills_level_design, docs_subsystems_subsystem_status_effects_design, docs_subsystems_subsystem_who_design [EXTRACTED 1.00]
- **Design skills requiring teach-impeccable** — skills_teach_impeccable, skills_onboard, skills_optimize, skills_overdrive, skills_polish, skills_quieter, skills_typeset, skills_design_context_persistence [EXTRACTED 1.00]
- **Earth-plane major geography locations** — data_mythosmud_obsidian_raw_sources_mythosmud_worldbuilding_earth_plane, data_mythosmud_obsidian_raw_sources_geography_major_locations_arkham_city, data_mythosmud_obsidian_raw_sources_geography_major_locations_innsmouth, data_mythosmud_obsidian_raw_sources_geography_major_locations_rlyeh [EXTRACTED 1.00]
- **Effects and grace period cluster** — plans_effects_system_adr_and_implementation, plans_effects_system_implementation, plans_disconnect_grace_period_and_rest, plans_effects_login_warded [EXTRACTED 1.00]
- **Event projection and room handoff authority path** — client_src_components_ui_v2_eventlog_handoffs_enter_room_rr [EXTRACTED 1.00]
- **Frontend-design reference docs** — skills_frontend_design_ref_color_and_contrast, skills_frontend_design_ref_interaction_design, skills_frontend_design_ref_motion_design, skills_frontend_design_ref_responsive_design, skills_frontend_design_ref_spatial_design, skills_frontend_design_ref_typography, skills_frontend_design_ref_ux_writing [EXTRACTED 1.00]
- **Memory leak metrics and remediation** — plans_memory_leak_metrics_collection, plans_memory_leak_remediation, plans_memory_closed_websockets_deque [EXTRACTED 1.00]
- **MOTD listed known zones** — data_local_motd_message_of_the_day, data_local_motd_arkham_city, data_local_motd_innsmouth, data_local_motd_katmandu [EXTRACTED 1.00]
- **Quest gap analysis to implementation** — plans_mud_subsystems_gap_analysis, plans_mud_quest_gap, plans_quest_subsystem_implementation, plans_quest_system [EXTRACTED 1.00]
- **Knowledge Management Flow** — mythosmud_llm_wiki, chaosium_ingest_pipeline [EXTRACTED 1.00]
- **Alert evaluation and routing pipeline** — monitoring_prometheus_yml_prometheus_config, monitoring_mythos_alerts_yml_alert_rules, monitoring_alertmanager_yml_alertmanager_config [EXTRACTED 1.00]
- **Core monitoring stack services** — monitoring_docker_compose_prometheus, monitoring_docker_compose_alertmanager, monitoring_docker_compose_grafana [EXTRACTED 1.00]
- **MythosMUD Memory System** — mythosmud_llm_wiki, chaosium_ingest_pipeline [EXTRACTED 1.00]
- **MythosMUD Obsidian Vault** — data_mythosmud_obsidian_readme, data_mythosmud_obsidian_log [EXTRACTED 1.00]
- **NATS 2026-01-13 Review and Remediation Cycle** — docs_archive_nats_anti_patterns_review_2026_01_13, docs_archive_nats_remediation_summary_2026_01_13_nats_anti_patterns_remediation_summary, docs_archive_nats_medium_priority_remediation_2026_01_13, docs_archive_nats_complete_remediation_summary_2026_01_13_nats_complete_remediation_summary [EXTRACTED 1.00]
- **Observability & Error Framework** — docs_enhanced_logging_guide, docs_error_handling_guide, docs_error_logging_implementation_guide, docs_memory_leak_metrics_usage_guide [EXTRACTED 1.00]
- **Persistence Async Repository Extraction** — docs_archive_persistence_extraction_complete_persistence_layer, docs_archive_persistence_refactoring_complete_seven_async_repositories, docs_archive_persistence_async_migration_plan_gradual_migration, docs_archive_persistence_extraction_complete_sync_to_async_delegation [EXTRACTED 1.00]
- **Persistence Three Access Paths** — docs_archive_asyncio_code_review_asyncpersistencelayer, docs_archive_asyncio_code_review_persistencelayer, docs_archive_facades_implementation_summary_playerrepository, docs_archive_facades_implementation_summary_complementary_facades [EXTRACTED 1.00]
- **Phase 2 Async Persistence Migration** — docs_archive_phase2_migration_complete, docs_archive_phase2_migration_status, docs_archive_phase2_migration_complete_asyncio_to_thread, docs_archive_asyncio_code_review_event_loop_blocking, docs_archive_phase2_migration_status_passive_lucidity_flux [EXTRACTED 1.00]
- **Migration 019 Schema and ORM Type Alignment** — docs_archive_postgresql_audit_report_2026_migration_019, docs_archive_postgresql_audit_report_2026_identity_ids, docs_archive_postgresql_audit_report_2026_varchar_vs_text, docs_archive_python_model_updates_required_integer_to_biginteger, docs_archive_python_model_updates_required_string_to_text [EXTRACTED 1.00]
- **Quality Enforcement Flow** — pre_commit_config_yaml, codacy_yml, github_workflows_ci_yml [EXTRACTED 1.00]
- **WebSocket message accept-validate-route-broadcast pipeline** — server_realtime_readme_websocket_api, server_realtime_readme_connection_manager, server_realtime_readme_message_validator, server_realtime_readme_nats_message_handler, server_realtime_readme_room_broadcasts [EXTRACTED 1.00]
- **Room validator core modules** — tools_room_toolkit_room_validator_readme_room_loader, tools_room_toolkit_room_validator_readme_schema_validator, tools_room_toolkit_room_validator_readme_path_validator, tools_room_toolkit_room_validator_readme_reporter, tools_room_toolkit_room_validator_readme_fixer [EXTRACTED 1.00]
- **Multi-character scenario group 27-30** — e2e_tests_scenarios_scenario_27_character_selection_character_selection, e2e_tests_scenarios_scenario_28_multi_character_creation_multi_character_creation, e2e_tests_scenarios_scenario_29_character_deletion_character_soft_deletion, e2e_tests_scenarios_scenario_30_character_name_uniqueness_case_insensitive_name_uniqueness [EXTRACTED 1.00]
- **Skills scenario group 39-41** — e2e_tests_scenarios_scenario_39_skills_new_tab_skills_new_tab, e2e_tests_scenarios_scenario_40_skills_command_skills_slash_command, e2e_tests_scenarios_scenario_41_skills_after_creation_skills_after_creation [EXTRACTED 1.00]
- **Visibility and combat scenarios 34-36** — e2e_tests_scenarios_scenario_34_two_players_same_room_same_room_visibility, e2e_tests_scenarios_scenario_35_player_combat_player_combat, e2e_tests_scenarios_scenario_36_movement_visibility_movement_visibility [EXTRACTED 1.00]
- **Security Rule Definitions** — codacy_tools_configs_semgrep [EXTRACTED 1.00]
- **JSON validate generate merge seed pipeline** — scripts_static_data_readme_generate_sql_mjs, scripts_static_data_readme_ajv_validation, scripts_static_data_readme_world_emotes_sql, scripts_static_data_readme_canonical_dml_merge, scripts_static_data_readme_uuid_v5_namespace [EXTRACTED 1.00]
- **November 2025 Test Quality Audit Family** — docs_archive_test_audit_executive_summary, docs_archive_test_value_distribution, docs_archive_test_pruning_candidates, docs_archive_test_coverage_gaps, docs_archive_test_optimization_roadmap [EXTRACTED 1.00]
- **Chaosium Pack Synthesis** — data_mythosmud_obsidian_raw_chaosium_reign_of_terror_graph_report, data_mythosmud_obsidian_raw_chaosium_s_petersen_s_field_guide_to_lovecraftian_horrors_graph_report, data_mythosmud_obsidian_raw_chaosium_the_grand_grimoire_of_cthulhu_mythos_magic_graph_report, data_mythosmud_obsidian_raw_chaosium_the_malleus_monstrorum_keeper_deck_graph_report, wiki_concepts_graphify_code_graph [EXTRACTED]
- **Database Access Architecture** — db_procedures_readme, docs_database_access_patterns, data_mythosmud_obsidian_wiki_code_dml_migrations_apply_paths_dml_migrations_apply_paths [EXTRACTED]
- **Dependency Injection Governance** — docs_container_injection_audit, docs_database_access_patterns [EXTRACTED]
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

## Communities (2300 total, 534 thin omitted)

### Community 0 - "get_logger"
Cohesion: 0.01
Nodes (560): AliasRecord, PasswordHasher, create_validator(), Shared schema validator for room definition files. This module provides JSON…, Check if a room ID follows the unified naming schema. Args: room_id: Room ID to…, Create a schema validator with the specified schema. Args: schema_name: Name of…, Validates room definitions against JSON schema. This validator can be used by…, SchemaValidator (+552 more)

### Community 1 - "Invite"
Cohesion: 0.03
Nodes (107): get_current_verified_user(), get_optional_current_user(), Authentication dependencies for MythosMUD. This module provides dependency…, Get current verified user or raise 403., Validate invite code for registration., Get current user if authenticated, otherwise None., require_invite_code(), Authentication module for MythosMUD. This package contains all authentication-… (+99 more)

### Community 2 - "test_users.py"
Cohesion: 0.02
Nodes (114): AuthenticationBackend, get_auth_backend(), get_user_db(), get_user_manager(), get_username_auth_backend(), AsyncSession, Depends, get_async_session (+106 more)

### Community 3 - "LootAllRequest"
Cohesion: 0.05
Nodes (57): _audit_loot_all(), loot_all_items(), Any, APIRouter, Request, Register loot-all endpoint to the router., Loot all eligible items from a container., register_loot_endpoints() (+49 more)

### Community 4 - "Player"
Cohesion: 0.01
Nodes (285): Base, DeclarativeBase, Shared SQLAlchemy DeclarativeBase for all models. This module provides a single…, Shared declarative base for all MythosMUD models. All models (User, Player,…, HolidayModel, NPCScheduleModel, Base, SQLAlchemy models for calendar data (holidays and NPC schedules). (+277 more)

### Community 5 - "UtilityCommandFactory"
Cohesion: 0.03
Nodes (107): Unit tests for utility command factories. Tests the UtilityCommandFactory class…, Test create_summon_command() with quantity., Test create_summon_command() with target type., Test create_summon_command() with quantity and target type., Test create_summon_command() raises error with invalid quantity., Test create_summon_command() raises error with negative quantity., Test create_summon_command() raises error with invalid token., Test create_summon_command() raises error with extra args. (+99 more)

### Community 6 - "server/dependencies.py"
Cohesion: 0.01
Nodes (353): computed_field, LevelUpHook, get_async_persistence(), get_catatonia_registry(), get_chat_service(), get_combat_service(), get_connection_manager(), get_container() (+345 more)

### Community 7 - "test_npc_combat_integration_service.py"
Cohesion: 0.04
Nodes (75): integration_service(), asyncio, MonkeyPatch, Unit tests for NPC combat integration service. Tests the…, Test init sets NPC combat integration reference on shared PlayerCombatService., Test init creates CombatService when combat_service is None., Test integration service has combat service with config., Test auto_progression_enabled is set on combat service. (+67 more)

### Community 8 - "ChatService"
Cohesion: 0.02
Nodes (120): ChatService, _publish_room_chat(), ChatMessage, UUID, _rate_limit_result(), Chat service for handling real-time communication between players. This service…, Normalize player identifiers to string form., Send a say message to players in the same room. This method publishes the… (+112 more)

### Community 9 - "server/services/__init__.py"
Cohesion: 0.03
Nodes (108): AbstractContextManager, _clone_equipped(), _clone_inventory(), EquipmentCapacityError, EquipmentService, EquipmentServiceError, Any, Exception (+100 more)

### Community 10 - "Room"
Cohesion: 0.03
Nodes (78): Any, UUID, Add a player to the room without triggering an event. This method is used for…, Remove a player from the room without triggering an event. This method is used…, Remove a player from the room and trigger event. Args: player_id: The ID of the…, Add an object to the room and trigger event. Args: object_id: The ID of the…, Remove an object from the room and trigger event. Args: object_id: The ID of…, Add an NPC to the room and trigger event. Args: npc_id: The ID of the NPC… (+70 more)

### Community 11 - "NATSService"
Cohesion: 0.02
Nodes (183): NATSConfig, Any, BaseSettings, field_validator, NATS messaging configuration., Validate TLS file paths exist when TLS is enabled., Validate max payload is reasonable., Validate value is positive. (+175 more)

### Community 12 - "test_spell_effects.py"
Cohesion: 0.04
Nodes (69): Optional deps for SpellEffects beyond player_service., SpellEffectsDeps, mock_player_service(), mock_spell(), mock_target_match(), asyncio, fixture, Unit tests for spell effects. Tests the SpellEffects class. (+61 more)

### Community 13 - "NPCPopulationController"
Cohesion: 0.02
Nodes (114): Initialize the NPC lifecycle manager. Args: event_bus: Event bus for publishing…, Subscribe to relevant game events., NPCPopulationController, Initialize the NPC population controller. Args: event_bus: Event bus for…, Load zone and sub-zone configurations from PostgreSQL database., Subscribe to relevant game events., Handle player entering a room., Handle player leaving a room. (+106 more)

### Community 14 - "test_security_validator.py"
Cohesion: 0.01
Nodes (251): AliasCommand, AliasesCommand, field_validator, Alias command models for MythosMUD. This module provides command models for…, Command for creating or viewing command aliases., Validate alias name format using centralized validation., Validate command content for security using centralized validation., Command for listing all aliases. (+243 more)

### Community 15 - "Profession"
Cohesion: 0.06
Nodes (44): CharacterNameScreenProps, CreateCharacterPayload, MechanicalEffect, Profession, ProfessionCard(), ProfessionCardProps, StatRequirement, ProfessionSelectionContentProps (+36 more)

### Community 16 - "CombatTurnProcessor"
Cohesion: 0.03
Nodes (108): CombatAction, Represents a combat action., CombatTurnProcessor, Any, UUID, Resolve NPC participant UUID to string npc_id via combat integration service., Return True if npc_id_str is in the lifecycle manager's active_npcs., Load queued actions for the next round into combat.round_actions. Actions are… (+100 more)

### Community 17 - "SecureBaseModel"
Cohesion: 0.01
Nodes (303): ChatMessageHandler, ClientErrorReportMessageHandler, CommandMessageHandler, FollowResponseMessageHandler, MessageHandler, MessageHandlerFactory, PartyInviteResponseMessageHandler, PingMessageHandler (+295 more)

### Community 18 - "JsonMap"
Cohesion: 0.07
Nodes (17): Msg, _as_json_map(), _NatsListenerClient, NatsMessageCallback, _NatsSubscribeFn, _NatsSubscription, JsonMap, Protocol (+9 more)

### Community 19 - "LoggedHTTPException"
Cohesion: 0.02
Nodes (203): BaseUserManager, CharacterInfo, get_container, get_current_active_user, ID, IntegrityError, get_current_superuser(), Get current superuser or raise 403. (+195 more)

### Community 20 - "NPCDefinition"
Cohesion: 0.01
Nodes (233): _JSONDict, Base, _loads_json_dict(), NPCDefinition, NPCRelationship, NPCSpawnRule, DeclarativeBase, NPC database models for MythosMUD. This module defines the SQLAlchemy models… (+225 more)

### Community 21 - "ContainerTransferFromMixin"
Cohesion: 0.19
Nodes (14): ContainerTransferFromMixin, InventoryStack, Player, UUID, Persist container changes and log audit trail., Mutation-guarded body: remove stack, add to player, persist, audit., Transfer items from container to player inventory., Transfer each container stack until capacity error; returns updated state. (+6 more)

### Community 22 - "test_rescue_service.py"
Cohesion: 0.04
Nodes (75): AsyncSessionFactory, EventDispatcher, LucidityServiceFactory, _dispatch_rescue_events(), _ensure_uuid(), _load_rescue_participants(), _maybe_await(), Any (+67 more)

### Community 23 - "AliasStorage"
Cohesion: 0.02
Nodes (154): AliasPayload, AliasStorage, _as_alias_payload(), _empty_alias_payload(), Path, Manages player alias storage in JSON files. Each player's aliases are stored in…, Get the file path for a player's aliases. Human: reject path separators /…, Absolute str path for open(); re-checks containment at the open site. Human:… (+146 more)

### Community 24 - "ContainerComponent"
Cohesion: 0.03
Nodes (86): ContainerComponent, BaseModel, Check if container is locked or sealed., Check if container is unlocked., Check if container has available capacity., Check if container can hold this many items (e.g. when replacing contents)., Get number of used inventory slots., Get number of available inventory slots. (+78 more)

### Community 25 - "api/character_creation.py"
Cohesion: 0.01
Nodes (206): _apply_rate_limiting_for_stats_roll(), _apply_stat_modifiers(), _as_float(), _as_int(), _check_shutdown_status(), _convert_stat_summary_to_stat_summary_model(), create_character_with_stats(), _dispatch_roll_stats() (+198 more)

### Community 26 - "test_combat_event_publisher.py"
Cohesion: 0.02
Nodes (154): CombatEndedEvent, CombatStartedEvent, CombatTargetSwitchEvent, NPCAttackedEvent, NPCDiedEvent, NPCTookDamageEvent, PlayerAttackedEvent, Combat-specific events for the MUD. This module defines combat-related events… (+146 more)

### Community 27 - "HolidayService"
Cohesion: 0.02
Nodes (79): Construct holiday_service, schedule_service, and mythos_tick_scheduler.…, Initialize the Temporal context: holiday/schedule/tick-scheduler, then the…, MythosHourTickEvent, Event fired when the accelerated Mythos clock rolls over to a new hour., _ensure_utc(), _holiday_entry_from_row(), _HolidayLoadResult, HolidayService (+71 more)

### Community 28 - ".auto_progression_enabled"
Cohesion: 0.29
Nodes (5): setter, Return whether auto-progression is enabled., Enable or disable combat auto-progression., Return the turn interval in seconds., Set the turn interval in seconds.

### Community 29 - "MemoryMonitor"
Cohesion: 0.03
Nodes (89): Return the live singleton without constructing one., AllocSiteSample, _append_sample_jsonl(), _as_int(), collect_idle_memory_sample(), ConnectionStatsSnapshot, _container_instance(), _event_bus_queue_depth() (+81 more)

### Community 30 - "players.py"
Cohesion: 0.03
Nodes (161): create_player(), delete_character(), delete_player(), _disconnect_other_characters(), _end_combat_for_grace_period(), _force_disconnect_character(), get_available_classes(), get_class_description() (+153 more)

### Community 31 - "EventBus"
Cohesion: 0.01
Nodes (245): ModuleType, Distributed EventBus that uses NATS for cross-instance event distribution.…, EventBusMixinBase, Attribute stubs for EventBus mixins (mypy attr-defined). Mirrors…, Attrs/methods provided by EventBus when mixed in., Start the async consumer. Real impl is EventBusLifecycleMixin., Drain the event queue. Real impl is EventBusProcessingMixin., Drop tracked service handlers. Real impl is EventBus. (+237 more)

### Community 32 - "get_npc_instance_service"
Cohesion: 0.02
Nodes (173): Get NPC instance from the spawning service. Public API., Get NPC instance from the spawning service., handle_npc_behavior_command(), handle_npc_react_command(), handle_npc_stop_command(), Any, NPC behavior control commands (behavior, react, stop)., Handle NPC behavior control command. (+165 more)

### Community 33 - "test_zone_config_loader.py"
Cohesion: 0.12
Nodes (35): async_load_zone_configurations(), process_subzone_rows(), process_zone_rows(), Connection, Process subzone rows from database and populate subzone configurations. Args:…, Async helper to load zone configurations from PostgreSQL database., Result of loading zone and sub-zone configs from PostgreSQL., Process zone rows from database and populate zone configurations. Args: conn:… (+27 more)

### Community 34 - "InventoryMutationGuard"
Cohesion: 0.03
Nodes (64): _AsyncPlayerGuardState, InventoryMutationGuard, _PlayerGuardState, Acquire sync mutation guard., Acquire async mutation guard., Get or create per-player guard state for sync contexts. Uses thread-safe…, Get or create per-player guard state for async contexts. Uses async lock to…, Clean up per-player guard state when no longer needed (sync context). Removes… (+56 more)

### Community 35 - "InventoryCommandFactory"
Cohesion: 0.10
Nodes (27): Test create_pickup_command() with numeric index., Test create_pickup_command() with quantity., test_create_pickup_command_with_index(), test_create_pickup_command_with_quantity(), Test create_pickup_command() creates PickupCommand., Test create_pickup_command() raises error with no args., Test create_pickup_command() raises error when quantity is zero., Test create_pickup_command() raises error when quantity is negative. (+19 more)

### Community 36 - "test_combat_monitoring_service.py"
Cohesion: 0.03
Nodes (91): AlertSeverity, AlertType, CombatMetrics, end_combat_monitoring(), get_combat_metrics(), get_combat_monitoring(), Enum, Combat monitoring and alerting service for MythosMUD. This service provides… (+83 more)

### Community 37 - "DatabaseManager"
Cohesion: 0.01
Nodes (338): add_flavor_text_column(), Add flavor_text column if missing., load_seed_data(), Load all seed data files., main(), Load seed data and verify., Initialize core services. No dependencies., close_db() (+330 more)

### Community 38 - "ConnectionManager"
Cohesion: 0.01
Nodes (125): detect_and_handle_error_state_impl(), handle_authentication_error_impl(), handle_security_violation_impl(), handle_websocket_error_impl(), Any, UUID, Error-handling method implementations for ConnectionManager. Thin wrappers that…, Detect when a client is in an error state and handle it appropriately. (+117 more)

### Community 39 - "PlayerNameExtractor"
Cohesion: 0.02
Nodes (85): PlayerNameExtractor, Any, UUID, Player name extraction and validation utilities. This module provides utilities…, Get name from user object (username or display_name). Args: user: The user…, Try to get name from related User object. Args: player: The player object…, Try to get player name from fallback sources (username, user object). Args:…, Perform basic validation on player name (not None, is string, not empty). Args:… (+77 more)

### Community 40 - "test_quest_instance_repository.py"
Cohesion: 0.03
Nodes (99): Base, QuestDefinition, QuestOffer, Quest subsystem models: quest_definitions, quest_instances, quest_offers. Maps…, Quest template: id (PK), definition JSONB, timestamps., Junction: links a quest to an NPC or room that offers it., Any, QuestDefinitionRepository (+91 more)

### Community 41 - "test_communication_commands_flows.py"
Cohesion: 0.03
Nodes (138): _chat_send_with_room_bundle(), _deliver_reply_to_last_whisper(), _deliver_whisper_message(), flow_global_command(), flow_local_command(), flow_reply_command(), flow_say_command(), flow_system_command() (+130 more)

### Community 42 - "connection_manager_methods.py"
Cohesion: 0.01
Nodes (223): delegate_game_state_provider(), Generic delegate for game state provider methods. Args: game_state_provider:…, broadcast_global_event_impl(), broadcast_global_impl(), broadcast_room_event_impl(), broadcast_to_room_impl(), canonical_room_id_public_impl(), check_all_connections_health_impl() (+215 more)

### Community 43 - "AsyncPersistenceLayer"
Cohesion: 0.02
Nodes (135): AsyncPersistenceLayer, datetime, Player, Profession, Room, Unpack, UUID, Set the instance manager for instanced room lookup (instance-first). (+127 more)

### Community 44 - "PlayerService"
Cohesion: 0.02
Nodes (120): _initialize_magic_service(), initialize_magic_services(), _initialize_mp_regeneration_service(), _initialize_spell_effects(), _initialize_spell_learning_service(), _initialize_spell_registry(), _initialize_spell_repositories(), _initialize_spell_targeting_service() (+112 more)

### Community 45 - "useRespawnHandlers.ts"
Cohesion: 0.05
Nodes (66): handleCombatDeath(), handleCombatEnded(), handleCombatStarted(), handleCombatTargetSwitch(), handleNpcAttacked(), handleNpcDied(), handlePlayerAttacked(), appendDaypartChange() (+58 more)

### Community 46 - "test_lifespan_startup.py"
Cohesion: 0.06
Nodes (62): _get_item_prototype_count(), _get_item_prototype_entries(), initialize_container_and_legacy_services(), initialize_mythos_time_consumer(), _log_npc_startup_errors(), Initialize container and set up container reference on app.state. Services are…, Initialize Mythos time event consumer. DEPRECATED: This function is no longer…, Log any errors from NPC startup spawning results. (+54 more)

### Community 47 - "test_target_resolution_service.py"
Cohesion: 0.03
Nodes (79): BaseModel, Target metadata schema for MythosMUD. This module defines Pydantic models for…, Metadata about a target in target resolution. This model represents additional…, TargetMetadata, Test TargetMatch can be instantiated., test_target_match(), mock_persistence(), mock_player_service() (+71 more)

### Community 48 - "ui-v2/types.ts"
Cohesion: 0.04
Nodes (94): IncapacitatedBanner, eventHandlers, processGameEvent(), hoisted, EventHandler, EventHandlerContext, GameEvent, GameStateUpdates (+86 more)

### Community 49 - "test_corpse_lifecycle_service.py"
Cohesion: 0.03
Nodes (91): CorpseNotFoundError, CorpseServiceError, Base exception for corpse service operations., Raised when a corpse container is not found., corpse_service(), mock_persistence(), asyncio, fixture (+83 more)

### Community 50 - "test_container_bundles.py"
Cohesion: 0.03
Nodes (118): ChatBundle, Chat bundle: chat service. Depends on Core (config, persistence), Game…, CombatBundle, Combat bundle: player combat, death, respawn, combat service, catatonia,…, Raise if prerequisites for NATS combat are missing., Start NATS message handler if available. Logs and swallows errors., Handle case when NATS is not connected. Raises in prod, sets combat_service to…, Initialize NATS-dependent combat service and start NATS message handler. (+110 more)

### Community 51 - "Communities (355 total, 223 thin omitted)"
Cohesion: 0.02
Nodes (133): Communities (355 total, 223 thin omitted), Community 0 - "Nyarlathotep Avatars", Community 100 - "Call Daoloth / Daoloth", Community 101 - "Call Nyogtha / Clutch of Nyogtha", Community 102 - "Call Saaitii / Saaitii", Community 103 - "Call Zu-Che-Quon / Enchant Bells of Horror", Community 104 - "Cast Out Shan / Shaggai", Community 105 - "Casting the Runes / Elder Sign" (+125 more)

### Community 52 - "test_magic_commands.py"
Cohesion: 0.03
Nodes (115): handle_cast_command(), handle_learn_command(), handle_spell_command(), handle_spells_command(), handle_stop_command(), MagicCommandHandler, Any, Exception (+107 more)

### Community 53 - "test_command_parser.py"
Cohesion: 0.02
Nodes (141): Smoke test for command parser., Test basic command parsing., Test command parsing with arguments., Test command parsing with pipes., test_parse_command_basic(), test_parse_command_with_args(), test_parse_command_with_pipes(), command_parser() (+133 more)

### Community 54 - "HolidayCollection"
Cohesion: 0.03
Nodes (82): _check_holiday_coverage(), _get_calendar_paths(), _load_and_validate_holidays(), load_document_ids(), main(), parse_args(), _print_errors(), _print_success_message() (+74 more)

### Community 55 - "BaseCommand"
Cohesion: 0.01
Nodes (355): GotoCommand, NPCCommand, field_validator, Admin command models for MythosMUD. This module provides command models for…, Command for shutting down the server (admin only). Args can be: - Empty:…, Command for NPC administrative utilities with subcommands., Administrative command for summoning prototypes into the current room., Validate prototype ID format. Args: value: The prototype ID to validate… (+347 more)

### Community 56 - "ChatHistoryPanel.tsx"
Cohesion: 0.03
Nodes (83): EldritchEffectsDemo(), EldritchEffectsDemoProps, mockAlert, ALWAYS_ACTIVE_EFFECTS, effectClass(), EffectOption, ELDRITCH_EFFECT_OPTIONS, hasEffect() (+75 more)

### Community 57 - "test_admin_auth_service.py"
Cohesion: 0.02
Nodes (201): create_npc_definition(), delete_npc_definition(), get_npc_definition(), get_npc_definitions(), AsyncSession, delete, get, post (+193 more)

### Community 58 - "test_look_container.py"
Cohesion: 0.02
Nodes (219): _as_map(), _as_map_list(), _as_uuid(), _container_name(), ContainerLookArgs, _ContainerPersistence, _extract_container_metadata(), _fetch_container() (+211 more)

### Community 59 - "test_command_inventory.py"
Cohesion: 0.02
Nodes (134): DropCommand, EquipCommand, GetCommand, InventoryCommand, PickupCommand, PutCommand, field_validator, model_validator (+126 more)

### Community 60 - "NPCCombatIntegration"
Cohesion: 0.04
Nodes (84): NPCCombatIntegration, Publish NPC attack event to event bus., Integrates NPCs with the existing combat and game mechanics systems. Extends…, Handle NPC death and related effects. Args: npc_id: ID of the dead NPC room_id:…, Get NPC stats or use defaults., integration(), asyncio, fixture (+76 more)

### Community 61 - "test_nats_message_handler.py"
Cohesion: 0.02
Nodes (128): asyncio, Unit tests for NATS message handler. Tests the NATSMessageHandler class…, Test _subscribe_to_chat_subjects() raises error when subject manager not…, Test _subscribe_to_standardized_chat_subjects() successfully subscribes., Test _subscribe_to_standardized_chat_subjects() continues on partial failure., Test _subscribe_to_subject() successfully subscribes., Test _subscribe_to_subject() raises error on failure., Test _unsubscribe_from_subject() successfully unsubscribes. (+120 more)

### Community 62 - "CommandValidator"
Cohesion: 0.05
Nodes (52): Test CommandValidator.validate_command_content returns True for valid command., Test CommandValidator.validate_command_content detects null bytes., Test CommandValidator.validate_command_content detects dangerous patterns., Test CommandValidator.validate_command_content detects excessive length., Test CommandValidator.validate_command_content detects non-printable characters., Test CommandValidator.validate_command_content allows newline, tab, and space., Test CommandValidator.validate_expanded_command returns True for valid expanded…, Test CommandValidator.validate_expanded_command inherits content validation. (+44 more)

### Community 63 - "MythosTickScheduler"
Cohesion: 0.04
Nodes (59): mock_chronicle(), mock_event_bus(), mock_task_registry(), asyncio, fixture, Unit tests for MythosTickScheduler., scheduler(), test_emit_pending_ticks_initializes_last_hour() (+51 more)

### Community 64 - "inventory_equip_command.py"
Cohesion: 0.02
Nodes (154): _equip_stack_from_inventory_index(), _find_equipped_by_item_id(), find_equipped_item_after_equip(), handle_wearable_container_on_equip(), handle_wearable_container_on_unequip(), normalize_equipped_items(), normalize_inventory_slots(), InventoryStack (+146 more)

### Community 65 - "SpellEffectType"
Cohesion: 0.03
Nodes (140): List all spells, optionally filtered by school. Args: school: Optional school…, Load all spells from the database into memory. This should be called during…, BaseModel, StrEnum, Spell data models for the magic system. This module contains Pydantic models…, Valid target types for spells., Valid range types for spells., Valid effect types for spells. (+132 more)

### Community 66 - "test_command_communication.py"
Cohesion: 0.02
Nodes (150): EmoteCommand, LocalCommand, MeCommand, PoseCommand, Communication command models for MythosMUD. This module provides command models…, Command for whispering to a specific player., Command for replying to the last whisper received., Command for saying something to other players in the room. (+142 more)

### Community 67 - "PanelState"
Cohesion: 0.05
Nodes (79): PanelManager(), PanelManagerProps, minimapBackdropLayout(), MinimapPanelBackdrop(), MinimapInlineBody(), MinimapPanelSection(), MinimapPanelSectionProps, ExpandedPanelBody() (+71 more)

### Community 68 - "CombatService"
Cohesion: 0.01
Nodes (193): Taunt command flow: validation and execution. Extracted from combat.py to…, Create CombatService with NATS and register it. Assumes NATS is connected., combat_room_id_for_npc_spell(), Internal helpers for spell_effects.py (coercion, combat room lookup). Keeps the…, Active combat room_id for an NPC, if any., CombatParticipantType, CombatStatus, Enum (+185 more)

### Community 69 - "._initialize_item_services"
Cohesion: 0.40
Nodes (3): Exception, On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item…, Load item prototypes from PostgreSQL and create item factory.

### Community 70 - "CombatConfiguration"
Cohesion: 0.04
Nodes (50): CombatConfiguration, CombatConfigurationError, CombatConfigurationScope, CombatConfigurationService, get_combat_config(), get_combat_configuration(), is_combat_available(), Any (+42 more)

### Community 71 - "magic_service_completion.py"
Cohesion: 0.18
Nodes (16): _is_heal_other_target(), MagicServiceCompletionMixin, Any, UUID, Casting completion flow for spellcasting. Mixin that handles completing a…, Apply spell costs and process effects. Args: player_id: Player ID spell: Spell…, Parse target_id from casting state. Returns None if missing or invalid., Apply costs and queue spell for next combat round. Returns True if queued,… (+8 more)

### Community 72 - "CORSConfig"
Cohesion: 0.03
Nodes (63): Composite application configuration model., ChatConfig, BaseSettings, field_validator, Chat and time configuration models., Chat system configuration., Validate rate limits are reasonable., Temporal compression configuration for the MythosChronicle. (+55 more)

### Community 73 - "CombatInstance"
Cohesion: 0.03
Nodes (100): CombatInstance, UUID, Represents an active combat instance., Get the participant whose turn it is., Advance to the next round - all participants act each round. In round-based…, Check if combat should end. CRITICAL: Combat should NOT end when a player is…, Get all participants that are not dead (includes mortally wounded players at 0…, Update the last activity tick and datetime. (+92 more)

### Community 74 - "asyncio"
Cohesion: 0.06
Nodes (35): asyncio, Test get_mortally_wounded_players() finds mortally wounded players., Test get_mortally_wounded_players() excludes healthy players., Test get_dead_players() returns empty list when no dead players., Test get_dead_players() finds dead players., Test get_dead_players() excludes alive players., Test get_dead_players() handles errors gracefully., Test process_mortally_wounded_tick() returns False when player not found. (+27 more)

### Community 75 - "RoomLoader"
Cohesion: 0.03
Nodes (54): fixture, Create a temporary directory for testing., temp_dir(), Path, Generate room ID from parsed filename and location data. Args: parsed_filename:…, Recursively scan directory for all room JSON files. Args: base_path: Optional…, Validate basic room structure., Extract plane, zone, sub_zone from file path. (+46 more)

### Community 76 - "test_websocket_initial_state.py"
Cohesion: 0.03
Nodes (110): get_container_async_persistence(), Return the container-backed AsyncPersistenceLayer instance. Uses importlib for…, add_npc_occupants_to_list(), _AppStateForEventHandler, _AppStateWithNpcLifecycle, _AppWithState, check_and_send_death_notification(), _ContainerWithNpcLifecycle (+102 more)

### Community 77 - "test_container_persistence_extended_parse.py"
Cohesion: 0.05
Nodes (37): Unit tests for container persistence: JSONB parsing, item fetch, and…, Test _fetch_container_items with no items., Test _fetch_container_items skips rows with missing item_instance_id., Test _fetch_container_items handles non-dictionary rows., Test _fetch_container_items parses string metadata., Test _fetch_container_items handles invalid JSON metadata., Test _fetch_container_items handles non-dict metadata., Test parsing empty list JSONB column. (+29 more)

### Community 78 - "ChatLogger"
Cohesion: 0.07
Nodes (25): ChatLogger, Any, Path, Shutdown the logger and wait for writer thread to finish., Wait for all queued log entries to be processed. Args: timeout: Maximum time to…, Queue a log entry for writing by the background thread. Args: log_type: Type of…, Get the current log file path for the specified type. Args: log_type: Type of…, Write a log entry to the appropriate log file. Args: log_type: Type of log… (+17 more)

### Community 79 - "test_admin_commands.py"
Cohesion: 0.03
Nodes (112): handle_admin_command(), _handle_admin_status_command(), _handle_admin_time_command(), Any, Administrative commands for MythosMUD. This module contains the main admin…, Expose current Mythos time metadata, active holidays, and freeze diagnostics., Entry point for general admin commands that expose subcommands like `admin…, Provide contextual status information about the caller's administrative… (+104 more)

### Community 80 - "test_real_time_helpers.py"
Cohesion: 0.11
Nodes (31): handle_new_game_session(), post, Validate connection manager and accept WebSocket connection. Returns True if…, Resolve player ID from JWT token payload. Validates that the user has a player…, Handle a new game session for a player. This will disconnect existing…, Resolve player ID from a valid JWT. Path UUID is an identity check, not a…, _resolve_player_id_from_path_or_token(), _resolve_player_id_from_token() (+23 more)

### Community 81 - "test_passive_lucidity_flux_service.py"
Cohesion: 0.12
Nodes (32): PassiveLucidityFluxService, PlayerFluxCtx, Bundle for _process_single_player (lizard PARAM)., _make_service(), asyncio, Unit tests for PassiveLucidityFluxService., E2E truncate race: player deleted after load must not abort the flux tick., test_apply_adaptive_resistance_positive_flux_unchanged() (+24 more)

### Community 82 - "PlayerRespawnEventHandler"
Cohesion: 0.03
Nodes (96): PlayerRespawnEventHandler, BoundLogger, ConnectionManager, Player, Room, UUID, Player respawn event handlers. This module handles player respawn and delirium…, Get updated player data for respawn event. As documented in "Resurrection and… (+88 more)

### Community 83 - "test_who_commands.py"
Cohesion: 0.05
Nodes (72): filter_online_players(), filter_players_by_name(), format_who_result(), get_players_for_who(), handle_who_command(), parse_last_active_datetime(), Any, Who command handlers and utilities for MythosMUD. This module contains the who… (+64 more)

### Community 84 - "test_connection_delegates.py"
Cohesion: 0.03
Nodes (119): _async_callable(), cleanup_dead_websocket_impl(), _close_dead_websocket_if_open(), delegate_connection_cleaner(), delegate_connection_cleaner_sync(), delegate_error_handler(), delegate_game_state_provider_sync(), delegate_health_monitor() (+111 more)

### Community 85 - "mythos_dev_ddl.sql"
Cohesion: 0.02
Nodes (5): mythos_dev.aliases, mythos_dev.calendar_holidays, mythos_dev.calendar_npc_schedules, mythos_dev.id_map_users, mythos_dev.professions

### Community 86 - "test_look_room.py"
Cohesion: 0.03
Nodes (112): _filter_other_players(), _format_containers_section(), _format_exits_list(), _format_items_section(), _format_npcs_section(), _format_players_section(), _get_room_description(), _get_room_id() (+104 more)

### Community 87 - "ExplorationCommandFactory"
Cohesion: 0.03
Nodes (98): Unit tests for exploration command factories. Tests the…, Test create_look_command() with 'in' but no target., Test create_look_command() with direction target., Test create_look_command() with direction and instance number., Test create_sit_command() creates SitCommand., Test create_sit_command() raises error with args., Test create_stand_command() creates StandCommand., Test create_stand_command() raises error with args. (+90 more)

### Community 88 - "test_rest_command.py"
Cohesion: 0.04
Nodes (78): Check if player is resting or in login grace period, interrupt rest if needed.…, Check if player is resting or in login grace period, interrupt rest if needed., cancel_rest_countdown(), check_player_in_combat(), _check_rest_location(), handle_rest_command(), Cancel the rest countdown for a player. Called from combat, movement, and spell…, Check if a player is currently in combat. Args: player_id: The player's ID app:… (+70 more)

### Community 89 - "NATSServicePoolMixin"
Cohesion: 0.05
Nodes (34): configure_nats_tls(), nats_connect(), _NatsConnectFn, NatsConnectOptions, Client, Protocol, TypedDict, NATS connect options, TLS setup, and client connect helper. (+26 more)

### Community 90 - "AsciiMapRenderer"
Cohesion: 0.03
Nodes (66): AsciiMapRenderer, _ExitRowContext, Any, NamedTuple, ASCII map renderer for MythosMUD. This module provides server-side rendering of…, True if target room has a reverse exit back to from_room_id., Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…, Return list of (direction, (target_x, target_y), is_bidirectional) for exits… (+58 more)

### Community 91 - "test_player_presence_tracker.py"
Cohesion: 0.03
Nodes (105): _acquire_disconnect_lock(), broadcast_connection_message_impl(), _build_player_info(), _disconnect_during_rest_is_intentional(), _get_instance_manager_from_manager(), Any, Player, UUID (+97 more)

### Community 92 - "look_helpers.py"
Cohesion: 0.03
Nodes (113): _AppWithState, _async_persistence_from_app(), _ContainerWithPersistence, _EquippedPlayer, _get_corruption_label(), _get_corruption_prose(), _get_health_label(), _get_lucidity_label() (+105 more)

### Community 93 - "NPCOccupantProcessor"
Cohesion: 0.03
Nodes (104): NPCOccupantProcessor, Any, NPC occupant processing utilities. This module handles querying and processing…, Determine if NPC should be included in room query results. Args: npc_id: The…, Scan active NPCs to find those in the target room. Args: active_npcs_dict:…, Processes NPC occupants for rooms., Initialize NPC occupant processor. Args: connection_manager: ConnectionManager…, Query NPCs for a room from lifecycle manager. Args: room_id: The room ID room:… (+96 more)

### Community 94 - "ContainerService"
Cohesion: 0.08
Nodes (73): ContainerSourceType, Source type for container instances., ContainerService, Service for managing container operations. Orchestrates open/close, transfer…, MutationDecision, Result of attempting to acquire a guarded mutation context., _allow_all_mutations(), _container() (+65 more)

### Community 95 - "chat_service.py"
Cohesion: 0.04
Nodes (103): ChatResult, _append_channel_history(), _authorize_global_sender(), _authorize_system_sender(), ChatEmoteService, ChatLogger, ChatPlayerService, ChatPlayerView (+95 more)

### Community 96 - "system_monitoring.py"
Cohesion: 0.03
Nodes (89): API module for MythosMUD. This module provides REST API endpoints for the…, AlertResolveResponse, AlertsResponse, CacheMetricsResponse, ConnectionHealthStatsResponse, DualConnectionStatsResponse, IntegrityResponse, MemoryAlertsResponse (+81 more)

### Community 97 - "WebSocketMessageValidator"
Cohesion: 0.04
Nodes (79): get_message_validator(), MessageValidationError, Exception, WebSocketInboundMessage, WebSocket message validation for MythosMUD. This module provides comprehensive…, Calculate the maximum nesting depth of a JSON structure. Args: obj: Object to…, Validate that strings in the JSON structure don't exceed length limits. Args:…, Ensure a message carries a recognizable top-level shape. Returns: bool: True if… (+71 more)

### Community 98 - "CombatParticipant"
Cohesion: 0.02
Nodes (188): CombatParticipant, _get_default_damage(), Check if participant is dead. For players: dead if DP <= -10 For NPCs: dead if…, Check if participant is mortally wounded (players only). For players: mortally…, Check if participant can perform voluntary combat actions. Unconscious (DP <=…, Apply damage to this participant and determine resulting death states.…, Get the default damage value from configuration., Represents a participant in combat. (+180 more)

### Community 99 - "npc_database.py"
Cohesion: 0.04
Nodes (67): close_npc_db(), ensure_npc_database_directory(), get_npc_database_path(), get_npc_engine(), get_npc_session(), get_npc_session_maker(), init_npc_db(), _initialize_npc_database() (+59 more)

### Community 100 - "test_chat_npc_system.py"
Cohesion: 0.04
Nodes (106): Initialize chat service., _ChatDeliveryService, deliver_npc_room_speech(), deliver_personal_system(), npc_sender_id(), _on_npc_spoke(), Protocol, UUID (+98 more)

### Community 101 - "cleanse_command.py"
Cohesion: 0.05
Nodes (52): CleanseApp, CleanseAppState, CleanseContainer, CleansePersistence, CleanseRequest, CleanseTargetPlayer, _format_cooldown_message(), handle_cleanse_command() (+44 more)

### Community 102 - "test_movement_service.py"
Cohesion: 0.02
Nodes (140): check_combat_state(), check_player_posture(), extract_player_id(), Any, Room, UUID, Movement validation helpers for MovementService. Cohesive validation and room-…, Validate player is in the from_room, auto-adding if database matches. (+132 more)

### Community 103 - "test_player_preferences_service.py"
Cohesion: 0.02
Nodes (111): mock_session(), preferences_service(), asyncio, fixture, Unit tests for player preferences service. Tests the PlayerPreferencesService…, Test _is_valid_json_array with invalid JSON., Test creating player preferences successfully., Test creating player preferences with string UUID. (+103 more)

### Community 104 - "maps.py"
Cohesion: 0.05
Nodes (103): _MapRooms, MapZoneContext, NamedTuple, Plane, zone, and sub_zone grouped for map/minimap APIs to reduce parameter…, _apply_exploration_filter_if_needed(), _AsciiMapViewport, _build_ascii_map_response(), _build_ascii_minimap_response() (+95 more)

### Community 105 - "test_combat_service_modules.py"
Cohesion: 0.03
Nodes (106): CombatResult, Result of a combat action., CombatDPSync, Any, UUID, Get persistence layer from application container. Args: player_id: Player ID…, Verify that player DP was successfully saved to database. Args: persistence:…, Log death threshold events based on DP changes. Args: current_dp: New current… (+98 more)

### Community 106 - "TestScheduleService"
Cohesion: 0.05
Nodes (24): Load schedules from PostgreSQL database., asyncio, MonkeyPatch, patch, Test get_active_entries returns empty list when no matches., Test get_active_entries returns matching entries., Test get_active_entries handles boundary conditions correctly., Test get_active_entries returns empty for wrong day. (+16 more)

### Community 107 - "seed_e2e_users.py"
Cohesion: 0.23
Nodes (10): E2eUserSpec, _ensure_player_for_user(), main(), Connection, datetime, UUID, Entry point: run E2E user seed via anyio., One row in users plus optional default character for login E2E. (+2 more)

### Community 109 - "SubjectValidator"
Cohesion: 0.04
Nodes (72): InvalidPatternError, MissingParameterError, NATSSubjectError, PatternNotFoundError, Exception, Custom exceptions for NATS Subject Manager. This module defines all exception…, Base exception for NATS subject-related errors., Exception raised when a pattern name is not found in registry. (+64 more)

### Community 110 - "test_npc_utils.py"
Cohesion: 0.04
Nodes (77): Check if this NPC is required to spawn., extract_definition_id_from_npc(), extract_npc_metadata(), extract_room_id_from_lifecycle_record(), extract_room_id_from_npc(), get_zone_key_from_room_id(), Any, NPC Utility Functions. This module provides utility functions for extracting… (+69 more)

### Community 111 - "Alias"
Cohesion: 0.04
Nodes (66): Alias, Any, BaseModel, Alias model for command aliases. This module defines the Alias model for…, Alias model for command aliases. Stores player command aliases for quick access…, String representation of the alias., Check equality based on name and command., Hash based on name and command for use in sets/dicts. (+58 more)

### Community 112 - "server/schemas/__init__.py"
Cohesion: 0.05
Nodes (81): cleanup_admin_sessions(), get_admin_audit_log(), get_admin_sessions(), get, post, Request, Get active admin sessions., Clean up expired admin sessions. (+73 more)

### Community 113 - "request_with_app_container"
Cohesion: 0.06
Nodes (55): handle_reply_command(), handle_whisper_command(), Reply to last whisper sender., Shared mock wiring for communication command unit tests., Return (request, container) with request.app.state.container wired. Typed…, request_with_app_container(), asyncio, Unit tests for whisper and reply communication command handlers. (+47 more)

### Community 114 - "is_player_in_login_grace_period"
Cohesion: 0.03
Nodes (142): Get login grace period status for player., _as_grace(), cancel_login_grace_period(), _EffectPersistence, get_login_grace_period_remaining(), _grace_period_task(), _GraceApp, _GraceAppState (+134 more)

### Community 115 - "test_logging_utilities.py"
Cohesion: 0.04
Nodes (95): _convert_max_size_to_bytes(), _prepare_log_environment(), Path, Convert max_size string to bytes., Ensure log dirs exist, rotate logs, set root level; return env_log_dir,…, _collect_rotatable_logs(), detect_environment(), ensure_log_directory() (+87 more)

### Community 116 - "test_command_combat.py"
Cohesion: 0.03
Nodes (102): AttackCommand, FleeCommand, KickCommand, PunchCommand, field_validator, Combat command models for MythosMUD. This module provides command models for…, Command for attacking a target., Validate combat target name format using centralized validation. (+94 more)

### Community 117 - "CombatMonitoringService"
Cohesion: 0.04
Nodes (36): Alert, CombatMonitoringService, Any, Convert to dictionary., Comprehensive combat monitoring and alerting service. Tracks combat system…, Initialize the combat monitoring service., Start monitoring a combat instance. Args: combat_id: Unique combat identifier, End monitoring a combat instance. Args: combat_id: Unique combat identifier… (+28 more)

### Community 118 - "container_events.py"
Cohesion: 0.03
Nodes (99): emit_close_container_event(), emit_container_opened_events(), emit_loot_all_event(), emit_transfer_event(), ConnectionManager, UUID, WebSocket event emission helpers for container API endpoints. This module…, Emit WebSocket event for container closing. Args: connection_manager:… (+91 more)

### Community 119 - "PlayerPositionService"
Cohesion: 0.03
Nodes (88): _begin_seated_rest_countdown(), _delayed_disconnect_player_intentionally(), _disconnect_player_intentionally(), _execute_rest_flow(), _get_services_from_app(), is_player_resting(), Any, UUID (+80 more)

### Community 120 - "test_population_control.py"
Cohesion: 0.02
Nodes (86): mock_async_persistence(), mock_event_bus(), mock_lifecycle_manager(), population_controller(), fixture, Unit tests for NPC population control. Tests the NPCPopulationController class., Test load_spawn_rules() loads rules., Test load_spawn_rules() handles empty list. (+78 more)

### Community 121 - "rooms.py"
Cohesion: 0.06
Nodes (77): _apply_room_exit_to_memory(), _apply_room_properties_to_memory(), _build_exit_attributes(), create_room_exit(), _create_room_link_in_db(), delete_room_exit(), _delete_room_link_in_db(), _invalidate_room_cache() (+69 more)

### Community 122 - "test_container_helpers_inventory_find.py"
Cohesion: 0.06
Nodes (88): check_item_matches_target(), _component_metadata(), _container_from_equip_dict(), _container_uuid(), create_wearable_container(), _fallback_create_equipment_container(), find_container_in_room(), find_item_in_inventory() (+80 more)

### Community 123 - "NPCDefinitionCRUDMixin"
Cohesion: 0.09
Nodes (23): NPCDefinitionCRUDMixin, Any, AsyncSession, Execute create_npc_definition stored procedure and return the created…, Validate create_npc_definition parameters. Raises ValueError if invalid., Log successful NPC definition creation., Validate NPC update parameters., Add a simple field to update_data if value is not None. (+15 more)

### Community 124 - "test_user_manager.py"
Cohesion: 0.02
Nodes (97): Unit tests for user manager service. Tests the UserManager class., Test unmute_player() when player is not muted., Test mute_channel() successfully mutes a channel., Test mute_channel() when channel is already muted., Test unmute_channel() successfully unmutes a channel., Test unmute_channel() when channel is not muted., Test mute_global() successfully globally mutes a player., Test mute_global() fails when trying to mute admin. (+89 more)

### Community 125 - "Reporter"
Cohesion: 0.03
Nodes (46): Any, Print validation warnings., Format an error message., Format a warning message., Legacy/programmatic use; prefer click.secho for new code. Colorize output text., Print validation errors., Formats and displays validation results., Generate JSON output for machine consumption. (+38 more)

### Community 126 - "logoutHandler.ts"
Cohesion: 0.15
Nodes (21): fetchSpy, mockLogoutHandler, fetchSpy, mockLogoutHandler, asRecordUnknown(), createLogoutAbortTimer(), createLogoutHandler(), logoutHandler() (+13 more)

### Community 127 - "test_manager.py"
Cohesion: 0.02
Nodes (82): fixture, Unit tests for NATS Subject Manager. Tests the NATSSubjectManager class., Test build_subject() raises SubjectValidationError for invalid parameter., Test build_subject() raises SubjectValidationError when subject too long., Test validate_subject() returns True for valid subject., Test validate_subject() returns False for invalid subject., Test validate_subject() accepts events.domain.{event_type} (distributed…, Test validate_subject() returns False for empty subject. (+74 more)

### Community 128 - "test_look_player.py"
Cohesion: 0.03
Nodes (99): _get_visible_equipment(), Get visible equipment from player, excluding internal/hidden slots. Visible…, _apply_grace_period_labels(), _find_matching_players(), _format_player_look_display(), _get_players_in_room(), _handle_player_look(), _player_id_uuid() (+91 more)

### Community 129 - "NPCCombatIntegrationService"
Cohesion: 0.02
Nodes (117): CombatCommandHandler, CombatCommandHandlerExtras, _NpcWithLife, Any, AppWithState, ConnectionManager, Protocol, Combat command handler class and shared helpers. Extracted from combat.py to… (+109 more)

### Community 130 - "test_combat_persistence_handler_events.py"
Cohesion: 0.06
Nodes (45): Combat persistence handling logic. Handles player DP persistence, verification,…, # NOTE: The game tick loop will also check for dead players, but this provides…, mock_combat_service(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - event publishing. Tests DP update…, Test _publish_player_dp_update_event_impl handles NATS errors gracefully. (+37 more)

### Community 131 - "test_container_helpers_inventory_ops.py"
Cohesion: 0.05
Nodes (88): object, _app_state_container_service(), _coerce_transfer_quantity(), _ensure_item_instance_for_put(), _ensure_mutation_token(), _extract_items_dict_branch(), extract_items_from_container(), _extract_items_json_branch() (+80 more)

### Community 132 - "TestHelperFunctions"
Cohesion: 0.04
Nodes (39): _check_rate_limit(), Check if player is rate limited. Returns result dict if blocked, None if…, asyncio, Unit tests for command handler unified helper functions. Tests helper…, Test _check_grace_period_block returns None when no connection manager., Test _check_grace_period_block returns None when not in grace period., Test _prepare_command_for_processing returns rate limit result., Test _prepare_command_for_processing returns validation result. (+31 more)

### Community 133 - "test_combat_handler.py"
Cohesion: 0.06
Nodes (56): _AppStatePersistence, _AppWithPersistence, _as_app_with_state(), _CmdType, _handler_with_persistence(), mock_persistence(), AppWithState, asyncio (+48 more)

### Community 134 - "IdleMovementHandler"
Cohesion: 0.03
Nodes (87): _cfg_bool(), _cfg_float(), IdleMovementHandler, _npc_id_str(), _passes_movement_probability(), NPC Idle Movement Handler for MythosMUD. This module provides idle movement…, Core gating for idle movement (interval handled by scheduler)., Determine if an NPC should attempt idle movement. Checks multiple conditions: -… (+79 more)

### Community 135 - "connection_manager.py"
Cohesion: 0.01
Nodes (287): Time bundle: the Temporal bounded context…, _apply_disconnect_side_effects(), _cleanup_connection_tracking(), _cleanup_fully_disconnected_player(), _cleanup_player_data(), _cleanup_room_subscriptions(), cleanup_websocket_disconnect(), _close_and_untrack_websockets() (+279 more)

### Community 136 - "test_rest_and_grace_period.py"
Cohesion: 0.07
Nodes (40): is_player_in_grace_period(), Check if a player is currently in grace period. Args: player_id: The player's…, mock_app_with_services(), mock_connection_manager_full(), mock_persistence_full(), MockPersistenceFull, asyncio, fixture (+32 more)

### Community 137 - "test_aggro_threat.py"
Cohesion: 0.04
Nodes (103): add_damage_threat(), add_heal_threat(), _aggression_scale(), apply_stealth_wipe(), apply_taunt(), clear_aggro_for_combat(), _corruption_scale(), _get_aggro_config() (+95 more)

### Community 138 - "test_rate_limiter.py"
Cohesion: 0.08
Nodes (25): Unit tests for rate limiter service. Tests the RateLimiter class which provides…, Test check_rate_limit returns True when within limits., Test check_rate_limit returns False when limit exceeded., Test check_rate_limit handles errors gracefully (fails open)., Test record_message adds timestamp to window., Test reset_player_limits handles nonexistent player., Test get_system_stats handles no active players., Test is_player_rate_limited returns False when not rate limited. (+17 more)

### Community 139 - "look_command.py"
Cohesion: 0.02
Nodes (146): _app_from_request(), _as_response(), _connection_manager_from_app(), _container_from_app(), _get_app_and_persistence(), _get_room_drops(), _handle_implicit_target_lookup(), handle_look_command() (+138 more)

### Community 140 - "ApplicationContainer"
Cohesion: 0.02
Nodes (122): nats_is_connected(), Return True when nats_service exposes is_connected() and it is true., _attach_combat_service(), _create_npc_services_on_app(), _ensure_room_cache_before_npc_startup(), initialize_chat_service(), initialize_combat_services(), initialize_nats_and_combat_services() (+114 more)

### Community 141 - "mythos_e2e_ddl.sql"
Cohesion: 0.02
Nodes (5): mythos_e2e.aliases, mythos_e2e.calendar_holidays, mythos_e2e.calendar_npc_schedules, mythos_e2e.id_map_users, mythos_e2e.professions

### Community 142 - "test_websocket_handler_validation_errors.py"
Cohesion: 0.03
Nodes (78): WebSocket, Send a system message to a player. Args: websocket: The WebSocket connection…, send_system_message(), Test send_system_message sends system message., test_send_system_message(), mock_websocket(), asyncio, fixture (+70 more)

### Community 143 - "FeatureFlagService"
Cohesion: 0.03
Nodes (54): Initialize the combat configuration service., FeatureFlagService, get_feature_flags(), is_combat_enabled(), is_combat_logging_enabled(), is_combat_monitoring_enabled(), Any, Feature flag service for MythosMUD. This service provides centralized feature… (+46 more)

### Community 144 - "test_player_event_handlers_utils.py"
Cohesion: 0.02
Nodes (91): mock_connection_manager(), mock_logger(), mock_name_extractor(), player_event_handler_utils(), asyncio, fixture, Unit tests for player event handler utilities. Tests the…, Test get_player_info() returns None for invalid player_id. (+83 more)

### Community 145 - "TargetType"
Cohesion: 0.08
Nodes (52): _flee_effect_failure_response(), _flee_effect_invalid_target_response(), _flee_effect_invalid_target_type_response(), _flee_effect_not_in_combat_response(), _flee_effect_room_error_response(), _flee_effect_services_available(), _flee_effect_services_unavailable_response(), _flee_effect_success_response() (+44 more)

### Community 146 - "test_logout_commands.py"
Cohesion: 0.03
Nodes (102): _clear_corrupted_cache_entry(), _coerce_player_uuid(), _disconnect_player_connections(), _force_disconnect_player(), _get_player_for_logout(), _get_player_position_from_connection_manager(), _is_coroutine_object(), _mark_quit_intentional() (+94 more)

### Community 147 - "test_player_combat_service.py"
Cohesion: 0.04
Nodes (71): PlayerCombatState, Get a player's combat state. Args: player_id: ID of the player Returns:…, Represents a player's combat state., Initialize last_activity if not provided., mock_event_bus(), mock_npc_service(), mock_persistence(), player_combat_service() (+63 more)

### Community 148 - "mythos_unit_ddl.sql"
Cohesion: 0.02
Nodes (5): mythos_unit.aliases, mythos_unit.calendar_holidays, mythos_unit.calendar_npc_schedules, mythos_unit.id_map_users, mythos_unit.professions

### Community 149 - "test_connection_helpers_impl.py"
Cohesion: 0.06
Nodes (60): broadcast_global_event_impl(), broadcast_room_event_impl(), handle_new_login_impl(), _optimize_payload(), Any, _queue_message_if_needed(), Queue message for later delivery if no active connections. Args: player_id: The…, Update final delivery status based on connection results. Args:… (+52 more)

### Community 150 - "test_metrics_endpoints.py"
Cohesion: 0.06
Nodes (79): delete_dlq_message(), get_dlq_messages(), get_metrics(), get_metrics_summary(), _get_nats_handler(), _handle_replay_error(), _load_dlq_message(), Any (+71 more)

### Community 151 - "test_look_npc.py"
Cohesion: 0.03
Nodes (131): _find_matching_npcs(), _format_core_attributes(), _format_lifecycle_info(), _format_multiple_npcs_result(), _format_npc_description(), _format_npc_stats_for_admin(), _format_other_stats(), _format_single_npc_result() (+123 more)

### Community 152 - "test_status_commands.py"
Cohesion: 0.04
Nodes (81): _add_additional_stats_lines(), _add_profession_lines(), _build_base_status_lines(), _build_status_result(), _get_combat_status(), _get_profession_info(), _get_status_persistence(), handle_status_command() (+73 more)

### Community 153 - "AppConfig"
Cohesion: 0.07
Nodes (38): AppConfig, Any, BaseSettings, model_validator, Composite application configuration. This is the main configuration class that…, Initialize configuration and set environment variables for legacy compatibility., Set environment variables for legacy code that reads them directly., Return first set CORS origins env var to reduce CCN in _sanitize. (+30 more)

### Community 154 - "test_quest_service.py"
Cohesion: 0.06
Nodes (84): _collect_progress_sync(), Return quest_service.sync_collect_progress when it is callable., _DefinitionRow, _FullInventory, _InstanceStub, _make_definition_row(), _make_kill_definition_row(), _make_turn_in_definition_row() (+76 more)

### Community 155 - "test_logging_processors.py"
Cohesion: 0.04
Nodes (79): EventDict, add_correlation_id(), add_request_context(), _enhance_one_player_id(), enhance_player_ids(), _EnhancePlayerIdsTls, _PlayerServiceHolder, UUID (+71 more)

### Community 156 - "test_npc_service.py"
Cohesion: 0.04
Nodes (90): NPCService, Comprehensive NPC management service. Handles CRUD operations for NPC…, Initialize the NPC service., _def_row(), _mock_result_mappings_all(), mock_session(), npc_service(), asyncio (+82 more)

### Community 157 - "SchemaValidator"
Cohesion: 0.04
Nodes (35): Convert legacy string format exits to new object format internally. This allows…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data…, Check if an exit is marked as one-way. Args: exit_data: Exit data in either…, Check if an exit is marked as self-reference. Args: exit_data: Exit data in…, Validates room definitions against JSON schema. Supports both legacy string…, SchemaValidator, Tests for the schema validator module. Tests JSON schema validation, exit… (+27 more)

### Community 158 - "manual_dependency_analysis.py"
Cohesion: 0.06
Nodes (55): _dep_info_from_npm_row(), DependencyAnalyzer, main(), _parse_npm_outdated_json(), Path, Analyze Python dependencies, Determine overall upgrade strategy, Assess overall project risks (+47 more)

### Community 159 - "api/monitoring.py"
Cohesion: 0.06
Nodes (84): _assemble_health_response(), force_memory_cleanup(), get_cache_metrics(), get_connection_health_stats(), get_dual_connection_stats(), get_eventbus_metrics(), get_health_status(), get_memory_alerts() (+76 more)

### Community 160 - "admin_teleport_commands.py"
Cohesion: 0.04
Nodes (106): Admin teleport command handlers for MythosMUD. This module provides handlers…, execute_confirm_goto(), execute_goto_teleport(), log_goto_failure(), Any, Exception, Helper functions for goto command operations., Log failed goto action. (+98 more)

### Community 161 - "FollowService"
Cohesion: 0.02
Nodes (163): NPCEnteredRoom, Event fired when an NPC enters a room. This event is triggered when an NPC…, drop_follower(), ensure_follower_standing(), follower_already_in_room(), follower_needs_stand(), _FollowMovementHost, on_npc_entered_room() (+155 more)

### Community 162 - "player.ts"
Cohesion: 0.09
Nodes (44): locationIndicatesDeathVoid(), requiredAliveButDeadMessage(), assertLookVisibleInPanels(), lookAndStand(), prepAwForAdminSet(), prepNonAdminForSetAttempt(), runAdminSetWithRecovery(), assertNpcSpawnVisible() (+36 more)

### Community 163 - "admin_setstat_command.py"
Cohesion: 0.04
Nodes (79): _apply_corruption_via_service(), _apply_lucidity_via_service(), _apply_stat_change_and_build_result(), _execute_admin_set_stat(), _finish_occult_stat_change(), _get_catatonia_registry_from_app(), _maybe_attach_dp_posture_message(), _mutate_player_stat() (+71 more)

### Community 164 - "ChatModeration"
Cohesion: 0.04
Nodes (44): ChatModeration, normalize_player_id(), PlayerServiceProtocol, Any, datetime, Protocol, UUID, Chat moderation utilities. This module provides moderation functionality… (+36 more)

### Community 165 - "QuestService"
Cohesion: 0.05
Nodes (60): Persist player after spell mutations., Quest subsystem: service, goal progression, rewards., _build_collect_n_progress(), _call_add_item_to_inventory(), _collect_goal_prototype_id(), _collect_goal_required_count(), _consume_collect_goals_from_player(), _definition_completion_mode_error() (+52 more)

### Community 166 - "test_combat_schema.py"
Cohesion: 0.08
Nodes (46): Draft7Validator, add_default_combat_data_to_config(), add_default_combat_data_to_stats(), CombatSchemaValidationError, get_combat_stats_summary(), Any, Exception, Combat system JSON schema validation. This module provides JSON schema… (+38 more)

### Community 167 - "deleteCharacterFlow.ts"
Cohesion: 0.12
Nodes (39): errorMessageFromApiBody(), parseSelectCharacterResult(), pickString(), requestDeleteCharacter(), resolveSelectedId(), CreationRefreshResult, messageFromCreationRefreshHttpError(), DeleteCharacterNextStep (+31 more)

### Community 168 - "test_go_command.py"
Cohesion: 0.04
Nodes (81): Exploration commands for MythosMUD. This module contains handlers for…, _cancel_rest_if_moving(), _canonical_room_id_for_go(), _connection_manager_from_go_app(), _execute_movement(), handle_go_command(), _movement_combat_and_event_bus_from_go_app(), _movement_service_for_go_command() (+73 more)

### Community 169 - "test_lifecycle_periodic.py"
Cohesion: 0.06
Nodes (56): NPCMaintenanceConfig, Any, NPC Configuration for MythosMUD. This module defines configuration settings for…, Configuration for NPC lifecycle maintenance. This class centralizes all timing…, Get the respawn delay for a specific NPC type. Args: npc_type: Type of NPC…, Check if NPC maintenance should run on this tick. Args: tick_count: Current…, Get a summary of all NPC configuration values. Returns: Dictionary containing…, Clean up old lifecycle records (delegates to lifecycle_periodic). (+48 more)

### Community 170 - "get_hallucinated_exits"
Cohesion: 0.11
Nodes (26): get_hallucinated_exits(), _hash_string(), mulberry32(), Server-side exit hallucination for the deranged lucidity tier (#626, #714).…, 32-bit string hash (djb2 variant) -- port of hashString() in…, Combine room + player into a single seed -- order matters, port of seedFrom()., mulberry32: small, fast, deterministic PRNG -- port of mulberry32() in…, Deterministic shuffle driven by rng -- port of shuffle() (random-key sort, not… (+18 more)

### Community 171 - "TaskRegistry"
Cohesion: 0.08
Nodes (40): get_registry(), Centralized TaskRegistry for MythosMUD server task lifecycle management. This…, Cancel lifecycle/critical tasks first (Phase 1)., Cancel remaining active tasks (Phase 2)., Wait for task completion with timeout., Forcibly cancel any lingering tasks that didn't respond to graceful…, Clean up active collections after final shutdown., Gracefully shutdown all tracked tasks with timeout coordination. Implements… (+32 more)

### Community 172 - "test_game_state_provider.py"
Cohesion: 0.03
Nodes (79): game_state_provider(), mock_get_app(), mock_get_async_persistence(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for game state provider. Tests the GameStateProvider class. (+71 more)

### Community 173 - "MemoryLeakMetricsCollector"
Cohesion: 0.03
Nodes (66): Initialize monitoring services. Depends on Core/Realtime/Game for injected deps., MemoryLeakMetricsCollector, Any, Collect event metrics from EventBus. Returns: Dictionary with event metrics, Collect cache metrics from CacheManager. Returns: Dictionary with cache metrics, Collect task metrics from TaskRegistry. Returns: Dictionary with task metrics, Collect NATS subscription metrics from NATSService. Returns: Dictionary with…, Unified metrics collector for memory leak detection. Aggregates metrics from… (+58 more)

### Community 174 - "test_message_queue.py"
Cohesion: 0.03
Nodes (111): Coord, build_tile_grid(), _check_disconnected_rooms(), compute_bounds(), dump_ascii_to_file(), example_validator(), _handle_coordinate_conflict(), _handle_spatial_collision() (+103 more)

### Community 175 - "NATSError"
Cohesion: 0.02
Nodes (144): NATSConnectionError, NATSError, NATSHealthCheckError, NATSPublishError, NATSRequestError, NATSSubscribeError, NATSUnsubscribeError, Exception (+136 more)

### Community 176 - "container_persistence.py"
Cohesion: 0.07
Nodes (67): _coerce_row_quantity(), parse_jsonb_column(), PsycopgCursor, Update container items using stored procedures. Args: cursor: Database cursor…, Normalize quantity/position from DB row cells; bool -> 1 (not…, Parse a JSONB column value from database. JSONB columns may be returned as: -…, update_container_items(), _after_container_insert() (+59 more)

### Community 177 - "PopulationStats"
Cohesion: 0.05
Nodes (52): PopulationStats, Any, Population Statistics Module. This module provides the PopulationStats class…, Statistics for NPC population in a zone or sub-zone., Initialize population statistics. Args: zone_id: The zone identifier…, Add an NPC to the population statistics. Args: npc_type: Type of the NPC…, Remove an NPC from the population statistics. Args: npc_type: Type of the NPC…, Convert population statistics to dictionary. (+44 more)

### Community 178 - "ExplorationService"
Cohesion: 0.03
Nodes (110): RoomDictList, _apply_exploration_filter_if_needed(), Any, Apply exploration filter to rooms if requested and user is not admin. Args:…, ExplorationService, Any, AsyncSession, UUID (+102 more)

### Community 179 - "logging_file_setup.py"
Cohesion: 0.04
Nodes (91): Formatter, Logger, _PlayerGuidFormatterType, Queue, QueueHandler, QueueListener, LoggingConfig, BaseSettings (+83 more)

### Community 180 - "dialogue_definitions_api.py"
Cohesion: 0.08
Nodes (45): create_dialogue_definition(), delete_dialogue_definition(), get_dialogue_definition(), list_dialogue_definitions(), delete, get, post, put (+37 more)

### Community 181 - "CreateItemInstanceInput"
Cohesion: 0.06
Nodes (54): CreateItemInstanceInput, TypedDict, Optional fields for create_item_instance. owner_type, owner_id, etc. with…, create_item_instance_async(), ensure_item_instance_async(), item_instance_exists_async(), _item_instance_upsert_params(), _metadata_from_options() (+46 more)

### Community 182 - "catatonia_check.py"
Cohesion: 0.04
Nodes (56): check_catatonia_block(), _check_catatonia_database(), _check_catatonia_registry(), _convert_player_id_to_uuid(), _fetch_lucidity_record(), _is_catatonic(), _load_player_for_catatonia_check(), _PersistenceGetPlayerByName (+48 more)

### Community 183 - "test_combat_flee_helpers.py"
Cohesion: 0.05
Nodes (62): AppWithState, Protocol, Shared Starlette/FastAPI-shaped protocols for combat command modules. Keeps…, Application object with a ``state`` namespace (dynamic attributes)., _ensure_flee_standing(), _FleeCommandHandlerLike, _get_flee_player_uuid(), _get_flee_room_id() (+54 more)

### Community 184 - "test_shutdown_sequence.py"
Cohesion: 0.05
Nodes (73): _find_uvicorn_processes(), Any, Process termination utilities for graceful server shutdown. This module handles…, Schedule a best-effort graceful process termination after a short delay. This…, Find all uvicorn processes using psutil., Terminate all uvicorn processes., Terminate all child processes of the current process., Fallback signal-based termination when psutil is not available. (+65 more)

### Community 185 - "player_presence_tracker.py"
Cohesion: 0.03
Nodes (117): build_catchup_message(), capture_grace_snapshot(), CatchupManager, CatchupPlayer, _dp_snapshot(), Protocol, UUID, Reconnect catch-up summary for disconnect-grace players (`#297`). While a… (+109 more)

### Community 186 - "useGameConnectionRefactored.ts"
Cohesion: 0.07
Nodes (35): ADR-0018, ThrowingWebSocket, connectOpenAndRunPingInterval(), defaultOptions, latestWebSocketInstance, { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval }, MockWebSocket, wsConnectionAfterEach() (+27 more)

### Community 187 - "test_player_event_handlers_room.py"
Cohesion: 0.04
Nodes (72): asyncio, Unit tests for player room event handlers. Tests the PlayerRoomEventHandler…, Test broadcast_player_entered_message() skips when room_id is None., Test subscribe_player_to_room() successfully subscribes player., #297/#610: subscribing on movement must also refresh…, Test subscribe_player_to_room() handles invalid player_id., Test subscribe_player_to_room() handles subscription errors., Test _send_room_name_message() sends room name. (+64 more)

### Community 188 - "ContainerLockState"
Cohesion: 0.05
Nodes (43): ContainerFactoryOptions, ContainerLockState, datetime, StrEnum, TypedDict, UUID, Container component model for the unified container system. As documented in…, Check if container has decayed (for corpse containers). (+35 more)

### Community 189 - "test_party_service.py"
Cohesion: 0.04
Nodes (49): Unit tests for PartyService. Covers: create_party, disband_party, add_member,…, Member can leave; party remains., When leader leaves, party is disbanded., Leader can kick a member., Non-leader cannot kick., Leader cannot kick themselves., Leader can disband the party., Non-leader cannot disband. (+41 more)

### Community 190 - "PerformanceMonitor"
Cohesion: 0.05
Nodes (58): ExceptionStats, Statistics for exception tracking., __getattr__(), Any, Monitoring package for MythosMUD server., Lazy import for modules that require numpy., MonitoringSummary, Comprehensive monitoring dashboard for MythosMUD server. This module provides a… (+50 more)

### Community 191 - "executeCommand"
Cohesion: 0.11
Nodes (38): prepCoLocatedContexts(), expectWhoListingOnPage(), nudgeStandBothPlayers(), primeBothForCoLocate(), waitForLookReflected(), executeUnmuteAndWaitForAck(), nudgeStandBothPlayers(), primeBothForCoLocate() (+30 more)

### Community 192 - "test_logging_handlers.py"
Cohesion: 0.04
Nodes (65): _aggregator_handler_class_for_windows(), AsyncioConnLostWriteFilter, create_aggregator_handler(), _make_exec_for_aggregator(), Any, LogRecord, Path, RotatingFileHandler (+57 more)

### Community 193 - "test_admin_setlucidity_command.py"
Cohesion: 0.05
Nodes (78): _apply_lucidity_change(), check_admin_permissions(), _execute_lucidity_change(), _extract_command_args(), _get_catatonia_registry_from_app(), get_current_lcd(), get_player_service_from_app(), _handle_admin_set_lucidity_command() (+70 more)

### Community 194 - "test_occupant_formatter.py"
Cohesion: 0.11
Nodes (17): Unit tests for occupant formatter. Tests the occupant_formatter module classes…, Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists., Test OccupantFormatter._process_player_name_for_update() skips UUID player name., Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict., Test OccupantFormatter.separate_occupants_by_type() separates dict players., Test OccupantFormatter.separate_occupants_by_type() handles empty list., Test OccupantFormatter._is_valid_name_for_occupant() returns True for valid… (+9 more)

### Community 195 - "RoomDataCache"
Cohesion: 0.04
Nodes (39): Any, Get statistics about the room data cache. Args: is_room_data_fresh_func:…, Merge room data with proper conflict resolution. Args: old_data: Existing room…, Manages room data caching and freshness validation., Check if new data is newer than old data for a specific key. Args: old_data:…, Initialize the room data cache. Args: freshness_threshold_seconds: Threshold in…, Check if room data is fresh enough to use. Args: room_data: Room data to check…, Get room data from cache. Args: room_id: Room ID to retrieve Returns: Dict[str,… (+31 more)

### Community 196 - "RoomDataValidator"
Cohesion: 0.07
Nodes (39): Any, Validate occupant count consistency. Args: room_data: Room data to validate…, Validate room ID format. Args: room_id: Room ID to validate Returns: bool: True…, Check if occupant count matches the actual occupants list length. Args:…, Validates room data structure and content., Check for duplicate occupants in the room. Args: room_data: Room data to check…, Check if room has occupants but no name. Args: room_data: Room data to check…, Validate room data structure and content. Args: room_data: Room data to… (+31 more)

### Community 197 - "test_error_handling_middleware.py"
Cohesion: 0.06
Nodes (53): add_error_handling_middleware(), ErrorHandlingMiddleware, extract_user_id_from_non_mapping(), ASGIApp, Exception, FastAPI, Protocol, Receive (+45 more)

### Community 198 - "test_lucidity_recovery_commands.py"
Cohesion: 0.05
Nodes (72): _format_cooldown_message(), _format_recovery_success_message(), handle_folk_tonic_command(), handle_group_solace_command(), handle_meditate_command(), handle_pray_command(), handle_therapy_command(), _perform_recovery_action() (+64 more)

### Community 199 - "test_hallucination_services.py"
Cohesion: 0.04
Nodes (69): LucidityActionCode, StrEnum, Action codes used for lucidity cooldowns (debrief, hallucination timer, etc.)., HallucinationFrequencyService, Any, AsyncSession, UUID, Hallucination frequency service for MythosMUD. Implements tier-based… (+61 more)

### Community 200 - "test_lucidity_event_dispatcher.py"
Cohesion: 0.05
Nodes (72): _dispatch_player_event(), _format_liabilities(), LucidityChangeEventExtras, LiabilityStackEntry, UUID, Helpers for broadcasting lucidity-related SSE events., Emit a catatonia state event to the affected player., Send rescue progress/status updates to either participant. (+64 more)

### Community 201 - "PlayerStateCommandFactory"
Cohesion: 0.04
Nodes (68): Unit tests for player state command factories. Tests the…, Test create_cleanse_command() raises error with args., Test create_skills_command() creates SkillsCommand., Test create_skills_command() raises error with args., Test create_catalog_command() with no args., Test create_catalog_command() preserves filter tokens., Test create_journal_command() creates JournalCommand., Test create_status_command() creates StatusCommand. (+60 more)

### Community 202 - "GameConfig"
Cohesion: 0.08
Nodes (23): GameConfig, BaseSettings, field_validator, Game-specific configuration., Validate combat tick interval., Validate combat timeout., Validate combat XP multiplier., Validate combat alert threshold. (+15 more)

### Community 203 - "apiTypeGuards.ts"
Cohesion: 0.12
Nodes (43): ApiErrorWithDetail, assertCharacterInfoArray(), assertProfessionArray(), assertRefreshTokenResponse(), assertStatsRollResponse(), hasAtLeastOneIdentifier(), hasOptionalString(), hasServerCharacterCoreFields() (+35 more)

### Community 204 - "ZoneConfiguration"
Cohesion: 0.05
Nodes (53): Represents the configuration for a zone or sub-zone., Calculate effective spawn probability based on zone modifiers. Args:…, Check if a player can access this zone based on requirements. Args:…, ZoneConfiguration, Test get_zone_configuration() returns exact match., Test get_zone_configuration() falls back to zone-level config., Test get_zone_configuration() handles zone key without slash., Test _check_spawn_requirements_for_room() checks NPC definitions. (+45 more)

### Community 205 - "CombatAuditLogger"
Cohesion: 0.05
Nodes (59): CombatAttackDetails, CombatAuditLogger, CombatMonitoringAlert, CombatParties, CombatSecurityEvent, Any, datetime, Combat-specific audit logging and monitoring. This module provides specialized… (+51 more)

### Community 206 - "MemoryProfiler"
Cohesion: 0.04
Nodes (58): OtherModel, BaseModel, Unit tests for memory profiler utilities. Tests the MemoryProfiler class…, Test MemoryProfiler.measure_model_instantiation() handles zero iterations., Test MemoryProfiler.get_memory_usage_summary() returns summary., Test MemoryProfiler.print_memory_summary() doesn't raise., Test Pydantic model for memory profiling tests., Test MemoryProfiler.print_model_memory_usage() doesn't raise. (+50 more)

### Community 207 - "test_alias_commands.py"
Cohesion: 0.05
Nodes (69): _create_alias(), _extract_alias_params(), handle_alias_command(), handle_aliases_command(), handle_unalias_command(), Any, Alias management commands for MythosMUD. This module contains handlers for…, Handle the aliases command for listing all aliases. Args: command_data: Command… (+61 more)

### Community 208 - "build_event"
Cohesion: 0.02
Nodes (180): build_event(), _get_next_global_sequence(), Protocol, UUID, Event envelope utilities for MythosMUD real-time messages. Provides a single,…, Minimal typing for connection_manager passed to build_event (sequence_counter…, Custom JSON encoder that handles UUID objects., Thread-safe global sequence number generation (fallback when no… (+172 more)

### Community 209 - "test_room_sync_service.py"
Cohesion: 0.04
Nodes (67): mock_room_service(), asyncio, fixture, Unit tests for room sync service. Tests the RoomSyncService class for room…, Test _process_room_update_with_validation() processes valid room data., Test _process_room_update_with_validation() fixes invalid room data., Test _process_room_update_with_validation() handles stale data., Test _process_room_update_with_validation() handles errors gracefully. (+59 more)

### Community 210 - "LogAggregator"
Cohesion: 0.06
Nodes (48): LogEntry, aggregate_log_entry(), get_log_aggregator(), LogAggregator, LogEntry, LogQueryFilter, _optional_datetime_from_object(), _optional_str_from_object() (+40 more)

### Community 211 - "admin_hallucinate_command.py"
Cohesion: 0.05
Nodes (79): deliver_forced_hallucination(), extract_args(), get_current_lcd_or_error(), HallucinateCommandError, _handle_admin_hallucinate_command(), _log_hallucinate_command(), Exception, Request (+71 more)

### Community 212 - "test_enhanced_logging_config.py"
Cohesion: 0.10
Nodes (31): configure_enhanced_structlog(), _configure_third_party_log_levels(), Set up enhanced logging configuration with MDC and security features. Args:…, Set third-party loggers to avoid ERROR noise in errors.log (e.g. NATS…, Configure enhanced Structlog with MDC, security, and performance features.…, setup_enhanced_logging(), _as_bound_logger(), _disabled_config() (+23 more)

### Community 213 - "exception_metrics.py"
Cohesion: 0.40
Nodes (4): get_summary(), Any, Exception metrics tracking for monitoring. This module provides thread-safe…, Get a summary of exception counts. Returns: dict[str, Any]: Dictionary…

### Community 214 - "test_nats_message_handler_subzone_events.py"
Cohesion: 0.04
Nodes (68): asyncio, Unit tests for NATS message handler subzone and event handling. Tests subzone…, Test cleanup_empty_subzone_subscriptions cleans up empty subzones., Test subscribe_to_subzone handles errors., Test subscribe_to_subzone raises error when subject manager unavailable., Test unsubscribe_from_event_subjects handles partial success., Test subscribe_to_event_subjects handles partial failure., Test get_event_subscription_count returns count. (+60 more)

### Community 215 - "game_state_provider.py"
Cohesion: 0.05
Nodes (47): Internal implementation for sending room occupants update. This method is used…, Send room occupants update to players in the room (public API). Preserves…, Game state provision for connection management. This module provides…, Integration components for connection management. This package provides…, build_room_update_event(), ConnectionManager, Room, TypedDict (+39 more)

### Community 216 - "inventory_command_helpers.py"
Cohesion: 0.03
Nodes (131): _DropResolved, _FloorPickupResolved, Protocol, Shared types for inventory command handlers (Lizard: keep main module small)., Narrows room managers for floor drop operations (pickup / get room)., RoomDropManager, add_pickup_to_inventory(), broadcast_room_event() (+123 more)

### Community 217 - "test_character_creation_service.py"
Cohesion: 0.03
Nodes (62): CharacterCreationService, Any, UUID, Validate character stats against class prerequisites. Args: stats: The stats…, Create a new character with specific stats. Args: name: The character's name…, Get information about all available character classes and their prerequisites.…, Service class for character creation and stats generation business operations., Get a description for a character class. (+54 more)

### Community 218 - "api/game.py"
Cohesion: 0.04
Nodes (59): broadcast_message(), get_game_status(), get_mythos_time(), get, post, Game mechanics API endpoints for MythosMUD server. This module handles all game…, Return the current Mythos calendar metadata for HUD initialization. In-memory…, Get current game status and connection information. (+51 more)

### Community 219 - "test_async_persistence_core.py"
Cohesion: 0.05
Nodes (54): asyncio, Unit tests for async persistence layer: init, close, player, user, room,…, Test get_players_by_user_id delegates to PlayerRepository., Test get_active_players_by_user_id delegates to PlayerRepository., Test get_user_by_username_case_insensitive with successful lookup., Test get_user_by_username_case_insensitive when user not found., Test get_user_by_username_case_insensitive with database error., Test save_player delegates to PlayerRepository. (+46 more)

### Community 220 - "maps.ts"
Cohesion: 0.09
Nodes (32): buildHeaders(), buildMapUrl(), fetchAsciiMap(), FetchAsciiMapParams, fetchAsciiMinimap(), FetchAsciiMinimapParams, formatDetailMessage(), formatMapErrorResponse() (+24 more)

### Community 221 - "Async Remediation Summary - December 3, 2025"
Cohesion: 0.03
Nodes (67): 1. Fixed Event Loop Blocking in PassiveLucidityFluxService, 2. Removed asyncio.run() from Exploration Service, 3. Added Exception Handling for Database Engine Creation, Achieved, 🏆 Achievement Highlights, Adjusts spectacles with scholarly satisfaction, After, After Fixes (+59 more)

### Community 222 - "test_player_respawn_service.py"
Cohesion: 0.02
Nodes (131): PlayerDeliriumRespawnedEvent, Event fired when a player respawns after delirium. This event is triggered when…, Delegate player delirium respawned event to specialized handler., Handle player delirium respawn events by sending respawn notification to the…, _PlayerCombatClearing, PlayerRespawnService, AsyncSession, datetime (+123 more)

### Community 223 - "TestCombatConfigurationService"
Cohesion: 0.05
Nodes (23): fixture, Test suite for CombatConfigurationService class., Create a mock config object., Create a CombatConfigurationService instance for testing., Test CombatConfigurationService initialization., Test get_combat_configuration returns configuration., Test get_combat_configuration caches configuration., Test get_combat_configuration_for_scope with global scope. (+15 more)

### Community 224 - "NPCThreadManager"
Cohesion: 0.04
Nodes (73): NPCThreadManager, Start a thread for a specific NPC. Args: npc_id: Unique identifier for the NPC…, Stop a specific NPC thread. Args: npc_id: Unique identifier for the NPC…, Internal method to stop an NPC thread., Restart a specific NPC thread. Args: npc_id: Unique identifier for the NPC…, Get list of active NPC thread IDs., Get NPC definition for a specific NPC., Worker function for individual NPC threads. This function runs in a separate… (+65 more)

### Community 225 - "test_npc_startup_service.py"
Cohesion: 0.04
Nodes (66): _errors_len(), asyncio, Unit tests for NPC startup service. Tests the NPCStartupService class., Test _spawn_required_npcs() successfully spawns required NPCs., Test _spawn_required_npcs() handles missing spawn room., Test _spawn_required_npcs() handles spawn failures., Test _spawn_optional_npcs() spawns based on probability., Test _spawn_optional_npcs() skips NPCs with low probability. (+58 more)

### Community 226 - "lifespan_protocols.py"
Cohesion: 0.07
Nodes (63): MemoryMonitor, _container_attr(), _legacy_container_attr(), lifespan_connection_manager(), lifespan_container(), lifespan_event_bus(), lifespan_memory_monitor(), lifespan_nats_handler() (+55 more)

### Community 227 - "compare_linting_results.py"
Cohesion: 0.07
Nodes (43): _build_file_line_index(), categorize_findings(), _categorize_pylint_finding(), _categorize_ruff_finding(), compare_findings(), _find_overlapping_findings(), _find_unmatched_findings(), Finding (+35 more)

### Community 228 - "AsyncPersistenceRoomFacade"
Cohesion: 0.12
Nodes (10): AsyncPersistenceRoomFacade, AsyncSession, Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests., Mixin: lazy room-cache load and loader delegation for unit tests., Delegate to room loader; exposed for unit tests., Delegate to room loader; exposed for unit tests. (+2 more)

### Community 229 - "CatatoniaRegistry"
Cohesion: 0.04
Nodes (36): Initialize combat services., CatatoniaRegistry, datetime, UUID, In-memory registry tracking catatonic investigators., Return True if the player is currently registered as catatonic., Return a shallow copy of the current registry for diagnostics., Track players who have entered catatonia and coordinate failover hooks. (+28 more)

### Community 230 - "test_metrics.py"
Cohesion: 0.03
Nodes (60): Any, Get current metrics summary. Returns: Dictionary containing all metrics, Calculate percentile from list of times. Args: times: List of time measurements…, Reset all metrics to zero., Performance metrics for NATS Subject Manager operations. Tracks validation…, Initialize metrics collection., Record a validation operation. Args: duration: Time taken in seconds success:…, Record a build operation. Args: duration: Time taken in seconds success:… (+52 more)

### Community 231 - ".resolve_target"
Cohesion: 0.05
Nodes (30): PersistenceProtocol, PlayerServiceProtocol, Player, Protocol, Room, UUID, Validate player exists and is in a room. Returns (room_id, error_result)., Clean target name and extract disambiguation suffix. Returns (clean_target,… (+22 more)

### Community 232 - "RoomMapViewer.tsx"
Cohesion: 0.08
Nodes (42): fetchSpy, useMapLayout(), UseMapLayoutOptions, buildRoomListRequest(), FetchRoomListConfig, fetchRoomListData(), parseRoomListResponse(), useRoomMapData() (+34 more)

### Community 233 - "PlayerEventHandlerUtils"
Cohesion: 0.02
Nodes (101): OccupantSnap, Initialize utility functions and specialized handlers., _as_map(), _as_occupant_snap(), _NamedRoom, OccupantsUpdateFn, PlayerRoomEventHandler, PlayerRoomEventHandlerDeps (+93 more)

### Community 234 - "HealthStatus"
Cohesion: 0.03
Nodes (124): HealthStatus, ConnectionsComponent, DatabaseComponent, HealthComponents, HealthResponse, HealthStatus, BaseModel, StrEnum (+116 more)

### Community 235 - "PlayerRepositoryProtocol"
Cohesion: 0.05
Nodes (34): PlayerRepositoryProtocol, datetime, Player, Protocol, Room, UUID, List all cached rooms., Protocol for player persistence operations. Defines the contract used by… (+26 more)

### Community 236 - "test_mp_regeneration_service.py"
Cohesion: 0.04
Nodes (63): mock_player(), mock_player_service(), mp_regeneration_service(), asyncio, fixture, Unit tests for MP regeneration service. Tests the MPRegenerationService class…, Test process_tick_regeneration() accumulates fractional MP., Test _get_regen_multiplier() returns 1.0 for standing position. (+55 more)

### Community 237 - "ExceptionTracker"
Cohesion: 0.05
Nodes (43): ExceptionContextTrackInput, ExceptionRecord, ExceptionTracker, ExceptionTrackInput, get_exception_tracker(), Any, Exception, TypedDict (+35 more)

### Community 238 - "catalog_commands.py"
Cohesion: 0.09
Nodes (32): _append_admin_rows(), _append_catalog_footer(), _append_player_rows(), _as_catalog_request(), _CatalogApp, _CatalogAppState, _CatalogContainer, _CatalogPersistence (+24 more)

### Community 239 - "DeadLetterQueue"
Cohesion: 0.01
Nodes (236): DeadLetterMessage, DeadLetterQueue, Any, Path, Dead Letter Queue for failed NATS messages. Stores messages that fail after all…, Add failed message to dead letter queue (async version). Args: message: Dead…, Add failed message to dead letter queue (sync version). Args: message: Dead…, Retrieve and remove oldest message from DLQ (async version). Returns: Message… (+228 more)

### Community 240 - "UserManager"
Cohesion: 0.07
Nodes (32): UUID, Check if a player is globally muted by any other player. Args: player_id:…, Get information about who muted a player. Args: player_id: Player ID to check…, Add a player as an admin. Args: player_id: Player ID player_name: Player name…, Update cache to mark load as failed., Convert mute_info datetime and UUID objects to JSON-serializable formats., Save player mutes to data dictionary for JSON serialization., Save channel mutes to data dictionary for JSON serialization. (+24 more)

### Community 241 - "test_event_handler.py"
Cohesion: 0.05
Nodes (53): event_handler(), mock_connection_manager(), mock_event_bus(), mock_task_registry(), asyncio, fixture, Unit tests for event handler. Tests the event_handler module classes and…, Test RealTimeEventHandler subscribes to all events. (+45 more)

### Community 242 - "TargetMatch"
Cohesion: 0.02
Nodes (162): Resolve a typed target match for the given name in the current context., _MagicServiceCore, JsonMap, UUID, Load player and return normalized stats (MP/max_MP). Returns (player, stats) or…, Return (False, message) if not enough MP, else (True, '')., Return (False, message) if Mythos spell and not enough lucidity, else (True,…, Return (False, message) if player has not learned the spell, else (True, ''). (+154 more)

### Community 243 - "test_command_moderation.py"
Cohesion: 0.02
Nodes (140): AddAdminCommand, AdminCommand, MuteCommand, MuteGlobalCommand, MutesCommand, field_validator, Moderation command models for MythosMUD. This module provides command models…, Command for showing current mute status. (+132 more)

### Community 244 - "NPCMovementIntegration"
Cohesion: 0.05
Nodes (46): Initialize the idle movement handler. Args: event_bus: Optional EventBus…, NPCMovementIntegration, Room, Get room objects and validate they exist. Args: npc_id: ID of the NPC…, Update room occupancy by removing NPC from source and adding to destination.…, Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…, Move an NPC to a different room with full integration. This method provides…, Get the current room ID for an NPC. Args: npc_id: ID of the NPC Returns:… (+38 more)

### Community 245 - "test_player_service_mutations.py"
Cohesion: 0.04
Nodes (67): _async_session_gen(), mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service mutations. Covers delete, location update, mythos…, Yield a single fake session -- mirrors get_async_session's shape for…, Test apply_corruption() applies corruption. (+59 more)

### Community 246 - "test_admin_commands_helpers.py"
Cohesion: 0.07
Nodes (49): broadcast_teleport_effects(), create_teleport_effect_message(), get_online_player_by_display_name(), notify_player_of_teleport(), Any, Teleport utility functions for admin commands in MythosMUD. This module…, Notify a player that they are being teleported by an admin. Args:…, Get online player information by display name. Args: display_name: Display name… (+41 more)

### Community 247 - "useGameClientV2Container.ts"
Cohesion: 0.09
Nodes (39): GameClientV2Container(), getEmptyOccupantsReportContextOrNull(), isWithinRoomOccupantsSettleGracePeriod(), runEmptyOccupantsReportIfNeeded(), tryGetRoomWithEmptyOccupantsList(), forceLogoutFallback(), performGameClientLogout(), stillShowingGameClient() (+31 more)

### Community 248 - "test_level_service.py"
Cohesion: 0.05
Nodes (56): level_from_total_xp(), Level and XP curve for MythosMUD. Placeholder implementation: XP required for…, Total XP required to reach a given level (cumulative). Level 1 requires 0 XP.…, XP required to go from (level - 1) to level. Args: level: Target level (2-based…, Compute character level from total experience points. Uses the same curve as…, total_xp_for_level(), xp_required_for_level(), UUID (+48 more)

### Community 249 - "NATSRetryHandler"
Cohesion: 0.04
Nodes (75): NATSRetryHandler, Any, Exception, Calculate exponential backoff delay with jitter. Args: attempt: Current attempt…, Determine if a message should be retried. Args: message: Message that failed…, Retry a function with exponential backoff. Args: func: Async function to retry…, Get retry statistics. Returns: Dictionary with retry metrics AI: For monitoring…, Retry async function with exponential backoff. Attempts the function up to… (+67 more)

### Community 250 - "LucidityService"
Cohesion: 0.02
Nodes (186): LucidityCooldown, LucidityExposureState, PlayerLucidity, Base, Lucidity tracking models drawn from the Pnakotic Manuscripts., Tracks repeated exposure to particular eldritch archetypes., Cooldown tracker for recovery rituals and hallucination timers., Authoritative lucidity state for a single investigator. (+178 more)

### Community 251 - "fixtures/auth.ts"
Cohesion: 0.06
Nodes (47): RoomSummary, STANDARD_DIRECTIONS, assertCommandChannelReady(), clickWithoutStability(), EnsurePlayableConnectionOptions, getLivePageForUsername(), isPageConnected(), isPageUsable() (+39 more)

### Community 252 - "TestCombatMessagingService"
Cohesion: 0.05
Nodes (34): CombatMessages, CombatMessagingService, Any, Generate combat start messages for all room occupants. Args: attacker_name:…, Generate combat end messages for all room occupants. Args: winner_name: Name of…, Generate thematic error messages for combat actions. Args: error_type: Type of…, Validate NPC message templates against the schema. Args: messages_data: NPC…, Service for generating combat messages. This service creates thematic,… (+26 more)

### Community 253 - "MonitoringDashboard"
Cohesion: 0.06
Nodes (40): PerformanceStats, Alert, MonitoringDashboard, Any, Get overall system health status. Returns: Current system health status, Get comprehensive monitoring summary. Returns: Complete monitoring summary with…, Evaluate thresholds and record new alerts., Record a custom alert emitted by subsystems. Args: alert_type: Identifier for… (+32 more)

### Community 254 - "TauntCommandHandler"
Cohesion: 0.05
Nodes (49): _apply_taunt_and_maybe_broadcast(), AppWithState, Protocol, UUID, Validate taunt preconditions and resolve combat/NPC. Returns error dict or…, Validate and resolve target name from command_data. Returns error dict or…, Apply taunt and broadcast target switch if aggro changed. Returns error dict or…, Handle taunt command: draw NPC aggro (ADR-016). Room-local only. (+41 more)

### Community 255 - "test_container_persistence_async_helpers.py"
Cohesion: 0.08
Nodes (60): Validate lock_state parameter. Args: lock_state: Lock state to validate Raises:…, validate_lock_state(), _build_item_dict(), _call_create_container_procedure(), _container_data_from_row(), create_container_async(), delete_container_async(), fetch_container_items_async() (+52 more)

### Community 256 - "test_inventory_display_helpers.py"
Cohesion: 0.07
Nodes (48): build_container_metadata(), build_equipped_lines(), build_inventory_lines(), filter_non_equipped_inventory(), format_metadata(), get_equipped_item_identifiers(), Any, Display and rendering helpers for inventory commands. (+40 more)

### Community 257 - "websocket_handler.py"
Cohesion: 0.01
Nodes (235): JSONResponse, ErrorResponseDetailsInput, post, Request, Receive and log alert webhooks, webhook(), Item catalog API: GET /v1/api/item-catalog, Pydantic error handler for consistent error processing. This module provides a… (+227 more)

### Community 258 - "test_active_lucidity_service.py"
Cohesion: 0.05
Nodes (59): active_lucidity_service(), mock_session(), asyncio, fixture, Unit tests for active lucidity service. Tests the ActiveLucidityService class…, Test apply_encounter_lucidity_loss() for acclimated encounter., Test apply_encounter_lucidity_loss() raises error for unknown category., Test apply_encounter_lucidity_loss() handles string player_id. (+51 more)

### Community 259 - "InstanceManager"
Cohesion: 0.05
Nodes (44): Wire exploration, movement, follow, and party services., Instance, InstanceManager, Room, UUID, Return template rooms matching instance_template_id., Clone template rooms into instance-scoped rooms with remapped exits., Extract stable_id from room - use room.id if it looks like a full path. (+36 more)

### Community 260 - "collect_inventory.py"
Cohesion: 0.08
Nodes (43): _apply_holdings(), collect_player_stacks(), _consume_from_equipped(), _consume_from_stack_list(), consume_prototype_from_player(), count_prototype_in_stacks(), _deepcopy_dict_stacks(), _deepcopy_equipped_map() (+35 more)

### Community 261 - "GameTickService"
Cohesion: 0.05
Nodes (32): GameTickService, Get the current tick count. Returns: int: Current number of ticks processed, Reset the tick count to zero., Get the current tick interval. Returns: float: Current tick interval in seconds, Set a new tick interval. Args: interval: New tick interval in seconds, Check if the service is currently running. Returns: bool: True if running,…, Service that manages the game tick system. The game tick system runs at regular…, Initialize the GameTickService. Args: event_publisher: EventPublisher instance… (+24 more)

### Community 262 - "devDependencies"
Cohesion: 0.05
Nodes (39): autoprefixer, devDependencies, autoprefixer, cross-env, eslint-plugin-jsx-a11y, eslint-plugin-playwright, eslint-plugin-react-hooks, eslint-plugin-react-refresh (+31 more)

### Community 263 - "gen_arena_migration_sql.py"
Cohesion: 0.06
Nodes (55): all_room_rows(), gen_room_link_id(), gen_room_links(), gen_room_row(), gen_subzone_row(), gen_zone_config_row(), gen_zone_row(), main() (+47 more)

### Community 264 - ".state"
Cohesion: 0.05
Nodes (38): NPCCombatIntegrationBase, ABC, Exception, UUID, ValidationError, Base segment of NPC combat integration (damage, effects, attack orchestration).…, Apply combat effects to a target (player or NPC). Args: target_id: ID of the…, Convert target_id to UUID, accepting either string or UUID input. (+30 more)

### Community 265 - "useMythosAppActions.ts"
Cohesion: 0.14
Nodes (26): postSelectCharacter(), runAfterCharacterCreatedFlow(), refreshCharactersAfterCreation(), executeDeleteCharacterUi(), isGracePeriodServerUnavailableError(), tryStartLoginGracePeriod(), runSelectCharacterFlow(), selectCharacterNetworkErrorMessage() (+18 more)

### Community 266 - "test_combat_service.py"
Cohesion: 0.07
Nodes (57): _make_combat_instance(), _make_participant(), _make_service(), asyncio, Unit tests for CombatService process_attack flow and private helper methods., When involuntary flee triggers, combat ends and an early CombatResult is…, finalize_attack_result wires target state, events, XP, and completion correctly., process_attack returns early CombatResult when melee validation ends combat. (+49 more)

### Community 267 - "get_username_from_user"
Cohesion: 0.04
Nodes (72): Unit tests for command_helpers utility functions. Tests the utility functions…, Test validate_command_safety() returns True for safe commands., Test validate_command_safety() returns False for shell metacharacters., Test validate_command_safety() returns False for SQL injection attempts., Test validate_command_safety() returns False for Python injection attempts., Test validate_command_safety() returns False for format string injection., Test validate_command_safety() returns False for XSS attempts., Test get_command_help() returns help for specific command. (+64 more)

### Community 268 - "test_command_processor.py"
Cohesion: 0.03
Nodes (70): command_processor(), fixture, Unit tests for command processor. Tests the CommandProcessor class which…, Test process_command_string handles KeyError., Test process_command_string handles RuntimeError., Test _extract_attributes extracts attributes correctly., Test _extract_attributes handles missing attributes., Test _is_combat_command returns True for attack command. (+62 more)

### Community 269 - "NPCLifecycleManager"
Cohesion: 0.02
Nodes (119): NPCDied, NPCLeftRoom, Event fired when an NPC leaves a room. This event is triggered when an NPC…, Event fired when an NPC dies. This event is triggered when an NPC's…, Event requesting that room occupants be broadcast to clients. Used after NPC…, RoomOccupantsRefreshRequested, handle_npc_died_impl(), _LifecycleManagerForDeath (+111 more)

### Community 270 - "get_item_catalog"
Cohesion: 0.11
Nodes (22): ge, le, Query, get_item_catalog(), Depends, get, Request, Return a paginated item prototype catalog with role-based columns. (+14 more)

### Community 271 - "_prepare_command_for_processing"
Cohesion: 0.04
Nodes (45): clean_command_input(), _is_predefined_emote(), normalize_command(), CommandExecutionRequest, Command Input Utilities for MythosMUD. This module provides utilities for…, Clean and normalize command input by collapsing multiple spaces and stripping…, Normalize command input by removing optional slash prefix. Supports both…, Check if a command is a predefined emote alias. Args: command: The command to… (+37 more)

### Community 272 - "test_rate_overrides.py"
Cohesion: 0.05
Nodes (71): get_asyncpg_server_settings_for_database_url(), Build asyncpg ``server_settings`` so unqualified table names resolve like…, _async_load_lucidity_rate_overrides(), build_override_key(), extract_lucidity_rate(), load_lucidity_rate_overrides(), _LucidityRateLoadResult, _normalize_database_url() (+63 more)

### Community 273 - "send_game_event"
Cohesion: 0.06
Nodes (56): broadcast_game_event(), _ConnectionManagerAPI, Protocol, UUID, Public API utility functions for connection manager. This module provides…, Send a room event to all players in a specific room. Args: room_id: The room's…, Send a system notification to a player. Args: player_id: The player's ID…, Send a player status update to a player. Args: player_id: The player's ID… (+48 more)

### Community 274 - "PlayerGuidFormatter"
Cohesion: 0.05
Nodes (51): PlayerGuidFormatter, Player GUID Formatter for MythosMUD logging system. This module provides a…, Determine if a GUID is likely to be a player ID based on context. Args: guid:…, Get player name for GUID from in-memory data. Args: guid: The player GUID to…, Custom formatter that converts player GUIDs to "<name>: <GUID>" format. This…, Initialize the PlayerGuidFormatter. Args: player_service: Service for accessing…, Convert player GUIDs in message to enhanced format. Args: message: The log…, formatter() (+43 more)

### Community 275 - "projectorRoom.ts"
Cohesion: 0.08
Nodes (50): formatNpcAttackedLine(), formatNpcTookDamageLine(), formatPlayerAttackedLine(), mergePlayerDpFromPlayerAttackedPayload(), messageHandlers, appendPostureGameInfoMessage(), mergePostureMessageIntoState(), mergeRespawnedPlayer() (+42 more)

### Community 276 - "test_command_validator.py"
Cohesion: 0.06
Nodes (48): Unit tests for command validator., Test validate_command_length returns True for valid length., Test validate_command_length returns False for too long command., Test validate_command_length with custom max_length., Test validate_command_format returns True for valid command., Test validate_command_format returns False for empty command., Test validate_command_format returns False for suspicious command., Test validate_command_format returns False for too long command. (+40 more)

### Community 277 - "RoomService"
Cohesion: 0.07
Nodes (24): Any, AsyncSession, UUID, Get a list of rooms adjacent to the specified room. Args: room_id: The room's…, Get the scope of rooms for local chat (current room + adjacent rooms). Args:…, Validate that a room exists using cached data. Args: room_id: The room's ID…, Validate that there's a valid exit from one room to another. Args:…, Get all occupants (players and NPCs) currently in a room using cached data.… (+16 more)

### Community 278 - "GameStateProvider"
Cohesion: 0.06
Nodes (45): GameStateProvider, Any, Player, UUID, Get NPC names for multiple NPCs in a batch operation. Args: npc_ids: List of…, Get player name and add grace period indicators if applicable., Convert player UUIDs to names in room_data., Convert player UUIDs and NPC IDs in room_data to names. CRITICAL: NEVER send… (+37 more)

### Community 279 - "player_event_handlers_respawn_room.py"
Cohesion: 0.09
Nodes (42): convert_npc_ids_to_names(), enrich_room_data_with_occupant_names(), extract_occupant_names(), get_npc_name_from_lifecycle_manager(), merge_player_lists(), prepare_room_data_for_respawn(), BoundLogger, Protocol (+34 more)

### Community 280 - "combat_turn_participant_actions.py"
Cohesion: 0.04
Nodes (68): armor_points_from_base_stats(), _damage_from_attack(), _first_attack(), _legacy_behavior_damage(), Random, Resolve NPC outgoing attack damage from base_stats / behavior (ADR-027 Phase 3)., Return damage from one attack entry, or None if it has no usable fields., Roll NPC damage: damage_expr if present, else min/max ints, else behavior, else… (+60 more)

### Community 281 - "test_windows_safe_rotation.py"
Cohesion: 0.05
Nodes (51): _copy_then_truncate(), RotatingFileHandler, Windows-safe log rotation handlers. These handlers avoid rename-while-open…, Timed rotating file handler that uses copy-then-truncate on Windows., Copy the source file to destination, then truncate the source file. This avoids…, Copy the source log file to the destination, then truncate the source. Public…, Size-based rotating file handler that uses copy-then-truncate on Windows., WindowsSafeRotatingFileHandler (+43 more)

### Community 282 - "test_movement_monitor.py"
Cohesion: 0.03
Nodes (60): Reset the global movement monitor (useful for testing)., reset_movement_monitor(), movement_monitor(), fixture, Unit tests for movement monitor. Tests the MovementMonitor class for monitoring…, Test record_integrity_check() records check without violation., Test record_integrity_check() records check with violation., Test validate_room_integrity() with valid room data. (+52 more)

### Community 283 - "MemoryMonitor"
Cohesion: 0.07
Nodes (16): ExtendedPerformance, MemoryLeakDetector, MemoryLeakDetectorOptions, MemorySnapshot, PerformanceMemory, useMemoryLeakDetector(), MemoryMonitor, MemoryMonitorOptions (+8 more)

### Community 284 - "map_minimap.py"
Cohesion: 0.07
Nodes (41): _append_room_with_fallback_coords_if_needed(), _apply_minimap_fallback_coordinates(), _ensure_current_room_in_minimap_rooms(), generate_minimap_html(), Any, AsyncSession, UUID, Minimap orchestration for the map API. Extracted from maps.py so the router… (+33 more)

### Community 285 - "NATSMessageSubscriptionMixin"
Cohesion: 0.05
Nodes (29): NATSMessageSubscriptionMixin, Any, Unsubscribe from local channel messages for a specific sub-zone. Args: subzone:…, Track a player's sub-zone subscription for local channels. Args: player_id:…, Mixin: room, subzone, and event NATS subscription lifecycle., Get list of players currently in a specific sub-zone. Args: subzone: Sub-zone…, Handle player movement between rooms and update sub-zone subscriptions. Args:…, Subscribe to chat messages for a specific room. Args: room_id: Room ID to… (+21 more)

### Community 286 - "websocket_handler_commands.py"
Cohesion: 0.02
Nodes (142): HTTP Request or WebSocketRequestContext for unified command processing., create_websocket_request_context(), Any, Request context factory for WebSocket command processing. This module provides…, Get the event bus from the request context., Factory function to create a WebSocket request context. Args: app_state: Real…, Creates FastAPI Request-like objects for WebSocket commands. This allows…, Initialize the WebSocket request context. Args: app_state: Real application… (+134 more)

### Community 287 - "test_nats_messages.py"
Cohesion: 0.06
Nodes (50): BaseMessageSchema, ChatMessageSchema, EventMessageSchema, Any, BaseModel, field_validator, Pydantic schemas for NATS message validation. This module provides type-safe…, Validate event type is not empty. (+42 more)

### Community 288 - "NPCCombatLucidity"
Cohesion: 0.06
Nodes (33): ActiveLucidityService, Handle active lucidity adjustments such as encounters and recovery actions., Return lucidity dependency for integration collaborators., _EncounterCtx, NPCCombatLucidity, Any, NamedTuple, Apply lucidity loss when a player engages an eldritch entity. Args: player_id:… (+25 more)

### Community 289 - "test_chat_logger.py"
Cohesion: 0.04
Nodes (43): Initialize chat service. Args: persistence: Database persistence layer…, ChatWhisperTracker, Chat whisper tracking utilities. This module provides whisper tracking…, Tracks last whisper senders for reply functionality., Initialize the whisper tracker., Store the last whisper sender for a player. Args: receiver_name: Name of the…, Get the last whisper sender for a player. Args: player_name: Name of the player…, Clear the last whisper sender for a player. Args: player_name: Name of the… (+35 more)

### Community 290 - "test_player_respawn_api.py"
Cohesion: 0.10
Nodes (40): _handle_delirium_respawn_validation_error(), _handle_respawn_validation_error(), Any, post, Request, ValidationError, Respawn a delirious player at the Sanitarium with restored lucidity. This…, Respawn a dead player at their respawn location with full DP. This endpoint… (+32 more)

### Community 291 - "ResourceManager"
Cohesion: 0.05
Nodes (19): trackComponentMount, trackComponentUnmount, trackStoreSubscription, trackStoreUnsubscription, useComponentLifecycleTracking(), UseComponentLifecycleTrackingOptions, useStoreSubscriptionTracking(), ClientMetrics (+11 more)

### Community 292 - "DialogueDefinitionRepository"
Cohesion: 0.09
Nodes (35): DialogueDefinition, Base, NPC dialogue tree template: id (PK), definition JSONB, optional npc link., _as_dialogue_row(), _definition_dict(), DialogueDefinitionRepository, _DialogueRow, Protocol (+27 more)

### Community 293 - "testing_examples.py"
Cohesion: 0.04
Nodes (51): async_operation(), client, database, LoggingMiddleware, process_batch(), process_item(), asyncio, Test WebSocket logging in integration tests. (+43 more)

### Community 294 - "test_party_commands.py"
Cohesion: 0.08
Nodes (50): _get_container(), _get_member_display(), _get_party_command_context(), _handle_party_chat(), handle_party_command(), _handle_party_invite(), _handle_party_kick(), _handle_party_leave() (+42 more)

### Community 295 - "StatusEffect"
Cohesion: 0.04
Nodes (71): InventoryItem, Player, BaseModel, Represents a status effect applied to a character., Represents an item in a player's inventory., Pydantic Player model for game logic and validation. This is separate from the…, Add an item to the player's inventory. Args: item_id: Unique identifier for the…, Remove an item from the player's inventory. Args: item_id: Unique identifier… (+63 more)

### Community 296 - "test_npc_combat_handlers.py"
Cohesion: 0.06
Nodes (42): CombatResultCtx, Bundle for handle_combat_result (lizard PARAM)., Handle combat result, broadcast, and NPC death., mock_combat_memory(), mock_combat_result(), mock_data_provider(), mock_lifecycle(), mock_messaging_integration() (+34 more)

### Community 297 - "test_room_subscription_manager.py"
Cohesion: 0.04
Nodes (53): asyncio, fixture, Unit tests for room subscription manager. Tests the RoomSubscriptionManager…, Test get_room_subscribers() returns empty set when no subscribers., Test get_room_subscribers() handles errors gracefully., Test add_room_occupant() adds occupant., Test add_room_occupant() with multiple occupants., Test add_room_occupant() adds occupant to new room. (+45 more)

### Community 298 - "rescue_commands.py"
Cohesion: 0.06
Nodes (63): _apply_grounding_adjustment(), _complete_ground_command(), _get_ground_services(), handle_ground_command(), handle_rescue_command(), _normalize_player_ids(), Any, UUID (+55 more)

### Community 299 - "Any"
Cohesion: 0.06
Nodes (21): Any, Retrieve current room drops as a defensive copy for callers. Args: room_id: The…, Append an item stack to the room drop ledger. Args: room_id: The room receiving…, Remove quantity of a drop entry, returning the removed stack. Args: room_id:…, Adjust quantity for an existing drop entry; removing entry when zero. Args:…, Add a player as an occupant of a room. Args: player_id: The player's ID…, Remove a player as an occupant of a room. Args: player_id: The player's ID…, Get online player occupants from room_occupants and room_subscriptions. Uses… (+13 more)

### Community 300 - "✅ Phase 2 Async Persistence Migration - COMPLETE"
Cohesion: 0.04
Nodes (53): 1. Eliminated Event Loop Blocking, 2. Consistent Async Patterns, 3. Proper Error Handling, 4. Resource Management, 5. Performance Optimization, 🏆 Achievement Summary, Additional Files Updated, Adjusts spectacles with profound satisfaction (+45 more)

### Community 301 - "MythosMUD Test Suite Modernization Plan"
Cohesion: 0.04
Nodes (53): Alternative: **GREENFIELD REWRITE**, Appendices, Appendix A: Test File Inventory, Appendix B: Direct app.state Access Locations, Appendix C: Fixture Audit, Backward Compatibility Strategy, Cons, Consolidation Opportunities (+45 more)

### Community 302 - "test_magic_service.py"
Cohesion: 0.06
Nodes (63): CastingState, CastingStateManager, Any, UUID, Casting state manager for tracking active spell castings. This module manages…, Check if a player is currently casting. Args: player_id: Player ID to check…, Get the casting state for a player. Args: player_id: Player ID Returns:…, Complete and remove a casting state. Args: player_id: Player ID Returns:… (+55 more)

### Community 303 - "test_admin_summon_command.py"
Cohesion: 0.08
Nodes (50): _broadcast_and_log_summon_success(), _complete_summon(), _create_summon_item_instance(), handle_summon_command(), _log_summon_success(), _parse_summon_command_data(), _persist_summoned_item(), Any (+42 more)

### Community 304 - "test_command_magic.py"
Cohesion: 0.05
Nodes (57): CastCommand, LearnCommand, field_validator, Magic command models for MythosMUD. This module provides command models for…, Command for casting a spell., Validate spell name format., Validate target format., Command for viewing spell details. (+49 more)

### Community 305 - "npc_config_parsing.py"
Cohesion: 0.06
Nodes (30): Get attribute from obj with default to avoid lazy-loading issues., Set npc_type, name, current_room, spawn_room_id from definition., Setup base behavior rules common to all NPCs., Return stats[key] as int, or default if missing/None., Return current_dp, max_dp, dexterity for CombatParticipantData., Heal and update determination points (DP)., Write new_dp to determination_points and dp for backward compatibility., Initialize the NPC base class. (+22 more)

### Community 306 - "AdminActionsLogger"
Cohesion: 0.07
Nodes (41): Admin permission validation utilities for MythosMUD. This module provides…, AdminActionsLogger, get_admin_actions_logger(), Any, datetime, Path, TypedDict, Admin actions logger for MythosMUD. This module provides comprehensive logging… (+33 more)

### Community 307 - "CharacterNameScreen.tsx"
Cohesion: 0.09
Nodes (35): buildCreateCharacterPayload(), CharacterNameScreen(), getCreateCharacterErrorMessage(), OccupationSlotPayload, PersonalInterestPayload, SkillsPayload, loadSkillsCatalog(), MIN_TOUCH_TARGET_STYLE (+27 more)

### Community 308 - "alias_schema.json"
Cohesion: 0.07
Nodes (27): command, version, additionalProperties, additionalProperties, description, required, type, description (+19 more)

### Community 309 - "get_cached_player"
Cohesion: 0.13
Nodes (23): Unit tests for player_cache utilities. Tests the player caching functions for…, Test get_cached_player() returns None when no cache exists., Test cache_player() and get_cached_player() operations., Test get_cached_player() returns None for nonexistent key., Test cache_player() can cache multiple players., Test cache_player() overwrites existing entries., Test get_cached_player() handles missing state., Test cache_player() handles missing state gracefully. (+15 more)

### Community 310 - "EmoteService"
Cohesion: 0.08
Nodes (28): EmoteDefinition, EmoteService, TypedDict, Check if a command is an emote alias. Args: command: The command to check…, Get the emote definition for a command. Args: command: The command (emote name…, Format emote messages for the player and room occupants. Args: command: The…, Get a list of all available emotes and their aliases. Returns: Dict mapping…, Reload predefined emote definitions from the database. (+20 more)

### Community 311 - "websocket_helpers.py"
Cohesion: 0.02
Nodes (137): _accumulate_valid_occupant_name(), _AppStateForPlayerService, build_basic_player_data(), check_shutdown_and_reject(), convert_schema_to_dict(), convert_uuids_to_strings(), _ensure_player_in_room_occupancy(), _fetch_room_for_tracked_player() (+129 more)

### Community 312 - "TestRoomDataFixer"
Cohesion: 0.06
Nodes (29): Any, Applies automatic fixes to room data when validation issues are detected., Fix missing name field., Fix missing description field., Fix occupant count mismatch., Fix missing timestamp field., Count the number of fixes that were applied., Apply automatic fixes to room data when possible. Args: room_data: Room data to… (+21 more)

### Community 313 - "connection_cleanup_methods.py"
Cohesion: 0.08
Nodes (33): check_and_cleanup_impl(), cleanup_dead_connections_impl(), cleanup_ghost_players_impl(), cleanup_orphaned_data_impl(), force_cleanup_impl(), prune_stale_players_impl(), Any, UUID (+25 more)

### Community 314 - "AliasGraph"
Cohesion: 0.08
Nodes (23): Unit tests for alias_graph utilities. Tests the AliasGraph class., Test AliasGraph initialization., Test AliasGraph.build_graph() builds dependency graph., Test AliasGraph.detect_cycle() returns None when no cycle., Test AliasGraph.is_safe_to_expand() returns True when safe., Test AliasGraph.get_expansion_depth() returns depth., Test AliasGraph.clear() clears the graph., test_alias_graph_build_graph() (+15 more)

### Community 315 - "test_validation.py"
Cohesion: 0.03
Nodes (64): custom_length_validator(), fixture, Unit tests for NATS Subject Validator. Tests the SubjectValidator class., Test validate_subject_components() returns False for invalid characters., Test validate_subject_components() returns False for empty component., Test validate_subject_components() allows numbers., Test validate_subject_components() allows hyphens., Test validate_parameter_value() passes for valid parameter. (+56 more)

### Community 316 - "handle_read_command"
Cohesion: 0.07
Nodes (49): _find_item_in_inventory(), _format_learn_spell_message(), handle_read_command(), _learn_single_spell(), _learn_specific_spell(), _list_spells_in_book(), _process_spellbook_read(), Any (+41 more)

### Community 317 - "event_types.py"
Cohesion: 0.01
Nodes (197): _default_timestamp(), NPCAttacked, NPCListened, NPCSpoke, NPCTookDamage, ObjectAddedToRoom, ObjectRemovedFromRoom, PlayerEnteredRoom (+189 more)

### Community 318 - "retry.py"
Cohesion: 0.07
Nodes (42): asyncio, Unit tests for retry utilities. Tests the retry decorator and retry logic., Test retry_with_backoff() with async function succeeds on first attempt., Test is_transient_error() identifies transient errors., Test retry_with_backoff() with async function retries on failure then succeeds., Test is_transient_error() returns False for non-transient errors., DatabaseError wrapping asyncpg closed-connection must still retry (e2e…, __cause__ ConnectionDoesNotExistError makes the outer wrapper transient. (+34 more)

### Community 319 - "debrief_command.py"
Cohesion: 0.08
Nodes (48): _check_debrief_availability(), _complete_debrief(), _generate_narrative_recap(), _get_catatonia_registry_from_app(), _get_persistence_from_app(), handle_debrief_command(), _perform_therapy_if_requested(), Any (+40 more)

### Community 320 - "passive_lucidity_flux/service.py"
Cohesion: 0.06
Nodes (45): FluxServiceConfig, lookup_profile(), normalize_environment_config(), period_label(), Any, datetime, Configuration and normalization for passive lucidity flux., Optional configuration for PassiveLucidityFluxService. All fields have defaults. (+37 more)

### Community 321 - "test_pattern_matcher.py"
Cohesion: 0.05
Nodes (44): Initialize NATS Subject Manager. Args: enable_cache: Enable validation result…, PatternMatcher, Any, Pattern matching utilities for NATS Subject Manager. This module provides…, Matcher for validating subjects against registered patterns., Initialize pattern matcher. Args: strict_validation: Enable strict validation…, Check if subject matches any registered pattern. Args: subject: Subject string…, Check if subject components match a pattern. Args: components: Subject… (+36 more)

### Community 322 - "should_spawn_npc"
Cohesion: 0.08
Nodes (37): _population_allows_spawn(), Any, Spawn Validator Module. This module provides logic for validating whether NPCs…, Determine if an NPC should spawn based on conditions. Args: definition: NPC…, Return False when zone population blocks this NPC definition., Evaluate one spawn rule; return True when probability roll succeeds., Return True when any spawn rule passes probability checks., should_spawn_npc() (+29 more)

### Community 323 - "test_combat_persistence_handler_persistence.py"
Cohesion: 0.07
Nodes (38): mock_combat_service(), mock_player(), persistence_handler(), asyncio, fixture, Unit tests for combat persistence handler - persistence operations. Tests…, Test _persist_player_dp_sync calls _verify_player_save., Test _persist_player_dp_sync handles save_player error. (+30 more)

### Community 324 - "CoordinateGenerator"
Cohesion: 0.06
Nodes (26): Select, CoordinateGenerator, Any, AsyncSession, Load rooms and their exits from database. Args: plane: Plane name zone: Zone…, Find the origin room (map_origin_zone=true, or first room)., Build adjacency list from room exits., Assign coordinates using BFS starting from origin. (+18 more)

### Community 325 - "command_guards.py"
Cohesion: 0.04
Nodes (62): command_request_app_state(), CommandExecutionRequest, Return app.state for HTTP Request or WebSocketRequestContext (duck-typed).…, _AppStateCommandGuards, _CastingStateManagerView, _CastingStateView, check_casting_state(), check_grace_period_block() (+54 more)

### Community 326 - "combat_attack.py"
Cohesion: 0.07
Nodes (47): _execute_combat_action(), _execute_phantom_combat_action(), _get_combat_action_context(), Any, Attack command flow: validation and execution. Extracted from combat.py to…, Resolve damage from equipped weapon or fall back to config unarmed damage., Execute combat action using the proper combat service., Execute an attack against a phantom hostile (#625). Deliberately bypasses… (+39 more)

### Community 327 - "command_handler_unified.py"
Cohesion: 0.04
Nodes (77): check_alias_safety(), handle_expanded_command(), Any, CommandExecutionRequest, Alias Expansion Logic for MythosMUD. This module handles alias resolution,…, Handle command processing with alias expansion and loop detection. This…, Check if an alias is safe to expand. Builds an alias dependency graph and…, Validate an expanded command for length and content. Args: expanded_command:… (+69 more)

### Community 328 - "App.tsx"
Cohesion: 0.11
Nodes (25): App(), fetchSpy, fetchSpy, TODO: Convert these to Playwright E2E tests in client/tests/, NOTE: These integration tests are currently skipped because they test full, createMockJsonResponse(), createMockProfessionsFetchResponse(), mockFetchForAuthAndProfessions() (+17 more)

### Community 329 - "migrate_combat_data.py"
Cohesion: 0.12
Nodes (30): main(), migrate_npc_combat_data(), _migrate_one_npc(), _MigrationArgs, MigrationResults, _npc_has_combat_data(), _npc_has_full_combat_data(), _omit_keys() (+22 more)

### Community 330 - "mock_app"
Cohesion: 0.29
Nodes (7): mock_app(), mock_container(), mock_player(), fixture, Create a mock FastAPI app., Create a mock ApplicationContainer., Create a mock player.

### Community 331 - "talk_command.py"
Cohesion: 0.05
Nodes (69): _emit_prompt(), handle_talk_command(), UUID, talk / talk <n> command for NPC dialogue trees (#583)., Handle talk <npc> or talk <n> against same-room NPCs., Extract player UUID from player model., Join talk args into a single remainder string., Send personal system message for a node; return short command result. (+61 more)

### Community 332 - "test_npc_threading_messages.py"
Cohesion: 0.06
Nodes (33): NPCMessageQueue, Thread-safe message queue for NPC actions. This queue handles pending actions…, Initialize the NPC message queue. Args: max_messages_per_npc: Maximum number of…, Add a message to an NPC's pending message queue. Args: npc_id: The NPC's ID…, Get all pending messages for an NPC. Args: npc_id: The NPC's ID Returns: List…, Clear all pending messages for an NPC. Args: npc_id: The NPC's ID Returns:…, Get the number of pending messages for an NPC., Get the total number of pending messages across all NPCs. (+25 more)

### Community 333 - "ConnectionCleaner"
Cohesion: 0.03
Nodes (71): ConnectionCleaner, Any, UUID, Identify players whose last_seen timestamp exceeds the max age. Args:…, Remove all data for a stale player. Args: pid: Player ID to remove…, Remove players whose presence is stale beyond the threshold. Args: last_seen:…, Return connection IDs that exceed max_connection_age., Extract player_id from connection metadata if present. (+63 more)

### Community 334 - "test_player_occupant_processor.py"
Cohesion: 0.04
Nodes (59): PlayerOccupantProcessor, Any, UUID, Player occupant processing utilities. This module handles querying and…, Process players and convert to occupant information. Args: room_id: The room ID…, Processes player occupants for rooms., Initialize player occupant processor. Args: connection_manager:…, Ensure a player is included in the player ID strings list if specified. Args:… (+51 more)

### Community 335 - "verify_enhanced_logging_compliance.py"
Cohesion: 0.07
Nodes (39): Assign, _check_all_files(), check_file(), _find_python_files(), _group_violations_by_type(), LoggingComplianceChecker, main(), _print_compliance_success() (+31 more)

### Community 336 - "CombatPersistenceHandler"
Cohesion: 0.05
Nodes (38): CombatPersistenceHandler, Any, UUID, Synchronously persist player DP to database. This is the actual persistence…, Persist player DP to database in background (fire-and-forget). This method runs…, Handles combat-related persistence operations., Initialize the persistence handler. Args: combat_service: Reference to the…, Persist player DP to database in background (fire-and-forget). Public API… (+30 more)

### Community 337 - "quality_fragmentation_lizard.py"
Cohesion: 0.12
Nodes (43): check_ai_guardrails(), build_context(), ChangedFile, _git_executable(), git_show_file(), GuardContext, is_code_file(), is_safe_git_ref() (+35 more)

### Community 338 - "_str_id"
Cohesion: 0.11
Nodes (19): Any, ConnectionManager, UUID, Create a new party with the given player as leader. Returns dict with success…, Disband a party. If by_player_id is given, only the leader may disband. If…, Add a player to a party. Fails if party does not exist or player is already in…, Safely schedule an async notification, handling cases where no event loop is…, Notify a player they have been removed from a party. Resolves leader name. (+11 more)

### Community 339 - "NPCCombatUUIDMapping"
Cohesion: 0.05
Nodes (34): Return UUID mapping dependency for integration collaborators., NPCCombatUUIDMapping, UUID, Get the original string ID from a UUID. Args: uuid_id: The UUID to look up…, Get XP value for a UUID. Args: uuid_id: The UUID to look up Returns: XP value…, Manages UUID mappings for NPC combat., Initialize UUID mapping storage., Check if a string is a valid UUID. Args: uuid_string: String to check Returns:… (+26 more)

### Community 340 - "test_shopkeeper_npc.py"
Cohesion: 0.14
Nodes (24): Coerce inventory quantity from JSON-shaped dict values to int (excludes bool)., _shop_quantity(), Unit tests for ShopkeeperNPC buy/sell helpers., _shopkeeper(), test_add_buyable_item(), test_add_buyable_item_invalid(), test_add_shop_item_and_inventory(), test_add_shop_item_invalid_item() (+16 more)

### Community 341 - "ContainerRepository"
Cohesion: 0.08
Nodes (38): ContainerCreateParams, Shared parameters for container creation (sync DB and async repository paths)., Optional fields for creating a container row (beyond source_type)., ContainerDataCore, Identity and placement fields for a container row., _container_data_to_dict(), ContainerRepository, Any (+30 more)

### Community 342 - "test_audit_logger.py"
Cohesion: 0.07
Nodes (35): _logger(), Path, Unit tests for audit_logger utilities. Tests the AuditLogger class., Test AuditLogger initialization., Test AuditLogger.log_command() logs command execution., Test AuditLogger.log_permission_change() logs permission change., Test AuditLogger.log_player_action() logs player action., Test AuditLogger.get_recent_entries() retrieves recent entries. (+27 more)

### Community 343 - "Uplift Strategy"
Cohesion: 0.04
Nodes (46): 0.1 Create Container Test Fixtures ✅, 0.2 Update conftest.py ✅, 1.1 Identify All Failing Tests ✅, 1.2 Fix Integration Test Fixtures ✅ **INFRASTRUCTURE COMPLETE**, 2.1 Categorize Unit Tests by Dependency Pattern, 2.2 Update Category B: Service Layer Tests, 2.3 Update Category C: Infrastructure Tests, 2.4 Update Category D: API Tests (+38 more)

### Community 344 - "Test Suite Optimization Roadmap"
Cohesion: 0.04
Nodes (46): After Month 1 (Pruning Phase), After Month 2 (Consolidation + Additions), After Month 3+ (Continuous Improvement), Guiding Principles, Implementation Timeline, Monitoring and Validation, Month 1: Pruning and Quick Wins, Month 2: Consolidation and Additions (+38 more)

### Community 345 - "Test Suite Refactoring Plan"
Cohesion: 0.04
Nodes (45): 1. Test Independence, 2. Mock Usage, 3. Assertion Quality, 4. Test Data Management, 5. Performance, 6-Week Timeline, Appendix A: Full File Mapping, Appendix B: Test Categories Reference (+37 more)

### Community 346 - "Test Value Distribution Chart"
Cohesion: 0.04
Nodes (46): After Each Phase, After Phase 1-3: Pruning (Month 1), After Phase 4: Consolidation (Month 2), After Phase 5: Gap Filling (Month 2), Appendix: Quick Reference Commands, Automatic Rollback If, Before Starting Optimization, Capture Baseline (+38 more)

### Community 347 - "catalog_dml.py"
Cohesion: 0.07
Nodes (48): _load_catalog(), _load_json(), main(), _object_dict(), Path, apply_weapon_dual_write(), _ensure_weapon_defaults(), _normalize_damage_expr() (+40 more)

### Community 348 - "_handle_admin_set_stat_command"
Cohesion: 0.07
Nodes (50): _handle_admin_set_stat_command(), Handle admin set <stat_name> <target_player> <value>., _assert_stat_write_path(), _async_session_gen(), asyncio, patch, Test handling when player service is not available., Test handling when persistence layer is not available. (+42 more)

### Community 349 - "TargetResolutionResult"
Cohesion: 0.05
Nodes (71): Resolve combat target using target resolution service. Public API., Validate target_result and resolve to a live NPC target_match., Resolve combat target using target resolution service., _get_container(), handle_follow_command(), handle_following_command(), handle_unfollow_command(), _load_follow_context() (+63 more)

### Community 350 - "test_chat_nats_publisher.py"
Cohesion: 0.08
Nodes (57): _build_legacy_subject(), _build_nats_message_data(), build_nats_subject(), _build_standardized_subject(), _chat_passes_nats_validation(), _extract_subzone_from_room(), _log_nats_publish_error(), _log_nats_unexpected_error() (+49 more)

### Community 351 - "fastapi_integration.py"
Cohesion: 0.05
Nodes (39): auth_service(), BackgroundTasks, create_player(), File, general_exception_handler(), get_player(), http_exception_handler(), list_players() (+31 more)

### Community 352 - "format_player_entry"
Cohesion: 0.06
Nodes (37): format_player_entry(), format_player_location(), Format player location as Zone: Sub-zone: Room from room ID. Args: room_id:…, Format a single player entry for the who command output. Args: player: Player…, Unit tests for who command helper functions. Tests the helper functions in…, Test filter_players_by_name() filters players by name., Test filter_players_by_name() returns empty list when no matches., Test filter_players_by_name() returns all players when filter is empty. (+29 more)

### Community 353 - "map/types.ts"
Cohesion: 0.11
Nodes (24): defaultReactFlowOptions, edgeTypes, getEdgeTypes(), getNodeTypes(), nodeTypes, ExitEdge, ExitEdgeBody(), ExitEdgeLabels() (+16 more)

### Community 354 - "test_rooms_api.py"
Cohesion: 0.08
Nodes (37): get_room(), list_rooms(), get, post, Validate authentication and admin permissions for room position update., Update room position in database and verify the update succeeded., List rooms filtered by plane, zone, and optionally sub_zone. Returns room data…, Request model for updating room map coordinates. (+29 more)

### Community 355 - "test_map_helpers.py"
Cohesion: 0.08
Nodes (36): build_room_dict(), build_zone_pattern(), load_room_exits(), load_rooms_with_coordinates(), load_single_room_with_coordinates(), Any, AsyncSession, Map API helpers: room loading and zone pattern utilities. Extracted from… (+28 more)

### Community 356 - "test_npc_spawn_rules_api.py"
Cohesion: 0.09
Nodes (35): NPCSpawnConditionsModel, NPCSpawnRuleCreate, NPCSpawnRuleResponse, BaseModel, Model for creating NPC spawn rules., Model for NPC spawn rule responses., Create response from ORM object., Model for NPC spawn conditions. (+27 more)

### Community 357 - "CharacterInfoPanel.tsx"
Cohesion: 0.08
Nodes (20): formatDelta(), HealthMeter, TIER_METADATA, TierMetadata, computeLucidityBar(), formatChange(), LucidityChangeFooter(), LucidityMeter (+12 more)

### Community 358 - "mock_container"
Cohesion: 0.40
Nodes (5): mock_connection_manager(), mock_container(), fixture, Create mock connection manager., Create mock container.

### Community 359 - "test_passive_corruption_flux_rate_overrides.py"
Cohesion: 0.09
Nodes (46): CorruptionOverride, A zone/subzone-level override for corruption flux rate and/or target (#815)., _async_load_corruption_overrides(), _CorruptionOverrideLoadResult, _extract_corruption_override(), load_corruption_overrides(), _normalize_database_url(), _parse_special_rules_from_raw() (+38 more)

### Community 360 - "vim Best Practices and Coding Standards"
Cohesion: 0.05
Nodes (43): 1.1 Directory Structure Best Practices for vim, 1.2 File Naming Conventions, 1.3 Module Organization Best Practices, 1.4 Component Architecture Recommendations, 1.5 Code Splitting Strategies, 1. Code Organization and Structure, 2.1 Design Patterns Specific to vim, 2.2 Recommended Approaches for Common Tasks (+35 more)

### Community 361 - "Async Code Review - Post Phase 2 Migration"
Cohesion: 0.04
Nodes (46): 1. Blocking the Event Loop?, 1. Consistent Pattern Application, 2. Missing `await` Keywords?, 2. Proper Async Propagation, 3. Exception Handling Preserved, 3. Using `asyncio.run()` in Library Code?, 4. Mixing Sync and Async Code Incorrectly?, 4. Resource Cleanup Maintained (+38 more)

### Community 362 - "FastAPI Code Review - Anti-Patterns and Best Practices"
Cohesion: 0.05
Nodes (44): FastAPI Code Review, 10. ℹ️ **Dependency Injection Pattern**, 11. ℹ️ **API Versioning** (OPTIONAL - NOT REQUIRED FOR WEBAPP), 1. ✅ **Inconsistent Response Models** - **RESOLVED**, 1. Response Models (Critical Issue #1) ✅, 2. Dependency Injection (Critical Issue #3) ✅, 2. 🟡 **Fat Endpoints with Business Logic** - **IN PROGRESS**, 3. ✅ **Direct app.state Access Instead of Dependency Injection** - **RESOLVED** (+36 more)

### Community 363 - "E2E Test Suite AI Execution Improvements - Summary"
Cohesion: 0.05
Nodes (43): AI Executor Role, Mandatory Execution Protocol, Pre-Execution Affirmation, Seven Commandments, Empty browser_evaluate Results Valid, Maximum 3 Attempts Per Step, 1. Updated Core Configuration, 1. Visual Emphasis (+35 more)

### Community 364 - "test_inventory_equip_command.py"
Cohesion: 0.13
Nodes (34): _equip_inventory_rollback_snapshot(), _equip_persist_or_rollback(), _equip_run_mutation(), _equip_success_payload(), _equip_target_slot_or_error(), _equip_try_inventory_swap(), EquipCommandInventoryStep, EquipCommandWork (+26 more)

### Community 365 - "test_room_utils.py"
Cohesion: 0.07
Nodes (40): Unit tests for room_utils. Tests utility functions for room operations., Test get_subzone_local_channel_subject() generates subject., Test get_subzone_local_channel_subject() returns None for invalid room ID., Test extract_subzone_from_room_id() extracts subzone., Test extract_subzone_from_room_id() extracts different subzone., Test extract_subzone_from_room_id() returns None for invalid format., Test get_zone_from_room_id() extracts zone., Test get_zone_from_room_id() extracts different zone. (+32 more)

### Community 366 - ".create_combat_instance"
Cohesion: 0.07
Nodes (23): _build_combat_instance(), _build_participant(), _compute_turn_order(), UUID, Build CombatInstance with turn interval in ticks (1 tick = 0.1s, so seconds *…, Build CombatParticipant from CombatParticipantData., Return participant IDs sorted by dexterity (highest first)., Create and initialize a combat instance. (+15 more)

### Community 367 - "test_player_service.py"
Cohesion: 0.06
Nodes (45): mock_persistence(), player_service(), asyncio, fixture, Unit tests for player service CRUD and lookup. Delete, location, mythos status,…, Test get_player_by_id() when player is not found., Test get_player_by_name() when player is found., Test get_player_by_name() when player is not found. (+37 more)

### Community 368 - "WearableContainerService"
Cohesion: 0.11
Nodes (21): _filter_container_data(), Any, UUID, Return existing equipment container ID for item instance if present., Create wearable container in persistence and return container_id payload., Handle equipping a wearable container item. Creates a container in PostgreSQL…, Handle unequipping a wearable container item. Preserves the container and its…, Get all wearable containers for a player. Args: player_id: UUID of the player… (+13 more)

### Community 369 - "get_room_environment"
Cohesion: 0.12
Nodes (14): Test get_room_environment() treats empty string as no environment., Test get_room_environment() function., Test get_room_environment() returns room-specific environment., Test get_room_environment() returns subzone environment when room doesn't have…, Test get_room_environment() returns zone environment when room and subzone…, Test get_room_environment() returns default 'outdoors' when no environment…, Test get_room_environment() prioritizes room environment over subzone and zone., Test get_room_environment() prioritizes subzone environment over zone. (+6 more)

### Community 370 - "TestHierarchicalSchema"
Cohesion: 0.06
Nodes (26): Any, Tests for hierarchical room schema validation. This module tests the new…, Test that invalid environment values fail validation., Test that a valid zone configuration passes validation., Test that invalid zone types fail validation., Test that a valid sub-zone configuration passes validation., Test that invalid sub-zone environment values fail validation., Test that valid room ID patterns pass validation. (+18 more)

### Community 371 - "RoomNodeData"
Cohesion: 0.09
Nodes (38): EdgeCreationModal(), EdgeCreationModalProps, EDGE_EXIT_FLAGS, EDGE_MODAL_MESSAGE_TONE_CLASSES, EdgeCreationModalView(), EdgeCreationModalViewProps, EdgeModalDirectionFieldsProps, EdgeModalValidationMessagesProps (+30 more)

### Community 372 - "messageHandlers.ts"
Cohesion: 0.08
Nodes (30): CHANNEL_TO_TYPE_MAP, handleChatMessage(), handleCommandResponse(), handleRoomMessage(), handleSystem(), resolveChatTypeFromChannel(), createMockAppendMessage(), createMockContext() (+22 more)

### Community 373 - "mythos_e2e.players"
Cohesion: 0.10
Nodes (22): mythos_e2e.account_sanctions, mythos_e2e.corruption_adjustment_log, mythos_e2e.corruption_cooldowns, mythos_e2e.id_map_players, mythos_e2e.invites, mythos_e2e.lucidity_adjustment_log, mythos_e2e.lucidity_cooldowns, mythos_e2e.lucidity_exposure_state (+14 more)

### Community 374 - "mythos_unit.players"
Cohesion: 0.10
Nodes (22): mythos_unit.account_sanctions, mythos_unit.corruption_adjustment_log, mythos_unit.corruption_cooldowns, mythos_unit.id_map_players, mythos_unit.invites, mythos_unit.lucidity_adjustment_log, mythos_unit.lucidity_cooldowns, mythos_unit.lucidity_exposure_state (+14 more)

### Community 375 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 376 - "properties"
Cohesion: 0.18
Nodes (11): additionalProperties, description, type, description, description, description, properties, exits (+3 more)

### Community 377 - "properties"
Cohesion: 0.11
Nodes (19): description, description, description, description, type, description, maxLength, minLength (+11 more)

### Community 378 - "test_admin_teleport_commands.py"
Cohesion: 0.16
Nodes (42): handle_confirm_goto_command(), handle_confirm_teleport_command(), handle_goto_command(), handle_teleport_command(), Any, Handle the goto command for teleporting the admin to a player's location. Args:…, Handle the confirm teleport command for executing the actual teleportation.…, Handle the confirm goto command for executing the actual teleportation. Args:… (+34 more)

### Community 379 - ".check_player_mute_status"
Cohesion: 0.09
Nodes (12): Any, Extract information from chat event. Args: chat_event: Chat event dictionary…, Determine if mute check should be applied for a channel. Args: channel: Channel…, Compare two room IDs using canonical room ID resolution. Args: player_room_id:…, Get player's current room ID from online players cache. Args: player_id: Player…, Get player's current room ID from async persistence layer. Args: player_id:…, Check if a player is currently in the specified room. Args: player_id: Player…, Initialize message filtering helper. Args: connection_manager:… (+4 more)

### Community 380 - "test_lucidity_models.py"
Cohesion: 0.04
Nodes (45): Unit tests for lucidity models. Tests the PlayerLucidity,…, Test LucidityAdjustmentLog can have optional location_id., Test LucidityAdjustmentLog defaults metadata_payload to '{}'., Test LucidityAdjustmentLog has correct table name., Test LucidityAdjustmentLog __repr__ method., Test LucidityAdjustmentLog can have positive delta (gain)., Test LucidityAdjustmentLog can have negative delta (loss)., Test LucidityExposureState can be instantiated with required fields. (+37 more)

### Community 381 - "test_websocket_handler_coverage_gaps.py"
Cohesion: 0.07
Nodes (44): handle_chat_message(), Handle a chat message from a player. Args: websocket: The WebSocket connection…, asyncio, Unit tests to fill coverage gaps in websocket_handler.py. These tests target…, Test handle_game_command exception handling path (lines 472-480)., Test handle_game_command RuntimeError handling path (lines 472-480)., Test process_websocket_command resolves connection_manager from app when None…, Test handle_chat_message resolves connection_manager from app when None (lines… (+36 more)

### Community 382 - "properties"
Cohesion: 0.20
Nodes (10): description, description, description, description, type, properties, field1, field2 (+2 more)

### Community 383 - "test_channel_commands.py"
Cohesion: 0.06
Nodes (56): _extract_channel_from_command(), _get_persistence_and_player(), handle_channel_command(), _handle_default_channel_setting(), Any, Validate channel name. Returns error dict if invalid, None if valid., Handle the channel command for switching channels or setting default channel.…, Get persistence and player. Returns (persistence, player) or (None, None) if… (+48 more)

### Community 384 - "NATSSubjectManager"
Cohesion: 0.05
Nodes (56): Admin API module for MythosMUD. This module provides administrative API…, get_patterns(), get_subject_manager_dependency(), get_subject_statistics(), PatternsResponse, BaseModel, get, post (+48 more)

### Community 385 - "test_lint_pyright_suppressions.py"
Cohesion: 0.15
Nodes (32): _Failure, lint_api_module_scope(), _LintModule, LintTestApi, _load_script_module(), _problems(), fixture, Path (+24 more)

### Community 386 - "test_rate_limiter_utils.py"
Cohesion: 0.05
Nodes (41): Unit tests for rate limiting utilities. Tests the simple in-memory rate limiter…, Test get_rate_limit_info returns correct info with requests., Test get_rate_limit_info calculates reset time correctly., Test get_rate_limit_info calculates retry_after correctly., Test get_rate_limit_info filters out old requests., Test enforce_rate_limit allows request within limit., Test enforce_rate_limit raises RateLimitError when limit exceeded., Test enforce_rate_limit includes retry_after in error. (+33 more)

### Community 387 - "GameClientV2ContainerView.tsx"
Cohesion: 0.08
Nodes (21): DeathInterstitial(), DeathInterstitialProps, DeliriumInterstitial(), DeliriumInterstitialProps, MainMenuModal(), MainMenuModalProps, maxWidthClasses, ModalContainer() (+13 more)

### Community 388 - "utils/layout.ts"
Cohesion: 0.11
Nodes (32): applyCardinalLinkForce(), applyCenterForce(), applyChargeForces(), applyCollisionForces(), applyCrossingMinimizationForces(), applyForceLayout(), applyLinkForces(), applyMutualForce() (+24 more)

### Community 389 - "🧪 MythosMUD E2E Testing Strategy"
Cohesion: 0.05
Nodes (40): 1.1 Unified Test Environment, 1.2 Test Framework Architecture, 2.1 Authentication Testing (Priority 1), 2.2 Movement System Testing (Priority 2), 2.3 Chat System Testing (Priority 3), 3.1 Performance & Reliability, 3.2 Debugging & Failure Analysis, 3.3 Test Data Management (+32 more)

### Community 390 - "CorruptionRepository"
Cohesion: 0.09
Nodes (30): CorruptionRepository, AsyncSession, datetime, UUID, Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE., Data-access helpers for corruption persistence. Mirrors `LucidityRepository`., Add a corruption adjustment log entry., Get cooldown state for a player and action. (+22 more)

### Community 391 - "npcs/catalog_dml.py"
Cohesion: 0.11
Nodes (31): _load_catalog(), _load_json(), main(), _object_dict(), Path, apply_attack_dual_write(), _as_str_object_dict(), _dual_write_one_attack() (+23 more)

### Community 392 - "test_item.py"
Cohesion: 0.07
Nodes (30): Convenience helper for composing uniqueness checks in higher layers., Unit tests for item models. Tests the ItemPrototype, ItemInstance, and…, Test unique_key returns different tuples for different inputs., Test primary_slot returns first wear slot when slots exist., Test unique_key returns different tuples for same instance, different component., Test unique_key returns different tuples for different instance, same component., Test unique_key handles empty strings., Test unique_key is a static method (can be called without instance). (+22 more)

### Community 393 - "player_connection_setup.py"
Cohesion: 0.11
Nodes (38): _add_player_to_room_silently(), _broadcast_player_entered_game(), handle_new_connection_setup(), Any, Player, UUID, Player connection setup functions. This module handles the setup tasks when a…, Broadcast a structured entry event to other occupants (excluding the newcomer).… (+30 more)

### Community 394 - "SkillRepository"
Cohesion: 0.11
Nodes (26): Base, Skill catalog entry. id: primary key (identity). key: stable identifier (e.g.…, String representation of the skill., Skill, Any, Get a skill by key (e.g. accounting, cthulhu_mythos). Args: key: Skill key.…, Map procedure result row to Skill model., Repository for skills catalog persistence. Handles skill queries for character… (+18 more)

### Community 395 - "test_container_persistence_extended_crud.py"
Cohesion: 0.05
Nodes (56): delete_container(), Delete by id; True if a row was removed. Raises DatabaseError on failure., _build_container_data_from_row(), get_containers_by_entity_id(), get_containers_by_room_id(), get_decayed_containers(), Any, ContainerData (+48 more)

### Community 396 - "test_message_broadcaster.py"
Cohesion: 0.07
Nodes (41): message_broadcaster(), mock_room_manager(), mock_send_personal_message(), asyncio, fixture, Unit tests for message broadcaster. Tests the MessageBroadcaster class., Test broadcast_global() excludes specified player., Test broadcast_global() when no players online. (+33 more)

### Community 397 - "properties"
Cohesion: 0.18
Nodes (11): description, description, description, description, pattern, type, properties, field1 (+3 more)

### Community 398 - "Memory Leak Prevention System - Implementation Summary"
Cohesion: 0.05
Nodes (39): **1. Memory Usage Monitoring**, **2. Automatic Cleanup System**, **3. Connection Management Enhancements**, **4. Data Structure Management**, **5. Comprehensive Alerting**, **API Usage Examples**, 🏗️ **Architecture Overview**, 🎉 **Benefits Achieved** (+31 more)

### Community 399 - "deprecated_patterns.py"
Cohesion: 0.06
Nodes (37): database, deprecated_api_logging(), deprecated_async_logging(), deprecated_basic_logging(), deprecated_batch_logging(), deprecated_database_logging(), deprecated_error_handling(), deprecated_exception_handling() (+29 more)

### Community 400 - "test_player_requests.py"
Cohesion: 0.04
Nodes (96): EffectHandler, apply_corruption(), apply_fear(), apply_lucidity_loss(), damage_player(), gain_occult_knowledge(), heal_player(), FastAPIRequest (+88 more)

### Community 401 - "SpellLearningService"
Cohesion: 0.11
Nodes (27): Any, UUID, Learn a spell for a player., Validate prerequisites for learning a spell. Args: player_id: Player ID spell:…, Service for handling spell learning from various sources. Manages spell…, Learn a spell from a spellbook item. Args: player_id: Player ID…, Learn a spell from an NPC teacher. Args: player_id: Player ID npc_id: ID of the…, Learn a spell as a quest reward. Args: player_id: Player ID quest_id: ID of the… (+19 more)

### Community 402 - "test_item_catalog.py"
Cohesion: 0.14
Nodes (27): CatalogQuery, normalize_catalog_query(), project_admin_item(), project_player_item(), Item catalog service: filtered listing with player/admin column projection., Normalized catalog list query., Clamp pagination and blank filters to None., P1 columns for non-admin viewers. (+19 more)

### Community 403 - "PlayerDPUpdated"
Cohesion: 0.03
Nodes (130): PlayerDPUpdated, PlayerXPAwardEvent, Event fired when a player's DP changes. This event is triggered when a player…, Event published when a player receives XP., _attach_dp_updated_posture_fields(), _decay_previous_position_before_lying(), _dispatch_player_dp_decay_payload(), _dispatch_player_dp_updated_payload() (+122 more)

### Community 404 - "npc_combat_integration_service.py"
Cohesion: 0.02
Nodes (103): Combat messaging integration with real-time messaging system. Re-exports from…, NPCCombatDataProvider, Any, UUID, NPC Combat Data Provider. This module provides data retrieval and preparation…, Get player name for messaging. Args: player_id: ID of the player Returns:…, Get the current room ID for a player. Args: player_id: ID of the player (must…, Get player combat participant data from persistence. Args: player_id: ID of the… (+95 more)

### Community 405 - "test_websocket_handler_helpers.py"
Cohesion: 0.33
Nodes (5): Unit tests for websocket handler helper functions. Tests the helper functions…, Test _is_websocket_disconnected() returns True for disconnection messages., Test _is_websocket_disconnected() returns False for other messages., test_is_websocket_disconnected_false(), test_is_websocket_disconnected_true()

### Community 406 - "test_config_models.py"
Cohesion: 0.04
Nodes (66): _apply_url_fallback(), _default_cors_origins(), _parse_env_list(), _parse_list_from_string(), Any, Parse non-empty string as JSON list or CSV. Used by _parse_env_list., Parse a string from the environment as JSON list or CSV., Derive default CORS origins with environment taking precedence. (+58 more)

### Community 407 - "handle_quest_command"
Cohesion: 0.09
Nodes (38): ExitStack, handle_quest_command(), Handle quest command subcommands: abandon, ask, turnin. Usage: quest abandon…, current_user(), _enter_quest_command_patches(), mock_request(), asyncio, fixture (+30 more)

### Community 408 - "LRUCache"
Cohesion: 0.08
Nodes (20): K, LRUCache, Put an item into the cache. Args: key: The key to store value: The value to…, Delete an item from the cache. Args: key: The key to delete Returns: True if…, Clear all items from the cache., Get the current number of items in the cache., Check if the cache is at maximum capacity., Get cache statistics. Returns: Dictionary containing cache statistics (+12 more)

### Community 409 - "TrackedTaskManager"
Cohesion: 0.09
Nodes (31): get_global_tracked_manager(), memory_leak_prevention_channel_start_session(), patch_asyncio_create_task_with_tracking(), Global TrackedTaskManager for Memory Leak Prevention Infrastructure. This…, Audit and reclaim orphaned task candidates across the system. Returns: Number…, Proactively clean up orphaned tasks by cancelling leak prevention violations.…, Return count of currently tracked task references within the manager's…, Attach a TaskRegistry instance to this Tracker for shared coordination. Args:… (+23 more)

### Community 410 - "PrototypeRegistry"
Cohesion: 0.05
Nodes (74): ItemPrototypeModel, BaseModel, Pydantic models for item prototype validation. This module defines the…, Validated representation of an item prototype definition. This model keeps the…, PrototypeRegistry, PrototypeRegistryError, Exception, Prototype registry for managing item prototypes. This module provides the… (+66 more)

### Community 411 - "PlayerDeathService"
Cohesion: 0.11
Nodes (20): Small types shared by CombatService wiring., PlayerDeathService, Any, AsyncSession, Player, UUID, Player Death Service for managing player mortality and DP decay. This service…, Process DP decay for a single mortally wounded player. Decreases player DP by… (+12 more)

### Community 412 - "test_time_bundle.py"
Cohesion: 0.08
Nodes (28): isolated_chronicle(), asyncio, fixture, Unit tests for TimeBundle container wiring., Calendar components and daypart helpers., Real/Mythos datetime conversion round-trips approximately., Advance and freeze update persisted state., Clock formatting includes Mythos suffix. (+20 more)

### Community 413 - "._build_player_attacked_event"
Cohesion: 0.09
Nodes (14): UUID, Resolve the player and UUID needed for DP update events., Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated., Publish the PlayerDPUpdated event to the event bus., Publish NPC-on-player attack as player_attacked to NATS so the client receives…, Resolve target UUID, player object, and stats needed for NATS attack event., Construct the PlayerAttackedEvent payload for NATS publication., Return an integer stat from stats[key], handling common primitive types. (+6 more)

### Community 414 - "test_flee_command.py"
Cohesion: 0.10
Nodes (36): flee_handler_deps(), _FleeCmdApp, _FleeCmdAppState, _FleeCmdRequest, FleeHandlerDeps, _GetCombatHandlerLoaderApp, _GetCombatHandlerLoaderAppState, _GetCombatHandlerLoaderContainer (+28 more)

### Community 415 - "test_room_subscription_manager_helpers.py"
Cohesion: 0.05
Nodes (40): fixture, Unit tests for room subscription manager helper functions. Tests the helper…, Test reconcile_room_presence() handles errors gracefully., Test _canonical_room_id() with None., Test _canonical_room_id() with empty string., Test _canonical_room_id() resolves via persistence., Test _canonical_room_id() returns original when room has no id., Test _canonical_room_id() handles errors gracefully. (+32 more)

### Community 416 - "test_player_death_service.py"
Cohesion: 0.07
Nodes (29): Unit tests for player death service. Tests the PlayerDeathService class for…, Test get_mortally_wounded_players() excludes dead players., Test process_mortally_wounded_tick() returns False when player already dead., Test process_mortally_wounded_tick() applies DP decay via Player.apply_dp_decay., Test _get_room_name_for_death() returns room name when available., Test _get_room_name_for_death() returns room_id when room not found., Test _get_room_name_for_death() returns 'Unknown' for empty location., Test _get_room_name_for_death() returns room_id when async_persistence… (+21 more)

### Community 417 - "useRoomEditModal.ts"
Cohesion: 0.07
Nodes (17): ENVIRONMENT_OPTIONS, EnvironmentOption, RoomEditModal(), EnvironmentOption, fieldBorderClass(), RoomEditDescriptionField(), RoomEditFormData, RoomEditModalForm() (+9 more)

### Community 418 - "multiplayer-browser-helpers.js"
Cohesion: 0.12
Nodes (33): buttonHasLoginSubmitLabel(), captureGameUiDiagnosticsInBrowser(), captureOccupantsSnapshotInBrowser(), coalesce(), computedStyleHidesElement(), elementShowsConnectedStatus(), elementTextIncludesGameInfo(), evaluateGameUiLoaded() (+25 more)

### Community 419 - "Chat Panel Separation Implementation Tasks"
Cohesion: 0.14
Nodes (13): Chat Panel Separation Implementation Tasks, Conclusion, Critical Path Analysis, Dependencies and Critical Path, Functional Metrics, Overview, Phase Dependencies, Quality Metrics (+5 more)

### Community 420 - "Async Persistence Migration Plan"
Cohesion: 0.05
Nodes (37): 1.1 Find all PersistenceLayer usage, 1.2 Document call sites, 2.1 Update ApplicationContainer, 2.2 Update lifespan.py, 2.3 Migrate API endpoints, 2.4 Migrate services, 2.5 Migrate commands, 2.6 Update test fixtures (+29 more)

### Community 421 - "migration_examples.py"
Cohesion: 0.06
Nodes (36): expensive_operation(), migration_example_1(), migration_example_10(), migration_example_11(), migration_example_12(), migration_example_13(), migration_example_14(), migration_example_15() (+28 more)

### Community 422 - "MessageBroadcaster"
Cohesion: 0.10
Nodes (23): SendPersonalMessage, _global_targets_and_stats(), MessageBroadcaster, _narrow_gather_delivery_dict(), UUID, Message broadcasting for connection management. This module provides room and…, Convert string player IDs to UUIDs for message sending. Args: target_list: List…, Process results from batch message delivery. Args: delivery_results: Results… (+15 more)

### Community 423 - "passive_corruption_flux/service.py"
Cohesion: 0.09
Nodes (29): CorruptionFluxServiceConfig, Configuration for passive corruption flux (#815 PR-5). `period_label`,…, Optional configuration for PassiveCorruptionFluxService. All fields have…, Passive corruption flux service package (#815 PR-5)., PassiveCorruptionFluxContext, Data models for passive corruption flux (#815 PR-5)., Resolved environmental context for one player's passive corruption flux…, _as_float() (+21 more)

### Community 424 - "quest_commands.py"
Cohesion: 0.04
Nodes (75): _get_lifecycle_manager(), _get_npc_room_id(), _get_npcs_in_room(), Get the lifecycle manager from the NPC instance service., Get the room ID from an NPC instance, checking both current_room and…, Check if an NPC should be included in the results (has name and is alive)., Get list of NPC names in a room from lifecycle manager., _should_include_npc() (+67 more)

### Community 425 - "test_catalog_commands.py"
Cohesion: 0.15
Nodes (25): handle_catalog_command(), parse_catalog_args(), Handle /catalog: print a paginated prototype table (text only)., Parse /catalog args. Supports key=value tokens: page, type, namespace, search,…, _CatalogAppStateStub, _CatalogAppStub, _CatalogRequestStub, _player_response() (+17 more)

### Community 426 - "test_dependency_analysis.py"
Cohesion: 0.08
Nodes (37): analyzer_api_module_scope(), _DependencyAnalyzerScriptInternals, DependencyAnalyzerTestApi, _DependencyRiskScriptInternals, DependencyRiskTestApi, _FakeCompletedProcess, _load_dependency_analyzer_script(), _load_dependency_risk_script() (+29 more)

### Community 427 - "TestNPCCombatRewards"
Cohesion: 0.08
Nodes (20): asyncio, fixture, Test check_player_connection_state handles missing container., Test award_xp_to_killer successfully awards XP., Test award_xp_to_killer handles failure gracefully., Test award_xp_to_killer handles exceptions gracefully., Test suite for NPCCombatRewards class., Test award_xp_to_killer handles zero XP. (+12 more)

### Community 428 - "TestEmitLootAllEvent"
Cohesion: 0.10
Nodes (22): _assert_warning_once(), _diff_items_from_emit(), mock_connection_manager(), asyncio, ConnectionManager, fixture, Test emit_loot_all_event handles emission errors gracefully., Test emit_loot_all_event correctly calculates items_removed in diff. (+14 more)

### Community 429 - "asyncio"
Cohesion: 0.12
Nodes (17): asyncio, get_skills_catalog returns list of skill dicts., get_player_skills for owned player returns list of skill dicts., get_player_skills for another user's player returns None., record_successful_skill_use delegates to repo.record_use with correct args., get_skills_used_this_level returns distinct skill_ids from repo., When roll > current value, update_value called with new value (gain 1 or 1d10)., roll_skill_check when player has no value for skill_id returns False. (+9 more)

### Community 430 - "RoomMapEditorRuntime.tsx"
Cohesion: 0.07
Nodes (33): useMapEditing(), UseRoomMapDataOptions, UseRoomMapDataResult, MapEditToolbar(), MapEditToolbarProps, buildModalCreateEdgeHandler(), buildModalPreviewHandler(), buildModalUpdateEdgeHandler() (+25 more)

### Community 431 - "Async Persistence Migration Tracker"
Cohesion: 0.13
Nodes (15): Async Persistence Migration Tracker, Current Status, Decision Tree, Files Requiring Migration, Migration Pattern, Migration Strategy, Overview, Phase 1: High Priority (✅ COMPLETE) (+7 more)

### Community 432 - "Phase 3, Task 3.2: NATS Subject Manager Usage Review"
Cohesion: 0.05
Nodes (36): chat_whisper_player Pattern, Legacy Whisper Subscription Bug, NATSSubjectManager, Phase 3 Comprehensive Code Review, 1. Resilience Through Redundancy, 2. Centralized Pattern Management, 3. Error Handling, 4. Logging and Observability (+28 more)

### Community 433 - "Execution Steps"
Cohesion: 0.05
Nodes (36): BEFORE EXECUTING THIS SCENARIO, YOU MUST, BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, CONFIRMATION CHECKLIST, EXECUTION AFFIRMATION (Type this before proceeding), 🛑 EXECUTION ENDS HERE - DO NOT PROCEED FURTHER, Execution Steps, Expected Results (+28 more)

### Community 434 - "properties"
Cohesion: 0.11
Nodes (19): description, items, type, default, description, maximum, minimum, type (+11 more)

### Community 435 - "TestValidatorComponents"
Cohesion: 0.17
Nodes (7): Test path validator integration., Test reporter integration., Test the full validation pipeline., Test individual validator components., Test room loader integration., Test schema validator integration., TestValidatorComponents

### Community 436 - "PayloadOptimizer"
Cohesion: 0.09
Nodes (29): get_payload_optimizer(), PayloadOptimizer, Any, Payload optimization for WebSocket messages. This module provides utilities for…, Create an incremental update payload containing only changed fields. Args:…, Optimizes payloads for WebSocket transmission. Features: - Size limit…, Get the global payload optimizer instance., Initialize the payload optimizer. Args: max_payload_size: Maximum payload size… (+21 more)

### Community 437 - "lint_pyright_suppressions.py"
Cohesion: 0.12
Nodes (27): Pattern, _collect_context(), _comment_text(), _extract_field(), Failure, _iter_target_files(), _join_continuation(), _justification_failures() (+19 more)

### Community 438 - "PydanticErrorHandler"
Cohesion: 0.08
Nodes (30): Error handlers package for MythosMUD. This package provides specialized error…, convert_pydantic_error(), _ExtractedErrorInfo, _ExtractedFieldErrorInfo, handle_pydantic_error(), TypedDict, Unpack, ValidationError (+22 more)

### Community 439 - "test_npc_event_handlers.py"
Cohesion: 0.03
Nodes (81): mock_connection_manager(), mock_message_builder(), mock_send_occupants_update(), npc_event_handler(), asyncio, fixture, Unit tests for NPC event handlers. Tests the NPCEventHandler class., Test _parse_behavior_config() with invalid JSON. (+73 more)

### Community 440 - "ChatPoseManager"
Cohesion: 0.15
Nodes (9): ChatPoseManager, Chat pose management utilities. This module provides pose management…, Manages in-memory storage of player poses., Initialize the pose manager., Normalize player identifiers to string form., Set a player's pose in memory. Args: player_id: ID of the player pose: Pose…, Get a player's current pose. Args: player_id: ID of the player Returns: Current…, Clear a player's pose. Args: player_id: ID of the player Returns: True if pose… (+1 more)

### Community 441 - "revised-character-creation.spec.ts"
Cohesion: 0.09
Nodes (24): assertCharacterVisibleOnList(), deleteRevisedTestCharacterToMakeRoom(), needsRecoveryFromWrongCreationScreen(), openStatsRollingFromLogin(), pollUntilCharacterListed(), readSkillsMessageText(), recoverCharacterSelectionAfterCreation(), ADR-0021 (+16 more)

### Community 442 - "authenticated.ts"
Cohesion: 0.13
Nodes (24): ADMIN_STORAGE_PATH, ADMIN_USERNAME, AUTH_STORAGE_PATH, BASE_URL, SERVER_API_V1, SERVER_URL, TEST_PASSWORD, TEST_USERNAME (+16 more)

### Community 443 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 444 - "Audit Coverage Boundary — 2026-08 Design Audit"
Cohesion: 0.05
Nodes (35): 1. Purpose, 2. Scope for the immediate next step: verifying #625–#628, 3. Enumeration method, 4.1 Documents — the audited 29, recovered from the audit's own claim registers, 4.2 Documents — the residual 74, conservative default, 4.3 Code — method fact, not a directory checklist, 4.4 `docs/subsystems/` — staleness, not conformance, 4.5 Security — a boundary issue #639 does not mention (+27 more)

### Community 445 - "PostgreSQL & SQL Audit Report"
Cohesion: 0.06
Nodes (31): 10. Prioritized Fixes, 11. Summary Table, 1.1. Snake_case (GOOD), 1.2. Quoted Identifier, 1. Naming Conventions, 2.1. Uppercase SQL Keywords, 2. SQL Formatting (Keywords Lowercase), 4.1. IDs: `serial` / `bigserial` (GOOD) (+23 more)

### Community 446 - "test_quality_fragmentation_guard.py"
Cohesion: 0.12
Nodes (35): ChangedFile, scan_changed_files(), _ChangedFile, _load_guard_module(), _load_lizard_module(), _load_trends_module(), CaptureFixture, MonkeyPatch (+27 more)

### Community 447 - "PeriodicOrphanAuditor"
Cohesion: 0.06
Nodes (42): create_lifespan_memory_service(), PeriodicOrphanAuditor, Any, Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task…, Core capability for granular investigation cycles. Repeated universal analysis…, Execute a single investigation loop synchronously producing operator summary.…, Stop the periodic orphan auditor background enforcement., # TODO: Improve graceful shutdown with early cancellation # pylint:… (+34 more)

### Community 448 - "RoomCacheService"
Cohesion: 0.15
Nodes (7): Service for caching room data., Invalidate cached room data. Args: room_id: The room ID to invalidate, Preload multiple rooms into cache. Args: room_ids: List of room IDs to preload, RoomCacheService, Any, _RoomObj, TestRoomCacheService

### Community 449 - "admin_shutdown_command.py"
Cohesion: 0.11
Nodes (33): _broadcast_shutdown_cancellation(), _cancel_countdown_task(), _cancel_existing_shutdown_task(), _clear_shutdown_state(), countdown_loop(), _create_countdown_task(), _get_shutdown_services(), _get_shutdown_state() (+25 more)

### Community 450 - "magic_healing_events.py"
Cohesion: 0.20
Nodes (11): MagicServiceHealingMixin, Any, UUID, Healing event notification for spellcasting. Mixin that sends player_dp_updated…, Publish DP update via event bus, or send fallback game event., If instant cast applied healing, send DP update event to the healed player., Mixin for MagicService: send DP update events when spells apply healing., True when healing was applied to another player (heal-other, not steal-life or… (+3 more)

### Community 451 - "websocket_integration.py"
Cohesion: 0.06
Nodes (28): auth_service, authenticate_websocket_connection(), chat_service, game_service, handle_chat_message(), handle_game_action(), handle_websocket_error(), handle_websocket_message() (+20 more)

### Community 452 - "NPCStartupService"
Cohesion: 0.12
Nodes (19): _merge_phase_into_startup(), _new_spawn_results(), NPCStartupService, Any, NPC Startup Service for MythosMUD. This module provides automatic NPC spawning…, Spawn all required NPCs. Args: required_npcs: List of required NPC definitions…, Spawn optional NPCs based on spawn probability. Args: optional_npcs: List of…, Second pass: spawn one instance per definition (that was spawned in… (+11 more)

### Community 453 - "stateNormalization.ts"
Cohesion: 0.11
Nodes (26): createInitialState(), createSessionActions(), SessionActions, SessionSelectors, SessionState, SessionStore, touchActivity(), useSessionStore (+18 more)

### Community 454 - "File-by-File Changes"
Cohesion: 0.06
Nodes (34): 1. Mutable Default Values (Rule 3 Violation), 2. Unsafe `dict[str, Any]` Types (Rule 2 Violation), 3. Old-Style model_config (Rule 1 Violation), 4. Missing Security Configuration, 5. Missing model_config Entirely, Critical Issues Identified, Executive Summary, File-by-File Changes (+26 more)

### Community 455 - "validate.py"
Cohesion: 0.09
Nodes (33): demo(), BugBlock, check_bug_content(), _check_bugs(), check_loose_tags(), check_relative_links(), _check_required_structure(), _exit_code_for_errors() (+25 more)

### Community 456 - "test_game_tick_death.py"
Cohesion: 0.10
Nodes (36): cleanup_decayed_corpses(), _cleanup_single_decayed_corpse(), _CorpseLike, _create_corpse_lifecycle_service(), _log_cleanup_results(), FastAPI, Protocol, Decayed corpse cleanup for the game tick loop. (+28 more)

### Community 457 - "Any"
Cohesion: 0.10
Nodes (16): Any, Task, Create callback function for task completion cleanup., Set up tracking for a newly created task., Register and create a tracked asyncio.Task. Args: coro: The coroutine to wrap…, Unregister task from tracking, optionally force-cancelling. Args: task: Task…, Cancel specific task with logical timeout boundaries. Args: task: Task…, Metadata for tracked asyncio.Tasks. (+8 more)

### Community 458 - "LucidityTierCache"
Cohesion: 0.10
Nodes (21): LucidityTierCache, UUID, In-memory cache of each player's current lucidity tier (#714). Exit…, Module-level singleton (mirrors phantom_hostile_service) -- callers MUST share…, Record this player's current tier., Return the cached tier, or None if this player has never been recorded., True only if the cached tier is exactly 'deranged' -- a cache miss is never…, Drop a player's cached tier (e.g. on disconnect). (+13 more)

### Community 459 - "ExperienceRepository"
Cohesion: 0.06
Nodes (37): Initialize the async persistence layer. This facade delegates to focused async…, ExperienceRepository, Player, UUID, Update player experience points atomically. Args: player_id: Player UUID or…, Run update_player_stat_field stored procedure and log success., Update a specific numeric field in player stats atomically. Args: player_id:…, Repository for player experience and stats persistence operations. Handles XP… (+29 more)

### Community 460 - "test_inventory_get_command.py"
Cohesion: 0.16
Nodes (27): _container_transfer_messages(), _get_from_container_path(), _get_route_after_validation(), _get_transfer_out_of_container(), GetCommandRuntime, GetItemSpec, handle_get_command(), CommandResponse (+19 more)

### Community 461 - "ConnectionErrorHandler"
Cohesion: 0.11
Nodes (27): ConnectionErrorHandler, Any, UUID, Error handling for connection management. This module provides comprehensive…, Handle WebSocket-specific errors. Args: player_id: The player's ID…, Handle authentication-related errors. Args: player_id: The player's ID…, Handle security violations. Args: player_id: The player's ID violation_type:…, Attempt to recover from an error state for a player. Args: player_id: The… (+19 more)

### Community 462 - "test_player_event_handlers_room_left.py"
Cohesion: 0.10
Nodes (26): asyncio, Unit tests for player room event handlers (player left / unsubscribe /…, Test handle_player_left() skips when connection manager not available., Test handle_player_left() handles player not found., Test handle_player_left() skips broadcast when player is disconnecting., Test handle_player_left() handles errors., Test _log_occupants_info() logs occupant information., Test unsubscribe_player_from_room() successfully unsubscribes player. (+18 more)

### Community 463 - "RateLimiter"
Cohesion: 0.09
Nodes (18): Any, RateLimiter, Remove timestamps older than the window size. Args: player_id: Player ID…, Check if a player is within rate limits for a channel. Args: player_id: Player…, Record a message for rate limiting. Args: player_id: Player ID channel: Channel…, Sliding window rate limiter for chat channels. Implements per-user, per-channel…, Get rate limiting statistics for a player. Args: player_id: Player ID Returns:…, Reset rate limiting for a player. Args: player_id: Player ID channel: Specific… (+10 more)

### Community 464 - "roomHandlers.ts"
Cohesion: 0.12
Nodes (32): buildGameStateResult(), calculateOccupantCount(), createInitialRoomState(), createMinimalRoomFromOccupantsEvent(), createRoomUpdateWithPreservedOccupants(), extractGraceAndFollowFields(), extractRoomMetadata(), getFinalNpcs() (+24 more)

### Community 465 - "e2e-bootstrap.ts"
Cohesion: 0.14
Nodes (28): appendBootstrapFailureLog(), countProfessionsPayload(), __dirname, E2E_BOOTSTRAP_ERRORS_LOG, E2E_BOOTSTRAP_LOG_DIR, E2E_CLIENT_URL, E2E_ENV_DEFAULTS, E2E_PROJECT_ROOT (+20 more)

### Community 466 - "multiplayer-colocated.ts"
Cohesion: 0.11
Nodes (21): forceLogoutPlayer(), assertNoRestDisconnectPollution(), assertNotStuckOnLogin(), executeCommandTrusted(), captureOccupantsSnapshot(), capturePresenceEvents(), EnsureMultiplayerCoLocatedOptions, ensureMultiplayerReadyForCoLocate() (+13 more)

### Community 467 - "FakeSenderRegistry"
Cohesion: 0.11
Nodes (20): FakeSenderRegistry, UUID, In-memory registry of each player's most recent fake NPC whisper sender (#625,…, Module-level singleton (mirrors phantom_hostile_service) -- callers MUST share…, Record that this player's most recent whisper came from this fake NPC., Return the fake NPC name this player was last whispered by, or None., Drop this player's fake-sender record (e.g. leaving fractured/deranged,…, Unit tests for the in-memory fake whisper sender registry (#625, #714). This… (+12 more)

### Community 468 - "ChatChannelLoggerMixin"
Cohesion: 0.08
Nodes (23): ChatChannelLoggerMixin, Any, Path, Channel-specific chat log methods for MythosMUD. Mixin used by ChatLogger:…, Log a global channel message to global.log file. Args: message_data: Global…, Get the global channel log file path. Returns: Path to the global channel log…, Log a system channel message to system.log file. Args: message_data: System…, Log a whisper channel message to whisper.log file. Args: message_data: Whisper… (+15 more)

### Community 469 - "start_grace_period"
Cohesion: 0.08
Nodes (37): cancel_grace_period(), _PlayerLookupManager, Any, Player, Protocol, UUID, Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…, The one typed slice of ConnectionManager needed to snapshot DP at grace start. (+29 more)

### Community 470 - "_find_item_in_equipped"
Cohesion: 0.11
Nodes (24): _check_equipped_item(), _check_item_in_location(), _find_item_in_equipped(), _handle_item_look(), Any, Item look functionality for MythosMUD. This module handles looking at items,…, Find an item in equipped items by name or prototype_id. Args: equipped:…, Check if item found in a location and return formatted result. (+16 more)

### Community 471 - "test_connection_state_machine.py"
Cohesion: 0.08
Nodes (25): Unit tests for connection state machine. Tests the NATSConnectionStateMachine…, Test start_reconnect() transition from disconnected to reconnecting., Test open_circuit() transition from reconnecting to circuit_open., Test can_attempt_connection() returns True when disconnected., Test can_attempt_connection() returns True when connecting., Test should_open_circuit() returns False when under threshold., Test get_stats() handles None connected time., Test reconnect_attempts resets on successful connection. (+17 more)

### Community 472 - "Frontend Design Skill"
Cohesion: 0.07
Nodes (28): Alpha Is A Design Smell, Building Functional Palettes, Color & Contrast, Color Spaces: Use OKLCH, Contrast & Accessibility, Dangerous Color Combinations, Dark Mode Is Not Inverted Light Mode, Never Use Pure Gray or Pure Black (+20 more)

### Community 473 - "Async Audit Executive Summary"
Cohesion: 0.05
Nodes (48): Alternative Approaches Considered, Async Audit Executive Summary, Benefit, Break-Even, Contact, Cost, Cost-Benefit Analysis, Critical Findings (+40 more)

### Community 474 - "Test Pruning Candidates - Detailed List"
Cohesion: 0.06
Nodes (33): 1. Command Validation Tests, 2. Error Response Tests, 3. Permission Check Tests, Aggressive Estimate (Full Optimization), Category A: Infrastructure Tests Testing Framework Behavior, Category B: Coverage Tests Written for Metrics, Category C: Model Property Tests, Conclusion (+25 more)

### Community 475 - "ItemFactory"
Cohesion: 0.07
Nodes (35): ItemInstance, initialize_components(), Any, Component hook coordination for freshly minted item instances., Prepare component state metadata for a new item instance. This routine…, Item system package. This module exposes the prototype schema and registry…, ItemFactory, ItemFactoryError (+27 more)

### Community 476 - "FStringLoggingFixer"
Cohesion: 0.09
Nodes (19): FStringLoggingFixer, main(), Any, Match, Path, Validate that file exists and is a Python file., Read file content with error handling., Build parameters list for complex patterns. (+11 more)

### Community 477 - "combat_loader.py"
Cohesion: 0.07
Nodes (50): Combat service for command modules., Movement service for command modules., Player position service for command modules., format_combat_status(), get_combat_target(), Any, Produce a human-readable combat status string. This helper is retained for…, Resolve a combat target by name. The current implementation is intentionally… (+42 more)

### Community 478 - "test_command_processing.py"
Cohesion: 0.07
Nodes (37): _dispatch_parsed_command(), _handle_processing_error(), _handle_validation_error(), _log_security_sensitive_command(), _parse_command_line_or_client_error(), CommandExecutionRequest, Exception, ValidationError (+29 more)

### Community 479 - "InventorySchemaValidationError"
Cohesion: 0.07
Nodes (43): _parse_equipped_raw(), _parse_inventory_raw(), PlayerSavePreparer, Any, datetime, Player, Player save/upsert helpers for PlayerRepository. Handles inventory validation,…, Validate and serialize inventory payload. Returns (inventory_json,… (+35 more)

### Community 480 - "GameMechanicsService"
Cohesion: 0.08
Nodes (30): GameMechanicsService, Gain occult knowledge (with lucidity loss)., Heal a player's health., Damage a player's health., Award experience points to a player. CRITICAL FIX: This method prevents XP…, Service class for game mechanics operations., Initialize the game mechanics service with a persistence layer., Apply lucidity loss to a player. (+22 more)

### Community 481 - "MovementMonitor"
Cohesion: 0.11
Nodes (15): MovementMonitor, Any, UUID, Record concurrent movement count., Record an integrity check result., Validate players are not in multiple rooms., Get comprehensive movement metrics., Get current alerts based on thresholds. (+7 more)

### Community 482 - "Profession"
Cohesion: 0.03
Nodes (71): Profession, Any, Base, Check if given stats meet the profession requirements. Args: stats: Dictionary…, Check if profession is available for player selection., Get formatted text for displaying stat requirements. Returns: Formatted string…, Profession model for game data. Stores profession information including name,…, String representation of the profession. (+63 more)

### Community 483 - "PersonalMessageSender"
Cohesion: 0.11
Nodes (28): Messaging components for connection management. This package provides modular…, PersonalMessageSender, Any, UUID, Personal message delivery for connection management. This module provides…, Send message to a single WebSocket connection. Returns True if successful., Queue message if no active connections., Send a personal message to a player via WebSocket. Args: player_id: The… (+20 more)

### Community 484 - "EventPublisher"
Cohesion: 0.05
Nodes (57): EventPublisher, JsonMap, Publish a player_entered event to NATS. Args: player_id: ID of the player who…, Publish a player_left event to NATS. Args: player_id: ID of the player who left…, Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…, Create a standardized event message structure. Args: event_type: Type of event…, Get the next sequence number for event ordering. Returns: Next sequence number, Reset the sequence number to 0. (+49 more)

### Community 485 - "directionHallucination.ts"
Cohesion: 0.18
Nodes (15): AsciiNoise(), AsciiNoiseProps, prefersReducedMotion(), ageBucket(), decayMessageText(), isProtectedToken(), MYTHOS_GLYPHS, DIRECTION_POOL (+7 more)

### Community 486 - "CommandRateLimiter"
Cohesion: 0.10
Nodes (22): CommandRateLimiter, Any, datetime, Per-player command rate limiting. Prevents command flooding and denial-of-…, Get number of commands player can still execute. Args: player_name: Player to…, Reset rate limit for a specific player. Useful for admin commands or when…, Reset rate limit for all players. Clears all accumulated timestamp data.…, Get system-wide rate limiting statistics. Returns: Dictionary containing rate… (+14 more)

### Community 487 - "test_lifecycle_respawn.py"
Cohesion: 0.12
Nodes (35): Process the respawn queue and spawn NPCs that are ready (delegates to…, _attempt_respawn_impl(), _cleanup_respawn_queue(), _process_respawn_queue_entry(), process_respawn_queue_impl(), Any, Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…, Process the respawn queue and spawn NPCs that are ready. Args: manager:… (+27 more)

### Community 488 - "test_inventory_mutation_guard_internal.py"
Cohesion: 0.09
Nodes (25): guard(), asyncio, fixture, Unit tests for inventory mutation guard - internal helper methods. Tests…, Test _cleanup_async_state removes empty state., Test _prune_tokens_async removes expired tokens., Test _prune_tokens_async with token_ttl=0 doesn't prune., Test _enforce_limit_async removes oldest tokens when limit exceeded. (+17 more)

### Community 489 - "test_inventory_helpers_extended.py"
Cohesion: 0.09
Nodes (33): Resolve player from persistence and current user., resolve_player(), asyncio, Extended unit tests for inventory command helper functions. Tests additional…, Test _persist_player handles InventorySchemaValidationError., Test _persist_player handles general errors., Test _resolve_player when persistence is None., Test _resolve_player when username resolution fails. (+25 more)

### Community 490 - "asyncio"
Cohesion: 0.06
Nodes (31): asyncio, Test is_player_muted_async() returns True when player is muted., Test is_player_muted_async() returns False when player is not muted., Test add_admin() handles missing persistence (#679: injected, not via…, Test add_admin() handles player not found., Test remove_admin() handles missing persistence (#679: injected, not via…, Test remove_admin() handles player not found., Test is_admin() returns False when persistence not available (#679: injected). (+23 more)

### Community 491 - "lint_optional_auth_no_guard.py"
Cohesion: 0.10
Nodes (30): expr, AllowlistEntry, _auth_posture(), _body_has_direct_guard(), _called_helper_names(), _collect_files(), _dep_names_in_default(), _find_unguarded() (+22 more)

### Community 492 - "CommandService"
Cohesion: 0.09
Nodes (17): CommandHandler, CommandService, Command, Main command processing service for MythosMUD. This service handles command…, Initialize the command service., Process a validated command with routing. Args: command_data: The validated…, Parse and validate command string. Returns: tuple of (parsed_command, cmd,…, Prepare command_data dictionary by merging parsed command fields. Returns:… (+9 more)

### Community 493 - "Does Love Forgive_ (source summary)"
Cohesion: 0.50
Nodes (3): Does Love Forgive_ (source summary), For MythosMUD design, Links

### Community 494 - "TEMPORAL_SYSTEM_RESEARCH.md"
Cohesion: 0.07
Nodes (30): The Call of Cthulhu, Canonical and Derived Observances, Implementation Notes, Mythos Holiday Candidates, Narrative Flavor Seeds, Opportunities for Expansion, 1. Research Synthesis, 2. Mythos Time Model Draft (+22 more)

### Community 495 - "Prometheus Configuration"
Cohesion: 0.09
Nodes (31): Alertmanager Configuration, connection-alerts receiver, critical-alerts receiver, Critical inhibits warning alerts, maintenance-window time interval, performance-alerts receiver, system-alerts receiver, warning-alerts receiver (+23 more)

### Community 496 - "load_world_seed.py"
Cohesion: 0.11
Nodes (30): Popen, _apply_schema(), _apply_schema_with_psql(), _asyncpg_server_settings(), _database_url_for_cli(), _load_dml_with_psql(), main(), _parse_pg_url_for_psql() (+22 more)

### Community 497 - "ReactNodeUpgradeAnalyzer"
Cohesion: 0.10
Nodes (17): main(), Any, Analyze Node.js ecosystem upgrade opportunities, Specialized analyzer for React/Node.js ecosystem upgrades, Analyze build tools and development dependencies, Categorize update by semver, Assess risk for React ecosystem updates, Assess risk for Node.js ecosystem updates (+9 more)

### Community 498 - "MemoryThresholdMonitor"
Cohesion: 0.06
Nodes (49): create_memory_cleanup_monitor(), get_managed_task_cleanup_implementation_for_task_four_spec_compliance(), MemoryStatusReport, MemoryThresholdMonitor, TypedDict, Managed Task Cleanup Service - Runtime Detection for Memory Threshold…, Flush persistent in-memory indexes associated with cached memory residency., Generate status report for diagnostic monitoring. Returns: Dictionary… (+41 more)

### Community 499 - "_find_item_in_inventory"
Cohesion: 0.08
Nodes (24): _find_item_in_inventory(), Find an item in player inventory by name or prototype_id. Args: inventory: List…, Test _find_item_in_inventory() with empty list., Test _find_item_in_inventory() with no matching items., Test _find_item_in_inventory() with multiple matches (ambiguous)., Test _find_item_in_inventory() with instance number., Test _find_item_in_inventory() with instance number out of range., Test _find_item_in_inventory() finds item by name. (+16 more)

### Community 500 - "DistributedEventBus"
Cohesion: 0.09
Nodes (28): DistributedEventBus, Any, EventBus that distributes domain events via NATS for horizontal scaling. When…, Initialize distributed EventBus. Args: nats_service: NATS service for…, Set NATS service and start the bridge (call after NATS connects)., Publish event locally and to NATS when bridge is active., Shutdown EventBus and stop NATS bridge., distributed_bus() (+20 more)

### Community 501 - "test_item_prototype_models.py"
Cohesion: 0.26
Nodes (11): Constants supporting item prototype validation. These enumerations anchor the…, Unit tests for item prototype Pydantic models., test_item_prototype_accepts_valid_flags(), test_item_prototype_accepts_valid_wear_slots(), test_item_prototype_normalizes_effect_components_and_tags(), test_item_prototype_rejects_empty_effect_components(), test_item_prototype_rejects_invalid_flags(), test_item_prototype_rejects_invalid_item_type() (+3 more)

### Community 502 - "NPCCommunicationIntegration"
Cohesion: 0.10
Nodes (23): NPCCommunicationIntegration, Handle a message received by an NPC from a player. Args: npc_id: ID of the NPC…, Process a message to determine if the NPC should respond. Args: npc_id: ID of…, Subscribe an NPC to messages in a specific room. Args: npc_id: ID of the NPC to…, Unsubscribe an NPC from messages in a specific room. Args: npc_id: ID of the…, Integrates NPCs with the existing chat and whisper systems. This class provides…, Initialize the NPC communication integration. Args: event_bus: Optional…, Send a message from an NPC to a room. Args: npc_id: ID of the NPC sending the… (+15 more)

### Community 503 - "test_connection_establishment.py"
Cohesion: 0.04
Nodes (134): _bind_accepted_websocket(), _cleanup_dead_connections(), _cleanup_failed_connection(), establish_websocket_connection(), _EstablishmentConnectionManager, _find_dead_connections(), Player, Protocol (+126 more)

### Community 504 - "test_room_write_procedures.py"
Cohesion: 0.15
Nodes (30): async_sessionmaker, asyncio, AsyncSession, fixture, integration, Integration tests for the room-editor write procedures…, update_room_properties() with p_set_environment=TRUE and NULL clears the…, p_set_environment=FALSE leaves attributes.environment untouched, regardless of… (+22 more)

### Community 505 - "ADR-025: Corruption as a Global Perceptual Filter, Not Per-Message Styling"
Cohesion: 0.10
Nodes (19): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. Related docs, 8. Changelog (+11 more)

### Community 506 - "Any"
Cohesion: 0.11
Nodes (10): Any, Initialize the room cache service. Args: persistence: Persistence layer instance, Get room data with caching. Args: room_id: The room ID Returns: Room data…, Get room data with caching (synchronous version). Args: room_id: The room ID…, Initialize the NPC cache service. Args: npc_service: NPC service instance, Get NPC definitions with caching. Args: session: Database session Returns: List…, Get a specific NPC definition with caching. Args: session: Database session…, Get NPC spawn rules with caching. Args: session: Database session Returns: List… (+2 more)

### Community 507 - "test_optimized_security_validator.py"
Cohesion: 0.09
Nodes (31): Unit tests for optimized security validation utilities. Tests the optimized…, Test validating message with dangerous characters., Test validating message with injection pattern., Test validating message with SQL injection pattern., Test validating message with XSS pattern., Test validating message with path traversal pattern., Test validating message with javascript: URL., Test validating message with event handler. (+23 more)

### Community 508 - "PathValidator"
Cohesion: 0.03
Nodes (60): option, Room fixer for automatic issue resolution. This module handles automatic fixing…, Automatically fixes common room validation issues. Implements safe correction…, Fix missing exits field. Returns True if fixed., Fix missing optional fields. Returns True if any fixed., Fix missing fields based on errors. Returns True if any fixed., Get a summary of applied fixes. Returns: Dictionary with fix statistics, RoomFixer (+52 more)

### Community 509 - "scripts"
Cohesion: 0.10
Nodes (20): scripts, build, dead-code, dev, format, knip, lint, postinstall (+12 more)

### Community 510 - "properties"
Cohesion: 0.11
Nodes (18): additionalProperties, type, minLength, type, type, minLength, type, properties (+10 more)

### Community 511 - "NATS Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (30): NATS Code Review, 10. **Inconsistent Error Handling**, 11. **Missing Input Validation**, 1. **Blocking Operations in Message Handlers** (Anti-pattern violation), 1. **Excellent Error Boundary Implementation**, 2. **Good Connection State Management**, 2. **Missing Message Acknowledgment** (Anti-pattern violation), 3. **Connection Pool Not Used by Default** (Inefficiency) (+22 more)

### Community 512 - "WebSocket Code Review - Branch: feature/sqlite-to-postgresql"
Cohesion: 0.07
Nodes (29): 10. **No Message Batching**, 11. **Missing Rate Limiting on WebSocket Messages**, 12. **Insufficient Authentication Validation**, 1. **Dependency Injection Pattern**, 1. **Event Loop Anti-Pattern in Connection Manager**, 2. **Missing Input Validation on Server Side**, 2. **Modern Async Patterns**, 3. **Error Boundaries** (+21 more)

### Community 513 - "enum"
Cohesion: 0.20
Nodes (10): default, description, enum, type, indoors, intersection, outdoors, street_paved (+2 more)

### Community 514 - "CombatEventHandler"
Cohesion: 0.11
Nodes (28): CombatEventHandler, Any, UUID, Publish attack events and calculate XP reward. Args: current_participant:…, Calculate XP reward for defeating an NPC. Args: npc_id: ID of the defeated NPC…, Award XP to player for defeating an NPC. Args: current_participant: Attacking…, Publish combat ended event., Handles combat event publishing. (+20 more)

### Community 515 - "container_helpers_inventory_display.py"
Cohesion: 0.12
Nodes (28): _apply_container_component_to_slot(), _component_metadata(), _equipped_matches_container_metadata(), get_container_data_for_inventory(), _inventory_stack_to_display_dict(), _lock_state_as_str(), match_container_to_slot(), InventoryStack (+20 more)

### Community 516 - "zone_config_loader.py"
Cohesion: 0.09
Nodes (25): extract_zone_name(), parse_zone_special_rules(), Record, TypedDict, Zone Configuration Loader Module. This module handles loading zone and sub-zone…, Build and store one subzone configuration from a database row., Parse a zone special_rules field from the database., Extract zone name from stable_id (format: 'plane/zone'). Args: stable_id: The… (+17 more)

### Community 517 - "EventBusLifecycleMixin"
Cohesion: 0.10
Nodes (17): EventBusLifecycleMixin, Exception, Task, Cancel leftover tasks after the grace wait, then give them a short drain., Cancel all active tasks and wait for graceful shutdown., Finalize shutdown by clearing tasks and logging., Stop pure async event processing gracefully., Unsubscribe every tracked service. No-op when none are registered. (+9 more)

### Community 518 - "ContainerData"
Cohesion: 0.10
Nodes (37): ContainerData, ContainerDataExtras, Container data class for persistence operations., Optional payload and timestamps for a container row., Data class for container information., Convert container data to dictionary. Returns dictionary with model field names…, _build_container_data_from_row_async(), get_containers_by_entity_id_async() (+29 more)

### Community 519 - "get_help_content"
Cohesion: 0.10
Nodes (22): get_command_categories(), get_commands_by_category(), _get_general_help(), get_help_content(), Any, Help content and command documentation for MythosMUD. This module contains the…, Get help content for commands. Args: command_name: Optional specific command…, Get general help content with command categories. (+14 more)

### Community 520 - "properties"
Cohesion: 0.08
Nodes (24): properties, description, maxLength, minLength, type, description, pattern, type (+16 more)

### Community 521 - "convert_uuids_to_strings"
Cohesion: 0.11
Nodes (23): convert_uuids_to_strings(), Recursively convert UUID objects to strings for JSON serialization. Args: obj:…, Test convert_uuids_to_strings() converts UUIDs in dict., Test convert_uuids_to_strings() converts UUIDs in list., Test convert_uuids_to_strings() converts UUID object., Test convert_uuids_to_strings() converts UUIDs in nested structures., test_convert_uuids_to_strings_dict(), test_convert_uuids_to_strings_list() (+15 more)

### Community 522 - "test_lint_container_get_instance.py"
Cohesion: 0.10
Nodes (26): _LintContainerGetInstanceModule, _load_script(), Protocol, Unit tests for scripts/lint_container_get_instance.py. Verifies the detection…, A file with more get_instance() calls than its allowlist entry expects fails --…, A file with fewer get_instance() calls than its allowlist entry expects fails…, An allowlist entry for a file with zero remaining hits (fully migrated) must…, A blank line inserted above the allowlisted site must not trip a violation --… (+18 more)

### Community 523 - "Async Remediation Final Report"
Cohesion: 0.07
Nodes (29): 48 Sync Persistence Call Instances, Async Remediation Final Report, All async anti-patterns have been exorcised from the codebase, All Targets Met, API/Commands (2 files), Checklist, ✅ COMPLETE - ALL 48 INSTANCES MIGRATED, Core Infrastructure (2 files) (+21 more)

### Community 524 - "🔴 CRITICAL ISSUES"
Cohesion: 0.07
Nodes (28): 10. Use of `BETWEEN` with Integer Ranges, 11. Missing Indexes on Foreign Keys, 12. Inconsistent Constraint Naming, 13. Mixed Case in Table/Column Names, 14. Missing `UNIQUE` Constraints Where Appropriate, 15. Inconsistent Use of `NOT NULL` Constraints, 16. Missing Documentation for Complex Constraints, 1. Use of `serial`/`SERIAL` Instead of `bigint generated always as identity` (+20 more)

### Community 525 - "Test Suite Quality Audit - Executive Summary"
Cohesion: 0.07
Nodes (29): **25-30% (~1,250-1,500 tests) provide CRITICAL regression protection**, Answer to Original Question, Breakdown, By Category, CI/CD Time Saved, Commit to full 2-month optimization plan, Comparison to Industry Benchmarks, Created Documents (+21 more)

### Community 526 - "test_inventory_command_prototype.py"
Cohesion: 0.14
Nodes (25): _first_normalized_wear_slot(), infer_equip_slot_from_prototype(), _inventory_prototype_id(), prototype_from_registry(), prototype_registry_from_request(), Prototype registry access and equip-slot inference for inventory items., Resolve prototype registry from FastAPI-style request (agent-readable…, Return the prototype object for ``prototype_id``, or None if missing or invalid. (+17 more)

### Community 527 - "properties"
Cohesion: 0.09
Nodes (23): $ref, $ref, minimum, type, minimum, type, minimum, type (+15 more)

### Community 528 - "PassiveMobNPC"
Cohesion: 0.04
Nodes (59): PassiveMobNPC, Check if idle movement should be scheduled based on configuration and timing.…, Create a WANDER action message. Args: current_time: Current timestamp Returns:…, Queue a WANDER action via the thread manager. Args: wander_action: The wander…, Schedule a WANDER action for idle movement if interval has elapsed. This method…, Respond to player interaction., Handle wandering action., Handle responding to greeting action. (+51 more)

### Community 529 - "NATSConnectionStateMachine"
Cohesion: 0.08
Nodes (14): NATSConnectionStateMachine, Initialize connection state machine. Args: connection_id: Unique identifier for…, Handler for connect transition. Resets reconnection counter and prepares for…, Handler for successful connection. Records connection time and increments…, Handler for disconnection. Increments disconnection counter. AI: Track…, Handler for starting reconnection. Checks if circuit breaker should be…, Handler for circuit breaker opening. Logs circuit open event for alerting. AI:…, Handler for circuit breaker closing. Resets failure counters. AI: Circuit… (+6 more)

### Community 530 - "test_lifespan_event_subscriptions.py"
Cohesion: 0.16
Nodes (20): Event subscription setup for application startup. Extracted from…, Subscribe to RoomOccupantsRefreshRequested so Occupants panel updates after NPC…, Subscribe to room events for quest triggers and progress (start on enter,…, subscribe_quest_events(), subscribe_room_occupants_refresh(), QuestCompleted, Event fired when a quest instance is completed (rewards applied, state set to…, asyncio (+12 more)

### Community 531 - "handle_logout_command"
Cohesion: 0.09
Nodes (27): _get_app_services(), handle_logout_command(), handle_quit_command(), _is_player_in_combat_for_logout(), Player, Request, Check whether `player` is currently in combat, for the quit/logout combat…, Handle the quit command for disconnecting from the game. Args: command_data:… (+19 more)

### Community 532 - "test_chat_moderation.py"
Cohesion: 0.11
Nodes (20): moderation(), player_service(), asyncio, fixture, Unit tests for chat moderation operations., test_add_admin_returns_true(), test_get_mute_status_handles_internal_error(), test_get_mute_status_includes_player_name() (+12 more)

### Community 533 - "test_lint_raw_sql_in_python.py"
Cohesion: 0.10
Nodes (25): _LintRawSqlModule, _load_script(), MonkeyPatch, Path, Protocol, Unit tests for scripts/lint_raw_sql_in_python.py. Verifies the detection logic…, server/ must have zero raw-SQL sites -- the migration completed under #633., Typed surface of the loaded script, for the parts these tests exercise. (+17 more)

### Community 534 - "Bug Investigator Subagent"
Cohesion: 0.07
Nodes (27): Authentication/Login Issues, Best Practices, Bug Investigator Subagent, Capabilities, Chat/Communication Issues, Critical Requirements, Evidence Collection, Evidence Standards (+19 more)

### Community 535 - "Code Review: Import Analysis and Anti-Patterns"
Cohesion: 0.07
Nodes (29): F-String Logging Anti-Pattern, Code Review Import Analysis, 1. **Import Inconsistency in `server/persistence.py`**, 2. **Import Organization Pattern**, Additional Findings, Best Practices Analysis, Code Review: Import Analysis and Anti-Patterns, Conclusion (+21 more)

### Community 536 - "Domain Model Anemic Anti-Pattern Audit"
Cohesion: 0.07
Nodes (27): 1. Already Addressed (Prior Work), 2.1 Player Death Service – DP Decay, 2.2 Combat Turn Processor – “Can Act” Checks, 2.3 Combat HP Sync – Death Threshold Logic, 2.4 Combat Persistence Handler – Same Patterns, 2.5 Player Respawn Service – Stats Restoration, 2. High Priority – Domain Logic in Services, 3.1 Wearable Container Service – Capacity Checks (+19 more)

### Community 537 - "session_factory"
Cohesion: 0.12
Nodes (24): FixtureRequest, Database fixtures for integration tests. This module provides database…, _assert_allowed_integration_test_db(), db_cleanup(), _delete_mutable_integration_test_rows(), _get_db_name_from_url(), integration_db_url(), integration_engine() (+16 more)

### Community 538 - "test_connection_room_utils.py"
Cohesion: 0.16
Nodes (13): Remove a player from all room subscriptions and occupant lists (compatibility…, prune_player_from_all_rooms_impl(), Any, Ensure room_occupants only contains currently online players., Remove a player from all room subscriptions and occupant lists., reconcile_room_presence_impl(), Unit tests for connection room utils. Tests the connection_room_utils module…, Test canonical_room_id_impl() handles DatabaseError. (+5 more)

### Community 539 - "zone_schema.json"
Cohesion: 0.22
Nodes (8): zone_type, additionalProperties, description, environment, required, $schema, title, type

### Community 540 - "ErrorMonitor"
Cohesion: 0.13
Nodes (17): ErrorMonitor, main(), Any, datetime, Path, Detect error trends over time. Returns trend analysis results., Check for alert conditions. Returns list of active alerts., Monitor errors continuously for a specified duration. Args: log_dir: Directory… (+9 more)

### Community 541 - "verify_linting_parity.py"
Cohesion: 0.15
Nodes (27): check_alignment(), _check_pylint_suppressions(), _check_ruff_suppressions(), find_suppressions(), _has_pylint_equivalent(), _has_ruff_equivalent(), main(), parse_pylint_suppression() (+19 more)

### Community 542 - "handle_skills_command"
Cohesion: 0.14
Nodes (21): _format_skills_output(), _get_container_services(), handle_skills_command(), Any, UUID, Get container, persistence, and skill_service from request, or None if…, Extract and validate player_id from player object, returning UUID or None., Resolve user_id from current_user (auth user) or fallback to player.user_id. (+13 more)

### Community 543 - "test_npc_combat_integration_service_player_attacks.py"
Cohesion: 0.04
Nodes (63): mock_async_persistence(), mock_combat_service(), mock_connection_manager(), mock_messaging_integration(), asyncio, Unit tests for NPC combat integration service - NPC-initiated aggro combat…, Test handle_npc_attack_on_player returns False when NPC instance cannot be…, Test handle_npc_attack_on_player returns False when NPC is dead. (+55 more)

### Community 544 - "RoomEventHandler"
Cohesion: 0.05
Nodes (56): initialize_connection_cleaner(), initialize_connection_state(), initialize_error_handler(), initialize_game_state_provider(), initialize_health_monitor(), initialize_messaging(), initialize_room_event_handler(), Any (+48 more)

### Community 545 - "validate_secure_path"
Cohesion: 0.08
Nodes (24): Validate and sanitize a user-provided path to prevent path traversal attacks.…, validate_secure_path(), Test validate_secure_path detects when common_path != base_path (lines 59-66)., Test validate_secure_path with valid path., Test validate_secure_path handles different drives on Windows., Test validate_secure_path rejects path traversal with .., Test validate_secure_path rejects path traversal with ~, Test validate_secure_path with nested valid path. (+16 more)

### Community 546 - "test_quest_service_collect.py"
Cohesion: 0.13
Nodes (27): _make_collect_quest_row(), _make_inventory_player(), mock_def_repo(), mock_instance_repo(), asyncio, fixture, _quest_service_with_persistence(), Unit tests for QuestService collect_n sync, auto-complete, and turn-in… (+19 more)

### Community 547 - "test_combat_death_handler.py"
Cohesion: 0.13
Nodes (22): combat(), combat_service(), handler(), npc_target(), player_target(), asyncio, fixture, patch (+14 more)

### Community 548 - "server/tests/conftest.py"
Cohesion: 0.10
Nodes (26): Config, Item, _apply_path_based_markers(), _create_test_event_loop(), deterministic_random_seed(), ensure_test_environment_variables(), _get_db_name_from_url(), AbstractEventLoop (+18 more)

### Community 549 - "test_emote.py"
Cohesion: 0.10
Nodes (22): Emote, Base, Predefined emote definitions., Unit tests for emote models. Tests the Emote and EmoteAlias SQLAlchemy models., Test EmoteAlias aliases are case sensitive., Test Emote can be instantiated with required fields., Test Emote has correct table name., Test Emote __repr__ method. (+14 more)

### Community 550 - "CorruptionService"
Cohesion: 0.16
Nodes (31): CorruptionService, High-level operations for corruption adjustments. The single write path for…, _async_session_gen(), _clear_tier_cache(), mock_repo(), persistence(), _player(), asyncio (+23 more)

### Community 551 - "debugLogger"
Cohesion: 0.13
Nodes (5): debugLogger, LogConfig, LogEntry, LogLevel, mockConsole

### Community 552 - "Communities (19 total, 4 thin omitted)"
Cohesion: 0.07
Nodes (26): Ambiguous Edges - Review These, Communities (19 total, 4 thin omitted), Community 0 - "Yog-Sothoth Keeper Decks", Community 10 - "Tsathoggua Formless Spawn", Community 11 - "Ygolonac and Xiclotl", Community 12 - "Nyogtha Spawn", Community 13 - "Hastur Spawn", Community 14 - "Fthagghua Fire Vampires" (+18 more)

### Community 553 - "properties"
Cohesion: 0.16
Nodes (23): type, type, properties, null, type, type, type, down (+15 more)

### Community 554 - "packages/README.md"
Cohesion: 0.11
Nodes (22): API OpenAPI/Swagger Specification, Command Handler Patterns, Command Models Reference, Command Security Guide, Command Testing Guide, Configuration Files Reference, ConnectionManager Modular Architecture, Container Injection Audit (+14 more)

### Community 555 - "Persistence Layer Refactoring - COMPLETE ✅"
Cohesion: 0.07
Nodes (27): Backward Compatibility, 📈 Benefits, Code Created, 🎉 Conclusion, Directory Structure, Documentation Created, 📚 Documentation Index, 📊 Final Metrics (+19 more)

### Community 556 - "enum"
Cohesion: 0.20
Nodes (10): city, countryside, desert, mountains, swamp, tundra, zone_type, description (+2 more)

### Community 557 - "LogAnalyzer"
Cohesion: 0.12
Nodes (16): LogAnalyzer, main(), Any, Path, Detect error trends over time. Returns trend analysis results., Find all error log files in the directory., Parse a log file and extract error information., Parse a single log line and extract error information. (+8 more)

### Community 558 - "quality_fragmentation_ai_guardrails.py"
Cohesion: 0.15
Nodes (25): _build_python_call_usage_map(), _call_target_name(), _check_exports_and_tiny_functions(), _check_single_use_file(), _collect_code_texts(), _collect_python_public_defs_and_tiny(), _guardrail_scan_inputs(), _is_public_function_stmt() (+17 more)

### Community 559 - "safe_run_static"
Cohesion: 0.06
Nodes (42): get_project_root(), Determine the project root based on current working directory, main(), Run a psql command and return the result., Load all seed data files., run_psql_command(), Read process output in background thread., read_output() (+34 more)

### Community 560 - "_NPCCombatIntegrationValidationDeps"
Cohesion: 0.09
Nodes (19): _coerce_xp_mapping_value(), _NPCCombatIntegrationValidationDeps, Protocol, UUID, Validate that player and NPC are in the same room., End any active combat that includes this player when room validation fails., Convert string IDs to UUIDs and set up XP mappings., Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid,… (+11 more)

### Community 561 - "._create_grid_map"
Cohesion: 0.09
Nodes (12): Any, Extract street name from room ID. Args: room_id: Full room ID Returns: Street…, Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…, Render the mini-map as ASCII art with grid-based visualization. Args:…, Create a grid-based map visualization. Args: nodes: List of room nodes edges:…, Assign grid coordinates to rooms based on connectivity. Args: nodes: List of…, Get coordinates for the next room based on direction. Args: x: Current x…, Reverse a direction. Args: direction: Original direction Returns: Reversed… (+4 more)

### Community 562 - "test_look_item_helpers.py"
Cohesion: 0.05
Nodes (49): _find_item_in_room_drops(), Find an item in room drops by name or prototype_id. Args: room_drops: List of…, Unit tests for look item helper functions. Tests the helper functions in…, Test _find_item_in_room_drops() with instance number out of range., Test _find_item_in_room_drops() finds item by name., Test _find_item_in_room_drops() with instance number zero., Test _find_item_in_equipped() with empty dict., Test _find_item_in_equipped() with no matching items. (+41 more)

### Community 563 - "MetricsCollector"
Cohesion: 0.06
Nodes (22): HolidayResolver, Lock, MetricsCollector, Any, Record a circuit breaker state change. Args: old_state: Previous circuit state…, Record message processing time. Args: duration_ms: Processing duration in…, Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…, Reset all metrics counters. Useful for clearing metrics after a deployment or… (+14 more)

### Community 564 - "attach_compatibility_properties"
Cohesion: 0.12
Nodes (25): attach_compatibility_properties(), _attach_connection_properties(), _attach_message_properties(), _attach_room_properties(), _create_property_with_accessors(), Any, Compatibility helpers for connection manager. This module provides…, Create getter, setter, and deleter functions for a property. Args: getter_attr:… (+17 more)

### Community 565 - "test_passive_corruption_flux_service.py"
Cohesion: 0.14
Nodes (30): FluxRoom, CorruptionUpdateResult, Normalized response describing the outcome of a corruption adjustment., _make_service(), _player(), asyncio, Unit tests for PassiveCorruptionFluxService (#815 PR-5)., A DB override still applies when the room authored neither rate nor target… (+22 more)

### Community 566 - "extract_player_name"
Cohesion: 0.13
Nodes (25): extract_player_name(), _get_name_from_user(), get_player_position(), _is_uuid_string(), _is_valid_name(), Any, Player, UUID (+17 more)

### Community 567 - "test_health_monitor.py"
Cohesion: 0.04
Nodes (52): HealthMonitor, Any, UUID, Find player_id for cleanup when metadata is missing., Check if connection is stale based on timeout., Check if WebSocket is actually open., Validate token and update last validation time if needed., Process health check for a single connection. (+44 more)

### Community 568 - "test_connection_session_management.py"
Cohesion: 0.05
Nodes (73): _disconnect_all_connections_for_session(), _disconnect_connection_for_session(), _is_websocket_connected(), WebSocket, Disconnect all connections for a new game session. Args: connection_ids: List…, Check if a WebSocket is connected. Args: websocket: The WebSocket to check…, Disconnect a single connection for a new game session. Args: connection_id: The…, _as_mgr() (+65 more)

### Community 569 - "waitForMessage"
Cohesion: 0.18
Nodes (24): ADMIN_SET_SUCCESS, assertLookVisible(), prepAwForCorruptionTest(), seedCorruption(), ADR-0025, despawnArmitage(), DIALOGUE, ensureArmitagePresent() (+16 more)

### Community 570 - "Path"
Cohesion: 0.14
Nodes (11): Path, Fix self-references by adding proper flags. Args: room_database: Complete room…, Find the file for a room. Returns None if file doesn't exist., Create backup if requested., Initialize the room fixer. Args: base_path: Base directory for room files, Save fixed room if changes were made., Fix basic schema issues. Args: room_database: Complete room database…, Create a backup of a room file. Args: file_path: Path to the file to backup… (+3 more)

### Community 571 - "test_report_any_baseline.py"
Cohesion: 0.20
Nodes (20): _load_script_module(), CaptureFixture, fixture, MonkeyPatch, Path, Protocol, Tests for scripts/report_any_baseline.py (#784). This script is the burn-down…, The two parameter rules close the laundering path; dropping them re-opens it. (+12 more)

### Community 572 - "test_support_helpers.py"
Cohesion: 0.15
Nodes (18): async_mock_of(), calls_of(), mock_of(), T, Typed mock helpers shared across the server test suite (#784).…, A ``MagicMock`` restricted to ``cls``'s interface, typed as ``cls``.…, ``mock_of`` for classes whose methods are coroutines.…, Recover the ``MagicMock`` assertion API from a double typed as its subject. The… (+10 more)

### Community 573 - "Dream Messaging Subsystem Design"
Cohesion: 0.10
Nodes (19): 1. Overview, 2. Architecture — Phase 1 (`/sleep`), 3. Key design decisions, 4. Constraints, 5. Roadmap — Phase 2: Dreamlands plane, 6. Roadmap — Phase 3: status-effect-driven waking dreams, 7. Related docs, 8. Changelog (+11 more)

### Community 574 - "Uvicorn/ASGI Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.08
Nodes (26): 1. Deprecated `asyncio.get_event_loop()` Usage, 1. Proper Connection Pool Management, 2. Good Error Handling Patterns, 2. SQL Injection Risk in Field Name Construction, 3. Async/Await Usage, 3. Connection Pool Cleanup Verification, 4. Blocking Operations in Async Context, 4. Security Considerations (+18 more)

### Community 575 - ".get_stats"
Cohesion: 0.10
Nodes (11): Get player stats as dictionary. Returns a MutableDict instance that…, Set player stats from dictionary. Accepts both plain dict and MutableDict…, Check if player is alive (DP > 0)., Check if player is mortally wounded (0 >= DP > -10). Returns: True if player…, Check if player is dead (DP <= -10). Returns: True if player has -10 DP or below, Get player's current health state. Returns: "alive" if DP > 0…, Get stats used for combat participant creation. Returns current_dp, max_dp, and…, Get player determination points (DP) as percentage. (+3 more)

### Community 576 - "test_load_world_seed.py"
Cohesion: 0.12
Nodes (25): regression, _load_script_module(), _LoadWorldSeedScriptInternals, LoadWorldSeedTestApi, CaptureFixture, fixture, MonkeyPatch, Protocol (+17 more)

### Community 577 - "handle_emote_command"
Cohesion: 0.13
Nodes (24): _extract_emote_action(), _format_emote_messages(), _get_emote_services(), handle_emote_command(), _handle_emote_result(), Any, Emote command handlers for MythosMUD. This module contains handlers for the…, Handle the result from chat service after sending emote. Args: result: Result… (+16 more)

### Community 578 - "test_chat_validator.py"
Cohesion: 0.14
Nodes (24): contains_malicious_content(), Chat message validation utilities. This module provides validation functions…, Validate chat message before transmission. Args: chat_message: The chat message…, Validate sender has access to the room. Args: sender_id: ID of the message…, Check for malicious content patterns. Args: content: The message content to…, validate_chat_message(), validate_room_access(), _message() (+16 more)

### Community 579 - ".load_from_path"
Cohesion: 0.31
Nodes (5): Any, Path, ValidationError, Get all invalid entries that failed validation. Returns: list[dict]: List of…, Load prototypes from a directory of JSON files.

### Community 580 - "PlayerEffectRepository"
Cohesion: 0.05
Nodes (55): PlayerEffect, Base, Persistent player effect (status effect) with tick-based duration. Table:…, _add_effect_params(), AddEffectInput, _int_opt(), _opt_str(), PlayerEffectRepository (+47 more)

### Community 581 - "test_audit_suppressions.py"
Cohesion: 0.16
Nodes (18): audit_api_module_scope(), _AuditModule, AuditTestApi, _load_script_module(), fixture, Protocol, Tests for scripts/audit_suppressions.py (#784 changes). Two defects were fixed:…, Public surface of scripts/audit_suppressions.py used by these tests. (+10 more)

### Community 582 - "_asyncio_mark"
Cohesion: 0.12
Nodes (23): _asyncio_mark, _await_shutdown_result(), Test handle_shutdown_command() when player service is not available., Test handle_shutdown_command() when player is not found., Test handle_shutdown_command() when player lacks admin permission., Test handle_shutdown_command() with invalid parameters., Test handle_shutdown_command() with cancel action., Test handle_shutdown_command() with cancel when no active shutdown. (+15 more)

### Community 583 - ".claude/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 584 - "Client Test Remediation"
Cohesion: 0.15
Nodes (11): Client Test Remediation — Reference, 🔴 Critical — TypeScript/rendering errors, Debugging when a fix doesn't take, Fix patterns by tier, 🟡 High — component issues, 🟢 Medium — hook/async issues, Client Test Remediation, Entry point (+3 more)

### Community 585 - "FeedbackManager"
Cohesion: 0.15
Nodes (4): FeedbackData, FeedbackManager, FeedbackStats, useFeedbackManager()

### Community 586 - ".cursor/hooks/record_edited_file.py"
Cohesion: 0.13
Nodes (24): _is_agent_config_path(), _is_client_test_path(), _is_server_test_path(), _is_test_file(), _load_payload(), _load_state(), main(), _normalize_path() (+16 more)

### Community 587 - "Migration Strategy"
Cohesion: 0.08
Nodes (24): Access Patterns, App.State to Dependency Injection Migration Plan, Current State Analysis, Dependencies, Dependency Injection Pattern, Estimated Effort, Implementation Guidelines, Migration Strategy (+16 more)

### Community 588 - "Async Facades Implementation - COMPLETE ✅"
Cohesion: 0.08
Nodes (25): (A) and (B) Relationship: **Complementary**, (A) AsyncPersistenceLayer Integration ✅, Async Facades Implementation - COMPLETE ✅, Async Tests, (B) Sync Shim - NOT NEEDED ⏭️, Benefits Achieved, Both facades are now operational, Conclusion (+17 more)

### Community 589 - "Feature Requirements Document: Random Stats Generator"
Cohesion: 0.08
Nodes (24): 1. Registration Process, 2. Stats Rolling Process, 3. Error Handling, Acceptance Criteria, Backend Requirements, Dependencies, Feature Requirements Document: Random Stats Generator, Frontend Requirements (+16 more)

### Community 590 - "Migration 019: Complete Implementation Summary"
Cohesion: 0.08
Nodes (25): 1. Database Schema Updates ✅, 2. Python Model Updates ✅, 3. Migration Script Created ✅, 4. Testing Infrastructure ✅, Before Production, Conclusion, Created Files (5), Documentation Files (4) (+17 more)

### Community 591 - "Persistence Layer Async Migration Plan"
Cohesion: 0.08
Nodes (25): Aggressive Timeline (Focused Migration), Conclusion, Conservative Timeline (Gradual Migration), Decision Points, Emergency Rollback, Individual File Rollback, Metrics to Track, Migration Timeline (+17 more)

### Community 592 - "Phase 4: Recommendations"
Cohesion: 0.08
Nodes (25): 1. Prune Infrastructure Tests (Save ~3 minutes, Remove ~350 tests), 2. Consolidate Coverage Tests (Save ~1 minute, Reduce ~60 tests), 3. Parametrize Repetitive Tests (Save ~1 minute, Reduce ~300 tests), 4.1 Pruning Candidates (750 tests, ~5 minutes savings), 4.2 Consolidation Opportunities, 4.3 Coverage Gap Identification, 4.4 Optimization Recommendations, 4. Migrate Model Tests to Property-Based Testing (+17 more)

### Community 593 - "fix_fstring_logging.py"
Cohesion: 0.12
Nodes (24): _build_structured_params(), _clean_message(), _create_replacement_for_fstring(), create_structured_log_message(), extract_variables_from_fstring(), fix_fstring_logging_in_file(), _handle_no_variables_case(), main() (+16 more)

### Community 594 - "Stop-MythosMudProjectProcessTree"
Cohesion: 0.12
Nodes (23): Get-MythosMudProtectedDevToolPattern(), Get-MythosMudRepoRoot(), Stop-MythosMudProjectProcessTree(), Stop-MythosMudProjectProcessTreeInternal(), Test-MythosMudProjectProcess(), Test-MythosMudProtectedDevToolProcess(), Find-NatsServerInstallation(), Get-NatsServerPath() (+15 more)

### Community 595 - "TestRunner"
Cohesion: 0.12
Nodes (13): main(), Path, Verify test database configuration. Note: For PostgreSQL databases, schema is…, Build the pytest command with proper configuration. Args: test_paths: List of…, Run the test suite with proper configuration. Args: test_paths: List of test…, Run integration tests only., Run all tests (unit, integration, but not E2E by default)., Generate coverage report only. (+5 more)

### Community 596 - "._bind_event_type"
Cohesion: 0.07
Nodes (20): Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type., Initialize the event with proper type. (+12 more)

### Community 597 - "test_chat_pose_helpers.py"
Cohesion: 0.16
Nodes (25): clear_player_pose(), get_player_pose(), get_room_poses(), normalize_player_id(), Any, UUID, Pose management helpers for chat service., Clear a player's pose. Args: player_id: ID of the player pose_manager: Pose… (+17 more)

### Community 598 - "BehaviorEngine"
Cohesion: 0.02
Nodes (121): BehaviorEngine, Any, Get all behavior rules., Evaluate equality condition (==). Returns: bool if condition matches, None if…, Evaluate inequality condition (!=). Returns: bool if condition matches, None if…, Evaluate numeric comparison conditions (>=, <=, >, <). Args: condition:…, Try multiple evaluator methods in sequence. Args: condition: Condition string…, Evaluate boolean conditions and variable lookups. Args: condition: Condition… (+113 more)

### Community 599 - "test_channel_broadcasting_strategies.py"
Cohesion: 0.11
Nodes (26): asyncio, Unit tests for channel broadcasting strategies. Tests the…, When party_service is missing on handler, no message is sent., When party does not exist, no message is sent., Test PartyChannelStrategy.broadcast() handles missing party_id., Test WhisperChannelStrategy.broadcast() sends personal message., Test WhisperChannelStrategy.broadcast() handles missing target_player_id., Test SystemAdminChannelStrategy.broadcast() broadcasts globally. (+18 more)

### Community 600 - "PerformanceTester"
Cohesion: 0.19
Nodes (7): ExtendedPerformance, PerformanceMemory, PerformanceTestConfig, PerformanceTester, PerformanceTestResult, usePerformanceTester(), ExtendedPerformance

### Community 601 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test handling item look when item is in room drops., Test handling item look when item is in inventory., Test handling item look when item is equipped., Test handling item look when item not found., Test handling item look with look_in flag skips equipped items., Test trying implicit lookup when item is in room drops., Test trying implicit lookup when item not found. (+17 more)

### Community 602 - "active_lucidity_service.py"
Cohesion: 0.11
Nodes (17): EncounterProfile, LucidityActionError, Any, AsyncSession, datetime, RuntimeError, UUID, Active LCD adjustment helpers for encounters and recovery rituals. (+9 more)

### Community 603 - "StatisticsAggregator"
Cohesion: 0.04
Nodes (51): MemoryStatsSnapshot, TypedDict, UUID, Assemble memory stats from a snapshot dict (keeps call sites param-stable)., Count active connections not tied to any online player., Build the connections subsection of memory stats., Build the sessions subsection of memory stats., Expose memory monitor configuration knobs for stats payload. (+43 more)

### Community 604 - "test_command_factories_inventory_helpers.py"
Cohesion: 0.10
Nodes (20): Unit tests for inventory command factory helper functions. Tests the helper…, Test create_equip_command() with item name and inferred slot., Test create_unequip_command() with slot., Test create_unequip_command() with item name., Test create_inventory_command() creates InventoryCommand., Test create_inventory_command() raises error with args., Test create_pickup_command() raises error for invalid quantity., Test create_pickup_command() raises error for invalid index. (+12 more)

### Community 605 - "ValidationRule"
Cohesion: 0.06
Nodes (24): Path, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a sub-zone configuration against its schema. Args: config_data: Sub-…, Validate a zone configuration against its schema. Args: config_data: Zone…, Initialize the schema validator. Args: schema_path: Path to the JSON schema file, Load and cache the JSON schema., Validate a single room against the schema. Args: room_data: Room data to… (+16 more)

### Community 606 - "test_request_schema_security.py"
Cohesion: 0.12
Nodes (23): APIRoute, BaseRoute, _all_route_reachable_models(), _iter_api_routes(), _iter_body_models(), _iter_nested_models(), BaseModel, Protocol (+15 more)

### Community 607 - "SQLAlchemyAsyncLinter"
Cohesion: 0.11
Nodes (18): Await, lint_directory(), lint_file(), main(), Call, Import, ImportFrom, Path (+10 more)

### Community 608 - "Test Suite Analyzer Subagent"
Cohesion: 0.08
Nodes (23): Best Practices, Capabilities, Coverage Analysis, Coverage Gap Analysis, Coverage Requirements, Critical Files Requiring High Coverage, Critical Path Coverage, Example Scenarios (+15 more)

### Community 609 - "properties"
Cohesion: 0.10
Nodes (21): maxLength, minLength, type, properties, maxLength, minLength, type, maxLength (+13 more)

### Community 610 - "Onboard Skill"
Cohesion: 0.08
Nodes (24): Onboard Skill, Assess Onboarding Needs, Context Over Ceremony, Contextual Help, Design Onboarding Experiences, Documentation & Help, Empty State Design, Feature Discovery & Adoption (+16 more)

### Community 611 - "DialogueEditorPage.tsx"
Cohesion: 0.16
Nodes (18): baseUrl(), buildHeaders(), deleteDialogueDefinition(), DialogueDefinitionDto, DialogueNodeDto, DialogueOptionDto, DialogueTreeDto, listDialogueDefinitions() (+10 more)

### Community 612 - "multiplayer-browser-helpers.bundle.js"
Cohesion: 0.16
Nodes (20): buttonHasLoginSubmitLabel(), coalesce(), computedStyleHidesElement(), elementTextIncludesGameInfo(), fieldHasCommandPlaceholder(), getBodyInnerText(), hasCommandInputInBrowser(), hasGameInfoAnyMessageInBrowser() (+12 more)

### Community 613 - "compilerOptions"
Cohesion: 0.13
Nodes (14): compilerOptions, allowImportingTsExtensions, composite, noEmit, rootDir, typeRoots, types, exclude (+6 more)

### Community 614 - "Dependency Upgrade Strategy Specification"
Cohesion: 0.08
Nodes (23): argon2-cffi (23.1.0 → 25.1.0), Automated Testing, Critical Dependencies Requiring Special Attention, Deliverables, Dependency Upgrade Strategy Specification, During Upgrade, Implementation Phases, Manual Validation (+15 more)

### Community 615 - "NATS Anti-Patterns and Best Practices Review"
Cohesion: 0.08
Nodes (24): 10. **Missing Connection Health Monitoring in Broker** (Observability), 1. **Synchronous Operations in Non-Handler Context** (Low Priority), 2. **Event Handler Callbacks May Block** (Anti-pattern), 3. **Inconsistent Error Handling Patterns** (Code Quality), 4. **Missing Input Validation in Some Methods** (Security/Reliability), 5. **Subject Naming: Potential for Too Broad Wildcards** (Anti-pattern), 6. **Connection Pool Error Handling** (Resilience), 7. **Message Acknowledgment: Manual Ack Not Default** (Reliability) (+16 more)

### Community 616 - "format_markdown_file"
Cohesion: 0.12
Nodes (23): fix_blank_lines_after_headings(), fix_bold_items_without_list_marker(), fix_checklist_items(), fix_checkmark_items(), fix_code_block_spacing(), fix_heading_trailing_colons(), fix_items_after_headings(), fix_plain_text_after_colons() (+15 more)

### Community 617 - "migrate_rooms.py"
Cohesion: 0.12
Nodes (23): _create_backup(), create_subzone_config(), _create_subzone_structure(), create_zone_config(), _create_zone_structure(), determine_zone_type(), _group_rooms_by_zone(), _load_and_validate_rooms() (+15 more)

### Community 618 - "handle_teach_command"
Cohesion: 0.18
Nodes (22): _format_teach_result(), _get_teach_services(), handle_teach_command(), Any, Teach command handler for learning spells from NPC teachers. This module…, Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…, _resolve_npc_teacher(), asyncio (+14 more)

### Community 619 - "ContainerTransferToMixin"
Cohesion: 0.20
Nodes (13): ContainerTransferToMixin, InventoryStack, Player, UUID, Best-effort audit log for transfer-to-container (must not fail the transfer)., Add a stack via InventoryService; map capacity failures to…, Load player or raise ValidationError for transfer ops., Load and validate container component for transfer-to. (+5 more)

### Community 620 - "_validate_command_basics"
Cohesion: 0.12
Nodes (12): Validate basic command requirements. Returns result dict if invalid, None if…, _validate_command_basics(), Test _validate_command_basics returns result for empty command., Test _validate_command_basics returns result for command too long., Test _validate_command_basics returns result for invalid content., Test _validate_command_basics returns None for valid command., Test _validate_command_basics function., Test _validate_command_basics returns result for empty command. (+4 more)

### Community 621 - "test_inventory_mutation_guard.py"
Cohesion: 0.07
Nodes (29): guard(), asyncio, fixture, Unit tests for inventory mutation guard - core functionality. Tests…, Test acquire_async without token allows mutation., Test acquire_async with unique token allows mutation., Test acquire_async with duplicate token suppresses mutation., Test acquire_async allows same token for different players. (+21 more)

### Community 622 - "playerHandlers.ts"
Cohesion: 0.14
Nodes (23): handlePlayerDeliriumRespawned(), handlePlayerDied(), handlePlayerDpUpdated(), handlePlayerEntered(), handlePlayerEnteredGame(), handlePlayerLeft(), handlePlayerLeftGame(), handlePlayerRespawned() (+15 more)

### Community 623 - "lifespan.py"
Cohesion: 0.08
Nodes (48): _calculate_metrics_delta(), _cleanup_container_on_error(), _cleanup_dead_letter_queue_periodically(), _initialize_enhanced_systems(), lifespan(), _log_memory_metrics_periodically(), _persist_metrics_to_file(), _persist_mythos_state_on_error() (+40 more)

### Community 624 - "test_room_subscription_manager_npcs.py"
Cohesion: 0.09
Nodes (23): asyncio, fixture, Unit tests for room subscription manager NPC helpers. Tests NPC-related helpers…, Test get_room_occupants() includes NPCs from lifecycle manager., Test get_room_occupants() falls back to room.get_npcs() when lifecycle manager…, Create a RoomSubscriptionManager instance., Test _get_npc_name_from_lifecycle_manager gets NPC name., Test _get_npc_name_from_lifecycle_manager returns ID when NPC not found. (+15 more)

### Community 625 - "properties"
Cohesion: 0.06
Nodes (32): description, minimum, type, description, minimum, type, description, maxLength (+24 more)

### Community 626 - "security.ts"
Cohesion: 0.07
Nodes (24): SafeHtml(), SafeHtmlProps, useCommandHandlers(), UseCommandHandlersParams, collectWindowCandidates(), COMMAND_PROBE_CONFIG, DOMPurifyInstance, getDomPurify() (+16 more)

### Community 627 - "ADR-012: python-statemachine for Backend Connection FSM"
Cohesion: 0.09
Nodes (22): ADR-011: XState for Frontend Connection State Machine, ADR-012: python-statemachine for Backend Connection FSM, 10. Related ADRs, 11. Changelog, 1. Overview, 2. Context and Problem Statement, 3. Decision Drivers, 4. Considered Options (+14 more)

### Community 628 - "MythosMUD Code Quality Targets for AI"
Cohesion: 0.09
Nodes (23): MythosMUD Code Quality AI Skill, `__all__` for public modules, As You Touch, Client return types (TypeScript), Complexity policy, Docstrings (D), High Priority, Medium Priority (+15 more)

### Community 629 - "MythosMUD Database Placement"
Cohesion: 0.09
Nodes (23): Database Placement Skill, Allowed Paths Only, Data Types, Forbidden, MythosMUD Database Placement, PostgreSQL Access (Procedures and Functions), Reference, When Adding or Moving Persistence (+15 more)

### Community 630 - "dependencies"
Cohesion: 0.09
Nodes (23): dependencies, dompurify, lucide-react, react, react-dom, react-grid-layout, react-rnd, react-router-dom (+15 more)

### Community 631 - "EdgeDetailsPanel.tsx"
Cohesion: 0.11
Nodes (15): buildEdgeFieldModel(), EdgeAdminActionsProps, EdgeDeleteConfirmProps, EdgeDetailRow(), EdgeDetailRowProps, EdgeDetailsFields(), EdgeDetailsFieldsProps, EdgeDetailsPanel() (+7 more)

### Community 632 - "MUD Disconnect Grace Period & Rest Command: Industry Comparison"
Cohesion: 0.33
Nodes (5): 11. Missing Features from Other MUDs, Executive Summary, Features We're NOT Implementing (but exist elsewhere), MUD Disconnect Grace Period & Rest Command: Industry Comparison, Questions for Discussion

### Community 633 - "Chaosium CoC Catalog.md"
Cohesion: 0.15
Nodes (10): Evocations of the Inner God, The Hungry Void, Church of Sunyata, Dark Young of Shub-Niggurath, Flying Polyp, Fungi from Yuggoth, Ghoul, The Faceless Men (+2 more)

### Community 634 - "ApplicationContainer Structure Analysis and Domain-Specific Split Proposal"
Cohesion: 0.09
Nodes (21): 1. Executive Summary, 2.1 Attribute Inventory by Domain, 2.2 Initialization Order and Dependencies, 2.3 Private Initializers and Helpers, 2.4 Public API and Consumers, 2. Current Structure Analysis, 3.1 Option A: Internal Bundles (Recommended), 3.2 Option B: Composed Sub-Containers (Alternative) (+13 more)

### Community 635 - "ContainerRepository and ItemRepository: Review and Full Async Migration Plan"
Cohesion: 0.09
Nodes (23): 1.1 Current Architecture, 1.2 Impact of Current Wrappers, 1.3 Recommendation, 1. Review Summary, 2.1 Functions to Migrate, 2.2 Callers, 2. Scope of Migration, 3. Migration Options (+15 more)

### Community 636 - "MythosMUD Dependency Upgrade Strategy - Implementation Summary"
Cohesion: 0.09
Nodes (22): ⚠️ Breaking Changes Detected, Conclusion, Critical Findings, 🔍 Dependency Analysis, 📋 Documentation Generated, Immediate Actions (Today), Implementation Strategy, Long-term Planning (Next 2-3 Weeks) (+14 more)

### Community 637 - "Documentation Updates - ConnectionManager Refactoring"
Cohesion: 0.09
Nodes (23): 1. **Accurate Reference Material**, ✅ 1. `REAL_TIME_ARCHITECTURE.md`, ✅ 2. `CONNECTION_MANAGER_ARCHITECTURE.md` (NEW), 2. **Reduced Confusion**, 3. **Better Onboarding**, ✅ 3. `WEBSOCKET_CODE_REVIEW.md`, ✅ 4. `DEVELOPMENT_AI.md`, 4. **Historical Record** (+15 more)

### Community 638 - "Persistence Layer Refactoring Summary"
Cohesion: 0.09
Nodes (23): Backward Compatibility, Benefits Achieved, Code Organization, Conclusion, Conservative Approach, Created, Existing Code (Unchanged), Files Created/Modified (+15 more)

### Community 639 - "TEST_AUDIT_EXECUTIVE_SUMMARY.md"
Cohesion: 0.10
Nodes (17): ConnectionCleaner, ConnectionManager Facade, MessageBroadcaster, PerformanceTracker, 25-30 Percent Critical Tests, Option B Quick Wins First, ApplicationContainer Lifecycle Gap, Domain Layer Coverage Gap (+9 more)

### Community 640 - "compilerOptions"
Cohesion: 0.09
Nodes (22): compilerOptions, baseUrl, lib, module, moduleResolution, noEmit, noFallthroughCasesInSwitch, noUnusedLocals (+14 more)

### Community 641 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 642 - "Execution Steps"
Cohesion: 0.09
Nodes (22): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, ✅ FIXES IMPLEMENTED - Ready for Testing, Overview, Prerequisites (+14 more)

### Community 643 - "test_command_factories_inventory.py"
Cohesion: 0.14
Nodes (18): Unit tests for inventory command factories. Tests the InventoryCommandFactory…, Test create_unequip_command() raises error with empty args., Test create_unequip_command() raises error with whitespace only., Test create_unequip_command() handles known slot., Test create_unequip_command() handles unknown slot as search term., Test create_unequip_command() handles multi-word search term., Test create_unequip_command() handles all known slots., Test create_unequip_command() creates UnequipCommand. (+10 more)

### Community 644 - "generate_html_visualization.py"
Cohesion: 0.13
Nodes (22): _format_exits(), _generate_edge_data(), generate_html_visualization(), _generate_intersection_items_for_subzone(), _generate_intersection_nodes(), _generate_room_items_for_subzone(), _generate_room_list_html(), _generate_room_nodes() (+14 more)

### Community 645 - "lint_container_get_instance.py"
Cohesion: 0.12
Nodes (22): _allowlist_count_violations(), AllowlistEntry, _code_tokens(), _collect_get_instance_counts(), _collect_python_files(), _find_get_instance_lines(), _is_application_container_get_instance(), main() (+14 more)

### Community 646 - "verify_migration.py"
Cohesion: 0.15
Nodes (22): _check_foreign_keys(), _check_null_values(), _check_table_exists(), main(), _print_json_validation_results(), _print_sample_data(), _print_verification_summary(), Connection (+14 more)

### Community 647 - "NPCCacheService"
Cohesion: 0.23
Nodes (8): NPCCacheService, Service for caching NPC definitions and spawn rules., Invalidate all NPC definition caches., Invalidate all NPC spawn rule caches., _NpcDef, asyncio, _SpawnRule, TestNPCCacheService

### Community 648 - "realtime/realtime.py"
Cohesion: 0.12
Nodes (25): get_connection_statistics(), Get comprehensive connection statistics. Returns detailed statistics about all…, ErrorStatistics, PresenceStatistics, BaseModel, Presence and health statistics schema for MythosMUD. This module defines…, Presence statistics for connection monitoring. This model represents aggregate…, Session statistics for connection monitoring. This model represents aggregate… (+17 more)

### Community 649 - "bind_request_context"
Cohesion: 0.04
Nodes (52): async_work(), correct_api_logging(), correct_async_logging(), correct_basic_logging(), correct_batch_logging(), correct_database_logging(), correct_error_handling(), correct_exception_tracking() (+44 more)

### Community 650 - ".create_put_command"
Cohesion: 0.10
Nodes (19): Test create_put_command() handles optional 'in' keyword., Test create_put_command() with quantity., test_create_put_command_with_in(), test_create_put_command_with_quantity(), Test create_put_command() raises error with no args., Test create_put_command() raises error with only item., Test create_put_command() handles 'in' keyword., Test create_put_command() raises error when quantity is zero. (+11 more)

### Community 651 - "apply_communication_dampening"
Cohesion: 0.17
Nodes (21): apply_communication_dampening(), _apply_receiver_effects(), _apply_sender_effects(), DampeningResult, _maybe_muffle_fractured_message(), _maybe_scramble_deranged_message(), TypedDict, Communication dampening utilities for lucidity system. Implements communication… (+13 more)

### Community 652 - "test_room_service.py"
Cohesion: 0.08
Nodes (23): Unit tests for room service. Tests the RoomService class for room-related…, Test get_room_by_name() returns None (not implemented)., Test list_rooms_in_zone() returns empty list (not implemented)., Test update_environment_state() updates environment state., Test get_environment_state() returns current environment state., Test describe_lighting() returns description for day., Test describe_lighting() returns description for night., Test describe_lighting() returns default for unknown daypart. (+15 more)

### Community 653 - "useMythosAppState.ts"
Cohesion: 0.06
Nodes (39): CharacterCard(), CharacterCardDeleteState, CharacterCardProps, CharacterSelectionScreenProps, formatCharacterDate(), restoreCharactersOnMount(), CreationStep, DeleteCharacterUiDeps (+31 more)

### Community 654 - "test_check_coverage_thresholds.py"
Cohesion: 0.15
Nodes (20): _CheckCoverageThresholdsModule, _fully_covered(), _load_script(), Protocol, Unit tests for scripts/check_coverage_thresholds.py. Covers `check_thresholds`'…, A KNOWN_COVERAGE_DEBT entry lowers the blanket 70% normal-file floor (#677)., A file present in CRITICAL_FILES but absent from the coverage.xml data (e.g.…, Typed surface of the loaded script, for the parts these tests exercise. (+12 more)

### Community 655 - "test_lint_optional_auth_no_guard.py"
Cohesion: 0.17
Nodes (20): _LintOptionalAuthModule, _load_script(), Path, Protocol, Unit tests for scripts/lint_optional_auth_no_guard.py. Verifies the detection…, Mirrors rooms.py's real shape: handler -> helper -> helper ->…, A route was fixed but the allowlist count wasn't lowered -- must fail, not pass…, Typed surface of the loaded script, for the parts these tests exercise. (+12 more)

### Community 656 - "Performance Profiler Subagent"
Cohesion: 0.10
Nodes (21): Bottleneck Identification, Capabilities, Code Performance Review, Database Performance, Database Query Optimization, Enhanced Logging Integration, Example Scenarios, Game Loop Performance (+13 more)

### Community 657 - "Security Auditor Subagent"
Cohesion: 0.09
Nodes (21): Authentication & Authorization, Authentication Security Review, Capabilities, COPPA Compliance, COPPA Compliance (Critical), COPPA Compliance Verification, Example Scenarios, Input Validation (+13 more)

### Community 659 - "get_session_maker"
Cohesion: 0.02
Nodes (116): get_10_active_invites(), main(), Get 10 active invite codes from the database., F, normalize_database_url(), Set test override database URL., Normalize database URL for asyncpg. Args: database_url: Original database URL…, set_test_database_url() (+108 more)

### Community 660 - "The Toolkit"
Cohesion: 0.09
Nodes (22): Overdrive Skill, Animate complex properties, Assess What "Extraordinary" Means Here, For data-heavy interfaces, For functional UI, For performance-critical UI, For visual/marketing surfaces, Implement with Discipline (+14 more)

### Community 661 - "GameClientV2Dock.test.tsx"
Cohesion: 0.05
Nodes (31): chatHistoryLayoutIdentity, chatHistoryLayoutState, defaultChatHistoryLayoutKey, dockTest, mockPanelRecord(), mockPanelRecordCore(), mockPanelRecordFlags(), mockUsePanelManagerNoops() (+23 more)

### Community 662 - "Communities (10 total, 2 thin omitted)"
Cohesion: 0.12
Nodes (17): Communities (10 total, 2 thin omitted), Community 0 - "Azotottal (fallen angel beyond the stars) / Captain Louis Malon", Community 1 - "Charenton (Paris district / asylum) / Christophe Pressi — Soldat (Soldier), age 20", Community 2 - "Dreamlands / Fenalik's Mansion (Poissy)", Community 3 - "Reign of Terror / Call of Cthulhu 7th Edition", Community 4 - "Bastille / James Coquillat", Community 5 - "Azathoth / Celine Bessette", Community 6 - "Christophe Pressi / Comte Benoit" (+9 more)

### Community 663 - "Game Subsystem Design Documents Overview"
Cohesion: 0.17
Nodes (18): Distributed EventBus via NATS, Event Ownership Matrix, NATS Subject Pattern Management, Game Subsystem Design Documents Overview, Admin Commands Subsystem Design, Combat Subsystem Design, Emote / Pose Subsystem Design, Follow Subsystem Design (+10 more)

### Community 664 - "Complexity Refactoring Test Plan"
Cohesion: 0.09
Nodes (22): 1. Application Startup & CORS (create_app), 2. WebSocket Connections, 3. Room Operations, 4. Container Operations, 5. Player Respawn, 6. Game Tick Processing, 7. Integration Tests, Complexity Refactoring Test Plan (+14 more)

### Community 665 - "NATS Complete Remediation Summary"
Cohesion: 0.09
Nodes (22): After Remediation, Backward Compatibility, Before Remediation, Complete Fix Summary, Conclusion, Configuration Options Added, Documentation Created, Enhanced Configuration Usage (+14 more)

### Community 666 - "SQLAlchemy Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.09
Nodes (21): 1. SQL Injection Vulnerability in `update_player_stat_field()` - ✅ FIXED, 2. Missing Eager Loading for Relationships, 3. Mixed Database Access Patterns, 4. F-String SQL Construction (Even with Constants), 5. Missing Indexes on Foreign Keys, 6. Long-Lived Sessions, 7. Connection Pool Configuration, 8. Transaction Boundaries (+13 more)

### Community 667 - "Execution Steps"
Cohesion: 0.09
Nodes (21): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, ✅ READY FOR TESTING (+13 more)

### Community 668 - "fix_suppression_alignment.py"
Cohesion: 0.16
Nodes (21): add_pylint_suppression(), add_ruff_suppression(), _apply_fixes_to_line(), fix_file(), _group_fixes_by_line(), main(), parse_alignment_report(), _parse_file_line_pattern() (+13 more)

### Community 669 - "identify_critical_code.py"
Cohesion: 0.15
Nodes (21): analyze_file(), analyze_function(), calculate_complexity(), calculate_priority(), check_file_keywords(), check_function_keywords(), main(), process_ast_functions() (+13 more)

### Community 670 - "test_auth_rate_limit.py"
Cohesion: 0.18
Nodes (21): auth_client_key(), auth_rate_limit_response(), is_auth_rate_limited_path(), Request, Return 429 when an auth POST exceeds the limiter; otherwise None., Return True if path is an unauthenticated auth POST covered by the limiter., Key the limiter by client IP. Default uses the TCP peer (request.client.host).…, _ok_post() (+13 more)

### Community 671 - "real_time.py"
Cohesion: 0.16
Nodes (23): _app_state_from_websocket(), _invoke_handle_websocket_connection(), _parse_websocket_token(), BoundLogger, WebSocket, Real-time communication API endpoints for MythosMUD server. This module handles…, Load the handler via importlib so basedpyright does not follow the factory…, Read Starlette app.state from a WebSocket connection. (+15 more)

### Community 672 - "Phase 1: Core Separation"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 1: Core Separation, Sub-tasks, Sub-tasks (+8 more)

### Community 673 - "Phase 2: Enhanced Features"
Cohesion: 0.12
Nodes (16): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 2: Enhanced Features, Sub-tasks, Sub-tasks (+8 more)

### Community 674 - "test_player_repository_room.py"
Cohesion: 0.20
Nodes (20): Any, Player, Player room validation helpers for PlayerRepository. Validates and fixes…, Return True if room validation should be skipped (cache empty, instanced, or…, Validate player's current room and fix if invalid. Args: room_cache: Shared…, Validate and fix player room, persisting the fix if needed. Args: room_cache:…, should_skip_room_validation(), validate_and_fix_player_room() (+12 more)

### Community 675 - ".create_get_command"
Cohesion: 0.10
Nodes (19): Test create_get_command() creates GetCommand., Test create_get_command() handles optional 'from' keyword., test_create_get_command(), test_create_get_command_with_from(), Test create_get_command() raises error with no args., Test create_get_command() with single arg returns get-from-room…, Test create_get_command() handles 'from' keyword., Test create_get_command() raises error when quantity is zero. (+11 more)

### Community 676 - "MPRegenerationService"
Cohesion: 0.15
Nodes (13): MPRegenerationService, Any, UUID, MP regeneration service for passive and active magic point recovery. This…, Get MP regeneration multiplier based on player state. Args: stats: Player stats…, # TODO: Check status effects for meditation when status effect system supports…, Restore MP from resting (accelerated regeneration). Args: player_id: Player ID…, # NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per… (+5 more)

### Community 677 - "test_security_utils.py"
Cohesion: 0.12
Nodes (23): get_secure_file_path(), Get a secure file path within a base directory. Args: filename: The filename…, Unit tests for security utilities. Tests path validation and file security…, Test get_secure_file_path with valid filename., Test get_secure_file_path rejects invalid characters., Test get_secure_file_path rejects filenames with slashes., Test get_secure_file_path creates base directory if it doesn't exist., Test get_secure_file_path accepts filenames with underscores. (+15 more)

### Community 678 - "test_players_procedures.py"
Cohesion: 0.23
Nodes (21): invite_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/players.sql's #633/#733 additions:…, reserve_invite then capture_invite in the same transaction (the real auth-and-… (+13 more)

### Community 679 - "asyncio"
Cohesion: 0.08
Nodes (25): asyncio, Test get_room() returns None when room not found in persistence., Test get_adjacent_rooms() handles room with no exits., Test get_adjacent_rooms() handles target room not found., Test get_local_chat_scope() returns empty list when source room not found., Test get_room_occupants() handles room dict., Test get_room_occupants() falls back to persistence., Test validate_player_in_room() returns False when player not in room. (+17 more)

### Community 680 - "test_wearable_container_service.py"
Cohesion: 0.04
Nodes (76): asyncio, Unit tests for wearable container service. Tests the WearableContainerService…, Test handle_unequip_wearable_container returns None when no item_instance_id., Test handle_unequip_wearable_container returns None when container not found., Test get_wearable_containers_for_player returns empty list when no containers., Test get_wearable_containers_for_player handles errors gracefully., Test add_items_to_wearable_container adds items., Test add_items_to_wearable_container raises error when container not found. (+68 more)

### Community 681 - "overrides"
Cohesion: 0.17
Nodes (11): dependencies, eslint, devDependencies, markdownlint-cli, eslint, markdownlint-cli, overrides, flatted (+3 more)

### Community 682 - "compilerOptions"
Cohesion: 0.05
Nodes (36): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, erasableSyntaxOnly, jsx, lib, module (+28 more)

### Community 683 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowImportingTsExtensions, erasableSyntaxOnly, jsx, lib, module, moduleDetection, moduleResolution (+24 more)

### Community 684 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "A Message of Art; And Some Fell on Stony Ground; Nameless Ho", Community 10 - "Stowell; Betty Considine (waitress); Wesley Frost (bank cler", Community 1 - "Handout: Amaranthine 1; Dunwich (Keeper Map); Dunwich Throug", Community 2 - "An Amaranthine Desire; Captain Louis Gerd; Dunwich (Suffolk)", Community 3 - "An Amaranthine Desire; Clare Boone; Dunwich, Suffolk, Englan", Community 4 - "A Message of Art; Evocations of the Inner God; Josephin Pela", Community 5 - "Church of Sunyata; Craig Steele; The Hungry Void" (+12 more)

### Community 685 - "Communities (11 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (20): Communities (11 total, 0 thin omitted), Community 0 - "Pandora's Box / Pandora Handout 10", Community 10 - "Chapter 6: Pulp Magic, Psychic Powers, and Weird S / Psychic Powers", Community 1 - "Disintegrator device / Handout: Disintegrator 1", Community 2 - "Chapter 1: The Pulps / Chapter 7: Running Pulp Games", Community 3 - "Avoiding Certain Death / Call of Cthulhu 7th Edition", Community 4 - "Cthulhu Mythos / Deep One", Community 5 - "Seekers of Eternal Wisdom / Handout: Pandora's Box 12" (+12 more)

### Community 686 - "Asyncio Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.10
Nodes (21): 1. Blocking Synchronous Operations in Async Methods, 2. asyncio.run() Called from Context with Existing Event Loop, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Event Loop Change Detection May Not Handle All Cases, 6. Synchronous Database Operations in Async Context, 7. Missing Transaction Management in Batch Operations, 8. Connection Pool Size Configuration (+13 more)

### Community 687 - "Environment Contamination Audit Report"
Cohesion: 0.10
Nodes (20): 1. **CRITICAL VIOLATION: `server/logging_config.py`**, 2. **ACCEPTABLE PATTERNS: Environment Variable Usage**, Analysis, Compliance Status, Conclusion, Critical Violations Found, Environment Contamination Audit Report, Executive Summary (+12 more)

### Community 688 - "Findings by Category"
Cohesion: 0.10
Nodes (21): 1.1 Database Connection Pools, 1.2 WebSocket Connection Leaks, 1.3 NATS Connection and Subscription Leaks, 1. Connection Management Leaks, 2.1 EventBus Subscriber Leaks, 2.2 Client-Side Event Handler Leaks, 2. Event System Leaks, 3.1 Task Registry Leaks (+13 more)

### Community 689 - "NATS Medium-Priority Remediation Summary"
Cohesion: 0.10
Nodes (21): NATSMessageBroker, 1. Integrated Subject Manager into NATSMessageBroker, 2. Added Health Monitoring to NATSMessageBroker, 3. Documented Manual Acknowledgment Strategy, After Medium-Priority Fixes, Before Medium-Priority Fixes, Completed Medium-Priority Fixes ✅, Configuration Options (+13 more)

### Community 690 - "Phase 2 Async Persistence Migration - Status Update"
Cohesion: 0.09
Nodes (21): asyncio.to_thread Persistence Pattern, Room Cache 60s TTL, adjusts spectacles and awaits instruction, Awaiting Your Direction, Professor Wolfshade, ✅ Completed Today, Critical Phase 1 Fixes (100% Complete), 🚦 Current Status, 🎯 Decision Point (+13 more)

### Community 691 - "Pydantic Code Review - feature/sqlite-to-postgresql Branch"
Cohesion: 0.10
Nodes (21): ⚠️ Areas for Improvement, 🟡 Business Logic in Models - Stats.**init**, Code Quality Observations, Conclusion, Critical Issues, 🔴 CRITICAL: Security Vulnerability - `extra="allow"` in Stats Model, Executive Summary, 🟢 Field Validator Organization (+13 more)

### Community 692 - "Execution Steps"
Cohesion: 0.10
Nodes (20): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 17: Whisper Integration **[REQUIRES MULTI-PLAYER]**, Step 10: Test Whisper with Performance Integration, Step 11: Test Whisper with Logging Integration (+12 more)

### Community 693 - "TestNPCCombatLifecycle"
Cohesion: 0.12
Nodes (13): asyncio, fixture, Test _despawn_npc handles NPC not in active_npcs., Test suite for NPCCombatLifecycle class., Create a mock persistence layer., Create a NPCCombatLifecycle instance for testing., Test NPCCombatLifecycle initialization., Test despawn_npc_safely successfully despawns NPC. (+5 more)

### Community 694 - "properties"
Cohesion: 0.15
Nodes (13): minLength, type, maximum, minimum, type, minLength, type, type (+5 more)

### Community 695 - "audit_suppressions.py"
Cohesion: 0.18
Nodes (20): calculate_statistics(), find_suppressions(), group_by_file(), group_by_tool(), has_explanation(), main(), print_summary_report(), Any (+12 more)

### Community 696 - "fix_markdown_line_length.py"
Cohesion: 0.15
Nodes (20): fix_markdown_file(), is_in_code_block(), main(), parse_markdownlint_output(), Path, Wrap a line that contains markdown links., Wrap plain text at word boundaries., Fix line length issues in a markdown file. Returns: (changed, lines_modified):… (+12 more)

### Community 697 - "populate_npc_sample_data.py"
Cohesion: 0.14
Nodes (20): _get_column_names(), get_npc_database_url(), main(), populate_database(), _process_other_statement(), _process_select_statement(), Verify foreign key constraints., Populate a PostgreSQL database with sample NPC data. Args: database_url: The… (+12 more)

### Community 698 - ".create_equip_command"
Cohesion: 0.10
Nodes (19): Test create_equip_command() raises error when index is zero., Test create_equip_command() raises error when index is negative., Test create_equip_command() handles index with slot., Test create_equip_command() handles search term with slot., Test create_equip_command() raises error when search term is empty., Test create_equip_command() infers slot from known slots., Test create_equip_command() creates EquipCommand., Test create_equip_command() raises error with no args. (+11 more)

### Community 699 - "schemas/unified_room_schema.json"
Cohesion: 0.13
Nodes (14): additionalProperties, allOf, description, description, exits, id, name, plane (+6 more)

### Community 700 - "properties"
Cohesion: 0.09
Nodes (23): maxLength, minLength, type, properties, maxLength, minLength, type, description (+15 more)

### Community 701 - "test_lucidity_command_disruption.py"
Cohesion: 0.16
Nodes (19): can_perform_action(), get_misfire_message(), Command disruption utilities for lucidity system. Implements command misfires…, Check if a command should misfire based on tier and command type. Args:…, Get the misfire message for a failed command. Args: command_type: Type of…, Check if player should involuntarily flee. Args: tier: Current lucidity tier…, Check if player can perform actions (motor lock check). Args: tier: Current…, should_involuntary_flee() (+11 more)

### Community 702 - "test_exploration_procedures.py"
Cohesion: 0.25
Nodes (20): player_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/exploration.sql (#633). Replaces raw SQL…, A third room at the source room's exact coordinates conflicts with it -- one… (+12 more)

### Community 703 - "TestPathValidator"
Cohesion: 0.10
Nodes (12): fixture, Tests for path validator functionality. Validates room connectivity analysis…, Test detection of mismatched return paths across zones., Test suite for path validation functionality., Create a path validator instance., Sample rooms with zone transitions., Test detection of zone transitions in room connections., Test detection of broken zone transitions. (+4 more)

### Community 704 - "Design Critique"
Cohesion: 0.10
Nodes (20): Critique Skill, 10. Microcopy & Voice, 1. AI Slop Detection (CRITICAL), 2. Visual Hierarchy, 3. Information Architecture, 4. Emotional Resonance, 5. Discoverability & Affordance, 6. Composition & Balance (+12 more)

### Community 705 - "useThemeContext.ts"
Cohesion: 0.15
Nodes (23): SettingsPanel(), ADR-0024, ADR-0025, useAccessibilityPreference(), useAnimationPreference(), useChatGrainPreference(), useColorSchemePreference(), useCompactModePreference() (+15 more)

### Community 706 - "compilerOptions"
Cohesion: 0.04
Nodes (45): compilerOptions, allowImportingTsExtensions, isolatedModules, jsx, lib, module, moduleResolution, noEmit (+37 more)

### Community 707 - "Communities (10 total, 0 thin omitted)"
Cohesion: 0.10
Nodes (19): Communities (10 total, 0 thin omitted), Community 0 - "Hotel Hell", Community 1 - "Petersen's Abominations", Community 2 - "Hotel Hell", Community 3 - "Voice on the Phone", Community 4 - "Mohole", Community 5 - "Panacea", Community 6 - "Panacea" (+11 more)

### Community 708 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, properties, minLength, type, id, name, season (+4 more)

### Community 709 - "properties"
Cohesion: 0.17
Nodes (12): minLength, type, minLength, type, properties, minLength, type, type (+4 more)

### Community 710 - "Lizard Complexity Analysis Findings"
Cohesion: 0.10
Nodes (19): 1. `create_app` - CCN: 22, 2. `_load_rooms_with_coordinates` - CCN: 12, 3. `_parse_websocket_token` - CCN: 12, 4. `_ensure_coordinates_generated` - CCN: 11, 🔴 CRITICAL: Functions Exceeding Threshold (CCN > 10), Functions with CCN = 10, Functions with CCN = 9, Lizard Complexity Analysis Findings (+11 more)

### Community 711 - "ConnectionManager Refactoring Summary"
Cohesion: 0.10
Nodes (20): 1. Statistics & Monitoring (`realtime/monitoring/`), 2. Error Handling (`realtime/errors/`), 3. Health Monitoring (`realtime/monitoring/`), 4. Cleanup & Maintenance (`realtime/maintenance/`), 5. Game State Management (`realtime/integration/`), 6. Room Event Integration (`realtime/integration/`), 7. Message Broadcasting (`realtime/messaging/`), After (+12 more)

### Community 712 - "Actionable Recommendations"
Cohesion: 0.10
Nodes (20): **~25-30% provide CRITICAL coverage**, Actionable Recommendations, Add Missing Integration Tests (70 tests, 0% risk, 10 hours effort), Command, Critical Gap Action (Month 2), Files, High-Priority Action (Next 2 Weeks), Immediate (This Week) (+12 more)

### Community 713 - "Phase 2: Qualitative Analysis Results"
Cohesion: 0.07
Nodes (30): 2.1 Regression Test Audit (★★★★★ HIGH VALUE), 2.2 Integration Test Analysis (★★★★☆ HIGH-MEDIUM VALUE), 2.3 Coverage Test Review (★★☆☆☆ MEDIUM-LOW VALUE), 2.4 Unit Test Pattern Analysis (★★★☆☆ MIXED VALUE), 2.5 Infrastructure Test Review (★☆☆☆☆ LOW VALUE), 2.6 E2E Test Analysis (★★★★★ HIGH VALUE), 2.7 Security Test Analysis (★★★★★ HIGH VALUE), Assessment (+22 more)

### Community 714 - "Transaction Boundaries Audit"
Cohesion: 0.10
Nodes (20): ✅ AsyncPersistenceLayer (Async), Audit Date, Audited Operations, Current State: ✅ GOOD, Future Improvements, Multi-Step Operations, Notes, Pattern 1: Connection Context Manager (PersistenceLayer) (+12 more)

### Community 715 - "Scenario 22: Invite-Only Registration Enforcement"
Cohesion: 0.10
Nodes (19): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Cleanup, ✅ EXECUTED - ALL STEPS PASSED, Execution Record, Execution Steps, Expected Results, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview (+11 more)

### Community 716 - "LoggingPatternLinter"
Cohesion: 0.11
Nodes (15): FormattedValue, lint_file(), LoggingPatternLinter, main(), Call, Import, ImportFrom, Path (+7 more)

### Community 717 - "required"
Cohesion: 0.13
Nodes (15): base_value, effect_components, flags, item_type, long_description, metadata, prototype_id, short_description (+7 more)

### Community 718 - "UpgradeImplementationPlan"
Cohesion: 0.14
Nodes (11): main(), Generate Phase 2: Minor Updates Plan, Comprehensive upgrade implementation plan, Generate Phase 3: Major Updates Plan, Generate detailed migration guides, Generate rollback procedures, Generate post-upgrade monitoring plan, Generate complete upgrade implementation plan (+3 more)

### Community 719 - "test_admin_shutdown_command.py"
Cohesion: 0.11
Nodes (28): cancel_shutdown_countdown(), is_shutdown_pending(), Check if server shutdown is currently pending. Args: app: FastAPI application…, Cancel active shutdown countdown. Args: app: FastAPI application instance…, _AppWithoutState, _PendingCheckAppStub, _PendingCheckStateStub, Unit tests for admin shutdown command handler. Tests the shutdown command… (+20 more)

### Community 720 - "properties"
Cohesion: 0.11
Nodes (19): minimum, type, minimum, type, maxLength, minLength, type, properties (+11 more)

### Community 721 - "NPCActionMessage"
Cohesion: 0.15
Nodes (15): _float_field(), NPCActionMessage, NPCActionType, _optional_int_field(), _optional_str_field(), Enum, Convert message to JSON string., Create message from JSON string. (+7 more)

### Community 722 - "NpcBaseStats"
Cohesion: 0.16
Nodes (17): NpcArmorMetadata, NpcAttackMetadata, NpcBaseStats, NpcCatalogMetadata, BaseModel, Pydantic contracts for NPC definition base_stats catalog shapes (ADR-027).…, Catalog namespace, canonical/variant linkage, opaque private source key., Single NPC attack: rich dice fields plus legacy min/max dual-write. (+9 more)

### Community 723 - ".validate_entity_id"
Cohesion: 0.12
Nodes (11): Any, field_validator, Validate that metadata does not contain personal information (COPPA…, Validate and convert source_type to enum., Validate and convert lock_state to enum., Validate that room_id is provided for environment and corpse containers., Validate that entity_id is provided for equipment containers., Check if container has room for additional items. (+3 more)

### Community 724 - "schedule_end_combat_if_npc_died_best_effort"
Cohesion: 0.12
Nodes (13): Update determination points after taking damage; return new DP., Publish damage event to event bus., Handle NPC death after taking fatal damage., Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…, Take damage and update determination points (DP)., Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…, schedule_end_combat_if_npc_died_best_effort(), patch (+5 more)

### Community 725 - "NPCSpawnRuleCRUDMixin"
Cohesion: 0.17
Nodes (13): Any, Map procedure result row to NPCSpawnRule model., _row_to_npc_spawn_rule(), NPCSpawnRuleCRUDMixin, Any, AsyncSession, Validate NPC definition existence and population counts for spawn rule creation., Execute create_spawn_rule stored procedure and return the created spawn rule. (+5 more)

### Community 726 - "test_lru_cache.py"
Cohesion: 0.07
Nodes (27): cache_with_ttl(), cache_without_ttl(), asyncio, fixture, Unit tests for LRU cache expiration and eviction. Tests the LRUCache class,…, Test that expired entry count is tracked in cache stats., Test that expiration rate is calculated in stats., Test that cache size stays within bounds after expiration cleanup. (+19 more)

### Community 727 - "TestVerificationSqlUsersPlayers"
Cohesion: 0.10
Nodes (12): PostgreSQL-focused tests for verification and maintenance SQL scripts.…, Tests for db/verification/users_players.sql alignment with current schema., Verification SQL file must exist., Verification SQL must not reference staging tables or select obsolete columns., Verification SQL must use explicit join syntax for multi-table queries., Verification SQL must reference users and players tables., Tests for server/scripts/add_npc_name_constraint.sql (PostgreSQL-only)., NPC name constraint script must exist. (+4 more)

### Community 728 - "utils/config.ts"
Cohesion: 0.20
Nodes (13): SkillsPage, AppCreationFlowViews(), creationShell(), renderNameStep(), renderProfessionStep(), renderSkillsStep(), renderStatsStep(), SkillEntry (+5 more)

### Community 729 - "required"
Cohesion: 0.14
Nodes (13): additionalProperties, $id, description, exits, id, name, plane, sub_zone (+5 more)

### Community 730 - "optimized_validate_player_name"
Cohesion: 0.09
Nodes (22): Test validating empty player name., Test validating player name below min length., Test validating player name above max length., Test validating player name with spaces., Test validating valid player name., Test validating player name with underscore., Test validating player name with hyphen., Test validating player name with numbers. (+14 more)

### Community 731 - "subzone_schema.json"
Cohesion: 0.05
Nodes (43): description, items, type, additionalProperties, description, type, description, description (+35 more)

### Community 732 - "static_data/package.json"
Cohesion: 0.11
Nodes (18): ajv, ajv-formats, dependencies, ajv, ajv-formats, uuid, description, uuid (+10 more)

### Community 733 - "test_metadata.py"
Cohesion: 0.11
Nodes (15): Shared SQLAlchemy metadata for MythosMUD models. This module provides the…, NPC Database metadata for MythosMUD. This module defines the SQLAlchemy…, Unit tests for metadata modules. Tests the shared SQLAlchemy metadata instances., Test that metadata is a MetaData instance., Test that npc_metadata is a MetaData instance., Test that metadata and npc_metadata are separate instances., Test that Base is a DeclarativeBase subclass., Test that Base has metadata attribute set to shared metadata. (+7 more)

### Community 734 - "submitAuth.ts"
Cohesion: 0.24
Nodes (14): AuthSessionSetters, persistTokensAndApplySession(), SetBool, SetChars, SetStep, toCharacterInfoFromLogin(), AuthSuccessPayload, SanitizedCredentials (+6 more)

### Community 735 - "Delight Techniques"
Cohesion: 0.11
Nodes (19): Delight Skill, Appropriate to Context, Assess Delight Opportunities, Celebration Moments, Compound Over Time, Delight Amplifies, Never Blocks, Delight Principles, Delight Techniques (+11 more)

### Community 736 - "knip.json"
Cohesion: 0.07
Nodes (27): entry, ignore, ignoreBinaries, ignoreDependencies, vite.userConfig.ts, project, rules, binaries (+19 more)

### Community 737 - "compilerOptions"
Cohesion: 0.07
Nodes (28): compilerOptions, allowImportingTsExtensions, composite, emitDeclarationOnly, lib, module, moduleDetection, moduleResolution (+20 more)

### Community 738 - "Enhanced Logging Best Practices for MythosMUD"
Cohesion: 0.11
Nodes (19): Common Anti-Patterns, Conclusion, Configuration, 🚨 CRITICAL ANTI-PATTERNS - DO NOT USE, Custom Log Analysis, ✅ Do This Instead, ❌ Don't Do This, Enhanced Logging Best Practices for MythosMUD (+11 more)

### Community 739 - "Persistence Layer Extraction - COMPLETE ✅"
Cohesion: 0.11
Nodes (19): Architecture Changes, Benefits, Cleanup, Conclusion, File Size Reduction, Files Modified, Migration Path for Callers, Next Steps (+11 more)

### Community 740 - "Test Coverage Summary: Disconnect Grace Period & Rest Command"
Cohesion: 0.13
Nodes (19): Coverage Targets, Coverage Verification, Critical Files (90% Target), E2E Scenarios, E2E Test Scenarios, Expected Coverage Results, Grace Period System Tests, Integration Tests (+11 more)

### Community 741 - "enum"
Cohesion: 0.09
Nodes (23): ACCESSORY, AMULET, BELT, CURSED, FEET, GLOW, HANDS, HEAD (+15 more)

### Community 742 - "test_email_utils.py"
Cohesion: 0.18
Nodes (17): generate_unique_bogus_email(), is_bogus_email(), AsyncSession, Email utilities for MythosMUD authentication. This module provides utilities…, Generate a unique bogus email address for a user. This function creates a bogus…, Check if an email address is a bogus email generated by our system. Args:…, Validate that a bogus email follows our expected format. Args: email: The email…, validate_bogus_email_format() (+9 more)

### Community 743 - "properties"
Cohesion: 0.11
Nodes (19): minimum, type, properties, maxLength, minLength, type, equipmentMetadata, additionalProperties (+11 more)

### Community 744 - "ADR-027: NPC Catalog Base Stats Contracts"
Cohesion: 0.12
Nodes (16): 1. Overview, 2. Context, 3.1 Phased delivery, 3.2 Storage and placement, 3.3 Rich `base_stats` shape, 3.4 Dice and dual-write, 3.5 Explicitly out of scope (this ADR / epic), 3. Decision (+8 more)

### Community 745 - "parse_json_field"
Cohesion: 0.17
Nodes (12): parse_json_field(), Parse a JSON field from database, handling both dict/list and string formats.…, Test parse_json_field() returns default when None., Test parse_json_field() parses JSON string., Test parse_json_field() returns dict as-is., Test parse_json_field() returns list as-is., Test parse_json_field() raises error on invalid JSON string., test_parse_json_field_dict() (+4 more)

### Community 746 - "._damage_player_inner"
Cohesion: 0.12
Nodes (14): Exception, Player, UUID, Log critical damage persistence failure., Execute atomic health update via update_player_health procedure., Damage a player and persist health changes atomically. Args: player: Player to…, Heal a player and persist health changes atomically., Core heal logic without error handling wrapper. (+6 more)

### Community 747 - "handle_unequip_command"
Cohesion: 0.29
Nodes (16): handle_unequip_command(), CommandResponse, Player, Unequip an item into the player's inventory., _unequip_persist_or_rollback(), _unequip_run_mutation(), _unequip_success_payload(), _mutation_cm() (+8 more)

### Community 748 - "test_corruption_reactions.py"
Cohesion: 0.23
Nodes (16): corruption_hostility_scale(), _pick_greeting(), Threat multiplier from the corruption gap between an NPC and a player,…, Unit tests for NPC <-> player corruption relationship (#815 PR-4). Covers both…, #815: the permanent scar (touched) stays private -- no special greeting for it., _reset_cache(), test_build_corruption_aware_greeting_fires_on_entry_to_the_npcs_room(), test_corruption_hostility_scale_intermediate_gap() (+8 more)

### Community 749 - "Any"
Cohesion: 0.11
Nodes (12): Any, Path, Validate a room file against the schema. Args: file_path: Path to the room JSON…, Validate all rooms in a database against the schema. Args: room_database:…, Validate a serialized alias bundle against the alias schema. Args: alias_data:…, Validate emote definition data against the emote schema. Args: emote_data:…, Extract target room ID from exit data, handling both formats. Args: exit_data:…, Extract flags from exit data, handling both formats. Args: exit_data: Exit data… (+4 more)

### Community 750 - "fixtures/shared/__init__.py"
Cohesion: 0.13
Nodes (15): fake_clock(), make_player_dict(), make_user_dict(), Any, fixture, Shared fixtures and builders for all test tiers., Create a user dictionary for testing., Create a player dictionary for testing. (+7 more)

### Community 751 - "test_command_service.py"
Cohesion: 0.03
Nodes (68): MythosValidationError, command_service(), mock_request(), mock_user(), asyncio, fixture, Unit tests for command service. Tests the CommandService class which handles…, Test _parse_command_string successfully parses command. (+60 more)

### Community 752 - "_GenerateOpenapiSpecModule"
Cohesion: 0.19
Nodes (15): _GenerateOpenapiSpecModule, _load_script(), fixture, Protocol, Unit tests for scripts/generate_openapi_spec.py's tag-table generation logic.…, Typed surface of the loaded script, for the parts these tests exercise., Build a minimal OpenAPI-shaped dict: one operation per tag list in paths_tags., script() (+7 more)

### Community 753 - "room_validator/tests/conftest.py"
Cohesion: 0.15
Nodes (18): dead_end_room(), invalid_room_data(), fixture, Pytest configuration and fixtures for room validator tests. Provides test data…, Sample room database for testing., Invalid room data for testing error conditions., Room data using the new object format for exits., Room data with self-reference exit. (+10 more)

### Community 754 - "coerce_int"
Cohesion: 0.15
Nodes (19): Parse numeric fields from object-typed JSON command payloads., Coerce a JSONB stat value to int for DP and combat helpers., _stats_int(), parametrize, Unit tests for server.utils.int_coercion.coerce_int., JSONB stats use the same coercion as inventory command payloads., test_coerce_int_bool_before_int(), test_coerce_int_float() (+11 more)

### Community 755 - ".build_subject"
Cohesion: 0.15
Nodes (9): Any, Build a NATS subject from a pattern and parameters. Args: pattern_name: Name of…, Ensure pattern exists in registry. Args: pattern_name: Name of the pattern to…, Ensure all required parameters are provided. Args: pattern_name: Name of the…, Format subject string from pattern and parameters. Args: pattern_name: Name of…, Ensure subject length is within limits. Args: subject: Subject string to…, Get information about a registered pattern. Args: pattern_name: Name of the…, Get all registered patterns. Returns: Dictionary of all registered patterns… (+1 more)

### Community 756 - "Animate Skill"
Cohesion: 0.11
Nodes (18): Animate Skill, Accessibility, Assess Animation Opportunities, CSS Animations, Delight Moments, Entrance Animations, Feedback & Guidance, Implement Animations (+10 more)

### Community 757 - "Polish Systematically"
Cohesion: 0.11
Nodes (18): Polish Skill, Code Quality, Color & Contrast, Content & Copy, Edge Cases & Error States, Final Verification, Forms & Inputs, Icons & Images (+10 more)

### Community 758 - "overrides"
Cohesion: 0.13
Nodes (15): overrides, @asyncapi/specs, fast-uri, flatted, glob, js-yaml, linkify-it, lodash (+7 more)

### Community 759 - "Enhanced Logging Quick Reference"
Cohesion: 0.17
Nodes (12): Clear Context, Context Binding, 🚨 CRITICAL: DO NOT USE, Enhanced Logging Quick Reference, For complete documentation, see [ENHANCED_LOGGING_GUIDE.md](ENHANCED_LOGGING_GUIDE.md), Log Levels, ✅ MANDATORY: ALWAYS USE, One-page cheat sheet for MythosMUD enhanced logging patterns (+4 more)

### Community 760 - "Migration 019 Ready for Deployment"
Cohesion: 0.12
Nodes (17): Migration 019 Complete Summary, 019_postgresql_anti_patterns_fixes.sql, Migration 019 Ready for Deployment, Application Script, Database Schema, Documentation, Files Ready, Implementation Complete (+9 more)

### Community 761 - "Gladiator Ring (Arena) Implementation Plan"
Cohesion: 0.11
Nodes (16): Gladiator Ring (Arena) — Implementation Todos, Phase 1: Schema and world data (Codebase Explorer for DML/schema pattern discovery) — DONE, Phase 2: Tutorial exit and respawn (main agent), Phase 3: NPC startup — also spawn in arena (main agent) — DONE, Phase 4: Tests and validation (main agent / Test Suite Analyzer) — DONE, Plan frontmatter todos (for Cursor plan file), Subagent usage, Todos (detailed) (+8 more)

### Community 762 - "Python Model Updates Required for Migration 019"
Cohesion: 0.11
Nodes (18): 1. Import BigInteger, 2. Files Requiring Updates, Impact Assessment, Integer → BigInteger, Low Risk Changes, No Breaking Changes Expected, Overview, Python Model Updates Required for Migration 019 (+10 more)

### Community 763 - "Recommended Test Additions"
Cohesion: 0.11
Nodes (18): 1. MessageBroker Integration Tests (15 tests, ~1 hour), 2. ApplicationContainer Lifecycle Tests (10 tests, ~1 hour), 3. Database Migration Tests (10 tests, ~1.5 hours), 4. WebSocket Edge Case Tests (15 tests, ~2 hours), 5. Error Recovery Tests (20 tests, ~3 hours), Additions, Coverage Gap Priority Matrix, If We Execute Full Recommendations (+10 more)

### Community 764 - "Critical Coverage Gaps"
Cohesion: 0.11
Nodes (18): Critical Coverage Gaps, Database Connection Loss, Gap 10: Configuration Edge Cases, Gap 1: Domain Layer (NEW ARCHITECTURE), Gap 2: Message Broker Abstraction, Gap 3: ApplicationContainer Lifecycle, Gap 4: Error Recovery Paths, Gap 5: Async/Await Pattern Verification (+10 more)

### Community 765 - "Execution Steps"
Cohesion: 0.11
Nodes (17): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 7: Who Command **[REQUIRES MULTI-PLAYER]**, Step 10: Verify Single Player Who List, Step 1: AW Uses Who Command (+9 more)

### Community 766 - "properties"
Cohesion: 0.06
Nodes (34): integer, minimum, type, minimum, type, null, maxLength, minLength (+26 more)

### Community 767 - "properties"
Cohesion: 0.20
Nodes (10): properties, minLength, pattern, type, minLength, type, type, id (+2 more)

### Community 768 - "fix_markdown_blanks_around_lists.py"
Cohesion: 0.17
Nodes (17): fix_blanks_around_lists(), fix_markdown_file(), get_list_type(), is_code_block_delimiter(), is_list_item(), is_table_row(), main(), parse_markdownlint_output() (+9 more)

### Community 769 - "init_npc_database.py"
Cohesion: 0.16
Nodes (17): _determine_database_init_flags(), get_npc_database_url(), get_npc_seed_data_from_postgresql(), init_database_schema(), _initialize_database_with_url(), main(), populate_npc_data(), _print_final_message() (+9 more)

### Community 770 - "test_profession_repository.py"
Cohesion: 0.14
Nodes (23): _bool_or_default(), Any, Profession, Return value as str or a default if falsy., Return text value or default if falsy., Return bool(value) when not None, otherwise default., Map procedure result row to Profession model., Get all available professions. Returns: list[Profession]: List of all… (+15 more)

### Community 771 - "validate_admin_permission"
Cohesion: 0.23
Nodes (14): Any, Validate that a player has admin permissions. Args: player: Player object to…, validate_admin_permission(), _BrokenAdminPlayer, mock_admin_logger(), asyncio, fixture, Unit tests for admin permission validation. (+6 more)

### Community 772 - "PartyService"
Cohesion: 0.14
Nodes (21): PartyUpdated, Event fired when party membership or leadership changes. Emitted by…, PartyService, Party service for MythosMUD. In-memory ephemeral party state: parties exist…, In-memory party management: create, disband, add/remove/kick members, leader…, event_bus(), party_events(), party_service() (+13 more)

### Community 773 - "_make_mock_row"
Cohesion: 0.12
Nodes (17): _make_mock_row(), UUID, Test get_player_by_name successfully retrieves player., Test list_players successfully retrieves players., Test get_player_by_id successfully retrieves player., Test get_players_by_user_id successfully retrieves players., Test get_active_players_by_user_id successfully retrieves active players., Test get_players_in_room successfully retrieves players. (+9 more)

### Community 774 - "Phase 3: Polish and Optimization"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 3: Polish and Optimization, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 775 - "test_player_spell_repository.py"
Cohesion: 0.27
Nodes (16): _mock_session_with_rows(), asyncio, fixture, Unit tests for PlayerSpellRepository., repo(), _spell_row(), test_get_player_spell_found(), test_get_player_spell_missing() (+8 more)

### Community 776 - "Phase 4: Testing and Refinement"
Cohesion: 0.15
Nodes (13): Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Acceptance Criteria, Phase 4: Testing and Refinement, Sub-tasks, Sub-tasks, Sub-tasks (+5 more)

### Community 777 - "test_chat_message_senders.py"
Cohesion: 0.27
Nodes (21): _attr(), _ctx(), _player(), asyncio, ChatMessage, Unit tests for chat message senders., MagicMock attributes are Any; getattr+cast is the typed access path., test_normalize_player_id() (+13 more)

### Community 778 - "Introduce Color Strategically"
Cohesion: 0.12
Nodes (17): Colorize Skill, Accent Color Application, Accessibility, Assess Color Opportunity, Background & Surfaces, Balance & Refinement, Borders & Accents, Cohesion (+9 more)

### Community 779 - "saveMapChanges.ts"
Cohesion: 0.16
Nodes (22): buildJsonHeaders(), createExit(), deleteExit(), ParsedEdgeId, parseEdgeId(), readErrorDetail(), recalculateCoordinates(), RecalculateCoordinatesResult (+14 more)

### Community 780 - "usePanelContext.ts"
Cohesion: 0.25
Nodes (13): usePanel(), usePanelActions(), usePanelContext(), usePanelLayout(), defaultPanels, PanelContext, PanelContextType, PanelLayout (+5 more)

### Community 781 - "commandStore.ts"
Cohesion: 0.16
Nodes (15): CommandActions, CommandAlias, CommandHistoryEntry, CommandSelectors, CommandState, CommandStore, CommandStoreGet, CommandStoreSet (+7 more)

### Community 782 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Starter Set  (2026-08-12)"
Cohesion: 0.12
Nodes (16): Communities (9 total, 4 thin omitted), Community 0 - "De Vermiis Mysteriis; Dust of Ibn-Ghazi", Community 1 - "Character Creation", Community 2 - "Alone Against the Flame", Community 3 - "Cover Art", Community 4 - "Azathoth; Banishment Chant (Latin)", Community Hubs (Navigation), Corpus Check (+8 more)

### Community 783 - "Petersen's Abominations.md"
Cohesion: 0.13
Nodes (10): Chaosium catalog notes, Voice on the Phone, Dimensional Shambler, Key extrated pages, Petersen's Abominations (source summary), Hotel Hell, Mohole, Cosmic Horror (+2 more)

### Community 784 - "Geography Overview.md"
Cohesion: 0.12
Nodes (12): Code Graph Entry, Live exploration (preferred for "how does X work?"), Synced community wiki (read-only dump), Chaosium pack graphs (external), Relationship to this vault, Geography and Major Locations (source summary), Geography Overview, Engineering memory (+4 more)

### Community 785 - "Chaosium CoC Catalog"
Cohesion: 0.14
Nodes (14): Chaosium CoC Catalog, Creature / motif families (adaptation stubs), How to use, MythosMUD adaptation notes, Ongoing ops, Tier A (full or batch-promoted), Tier B (source-only), Tier C (+6 more)

### Community 786 - "players.sql"
Cohesion: 0.10
Nodes (6): schema_name.get_user_id_by_username_ci(), schema_name.player_is_deleted(), schema_name.reserve_invite(), players, users, invites

### Community 787 - "applies_to"
Cohesion: 0.28
Nodes (9): items, minItems, type, uniqueItems, items, items, minLength, type (+1 more)

### Community 788 - "Async Remediation Complete"
Cohesion: 0.12
Nodes (17): Async Remediation Complete, Adjusts spectacles with scholarly satisfaction, Critical Fixes Implemented (4 Code Changes), December 3, 2025, Documentation Created (5 Documents, ~2,500 lines), 📚 Key Documents, 🎓 Key Takeaway, Mission Accomplished (+9 more)

### Community 789 - "Execution Steps"
Cohesion: 0.12
Nodes (16): BEFORE EXECUTING THIS SCENARIO, YOU MUST VERIFY, Execution Steps, ⚠️ FAILURE TO VERIFY THESE PREREQUISITES = COMPLETE SCENARIO FAILURE, Overview, Prerequisites, Scenario 6: Admin Teleportation **[REQUIRES MULTI-PLAYER]**, Step 1: Verify Admin Status, Step 2: AW Teleports Ithaqua (+8 more)

### Community 790 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 791 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 792 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 793 - "fix_file"
Cohesion: 0.18
Nodes (16): fix_blanks_around_fences(), fix_blanks_around_headings(), fix_blanks_around_lists(), fix_fence_language(), fix_file(), fix_line_length(), fix_trailing_punctuation_in_headings(), main() (+8 more)

### Community 794 - "jackson_linter.py"
Cohesion: 0.20
Nodes (16): collect_json_files(), _file_appears_binary_or_terminal_output(), _first_fallback_encoding_that_parses(), _is_vscode_jsonc_settings(), main(), Path, Discover JSON files under cwd, validate syntax, return exit code (0 ok, 1…, VS Code allows JSON with Comments in settings.json; stdlib json cannot parse it. (+8 more)

### Community 795 - "RoomFilenameMigrator"
Cohesion: 0.19
Nodes (10): main(), Path, Update the room ID in the JSON file to match new naming schema., Execute the migration., Handles migration of room filenames from old to new schema., Initialize the migrator., Parse old filename format to extract components., Discover all room files that need migration. (+2 more)

### Community 796 - "game_tick_processing.py"
Cohesion: 0.02
Nodes (171): get_current_tick(), Shared game tick counter. Kept in a leaf module so combat services can read the…, Get the current game tick., Set the current game tick (game tick loop)., Reset the current tick for testing., reset_current_tick(), set_current_tick(), _handle_player_death_threshold() (+163 more)

### Community 797 - "get_cache_manager"
Cohesion: 0.17
Nodes (14): cached(), Cache service for MythosMUD server. This module provides caching services that…, Decorator to cache function results. Args: cache_name: Name of the cache to use…, Caching module for MythosMUD server. This module provides comprehensive caching…, get_cache_manager(), LRU Cache implementation for MythosMUD server. This module provides thread-safe…, Get the global cache manager instance. Returns: The global cache manager…, Reset the global cache manager (for testing). (+6 more)

### Community 798 - "ProfessionCacheService"
Cohesion: 0.14
Nodes (9): ProfessionCacheService, Service for caching profession data., Get all professions with caching. Returns: List of profession objects, Get a specific profession by ID with caching. Args: profession_id: The…, Invalidate all profession caches., Create room and profession cache services; set to None on RuntimeError., _Profession, fixture (+1 more)

### Community 799 - "CacheManager"
Cohesion: 0.14
Nodes (9): CacheManager, Any, Centralized cache manager for MythosMUD server. Manages multiple LRU caches for…, Initialize the cache manager., Initialize default caches with appropriate configurations., Get a cache by name. Args: name: The name of the cache Returns: The cache…, Create a new cache. Args: name: The name of the cache max_size: Maximum number…, Delete a cache. Args: name: The name of the cache to delete Returns: True if… (+1 more)

### Community 800 - "test_occupants.py"
Cohesion: 0.18
Nodes (16): _format_occupants_result(), _get_event_handler_for_test_occupants(), _get_room_id_for_test_occupants(), Any, NPC test-occupants command for debugging occupant queries., Resolve application, player, room_id, and event handler for NPC test occupants…, Get room_id from args or current room. Returns (room_id, error_result)., Get event handler from app.state. Returns (event_handler, error_result). (+8 more)

### Community 801 - "handle_time_command"
Cohesion: 0.18
Nodes (16): handle_time_command(), Any, Time command handlers for MythosMUD. This module contains handlers for the time…, Handle the time command, exposing the current Mythos time and active holidays., asyncio, Unit tests for time command handlers. Tests the time command functionality., Test handle_time_command() handles holiday service errors., Test handle_time_command() handles missing holiday service. (+8 more)

### Community 802 - "_ensure_alias_storage"
Cohesion: 0.14
Nodes (10): _ensure_alias_storage(), Ensure alias storage is initialized., Test _ensure_alias_storage function., Test _ensure_alias_storage returns existing storage if provided., Test _ensure_alias_storage initializes new storage when None., Test _ensure_alias_storage returns None on initialization error., TestEnsureAliasStorage, Test _ensure_alias_storage creates new storage when None. (+2 more)

### Community 803 - "PlayerSchemaConverter"
Cohesion: 0.09
Nodes (24): Item prototype registry for command modules., _inventory_item_with_weapon(), PlayerSchemaConverter, Any, Get stats, inventory, and status_effects from player, handling async methods., Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…, Get PositionState from position value, with fallback to STANDING., Create PlayerRead schema from player object. (+16 more)

### Community 804 - "command_service.py"
Cohesion: 0.04
Nodes (89): Command service for MythosMUD. This module provides the main command processing…, handle_me_command(), handle_pose_command(), handle_say_command(), Room-wide say; returns user-facing result dict., Set or clear persistent pose text., Help command adapter module. The original help command handler lives in…, Command processing system for MythosMUD. This package provides the command… (+81 more)

### Community 805 - "npc_combat_grace.py"
Cohesion: 0.14
Nodes (17): _connection_manager_from_config_app(), is_npc_attack_on_player_blocked_by_login_grace_period(), is_player_attack_blocked_by_login_grace_period(), ConnectionManager, UUID, Login grace-period checks for NPC combat integration (extracted to keep service…, Resolve connection_manager from the public config app accessor. Uses getattr on…, True if the player should not attack (in login grace period). Fail-open on… (+9 more)

### Community 806 - "._cleanup_player_mutes"
Cohesion: 0.09
Nodes (14): datetime, Path, Get active global mutes applied by a player., Get all mutes applied by a player. Args: player_id: Player ID Returns:…, Get system-wide user management statistics. Returns: Dictionary with system…, Clean up expired player mutes., Clean up expired channel mutes., Clean up expired global mutes. (+6 more)

### Community 807 - "CoordinateValidator"
Cohesion: 0.14
Nodes (15): _conflict_from_row(), CoordinateValidator, Any, AsyncSession, Coordinate validation service for ASCII maps. This module provides conflict…, Validates room coordinates and detects conflicts. A conflict occurs when…, Initialize coordinate validator. Args: session: Database session for coordinate…, Validate coordinates for rooms in a zone/subzone and detect conflicts. Args:… (+7 more)

### Community 808 - "asyncio"
Cohesion: 0.10
Nodes (21): asyncio, Test get_player_by_name returns None when player not found., Test get_player_by_name handles database errors., Test save_player handles database errors., Test list_players handles database errors., Test get_player_by_id returns None when player not found., Test get_player_by_user_id returns first active player., Test get_player_by_user_id returns None when no players. (+13 more)

### Community 809 - "test_nats_message_handler_chat.py"
Cohesion: 0.03
Nodes (76): asyncio, Unit tests for NATS message handler chat and messaging. Tests chat field…, Test _get_player_lucidity_tier returns default on error., Test _validate_chat_message_fields raises TypeError for invalid types., Test _validate_chat_message_fields raises TypeError for invalid sender_name…, Test _validate_chat_message_fields raises TypeError for invalid content type., Test _validate_chat_message_fields raises TypeError for invalid sender_id type., Test _extract_chat_message_fields handles whisper target_id. (+68 more)

### Community 810 - "test_analyze_idle_memory_samples.py"
Cohesion: 0.25
Nodes (14): _AnalyzeIdleMemorySamplesModule, _base_row(), _load_script(), Path, Protocol, Unit tests for scripts/analyze_idle_memory_samples.py. Covers the `--warmup`…, Typed surface of the loaded script, for the parts these tests exercise., Passing no warmup_seconds keeps existing callers' behavior unchanged. (+6 more)

### Community 811 - "test_run_test_ci.py"
Cohesion: 0.11
Nodes (23): Regression tests for scripts/run_test_ci.py's CI-gating pytest invocation, the…, pytest-xdist is removed from the project (#724); no CI step should reinstall it…, Same guarantee as the CI workflow check, for the local Docker branch of this…, scripts/install_ci_dependencies.sh is the shared installer Dockerfile.github-…, run_integration_tests_playwright.ps1 used to force -n 1 to keep integration…, pytest-xdist is removed (#724); no invocation in this script may pass -n, which…, The Run 1 / Run 2 / `coverage combine` split existed only because one module…, With only one coverage-producing run, COVERAGE_FILE can safely be the bare… (+15 more)

### Community 812 - "properties"
Cohesion: 0.12
Nodes (17): oneOf, oneOf, additionalProperties, description, properties, type, oneOf, down (+9 more)

### Community 813 - "properties"
Cohesion: 0.15
Nodes (13): oneOf, oneOf, properties, oneOf, down, east, north, south (+5 more)

### Community 814 - "Codebase Explorer Subagent"
Cohesion: 0.14
Nodes (15): Architecture Analysis, Best Practices, Capabilities, Codebase Explorer Subagent, Dependency Research, Example Scenarios, Finding All Implementations, Integration (+7 more)

### Community 815 - ".accept_party_invite"
Cohesion: 0.20
Nodes (6): Remove expired pending invites and notify inviters., Send a command_response-style message to a single player., Send party_invite event to the target player only., Create a pending party invite and send party_invite event to target. Target…, Accept a party invite. Target is the player who accepted (the invitee)., Decline a party invite.

### Community 816 - "Adapt Skill"
Cohesion: 0.12
Nodes (16): Adapt Skill, Assess Adaptation Challenge, Content Adaptation, Desktop Adaptation (Mobile → Desktop), Email Adaptation (Web → Email), Implement Adaptations, Layout Adaptation Techniques, MANDATORY PREPARATION (+8 more)

### Community 817 - "Improve Copy Systematically"
Cohesion: 0.12
Nodes (16): Clarify Skill, Apply Clarity Principles, Assess Current Copy, Button & CTA Text, Confirmation Dialogs, Empty States, Error Messages, Form Labels & Instructions (+8 more)

### Community 818 - "UX Writing"
Cohesion: 0.12
Nodes (16): Avoid Redundant Copy, Confirmation Dialogs: Use Sparingly, Consistency: The Terminology Problem, Don't Blame the User, Empty States Are Opportunities, Error Message Templates, Error Messages: The Formula, Form Instructions (+8 more)

### Community 819 - "whisper-movement.spec.ts"
Cohesion: 0.21
Nodes (13): assertNeitherPlayerInVoid(), attemptEastHop(), bringFrontAndAssertPlayerBanner(), deliverWhisperAcrossRooms(), focusCommandInput(), hopEastUntilHallway(), lookAndWaitForUi(), moveAwToEasternHallway() (+5 more)

### Community 820 - "containers.sql"
Cohesion: 0.13
Nodes (5): container_contents, schema_name.add_item_to_container(), schema_name.get_container_contents_json(), item_instances, item_prototypes

### Community 821 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)"
Cohesion: 0.12
Nodes (15): Communities (17 total, 12 thin omitted), Community 0 - "Character and Skills", Community 1 - "Character and Skills (1)", Community 2 - "Core Rules", Community 3 - "Core Rules (3)", Community 4 - "Character Sheets", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 822 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Down Darker Trails  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (12 total, 7 thin omitted), Community 0 - "Call of Cthulhu (7th Edition); Chaosium Inc.", Community 1 - "APP; Characteristics", Community 2 - "Everett Scanlon; Gustavo Romero", Community 3 - "First Aid; Hit Points", Community 4 - "Formless Spawn of Tsathoggua; Rudolf Zimmer", Community Hubs (Navigation), Corpus Check (+7 more)

### Community 823 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)"
Cohesion: 0.12
Nodes (15): Communities (5 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Bernard Corbitt; Randolph Tomaszewski", Community 2 - "Ramasekva; Yog-Sothoth", Community 3 - "Arthur Cornthwaite; Fitzgerald Manse", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions) (+7 more)

### Community 824 - "mythos_dev.players"
Cohesion: 0.10
Nodes (22): mythos_dev.account_sanctions, mythos_dev.corruption_adjustment_log, mythos_dev.corruption_cooldowns, mythos_dev.id_map_players, mythos_dev.invites, mythos_dev.lucidity_adjustment_log, mythos_dev.lucidity_cooldowns, mythos_dev.lucidity_exposure_state (+14 more)

### Community 825 - "Changes by document"
Cohesion: 0.12
Nodes (16): Changes by document, CLAUDE.md, docs/COMMAND_MODELS_REFERENCE.md, docs/CONFIGURATION_FILES_REFERENCE.md, docs/CONTAINER_SYSTEM_API_REFERENCE.md, docs/DATABASE_ACCESS_PATTERNS.md, docs/E2E_TESTING_GUIDE.md, docs/EVENT_OWNERSHIP_MATRIX.md (+8 more)

### Community 826 - "Memory Leak Audit Report"
Cohesion: 0.12
Nodes (16): Audit Completion Summary, Audit Methodology, _closed_websockets Unbounded Set, Common Patterns Identified, EventBus Subscriber Leaks, Executive Summary, ✅ Good Patterns (No Leaks), High Priority Fixes (+8 more)

### Community 827 - "Quick Start: Running E2E Tests"
Cohesion: 0.12
Nodes (16): Expected Results, Method A: Use the E2E startup script (Simplest), Method B: Manual startup (More control), Next Actions, Prerequisites ✅, Problem: "element(s) not found" errors, Problem: Login failed (500), Problem: Server won't start (+8 more)

### Community 828 - "holiday.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 829 - "schedule.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 830 - "type"
Cohesion: 0.15
Nodes (16): items, type, items, type, minLength, type, damage_types, effect_components (+8 more)

### Community 831 - "analyze_coverage_gaps.py"
Cohesion: 0.23
Nodes (15): categorize_files(), generate_status_doc(), main(), parse_coverage_xml(), Any, Path, Categorize files into critical below threshold, normal below threshold, and…, Write critical files below threshold section. (+7 more)

### Community 832 - "_apply_arena_seed_patch.py"
Cohesion: 0.28
Nodes (15): _append_before_copy_terminator(), _apply_arena_room_links(), _apply_arena_room_rows(), _apply_zone_configuration_row(), _apply_zones_and_subzones(), _insert_after_line_containing(), _load_arena_links(), _load_arena_rooms() (+7 more)

### Community 833 - "pylint.py"
Cohesion: 0.23
Nodes (13): _combined_output(), _CompletedProcessLike, is_pylint_startup_failure(), main(), Path, Protocol, Prefer current interpreter -m pylint (works under uv run --no-sync)., Fail fast before scanning if pylint cannot start (missing package, broken venv). (+5 more)

### Community 834 - "generate_sql.mjs"
Cohesion: 0.30
Nodes (15): ajv, __dirname, ensureDir(), __filename, generateEmotes(), generateHolidays(), generateNpcSchedules(), generateRooms() (+7 more)

### Community 835 - "SpellMaterialsService"
Cohesion: 0.18
Nodes (10): Any, UUID, Build final inventory with consumed materials removed. Args: inventory:…, Consume spell materials from player inventory. Args: player_id: Player ID…, Service for handling spell material requirements. Handles checking if players…, Initialize the spell materials service. Args: player_service: Player service…, Check if player has all required materials. Args: player_id: Player ID spell:…, Process a single material requirement. Args: material: Material requirement… (+2 more)

### Community 836 - "UUID"
Cohesion: 0.17
Nodes (9): Any, UUID, Broadcast party message to party members only, with dampening and mute checks., Send whisper message to specific player with communication dampening., Broadcast system/admin message; personal when target_player_id is set., Handle unknown channel type., Broadcast message according to channel strategy. Args: chat_event: WebSocket…, Broadcast room-based message with server-side filtering. (+1 more)

### Community 837 - "get_npc_name_from_instance"
Cohesion: 0.17
Nodes (15): get_npc_name_from_instance(), Get NPC name from the actual NPC instance, preserving original case from…, Unit tests for connection utils. Tests the connection_utils module functions., Test get_npc_name_from_instance() returns NPC name when found., Test get_npc_name_from_instance() returns None when NPC not found., Test get_npc_name_from_instance() returns None when NPC has no name., Test get_npc_name_from_instance() returns None when service not available., Test get_npc_name_from_instance() returns None when no lifecycle manager. (+7 more)

### Community 838 - "bundles/game.py"
Cohesion: 0.04
Nodes (65): LinkRow, RoomRow, Game bundle: player, room, movement, exploration, user_manager,…, decode_json_column(), Any, Shared utilities for container and bundles. Holds helpers extracted from…, Decode a JSON column value, returning the type's default on failure. Used by…, _DatabaseLoadResult (+57 more)

### Community 839 - "ContainerLockMixin"
Cohesion: 0.23
Nodes (10): ContainerLockMixin, Player, UUID, Lock a container (LOCKED or SEALED). Requires ownership or admin., Unlock a container. Requires access and unlock eligibility (key/admin)., Lock/unlock container state persistence., Load container for lock/unlock ops, or raise ContainerNotFoundError., Load player for lock/unlock ops, or raise ValidationError. (+2 more)

### Community 840 - "command_result_text"
Cohesion: 0.05
Nodes (88): Remove or update item quantity in player inventory after transfer., remove_item_from_inventory(), handle_inventory_command(), CommandResponse, Display the player's inventory and equipped items, including container contents., handle_put_command(), _put_resolve_container_id(), _put_run_validated() (+80 more)

### Community 841 - "test_security_headers.py"
Cohesion: 0.03
Nodes (75): MutableHeaders, CorrelationMiddleware, create_correlation_middleware(), _get_header(), Any, ASGIApp, Receive, Scope (+67 more)

### Community 842 - "test_follow_flow.py"
Cohesion: 0.17
Nodes (15): connection_manager(), event_bus(), follow_service(), movement_service(), asyncio, fixture, Integration tests for follow feature. Flow: Player A requests follow B; B…, Real EventBus for integration. (+7 more)

### Community 843 - "CircuitBreaker"
Cohesion: 0.04
Nodes (75): CircuitBreaker, CircuitBreakerOpen, CircuitState, Any, Enum, Exception, timedelta, Circuit breaker pattern for NATS message processing. Implements three-state… (+67 more)

### Community 845 - "test_combat_messaging_integration.py"
Cohesion: 0.12
Nodes (15): Unit tests for combat messaging integration. Tests the…, Test connection_manager setter updates value., Test connection_manager setter overrides lazy load mechanism., A room broadcast with failed_deliveries must log at error level, not just debug…, A clean room broadcast (no failures) stays at debug level., Test CombatMessagingIntegration initialization., Test connection_manager property lazy loads from container., Test _resolve_connection_manager_from_container raises when no manager. (+7 more)

### Community 846 - "test_player_repository.py"
Cohesion: 0.12
Nodes (15): Unit tests for player repository. Tests the PlayerRepository class which…, Test PlayerRepository initializes correctly., Test PlayerRepository initializes with room cache., Test PlayerRepository initializes with event bus., Test validate_and_fix_player_room returns False for valid room., Test validate_and_fix_player_room fixes invalid room., Test save_player successfully saves player., Test delete_player returns False when player not found. (+7 more)

### Community 847 - "test_check_no_production_assert.py"
Cohesion: 0.18
Nodes (15): _load_checker(), _NoProductionAssertModule, Path, Protocol, Tests for scripts/check_no_production_assert.py., Verify no-production-assert hook targets server code and excludes tests., Public surface of check_no_production_assert loaded via importlib., test_find_assert_line_numbers_detects_assert() (+7 more)

### Community 848 - "HallucinationRng"
Cohesion: 0.18
Nodes (10): HallucinationRng, Random, Shared RNG for the hallucination subsystem (#714). Deterministic when…, Lazily-seeded `random.Random`, shared by every hallucination call site., Return the shared RNG, seeding it from config on first use., Drop the cached RNG so the next `get()` re-reads the config seed (tests)., Unit tests for the shared hallucination RNG (#714)., test_get_returns_same_instance_across_calls() (+2 more)

### Community 849 - "test_validate_codacy_coverage_gate.py"
Cohesion: 0.18
Nodes (15): _CodacyGateModule, _load_gate_module(), Path, Protocol, Tests for scripts/validate_codacy_coverage_gate.py (Codacy upload quality gate)., Public surface of validate_codacy_coverage_gate loaded via importlib., `coverage xml --cov=server` writes `<source>server</source>` and lists…, An empty/malformed Cobertura report (no <class> elements at all) must still be… (+7 more)

### Community 850 - "ADR-018: New Game Session vs Grace Reconnect"
Cohesion: 0.13
Nodes (14): ADR-004: WebSocket-Only Real-Time Architecture, ADR-018: New Game Session vs Grace Reconnect, ADR-020: WebSocket Authentication and CSRF, 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences (+6 more)

### Community 851 - "test_logging_file_categories.py"
Cohesion: 0.15
Nodes (15): Unit tests for DEFAULT_LOG_CATEGORIES. Regression coverage for #687: the…, No "infrastructure" category: server/infrastructure/ (its only logger source)…, No surviving category's logger-name list should point at the deleted…, #297: get_logger(__name__) in server/realtime/*.py produces…, Undo add_handler_to_loggers' effects on both loggers it touches for a given…, #297/#610: NPC behavior-engine/threading debug lines fire continuously enough…, The e2e-only suppression must not leak into local development, where full NPC…, Regression guard: the new npc-specific e2e branch must not shadow the existing… (+7 more)

### Community 852 - "Spatial Design"
Cohesion: 0.13
Nodes (14): Cards Are Not Required, Container Queries, Depth & Elevation, Grid Systems, Hierarchy Through Multiple Dimensions, Name Tokens Semantically, Optical Adjustments, Spacing Systems (+6 more)

### Community 853 - "Typography"
Cohesion: 0.13
Nodes (14): Accessibility Considerations, Choosing Distinctive Fonts, Classic Typography Principles, Fluid Type, Font Selection & Pairing, Modern Web Typography, Modular Scale & Hierarchy, OpenType Features (+6 more)

### Community 854 - "Fix patterns by tier"
Cohesion: 0.13
Nodes (13): 🔴 Critical — import and name errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — type errors, 🔵 Low — type precision, 🟢 Medium — type refinement, Mypy Remediation — Reference (+5 more)

### Community 855 - "Skill: Create a New Worktree for a Task"
Cohesion: 0.13
Nodes (15): Worktree Workflow Skill, Canonical Layout (Summary), MythosMUD Worktree Workflow, Preconditions and Safety, Skill: Clean Up a Completed or Stale Worktree, Skill: Create a New Worktree for a Task, Step 1 — Gather Task Metadata, Step 2 — Derive Names and Paths (+7 more)

### Community 856 - "MessageBatcher"
Cohesion: 0.25
Nodes (4): BatchConfig, BatchedMessage, MessageBatcher, useMessageBatcher()

### Community 857 - "RateLimiter"
Cohesion: 0.14
Nodes (11): fixture, rate_limiter(), Create a RateLimiter instance for testing., Utility modules for MythosMUD server. This package contains various utility…, Any, RateLimiter, Enforce rate limiting for a user. Args: user_id: The user's ID Raises:…, Simple in-memory rate limiter for API endpoints. This rate limiter tracks… (+3 more)

### Community 858 - "P4 · Intent Sweep — Core Feature Issues"
Cohesion: 0.13
Nodes (14): #17 · Party — one of three bullets built, #21 · Admin commands — "ban" was in the issue title and never built, #29 · Cultist faction and PvP — zero implementation, #30 · Branching quests and morality — two of three bullets absent, #62 · Tick-rate validation — not built, #9 · The xterm.js substitution — real, user-facing, unrecorded, CLOSED BUT NOT BUILT, Conforming, worth recording (+6 more)

### Community 859 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11)"
Cohesion: 0.13
Nodes (14): Communities (8 total, 5 thin omitted), Community 0 - "Baron Arthur von Kleist; Pyotr Shabelsky-Bork", Community 1 - "The Demon-Großmann; Demonic Mutation Table", Community 2 - "Erwin Kern; Manfred Freiherr von Killinger", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Berlin - The Wicked City  (2026-08-11) (+6 more)

### Community 860 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Scenario Handouts", Community 1 - "Anna Konrad; Lucas Reston", Community 2 - "Does Love Forgive", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Does Love Forgive_  (2026-08-12) (+6 more)

### Community 861 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12)"
Cohesion: 0.13
Nodes (14): Communities (4 total, 1 thin omitted), Community 0 - "Pre-Generated Investigators", Community 1 - "Pre-Generated Investigators (1)", Community 2 - "Pre-Generated Investigators (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Gateways to Terror  (2026-08-12) (+6 more)

### Community 862 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\S. Petersen's Field Guide to Lovecraftian Horrors  (2026-08-12)"
Cohesion: 0.13
Nodes (15): Communities (10 total, 4 thin omitted), Community 0 - "Azathoth / Byakhee", Community 1 - "Call of Cthulhu / Chaosium Inc.", Community 2 - "Dimensional Shambler / Elder Thing", Community 3 - "Abhoth / Atlach-Nacha", Community 4 - "Deep One / Ghast", Community 5 - "Dark Young / Dark Young of Shub-Niggurath", Community Hubs (Navigation) (+7 more)

### Community 863 - "rooms.sql"
Cohesion: 0.15
Nodes (4): schema_name.create_room_link(), schema_name.delete_room_link(), schema_name.update_room_link(), rooms

### Community 864 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 865 - "npc_schedules.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, schedules, required, $schema, title, type

### Community 866 - "DOCUMENTATION_AUDIT.md"
Cohesion: 0.15
Nodes (13): Audit date, Code as Source of Truth, Documentation vs. Code Accuracy Audit Log, Summary, CONNECTION_MANAGER_ARCHITECTURE.md, ConnectionManager Modular Architecture, Logging Best Practices Pointer, ENHANCED_LOGGING_GUIDE.md (+5 more)

### Community 867 - "PARALLEL EXECUTION RESULTS (2025-11-05)"
Cohesion: 0.13
Nodes (15): After Parallelization, Before Parallelization, Benefits, Changes Implemented, Comprehensive Tests (Serial + Long-Running), Daily Development Tests (Parallel), Excluded from Fast Suite, FINAL METRICS (+7 more)

### Community 868 - "Result"
Cohesion: 0.13
Nodes (10): database, Simulate database operations., Simulate database query., Simulate database execute., database, Simulate database operations., Simulate database execute., Simulate user creation. (+2 more)

### Community 869 - "fix_markdown_common_issues.py"
Cohesion: 0.22
Nodes (14): fix_emphasis_as_heading(), fix_first_line_heading(), fix_link_fragments(), fix_markdown_file(), generate_anchor(), main(), parse_markdownlint_output(), Path (+6 more)

### Community 870 - "process_room_files"
Cohesion: 0.21
Nodes (14): load_room_file(), main(), process_room_files(), Path, Load a room file safely., Save a room file safely., Convert room ID to lowercase., Convert filename to lowercase. (+6 more)

### Community 871 - "validate_codacy_coverage_gate.py"
Cohesion: 0.25
Nodes (14): cobertura_has_server_sources(), cobertura_root_line_rate(), lcov_aggregate_hits(), main(), _parse_cobertura_xml(), Path, Parse Cobertura XML with defusedxml (lazy import: LCOV-only runs skip this…, Return root line-rate from Cobertura XML (0.0--1.0). (+6 more)

### Community 872 - "ProcessedRoomData"
Cohesion: 0.22
Nodes (13): Delegate to room loader; exposed for unit tests., ProcessedRoomData, TypedDict, Intermediate room row after zone/id normalization., Mutable container passed through room object construction., Payload passed to Room.__init__ during cache load., RoomInitPayload, RoomLoadResult (+5 more)

### Community 873 - "test_look_item.py"
Cohesion: 0.09
Nodes (27): _get_item_description_from_prototype(), Get item description from prototype registry. Returns: Formatted result string…, Unit tests for item look functionality. Tests the helper functions for looking…, Test finding item in equipped items by name., Test finding item in equipped items when not found., Test getting item description from prototype., Test getting item description when prototype registry is None., Test getting item description when prototype_id is missing. (+19 more)

### Community 874 - "rest_countdown_task.py"
Cohesion: 0.21
Nodes (16): create_rest_countdown_task(), _disconnect_player_after_rest(), _handle_countdown_loop(), _is_rest_interrupted(), Any, Task, UUID, Rest countdown task implementation. This module contains the async task that… (+8 more)

### Community 875 - "room_hierarchy_schema.json"
Cohesion: 0.17
Nodes (11): additionalProperties, anyOf, description, description, exits, id, name, required (+3 more)

### Community 876 - "factory.py"
Cohesion: 0.03
Nodes (85): main(), Rewrite the generated tag table between its markers in the spec doc., Replace auth token examples with clearly fake placeholders., Generate and write OpenAPI spec to docs/openapi/openapi.json., Tags actually declared by routes, in first-seen order. This is the authority., name -> description, from the spec's top-level tags block (OPENAPI_TAGS)., Build the markdown table, failing loudly if a route tag has no description., _render_tag_table() (+77 more)

### Community 877 - "enum"
Cohesion: 0.17
Nodes (12): default, description, enum, type, arena, indoors, intersection, outdoors (+4 more)

### Community 878 - "TestValidateRoomData"
Cohesion: 0.15
Nodes (11): patch, Test validate_room_data() function., Test validate_room_data() returns empty list when validation not available., Test validate_room_data() with provided validator., Test validate_room_data() creates validator when not provided., Test validate_room_data() returns validation errors., Test validate_room_data() raises exception in strict mode with errors., Test validate_room_data() returns empty list when validator creation fails. (+3 more)

### Community 879 - "Any"
Cohesion: 0.13
Nodes (8): Any, Handle an incoming event and trigger appropriate NPC reactions. Args: event:…, Update stored NPC context used by reaction conditions (room, name, alive)., Get context information for an NPC. Args: npc_id: The ID of the NPC Returns:…, Get statistics about an NPC's reactions. Args: npc_id: The ID of the NPC…, Initialize an NPC event reaction. Args: event_type: The type of event this…, Check if this reaction should trigger for the given event. Args: event: The…, Execute the reaction action. Args: event: The event that triggered the reaction…

### Community 880 - "Corruption Subsystem Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Architecture, 3. Key design decisions, 4. Constraints, 5. Component interactions, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 881 - "channel_broadcasting_strategies.py"
Cohesion: 0.14
Nodes (17): ChannelBroadcastingStrategy, GlobalChannelStrategy, PartyChannelStrategy, ABC, Channel Broadcasting Strategies for NATS Message Handler. This module…, Strategy for party channel broadcasting. Delivers only to current party members., Strategy for whisper channel broadcasting., Strategy for system/admin channel broadcasting. (+9 more)

### Community 882 - "ADR-026: Item Catalog Metadata Contracts"
Cohesion: 0.11
Nodes (17): 1. Overview, 2. Context, 3.1 Phased delivery, 3.2 Inclusion and IP, 3.3 Storage shape, 3.4 Coexistence and dedupe, 3.5 Combat bridge, 3.6 Explicitly out of scope (this ADR) (+9 more)

### Community 883 - "test_aggressive_mob_npc.py"
Cohesion: 0.25
Nodes (14): _make_aggro(), asyncio, Unit tests for AggressiveMobNPC. Regression test: aggressive mobs must have…, test_attack_target_error_returns_false(), test_attack_target_fallback_publishes_event(), test_attack_via_combat_integration_none_when_missing(), test_attack_via_create_task_with_running_loop(), test_attack_via_dropped_without_loop_or_bus() (+6 more)

### Community 884 - "CorruptionTierCache"
Cohesion: 0.24
Nodes (7): CorruptionTierCache, CorruptionTier, UUID, Module-level singleton (mirrors `lucidity_tier_cache`) -- callers MUST share…, Record this player's current tier., Return the cached tier, or `pure` if this player has never been recorded., Drop a player's cached tier (e.g. on disconnect).

### Community 885 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Accepting a party invite adds the player to the party., Declining removes pending invite and does not add to party., Request fails if target is already in a party., party_invite producer emits a build_event-shaped envelope., Requesting a party invite creates a pending invite (target must accept)., test_accept_party_invite_success(), test_decline_party_invite_success() (+3 more)

### Community 886 - "is_safe_filename"
Cohesion: 0.12
Nodes (16): is_safe_filename(), Check if a filename is safe (no path traversal, no special characters). Args:…, Test is_safe_filename with valid filename., Test is_safe_filename with empty string (considered safe)., Test is_safe_filename rejects filenames with .., Test is_safe_filename rejects filenames with forward slash., Test is_safe_filename rejects filenames with backslash., Test is_safe_filename rejects filenames with special characters. (+8 more)

### Community 887 - "test_update_container_found_returns_the_id"
Cohesion: 0.23
Nodes (14): container_row(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration tests for db/procedures/containers.sql's update_container() return-…, Create one container row. Yields its container_instance_id. (+6 more)

### Community 888 - "enum"
Cohesion: 0.18
Nodes (11): description, enum, type, arena, indoors, intersection, outdoors, street_paved (+3 more)

### Community 889 - "client/package.json"
Cohesion: 0.20
Nodes (9): argon2, engines, node, name, optionalDependencies, argon2, private, type (+1 more)

### Community 890 - "event_publisher.py"
Cohesion: 0.09
Nodes (21): _EventPersistence, _Named, _NatsPublish, Protocol, UUID, EventPublisher service for MythosMUD real-time events. This module provides a…, Initialize EventPublisher service. Args: nats_service: NATS service instance…, event_publisher() (+13 more)

### Community 891 - "ADR-024: Server-Authoritative Perceived Reality for Hallucinations"
Cohesion: 0.20
Nodes (10): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. Related docs, 8. Changelog (+2 more)

### Community 892 - "test_lint_imports.py"
Cohesion: 0.14
Nodes (14): _LintImportsModule, _load_module(), Protocol, Tests for scripts/lint_imports.py ADR-001 wrapper., Shape of scripts/lint_imports.py, loaded dynamically below (not a static…, import-linter's rich progress spinner renders emoji; on a non-UTF-8 Windows…, The parent must decode the child's output as UTF-8 too --…, test_broken_contract_count_parses_summary() (+6 more)

### Community 893 - "update_container"
Cohesion: 0.08
Nodes (27): Apply item/lock/metadata updates; returns refreshed row or None if missing., update_container(), Test update_container successfully updates container., Test update_container returns None when container not found., Test update_container handles database errors., Test update_container with no updates provided (all None)., Test update_container handles UUID to string conversion., Test update_container skips items without item_instance_id or prototype_id. (+19 more)

### Community 894 - "optimized_security_validator.py"
Cohesion: 0.13
Nodes (15): Test benchmark function runs without errors., Test stripping ANSI codes from empty string., Test stripping ANSI codes from text without ANSI., Test stripping ANSI codes from text with ANSI., test_benchmark_validation_performance(), test_optimized_strip_ansi_codes_empty(), test_optimized_strip_ansi_codes_no_ansi(), test_optimized_strip_ansi_codes_with_ansi() (+7 more)

### Community 895 - "properties"
Cohesion: 0.18
Nodes (11): description, type, description, type, description, minimum, type, combat_modifier (+3 more)

### Community 896 - "check_no_production_assert.py"
Cohesion: 0.22
Nodes (11): Assert, _AssertFinder, _excluded_server_module_filename(), find_assert_line_numbers(), is_production_server_py(), main(), _path_parts_indicate_production_server(), Path (+3 more)

### Community 897 - "Generate Comprehensive Report"
Cohesion: 0.14
Nodes (14): Audit Skill, Anti-Patterns Verdict, Critical Issues, Detailed Findings by Severity, Diagnostic Scan, Executive Summary, Generate Comprehensive Report, High-Severity Issues (+6 more)

### Community 898 - "Lint Remediation"
Cohesion: 0.14
Nodes (12): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Error code table, Fix patterns by tier, 🟡 High — code quality, Lint Remediation — Reference, 🟢 Medium — style, Entry point (+4 more)

### Community 899 - "Optimize Skill"
Cohesion: 0.14
Nodes (14): Optimize Skill, Animation Performance, Assess Performance Issues, Core Web Vitals Optimization, Cumulative Layout Shift (CLS < 0.1), First Input Delay (FID < 100ms) / INP (< 200ms), Largest Contentful Paint (LCP < 2.5s), Loading Performance (+6 more)

### Community 900 - "Semgrep Configuration"
Cohesion: 0.14
Nodes (14): Semgrep Configuration, Java Jackson Deserialization Rule, Java JMS Deserialization Rule, Java Path Traversal Rule, Java Unvalidated Redirect Rule, Java Weak SSL Context Rule, Java XPath Injection Rule, Java XSS Response Writer Rule (+6 more)

### Community 901 - "Test Server Remediation Prompt - Cursor Executable Version"
Cohesion: 0.14
Nodes (13): Best Practices, COMPLETION VERIFICATION, CRITICAL "DO NOT" INSTRUCTIONS, CRITICAL: EXECUTION REQUIREMENTS, DECISION TREE - START HERE, ERROR HANDLING PROTOCOL, MANDATORY PROGRESS TRACKING, MANDATORY VERIFICATION CHECKPOINTS (+5 more)

### Community 902 - "INDEX.md"
Cohesion: 0.23
Nodes (4): P6 · Review Queue (rebuilt), TRACK A · Code defects — not review material, TRACK B · Bulk confirmation, Design Audit Index

### Community 903 - "Decisions required"
Cohesion: 0.14
Nodes (14): A · Hard-coded metrics in documents, B · Migration scaffolding that outlived its migration, C · Broken links to archived documents, D · The design record was built from the code, Decisions required, E · Who owns query construction?, F · Layer boundaries: enforce or amend?, G · Doc ↔ doc contradictions (+6 more)

### Community 904 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (16 total, 14 thin omitted), Community 0 - "Open Mind Circle", Community 1 - "Campaign Materials", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\A Cold Fire Within  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 905 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11)"
Cohesion: 0.14
Nodes (13): Communities (6 total, 4 thin omitted), Community 0 - "Solo Investigators", Community 1 - "Design & Authorship", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Dark  (2026-08-11), Hyperedges (group relationships) (+5 more)

### Community 906 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (4 total, 1 thin omitted), Community 0 - "Keeper Screen References", Community 1 - "Keeper Screen References (1)", Community 2 - "Keeper Screen References (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition Keeper Screen Pack  (2026-08-12) (+5 more)

### Community 907 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12)"
Cohesion: 0.14
Nodes (13): Communities (3 total, 0 thin omitted), Community 0 - "Call of Cthulhu Stat Block; Chaosium Inc.", Community 1 - "Mythos Elements", Community 2 - "Mythos Elements (2)", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Malleus Monstrorum - Cthulhu Mythos Bestiary  (2026-08-12) (+5 more)

### Community 908 - "mythos_dev.rooms"
Cohesion: 0.16
Nodes (14): mythos_dev.count_coordinated_rooms(), mythos_dev.create_room_link(), mythos_dev.delete_room_link(), mythos_dev.get_room_id_by_stable_id(), mythos_dev.is_room_explored(), mythos_dev.player_exploration, mythos_dev.room_links, mythos_dev.rooms (+6 more)

### Community 909 - "Migration 019 Verification Report"
Cohesion: 0.14
Nodes (14): Before Production Deployment, Conclusion, Documentation (3 files), Files Modified Summary, Low Risk ✅, Medium Risk ⚠️, Migration 019 Verification Report, Migration Scripts (1 file) (+6 more)

### Community 910 - "NATS Anti-Patterns Remediation Summary"
Cohesion: 0.14
Nodes (14): After Remediation, Backward Compatibility, Before Remediation, Code Quality Improvements, Configuration Options, Exception Hierarchy, Executive Summary, Impact Assessment (+6 more)

### Community 911 - "analyze_log_file"
Cohesion: 0.23
Nodes (13): analyze_log_file(), categorize_error(), categorize_warning(), generate_report(), main(), parse_log_line(), Any, Path (+5 more)

### Community 912 - "find_fstring_logging_violations"
Cohesion: 0.20
Nodes (11): find_fstring_logging_violations(), format_violation_report(), FStringLoggingDetector, main(), Call, Path, Main function to scan files and report violations., AST visitor to detect f-string logging violations. (+3 more)

### Community 913 - "check_pr_issue_references.py"
Cohesion: 0.20
Nodes (13): _extract_numbers(), find_bare_references(), _format_message(), get_open_issue_numbers(), main(), Warn when a PR references an open issue without a GitHub closing keyword. This…, Return issue numbers referenced in text that are NOT preceded by a closing…, Return every #NNN issue number appearing in text, as an int set. (+5 more)

### Community 914 - "lint_raw_sql_in_python.py"
Cohesion: 0.20
Nodes (13): _collect_python_files(), _find_raw_sql_lines(), main(), Path, Guard against raw table CRUD SQL string literals inside Python source. Replaces…, Scan server/ for raw SQL. Returns a list of violation messages., Run the raw-SQL guard and return 1 if any raw-SQL site is found., Return line with a trailing '# ...' comment removed, so prose mentioning SQL… (+5 more)

### Community 915 - "lint_sql_guardrails.py"
Cohesion: 0.23
Nodes (13): check_not_in_subquery(), check_select_star(), _collect_sql_files(), main(), Path, Lightweight guardrails for hand-maintained PostgreSQL SQL. Warns on: - select *…, Return line with line comment removed (-- ...)., Return content with block comments /* ... */ removed (simple, no nested). (+5 more)

### Community 916 - "fixture"
Cohesion: 0.13
Nodes (15): mock_event_bus(), mock_player(), mock_player_combat_service(), mock_session(), player_death_service(), player_death_service_no_dependencies(), fixture, Create a mock event bus. (+7 more)

### Community 917 - "RoomCacheLoader"
Cohesion: 0.31
Nodes (4): _attributes_from_row(), Loads room data from the database and populates a room cache dict. Used by…, RoomCacheLoader, _row_optional_str()

### Community 918 - "ChannelBroadcastingStrategyFactory"
Cohesion: 0.17
Nodes (11): ChannelBroadcastingStrategyFactory, Factory for creating channel broadcasting strategies., Register a new strategy for a channel type. Args: channel_type: Channel type to…, Test ChannelBroadcastingStrategyFactory.__init__() initializes with default…, Test ChannelBroadcastingStrategyFactory.get_strategy() returns known strategy., Test ChannelBroadcastingStrategyFactory.register_strategy() registers new…, Test global channel_strategy_factory instance exists., test_channel_broadcasting_strategy_factory_get_strategy_known() (+3 more)

### Community 919 - "handle_explore_command"
Cohesion: 0.27
Nodes (9): handle_explore_command(), Any, Handle exploration requests by returning a simple message. This lightweight…, asyncio, Unit tests for exploration command handlers. Tests the exploration command…, Test handle_explore_command() explores area., Test handle_explore_command() handles missing persistence., test_handle_explore_command() (+1 more)

### Community 920 - "AsciiMapViewer.tsx"
Cohesion: 0.21
Nodes (11): AsciiMapViewer(), AsciiMapViewerProps, chooseMapView(), getMapClickHandler(), useAsciiMapViewerBindings(), createViewportKeyHandler(), VIEWPORT_BUTTON_CLASS, AsciiMapViewerContent() (+3 more)

### Community 921 - "event_handler.py"
Cohesion: 0.01
Nodes (142): PlayerDPDecayEvent, PlayerRespawnedEvent, Event fired when a mortally wounded player loses DP due to decay. This event is…, Event fired when a player respawns after death. This event is triggered when a…, UUID, Real-time event handler for MythosMUD. This module provides the…, Initialize specialized handler modules., Get the next sequence number for events. (+134 more)

### Community 922 - "Party"
Cohesion: 0.20
Nodes (8): Party, In-memory party model. Ephemeral: not persisted. party_id and member_ids are…, Return the party by id, or None., Ensure leader is in member set., Party __post_init__ ensures leader is in member_ids., Party __post_init__ keeps existing members and adds leader., test_party_post_init_includes_leader_in_members(), test_party_post_init_preserves_other_members()

### Community 923 - "test_get_npc_system_statistics_return_shape"
Cohesion: 0.29
Nodes (11): async_sessionmaker, asyncio, AsyncSession, Verify get_rooms_with_exits() (room cache data source) includes arena zone…, Call get_player_by_id() with non-existent UUID; verify return shape when empty., Call get_npc_system_statistics() and verify result columns., Call get_rooms_with_exits() and verify result columns match procedure…, test_get_npc_system_statistics_return_shape() (+3 more)

### Community 924 - "test_profession_service.py"
Cohesion: 0.25
Nodes (13): persistence(), _profession(), asyncio, fixture, Unit tests for ProfessionService., service(), test_get_all_professions_dict(), test_get_profession_by_id_dict_found() (+5 more)

### Community 925 - "CacheService"
Cohesion: 0.21
Nodes (5): CacheService, Main cache service that coordinates all caching operations. This service…, Initialize the cache service. Args: persistence: Persistence layer instance…, Preload frequently accessed data into caches. This method loads commonly used…, TestCacheService

### Community 926 - "test_persistence_container_persistence.py"
Cohesion: 0.14
Nodes (13): Unit tests for persistence.container_persistence module. This module tests the…, Test parsing None JSONB column., Test parsing string JSONB column., Test parsing dict JSONB column., Test parsing empty string JSONB column., Test parsing list JSONB column., Test parsing invalid JSON string., test_parse_jsonb_column_dict() (+5 more)

### Community 927 - "ItemCatalogService"
Cohesion: 0.19
Nodes (10): Wire player/room/user, container, skill, level, and quest services., get_item_catalog_service(), Get ItemCatalogService for /catalog and GET /api/item-catalog., ItemCatalogService, List item prototypes with role-based projection., Create service with optional repository override for tests., ItemCatalogRepository, Persistence for item catalog listing via list_item_prototypes_page(). (+2 more)

### Community 928 - "test_websocket_handler_rate_limit.py"
Cohesion: 0.18
Nodes (13): mock_connection_manager(), mock_websocket(), asyncio, fixture, Unit tests for websocket handler rate limiting. Tests the rate limiting…, Create a mock WebSocket., Create a mock connection manager., Test _check_rate_limit() returns True when no connection_id. (+5 more)

### Community 929 - "asyncio"
Cohesion: 0.13
Nodes (15): asyncio, Test broadcast_player_died broadcasts death message., Test broadcast_combat_attack sends personal message to attacker., Test broadcast_combat_attack without attacker_id., Test send_dp_decay_message handles errors gracefully., broadcast_combat_attack surfaces a partial room-broadcast failure at error…, Test broadcast_combat_attack broadcasts attack event., Test broadcast_combat_attack handles personal message errors gracefully. (+7 more)

### Community 930 - "test_command_factories.py"
Cohesion: 0.12
Nodes (15): Unit tests for command factories. Tests the CommandFactory class., Test create_pickup_command delegates to inventory factory., Test create_unmute_command delegates to moderation factory., Test create_whoami_command delegates to player_state factory., Test create_who_command delegates to player_state factory., Test create_kick_command delegates to combat factory., Test create_shutdown_command delegates to utility factory., Test create_local_command delegates to communication factory. (+7 more)

### Community 931 - "AggressiveMobNPC"
Cohesion: 0.15
Nodes (11): AggressiveMobNPC, Hunt a specific target., Handle hunting target action., Aggressive mob NPC type with hunting and territorial behaviors., Get aggressive mob-specific behavior rules., Non-digit attack_damage string in behavior_config falls back to 1., hunt_target appends each id once; repeated calls keep a single _targets entry., Warnings path: failure in _compute_player_context must not raise. (+3 more)

### Community 932 - "Improve Layout Systematically"
Cohesion: 0.15
Nodes (13): Arrange Skill, Assess Current Layout, Break Card Grid Monotony, Choose the Right Layout Tool, Create Visual Rhythm, Establish a Spacing System, Improve Layout Systematically, Manage Depth & Elevation (+5 more)

### Community 933 - "Distill Skill"
Cohesion: 0.15
Nodes (13): Distill Skill, Assess Current State, Code Simplification, Content Simplification, Document Removed Complexity, Information Architecture, Interaction Simplification, Layout Simplification (+5 more)

### Community 934 - "MotdInterstitialScreen.tsx"
Cohesion: 0.19
Nodes (6): MotdContent(), YELLOW_SIGN_ASCII, MOTD_BUTTON_STYLE, MotdInterstitialScreen(), MotdInterstitialScreenProps, MotdInterstitialScreen

### Community 935 - "connectionStore.ts"
Cohesion: 0.21
Nodes (11): ConnectionActions, ConnectionHealth, ConnectionMetadata, ConnectionSelectors, ConnectionState, ConnectionStore, createInitialState(), GameEvent (+3 more)

### Community 937 - "Mypy Remediation"
Cohesion: 0.15
Nodes (12): 🔴 Critical — import and name errors, Debugging when a fix doesn't take, Entry point, Error code table, Fix patterns by tier, Fix-verify loop, 🟡 High — type errors, 🔵 Low — type precision (+4 more)

### Community 938 - "Claims by cluster"
Cohesion: 0.15
Nodes (12): Claims by cluster, config-api — API_OPENAPI_SPECIFICATION, container-di — BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES, container-di — CONTAINER_SYSTEM_ARCHITECTURE, Corpus correction, Design↔design contradictions (findings without needing code), domain — aggro-threat-system, events-nats — EVENT_OWNERSHIP_MATRIX, DISTRIBUTED_EVENTBUS_NATS, NATS_SUBJECT_PATTERNS (+4 more)

### Community 939 - "P4 · Intent Sweep — FRD/SPEC Documents"
Cohesion: 0.15
Nodes (12): Correction to the core-issues sweep — verified directly, Corroborations from a second source, Deliberately superseded — and one of them is more interesting than a blanket ruling, HIGH · Phantom hostiles spawn but cannot be fought, HIGH · Reversed compass directions — never implemented, with a trap, MEDIUM · Admin teleport audit trail uses the wrong mechanism, MEDIUM · Room `environment` enum has drifted in production data, New undocumented items (+4 more)

### Community 940 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11)"
Cohesion: 0.15
Nodes (12): Communities (4 total, 2 thin omitted), Community 0 - "Kingsport Setting", Community 1 - "Solo Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone against the Tide  (2026-08-11), Hyperedges (group relationships) (+4 more)

### Community 941 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (3 total, 1 thin omitted), Community 0 - "Scenario Design", Community 1 - "Call of Cthulhu Roleplaying Game; Keeper Tips: C", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Keeper Tips  (2026-08-12), Hyperedges (group relationships) (+4 more)

### Community 942 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12)"
Cohesion: 0.15
Nodes (12): Communities (17 total, 16 thin omitted), Community 0 - "Scenario Handouts", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Doors to Darkness  (2026-08-12), Hyperedges (group relationships), Import Cycles (+4 more)

### Community 943 - "exploration.sql"
Cohesion: 0.17
Nodes (7): schema_name.count_coordinated_rooms(), schema_name.get_room_id_by_stable_id(), schema_name.is_room_explored(), rooms, subzones, zones, player_exploration

### Community 944 - "npcs.sql"
Cohesion: 0.15
Nodes (3): schema_name.get_npc_system_statistics(), npc_definitions, npc_spawn_rules

### Community 945 - "required"
Cohesion: 0.17
Nodes (12): $defs, scheduleEntry, applies_to, category, days, end_hour, id, name (+4 more)

### Community 946 - "Technical Implementation"
Cohesion: 0.15
Nodes (13): 1. Component Refactoring, 2. Message Routing Logic, 3. State Management, 4. Event Handling, ChatPanel.tsx Enhancements (New Chat Input Panel), Command Routing Logic, CommandPanel.tsx Simplifications, Current Logic (in CommandPanel) (+5 more)

### Community 947 - "Critical Issues"
Cohesion: 0.15
Nodes (13): 1. Entry Point Anti-Pattern: `asyncio.run()` Usage, 3.1 `asyncio.create_task()` Usage, 3.2 `asyncio.gather()` Usage, 3. Task Management Anti-Patterns, 4. Missing Explicit Dependency, 5.1 Uvicorn Integration, 5.2 Test Files, 5.3 Event Bus Queue Migration (+5 more)

### Community 948 - "Easy Coverage Wins - Quick Analysis"
Cohesion: 0.15
Nodes (13): Easy Coverage Wins - Quick Analysis, 🚀 Next Steps, Phase 1: Quick Wins (Tier 1 + Tier 2) ✅ COMPLETED, Phase 2: Medium Effort (Tier 3) ✅ COMPLETED, Phase 3: New Small Files (Tier 4) ✅ COMPLETED, Phase 4: Additional Realtime Files 🔄 IN PROGRESS, 📊 Recommended Priority Order, 🎉 Summary (+5 more)

### Community 949 - "Entries"
Cohesion: 0.15
Nodes (11): Codacy High/Critical Baseline – MythosMUD, Distribution notes, Example issue types, Summary (from Codacy UI snapshot), Top code patterns by issue count, 2026-02-24 — Wave 3 (Backend security) completed, 2026-02-24 — Wave 4 (Frontend security) verified, 2026-02-24 — Wave 5 (Complexity refactors) (+3 more)

### Community 950 - "Unique Pylint Findings Analysis"
Cohesion: 0.15
Nodes (13): Linting Complexity Alignment, 2.1 No Name in Module (E0611), 2. ERROR Findings (33 findings), 4.1 Unused Variable (W0612), 4.2 Unused Argument (W0613), 4. WARNINGS Findings (5 findings), Configure Ruff to Catch (Small subset), Executive Summary (+5 more)

### Community 951 - "Migration Guide: From Default Logging to Enhanced Logging"
Cohesion: 0.17
Nodes (12): 1. Update Import Statements, 2. Migrate Context Parameters, 3. Convert String Formatting to Structured Logging, 4. Add Rich Context to Error Messages, Issue 1: ImportError when using enhanced logging, Issue 2: TypeError with context parameter, Issue 3: Logs not appearing in files, Issue 4: Sensitive data appearing in logs (+4 more)

### Community 952 - "Execution Timeline"
Cohesion: 0.15
Nodes (13): Execution Timeline, Month 1: Pruning Phase, Month 2: Consolidation + Gap Filling, Month 3+: Continuous Improvement, Ongoing Tasks, Week 1: Quick Wins, Week 2: Infrastructure Reduction, Week 3: Coverage Test Optimization (+5 more)

### Community 953 - "._is_valid_name_for_occupant"
Cohesion: 0.24
Nodes (7): Any, Process a dictionary occupant and add to appropriate lists if valid. Args: occ:…, Separate occupants into players, NPCs, and all occupants lists. Args:…, Check if a name is valid for use as an occupant name. Args: name: The name to…, Add a valid name to both target list and all occupants list. Args: name: The…, Process a player name and add to appropriate lists if valid. Args: player_name:…, Process an NPC name and add to appropriate lists if valid. Args: npc_name: The…

### Community 954 - "analyze_idle_memory_samples.py"
Cohesion: 0.27
Nodes (12): analyze(), _append_qualname_deltas(), _append_slope_rows(), JsonSample, main(), Path, _qualname_counts(), Analyze idle memory JSONL samples (warmup + measurement windows). (+4 more)

### Community 955 - "main"
Cohesion: 0.22
Nodes (12): analyze_connectivity(), generate_dot_file(), load_room_data(), main(), print_detailed_statistics(), print_room_listing(), Print a detailed listing of all rooms by subzone., Load all room and intersection data from the zone directory. (+4 more)

### Community 956 - "fix_markdown_code_block_style.py"
Cohesion: 0.24
Nodes (12): detect_code_language(), fix_code_block_style(), fix_markdown_file(), is_indented_code_line(), main(), parse_markdownlint_output(), Path, Parse markdownlint output to get files with MD046 issues. (+4 more)

### Community 957 - "main"
Cohesion: 0.22
Nodes (12): fix_md001_heading_increment(), fix_md013_line_length(), fix_md041_first_line_heading(), fix_md051_link_fragments(), main(), parse_errors(), Fix MD001: Heading levels should only increment by one level at a time., Parse markdownlint output file and extract errors. (+4 more)

### Community 958 - "SyntaxErrorFixer"
Cohesion: 0.22
Nodes (8): main(), Path, Process multiple files and return statistics., Main function to run the syntax error fixer., Tool to fix syntax errors introduced by automated f-string remediation., Fix malformed logger calls with broken syntax., Fix syntax errors in a specific file., SyntaxErrorFixer

### Community 959 - "fixture"
Cohesion: 0.15
Nodes (13): catalog_with_own_language_and_mythos(), mock_persistence(), mock_player_skill_repo(), mock_skill_repo(), mock_skill_use_log_repo(), fixture, Mock PlayerSkillRepository., Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id). (+5 more)

### Community 960 - "lint_imports.py"
Cohesion: 0.27
Nodes (12): broken_contract_count(), broken_contract_names(), _contracts_summary_message(), lint_imports_failed(), main(), _print_failure(), _print_success(), Return contract names marked BROKEN in import-linter output. (+4 more)

### Community 961 - ".create_drop_command"
Cohesion: 0.15
Nodes (12): Test create_drop_command() with quantity., Test create_drop_command() raises error for invalid index., test_create_drop_command_invalid_index(), test_create_drop_command_with_quantity(), Test create_drop_command() raises error when index is not integer., Test create_drop_command() raises error when quantity is not integer., Test create_drop_command() creates DropCommand., Test create_drop_command() raises error with no args. (+4 more)

### Community 962 - "catalogMetadata"
Cohesion: 0.17
Nodes (12): additionalProperties, required, type, definitions, catalogMetadata, npcArmor, npcAttack, namespace (+4 more)

### Community 963 - "parse_shutdown_parameters"
Cohesion: 0.14
Nodes (14): parse_shutdown_parameters(), Parse shutdown command parameters. Args: command_data: Command data dictionary…, Test parse_shutdown_parameters() with no args defaults to 10 seconds., Test parse_shutdown_parameters() with cancel action., Test parse_shutdown_parameters() with seconds., Test parse_shutdown_parameters() with negative seconds., Test parse_shutdown_parameters() with zero seconds., Test parse_shutdown_parameters() with invalid string. (+6 more)

### Community 964 - ".load"
Cohesion: 0.18
Nodes (5): AsyncSession, BaseException, BoundLogger, Room, Load rooms from PostgreSQL and update the room cache.

### Community 965 - "_utc_now"
Cohesion: 0.21
Nodes (12): datetime, Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE…, _utc_now(), Unit tests for lucidity model utility functions. Tests the _utc_now utility…, Test _utc_now returns a datetime object., Test _utc_now returns naive datetime (tzinfo=None)., Test _utc_now returns time close to current UTC time., Test _utc_now returns different times on subsequent calls. (+4 more)

### Community 966 - "api/conftest.py"
Cohesion: 0.17
Nodes (15): mock_connection_manager(), mock_container(), mock_container_service(), mock_persistence(), mock_player(), mock_request(), mock_user(), fixture (+7 more)

### Community 967 - "fetch_container_items"
Cohesion: 0.40
Nodes (6): fetch_container_items(), _item_dict_from_contents_row(), _metadata_dict_from_cell(), PsycopgConnection, UUID, Fetch container items directly from normalized tables. Queries…

### Community 968 - "_weapon_from_prototype_registry"
Cohesion: 0.17
Nodes (12): Resolve metadata.weapon from prototype registry for a given prototype_id.…, _weapon_from_prototype_registry(), Weapon statistics for items that can be used as weapons. This model represents…, WeaponStats, When registry is None, returns None., When prototype_id is empty, returns None., When prototype has no metadata.weapon, returns None., When prototype has metadata.weapon, returns weapon dict. (+4 more)

### Community 969 - "._is_uuid_string"
Cohesion: 0.17
Nodes (10): Process a string occupant (legacy format) and add to list if valid. Args: occ:…, Check if a string looks like a UUID. Args: value: The string to check Returns:…, Test OccupantFormatter._is_uuid_string() returns True for valid UUID., Test OccupantFormatter._is_uuid_string() returns False for invalid length., Test OccupantFormatter._is_uuid_string() returns False for wrong dash count., Test OccupantFormatter._is_uuid_string() returns False for invalid characters., test_occupant_formatter_is_uuid_string_invalid_chars(), test_occupant_formatter_is_uuid_string_invalid_dashes() (+2 more)

### Community 970 - "test_skill_service.py"
Cohesion: 0.17
Nodes (11): Unit tests for SkillService (get_skills_catalog, set_player_skills,…, run_improvement_rolls with new_level 1 does nothing (previous level 0)., run_improvement_rolls when no skills used at previous level does not update., When current >= 90, successful improvement adds 1 (cap 99)., When roll <= current value, no update_value call., When roll <= skill value, record_use is called and returns True., test_roll_skill_check_success_records_use_and_returns_true(), test_run_improvement_rolls_high_skill_gains_one() (+3 more)

### Community 971 - "_occupation_slots_9"
Cohesion: 0.17
Nodes (12): _occupation_slots_9(), Valid 9 slots: one 70, two 60, three 50, three 40; 9 distinct skill_ids (no…, Personal interest with Cthulhu Mythos raises ValueError., personal_interest must have exactly 4 entries., occupation_slots with duplicate skill_id raises ValueError., personal_interest with duplicate skill_id raises ValueError., Occupation and personal interest sharing a skill_id raises ValueError., test_set_player_skills_cthulhu_mythos_in_personal_rejected() (+4 more)

### Community 972 - "required"
Cohesion: 0.22
Nodes (9): required, bonus_tags, day, duration_hours, id, month, name, season (+1 more)

### Community 973 - "_personal_interest_4"
Cohesion: 0.17
Nodes (12): _personal_interest_4(), Four personal interest (skill_ids only); distinct and no overlap with…, set_player_skills with valid occupation and personal calls delete then…, When Own Language is not in occupation or personal, its value is stats_for_edu., Occupation slot with Cthulhu Mythos (allow_at_creation=False) raises ValueError., occupation_slots not length 9 raises ValueError., occupation_slots with wrong value set (e.g. two 70s) raises ValueError., test_set_player_skills_cthulhu_mythos_in_occupation_rejected() (+4 more)

### Community 974 - "test_room_environment_parity.py"
Cohesion: 0.19
Nodes (12): _environment_enum_from_schema(), _environment_options_from_room_edit_modal(), Path, Parity test for the room environment enum (#623). Guards against the exact…, Return the `environment` property's `enum` values from a room JSON schema., Return the non-empty `value`s of RoomEditModal.tsx's ENVIRONMENT_OPTIONS…, room_hierarchy_schema.json's environment enum must equal ROOM_ENVIRONMENTS., unified_room_schema.json's environment enum must equal ROOM_ENVIRONMENTS. (+4 more)

### Community 975 - "Commands"
Cohesion: 0.17
Nodes (12): Add a branch — `gh stack add`, Check out a stack — `gh stack checkout`, Commands, Initialize a stack — `gh stack init`, Link branches as a stack (no local tracking) — `gh stack link`, Navigate the stack, Push branches to remote — `gh stack push`, Rebase the stack — `gh stack rebase` (+4 more)

### Community 976 - "Dependency Upgrade"
Cohesion: 0.18
Nodes (7): Codacy MCP Rules, Before starting, Dependency Upgrade, Never, Rollback, Upgrade procedure, Verify

### Community 977 - "required"
Cohesion: 0.22
Nodes (9): required, applies_to, category, days, end_hour, id, name, start_hour (+1 more)

### Community 978 - "mapPageRenderer.tsx"
Cohesion: 0.13
Nodes (21): RoomMapViewerProps, MapPage(), AuthenticatedMapProps, MapViewResolvedProps, renderAuthenticatedMapView(), renderMapPageState(), renderStatusGate(), resolveMapViewProps() (+13 more)

### Community 979 - "Amplify the Design"
Cohesion: 0.17
Nodes (12): Bolder Skill, Amplify the Design, Assess Current State, Color Intensification, Composition Boldness, MANDATORY PREPARATION, Motion & Animation, Plan Amplification (+4 more)

### Community 980 - "Interaction Design"
Cohesion: 0.17
Nodes (12): Destructive Actions: Undo > Confirm, Focus Rings: Do Them Right, Form Design: The Non-Obvious, Gesture Discoverability, Interaction Design, Keyboard Navigation Patterns, Loading States, Modals: The Inert Approach (+4 more)

### Community 981 - "Hardening Dimensions"
Cohesion: 0.17
Nodes (12): Harden Skill, Accessibility Resilience, Assess Hardening Needs, Edge Cases & Boundary Conditions, Error Handling, Hardening Dimensions, Input Validation & Sanitization, Internationalization (i18n) (+4 more)

### Community 982 - "MythosMUD LLM Wiki (Obsidian)"
Cohesion: 0.17
Nodes (12): LLM Wiki Skill, Chaosium ingest, Division of labor, Graphify sync, Ingest, Lint, MythosMUD LLM Wiki (Obsidian), Non-goals (+4 more)

### Community 983 - "generate_room_id"
Cohesion: 0.21
Nodes (8): Test generate_room_id() function., Test generate_room_id() with basic components., Test generate_room_id() handles components with underscores., Test generate_room_id() with empty components., Test generate_room_id() preserves special characters in components., TestGenerateRoomId, generate_room_id(), Generate hierarchical room ID from components. Args: plane: Plane identifier…

### Community 984 - "MapPerformanceMonitor"
Cohesion: 0.23
Nodes (3): debounce(), MapPerformanceMonitor, throttle()

### Community 985 - "PanelContextRuntime.tsx"
Cohesion: 0.21
Nodes (9): defaultPanels, PanelContext, PanelContextType, PanelLayout, PanelPosition, PanelProvider(), PanelProviderProps, PanelSize (+1 more)

### Community 986 - "properties"
Cohesion: 0.18
Nodes (11): minimum, type, maxLength, minLength, type, maxLength, type, properties (+3 more)

### Community 987 - "Lint Remediation"
Cohesion: 0.17
Nodes (11): 🔴 Critical — compilation errors, Debugging when a fix doesn't take, Entry point, Error code table, Fix patterns by tier, Fix-verify loop, 🟡 High — code quality, Lint Remediation (+3 more)

### Community 988 - "mcp.json"
Cohesion: 0.16
Nodes (13): codacy, context7, graphify, jcodemunch, playwright, JCODEMUNCH_MAX_FOLDER_FILES, graphify-mcp, npx (+5 more)

### Community 989 - "TRACK C · The interactive review — 8 decisions"
Cohesion: 0.17
Nodes (12): C1 · What are the ADRs *for*?, C2 · Who owns query construction?, C3 · Layer boundaries: enforce or amend?, C4 · Is `APPLICATION_CONTAINER_ANALYSIS.md` restored or left archived?, C5 · Four doc↔doc contradictions, C6 · Contract drift from one unrecorded decision, C7 · Closed-but-not-built — six features, C8 · Undocumented systems worth an ADR (+4 more)

### Community 990 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11)"
Cohesion: 0.17
Nodes (11): Communities (2 total, 1 thin omitted), Community 0 - "Expedition Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Alone Against the Frost  (2026-08-11), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 991 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (3 total, 2 thin omitted), Community 0 - "Player Investigators", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 992 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12)"
Cohesion: 0.17
Nodes (11): Communities (8 total, 7 thin omitted), Community 0 - "Character Sheets", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Cthulhu Dark Ages - 3rd Edition  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps (+3 more)

### Community 993 - "bonus_tags"
Cohesion: 0.33
Nodes (6): items, type, uniqueItems, minLength, type, bonus_tags

### Community 994 - "ADR-023: Package Ownership (`game/` vs `services/` vs `npc/`) and Fan-Out Watch List"
Cohesion: 0.17
Nodes (11): 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Methodology, 7. Related ADRs, 8. Related docs (+3 more)

### Community 995 - "Complexity Checking Alignment: Ruff C901 vs Pylint"
Cohesion: 0.17
Nodes (12): 1. Use Ruff for Cyclomatic Complexity ✅, 2. Suppress Pylint Complexity Metrics ✅, 3. Align Inline Suppressions, Complexity Checking Alignment: Ruff C901 vs Pylint, Conclusion, Current State Analysis, Example Comparison, Executive Summary (+4 more)

### Community 996 - "What They Measure"
Cohesion: 0.17
Nodes (12): Configuration, Example, Pylint Complexity Metrics (R0911-R0915), R0911: Too Many Return Statements, R0912: Too Many Branches, R0913: Too Many Arguments, R0914: Too Many Local Variables, R0915: Too Many Statements (+4 more)

### Community 997 - "PERSISTENCE_REFACTORING_COMPLETE.md"
Cohesion: 0.18
Nodes (9): Persistence Async Migration Plan, Gradual File-by-File Async Migration, HealthRepository, Implementation Pattern, PersistenceLayer Sync Facade, PlayerRepository, Sync-to-Async Delegation, Seven Async Repositories (+1 more)

### Community 998 - "Migration Roadmap"
Cohesion: 0.17
Nodes (12): Files to Migrate (11 total), Files to Migrate (2 total), Files to Migrate (6 total), Game Systems (3 files), Migration Roadmap, NPC Systems (7 files), Phase 2: API Endpoints (Priority 1) 🎯, Phase 3: Real-Time Handlers (Priority 2) 🚀 (+4 more)

### Community 999 - "Critical Insights"
Cohesion: 0.17
Nodes (12): 1. Infrastructure Tests are the Main Optimization Target, 2. Regression Tests are 100% High-Value, 3. Coverage Tests Written for Metrics, Not Quality, 4. No Parametrized Tests (Major Opportunity), 5. Critical Gaps in New Architecture, Critical Insights, Example, Example Low-Value Test (+4 more)

### Community 1000 - "Multi-Character Support System"
Cohesion: 0.20
Nodes (12): Scenario 27 Character Selection, Scenario 28 Multi-Character Creation, Scenario 29 Character Soft Deletion, Scenario 30 Case-Insensitive Name Uniqueness, Scenario 31 Administrative Set Stat, Scenario 38 Revised Character Creation, Stats-Profession-Skills-Name Creation Flow, Scenario 39 Skills New Tab (+4 more)

### Community 1001 - "enum"
Cohesion: 0.25
Nodes (8): Friday, Monday, Saturday, Sunday, Thursday, Tuesday, Wednesday, enum

### Community 1002 - "grype.py"
Cohesion: 0.26
Nodes (11): _grype_command(), _handle_grype_result(), main(), merge_windows_machine_user_path_into_environ(), CompletedProcess, Path, Append Machine and User Path from the registry (matches hadolint.ps1 behavior).…, Return the MythosMUD project root (parent of scripts/). (+3 more)

### Community 1003 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Print statistics about the room data., Main function to generate the visualization., Load all room and intersection data from the zone directory. (+3 more)

### Community 1004 - "main"
Cohesion: 0.24
Nodes (11): create_graph(), load_room_data(), main(), print_statistics(), Graph, Create a visual representation of the graph., Print statistics about the room data., Main function to generate the visualization. (+3 more)

### Community 1005 - "PlayerRespawnWrapper"
Cohesion: 0.05
Nodes (42): PlayerCreationService, Any, Stats, UUID, Create a new player character with specific stats. Args: name: The player's…, Service for player creation operations., Initialize with persistence layer, schema converter, and optional instance…, Resolve starting room and tutorial instance ID. For tutorial players, returns… (+34 more)

### Community 1006 - "mythos_e2e.rooms"
Cohesion: 0.16
Nodes (14): mythos_e2e.count_coordinated_rooms(), mythos_e2e.create_room_link(), mythos_e2e.delete_room_link(), mythos_e2e.get_room_id_by_stable_id(), mythos_e2e.is_room_explored(), mythos_e2e.player_exploration, mythos_e2e.room_links, mythos_e2e.rooms (+6 more)

### Community 1007 - "SkillUseLog"
Cohesion: 0.21
Nodes (10): Base, One recorded successful use of a skill by a character at a given level.…, SkillUseLog, Unit tests for SkillUseLog ORM model., SkillUseLog can be instantiated with required fields., SkillUseLog maps to the expected table., SkillUseLog __repr__ includes key identifiers., test_skill_use_log_creation() (+2 more)

### Community 1008 - "fixture"
Cohesion: 0.22
Nodes (9): mock_prototype_registry(), fixture, Create a mock prototype registry., Create a sample room drop item., Create a sample inventory item., Create a sample equipped item., sample_equipped_item(), sample_inventory_item() (+1 more)

### Community 1009 - "subzone_with_override"
Cohesion: 0.29
Nodes (11): async_sessionmaker, asyncio, AsyncSession, fixture, Integration test for db/procedures/lucidity.sql's get_lucidity_rate_overrides()…, A zone with special_rules set, and a subzone under it with special_rules NULL…, A zone with NO override, and a subzone under it WITH special_rules set. Yields…, subzone_with_override() (+3 more)

### Community 1010 - "test_monitoring_init.py"
Cohesion: 0.17
Nodes (11): Unit tests for server.monitoring lazy __getattr__ re-exports., Exception tracker symbols import without triggering numpy lazy paths., __getattr__ resolves MonitoringDashboard and get_monitoring_dashboard., __getattr__ resolves PerformanceStats and get_performance_monitor., Unknown attribute names raise AttributeError., Direct __getattr__ covers both branch returns for dashboard imports., test_monitoring_eager_imports(), test_monitoring_getattr_direct_call() (+3 more)

### Community 1011 - "mythos_unit.rooms"
Cohesion: 0.16
Nodes (14): mythos_unit.count_coordinated_rooms(), mythos_unit.create_room_link(), mythos_unit.delete_room_link(), mythos_unit.get_room_id_by_stable_id(), mythos_unit.is_room_explored(), mythos_unit.player_exploration, mythos_unit.room_links, mythos_unit.rooms (+6 more)

### Community 1012 - "field_validator"
Cohesion: 0.18
Nodes (6): field_validator, Validate and normalize effect components. Args: value: The list of effect…, Validate and normalize tags. Args: value: The list of tags to validate Returns:…, Validate that item_type is in the allowed list. Args: value: The item type to…, Validate that all flags are in the allowed list. Args: value: The list of flags…, Validate that all wear slots are in the allowed list. Args: value: The list of…

### Community 1013 - "skill"
Cohesion: 0.14
Nodes (14): bonus, skill, type, equipmentBonus, additionalProperties, properties, required, type (+6 more)

### Community 1014 - "load_motd"
Cohesion: 0.20
Nodes (12): Unit tests for motd_loader utilities. Tests the MOTD loading functions., Test load_motd() loads MOTD from file., Test load_motd() returns default when file doesn't exist., Test load_motd() handles file read errors., Test load_motd() handles empty file., test_load_motd_empty_file(), test_load_motd_file_exists(), test_load_motd_file_not_exists() (+4 more)

### Community 1015 - "main"
Cohesion: 0.27
Nodes (10): _exit_empty(), _load_state(), main(), NoReturn, Path, Exit successfully with no decision (allow the stop)., Load and validate edited-files state. Returns None if missing or invalid., Write state via a same-directory temp file + os.replace. See… (+2 more)

### Community 1016 - "Codacy Rules"
Cohesion: 0.18
Nodes (10): After every response, Codacy Rules, CRITICAL: After ANY successful file edit, CRITICAL: Dependencies and Security Checks, General, Trying to call a tool that needs a `rootPath` parameter, Using any tool that accepts `provider`, `organization`, or `repository`, When `codacy_cli_analyze` fails because the Codacy CLI is not installed (+2 more)

### Community 1017 - "Quieter Skill"
Cohesion: 0.18
Nodes (11): Quieter Skill, Assess Current State, Color Refinement, Composition Refinement, MANDATORY PREPARATION, Motion Reduction, Plan Refinement, Refine the Design (+3 more)

### Community 1018 - "Typeset Skill"
Cohesion: 0.18
Nodes (11): Typeset Skill, Assess Current Typography, Establish Hierarchy, Fix Readability, Font Selection, Improve Typography Systematically, MANDATORY PREPARATION, Plan Typography Improvements (+3 more)

### Community 1019 - "PlayerServiceHealPort"
Cohesion: 0.20
Nodes (7): PlayerServiceHealPort, UUID, Apply healing to a player by id., Apply typed damage to a player; returns damage result payload., Load player by id; None if missing., Return registry string id for npc_uuid, or None if unmapped., Player service methods used by heal and steal-life spell paths.

### Community 1020 - "vite.userConfig.ts"
Cohesion: 0.25
Nodes (5): TODO: Implement AST-based console removal plugin to selectively remove, configureForwardAuthorization(), createViteUserConfig(), TODO: Implement AST-based console removal to preserve console.error/warn, vitestTestOptions

### Community 1021 - "Client Test Remediation"
Cohesion: 0.18
Nodes (10): Client Test Remediation, 🔴 Critical — TypeScript/rendering errors, Debugging when a fix doesn't take, Entry point, Fix patterns by tier, Fix-verify loop, 🟡 High — component issues, 🟢 Medium — hook/async issues (+2 more)

### Community 1022 - "main"
Cohesion: 0.27
Nodes (10): _exit_empty(), _load_state(), main(), NoReturn, Path, Print empty JSON and exit successfully (no followup)., Load and validate edited-files state. Returns None if missing or invalid., Write state via a same-directory temp file + os.replace. See… (+2 more)

### Community 1023 - "Arkham City (MOTD Zone)"
Cohesion: 0.24
Nodes (11): Arkham City Graph PNG, Arkham City PDF Map, Arkham City (MOTD Zone), Welcome to the Dreamlands, Innsmouth (MOTD Zone), Katmandu, MythosMUD Message of the Day, The Yellow Sign (+3 more)

### Community 1024 - "Claims by cluster"
Cohesion: 0.18
Nodes (11): Claims by cluster, client — ADR-008, ADR-011, ADR-017, config-api — ADR-013, container-di / layering — ADR-001, ADR-002, ADR-007, domain — ADR-009, ADR-010, ADR-016, events-nats — ADR-003, ADR-014, P2 · ADR Claim Register, persistence-db — ADR-005, ADR-006, ADR-015 (+3 more)

### Community 1025 - "P3 · container-di + client + domain"
Cohesion: 0.18
Nodes (10): Further P0 reversals, H10 · ADR-011 declares completed work as "planned", H7 · The global-singleton leak grew rather than shrank, H8 · Twelve modules bypass the persistence facade — and the two docs disagree about whether that's allowed, H9 · ADR-008 styling claim is wholly counterfactual, Low / STALE, Medium, Notable CONFORMS (+2 more)

### Community 1026 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (1 total, 0 thin omitted), Community 0 - "Mythos Subjects", Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu_ The Coloring Book  (2026-08-12), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1027 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Communities (2 total, 2 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Dead Light and Other Dark Turns  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1028 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12)"
Cohesion: 0.18
Nodes (10): Ambiguous Edges - Review These, Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\The Grand Grimoire of Cthulhu Mythos Magic  (2026-08-12), Hyperedges (group relationships), Knowledge Gaps, Suggested Questions (+2 more)

### Community 1029 - "AnyIO Code Review - Anti-Patterns and Issues"
Cohesion: 0.18
Nodes (9): AnyIO Code Review - Anti-Patterns and Issues, Executive Summary, High Priority (Entry Points), Low Priority (Complex Refactoring), Medium Priority (Core Primitives), Migration Priority, Notes, Recommendations (+1 more)

### Community 1030 - "✅ Best Practices Compliance"
Cohesion: 0.18
Nodes (11): 10. Exception Handling in Async Operations (asyncio.mdc Section 2.5), 1. Blocking the Event Loop (asyncio.mdc Section 2.3), 2. Async/Await Usage (anyio.mdc Section 2.2), 3. Method Signature Consistency (asyncio.mdc Section 2.1), 4. Error Handling (asyncio.mdc Section 2.5), 5. Resource Management (anyio.mdc Section 2.1), 6. Task Groups / Structured Concurrency (anyio.mdc Section 2.1), 7. Avoiding asyncio.run() in Library Code (asyncio.mdc Section 6.1) (+3 more)

### Community 1031 - "🔍 Specific File Reviews"
Cohesion: 0.18
Nodes (11): ✅ container_service.py, ✅ corpse_lifecycle_service.py, ✅ database.py, ✅ exploration_service.py, ✅ npc_combat_integration_service.py, ✅ passive_lucidity_flux_service.py, ✅ persistence.py, ✅ player_death_service.py (+3 more)

### Community 1032 - "CircuitBreaker Implementation Planning Document"
Cohesion: 0.18
Nodes (10): CircuitBreaker Implementation Planning Document, Configuration Schema, Dependencies, Gradual Rollback, Immediate Rollback, Objectives, Overview, Rollback Plan (+2 more)

### Community 1033 - "Ruff to Pylint Rule Mapping"
Cohesion: 0.18
Nodes (11): B008 - Function calls in argument defaults, C901 - Too complex (PRIMARY COMPLEXITY CHECKER), Category Mappings, Complexity Checking, E501 - Line too long, Global Ignores (pyproject.toml), Next Steps, Purpose (+3 more)

### Community 1034 - "Test Timing Analysis - Optimization Targets"
Cohesion: 0.18
Nodes (11): Test Timing Analysis, 1. **Mark Additional Slow Tests**, 2. **Investigate Heavy Setup Tests**, 3. **Verify Marker Application**, 4. **Target Time Budget (5-7 min = 300-420 seconds)**, Critical Finding: Tests Still Running Despite Markers, Next Actions, pytest-xdist Parallel Fast Suite (+3 more)

### Community 1035 - "App Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1036 - "Auth Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1037 - "Middleware Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1038 - "apply_stat_modifications"
Cohesion: 0.29
Nodes (9): apply_stat_modifications(), Stat modification helpers for spell effects. This module contains utility…, Apply stat modification dict to stats. Returns (updated stats, stat_changes,…, Unit tests for spell_effects_stats helpers., test_apply_stat_modifications_bad_string_skipped(), test_apply_stat_modifications_basic(), test_apply_stat_modifications_clamps_to_bounds(), test_apply_stat_modifications_skips_invalid_stat() (+1 more)

### Community 1039 - "Schemas Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1040 - "Services Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1041 - "Movement Subsystem Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Architecture, 3. Key design decisions, 4. Constraints, 5. Component interactions, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1042 - "analyze_file"
Cohesion: 0.22
Nodes (10): analyze_file(), check_comment_references_nonexistent_code(), extract_function_and_class_names(), main(), Any, Path, Analyze a single file for comment issues. Args: file_path: Path to file to…, Main entry point for comment analysis. (+2 more)

### Community 1043 - "main"
Cohesion: 0.25
Nodes (10): apply_migration_013(), apply_migration_014(), check_migration_013(), check_migration_014(), main(), Main function to check and apply migrations., Check if migration 013 (map_x/map_y columns) has been applied., Check if migration 014 (player_exploration table) has been applied. (+2 more)

### Community 1044 - "main"
Cohesion: 0.29
Nodes (10): check_thresholds(), _ensure_coverage_xml_or_exit(), main(), parse_coverage_xml(), _print_results_and_exit(), Path, Check files against their thresholds. Returns hard-fail messages., Exit if coverage.xml not found. In pre-commit context, exit 0 so commits aren't… (+2 more)

### Community 1045 - "main"
Cohesion: 0.25
Nodes (10): generate_simple_dot_file(), generate_simple_html_visualization(), load_room_data(), main(), print_simple_statistics(), Load all room and intersection data from the zone directory., Print simplified statistics about the room data., Main function to generate the simplified visualization. (+2 more)

### Community 1046 - "damage_expr_to_min_max"
Cohesion: 0.10
Nodes (27): _RollInt, damage_expr_to_min_max(), _parse_terms(), Random, Shared damage_expr helpers for catalog dual-write and combat rolls. Used by…, Inclusive lo..hi using secrets (avoids Bandit/Codacy B311 on random)., Roll a dice expression once and return a non-negative integer. Args: expr: Dice…, Drop trailing +DB / -flavor suffixes until none remain. (+19 more)

### Community 1047 - "Cult Chat Seam Design"
Cohesion: 0.25
Nodes (8): 1. Overview, 2. Architecture, 3. Key design decisions, 4. Constraints, 5. Related docs, 6. Changelog, AI READING INSTRUCTION, Cult Chat Seam Design

### Community 1048 - "test_lucidity_round_trip.py"
Cohesion: 0.24
Nodes (10): cleanup_test_user(), async_sessionmaker, asyncio, AsyncSession, fixture, UUID, Integration test for lucidity service round-trip. Tests that LucidityService…, Yield a fresh user id and guarantee its row is deleted after the test, pass or… (+2 more)

### Community 1049 - "test_spell_effects_support.py"
Cohesion: 0.39
Nodes (11): asyncio, Unit tests for server.game.magic.spell_effects_support., _spell(), _target(), test_build_stat_modifications_missing(), test_build_stat_modifications_shorthand(), test_create_object_for_room_placeholder(), test_process_create_object_for_player() (+3 more)

### Community 1050 - "lock_state"
Cohesion: 0.25
Nodes (8): locked, sealed, unlocked, default, description, enum, type, lock_state

### Community 1051 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1052 - "npc_base_stats.schema.json"
Cohesion: 0.20
Nodes (9): determination_points, max_dp, xp_value, additionalProperties, description, required, $schema, title (+1 more)

### Community 1053 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 1054 - "environment"
Cohesion: 0.25
Nodes (8): default, description, enum, type, indoors, outdoors, underwater, environment

### Community 1055 - "fixture"
Cohesion: 0.18
Nodes (11): mock_persistence(), mock_room_cache(), fixture, Create a mock persistence layer., Create a mock room cache service., Create a RoomService instance., Create a RoomService instance with cache., Create a sample room dictionary. (+3 more)

### Community 1056 - "test_async_persistence_room_cache.py"
Cohesion: 0.04
Nodes (60): asyncio, Unit tests for async persistence layer: load_room_cache_async, query_rooms,…, Test get_user_by_username_case_insensitive when no session is yielded., Test get_professions when no session is yielded., Test get_players_batch with empty list., Test get_players_batch with actual players (UUID conversion)., Test _generate_room_id_from_zone_data when stable_id already has full path., Test _generate_room_id_from_zone_data when room ID needs generation. (+52 more)

### Community 1057 - "asyncio"
Cohesion: 0.18
Nodes (11): asyncio, Test _ensure_room_cache_loaded returns early when cache is already loaded., Test _ensure_room_cache_loaded handles concurrent load scenario (double-check…, Test _ensure_room_cache_loaded handles DatabaseError gracefully., Test _ensure_room_cache_loaded handles OSError gracefully., Test _ensure_room_cache_loaded handles RuntimeError gracefully., test_ensure_room_cache_loaded_already_loaded(), test_ensure_room_cache_loaded_concurrent_load() (+3 more)

### Community 1058 - "._attack_target_impl"
Cohesion: 0.20
Nodes (5): Resolve attack damage from base_stats attacks, else behavior_config., Try to handle the attack via combat integration. Returns: True/False if…, Internal implementation for attacking a target., Attack a specific target., Handle attacking target action.

### Community 1059 - "Teach Impeccable Skill"
Cohesion: 0.24
Nodes (11): Aha Moment Onboarding, Core Web Vitals Performance, Design Context Persistence (.impeccable.md), Onboard Skill, Optimize Skill, Overdrive Skill, Overdrive Mode, Polish Skill (+3 more)

### Community 1060 - "ADR-019: Player Effects System"
Cohesion: 0.20
Nodes (9): ADR-019: Player Effects System, 1. Overview, 2. Context, 3. Decision, 4. Alternatives Considered, 5. Consequences, 6. Related ADRs, 7. Changelog (+1 more)

### Community 1061 - "_ScalarResult"
Cohesion: 0.22
Nodes (8): Minimal typed stand-in for the sqlalchemy Result returned by session.execute()…, save_player must not resurrect a soft-deleted row (#777): when…, save_player must still upsert a not-yet-inserted player, where…, Build the `session_maker` callable that `get_session_maker()` returns: calling…, _ScalarResult, _session_maker_double(), test_save_player_allows_new_player(), test_save_player_refuses_deleted_player()

### Community 1062 - "Responsive Design"
Cohesion: 0.20
Nodes (10): Breakpoints: Content-Driven, Detect Input Method, Not Just Screen Size, Layout Adaptation Patterns, Mobile-First: Write It Right, Picture Element for Art Direction, Responsive Design, Responsive Images: Get It Right, Safe Areas: Handle the Notch (+2 more)

### Community 1063 - "._get_npc_display_name"
Cohesion: 0.25
Nodes (4): Resolve NPC instance display name from lifecycle manager, or derive from npc_id., Best-effort lookup of NPC name from the lifecycle manager., Resolve the NPC lifecycle manager from the app state, if available., Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->…

### Community 1064 - "Cursor Subagents Overview"
Cohesion: 0.20
Nodes (10): Bug Investigator Subagent, Codebase Explorer Subagent, Performance Profiler Subagent, Subagent Automatic Discovery, Cursor Subagents Overview, Security Auditor Subagent, Test Suite Analyzer Subagent, Official Test Credentials (+2 more)

### Community 1065 - "REQUIRED TOOL USAGE PATTERN"
Cohesion: 0.18
Nodes (11): 10. Final Verification, 3. Systematic Investigation Approach, 5. Test Environment Setup, 6. Quality Assurance Checklist, Environment Variables, For Authentication Failures, For Database-Related Failures, For Game Logic Failures (+3 more)

### Community 1066 - "FAILURE PATTERN RECOGNITION"
Cohesion: 0.33
Nodes (6): A. Database-Related Failures, B. Authentication/Security Failures, C. WebSocket/Connection Failures, D. Game Logic Failures, E. Integration Test Failures, FAILURE PATTERN RECOGNITION

### Community 1067 - "P3 · realtime-connection + events-nats"
Cohesion: 0.20
Nodes (9): CONFORMS worth recording, H1 · DLQ automatic cleanup is not wired — unbounded disk growth, H2 · ADR-003 is self-contradictory about the EventBus being networked, H3 · ADR-003 quotes deprecated NATS subject forms as current, High risk — require P5 refutation before ruling, Low / STALE, Medium risk, Meta-finding (+1 more)

### Community 1068 - "P4 · Intent Sweep — Plan Documents"
Cohesion: 0.20
Nodes (9): Conforming — substantial features that check out, Correction to a prior audit finding, CRITICAL · The guard that was supposed to prevent raw SQL was never connected, HIGH · ADR-009 number collision — code cites a decision that does not exist, Meta-finding · plan status is unreliable in *both* directions, P4 · Intent Sweep — Plan Documents, PLAN CLAIMED COMPLETE, CODE ABSENT, PLANNED BUT NOT BUILT (+1 more)

### Community 1069 - "P7 · Rulings — complete"
Cohesion: 0.20
Nodes (10): C1 · What are the ADRs for? — **Mark provenance, keep ADRs for new decisions**, C2 · Query construction — **Fix the guard now, defer the doc decision**, C3 · Layer boundaries — **Split three ways**, C4 · Container architecture doc — **Restore to `docs/` with a provenance note**, C5 · Doc↔doc contradictions — **In-place for ADR-003, cross-reference for ADR-004**, C6 · Contract drift — **Record `/v1` + fix all dependent paths**, C7 · Closed-but-not-built — **Reopen everything**, C8 · Undocumented systems — **ADR for WebSocket security + ui-v2; doc updates for the rest** (+2 more)

### Community 1070 - "P8 · Applied"
Cohesion: 0.20
Nodes (9): Code changes — comment-only, explicitly authorised, Documentation changes — 33 files, Issues created — 14, Issues reopened — 12, New ADRs, Not done — deliberately, P8 · Applied, Security — filed privately, not publicly (+1 more)

### Community 1071 - "Design ↔ Implementation Drift Audit — Final Summary"
Cohesion: 0.20
Nodes (10): Decisions made — do not re-litigate, Design ↔ Implementation Drift Audit — Final Summary, Do first — small, high value, Loose ends outside the tracker, Sequencing that matters, User-visible defects, Weight the evidence correctly, What the audit concluded (+2 more)

### Community 1072 - "Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12)"
Cohesion: 0.20
Nodes (9): Communities (1 total, 1 thin omitted), Community Hubs (Navigation), Corpus Check, God Nodes (most connected - your core abstractions), Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu Investigator Handbook 7th Edition  (2026-08-12), Knowledge Gaps, Suggested Questions, Summary (+1 more)

### Community 1073 - "Lucidity.md"
Cohesion: 0.24
Nodes (5): Lucidity, Pandora's Box (Pulp campaign), Using Luck (Pulp), Key extrated pages, Pulp Sanity

### Community 1075 - "enum"
Cohesion: 0.29
Nodes (7): autumn, spring, summer, winter, season, enum, type

### Community 1076 - "Chat Panel Separation Specification"
Cohesion: 0.29
Nodes (6): Chat Panel Separation Specification, Conclusion, Current Integration Points, Current State Analysis, Existing Structure, Overview

### Community 1077 - "AnyIO vs Asyncio: High-Level Comparison and Decision Guide"
Cohesion: 0.20
Nodes (10): Adjusts spectacles and peers at the codebase, anyio Cons ❌, anyio Pros ✅, AnyIO vs Asyncio: High-Level Comparison and Decision Guide, asyncio Cons ❌, asyncio Pros ✅, Decision Matrix, My Academic Opinion (Mythos Persona) (+2 more)

### Community 1078 - "Asynchronous Code Audit - December 3, 2025"
Cohesion: 0.14
Nodes (13): adjusts spectacles grimly, Asynchronous Code Audit - December 3, 2025, ✍️ AUDIT CONCLUSION, Audit Status**: ✅**COMPLETE, Blocking Risks, 📞 ESCALATION MATRIX, Executive Summary, Non-Blocking Risks (+5 more)

### Community 1079 - "Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES"
Cohesion: 0.20
Nodes (10): Phase 1: Critical Fixes (Week 1) - BLOCKING ISSUES, Phase 3: Medium Priority Improvements (Week 4) - POLISH, 📋 REMEDIATION PLAN, Task 1.1: Fix Synchronous Blocking in Passive Lucidity Flux Service, Task 1.2: Eliminate asyncio.run() from Library Code, Task 1.3: Ensure Connection Pool Cleanup, Task 1.4: Add Exception Handling to Pool Creation, Task 1.5: Fix Blocking Operations in NATS Message Handlers (+2 more)

### Community 1080 - "📋 Test Coverage Breakdown"
Cohesion: 0.20
Nodes (10): API Endpoints (Tests Created, Pending Fresh Session), Auth (Tests Created, Pending Fresh Session), Caching (100% Complete), Commands (Tests Created, Pending Fresh Session), Infrastructure (100% Complete), NPC System (Tests Created, Pending Fresh Session), Real-Time (100% Complete), 📋 Test Coverage Breakdown (+2 more)

### Community 1081 - "`docs/**/*` files: Multiple rules"
Cohesion: 0.20
Nodes (10): B904 - Broad except, `docs/**/*` files: Multiple rules, E402 - Module level import not at top, F811 - Redefined name, F821 - Undefined name, F841 - Unused variable, `__init__.py` files: F401 (unused import), Per-File Ignores (pyproject.toml) (+2 more)

### Community 1082 - "2. Model Updates Verified"
Cohesion: 0.20
Nodes (10): 1. Code Quality Checks, 2. Model Updates Verified, 3. Type Compatibility, 4. Database Schema Alignment, ✅ `server/models/lucidity.py`, ✅ `server/models/npc.py`, ✅ `server/models/player.py`, ✅ `server/models/player_spells.py` (+2 more)

### Community 1083 - "Findings"
Cohesion: 0.20
Nodes (10): Findings, 🟡 HIGH PRIORITY: Manual Statistical Calculations, Issue 1: Performance Monitor - Manual Statistics, Issue 2: Performance Tracker - Repeated Statistical Operations, Issue 3: Stats Generator - Manual Dice Rolling, Issue 4: Stats Summary - Manual Summation, Issue 5: Missing NumPy Type Hints, 🔵 LOW PRIORITY: Type Hints and Documentation (+2 more)

### Community 1084 - "Repository Details"
Cohesion: 0.20
Nodes (10): 1. PlayerRepository (439 lines), 2. RoomRepository (42 lines), 3. ProfessionRepository (74 lines), 4. HealthRepository (165 lines), 5. ExperienceRepository (203 lines), 6. ContainerRepository (80 lines), 7. ItemRepository (84 lines), Async Repository Structure (+2 more)

### Community 1085 - "POSTGRESQL_AUDIT_REPORT_2026.md"
Cohesion: 0.27
Nodes (8): bigint generated always as identity, Migration 019 PostgreSQL Anti-patterns Fixes, Schema Drift player_id uuid vs varchar, SELECT * Anti-pattern, varchar(n) Prefer text, players.current_room_id Index Gap, Integer to BigInteger Column Mapping, String(n) to Text Column Mapping

### Community 1086 - "TEST_COVERAGE_DISCONNECT_GRACE_PERIOD_REST.md"
Cohesion: 0.20
Nodes (9): Disconnect Grace Period, Zombie Linkdead State, Disconnect Grace Period and Rest Command, Rest Command, 30-Second Disconnect Grace Period, ADR-009 Effects System Architecture, LOGIN_WARDED Effect, Effects System ADR and Implementation (+1 more)

### Community 1087 - "Implementation Phases"
Cohesion: 0.20
Nodes (10): Deliverables, Implementation Phases, Phase 0: Foundation (Week 1) - 40 hours, Phase 1: Fix Failing Tests (Week 1-2) - 40 hours, Phase 2: Unit Test Modernization (Week 3-4) - 80 hours, Phase 2A: Service Layer Tests (Week 3), Phase 2B: Infrastructure Tests (Week 4), Phase 3: Test Pattern Modernization (Week 5) - 40 hours (+2 more)

### Community 1088 - "Conclusion"
Cohesion: 0.40
Nodes (5): ~25-30% (1,250-1,500 tests) provide CRITICAL protection, Answer to Your Question, Conclusion, Recommended Action, The remaining 70-75% provide

### Community 1089 - "MythosMUD Testing Strategy (Greenfield Suite)"
Cohesion: 0.22
Nodes (9): Coverage policy, Fixtures/layout, Isolation rules, Logging and diagnostics, Markers, Mocking standards, MythosMUD Testing Strategy (Greenfield Suite), Tiers and commands (+1 more)

### Community 1090 - "Dialogue Content Tools (Content Creators)"
Cohesion: 0.20
Nodes (9): 1. Overview, 2. Open the editor, 3. Tree shape (nav-only), 4. Editor workflow, 5. Player verification, 6. Seed and API reference, 7. Related docs, AI READING INSTRUCTION (+1 more)

### Community 1091 - "load_test_10_players.spec.ts"
Cohesion: 0.22
Nodes (6): generateLoadTestCredential(), INVITE_CODES, PLAYER_CONFIGS, PlayerConfig, NOTE: This test is designed to be executed using Playwright MCP tools for, registerPlayer()

### Community 1092 - "emote_schema.json"
Cohesion: 0.05
Nodes (38): additionalProperties, properties, required, type, additionalProperties, description, items, type (+30 more)

### Community 1093 - "bench_cache_npc.py"
Cohesion: 0.31
Nodes (5): bench_npc_cache(), _FakeNPCService, main(), Any, NPC cache micro-benchmark for CI artifacts. Measures miss vs. hit timings for…

### Community 1094 - "bench_cache_professions.py"
Cohesion: 0.31
Nodes (7): bench_profession_cache(), _FakePersistence, _get_empty_dict(), main(), Any, Professions cache micro-benchmark for CI artifacts. Measures miss vs. hit…, Helper function to return empty dict for mock methods.

### Community 1095 - "check_file"
Cohesion: 0.27
Nodes (9): check_file(), main(), Path, Remove triple-quoted string blocks from file content., Remove string literals from line to avoid false positives inside docs/strings., Return list of (line_no, line) where asyncio.run( appears in code., Return 0 if no asyncio.run( in server/, else 1., _strip_string_literals() (+1 more)

### Community 1096 - "populate_test_npc_databases.py"
Cohesion: 0.31
Nodes (8): get_npc_data_from_source(), get_npc_database_url(), main(), populate_database(), Populate a PostgreSQL database with NPC data. Args: target_url: PostgreSQL…, Main function to populate test NPC databases., Get NPC database URL for the specified environment. Args: environment:…, Extract NPC data from the source PostgreSQL database. Args: source_url:…

### Community 1097 - ".__init__"
Cohesion: 0.20
Nodes (7): Check if the status effect is still active., Any, Initialize Invite with defaults., _npc_alive_and_active(), setter, Return True if NPC is alive (determination_points > 0)., Allow backward-compatible assignment (npc.is_alive = False).

### Community 1098 - "properties"
Cohesion: 0.12
Nodes (16): tomeMetadata, minimum, type, mythos_gain, sanity_loss_expr, spells, study_hours, maxLength (+8 more)

### Community 1099 - "Any"
Cohesion: 0.22
Nodes (9): _coerce_row_stats(), _defaulted_numerics(), _defaulted_strings(), _parse_equipped_safely(), Any, Extract and coerce stats from row. Returns empty dict if not a dict., Parse equipped_json to dict. Returns empty dict on parse error or invalid type., Extract string fields with defaults: inventory_json, equipped_json,… (+1 more)

### Community 1100 - "lucidity_migration.py"
Cohesion: 0.24
Nodes (9): migrate_lucidity_system(), migrate_multiple(), parse_args(), Namespace, Path, Schema migration for the MythosMUD lucidity system tables., Run the lucidity migration across multiple database files., Parse CLI arguments for the lucidity migration runner. (+1 more)

### Community 1101 - "ensure_directory_exists"
Cohesion: 0.25
Nodes (8): ensure_directory_exists(), Ensure a directory exists and return its absolute path. Args: directory: The…, Test ensure_directory_exists with existing directory., Test ensure_directory_exists creates directory if it doesn't exist., Test ensure_directory_exists with relative path., test_ensure_directory_exists_creates(), test_ensure_directory_exists_existing(), test_ensure_directory_exists_relative_path()

### Community 1102 - "test_calendar_procedures.py"
Cohesion: 0.38
Nodes (9): holiday_row(), npc_schedule_row(), async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/calendar.sql (#633). Replace raw SQL…, test_get_calendar_holidays_includes_the_new_row() (+1 more)

### Community 1103 - "emote_row"
Cohesion: 0.31
Nodes (9): emote_row(), async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/emotes.sql (#633). Replace raw SQL…, Create one emote with one alias. Yields (stable_id, alias)., test_get_emote_aliases_joins_owning_emote() (+1 more)

### Community 1104 - "zone_and_subzone"
Cohesion: 0.31
Nodes (9): async_sessionmaker, asyncio, AsyncSession, fixture, Integration tests for db/procedures/npcs.sql's zone/subzone config read…, Create one zone and one subzone with unique stable_ids. Yields (zone_stable_id,…, test_get_subzone_configs_joins_parent_zone(), test_get_zone_configs_includes_the_zone() (+1 more)

### Community 1105 - "test_async_persistence_room_loading.py"
Cohesion: 0.20
Nodes (9): Unit tests for async persistence layer: process_room_rows, process_exit_rows,…, Test _process_exit_rows with stable_ids that already contain full hierarchical…, Test _build_room_objects logs debug info for specific room., Test _load_room_cache successfully loads rooms., Test _process_room_rows with zone_stable_id that has only one part (no slash)., test_build_room_objects_debug_logging(), test_load_room_cache_success(), test_process_exit_rows_with_full_room_ids() (+1 more)

### Community 1106 - "TestMinimapExplorationInvestigationDoc"
Cohesion: 0.20
Nodes (6): Guardrails for minimap / exploration documentation. Ensures the investigation…, Content checks for the minimap explored-rooms investigation document., The session document must remain present for traceability., Documentation must state that explored room identifiers are UUIDs, not…, Documentation must tie the bug to non-admin minimap behavior (not only admins)., TestMinimapExplorationInvestigationDoc

### Community 1107 - "test_skill_use_log_repository.py"
Cohesion: 0.33
Nodes (8): _mock_session(), asyncio, fixture, Unit tests for SkillUseLogRepository., repo(), test_get_skill_ids_used_at_level(), test_record_use(), test_record_use_db_error()

### Community 1108 - "local-channel-isolation.spec.ts"
Cohesion: 0.43
Nodes (7): ensureIthaquaInFoyer(), leaveEasternHallwayWest(), pageShowsEasternHallway(), primeBothForCoLocate(), returnAwToFoyerIfInHallway(), softCommand(), waitForLookReflected()

### Community 1109 - "test_combat_validator.py"
Cohesion: 0.02
Nodes (96): combat_validator(), fixture, Unit tests for combat validator. Tests the CombatValidator class for combat…, Test validate_combat_command with target name too long., Test validate_combat_command when rate limited., Test validate_combat_command handles exceptions gracefully., Test validate_target_exists with exact match., Test validate_target_exists with case-insensitive match. (+88 more)

### Community 1110 - "optimized_validate_action_content"
Cohesion: 0.20
Nodes (10): Test validating empty action., Test validating valid action., Test validating action with dangerous characters., Test validating action with injection pattern., test_optimized_validate_action_content_dangerous_chars(), test_optimized_validate_action_content_empty(), test_optimized_validate_action_content_injection(), test_optimized_validate_action_content_valid() (+2 more)

### Community 1111 - "optimized_validate_alias_name"
Cohesion: 0.20
Nodes (10): Test validating empty alias name., Test validating valid alias name., Test validating alias name starting with number (invalid)., Test validating alias name with hyphen (invalid - aliases don't allow hyphens)., test_optimized_validate_alias_name_empty(), test_optimized_validate_alias_name_hyphen(), test_optimized_validate_alias_name_starts_with_number(), test_optimized_validate_alias_name_valid() (+2 more)

### Community 1112 - "optimized_sanitize_unicode_input"
Cohesion: 0.20
Nodes (10): Test sanitizing empty string., Test sanitizing normal text (no changes expected)., Test sanitizing text with Unicode issues., test_optimized_sanitize_unicode_input_empty(), test_optimized_sanitize_unicode_input_normal_text(), test_optimized_sanitize_unicode_input_unicode(), _cached_ftfy_fix(), optimized_sanitize_unicode_input() (+2 more)

### Community 1113 - "optimized_validate_security_comprehensive"
Cohesion: 0.20
Nodes (10): Test comprehensive security validation of empty string., Test comprehensive security validation of valid text., Test comprehensive security validation with dangerous characters., Test comprehensive security validation with injection pattern., test_optimized_validate_security_comprehensive_dangerous_chars(), test_optimized_validate_security_comprehensive_empty(), test_optimized_validate_security_comprehensive_injection(), test_optimized_validate_security_comprehensive_valid() (+2 more)

### Community 1114 - "gh-stack (MythosMUD)"
Cohesion: 0.22
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1115 - "Workflows"
Cohesion: 0.22
Nodes (9): End-to-end: create a stack from scratch, Handle rebase conflicts (agent workflow), Making mid-stack changes, Modify a mid-stack branch and sync, Parsing `--json` output, Restructure a stack (remove a branch, reorder, or rename), Routine sync after merges, Squash-merge recovery (+1 more)

### Community 1116 - "test_db_connectivity_create_and_read_user"
Cohesion: 0.29
Nodes (8): cleanup_test_user(), async_sessionmaker, asyncio, AsyncSession, fixture, Yield a fresh user id and guarantee its row is deleted after the test, pass or…, Test that we can create and read a User from the database., test_db_connectivity_create_and_read_user()

### Community 1117 - "run_quality_fragmentation_guard.py"
Cohesion: 0.31
Nodes (12): _argv_char_len(), _build_guard_command(), _changed_files_between(), _git_executable(), _is_graphify_path(), _local_changed_files(), main(), Path (+4 more)

### Community 1118 - "Frontend Aesthetics Guidelines"
Cohesion: 0.22
Nodes (9): Color & Theme, Frontend Aesthetics Guidelines, Interaction, Layout & Space, Motion, Responsive, Typography, UX Writing (+1 more)

### Community 1119 - "run-playwright-tests.js"
Cohesion: 0.22
Nodes (7): clientRoot, __dirname, E2E_BACKEND_BASE_URL, env, __filename, playwright, testsDir

### Community 1120 - "mythos_e2e Database"
Cohesion: 0.25
Nodes (8): ArkanWolfshade E2E Account, Ithaqua E2E Account, mythos_e2e Database, Playwright Runtime E2E Suite, seed_e2e_users.py, start_e2e_test.ps1, pytest Markers unit integration e2e slow serial, Post-Scenario Cleanup

### Community 1122 - "holidays.schema.json"
Cohesion: 0.25
Nodes (7): additionalProperties, $id, holidays, required, $schema, title, type

### Community 1123 - "🟡 HIGH PRIORITY ISSUES"
Cohesion: 0.22
Nodes (9): 10. Loading All Players Instead of Active Only, 11. NATS Connection Pool Not Used by Default, 12. No TLS Configuration for NATS, 13. Event Loop Change Detection Edge Cases, 14. Missing Transaction Rollback on Critical Failures, 7. Missing Room Lookup Caching, 8. Incomplete Migration to Async Persistence, 9. Multiple Database Flushes Before Commit (+1 more)

### Community 1124 - "🟢 MEDIUM PRIORITY IMPROVEMENTS"
Cohesion: 0.13
Nodes (15): 15. Hardcoded Connection Pool Sizes, 16. Deprecated asyncio.get_event_loop() Usage, 17. Inconsistent Error Handling Patterns, 18. Memory Leak Risk in Metrics Collection, 19. Missing Message Acknowledgment in NATS, 20. Subject Naming Inconsistency, 21. No Connection Health Monitoring, 🟢 MEDIUM PRIORITY IMPROVEMENTS (+7 more)

### Community 1125 - "Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE"
Cohesion: 0.22
Nodes (9): Phase 2: High Priority Fixes (Week 2-3) - PERFORMANCE, Task 2.1: Add Room Lookup Caching, Task 2.2: Complete Async Persistence Migration, Task 2.3: Optimize Database Flush Operations, Task 2.4: Load Only Active Players, Task 2.5: Use NATS Connection Pool by Default, Task 2.6: Add TLS Configuration, Task 2.7: Improve Event Loop Change Detection (+1 more)

### Community 1126 - "async_persistence_room_loader.py"
Cohesion: 0.36
Nodes (5): Room-cache loading and RoomCacheLoader test hooks for AsyncPersistenceLayer., _coerce_exit_entries(), ExitJsonEntry, Room cache loading for async persistence layer. Extracted from…, One exit entry from get_rooms_with_exits exits JSON.

### Community 1127 - "Coverage Improvement Summary - Plan 2 Execution"
Cohesion: 0.22
Nodes (9): 🏆 Achievement Highlights, ✅ COMPLETED & VERIFIED (6 modules), Coverage Improvement Summary - Plan 2 Execution, 📝 CREATED & READY (6 modules), 📚 Documentation Created, Executive Summary, 📊 Expected Final Results, 📞 Support (+1 more)

### Community 1128 - "Implementation Notes"
Cohesion: 0.22
Nodes (8): Critical Priority, Dependencies, Environment Contamination Remediation Tasks, Implementation Notes, Spec Tasks, Success Criteria, Tasks, Testing Strategy

### Community 1129 - "Ruff C901 McCabe Complexity"
Cohesion: 0.25
Nodes (9): Fat Endpoints, Service Layer Delegation, McCabe Cyclomatic Complexity, Pylint R0911-R0915 Complexity Metrics, Ruff C901 McCabe Complexity, Ruff-Pylint Rule Parity, Lizard CCN Threshold, create_app (+1 more)

### Community 1130 - "Positive Findings ✅"
Cohesion: 0.22
Nodes (9): 1. **Excellent Error Boundary Implementation**, 2. **Good Connection State Management**, 3. **Proper Async/Await Usage**, 4. **Subject Manager Pattern**, 5. **TLS Configuration Implemented**, 6. **Connection Pooling Implemented**, 7. **Message Acknowledgment Support**, 8. **Async Mute Data Loading** (+1 more)

### Community 1131 - "Detailed Implementation"
Cohesion: 0.22
Nodes (9): 1. Error Handling Standardization, 2. Message Validation, 3. Batch Flush Error Recovery, 4. Connection Pool Error Handling, 5. Subject Manager Integration, 6. Health Monitoring, 7. Acknowledgment Metrics, 8. Wildcard Validation (+1 more)

### Community 1132 - "Specific File Reviews"
Cohesion: 0.22
Nodes (9): `server/api/players.py`, `server/auth/endpoints.py`, `server/config/models.py`, `server/models/command.py`, `server/models/game.py`, `server/schemas/invite.py`, `server/schemas/player.py`, `server/schemas/user.py` (+1 more)

### Community 1133 - "Python Code Coverage Status"
Cohesion: 0.22
Nodes (8): Critical Files Below Threshold, Immediate Priority (Critical Files), Normal Files Below 70% Threshold, Priority Recommendations, Python Code Coverage Status, Secondary Priority (Normal Files), Showing top 50 files with largest coverage gaps, Summary

### Community 1134 - "Server & Client Package Documentation Coverage"
Cohesion: 0.22
Nodes (9): 1. Overview, 2. Index, 3. Related documentation, 4. Changelog, AI READING INSTRUCTION, Documented (16), Provisional (2), Server & Client Package Documentation Coverage (+1 more)

### Community 1135 - "monitoring_service"
Cohesion: 0.25
Nodes (8): mock_combat_config(), mock_config(), mock_feature_flags(), monitoring_service(), fixture, Create mock feature flags., Create mock combat config., Create CombatMonitoringService instance with mocked dependencies.

### Community 1136 - "enum"
Cohesion: 0.20
Nodes (10): artifact, consumable, container, currency, equipment, quest, enum, type (+2 more)

### Community 1137 - "applies_to"
Cohesion: 0.17
Nodes (13): items, minItems, type, items, minItems, type, items, type (+5 more)

### Community 1138 - "validate_shutdown_admin_permission"
Cohesion: 0.25
Nodes (8): Validate that a player has admin permissions for server shutdown. Args: player:…, validate_shutdown_admin_permission(), Test validate_shutdown_admin_permission() returns False when player is None., Test validate_shutdown_admin_permission() returns False when player is not…, Test validate_shutdown_admin_permission() returns True when player is admin., test_validate_shutdown_admin_permission_admin(), test_validate_shutdown_admin_permission_no_player(), test_validate_shutdown_admin_permission_not_admin()

### Community 1139 - "bench_cache.py"
Cohesion: 0.31
Nodes (6): bench_room_cache(), _FakePersistence, main(), Any, Lightweight cache benchmark for CI artifacts. Measures miss vs. hit timings for…, Fake persistence layer providing async_get_room with simulated latency.

### Community 1140 - "HealthErrorResponse"
Cohesion: 0.25
Nodes (8): HealthErrorResponse, Error response for health check failures., Test HealthErrorResponse can be created with required fields., Test HealthErrorResponse rejects unknown fields., Test HealthErrorResponse is frozen (immutable)., test_health_error_response_creation(), test_health_error_response_frozen(), test_health_error_response_rejects_extra_fields()

### Community 1141 - "_filter_lines"
Cohesion: 0.31
Nodes (8): _filter_lines(), main(), Skip a TABLE DATA block (COPY ... \\.). Return index after the block., Skip a SEQUENCE SET block (setval + trailing blank lines). Return index after…, Filter out TABLE DATA and SEQUENCE SET blocks for excluded tables/sequences., Read export DML, drop COPY/SEQUENCE blocks for runtime tables, write back., _skip_sequence_set_block(), _skip_table_data_block()

### Community 1142 - "fix_markdown_file"
Cohesion: 0.36
Nodes (8): fix_markdown_file(), fix_multiple_blanks(), main(), parse_markdownlint_output(), Path, Fix multiple consecutive blank lines (MD012). Returns: (new_content,…, Parse markdownlint output to get files with MD012 issues., Fix multiple blank lines in a single markdown file. Returns: (changed,…

### Community 1143 - "fix_room_references"
Cohesion: 0.36
Nodes (8): fix_room_references(), load_room_file(), main(), Path, Load a room file safely., Save a room file safely., Fix room ID references in the northside area. Args: base_path: Path to the…, save_room_file()

### Community 1144 - "run_bug_prevention_tests.ps1"
Cohesion: 0.53
Nodes (8): Invoke-ClientTest(), Invoke-IntegrationTest(), Invoke-ServerTest(), Show-TestSummary(), Test-Command(), Write-ColorOutput(), Write-Header(), Write-Section()

### Community 1145 - "run_make_stages.py"
Cohesion: 0.33
Nodes (8): keep_going_requested(), main(), _print_fail(), Return True when Make was invoked with -k / --keep-going., Return a short failure reason, or None if the stage is OK., Run `make <stage>`, stream output, return (exit_code, captured_output)., run_stage(), stage_failed_from_output()

### Community 1146 - "load_zone_configurations"
Cohesion: 0.25
Nodes (8): load_zone_configurations(), Load zone and sub-zone configurations from PostgreSQL database. Returns:…, Test load_zone_configurations() loads configurations., Test load_zone_configurations() merges zone and subzone configs., Test load_zone_configurations() raises RuntimeError on failure., test_load_zone_configurations_error(), test_load_zone_configurations_merges_zone_and_subzone(), test_load_zone_configurations_success()

### Community 1147 - "required"
Cohesion: 0.25
Nodes (8): description, exits, id, name, plane, sub_zone, zone, required

### Community 1148 - "connection_state_machine.py"
Cohesion: 0.29
Nodes (7): ConnectionEvent, Enum, Connection state machine for NATS messaging. Implements a robust state machine…, Events that trigger state transitions. AI: Explicit events make the FSM…, Test ConnectionEvent enum values., test_connection_event_enum(), StateMachine

### Community 1149 - "logger.test.ts"
Cohesion: 0.29
Nodes (6): mockAppendChild, mockClick, mockConsole, mockCreateElement, mockCreateObjectURL, mockRemoveChild

### Community 1150 - "verify_npc_occupants.py"
Cohesion: 0.23
Nodes (12): _check_service_availability(), _collect_npcs_by_room(), _print_summary(), Any, Verification script to check NPCs in lifecycle manager and test occupant query…, Print verification summary. Args: npc_count: Total number of active NPCs…, Verify NPCs exist in lifecycle manager and test query logic., Check if NPC service, lifecycle manager, and active_npcs are available.… (+4 more)

### Community 1151 - "NPC catalog pipeline (private `data/` submodule)"
Cohesion: 0.29
Nodes (6): Current batches, Generate (from MythosMUD repo root), Human review gate (required before DML commit), Layout, NPC catalog pipeline (private `data/` submodule), Out of scope here

### Community 1152 - "player_inventory_migration.py"
Cohesion: 0.28
Nodes (8): migrate_multiple(), migrate_player_inventories(), parse_args(), Namespace, Path, Create and backfill the player_inventories table., Ensure the player_inventories table exists and is populated for existing…, Run the migration across multiple database paths.

### Community 1153 - "strict_mocker"
Cohesion: 0.28
Nodes (8): Any, fixture, MockerFixture, Strict mocking helpers for unit tests. Provides fixtures and helpers that…, Return a patch helper that enables autospec by default. Usage: patched_fn =…, Convenience helper for direct calls with autospec=True by default., strict_mocker(), strict_patch()

### Community 1154 - "fixture"
Cohesion: 0.22
Nodes (9): mock_connection_manager(), mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request object., Create a mock persistence layer., Create a mock connection manager. (+1 more)

### Community 1155 - "test_utility_commands_whoami.py"
Cohesion: 0.28
Nodes (8): asyncio, Unit tests for utility command handlers. Tests the whoami command functionality., Test handle_whoami_command() returns player information., Test handle_whoami_command() handles missing persistence., Test handle_whoami_command() handles player not found., test_handle_whoami_command(), test_handle_whoami_command_no_persistence(), test_handle_whoami_command_player_not_found()

### Community 1156 - "get_config"
Cohesion: 0.06
Nodes (40): _create_config_instance(), get_app_instance(), get_config(), _get_config_cached(), _get_config_test(), _is_test_mode(), Configuration module for MythosMUD server. This module provides type-safe,…, Return the runtime app instance attached during lifespan startup. This provides… (+32 more)

### Community 1157 - "test_spell_effects_internal.py"
Cohesion: 0.33
Nodes (6): coerce_effect_float_times_mastery_as_int(), Coerce to float first, then apply mastery (lucidity-style deltas)., Unit tests for internal spell effect helpers., test_coerce_effect_float_times_mastery_as_int(), test_coerce_effect_int_times_mastery(), test_combat_room_id_for_npc_spell_paths()

### Community 1158 - "room_validator/schemas/unified_room_schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, allOf, description, $schema, title, type

### Community 1159 - "test_room_subscription_manager_drops.py"
Cohesion: 0.03
Nodes (64): fixture, Unit tests for room subscription manager drop functions. Tests the room drop…, Test adjust_room_drop() returns False for invalid index., Test list_room_drops() returns room drops., Test add_room_drop() adds drop to new room., Test add_room_drop() adds drop to existing room., Test take_room_drop() successfully takes drop., Test take_room_drop() with index out of range. (+56 more)

### Community 1160 - "test_websocket_handler_disconnect.py"
Cohesion: 0.22
Nodes (8): MockerFixture, Unit tests for websocket handler disconnect handling. Tests the disconnect…, Test _handle_websocket_disconnect() returns True., Test _handle_websocket_disconnect() with no connection_id., The WebSocket close code/reason must reach the log, not be silently discarded.…, test_handle_websocket_disconnect(), test_handle_websocket_disconnect_logs_close_code_and_reason(), test_handle_websocket_disconnect_no_connection_id()

### Community 1161 - "properties"
Cohesion: 0.25
Nodes (8): description, enum, type, indoors, outdoors, underwater, properties, environment

### Community 1162 - "_RealtimeConnectionManager"
Cohesion: 0.23
Nodes (3): UUID, Connection manager API used by realtime HTTP/WebSocket routes., _RealtimeConnectionManager

### Community 1163 - "optimized_validate_target_player"
Cohesion: 0.25
Nodes (8): Test validating empty target player name., Test validating valid target player name., Test validating invalid target player name., test_optimized_validate_target_player_empty(), test_optimized_validate_target_player_invalid(), test_optimized_validate_target_player_valid(), optimized_validate_target_player(), Optimized validation for target player fields. Args: value: The target player…

### Community 1164 - "Room Pathing Validator Implementation Spec"
Cohesion: 0.22
Nodes (9): Bidirectional Path Validation, Connectivity Analysis, Exit Flags (one_way, self_reference), Legacy string exit format, Object exit format with flags, Room Pathing Validator Implementation Spec, Legacy exit format migration support, earth_arkhamcity_intersection_derby_high start room (+1 more)

### Community 1165 - "validator.py CLI"
Cohesion: 0.22
Nodes (9): core/path_validator.py, core/reporter.py, core/room_loader.py, core/schema_validator.py, validator.py CLI, click CLI dependency, Graph Building Issues, Path Validator Test Failures (+1 more)

### Community 1166 - "gh-stack"
Cohesion: 0.25
Nodes (8): Agent rules, Exit codes and error recovery, gh-stack, Known limitations, Output conventions, Prerequisites, Quick reference, When to use this skill

### Community 1167 - "items"
Cohesion: 0.33
Nodes (6): additionalProperties, properties, schedules, items, minItems, type

### Community 1168 - "Motion Design"
Cohesion: 0.25
Nodes (8): Duration: The 100/300/500 Rule, Easing: Pick the Right Curve, Motion Design, Perceived Performance, Performance, Reduced Motion, Staggered Animations, The Only Two Properties You Should Animate

### Community 1169 - "MythosMUD Commit Messages"
Cohesion: 0.25
Nodes (8): GH Stack Skill, Commit Messages Skill, Examples, Format, MythosMUD Commit Messages, Rules, Template, Types

### Community 1170 - "worktree-plan-template.md"
Cohesion: 0.25
Nodes (7): Cleanup Checklist, Context, Design Notes, Metadata, Plan / Todos, Risks and Edge Cases, Testing

### Community 1171 - "Step 2: Ask UX-Focused Questions"
Cohesion: 0.25
Nodes (8): Teach Impeccable Skill, Accessibility & Inclusion, Aesthetic Preferences, Brand & Personality, Step 1: Explore the Codebase, Step 2: Ask UX-Focused Questions, Step 3: Write Design Context, Users & Purpose

### Community 1172 - "run-vitest.js"
Cohesion: 0.25
Nodes (7): args, clientRoot, __dirname, env, __filename, vitest, vitestBin

### Community 1173 - "usePerformanceMonitor.ts"
Cohesion: 0.29
Nodes (6): ExtendedPerformance, ExtendedPerformance, PerformanceMemory, PerformanceMetrics, usePerformanceMonitor(), UsePerformanceMonitorOptions

### Community 1174 - "mock_persistence"
Cohesion: 0.29
Nodes (7): mock_persistence(), mock_player(), mock_request(), fixture, Create a mock request with app state and container., Create a mock persistence., Create a mock player.

### Community 1175 - "cli.sh"
Cohesion: 0.46
Nodes (7): download(), download_cli(), download_file(), get_latest_version(), get_version_from_yaml(), handle_rate_limit(), cli.sh script

### Community 1176 - "Earth Plane"
Cohesion: 0.25
Nodes (8): Arkham City Zone Visualization, Arkham City, Innsmouth, Miskatonic University, The Dreamlands, Earth Plane, The Investigators, Limbo / Death Plane

### Community 1177 - "C2 · REVISED — procedures-only is binding"
Cohesion: 0.25
Nodes (7): C2 · REVISED — procedures-only is binding, Consequence for enforcement (#618), Consequence for the code — migration backlog, Consequence for the documents, Known bounded exception, Status, The rule

### Community 1178 - "P3 · config-api"
Cohesion: 0.25
Nodes (7): CONFORMS worth recording, H11 · Config fail-fast is defeated at app construction, degrading to dev CORS, H12 · The `/v1` prefix exists in no design document, and every ADR endpoint path is wrong, H13 · The API specification document specifies no API, Medium / Low, P3 · config-api, Prior finding resolved

### Community 1179 - "P3 · persistence-db"
Cohesion: 0.25
Nodes (7): CONFORMS worth recording, H4 · D1 resolved — the code is a three-pattern hybrid no document describes, H5 · "Services never construct raw queries" is false at three layers, H6 · "Fully Async" is true of the class but not of the code, Medium, P3 · persistence-db, STALE — docs behind completed work

### Community 1180 - "P5 · Adversarial Refutation"
Cohesion: 0.25
Nodes (7): DOWNGRADED · F2 — config fail-fast → dev CORS (High → Low/Medium), DOWNGRADED · F5 — raw SQL at three layers (High → Medium), DOWNGRADED & REFRAMED · F4 — "12 modules bypass the facade" (High → Low), P5 · Adversarial Refutation, SURVIVES · F1 — DLQ never prunes (High, effort S), SURVIVES · F3 — deprecated global still called (High) — and it is worse than stated, What this pass changed

### Community 1181 - "Paris (Reign of Terror).md"
Cohesion: 0.18
Nodes (7): Dietrich Zann, Key extrated pages, Reign of Terror (source summary), Paris (Reign of Terror), Azotottal, Comte Fenalik, Reign of Terror

### Community 1182 - "Authoritative Environment DML"
Cohesion: 0.29
Nodes (8): DB Bootstrap Execution Order, Authoritative Environment DML, Removed Schema and Migration SQL, Legacy Schema Files Removed, Historical DDL Final Status, Historical DDL Partial Status, Historical DDL Verification Summary, mythos_dev players UUID Schema Variation

### Community 1183 - "mythos_dev.item_instances"
Cohesion: 0.36
Nodes (8): mythos_dev.add_item_to_container(), mythos_dev.container_contents, mythos_dev.containers, mythos_dev.get_container_contents_json(), mythos_dev.item_component_states, mythos_dev.item_instance_exists(), mythos_dev.item_instances, mythos_dev.item_prototypes

### Community 1185 - "emotes.schema.json"
Cohesion: 0.06
Nodes (31): additionalProperties, additionalProperties, properties, required, type, items, type, uniqueItems (+23 more)

### Community 1186 - "1. Enhanced ChatPanel (New Chat Input Panel)"
Cohesion: 0.25
Nodes (8): 1. Enhanced ChatPanel (New Chat Input Panel), 2. Renamed Game Log Panel (Formerly ChatPanel), ChatPanel Layout Structure, Enhanced ChatPanel Interface, Game Log Panel Layout Structure, New Features to Add, Proposed Changes, Purpose and Functionality

### Community 1187 - "✅ Verified Already Implemented"
Cohesion: 0.25
Nodes (8): 10. TLS Configuration, 4. Connection Pool Cleanup, 5. Mute Data Caching, 6. F-String Logging, 7. Database Flush Operations, 8. Active Player Filtering, 9. NATS Connection Pooling, ✅ Verified Already Implemented

### Community 1188 - "Implementation Phases"
Cohesion: 0.25
Nodes (8): 1.1 Enhance CircuitBreaker Class, 1.2 Create CircuitBreaker Manager, 1.3 Add Configuration Support, 5.1 Authentication Operations, 5.2 Rate Limiting Integration, Implementation Phases, Phase 1: Core Infrastructure Enhancement, Phase 5: Authentication and Security

### Community 1189 - "3. REFACTOR Findings (935 findings)"
Cohesion: 0.25
Nodes (8): 3.1 Too Many Instance Attributes (R0902), 3.2 Too Many Arguments (R0913, R0917), 3.3 Too Many Local Variables (R0914), 3.4 Too Many Statements (R0915), 3.5 Too Many Return Statements (R0911), 3.6 Too Many Public Methods (R0904), 3.7 No-Else-Return (R1705), 3. REFACTOR Findings (935 findings)

### Community 1190 - "LOGGING_BEST_PRACTICES.md"
Cohesion: 0.25
Nodes (6): enhanced_logging_config.get_logger, Structured Logging, measure_performance, NumPy Code Review, roll_4d6_drop_lowest, NumPy Vectorized Statistics

### Community 1191 - "NumPy Code Review - MythosMUD Codebase"
Cohesion: 0.25
Nodes (8): Code Quality Improvements Achieved, Completed Actions, Conclusion, Executive Summary, ✅ Implementation Status, NumPy Code Review - MythosMUD Codebase, Summary of Recommendations, Testing Considerations

### Community 1192 - "Multiplayer Architecture Planning"
Cohesion: 0.25
Nodes (8): Performance Optimization Summary, Alias System Implementation Plan, Chat System Implementation Plan, Planning Completion Summary, Movement System Planning, Multiplayer Architecture Planning, NATS Service, Redis to NATS Migration Plan

### Community 1193 - "API Endpoints (Phase 2)"
Cohesion: 0.25
Nodes (8): API Endpoints (Phase 2), Detailed File Migration Instructions, `server/api/containers.py`, `server/api/players.py`, `server/api/rooms.py`, `server/services/combat_service.py`, `server/services/user_manager.py`, Services (Phase 4)

### Community 1194 - "PYDANTIC_CODE_REVIEW.md"
Cohesion: 0.22
Nodes (7): Parameterized Queries, Pydantic v2 ConfigDict, Pydantic __slots__ Performance, Stats extra=allow Security Risk, Deprecated asyncio.get_event_loop, jsonb_set Field Name f-string SQL, time.sleep in Async Retry

### Community 1195 - "Top Time Consumers (>10 seconds)"
Cohesion: 0.25
Nodes (8): Argon2 Password Tests (1.4+ seconds), Auth & Security Tests (21+ seconds setup each), Infrastructure Tests (3.5+ seconds), NATS Message Handler Tests (2-3 seconds), Performance Tests (still running despite slow marker), Rate Limiter Timing Tests (still running), SSE Handler Tests (60 seconds total), Top Time Consumers (>10 seconds)

### Community 1196 - "pyrightconfig.json"
Cohesion: 0.25
Nodes (7): extends, extraPaths, pythonVersion, venv, venvPath, ., ./pyproject.toml

### Community 1197 - "enum"
Cohesion: 0.25
Nodes (8): catholic, islamic, jewish, mythos, neo_pagan, tradition, enum, type

### Community 1198 - "main"
Cohesion: 0.36
Nodes (7): main(), cursor, Connect to DB from DATABASE_URL, run quest DDL and seed (leave_the_tutorial),…, Create quest_definitions, quest_instances, quest_offers tables and indexes., Insert leave_the_tutorial quest definition and room offer (idempotent)., _run_quest_ddl(), _seed_leave_the_tutorial()

### Community 1199 - "migrate_file"
Cohesion: 0.36
Nodes (7): main(), migrate_file(), MigrationResult, NamedTuple, Path, Result of a file migration., Migrate a single file to use async persistence patterns. Args: file_path: Path…

### Community 1200 - "generate_sql.mjs"
Cohesion: 0.25
Nodes (8): PostgreSQL DDL Initialization, AJV JSON Schema Validation, Canonical DML Merge (mythos_*_dml.sql), generate_sql.mjs, Static Data SQL Generation, Deterministic UUID v5 Namespace, world_and_emotes_generated.sql, generate_sql.mjs Path Resolution Failure

### Community 1201 - "Common Mistakes and How to Fix Them"
Cohesion: 0.33
Nodes (6): Common Mistakes and How to Fix Them, Mistake 1: Forgetting to Update Imports, Mistake 2: Using Deprecated Context Parameter, Mistake 3: String Formatting in Log Messages, Mistake 4: Missing Context in Error Logs, Mistake 5: Wrong Log Levels

### Community 1202 - "validate.mjs"
Cohesion: 0.32
Nodes (7): ajv, __dirname, __filename, loadJson(), main(), root, validateFile()

### Community 1203 - "calculate_notification_times"
Cohesion: 0.25
Nodes (8): calculate_notification_times(), Calculate notification times for countdown. Notifications occur: - Every 10…, Test calculate_notification_times() for short countdown., Test calculate_notification_times() for long countdown., Test calculate_notification_times() returns sorted descending., test_calculate_notification_times_long(), test_calculate_notification_times_short(), test_calculate_notification_times_sorted()

### Community 1204 - "Log Levels and Usage"
Cohesion: 0.33
Nodes (6): CRITICAL, DEBUG, ERROR, INFO, Log Levels and Usage, WARNING

### Community 1205 - "AuthRateLimitMiddleware"
Cohesion: 0.25
Nodes (6): AuthRateLimitMiddleware, ASGIApp, Receive, Scope, Send, Pure ASGI middleware; HTTP POST login/register only.

### Community 1206 - "UnknownChannelStrategy"
Cohesion: 0.25
Nodes (6): Strategy for unknown channel types., Initialize unknown channel strategy. Args: channel_type: Unknown channel type, Get strategy for channel type. Args: channel_type: Type of channel to get…, UnknownChannelStrategy, Test ChannelBroadcastingStrategyFactory.get_strategy() returns…, test_channel_broadcasting_strategy_factory_get_strategy_unknown()

### Community 1207 - "mock_zone_config"
Cohesion: 0.29
Nodes (7): mock_npc_definition(), mock_population_stats(), mock_zone_config(), fixture, Create a mock NPC definition., Create a mock zone configuration., Create mock population statistics.

### Community 1208 - "CorruptionTier"
Cohesion: 0.11
Nodes (37): compute_tier(), CorruptionTier, StrEnum, Corruption bands over 0..100. `PURE` is reserved for exactly 0 (#815) --…, Derive a corruption tier from the raw stat value. Pure function, no I/O. Unlike…, _apply_corruption_badge(), _apply_grace_badges(), format_occupant_display_name() (+29 more)

### Community 1209 - "test_websocket_handler_json_error.py"
Cohesion: 0.25
Nodes (7): mock_websocket(), asyncio, fixture, Unit tests for websocket handler JSON error handling. Tests the JSON decode…, Create a mock WebSocket., Test _handle_json_decode_error() sends error response., test_handle_json_decode_error()

### Community 1210 - "test_run_make_stages.py"
Cohesion: 0.39
Nodes (6): _load_module(), Tests for scripts/run_make_stages.py fail-fast helpers., test_keep_going_requested(), test_stage_failed_from_output_nonzero(), test_stage_failed_from_output_ok(), test_stage_failed_from_output_traceback()

### Community 1211 - "Common Patterns"
Cohesion: 0.33
Nodes (6): API Requests, Common Patterns, Database Operations, Errors with Context, Performance Monitoring, User Actions

### Community 1212 - "optimized_validate_command_content"
Cohesion: 0.25
Nodes (8): Test validating empty command content., Test validating valid command content., Test validating command content with injection pattern., test_optimized_validate_command_content_empty(), test_optimized_validate_command_content_injection(), test_optimized_validate_command_content_valid(), optimized_validate_command_content(), Optimized validation for command content fields. Args: value: The command…

### Community 1213 - "optimized_validate_reason_content"
Cohesion: 0.25
Nodes (8): Test validating empty reason content., Test validating valid reason content., Test validating reason content with injection pattern., test_optimized_validate_reason_content_empty(), test_optimized_validate_reason_content_injection(), test_optimized_validate_reason_content_valid(), optimized_validate_reason_content(), Optimized validation for reason content fields. Args: value: The reason to…

### Community 1214 - "optimized_validate_pose_content"
Cohesion: 0.25
Nodes (8): Test validating empty pose content., Test validating valid pose content., Test validating pose content with injection pattern., test_optimized_validate_pose_content_empty(), test_optimized_validate_pose_content_injection(), test_optimized_validate_pose_content_valid(), optimized_validate_pose_content(), Optimized validation for pose content fields. Args: value: The pose to validate…

### Community 1215 - "optimized_validate_filter_name"
Cohesion: 0.25
Nodes (8): Test validating empty filter name., Test validating valid filter name., Test validating invalid filter name., test_optimized_validate_filter_name_empty(), test_optimized_validate_filter_name_invalid(), test_optimized_validate_filter_name_valid(), optimized_validate_filter_name(), Optimized validation for filter name fields. Args: value: The filter name to…

### Community 1216 - "optimized_validate_help_topic"
Cohesion: 0.25
Nodes (8): Test validating empty help topic., Test validating valid help topic., Test validating invalid help topic., test_optimized_validate_help_topic_empty(), test_optimized_validate_help_topic_invalid(), test_optimized_validate_help_topic_valid(), optimized_validate_help_topic(), Optimized validation for help topic fields. Args: value: The help topic to…

### Community 1217 - "optimized_comprehensive_sanitize_input"
Cohesion: 0.25
Nodes (8): Test comprehensive sanitization of empty string., Test comprehensive sanitization of normal text., Test that optimized comprehensive sanitization normalizes newlines to spaces., test_optimized_comprehensive_sanitize_input_empty(), test_optimized_comprehensive_sanitize_input_normal(), test_optimized_comprehensive_sanitize_input_normalizes_newlines(), optimized_comprehensive_sanitize_input(), Optimized comprehensive input sanitization. Args: text: Raw input text to…

### Community 1218 - "ADR-001: Layered Architecture with Event-Driven Components"
Cohesion: 0.29
Nodes (7): ADR-001: Layered Architecture with Event-Driven Components, ADR-002: ApplicationContainer for Dependency Injection, ADR-003: Dual Event Systems (EventBus + NATS), ADR-005: Repository Pattern for Data Access, ADR-006: PostgreSQL as Primary Datastore, ADR-007: FastAPI with Async/Await, ADR-015: PostgreSQL Procedures and Functions

### Community 1219 - "container"
Cohesion: 0.33
Nodes (6): enabled, additionalProperties, description, required, type, container

### Community 1220 - "Server Management"
Cohesion: 0.29
Nodes (7): Server Management, CRITICAL SERVER MANAGEMENT RULES, Implications, MANDATORY SERVER STARTUP PROCEDURE, ONE SERVER ONLY RULE, PRE-COMMAND CHECKLIST, Server Authority (Critical)

### Community 1221 - "Test Coverage"
Cohesion: 0.29
Nodes (6): Coverage Measurement, Forbidden Test Patterns, Minimum Coverage Standard, Required Test Patterns, Test Coverage Requirements, Test Quality Standards

### Community 1222 - "Skill"
Cohesion: 0.29
Nodes (7): Automatic decision tree, Forbidden (hangs non-interactive agents), Full skill body, gh-stack (MythosMUD), Integration with other skills, Mythos defaults, One-liner status check (PowerShell)

### Community 1223 - "Skill"
Cohesion: 0.29
Nodes (6): Branching, Commit messages, Git Workflow, History hygiene, Never, Repository hygiene

### Community 1224 - "Skill"
Cohesion: 0.29
Nodes (7): ADR Authoring Skill, Index Update, Location, MythosMUD ADR Authoring, Reference, Structure, Template

### Community 1225 - "Skill"
Cohesion: 0.29
Nodes (7): Logging Standards Skill, Import, MythosMUD Logging Standards, Optional Helpers, Reference, Structured Logging, Summary

### Community 1226 - "Skill"
Cohesion: 0.29
Nodes (7): Server Runbook Skill, Commands, Critical Rules, MythosMUD Server Runbook, ONE SERVER ONLY RULE, Pre-Start Checklist, Reference

### Community 1227 - "Skill"
Cohesion: 0.29
Nodes (7): MythosMUD Test Writing Skill, Coverage, How to Run Tests, MythosMUD Test Writing, Reference, Rules, Where Tests Live

### Community 1228 - "Readme"
Cohesion: 0.33
Nodes (7): Playwright E2E Runtime Tests, E2E Tests Playwright, Runtime Auth Isolation, Playwright storageState Session Sharing, E2E Login Timeout Issue, authenticatedTest Fixture, E2E Timeout Analysis and Fixes

### Community 1229 - "useGridLayout.ts"
Cohesion: 0.33
Nodes (5): layoutConfig, PanelState, STORAGE_KEYS, useGridLayout(), UseGridLayoutReturn

### Community 1230 - "CatalogPage.tsx"
Cohesion: 0.06
Nodes (27): AppRouter(), CatalogPage, DialogueEditorPage, MapPage, buildCatalogUrl(), CatalogAdminItem, CatalogFilterFormProps, CatalogItem (+19 more)

### Community 1231 - "Wireframe"
Cohesion: 0.29
Nodes (7): Character Info Panel, Chat History Panel, Command History and Input, Game Info Panel, Location Room Description Occupants, Three-Column Game UI Layout, MythosMUD Client UI Wireframe

### Community 1232 - "Corrections Corpus Gap"
Cohesion: 0.29
Nodes (7): Corrections · `docs/subsystems/` was missing from the corpus, `docs/subsystems/` — 15 documents, 2,497 lines, FINDING SHARPENED — the ADR-009 collision is real and now better characterised, FINDINGS WITHDRAWN, Open decision, The headline finding is REINFORCED, not weakened, What happened

### Community 1233 - "Critical Websocket Auth"
Cohesion: 0.29
Nodes (7): AGENT-REPORTED, NOT YET VERIFIED BY ME — `/ws/{player_id}`, CRITICAL · WebSocket authentication bypass on `/ws`, Documentation status, Issue #472 status, Recommended fix — one guard, not three, VERIFIED — anonymous WebSocket connection via query parameter, VERIFIED — CSRF validation fails open

### Community 1234 - "Index"
Cohesion: 0.29
Nodes (7): Correction · the "back-dated ADRs" evidence was wrong, Design ↔ Implementation Drift Audit, Headline finding · the design record was largely built from the code, Notes, P8 progress, Rulings — all 8 complete, Scope boundary

### Community 1235 - "P0 Known Deviations"
Cohesion: 0.29
Nodes (7): ACCEPTED — do not re-report as new, Contradiction found in prior work, Corroboration of the P2 provenance finding, Deferred / residual (open by admission), P0 · Previously-Known Deviations, PLANNED-NOT-DONE — highest-value rows, REMEDIATED — expect CONFORMS; a deviation here is a regression

### Community 1236 - "holidays"
Cohesion: 0.33
Nodes (6): items, minItems, type, $ref, properties, holidays

### Community 1237 - "schedules"
Cohesion: 0.33
Nodes (6): $ref, properties, schedules, items, minItems, type

### Community 1238 - "Chat Panel Separation Documentation"
Cohesion: 0.29
Nodes (7): Chat Message Type Categorization Bug, Chat Panel, Commands Panel, Game Log Panel, Chat Message Routing Bug Fix, Room Description Routing Bug Fix, Bug Prevention Testing Strategy

### Community 1239 - "Aggro Threat Implementation Plan"
Cohesion: 0.29
Nodes (6): Aggro and Threat System Implementation Plan, Constants (locked), Integration with NPC static data (behavior_config / npc_type), Key Modules and Files, References, Status

### Community 1240 - "Async Audit 2025 12 03"
Cohesion: 0.29
Nodes (7): 1. Excellent Error Boundary Implementation, 2. Proper Use of asyncio.gather with return_exceptions=True, 3. Task Tracking and Lifecycle Management, 4. Good Connection State Management, 5. Proper Async Context Managers, 6. Enhanced Structured Logging, ✅ POSITIVE FINDINGS

### Community 1241 - "Async Audit 2025 12 03"
Cohesion: 0.29
Nodes (7): 1. Synchronous Blocking Operations in Async Context (CONFIRMED PERFORMANCE ISSUE), 2. asyncio.run() Called from Existing Event Loop Context, 3. Connection Pool Resource Leak Risk, 4. Missing Exception Handling in Pool Creation, 5. Blocking Operations in NATS Message Handlers, 6. F-String Logging Destroying Structured Logging, 🔴 CRITICAL ISSUES

### Community 1242 - "Python Coverage Status"
Cohesion: 0.33
Nodes (7): Coverage Improvement Summary, bcrypt PyO3 Reimport Limitation, Easy Coverage Wins, Realtime Small-File Coverage Sweep, Python Code Coverage Status, analyze_coverage_gaps.py, 70% Coverage Threshold

### Community 1243 - "Linting Pylint Unique Findings"
Cohesion: 0.29
Nodes (7): 1.1 Missing Module Docstrings (C0114), 1.2 Invalid Name (C0103), 1.3 Too Many Lines in Module (C0302), 1.4 Use Implicit Booleaness (C1805, C1804), 1.5 Singleton Comparison (C0121), 1.6 Missing Function Docstring (C0116), 1. CONVENTION Findings (260 findings)

### Community 1244 - "Nats Anti Patterns Review 2026"
Cohesion: 0.33
Nodes (7): NATS Anti-Patterns Review 2026-01-13, NATS Inconsistent Error Handling, NATSService, Blocking Operations in Message Handlers, NATS Exception Hierarchy, NATS Medium-Priority Remediation, NATS Batch Flush Recovery

### Community 1245 - "Persistence Async Migration Plan"
Cohesion: 0.29
Nodes (7): Migration Workflow (Per File), Step 1: Pre-Migration Assessment, Step 2: Create Async Repository Instances, Step 3: Convert Methods to Async, Step 4: Update All Callers, Step 5: Test Migration, Step 6: Validate Performance

### Community 1246 - "Persistence Extraction Complete"
Cohesion: 0.29
Nodes (7): Group 1: Player Operations (~800 lines → ~80 lines), Group 2: Health & XP Operations (~400 lines → ~40 lines), Group 3: Container Operations (~300 lines → ~30 lines), Group 4: Item Operations (~200 lines → ~20 lines), Group 5: Profession Operations (~100 lines → ~20 lines), Group 6: Room Operations (~100 lines → ~20 lines), Methods Extracted

### Community 1247 - "Planning Users Db"
Cohesion: 0.29
Nodes (7): Argon2 Password Hashing, FastAPI Users Migration, Invite System, Secure Path Validation, Security Implementation, Client XSS Protection, SSE Authentication System

### Community 1248 - "Test Suite Quality Audit Report"
Cohesion: 0.15
Nodes (12): 3.1 Scoring Criteria Matrix, 3.2 Category Scores, 3.3 Value Distribution Calculation, 🔴 CRITICAL VALUE TESTS (Score ≥75): **1,272 tests (25.6%)**, Executive Summary, 🟡 IMPORTANT (Medium-Value):**~2,500-3,000 tests (50-60%) —**~15-18 minutes, 🟡 IMPORTANT VALUE TESTS (Score 50-74): **2,943 tests (59.3%)**, Key Findings (+4 more)

### Community 1249 - "Attack Command Not Starting Combat"
Cohesion: 0.29
Nodes (7): Attack Command Not Starting Combat, CommandType Enum vs String Comparison, Target Resolution via Lifecycle Manager, NPC Dual Tracking System Issue, Stale Room.get_npcs After Persistence Reload, NPC Spawning vs Occupants Display Issue, Flattened Occupants Losing Player NPC Distinction

### Community 1250 - "Second NPC Combat And Linkdead Findings"
Cohesion: 0.29
Nodes (7): Coroutine Object Has No current_room_id, Combat Start Missing Await get_player_by_name, get_player_by_id vs async_get_player Mismatch, XP Award async_get_player Missing Method, Linkdead WebSocket Grace Period, Second NPC Combat And Linkdead Findings, Stale Queued Attack Target Validation

### Community 1251 - "Multi-Word Spell Name Parsing Failure"
Cohesion: 0.29
Nodes (7): Missing cast spell spells Pydantic Models, Spell Slash Commands Missing From Validation, create_cast_command First-Word-Only Parse, Multi-Word Spell Name Parsing Failure, Missing async_heal_player Method, record_spell_cast Cross-Session Object Use, Heal Spell SQLAlchemy Session Boundary Error

### Community 1252 - "main"
Cohesion: 0.38
Nodes (6): generate_html_visualization(), load_room_data(), main(), Load all room and intersection data from the zone directory., Main function to generate the HTML visualization., Generate an HTML visualization of the room network.

### Community 1253 - "intersection_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1254 - "Server Realtime Module"
Cohesion: 0.38
Nodes (7): FastAPI, ConnectionManager, Message Validator, NATS Message Handler, Server Realtime Module, Room Broadcasts, WebSocket API /api/ws

### Community 1255 - "room_schema.json"
Cohesion: 0.33
Nodes (5): additionalProperties, description, $schema, title, type

### Community 1256 - "🔍 Anti-Pattern Check"
Cohesion: 0.33
Nodes (6): 🔍 Anti-Pattern Check, ❌ Blocking Calls in Async Functions?, ❌ Ignoring Exceptions?, ❌ Long-Running Coroutines?, ❌ Missing `await` Keywords?, ❌ Unstructured Concurrency?

### Community 1257 - "Models Package Design"
Cohesion: 0.18
Nodes (11): 1. Overview, 2. Members, 3. Boundary contract, 4. Key design decisions, 5. Constraints, 6. Developer guide, 7. Troubleshooting, 8. Related docs (+3 more)

### Community 1258 - "_ensure_connection_manager"
Cohesion: 0.22
Nodes (11): _app_state_from_request(), _ensure_connection_manager(), get_player_connections(), get, Request, Read Starlette app.state without treating Request.app as Any., Ensure connection manager is available. Raises LoggedHTTPException with proper…, Get connection information for a player. Returns detailed connection metadata… (+3 more)

### Community 1259 - ".create_supervised_task"
Cohesion: 0.47
Nodes (4): Any, Task, Create a task with enhanced supervision for legacy cleanup scenarios. Args:…, Create a managed asyncio.Task with mandatory lifecycle tracking. Args: coro:…

### Community 1260 - "_AsyncPersistenceRoomFacadeBase"
Cohesion: 0.40
Nodes (4): _AsyncPersistenceRoomFacadeBase, Attrs provided by AsyncPersistenceLayer when mixed in., Ensure room cache is loaded (lazy loading with lock)., Load rooms from PostgreSQL via RoomCacheLoader.

### Community 1261 - "broadcast_shutdown_notification"
Cohesion: 0.33
Nodes (6): broadcast_shutdown_notification(), Broadcast shutdown notification to all players. Args: connection_manager:…, Test broadcast_shutdown_notification() successfully broadcasts., Test broadcast_shutdown_notification() handles errors., test_broadcast_shutdown_notification_failure(), test_broadcast_shutdown_notification_success()

### Community 1262 - "Thinking about stack structure"
Cohesion: 0.33
Nodes (6): Branch naming, Dependency chain, One stack, one story, Staging changes deliberately, Thinking about stack structure, When to create a new branch

### Community 1263 - ".claude/CLAUDE.md"
Cohesion: 0.33
Nodes (4): Chaosium Ingest Pipeline, MythosMUD — Claude pointer, basedpyright: no Any, MythosMUD LLM Wiki (Obsidian)

### Community 1264 - "Extract Skill"
Cohesion: 0.33
Nodes (6): Extract Skill, Discover, Document, Extract & Enrich, Migrate, Plan Extraction

### Community 1265 - "MythosMUD Server Test Suite"
Cohesion: 0.33
Nodes (6): Command Tests Relocated, server/tests/unit/commands/, Integration Test Tier, make test-server, MythosMUD Server Test Suite, Unit Test Tier

### Community 1266 - "Common Test Failure Categories"
Cohesion: 0.33
Nodes (6): 1. Database Test Failures, 2. Authentication Test Failures, 3. WebSocket Test Failures, 4. Game Logic Test Failures, 5. Integration Test Failures, Common Test Failure Categories

### Community 1267 - "P3 · Findings Verified Directly"
Cohesion: 0.33
Nodes (6): F-D3 · Inbound links to archived documents — DEVIATED (7 instances, one root cause), F-D5 · The DI system's architecture doc is archived, not live — DEVIATED, F-D6 · `docs/DEVELOPMENT_AI.md` is not valid text — DEVIATED, F-V1 · Sync PersistenceLayer removal — CONFORMS (reverses a P0 row), F-V2 · sqlite3 imports survive in migration scripts — STALE, P3 · Findings Verified Directly

### Community 1268 - "P8 · Action plan"
Cohesion: 0.33
Nodes (6): Documentation edits, Issues to reopen — **C7**, New ADRs (next free numbers, index updated in `decisions/README.md`), P8 · Action plan, Remediation plans to draft (not execute), Verification before closing P8

### Community 1271 - "._compute_player_context"
Cohesion: 0.33
Nodes (3): Debug log for context enrichment (best-effort, must not fail)., Populate player_in_range, enemy_nearby, and target_id for attack rules. Uses…, Get player_in_range, enemy_nearby, and target_id from persistence. Returns…

### Community 1272 - "2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage"
Cohesion: 0.33
Nodes (6): 2.1 `asyncio.sleep()` Usage, 2.2 `asyncio.Lock()` Usage, 2.3 `asyncio.Event()` Usage, 2.4 `asyncio.Queue()` Usage, 2.5 `asyncio.wait_for()` Usage, 2. Primitive Anti-Patterns: Direct `asyncio` Primitive Usage

### Community 1273 - "📚 Documentation Created"
Cohesion: 0.33
Nodes (6): 1. Comprehensive Audit Report, 2. Executive Summary, 3. Developer Quick Reference, 4. Migration Tracker, 5. Test Suite, 📚 Documentation Created

### Community 1274 - "Implementation Details"
Cohesion: 0.33
Nodes (6): CircuitBreaker Manager, Database Operations, Enhanced CircuitBreaker Class, Implementation Details, Integration Examples, NATS Operations

### Community 1275 - "Core Logging Principles"
Cohesion: 0.33
Nodes (6): 1. **Structured Logging**, 2. **Context is Everything**, 3. **Security First**, 4. **Performance Aware**, 5. **Actionable Information**, Core Logging Principles

### Community 1276 - "Performance Logging"
Cohesion: 0.33
Nodes (6): API Request Logging, Basic Logging, Database Query Logging, Error Logging with Context, Performance Logging, Structured Logging Patterns

### Community 1277 - "Enhanced Logging Features"
Cohesion: 0.33
Nodes (6): Correlation IDs, Enhanced Logging Features, Exception Tracking, MDC (Mapped Diagnostic Context), Performance Monitoring, Security Sanitization

### Community 1278 - "Enhanced Logging Migration Report"
Cohesion: 0.33
Nodes (5): Enhanced Logging Features, Enhanced Logging Migration Report, Next Steps, Successfully Updated Files, Summary

### Community 1279 - "Completed Fixes ✅"
Cohesion: 0.33
Nodes (6): 1. Fixed Synchronous Operation in WebSocket Helpers, 2. Standardized Error Handling, 3. Added Message Validation to NATSMessageBroker, 4. Improved Batch Flush Error Recovery, 5. Improved Connection Pool Error Handling, Completed Fixes ✅

### Community 1280 - "NPC Startup Duplication Analysis"
Cohesion: 0.33
Nodes (6): NPC Duplication Bug Fix Plan, NPC Population Field Rename, NPC Lifecycle Manager, NPC Population Controller, NPC Startup Duplication Analysis, NPC Startup Service

### Community 1281 - "✨ Key Achievements"
Cohesion: 0.33
Nodes (6): 1. Modular Architecture, 2. Async Foundation, 3. Zero Breaking Changes, 4. Comprehensive Documentation, 5. Quality Maintained, ✨ Key Achievements

### Community 1282 - "PostgreSQL Procedures Migration - Audit Spreadsheet"
Cohesion: 0.33
Nodes (5): Audit Table, Domain Grouping Summary, Existing PostgreSQL Functions (Already in DDL), PostgreSQL Procedures Migration - Audit Spreadsheet, Scope

### Community 1283 - "Real-Time Communication (WebSocket)"
Cohesion: 0.33
Nodes (5): Authentication and Token in URL, Connection Grace Periods, Deprecated Endpoints, Production: HTTPS and WSS, Real-Time Communication (WebSocket)

### Community 1284 - "Test Suite Analysis"
Cohesion: 0.33
Nodes (6): Current Test Organization, Dependency Access Patterns, Pattern 1: Direct app.state Access (Broken - 445 instances), Pattern 2: Using Real Lifespan (Works - Limited), Pattern 3: Fixture-Based Mocking (Mixed), Test Suite Analysis

### Community 1285 - "Modern Testing Patterns"
Cohesion: 0.33
Nodes (6): Modern Testing Patterns, Pattern 1: Container-Based Fixtures, Pattern 2: Mock Container for Unit Tests, Pattern 3: Parametrized Integration Tests, Pattern 4: Fixture Factories, Pattern 5: Async Test Context Managers

### Community 1286 - "Test Modernization Checklist"
Cohesion: 0.33
Nodes (6): Phase 0: Foundation, Phase 1: Fix Failures, Phase 2: Modernize Units, Phase 3: Pattern Updates, Phase 4: New Coverage, Test Modernization Checklist

### Community 1287 - "Phase 5: Strategic Additions (Week 5)"
Cohesion: 0.33
Nodes (6): Phase 5: Strategic Additions (Week 5), Task 5.1: Add MessageBroker Integration Tests (3 hours), Task 5.2: Add ApplicationContainer Lifecycle Tests (2 hours), Task 5.3: Add Database Migration Tests (3 hours), Task 5.4: Add WebSocket Edge Case Tests (4 hours), Task 5.5: Add Error Recovery Tests (3 hours)

### Community 1288 - "Whisper Channel System"
Cohesion: 0.40
Nodes (6): Scenario 13 Whisper Basic, Scenario 14 Whisper Errors, Scenario 16 Whisper Movement, Scenario 18 Whisper Logging, Whisper Moderation Logging, Whisper Channel System

### Community 1289 - "NPC Occupants Verification Summary"
Cohesion: 0.33
Nodes (6): NPC Display Final Fixes, room_update Overwriting NPC Data, asyncpg UUID replace AttributeError, Legacy Occupants Snapshot Format, NPC Occupants Verification Summary, Rooms API User Object AttributeError

### Community 1290 - "Combat Client Crash"
Cohesion: 0.33
Nodes (6): event_data vs data Field Name Mismatch, NATS Event Message Field Mismatch, Combat Client Crash, CombatMessaging Connection Manager Init Failure, Combat Disconnect At NPC Death, Passive Lucidity Flux Performance Degradation

### Community 1291 - "Respawn Death Screen Loop Limbo ID Mismatch"
Cohesion: 0.33
Nodes (6): limbo_death_void vs limbo_death_void_limbo_death_void, Respawn Death Screen Loop Limbo ID Mismatch, SQLAlchemy JSONB Mutation Detection, Respawn Persistence JSONB Mutation Failure, Death Threshold and Posture Bugs, HP -10 Limbo Transition Delay

### Community 1292 - "NPC Combat Start Race Condition"
Cohesion: 0.33
Nodes (6): NPC Combat Start Race Condition, Redundant NPC Instance Lookup Failure, NPCs Incorrectly Marked is_alive False, December 3 Final Investigation Summary, Character Info Panel Missing Stats Field, Room Occupants Duplicates and Missing Player

### Community 1293 - "mark_player_seen_impl"
Cohesion: 0.33
Nodes (5): mark_player_seen_impl(), Update last-seen timestamp for a player and all their connections., Update last-seen timestamp for a player and all their connections., Test mark_player_seen_impl() marks player as seen., test_mark_player_seen_impl()

### Community 1294 - "Round-Based Combat"
Cohesion: 0.33
Nodes (6): Combat Action Queue, Combat Bugs Investigation and Fixes, Round-Based Combat, Combat Round System Refactor, First Weapon Switchblade, Flee Command and Effect

### Community 1295 - "WebSocket-Only Migration"
Cohesion: 0.33
Nodes (6): SSE Connection Removal, Unified Client Message Pipeline, Unify Client Message Handling, WebSocket Best-Practices Remediation, WebSocket-Only Architecture, WebSocket-Only Migration

### Community 1296 - ".on_enter_state"
Cohesion: 0.33
Nodes (4): Any, Called whenever state machine enters a new state. Logs state transitions for…, Get connection statistics. Returns: Dictionary with connection metrics AI: For…, State

### Community 1297 - "_get_enum_value"
Cohesion: 0.33
Nodes (6): _get_enum_value(), Safely get enum value, handling both enum instances and string values. When…, Test _get_enum_value returns value from enum instance., Test _get_enum_value returns string value unchanged., test_get_enum_value_with_enum(), test_get_enum_value_with_string()

### Community 1298 - "_run_dialogue_ddl"
Cohesion: 0.40
Nodes (5): main(), cursor, Create dialogue_definitions table if missing in the given schema., Connect via DATABASE_URL and ensure dialogue_definitions exists., _run_dialogue_ddl()

### Community 1299 - "check_file_for_logging_issues"
Cohesion: 0.47
Nodes (5): check_file_for_logging_issues(), main(), Path, Check a single file for logging consistency issues. Args: file_path: Path to…, Main function to check all service files for logging consistency.

### Community 1300 - "e2e_reset_players.py"
Cohesion: 0.47
Nodes (5): _load_default_respawn_room(), main(), Load DEFAULT_RESPAWN_ROOM from disk so analyzers do not need to resolve the…, Entry point: run E2E player reset via anyio., _reset_e2e_players()

### Community 1301 - "add_suppression_to_file"
Cohesion: 0.47
Nodes (5): add_suppression_to_file(), main(), Path, Add suppression comment to a PowerShell file if it uses Write-Host and doesn't…, Process all PowerShell scripts in the scripts directory.

### Community 1302 - "test_initiate_shutdown_countdown_success"
Cohesion: 0.40
Nodes (6): _InitiateAppStub, _InitiateStateStub, Test initiate_shutdown_countdown() successfully initiates shutdown., Test initiate_shutdown_countdown() cancels existing shutdown., test_initiate_shutdown_countdown_success(), test_initiate_shutdown_countdown_supersedes()

### Community 1303 - "3. Anti-patterns and Semantic Problems"
Cohesion: 0.40
Nodes (5): 3.1. Explicit Joins (GOOD), 3.2. `NOT IN` Avoidance, 3.3. `SELECT *` in Non-Test, Non-Migration Code, 3.4. `SELECT *` in Test and Documentation, 3. Anti-patterns and Semantic Problems

### Community 1304 - "create_error_context"
Cohesion: 0.24
Nodes (9): create_error_context(), Any, Request, Create error context from request and user. Helper function to reduce…, Unit tests for server.api.player_helpers (error context helper)., When current_user is None, context gets metadata only., When current_user is set, user_id is populated and metadata merged., test_create_error_context_with_user_sets_user_id_and_metadata() (+1 more)

### Community 1305 - "auth_rate_limit.py"
Cohesion: 0.15
Nodes (15): assert_auth_rate_limit_paths_registered(), _auth_bucket(), _canonical_ip(), _collect_post_paths(), _HasPrefix, _HasRoutes, _IncludedRouterLike, _join_route_path() (+7 more)

### Community 1306 - "User"
Cohesion: 0.01
Nodes (385): DependsParam, get_current_user(), Get current user with enhanced logging., get_connection_manager, _apply_inventory_stack_defaults(), _as_inventory_dicts(), _as_str_list(), _as_str_object_dict() (+377 more)

### Community 1307 - "damage_expr"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, damage_expr

### Community 1308 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1309 - "player_repository"
Cohesion: 0.40
Nodes (5): mock_player(), player_repository(), fixture, Create a mock player for save operations., Create a PlayerRepository instance.

### Community 1310 - "_PlayerLookupPersistence"
Cohesion: 0.22
Nodes (7): _ConnectionManagerUtilsModule, _PlayerLookupPersistence, Player, Protocol, Resolve the connection manager singleton (or optional candidate)., Minimal async persistence surface for WebSocket player resolution., _WebSocketHandlerModule

### Community 1312 - "rate_limiter"
Cohesion: 0.40
Nodes (5): mock_config(), fixture, rate_limiter(), Create a mock config with chat rate limits., Create a RateLimiter instance with mocked config.

### Community 1313 - "wearable_service"
Cohesion: 0.40
Nodes (5): mock_persistence(), fixture, Create mock persistence layer., Create WearableContainerService instance., wearable_service()

### Community 1314 - "Database"
Cohesion: 0.40
Nodes (4): CRITICAL: Which databases may be reset, Database placement (production vs test), Enforcement, PostgreSQL database names (MythosMUD)

### Community 1315 - "Skill"
Cohesion: 0.40
Nodes (5): COPPA Checklist Skill, Checklist, Implementation, MythosMUD COPPA Checklist, Reference

### Community 1317 - "Global Teardown"
Cohesion: 0.40
Nodes (3): __dirname, __filename, projectRoot

### Community 1318 - "Review"
Cohesion: 0.40
Nodes (5): AI PR Reviewer Instructions, COPPA and Security Review Mandates, Review Coverage Thresholds, player_id UUID Type Rule, Server Authority Review Rule

### Community 1319 - "Server Test Remediation"
Cohesion: 0.40
Nodes (5): 4. Common Fix Patterns, Authentication Test Patterns, Database Test Patterns, Game Logic Test Patterns, WebSocket Test Patterns

### Community 1320 - "DML Migrations"
Cohesion: 0.33
Nodes (5): Dialogue definitions (#583), DML Migrations, Historical CSV files, Item catalog (ADR-026 Phase 2), Migration files

### Community 1321 - "S. Petersen's Field Guide to Lovecraftian Horrors (source summary)"
Cohesion: 0.40
Nodes (4): External live graph, For MythosMUD design, Key extrated pages, S. Petersen's Field Guide to Lovecraftian Horrors (source summary)

### Community 1322 - "mythos_dev.npc_definitions"
Cohesion: 0.50
Nodes (5): mythos_dev.dialogue_definitions, mythos_dev.get_npc_system_statistics(), mythos_dev.npc_definitions, mythos_dev.npc_relationships, mythos_dev.npc_spawn_rules

### Community 1323 - "websocket_handler_connection.py"
Cohesion: 0.14
Nodes (16): AsyncPersistenceRoomLookup, cleanup_websocket_connection(), PlayerDisconnectService, PlayerMuteCleanup, Protocol, UUID, WebSocket, WebSocket connection lifecycle: setup, welcome, and cleanup on disconnect.… (+8 more)

### Community 1325 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1326 - "Advanced Chat Channels Specification"
Cohesion: 0.40
Nodes (5): Advanced Chat Channels Specification, Global Chat Channel, Local Chat Channel, Advanced Chat Channels Tasks, Whisper Chat Channel

### Community 1327 - "UI/UX Considerations"
Cohesion: 0.40
Nodes (5): 1. Visual Distinction, 2. Panel Positioning, 3. Responsive Design, 4. Accessibility, UI/UX Considerations

### Community 1328 - "3. Simplified CommandPanel"
Cohesion: 0.40
Nodes (5): 3. Simplified CommandPanel, CommandPanel Layout Structure, Features to Keep, Features to Remove, Simplified CommandPanel Interface

### Community 1329 - "Implementation Phases"
Cohesion: 0.40
Nodes (5): Implementation Phases, Phase 1: Core Separation, Phase 2: Enhanced Features, Phase 3: Polish and Optimization, Phase 4: Testing and Refinement

### Community 1330 - "Magic and Spellcasting System"
Cohesion: 0.40
Nodes (5): EffectList Pattern, Effects System Reference, Magic Points MP, Magic and Spellcasting System, Spell Registry

### Community 1331 - "Implementation Plan"
Cohesion: 0.40
Nodes (5): Implementation Plan, Step 1: Update `.pylintrc` ✅, Step 2: Refactor Ruff C901 Violations, Step 3: Document the Strategy, Step 4: Verify Alignment

### Community 1332 - "Specific Actionable Recommendations"
Cohesion: 0.50
Nodes (4): Phase A: Quick Wins (1-2 hours effort), Phase B: Medium Effort (4-8 hours effort), Phase C: Strategic Enhancements (8-16 hours effort), Specific Actionable Recommendations

### Community 1333 - "Lucidity Tiers"
Cohesion: 0.60
Nodes (5): Catatonic Rescue Window, Lucidity System (LCD), Lucidity Tiers, Phantom Hostiles, Reversed Compass Directions

### Community 1334 - "Code Quality Improvements"
Cohesion: 0.40
Nodes (5): Code Quality Improvements, Documentation, Exception Handling, Monitoring, Validation

### Community 1335 - "Common Conversion Patterns"
Cohesion: 0.40
Nodes (5): Common Conversion Patterns, Pattern 1: Simple Query, Pattern 2: Batch Operations, Pattern 3: Health Operations, Pattern 4: FastAPI Dependency Injection

### Community 1336 - "Gotchas & Solutions"
Cohesion: 0.40
Nodes (5): Gotcha 1: Async Propagation, Gotcha 2: Mixing Sync and Async, Gotcha 3: Transaction Management, Gotcha 4: Testing Async Code, Gotchas & Solutions

### Community 1337 - "Four-Level Room Hierarchy"
Cohesion: 0.40
Nodes (5): Environment Classification, Four-Level Room Hierarchy, Environment Inheritance, Room Hierarchy Implementation, Hierarchical World Loader

### Community 1338 - "Phase 1: Quantitative Analysis Results"
Cohesion: 0.40
Nodes (5): 1.1 Test Distribution by Category, 1.2 Largest Test Files (Splitting/Pruning Candidates), 1.3 Infrastructure Test Analysis, Files, Phase 1: Quantitative Analysis Results

### Community 1339 - "attacks"
Cohesion: 0.50
Nodes (4): items, type, $ref, attacks

### Community 1340 - "Summary: Test Quality Metrics"
Cohesion: 0.40
Nodes (5): By removing 15% of tests, we, Current State, Optimized State (After Pruning), Summary: Test Quality Metrics, Value Proposition

### Community 1341 - "Modular E2E Test Suite"
Cohesion: 0.40
Nodes (5): Modular E2E Test Suite, MULTIPLAYER_SCENARIOS_PLAYBOOK, E2E Validation Passed, AI Context Limit 20KB, E2E Test Suite README

### Community 1342 - "Playwright MCP Scenarios"
Cohesion: 0.40
Nodes (5): Automated Playwright CLI Tests, Hybrid E2E Testing Approach, Mandatory Execution Order, Playwright MCP Scenarios, Room Occupants Fix

### Community 1343 - "Local Channel System"
Cohesion: 0.40
Nodes (5): Local Channel Sub-Zone Routing, Scenario 10 Local Channel Movement, Scenario 11 Local Channel Errors, Scenario 12 Local Channel Integration, Local Channel System

### Community 1344 - "Container Contents Synchronization Bug"
Cohesion: 0.50
Nodes (5): Container Contents Synchronization Bug, Fail-Fast Container Error Philosophy, slot_type backpack Assignment, Dual Inventory Storage Architecture, Inventory Slot Calculation Bug

### Community 1345 - "F-String Logging Violations"
Cohesion: 0.40
Nodes (5): F-String Logging Violations, Enhanced Logging Compliance Audit, F-String Logging Remediation Complete, Pre-Commit F-String Hook Gaps, AST-Based F-String Logging Detector

### Community 1346 - "Quest System Gap"
Cohesion: 0.40
Nodes (5): Quest System Gap, MUD Subsystems Gap Analysis, Player Skills and Profession Modifiers, Quest Subsystem Implementation, Quest System

### Community 1347 - "items"
Cohesion: 0.40
Nodes (5): items, type, pattern, type, bonus_tags

### Community 1348 - "determination_points"
Cohesion: 0.50
Nodes (4): description, minimum, type, determination_points

### Community 1349 - "fix_file"
Cohesion: 0.60
Nodes (4): fix_file(), main(), Path, Fix suppressions in a file. Returns: (number_fixed, list of changes)

### Community 1350 - "check_codacy_yaml"
Cohesion: 0.50
Nodes (4): check_codacy_yaml(), _content_is_valid(), Return (valid, list of reasons if invalid)., Warn if .codacy/codacy.yaml is missing or invalid; never fail the commit.

### Community 1351 - "HADS tooling (MythosMUD)"
Cohesion: 0.40
Nodes (4): HADS tooling (MythosMUD), Policy, Source pin, Usage

### Community 1352 - "max_dp"
Cohesion: 0.50
Nodes (4): description, minimum, type, max_dp

### Community 1354 - "2025_01_XX_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 1355 - "2025_11_21_convert_players_player_id_to_uuid.py"
Cohesion: 0.40
Nodes (4): downgrade(), Convert players.player_id from VARCHAR to UUID. PostgreSQL can directly cast…, Convert players.player_id from UUID back to VARCHAR. This is a downgrade path,…, upgrade()

### Community 1356 - "2025_11_25_normalize_container_schema.py"
Cohesion: 0.40
Nodes (4): downgrade(), Normalize container schema with proper relational structure., Revert to denormalized schema with items_json., upgrade()

### Community 1357 - "2025_11_25_remove_get_container_contents_json_procedure.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove deprecated stored procedure., Restore deprecated stored procedure., upgrade()

### Community 1358 - "2025_11_25_remove_items_json_column.py"
Cohesion: 0.40
Nodes (4): downgrade(), Remove items_json column from containers table., Restore items_json column (data will be empty)., upgrade()

### Community 1359 - "2025_11_26_ensure_item_instance_foreign_keys.py"
Cohesion: 0.40
Nodes (4): downgrade(), Ensure foreign key constraints exist for item_instances., This migration only ensures constraints exist - no downgrade needed., upgrade()

### Community 1360 - "2026_02_09_add_player_effects_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_effects table and indexes (ADR-019 effects system)., Drop player_effects table and indexes., upgrade()

### Community 1361 - "2026_02_18_add_player_skills_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create player_skills table if not exists (matches db/migrations/025)., Drop player_skills table., upgrade()

### Community 1362 - "2026_02_18_add_profession_modifiers_columns.py"
Cohesion: 0.40
Nodes (4): downgrade(), Add stat_modifiers and skill_modifiers columns to professions table., Remove stat_modifiers and skill_modifiers columns from professions table., upgrade()

### Community 1363 - "2026_02_19_add_quest_tables.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create quest_definitions, quest_instances, quest_offers tables., Drop quest tables (order matters for FKs)., upgrade()

### Community 1364 - "2026_02_19_seed_quest_leave_the_tutorial.py"
Cohesion: 0.40
Nodes (4): downgrade(), Insert leave_the_tutorial quest and quest_offers row., Remove seed quest and its offer., upgrade()

### Community 1365 - "2026_02_26_add_arena_zone_type.py"
Cohesion: 0.40
Nodes (4): downgrade(), Allow zone_type 'arena' in zones CHECK., Remove 'arena' from zones.zone_type CHECK (fails if arena zone exists)., upgrade()

### Community 1366 - "2026_08_20_align_room_environment_enum.py"
Cohesion: 0.40
Nodes (4): downgrade(), Fix the two one-off room rows, then widen/add the environment CHECKs., Restore the narrower zones/subzones CHECKs and drop the rooms CHECK. Does not…, upgrade()

### Community 1367 - "rename_players_to_population.py"
Cohesion: 0.40
Nodes (4): downgrade(), Rename columns from min_players/max_players to min_population/max_population., Revert column names back to min_players/max_players., upgrade()

### Community 1368 - "xp_value"
Cohesion: 0.50
Nodes (4): xp_value, description, minimum, type

### Community 1369 - ".generate_fake_npc_tell"
Cohesion: 0.22
Nodes (8): FakeNpcTellData, TypedDict, UUID, Generate a room text overlay hallucination. Args: player_id: Player UUID who…, Data describing one fake NPC tell hallucination (#714)., Data describing one room text overlay hallucination (#714)., Generate a fake NPC tell hallucination. Args: player_id: Player UUID who will…, RoomTextOverlayData

### Community 1370 - "EventHandler"
Cohesion: 0.05
Nodes (53): _as_event_data_dict(), _EventBusPublishPort, EventHandler, _npc_died_broadcast_and_bridge(), _npc_died_ids_or_warn(), _participant_key_strings(), _publish_npc_died_to_event_bus(), ConnectionManager (+45 more)

### Community 1371 - "enabled"
Cohesion: 0.50
Nodes (4): default, description, type, enabled

### Community 1372 - "._load_player_mutes_from_data"
Cohesion: 0.22
Nodes (5): Convert timestamp strings in mute_info to datetime objects., Convert UUID strings in mute_info to UUID objects., Load player mutes from JSON data into memory., Load channel mutes from JSON data into memory., Load global mutes from JSON data into memory.

### Community 1373 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1377 - "charisma"
Cohesion: 0.67
Nodes (3): minimum, type, charisma

### Community 1378 - "dexterity"
Cohesion: 0.67
Nodes (3): minimum, type, dexterity

### Community 1380 - "messaging_integration"
Cohesion: 0.40
Nodes (5): messaging_integration(), mock_connection_manager(), fixture, Create mock connection manager., Create CombatMessagingIntegration instance.

### Community 1381 - "user_manager"
Cohesion: 0.40
Nodes (5): mock_data_dir(), fixture, Create a temporary data directory., Create a UserManager instance., user_manager()

### Community 1382 - "intelligence"
Cohesion: 0.67
Nodes (3): minimum, type, intelligence

### Community 1385 - "Tiered Test Coverage Strategy"
Cohesion: 0.50
Nodes (4): Critical Code 90% Coverage, Global 70% Coverage Threshold, Tiered Test Coverage Strategy, Vitest Unit Tests

### Community 1387 - "multiplayer-browser-helpers.d.ts"
Cohesion: 0.50
Nodes (3): GameUiDiagnostics, OccupantsSnapshot, PresenceEvent

### Community 1388 - "9. Test Maintenance Best Practices"
Cohesion: 0.50
Nodes (4): 9. Test Maintenance Best Practices, Performance Considerations, Test Data Management, Test Isolation

### Community 1389 - "DML Migrations Apply Paths"
Cohesion: 0.50
Nodes (3): Agent rule, DML Migrations Apply Paths, Facts

### Community 1390 - "A Cold Fire Within (source summary)"
Cohesion: 0.50
Nodes (3): A Cold Fire Within (source summary), For MythosMUD design, Links

### Community 1391 - "Alone Against the Dark (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Dark (source summary), For MythosMUD design, Links

### Community 1392 - "Alone Against the Frost (source summary)"
Cohesion: 0.50
Nodes (3): Alone Against the Frost (source summary), For MythosMUD design, Links

### Community 1393 - "Alone against the Tide (source summary)"
Cohesion: 0.50
Nodes (3): Alone against the Tide (source summary), For MythosMUD design, Links

### Community 1394 - "Berlin - The Wicked City (source summary)"
Cohesion: 0.50
Nodes (3): Berlin - The Wicked City (source summary), For MythosMUD design, Links

### Community 1395 - "Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition - Keeper's Rulebook (source summary), For MythosMUD design, Links

### Community 1396 - "Call of Cthulhu Keeper Tips (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Keeper Tips (source summary), For MythosMUD design, Links

### Community 1397 - "Call of Cthulhu Starter Set (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Starter Set (source summary), For MythosMUD design, Links

### Community 1398 - "Call of Cthulhu_ The Coloring Book (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu_ The Coloring Book (source summary), For MythosMUD design, Links

### Community 1399 - "character_sheets (source summary)"
Cohesion: 0.50
Nodes (3): character_sheets (source summary), For MythosMUD design, Links

### Community 1400 - "Cthulhu Dark Ages - 3rd Edition (source summary)"
Cohesion: 0.50
Nodes (3): Cthulhu Dark Ages - 3rd Edition (source summary), For MythosMUD design, Links

### Community 1401 - "Doors to Darkness (source summary)"
Cohesion: 0.50
Nodes (3): Doors to Darkness (source summary), For MythosMUD design, Links

### Community 1402 - "Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Malleus Monstrorum - Cthulhu Mythos Bestiary (source summary)

### Community 1403 - "The Grand Grimoire of Cthulhu Mythos Magic (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Grand Grimoire of Cthulhu Mythos Magic (source summary)

### Community 1404 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 1405 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Non-Functional Requirements, Success Criteria, User Experience Requirements

### Community 1406 - "Risk Assessment"
Cohesion: 0.50
Nodes (4): Implementation Risks, Risk Assessment, Technical Risks, User Experience Risks

### Community 1407 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Testing Strategy, Unit Tests, User Acceptance Tests

### Community 1408 - "Core Architectural Differences"
Cohesion: 0.50
Nodes (4): 1. **Structured Concurrency**, 2. **Backend Abstraction**, 3. **API Design Philosophy**, Core Architectural Differences

### Community 1409 - "Real-World Impact for MythosMUD"
Cohesion: 0.50
Nodes (4): Current Stack Compatibility, Migration Complexity, Performance Considerations, Real-World Impact for MythosMUD

### Community 1410 - "Detailed Feature Comparison"
Cohesion: 0.50
Nodes (4): Detailed Feature Comparison, Entry Points, Primitives, Task Management

### Community 1411 - "Recommendation for MythosMUD"
Cohesion: 0.50
Nodes (4): Option 1: Full Migration (Recommended for Long-Term), Option 2: Hybrid Approach (Pragmatic), Option 3: Stay with asyncio (Status Quo), Recommendation for MythosMUD

### Community 1412 - "📚 REFERENCES AND RESOURCES"
Cohesion: 0.50
Nodes (4): Best Practice Documents, External Resources, Investigation Reports, 📚 REFERENCES AND RESOURCES

### Community 1413 - "📊 METRICS AND SUCCESS CRITERIA"
Cohesion: 0.50
Nodes (4): Code Quality Metrics, 📊 METRICS AND SUCCESS CRITERIA, Performance Metrics, Test Coverage

### Community 1414 - "🚀 DEPLOYMENT STRATEGY"
Cohesion: 0.50
Nodes (4): 🚀 DEPLOYMENT STRATEGY, Monitoring Post-Deployment, Pre-Deployment Checklist, Rollback Plan

### Community 1415 - "magic_points"
Cohesion: 0.67
Nodes (3): minimum, type, magic_points

### Community 1416 - "Phase 2: Database Layer Integration"
Cohesion: 0.50
Nodes (4): 2.1 Persistence Layer Protection, 2.2 Database Connection Protection, 2.3 Configuration, Phase 2: Database Layer Integration

### Community 1417 - "Phase 3: Real-Time Communication Protection"
Cohesion: 0.50
Nodes (4): 3.1 NATS Integration, 3.2 WebSocket Protection, 3.3 Configuration, Phase 3: Real-Time Communication Protection

### Community 1418 - "Phase 4: File System Operations"
Cohesion: 0.50
Nodes (4): 4.1 Room Loading Protection, 4.2 Player Data File Operations, 4.3 Configuration, Phase 4: File System Operations

### Community 1419 - "Phase 6: Monitoring and Observability"
Cohesion: 0.50
Nodes (4): 6.1 Metrics Collection, 6.2 Health Check Endpoints, 6.3 Logging Integration, Phase 6: Monitoring and Observability

### Community 1420 - "Future Enhancements"
Cohesion: 0.50
Nodes (4): Advanced Features, Document metadata, Future Enhancements, Integration Opportunities

### Community 1421 - "Monitoring and Alerting"
Cohesion: 0.50
Nodes (4): Alerting Rules, Health Checks, Metrics to Monitor, Monitoring and Alerting

### Community 1422 - "Success Criteria"
Cohesion: 0.50
Nodes (4): Functional Requirements, Monitoring Requirements, Performance Requirements, Success Criteria

### Community 1423 - "Testing Strategy"
Cohesion: 0.50
Nodes (4): Integration Tests, Load Tests, Testing Strategy, Unit Tests

### Community 1424 - "🔬 Lessons Learned"
Cohesion: 0.50
Nodes (4): Challenges Encountered, 🔬 Lessons Learned, Solutions Applied, What Worked Well

### Community 1425 - "🛠️ Technical Achievements"
Cohesion: 0.50
Nodes (4): Code Quality, Performance, 🛠️ Technical Achievements, Test Organization

### Community 1426 - "🚀 How to Run Remaining Tests"
Cohesion: 0.50
Nodes (4): Docker-Based Testing (Zero bcrypt Issues), 🚀 How to Run Remaining Tests, Individual Module Testing (For Debugging), Quick Start (All Tests in One Fresh Session)

### Community 1427 - "WebSocket and SSE Dual Connections"
Cohesion: 0.50
Nodes (4): Dual Connection API Reference, WebSocket and SSE Dual Connections, Dual Connection Client Guide, Dual Connection Deployment Guide

### Community 1428 - "power"
Cohesion: 0.67
Nodes (3): minimum, type, power

### Community 1429 - "MythosMUD Product Requirements"
Cohesion: 0.50
Nodes (4): Aggro System, Lucidity System, MythosMUD Product Requirements, Room-Based Combat

### Community 1430 - "Test Execution"
Cohesion: 0.50
Nodes (4): Run E2E Scenarios, Run Integration Tests, Run Unit Tests, Test Execution

### Community 1431 - "Cursor Subagents Documentation"
Cohesion: 0.50
Nodes (4): Cursor CLI Documentation, Cursor IDE Setup Guide, Cursor Subagents Documentation, Cursor Workflows Documentation

### Community 1432 - "Scenario Group Execution"
Cohesion: 0.50
Nodes (4): Scenario Group Execution, Local Channel Scenario Group (8-12), Logout Scenario Group (19-21), Whisper Channel Scenario Group (13-18)

### Community 1433 - "Main Foyer Starting Room"
Cohesion: 0.50
Nodes (4): Main Foyer Starting Room, Scenario 2 Clean Game State, Players Start in Different Rooms, Wrong Starting Room Bug

### Community 1434 - "Per-Recipient Whisper Rate Limiting"
Cohesion: 0.50
Nodes (4): Whisper System Remediation, Per-Recipient Whisper Rate Limiting, Global Whisper Rate Limit, Scenario 15 Rate Limiting Blocked

### Community 1435 - "Lucidity System Expansion Scenarios"
Cohesion: 0.67
Nodes (4): Lucidity System Expansion Scenarios, Catatonia Grounding Ritual Scenario, player_lucidity Ledger, Sanitarium Failover Escalation

### Community 1436 - "Container System"
Cohesion: 0.50
Nodes (4): Scenario 23 Multi-User Container Looting, Scenario 24 Environmental Containers, Scenario 26 Corpse Looting Grace Periods, Container System

### Community 1437 - "Scenario 32 Disconnect Grace Period"
Cohesion: 0.50
Nodes (4): Scenario 32 Disconnect Grace Period, Linkdead Zombie State, Scenario 33 Rest Command, Scenario 35 Player Combat

### Community 1438 - "Catatonic Movement Prevention Bug"
Cohesion: 0.50
Nodes (4): Catatonic Movement Prevention Bug, WebSocket Go Command Unified Handler Bypass, current_room_id VARCHAR(50) Truncation, Movement Valid Exits Rejection Bug

### Community 1439 - "Rooms List SQL ::uuid[] Parameter Conflict"
Cohesion: 0.50
Nodes (4): asyncpg Colon Cast Parameter Parsing, Rooms List SQL ::uuid[] Parameter Conflict, Minimap Explored Rooms UUID vs stable_id, Explored Room UUIDs Treated As stable_ids

### Community 1440 - "Vite Best-Practices Remediation"
Cohesion: 0.50
Nodes (4): Test Suite Improvement, Vite Best-Practices Remediation, import.meta.env (Vite), Vitest Best-Practices Remediation

### Community 1441 - "duration_hours"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, duration_hours

### Community 1443 - "test_room_write_request_schemas_reject_unknown_field"
Cohesion: 0.67
Nodes (3): parametrize, An extra field in the request body must be rejected, not silently discarded., test_room_write_request_schemas_reject_unknown_field()

### Community 1444 - "factory"
Cohesion: 0.67
Nodes (3): factory(), fixture, Create a CommandFactory instance.

### Community 1445 - "quality_fragmentation_graph.py"
Cohesion: 0.42
Nodes (8): build_call_graph(), collect_python_defs_and_calls(), compute_python_cross_file_depth(), max_path_length(), _named_calls(), Module, Path, _top_level_definitions()

### Community 1446 - "Shared JSON schemas"
Cohesion: 0.50
Nodes (4): alias_schema.json, emote_schema.json, Shared JSON schemas, unified_room_schema.json

### Community 1447 - "apply_migration"
Cohesion: 0.67
Nodes (3): apply_migration(), main(), Apply migration to a single database.

### Community 1448 - "main"
Cohesion: 0.67
Nodes (3): main(), Entry point: ensure collect_n quest seed and clear instances via anyio., _reset_collect_n_quest()

### Community 1450 - "_resolved_npm"
Cohesion: 0.67
Nodes (3): main(), Return absolute path to npm (prefer npm.cmd on Windows), or None if not found., _resolved_npm()

### Community 1451 - "start_server.ps1"
Cohesion: 0.50
Nodes (4): Default Server Port 54768, start_local.ps1, start_server.ps1, stop_server.ps1

### Community 1452 - "verify_schema_match.sh script"
Cohesion: 0.83
Nodes (3): find_pg_dump(), find_pg_isready(), verify_schema_match.sh script

### Community 1453 - "verify_tutorial_migrations.ps1"
Cohesion: 0.83
Nodes (3): Test-Migration08(), Test-Migration12(), Write-ColorOutput()

### Community 1455 - "enum"
Cohesion: 0.40
Nodes (5): autumn, spring, summer, winter, enum

### Community 1456 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1457 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1458 - "item_prototype.schema.json"
Cohesion: 0.11
Nodes (17): additionalProperties, additionalProperties, type, additionalProperties, required, type, definitions, armorMetadata (+9 more)

### Community 1459 - "test_auth_utils.py"
Cohesion: 0.02
Nodes (130): AttributeError, create_access_token(), decode_access_token(), hash_password(), timedelta, Decode and validate a JWT access token., Hash a plaintext password using Argon2id. This function provides superior…, Verify a plaintext password against a hash. This function safely handles both… (+122 more)

### Community 1460 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1462 - "Client Security and Privacy Policies"
Cohesion: 0.67
Nodes (3): Client Security and Privacy Policies, DOMPurify Sanitization, WebSocket Subprotocol Auth

### Community 1463 - "MythosMUD UI Component Library"
Cohesion: 0.67
Nodes (3): Mythos Terminal Theme Tokens, StatusPanel, MythosMUD UI Component Library

### Community 1465 - "Step-by-Step Remediation Process"
Cohesion: 0.67
Nodes (3): 1. Initial Assessment, 2. Categorize Test Failures, Step-by-Step Remediation Process

### Community 1466 - "8. Error Handling and Debugging"
Cohesion: 0.67
Nodes (3): 8. Error Handling and Debugging, Common Debug Commands, Test Debugging

### Community 1497 - "Expansion Backlog (Raw)"
Cohesion: 0.67
Nodes (3): Delta Green, Expansion Backlog (Raw), Things and Notes to Expand On

### Community 1502 - "What Are They?"
Cohesion: 0.67
Nodes (3): `anyio` (Third-Party Library), `asyncio` (Python Standard Library), What Are They?

### Community 1503 - "Character Creation Revamp"
Cohesion: 0.67
Nodes (3): Character Creation Revamp, CoC-Style Skills Allocation, Skill Use Tracking and Level-Up Improvement

### Community 1504 - "Comprehensive System Audit"
Cohesion: 0.67
Nodes (3): CI/CD Enhanced Logging Validation, Comprehensive System Audit, Database Migration Guide

### Community 1505 - "Architecture Overview"
Cohesion: 0.67
Nodes (3): Architecture Overview, CircuitBreaker States, Integration Points

### Community 1506 - "Dead Code Cleanup Completion"
Cohesion: 0.67
Nodes (3): Legacy Files Cleanup Summary, Dead Code Cleanup Completion, Dead Code Cleanup Planning

### Community 1507 - "Single Session Per User"
Cohesion: 0.67
Nodes (3): force_disconnect_player, Single Session Per User, Player Spawn Protection

### Community 1508 - "🎯 Next Steps"
Cohesion: 0.67
Nodes (3): Future Enhancements, Immediate Actions, 🎯 Next Steps

### Community 1509 - "Fixture Optimization Complete"
Cohesion: 0.67
Nodes (3): E2E Testing Setup Status, Fixture Optimization Complete, Test Suite Post-Merge Refactoring

### Community 1510 - "Test Warning Remediation"
Cohesion: 0.67
Nodes (3): Early Logging Initialization, datetime.utcnow Deprecation Fix, Test Warning Remediation

### Community 1511 - "Enhanced Logging Migration Complete"
Cohesion: 0.67
Nodes (3): Enhanced Logging Implementation Complete, Enhanced Logging Implementation Summary, Enhanced Logging Migration Complete

### Community 1512 - "Random Stats Generator Planning"
Cohesion: 0.67
Nodes (3): Pydantic Click Command Validation Integration, Random Stats Generator Technical Plan, Random Stats Generator Planning

### Community 1513 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1514 - "report_any_baseline.py"
Cohesion: 0.70
Nodes (4): _group_of(), _load(), main(), _rule_of()

### Community 1516 - "Party System Reference"
Cohesion: 0.67
Nodes (3): Party Invite Command, Party System Reference, Ephemeral Grouping Party Planning

### Community 1517 - "Archive Directory README"
Cohesion: 0.67
Nodes (3): Archive Directory README, HADS Archive Exclusion, PLANNING.md Single Source of Truth

### Community 1518 - "Structured Error Logging"
Cohesion: 0.67
Nodes (3): Structured Error Logging, log_and_raise Utilities, Test/Production Environment Separation

### Community 1519 - "Test File Migration Mapping"
Cohesion: 0.67
Nodes (3): Test Suite Hierarchical Migration, Test File Migration Mapping, Test Suite Refactoring Deliverables

### Community 1520 - "Who Command Enhancement"
Cohesion: 0.67
Nodes (3): Who Command Name Filtering, Who Command Enhancement, Who Command Implementation Tasks

### Community 1521 - "10 Concurrent Players Load Test"
Cohesion: 0.67
Nodes (3): who Command Unawaited Coroutine Bug, 10 Concurrent Players Load Test, Load Test Suite

### Community 1522 - "Scenario 20 Logout Errors"
Cohesion: 0.67
Nodes (3): Scenario 19 Logout Button, Scenario 20 Logout Errors, Scenario 21 Logout Accessibility

### Community 1523 - "Scenario 34 Two Players Same Room Visibility"
Cohesion: 0.67
Nodes (3): Scenario 34 Two Players Same Room Visibility, Scenario 36 Movement Visibility, Scenario 37 Chat Message Ordering

### Community 1524 - "E2E Session Report 2025-12-02"
Cohesion: 0.67
Nodes (3): Admin Teleportation Display Bug, E2E Session Report 2025-12-02, Whisper Messages Not Received Bug

### Community 1525 - "Playwright MCP Primary Testing Tool"
Cohesion: 0.67
Nodes (3): Playwright MCP Primary Testing Tool, Standard Playwright Unsuitable for Multiplayer, Server Won't Start Troubleshooting

### Community 1526 - "Whisper NATS Subject Bug Fix"
Cohesion: 0.67
Nodes (3): chat.whisper.player Subject Segment, Whisper NATS Subject Bug Fix, Whisper Work Completed and Remaining

### Community 1527 - "CodeQL Configuration"
Cohesion: 0.67
Nodes (3): CodeQL Configuration, CodeQL Test Credential Exclusions, CodeQL Workflow

### Community 1528 - "Dependency Review Workflow"
Cohesion: 0.67
Nodes (3): Dependabot Dependency Updates, Dependency Review Workflow, UV Lock Dependency Snapshot Gate

### Community 1529 - "Impeccable design context"
Cohesion: 0.67
Nodes (3): Impeccable design context, Legibility under pressure, Dark terminal-first aesthetic

### Community 1530 - "NPCs Not Updating On Player Movement"
Cohesion: 0.67
Nodes (3): exclude_player Occupants Snapshot Pattern, NPCs Not Updating On Player Movement, Canonical Room ID NPC Matching Remediation

### Community 1531 - "Combat Messages Dual Panel Display"
Cohesion: 0.67
Nodes (3): Combat Turn Order UUID Display, Combat Messages Dual Panel Display, Missing NPC Death Message Handlers

### Community 1532 - "Test Suite Stall After Performance Comparison"
Cohesion: 0.67
Nodes (3): Docker Build mythos_unitql Typo, Test Suite Stall After Performance Comparison, thread.join Without Timeout Hang

### Community 1533 - "Client Updates System Audit"
Cohesion: 0.67
Nodes (3): Architecture Review Plan, Option C Replacement Client Updates, Client Updates System Audit

### Community 1534 - "Cursor Rules as Canonical Config"
Cohesion: 0.67
Nodes (3): Cursor-Centric AI Config, Cursor Rules as Canonical Config, GitHub Worktrees Cursor Setup

### Community 1535 - "Logging Aggregator Verification"
Cohesion: 0.67
Nodes (3): Logging Aggregator Verification, warnings.log and errors.log Aggregators, Structlog Anti-Pattern Remediation

### Community 1536 - "Memory Leak Remediation"
Cohesion: 0.67
Nodes (3): Closed WebSockets Deque Cap, Memory Leak Metrics Collection, Memory Leak Remediation

### Community 1537 - "Playwright DI Migration Validation"
Cohesion: 0.67
Nodes (3): Playwright Best-Practices Remediation, Playwright DI Migration Validation, E2E Harness Overhaul

### Community 1538 - "Server Authority Remediation"
Cohesion: 0.67
Nodes (3): game_state Room Replace (not Merge), Server Authority Remediation, Server Authority Rule

### Community 1555 - "mythos_e2e.item_instances"
Cohesion: 0.36
Nodes (8): mythos_e2e.add_item_to_container(), mythos_e2e.container_contents, mythos_e2e.containers, mythos_e2e.get_container_contents_json(), mythos_e2e.item_component_states, mythos_e2e.item_instance_exists(), mythos_e2e.item_instances, mythos_e2e.item_prototypes

### Community 1557 - "mythos_unit.item_instances"
Cohesion: 0.36
Nodes (8): mythos_unit.add_item_to_container(), mythos_unit.container_contents, mythos_unit.containers, mythos_unit.get_container_contents_json(), mythos_unit.item_component_states, mythos_unit.item_instance_exists(), mythos_unit.item_instances, mythos_unit.item_prototypes

### Community 1558 - "normalize_path_from_url_or_path"
Cohesion: 0.25
Nodes (6): Path, Return and cache the repository root directory., Delegate to shared util. Kept for backward compatibility., normalize_path_from_url_or_path(), Path, Normalize an item database override into a filesystem path. DEPRECATED: Items…

### Community 1560 - "description"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, description

### Community 1561 - "name"
Cohesion: 0.40
Nodes (5): description, maxLength, minLength, type, name

### Community 1562 - "weather_patterns"
Cohesion: 0.40
Nodes (5): type, weather_patterns, description, items, type

### Community 1563 - "7. Common Test Failure Solutions"
Cohesion: 0.50
Nodes (4): 7. Common Test Failure Solutions, Authentication Test Issues, Database Connection Issues, WebSocket Test Issues

### Community 1564 - "10. Grace Period Persistence"
Cohesion: 0.50
Nodes (4): 10. Grace Period Persistence, Gap Analysis, Industry Practices, Our Plan

### Community 1565 - "1. Disconnect Grace Period Duration"
Cohesion: 0.50
Nodes (4): 1. Disconnect Grace Period Duration, Gap Analysis, Industry Practices, Our Plan

### Community 1566 - "2. Auto-Attack During Grace Period"
Cohesion: 0.50
Nodes (4): 2. Auto-Attack During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 1661 - "3. Grace Period Visibility & Messaging"
Cohesion: 0.50
Nodes (4): 3. Grace Period Visibility & Messaging, Gap Analysis, Industry Practices, Our Plan

### Community 1662 - "4. Rest/Quit Command During Combat"
Cohesion: 0.50
Nodes (4): 4. Rest/Quit Command During Combat, Gap Analysis, Industry Practices, Our Plan

### Community 1663 - "5. Rest Command Countdown Duration"
Cohesion: 0.50
Nodes (4): 5. Rest Command Countdown Duration, Gap Analysis, Industry Practices, Our Plan

### Community 1666 - "6. Rest Location (Inn/Hotel) Behavior"
Cohesion: 0.50
Nodes (4): 6. Rest Location (Inn/Hotel) Behavior, Gap Analysis, Industry Practices, Our Plan

### Community 1667 - "7. Reconnection During Grace Period"
Cohesion: 0.50
Nodes (4): 7. Reconnection During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 1668 - "8. Grace Period After Intentional Disconnect"
Cohesion: 0.50
Nodes (4): 8. Grace Period After Intentional Disconnect, Gap Analysis, Industry Practices, Our Plan

### Community 1675 - "9. Command Blocking During Grace Period"
Cohesion: 0.50
Nodes (4): 9. Command Blocking During Grace Period, Gap Analysis, Industry Practices, Our Plan

### Community 1679 - "Recommendations Summary"
Cohesion: 0.50
Nodes (4): High Priority Decisions, Low Priority (Future Considerations), Medium Priority Enhancements, Recommendations Summary

### Community 1680 - "Call of Cthulhu 7th Edition Keeper Screen Pack (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu 7th Edition Keeper Screen Pack (source summary), For MythosMUD design, Links

### Community 1681 - "Call of Cthulhu Investigator Handbook 7th Edition (source summary)"
Cohesion: 0.50
Nodes (3): Call of Cthulhu Investigator Handbook 7th Edition (source summary), For MythosMUD design, Links

### Community 1690 - "Dead Light and Other Dark Turns (source summary)"
Cohesion: 0.50
Nodes (3): Dead Light and Other Dark Turns (source summary), For MythosMUD design, Links

### Community 1692 - "Down Darker Trails (source summary)"
Cohesion: 0.50
Nodes (3): Down Darker Trails (source summary), For MythosMUD design, Links

### Community 1698 - "Gateways to Terror (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Gateways to Terror (source summary), Links

### Community 1704 - "Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, Mansions of Madness_ Vol 1 - Behind Closed Doors (source summary)

### Community 1706 - "Nameless Horrors - 2nd Edition (source summary)"
Cohesion: 0.50
Nodes (4): External live graph, For MythosMUD design, Key extractions pages, Nameless Horrors - 2nd Edition (source summary)

### Community 1709 - "The Malleus Monstrorum Keeper Deck (source summary)"
Cohesion: 0.50
Nodes (3): For MythosMUD design, Links, The Malleus Monstrorum Keeper Deck (source summary)

### Community 1710 - "corruption_adjustment_log.sql"
Cohesion: 0.67
Nodes (3): corruption_adjustment_log, corruption_cooldowns, players

### Community 1712 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 1716 - "days"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, days

### Community 1717 - "effects"
Cohesion: 0.50
Nodes (4): minItems, type, uniqueItems, effects

### Community 1720 - "_ExecuteResult"
Cohesion: 0.25
Nodes (4): _ExecuteResult, _MappingsProxy, Typed stand-in for Result.mappings() so .all() is not MagicMock Any., Typed stand-in for sqlalchemy Result when only .mappings().all() is used.

### Community 1735 - "end_hour"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, end_hour

### Community 1736 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 1737 - "exits"
Cohesion: 0.50
Nodes (4): type, additionalProperties, type, exits

### Community 1739 - "Migration Considerations"
Cohesion: 0.50
Nodes (4): Backward Compatibility, Data Migration, Migration Considerations, Performance Impact

### Community 1741 - "day"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, day

### Community 1742 - "holiday"
Cohesion: 0.50
Nodes (4): $defs, holiday, additionalProperties, type

### Community 1743 - "month"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, month

### Community 1745 - "id"
Cohesion: 0.50
Nodes (4): minLength, pattern, type, id

### Community 1746 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1747 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1748 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1749 - "id"
Cohesion: 0.50
Nodes (4): description, pattern, type, id

### Community 1750 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1751 - "rest_location"
Cohesion: 0.50
Nodes (4): rest_location, default, description, type

### Community 1752 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1753 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1754 - "test_run_quality_fragmentation_guard.py"
Cohesion: 0.57
Nodes (7): _assert_utf8_replace(), _fake_result(), _load_module(), Regression test for scripts/run_quality_fragmentation_guard.py's git-output…, test_changed_files_between_passes_utf8_replace_encoding(), test_local_changed_files_passes_utf8_replace_encoding(), test_run_git_passes_utf8_replace_encoding()

### Community 1755 - "Item catalog pipeline (private `data/` submodule)"
Cohesion: 0.29
Nodes (6): Current batches, Generate (from MythosMUD repo root), Human review gate (required before DML commit), Item catalog pipeline (private `data/` submodule), Layout, Out of scope here

### Community 1756 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1757 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1758 - "_extract_bearer_token"
Cohesion: 0.29
Nodes (7): _extract_bearer_token(), _parse_subprotocol_token(), Extract bearer token from parsed subprotocol parts. If 'bearer' marker is…, Parse token from WebSocket subprotocol header. Example formats: "bearer,…, test_extract_bearer_token_empty(), test_extract_bearer_token_last_part(), test_parse_subprotocol_token()

### Community 1765 - "test_validate_secure_path_path_traversal_commonpath"
Cohesion: 0.33
Nodes (4): Test validate_secure_path normalizes backslashes., Test validate_secure_path detects path traversal via commonpath check., test_validate_secure_path_path_traversal_commonpath(), test_validate_secure_path_with_backslash()

### Community 1766 - "items"
Cohesion: 0.33
Nodes (6): items, minItems, type, additionalProperties, properties, holidays

### Community 1767 - "test_asyncio_run_guardrails.py"
Cohesion: 0.50
Nodes (3): Test that server library code does not use asyncio.run() (AnyIO best practice).…, Assert server/ has no asyncio.run() in library code (use anyio.run() at entry…, test_no_asyncio_run_in_server_library_code()

### Community 1768 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1769 - "name"
Cohesion: 0.50
Nodes (4): description, minLength, type, name

### Community 1770 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1771 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1772 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1773 - "exits"
Cohesion: 0.50
Nodes (4): additionalProperties, description, type, exits

### Community 1774 - "plane"
Cohesion: 0.50
Nodes (4): description, pattern, type, plane

### Community 1775 - "sub_zone"
Cohesion: 0.50
Nodes (4): sub_zone, description, pattern, type

### Community 1776 - "zone"
Cohesion: 0.50
Nodes (4): zone, description, pattern, type

### Community 1777 - "description"
Cohesion: 0.50
Nodes (4): description, minLength, type, description

### Community 1779 - "npc_spawn_modifier"
Cohesion: 0.50
Nodes (4): description, minimum, type, npc_spawn_modifier

### Community 1780 - "special_rules"
Cohesion: 0.50
Nodes (4): special_rules, additionalProperties, description, type

### Community 1782 - "plane"
Cohesion: 0.67
Nodes (3): minLength, type, plane

### Community 1785 - "properties"
Cohesion: 0.13
Nodes (15): $ref, $ref, $ref, additionalProperties, description, properties, type, armor (+7 more)

### Community 1818 - "mythos_e2e.npc_definitions"
Cohesion: 0.50
Nodes (5): mythos_e2e.dialogue_definitions, mythos_e2e.get_npc_system_statistics(), mythos_e2e.npc_definitions, mythos_e2e.npc_relationships, mythos_e2e.npc_spawn_rules

### Community 1821 - "mythos_unit.npc_definitions"
Cohesion: 0.50
Nodes (5): mythos_unit.dialogue_definitions, mythos_unit.get_npc_system_statistics(), mythos_unit.npc_definitions, mythos_unit.npc_relationships, mythos_unit.npc_spawn_rules

### Community 1823 - "get_alerts"
Cohesion: 0.40
Nodes (5): get_alerts(), health(), get, Health check endpoint, Get recent alerts (for testing)

### Community 1825 - "snapshot_source_pack_graphify.ps1"
Cohesion: 0.70
Nodes (4): Export-PackSnapshot(), Get-GraphCount(), Get-HonestyNote(), Get-SourcePackSlug()

### Community 1826 - "2026_09_11_add_account_sanctions_table.py"
Cohesion: 0.40
Nodes (4): downgrade(), Create account_sanctions table and its index., Drop account_sanctions table and its index., upgrade()

### Community 1828 - "_RoomPersistence"
Cohesion: 0.40
Nodes (4): Protocol, Protocol for persistence with get_room_by_id., Return the room object for the given room_id, or None if not found., _RoomPersistence

### Community 1831 - "add_used_by_user_id_column.py"
Cohesion: 0.50
Nodes (4): apply_migration(), main(), Main entry point for the migration script., Apply the migration to add used_by_user_id column. Args: database_url:…

### Community 1834 - "quest_seed_data"
Cohesion: 0.40
Nodes (5): async_sessionmaker, AsyncSession, fixture, quest_seed_data(), Create User, Player, leave_the_tutorial QuestDefinition and QuestOffer. Quest…

### Community 1839 - "health_service"
Cohesion: 0.40
Nodes (5): health_service(), mock_connection_manager(), fixture, Create a mock connection manager., Create a HealthService instance.

### Community 1840 - "_RaisesOnBool"
Cohesion: 0.40
Nodes (4): _RaisesOnBool, Test double whose truthiness check raises, to exercise the broad except path., Test check_database_health handles errors gracefully., test_check_database_health_error()

### Community 1841 - "Context Management"
Cohesion: 0.50
Nodes (4): Context Management, Request Context, System Context, User Context

### Community 1842 - "start_hour"
Cohesion: 0.50
Nodes (4): start_hour, maximum, minimum, type

### Community 1848 - "resolve_connection_manager"
Cohesion: 0.50
Nodes (4): Prefer the supplied manager; otherwise the container singleton. Static import…, resolve_connection_manager(), test_resolve_connection_manager_delegates_when_none(), test_resolve_connection_manager_returns_candidate()

### Community 1855 - "mythos_dev.quest_definitions"
Cohesion: 0.67
Nodes (3): mythos_dev.quest_definitions, mythos_dev.quest_instances, mythos_dev.quest_offers

### Community 1856 - "mythos_e2e.quest_definitions"
Cohesion: 0.67
Nodes (3): mythos_e2e.quest_definitions, mythos_e2e.quest_instances, mythos_e2e.quest_offers

### Community 1857 - "mythos_unit.quest_definitions"
Cohesion: 0.67
Nodes (3): mythos_unit.quest_definitions, mythos_unit.quest_instances, mythos_unit.quest_offers

### Community 1860 - "id"
Cohesion: 0.67
Nodes (3): minLength, type, id

### Community 1861 - "Security Considerations"
Cohesion: 0.67
Nodes (3): Data Sanitization, Security Considerations, Sensitive Data Protection

### Community 1863 - "websocket_player_id_fallback_allowed"
Cohesion: 0.67
Nodes (3): Return True only when anonymous player_id query fallback is explicitly enabled.…, websocket_player_id_fallback_allowed(), test_websocket_player_id_fallback_allowed_default_off()

### Community 1912 - "OccupantFormatter"
Cohesion: 0.14
Nodes (13): OccupantFormatter, Formats and separates occupants by type., Initialize occupant formatter., Test OccupantFormatter._process_npc_name_for_update() adds valid NPC name., Test OccupantFormatter._process_dict_occupant_for_update() processes player…, Test OccupantFormatter._process_string_occupant_for_update() adds valid string., Test OccupantFormatter.separate_occupants_by_type() processes string occupants., Test OccupantFormatter.separate_occupants_by_type() handles mixed types. (+5 more)

## Knowledge Gaps
- **6229 isolated node(s):** `wsl-bashrc-codacy.sh script`, `uvx`, `jcodemunch-mcp`, `JCODEMUNCH_MAX_FOLDER_FILES`, `@codacy/codacy-mcp` (+6224 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **534 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_logger()` connect `get_logger` to `Invite`, `zone_config_loader.py`, `Player`, `server/dependencies.py`, `get_help_content`, `ContainerData`, `server/services/__init__.py`, `Room`, `apply_stat_modifications`, `SecureBaseModel`, `test_lifespan_event_subscriptions.py`, `LoggedHTTPException`, `NPCDefinition`, `test_rescue_service.py`, `ContainerComponent`, `api/character_creation.py`, `test_combat_event_publisher.py`, `HolidayService`, `session_factory`, `MemoryMonitor`, `players.py`, `EventBus`, `get_npc_instance_service`, `RoomEventHandler`, `test_combat_monitoring_service.py`, `DatabaseManager`, `server/tests/conftest.py`, `PlayerNameExtractor`, `test_quest_instance_repository.py`, `test_communication_commands_flows.py`, `connection_manager_methods.py`, `PlayerService`, `test_container_bundles.py`, `MetricsCollector`, `test_magic_commands.py`, `extract_player_name`, `test_admin_auth_service.py`, `test_look_container.py`, `MythosTickScheduler`, `inventory_equip_command.py`, `handle_emote_command`, `test_chat_validator.py`, `CombatService`, `CombatConfiguration`, `magic_service_completion.py`, `CORSConfig`, `CombatInstance`, `test_websocket_initial_state.py`, `lucidity_migration.py`, `test_admin_commands.py`, `test_real_time_helpers.py`, `test_who_commands.py`, `test_connection_delegates.py`, `test_chat_pose_helpers.py`, `test_look_room.py`, `NATSServicePoolMixin`, `active_lucidity_service.py`, `AsciiMapRenderer`, `look_helpers.py`, `NPCOccupantProcessor`, `chat_service.py`, `system_monitoring.py`, `WebSocketMessageValidator`, `CombatParticipant`, `npc_database.py`, `test_chat_npc_system.py`, `cleanse_command.py`, `test_movement_service.py`, `maps.py`, `test_combat_service_modules.py`, `handle_teach_command`, `lifespan.py`, `server/schemas/__init__.py`, `is_player_in_login_grace_period`, `container_events.py`, `PlayerPositionService`, `rooms.py`, `connection_state_machine.py`, `test_look_player.py`, `NPCCombatIntegrationService`, `player_inventory_migration.py`, `test_combat_persistence_handler_events.py`, `IdleMovementHandler`, `connection_manager.py`, `realtime/realtime.py`, `test_aggro_threat.py`, `look_command.py`, `ApplicationContainer`, `apply_communication_dampening`, `FeatureFlagService`, `TargetType`, `test_logout_commands.py`, `get_session_maker`, `test_metrics_endpoints.py`, `test_look_npc.py`, `test_status_commands.py`, `real_time.py`, `api/monitoring.py`, `admin_teleport_commands.py`, `FollowService`, `admin_setstat_command.py`, `ChatModeration`, `MPRegenerationService`, `QuestService`, `test_go_command.py`, `test_lifecycle_periodic.py`, `TaskRegistry`, `NATSError`, `container_persistence.py`, `logging_file_setup.py`, `dialogue_definitions_api.py`, `CreateItemInstanceInput`, `catatonia_check.py`, `test_shutdown_sequence.py`, `player_presence_tracker.py`, `ContainerLockState`, `test_lucidity_command_disruption.py`, `PerformanceMonitor`, `test_admin_setlucidity_command.py`, `test_error_handling_middleware.py`, `test_lucidity_recovery_commands.py`, `test_hallucination_services.py`, `test_lucidity_event_dispatcher.py`, `CombatAuditLogger`, `test_alias_commands.py`, `build_event`, `NPCActionMessage`, `LogAggregator`, `admin_hallucinate_command.py`, `test_enhanced_logging_config.py`, `game_state_provider.py`, `inventory_command_helpers.py`, `api/game.py`, `test_player_respawn_service.py`, `lifespan_protocols.py`, `CatatoniaRegistry`, `test_email_utils.py`, `_ensure_connection_manager`, `HealthStatus`, `ExceptionTracker`, `catalog_commands.py`, `DeadLetterQueue`, `TargetMatch`, `test_admin_commands_helpers.py`, `LucidityService`, `test_container_persistence_async_helpers.py`, `test_inventory_display_helpers.py`, `websocket_handler.py`, `InstanceManager`, `PartyService`, `.state`, `NPCLifecycleManager`, `_prepare_command_for_processing`, `test_rate_overrides.py`, `send_game_event`, `combat_turn_participant_actions.py`, `User`, `map_minimap.py`, `game_tick_processing.py`, `get_cache_manager`, `websocket_handler_commands.py`, `test_occupants.py`, `handle_time_command`, `test_chat_logger.py`, `command_service.py`, `DialogueDefinitionRepository`, `test_party_commands.py`, `add_used_by_user_id_column.py`, `CoordinateValidator`, `npc_combat_grace.py`, `rescue_commands.py`, `websocket_handler_connection.py`, `test_magic_service.py`, `npc_config_parsing.py`, `AdminActionsLogger`, `websocket_helpers.py`, `connection_cleanup_methods.py`, `AliasGraph`, `handle_read_command`, `event_types.py`, `retry.py`, `debrief_command.py`, `passive_lucidity_flux/service.py`, `should_spawn_npc`, `command_guards.py`, `combat_attack.py`, `command_handler_unified.py`, `command_result_text`, `bundles/game.py`, `test_security_headers.py`, `talk_command.py`, `CircuitBreaker`, `migrate_combat_data.py`, `test_player_occupant_processor.py`, `_str_id`, `ContainerRepository`, `EventHandler`, `TargetResolutionResult`, `test_chat_nats_publisher.py`, `test_map_helpers.py`, `test_passive_corruption_flux_rate_overrides.py`, `rest_countdown_task.py`, `factory.py`, `channel_broadcasting_strategies.py`, `OccupantFormatter`, `event_publisher.py`, `optimized_security_validator.py`, `NATSSubjectManager`, `player_connection_setup.py`, `SkillRepository`, `test_container_persistence_extended_crud.py`, `test_player_requests.py`, `PlayerDPUpdated`, `npc_combat_integration_service.py`, `TrackedTaskManager`, `PrototypeRegistry`, `event_handler.py`, `PlayerDeathService`, `ItemCatalogService`, `MessageBroadcaster`, `passive_corruption_flux/service.py`, `quest_commands.py`, `PayloadOptimizer`, `ChatPoseManager`, `PeriodicOrphanAuditor`, `admin_shutdown_command.py`, `magic_healing_events.py`, `NPCStartupService`, `test_game_tick_death.py`, `ExperienceRepository`, `ConnectionErrorHandler`, `ChatChannelLoggerMixin`, `_find_item_in_equipped`, `ItemFactory`, `MovementMonitor`, `PersonalMessageSender`, `CommandRateLimiter`, `test_lifecycle_respawn.py`, `MemoryThresholdMonitor`, `load_motd`, `test_connection_establishment.py`?**
  _High betweenness centrality (0.147) - this node is a cross-community bridge._
- **Why does `ConnectionManager` connect `ConnectionManager` to `NPCCombatIntegrationService`, `websocket_handler.py`, `PartyService`, `server/dependencies.py`, `connection_manager.py`, `look_command.py`, `mark_player_seen_impl`, `PlayerDPUpdated`, `npc_combat_integration_service.py`, `player_event_handlers_respawn_room.py`, `event_handler.py`, `User`, `test_connection_room_utils.py`, `MemoryMonitor`, `websocket_handler_commands.py`, `api/monitoring.py`, `RoomEventHandler`, `FollowService`, `npc_combat_grace.py`, `websocket_handler_connection.py`, `TestEmitLootAllEvent`, `MemoryLeakMetricsCollector`, `test_container_bundles.py`, `connection_cleanup_methods.py`, `player_presence_tracker.py`, `test_websocket_initial_state.py`, `build_event`, `PlayerRespawnEventHandler`, `game_state_provider.py`, `inventory_command_helpers.py`, `api/game.py`, `EventHandler`, `combat_loader.py`, `lifespan_protocols.py`, `EventPublisher`, `DeadLetterQueue`, `container_events.py`?**
  _High betweenness centrality (0.016) - this node is a cross-community bridge._
- **Why does `DatabaseError` connect `get_logger` to `websocket_handler.py`, `test_profession_repository.py`, `Player`, `ContainerData`, `connection_manager.py`, `test_player_spell_repository.py`, `player_connection_setup.py`, `SkillRepository`, `test_container_persistence_extended_crud.py`, `get_item_catalog`, `send_game_event`, `test_item_catalog.py`, `get_session_maker`, `NPCDefinition`, `RoomCacheLoader`, `PrototypeRegistry`, `test_connection_room_utils.py`, `test_npc_service.py`, `HolidayService`, `players.py`, `ItemCatalogService`, `admin_teleport_commands.py`, `asyncio`, `admin_setstat_command.py`, `DialogueDefinitionRepository`, `DatabaseManager`, `test_go_command.py`, `test_quest_instance_repository.py`, `connection_manager_methods.py`, `asyncio`, `PlayerService`, `test_admin_summon_command.py`, `container_persistence.py`, `ExplorationService`, `test_auth_utils.py`, `CreateItemInstanceInput`, `extract_player_name`, `test_shutdown_sequence.py`, `player_presence_tracker.py`, `test_connection_session_management.py`, `retry.py`, `test_admin_setlucidity_command.py`, `PlayerEffectRepository`, `populate_test_npc_databases.py`, `ExperienceRepository`, `ConnectionCleaner`, `test_player_repository.py`, `test_admin_commands.py`, `test_async_persistence_room_loading.py`, `test_skill_use_log_repository.py`, `test_connection_delegates.py`, `NPCSpawnRuleCRUDMixin`, `PlayerPositionService`, `test_async_persistence_core.py`, `test_player_presence_tracker.py`, `test_player_respawn_service.py`, `PersonalMessageSender`, `async_persistence_room_loader.py`, `test_movement_service.py`, `maps.py`, `test_combat_service_modules.py`, `_AsyncPersistenceRoomFacadeBase`, `test_player_service_mutations.py`, `test_connection_establishment.py`, `NPCDefinitionCRUDMixin`, `update_container`, `test_container_persistence_async_helpers.py`?**
  _High betweenness centrality (0.014) - this node is a cross-community bridge._
- **Are the 143 inferred relationships involving `LoggedHTTPException` (e.g. with `test_get_admin_sessions_error()` and `test_get_npc_population_stats_generic_error()`) actually correct?**
  _`LoggedHTTPException` has 143 INFERRED edges - model-reasoned connections that need verification._
- **Are the 194 inferred relationships involving `ValidationError` (e.g. with `fetch_user_by_username_case_insensitive()` and `load_database_url()`) actually correct?**
  _`ValidationError` has 194 INFERRED edges - model-reasoned connections that need verification._
- **Are the 82 inferred relationships involving `User` (e.g. with `.verify_token()` and `.create_user()`) actually correct?**
  _`User` has 82 INFERRED edges - model-reasoned connections that need verification._
- **Are the 74 inferred relationships involving `AliasStorage` (e.g. with `_handle_special_command_routing()` and `_prepare_command_for_processing()`) actually correct?**
  _`AliasStorage` has 74 INFERRED edges - model-reasoned connections that need verification._