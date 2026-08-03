# instance game manager

> 14 nodes

## Key Concepts

- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **Normalize NATS event_data payload to a string-keyed dict.** (1 connections) — `server/realtime/event_handlers.py`
- **Get mapping of event types to their handler methods.          Returns:** (1 connections) — `server/realtime/event_handlers.py`
- **Validate that event message has required fields.          Args:             e** (1 connections) — `server/realtime/event_handlers.py`
- **Handle incoming event messages from NATS.          Args:             message_** (1 connections) — `server/realtime/event_handlers.py`
- **Handle player_attacked event.** (1 connections) — `server/realtime/event_handlers.py`
- **Handle npc_attacked event.** (1 connections) — `server/realtime/event_handlers.py`
- **Handle npc_took_damage event.** (1 connections) — `server/realtime/event_handlers.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (7 shared connections)

## Source Files

- `server/realtime/event_handlers.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*