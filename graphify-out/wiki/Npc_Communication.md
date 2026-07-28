# Npc Communication

> 65 nodes · cohesion 0.04

## Key Concepts

- **MessageBroadcaster** (20 connections) — `server/realtime/messaging/message_broadcaster.py`
- **test_message_broadcaster.py** (17 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **message_broadcaster.py** (16 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_empty()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 40 more nodes in this community*

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (4 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (2 shared connections)
- [Realtime Messaging Message](Realtime_Messaging_Message.md) (2 shared connections)
- [Whisper Work Remaining](Whisper_Work_Remaining.md) (1 shared connections)
- [Whisper Reply Command Tests](Whisper_Reply_Command_Tests.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 200 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*