# Contributing Guidelines

> 14 nodes · cohesion 0.14

## Key Concepts

- **DeadLetterQueue** (35 connections) — `server/realtime/dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_handles_errors()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_handles_read_error()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Clean up old DLQ messages.          Args:             max_age_days: Maximum age** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries.      Implements file-based storage f** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterQueue initialization without storage directory.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats with messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() returns empty list when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() handles file errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [Room Validator Instructions](Room_Validator_Instructions.md) (12 shared connections)
- [Cursor Workflows Docs](Cursor_Workflows_Docs.md) (7 shared connections)
- [Dead Letter Queue](Dead_Letter_Queue.md) (5 shared connections)
- [Realtime Schemas Presence](Realtime_Schemas_Presence.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (1 shared connections)
- [Migration Verification](Migration_Verification.md) (1 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*