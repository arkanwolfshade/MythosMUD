# Server Time

> 75 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **MythosTickScheduler** (15 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **__init__.py** (8 connections) — `server/time/__init__.py`
- **.get_daypart()** (8 connections) — `server/time/time_service.py`
- **._load_state()** (8 connections) — `server/time/time_service.py`
- **._persist_state()** (8 connections) — `server/time/time_service.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **.to_mythos_datetime()** (7 connections) — `server/time/time_service.py`
- **.is_witching_hour()** (7 connections) — `server/time/time_service.py`
- **.is_daytime()** (7 connections) — `server/time/time_service.py`
- **._migrate_old_state_file()** (6 connections) — `server/time/time_service.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._run()** (5 connections) — `server/time/tick_scheduler.py`
- **._emit_pending_ticks()** (5 connections) — `server/time/tick_scheduler.py`
- **._publish_tick()** (5 connections) — `server/time/tick_scheduler.py`
- **.to_real_datetime()** (5 connections) — `server/time/time_service.py`
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- **._truncate_to_hour()** (4 connections) — `server/time/tick_scheduler.py`
- *... and 50 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (11 shared connections)
- [Server Events](Server_Events.md) (6 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (5 shared connections)
- [Server Config](Server_Config.md) (3 shared connections)
- [Server Utils (4)](Server_Utils_%284%29.md) (2 shared connections)
- [Server App (2)](Server_App_%282%29.md) (2 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (2 shared connections)
- [Server Monitoring](Server_Monitoring.md) (1 shared connections)
- [Server Middleware (2)](Server_Middleware_%282%29.md) (1 shared connections)
- [Server Structured Logging (9)](Server_Structured_Logging_%289%29.md) (1 shared connections)
- [Server Services (22)](Server_Services_%2822%29.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 271 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*