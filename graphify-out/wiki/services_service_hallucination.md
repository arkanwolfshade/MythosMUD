# services service hallucination

> 8 nodes

## Key Concepts

- **_send_combat_participant_updates()** (8 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **Keys from a participants mapping (NATS may send dict-like payloads).** (1 connections) — `server/realtime/event_handlers.py`
- **Push player_update to each combat participant (in_combat flag).** (1 connections) — `server/realtime/event_handlers.py`
- **Handle combat_started event.** (1 connections) — `server/realtime/event_handlers.py`
- **Handle combat_ended event.** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*