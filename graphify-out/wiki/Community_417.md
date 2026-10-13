# Community 417

> 42 nodes

## Key Concepts

- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._broadcast_to_room_with_filtering()** (10 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Any** (7 connections)
- **._filter_target_players()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._send_messages_to_players()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._apply_dampening_and_send_message()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._collect_room_targets()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_echo_to_sender()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._compare_canonical_rooms()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_room_from_online_players()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_room_from_persistence()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_in_room()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_apply_mute_check()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandlerMixinBase** (1 connections)
- **Determine if message should be echoed to sender. Args: channel: Channel type…** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Echo message back to sender. Args: sender_id: Sender player ID chat_event: Chat…** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Broadcast room-based messages with server-side filtering. This method ensures…** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`
- *... and 17 more nodes in this community*

## Relationships

- [Community 47](Community_47.md) (5 shared connections)
- [Community 85](Community_85.md) (4 shared connections)
- [Community 805](Community_805.md) (1 shared connections)
- [Community 646](Community_646.md) (1 shared connections)
- [DB Seed & Migration Scripts](DB_Seed_&_Migration_Scripts.md) (1 shared connections)
- [Community 138](Community_138.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_broadcast.py`

## Audit Trail

- EXTRACTED: 69 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*