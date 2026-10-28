# DOCUMENTATION_AUDIT.md

> 13 nodes · cohesion 0.15

## Key Concepts

- **_persistence_row()** (6 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_equip_reuses_the_existing_row_found_through_metadata_json()** (6 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_items_awaits_update_container_and_raises_when_it_fails()** (6 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_equip_awaits_create_container_and_returns_its_id()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_get_wearable_containers_validates_real_rows()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_unequip_folds_the_real_rows_contents_into_inner_container()** (5 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **_backpack_stack()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **UUID** (2 connections)
- **create_container is async: unawaited, equipping a wearable container always…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Re-equipping matches the row by metadata_json.item_instance_id instead of…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **Unequip finds the row by metadata_json and returns its items_json as…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **ContainerComponent forbids extra fields, so un-renamed items_json/metadata_json…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **update_container is async: unawaited, a failed update (None) was never detected…** (1 connections) — `server/tests/unit/services/test_wearable_container_service.py`

## Relationships

- [HolidayService](HolidayService.md) (14 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)

## Source Files

- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 25 (81%)
- INFERRED: 6 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*