# Player Respawn Events

> 276 nodes · cohesion 0.02

## Key Concepts

- **PlayerNameExtractor** (137 connections) — `server/realtime/player_name_utils.py`
- **PlayerEventHandlerUtils** (71 connections) — `server/realtime/player_event_handlers_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **MessageBuilder** (52 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (49 connections) — `server/realtime/room_occupant_manager.py`
- **PlayerRespawnEventHandler** (41 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerEventHandler** (39 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (38 connections) — `server/realtime/npc_event_handlers.py`
- **PlayerRoomEventHandler** (38 connections) — `server/realtime/player_event_handlers_room.py`
- **event_handler.py** (34 connections) — `server/realtime/event_handler.py`
- **player_event_handlers_respawn.py** (32 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_event_handlers.py** (25 connections) — `server/realtime/player_event_handlers.py`
- **PlayerStateEventHandler** (22 connections) — `server/realtime/player_event_handlers_state.py`
- **player_event_handlers_room.py** (16 connections) — `server/realtime/player_event_handlers_room.py`
- **Any** (16 connections) — `server/realtime/player_event_handlers.py`
- **UUID** (16 connections) — `server/realtime/player_event_handlers_room.py`
- **npc_event_handlers.py** (14 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (14 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (11 connections) — `server/realtime/player_event_handlers_utils.py`
- **player_name_utils.py** (11 connections) — `server/realtime/player_name_utils.py`
- **PlayerDeliriumRespawnedEvent** (10 connections) — `server/events/event_types.py`
- **PlayerRespawnedEvent** (10 connections) — `server/events/event_types.py`
- **Any** (10 connections) — `server/realtime/event_handler.py`
- **message_builders.py** (9 connections) — `server/realtime/message_builders.py`
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 251 more nodes in this community*

## Relationships

- [[Realtime Player Event]] (35 shared connections)
- [[Realtime Event Delegation]] (25 shared connections)
- [[Room Occupant Events]] (25 shared connections)
- [[Player Respawn Events]] (22 shared connections)
- [[NPC Admin API]] (20 shared connections)
- [[NPC Occupant Processor]] (20 shared connections)
- [[Distributed Event Bus]] (18 shared connections)
- [[NPC Room Event Handlers]] (18 shared connections)
- [[Player Name Validation]] (18 shared connections)
- [[Respawn Occupant Enrichment]] (13 shared connections)
- [[Player Event Handler Tests]] (8 shared connections)
- [[Realtime Message Builders]] (7 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 1084 (73%)
- INFERRED: 409 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
