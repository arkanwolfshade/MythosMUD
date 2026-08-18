# server game items prototype registry

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

- [server game weapons](server_game_weapons.md) (14 shared connections)
- [iteminstance](iteminstance.md) (11 shared connections)
- [server game items constants](server_game_items_constants.md) (8 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server services combat turn participant](server_services_combat_turn_participant.md) (2 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (1 shared connections)
- [server commands inventory command prototype](server_commands_inventory_command_prototype.md) (1 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 66 (73%)
- INFERRED: 25 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*