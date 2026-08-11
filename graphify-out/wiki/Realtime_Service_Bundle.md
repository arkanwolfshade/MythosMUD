# Realtime Service Bundle

> 67 nodes

## Key Concepts

- **container_endpoints_basic.py** (49 connections) — `server/api/container_endpoints_basic.py`
- **transfer_items()** (25 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **close_container()** (19 connections) — `server/api/container_endpoints_basic.py`
- **get_container_service()** (16 connections) — `server/api/container_helpers.py`
- **_convert_container_dict_to_container_data()** (12 connections) — `server/api/container_endpoints_basic.py`
- **_convert_inventory_list_to_inventory_stacks()** (11 connections) — `server/api/container_endpoints_basic.py`
- **ContainerLootAllResponse** (11 connections) — `server/schemas/containers/container.py`
- **ContainerOpenResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerTransferResponse** (10 connections) — `server/schemas/containers/container.py`
- **ContainerCloseResponse** (10 connections) — `server/schemas/containers/container.py`
- **InventoryStack** (10 connections) — `server/schemas/containers/container_data.py`
- **ContainerData** (10 connections) — `server/schemas/containers/container_data.py`
- **register_basic_endpoints()** (9 connections) — `server/api/container_endpoints_basic.py`
- **container.py** (9 connections) — `server/schemas/containers/container.py`
- **_build_container_data_from_dict()** (7 connections) — `server/api/container_endpoints_basic.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- **__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **_build_loot_all_response()** (6 connections) — `server/api/container_endpoints_loot.py`
- **Any** (5 connections)
- **BaseModel** (5 connections)
- **_convert_uuid_to_string()** (4 connections) — `server/api/container_endpoints_basic.py`
- **_convert_datetime_to_iso()** (4 connections) — `server/api/container_endpoints_basic.py`
- *... and 42 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (32 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (29 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (7 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (4 shared connections)
- [Player Effects API](Player_Effects_API.md) (4 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_helpers.py`
- `server/models/game.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 326 (90%)
- INFERRED: 37 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*