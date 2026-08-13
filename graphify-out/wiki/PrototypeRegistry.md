# PrototypeRegistry

> 17 nodes

## Key Concepts

- **PrototypeRegistry** (29 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **.load_from_path()** (7 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **._record_validation_failure()** (5 connections) — `server/game/items/prototype_registry.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **main()** (3 connections) — `server/scripts/validate_prototypes.py`
- **parse_arguments()** (3 connections) — `server/scripts/validate_prototypes.py`
- **Path** (3 connections)
- **ValidationError** (1 connections)
- **Namespace** (1 connections)
- **Get all invalid entries that failed validation. Returns: list[dict]: List of…** (1 connections) — `server/game/items/prototype_registry.py`
- **In-memory registry for validated item prototypes.** (1 connections) — `server/game/items/prototype_registry.py`
- **Load prototypes from a directory of JSON files.** (1 connections) — `server/game/items/prototype_registry.py`
- **CLI entrypoint for validating MythosMUD item prototype definitions.** (1 connections) — `server/scripts/validate_prototypes.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (5 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (5 shared connections)
- [ItemFactory](ItemFactory.md) (4 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (3 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (2 shared connections)
- [registry_with_switchblade](registry_with_switchblade.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`
- `server/scripts/validate_prototypes.py`

## Audit Trail

- EXTRACTED: 50 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*