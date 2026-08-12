# resolve_weapon_attack_from_equipped

> 40 nodes

## Key Concepts

- **resolve_weapon_attack_from_equipped()** (24 connections) — `server/game/weapons.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (14 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **items/models.py** (7 connections) — `server/game/items/models.py`
- **_roll_weapon_attack()** (4 connections) — `server/game/weapons.py`
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
- **constants.py** (2 connections) — `server/game/items/constants.py`
- **NamedTuple** (1 connections)
- **Constants supporting item prototype validation. These enumerations anchor the…** (1 connections) — `server/game/items/constants.py`
- **Pydantic models for item prototype validation. This module defines the…** (1 connections) — `server/game/items/models.py`
- **Prototype registry for managing item prototypes. This module provides the…** (1 connections) — `server/game/items/prototype_registry.py`
- *... and 15 more nodes in this community*

## Relationships

- [PrototypeRegistry](PrototypeRegistry.md) (7 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (6 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (4 shared connections)
- [ItemPrototypeModel](ItemPrototypeModel.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [combat_attack.py](combat_attack.py.md) (3 shared connections)
- [item_factory.py](item_factory.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [server/models/game.py](server-models-game.py.md) (2 shared connections)
- [registry_with_switchblade](registry_with_switchblade.md) (2 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (1 shared connections)

## Source Files

- `server/game/items/constants.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 162 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*