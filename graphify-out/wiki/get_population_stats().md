# .get population stats()

> 113 nodes

## Key Concepts

- **container.py** (25 connections) — `server/models/container.py`
- **test_container_websocket_events.py** (23 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **test_container_events.py** (22 connections) — `server/tests/unit/api/test_container_events.py`
- **container_events.py** (21 connections) — `server/api/container_events.py`
- **emit_loot_all_event()** (17 connections) — `server/api/container_events.py`
- **container_websocket_events.py** (17 connections) — `server/services/container_websocket_events.py`
- **emit_container_opened_events()** (16 connections) — `server/api/container_events.py`
- **_emit_close_container_event()** (14 connections) — `server/api/container_events.py`
- **emit_container_opened()** (14 connections) — `server/services/container_websocket_events.py`
- **TestEmitLootAllEvent** (13 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_opened_to_room()** (12 connections) — `server/services/container_websocket_events.py`
- **TestEmitCloseContainerEvent** (12 connections) — `server/tests/unit/api/test_container_events.py`
- **TestEmitContainerOpenedEvents** (11 connections) — `server/tests/unit/api/test_container_events.py`
- **emit_container_updated()** (10 connections) — `server/services/container_websocket_events.py`
- **emit_container_closed()** (9 connections) — `server/services/container_websocket_events.py`
- **emit_container_decayed()** (8 connections) — `server/services/container_websocket_events.py`
- **UUID** (6 connections)
- **UUID** (5 connections)
- **Any** (5 connections)
- **Any** (4 connections)
- **.test_emit_loot_all_event_success()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_no_connection_manager()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_no_room_id()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_emission_error()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- **.test_emit_loot_all_event_calculates_items_removed()** (4 connections) — `server/tests/unit/api/test_container_events.py`
- *... and 88 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (37 shared connections)
- [BaseCommand](BaseCommand.md) (20 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [datetime](datetime.md) (3 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)
- [Lock](Lock.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (1 shared connections)

## Source Files

- `server/api/container_events.py`
- `server/models/container.py`
- `server/services/container_websocket_events.py`
- `server/tests/unit/api/test_container_events.py`
- `server/tests/unit/services/test_container_websocket_events.py`

## Audit Trail

- EXTRACTED: 424 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*