# ._initialize_item_services

> 5 nodes

## Key Concepts

- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **Exception** (1 connections)
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item…** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*