# health models rationale

> 36 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (8 connections) — `server/api/monitoring.py`
- **test_get_health_status_healthy_returns_model()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_dual_connection_and_performance_and_health_stats()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Any** (5 connections)
- **_resolve_task_registry()** (5 connections) — `server/api/monitoring.py`
- **_connection_manager_stub()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_memory_alerts_and_force_cleanup()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_memory_stats_with_leak_collector()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_memory_stats_leak_collector_warning_branch()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_movement_metrics_uses_monitor()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_movement_metrics_logged_http_on_failure()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_connection_manager_from_request()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_event_bus_from_request()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_cache_manager_from_container()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_cache_metrics_builds_response()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_eventbus_metrics_shapes()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_event_bus_missing_raises()** (2 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_cache_manager_fallback_global()** (2 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 11 more nodes in this community*

## Relationships

- [command combat models](command_combat_models.md) (41 shared connections)
- [grace period login](grace_period_login.md) (10 shared connections)
- [npc population control](npc_population_control.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [System Metrics](System_Metrics.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 197 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*