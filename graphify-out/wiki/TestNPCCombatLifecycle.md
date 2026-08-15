# TestNPCCombatLifecycle

> 24 nodes

## Key Concepts

- **TestNPCCombatLifecycle** (12 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **asyncio** (6 connections)
- **.lifecycle_service()** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **test_npc_combat_lifecycle.py** (4 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.mock_persistence()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_no_active_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_exception()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_no_lifecycle_manager()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_sqlalchemy_error()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_safely_success()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_despawn_npc_with_active_npcs()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **fixture** (2 connections)
- **Unit tests for NPC combat lifecycle. Tests the NPCCombatLifecycle class for…** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test _despawn_npc handles NPC not in active_npcs.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test suite for NPCCombatLifecycle class.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Create a NPCCombatLifecycle instance for testing.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test NPCCombatLifecycle initialization.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely successfully despawns NPC.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely handles missing lifecycle manager.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test despawn_npc_safely handles SQLAlchemy errors.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`
- **Test _despawn_npc handles NPC in active_npcs via fallback path.** (1 connections) — `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_combat_lifecycle.py`

## Audit Trail

- EXTRACTED: 33 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*