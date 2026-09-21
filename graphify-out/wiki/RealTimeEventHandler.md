# RealTimeEventHandler

> 41 nodes

## Key Concepts

- **RealTimeEventHandler** (35 connections) — `server/realtime/event_handler.py`
- **._create_player_entered_message()** (3 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (3 connections) — `server/realtime/event_handler.py`
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
- **._subscribe_to_events()** (3 connections) — `server/realtime/event_handler.py`
- **test_event_handler_init()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_init_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **._get_next_sequence()** (2 connections) — `server/realtime/event_handler.py`
- **._get_room_occupants()** (2 connections) — `server/realtime/event_handler.py`
- **.shutdown()** (2 connections) — `server/realtime/event_handler.py`
- **UUID** (2 connections)
- **Get the next sequence number for events.** (1 connections) — `server/realtime/event_handler.py`
- **Subscribe to relevant game events.** (1 connections) — `server/realtime/event_handler.py`
- **Delegate player entered event to specialized handler.** (1 connections) — `server/realtime/event_handler.py`
- **Delegate player left event to specialized handler.** (1 connections) — `server/realtime/event_handler.py`
- *... and 16 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [MessageBuilder](MessageBuilder.md) (2 shared connections)
- [get_viewer_phantom_names](get_viewer_phantom_names.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [NPCEventHandler](NPCEventHandler.md) (1 shared connections)
- [event_handler](event_handler.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 64 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*