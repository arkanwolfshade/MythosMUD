# Client Server-Authority Register — 2026-09

**Version 1.0.0** · MythosMUD · 2026-09-23

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts. Read `[NOTE]` only if additional context
is needed. `[?]` blocks are unverified — treat with lower confidence.

---

## 1. Purpose

**[NOTE]**

This document closes issue `#752`, filed from `FRD_PLAN_VERIFICATION_REGISTER_2026-08.md` §5.2:
the 2026-08 audit's plan sweep adjudicated `server-authority.mdc` itself as needing no ADR, but
could not certify on a stale jCodemunch index that the client's actual stores/state-management
code doesn't quietly assume client-side authority. This is that dedicated client-side pass.

**Evidence bar** (applies to every row below, per `.cursor/rules/verification-sweeps.mdc`): every
verdict carries a citation. A `CONFORMS` claim cites the implementing `file:line`. A `VIOLATION`
claim cites both the client code that assumed authority and the server evidence proving it wrong
(or absent). `DEAD` claims cite the code and its lack of a production importer. No row in this
register carries a verdict without one of these.

**Principle under test** (`.cursor/rules/server-authority.mdc`, `alwaysApply: true`): the server is
always authoritative over the client; client state must reflect server payloads
(`room_state`, `game_state`, command responses), never assume its own inference.

## 2. Corpus — in and out, with reasons

### 2.1 In corpus

| Area | Reason for inclusion |
|---|---|
| `client/src/components/ui-v2/eventLog/*` | The live projector: derives `GameState` from the server event log. Primary surface for this audit. |
| `client/src/components/ui-v2/hooks/*` | Wires the projector to the container; several hooks wrote directly to `GameState` outside the projector. |
| `client/src/components/ui-v2/GameClientV2*.tsx`, `GameClientV2ContainerView.tsx` | Top-level container and view; owns modal dismissal and map-tab wiring. |
| `client/src/components/map/{AsciiMinimap,AsciiMapViewer}.tsx`, `client/src/components/MapView.tsx` | In-game minimap/map-modal surfaces; found wired to client-side hallucination in violation of ADR-024. |
| `client/src/utils/{lucidityTierRelay,lucidityEventUtils,directionHallucination,mythosTime}.ts` | Lucidity/tier and hallucination utilities directly implicated by the findings. |
| `client/src/types/{lucidity,health}.ts` | `LucidityStatus`/`HealthStatus` shapes; found a hardcoded tier. |
| `client/src/hooks/useConnectionStateMachine.ts` | The only XState machine in the client; checked for game-state authority (found transport-only). |
| `client/src/stores/*`, `client/src/hooks/useStoreSubscriptionTracking.ts` | The four Zustand stores named in the issue; found dead (test-only) with latent authority-violating APIs. |
| `client/src/components/ui-v2/eventHandlers/*` (pre-deletion) | The legacy event-handler registry; found dead (test-only) and containing the same class of violations as the live projector. User approved deleting rather than auditing dead code twice. |

### 2.2 Out of corpus

| Area | Reason |
|---|---|
| `client/src/components/map/{RoomMapViewer,RoomDetailsPanel,AsciiNoise}.tsx`, `pages/mapPageRenderer.tsx` | ADR-024-sanctioned client-side hallucination for the out-of-world `/map` admin/editing surface. Explicitly out of ADR-024's server-authority rule (ADR-024 §3 final paragraph, §5). |
| `client/src/contexts/*`, `PanelManagerContext.tsx`, `PanelSystem/*` | UI-only (theme, panel layout, localStorage). No game-authority surface. |
| Server (`server/`) | Evidence only — cited for what payloads the client is entitled to trust, not itself audited for correctness. |
| Test files (`__tests__/**`) | Not production code; updated to match fixes, not treated as findings. |

## 3. Server facts (evidence for §4)

**[SPEC]**

| # | Fact | Evidence |
|---|---|---|
| S1 | `lucidity_change` payload is `{player_id, current_lcd, max_lcd, delta, tier, liabilities?, reason?, source?}` — never `current_dp`. | `server/services/lucidity_event_dispatcher.py:101-119` |
| S2 | `rescue_update` is sent once on crossing LCD ≤ -10, debounced 120s. | `server/services/lucidity_trigger_handlers.py:61-80` |
| S3 | `game_state` (both builders) carries player `stats.lucidity`/`max_lucidity` but not the authoritative tier; the tier lives in `PlayerLucidity.current_tier`, a separate row. | `server/services/game_state_provider.py:596-604`, `server/realtime/websocket_initial_state.py:167-177`, `server/models/lucidity.py:68` |
| S4 | Personal `player_died` always carries `current_dp`. The NATS publish (no `current_dp`) is never forwarded to a client. | `server/realtime/player_event_handlers_state.py:183-196`, `server/services/combat_messaging/player_broadcasts.py:92-103`, `server/realtime/websocket_initial_state.py:297-310` (reconnect re-send); `server/services/combat_event_publisher.py:484-493` (NATS-only) with `server/realtime/event_handlers.py:205-215` (not subscribed) |
| S5 | `player_respawned` is server-pushed after the respawn API succeeds; `player_delirium_respawned` likewise. | `server/realtime/player_event_handlers_respawn.py:307-325` (respawned), `:539-551` (delirium, pre-fix had no room) |
| S6 | The server never emits `follow_request_cleared` or `party_invite_cleared`; a decline only sends `follow_state`, to the requester only. | `server/realtime/message_handlers.py:109-146` |
| S7 | Room occupant lists sent to a client always include that client's own player. | `server/realtime/player_event_handlers_room.py:418,533,574-612`, `server/realtime/websocket_initial_state.py:158-163` |
| S8 | `mythos_time_update` is broadcast by the time service. | `server/time/time_event_consumer.py:90` |
| S9 | `game_state` now includes `lucidity_tier`/`current_lcd` from `PlayerLucidity` (added by this pass). `_get_lucidity_for_client` looks up `PlayerLucidity` by player id, returning `(None, None)` for a new character with no row yet. | `server/realtime/integration/game_state_provider.py:547-556,608-618` (provider path), `server/realtime/websocket_initial_state.py:142-151,179-188` (initial-connect path) |
| S10 | `player_delirium_respawned` now includes `room`, built via the same `_prepare_room_data_for_respawn` helper `player_respawned` uses, keyed on `event.respawn_room_id` (added by this pass). | `server/realtime/player_event_handlers_respawn.py:536-554` |
| S11 | On reconnect, the server now re-sends `rescue_update(delirium)` when LCD ≤ -10 via `check_and_send_delirium_notification`, calling the same `send_rescue_update_event` dispatcher the live trigger path uses (single-player-targeted, never broadcast) (added by this pass). | `server/realtime/websocket_initial_state.py:338-357` (function), `server/realtime/websocket_handler.py:56-58,80-82` (re-export), `server/realtime/websocket_handler_connection.py:113` (call site, mirrors `check_and_send_death_notification`) |

## 4. Findings

**[SPEC]**

| # | Claim | Client evidence (before fix) | Server evidence | Verdict | Fix |
|---|---|---|---|---|---|
| F1 | `lucidity_change` handler read `event.data.current_dp`, a field the event never carries. | `projectorHandlersState.ts` (pre-fix) `lucidity_change` | S1 | **VIOLATION — FIXED** | Reuses `buildLucidityStatus`; writes `stats.lucidity`/`max_lucidity`, never `current_dp`. |
| F2 | The lucidity tier shown in the UI was hardcoded `'lucid'` (`deriveLucidityStatusFromPlayer`) and the real `lucidityStatus` state was `const [lucidityStatus] = useState(null)` with no setter. | `types/lucidity.ts` (pre-fix), `useGameClientV2ContainerState.ts` (pre-fix) | S3 | **VIOLATION — FIXED** | Tier is now optional (no invented default); `lucidityStatus` lives in `GameState`, set by `game_state` (S9) and `lucidity_change`. |
| F3 | In-game surfaces (minimap panel, map modal) were wired to client-computed `directionHallucination.ts` scrambles, reversed by ADR-024 for exactly this reason. | `GameClientV2MinimapSection.tsx`, `AsciiMinimap.tsx`, `AsciiMapViewer.tsx`, `MapView.tsx`, `GameClientV2ContainerView.tsx` (pre-fix) | ADR-024 §3/§5 | **DRIFT FROM ADR-024 — FIXED** | `hallucinate`/`seed`/`playerId` props removed from all in-game callers; only the `/map`-page `RoomMapViewer`/`RoomDetailsPanel` path (ADR-024-sanctioned) still uses `directionHallucination.ts`. |
| F4 | Death was inferred from `current_dp <= -10` plus hardcoded limbo/foyer room IDs, instead of the server's `player_died` event. | `usePlayerStatusEffects.ts` (deleted) | S4 | **VIOLATION — FIXED** | `player_died` sets `isDead`/`deathLocation` in `GameState` directly; `player_respawned` clears them. Threshold-inference hook deleted. |
| F5 | `player_dp_updated` discarded a DP increase while `current_dp <= -10`, second-guessing the server. | `projectorHandlersState.ts` (pre-fix) | S4 | **VIOLATION — FIXED** | Discard rule removed; the handler applies whatever DP the server sends. |
| F6 | Delirium was inferred client-side from `lucidity <= -10` (defaulting to 100 when absent), instead of the server's `rescue_update`. | `usePlayerStatusEffects.ts` (deleted) | S2 | **VIOLATION — FIXED** | `rescue_update` (now projected) sets `isDelirious`/`deliriumLocation`; `player_delirium_respawned` clears them. |
| F7 | `useRespawnHandlers` fabricated `player_respawned`/`player_delirium_respawned` events (`sequence_number: 0`, client-written message text) after the HTTP respawn call succeeded, duplicating the server's own push. | `useRespawnHandlers.ts` (pre-fix) | S5 | **VIOLATION — FIXED** | Success path resets only local in-flight flags; the server-pushed event is the sole source of the respawn state change. |
| F8 | `clearPendingFollowRequest` wrote a client-made `follow_request_cleared` event into the server event log; the server never sends one. | `useEventProcessing.ts` (pre-fix), `projectorHandlersState.ts` (pre-fix) | S6 | **VIOLATION — FIXED** | Removed. `clearedFollowRequestId`/`clearedPartyInviteId` (local `useState`, not appended to the event log) remain as the UX-only dismissal mechanism; documented as such in `GameClientV2ContainerView.tsx`. |
| F9 | `ensureSelfListedInRoomPlayers` injected the local player into `room.players`/`occupants` on every projected state, second-guessing a server list that already includes self. | `projector.ts` (pre-fix) | S7 | **VIOLATION — FIXED** | Injection removed; the projector trusts the payload. |
| F10 | On a room-ID change, `room_update` zeroed `occupants`/`occupant_count` to 0 instead of using the payload's own (server-authoritative) occupants. | `projectorRoom.ts` `roomAfterIdChange` (pre-fix) | S7 | **VIOLATION — FIXED** | Uses `createInitialRoomState(roomMetadata, payloadRoom)`. |
| F11 | `mythos_time_update` was broadcast by the server but not in the projector's event allowlist; its only handler was in the dead legacy registry. | `projectorConstants.ts` (pre-fix), `eventHandlers/systemHandlers.ts` (deleted) | S8 | **GAP — FIXED** | Added to the allowlist with a handler that sets `mythosTime` and ports the daypart/holiday flavor messages. |
| F12 | Direct `setGameState` writes for local UI messages (clear messages, connection lost, respawn error) were silently reverted by the next event-log replay, which keeps only `commandHistory` across replays. | `useCommandHandlers.ts`, `useGameConnectionManagement.ts`, `useRespawnHandlers.ts` (pre-fix) | — (client-internal bug, not a server-authority issue per se) | **BUG — FIXED** | A `client_`-prefixed local-event mechanism (`buildLocalMessageEvent`/`buildLocalClearMessagesEvent`) routes these through the same event log so they survive replay. |
| F13 | `game_state` carried no lucidity tier, so the client would show none until the first `lucidity_change` of the session. | `game_state_provider.py`/`websocket_initial_state.py` (pre-fix) | S3 | **SERVER GAP — FIXED** | `lucidity_tier`/`current_lcd` added to both `game_state` builders (S9). |
| F14 | `player_delirium_respawned` carried no `room`; the delirium respawn moves the player only in the DB. | `player_event_handlers_respawn.py:539-551` (pre-fix) | S5 | **SERVER GAP — FIXED** | `room` added, reusing the same helper `player_respawned` uses (S10). |
| F15 | A player who reconnects while delirious (LCD ≤ -10) does not see the delirium modal — `rescue_update` is sent only once, on crossing the threshold, never on reconnect. | `websocket_initial_state.py` (pre-fix) | S2 | **SERVER GAP — FIXED** | Reconnect now re-sends `rescue_update(delirium)` when LCD ≤ -10, mirroring the existing death re-send (S11). |
| F16 | The stats-JSON `player.stats.lucidity` and the authoritative `PlayerLucidity.current_lcd`/`current_tier` are two separate stores that can drift (nothing keeps them in sync). | `server/config/models/player_stats.py`, `server/models/lucidity.py` | — | **UNVERIFIABLE — server design question, out of this pass's client-only scope** | Filed: `#891` (§8). |

## 5. Items that conform (citations)

**[SPEC]**

| Claim | Evidence | Verdict |
|---|---|---|
| Clock chime / tick messages are built from the server's `game_tick` payload, not a local clock. | `projectorHandlersMessages.ts` `game_tick` handler | CONFORMS |
| "X has entered/left the game" text uses the server's `player_name`. | `projectorHandlersState.ts` `player_entered_game`/`player_left_game` | CONFORMS |
| `isRoomNameOnly` only suppresses a duplicate display line; it never changes what state is stored. | `projectorHandlersMessages.ts` `command_response` | CONFORMS |
| Regex-based message typing (`determineMessageType`) only picks a display channel/color, not authoritative state. | `utils/messageTypeUtils.ts` via `projectorHandlersMessages.ts` | CONFORMS |
| Movement-message dedupe is a display-only window, not a state change. | `projectorMessageUtils.ts` `appendMovementMessage` | CONFORMS |
| Map-editor optimistic edits (`RoomMapEditor`) re-read the server after saving. | `saveMapChanges.ts`, `MapEditToolbar.tsx` | CONFORMS |
| The XState connection machine (`useConnectionStateMachine.ts`) tracks transport lifecycle only (connect/retry/backoff) — no game state. | `hooks/useConnectionStateMachine.ts` | CONFORMS |
| Health-tier display bucketing (`types/health.ts` `determineDpTier`) is a display-only classification of the server's raw DP; the server sends no health tier of its own to conflict with. | `types/health.ts` | CONFORMS (display-only bucketing is allowed where the server sends only a raw number, not a competing classification) |
| `command_response`'s embedded `room_state`/`player_update` are applied as server payloads, not client inference. | `projectorHandlersMessages.ts` `command_response` | CONFORMS |

## 6. Original remediation plan — todo status

Source: `.cursor/plans/server_authority_remediation_de891aa1.plan.md` (7 todos, all Low risk).

| Todo | Status | Evidence |
|---|---|---|
| `sa-game-state-room` | Done (pre-existing) | `projectorHandlersState.ts` `game_state` uses `room ?? prevState.room` |
| `sa-command-response-player` | Done (pre-existing) | `messageHandlers.ts`/`projectorHandlersMessages.ts` `command_response` applies full `player_update` |
| `sa-projector-command-response-player` | Done (pre-existing) | Same handler as above |
| `sa-status-vs-player-update-doc` | Done (pre-existing) | Comment present at the relevant call site |
| `sa-sanitize-apply-doc` | Superseded | `sanitizeAndApplyUpdates` deleted entirely as dead code (§7) rather than documented |
| `sa-cleared-invite-doc` | **Done by this pass** | `GameClientV2ContainerView.tsx` now documents `clearedFollowRequestId`/`clearedPartyInviteId` as UX-only, not persisted (F8) |
| `sa-doc-refs` | Done (pre-existing) | `projector.ts`/`eventLog` files reference `server-authority.mdc` |

## 7. Dead code removed

| Item | Reason | Disposition |
|---|---|---|
| `client/src/stores/{gameStore,commandStore,sessionStore,connectionStore,stateNormalization}.ts` | Zustand stores with zero production importers (test-only); `gameStore`/`commandStore` contained latent authority-violating APIs (client-side occupant-count recomputation, optimistic command results, client-side alias expansion) that would have reactivated if ever wired up. | Deleted. `Room` type moved to `components/map/types.ts` (the one production consumer of that specific shape). |
| `client/src/hooks/useStoreSubscriptionTracking.ts` | Zustand-only dev-metrics hook, no production caller. | Deleted, along with the now-orphaned `trackStoreSubscription`/`trackStoreUnsubscription` methods on `clientMetricsCollector`. |
| `client/src/components/ui-v2/eventHandlers/{combatHandlers,messageHandlers,systemHandlers,playerHandlers,roomHandlers,index}.ts` | Legacy pre-event-sourcing handler registry (`processGameEvent`), zero production importers; contained the same class of violations (F1-F10) a second time. | Deleted. `types.ts` kept, trimmed to the still-used `GameEvent` interface. Its one live behavior (`rescue_update` → delirium) ported to the live projector (F6). |
| `client/src/components/ui-v2/utils/stateUpdateUtils.ts` `sanitizeAndApplyUpdates`/`mergeRoomUpdate`/`mergeOccupantData`/`applyEventUpdates`/etc. | Dead outside the legacy registry and its own tests once that registry was removed. | Deleted; `GameState`/`ActiveEffectDisplay` types kept (still the live projector's state shape). |
| `client/src/components/ui-v2/hooks/useRefSynchronization.ts` | Synced refs (`currentPlayerRef`, `lucidityStatusRef`, `lastDaypartRef`, etc.) that fed only the deleted legacy registry's `EventHandlerContext`. | Deleted, along with the now-unused refs in `useGameClientV2ContainerRefsAndBootstrap.ts`. |
| `zustand` dependency | Only import was the deleted stores. | Removed from `client/package.json`; `package-lock.json` updated via `npm uninstall`. |
| Two in-game hallucination test files (`AsciiMapViewer.hallucination.test.tsx`, `AsciiMinimap.hallucination.test.tsx`) | Tested the now-removed in-game hallucination wiring (F3). | Deleted. `directionHallucination.test.ts` (the `/map`-scoped util) kept. |

`npx knip` confirms no orphaned exports/files remain after these deletions.

## 8. Gaps and follow-ups

- **ADR-024 wording nit** (not a code violation): ADR-024 §3 names only `AsciiNoise` as the
  surviving `directionHallucination.ts` caller, but `RoomDetailsPanel.tsx`'s exit-hallucination
  (`getHallucinatedExits`) is also reached only through the `/map` page. Both are genuinely
  out-of-world/admin-only in the current routing; this register treats `RoomDetailsPanel` as
  equally in-scope for the ADR-024 exception, and flags the ADR's wording as worth a follow-up
  correction.
- **Server-side dual lucidity stores** (F16): `player.stats.lucidity` (JSON blob) and
  `PlayerLucidity.current_lcd`/`current_tier` (dedicated table) are two sources of truth with
  no synchronization guarantee found in this pass. Filed as `#891` — out of this client-only
  pass's scope to fix.

## 9. Related documentation

- `.cursor/rules/server-authority.mdc` / `.claude/rules/server-management.md` — the principle under test.
- `.cursor/rules/verification-sweeps.mdc` — the citation convention this register follows.
- `docs/architecture/decisions/ADR-024-server-authoritative-perceived-reality.md` — the hallucination-placement precedent (F3, §8).
- `docs/architecture/FRD_PLAN_VERIFICATION_REGISTER_2026-08.md` §5.2 — filed issue `#752`, closed by this document.
- `docs/architecture/AUDIT_COVERAGE_BOUNDARY_2026-08.md` §4.7 — the `server_authority_remediation` row this closes.
- `.cursor/plans/server_authority_remediation_de891aa1.plan.md` — original remediation plan (§6).
- `client/src/components/ui-v2/eventLog/EVENTS_SCHEMA.md`, `HANDOFFS.md` — updated event catalog and respawn handoff description.

## 10. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-09-23 | Initial version. Closes `#752`: client server-authority pass, 10 client-side violations fixed, 3 server-side gaps closed, legacy dead code removed. |
