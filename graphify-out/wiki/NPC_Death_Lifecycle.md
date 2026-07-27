# NPC Death Lifecycle

> 223 nodes · cohesion 0.02

## Key Concepts

- **NPCBase** (92 connections) — `server/npc/npc_base.py`
- **NPCLifecycleManager** (86 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_manager.py** (38 connections) — `server/npc/lifecycle_manager.py`
- **NPCDied** (34 connections) — `server/events/event_types.py`
- **NPCThreadManager** (32 connections) — `server/npc/threading.py`
- **NPCLifecycleState** (28 connections) — `server/npc/lifecycle_types.py`
- **RoomOccupantsRefreshRequested** (27 connections) — `server/events/event_types.py`
- **NPCLifecycleEvent** (25 connections) — `server/npc/lifecycle_types.py`
- **NPCLifecycleRecord** (25 connections) — `server/npc/lifecycle_types.py`
- **NPCDefinition** (22 connections) — `server/npc/lifecycle_manager.py`
- **lifecycle_death.py** (19 connections) — `server/npc/lifecycle_death.py`
- **_LifecycleManagerForDeath** (16 connections) — `server/npc/lifecycle_death.py`
- **_SpawningServiceProtocol** (16 connections) — `server/npc/lifecycle_manager.py`
- **_SpawnTrackedNPC** (16 connections) — `server/npc/lifecycle_manager.py`
- **NPCLifecycleRecord** (14 connections) — `server/npc/lifecycle_manager.py`
- **._spawn_npc_impl()** (13 connections) — `server/npc/lifecycle_manager.py`
- **NPCThreadManager** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCDied** (12 connections) — `server/npc/lifecycle_death.py`
- **AsyncPersistenceLayer** (12 connections) — `server/npc/lifecycle_manager.py`
- **EventBus** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCBase** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCDied** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCEnteredRoom** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCLeftRoom** (12 connections) — `server/npc/lifecycle_manager.py`
- **NPCPopulationController** (12 connections) — `server/npc/lifecycle_manager.py`
- *... and 198 more nodes in this community*

## Relationships

- [[NPC Services Bundle]] (56 shared connections)
- [[Distributed Event Bus]] (55 shared connections)
- [[Aggressive Mob NPC]] (24 shared connections)
- [[NPC Admin API]] (16 shared connections)
- [[Player Combat XP]] (13 shared connections)
- [[NPC Definition Schemas]] (10 shared connections)
- [[Time Event Consumer]] (9 shared connections)
- [[Npc Config Parsing]] (7 shared connections)
- [[NPC Movement Integration]] (6 shared connections)
- [[Async Persistence Layer]] (5 shared connections)
- [[NPC Occupant Verification]] (4 shared connections)
- [[Quest Game Events]] (3 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/room.py`
- `server/npc/lifecycle_death.py`
- `server/npc/lifecycle_despawn.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_types.py`
- `server/npc/npc_base.py`
- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 719 (66%)
- INFERRED: 367 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
