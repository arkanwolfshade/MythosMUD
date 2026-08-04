# message broadcast realtime

> 60 nodes

## Key Concepts

- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **apply_communication_dampening()** (13 connections) — `server/services/lucidity_communication_dampening.py`
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_lucidity_communication_dampening.py** (11 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **Any** (7 connections)
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **lucidity_communication_dampening.py** (6 connections) — `server/services/lucidity_communication_dampening.py`
- **UserManager** (5 connections)
- **._filter_target_players()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._preload_receiver_mute_data()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **should_block_shout()** (4 connections) — `server/services/lucidity_communication_dampening.py`
- **._collect_room_targets()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_echo_to_sender()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_apply_mute_check()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._compare_canonical_rooms()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_room_from_online_players()** (2 connections) — `server/realtime/nats_message_handler_broadcast.py`
- *... and 35 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (3 shared connections)
- [startup npc services](startup_npc_services.md) (3 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Audit Trail

- EXTRACTED: 190 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*