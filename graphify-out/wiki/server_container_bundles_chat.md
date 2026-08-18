# server container bundles chat

> 135 nodes

## Key Concepts

- **test_container_bundles.py** (65 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (54 connections) — `server/container/bundles/game.py`
- **container/main.py** (37 connections) — `server/container/main.py`
- **CombatBundle** (33 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (23 connections)
- **NPCBundle** (19 connections) — `server/container/bundles/npc.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **bundles/realtime.py** (15 connections) — `server/container/bundles/realtime.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **bundles/combat.py** (14 connections) — `server/container/bundles/combat.py`
- **bundles/monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **test_realtime_bundle_nats.py** (11 connections) — `server/tests/unit/container/test_realtime_bundle_nats.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **._initialize_primary_bundles()** (10 connections) — `server/container/main.py`
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._connect_nats()** (7 connections) — `server/container/bundles/realtime.py`
- **_flatten_bundle()** (7 connections) — `server/container/main.py`
- *... and 110 more nodes in this community*

## Relationships

- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (45 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (19 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (15 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (15 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (8 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (8 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (8 shared connections)
- [server container bundles chat chatbundle](server_container_bundles_chat_chatbundle.md) (3 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (3 shared connections)
- [server realtime event publisher eventpublisher](server_realtime_event_publisher_eventpublisher.md) (3 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (3 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (3 shared connections)

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
- `server/tests/unit/container/test_realtime_bundle_nats.py`
- `server/tests/unit/container/test_time_bundle.py`

## Audit Trail

- EXTRACTED: 389 (81%)
- INFERRED: 90 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*