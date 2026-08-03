# room realtime subscription

> 72 nodes

## Key Concepts

- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **test_room_subscription_manager_npcs.py** (13 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.list_room_drops()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_online_player_occupants()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.reconcile_room_presence()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.set_async_persistence()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.unsubscribe_from_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_room_subscribers()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.adjust_room_drop()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.remove_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_stats()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **subscription_manager()** (3 connections) — `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`
- *... and 47 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (4 shared connections)
- [room subscription manager](room_subscription_manager.md) (3 shared connections)
- [realtime messaging message](realtime_messaging_message.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [room subscription realtime](room_subscription_realtime.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [grace period disconnect](grace_period_disconnect.md) (1 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_room_subscription_manager_npcs.py`

## Audit Trail

- EXTRACTED: 225 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*