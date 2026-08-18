# server realtime room subscription manager

> 47 nodes

## Key Concepts

- **RoomSubscriptionManager** (52 connections) — `server/realtime/room_subscription_manager.py`
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

- [server tests unit realtime test](server_tests_unit_realtime_test.md) (8 shared connections)
- [server realtime connection disconnection](server_realtime_connection_disconnection.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [deque](deque.md) (2 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (2 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (2 shared connections)
- [server realtime connection manager methods](server_realtime_connection_manager_methods.md) (2 shared connections)
- [server realtime connection session management](server_realtime_connection_session_management.md) (2 shared connections)
- [sendpersonalmessage](sendpersonalmessage.md) (2 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (1 shared connections)
- [server realtime integration init](server_realtime_integration_init.md) (1 shared connections)
- [server realtime monitoring health monitor](server_realtime_monitoring_health_monitor.md) (1 shared connections)

## Source Files

- `server/realtime/room_subscription_manager.py`

## Audit Trail

- EXTRACTED: 97 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*