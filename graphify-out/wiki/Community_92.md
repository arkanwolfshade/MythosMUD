# Community 92

> 102 nodes

## Key Concepts

- **MythosTickScheduler** (32 connections) — `server/time/tick_scheduler.py`
- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **test_tick_scheduler.py** (18 connections) — `server/tests/unit/time/test_tick_scheduler.py`
- **tick_scheduler.py** (16 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **get_mythos_chronicle()** (14 connections) — `server/time/time_service.py`
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **asyncio** (9 connections)
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **time/__init__.py** (8 connections) — `server/time/__init__.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **isolated_chronicle()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **test_get_mythos_chronicle_singleton()** (5 connections) — `server/tests/unit/container/test_time_bundle.py`
- **.error()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- *... and 77 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (13 shared connections)
- [Community 588](Community_588.md) (11 shared connections)
- [Community 247](Community_247.md) (4 shared connections)
- [Distributed Event Bus (NATS)](Distributed_Event_Bus_NATS.md) (4 shared connections)
- [Community 173](Community_173.md) (4 shared connections)
- [Community 162](Community_162.md) (4 shared connections)
- [Community 264](Community_264.md) (3 shared connections)
- [Community 563](Community_563.md) (3 shared connections)
- [Community 550](Community_550.md) (2 shared connections)
- [Community 69](Community_69.md) (2 shared connections)
- [Community 454](Community_454.md) (1 shared connections)
- [Community 1074](Community_1074.md) (1 shared connections)

## Source Files

- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/time/test_tick_scheduler.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 234 (91%)
- INFERRED: 22 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*