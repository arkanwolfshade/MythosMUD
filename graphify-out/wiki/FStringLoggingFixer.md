# FStringLoggingFixer

> 33 nodes

## Key Concepts

- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **Extract spawn_message from behavior_config. Args: behavior_config: The parsed…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the spawn message for an NPC from its behavior_config. If no custom spawn…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the name of an NPC by ID. Args: npc_id: The NPC ID Returns: NPC name or…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Determine the direction from one room to another by checking room exits. Args:…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Handles all NPC-related real-time events.** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Get the departure message for an NPC from its behavior_config. If no custom…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Send a message to all players in a room. Args: room_id: The room ID message:…** (1 connections) — `server/realtime/npc_event_handlers.py`
- **Initialize the NPC event handler. Args: connection_manager: ConnectionManager…** (1 connections) — `server/realtime/npc_event_handlers.py`
- *... and 8 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (3 shared connections)
- [ui-v2/types.ts](ui-v2-types.ts.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [test_event_publisher.py](test_event_publisher.py.md) (2 shared connections)
- [_container_data_to_dict](_container_data_to_dict.md) (2 shared connections)
- [ChatLogger](ChatLogger.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 69 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*