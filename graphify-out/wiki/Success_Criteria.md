# Success Criteria

> 4 nodes

## Key Concepts

- **test_get_wearable_containers_for_player_filters_non_equipment()** (4 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_unequip_wearable_container_with_allowed_roles()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test handle_unequip_wearable_container preserves allowed_roles.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Test get_wearable_containers_for_player filters out non-equipment containers.** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [Phase 1: Core Separation](Phase_1-_Core_Separation.md) (2 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 6 (86%)
- INFERRED: 1 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*