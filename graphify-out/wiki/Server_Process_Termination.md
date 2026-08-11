# Server Process Termination

> 23 nodes

## Key Concepts

- **look_container.py** (23 connections) — `server/commands/look_container.py`
- **Any** (14 connections)
- **_find_container_in_room_or_equipped()** (14 connections) — `server/commands/look_container.py`
- **_find_container_via_inner_container()** (13 connections) — `server/commands/look_container.py`
- **_handle_container_look()** (11 connections) — `server/commands/look_container.py`
- **_try_lookup_container_implicit()** (10 connections) — `server/commands/look_container.py`
- **_matches_item_instance_id()** (8 connections) — `server/commands/look_container.py`
- **_try_match_container_component()** (8 connections) — `server/commands/look_container.py`
- **_matches_name_or_slot()** (7 connections) — `server/commands/look_container.py`
- **_get_container_data_from_component()** (7 connections) — `server/commands/look_container.py`
- **_extract_container_metadata()** (6 connections) — `server/commands/look_container.py`
- **_find_container_via_wearable_service()** (6 connections) — `server/commands/look_container.py`
- **Container look functionality for MythosMUD.  This module handles looking at cont** (1 connections) — `server/commands/look_container.py`
- **Find container via inner_container_id from item.** (1 connections) — `server/commands/look_container.py`
- **Check if item instance IDs match.** (1 connections) — `server/commands/look_container.py`
- **Check if container matches by name or slot.** (1 connections) — `server/commands/look_container.py`
- **Get container data from component ID.** (1 connections) — `server/commands/look_container.py`
- **Extract metadata from container component.** (1 connections) — `server/commands/look_container.py`
- **Try to match a container component and return container data if found.** (1 connections) — `server/commands/look_container.py`
- **Find container via wearable container service.** (1 connections) — `server/commands/look_container.py`
- **Find container in room or equipped items.      Returns:         tuple: (containe** (1 connections) — `server/commands/look_container.py`
- **Handle looking at a specific container.** (1 connections) — `server/commands/look_container.py`
- **Try to find and display a container in implicit lookup.** (1 connections) — `server/commands/look_container.py`

## Relationships

- [Look Container Command](Look_Container_Command.md) (21 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (18 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (5 shared connections)
- [Health Check Service](Health_Check_Service.md) (4 shared connections)
- [Client ASCII Map API](Client_ASCII_Map_API.md) (4 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (3 shared connections)
- [Chat Archive Advanced](Chat_Archive_Advanced.md) (2 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Look Player Command](Look_Player_Command.md) (1 shared connections)

## Source Files

- `server/commands/look_container.py`

## Audit Trail

- EXTRACTED: 138 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*