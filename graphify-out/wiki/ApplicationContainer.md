# ApplicationContainer

> 248 nodes

## Key Concepts

- **ApplicationContainer** (162 connections) — `server/container/main.py`
- **test_container_bundles.py** (72 connections) — `server/tests/unit/container/test_container_bundles.py`
- **container/main.py** (38 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **asyncio** (25 connections)
- **.get_instance()** (23 connections) — `server/container/main.py`
- **NPCBundle** (21 connections) — `server/container/bundles/npc.py`
- **TimeBundle** (21 connections) — `server/container/bundles/time.py`
- **get_container()** (21 connections) — `server/container/main.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **MonitoringBundle** (17 connections) — `server/container/bundles/monitoring.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **bundles/monitoring.py** (14 connections) — `server/container/bundles/monitoring.py`
- **bundles/realtime.py** (14 connections) — `server/container/bundles/realtime.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- *... and 223 more nodes in this community*

## Relationships

- [GameBundle](GameBundle.md) (29 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (20 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [time.py](time.py.md) (14 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (13 shared connections)
- [event_types.py](event_types.py.md) (12 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (11 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (9 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (6 shared connections)
- [TargetMatch](TargetMatch.md) (6 shared connections)
- [NPCBase](NPCBase.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)

## Source Files

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
- `server/services/combat_service_types.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 696 (88%)
- INFERRED: 92 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*