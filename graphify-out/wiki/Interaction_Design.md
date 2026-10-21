# Interaction Design

> 13 nodes · cohesion 0.17

## Key Concepts

- **.move_npc_to_room()** (7 connections) — `server/npc/movement_integration.py`
- **._get_room_objects()** (4 connections) — `server/npc/movement_integration.py`
- **._is_npc_in_combat()** (4 connections) — `server/npc/movement_integration.py`
- **._update_npc_instance_room_tracking()** (4 connections) — `server/npc/movement_integration.py`
- **._update_room_occupancy()** (4 connections) — `server/npc/movement_integration.py`
- **._validate_room_ids()** (3 connections) — `server/npc/movement_integration.py`
- **Room** (2 connections)
- **Return True if the NPC is currently in combat (blocks normal movement).** (1 connections) — `server/npc/movement_integration.py`
- **Get room objects and validate they exist. Args: npc_id: ID of the NPC…** (1 connections) — `server/npc/movement_integration.py`
- **Update room occupancy by removing NPC from source and adding to destination.…** (1 connections) — `server/npc/movement_integration.py`
- **Update NPC instance room tracking for occupant queries. Args: npc_id: ID of the…** (1 connections) — `server/npc/movement_integration.py`
- **Move an NPC to a different room with full integration. This method provides…** (1 connections) — `server/npc/movement_integration.py`
- **Validate room IDs for NPC movement. Args: npc_id: ID of the NPC from_room_id:…** (1 connections) — `server/npc/movement_integration.py`

## Relationships

- [StatusEffect](StatusEffect.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)

## Source Files

- `server/npc/movement_integration.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*