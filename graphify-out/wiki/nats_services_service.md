# nats services service

> 99 nodes

## Key Concepts

- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (50 connections) — `server/container/bundles/game.py`
- **CombatBundle** (28 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (25 connections) — `server/container/bundles/realtime.py`
- **MagicBundle** (22 connections) — `server/container/bundles/magic.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **NPCBundle** (16 connections) — `server/container/bundles/npc.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **TimeBundle** (14 connections) — `server/container/bundles/time.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **_validate_magic_prerequisites()** (6 connections) — `server/container/bundles/magic.py`
- **.initialize()** (6 connections) — `server/container/bundles/magic.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/realtime.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **.shutdown()** (5 connections) — `server/container/main.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- *... and 74 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (38 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (14 shared connections)
- [time service rationale](time_service_rationale.md) (8 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (5 shared connections)
- [quest chat game](quest_chat_game.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (4 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (3 shared connections)

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
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/container/test_time_bundle.py`

## Audit Trail

- EXTRACTED: 421 (86%)
- INFERRED: 71 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*