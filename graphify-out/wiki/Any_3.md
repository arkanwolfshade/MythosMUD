# Any

> 23 nodes

## Key Concepts

- **Any** (10 connections)
- **.move_npc_instance()** (5 connections) — `server/services/npc_instance_service.py`
- **._apply_npc_room_move()** (4 connections) — `server/services/npc_instance_service.py`
- **._check_npc_move_blocked_by_combat()** (4 connections) — `server/services/npc_instance_service.py`
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.spawn_npc_instance()** (4 connections) — `server/services/npc_instance_service.py`
- **.despawn_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_instances()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_system_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **Despawn an NPC instance. Args: npc_id: ID of the NPC to despawn reason: Reason…** (1 connections) — `server/services/npc_instance_service.py`
- **Return a failure result dict if the NPC is in combat, else None to allow the…** (1 connections) — `server/services/npc_instance_service.py`
- **Move the NPC to new_room_id via move_to_room(), or set current_room_id directly.** (1 connections) — `server/services/npc_instance_service.py`
- **Move an NPC instance to a different room. Args: npc_id: ID of the NPC to move…** (1 connections) — `server/services/npc_instance_service.py`
- **Get all active NPC instances. Returns: List of NPC instance information** (1 connections) — `server/services/npc_instance_service.py`
- **Get detailed stats for a specific NPC instance. Args: npc_id: ID of the NPC…** (1 connections) — `server/services/npc_instance_service.py`
- **Get NPC population statistics. Returns: Dictionary with population statistics** (1 connections) — `server/services/npc_instance_service.py`
- **Get NPC zone statistics. Returns: Dictionary with zone statistics** (1 connections) — `server/services/npc_instance_service.py`
- **Get system-wide NPC statistics. Returns: Dictionary with system statistics** (1 connections) — `server/services/npc_instance_service.py`
- **Extract zone key from room ID. Args: room_id: Room ID like…** (1 connections) — `server/services/npc_instance_service.py`
- **Spawn a new NPC instance. Args: definition_id: ID of the NPC definition to…** (1 connections) — `server/services/npc_instance_service.py`

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [npc_database.py](npc_database.py.md) (1 shared connections)

## Source Files

- `server/services/npc_instance_service.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*