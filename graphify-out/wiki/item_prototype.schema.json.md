# item_prototype.schema.json

> 32 nodes · cohesion 0.10

## Key Concepts

- **metadata_models.py** (16 connections) — `server/game/items/metadata_models.py`
- **ItemMetadata** (15 connections) — `server/game/items/metadata_models.py`
- **constants/containers.py** (12 connections) — `server/constants/containers.py`
- **test_metadata_models.py** (11 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **BaseModel** (9 connections)
- **ContainerMetadata** (5 connections) — `server/game/items/metadata_models.py`
- **LucidityRecoveryMetadata** (5 connections) — `server/game/items/metadata_models.py`
- **WeaponMetadata** (5 connections) — `server/game/items/metadata_models.py`
- **ArmorMetadata** (3 connections) — `server/game/items/metadata_models.py`
- **CatalogMetadata** (3 connections) — `server/game/items/metadata_models.py`
- **EquipmentBonus** (3 connections) — `server/game/items/metadata_models.py`
- **EquipmentMetadata** (3 connections) — `server/game/items/metadata_models.py`
- **TomeMetadata** (3 connections) — `server/game/items/metadata_models.py`
- **test_item_metadata_accepts_rich_dual_write_weapon()** (3 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **test_item_metadata_container_rejects_invalid()** (3 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **test_item_metadata_rejects_bad_lucidity_recovery()** (3 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **parametrize** (2 connections)
- **test_item_metadata_accepts_legacy_weapon_ints()** (2 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **test_item_metadata_accepts_lucidity_recovery()** (2 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **test_item_metadata_container_defaults_and_cap()** (2 connections) — `server/tests/unit/game/items/test_metadata_models.py`
- **Shared container limits. Kept import-free so models, schemas, and item metadata…** (1 connections) — `server/constants/containers.py`
- **Pydantic contracts for item prototype metadata (ADR-026). Known mechanical…** (1 connections) — `server/game/items/metadata_models.py`
- **Validated known keys under item prototype metadata (ADR-026). Additional lore…** (1 connections) — `server/game/items/metadata_models.py`
- **Weapon stats: rich CoC-like fields plus legacy WeaponStats integers.** (1 connections) — `server/game/items/metadata_models.py`
- **Armor points and coverage.** (1 connections) — `server/game/items/metadata_models.py`
- *... and 7 more nodes in this community*

## Relationships

- [UserManager](UserManager.md) (7 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (3 shared connections)
- [test_metrics.py](test_metrics.py.md) (3 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (2 shared connections)
- [.profession_to_dict](profession_to_dict.md) (2 shared connections)
- [test_event_publisher.py](test_event_publisher.py.md) (2 shared connections)
- [ADR-026: Item Catalog Metadata Contracts](ADR-026-_Item_Catalog_Metadata_Contracts.md) (2 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (1 shared connections)

## Source Files

- `server/constants/containers.py`
- `server/game/items/metadata_models.py`
- `server/tests/unit/game/items/test_metadata_models.py`

## Audit Trail

- EXTRACTED: 60 (83%)
- INFERRED: 12 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*