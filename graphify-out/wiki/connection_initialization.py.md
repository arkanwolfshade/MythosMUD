# connection_initialization.py

> 74 nodes

## Key Concepts

- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **test_connection_initialization.py** (18 connections) — `server/tests/unit/realtime/test_connection_initialization.py`
- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **initialize_core_components()** (13 connections) — `server/realtime/connection_initialization.py`
- **.__init__()** (12 connections) — `server/realtime/connection_manager.py`
- **initialize_connection_state()** (9 connections) — `server/realtime/connection_initialization.py`
- **initialize_messaging()** (9 connections) — `server/realtime/connection_initialization.py`
- **UUID** (9 connections)
- **initialize_connection_cleaner()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_error_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_game_state_provider()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_health_monitor()** (8 connections) — `server/realtime/connection_initialization.py`
- **initialize_room_event_handler()** (8 connections) — `server/realtime/connection_initialization.py`
- **Any** (8 connections)
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **server/realtime/messaging/__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- *... and 49 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (13 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [build_event](build_event.md) (7 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (4 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (3 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (3 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (3 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (3 shared connections)
- [ConnectionCleaner](ConnectionCleaner.md) (2 shared connections)
- [deque](deque.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [MessageQueue](MessageQueue.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/connection_manager.py`
- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/test_connection_initialization.py`

## Audit Trail

- EXTRACTED: 192 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*