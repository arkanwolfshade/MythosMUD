# NATSMessageSubscriptionMixin

> 43 nodes

## Key Concepts

- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Any** (12 connections)
- **._get_event_handler_map()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_combat_ended_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_combat_started_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_event_message()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_game_tick_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_npc_attacked_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_npc_died_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_npc_took_damage_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_player_attacked_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_player_entered_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._handle_player_left_event()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._validate_event_message()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_active_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_event_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.is_event_subscription_active()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_room()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_room()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Mixin: room, subzone, and event NATS subscription lifecycle.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to chat messages for a specific room. Args: room_id: Room ID to…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to all event-related NATS subjects using standardized patterns.…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- *... and 18 more nodes in this community*

## Relationships

- [.handle_player_movement](handle_player_movement.md) (6 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 61 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*