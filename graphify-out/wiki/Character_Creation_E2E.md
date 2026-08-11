# Character Creation E2E

> 152 nodes

## Key Concepts

- **PlayerLeftRoom** (51 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **npc_event_handlers.py** (16 connections) — `server/realtime/npc_event_handlers.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **message_builders.py** (9 connections) — `server/realtime/message_builders.py`
- **Any** (9 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 127 more nodes in this community*

## Relationships

- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (19 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (14 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (12 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (11 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (10 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (8 shared connections)
- [Services Combat Initialization](Services_Combat_Initialization.md) (8 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (6 shared connections)
- [Look Item Commands](Look_Item_Commands.md) (6 shared connections)
- [API Type Guards](API_Type_Guards.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/spawning_service.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 650 (93%)
- INFERRED: 51 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*