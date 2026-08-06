# time service rationale

> 51 nodes

## Key Concepts

- **MythosChronicle** (29 connections) — `server/time/time_service.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **.format_clock()** (4 connections) — `server/time/time_service.py`
- **.advance_mythos()** (4 connections) — `server/time/time_service.py`
- **test_ensure_utc_naive_datetime()** (3 connections) — `server/tests/unit/container/test_time_bundle.py`
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_instance()** (3 connections) — `server/time/time_service.py`
- **.get_state_snapshot()** (3 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [player respawn event](player_respawn_event.md) (4 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)
- [admin shutdown commands](admin_shutdown_commands.md) (2 shared connections)
- [schemas items item](schemas_items_item.md) (2 shared connections)
- [rate limiter services](rate_limiter_services.md) (2 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (2 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (2 shared connections)
- [tools generate invite](tools_generate_invite.md) (1 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/container/test_time_bundle.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 206 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*