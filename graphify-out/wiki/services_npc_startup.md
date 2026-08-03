# services npc startup

> 15 nodes

## Key Concepts

- **PersonalMessageSender** (21 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (14 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
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
- **Sends personal messages to individual players.      This class provides:     - P** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Unit tests for PersonalMessageSender.** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **E2E teardown: send after client drop must not warn.** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`

## Relationships

- [startup services npc](startup_services_npc.md) (6 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (5 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 62 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*