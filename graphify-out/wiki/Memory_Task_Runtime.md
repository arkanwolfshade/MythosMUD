# Memory Task Runtime

> 309 nodes

## Key Concepts

- **game.py** (42 connections) — `server/container/bundles/game.py`
- **GameBundle** (41 connections) — `server/container/bundles/game.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **project_paths.py** (12 connections) — `server/utils/project_paths.py`
- **monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- *... and 284 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (61 shared connections)
- [NATS Messaging](NATS_Messaging.md) (57 shared connections)
- [time service rationale](time_service_rationale.md) (14 shared connections)
- [Item Instances](Item_Instances.md) (12 shared connections)
- [player model models](player_model_models.md) (12 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (9 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [services combat sync](services_combat_sync.md) (7 shared connections)
- [calendar schemas validate](calendar_schemas_validate.md) (7 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (5 shared connections)
- [project paths rationale](project_paths_rationale.md) (5 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/game/instance_manager.py`
- `server/realtime/nats_message_handler.py`
- `server/services/schedule_service.py`
- `server/tests/unit/test_application_container.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/time/tick_scheduler.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 1140 (93%)
- INFERRED: 89 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*