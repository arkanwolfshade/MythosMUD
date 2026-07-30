# AsyncSessionFactory

> 157 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **game.py** (25 connections) — `server/api/game.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- **datetime** (15 connections)
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **broadcast_message()** (13 connections) — `server/api/game.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **GameStatusResponse** (9 connections) — `server/schemas/game/game.py`
- **BroadcastMessageResponse** (9 connections) — `server/schemas/game/game.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **get_game_status()** (7 connections) — `server/api/game.py`
- **__init__.py** (7 connections) — `server/schemas/game/__init__.py`
- *... and 132 more nodes in this community*

## Relationships

- [Connection Manager](Connection_Manager.md) (11 shared connections)
- [close db()](close_db%28%29.md) (9 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (9 shared connections)
- [world](world.md) (8 shared connections)
- [.shutdown()](shutdown%28%29.md) (7 shared connections)
- [HolidayCollection](HolidayCollection.md) (5 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (5 shared connections)
- [Protocol](Protocol.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [get health status()](get_health_status%28%29.md) (3 shared connections)
- [get current tick()](get_current_tick%28%29.md) (3 shared connections)
- [init](init.md) (2 shared connections)

## Source Files

- `server/api/game.py`
- `server/app/lifespan_shutdown.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 594 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*