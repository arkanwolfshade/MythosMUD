# _send_combat_participant_updates

> 8 nodes

## Key Concepts

- **_send_combat_participant_updates()** (7 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (3 connections) — `server/realtime/event_handlers.py`
- **Handle combat_started event.** (1 connections) — `server/realtime/event_handlers.py`
- **Handle combat_ended event.** (1 connections) — `server/realtime/event_handlers.py`
- **Keys from a participants mapping (NATS may send dict-like payloads).** (1 connections) — `server/realtime/event_handlers.py`
- **Push player_update to each combat participant (in_combat flag).** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [EventHandler](EventHandler.md) (2 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*