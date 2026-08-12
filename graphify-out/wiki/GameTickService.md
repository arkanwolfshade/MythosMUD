# GameTickService

> 59 nodes

## Key Concepts

- **GameTickService** (30 connections) — `server/services/game_tick_service.py`
- **TestGameTickService** (20 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **asyncio** (13 connections)
- **test_game_tick_service.py** (5 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.start()** (4 connections) — `server/services/game_tick_service.py`
- **.test_start_already_running()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_start_failure()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_start_success()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_failure()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_not_running()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_success()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_task_already_done()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_cancellation()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_exceptions()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_publish_failure()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_increments_count()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_publishes_events()** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **._tick_loop()** (3 connections) — `server/services/game_tick_service.py`
- **.test_get_tick_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_get_tick_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_custom_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_default_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_reset_tick_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.get_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [time.py](time.py.md) (3 shared connections)

## Source Files

- `server/services/game_tick_service.py`
- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 179 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*