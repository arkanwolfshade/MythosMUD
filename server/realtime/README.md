# Server Realtime Module

This directory contains WebSocket connection handling, message routing, and
real-time broadcast logic for MythosMUD. It works with the FastAPI real-time
router and NATS for server-to-server and room events.

## Entry Points

- **API routes**: [server/api/real_time.py](../api/real_time.py) defines the WebSocket
  endpoints:
  - `GET /api/ws` — primary endpoint (JWT via query or subprotocol; session_id optional)
  - `GET /api/ws/{player_id}` — deprecated; prefer `/api/ws` with JWT
- Incoming client connections are accepted, validated (token, persistence), then
  handed to `handle_websocket_connection` in `websocket_handler`.

## Connection Lifecycle

1. **Accept and validate**: `real_time.websocket_endpoint` (or compat route) validates
   the connection manager and persistence, parses token, resolves player_id.
2. **Connect**: [websocket_handler.py](websocket_handler.py) `handle_websocket_connection`
   calls [connection_manager.py](connection_manager.py) `connect_websocket`, sends
   initial game and room state, then sends a welcome event.
3. **Message loop**: `_handle_websocket_message_loop` receives text frames, validates
   (rate limit, message validator), then dispatches via the message handler factory.
4. **Disconnect**: On close or error, `_cleanup_connection` runs: follow/party
   cleanup, `disconnect_websocket`, mute data cleanup.

The [ConnectionManager](connection_manager.py) holds active WebSockets, player-to-
connection mapping, room subscriptions, and delegates to components (rate limiter,
room subscription manager, health monitor, etc.). See `docs/CONNECTION_MANAGER_ARCHITECTURE.md`
if present.

## Message Flow

1. **Validation**: [message_validator.py](message_validator.py) enforces size limits,
   JSON depth, and schema (command, chat, ping, etc.). Invalid messages get an error
   response and are not dispatched.
2. **Routing**: [message_handler_factory.py](message_handler_factory.py) looks up the
   handler by `message.type` (command, chat, ping, follow_response, party_invite_response).
3. **Handlers**: [message_handlers.py](message_handlers.py) implements each type; e.g.
   command → `handle_game_command` in websocket_handler (unified command handler),
   chat → `handle_chat_message`, ping → pong. Handlers receive `connection_manager`
   from the pipeline (or resolve via fallback for backward compatibility).

Schemas for client messages are in [server/schemas/realtime/websocket_messages.py](../schemas/realtime/websocket_messages.py).

## NATS and Room Updates

- **NATS → WebSocket**: [nats_message_handler.py](nats_message_handler.py) subscribes to
  NATS subjects, validates and transforms messages, then uses the ConnectionManager to
  broadcast to WebSocket clients (by room or channel). Room and chat events from other
  services are delivered to players via this path.
- **Room broadcasts**: [websocket_room_updates.py](websocket_room_updates.py)
  `broadcast_room_update` sends room state to occupants. The ConnectionManager’s
  `broadcast_to_room` and room subscription manager determine which connections
  receive which events.
- **EventBus**: In-process game events (e.g. player_entered, combat) are handled by
  realtime event handlers that may call `broadcast_to_room` or send personal
  messages; NATS is used for cross-process or multi-instance messaging.

For NATS subject patterns and configuration, see `docs/NATS_SUBJECT_PATTERNS.md` and
env NATS sections in the project root.
