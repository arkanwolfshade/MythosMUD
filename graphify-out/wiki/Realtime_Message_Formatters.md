# Realtime Message Formatters

> 20 nodes · cohesion 0.19

## Key Concepts

- **format_message_content()** (17 connections) — `server/realtime/message_formatters.py`
- **test_message_formatters.py** (14 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'say' channel messages.** (7 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_nats_error()** (4 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_admin()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_emote()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_global()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_local()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_pose()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_say()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_system()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_unknown_channel()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_whisper()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_whisper_for_recipient()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Format message content based on channel type and sender name.      Args:** (1 connections) — `server/realtime/message_formatters.py`
- **Unit tests for message formatters.  Tests the message_formatters module function** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'whisper' channel messages (default).** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'whisper' for recipient as 'X whispers to** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'system' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() handles NATSError.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`

## Relationships

- [[NPC Admin API]] (2 shared connections)
- [[NATS Chat Broadcasting]] (2 shared connections)
- [[Combat Domain Events]] (2 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
