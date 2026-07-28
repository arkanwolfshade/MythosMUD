# Docker PostgreSQL Typo Bug

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

- [Item Model Unit Tests](Item_Model_Unit_Tests.md) (8 shared connections)
- [Archive Who Command](Archive_Who_Command.md) (1 shared connections)
- [Schemas Calendar Schedule](Schemas_Calendar_Schedule.md) (1 shared connections)
- [Community 1592](Community_1592.md) (1 shared connections)
- [Combat Results Messages](Combat_Results_Messages.md) (1 shared connections)
- [Community 1594](Community_1594.md) (1 shared connections)
- [Readme Commands](Readme_Commands.md) (1 shared connections)
- [Community 1593](Community_1593.md) (1 shared connections)
- [Community 1596](Community_1596.md) (1 shared connections)
- [Schemas Calendar Holiday](Schemas_Calendar_Holiday.md) (1 shared connections)
- [Command Parser](Command_Parser.md) (1 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_game_tick_service.py`

## Audit Trail

- EXTRACTED: 48 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*