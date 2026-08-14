# .handle_player_movement

> 6 nodes

## Key Concepts

- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.subscribe_to_subzone()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.track_player_subzone_subscription()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Track a player's sub-zone subscription for local channels. Args: player_id:…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Handle player movement between rooms and update sub-zone subscriptions. Args:…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Subscribe to local channel messages for a specific sub-zone. Args: subzone:…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`

## Relationships

- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (3 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (1 shared connections)
- [.cleanup_empty_subzone_subscriptions](cleanup_empty_subzone_subscriptions.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*