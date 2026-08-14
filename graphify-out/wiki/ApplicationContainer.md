# ApplicationContainer

> 308 nodes

## Key Concepts

- **ApplicationContainer** (156 connections) — `server/container/main.py`
- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (54 connections) — `server/container/bundles/game.py`
- **bundles/game.py** (43 connections) — `server/container/bundles/game.py`
- **container/main.py** (34 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (32 connections) — `server/container/bundles/realtime.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **asyncio** (23 connections)
- **NPCBundle** (19 connections) — `server/container/bundles/npc.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **bundles/realtime.py** (14 connections) — `server/container/bundles/realtime.py`
- **ItemPrototype** (13 connections) — `server/models/item.py`
- **bundles/monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- *... and 283 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (58 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (34 shared connections)
- [test_application_container.py](test_application_container.py.md) (31 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (16 shared connections)
- [CombatService](CombatService.md) (14 shared connections)
- [normalize_environment](normalize_environment.md) (12 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (10 shared connections)
- [Player](Player.md) (9 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (8 shared connections)
- [EventBus](EventBus.md) (7 shared connections)
- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [test_lifespan_shutdown.py](test_lifespan_shutdown.py.md) (6 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/game/instance_manager.py`
- `server/models/item.py`
- `server/realtime/message_handlers.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`

## Audit Trail

- EXTRACTED: 868 (93%)
- INFERRED: 69 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*