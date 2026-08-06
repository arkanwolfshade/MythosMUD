# command commands handler

> 44 nodes

## Key Concepts

- **apply_communication_dampening()** (13 connections) — `server/services/lucidity_communication_dampening.py`
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_lucidity_communication_dampening.py** (11 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **Any** (7 connections)
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
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
- **._is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_should_block_shout_deranged()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_whisper_uneasy_adds_strained_tag()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_deranged_shout_blocked()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_outgoing_no_glyph_when_roll_high()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_outgoing_appends_glyph()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **test_fractured_incoming_strips_punctuation()** (2 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- *... and 19 more nodes in this community*

## Relationships

- [follow game service](follow_game_service.md) (14 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [game chat service](game_chat_service.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Audit Trail

- EXTRACTED: 141 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*