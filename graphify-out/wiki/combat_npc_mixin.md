# combat npc mixin

> 36 nodes

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
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **registry_with_switchblade()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
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
- *... and 11 more nodes in this community*

## Relationships

- [npc spawn validator](npc_spawn_validator.md) (26 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [holiday service services](holiday_service_services.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)
- [stats game generator](stats_game_generator.md) (1 shared connections)

## Source Files

- `server/game/items/item_factory.py`
- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 143 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*