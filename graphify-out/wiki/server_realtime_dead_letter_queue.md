# server realtime dead letter queue

> 85 nodes

## Key Concepts

- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Any** (7 connections)
- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **Path** (5 connections)
- **.enqueue()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_no_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_datetime_timestamp()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_delete_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_removes_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_oldest_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_writes_correct_data()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- *... and 60 more nodes in this community*

## Relationships

- [server realtime event handlers](server_realtime_event_handlers.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server schemas realtime init](server_schemas_realtime_init.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 114 (75%)
- INFERRED: 39 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*