# MythosChronicle

> 57 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **datetime** (15 connections)
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **MythosCalendarComponents** (4 connections) — `server/time/time_service.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- **.format_clock()** (4 connections) — `server/time/time_service.py`
- **.get_instance()** (3 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- *... and 32 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [.__post_init__](__post_init__.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [ChronicleLike](ChronicleLike.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [lifespan_shutdown.py](lifespan_shutdown.py.md) (3 shared connections)
- [handle_time_command](handle_time_command.md) (3 shared connections)
- [AppConfig](AppConfig.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 158 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*