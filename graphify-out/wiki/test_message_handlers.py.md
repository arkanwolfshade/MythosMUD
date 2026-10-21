# test_message_handlers.py

> 210 nodes · cohesion 0.02

## Key Concepts

- **ApplicationContainer** (162 connections) — `server/container/main.py`
- **test_container_bundles.py** (72 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (61 connections) — `server/container/bundles/game.py`
- **bundles/game.py** (48 connections) — `server/container/bundles/game.py`
- **container/main.py** (42 connections) — `server/container/main.py`
- **CombatBundle** (36 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (33 connections) — `server/container/bundles/realtime.py`
- **asyncio** (25 connections)
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **NPCBundle** (21 connections) — `server/container/bundles/npc.py`
- **TimeBundle** (21 connections) — `server/container/bundles/time.py`
- **bundles/combat.py** (20 connections) — `server/container/bundles/combat.py`
- **bundles/npc.py** (20 connections) — `server/container/bundles/npc.py`
- **core.py** (19 connections) — `server/container/bundles/core.py`
- **bundles/__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **container/__init__.py** (18 connections) — `server/container/__init__.py`
- **._init_player_quest_layer()** (17 connections) — `server/container/bundles/game.py`
- **MonitoringBundle** (17 connections) — `server/container/bundles/monitoring.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **bundles/monitoring.py** (14 connections) — `server/container/bundles/monitoring.py`
- **bundles/realtime.py** (14 connections) — `server/container/bundles/realtime.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **.initialize()** (12 connections) — `server/container/bundles/core.py`
- *... and 185 more nodes in this community*

## Relationships

- [websocket_integration.py](websocket_integration.py.md) (31 shared connections)
- [Room](Room.md) (26 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (18 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (16 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (12 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (11 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (11 shared connections)
- [start_grace_period](start_grace_period.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (9 shared connections)
- [multiplayer-colocated.ts](multiplayer-colocated.ts.md) (8 shared connections)
- [endpoints.py](endpoints.py.md) (7 shared connections)
- [BaseEvent](BaseEvent.md) (7 shared connections)

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
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 735 (86%)
- INFERRED: 122 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*