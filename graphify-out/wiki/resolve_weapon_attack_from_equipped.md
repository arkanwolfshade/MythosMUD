# resolve_weapon_attack_from_equipped

> 35 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (25 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **_prototype_from_equipped_stack()** (6 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (6 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **_roll_weapon_attack()** (3 connections) — `server/game/weapons.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **_weapon_damage_bounds()** (2 connections) — `server/game/weapons.py`
- **PrototypeRegistry** (2 connections)
- **NamedTuple** (1 connections)
- **Weapon resolution helpers for combat. Resolves equipped main-hand items to…** (1 connections) — `server/game/weapons.py`
- **Result of resolving an equipped item to a weapon attack. base_damage: Rolled…** (1 connections) — `server/game/weapons.py`
- **Resolve equipped main-hand stack to weapon attack info, or None if unarmed.** (1 connections) — `server/game/weapons.py`
- **With switchblade equipped, resolved damage is in [1, 4] and damage_type is…** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **When main_hand is empty, resolve returns None.** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- *... and 10 more nodes in this community*

## Relationships

- [ItemPrototypeModel](ItemPrototypeModel.md) (15 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (12 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (6 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 75 (80%)
- INFERRED: 19 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*