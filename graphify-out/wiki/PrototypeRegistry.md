# PrototypeRegistry

> 30 nodes

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
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
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
- **Find all prototypes that have a specific tag. Args: tag: The tag to search for…** (1 connections) — `server/game/items/prototype_registry.py`
- *... and 5 more nodes in this community*

## Relationships

- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (12 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (11 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (10 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [._initialize_item_services](_initialize_item_services.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [get_monitoring_dashboard](get_monitoring_dashboard.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 70 (74%)
- INFERRED: 25 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*