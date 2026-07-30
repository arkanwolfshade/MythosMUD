# PerformanceTracker

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

- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [handle explore command()](handle_explore_command%28%29.md) (1 shared connections)
- [.get original string id()](get_original_string_id%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [logging utilities](logging_utilities.md) (1 shared connections)
- [Tests for get spell targeting](Tests_for_get_spell_targeting.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*