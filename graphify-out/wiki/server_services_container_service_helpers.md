# server services container service helpers

> 49 nodes

## Key Concepts

- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **ContainerTransferFromMixin** (18 connections) — `server/services/container_service_transfer_from.py`
- **._execute_transfer_from_container()** (12 connections) — `server/services/container_service_transfer_from.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **._finalize_loot_all()** (10 connections) — `server/services/container_service_transfer_from.py`
- **._require_container_component()** (10 connections) — `server/services/container_service_transfer_to.py`
- **._persist_and_audit_transfer_from_container()** (9 connections) — `server/services/container_service_transfer_from.py`
- **.transfer_to_container()** (9 connections) — `server/services/container_service_transfer_to.py`
- **UUID** (9 connections)
- **UUID** (9 connections)
- **items_json_for_persist()** (8 connections) — `server/services/container_service_helpers.py`
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service_transfer_from.py`
- **._loot_items_until_full()** (8 connections) — `server/services/container_service_transfer_from.py`
- **InventoryStack** (8 connections)
- **.loot_all()** (7 connections) — `server/services/container_service_transfer_from.py`
- **._remove_item_from_container()** (7 connections) — `server/services/container_service_transfer_from.py`
- **.transfer_from_container()** (7 connections) — `server/services/container_service_transfer_from.py`
- **._add_stack_to_container_or_raise()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._audit_transfer_to_container()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._require_container_has_capacity()** (7 connections) — `server/services/container_service_transfer_to.py`
- **._require_player_for_transfer()** (7 connections) — `server/services/container_service_transfer_to.py`
- **InventoryStack** (7 connections)
- **ContainerComponent** (5 connections)
- **ContainerComponent** (5 connections)
- **._prepare_transfer_item()** (4 connections) — `server/services/container_service_transfer_from.py`
- *... and 24 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (35 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (7 shared connections)
- [object](object.md) (2 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (1 shared connections)

## Source Files

- `server/services/container_service_helpers.py`
- `server/services/container_service_transfer_from.py`
- `server/services/container_service_transfer_to.py`

## Audit Trail

- EXTRACTED: 132 (89%)
- INFERRED: 17 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*