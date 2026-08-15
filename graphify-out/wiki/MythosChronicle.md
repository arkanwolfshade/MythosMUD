# MythosChronicle

> 171 nodes

## Key Concepts

- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **api/game.py** (28 connections) — `server/api/game.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **time_service.py** (26 connections) — `server/time/time_service.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **test_time_bundle.py** (20 connections) — `server/tests/unit/container/test_time_bundle.py`
- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **datetime** (15 connections)
- **broadcast_message()** (14 connections) — `server/api/game.py`
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **server/api/__init__.py** (12 connections) — `server/api/__init__.py`
- **TestGetMythosTime** (11 connections) — `server/tests/unit/api/test_game.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **BroadcastMessageResponse** (8 connections) — `server/schemas/game/game.py`
- **GameStatusResponse** (8 connections) — `server/schemas/game/game.py`
- **MythosTimeResponse** (8 connections) — `server/schemas/game/game.py`
- **get_game_status()** (8 connections) — `server/api/game.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- *... and 146 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (23 shared connections)
- [HolidayService](HolidayService.md) (12 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (5 shared connections)
- [User](User.md) (5 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (5 shared connections)
- [get_config](get_config.md) (4 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (3 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (3 shared connections)
- [handle_time_command](handle_time_command.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/containers.py`
- `server/api/game.py`
- `server/commands/time_commands.py`
- `server/config/models/chat_time.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 375 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*