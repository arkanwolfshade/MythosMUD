# NPCThreadManager

> 46 nodes

## Key Concepts

- **NPCThreadManager** (30 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (24 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (15 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (13 connections) — `server/npc/threading.py`
- **asyncio** (10 connections)
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.get_npc_definition()** (3 connections) — `server/npc/threading.py`
- **.stop()** (3 connections) — `server/npc/threading.py`
- **test_bridge_broadcast_failure()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_bridge_receive_message_failure()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_communication_bridge_messages()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_restart_npc_thread()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_start_stop()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_start_stop_npc_thread()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_npc_thread_manager_stop_cancels_running_task()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_process_npc_message_dispatches_wander()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **test_process_npc_message_handles_errors()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **.clear_messages()** (2 connections) — `server/npc/threading.py`
- **.get_queue_size()** (2 connections) — `server/npc/threading.py`
- **.get_total_queue_size()** (2 connections) — `server/npc/threading.py`
- **.__init__()** (2 connections) — `server/npc/threading.py`
- **.get_active_npc_threads()** (2 connections) — `server/npc/threading.py`
- *... and 21 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [Any](Any.md) (12 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (5 shared connections)
- [HealthMonitor](HealthMonitor.md) (2 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 89 (84%)
- INFERRED: 17 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*