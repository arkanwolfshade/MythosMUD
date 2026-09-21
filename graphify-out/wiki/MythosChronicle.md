# MythosChronicle

> 99 nodes

## Key Concepts

- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.error()** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **isolated_chronicle()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- *... and 74 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (10 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (8 shared connections)
- [HolidayService](HolidayService.md) (8 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (5 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [api/game.py](api-game.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (3 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/commands/time_commands.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 247 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*