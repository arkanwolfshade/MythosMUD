# NATSMessageSubscriptionMixin

> 55 nodes

## Key Concepts

- **NATSMessageSubscriptionMixin** (31 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Any** (12 connections)
- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.cleanup_empty_subzone_subscriptions()** (4 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_subzone()** (4 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._get_event_handler_map()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_players_in_subzone()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
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
- **.subscribe_to_subzone()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.track_player_subzone_subscription()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **._validate_event_message()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_active_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_event_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.is_event_subscription_active()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_event_subjects()** (2 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- *... and 30 more nodes in this community*

## Relationships

- [nats_exceptions.py](nats_exceptions.py.md) (3 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [extract_subzone_from_room_id](extract_subzone_from_room_id.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*