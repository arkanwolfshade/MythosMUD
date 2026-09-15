# _weapon_from_prototype_registry

> 12 nodes

## Key Concepts

- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (5 connections) — `server/models/game.py`
- **test_weapon_from_prototype_registry_empty_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_no_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapon_from_prototype_registry_weapon_present_returns_dict()** (3 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **Resolve metadata.weapon from prototype registry for a given prototype_id.…** (1 connections) — `server/game/player_schema_converter.py`
- **Weapon statistics for items that can be used as weapons. This model represents…** (1 connections) — `server/models/game.py`
- **When registry is None, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype_id is empty, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype has no metadata.weapon, returns None.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **When prototype has metadata.weapon, returns weapon dict.** (1 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (8 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)
- [StatusEffect](StatusEffect.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*