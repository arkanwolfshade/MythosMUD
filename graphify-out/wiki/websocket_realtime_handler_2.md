# websocket realtime handler

> 85 nodes

## Key Concepts

- **test_container_bundles.py** (64 connections) — `server/tests/unit/container/test_container_bundles.py`
- **GameBundle** (50 connections) — `server/container/bundles/game.py`
- **CombatBundle** (28 connections) — `server/container/bundles/combat.py`
- **RealtimeBundle** (25 connections) — `server/container/bundles/realtime.py`
- **CoreBundle** (18 connections) — `server/container/bundles/core.py`
- **NPCBundle** (16 connections) — `server/container/bundles/npc.py`
- **MonitoringBundle** (15 connections) — `server/container/bundles/monitoring.py`
- **.initialize()** (12 connections) — `server/container/main.py`
- **ChatBundle** (10 connections) — `server/container/bundles/chat.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **.initialize()** (7 connections) — `server/container/bundles/chat.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/realtime.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **.shutdown()** (5 connections) — `server/container/main.py`
- **._sanitarium_failover_callback()** (4 connections) — `server/container/bundles/combat.py`
- **.shutdown()** (4 connections) — `server/container/bundles/core.py`
- **._resolve_hourly_holidays()** (3 connections) — `server/container/bundles/game.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- **.shutdown()** (3 connections) — `server/container/bundles/monitoring.py`
- **.shutdown()** (3 connections) — `server/container/bundles/realtime.py`
- **datetime** (2 connections)
- *... and 60 more nodes in this community*

## Relationships

- [nats services service](nats_services_service.md) (42 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (9 shared connections)
- [dead letter queue](dead_letter_queue.md) (9 shared connections)
- [Error Conversion](Error_Conversion.md) (7 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (4 shared connections)
- [player respawn event](player_respawn_event.md) (4 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (3 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)

## Source Files

- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/npc.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 350 (85%)
- INFERRED: 61 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*