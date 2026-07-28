# Server Realtime (15)

> 82 nodes

## Key Concepts

- **MessageQueue** (49 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (24 connections)
- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **Any** (4 connections)
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_message_queue_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_init_custom()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 57 more nodes in this community*

## Relationships

- [Data Local](Data_Local.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Realtime (64)](Server_Realtime_%2864%29.md) (2 shared connections)
- [Server Realtime (85)](Server_Realtime_%2885%29.md) (2 shared connections)
- [Scripts (10)](Scripts_%2810%29.md) (1 shared connections)
- [Docs Examples](Docs_Examples.md) (1 shared connections)
- [Server Realtime (90)](Server_Realtime_%2890%29.md) (1 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (1 shared connections)
- [Server Services (57)](Server_Services_%2857%29.md) (1 shared connections)
- [Server Monitoring](Server_Monitoring.md) (1 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 245 (88%)
- INFERRED: 34 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*