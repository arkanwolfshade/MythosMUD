# NATSMessageBroadcastMixin

> 63 nodes

## Key Concepts

- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **apply_communication_dampening()** (15 connections) — `server/services/lucidity_communication_dampening.py`
- **._broadcast_to_room_with_filtering()** (11 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **lucidity_communication_dampening.py** (11 connections) — `server/services/lucidity_communication_dampening.py`
- **test_lucidity_communication_dampening.py** (11 connections) — `server/tests/unit/services/test_lucidity_communication_dampening.py`
- **DampeningResult** (8 connections) — `server/services/lucidity_communication_dampening.py`
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Any** (7 connections)
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._filter_target_players()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **_apply_receiver_effects()** (5 connections) — `server/services/lucidity_communication_dampening.py`
- **UserManager** (5 connections)
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._preload_receiver_mute_data()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **should_block_shout()** (4 connections) — `server/services/lucidity_communication_dampening.py`
- **patch** (4 connections)
- **._collect_room_targets()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_echo_to_sender()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **_apply_sender_effects()** (3 connections) — `server/services/lucidity_communication_dampening.py`
- **_maybe_muffle_fractured_message()** (3 connections) — `server/services/lucidity_communication_dampening.py`
- *... and 38 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (1 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (1 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/services/test_lucidity_communication_dampening.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*