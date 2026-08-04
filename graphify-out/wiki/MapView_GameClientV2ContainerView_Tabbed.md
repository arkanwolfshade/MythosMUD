# MapView GameClientV2ContainerView Tabbed

> 38 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (12 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **switchblade_prototype()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **registry_with_switchblade()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **NamedTuple** (1 connections)
- **Any** (1 connections)
- **Weapon resolution helpers for combat.  Resolves equipped main-hand items to weap** (1 connections) — `server/game/weapons.py`
- **Result of resolving an equipped item to a weapon attack.      base_damage: Rolle** (1 connections) — `server/game/weapons.py`
- **Resolve equipped main-hand stack to weapon attack info, or indicate non-weapon.** (1 connections) — `server/game/weapons.py`
- **Integration tests for combat weapon resolution.  Verifies that the switchblade p** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **Build ItemPrototypeModel for switchblade (weapon.main_hand.switchblade).** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- *... and 13 more nodes in this community*

## Relationships

- [combat npc mixin](combat_npc_mixin.md) (14 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (10 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (7 shared connections)
- [attack combat commands](attack_combat_commands.md) (3 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 130 (88%)
- INFERRED: 17 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*