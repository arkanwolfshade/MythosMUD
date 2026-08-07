# follow service game

> 50 nodes

## Key Concepts

- **TaskRegistry** (49 connections) — `server/app/task_registry.py`
- **test_task_registry.py** (23 connections) — `server/tests/unit/app/test_task_registry.py`
- **task_registry.py** (11 connections) — `server/app/task_registry.py`
- **get_registry()** (9 connections) — `server/app/task_registry.py`
- **_sleep_briefly()** (9 connections) — `server/tests/unit/app/test_task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **unregister_task()** (7 connections) — `server/app/task_registry.py`
- **register_task()** (6 connections) — `server/app/task_registry.py`
- **.get_task_lifecycle_metrics()** (5 connections) — `server/app/task_registry.py`
- **test_module_level_helpers()** (5 connections) — `server/tests/unit/app/test_task_registry.py`
- **._cleanup_registry_collections()** (4 connections) — `server/app/task_registry.py`
- **test_register_closes_coro_when_create_task_fails()** (4 connections) — `server/tests/unit/app/test_task_registry.py`
- **._cancel_lifecycle_tasks()** (3 connections) — `server/app/task_registry.py`
- **._cancel_remaining_tasks()** (3 connections) — `server/app/task_registry.py`
- **._wait_for_task_completion()** (3 connections) — `server/app/task_registry.py`
- **._forcible_cleanup_on_timeout()** (3 connections) — `server/app/task_registry.py`
- **.get_active_task_count()** (3 connections) — `server/app/task_registry.py`
- **.get_task_stats_by_type()** (3 connections) — `server/app/task_registry.py`
- **_hang_until_cancelled()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_task_metadata_repr()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_and_unregister_task()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_duplicate_name_gets_suffix()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_register_during_shutdown_raises()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_cancel_task_by_name()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- **test_shutdown_all_clears_active_tasks()** (3 connections) — `server/tests/unit/app/test_task_registry.py`
- *... and 25 more nodes in this community*

## Relationships

- [realtime messaging message](realtime_messaging_message.md) (16 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (5 shared connections)
- [rate limiter services](rate_limiter_services.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (1 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/tests/unit/app/test_task_registry.py`

## Audit Trail

- EXTRACTED: 209 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*