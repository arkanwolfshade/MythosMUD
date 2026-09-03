# Test Prototype Registry

> 26 nodes

## Key Concepts

- **PrototypeRegistry** (47 connections) — `server/game/items/prototype_registry.py`
- **test_prototype_registry.py** (18 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **.load_from_path()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **._record_validation_failure()** (5 connections) — `server/game/items/prototype_registry.py`
- **_make_prototype()** (5 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Path** (5 connections)
- **test_load_from_path_missing_directory()** (4 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **test_all_returns_values()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_find_by_tag()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_get_missing_raises()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_get_returns_prototype()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_durability_anomaly()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_invalid_json()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_valid_json()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_validation_error()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Path** (3 connections)
- **test_invalid_entries_returns_copy()** (2 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **ValidationError** (1 connections)
- **Get all invalid entries that failed validation. Returns: list[dict]: List of…** (1 connections) — `server/game/items/prototype_registry.py`
- **In-memory registry for validated item prototypes.** (1 connections) — `server/game/items/prototype_registry.py`
- **Load prototypes from a directory of JSON files.** (1 connections) — `server/game/items/prototype_registry.py`
- *... and 1 more nodes in this community*

## Relationships

- [Test Weapons](Test_Weapons.md) (14 shared connections)
- [Item Factory](Item_Factory.md) (11 shared connections)
- [Models](Models.md) (7 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (3 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (2 shared connections)
- [Test Inventory Command Prototype](Test_Inventory_Command_Prototype.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Test Combat Weapon Resolution](Test_Combat_Weapon_Resolution.md) (1 shared connections)
- [Performance Monitor](Performance_Monitor.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 66 (73%)
- INFERRED: 25 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*