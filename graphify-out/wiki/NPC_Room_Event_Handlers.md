# NPC Room Event Handlers

> 32 nodes · cohesion 0.07

## Key Concepts

- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **NPCLeftRoom** (4 connections) — `server/realtime/npc_event_handlers.py`
- **Initialize the NPC event handler.          Args:             connection_manager:** (2 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (2 connections) — `server/realtime/npc_event_handlers.py`
- **NPCEnteredRoom** (2 connections) — `server/realtime/npc_event_handlers.py`
- **Extract spawn_message from behavior_config.          Args:             behavior_** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the spawn message for an NPC from its behavior_config.          If no custom** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the name of an NPC by ID.          Args:             npc_id: The NPC ID** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Determine the direction from one room to another by checking room exits.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the departure message for an NPC from its behavior_config.          If no cu** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handle NPC entering a room.          This method broadcasts NPC appearance and t** (1 connections) — `server/realtime/npc_event_handlers.py`
- *... and 7 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (18 shared connections)
- [[NPC Occupant Verification]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Combat Player Broadcasts]] (2 shared connections)
- [[Realtime Player Event]] (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 97 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
