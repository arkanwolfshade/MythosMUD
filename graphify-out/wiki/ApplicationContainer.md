# ApplicationContainer

> 293 nodes

## Key Concepts

- **ApplicationContainer** (145 connections) — `server/container/main.py`
- **lifespan_startup.py** (60 connections) — `server/app/lifespan_startup.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **container/main.py** (33 connections) — `server/container/main.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **CombatBundle** (24 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (24 connections) — `server/container/bundles/realtime.py`
- **MythosTimeEventConsumer** (22 connections) — `server/time/time_event_consumer.py`
- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **get_container()** (17 connections) — `server/container/main.py`
- **CoreBundle** (14 connections) — `server/container/bundles/core.py`
- **NPCService** (14 connections) — `server/services/npc_service/__init__.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **FastAPI** (13 connections)
- **bundles/combat.py** (13 connections) — `server/container/bundles/combat.py`
- **bundles/realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **asyncio** (12 connections)
- **initialize_combat_services()** (11 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **lifespan_event_subscriptions.py** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **bundles/monitoring.py** (11 connections) — `server/container/bundles/monitoring.py`
- **_create_npc_services_on_app()** (10 connections) — `server/app/lifespan_startup.py`
- *... and 268 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (42 shared connections)
- [EventBus](EventBus.md) (41 shared connections)
- [get_logger](get_logger.md) (33 shared connections)
- [CombatService](CombatService.md) (16 shared connections)
- [lifespan.py](lifespan.py.md) (14 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (8 shared connections)
- [npc_database.py](npc_database.py.md) (8 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (6 shared connections)
- [LucidityService](LucidityService.md) (6 shared connections)
- [ChatService](ChatService.md) (5 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (5 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (5 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/realtime/event_publisher.py`
- `server/services/npc_service/__init__.py`
- `server/services/npc_startup_service.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/test_application_container.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 781 (94%)
- INFERRED: 52 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*