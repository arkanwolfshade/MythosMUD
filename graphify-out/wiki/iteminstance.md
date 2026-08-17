# iteminstance

> 158 nodes

## Key Concepts

- **PrototypeRegistry** (47 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (39 connections) — `server/game/items/models.py`
- **PrototypeRegistryError** (25 connections) — `server/game/items/prototype_registry.py`
- **resolve_weapon_attack_from_equipped()** (25 connections) — `server/game/weapons.py`
- **prototype_registry.py** (23 connections) — `server/game/items/prototype_registry.py`
- **ItemFactory** (19 connections) — `server/game/items/item_factory.py`
- **test_prototype_registry.py** (18 connections) — `server/tests/unit/game/items/test_prototype_registry.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **weapons.py** (17 connections) — `server/game/weapons.py`
- **item_factory.py** (16 connections) — `server/game/items/item_factory.py`
- **test_item_prototype_models.py** (15 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **test_combat_weapon_resolution.py** (13 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **ItemFactoryError** (12 connections) — `server/game/items/item_factory.py`
- **test_item_factory.py** (12 connections) — `server/tests/unit/game/test_item_factory.py`
- **items/__init__.py** (11 connections) — `server/game/items/__init__.py`
- **items/models.py** (11 connections) — `server/game/items/models.py`
- **ItemInstance** (9 connections) — `server/game/items/item_instance.py`
- **WeaponAttackInfo** (9 connections) — `server/game/weapons.py`
- **initialize_components()** (9 connections) — `server/game/items/component_hooks.py`
- **_valid_payload()** (9 connections) — `server/tests/unit/game/items/test_item_prototype_models.py`
- **validate_prototypes.py** (8 connections) — `server/scripts/validate_prototypes.py`
- **.create_instance()** (7 connections) — `server/game/items/item_factory.py`
- **.load_from_path()** (6 connections) — `server/game/items/prototype_registry.py`
- **._load_one_prototype()** (6 connections) — `server/game/items/prototype_registry.py`
- **_prototype_from_equipped_stack()** (6 connections) — `server/game/weapons.py`
- *... and 133 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (13 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (7 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (5 shared connections)
- [server commands admin summon command](server_commands_admin_summon_command.md) (4 shared connections)
- [server commands inventory command prototype](server_commands_inventory_command_prototype.md) (4 shared connections)
- [characterinfo](characterinfo.md) (4 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (3 shared connections)
- [server commands combat attack](server_commands_combat_attack.md) (3 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (2 shared connections)

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
- `server/tests/unit/game/items/test_component_hooks.py`
- `server/tests/unit/game/items/test_item_prototype_models.py`
- `server/tests/unit/game/items/test_prototype_registry.py`
- `server/tests/unit/game/test_item_factory.py`
- `server/tests/unit/game/test_item_instance.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 307 (82%)
- INFERRED: 69 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*