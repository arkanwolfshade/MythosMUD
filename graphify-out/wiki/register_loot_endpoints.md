# register_loot_endpoints

> 5 nodes

## Key Concepts

- **register_loot_endpoints()** (6 connections) — `server/api/container_endpoints_loot.py`
- **.test_register_loot_endpoints()** (3 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`
- **APIRouter** (1 connections)
- **Register loot-all endpoint to the router.** (1 connections) — `server/api/container_endpoints_loot.py`
- **Test register_loot_endpoints registers the endpoint.** (1 connections) — `server/tests/unit/api/test_container_endpoints_loot_register.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [LootAllRequest](LootAllRequest.md) (1 shared connections)
- [loot_all_items](loot_all_items.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`

## Audit Trail

- EXTRACTED: 7 (88%)
- INFERRED: 1 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*