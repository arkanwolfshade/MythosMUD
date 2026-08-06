# connection disconnection realtime

> 150 nodes

## Key Concepts

- **connection_manager_methods.py** (80 connections) — `server/realtime/connection_manager_methods.py`
- **RoomSubscriptionManager** (46 connections) — `server/realtime/room_subscription_manager.py`
- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (15 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (15 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (15 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **Any** (13 connections)
- **._canonical_room_id()** (13 connections) — `server/realtime/room_subscription_manager.py`
- **_cleanup_player_data()** (12 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (11 connections)
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.get_room_occupants()** (8 connections) — `server/realtime/room_subscription_manager.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **is_websocket_open_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **._get_fallback_npcs_from_room()** (7 connections) — `server/realtime/room_subscription_manager.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- *... and 125 more nodes in this community*

## Relationships

- [Room Broadcast](Room_Broadcast.md) (47 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (18 shared connections)
- [Error Conversion](Error_Conversion.md) (17 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (10 shared connections)
- [spell models rationale](spell_models_rationale.md) (8 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (7 shared connections)
- [persistence container parse](persistence_container_parse.md) (5 shared connections)
- [message handler factory](message_handler_factory.md) (2 shared connections)
- [realtime connection helpers](realtime_connection_helpers.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [services chat logger](services_chat_logger.md) (2 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`

## Audit Trail

- EXTRACTED: 652 (98%)
- INFERRED: 15 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*