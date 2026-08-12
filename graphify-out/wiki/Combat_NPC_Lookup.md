# Combat NPC Lookup

> 46 nodes

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **BaseModel** (5 connections)
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **.add_item()** (3 connections) — `server/models/game.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_creation()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **test_inventory_item_default_quantity()** (3 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **WeaponStats** (1 connections)
- **Player schema conversion utilities.  This module handles conversion of Player ob** (1 connections) — `server/game/player_schema_converter.py`
- *... and 21 more nodes in this community*

## Relationships

- [Player Creation Service](Player_Creation_Service.md) (9 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (7 shared connections)
- [NATS Retry Handler](NATS_Retry_Handler.md) (5 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (4 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (4 shared connections)
- [Test Refactoring Complete](Test_Refactoring_Complete.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (3 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (3 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (3 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (2 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (2 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`

## Audit Trail

- EXTRACTED: 194 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*