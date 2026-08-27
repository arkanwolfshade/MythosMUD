# Test Suite Quality Audit Report

> 12 nodes

## Key Concepts

- **test_monitoring_init.py** (7 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **test_monitoring_eager_imports()** (2 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **test_monitoring_getattr_direct_call()** (2 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **test_monitoring_getattr_lazy_dashboard_symbols()** (2 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **test_monitoring_getattr_lazy_performance_symbols()** (2 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **test_monitoring_getattr_unknown_raises()** (2 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **Unit tests for server.monitoring lazy __getattr__ re-exports.** (1 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **Exception tracker symbols import without triggering numpy lazy paths.** (1 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **__getattr__ resolves MonitoringDashboard and get_monitoring_dashboard.** (1 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **__getattr__ resolves PerformanceStats and get_performance_monitor.** (1 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **Unknown attribute names raise AttributeError.** (1 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`
- **Direct __getattr__ covers both branch returns for dashboard imports.** (1 connections) — `server/tests/unit/monitoring/test_monitoring_init.py`

## Relationships

- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/tests/unit/monitoring/test_monitoring_init.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*