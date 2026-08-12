# RealTimeEventHandler

> 57 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **event_handler()** (7 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **._create_player_entered_message()** (4 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (4 connections) — `server/realtime/event_handler.py`
- **Any** (4 connections)
- **fixture** (4 connections)
- **._get_room_occupants()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **._send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/event_handler.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **._send_room_occupants_update_internal()** (3 connections) — `server/realtime/event_handler.py`
- **._subscribe_to_events()** (3 connections) — `server/realtime/event_handler.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_task_registry()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- *... and 32 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (22 shared connections)
- [Protocol](Protocol.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [chat_logger](chat_logger.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 90 (83%)
- INFERRED: 18 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*