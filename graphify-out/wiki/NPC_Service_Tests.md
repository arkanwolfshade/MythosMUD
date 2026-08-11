# NPC Service Tests

> 41 nodes

## Key Concepts

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
- **__init__.py** (7 connections) — `server/schemas/containers/__init__.py`
- **container_data.py** (7 connections) — `server/schemas/containers/container_data.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **_build_loot_all_response()** (6 connections) — `server/api/container_endpoints_loot.py`
- **Any** (5 connections)
- **_convert_uuid_to_string()** (4 connections) — `server/api/container_endpoints_basic.py`
- **_convert_datetime_to_iso()** (4 connections) — `server/api/container_endpoints_basic.py`
- **BaseModel** (4 connections)
- **BaseModel** (3 connections)
- **InnerContainer** (3 connections) — `server/schemas/containers/container_data.py`
- **InventoryStack** (2 connections)
- **ContainerData** (2 connections)
- **APIRouter** (1 connections)
- **Convert UUID-like object to string if it has __str__ method.** (1 connections) — `server/api/container_endpoints_basic.py`
- *... and 16 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (23 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (3 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (3 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (1 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (1 shared connections)

## Source Files

- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`

## Audit Trail

- EXTRACTED: 153 (85%)
- INFERRED: 28 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*