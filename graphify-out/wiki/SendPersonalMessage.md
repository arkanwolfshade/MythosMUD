# SendPersonalMessage

> 65 nodes

## Key Concepts

- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **test_message_broadcaster.py** (17 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_message_broadcaster_init()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_exclude_player()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 40 more nodes in this community*

## Relationships

- [circuit breaker](circuit_breaker.md) (4 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 198 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*