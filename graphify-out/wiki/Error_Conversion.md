# Error Conversion

> 103 nodes

## Key Concepts

- **PrototypeRegistry** (35 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (12 connections) — `server/game/weapons.py`
- **test_combat_weapon_resolution.py** (12 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **ItemFactory** (11 connections) — `server/game/items/item_factory.py`
- **ItemFactoryError** (9 connections) — `server/game/items/item_factory.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **.load_from_path()** (8 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **ItemInstance** (7 connections) — `server/game/items/item_instance.py`
- **models.py** (7 connections) — `server/game/items/models.py`
- **.create_instance()** (6 connections) — `server/game/items/item_factory.py`
- **.get()** (6 connections) — `server/game/items/prototype_registry.py`
- **initialize_components()** (5 connections) — `server/game/items/component_hooks.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- *... and 78 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (16 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (6 shared connections)
- [game weapon player](game_weapon_player.md) (5 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)
- [config models rationale](config_models_rationale.md) (1 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/constants.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 351 (87%)
- INFERRED: 52 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*