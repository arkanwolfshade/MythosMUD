# TerminalButtonProps

> 1162 nodes

## Key Concepts

- **get_logger()** (511 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (485 connections) — `server/structured_logging/enhanced_logging_config.py`
- **EventBus** (135 connections) — `server/events/event_bus.py`
- **NPCDefinition** (119 connections) — `server/models/npc.py`
- **time.py** (89 connections) — `server/container/bundles/time.py`
- **NPCBase** (83 connections) — `server/npc/npc_base.py`
- **event_types.py** (79 connections) — `server/events/event_types.py`
- **get_npc_instance_service()** (79 connections) — `server/services/npc_instance_service.py`
- **NPCLifecycleManager** (76 connections) — `server/npc/lifecycle_manager.py`
- **async_persistence.py** (73 connections) — `server/async_persistence.py`
- **BaseEvent** (73 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (71 connections) — `server/events/event_types.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **NPCPopulationController** (64 connections) — `server/npc/population_control.py`
- **NPCCombatIntegration** (63 connections) — `server/npc/combat_integration.py`
- **PlayerLeftRoom** (53 connections) — `server/events/event_types.py`
- **test_npc_instance_service.py** (53 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **NPCSpawningService** (50 connections) — `server/npc/spawning_service.py`
- **npc_combat_integration_service.py** (50 connections) — `server/services/npc_combat_integration_service.py`
- **lifecycle_manager.py** (48 connections) — `server/npc/lifecycle_manager.py`
- **threading.py** (47 connections) — `server/npc/threading.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **npc_base.py** (44 connections) — `server/npc/npc_base.py`
- **population_control.py** (42 connections) — `server/npc/population_control.py`
- *... and 1137 more nodes in this community*

## Relationships

- [Any](Any.md) (204 shared connections)
- [. init ()](_init_%28%29.md) (147 shared connections)
- [Player](Player.md) (102 shared connections)
- [real time](real_time.md) (100 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (76 shared connections)
- [test command parser](test_command_parser.md) (73 shared connections)
- [UUID](UUID.md) (56 shared connections)
- [metrics](metrics.md) (51 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (48 shared connections)
- [. repr ()](_repr_%28%29.md) (44 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (35 shared connections)
- [.initialize()](initialize%28%29.md) (33 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/app/lifespan_startup.py`
- `server/app/task_registry.py`
- `server/async_persistence.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/commands/position_commands.py`
- `server/commands/shutdown_process_termination.py`
- `server/config/models/cors.py`
- `server/constants/spawn_defaults.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/events/__init__.py`
- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/game/chat_pose_manager.py`
- `server/game/chat_whisper_tracker.py`

## Audit Trail

- EXTRACTED: 6550 (93%)
- INFERRED: 471 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*