# test_event_bus_lifecycle.py

> 44 nodes

## Key Concepts

- **test_event_bus_lifecycle.py** (25 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **asyncio** (11 connections)
- **event_bus()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_abandon_pending_tasks_cancels_and_drains()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_active_tasks_best_effort_cancels_running_tasks()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_and_wait_for_active_tasks_abandons_pending()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_and_wait_for_active_tasks_all_already_done()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_processing_task_swallows_timeout()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_del_running_swallows_logger_warning_error()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_finalize_shutdown_swallows_logging_error()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_shutdown_finally_cancels_leftover_processing_task()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_shutdown_swallows_cancelled_error()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_shutdown_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_stop_processing_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_active_tasks_best_effort_no_active_tasks()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_cancel_task_quietly_swallows_runtime_error()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_del_no_op_when_not_running()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_del_running_swallows_shutdown_event_set_error()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_ensure_async_processing_loop_not_running_logs_warning()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_ensure_async_processing_unexpected_exception_logged()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_signal_shutdown_swallows_queue_full()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **test_warn_shutdown_error_swallows_logging_error()** (3 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **fixture** (1 connections)
- **Unit tests for EventBusLifecycleMixin's edge-case and exception-handling…** (1 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- **_cancel_and_wait_for_active_tasks() falls through to _abandon_pending_tasks…** (1 connections) — `server/tests/unit/events/test_event_bus_lifecycle.py`
- *... and 19 more nodes in this community*

## Relationships

- [EventBus](EventBus.md) (21 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus_lifecycle.py`

## Audit Trail

- EXTRACTED: 57 (74%)
- INFERRED: 20 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*