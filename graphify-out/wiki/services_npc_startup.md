# services npc startup

> 13 nodes

## Key Concepts

- **.spawn_npcs_on_startup()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (6 connections) — `server/services/npc_startup_service.py`
- **._determine_spawn_room()** (6 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (5 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (5 connections) — `server/services/npc_startup_service.py`
- **Any** (4 connections)
- **._get_default_room_for_sub_zone()** (3 connections) — `server/services/npc_startup_service.py`
- **Spawn NPCs during server startup.          This method handles the automatic spa** (1 connections) — `server/services/npc_startup_service.py`
- **Spawn all required NPCs.          Args:             required_npcs: List of requi** (1 connections) — `server/services/npc_startup_service.py`
- **Spawn optional NPCs based on spawn probability.          Args:             optio** (1 connections) — `server/services/npc_startup_service.py`
- **Second pass: spawn one instance per definition (that was spawned in required/opt** (1 connections) — `server/services/npc_startup_service.py`
- **Determine the appropriate room for spawning an NPC.          Args:             n** (1 connections) — `server/services/npc_startup_service.py`
- **Get a default room for a given sub-zone.          Args:             sub_zone_id:** (1 connections) — `server/services/npc_startup_service.py`

## Relationships

- [startup npc services](startup_npc_services.md) (6 shared connections)
- [services combat sync](services_combat_sync.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*