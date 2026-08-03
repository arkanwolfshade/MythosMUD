# game weapon player

> 52 nodes

## Key Concepts

- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **.check_player_combat_state()** (5 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (5 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (5 connections) — `server/game/player_schema_converter.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (5 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **test_weapon_from_prototype_registry_missing_prototype_returns_none()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_minimal_dict()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- *... and 27 more nodes in this community*

## Relationships

- [game models player](game_models_player.md) (13 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [npc populate databases](npc_populate_databases.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [game models stats](game_models_stats.md) (3 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [spell models rationale](spell_models_rationale.md) (2 shared connections)
- [magic healing game](magic_healing_game.md) (2 shared connections)
- [combat commands handler](combat_commands_handler.md) (2 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 204 (94%)
- INFERRED: 14 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*