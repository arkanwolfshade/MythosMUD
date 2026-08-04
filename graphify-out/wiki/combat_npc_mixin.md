# combat npc mixin

> 16 nodes

## Key Concepts

- **.load_from_path()** (13 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **Path** (5 connections)
- **test_load_from_path_missing_directory()** (4 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **test_load_from_path_valid_json()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_invalid_json()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_validation_error()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_load_from_path_durability_anomaly()** (3 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **Path** (1 connections)
- **Load item prototypes from JSON files in a directory.          Args:** (1 connections) — `server/game/items/prototype_registry.py`
- **Get a prototype by ID.          Args:             prototype_id: The ID of the pr** (1 connections) — `server/game/items/prototype_registry.py`
- **Namespace** (1 connections)
- **CLI entrypoint for validating MythosMUD item prototype definitions.** (1 connections) — `server/scripts/validate_prototypes.py`

## Relationships

- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (9 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (4 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [room cache services](room_cache_services.md) (1 shared connections)
- [stats game generator](stats_game_generator.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/unit/game/items/test_prototype_registry.py`

## Audit Trail

- EXTRACTED: 57 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*