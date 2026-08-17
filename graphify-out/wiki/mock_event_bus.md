# mock_event_bus

> 9 nodes

## Key Concepts

- **mock_event_bus()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **population_controller()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **fixture** (4 connections)
- **mock_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **Create a mock event bus.** (1 connections) — `server/tests/unit/npc/test_population_control.py`
- **Create a mock async persistence.** (1 connections) — `server/tests/unit/npc/test_population_control.py`
- **Create a mock lifecycle manager.** (1 connections) — `server/tests/unit/npc/test_population_control.py`
- **Create an NPCPopulationController instance.** (1 connections) — `server/tests/unit/npc/test_population_control.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 12 (86%)
- INFERRED: 2 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*