# resolve_weapon_attack_from_equipped

> 41 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (25 connections) — `server/game/weapons.py`
- **prototype_registry.py** (23 connections) — `server/game/items/prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (13 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **items/models.py** (11 connections) — `server/game/items/models.py`
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
- **Pydantic models for item prototype validation. This module defines the…** (1 connections) — `server/game/items/models.py`
- **Prototype registry for managing item prototypes. This module provides the…** (1 connections) — `server/game/items/prototype_registry.py`
- *... and 16 more nodes in this community*

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (16 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (13 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [registry_with_switchblade](registry_with_switchblade.md) (2 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)

## Source Files

- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 110 (85%)
- INFERRED: 19 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*