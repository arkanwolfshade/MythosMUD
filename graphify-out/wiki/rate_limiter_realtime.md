# rate limiter realtime

> 88 nodes

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (6 connections) — `server/models/game.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **.check_player_combat_state()** (5 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (5 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (5 connections) — `server/game/player_schema_converter.py`
- **BaseModel** (5 connections)
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- *... and 63 more nodes in this community*

## Relationships

- [combat services turn](combat_services_turn.md) (15 shared connections)
- [System Metrics](System_Metrics.md) (10 shared connections)
- [player room realtime](player_room_realtime.md) (10 shared connections)
- [Player Stats](Player_Stats.md) (8 shared connections)
- [MapView GameClientV2ContainerView Tabbed](MapView_GameClientV2ContainerView_Tabbed.md) (6 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (5 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (4 shared connections)
- [player service game](player_service_game.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [combat flee commands](combat_flee_commands.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_game_inventory_item.py`

## Audit Trail

- EXTRACTED: 344 (94%)
- INFERRED: 23 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*