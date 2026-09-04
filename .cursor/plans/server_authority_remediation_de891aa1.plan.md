---
name: Server Authority Remediation
overview: Remediate client code that treats local or merged state as authoritative instead of preferring server payloads (room_state, game_state, command_response) per .cursor/rules/server-authority.mdc.
todos: []
isProject: false
---

# Server Authority Remediation Plan

**Rule:** [.cursor/rules/server-authority.mdc](.cursor/rules/server-authority.mdc) — The server is always authoritative. Client state must be updated from server data; prefer server payloads over client-inferred or cached state.

**Scope:** Client event processing (projector, message handlers, state utils). Server already documents room_state as authoritative and sends game_state with full player + room.

---

## 1. game_state room: replace instead of merge (State sync)

**Finding:** In [client/src/components/ui-v2/eventLog/projector.ts](client/src/components/ui-v2/eventLog/projector.ts) (L145–148), for `game_state` the client does:

- `room: room ? mergeRoomState(room, prevState.room) : prevState.room`

The server sends a full snapshot (player + room) in `game_state` ([HANDOFFS.md](client/src/components/ui-v2/eventLog/HANDOFFS.md), [game_state_provider.py](server/realtime/integration/game_state_provider.py)). Merging with `prevState.room` can preserve stale client room data (e.g. old occupants). `room_state` is already handled as authoritative (replace) in the same file (L176–182).

**Action:** In `projector.ts` case `'game_state'`, when `room` is derived, set room authoritatively: use `room` directly when present (replace), not `mergeRoomState(room, prevState.room)`. Use `room: room ?? prevState.room` so we only replace when the server sent a room.

**Todo (sa-game-state-room):**

- In `projector.ts`, in the `case 'game_state':` block, change the line that sets `room` from `room: room ? mergeRoomState(room, prevState.room) : prevState.room` to `room: room ?? prevState.room`.
- Add a one-line comment: `// Server-authoritative: game_state sends full snapshot; replace room when present.`
- Run existing projector tests; add or adjust a test that game_state with room replaces (not merges) previous room when same room_id.

---

## 2. command_response player_update: prefer full server payload (Conflict resolution)

**Finding:** In [client/src/components/ui-v2/eventHandlers/messageHandlers.ts](client/src/components/ui-v2/eventHandlers/messageHandlers.ts) (L63–76), when processing `player_update` from a command response the client builds:

- `updates.player = { ...context.currentPlayerRef.current, stats: { ...context.currentPlayerRef.current.stats, ...(playerUpdate.position && { position: playerUpdate.position }) } }`

So the client uses **client-held** state as the base and only overlays `position` from the server. Any other fields sent by the server in `player_update` (e.g. `in_combat`, other stats) are ignored. The rule says to prefer server payloads over client state.

**Action:** Treat server `player_update` as the source for the fields it contains: merge all top-level and nested fields from `event.data.player_update` onto the current player, with server values winning. Keep client state only for fields the server did not send. Implementation: build `updates.player` by shallow-merge of `context.currentPlayerRef.current` with `event.data.player_update`, and deep-merge `stats` (server stats overwrite client stats for keys present).

**Todo (sa-command-response-player):**

- In `messageHandlers.ts` `handleCommandResponse`, replace the block that sets `updates.player` from `event.data.player_update` (L63–76) with logic that: (1) starts from `context.currentPlayerRef.current` if present; (2) applies all keys from `event.data.player_update` (e.g. position, in_combat, or any future fields) with server winning; (3) for nested `stats`, merges so server-provided stat keys overwrite client stats.
- Ensure type safety for known fields (position, previous_position, etc.) while allowing additional server keys.
- Update [client/src/components/ui-v2/eventHandlers/**tests**/handleCommandResponse.test.ts](client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts) so tests expect server-supplied fields (e.g. a new stat) to appear in `updates.player` and not be dropped.

---

## 3. Projector command_response player_update: apply full server payload (Conflict resolution)

**Finding:** In [client/src/components/ui-v2/eventLog/projector.ts](client/src/components/ui-v2/eventLog/projector.ts) (L344–354), for `command_response` the client applies only `player_update.position` to `nextState.player.stats`. Other fields in `event.data.player_update` are ignored.

**Action:** Apply the full `player_update` payload from the server: merge all provided fields into `nextState.player` (and `nextState.player.stats` for stats), with server values winning. Mirror the same “server overwrites for keys present” behavior as in messageHandlers.

**Todo (sa-projector-command-response-player):**

- In `projector.ts` case `'command_response'`, replace the block that applies `playerUpdatePayload?.position` (L344–354) with logic that applies every key from `event.data.player_update` to the player (and stats sub-object), not only `position`.
- Add a short comment: `// Server-authoritative: apply full player_update from command response.`
- Run projector tests; add or update a test that command_response with player_update containing multiple fields (e.g. position + in_combat or another stat) results in all those fields on the projected player.

---

## 4. Parsed status vs server player_update precedence (Conflict resolution)

**Finding:** In `handleCommandResponse`, when the message looks like a status response the client parses it and sets `updates.player` from `parseStatusResponse` (L49–59). Later, if `event.data.player_update` exists, the code overwrites `updates.player` with the merge based on currentPlayerRef + player_update (L63–76). So when both exist, the final `updates.player` comes from the player_update path. After fixing (2), that path will be server-authoritative for fields in player_update. If the same command_response carries both parsed status text and a structured player_update, we should prefer the structured server payload for the fields it contains. Parsed status can still fill in player when server does not send player_update.

**Action:** No code change required beyond (2). After (2), server player_update will already take precedence for its fields. Document in a one-line comment in `handleCommandResponse`: when both parsed status and player_update exist, structured player_update (server) wins for overlapping fields.

**Todo (sa-status-vs-player-update-doc):**

- In `messageHandlers.ts`, add a single-line comment above or beside the player_update block: e.g. "When both parsed status and player_update exist, server player_update wins for the fields it provides."

---

## 5. sanitizeAndApplyUpdates and authoritative room (State sync)

**Finding:** [client/src/components/ui-v2/utils/stateUpdateUtils.ts](client/src/components/ui-v2/utils/stateUpdateUtils.ts) (L160) always merges: `finalRoom = updates.room ? mergeRoomState(updates.room, prev.room) : prev.room`. This path is currently only used in tests. If a future caller passes an authoritative room (e.g. from room_state), merging would violate server authority.

**Action:** Document the contract: callers passing room from an authoritative server event (e.g. room_state) should pass a flag or use a different helper so room replaces rather than merges. Optionally add a parameter (e.g. `replaceRoom?: boolean`) to `sanitizeAndApplyUpdates` and when true set `finalRoom = updates.room ?? prev.room` instead of merging. Lower priority if no production code path uses this for server payloads.

**Todo (sa-sanitize-apply-doc):**

- In `stateUpdateUtils.ts`, add a JSDoc or inline note on `sanitizeAndApplyUpdates`: when `updates.room` comes from an authoritative server event (e.g. room_state), room should replace; current implementation always merges, so do not use this function for authoritative room updates from server, or extend the API to support replace (e.g. replaceRoom flag).

---

## 6. Cleared follow/party invite state (Documentation and alignment)

**Finding:** [GameClientV2Container.tsx](client/src/components/ui-v2/GameClientV2Container.tsx) keeps `clearedFollowRequestId` and `clearedPartyInviteId` so the client hides dialogs after the user dismisses them. If the event log re-applies the same invite/request (e.g. on replay), the client may keep hiding it. The rule says client state must align with server; server should send clear events (e.g. follow_request_cleared, party_invite_cleared) when the user accepts/declines.

**Action:** Do not change behavior yet. Add a short note in the plan or in code: (1) Ensure server sends explicit clear events when the user accepts/declines so client can clear pending state from server; (2) on reconnect, do not persist client-only cleared IDs so that server state (e.g. pending invite) wins after reconnect. If desired, add a follow-up task to verify server sends clear events and that client clears `pendingFollowRequest` / `pendingPartyInvite` from those events.

**Todo (sa-cleared-invite-doc):**

- In `GameClientV2Container.tsx` or in a short comment near `clearedFollowRequestId` / `clearedPartyInviteId`, add a one-line note: "Server-authority: rely on server follow_request_cleared / party_invite_cleared events where possible; cleared IDs are UX-only so we don't re-show after user dismiss; do not persist across reconnect."
- Optionally add a follow-up verification task (non-blocking): confirm server sends clear events and client updates pending state from them.

---

## 7. Documentation references (Maintainability)

**Action:** Add a brief reference to server-authority in key client files so future edits preserve the rule.

**Todo (sa-doc-refs):**

- In [client/src/components/ui-v2/eventLog/projector.ts](client/src/components/ui-v2/eventLog/projector.ts), add at top of file (or near getInitialGameState) a one-line comment: "Server is authoritative; prefer server payloads (game_state, room_state, command_response) over client state. See .cursor/rules/server-authority.mdc."
- In [client/src/components/ui-v2/eventHandlers/messageHandlers.ts](client/src/components/ui-v2/eventHandlers/messageHandlers.ts), add a one-line comment near the top: "Command response state must prefer server payloads (player_update, room_state) over client-held state. See server-authority.mdc."

---

## Implementation order

| Priority | Todo                                 | Risk |
| -------- | ------------------------------------ | ---- |
| 1        | sa-game-state-room                   | Low  |
| 2        | sa-command-response-player           | Low  |
| 3        | sa-projector-command-response-player | Low  |
| 4        | sa-status-vs-player-update-doc       | Low  |
| 5        | sa-sanitize-apply-doc                | Low  |
| 6        | sa-cleared-invite-doc                | Low  |
| 7        | sa-doc-refs                          | Low  |

---

## Verification

- Run client unit tests: projector tests, messageHandlers tests, stateUpdateUtils tests (`make test-client-coverage` or equivalent from project root).
- Run `npx tsc --noEmit` in client.
- Manually or via E2E: connect, run status and a movement command; confirm room and player state (including position/stats) match server (e.g. room occupants, player position after /sit).
- After changes, run Codacy CLI on modified files per [.cursor/rules/codacy.mdc](.cursor/rules/codacy.mdc).
