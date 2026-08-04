# metrics memory leak

> 44 nodes

## Key Concepts

- **test_memory_leak_metrics.py** (23 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **collector()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collector_initialization()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics_no_manager()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics_no_bus()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_cache_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_task_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_nats_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_all_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_calculate_growth_rates_insufficient_history()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_closed_websockets_threshold()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_subscriber_growth_rate()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_cache_capacity()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_task_growth_rate()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_check_alerts_no_alerts()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_metrics_collection_performance()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_metrics_history_bounded()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_all_metrics_error_handling()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Memory leak metrics collector for MythosMUD.  This module provides comprehensive** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Unit tests for memory leak metrics collector.  Tests the MemoryLeakMetricsCollec** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Create a MemoryLeakMetricsCollector instance.** (1 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 19 more nodes in this community*

## Relationships

- [command combat models](command_combat_models.md) (3 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [room cache services](room_cache_services.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 99 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*