# Container Injection Audit

**Version 1.0.0** · MythosMUD · 2026-08-25

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
Issue #636 asked for every `ApplicationContainer.get_instance()` call site to be classified against
ADR-002's injection-vs-service-location rule (§3) — sanctioned or debt — and for cycle-free debt to
be migrated to constructor injection. This document is that classification, re-run after #679 closed
the module-level-singleton pathology that produced most of the original debt.

The issue's original estimate was "~31 call sites across 21 modules." That count was gathered before
applying the rule — it is every textual occurrence of `ApplicationContainer.get_instance()`,
including sites in domain entities, mixins, and free functions that the rule never intended to flag.
Applying the rule directly (§2) lands on a much smaller number.

## 2. Method

**[SPEC]**
For each class or function that calls `ApplicationContainer.get_instance()`:

1. Find where it is constructed. `CONTAINER` = a `server/container/bundles/*.py` file's
   `initialize()` builds it directly (e.g. `self.x = X(...)`). Anything else — a module-level global,
   another service's constructor, an entity factory, a bundled subclass — is `OTHER`.
2. `CONTAINER` sites are **debt**: the dependency the site reaches for via `get_instance()` should
   instead be passed in at that same construction site.
3. `OTHER` sites, plus mixins (never instantiated directly) and free functions, are **sanctioned**
   under ADR-002 §3 — the container has no constructor to inject through.
4. For each debt site, the claimed blocking import cycle (if any) was verified empirically: moving
   the import to module level and running `python -c "import <module>"` to see whether it actually
   fails, rather than trusting existing `# noqa ... lazy load avoids container import cycle` comments.

## 3. Classification table

**[SPEC]**

| Site | File:line | Constructed by | Verdict |
| --- | --- | --- | --- |
| `UserManager` (3 sites) | `services/user_manager.py` | `GameBundle` | **Debt — migrated (#679)**: `async_persistence` injected at construction |
| `EventPublisher` | `realtime/event_publisher.py` | `RealtimeBundle` | **Debt — migrated (#679)**: `async_persistence` injected at construction |
| `PlayerDeathService` | `services/player_death_service.py` | `CombatBundle` | **Debt — migrated (#679)**: `async_persistence` injected at construction |
| `HealthService` (2 sites) | `services/health_service.py` | `MonitoringBundle` (was a module-level global via `get_health_service()`, deleted in #679) | **Debt — migrated (#679)**: `async_persistence`/`room_service`/`connection_manager` injected at construction |
| `NPCStartupService` (3 sites) | `services/npc_startup_service.py` | `NPCBundle` (was a module-level global via `get_npc_startup_service()`, deleted in #679) | **Debt — migrated (#679)**: `async_persistence` injected at construction |
| `MemoryLeakMetricsCollector` (2 sites: `collect_event_metrics`, `collect_nats_metrics`) | `monitoring/memory_leak_metrics.py` | `MonitoringBundle` (was 4 independent bare instances, deleted in #679) | **Debt — migrated (#636)**: `event_bus`/`nats_service` injected at construction. Fallback to `get_instance()` retained *only* when neither is supplied, for the untouched `get_monitoring_dashboard()` module-level singleton (out of scope — see §5) |
| `CombatDeathHandler`, `CombatCleanupHandler`, `CombatPersistenceHandler` | `services/combat_{death,cleanup,persistence}_handler.py` | `CombatService.__init__` (`services/combat_service.py:145-148`) — a service, not a bundle | Sanctioned |
| `NPCCombatHandlers`, `NPCCombatRewards` | `services/npc_combat_{handlers,rewards}.py` | `NPCCombatIntegrationService` — a service, not a bundle | Sanctioned |
| `NPCThreadManager` | `npc/threading.py` | Lazy default inside `NPCLifecycleManager.__init__` | Sanctioned |
| `StatsGenerator` | `game/stats_generator.py` | FastAPI dependency (`server/dependencies.py`) and a service-local `self.stats_generator = StatsGenerator()` | Sanctioned |
| `NPCBase` (and subclasses e.g. `PassiveMobNPC`) | `npc/npc_base.py`, `npc/passive_mob_npc.py` | Abstract entity base; subclasses built by entity factories (`npc/spawning_instance_factory.py`), not a bundle | Sanctioned (domain entity, ADR-002 §3's own example) |
| `CombatMessagingBase` | `services/combat_messaging/base.py` | Mixin, never instantiated directly | Sanctioned |
| `MagicServiceHealingMixin` | `game/magic/magic_healing_events.py` | Mixin, never instantiated directly | Sanctioned |
| `resolve_connection_manager` | `realtime/connection_manager_utils.py` | Free function | Sanctioned |
| `_room_from_persistence` | `npc/spawning_request_execution.py` | Free function | Sanctioned |
| `get_container()` | `container/main.py` | The DI accessor itself | Sanctioned (infrastructure) |
| `_ensure_room_cache_before_npc_startup` | `app/lifespan_startup.py` | Startup-sequence helper function | Sanctioned (infrastructure) |
| (docstring reference only) | `async_persistence.py:599,611` | N/A | Sanctioned (infrastructure — the fallback-container comment/lookup for a function with no other way to reach it) |
| `CombatDPSync` | `services/combat_hp_sync.py` | **Zero production callers** — only `test_combat_service_modules.py:287` constructs it | **Dead code, not debt.** Belongs to #630, not #636 |

## 4. Cycle verification

**[SPEC]**
None of the six debt classes above were blocked by a real import cycle: `async_persistence`,
`event_bus`, `room_service`, `connection_manager`, and `nats_service` are all already available on
`ApplicationContainer` by the time the constructing bundle runs (bundle initialization order:
`CoreBundle` → `RealtimeBundle` → `GameBundle` → `MonitoringBundle` → `CombatBundle` → `NPCBundle`).
All six were migrated in full; no site was left cycle-blocked by this audit.

## 5. Out of scope

**[SPEC]**

- **`CombatDPSync`** (§3) — dead code, tracked under #630, not migrated here.
- **The `get_monitoring_dashboard()` module-level singleton** (`monitoring/monitoring_dashboard.py`)
  and its own nested singletons (`get_performance_monitor()`, `get_exception_tracker()`,
  `get_log_aggregator()`) — a parallel, still-live instance of the same
  module-level-singleton pathology #679 closed for `UserManager`/`HealthService`/etc., discovered
  during #679's work but not fixed there to keep that PR scoped to its four named services. Not
  addressed by #636 either. Worth its own follow-up issue if picked up.
- **Breaking import cycles** — moot for this audit (§4), but remains the general blocker pattern for
  any future debt site that genuinely needs it.
- **#635's `GameBundle` → `TimeBundle` move** — decoupled from this work; it constructs none of the
  classes audited here.

## 6. Related ADRs

**[SPEC]**

- ADR-002: ApplicationContainer for Dependency Injection (the rule this document classifies against)

## 7. References

**[SPEC]**

- Issue: #636
- Prerequisite: #679 (module-level singleton removal)
- `docs/DATABASE_ACCESS_PATTERNS.md` (corrected in the same change to stop teaching
  `ApplicationContainer.get_instance()` as the default pattern)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-25 | Initial audit, post-#679 |
