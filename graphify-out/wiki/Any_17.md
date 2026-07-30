# Any

> 54 nodes

## Key Concepts

- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **._query_npcs_from_lifecycle_manager()** (6 connections) — `server/realtime/room_subscription_manager.py`
- **._add_npc_to_occupants()** (5 connections) — `server/realtime/room_subscription_manager.py`
- **mock_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
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
- **subscription_manager()** (3 connections) — `server/tests/unit/realtime/test_room_subscription_manager_drops.py`
- *... and 29 more nodes in this community*

## Relationships

- [connection disconnection](connection_disconnection.md) (4 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (4 shared connections)
- [SendPersonalMessage](SendPersonalMessage.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [test room subscription manager](test_room_subscription_manager.md) (2 shared connections)
- [test room subscription manager drops](test_room_subscription_manager_drops.md) (2 shared connections)
- [Represents the configuration for a](Represents_the_configuration_for_a.md) (2 shared connections)
- [Reset the current tick for](Reset_the_current_tick_for.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (2 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (1 shared connections)
- [nats config()](nats_config%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_room_subscription_manager_drops.py`

## Audit Trail

- EXTRACTED: 187 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*