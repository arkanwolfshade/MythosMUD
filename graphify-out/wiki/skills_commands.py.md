# skills_commands.py

> 44 nodes · cohesion 0.07

## Key Concepts

- **NATSMessageBroadcastMixin** (26 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._broadcast_to_room_with_filtering()** (10 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._send_messages_to_players()** (8 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._apply_dampening_and_send_message()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Any** (7 connections)
- **._apply_receiver_segments()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._filter_target_players()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **UserManager** (4 connections)
- **._collect_room_targets()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_echo_to_sender()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._compare_canonical_rooms()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_room_from_online_players()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_room_from_persistence()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_in_room()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_apply_mute_check()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Determine if message should be echoed to sender. Args: channel: Channel type…** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Echo message back to sender. Args: sender_id: Sender player ID chat_event: Chat…** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`
- *... and 19 more nodes in this community*

## Relationships

- [Room](Room.md) (3 shared connections)
- [look_container.py](look_container.py.md) (3 shared connections)
- [mp_regeneration_service](mp_regeneration_service.md) (2 shared connections)
- [ValidationRule](ValidationRule.md) (2 shared connections)
- [deque](deque.md) (1 shared connections)
- [ItemFactory](ItemFactory.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [WebSocketManager](WebSocketManager.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_broadcast.py`

## Audit Trail

- EXTRACTED: 77 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*