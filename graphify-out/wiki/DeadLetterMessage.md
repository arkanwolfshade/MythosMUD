# DeadLetterMessage

> 59 nodes

## Key Concepts

- **ContainerService** (78 connections) — `server/services/container_service.py`
- **.transfer_from_container()** (18 connections) — `server/services/container_service.py`
- **UUID** (17 connections)
- **.open_container()** (15 connections) — `server/services/container_service.py`
- **Any** (13 connections)
- **.transfer_to_container()** (13 connections) — `server/services/container_service.py`
- **.lock_container()** (12 connections) — `server/services/container_service.py`
- **.unlock_container()** (12 connections) — `server/services/container_service.py`
- **.loot_all()** (11 connections) — `server/services/container_service.py`
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
- **.is_admin()** (10 connections) — `server/services/user_manager.py`
- **._remove_item_from_container()** (8 connections) — `server/services/container_service.py`
- **ContainerComponent** (8 connections)
- **._add_item_to_player_inventory()** (8 connections) — `server/services/container_service.py`
- **._persist_and_audit_transfer_from_container()** (8 connections) — `server/services/container_service.py`
- **_get_enum_value()** (7 connections) — `server/services/container_service.py`
- **._verify_container_open()** (7 connections) — `server/services/container_service.py`
- **._validate_proximity()** (7 connections) — `server/services/container_service.py`
- **._validate_ownership()** (7 connections) — `server/services/container_service.py`
- **._can_unlock_container()** (7 connections) — `server/services/container_service.py`
- **._validate_container_close()** (6 connections) — `server/services/container_service.py`
- **._audit_log_container_close()** (6 connections) — `server/services/container_service.py`
- **.close_container()** (6 connections) — `server/services/container_service.py`
- **InventoryStack** (6 connections)
- *... and 34 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (35 shared connections)
- [BaseCommand](BaseCommand.md) (22 shared connections)
- [APIRouter](APIRouter.md) (15 shared connections)
- [real time](real_time.md) (13 shared connections)
- [Lock](Lock.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (3 shared connections)
- [container helpers inventory](container_helpers_inventory.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (2 shared connections)
- [test container persistence sql injection](test_container_persistence_sql_injection.md) (1 shared connections)
- [init](init.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 293 (80%)
- INFERRED: 73 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*