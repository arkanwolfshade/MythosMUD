# NPC Room Event Handlers

> 31 nodes · cohesion 0.10

## Key Concepts

- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **Extract spawn_message from behavior_config.          Args:             behavior_** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the spawn message for an NPC from its behavior_config.          If no custom** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the name of an NPC by ID.          Args:             npc_id: The NPC ID** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Determine the direction from one room to another by checking room exits.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handles all NPC-related real-time events.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the departure message for an NPC from its behavior_config.          If no cu** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Send a message to all players in a room.          Args:             room_id: The** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handle NPC entering a room.          This method broadcasts NPC appearance and t** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handle NPC leaving a room.          This method broadcasts NPC departure and tri** (1 connections) — `server/realtime/npc_event_handlers.py`
- *... and 6 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (16 shared connections)
- [Combat UUID Display Bug](Combat_UUID_Display_Bug.md) (2 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)
- [Schemas Items Item](Schemas_Items_Item.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 116 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*