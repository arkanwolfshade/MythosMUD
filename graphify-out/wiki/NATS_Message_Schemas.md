# NATS Message Schemas

> 54 nodes

## Key Concepts

- **test_nats_messages.py** (22 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **validate_message()** (14 connections) — `server/schemas/realtime/nats_messages.py`
- **ChatMessageSchema** (12 connections) — `server/schemas/realtime/nats_messages.py`
- **BaseMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **EventMessageSchema** (11 connections) — `server/schemas/realtime/nats_messages.py`
- **__init__.py** (9 connections) — `server/schemas/realtime/__init__.py`
- **nats_messages.py** (9 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_chat_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **validate_event_message()** (7 connections) — `server/schemas/realtime/nats_messages.py`
- **test_base_message_schema_invalid_timestamp()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_invalid_channel()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_content_validation()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema_empty_event_type()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_chat_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_event_message()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_chat()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_validate_message_event()** (4 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **Any** (3 connections)
- **test_base_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_base_message_schema_validate_timestamp()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_chat_message_schema_validate_channel()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **test_event_message_schema_validate_event_type()** (3 connections) — `server/tests/unit/schemas/test_nats_messages.py`
- **.validate_timestamp()** (2 connections) — `server/schemas/realtime/nats_messages.py`
- *... and 29 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Command Testing Guide](Command_Testing_Guide.md) (3 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (2 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (1 shared connections)
- [Services Combat Persistence](Services_Combat_Persistence.md) (1 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)

## Source Files

- `server/schemas/realtime/__init__.py`
- `server/schemas/realtime/nats_messages.py`
- `server/tests/unit/schemas/test_nats_messages.py`

## Audit Trail

- EXTRACTED: 176 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*