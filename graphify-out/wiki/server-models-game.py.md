# server/models/game.py

> 54 nodes

## Key Concepts

- **server/models/game.py** (32 connections) — `server/models/game.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (5 connections) — `server/models/game.py`
- **BaseModel** (5 connections)
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **test_inventory_item_with_weapon_minimal_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_uses_prototype_id_for_lookup()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_inventory_item_with_weapon_with_registry_weapon()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- *... and 29 more nodes in this community*

## Relationships

- [StatusEffect](StatusEffect.md) (15 shared connections)
- [Stats](Stats.md) (7 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [PlayerRead](PlayerRead.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [_convert_container_dict_to_container_data](_convert_container_dict_to_container_data.md) (2 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [test_player_schemas.py](test_player_schemas.py.md) (2 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (2 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 150 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*