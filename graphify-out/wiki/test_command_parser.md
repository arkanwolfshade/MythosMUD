# test command parser

> 142 nodes

## Key Concepts

- **game.py** (42 connections) — `server/container/bundles/game.py`
- **GameBundle** (41 connections) — `server/container/bundles/game.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **PrototypeRegistry** (35 connections) — `server/game/items/prototype_registry.py`
- **main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **npc.py** (14 connections) — `server/container/bundles/npc.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **NPCBundle** (11 connections) — `server/container/bundles/npc.py`
- **ItemFactory** (11 connections) — `server/game/items/item_factory.py`
- *... and 117 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (50 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (23 shared connections)
- [world](world.md) (21 shared connections)
- [Any](Any.md) (15 shared connections)
- [real time](real_time.md) (12 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (11 shared connections)
- [Player](Player.md) (10 shared connections)
- [HolidayCollection](HolidayCollection.md) (9 shared connections)
- [test command base](test_command_base.md) (9 shared connections)
- [message handler factory](message_handler_factory.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)

## Source Files

- `server/app/tracked_task_manager.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/game/instance_manager.py`
- `server/game/items/item_factory.py`
- `server/game/items/prototype_registry.py`
- `server/game/level_service.py`
- `server/services/schedule_service.py`
- `server/tests/unit/test_application_container.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 695 (90%)
- INFERRED: 79 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*