# Server Realtime Module

This directory contains WebSocket connection handling, message routing, and
real-time broadcast logic for MythosMUD. It works with the FastAPI real-time
router and NATS for server-to-server and room events.

## Entry Points

- **API routes**: [server/api/real_time.py](../api/real_time.py) defines the WebSocket
  endpoints:
  - `GET /api/ws` — the only endpoint (JWT via query or subprotocol; `character_id` required, and
    it must belong to the token's account; `session_id` optional)
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
   JSON depth, string-length limits, CSRF, and a required-top-level-field check
   (`type` or `message`). It then validates the unwrapped, CSRF-stripped message against
   `WebSocketInboundMessage` — a `type`-discriminated union of Pydantic schemas in
   [server/schemas/realtime/websocket_messages.py](../schemas/realtime/websocket_messages.py),
   each inheriting `SecureBaseModel` (`extra="forbid"`), the same pattern `#755` used for HTTP
   request bodies. `parse_and_validate` returns the validated, typed message rather than a raw
   dict. An unrecognized `type` or an unmodelled field is rejected before it reaches routing.
   `server/tests/unit/realtime/test_websocket_message_schema_registry.py` is a drift guard
   asserting the schema union's discriminator values exactly match the handler factory's
   registered types (`#765`; supersedes the dead `schema` parameter removed in `#754`).
2. **Routing**: [message_handler_factory.py](message_handler_factory.py) looks up the
   handler by `message.type` (command, chat, ping, follow_response, party_invite_response,
   client_error_report) and dispatches the typed message — no `dict[str, Any]` on this path.
3. **Handlers**: [message_handlers.py](message_handlers.py) implements each type; e.g.
   command → `handle_game_command` in websocket_handler (unified command handler),
   chat → `handle_chat_message`, ping → pong. Handlers receive the validated envelope model
   and `connection_manager` from the pipeline (or resolve via fallback for backward
   compatibility).

## Message Categories

Every outgoing event that carries player-visible text puts a semantic category in its payload as
`data.category` (`domain.kind`, e.g. `chat.say`, `combat.hurt`, `room.movement`). The client styles and routes
the line from it; it does not infer meaning from the text.

- **Source of truth**: [server/constants/message_category.py](../constants/message_category.py) (`MessageCategory`).
  Reserved, not yet populated: `lore.*`, `item.*`, `npc.*`, `command.misfire`. The client mirror and the full
  payload reference are in `client/src/components/ui-v2/eventLog/EVENTS_SCHEMA.md`.
- **Assigned only in shared builders**, never per call site: the command chokepoint
  (`websocket_handler_commands.py`, default `command.output`), `build_event` (defaults a `command_response` that
  names none to `command.output`), `NATSMessageHandler._build_chat_event` (channel to `chat.*`), `MessageBuilder`,
  `posture_notify.attach_posture_self_message`, and the combat and lucidity dispatchers. Command handlers normally
  put no `category` in their result dicts; the exception is failure: a handler (or pipeline step) that rejects a
  command for a usage, permission, or system reason returns `command_error(msg)`
  (`server/commands/command_results.py`), which sets `system.error`. In-world refusals ("You don't see that here")
  stay plain and render as `command.output`.
- **`combat_attack`** is the one event with several perspectives: it carries `data.categories`, keyed like
  `data.messages`, instead of a single `data.category`.
- **Hallucination code never chooses a category** (ADR-024). A hallucinated message reaches the player through the
  same builder as the real one, so the two are indistinguishable on the wire.
  `server/tests/unit/services/test_hallucination_category_ban.py` enforces the import ban.
- **Adding an emitter**: tag it in a shared builder and add it to `INVENTORY` in
  `server/tests/unit/realtime/test_message_category_invariants.py`.

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
