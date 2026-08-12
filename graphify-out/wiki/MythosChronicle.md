# MythosChronicle

> 70 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **MythosTimeEventConsumer** (22 connections) — `server/time/time_event_consumer.py`
- **datetime** (15 connections)
- **ChronicleLike** (13 connections) — `server/time/time_service.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **._build_broadcast_payload()** (7 connections) — `server/time/time_event_consumer.py`
- **.__init__()** (7 connections) — `server/time/time_event_consumer.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **._handle_tick()** (5 connections) — `server/time/time_event_consumer.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **._serialize_holiday()** (4 connections) — `server/time/time_event_consumer.py`
- **._serialize_schedule()** (4 connections) — `server/time/time_event_consumer.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- *... and 45 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (25 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [GameBundle](GameBundle.md) (2 shared connections)
- [RoomService](RoomService.md) (2 shared connections)
- [ErrorContext](ErrorContext.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/time/time_event_consumer.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 270 (95%)
- INFERRED: 15 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*