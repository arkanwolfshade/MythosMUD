# player_service

> 50 nodes

## Key Concepts

- **test_npc_threading_messages.py** (24 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (17 connections) — `server/npc/threading_messages.py`
- **NPCCommunicationBridge** (15 connections) — `server/npc/threading.py`
- **asyncio** (11 connections)
- **.__init__()** (3 connections) — `server/npc/threading.py`
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
- **.get_messages_for_npc()** (2 connections) — `server/npc/threading.py`
- **.get_pending_messages()** (2 connections) — `server/npc/threading.py`
- *... and 25 more nodes in this community*

## Relationships

- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (12 shared connections)
- [fixtures/shared/__init__.py](fixtures-shared-__init__.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 70 (80%)
- INFERRED: 17 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*