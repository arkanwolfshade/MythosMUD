# server realtime messaging personal message

> 35 nodes

## Key Concepts

- **PersonalMessageSender** (22 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (17 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **personal_message_sender.py** (16 connections) — `server/realtime/messaging/personal_message_sender.py`
- **asyncio** (8 connections)
- **.send_message()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_send_message_fans_out_to_all_listed_sockets()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_outer_exception()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_empty_runtime_error_is_debug()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **sender()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_get_delivery_stats()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_prepare_payload_too_large()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_via_websocket()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_queues_when_offline()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **LogCaptureFixture** (2 connections)
- **fixture** (1 connections)
- **Personal message delivery for connection management. This module provides…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- *... and 10 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [deque](deque.md) (3 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (3 shared connections)
- [sendpersonalmessage](sendpersonalmessage.md) (2 shared connections)
- [server realtime payload optimizer](server_realtime_payload_optimizer.md) (2 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (2 shared connections)
- [server realtime connection initialization initialize](server_realtime_connection_initialization_initialize.md) (1 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 78 (86%)
- INFERRED: 13 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*