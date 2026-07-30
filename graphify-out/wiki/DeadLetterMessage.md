# DeadLetterMessage

> 99 nodes

## Key Concepts

- **ContainerService** (78 connections) — `server/services/container_service.py`
- **transfer_all_items_from_container()** (21 connections) — `server/api/container_helpers.py`
- **TestTransferAllItemsFromContainer** (20 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **.transfer_from_container()** (18 connections) — `server/services/container_service.py`
- **UUID** (17 connections)
- **.open_container()** (15 connections) — `server/services/container_service.py`
- **Any** (13 connections)
- **.transfer_to_container()** (13 connections) — `server/services/container_service.py`
- **.lock_container()** (12 connections) — `server/services/container_service.py`
- **.unlock_container()** (12 connections) — `server/services/container_service.py`
- **.loot_all()** (11 connections) — `server/services/container_service.py`
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **TestExecuteTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **.is_admin()** (10 connections) — `server/services/user_manager.py`
- **TestGetContainerService** (10 connections) — `server/tests/unit/api/test_container_helpers.py`
- **._remove_item_from_container()** (8 connections) — `server/services/container_service.py`
- **ContainerComponent** (8 connections)
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service.py`
- **._persist_and_audit_transfer_from_container()** (8 connections) — `server/services/container_service.py`
- **_get_enum_value()** (7 connections) — `server/services/container_service.py`
- **._verify_container_open()** (7 connections) — `server/services/container_service.py`
- **._validate_proximity()** (7 connections) — `server/services/container_service.py`
- **._validate_ownership()** (7 connections) — `server/services/container_service.py`
- **._can_unlock_container()** (7 connections) — `server/services/container_service.py`
- *... and 74 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (52 shared connections)
- [APIRouter](APIRouter.md) (29 shared connections)
- [BaseCommand](BaseCommand.md) (13 shared connections)
- [real time](real_time.md) (13 shared connections)
- [Lock](Lock.md) (9 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [container helpers inventory](container_helpers_inventory.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Connection Manager](Connection_Manager.md) (3 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (2 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/services/container_service.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 426 (81%)
- INFERRED: 98 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*