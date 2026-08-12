# Archive Environment Contamination

> 43 nodes

## Key Concepts

- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (3 connections)
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **Any** (2 connections)
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Example 5: Request context migration.** (1 connections) — `docs/examples/logging/migration_examples.py`
- **Test request context binding functionality.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Test logging correlation IDs.** (1 connections) — `docs/examples/logging/testing_examples.py`
- *... and 18 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (7 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (5 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (3 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (2 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (2 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (2 shared connections)
- [Async Code Review Docs](Async_Code_Review_Docs.md) (1 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (1 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (1 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (1 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 96 (74%)
- INFERRED: 33 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*