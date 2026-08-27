# test_admin_shutdown_command.py

> 47 nodes

## Key Concepts

- **test_message_handlers.py** (26 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **asyncio** (16 connections)
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **Any** (6 connections)
- **WebSocket** (6 connections)
- **test_handle_chat_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_chat_message_no_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_client_error_report_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_args()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_command_message_no_command()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_accept_success()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_decline()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_invalid_request_id()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_follow_response_no_container()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_accept()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_decline()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_invalid()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_party_invite_response_no_container()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message_with_data()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- *... and 22 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (7 shared connections)
- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [ItemInstance](ItemInstance.md) (5 shared connections)
- [player_combat_service_support.py](player_combat_service_support.py.md) (5 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 110 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*