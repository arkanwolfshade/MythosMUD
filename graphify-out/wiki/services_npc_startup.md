# services npc startup

> 33 nodes

## Key Concepts

- **PersonalMessageSender** (21 connections) — `server/realtime/messaging/personal_message_sender.py`
- **personal_message_sender.py** (15 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (14 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_empty_runtime_error_is_debug()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_get_delivery_stats()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_outer_exception()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **sender()** (2 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_via_websocket()** (2 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_queues_when_offline()** (2 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_prepare_payload_too_large()** (2 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_disconnect()** (2 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **LogCaptureFixture** (2 connections)
- **Messaging components for connection management.  This package provides modular m** (1 connections) — `server/realtime/messaging/__init__.py`
- **Personal message delivery for connection management.  This module provides direc** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Sends personal messages to individual players.      This class provides:     - P** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- *... and 8 more nodes in this community*

## Relationships

- [taunt combat commands](taunt_combat_commands.md) (7 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (5 shared connections)
- [combat configuration service](combat_configuration_service.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [npc event handlers](npc_event_handlers.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 135 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*