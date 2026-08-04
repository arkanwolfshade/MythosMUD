# payload realtime optimizer

> 13 nodes

## Key Concepts

- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **._extract_required_fields()** (4 connections) — `server/services/inventory_service.py`
- **._can_merge()** (4 connections) — `server/services/inventory_service.py`
- **._normalize_metadata()** (4 connections) — `server/services/inventory_service.py`
- **Add or merge an item stack into the inventory.          Args:             invent** (1 connections) — `server/services/inventory_service.py`
- **Split a stack into two, inserting the new stack immediately after the source slo** (1 connections) — `server/services/inventory_service.py`
- **Extract required fields from stack.          Returns:             Tuple of (item** (1 connections) — `server/services/inventory_service.py`
- **Validate and clone optional fields (metadata, flags, origin, etc.).          Arg** (1 connections) — `server/services/inventory_service.py`

## Relationships

- [Exception Containers](Exception_Containers.md) (12 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (8 shared connections)
- [player cache rationale](player_cache_rationale.md) (2 shared connections)

## Source Files

- `server/services/inventory_service.py`

## Audit Trail

- EXTRACTED: 61 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*