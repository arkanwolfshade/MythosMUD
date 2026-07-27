# Memory Leak Metrics

> 15 nodes · cohesion 0.01

## Key Concepts

- **Request** (10 connections) — `server/api/system_monitoring.py`
- **Any** (10 connections) — `server/monitoring/memory_leak_metrics.py`
- **Any** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections) — `server/monitoring/performance_monitor.py`
- **Any** (5 connections) — `server/monitoring/exception_tracker.py`
- **Exception** (5 connections) — `server/monitoring/exception_tracker.py`
- **FastAPI** (4 connections) — `server/app/lifespan.py`
- **Any** (4 connections) — `server/monitoring/__init__.py`
- **Any** (3 connections) — `server/app/lifespan.py`
- **Exception** (2 connections) — `docs/examples/logging/websocket_integration.py`
- **BaseUserManager** (1 connections) — `server/auth/jwt_strategy.py`
- **ID** (1 connections) — `server/auth/jwt_strategy.py`
- **BoundLogger** (1 connections) — `server/structured_logging/logging_context.py`
- **UP** (1 connections) — `server/auth/jwt_strategy.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 53 (77%)
- INFERRED: 16 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*