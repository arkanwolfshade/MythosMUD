# .load_from_path

> 10 nodes

## Key Concepts

- **.load_from_path()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **._record_validation_failure()** (5 connections) — `server/game/items/prototype_registry.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/game/items/prototype_registry.py`
- **.invalid_entries()** (3 connections) — `server/game/items/prototype_registry.py`
- **Path** (3 connections)
- **ValidationError** (1 connections)
- **Get all invalid entries that failed validation. Returns: list[dict]: List of…** (1 connections) — `server/game/items/prototype_registry.py`
- **Load prototypes from a directory of JSON files.** (1 connections) — `server/game/items/prototype_registry.py`

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (5 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (2 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/items/prototype_registry.py`

## Audit Trail

- EXTRACTED: 21 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*