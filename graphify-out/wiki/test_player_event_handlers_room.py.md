# test_player_event_handlers_room.py

> 83 nodes · cohesion 0.03

## Key Concepts

- **MemoryLeakMetricsCollector** (28 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_memory_leak_metrics.py** (25 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **.event_bus()** (14 connections) — `server/realtime/connection_manager.py`
- **.initialize()** (11 connections) — `server/container/bundles/monitoring.py`
- **Any** (11 connections)
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (6 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **collector()** (4 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._get_event_bus()** (3 connections) — `server/realtime/connection_manager.py`
- **test_collect_event_metrics_uses_injected_event_bus()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_nats_metrics_uses_injected_nats_service()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates_insufficient_history()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 58 more nodes in this community*

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [Room](Room.md) (3 shared connections)
- [websocket_integration.py](websocket_integration.py.md) (3 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (2 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (2 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (1 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 128 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*