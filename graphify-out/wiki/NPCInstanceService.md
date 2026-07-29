# NPCInstanceService

> 23 nodes

## Key Concepts

- **NPCInstanceService** (20 connections) — `server/services/npc_instance_service.py`
- **Any** (8 connections)
- **.get_population_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **.get_zone_stats()** (4 connections) — `server/services/npc_instance_service.py`
- **._extract_zone_from_room_id()** (4 connections) — `server/services/npc_instance_service.py`
- **.spawn_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.despawn_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.move_npc_instance()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_instances()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_npc_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **.get_system_stats()** (3 connections) — `server/services/npc_instance_service.py`
- **test_npc_instance_service_init()** (3 connections) — `server/tests/unit/services/test_npc_instance_service.py`
- **High-level API wrapper for NPC instance management.      This service provides a** (1 connections) — `server/services/npc_instance_service.py`
- **Spawn a new NPC instance.          Args:             definition_id: ID of the NP** (1 connections) — `server/services/npc_instance_service.py`
- **Despawn an NPC instance.          Args:             npc_id: ID of the NPC to des** (1 connections) — `server/services/npc_instance_service.py`
- **Move an NPC instance to a different room.          Args:             npc_id: ID** (1 connections) — `server/services/npc_instance_service.py`
- **Get all active NPC instances.          Returns:             List of NPC instance** (1 connections) — `server/services/npc_instance_service.py`
- **Get detailed stats for a specific NPC instance.          Args:             npc_i** (1 connections) — `server/services/npc_instance_service.py`
- **Get NPC population statistics.          Returns:             Dictionary with pop** (1 connections) — `server/services/npc_instance_service.py`
- **Get NPC zone statistics.          Returns:             Dictionary with zone stat** (1 connections) — `server/services/npc_instance_service.py`
- **Get system-wide NPC statistics.          Returns:             Dictionary with sy** (1 connections) — `server/services/npc_instance_service.py`
- **Extract zone key from room ID.          Args:             room_id: Room ID like** (1 connections) — `server/services/npc_instance_service.py`
- **Test NPCInstanceService initialization.** (1 connections) — `server/tests/unit/services/test_npc_instance_service.py`

## Relationships

- [.initialize()](initialize%28%29.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [test npc instance service](test_npc_instance_service.md) (2 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [.get instance()](get_instance%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [npc instance service()](npc_instance_service%28%29.md) (1 shared connections)

## Source Files

- `server/services/npc_instance_service.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 71 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*