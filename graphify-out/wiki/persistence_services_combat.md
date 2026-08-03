# persistence services combat

> 13 nodes

## Key Concepts

- **Any** (12 connections)
- **._get_event_handler_map()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._validate_event_message()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_player_left_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_combat_ended_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_player_attacked_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_npc_took_damage_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get mapping of event types to their handler methods.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Validate that event message has required fields.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Handle player_left event.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Handle combat_ended event.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Handle player_attacked event.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Handle npc_took_damage event.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`

## Relationships

- [handler realtime nats](handler_realtime_nats.md) (6 shared connections)
- [AppRouter main AppRouter()](AppRouter_main_AppRouter%28%29.md) (1 shared connections)
- [invite models generate](invite_models_generate.md) (1 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)
- [invite models create](invite_models_create.md) (1 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*