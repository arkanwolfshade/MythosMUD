# npc spawn validator

> 83 nodes

## Key Concepts

- **PrototypeRegistryError** (26 connections) — `server/game/items/prototype_registry.py`
- **prototype_registry.py** (22 connections) — `server/game/items/prototype_registry.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **ItemFactory** (17 connections) — `server/game/items/item_factory.py`
- **item_factory.py** (16 connections) — `server/game/items/item_factory.py`
- **ItemFactoryError** (15 connections) — `server/game/items/item_factory.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **weapons.py** (12 connections) — `server/game/weapons.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **test_item_factory.py** (11 connections) — `server/tests/unit/game/test_item_factory.py`
- **ItemInstance** (10 connections) — `server/game/items/item_instance.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **weapon.py** (7 connections) — `server/schemas/game/weapon.py`
- **item_instance.py** (5 connections) — `server/game/items/item_instance.py`
- **test_item_instance.py** (5 connections) — `server/tests/unit/game/test_item_instance.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_no_weapon_metadata_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_missing_min_max_returns_none()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_returns_info_in_range()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_weapon_with_modifier()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_resolve_weapon_attack_from_equipped_empty_damage_types_uses_physical()** (5 connections) — `server/tests/unit/game/test_weapons.py`
- **test_weapon_resolution_switchblade_damage_in_range()** (4 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- *... and 58 more nodes in this community*

## Relationships

- [combat npc mixin](combat_npc_mixin.md) (26 shared connections)
- [connection cleaner realtime](connection_cleaner_realtime.md) (19 shared connections)
- [player service game](player_service_game.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [command factories communication](command_factories_communication.md) (6 shared connections)
- [stats game generator](stats_game_generator.md) (5 shared connections)
- [game chat moderation](game_chat_moderation.md) (4 shared connections)
- [schedule service services](schedule_service_services.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [combat models rationale](combat_models_rationale.md) (4 shared connections)
- [attack combat commands](attack_combat_commands.md) (3 shared connections)
- [commands inventory put](commands_inventory_put.md) (2 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/prototype_registry.py`
- `server/game/player_schema_converter.py`
- `server/game/weapons.py`
- `server/schemas/game/weapon.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_item_factory.py`
- `server/tests/unit/game/test_item_instance.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 344 (90%)
- INFERRED: 37 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*