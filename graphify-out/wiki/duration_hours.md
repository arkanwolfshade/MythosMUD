# duration_hours

> 5 nodes

## Key Concepts

- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **fixture** (2 connections)
- **Persistence mock with async get_player_by_id for integration tests.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **NPCCombatIntegration wired to the mock persistence layer.** (1 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Relationships

- [test_movement_monitor.py](test_movement_monitor.py.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*