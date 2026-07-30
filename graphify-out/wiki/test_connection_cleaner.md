# test connection cleaner

> 53 nodes

## Key Concepts

- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **ConnectionErrorHandler** (12 connections) — `server/realtime/errors/error_handler.py`
- **PersonalMessageSender** (11 connections) — `server/realtime/messaging/personal_message_sender.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **__init__.py** (3 connections) — `server/realtime/errors/__init__.py`
- **test_initialize_connection_state()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_health_monitor()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_error_handler()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **test_initialize_connection_cleaner()** (3 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- *... and 28 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (16 shared connections)
- [Player](Player.md) (9 shared connections)
- [GameTerminalContext](GameTerminalContext.md) (7 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (4 shared connections)
- [Coord](Coord.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [Lock](Lock.md) (1 shared connections)
- [GameConfig](GameConfig.md) (1 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [Remove sensitive data from log](Remove_sensitive_data_from_log.md) (1 shared connections)
- [test command parser](test_command_parser.md) (1 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/errors/__init__.py`
- `server/realtime/errors/error_handler.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 209 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*