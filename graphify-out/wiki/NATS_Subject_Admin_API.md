# NATS Subject Admin API

> 18 nodes

## Key Concepts

- **PrototypeRegistry** (37 connections) — `server/game/items/prototype_registry.py`
- **.load_from_path()** (7 connections) — `server/game/items/prototype_registry.py`
- **._record_validation_failure()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **Path** (3 connections)
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **registry_with_switchblade()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **Initialize the item factory with a prototype registry.          Args:** (1 connections) — `server/game/items/item_factory.py`
- **ValidationError** (1 connections)
- **In-memory registry for validated item prototypes.** (1 connections) — `server/game/items/prototype_registry.py`
- **Load prototypes from a directory of JSON files.** (1 connections) — `server/game/items/prototype_registry.py`
- **Get a prototype by ID.          Args:             prototype_id: The ID of the** (1 connections) — `server/game/items/prototype_registry.py`
- **Get all invalid entries that failed validation.          Returns:** (1 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistry containing only the switchblade.** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`

## Relationships

- [NATS Retry Handler](NATS_Retry_Handler.md) (14 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (7 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (6 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (3 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)

## Source Files

- `server/game/items/item_factory.py`
- `server/game/items/prototype_registry.py`
- `server/tests/integration/test_combat_weapon_resolution.py`

## Audit Trail

- EXTRACTED: 74 (84%)
- INFERRED: 14 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*