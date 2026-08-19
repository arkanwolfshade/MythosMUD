# ADR-002: ApplicationContainer for Dependency Injection

**Version 1.1.0** · MythosMUD · 2026-07-30

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
**Provenance:** Recorded by the 2026-08 design/implementation audit. This ADR set was authored after the
systems it describes: the structural architecture documents it draws on predate it by months, and
`DOCUMENTATION_AUDIT.md` records that the design documentation was reverse-engineered with code treated as
the source of truth. Read it as a description of a decision already in force, not a record made at decision
time.

## 2. Context

**[NOTE]**
Before the ApplicationContainer refactor, MythosMUD used 19+ global singletons for services such as PlayerService, RoomService, ConnectionManager, and EventBus. Global singletons cause tight coupling, make unit testing difficult (services cannot be mocked or replaced), and obscure the dependency graph. Test setup required mutating global state, leading to fragile, order-dependent tests.

## 3. Decision

**[SPEC]**
Implement a single **ApplicationContainer** class in the `server/container/` package (orchestrator in `main.py`, domain bundles in `bundles/`) that:

- Manages all service lifecycle and dependency resolution
- Provides thread-safe initialization with explicit phases
- Exposes services as attributes (e.g., `container.player_service`)
- Replaces global singleton access with container injection **for services the container constructs**

**Access patterns (clarified 2026-08-19).** Two are sanctioned, and the distinction is whether the
container builds the thing:

- **Injection (required)** for anything the container constructs. If a bundle builds it, the bundle
  passes it what it needs. A container-constructed service reaching back into the container at call time
  is **debt**, not design.
- **Service location (permitted, bounded)** via `ApplicationContainer.get_instance()` for types the
  container does **not** construct - domain entities and models such as `NPCBase`, and module-level
  utility functions. These have no constructor the container can inject through, so a call-time lookup is
  the only option available to them.

The deciding question for any new call site: *does the container construct this?* If yes, inject. If no,
`get_instance()` is acceptable.

**Root cause worth naming.** Most current `get_instance()` sites are written as function-local lazy
imports carrying comments such as `# Reason: lazy load avoids container import cycle`. The pattern is
therefore largely a **symptom of import cycles**, not a deliberate architectural choice. Reducing those
cycles is what would let the debt population migrate to injection; see also the `TYPE_CHECKING`
consequence in section 5.

- Ensures dependency inversion: services depend on abstractions, container wires concrete implementations

The container is initialized once at application startup and passed (or accessed via a single accessor) where services are needed.

## 4. Alternatives Considered

**[SPEC]**

1. **Continue with global singletons** - Rejected: testing and maintainability suffer
2. **Third-party DI framework (e.g., dependency-injector, injector)** - Rejected: ApplicationContainer provides sufficient control; avoids extra dependency; custom phases (e.g., warm room cache before starting real-time) are explicit
3. **Domain-specific sub-containers** - Implemented as internal bundles with flattened attributes; see [APPLICATION_CONTAINER_ANALYSIS.md](../../APPLICATION_CONTAINER_ANALYSIS.md)

## 5. Consequences

**[SPEC]**

- **Positive**: Eliminated global singletons; explicit dependency graph; testable services via mock injection; proper lifecycle management
- **Negative**: Some circular dependencies handled with TYPE_CHECKING; orchestration lives in `main.py`, domain logic in bundles under `server/container/bundles/`
- **Negative (measured 2026-08-19)**: `ApplicationContainer.get_instance()` is used as a runtime service
  locator at roughly 31 call sites across 21 modules. Some are legitimate under the rule above; others are
  container-constructed services that could take the dependency at construction - `UserManager`, for
  example, is built as `UserManager(data_dir=...)` and then reaches back to the container for persistence.
  That subset is tracked as debt, not sanctioned.
- **Neutral**: Initialization order is explicit but complex; document initialization phases for maintainers

## 6. Related ADRs

**[SPEC]**

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-005: Repository Pattern for Data Access

## 7. References

**[SPEC]**

- [ApplicationContainer Analysis](../../APPLICATION_CONTAINER_ANALYSIS.md)
- [Bounded Contexts and Service Boundaries](../../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-19 | Clarify sanctioned access patterns: injection for container-constructed services, bounded service location for entities; record the locator debt |
