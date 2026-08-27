# maps/__init__.py

> 26 nodes

## Key Concepts

- **PickupCommand** (22 connections) — `server/models/command_inventory.py`
- **test_pickup_command_index_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_quantity_validation_min()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_search_term_max_length()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_requirements_index_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_requirements_neither_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_requirements_search_term_provided()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_empty_string()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_none()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_strips()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_validate_search_term_whitespace_only()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_with_both()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_with_index()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **test_pickup_command_with_search_term()** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand can be created with index.** (3 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Command for picking up items from room drops.** (1 connections) — `server/models/command_inventory.py`
- **Test PickupCommand accepts index alone.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand accepts search_term alone.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand validates index is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand validates quantity is >= 1.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand validates search_term max length.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand strips whitespace from search_term.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand cannot accept empty search_term (fails min_length before…** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand converts whitespace-only search_term to None.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- **Test PickupCommand accepts None for search_term.** (1 connections) — `server/tests/unit/models/test_command_inventory.py`
- *... and 1 more nodes in this community*

## Relationships

- [devDependencies](devDependencies.md) (15 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [_should_include_npc](_should_include_npc.md) (1 shared connections)
- [✅ POSITIVE FINDINGS](✅_POSITIVE_FINDINGS.md) (1 shared connections)
- [Church of Sunyata.md](Church_of_Sunyata.md.md) (1 shared connections)

## Source Files

- `server/models/command_inventory.py`
- `server/tests/unit/models/test_command_inventory.py`

## Audit Trail

- EXTRACTED: 47 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*