# asyncsessionfactory

> 22 nodes

## Key Concepts

- **rescue_service.py** (20 connections) — `server/services/rescue_service.py`
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **.rescue()** (8 connections) — `server/services/rescue_service.py`
- **Any** (7 connections)
- **_load_rescue_participants()** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **._apply_rescue_adjustment()** (5 connections) — `server/services/rescue_service.py`
- **_dispatch_rescue_events()** (4 connections) — `server/services/rescue_service.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **_rescue_success_payload()** (3 connections) — `server/services/rescue_service.py`
- **UUID** (3 connections)
- **EventDispatcher** (2 connections)
- **AsyncSessionFactory** (1 connections)
- **LucidityServiceFactory** (1 connections)
- **Rescue service encapsulating rescue flows with injectable dependencies. This…** (1 connections) — `server/services/rescue_service.py`
- **Service for performing rescue operations.** (1 connections) — `server/services/rescue_service.py`
- **Perform a rescue for the given target. Returns: dict containing a user-facing…** (1 connections) — `server/services/rescue_service.py`
- **Convert value to UUID, raising ValueError if invalid.** (1 connections) — `server/services/rescue_service.py`
- **Await the value if it is awaitable.** (1 connections) — `server/services/rescue_service.py`
- **Load rescuer and target or return an error payload.** (1 connections) — `server/services/rescue_service.py`
- **Dispatch rescue notifications (best-effort).** (1 connections) — `server/services/rescue_service.py`

## Relationships

- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (8 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (3 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (2 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`

## Audit Trail

- EXTRACTED: 53 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*