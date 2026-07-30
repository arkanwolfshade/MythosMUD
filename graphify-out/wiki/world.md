# world

> 620 nodes

## Key Concepts

- **get_logger()** (511 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (485 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **LRUCache** (27 connections) — `server/caching/lru_cache.py`
- **__init__.py** (24 connections) — `server/config/models/__init__.py`
- **HealthMonitor** (22 connections) — `server/realtime/monitoring/health_monitor.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **user_manager.py** (20 connections) — `server/services/user_manager.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **get_global_tracked_manager()** (18 connections) — `server/app/tracked_task_manager.py`
- **PerformanceTracker** (18 connections) — `server/realtime/monitoring/performance_tracker.py`
- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **enhance_player_ids()** (17 connections) — `server/structured_logging/logging_processors.py`
- **detect_environment()** (16 connections) — `server/structured_logging/logging_utilities.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **npc_combat_handlers.py** (15 connections) — `server/services/npc_combat_handlers.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- *... and 595 more nodes in this community*

## Relationships

- [Any](Any.md) (78 shared connections)
- [real time](real_time.md) (74 shared connections)
- [. init ()](_init_%28%29.md) (68 shared connections)
- [Spell Targeting](Spell_Targeting.md) (45 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (44 shared connections)
- [Player](Player.md) (42 shared connections)
- [close db()](close_db%28%29.md) (30 shared connections)
- [circuit breaker](circuit_breaker.md) (29 shared connections)
- [get current tick()](get_current_tick%28%29.md) (28 shared connections)
- [main()](main%28%29.md) (27 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (25 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (23 shared connections)

## Source Files

- `server/api/base.py`
- `server/app/memory_cleanup_service.py`
- `server/app/memory_lifespan_coordinator.py`
- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/auth/email_utils.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`

## Audit Trail

- EXTRACTED: 3272 (98%)
- INFERRED: 58 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*