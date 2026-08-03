# System Metrics

> 194 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MonitoringDashboard** (31 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceMonitor** (24 connections) — `server/monitoring/performance_monitor.py`
- **websocket_integration.py** (22 connections) — `docs/examples/logging/websocket_integration.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (20 connections) — `server/monitoring/performance_monitor.py`
- **exception_tracker.py** (18 connections) — `server/monitoring/exception_tracker.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **log_aggregator.py** (13 connections) — `server/structured_logging/log_aggregator.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- *... and 169 more nodes in this community*

## Relationships

- [health models rationale](health_models_rationale.md) (20 shared connections)
- [NATS Messaging](NATS_Messaging.md) (19 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (15 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (8 shared connections)
- [log structured logging](log_structured_logging.md) (8 shared connections)
- [time service rationale](time_service_rationale.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (7 shared connections)
- [examples logging testing](examples_logging_testing.md) (7 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (6 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (6 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/app/lifespan.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_main.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 792 (93%)
- INFERRED: 59 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*