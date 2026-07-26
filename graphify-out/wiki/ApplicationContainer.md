# ApplicationContainer

> 184 nodes · cohesion 0.02

## Key Concepts

- **ApplicationContainer** (139 connections) — `server/container/main.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **CombatBundle** (19 connections) — `server/container/bundles/combat.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **magic.py** (19 connections) — `server/container/bundles/magic.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **MagicBundle** (18 connections) — `server/container/bundles/magic.py`
- **RealtimeBundle** (17 connections) — `server/container/bundles/realtime.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **combat.py** (13 connections) — `server/container/bundles/combat.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **realtime.py** (12 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **DistributedEventBus** (12 connections) — `server/events/distributed_event_bus.py`
- **monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **NPCBundle** (11 connections) — `server/container/bundles/npc.py`
- **init_npc_db()** (11 connections) — `server/npc_database.py`
- **_create_learning_mp_regen_and_magic()** (9 connections) — `server/container/bundles/magic.py`
- **close_npc_db()** (9 connections) — `server/npc_database.py`
- **chat.py** (8 connections) — `server/container/bundles/chat.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- *... and 159 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (55 shared connections)
- [SpellRegistry](SpellRegistry.md) (22 shared connections)
- [CombatService](CombatService.md) (19 shared connections)
- [lifespan.py](lifespan.py.md) (18 shared connections)
- [__init__.py](__init__.py.md) (14 shared connections)
- [test_lifespan_startup.py](test_lifespan_startup.py.md) (10 shared connections)
- [test_npc_database.py](test_npc_database.py.md) (9 shared connections)
- [Player](Player.md) (8 shared connections)
- [TaskRegistry](TaskRegistry.md) (7 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [dependencies.py](dependencies.py.md) (6 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/events/distributed_event_bus.py`
- `server/npc_database.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 813 (92%)
- INFERRED: 72 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*