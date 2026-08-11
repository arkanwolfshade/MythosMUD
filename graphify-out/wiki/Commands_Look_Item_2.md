# Commands Look Item

> 19 nodes

## Key Concepts

- **Any** (8 connections)
- **.spawn_npc_instance()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.despawn_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.move_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_instances()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_system_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **Spawn a new NPC instance.          Args:             definition_id: ID of the NP** (1 connections) — `server/services/npc_instance_service.py`
- **Despawn an NPC instance.          Args:             npc_id: ID of the NPC to des** (1 connections) — `server/services/npc_instance_service.py`
- **Move an NPC instance to a different room.          Args:             npc_id: ID** (1 connections) — `server/services/npc_instance_service.py`
- **Get all active NPC instances.          Returns:             List of NPC instance** (1 connections) — `server/services/npc_instance_service.py`
- **Get detailed stats for a specific NPC instance.          Args:             npc_i** (1 connections) — `server/services/npc_instance_service.py`
- **Get NPC population statistics.          Returns:             Dictionary with pop** (1 connections) — `server/services/npc_instance_service.py`
- **Get NPC zone statistics.          Returns:             Dictionary with zone stat** (1 connections) — `server/services/npc_instance_service.py`
- **Get system-wide NPC statistics.          Returns:             Dictionary with sy** (1 connections) — `server/services/npc_instance_service.py`
- **Extract zone key from room ID.          Args:             room_id: Room ID like** (1 connections) — `server/services/npc_instance_service.py`

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (9 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (1 shared connections)

## Source Files

- `server/services/npc_instance_service.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*