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

## References

- **GAME_BUG_INVESTIGATION_PLAYBOOK.mdc**: Use for full investigation methodology; this doc focuses on mid-run drops only.
