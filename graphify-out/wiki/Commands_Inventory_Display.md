# Commands Inventory Display

> 34 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (14 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (10 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **_roll_weapon_attack()** (4 connections) — `server/game/weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_stack_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_missing_prototype_id_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **_weapon_damage_bounds()** (3 connections) — `server/game/weapons.py`
- **Any** (3 connections)
- **test_weapon_resolution_switchblade_no_main_hand_returns_none()** (3 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **test_resolve_weapon_attack_from_equipped_none_registry_returns_none()** (3 connections) — `server/tests/unit/game/test_weapons.py`
- **NamedTuple** (1 connections)
- **Weapon resolution helpers for combat.  Resolves equipped main-hand items to weap** (1 connections) — `server/game/weapons.py`
- **Result of resolving an equipped item to a weapon attack.      base_damage: Rolle** (1 connections) — `server/game/weapons.py`
- **Resolve equipped main-hand stack to weapon attack info, or None if unarmed.** (1 connections) — `server/game/weapons.py`
- **Integration tests for combat weapon resolution.  Verifies that the switchblade p** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **With switchblade equipped, resolved damage is in [1, 4] and damage_type is slash** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **When main_hand is empty, resolve returns None.** (1 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- *... and 9 more nodes in this community*

## Relationships

- [Commands Look Item](Commands_Look_Item.md) (13 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (10 shared connections)
- [Command Integration Summary](Command_Integration_Summary.md) (8 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 131 (89%)
- INFERRED: 16 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*