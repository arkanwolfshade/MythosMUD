# resolve_weapon_attack_from_equipped

> 36 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (14 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **_roll_weapon_attack()** (4 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **_weapon_damage_bounds()** (3 connections) — `server/game/weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **Any** (3 connections)
- **NamedTuple** (1 connections)
- **Weapon resolution helpers for combat. Resolves equipped main-hand items to…** (1 connections) — `server/game/weapons.py`
- **Result of resolving an equipped item to a weapon attack. base_damage: Rolled…** (1 connections) — `server/game/weapons.py`
- **Resolve equipped main-hand stack to weapon attack info, or None if unarmed.** (1 connections) — `server/game/weapons.py`
- **Integration tests for combat weapon resolution. Verifies that the switchblade…** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **With switchblade equipped, resolved damage is in [1, 4] and damage_type is…** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- *... and 11 more nodes in this community*

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (5 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (4 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (2 shared connections)
- [registry_with_switchblade](registry_with_switchblade.md) (2 shared connections)

## Source Files

- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*