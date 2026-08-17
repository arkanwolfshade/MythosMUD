# NATSMessageSubscriptionMixin

> 16 nodes

## Key Concepts

- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_active_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_event_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.is_event_subscription_active()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_room()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Mixin: room, subzone, and event NATS subscription lifecycle.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to chat messages for a specific room. Args: room_id: Room ID to…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to all event-related NATS subjects using standardized patterns.…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Unsubscribe from all event-related NATS subjects using standardized patterns.…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get the number of active event subscriptions. Returns: Number of active event…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Check if a specific event subscription is active. Args: subject: NATS subject…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get the number of active subscriptions.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get list of active subscription subjects.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`

## Relationships

- [Any](Any.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [.cleanup_empty_subzone_subscriptions](cleanup_empty_subzone_subscriptions.md) (3 shared connections)
- [.handle_player_movement](handle_player_movement.md) (3 shared connections)
- [._handle_event_message](_handle_event_message.md) (1 shared connections)
- [._handle_player_entered_event](_handle_player_entered_event.md) (1 shared connections)
- [._handle_game_tick_event](_handle_game_tick_event.md) (1 shared connections)
- [._handle_combat_started_event](_handle_combat_started_event.md) (1 shared connections)
- [._handle_npc_attacked_event](_handle_npc_attacked_event.md) (1 shared connections)
- [._handle_npc_died_event](_handle_npc_died_event.md) (1 shared connections)
- [.unsubscribe_from_room](unsubscribe_from_room.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 36 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*