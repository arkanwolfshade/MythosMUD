# startup npc services

> 30 nodes

## Key Concepts

- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **test_format_message_content_nats_error()** (4 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_say()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_local()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_global()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_emote()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_pose()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_whisper()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_whisper_for_recipient()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_system()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_admin()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_unknown_channel()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Message formatting utilities for NATS message handler.** (1 connections) — `server/realtime/message_formatters.py`
- **Format message content based on channel type and sender name.      Args:** (1 connections) — `server/realtime/message_formatters.py`
- **Room broadcast / mute / dampening mixin for NATSMessageHandler.  Extracted to ke** (1 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **Unit tests for message formatters.  Tests the message_formatters module function** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'say' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'local' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'global' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'emote' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'pose' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'whisper' channel messages (default).** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- *... and 5 more nodes in this community*

## Relationships

- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (3 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)
- [services user manager](services_user_manager.md) (1 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 108 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*