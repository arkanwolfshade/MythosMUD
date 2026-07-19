# Services Npc Combat

> 20 nodes · cohesion 0.10

## Key Concepts

- **TestNPCCombatLifecycle** (12 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **test_npc_combat_lifecycle.py** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.lifecycle_service()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.mock_persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_no_active_npcs()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_exception()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_no_lifecycle_manager()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_sqlalchemy_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_with_active_npcs()** (2 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Unit tests for NPC combat lifecycle.  Tests the NPCCombatLifecycle class for man** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test _despawn_npc handles NPC not in active_npcs.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test suite for NPCCombatLifecycle class.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Create a NPCCombatLifecycle instance for testing.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test NPCCombatLifecycle initialization.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely handles missing lifecycle manager.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely handles SQLAlchemy errors.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test _despawn_npc handles NPC in active_npcs via fallback path.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Relationships

- [[NPC Combat Lifecycle]] (4 shared connections)
- [[NPC Population Control]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Audit Trail

- EXTRACTED: 42 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
