# NATSMessageSubscriptionMixin

> 16 nodes

## Key Concepts

- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_room()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_active_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_event_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.is_event_subscription_active()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Mixin: room, subzone, and event NATS subscription lifecycle.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to chat messages for a specific room.          Args:             room_** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get the number of active subscriptions.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get list of active subscription subjects.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to all event-related NATS subjects using standardized patterns.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Unsubscribe from all event-related NATS subjects using standardized patterns.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get the number of active event subscriptions.          Returns:             Numb** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Check if a specific event subscription is active.          Args:             sub** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`

## Relationships

- [PerformanceTracker](PerformanceTracker.md) (6 shared connections)
- [Player](Player.md) (4 shared connections)
- [verify npc occupants](verify_npc_occupants.md) (3 shared connections)
- [EnvironmentalContainerLoader](EnvironmentalContainerLoader.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [handle explore command()](handle_explore_command%28%29.md) (1 shared connections)
- [.get original string id()](get_original_string_id%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [logging utilities](logging_utilities.md) (1 shared connections)
- [Tests for get spell targeting](Tests_for_get_spell_targeting.md) (1 shared connections)
- [get alias validator()](get_alias_validator%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*