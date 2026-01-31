# Debugging Mid-Run Drops (linkdead / has left the game)

E2E or multiplayer runs sometimes show one player (often Ithaqua) as "linkdead", "has left the game",
or disconnected mid-test. **These are bugs to debug**, not flakiness to mask with retries or timeouts.

## Disconnect causes and what to grep for

| `disconnect_reason`      | Meaning                                                                                                                                         | Where                                      |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `connection_timeout`     | Connection age > `max_connection_age`. Default 5 min; **30 min** when `LOGGING_ENVIRONMENT` is `local` or `e2e_test`.                           | `connection_cleaner.cleanup_orphaned_data` |
| `stale_prune`            | `last_seen` beyond threshold. Default 90s; **5 min** when `LOGGING_ENVIRONMENT` is `local` or `e2e_test`. Player pruned, connections torn down. | `connection_cleaner.prune_stale_players`   |
| `new_game_session`       | Same character reconnected (e.g. new tab); old connection closed.                                                                               | `connection_session_management`            |
| `select_character_other` | User selected another character; other character's connection force-disconnected.                                                               | `api/players._disconnect_other_characters` |

## Investigation steps

### Step 1: Reproduce and capture server logs

- Run e2e (`make test-playwright`) or the failing multiplayer scenario.
- Ensure server logs go to `logs/local/` (or your dev log dir).

### Step 2: Grep for disconnect reasons and broadcast

```powershell
# PowerShell
Select-String -Path "logs/local/*.log" -Pattern "disconnect_reason|Broadcasting player_left_game|broadcast_event|connection timeout|Pruned stale|new game session|Disconnected existing character"
```

- Correlate timestamps: `disconnect_reason` and `Broadcasting player_left_game` / `broadcast_event=player_left_game` (with `player_id`) appear when a drop occurs.
- Note which `disconnect_reason` applies to the dropped player (use `player_id` or `stale_ids`).

### Step 3: Interpret

- **`connection_timeout`**: Connection exceeded `max_connection_age`. In local/e2e this is 30 min; otherwise 5 min. Long describe blocks or suite length can still trigger it.
- **`stale_prune`**: No client traffic for the configured window (5 min in local/e2e, 90s otherwise). `last_seen` is updated on each WebSocket message (including ping). If pings run but a tab is idle, consider whether that tab sends pings.
- **`new_game_session`**: Client opened a new game session for the same character (e.g. reconnect flow). Check client flow for duplicate connect or session API usage.
- **`select_character_other`**: Same user, different character selected. E2E uses distinct users (AW, Ithaqua); this path should not cross-affect them unless test data shares a user.

### Step 4: Code and config

- **Connection timeout**: `server/realtime/memory_monitor.py` (`max_connection_age`), `server/realtime/maintenance/connection_cleaner.py` (cleanup loop).
- **Stale prune**: `server/realtime/maintenance/connection_cleaner.py` (`prune_stale_players`), `last_seen` updates in `connection_helpers.mark_player_seen_impl` and `websocket_handler` (on each message).
- **New game session**: `server/api/real_time.py` (`handle_new_game_session`), `server/realtime/connection_session_management.py`.
- **Select-character disconnect**: `server/api/players.py` (`_disconnect_other_characters`), `get_user_characters`.

### Step 5: Report

- Document which `disconnect_reason` (and `player_id` if present) matched the drop.
- Include relevant log snippets and timestamps.
- Note configuration (e.g. `max_connection_age`, prune interval) and test setup (describe length, which player dropped).

## Both players see linkdead (Occupants (1) with linkdead)

When E2E instrumentation shows **both** players with `occupantsCount: 1` and `hasLinkdead: true`, each client sees the *other* player as linkdead. That implies both WebSockets have disconnected and entered the 30-second grace period.

### Log evidence (2026-01-30)

Server logs (`logs/local/server.log`) showed:

- **9a2a5560** (ArkanWolfshade): Connected 22:58:00; **Unintentional disconnect, grace period** at 22:58:32.
- **dd1ef0e8** (Ithaqua): Connected 22:58:11; **Unintentional disconnect, grace period** at 22:58:32 (~50ms later).
- **Close code**: `CLOSE 1001 (going away)` for both—**client-initiated** close (browser/tab navigating away or closing).

So both tabs/contexts were closed almost at the same time, which matches Playwright tearing down contexts when a test fails or times out.

### Root cause (CONFIRMED from logs)

The **client** closes the WebSocket with code 1001 (going away). Both connections close within ~50ms. That points to:

1. **Playwright closing both contexts together** when a test fails or times out.
2. **Test flow closing pages** before `ensurePlayersInSameRoom` finishes (e.g. timeout, navigation, or cleanup).

### Possible mitigations

1. **Increase `ensurePlayersInSameRoom` timeout** so it can succeed before Playwright tears down.
2. **Avoid premature context teardown**—ensure `beforeAll`/fixtures keep contexts alive until the hook/test finishes.
3. **Inspect Playwright config**—`fullyParallel: false`, `workers: 1`, and test timeouts can affect when contexts are closed.

### Investigation steps for both-linkdead

1. **Check server logs** for `Unintentional disconnect detected, starting grace period` and `disconnect_reason` to see why each WebSocket closed.
2. **Check close reason** in server.log: `CLOSE 1001 (going away)` = client closed; `disconnect_reason=new_game_session` = server closed for new session.
3. **Check ping behavior**: Ping interval is 30s (`useWebSocketConnection.ts`). If tabs are throttled, pings may not run; verify `last_seen` updates.
4. **Run a single multiplayer spec** (e.g. who-command only) to reduce suite length and connection_age / stale_prune pressure.

## References

- **GAME_BUG_INVESTIGATION_PLAYBOOK.mdc**: Use for full investigation methodology; this doc focuses on mid-run drops only.
