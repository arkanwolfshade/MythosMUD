# RoomSubscriptionManager

> 47 nodes

## Key Concepts

- **RoomSubscriptionManager** (43 connections) — `server/realtime/room_subscription_manager.py`
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._filter_fallback_npcs()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **._get_online_player_occupants()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.list_room_drops()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.reconcile_room_presence()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.take_room_drop()** (4 connections) — `server/realtime/room_subscription_manager.py`
- **.add_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.adjust_room_drop()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_room_subscribers()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.get_stats()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.remove_room_occupant()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.set_async_persistence()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.unsubscribe_from_room()** (3 connections) — `server/realtime/room_subscription_manager.py`
- **.__init__()** (2 connections) — `server/realtime/room_subscription_manager.py`
- **.remove_player_from_all_rooms()** (2 connections) — `server/realtime/room_subscription_manager.py`
- **Retrieve current room drops as a defensive copy for callers. Args: room_id: The…** (1 connections) — `server/realtime/room_subscription_manager.py`
- *... and 22 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [subscription_manager](subscription_manager.md) (2 shared connections)
- [test_room_subscription_manager_helpers.py](test_room_subscription_manager_helpers.py.md) (2 shared connections)
- [test_room_subscription_manager_npcs.py](test_room_subscription_manager_npcs.py.md) (2 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [test_room_subscription_manager.py](test_room_subscription_manager.py.md) (1 shared connections)
- [test_room_subscription_manager_drops.py](test_room_subscription_manager_drops.py.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/realtime/room_subscription_manager.py`

## Audit Trail

- EXTRACTED: 97 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*