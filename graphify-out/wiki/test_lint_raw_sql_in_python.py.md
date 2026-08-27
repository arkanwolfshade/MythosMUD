# test_lint_raw_sql_in_python.py

> 42 nodes

## Key Concepts

- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Any** (7 connections)
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._send_messages_to_players()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._apply_dampening_and_send_message()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._filter_target_players()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._preload_receiver_mute_data()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._collect_room_targets()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
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

- [container_persistence.py](container_persistence.py.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [verify_npc_occupants.py](verify_npc_occupants.py.md) (1 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (1 shared connections)
- [look_command.py](look_command.py.md) (1 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_broadcast.py`

## Audit Trail

- EXTRACTED: 69 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*