# realtime messaging message

> 35 nodes

## Key Concepts

- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
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
- **Messaging components for connection management.  This package provides modular m** (1 connections) — `server/realtime/messaging/__init__.py`
- **Message broadcasting for connection management.  This module provides room and g** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Read an integer delivery counter from stats dicts typed as dict[str, object].** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Compute recipient list and initial stats for broadcast_global.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcasts messages to rooms and globally.      This class provides:     - Room-** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Convert string player IDs to UUIDs for message sending.          Args:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- *... and 10 more nodes in this community*

## Relationships

- [connection disconnection realtime](connection_disconnection_realtime.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [combat configuration service](combat_configuration_service.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [services npc startup](services_npc_startup.md) (1 shared connections)
- [realtime maintenance connection](realtime_maintenance_connection.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 137 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*