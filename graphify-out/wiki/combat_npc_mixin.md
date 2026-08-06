# combat npc mixin

> 32 nodes

## Key Concepts

- **PrototypeRegistry** (41 connections) — `server/game/items/prototype_registry.py`
- **test_prototype_registry.py** (17 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **.load_from_path()** (13 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **_make_prototype()** (5 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Path** (5 connections)
- **test_load_from_path_missing_directory()** (4 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **.__init__()** (3 connections) — `server/game/items/item_factory.py`
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **test_get_returns_prototype()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_get_missing_raises()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_find_by_tag()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_all_returns_values()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_valid_json()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_invalid_json()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_validation_error()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_durability_anomaly()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Any** (2 connections)
- **test_invalid_entries_returns_copy()** (2 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Initialize the item factory with a prototype registry.          Args:** (1 connections) — `server/game/items/item_factory.py`
- **Path** (1 connections)
- *... and 7 more nodes in this community*

## Relationships

- [npc spawn validator](npc_spawn_validator.md) (14 shared connections)
- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (14 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (9 shared connections)
- [EdgeCreationModal map STANDARD](EdgeCreationModal_map_STANDARD.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [stats game generator](stats_game_generator.md) (1 shared connections)

## Source Files

- `server/game/items/item_factory.py`
- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 135 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*