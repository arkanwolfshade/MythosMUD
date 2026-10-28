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

## Respawn

- **Mechanism:** Push-only, dedicated event (`player_respawned` / `player_delirium_respawned`).
- **Server:** After `POST /api/players/respawn` (or `/respawn-delirium`) succeeds, the server
  pushes `player_respawned` / `player_delirium_respawned` over the websocket, carrying `player`,
  `room` and `message` directly -- no separate `game_state`/room-update round trip needed.
- **Client:** `useRespawnHandlers` only resets its local in-flight flag on HTTP success; it does
  not fabricate the respawn event itself (see #752's client server-authority register). The
  projector's `player_respawned` handler clears `isDead`/`deathLocation`/`isDelirious`/
  `deliriumLocation` and applies the server's `player`/`room`.
- **Rationale:** A client-fabricated event with `sequence_number: 0` and client-written message
  text was a server-authority violation and produced a duplicate message alongside the real
  server push. Trusting the server push alone fixes both.

## Container open/transfer/close/loot-all (#711)

- **Mechanism:** HTTP request + push confirmation (not request/response -- the HTTP response
  body is not used for state).
- **Server:** `POST /api/containers/{open,transfer,close,loot-all}` report success/failure only
  (`ContainerOpenResponse`, etc.). The actual state -- the full container snapshot, or the
  session closing -- arrives separately over the websocket as `container.opened` /
  `container.updated` / `container.closed`, sent personally to the actor.
- **Client:** `api/containers.ts` calls do nothing on success and only report the error on
  failure (e.g. the 409 from `ContainerOpenByAnotherPlayerError`, surfaced verbatim). The
  projector (`projectorHandlersContainers.ts`) applies the resulting event to `openContainers`;
  the UI (`ContainerTransferModal`) is driven entirely by that state, not by the HTTP response.
- **Rationale:** The HTTP response and the websocket event can race (the event may arrive before
  the fetch promise resolves); trusting only the event avoids a client-side "double open" or a
  stale response body overwriting a newer push.

## Summary

| Handoff                       | Mechanism           | Notes                                                                                 |
| ----------------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Enter-room                    | Request/response    | `command_response` includes `room_state`                                              |
| Login/game_state              | Push-only           | Deterministic on connect                                                              |
| Respawn                       | Push-only           | Dedicated `player_respawned`/`player_delirium_respawned` event; no client fabrication |
| Container open/transfer/close | HTTP request + push | HTTP reports success/failure only; state comes from `container.*` events              |
