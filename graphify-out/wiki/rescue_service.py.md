# rescue_service.py

> 22 nodes

## Key Concepts

- **rescue_service.py** (19 connections) — `server/services/rescue_service.py`
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

- [Player](Player.md) (4 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [.state](state.md) (3 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (3 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`

## Audit Trail

- EXTRACTED: 90 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*