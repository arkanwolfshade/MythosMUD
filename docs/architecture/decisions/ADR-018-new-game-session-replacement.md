# ADR-018: New Game Session vs Grace Reconnect

**Version 1.1.0** · MythosMUD · 2026-08-27

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-08-14

This addendum to [ADR-004](ADR-004-websocket-only-realtime.md) defines how session
replacement works. One WebSocket per _session_, not a rewrite of
`player_websockets` on every register.

## 2. Context

**[NOTE]**
`ConnectionManager.player_websockets` is `dict[UUID, list[str]]`. Occupant, who,
chat, and personal events fan out over that list. Register **appends**. Dead
sockets leave via `cleanup_dead_websocket`, `force_disconnect`, or
`new_game_session`.

**[BUG]**
**Symptom:** Rewriting `player_websockets[player_id] = [new_id]` on register (2026-08 E2E)
starved occupancy: the looking tab was dropped from the send list while a
harness-recovered socket stayed registered. That shortcut is forbidden.
**Fix:** keep the two reconnect kinds distinct, per the table below — append on grace
reconnect, close-then-append on new game session.

Two reconnect kinds must stay distinct:

| Kind             | When                                        | Behavior                                                                                                        |
| ---------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Grace reconnect  | Same `session_id`; drop; 30s grace          | Keep `online_players`; **append** new WS; cancel grace + rest; prune dead. Do not close a healthy prior socket. |
| New game session | Login replace, new tab, `session_id` change | Close **all** prior sockets with `disconnect_reason=new_game_session`, then append-register the new one.        |

Related: [dual-connection spec](../../archive/DUAL_CONNECTION_SYSTEM_SPEC.md)
(archival, still binds grace), [mid-run drops](../../debugging-mid-run-drops.md),
[memory leak metrics](../../MEMORY_LEAK_METRICS_USAGE_GUIDE.md)
(`active_to_player_ratio` > 2 is a leak to **clean**, not hide by shrinking the
send list).

## 3. Decision

**[SPEC]**
**Single replacement entry:** WebSocket establish. If `session_id` is present
and differs from `manager.player_sessions.get(player_id)`, call existing
`handle_new_game_session_impl` **before** `websocket.accept()` and
`_register_new_connection`. Register still **appends**.

- Same `session_id`, or missing `session_id` (grace recover): append only.
- First connect (`player_sessions` has no entry): append only; do not run full
  session replacement (avoids room-unsubscribe then re-subscribe).
- `POST /connections/{player_id}/session` remains. It must be **idempotent**:
  if `player_sessions[player_id] == new_session_id`, do not disconnect the live
  socket (HTTP after WS must not kill the new tab).
- Reuse `_disconnect_all_connections_for_session`. Do not add a second
  disconnect path. Do not persist a new session table unless the owner
  confirms a database change.
- Client already sends `session_id` on the WS URL. POST `/session` is optional
  for an explicit replace; do not POST on every recover.
- E2E `ensurePlayableConnection`: a second WS with the **same** `session_id` is
  grace/append. A new `session_id` is replacement. Recover must not open a
  second socket and then treat it as the only send target.

## 4. Alternatives Considered

**[SPEC]**

1. **Rewrite `player_websockets` on register** - Rejected: occupancy starvation
   (issue #610).
2. **HTTP POST only before every WS** - Rejected: client/E2E often open WS
   without POST; replacement would never run.
3. **Always call `new_game_session` on establish** - Rejected: would kill a
   healthy grace socket (dual-connection / mid-run-drop rules).
4. **Register then disconnect all-but-current** - Rejected: occupant events can
   hit a closing zombie; disconnect-then-register is the ordered path.

## 5. Consequences

**[SPEC]**

- **Positive**: New tab gets who/occupant/chat; old tab is closed with
  `new_game_session`. Grace recover still appends. Memory ratio stays honest.
- **Negative**: Two live sockets can exist briefly during same-session recover
  until dead cleanup; send path must skip CONNECTING/DISCONNECTED (already
  landed).
- **Neutral**: Server remains authoritative. No new persistence.

## 6. Related ADRs

**[SPEC]**

- ADR-004: WebSocket-Only Real-Time Architecture

## 7. References

**[SPEC]**

- GitHub issue [#610](https://github.com/arkanwolfshade/MythosMUD/issues/610)
- [ADR-004](ADR-004-websocket-only-realtime.md)
- [DUAL_CONNECTION_SYSTEM_SPEC](../../archive/DUAL_CONNECTION_SYSTEM_SPEC.md)
- [debugging-mid-run-drops](../../debugging-mid-run-drops.md)

## 8. Changelog

**[SPEC]**

| Version | Date       | Change                                                      |
| ------- | ---------- | ----------------------------------------------------------- |
| 1.0.0   | 2026-08-14 | Initial decision for session replacement vs grace reconnect |
| 1.1.0   | 2026-08-27 | Restructure the `[BUG]` block into HADS-required Symptom/Fix fields (audit deferred register, #648). |
