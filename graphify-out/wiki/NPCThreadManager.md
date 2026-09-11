# NPCThreadManager

> 81 nodes

## Key Concepts

- **NPCThreadManager** (60 connections) — `server/npc/threading.py`
- **test_npc_thread_manager_internals.py** (32 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **asyncio** (17 connections)
- **._execute_wander_movement()** (8 connections) — `server/npc/threading.py`
- **._parse_behavior_config()** (7 connections) — `server/npc/threading.py`
- **._process_wander_action()** (5 connections) — `server/npc/threading.py`
- **._process_npc_message()** (4 connections) — `server/npc/threading.py`
- **._resolve_wander_npc()** (4 connections) — `server/npc/threading.py`
- **.stop_npc_thread()** (4 connections) — `server/npc/threading.py`
- **._stop_npc_thread_internal()** (4 connections) — `server/npc/threading.py`
- **test_bridge_send_message_to_npc_swallows_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_no_instance_service()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_npc_not_active()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_success()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_swallows_inner_execute_error()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_execute_npc_behavior_swallows_outer_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_dict_attr()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_invalid_json_string()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_json_non_dict()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_parse_behavior_config_valid_json_string()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_process_wander_action_handles_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_process_wander_action_returns_early_when_unresolved()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_restart_npc_thread_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_start_swallows_unexpected_exception()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- **test_stop_cancels_active_threads_via_gather()** (4 connections) — `server/tests/unit/npc/test_npc_thread_manager_internals.py`
- *... and 56 more nodes in this community*

## Relationships

- [test_npc_threading_messages.py](test_npc_threading_messages.py.md) (11 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [NPCDefinition](NPCDefinition.md) (7 shared connections)
- [IdleMovementHandler](IdleMovementHandler.md) (2 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [NPCActionMessage](NPCActionMessage.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [.async_persistence](async_persistence.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)

## Source Files

- `server/npc/threading.py`
- `server/tests/unit/npc/test_npc_thread_manager_internals.py`

## Audit Trail

- EXTRACTED: 131 (80%)
- INFERRED: 33 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*