# NPCThreadManager

> 54 nodes

## Key Concepts

- **NPCThreadManager** (30 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (25 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (15 connections) — `server/npc/threading.py`
- **NPCCommunicationBridge** (13 connections) — `server/npc/threading.py`
- **asyncio** (10 connections)
- **._npc_thread_worker()** (6 connections) — `server/npc/threading.py`
- **._execute_npc_behavior()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (5 connections) — `server/npc/threading.py`
- **.restart_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.start_npc_thread()** (5 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
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
- *... and 29 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [Any](Any.md) (13 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (5 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 105 (87%)
- INFERRED: 16 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*