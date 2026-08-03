# Error Conversion

> 387 nodes

## Key Concepts

- **ApplicationContainer** (140 connections) — `server/container/main.py`
- **game.py** (42 connections) — `server/container/bundles/game.py`
- **GameBundle** (41 connections) — `server/container/bundles/game.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **.get_instance()** (35 connections) — `server/container/main.py`
- **PrototypeRegistry** (35 connections) — `server/game/items/prototype_registry.py`
- **main.py** (33 connections) — `server/container/main.py`
- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **magic.py** (19 connections) — `server/container/bundles/magic.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **MagicBundle** (18 connections) — `server/container/bundles/magic.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **npc.py** (14 connections) — `server/container/bundles/npc.py`
- *... and 362 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (45 shared connections)
- [time service rationale](time_service_rationale.md) (32 shared connections)
- [game models player](game_models_player.md) (26 shared connections)
- [holiday service services](holiday_service_services.md) (25 shared connections)
- [NPC Combat](NPC_Combat.md) (20 shared connections)
- [Database Config](Database_Config.md) (20 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (19 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (16 shared connections)
- [command base models](command_base_models.md) (12 shared connections)
- [Item Instances](Item_Instances.md) (11 shared connections)
- [command inventory models](command_inventory_models.md) (8 shared connections)
- [item models rationale](item_models_rationale.md) (8 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/constants.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`

## Audit Trail

- EXTRACTED: 1624 (91%)
- INFERRED: 160 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*