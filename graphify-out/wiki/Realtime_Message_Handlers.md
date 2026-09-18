# Realtime Message Handlers

> 181 nodes

## Key Concepts

- **test_websocket_handler_core.py** (47 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **test_message_handlers.py** (35 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handler_factory.py** (32 connections) — `server/realtime/message_handler_factory.py`
- **test_message_handler_factory.py** (29 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **asyncio** (28 connections)
- **message_handlers.py** (27 connections) — `server/realtime/message_handlers.py`
- **websocket_messages.py** (26 connections) — `server/schemas/realtime/websocket_messages.py`
- **schemas/realtime/__init__.py** (25 connections) — `server/schemas/realtime/__init__.py`
- **test_websocket_message_schema_registry.py** (23 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- **CommandMessage** (17 connections) — `server/schemas/realtime/websocket_messages.py`
- **ChatMessage** (16 connections) — `server/schemas/realtime/websocket_messages.py`
- **CommandData** (16 connections) — `server/schemas/realtime/websocket_messages.py`
- **handle_follow_response_message()** (15 connections) — `server/realtime/message_handlers.py`
- **asyncio** (15 connections)
- **FollowResponseMessage** (14 connections) — `server/schemas/realtime/websocket_messages.py`
- **PartyInviteResponseMessage** (14 connections) — `server/schemas/realtime/websocket_messages.py`
- **ClientErrorReportMessage** (13 connections) — `server/schemas/realtime/websocket_messages.py`
- **GameCommandMessage** (13 connections) — `server/schemas/realtime/websocket_messages.py`
- **PingMessage** (13 connections) — `server/schemas/realtime/websocket_messages.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **handle_command_message()** (12 connections) — `server/realtime/message_handlers.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **ChatData** (10 connections) — `server/schemas/realtime/websocket_messages.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **_discriminator_values()** (10 connections) — `server/tests/unit/realtime/test_websocket_message_schema_registry.py`
- *... and 156 more nodes in this community*

## Relationships

- [Community 280](Community_280.md) (36 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (14 shared connections)
- [Community 306](Community_306.md) (12 shared connections)
- [Community 243](Community_243.md) (10 shared connections)
- [Community 111](Community_111.md) (9 shared connections)
- [Community 154](Community_154.md) (9 shared connections)
- [Community 71](Community_71.md) (6 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (5 shared connections)
- [Community 62](Community_62.md) (4 shared connections)
- [Community 93](Community_93.md) (4 shared connections)
- [Community 336](Community_336.md) (4 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (4 shared connections)

## Source Files

- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/realtime/websocket_handler.py`
- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/websocket_messages.py`
- `server/tests/unit/realtime/test_message_handler_factory.py`
- `server/tests/unit/realtime/test_message_handlers.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_validation_errors.py`
- `server/tests/unit/realtime/test_websocket_message_schema_registry.py`

## Audit Trail

- EXTRACTED: 447 (87%)
- INFERRED: 67 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*