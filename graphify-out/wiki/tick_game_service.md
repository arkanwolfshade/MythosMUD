# tick game service

> 16 nodes

## Key Concepts

- **TestGameTickService** (20 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_init_default_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_not_running()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_stop_failure()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_get_tick_interval()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_increments_count()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_publishes_events()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **.test_tick_loop_handles_exceptions()** (3 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test suite for GameTickService class.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test GameTickService initialization with default interval.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test stop returns True when not running.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test stop handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test get_tick_interval returns interval.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop increments tick count.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop publishes game tick events.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`
- **Test _tick_loop handles exceptions and continues.** (1 connections) — `server/tests/unit/services/test_game_tick_service.py`

## Relationships

- [tick service services](tick_service_services.md) (8 shared connections)
- [tick services game](tick_services_game.md) (4 shared connections)
- [services game tick](services_game_tick.md) (4 shared connections)
- [npc realtime event](npc_realtime_event.md) (2 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*