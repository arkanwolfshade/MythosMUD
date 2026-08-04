# combat configuration service

> 76 nodes

## Key Concepts

- **test_message_broadcaster.py** (22 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_message_broadcaster_init()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_exclude_player()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 51 more nodes in this community*

## Relationships

- [services npc startup](services_npc_startup.md) (5 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 218 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*