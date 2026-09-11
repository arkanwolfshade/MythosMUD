# test_system_monitoring_endpoints.py

> 14 nodes

## Key Concepts

- **test_system_monitoring_endpoints.py** (10 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **_resolve_memory_leak_collector_from_request()** (9 connections) — `server/api/system_monitoring.py`
- **_request_with_container()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_handles_missing_collector_gracefully()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_includes_memory_leak_metrics()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_resolve_memory_leak_collector_from_request_none_when_unset()** (3 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_resolve_memory_leak_collector_from_request_returns_container_instance()** (3 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_resolve_memory_leak_collector_from_request_none_when_no_container()** (2 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **asyncio** (2 connections)
- **Any** (1 connections)
- **Resolve the container-owned MemoryLeakMetricsCollector (#679: no per-request…** (1 connections) — `server/api/system_monitoring.py`
- **Unit tests for server.api.system_monitoring resolvers. #679:…** (1 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **The collector resolved from the container is reused, not rebuilt per request.** (1 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **No collector on the container -- endpoint still succeeds, just without leak…** (1 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*