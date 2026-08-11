# NATS Retry Handler

> 36 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (14 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (10 connections) — `server/game/weapons.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
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
- *... and 11 more nodes in this community*

## Relationships

- [NATS Subject Admin API](NATS_Subject_Admin_API.md) (14 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (8 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (5 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (4 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (3 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)

## Source Files

- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 136 (89%)
- INFERRED: 17 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*