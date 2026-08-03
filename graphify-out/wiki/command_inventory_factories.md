# command inventory factories

> 700 nodes

## Key Concepts

- **get_logger()** (516 connections) — `server/structured_logging/enhanced_logging_config.py`
- **enhanced_logging_config.py** (489 connections) — `server/structured_logging/enhanced_logging_config.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **players.py** (66 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **factory.py** (45 connections) — `server/app/factory.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **processing.py** (25 connections) — `server/command_handler/processing.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **__init__.py** (24 connections) — `server/config/models/__init__.py`
- **PerformanceMonitor** (24 connections) — `server/monitoring/performance_monitor.py`
- **ExceptionTracker** (23 connections) — `server/monitoring/exception_tracker.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- *... and 675 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (143 shared connections)
- [command inventory models](command_inventory_models.md) (91 shared connections)
- [commands admin mute](commands_admin_mute.md) (63 shared connections)
- [time service rationale](time_service_rationale.md) (47 shared connections)
- [Error Conversion](Error_Conversion.md) (45 shared connections)
- [NPC Combat](NPC_Combat.md) (43 shared connections)
- [Room Broadcast](Room_Broadcast.md) (42 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (40 shared connections)
- [command factories create](command_factories_create.md) (40 shared connections)
- [game models player](game_models_player.md) (37 shared connections)
- [item models rationale](item_models_rationale.md) (30 shared connections)
- [Player Stats](Player_Stats.md) (29 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/base.py`
- `server/api/containers.py`
- `server/api/players.py`
- `server/api/skills.py`
- `server/app/factory.py`
- `server/app/lifespan.py`
- `server/caching/__init__.py`
- `server/caching/cache_service.py`
- `server/caching/lru_cache.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/processing.py`
- `server/commands/container_helpers_inventory_logging.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`

## Audit Trail

- EXTRACTED: 4047 (97%)
- INFERRED: 135 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*