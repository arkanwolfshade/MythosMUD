# connection disconnection realtime

> 205 nodes

## Key Concepts

- **RateLimiter** (61 connections) — `server/realtime/rate_limiter.py`
- **MessageQueue** (54 connections) — `server/realtime/message_queue.py`
- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_connection_rate_limiter.py** (33 connections) — `server/tests/unit/realtime/test_connection_rate_limiter.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **_track_disconnect_if_needed()** (15 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (15 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **message_queue.py** (14 connections) — `server/realtime/message_queue.py`
- **rate_limiter.py** (14 connections) — `server/realtime/rate_limiter.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (12 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (11 connections)
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- *... and 180 more nodes in this community*

## Relationships

- [taunt combat commands](taunt_combat_commands.md) (30 shared connections)
- [spell models rationale](spell_models_rationale.md) (20 shared connections)
- [Loot Generation](Loot_Generation.md) (14 shared connections)
- [services npc startup](services_npc_startup.md) (13 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (10 shared connections)
- [Room Broadcast](Room_Broadcast.md) (10 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (9 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (6 shared connections)
- [room subscription manager](room_subscription_manager.md) (6 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/message_queue.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_rate_limiter.py`

## Audit Trail

- EXTRACTED: 809 (97%)
- INFERRED: 28 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*