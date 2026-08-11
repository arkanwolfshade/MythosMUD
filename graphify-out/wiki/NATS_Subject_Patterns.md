# NATS Subject Patterns

> 168 nodes

## Key Concepts

- **MessageQueue** (52 connections) — `server/realtime/message_queue.py`
- **test_connection_disconnection.py** (34 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (32 connections) — `server/realtime/connection_disconnection.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **_DisconnectConnectionManager** (20 connections) — `server/realtime/connection_disconnection.py`
- **test_connection_disconnection_websockets.py** (19 connections) — `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (13 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **safe_close_websocket_impl()** (13 connections) — `server/realtime/connection_manager_methods.py`
- **message_queue.py** (13 connections) — `server/realtime/message_queue.py`
- **UUID** (12 connections)
- **rate_limiter.py** (12 connections) — `server/realtime/rate_limiter.py`
- **_cleanup_player_data()** (10 connections) — `server/realtime/connection_disconnection.py`
- **_run_websocket_disconnect_cleanup()** (9 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **mock_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 143 more nodes in this community*

## Relationships

- [Players API Endpoints](Players_API_Endpoints.md) (11 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Realtime Payload Optimizer](Realtime_Payload_Optimizer.md) (9 shared connections)
- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (8 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (4 shared connections)
- [JSONB Column Parsing](JSONB_Column_Parsing.md) (4 shared connections)
- [WebSocket Connection Setup](WebSocket_Connection_Setup.md) (3 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (3 shared connections)
- [Unified Command Handler](Unified_Command_Handler.md) (3 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/message_queue.py`
- `server/realtime/rate_limiter.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 610 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*