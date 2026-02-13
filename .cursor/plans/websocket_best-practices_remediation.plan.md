---
name: ""
overview: ""
todos: []
isProject: false
---

# WebSocket Best-Practices Remediation Plan

**Source**: Analysis against `.cursor/rules/websocket.mdc`
**Scope**: Server and client WebSocket code (real-time API, connection handling, messaging)
**Status**: Draft

---

## Executive Summary

The codebase already follows several WebSocket best practices: dependency injection for
ConnectionManager, Factory pattern for message routing, server-side validation (size, depth,
schema), rate limiting, heartbeats, and structured error handling. This plan addresses
semantic bugs, anti-patterns, security and logging issues, and documentation gaps
identified against the rule.

---

## Findings Summary

| Category            | Severity | Count | Notes                                     |
| ------------------- | -------- | ----- | ----------------------------------------- |
| Semantic / bugs     | High     | 1     | Deprecated route validation inconsistency |
| Anti-patterns       | Medium   | 3     | Debug logging, coupling, token in URL     |
| Security / logging  | Medium   | 2     | Sensitive data in logs, WSS documentation |
| Code organization   | Low      | 1     | Realtime layout documentation             |
| Dead / brittle code | Low      | 1     | get_help_content stub                     |

---

## 1. Semantic Error: Deprecated Route Validation

**Rule**: Server authority; consistent validation across endpoints.

**Finding**: The deprecated WebSocket endpoint `/api/ws/{player_id}` uses
`_validate_websocket_connection_manager`, which checks `connection_manager.persistence`.
The primary endpoint and the rest of the codebase use `async_persistence`. The
ConnectionManager no longer exposes `persistence` (replaced by `async_persistence`), so
the deprecated route can incorrectly reject valid connections (or behave inconsistently
with the main route).

**Location**: `server/api/real_time.py` — `_validate_websocket_connection_manager` (around
line 410).

**Fix**: In `_validate_websocket_connection_manager`, check `getattr(connection_manager, "async_persistence", None) is not None` instead of `getattr(connection_manager, "persistence", None) is None`, aligning with `_validate_and_accept_websocket`.

---

## 2. Anti-Pattern: Debug Logging in Production Path

**Rule**: Log errors for debugging; avoid noisy or sensitive logs in production.

**Finding**: Server-side WebSocket message handling logs at INFO level with "SERVER DEBUG"
and emoji (e.g. "🚨 SERVER DEBUG: message_handler_factory.handle_message called"), and
includes `full_message` in the log payload. This is noisy in production and may log
user-generated or sensitive content.

**Locations**:

- `server/realtime/message_handler_factory.py`: `handle_message` — two `logger.info`
  calls with "🚨 SERVER DEBUG" and `extra={"full_message": message}`.
- `server/realtime/message_handlers.py`: `handle_command_message` — `logger.info` with
  "🚨 SERVER DEBUG" and `data=data`.

**Fix**: Remove or gate these logs: either delete them or convert to `logger.debug` and
remove the `full_message` / full `data` from structured fields (log only message_type and
non-sensitive identifiers). Ensure no PII or full message bodies are logged at INFO in
production.

---

## 3. Anti-Pattern: Tight Coupling to `app` for Connection Manager

**Rule**: Avoid tight coupling; use dependency injection.

**Finding**: In `server/realtime/websocket_handler.py`, `handle_game_command`,
`process_websocket_command`, and `handle_chat_message` accept an optional
`connection_manager`. When it is `None`, they resolve it via `from ..main import app`
and `app.state.container.connection_manager`. This couples the handler to the global app
and makes testing and reuse harder.

**Fix**: Prefer always passing `connection_manager` from the endpoint (which already
receives it from app state). If backward compatibility is required, resolve it in a
single helper (e.g. `_resolve_connection_manager(connection_manager)` that returns the
argument if not None, otherwise resolves from a passed app/state), and avoid importing
`app` in multiple handlers. Document that callers must pass `connection_manager` when
invoking these functions from the WebSocket pipeline.

---

## 4. Security / UX: Token in WebSocket URL

**Rule**: Use HTTPS; protect authentication credentials in transit; avoid leaking tokens.

**Finding**: The client sends the JWT in the WebSocket URL query string
(`token=${encodeURIComponent(authToken)}`). Over HTTPS the URL is encrypted in transit,
but query parameters can appear in server access logs, referrer headers, and browser
history. The codebase already notes that JWT in subprotocol was avoided due to invalid
characters in the token.

**Fix**: (1) Document in client and/or server that tokens in query are a known
trade-off; recommend short-lived access tokens and ensure server logs do not log query
strings for the WebSocket path. (2) Optionally, implement a one-time connection token
(short-lived) exchanged via a secure REST call, and use that in the WebSocket URL
instead of the JWT, and document it in the plan or ADR.

---

## 5. Security / Documentation: WSS in Production

**Rule**: Use HTTPS for all API communication; validate SSL/TLS certificates.

**Finding**: The client builds the WebSocket URL from `API_V1_BASE` (same-origin in
production). When the app is served over HTTPS, the browser will use WSS. There is no
explicit documentation that production must be served over HTTPS so that WebSocket
connections use WSS.

**Fix**: Add a short note in `docs/` or in the WebSocket/realtime section of the main
docs stating that production deployments must serve the application over HTTPS so that
WebSocket connections use WSS and credentials remain protected. Optionally add a
comment in `client/src/hooks/useWebSocketConnection.ts` near the URL construction.

---

## 6. Code Organization: Realtime Layout Documentation

**Rule**: Well-organized codebase; clear structure for WebSocket/real-time code.

**Finding**: The server uses `server/realtime/` for WebSocket handling, connection
management, message routing, and NATS integration. There is no README or layout
document describing how these modules relate (e.g. `websocket_handler`, `connection_manager`,
`message_handler_factory`, `message_handlers`, `message_validator`, NATS handler).

**Fix**: Add `server/realtime/README.md` (or a section in existing architecture docs)
describing: entry points (e.g. `api/real_time.py`), connection lifecycle
(`websocket_handler`, `connection_manager`), message flow (validator → factory →
handlers), and where NATS and room updates integrate. Keep it concise (e.g. one page).

---

## 7. Dead / Brittle Code: get_help_content Stub

**Rule**: Keep handlers focused; avoid dead or misleading code.

**Finding**: In `server/realtime/websocket_handler.py`, `get_help_content(command_name)`
returns a generic string for any command ("Command not found or help not available")
and a short hardcoded list for the general case. It is unclear if this is used or
intended to be expanded; if unused, it is dead code; if used, it is brittle.

**Fix**: (1) Grep for callers of `get_help_content`. (2) If unused, remove it (and any
references). (3) If used, either document it as a stub and add a TODO, or implement
proper help resolution from a single source of truth (e.g. command registry) and avoid
hardcoding command lists in the WebSocket layer.

---

## 8. Optional: Remove or Formalize Deprecated WebSocket Route

**Rule**: Prefer one canonical endpoint; avoid duplicate behavior.

**Finding**: The route `GET /api/ws/{player_id}` is deprecated in favor of `GET /api/ws`
with JWT (and query params). It is still present for backward compatibility and uses
different validation until the bug in §1 is fixed.

**Fix**: (1) Apply the fix in §1 so validation matches the main route. (2) Either:
(a) Document the deprecation and a removal timeline in the API docs and in code, or
(b) Remove the route and update any remaining clients/tests. Prefer (a) unless
stakeholders confirm no usage.

---

## Detailed Todos

- **WS-1** Fix deprecated route validation: In `server/api/real_time.py`, in
  `_validate_websocket_connection_manager`, replace the check for `persistence` with
  `async_persistence` so it matches `_validate_and_accept_websocket`. Run real_time and
  websocket tests; verify deprecated route accepts/rejects consistently with main route.
- **WS-2** Remove or gate WebSocket debug logging: In `message_handler_factory.py`,
  remove or change to `logger.debug` the two "🚨 SERVER DEBUG" logs and remove
  `full_message` from log payloads. In `message_handlers.py`, remove or change to
  `logger.debug` the "🚨 SERVER DEBUG" log and avoid logging full `data`. Ensure no
  PII/full message bodies at INFO.
- **WS-3** Reduce coupling to `app` in websocket_handler: Ensure
  `handle_game_command`, `process_websocket_command`, and `handle_chat_message` are
  always called with `connection_manager` from the WebSocket pipeline; add a single
  internal helper for the fallback (if kept) and document that callers should pass
  `connection_manager`. Prefer removing the fallback if no callers need it.
- **WS-4** Document token-in-URL trade-off: Add a short note (client or server docs)
  that the WebSocket token is passed in the query string due to subprotocol
  limitations; recommend short-lived tokens and ensure WebSocket URL or query is not
  logged. Optionally add a one-time connection-token flow and document it.
- **WS-5** Document WSS in production: Add a note in docs (and optionally in
  `useWebSocketConnection.ts`) that production must be served over HTTPS so WebSocket
  uses WSS.
- **WS-6** Add realtime layout doc: Create `server/realtime/README.md` (or
  equivalent section) describing entry points, connection lifecycle, message flow, and
  NATS/room integration.
- **WS-7** Resolve get_help_content: Find callers of `get_help_content`; remove if
  unused, or document as stub/TODO and improve (e.g. single source of truth for help)
  if used.
- **WS-8** Deprecated route: After WS-1, document deprecation and removal timeline
  for `/api/ws/{player_id}` or remove the route and update clients/tests if agreed.

---

## Success Criteria

- Deprecated WebSocket route uses the same persistence check as the main route
  (`async_persistence`).
- No "SERVER DEBUG" or full message payloads at INFO in WebSocket message path.
- Connection manager is injected from the WebSocket pipeline; no (or minimal) direct
  imports of `app` in handlers.
- Docs mention token-in-URL trade-off and WSS requirement for production.
- Realtime module layout is documented.
- get_help_content is either removed or documented and improved.
- All existing WebSocket and real_time tests pass; no regressions in connection or
  message handling.

---

## References

- `.cursor/rules/websocket.mdc` — WebSocket best practices
- `server/api/real_time.py` — WebSocket endpoints
- `server/realtime/websocket_handler.py` — Connection and message handling
- `server/realtime/message_handler_factory.py` — Message routing
- `client/src/hooks/useWebSocketConnection.ts` — Client WebSocket lifecycle
- `docs/WEBSOCKET_CODE_REVIEW.md` — Prior review (outdated; ConnectionManager
  refactored)
