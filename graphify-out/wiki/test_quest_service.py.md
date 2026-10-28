# test_quest_service.py

> 82 nodes · cohesion 0.04

## Key Concepts

- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (28 connections)
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **Any** (4 connections)
- **test_message_queue_add_message_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 57 more nodes in this community*

## Relationships

- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (8 shared connections)
- [SpellEffects](SpellEffects.md) (8 shared connections)
- [Test Suite Optimization Roadmap](Test_Suite_Optimization_Roadmap.md) (5 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (3 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (3 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (3 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (2 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [test_combat_validator.py](test_combat_validator.py.md) (2 shared connections)

## Source Files

- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 148 (83%)
- INFERRED: 31 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*