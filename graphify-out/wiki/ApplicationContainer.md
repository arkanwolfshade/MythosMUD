# ApplicationContainer

> 214 nodes

## Key Concepts

- **ApplicationContainer** (157 connections) — `server/container/main.py`
- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (54 connections) — `server/container/bundles/game.py`
- **container/main.py** (34 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (23 connections)
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **NPCBundle** (19 connections) — `server/container/bundles/npc.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **bundles/realtime.py** (14 connections) — `server/container/bundles/realtime.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **bundles/monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- *... and 189 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (53 shared connections)
- [.get_instance](get_instance.md) (30 shared connections)
- [HolidayService](HolidayService.md) (17 shared connections)
- [lifespan.py](lifespan.py.md) (15 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (15 shared connections)
- [test_chat_npc_system.py](test_chat_npc_system.py.md) (10 shared connections)
- [npc_database.py](npc_database.py.md) (9 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [Player](Player.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (6 shared connections)
- [DatabaseManager](DatabaseManager.md) (5 shared connections)

## Source Files

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
- `server/game/chat_npc_system.py`
- `server/npc_database.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/container/test_time_bundle.py`
- `server/tests/unit/services/nats_subject_manager/test_manager.py`

## Audit Trail

- EXTRACTED: 629 (81%)
- INFERRED: 145 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*