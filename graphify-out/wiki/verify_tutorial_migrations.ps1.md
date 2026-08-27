# verify_tutorial_migrations.ps1

> 5 nodes

## Key Concepts

- **wearable_service()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **fixture** (2 connections)
- **Create mock persistence layer.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Create WearableContainerService instance.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [asyncio](asyncio.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 6 (86%)
- INFERRED: 1 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*