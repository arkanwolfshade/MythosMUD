# Aggressive Mob NPC

> 225 nodes · cohesion 0.01

## Key Concepts

- **IdleMovementHandler** (38 connections) — `server/npc/idle_movement.py`
- **AggressiveMobNPC** (33 connections) — `server/npc/aggressive_mob_npc.py`
- **PassiveMobNPC** (30 connections) — `server/npc/passive_mob_npc.py`
- **NPCEventReactionSystem** (25 connections) — `server/npc/event_reaction_system.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **npc.py** (21 connections) — `server/models/npc.py`
- **ShopkeeperNPC** (18 connections) — `server/npc/shopkeeper_npc.py`
- **aggressive_mob_npc.py** (17 connections) — `server/npc/aggressive_mob_npc.py`
- **threading.py** (17 connections) — `server/npc/threading.py`
- **passive_mob_npc.py** (16 connections) — `server/npc/passive_mob_npc.py`
- **idle_movement.py** (15 connections) — `server/npc/idle_movement.py`
- **behaviors.py** (13 connections) — `server/npc/behaviors.py`
- **NPCActionMessage** (13 connections) — `server/npc/threading.py`
- **Any** (12 connections) — `server/npc/threading.py`
- **NPCActionType** (11 connections) — `server/npc/threading.py`
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **test_aggressive_mob_npc.py** (9 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.execute_idle_movement()** (8 connections) — `server/npc/idle_movement.py`
- **._should_idle_move_inner()** (8 connections) — `server/npc/idle_movement.py`
- **_RoomPersistence** (7 connections) — `server/npc/aggressive_mob_npc.py`
- **_npc_id_str()** (7 connections) — `server/npc/idle_movement.py`
- **test_npc_base.py** (7 connections) — `server/tests/unit/npc/test_npc_base.py`
- **NPCActionMessage** (7 connections) — `server/npc/passive_mob_npc.py`
- **._attack_target_impl()** (6 connections) — `server/npc/aggressive_mob_npc.py`
- *... and 200 more nodes in this community*

## Relationships

- [[NPC Death Lifecycle]] (24 shared connections)
- [[Distributed Event Bus]] (22 shared connections)
- [[NPC Admin API]] (17 shared connections)
- [[NPC Services Bundle]] (10 shared connections)
- [[NPC Definition Schemas]] (9 shared connections)
- [[NPC Occupant Verification]] (7 shared connections)
- [[NPC Movement Integration]] (6 shared connections)
- [[Npc Event Reaction]] (5 shared connections)
- [[Npc Idle Movement]] (4 shared connections)
- [[NPC Combat Events]] (3 shared connections)
- [[NPC Admin Commands]] (2 shared connections)
- [[Application DI Bundles]] (2 shared connections)

## Source Files

- `server/models/npc.py`
- `server/npc/__init__.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/behaviors.py`
- `server/npc/event_reaction_system.py`
- `server/npc/idle_movement.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`
- `server/tests/unit/npc/test_npc_base.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 726 (91%)
- INFERRED: 70 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
