# Server App (2)

> 130 nodes

## Key Concepts

- **TaskRegistry** (33 connections) — `server/app/task_registry.py`
- **main.py** (33 connections) — `server/container/main.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **TrackedTaskManager** (14 connections) — `server/app/tracked_task_manager.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **npc.py** (14 connections) — `server/container/bundles/npc.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **NPCBundle** (11 connections) — `server/container/bundles/npc.py`
- **Any** (10 connections)
- **._setup_task_tracking()** (9 connections) — `server/app/task_registry.py`
- **Task** (8 connections)
- **TimeBundle** (8 connections) — `server/container/bundles/time.py`
- **TaskMetadata** (7 connections) — `server/app/task_registry.py`
- **.register_task()** (7 connections) — `server/app/task_registry.py`
- **.shutdown_all()** (7 connections) — `server/app/task_registry.py`
- **.initialize_nats_combat()** (7 connections) — `server/container/bundles/combat.py`
- **chat.py** (6 connections) — `server/container/bundles/chat.py`
- **ChatBundle** (6 connections) — `server/container/bundles/chat.py`
- **._create_task_completion_callback()** (5 connections) — `server/app/task_registry.py`
- *... and 105 more nodes in this community*

## Relationships

- [Server App](Server_App.md) (25 shared connections)
- [Server Commands](Server_Commands.md) (23 shared connections)
- [Server Events](Server_Events.md) (9 shared connections)
- [Server Realtime (16)](Server_Realtime_%2816%29.md) (6 shared connections)
- [Server Npc](Server_Npc.md) (6 shared connections)
- [Server Container](Server_Container.md) (5 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (5 shared connections)
- [Server Services](Server_Services.md) (5 shared connections)
- [Server Infrastructure (2)](Server_Infrastructure_%282%29.md) (5 shared connections)
- [Server Infrastructure (7)](Server_Infrastructure_%287%29.md) (5 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (5 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (4 shared connections)

## Source Files

- `server/app/task_registry.py`
- `server/app/tracked_task_manager.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`

## Audit Trail

- EXTRACTED: 488 (93%)
- INFERRED: 35 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*