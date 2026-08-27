# test_alias_expansion.py

> 26 nodes

## Key Concepts

- **PrototypeRegistry** (44 connections) — `server/game/items/prototype_registry.py`
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

- [test_npc_combat_integration_service_player_attacks.py](test_npc_combat_integration_service_player_attacks.py.md) (15 shared connections)
- [authenticated.ts](authenticated.ts.md) (11 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [command_input.py](command_input.py.md) (1 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 64 (73%)
- INFERRED: 24 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*