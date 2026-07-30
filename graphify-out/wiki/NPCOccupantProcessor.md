# NPCOccupantProcessor

> 42 nodes

## Key Concepts

- **RoomIDUtils** (20 connections) — `server/realtime/room_id_utils.py`
- **NPCOccupantProcessor** (18 connections) — `server/realtime/npc_occupant_processor.py`
- **Any** (11 connections)
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **.query_npcs_for_room()** (6 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._validate_npc_room_tracking()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._should_include_npc_in_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._scan_active_npcs_for_room()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_lifecycle_manager_for_filtering()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_fallback_npcs()** (5 connections) — `server/realtime/npc_occupant_processor.py`
- **._get_npc_room_id()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **._filter_single_fallback_npc()** (4 connections) — `server/realtime/npc_occupant_processor.py`
- **.get_room_occupants()** (4 connections) — `server/realtime/room_occupant_manager.py`
- **.process_npcs_for_occupants()** (3 connections) — `server/realtime/npc_occupant_processor.py`
- **.__init__()** (3 connections) — `server/realtime/room_id_utils.py`
- **Any** (3 connections)
- **.separate_occupants_by_type()** (3 connections) — `server/realtime/room_occupant_manager.py`
- **.get_canonical_room_id()** (2 connections) — `server/realtime/room_id_utils.py`
- **UUID** (2 connections)
- **Processes NPC occupants for rooms.** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Initialize NPC occupant processor.          Args:             connection_manager** (1 connections) — `server/realtime/npc_occupant_processor.py`
- **Get and validate NPC lifecycle manager.          Args:             room_id: The** (1 connections) — `server/realtime/npc_occupant_processor.py`
- *... and 17 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (10 shared connections)
- [npc occupant processor](npc_occupant_processor.md) (10 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (5 shared connections)
- [command parser()](command_parser%28%29.md) (1 shared connections)
- [container websocket events](container_websocket_events.md) (1 shared connections)
- [login grace period](login_grace_period.md) (1 shared connections)

## Source Files

- `server/realtime/npc_occupant_processor.py`
- `server/realtime/room_id_utils.py`
- `server/realtime/room_occupant_manager.py`

## Audit Trail

- EXTRACTED: 148 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*