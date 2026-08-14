# _send_combat_participant_updates

> 10 nodes

## Key Concepts

- **_send_combat_participant_updates()** (9 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **test_send_combat_participant_updates()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_participant_key_strings()** (2 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **Handle combat_started event.** (1 connections) — `server/realtime/event_handlers.py`
- **Handle combat_ended event.** (1 connections) — `server/realtime/event_handlers.py`
- **Keys from a participants mapping (NATS may send dict-like payloads).** (1 connections) — `server/realtime/event_handlers.py`
- **Push player_update to each combat participant (in_combat flag).** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [EventHandler](EventHandler.md) (7 shared connections)
- [event_handlers.py](event_handlers.py.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*