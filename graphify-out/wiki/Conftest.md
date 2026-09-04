# Conftest

> 37 nodes

## Key Concepts

- **realtime/conftest.py** (24 connections) — `server/tests/unit/realtime/conftest.py`
- **fixture** (15 connections)
- **PlayerRoomEventHandlerDeps** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **player_room_event_handler()** (5 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/conftest.py`
- **nats_message_handler()** (4 connections) — `server/tests/unit/realtime/conftest.py`
- **.__init__()** (3 connections) — `server/realtime/player_event_handlers_room.py`
- **mock_chat_logger()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_logger()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_message_builder()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_name_extractor()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_nats_service()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_occupant_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_room_sync_service()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_subject_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_user_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **mock_ws_connection_manager()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **Constructor bundle so Lizard does not count eight service args.** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Initialize room event handler from a deps bundle.** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Shared fixtures for realtime unit tests. Provides fixtures used by NATS message…** (1 connections) — `server/tests/unit/realtime/conftest.py`
- **Create a mock occupant manager.** (1 connections) — `server/tests/unit/realtime/conftest.py`
- **Create a mock PlayerEventHandlerUtils.** (1 connections) — `server/tests/unit/realtime/conftest.py`
- **Create a mock logger.** (1 connections) — `server/tests/unit/realtime/conftest.py`
- *... and 12 more nodes in this community*

## Relationships

- [Player Event Handlers Room](Player_Event_Handlers_Room.md) (5 shared connections)
- [Player Event Handlers Utils](Player_Event_Handlers_Utils.md) (3 shared connections)
- [Nats Message Handler Broadcast](Nats_Message_Handler_Broadcast.md) (2 shared connections)
- [Message Builders](Message_Builders.md) (1 shared connections)
- [Test Player Name Utils](Test_Player_Name_Utils.md) (1 shared connections)
- [Npc Occupant Processor](Npc_Occupant_Processor.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 59 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*