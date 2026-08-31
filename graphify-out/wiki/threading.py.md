# threading.py

> 52 nodes

## Key Concepts

- **threading.py** (45 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (24 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (17 connections) — `server/npc/threading_messages.py`
- **NPCCommunicationBridge** (15 connections) — `server/npc/threading.py`
- **asyncio** (11 connections)
- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **test_bridge_broadcast_failure()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_bridge_receive_message_failure()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_communication_bridge_messages()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_restart_npc_thread()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_start_stop()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_start_stop_npc_thread()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_stop_cancels_running_task()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_process_npc_message_dispatches_wander()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_process_npc_message_handles_errors()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_thread_stop_and_shutdown_drop_pending_keys()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **.add_message()** (2 connections) — `server/npc/threading_messages.py`
- **.clear_all_messages()** (2 connections) — `server/npc/threading_messages.py`
- **.clear_messages()** (2 connections) — `server/npc/threading_messages.py`
- **.get_messages()** (2 connections) — `server/npc/threading_messages.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading_messages.py`
- **.get_total_queue_size()** (2 connections) — `server/npc/threading_messages.py`
- **.__init__()** (2 connections) — `server/npc/threading_messages.py`
- **.broadcast_to_all_npcs()** (2 connections) — `server/npc/threading.py`
- *... and 27 more nodes in this community*

## Relationships

- [NPCThreadManager](NPCThreadManager.md) (13 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [Lock](Lock.md) (2 shared connections)
- [schedule_service.py](schedule_service.py.md) (2 shared connections)
- [safe_run_static](safe_run_static.md) (1 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (1 shared connections)
- [shutdown_process_termination.py](shutdown_process_termination.py.md) (1 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`
- `server/npc/threading.py`
- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 114 (87%)
- INFERRED: 17 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*