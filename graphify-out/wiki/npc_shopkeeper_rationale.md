# npc shopkeeper rationale

> 163 nodes

## Key Concepts

- **threading.py** (47 connections) — `server/npc/threading.py`
- **PassiveMobNPC** (29 connections) — `server/npc/passive_mob_npc.py`
- **NPCEventReactionSystem** (25 connections) — `server/npc/event_reaction_system.py`
- **__init__.py** (22 connections) — `server/npc/__init__.py`
- **NPCThreadManager** (22 connections) — `server/npc/threading.py`
- **passive_mob_npc.py** (18 connections) — `server/npc/passive_mob_npc.py`
- **behaviors.py** (17 connections) — `server/npc/behaviors.py`
- **ShopkeeperNPC** (17 connections) — `server/npc/shopkeeper_npc.py`
- **NPCActionMessage** (12 connections) — `server/npc/threading.py`
- **shopkeeper_npc.py** (11 connections) — `server/npc/shopkeeper_npc.py`
- **Any** (11 connections)
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **NPCActionType** (8 connections) — `server/npc/threading.py`
- **._npc_thread_worker()** (8 connections) — `server/npc/threading.py`
- **._process_wander_action()** (8 connections) — `server/npc/threading.py`
- **test_npc_base.py** (8 connections) — `server/tests/unit/npc/test_npc_base.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.__init__()** (5 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.from_dict()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- *... and 138 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (35 shared connections)
- [item models rationale](item_models_rationale.md) (18 shared connections)
- [config models player](config_models_player.md) (10 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [commands npc admin](commands_npc_admin.md) (5 shared connections)
- [lucidity event services](lucidity_event_services.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (3 shared connections)
- [commands logout helpers](commands_logout_helpers.md) (2 shared connections)
- [behavior engine npc](behavior_engine_npc.md) (2 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`
- `server/npc/__init__.py`
- `server/npc/behaviors.py`
- `server/npc/event_reaction_system.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/shopkeeper_npc.py`
- `server/npc/threading.py`
- `server/tests/unit/npc/test_event_reaction_speech.py`
- `server/tests/unit/npc/test_npc_base.py`

## Audit Trail

- EXTRACTED: 544 (95%)
- INFERRED: 27 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*