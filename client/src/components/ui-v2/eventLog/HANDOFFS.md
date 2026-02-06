# Critical State Handoffs (Request/Response vs Push-Only)

**Authority:** The server is always authoritative over the client. If there is a disparity, the server is
assumed to be correct; client state must be updated from server payloads (room_state, game_state, command
responses).

As documented in the Client Updates System Audit plan (Option C3). This file records which
critical handoffs use request/response (to avoid ordering bugs) and which remain push-only.

## Enter-room (Movement)

- **Mechanism:** Request/response.
- **Server:** When a movement command succeeds, the server includes `room_state` in the
  `command_response` payload (`result.room_changed` and `result.room_id` trigger attachment
  of `result.room_state`). The client receives one response with both command result and
  authoritative room snapshot.
- **Client:** The projector applies `event.data.room_state` from `command_response` events,
  so room state is set from the response and does not rely on ordering of push events
  (e.g. `room_state`, `room_occupants`, `room_update`).
- **Rationale:** Enter-room had an observed bug where the entering player sometimes saw
  empty occupants due to push event ordering; request/response eliminates that.

## Login / Initial game_state

- **Mechanism:** Push-only (on connect).
- **Server:** On WebSocket connect, the server sends `game_state` (player + room) and then
  initial room state (e.g. `room_update`, `room_occupants` or `room_state`). Order is
  deterministic within a single connection setup.
- **Client:** The event-sourced projector derives state from the event log; the first
  `game_state` event sets player and room; any subsequent room events update the room.
- **Rationale:** No separate client “request” for login state; connection establishment
  triggers a defined sequence. No ordering bug reported; leave as push-only.

## Resawn

- **Mechanism:** Push-only (for now).
- **Server:** Respawn flow sends game/room updates (e.g. `game_state`, room updates) via
  existing push paths.
- **Client:** State is derived from the event log; respawn-related events update player and
  room as they arrive.
- **Rationale:** If ordering issues appear (e.g. room empty after respawn), consider adding
  a `room_state` payload to the respawn response (similar to enter-room). Until then,
  leave as push-only.

## Summary

| Handoff          | Mechanism        | Notes                                    |
| ---------------- | ---------------- | ---------------------------------------- |
| Enter-room       | Request/response | `command_response` includes `room_state` |
| Login/game_state | Push-only        | Deterministic on connect                 |
| Respawn          | Push-only        | May add request/response if needed later |
