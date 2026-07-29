# message formatters

> 75 nodes

## Key Concepts

- **NATSMessageBroadcastMixin** (25 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **._broadcast_to_room_with_filtering()** (12 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **NATSMessageHandlerMixinBase** (10 connections) — `server/realtime/nats_message_handler_base.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **Any** (7 connections)
- **._send_messages_to_players()** (7 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Test format_message_content() formats 'say' channel messages.** (7 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **._apply_dampening_and_send_message()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_player_lucidity_tier()** (6 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **apply_communication_dampening()** (6 connections) — `server/services/lucidity_communication_dampening.py`
- **UserManager** (5 connections)
- **._filter_target_players()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._echo_message_to_sender()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._format_message_for_receiver()** (5 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **nats_message_handler_base.py** (5 connections) — `server/realtime/nats_message_handler_base.py`
- **._preload_receiver_mute_data()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._extract_chat_event_info()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._check_player_mute_status()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._get_user_manager()** (4 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_format_message_content_nats_error()** (4 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **._collect_room_targets()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **._should_echo_to_sender()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- *... and 50 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (12 shared connections)
- [main()](main%28%29.md) (7 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [Any](Any.md) (3 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [message filtering](message_filtering.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/lucidity_communication_dampening.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 266 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*