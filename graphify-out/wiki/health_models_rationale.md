# health models rationale

> 450 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_movement_monitor.py** (33 connections) — `server/tests/unit/game/test_movement_monitor.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **MovementMonitor** (21 connections) — `server/game/movement_monitor.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **HealthService** (21 connections) — `server/services/health_service.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **health_service.py** (20 connections) — `server/services/health_service.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **HealthResponse** (17 connections) — `server/models/health.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **health.py** (14 connections) — `server/models/health.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 425 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (34 shared connections)
- [NATS Messaging](NATS_Messaging.md) (28 shared connections)
- [System Metrics](System_Metrics.md) (20 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [Room Broadcast](Room_Broadcast.md) (5 shared connections)
- [services combat sync](services_combat_sync.md) (5 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [auth rationale access](auth_rationale_access.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (3 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (3 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/base.py`
- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/task_registry.py`
- `server/caching/lru_cache.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 1785 (98%)
- INFERRED: 32 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*