# Player Effects API

> 63 nodes

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
- *... and 38 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (38 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (23 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (14 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (13 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (5 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (4 shared connections)
- [Container Inventory Ops](Container_Inventory_Ops.md) (3 shared connections)
- [Player Mute Persistence](Player_Mute_Persistence.md) (3 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (1 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (1 shared connections)

## Source Files

- `server/services/container_service.py`
- `server/services/user_manager.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 301 (80%)
- INFERRED: 75 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*