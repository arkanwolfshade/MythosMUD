# ADR-029: Authoritative In-Memory Player Registry

**Version 1.0.20** · MythosMUD · 2026-11-11

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
| lucidity | `player_lucidity` |
| exposure | `lucidity_exposure_state` (encounter counts per archetype) |
| effects | `player_effects` |
| quests | `quest_instances` |
| skills / spells | `player_skills` / `player_spells` |
| cooldowns | `lucidity_cooldowns` (including `DEBRIEF_PENDING`), `corruption_cooldowns` |
| social | `player_aliases`, `player_mutes`, `player_channel_preferences` |
| exploration | `player_exploration` |
| owned items | player-owned `containers` (wearable, bank box) and `item_instances` with `owner_type='player'` |

- Outside the aggregate: append-only ledgers (`lucidity_adjustment_log`, `corruption_adjustment_log`,
  `skill_use_log`). They are written in the same transaction as the flush that applies the change they record:
  a part queues the rows (lucidity's own, or a generic ledger part for corruption) and its write inserts them.
- The core part writes only what a unit changed: the changed columns and the changed `stats` keys, merged into
  the stored jsonb (`stats || changes`; a key sent as null is removed). Players are still saved outside the
  registry until step 9, so a write must never put back a stale copy of anything it did not change.
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

async with registry.mutate(player_id, containers=[cid]) as player:  # then the container's lock
    player.inventory.set_carried(carried)
    registry.write_container(cid, write)                         # committed in the unit's transaction

view = registry.peek(player_id)   # live object, read-only Protocol type; no lock, never awaits
```

- **Locking:** one `asyncio.Lock` per player covers the whole read-modify-write. A transfer with a world container
  names it when the unit opens (`containers=[...]`); the unit takes the player locks first, then the container
  locks, each set in sorted id order, so two units never wait on each other. Asking for a player or container the
  unit does not hold raises `LockOrderError`. A container session's mutation token only authorises the transfer: it
  is the same for every transfer while the container is open, so it is never used to drop duplicates.
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
| Sync | inventory, equipped, owned items and containers (including the bank), currency, every quest change (start, progress, complete, abandon), cooldowns, encounter counts, corruption, effects and their countdown (until step 8), DP and MP (until step 8), death and respawn, character delete | Commits before the command returns. On failure the in-memory change is rolled back and the command fails. |
| Lazy | DP and MP (from step 8), lucidity, effect counters (from step 8), position and posture, XP | Marked dirty; written by the sweep. |

- A mutator can force sync (`mutate(pid, sync=True)`, for example admin set). A sync part is never written lazily.
- **Flush unit:** one transaction per player, calling only the dirty parts' procedures, then one commit. A sync
  commit writes every dirty part, lazy ones included. Each part's procedure writes only that part's columns
  (`update_player_row`, `update_player_inventory`), never the full-row `upsert_player`, so a part write cannot carry
  a stale copy of a part it did not change. The reverse holds too: once a player exists, `upsert_player` writes no
  inventory columns (step 4c-iii), so a legacy full-row save of a copy loaded before an inventory commit keeps its
  own columns and leaves the stacks alone.
- **Lazy sweep:** every `save_interval` (repurposed; default 2 s, configurable), the tick loop starts
  `registry.flush_dirty()` as a tracked task. At most K player transactions run concurrently (configurable), and a
  sweep is skipped while the previous one is still running.
- **Failure:** a failed lazy flush leaves the player dirty and retries with backoff; `track_exception` fires after N
  consecutive failures.
- **Shutdown:** `flush_all()` runs in `shutdown_sequence` before the DB pool closes.
- **Transfers** with a world container (furniture, corpse) or another player lock every party, mutate in memory, and
  commit everything in one transaction before returning; on failure everything rolls back. The container's new
  contents are a write handed to the unit (`write_container`), applied after the players' parts in the same
  transaction; that write never commits and never skips an item it cannot write, so a failure moves nothing. A row
  the unit itself creates (a corpse) is a `write_new` write: it takes no lock, since no other unit can see it before
  the commit. A death is one such unit: the corpses, the deletes of the worn-container rows folded into them, and
  the emptied player commit together. A write to a container alone (the bank forward of a flushed instance) is a
  unit with no players, `mutate_many([], containers=[cid])`. Room
  floor drops are in-memory only (`room_subscription_manager.py`), so a floor pickup or drop is a sync commit on the
  player alone.

### 3.5 Subsystem consequences

**[SPEC]**

- **Combat:** DP has one home, the aggregate. A hit on a player runs as one unit on the live DP, and a player's
  `CombatParticipant` holds a copy refreshed each round: unpinned aggregates can be evicted until step 8, so it cannot
  hold a reference. `persist_player_dp_background`, the player side of `combat_persistence_handler.py`, and the dead
  `combat_hp_sync.py` are deleted.
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
  - `scripts/e2e_reset_players.py`, `scripts/e2e_player_state.py` and `scripts/e2e_place_player.py` are retired.
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
   - 4c: the remaining inventory writers, in three PRs. Admin and player creation need nothing (creation is an
     insert).
     - 4c-i: the spells (create object, consume reagents), the quests (collect_n turn-in consumption, and "item"
       rewards built for real through one `ItemGranter`), and the tutorial run reset. The run reset strips
       instance-bound items through the registry after the caller's own save (reconnect) or commit (the First
       Exposure ending, whose respawn commits through its own ORM session). Stacks taken from a container are
       carried as general inventory (`slot_type` `inventory`), like a pickup, so `equip` infers their slot.
     - 4c-ii: death's corpse transfer as one unit (the corpses and the strip in one transaction), with an
       `inventory_updated` to the player; the instance flush's bank forward under the container lock.
     - 4c-iii: `upsert_player` stops updating the inventory columns, and the lost-update regression test lands.
       That can't happen earlier, because until then the legacy writers save inventory only through
       `upsert_player`.
5. Quests, lucidity, corruption, cooldowns and debrief, split by area:
     - 5a: quests. A quests part (every `quest_instances` row of the player, keyed by quest id); each `QuestService`
       operation is one unit, and `QuestLogChanged` / `QuestCompleted` are published after its commit.
       `QuestInstanceRepository` is deleted. Quest progress counters are sync too, not lazy: a kill or a pickup
       that counts commits before it returns.
     - 5b: lucidity, split by table:
         - 5b-i: a lucidity part (`player_lucidity`: LCD, tier, liabilities, `catatonia_entered_at`). It is lazy;
           each change queues its `lucidity_adjustment_log` row on the part, and the flush writes both in one
           transaction. `LucidityService` runs each operation as one unit and announces (observer, client events,
           tier cache) only after it. Every reader and writer moves at once, the ticks (catatonia, drain, passive
           flux) and the run restart's lucidity reset included, because a writer left on the ORM would revert the
           registry's unflushed change.
         - 5b-ii: an exposure part (`lucidity_exposure_state`) and a cooldowns part (`lucidity_cooldowns`: recovery
           actions, hallucination timers, the involuntary flee, the debrief's `DEBRIEF_PENDING`), both sync. One
           function, `get_player_lucidity_state`, loads them with the lucidity row; a cooldown write replaces the
           player's whole set, so a cleared code is deleted. A check and its new cooldown are one unit (a recovery,
           a hallucination roll, a flee), as are an encounter's count and its loss, and a delirium respawn's
           lucidity reset and its `DEBRIEF_PENDING`. `LucidityRepository` is deleted.
     - 5c: corruption (`stats.corruption` in the row part, `corruption_cooldowns`, `corruption_adjustment_log`).
       Corruption is sync: `CorruptionService` runs each change as one unit, committing the value, its ledger row
       and any cleanse cooldown before it returns, so the readers that still load players from the database see
       it. Writers that hold only `persistence` (spells, mechanics) call its `adjust_corruption`, which runs the
       service injected at startup.
       Until step 8 raises the idle TTL, a lazily dirty part keeps its player in memory until the sweep, so its
       row part can trail writers that still use `upsert_player`. 5c closes that for corruption in two ways: the
       row part writes only the `stats` keys a unit changed (`update_player_row` merges them), and `upsert_player`
       keeps an existing player's stored corruption, so the registry is its only writer. Out-of-band scripts
       (`e2e_reset_players.py`, `e2e_player_state.py`) could still race a resident dirty player in that window;
       step 8b replaced them with server endpoints.
6. Ticks and periodic writers, combat, death and respawn.
   - 6a: DP. The DP rules are pure functions of a player's stats (`models/player_dp.py`), shared by the ORM
     `Player` and `PlayerHealthService`, the one write path for `stats.current_dp`. Damage and healing (status
     effects, mechanics, spells, the effects API) reach it through the persistence layer's injected service;
     combat's background write, admin `set DP`, the death tick's decay, `handle_player_death` and every respawn are
     registry units. A respawn is one unit: room, DP, posture, death room and, after a delirium or sanitarium, the
     lucidity and `DEBRIEF_PENDING` commit together. `HealthRepository` and the dead `combat_hp_sync.py` are
     deleted.
     DP is sync until step 8 moves its readers onto the registry: the tick's candidate queries and many commands
     still read players from the database. `update_player_row` now sets only changed columns too: before 6a it
     wrote every column from the aggregate's copy, so a sync corruption write from a player kept resident by lazy
     lucidity could put back a room or XP that movement had saved meanwhile. `upsert_player` keeps an existing
     player's stored `current_dp`, `corruption`, `death_room_id` and `death_location` (present or absent), so the
     registry is their only writer. Posture (`position`) still has legacy writers (sit, stand, logout) until step 7.
   - 6b: MP. `models/player_mp.py` holds the rules and `PlayerMpService` is the one write path for
     `stats.magic_points`: spell costs, spell and item restores, rest, meditation, regeneration and admin `set MP`,
     each one sync unit. `upsert_player` keeps an existing player's stored MP too. Regeneration runs every tick, and
     a unit costs several reads and a commit, so the fraction accrues on `MPRegenerationService` (it used to be
     `stats._mp_fractional`, saved with a full `save_player` at 10 Hz) and a unit opens only when a whole MP has
     built up, about every 10 s. A restart loses less than one MP's progress. The tick still reads the player's row
     each time, for the max check and the posture; step 8 can read the pinned aggregate instead.
     Two MP bugs went with it. 0 MP used to read as full, in the cast check and the client's stats: new characters
     were stored with 0, and those reads patched it. A new character is now stored with full MP and 0 means drained.
     And a `stat_modify` effect can now change MP: Power Drain's `{"stat": "mp", "transfer_to_caster": true}` was
     ignored, and now moves the MP to the caster in one transaction (player targets only).
   - 6c: combat DP. A hit on a player is one sync unit (`CombatAttackHandler.apply_player_hit`): it reads the live DP,
     runs combat's rules (armor, `no_death` rooms, the login ward) and commits before the client's `PlayerDPUpdated`
     goes out. 6a only moved the old write onto the registry: it still wrote the participant's copy as an absolute
     value, from a background task, so a heal or damage over time during a fight was overwritten by the next hit. The
     background task and its correction event are gone; a failed commit lands no damage. Each round starts by
     refreshing players' copies, so who can act and who is targeted follow heals made between rounds.
   - 6d: status effects. A player's running `player_effects` rows are a part of the aggregate (`PlayerEffectsPart`),
     loaded with the player by the same function as lucidity's cooldowns and exposures (`get_player_lucidity_state`
     gained an `effects` column). Every change is sync and is one row-level write queued on the part: add, end by
     id or type, end the instance-scoped ones, replace a payload, and the countdown. The part names its row ids
     (`add_player_effect` takes an optional id), so a row added in one unit can be changed in a later one. Spells,
     the login ward and scripted content add and end effects through `PlayerEffects`, the persistence layer's
     injected effects service. The tick runs one unit per online player who has an effect (a single candidate query
     a second, `get_player_ids_with_active_effects`): every effect's second, the DP and lucidity it moved, a changed
     payload, and the countdown commit together, and the client's DP update is queued on the aggregate and sent
     after the commit. That closes three seams: the lucidity drain's LCD loss and its `elapsed` were two commits,
     so a failure between them replayed a second; an effect removed or added after the tick's snapshot still got
     (or lost) a second; and damage over time sent no DP update, where healing did. The ORM load per second is gone.
     The countdown stays sync here, against §3.4's lazy counters: `advance_player_effects` used to be a separate
     batched statement, which would leave a resident copy of the rows stale (an expired effect would keep running),
     so the part now counts down its own copy and queues the same procedure for the one player in the unit. A
     player with only count-down effects costs one unit a second until pinning (step 8) lets the counters be lazy.
7. Movement, magic, skills and spells, social, exploration. Split by area (7a to 7d), each its own PR.
   - 7a: movement and posture. `MovementService.move_player` is one unit of work on the moving player: it resolves
     the player (by id or name), holds their registry lock from validation to the commit, writes the new room (and,
     on leaving a tutorial instance, `tutorial_instance_id` and a template `respawn_room_id`) as one sync write of
     only the changed columns, and flushes the exited instance after the commit. The flush opens its own container
     unit, so it cannot run inside the player's. This replaces the `threading.RLock` held across awaits, which
     excluded nothing between coroutines: two moves of one player validated at once, each saved the whole loaded
     row, and either could put back a posture or XP change the other had just made. `add_player_to_room` writes
     its room through a unit the same way, and the sync occupancy methods lose the lock (they hold it across no
     awaits). `PlayerPositionService` writes `stats.position` as a unit, so sitting, standing and resting no
     longer save the player. Both services require the registry; there is no fallback to `save_player`.
     Still open until step 8: `upsert_player` writes the room, `last_active` and most stats from whatever copy a
     legacy saver holds (logout, the tutorial reconnect, admin set stat, quest rewards, communication), and the
     reconnect relies on that to place a player in a fresh instance. A save from a copy loaded before a move or
     a posture change can still put the old value back; making `upsert_player` keep an existing player's room and
     posture waits for those writers to move.
   - 7b: XP and level. `LevelService.grant_xp` (combat and quest rewards both use it) is one sync unit on the
     player: the XP is added to the live total, the level follows the curve and never falls, only those two columns
     are written, and the client's `PlayerXPAwardEvent` is sent after the commit. It used to call the stored
     function `award_player_xp`, a row-locked atomic update; a resident copy of the row would have gone stale
     against that (the lesson of step 6d's countdown), so the function, its repository method and the persistence
     delegate are gone. The curve lives in `models/player_xp.py` as integer arithmetic, and an integration test
     checks it against the SQL `level_for_xp` for every level boundary (and the XP either side) up to level 5,999
     and the top of the integer range, so the one remaining copy of the curve in SQL cannot drift. `upsert_player`
     now leaves an existing player's `experience_points` and `level` as stored, as it does for DP and MP: a save of a
     copy loaded before an award can no longer write the old XP back (the integration test fails on the old
     procedure). The `respawn_room` quest reward was the other `save_player` here: it is a unit that writes only
     `respawn_room_id`, and `QuestService` no longer takes `async_persistence`.
8. Connection lifecycle (login, grace, logout, pin and evict), API and admin, e2e test endpoints and fixtures.
   Delivered in slices; making DP and MP lazy is deliberately not one of them (issue #1202: it needs every DP and MP
   reader on the registry first, the death tick's SQL candidate queries included).
   - 8a: the lifecycle savers. Logout and quit stamp `last_active` through a registry unit (lazy: the sweep or shutdown
     writes it) instead of saving the whole row, and no longer copy the connection manager's `position` into the
     player's stats first. That value is a cache set at connect and on respawn only, so the copy put an old posture
     back (sit, log out, come back standing). The tutorial reconnect commits the room and the new instance id as one
     sync unit (`place_in_instance`); the instance id used to reach the database only through the whole-row
     save. The admin shutdown's first phase flushes the registry (`close()`) instead of loading and re-saving every
     online player; the lifespan shutdown flushes again, but the process terminator forces an exit ten seconds after
     it asks, so the early flush stays. Pin and unpin move to 8d: a pinned player stays resident like a non-zero idle
     TTL, which is only safe once every writer of registry-owned values is a unit, so it waits for 8c.
   - 8b: the e2e harness. `/v1/admin/test/...` replaces the three scripts that wrote Postgres behind the registry:
     `POST players/reset` (the shared players back in the default room at 50 DP), `POST players/{name}/reset-tutorial`,
     `POST players/{name}/place` and `GET players/{name}/state` (the `E2ePlayerState` shape). Each reset is one sync
     registry unit over the aggregate's own parts: room, DP, corruption and posture on the row part, the Sling through
     `inventory.replace`, lucidity, cooldowns and effects (the login ward kept), and quests through a new
     `PlayerQuestsPart.clear()` whose write calls `delete_quest_instances_by_player` before the upserts. Only the
     lost-and-found chest and the deposit box, which are containers outside the aggregate, are emptied through the
     persistence layer. The state read is the registry's view, not a database query, so it also shows what a lazy
     write has not yet flushed. The router is mounted only when the logging environment is `e2e_test` and the
     database is `mythos_e2e`, and checks the admin role itself rather than through `validate_permission`, whose
     100-requests-per-five-minutes limit the specs' polling of the state endpoint would exhaust. The Playwright
     fixtures sign in as the seeded admin (ArkanWolfshade) once per worker and await the calls; global setup resets
     the shared players after the server checks, since the reset needs the server up. A reset still does not refuse
     an online character, as the scripts did not: the spec logs them out first.
   - 8c: the remaining writers of registry-owned values (fear and occult knowledge, admin set stat, `last_active`)
     and the communication and spell-effect savers deferred from 7c and 7d.
   - 8d: pin on connect and unpin when the grace period ends; raise `player_registry_idle_ttl_seconds` above 0 once
     every writer is a unit, and make the effects countdown lazy.
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
| 1.0.20 | 2026-11-11 | §6: step 8a as shipped (logout and quit stamp `last_active` through the registry and stop copying the connection manager's cached position; the tutorial reconnect commits room and instance as one unit; the admin shutdown flushes the registry instead of re-saving players). Pin and unpin move from 8a to 8d, since pinning is equivalent to a non-zero idle TTL |
| 1.0.19 | 2026-11-11 | §6: step 8 is sliced into 8a to 8d, with lazy DP and MP out of it (#1202). Step 8b as shipped (test-only `/v1/admin/test` endpoints on the e2e server replace `e2e_reset_players.py`, `e2e_player_state.py` and `e2e_place_player.py`; resets are registry units, `PlayerQuestsPart.clear()` and `delete_quest_instances_by_player` are new, the state read is the registry's view) |
| 1.0.18 | 2026-11-11 | §6: step 7b as shipped (XP and level are a registry unit with the curve in Python, pinned to `level_for_xp`; `award_player_xp` removed; `upsert_player` keeps XP and level; the respawn-room quest reward is a unit) |
| 1.0.17 | 2026-11-10 | §6: step 7 is split into 7a to 7d. Step 7a as shipped (a move is one unit on the moving player, replacing the `RLock`; room, tutorial exit and posture are changed-column sync writes; the instance flush follows the commit; `upsert_player` still takes the room from legacy savers until step 8) |
| 1.0.16 | 2026-11-10 | §3.4: effects and their countdown are sync until step 8 (counters lazy then). §6: step 6d as shipped (`PlayerEffectsPart`, row-level sync writes with part-named ids, loaded by `get_player_lucidity_state`; `PlayerEffects` service; the tick is one unit per player with effects and sends damage-over-time DP updates; the countdown moves from a batched statement into the unit) |
| 1.0.15 | 2026-11-05 | §3.5: a player's `CombatParticipant` holds a per-round copy of DP, not a reference. §6: step 6c as shipped (a hit is one sync unit on the live DP; background write and correction event removed) |
| 1.0.14 | 2026-11-03 | §3.4: MP is sync until step 8. §6: step 6b as shipped (MP rules, `PlayerMpService`, regeneration accrues in memory and writes per whole MP, `upsert_player` keeps MP; 0 MP means drained; Power Drain moves MP) |
| 1.0.13 | 2026-11-03 | §3.2: the core part writes only changed columns and stats keys (a null key is removed). §3.4: DP is sync until step 8. §6: step 6a as shipped (DP rules, `PlayerHealthService`, death and respawn units, `upsert_player` keeps DP and the death room) |
| 1.0.12 | 2026-11-03 | §3.2: the core part writes only changed `stats` keys (merged); ledgers are queued on a part. §3.4: corruption is sync. §6: step 5c as shipped (`upsert_player` keeps stored corruption; `adjust_corruption` on the persistence layer) |
| 1.0.11 | 2026-11-02 | §3.2: exposure is its own part. §3.4: cooldowns and encounter counts are sync. §6: step 5b-ii as shipped (one load function, replace-set cooldown writes, checks and their cooldowns in one unit) |
| 1.0.10 | 2026-10-30 | §6: step 5b splits into 5b-i (the lazy lucidity part and its ledger, every reader and writer, ticks and the run restart's reset included) and 5b-ii (exposure state and cooldowns, sync); 5c is corruption only; the TTL-0 residency hazard for 5c and the e2e scripts is recorded |
| 1.0.9 | 2026-10-30 | §3.4: every quest change is sync, progress counters included. §6: step 5 splits into 5a (quests), 5b (lucidity, cooldowns, debrief) and 5c (corruption, run restart) |
| 1.0.8 | 2026-10-30 | §3.4: `upsert_player` writes the inventory columns only when it inserts a player; after that only the registry writes them (step 4c-iii, which ends step 4) |
| 1.0.7 | 2026-10-29 | §3.4: `write_new` for rows a unit creates (corpses); a death is one unit; a container-only unit for the bank forward (step 4c-ii) |
| 1.0.6 | 2026-10-29 | §6: step 4c splits into 4c-i (spells, quests, tutorial run reset), 4c-ii (death's corpse transfer, the bank forward) and 4c-iii (the `upsert_player` narrowing); quest "item" rewards, never wired to a working service, are built in 4c-i |
| 1.0.5 | 2026-10-28 | §3.3: units name the world containers they write, whose locks follow the player locks; container session tokens are not deduplication tokens. §3.4: the container write runs in the unit's transaction and never commits or skips items on its own (4b's integration test found the item upserts committing mid-transfer). §6: 4c also puts the remaining out-of-unit container writers under the container lock |
| 1.0.4 | 2026-10-27 | §3: each part's procedure writes only its own columns; the idle TTL is 0 until every writer of a part goes through the registry (4a's e2e run showed a cached inventory writing back items a legacy `put` had moved). §6: step 4 splits into 4a (inventory part, player-only commands), 4b (container transfers in one transaction, bank, wearable) and 4c (remaining writers, then `upsert_player` stops writing inventory) |
