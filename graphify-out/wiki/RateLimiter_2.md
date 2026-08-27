# RateLimiter

> 26 nodes

## Key Concepts

- **format_message_content()** (16 connections) — `server/realtime/message_formatters.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
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
- **Format message content based on channel type and sender name. Args: channel:…** (1 connections) — `server/realtime/message_formatters.py`
- **Unit tests for message formatters. Tests the message_formatters module…** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'say' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'local' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'global' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'emote' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'pose' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'whisper' channel messages (default).** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'whisper' for recipient as 'X whispers to…** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'system' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats 'admin' channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **Test format_message_content() formats unknown channel messages.** (1 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- *... and 1 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (2 shared connections)
- [Argon2 Password Hashing Best Practices](Argon2_Password_Hashing_Best_Practices.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*