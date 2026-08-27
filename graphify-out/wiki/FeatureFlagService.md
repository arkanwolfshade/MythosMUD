# FeatureFlagService

> 84 nodes

## Key Concepts

- **test_connection_disconnection.py** (39 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (29 connections) — `server/realtime/connection_disconnection.py`
- **_DisconnectConnectionManager** (22 connections) — `server/realtime/connection_disconnection.py`
- **UUID** (16 connections)
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **asyncio** (14 connections)
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (12 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (11 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_apply_disconnect_side_effects()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_close_and_untrack_websockets()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (5 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_intentional_without_sockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_cleanup_websocket_disconnect_when_mapping_cleared_during_close()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_all_websockets_none_websocket()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_disconnect_connection_by_id_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_force_disconnect_player_impl_intentional_without_sockets()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 59 more nodes in this community*

## Relationships

- [roomHandlers.ts](roomHandlers.ts.md) (18 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (14 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (4 shared connections)
- [QuestService](QuestService.md) (2 shared connections)
- [Commands](Commands.md) (1 shared connections)
- [_parse_env_list](_parse_env_list.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`

## Audit Trail

- EXTRACTED: 200 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*