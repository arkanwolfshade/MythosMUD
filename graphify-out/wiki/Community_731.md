# Community 731

> 23 nodes

## Key Concepts

- **PersonalMessageSender** (24 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (17 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **asyncio** (10 connections)
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_prepare_payload_too_large()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_when_player_id_is_a_string()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_fans_out_to_all_listed_sockets()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_outer_exception()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_reports_failure_for_non_uuid_player_id()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_empty_runtime_error_is_debug()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **sender()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_via_websocket()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_queues_when_offline()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_get_delivery_stats()** (2 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **LogCaptureFixture** (2 connections)
- **fixture** (1 connections)
- **Sends personal messages to individual players. This class provides: - Personal…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Unit tests for PersonalMessageSender.** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **E2E teardown: send after client drop must not warn.** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **Regression: a str player_id must still hit the UUID-keyed connection map.…** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **A malformed id degrades to a failed delivery rather than breaking the caller's…** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **Occupancy/who/chat ride the full player_websockets list (#610).** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`

## Relationships

- [Community 942](Community_942.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (3 shared connections)
- [Community 501](Community_501.md) (1 shared connections)
- [Community 226](Community_226.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 46 (78%)
- INFERRED: 13 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*