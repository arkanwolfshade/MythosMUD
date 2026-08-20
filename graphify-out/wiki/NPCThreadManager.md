# NPCThreadManager

> 72 nodes

## Key Concepts

- **NPCThreadManager** (33 connections) — `server/npc/threading.py`
- **test_npc_threading_messages.py** (24 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- **NPCMessageQueue** (17 connections) — `server/npc/threading_messages.py`
- **NPCCommunicationBridge** (13 connections) — `server/npc/threading.py`
- **asyncio** (11 connections)
- **._execute_wander_movement()** (7 connections) — `server/npc/threading.py`
- **._process_wander_action()** (5 connections) — `server/npc/threading.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **._process_npc_message()** (4 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **.get_npc_definition()** (3 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (3 connections) — `server/npc/threading.py`
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
- **test_thread_stop_and_shutdown_drop_pending_keys()** (3 connections) — `server/tests/unit/npc/test_npc_threading_messages.py`
- *... and 47 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (5 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (4 shared connections)
- [NPCCommunicationIntegration](NPCCommunicationIntegration.md) (2 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (2 shared connections)
- [.get_instance](get_instance.md) (2 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (1 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/npc/threading_messages.py`
- `server/tests/unit/npc/test_npc_threading_messages.py`

## Audit Trail

- EXTRACTED: 111 (84%)
- INFERRED: 21 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*