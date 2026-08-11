# Async Persistence Migration

> 22 nodes

## Key Concepts

- **deque** (24 connections)
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Clean up large data structures to prevent memory bloat.          Args:** (1 connections) — `server/realtime/message_queue.py`
- **Initialize metrics collection.** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Test MessageQueue.get_messages() handles errors.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.has_messages() returns False for empty list.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() removes old messages.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() removes empty queues.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() handles ISO string timestamps.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() handles invalid timestamps.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_large_structures() trims large queues.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`

## Relationships

- [Playwright E2E Specs](Playwright_E2E_Specs.md) (9 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (7 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (5 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (2 shared connections)
- [Cursor Plans Pydantic](Cursor_Plans_Pydantic.md) (2 shared connections)
- [Mythos Map Builder](Mythos_Map_Builder.md) (1 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (1 shared connections)
- [UI Animation Testing Standards](UI_Animation_Testing_Standards.md) (1 shared connections)
- [Zone Coordinate Generator](Zone_Coordinate_Generator.md) (1 shared connections)
- [Combat Service Bundle](Combat_Service_Bundle.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 43 (59%)
- INFERRED: 30 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*