# AnyIO Code Review

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

- [Combat Health Persistence Fix](Combat_Health_Persistence_Fix.md) (8 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (3 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)
- [Cursor Plans Postgresql](Cursor_Plans_Postgresql.md) (1 shared connections)
- [Realtime Player Event](Realtime_Player_Event.md) (1 shared connections)
- [Realtime Websocket Handler](Realtime_Websocket_Handler.md) (1 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (1 shared connections)
- [Realtime Nats Message](Realtime_Nats_Message.md) (1 shared connections)
- [Persistence Repositories Skill](Persistence_Repositories_Skill.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*