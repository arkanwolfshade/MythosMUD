# App Package Design

**Version 1.0.0** · MythosMUD · 2026-08-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`server/app/` is the process orchestration layer: FastAPI app construction, the startup/shutdown
lifespan sequence, the container wiring entry point, tracked-task bookkeeping, the game tick
loop, and memory/orphan-task cleanup. `CONTAINER_SYSTEM_ARCHITECTURE.md` and ADR-002 document
the container itself; this package documents what *drives* it. Reverse-engineered from code;
code is the source of truth (see [`docs/subsystems/README.md`](../subsystems/README.md)). Written
to close [`#741`](https://github.com/arkanwolfshade/MythosMUD/issues/741).

## 2. Members

**[SPEC]**

| Cluster | Files | Purpose |
| --- | --- | --- |
| App factory | `factory.py` | `create_app()` — constructs the `FastAPI` instance, configures CORS, wires the HTTP middleware stack (see [`PACKAGE_MIDDLEWARE_DESIGN.md`](PACKAGE_MIDDLEWARE_DESIGN.md)), registers v1 routers, runs the startup invariant check. Called once from `server/main.py`. |
| Lifespan orchestration | `lifespan.py`, `lifespan_startup.py`, `lifespan_shutdown.py` | `lifespan()` — the `@asynccontextmanager` FastAPI passes to `create_app(lifespan=...)`. Delegates to `_startup_application` (`lifespan_startup.py`, 21 functions — the single largest file in the package: service construction order, item prototypes, legacy service bindings) and `_shutdown_with_error_handling` (`lifespan_shutdown.py`, 7 functions: NATS handler, connection manager, and further subsystem teardown, each independently error-guarded so one failing shutdown step doesn't block the rest). `lifespan.py` itself also owns periodic memory-metrics logging (`_log_memory_metrics_periodically`) and startup/shutdown metrics delta + persistence-to-file. |
| Event subscription wiring | `lifespan_event_subscriptions.py` | `subscribe_room_occupants_refresh`, `subscribe_quest_events` — connects the EventBus to handlers at startup; the wiring layer between `server/events/` and the subsystems that react to game events. |
| Magic system startup | `lifespan_magic.py` | Spell repository and `SpellRegistry` initialization, prerequisite validation — magic-specific startup sequencing broken out of the general `_startup_application` flow. |
| Container/protocol access | `lifespan_protocols.py` | `lifespan_container` and helpers (`_container_attr`, `_legacy_container_attr`) — typed accessors into `app.state`'s `ApplicationContainer`, insulating the rest of this package from `app.state`'s untyped `Any` shape. |
| Task tracking infrastructure | `task_registry.py`, `tracked_task_manager.py` | `TaskRegistry` (20 methods) — the canonical `register_task(coro, name, category)` entry point every long-lived background coroutine in the server goes through, keyed by a lifecycle name and category, with completion callbacks. `TrackedTaskManager` (7 methods) plus `patch_asyncio_create_task_with_tracking` — a lower-level supervision layer `TaskRegistry` is built on. |
| Game tick loop | `game_tick_counter.py`, `game_tick_processing.py`, `game_tick_corpses.py`, `game_tick_death.py`, `game_tick_status_effects.py`, `game_tick_protocols.py` | The per-tick simulation step: `get_current_tick`/`set_current_tick` (the counter), `process_combat_tick`/`process_casting_progress` (dispatch), corpse decay cleanup, death-threshold/mortally-wounded processing, damage/heal-over-time status effects, and the `_TickCombatService`/`_TickConnectionManager` protocol definitions the tick loop depends on without importing their concrete classes. |
| Memory/orphan cleanup | `memory_cleanup_service.py`, `memory_lifespan_coordinator.py` | `MemoryThresholdMonitor` — watches process memory, triggers `managed_task_cleanup` past a threshold. `PeriodicOrphanAuditor` — a periodic sweep for orphaned tracked tasks, registered the same way as any other background loop (§3). |

## 3. Boundary contract

**[SPEC]**

**Exports.** `server/main.py` imports `create_app`-adjacent wiring from `factory.py` and
`lifespan` from `lifespan.py` — those two names are this package's actual public surface. Every
other member (task registry, game tick functions, memory services) is imported directly by the
services that need it; there is no package-level `__init__.py` re-export list.

**Dependents:** `server/main.py` (`create_app()`, `lifespan`); every service that registers a
background loop goes through `container.task_registry.register_task` rather than calling
`asyncio.create_task` directly; the combat/status-effect/corpse/death services the tick-loop
files dispatch into.

**Invariants a caller must not violate:**

- **The established pattern for periodic background work is register-through-`TaskRegistry`, not
  a bare `asyncio.create_task`.** `_log_memory_metrics_periodically` (`lifespan.py`) is the
  reference example: an `async def` with a `while True: ... await asyncio.sleep(interval)` loop,
  registered via `container.task_registry.register_task(coro, "lifecycle/name", "lifecycle")`
  inside `_startup_application`. Any new periodic task should follow this shape — it is what
  makes `PeriodicOrphanAuditor` (memory_lifespan_coordinator.py) able to find and audit every
  tracked task uniformly, and what lets shutdown drain them in one place instead of each service
  tracking its own handle.
- **`lifespan()` is the only place startup/shutdown ordering is decided.** `_startup_application`
  returns the constructed `ApplicationContainer`; `_shutdown_with_error_handling` receives that
  same container back — the two must run against the same instance, and shutdown steps are each
  independently try/excepted so a failure in one (e.g. NATS handler teardown) does not prevent
  the connection manager or the rest from shutting down.
- **Game-tick dispatch depends on Protocol definitions (`game_tick_protocols.py`), not concrete
  service imports.** `_TickCombatService`/`_TickConnectionManager` let the tick loop stay
  decoupled from `server/services/`'s concrete classes — a structural-typing boundary, not an
  accident of import order.

## 4. Key design decisions

**[SPEC]**

- **Startup/shutdown metrics are persisted to file, not just logged.**
  `_calculate_metrics_delta` and `_persist_metrics_to_file` (`lifespan.py:56-97`) compute and
  write a JSON delta between
  startup and shutdown metrics — a deliberate operational artifact for diagnosing what a given
  process lifetime actually did, beyond what structured logs alone would show at a glance.
- **Magic-system startup is broken out into its own file** (`lifespan_magic.py`) rather than
  inlined in `_startup_application`, despite `_startup_application` already being the package's
  largest file — a scale decision, not a layering one; magic's prerequisite validation and
  registry construction is substantial enough to warrant isolation.
- **Shutdown is defensive by construction**: `_shutdown_with_error_handling`'s docstring and
  structure (each subsystem's teardown independently guarded) reflect a "best-effort, not
  all-or-nothing" shutdown philosophy — one subsystem failing to tear down cleanly should not
  prevent the others from getting a chance to.

## 5. Constraints

**[SPEC]**

- `lifespan()` must be passed to `FastAPI(lifespan=lifespan)` at construction — it cannot be
  attached after the fact; `factory.py`'s `create_app()` does this in its `FastAPI(...)` call.
- Any code needing the `ApplicationContainer` outside `lifespan.py` itself should go through
  `lifespan_protocols.py`'s typed accessors rather than reaching into `app.state` directly.
- Game-tick processing functions assume they run within a tick loop that has already established
  the current tick via `set_current_tick` — calling `process_combat_tick` etc. outside that
  sequencing is unverified/untested territory.

## 6. Developer guide

**[NOTE]**

- **Adding a new periodic background task**: follow `_log_memory_metrics_periodically`'s shape
  and register it via `container.task_registry.register_task(coro, "lifecycle/<name>",
  "lifecycle")` inside `_startup_application` — see §3.
- **Adding a new startup step**: add it to `_startup_application` (`lifespan_startup.py`) if
  general, or a new dedicated `lifespan_<subsystem>.py` file if substantial enough to warrant
  isolation (the pattern `lifespan_magic.py` sets).
- **Tests**: `server/tests/unit/app/` mirrors this package's module layout.

## 7. Troubleshooting

**[NOTE]**

- **A background task silently stops running**: check whether it was registered through
  `TaskRegistry.register_task` — unregistered tasks are invisible to `PeriodicOrphanAuditor` and
  to shutdown's drain sequence.
- **Startup/shutdown metrics file missing or stale**: check `_persist_metrics_to_file`'s output
  path and whether `_shutdown_with_error_handling` actually completed — a hard process kill
  bypasses it entirely.
- **Game tick logic behaves unexpectedly after a service refactor**: check
  `game_tick_protocols.py`'s `_TickCombatService`/`_TickConnectionManager` — a service satisfying
  the protocol only loosely (structural typing, no explicit `implements`) can drift from what the
  tick loop actually calls without a type error until runtime.

## 8. Related docs

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the sibling reverse-engineered-doc
  family, behavioral rather than structural axis.
- [`CONTAINER_SYSTEM_ARCHITECTURE.md`](../CONTAINER_SYSTEM_ARCHITECTURE.md),
  [ADR-002](../architecture/decisions/ADR-002-application-container-dependency-injection.md) —
  the `ApplicationContainer` this package constructs and drives.
- [`PACKAGE_MIDDLEWARE_DESIGN.md`](PACKAGE_MIDDLEWARE_DESIGN.md) — the HTTP pipeline
  `factory.py` wires into the app it creates.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version, closes #741 |
