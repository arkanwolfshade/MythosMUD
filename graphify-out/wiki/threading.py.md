# threading.py

> 62 nodes

## Key Concepts

- **threading.py** (45 connections) — `server/npc/threading.py`
- **server/npc/__init__.py** (22 connections) — `server/npc/__init__.py`
- **NPCActionMessage** (12 connections) — `server/npc/threading.py`
- **NPCMessageQueue** (11 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (10 connections) — `server/npc/threading.py`
- **NPCActionType** (8 connections) — `server/npc/threading.py`
- **.schedule_idle_movement()** (6 connections) — `server/npc/passive_mob_npc.py`
- **.wander()** (6 connections) — `server/npc/passive_mob_npc.py`
- **._queue_wander_action()** (5 connections) — `server/npc/passive_mob_npc.py`
- **.from_dict()** (5 connections) — `server/npc/threading.py`
- **._create_wander_action()** (4 connections) — `server/npc/passive_mob_npc.py`
- **.to_dict()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **._handle_wander()** (3 connections) — `server/npc/passive_mob_npc.py`
- **._should_schedule_movement()** (3 connections) — `server/npc/passive_mob_npc.py`
- **.from_json()** (3 connections) — `server/npc/threading.py`
- **.to_json()** (3 connections) — `server/npc/threading.py`
- **.broadcast_to_all_npcs()** (3 connections) — `server/npc/threading.py`
- **.get_messages_for_npc()** (3 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (3 connections) — `server/npc/threading.py`
- **.receive_message_from_npc()** (3 connections) — `server/npc/threading.py`
- **.send_message_to_npc()** (3 connections) — `server/npc/threading.py`
- **.add_message()** (3 connections) — `server/npc/threading.py`
- *... and 37 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (21 shared connections)
- [EventBus](EventBus.md) (19 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [.__post_init__](__post_init__.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [shutdown_process_termination.py](shutdown_process_termination.py.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`
- `server/npc/__init__.py`
- `server/npc/passive_mob_npc.py`
- `server/npc/threading.py`

## Audit Trail

- EXTRACTED: 216 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*