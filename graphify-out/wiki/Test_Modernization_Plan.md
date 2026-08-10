# Test Modernization Plan

> 106 nodes

## Key Concepts

- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **time_service.py** (25 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **datetime** (15 connections)
- **tick_scheduler.py** (14 connections) — `server/time/tick_scheduler.py`
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **_ensure_utc()** (11 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **._init_temporal_layer()** (9 connections) — `server/container/bundles/game.py`
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
- **FastAPI** (5 connections)
- *... and 81 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (15 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (9 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (7 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (4 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (3 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)

## Source Files

- `server/app/lifespan_shutdown.py`
- `server/config/models/chat_time.py`
- `server/container/bundles/game.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 430 (96%)
- INFERRED: 17 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*