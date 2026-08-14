# .cleanup_empty_subzone_subscriptions

> 6 nodes

## Key Concepts

- **.cleanup_empty_subzone_subscriptions()** (4 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.unsubscribe_from_subzone()** (4 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **.get_players_in_subzone()** (3 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Unsubscribe from local channel messages for a specific sub-zone. Args: subzone:…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Get list of players currently in a specific sub-zone. Args: subzone: Sub-zone…** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **Clean up sub-zone subscriptions that have no active players.** (1 connections) — `server/realtime/nats_message_handler_subscriptions.py`

## Relationships

- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (3 shared connections)
- [.handle_player_movement](handle_player_movement.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_subscriptions.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*