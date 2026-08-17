# holidayresolver

> 87 nodes

## Key Concepts

- **MythosChronicle** (30 connections) — `server/time/time_service.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (23 connections) — `server/time/time_service.py`
- **test_time_bundle.py** (21 connections) — `server/tests/unit/container/test_time_bundle.py`
- **tick_scheduler.py** (16 connections) — `server/time/tick_scheduler.py`
- **datetime** (15 connections)
- **_ensure_utc()** (13 connections) — `server/time/time_service.py`
- **.get_calendar_components()** (10 connections) — `server/time/time_service.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **ChronicleState** (9 connections) — `server/time/time_service.py`
- **.get_current_mythos_datetime()** (9 connections) — `server/time/time_service.py`
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
- **.freeze()** (5 connections) — `server/time/time_service.py`
- **._hours_between()** (5 connections) — `server/time/time_service.py`
- *... and 62 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (13 shared connections)
- [server tests unit time test](server_tests_unit_time_test.md) (6 shared connections)
- [server config init create config](server_config_init_create_config.md) (5 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (4 shared connections)
- [scripts validate calendar load and](scripts_validate_calendar_load_and.md) (4 shared connections)
- [server app lifespan](server_app_lifespan.md) (3 shared connections)
- [server app lifespan shutdown](server_app_lifespan_shutdown.md) (3 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (3 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [server commands time commands handle](server_commands_time_commands_handle.md) (3 shared connections)
- [server app task registry get](server_app_task_registry_get.md) (2 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (2 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/config/models/chat_time.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/time/__init__.py`
- `server/time/tick_scheduler.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 219 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*