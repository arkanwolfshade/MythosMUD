# Weapon Resolution Helpers

> 106 nodes · cohesion 0.03

## Key Concepts

- **PrototypeRegistry** (41 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (25 connections) — `server/game/items/prototype_registry.py`
- **ItemPrototypeModel** (24 connections) — `server/game/items/models.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **test_weapons.py** (15 connections) — `server/tests/unit/game/test_weapons.py`
- **ItemFactory** (15 connections) — `server/game/items/item_factory.py`
- **__init__.py** (11 connections) — `server/game/items/__init__.py`
- **item_factory.py** (10 connections) — `server/game/items/item_factory.py`
- **ItemInstance** (10 connections) — `server/game/items/item_instance.py`
- **test_combat_weapon_resolution.py** (9 connections) — `server/tests/integration/test_combat_weapon_resolution.py`
- **ItemFactoryError** (9 connections) — `server/game/items/item_factory.py`
- **prototype_registry.py** (9 connections) — `server/game/items/prototype_registry.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **WeaponAttackInfo** (8 connections) — `server/game/weapons.py`
- **weapons.py** (6 connections) — `server/game/weapons.py`
- **.create_instance()** (6 connections) — `server/game/items/item_factory.py`
- **.load_from_path()** (6 connections) — `server/game/items/prototype_registry.py`
- **validate_prototypes.py** (6 connections) — `server/scripts/validate_prototypes.py`
- **ItemPrototypeModel** (5 connections) — `server/game/items/prototype_registry.py`
- **initialize_components()** (5 connections) — `server/game/items/component_hooks.py`
- **.get()** (5 connections) — `server/game/items/prototype_registry.py`
- **test_resolve_weapon_attack_from_equipped_registry_error_returns_none()** (4 connections) — `server/tests/unit/game/test_weapons.py`
- **ItemInstance** (4 connections) — `server/game/items/item_factory.py`
- **Any** (4 connections) — `server/game/items/item_factory.py`
- **PrototypeRegistry** (4 connections) — `server/game/items/item_factory.py`
- *... and 81 more nodes in this community*

## Relationships

- [[Game Service Bundle]] (23 shared connections)
- [[Combat Aggro Threat]] (11 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[Admin Summon Command]] (4 shared connections)
- [[Combat Attack Flow]] (2 shared connections)
- [[Combat Domain Events]] (2 shared connections)
- [[System Monitoring API]] (2 shared connections)
- [[Player Schema Converter]] (2 shared connections)
- [[Migrate Async Persistence]] (1 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/weapons.py`
- `server/models/item.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/integration/test_combat_weapon_resolution.py`
- `server/tests/unit/game/test_weapons.py`

## Audit Trail

- EXTRACTED: 333 (81%)
- INFERRED: 79 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
