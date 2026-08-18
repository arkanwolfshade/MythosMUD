# holidayresolver

> 107 nodes

## Key Concepts

- **NPCThreadManager** (33 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (24 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (17 connections) — `server/npc/threading_messages.py`
- **NPCCommunicationBridge** (13 connections) — `server/npc/threading.py`
- **NPCActionMessage** (12 connections) — `server/npc/threading_messages.py`
- **threading_messages.py** (11 connections) — `server/npc/threading_messages.py`
- **asyncio** (11 connections)
- **.from_dict()** (8 connections) — `server/npc/threading_messages.py`
- **Lock** (8 connections)
- **._execute_wander_movement()** (7 connections) — `server/npc/threading.py`
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **NPCActionType** (6 connections) — `server/npc/threading_messages.py`
- **._npc_thread_worker()** (6 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_wander_action()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.from_json()** (4 connections) — `server/npc/threading_messages.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **._process_npc_message()** (4 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.to_dict()** (3 connections) — `server/npc/threading_messages.py`
- *... and 82 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (15 shared connections)
- [jsondict](jsondict.md) (5 shared connections)
- [server npc passive mob npc](server_npc_passive_mob_npc.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server npc idle movement idlemovementhandler](server_npc_idle_movement_idlemovementhandler.md) (2 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server services inventory mutation guard](server_services_inventory_mutation_guard.md) (2 shared connections)
- [server events event types npcdied](server_events_event_types_npcdied.md) (1 shared connections)
- [server middleware metrics collector](server_middleware_metrics_collector.md) (1 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)
- [server app task registry](server_app_task_registry.md) (1 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 167 (85%)
- INFERRED: 29 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*