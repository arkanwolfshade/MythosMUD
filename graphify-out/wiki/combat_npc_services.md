# combat npc services

> 14 nodes

## Key Concepts

- **find_wearable_container()** (17 connections) — `server/commands/container_helpers_inventory_find.py`
- **_player_for_wearable()** (12 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **find_wearable_container_for_put()** (10 connections) — `server/commands/container_helpers_inventory_find.py`
- **test_find_wearable_container_resolves_via_wearable_instance_id()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_falls_back_to_name_slot_match()** (4 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_uses_equip_dict_branch()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_create_wearable_container_fallback_when_equip_returns_non_dict()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_for_put_hits_inner_container()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_for_put_creates_on_slot_only_match()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_no_match_returns_none()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_inner_id_short_circuits()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **test_find_wearable_container_wearable_raises_returns_none()** (3 connections) — `server/tests/unit/commands/test_container_helpers_inventory_find.py`
- **Find a wearable container for put command, creating if necessary.** (1 connections) — `server/commands/container_helpers_inventory_find.py`
- **Find a wearable container by name.** (1 connections) — `server/commands/container_helpers_inventory_find.py`

## Relationships

- [container find inventory](container_find_inventory.md) (14 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (13 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (2 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [commands communication flows](commands_communication_flows.md) (2 shared connections)
- [Inventory Equip](Inventory_Equip.md) (1 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_find.py`
- `server/tests/unit/commands/test_container_helpers_inventory_find.py`

## Audit Trail

- EXTRACTED: 66 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*