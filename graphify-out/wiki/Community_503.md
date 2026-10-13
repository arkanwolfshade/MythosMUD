# Community 503

> 35 nodes

## Key Concepts

- **TestNPCCombatLifecycle** (12 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **NPCCombatLifecycle** (9 connections) — `server/services/npc_combat_lifecycle.py`
- **asyncio** (6 connections)
- **._despawn_npc()** (4 connections) — `server/services/npc_combat_lifecycle.py`
- **.lifecycle_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **test_npc_combat_lifecycle.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.despawn_npc_safely()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_lifecycle.py`
- **.get_npc_lifecycle_manager()** (3 connections) — `server/services/player_combat_service_support.py`
- **.mock_persistence()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_no_active_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_exception()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_no_lifecycle_manager()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_sqlalchemy_error()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_success()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_with_active_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **fixture** (2 connections)
- **Any** (1 connections)
- **Manages NPC lifecycle operations during combat.** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Initialize the lifecycle manager. Args: async_persistence: Async persistence…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn NPC with defensive error handling. Args: npc_id: ID of the NPC to…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Despawn an NPC. Args: npc_id: ID of the NPC to despawn _room_id: ID of the room…** (1 connections) — `server/services/npc_combat_lifecycle.py`
- **Return lifecycle manager (sync); may be wrapped by asyncio.to_thread.** (1 connections) — `server/services/player_combat_service_support.py`
- **Unit tests for NPC combat lifecycle. Tests the NPCCombatLifecycle class for…** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- *... and 10 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (3 shared connections)

## Source Files

- `server/services/npc_combat_lifecycle.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Audit Trail

- EXTRACTED: 45 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*