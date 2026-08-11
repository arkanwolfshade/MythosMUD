# Player Movement Service

> 72 nodes

## Key Concepts

- **correct_patterns.py** (20 connections) — `docs/examples/logging/correct_patterns.py`
- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **correct_performance_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_async_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_exception_tracking()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **risky_operation()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **database** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.execute()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **correct_error_handling()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_database_logging()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **process_data()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **.query()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- *... and 47 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (6 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (5 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (3 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (3 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Async Code Review Docs](Async_Code_Review_Docs.md) (1 shared connections)
- [Cursor Skills Frontend](Cursor_Skills_Frontend.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 171 (85%)
- INFERRED: 31 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*