# ADR-002: ApplicationContainer for Dependency Injection

**Version 1.3.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-02-02
**Provenance:** Post-hoc — authored after the systems it describes. See [README §2](README.md).

## 2. Context

**[NOTE]**
Before the ApplicationContainer refactor, MythosMUD used 19+ global singletons for services such as PlayerService, RoomService, ConnectionManager, and EventBus. Global singletons cause tight coupling, make unit testing difficult (services cannot be mocked or replaced), and obscure the dependency graph. Test setup required mutating global state, leading to fragile, order-dependent tests.

## 3. Decision

**[SPEC]**
Implement a single **ApplicationContainer** class in the `server/container/` package (orchestrator in `main.py`, domain bundles in `bundles/`) that:

- Manages all service lifecycle and dependency resolution
- Provides thread-safe initialization with explicit phases
- Exposes services as attributes (e.g., `container.player_service`)
- Replaces all global singleton access with container injection
- Ensures dependency inversion: services depend on abstractions, container wires concrete implementations

The container is initialized once at application startup and passed (or accessed via a single accessor) where services are needed.

**[SPEC] Injection-vs-service-location rule (v1.1.0, #636):** `ApplicationContainer.get_instance()` is a
service locator, not injection — the decision above ("replaces all global singleton access with container
injection") means it is a fallback for genuine construction-order problems, not a substitute for passing a
dependency in. The rule that governs which is which:

- **Injection is required** for any type the container itself constructs (a bundle's `initialize()` builds
  it, e.g. `self.user_manager = UserManager(...)` in `GameBundle`). Its dependencies must be passed at that
  same construction site. Reaching back into `ApplicationContainer.get_instance()` from inside such a type is
  debt, not a design choice.
- **Service location is permitted** for types the container does not construct: domain entities (e.g.
  `NPCBase` and its subclasses, built by `NPCSpawningRequestExecution`/entity factories, not a bundle),
  mixins (never instantiated directly), free functions, and module-level utilities. These have no
  constructor a bundle could inject through.
- A cycle that forces a lazy `get_instance()` call inside a container-constructed type is a **known,
  temporary exception**, not a precedent — resolving the cycle (not routing around it again) is the
  intended fix. See `docs/CONTAINER_INJECTION_AUDIT.md` for the current measured debt and which sites are
  cycle-blocked.

## 4. Alternatives Considered

**[SPEC]**

1. **Continue with global singletons** - Rejected: testing and maintainability suffer
2. **Third-party DI framework (e.g., dependency-injector, injector)** - Rejected: ApplicationContainer provides sufficient control; avoids extra dependency; custom phases (e.g., warm room cache before starting real-time) are explicit
3. **Domain-specific sub-containers** - Implemented as internal bundles with flattened attributes; see [APPLICATION_CONTAINER_ANALYSIS.md](../../APPLICATION_CONTAINER_ANALYSIS.md)

## 5. Consequences

**[SPEC]**

- **Positive**: Eliminated global singletons; explicit dependency graph; testable services via mock injection; proper lifecycle management
- **Negative**: Some circular dependencies handled with TYPE_CHECKING; orchestration lives in `main.py`, domain logic in bundles under `server/container/bundles/`. A 2026-08 audit (#636) found ~20 remaining `ApplicationContainer.get_instance()` call sites across the codebase; applying the rule above, all were sanctioned (entities/mixins/free-functions/service-constructed helpers) except one dead-code site (`CombatDPSync`, #630) and a handful already closed by #679/#636 (`UserManager`, `EventPublisher`, `PlayerDeathService`, `HealthService`, `NPCStartupService`, `MemoryLeakMetricsCollector`) — see `docs/CONTAINER_INJECTION_AUDIT.md` for the full, per-site table.
- **Neutral**: Initialization order is explicit but complex; document initialization phases for maintainers

## 6. Related ADRs

**[SPEC]**

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-005: Repository Pattern for Data Access

## 7. References

**[SPEC]**

- [ApplicationContainer Analysis](../../APPLICATION_CONTAINER_ANALYSIS.md)
- [Bounded Contexts and Service Boundaries](../../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
- [Container Injection Audit](../../CONTAINER_INJECTION_AUDIT.md) (#636)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-25 | Added the injection-vs-service-location rule (§3) and the measured debt count (§5); rule was implicit in the original decision but never written down, so #636's classification work had nothing to classify against |
| 1.2.0 | 2026-08-28 | Record provenance (post-hoc authorship); resolve the bare `APPLICATION_CONTAINER_ANALYSIS.md` reference to a link, correcting its target to `docs/archive/` where the file now lives (#721) |
| 1.3.0 | 2026-08-28 | Repoint the `APPLICATION_CONTAINER_ANALYSIS.md` link at `docs/`: the file was restored there per audit ruling C4 — four live documents cite it as authoritative, so it is not archival (#722) |
