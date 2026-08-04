# tick service services

> 54 nodes

## Key Concepts

- **GameTickService** (30 connections) — `server/services/game_tick_service.py`
- **TestGameTickService** (20 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **test_game_tick_service.py** (4 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_default_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_custom_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_start_success()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_start_already_running()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_start_failure()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_success()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_not_running()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_task_already_done()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_failure()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_get_tick_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_reset_tick_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_get_tick_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_increments_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_publishes_events()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_cancellation()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_publish_failure()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_exceptions()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.__init__()** (2 connections) — `server/services/game_tick_service.py`
- **.stop()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.reset_tick_count()** (2 connections) — `server/services/game_tick_service.py`
- **.get_tick_interval()** (2 connections) — `server/services/game_tick_service.py`
- *... and 29 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (2 shared connections)

## Source Files

- `server/services/game_tick_service.py`
- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 144 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*