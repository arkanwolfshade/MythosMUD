# server realtime connection delegates

> 43 nodes

## Key Concepts

- **connection_delegates.py** (41 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor()** (11 connections) — `server/realtime/connection_delegates.py`
- **validate_token_impl()** (11 connections) — `server/realtime/connection_delegates.py`
- **delegate_health_monitor_sync()** (10 connections) — `server/realtime/connection_delegates.py`
- **UUID** (10 connections)
- **delegate_personal_message_sender()** (9 connections) — `server/realtime/connection_delegates.py`
- **_async_callable()** (8 connections) — `server/realtime/connection_delegates.py`
- **_WebsocketCleanupManager** (7 connections) — `server/realtime/connection_delegates.py`
- **_close_dead_websocket_if_open()** (7 connections) — `server/realtime/connection_delegates.py`
- **delegate_personal_message_sender_sync()** (7 connections) — `server/realtime/connection_delegates.py`
- **delegate_game_state_provider_sync()** (6 connections) — `server/realtime/connection_delegates.py`
- **delegate_room_event_handler()** (6 connections) — `server/realtime/connection_delegates.py`
- **_remove_connection_from_player_list()** (5 connections) — `server/realtime/connection_delegates.py`
- **_sync_callable()** (5 connections) — `server/realtime/connection_delegates.py`
- **WebSocket** (5 connections)
- **_PlayerIdCarrier** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (4 connections) — `server/realtime/connection_delegates.py`
- **_websocket_client_connected()** (4 connections) — `server/realtime/connection_delegates.py`
- **test_delegate_personal_message_sender_success()** (4 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **Protocol** (4 connections)
- **_is_benign_websocket_close_error()** (3 connections) — `server/realtime/connection_delegates.py`
- **.get_player_by_user_id()** (3 connections) — `server/realtime/connection_delegates.py`
- **test_delegate_personal_message_sender_sync_none()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- **test_delegate_personal_message_sender_sync_success()** (3 connections) — `server/tests/unit/realtime/test_connection_delegates.py`
- *... and 18 more nodes in this community*

## Relationships

- [server realtime connection delegates cleanup](server_realtime_connection_delegates_cleanup.md) (37 shared connections)
- [server realtime connection delegates delegate](server_realtime_connection_delegates_delegate.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server realtime connection models connectionmetadata](server_realtime_connection_models_connectionmetadata.md) (2 shared connections)
- [server realtime rate limiter ratelimiter](server_realtime_rate_limiter_ratelimiter.md) (2 shared connections)
- [server auth utils](server_auth_utils.md) (2 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)
- [server realtime connection cleanup methods](server_realtime_connection_cleanup_methods.md) (1 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`
- `server/tests/unit/realtime/test_connection_delegates.py`

## Audit Trail

- EXTRACTED: 133 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*