# deque

> 122 nodes

## Key Concepts

- **MessageQueue** (60 connections) — `server/realtime/message_queue.py`
- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (26 connections)
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **message_queue.py** (17 connections) — `server/realtime/message_queue.py`
- **personal_message_sender.py** (16 connections) — `server/realtime/messaging/personal_message_sender.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 97 more nodes in this community*

## Relationships

- [server realtime connection error methods](server_realtime_connection_error_methods.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server realtime connection disconnection](server_realtime_connection_disconnection.md) (10 shared connections)
- [server realtime monitoring health monitor](server_realtime_monitoring_health_monitor.md) (9 shared connections)
- [server realtime messaging personal message](server_realtime_messaging_personal_message.md) (7 shared connections)
- [coord](coord.md) (5 shared connections)
- [sendpersonalmessage](sendpersonalmessage.md) (4 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (3 shared connections)
- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (3 shared connections)
- [server realtime connection session management](server_realtime_connection_session_management.md) (3 shared connections)
- [server realtime errors error handler](server_realtime_errors_error_handler.md) (3 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (3 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/message_queue.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_connection_initialization.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 276 (90%)
- INFERRED: 29 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*