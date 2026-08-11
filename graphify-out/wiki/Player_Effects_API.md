# Player Effects API

> 71 nodes

## Key Concepts

- **ContainerService** (78 connections) — `server/services/container_service.py`
- **.transfer_from_container()** (18 connections) — `server/services/container_service.py`
- **UUID** (17 connections)
- **.open_container()** (15 connections) — `server/services/container_service.py`
- **conftest.py** (14 connections) — `server/tests/unit/api/conftest.py`
- **Any** (13 connections)
- **.transfer_to_container()** (13 connections) — `server/services/container_service.py`
- **.lock_container()** (12 connections) — `server/services/container_service.py`
- **.unlock_container()** (12 connections) — `server/services/container_service.py`
- **.loot_all()** (11 connections) — `server/services/container_service.py`
- **._validate_container_access()** (11 connections) — `server/services/container_service.py`
- **_filter_container_data()** (10 connections) — `server/services/container_service.py`
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
- *... and 46 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (32 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (18 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (18 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (13 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (9 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (5 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (4 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (3 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 320 (82%)
- INFERRED: 70 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*