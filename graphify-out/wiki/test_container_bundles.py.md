# test_container_bundles.py

> 84 nodes

## Key Concepts

- **test_container_bundles.py** (65 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (54 connections) — `server/container/bundles/game.py`
- **container/main.py** (35 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (23 connections)
- **NPCBundle** (19 connections) — `server/container/bundles/npc.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **bundles/npc.py** (15 connections) — `server/container/bundles/npc.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **bundles/monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **._initialize_primary_bundles()** (10 connections) — `server/container/main.py`
- **.initialize()** (6 connections) — `server/container/bundles/npc.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/realtime.py`
- **.shutdown()** (5 connections) — `server/container/main.py`
- **._load_npc_definitions()** (4 connections) — `server/container/bundles/npc.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- **.shutdown()** (3 connections) — `server/container/bundles/monitoring.py`
- **.shutdown()** (3 connections) — `server/container/bundles/realtime.py`
- **test_chat_bundle_initialize_missing_player_service()** (3 connections) — `server/tests/unit/container/test_container_bundles.py`
- *... and 59 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (56 shared connections)
- [magic.py](magic.py.md) (15 shared connections)
- [ConnectionManager](ConnectionManager.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_realtime_bundle_nats.py](test_realtime_bundle_nats.py.md) (7 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (7 shared connections)
- [test_application_container_main.py](test_application_container_main.py.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [.initialize_nats_combat](initialize_nats_combat.md) (4 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (4 shared connections)
- [._connect_nats](_connect_nats.md) (4 shared connections)

## Source Files

- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 271 (74%)
- INFERRED: 97 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*