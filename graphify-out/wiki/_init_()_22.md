# . init ()

> 55 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **datetime** (15 connections)
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
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
- **.get_current_mythos_datetime()** (3 connections) — `server/time/time_service.py`
- **.format_clock()** (3 connections) — `server/time/time_service.py`
- **.get_instance()** (3 connections) — `server/time/time_service.py`
- **.get_state_snapshot()** (3 connections) — `server/time/time_service.py`
- **.get_last_freeze_state()** (3 connections) — `server/time/time_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (12 shared connections)
- [Any](Any.md) (2 shared connections)
- [time commands](time_commands.md) (2 shared connections)
- [init](init.md) (2 shared connections)
- [Cancel lifecycle/critical tasks first (Phase](Cancel_lifecycle-critical_tasks_first_%28Phase.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [Lock](Lock.md) (1 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 212 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*