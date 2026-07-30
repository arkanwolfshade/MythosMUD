# emit close container event()

> 64 nodes

## Key Concepts

- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (12 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **.load_from_path()** (8 connections) — `server/game/items/prototype_registry.py`
- **models.py** (7 connections) — `server/game/items/models.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **.find_by_tag()** (3 connections) — `server/game/items/prototype_registry.py`
- **.all()** (3 connections) — `server/game/items/prototype_registry.py`
- **switchblade_prototype()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **registry_with_switchblade()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **constants.py** (2 connections) — `server/game/items/constants.py`
- *... and 39 more nodes in this community*

## Relationships

- [test command parser](test_command_parser.md) (23 shared connections)
- [Player](Player.md) (15 shared connections)
- [combat attack](combat_attack.md) (3 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [init](init.md) (1 shared connections)
- [.add message()](add_message%28%29.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 202 (89%)
- INFERRED: 26 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*