# TestGameTickService

> 16 nodes · cohesion 0.12

## Key Concepts

- **TestGameTickService** (20 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_get_tick_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_default_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_failure()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_not_running()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_exceptions()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_increments_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_publishes_events()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test stop handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test get_tick_interval returns interval.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop increments tick count.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop publishes game tick events.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test suite for GameTickService class.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test GameTickService initialization with default interval.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop handles exceptions and continues.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test stop returns True when not running.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`

## Relationships

- [GameTickService](GameTickService.md) (8 shared connections)
- [test_game_tick_service.py](test_game_tick_service.py.md) (1 shared connections)
- [.test_get_tick_count](test_get_tick_count.md) (1 shared connections)
- [.test_init_custom_interval](test_init_custom_interval.md) (1 shared connections)
- [.test_reset_tick_count](test_reset_tick_count.md) (1 shared connections)
- [.test_start_already_running](test_start_already_running.md) (1 shared connections)
- [.test_start_failure](test_start_failure.md) (1 shared connections)
- [.test_start_success](test_start_success.md) (1 shared connections)
- [.test_stop_success](test_stop_success.md) (1 shared connections)
- [.test_stop_task_already_done](test_stop_task_already_done.md) (1 shared connections)
- [.test_tick_loop_handles_cancellation](test_tick_loop_handles_cancellation.md) (1 shared connections)
- [.test_tick_loop_handles_publish_failure](test_tick_loop_handles_publish_failure.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*