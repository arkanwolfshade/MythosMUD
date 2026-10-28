# ADR-029: Authoritative In-Memory Player Registry

**Version 1.0.4** · MythosMUD · 2026-10-27

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted (design); implementation pending, delivered as a stacked PR series (§6)
**Date:** 2026-10-26
**Amends:** ADR-005 (repository pattern: player repositories become private to the registry), ADR-019 (player
effects: `player_effects` is the only effects store)
**Constrains:** ADR-006 / ADR-007 (one server process; see §5)

## 2. Context

**[BUG] Concurrent full-row saves silently revert each other's player changes**

- **Symptom:** an item picked up during a heal-over-time effect vanished from Postgres milliseconds after the pickup
  saved it. `first-exposure.spec.ts` failed intermittently at `toContain('Jade Amulet')`.
- **Cause:** nothing holds a shared `Player`. `player_repository.get_player_by_id` / `get_player_by_name` build a
  new object from a query on every call, and `save_player` runs `CALL upsert_player(...)`, which overwrites every
  column. The status-effect tick (`server/app/game_tick_status_effects.py`) loaded the player, awaited
  `heal_player`, then saved its pre-pickup copy. Logs (`logs/e2e_test`, 2026-10-26 15:15:23): the pickup's save
  prepared 3 items at .638418, the tick's save prepared 2 at .640323, and every later tick re-wrote 2.
- **Fix:** this ADR. One authoritative in-memory aggregate per player; all reads and writes go through it.

**[NOTE]**
Issue #917 patched one instance of the same class (`clear_player_inventory` exists so it "never rewrites stats"). A survey
of `server/` found the problem is structural, not local:

- `save_player` has 37 non-test call sites, `get_player_by_id` 132 and `get_player_by_name` 64, each loading and
  saving its own copy.
- Writers bypass the row with atomic SQL (`health_repository` damage and heal deltas, `award_player_xp`,
  `update_player_stat_field`, `clear_player_inventory`), and ORM `session.get(Player)` commits run from the death
  and respawn services. Any later full save of an older copy reverts them.
- Periodic writers make the race frequent. The status-effect tick loads every 0.1 s, MP regeneration does a full
  save at 10 Hz, corruption flux runs every 0.6 s, and catatonia decay every 2 s.
- Combat copies DP into `CombatParticipant` at combat start and persists an absolute DP from untracked background
  tasks (`persist_player_dp_background`).
- Two values are stored twice and already disagree: lucidity (`players.stats.lucidity` and
  `player_lucidity.current_lcd`) and status effects (`players.status_effects` and `player_effects`).
- `save_interval = 60` exists in `config/models/game.py` and nothing reads it.

## 3. Decision

**[SPEC]**
A `PlayerRegistry` on the application container owns exactly one `PlayerAggregate` per player. Every read and
mutation of player data goes through it, and every write to the database is made from it. No other code loads or
saves player-keyed rows.

### 3.1 Registry lifecycle

**[SPEC]**

| Concern | Rule |
| --- | --- |
| Scope | Every player that is touched, online or offline. An offline player is loaded on first use. |
| Pinning | Online and disconnect-grace players are pinned. When grace ends: checkpoint flush, then evictable. |
| Eviction | An evictable aggregate with no lock holder and nothing dirty is dropped after 60 s idle. A deleted character is flushed and evicted at once. A dirty aggregate is never evicted. Until every writer of a part goes through the registry (step 4c, and step 8 for the e2e resets), the idle TTL is 0: each unit ends by dropping its unpinned, clean players, so the next unit reads the database fresh. A part kept between units would miss what the other writers change, and its next write would put that stale copy back. |
| Load | The first acquire loads every part in one session (per-part procedures run concurrently), so reads never await. |
| Summary read | Account character lists (character select, `api/tutorial_skip.py`) use a read-only summary query, served from the registry when the player is loaded. It is the only sanctioned non-registry read and never writes. |
| Out-of-band writes | Not handled. No reload on login and no row-version check; the registry is trusted. |

### 3.2 The aggregate

**[SPEC]**

- `PlayerAggregate` is a plain, typed, slotted domain class with no SQLAlchemy. The ORM `Player` model is not used at
  runtime.
- It is made of parts, each with its own mutators and dirty flag:

| Part | Store |
| --- | --- |
| core | `players` row and `stats` jsonb: DP, MP, corruption, fear, occult knowledge, position, XP, level, room, tutorial instance |
| inventory | `player_inventories` (inventory, equipped) |
| lucidity | `player_lucidity`, `lucidity_exposure_state` |
| effects | `player_effects` |
| quests | `quest_instances` |
| skills / spells | `player_skills` / `player_spells` |
| cooldowns | `lucidity_cooldowns` (including `DEBRIEF_PENDING`), `corruption_cooldowns` |
| social | `player_aliases`, `player_mutes`, `player_channel_preferences` |
| exploration | `player_exploration` |
| owned items | player-owned `containers` (wearable, bank box) and `item_instances` with `owner_type='player'` |

- Outside the aggregate: append-only ledgers (`lucidity_adjustment_log`, `corruption_adjustment_log`,
  `skill_use_log`). They are written in the same transaction as the flush that applies the change they record.
- Duplicate stores are removed: `player_lucidity` and `player_effects` win. A DDL migration drops
  `players.stats.lucidity` and `players.status_effects`, with a DML migration in the data repo if values need
  carrying over.
- Validation (inventory schema, stat ranges) runs in the mutators, so a bad change is rejected inside the command.

### 3.3 Access API

**[SPEC]**

```python
async with registry.mutate(player_id, sync=False) as player:   # per-player asyncio.Lock
    player.inventory.add(stack)                                  # mutators mark parts dirty, queue events

async with registry.mutate_many([a, b]) as (pa, pb):            # locks taken in sorted player-id order
    ...

view = registry.peek(player_id)   # live object, read-only Protocol type; no lock, never awaits
```

- **Locking:** one `asyncio.Lock` per player covers the whole read-modify-write. A transfer with a world container
  takes the player locks first, then the container lock.
- **Re-entrancy:** a nested `mutate(pid)` in the same task reuses the outer handle, found through a contextvar. The
  handle records its owning task, and reuse requires `asyncio.current_task() is handle.owner`, because child tasks
  (`create_task`, EventBus subscriber tasks) inherit contextvars. Inner changes join the outer unit; an inner
  `sync=True` escalates it; only the outermost block commits or rolls back.
- **Reads:** `peek()` is typed as a getters-only Protocol, so basedpyright rejects mutation outside `mutate()`.
- **Events:** mutators queue domain events on the handle. The outermost successful exit publishes them to the
  EventBus (after the commit, in sync mode); a rollback discards them. They replace the hand-published
  `PlayerDPUpdated`, `QuestLogChanged`, inventory broadcasts and lucidity change events.

### 3.4 Persistence

**[SPEC]**

| Mode | Parts / operations | Behaviour |
| --- | --- | --- |
| Sync | inventory, equipped, owned items and containers (including the bank), currency, quest state changes (start, complete, abandon), death and respawn, character delete | Commits before the command returns. On failure the in-memory change is rolled back and the command fails. |
| Lazy | DP, MP, lucidity, effect counters, position and posture, XP, quest progress counters | Marked dirty; written by the sweep. |

- A mutator can force sync (`mutate(pid, sync=True)`, for example admin set). A sync part is never written lazily.
- **Flush unit:** one transaction per player, calling only the dirty parts' procedures, then one commit. A sync
  commit writes every dirty part, lazy ones included. Each part's procedure writes only that part's columns
  (`update_player_row`, `update_player_inventory`), never the full-row `upsert_player`, so a part write cannot carry
  a stale copy of a part it did not change.
- **Lazy sweep:** every `save_interval` (repurposed; default 2 s, configurable), the tick loop starts
  `registry.flush_dirty()` as a tracked task. At most K player transactions run concurrently (configurable), and a
  sweep is skipped while the previous one is still running.
- **Failure:** a failed lazy flush leaves the player dirty and retries with backoff; `track_exception` fires after N
  consecutive failures.
- **Shutdown:** `flush_all()` runs in `shutdown_sequence` before the DB pool closes.
- **Transfers** with a world container (furniture, corpse) or another player lock every party, mutate in memory, and
  commit everything in one transaction before returning; on failure everything rolls back. Room floor drops are
  in-memory only (`room_subscription_manager.py`), so a floor pickup or drop is a sync commit on the player alone.

### 3.5 Subsystem consequences

**[SPEC]**

- **Combat:** a player's `CombatParticipant` references the aggregate; DP has one home. `persist_player_dp_background`,
  the player side of `combat_persistence_handler.py`, and the dead `combat_hp_sync.py` are deleted.
- **Ticks** (status effects, MP regeneration, DP decay, catatonia, corruption and lucidity flux) iterate pinned
  aggregates through lazy `mutate()`. No per-tick loads or full saves.
- **Atomic bypass writers** become aggregate mutators. That covers `heal_player` / `damage_player`, `award_player_xp`,
  `update_player_stat_field`, `clear_player_inventory`, `update_player_current_room`, `update_player_last_active`,
  the LucidityService ORM writes, and the death and respawn ORM commits.
- **Movement:** the `threading.RLock` held across awaits in `movement_service.py` (no exclusion between coroutines)
  is replaced by the registry lock.
- **E2E harness:**
  - Test-only endpoints, mounted only under the e2e config flag, reset players through the registry and serve
    `GET /admin/test/players/{name}/state` in the `E2ePlayerState` shape.
  - `scripts/e2e_reset_players.py` and `scripts/e2e_player_state.py` are retired.
- **Enforcement:** the player repositories' load and save become private to the registry. A lint rule (in the style
  of `scripts/lint_raw_sql_in_python.py`) rejects direct use anywhere else.

## 4. Alternatives Considered

**[NOTE]**

- **Narrow column writes for the hot writers only** (the #917 approach, extended): rejected as the end state. It
  removes the most frequent racer quickly but leaves command-versus-command races and the duplicate stores.
- **Optimistic locking (a `version` column checked by `upsert_player`)**: rejected. It turns silent loss into loud
  failure but leaves every caller with a fresh copy and a retry policy to decide.
- **Per-player lock around today's load-modify-save**: rejected. It is cheap, but any new caller can bypass it, and
  it keeps the database round trip per operation.
- **Phased aggregate (the `players` row first, other tables later)**: rejected by the project owner in favour of
  owning all per-player state at once.
- **Write-through for everything**: rejected. It keeps the 1 Hz and 10 Hz ticks' write volume and makes commands
  wait on the database for values that change continuously.
- **Per-player debounced flush (quiet window plus cap)**: rejected. With ticks at 1 Hz and faster, an active player
  always hits the cap, so it degenerates into a fixed sweep with extra bookkeeping.
- **Reload on login and a row version for out-of-band writes**: rejected. In normal operation nothing else writes
  player rows, and reloading on reconnect discards the value of the idle TTL.
- **Compatibility shims during migration** (the old `get_player_*` / `save_player` returning the registry object):
  rejected. There is no production server, so intermediate PRs may coexist with old paths.

## 5. Consequences

**[SPEC]**

- **Positive:** the lost-update class is closed for every player write, including the atomic bypasses and combat.
  Tick write volume drops from per-tick full saves to one sweep. The duplicate lucidity and effects stores are
  removed. Client events fire only for changes that happened.
- **Negative:** a crash loses up to one sweep interval of lazy data (DP, MP, lucidity, XP, counters). The server must
  run as a **single process**; a second process would hold its own registry and reintroduce lost updates. The change
  touches roughly 230 call sites and the combat, tick, death and respawn paths.
- **Neutral:** out-of-band SQL against a loaded player is silently overwritten; tooling must go through server
  endpoints. Offline players cost memory for up to 60 s after use.

## 6. Delivery

**[SPEC]**
Stacked PRs (`gh stack`), each green on its own, with correctness required once the stack merges:

1. This ADR.
2. Core: `PlayerRegistry`, `PlayerAggregate`, the `Part` protocol, the read-only Protocol, locks, re-entrancy,
   events, sweep, and shutdown flush, plus the first real part (the `players` row and inventory, over
   `get_player_by_id` / `upsert_player`). Unit-tested on its own; no callers yet. Each later step adds its own
   parts and mappers alongside the callers that use them.
3. Schema: drop the duplicate stores and move their readers, in two PRs. 3a moves lucidity onto `player_lucidity`
   (readers and writers through `LucidityService`, `stats.lucidity` dropped from the store and the wire). 3b is
   itself two PRs: 3b-i extends `player_effects` for the tick-driven and spell effects and moves every reader and
   writer onto it; 3b-ii drops `players.status_effects` from the table, the player procedures, the ORM model and
   `PlayerRead`.
4. Inventory, bank, containers and transfers, in three PRs. Only the registry writes the inventory columns.
   - 4a: the inventory part and its narrow write; the player-only commands (pickup, drop, equip, unequip, use) run
     their read-modify-write as one unit of work.
   - 4b: world-container transfers (put, get, the REST transfer and loot-all) commit the player and the container in
     one transaction, under a per-container lock taken after the player locks; plus bank and wearable containers.
   - 4c: the remaining inventory writers (quest rewards, spells, the instance flush, the corpse transfer, admin).
     Then `upsert_player` stops updating the inventory columns, and the lost-update regression test lands. That
     can't happen earlier, because until then the legacy writers save inventory only through `upsert_player`.
5. Quests, lucidity, corruption, cooldowns and debrief.
6. Ticks and periodic writers, combat, death and respawn.
7. Movement, magic, skills and spells, social, exploration.
8. Connection lifecycle (login, grace, logout, pin and evict), API and admin, e2e test endpoints and fixtures.
9. Gate: privatise the player repositories, delete the ORM runtime paths, and add the lint rule.

## 7. Open Items

**[?]**

- Whether `player.pose` is a persisted column (the survey did not confirm it) decides which part owns it.

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-10-26 | Initial decision record |
| 1.0.1 | 2026-10-26 | §6: step 2 ships the machinery plus the `players`-row part; other parts land with their callers |
| 1.0.2 | 2026-10-26 | §6: step 3 splits into 3a (lucidity) and 3b (effects). §7: K and N were set in step 2 (4 and 5); lucidity's drift was measured (2 of 4 dev characters disagreed) and resolved by backfilling missing `player_lucidity` rows from `stats.lucidity` |
| 1.0.3 | 2026-10-27 | §6: step 3b splits into 3b-i (move to `player_effects`) and 3b-ii (drop `players.status_effects`). §7: no data migration was needed; the column held only short-lived tick state, which 3b-i stopped reading |
| 1.0.4 | 2026-10-27 | §3: each part's procedure writes only its own columns; the idle TTL is 0 until every writer of a part goes through the registry (4a's e2e run showed a cached inventory writing back items a legacy `put` had moved). §6: step 4 splits into 4a (inventory part, player-only commands), 4b (container transfers in one transaction, bank, wearable) and 4c (remaining writers, then `upsert_player` stops writing inventory) |
