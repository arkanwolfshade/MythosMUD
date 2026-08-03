# realtime messaging message

> 17 nodes

## Key Concepts

- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Message broadcasting for connection management.  This module provides room and g** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Read an integer delivery counter from stats dicts typed as dict[str, object].** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Compute recipient list and initial stats for broadcast_global.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Process results from batch message delivery.          Args:             delivery** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Merge asyncio.gather outcomes into global broadcast stats.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Send global broadcast recipients one-by-one after batch failure.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all connected players.          Args:             event:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [realtime maintenance connection](realtime_maintenance_connection.md) (8 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [combat configuration service](combat_configuration_service.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*