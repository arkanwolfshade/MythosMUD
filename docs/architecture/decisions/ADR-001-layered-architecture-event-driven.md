# ADR-001: Layered Architecture with Event-Driven Components

**Version 1.2.0** · MythosMUD · 2026-08-30

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
MythosMUD requires a clear separation of concerns to support maintainability, testability, and scalability. The system must handle HTTP/REST requests, WebSocket real-time communication, domain logic, and data persistence. Without explicit layer boundaries, business logic can become entangled with infrastructure, making changes risky and testing difficult.

## 3. Decision

**[SPEC]**
Adopt a **layered architecture** with **event-driven components**:

1. **Client Layer** (React/TypeScript) - Presentation and user interaction
2. **API Layer** (FastAPI Routers) - HTTP/WebSocket entry points, request routing
3. **Service Layer** - Domain-specific business logic (PlayerService, CombatService, etc.)
4. **Domain Layer** - Models (Player, Room, NPC), EventBus for domain events. Concretely
   `server/models/` + `server/events/`. (`server/domain/` was a separate, unrelated
   hexagonal-architecture scaffold — entities/value_objects/repositories/ports — that was never
   adopted and was removed; see the 2026-08 architecture review, `#757`.)
5. **Persistence Layer** - AsyncPersistenceLayer facade, repositories (Player, Room, etc.)
6. **Database** - PostgreSQL

Outer layers depend on inner layers. Domain events flow through EventBus; services publish domain events that trigger side effects (e.g., WebSocket broadcasts) without direct coupling.

## 4. Alternatives Considered

**[SPEC]**

1. **Monolithic flat structure** - Rejected: leads to spaghetti dependencies and unclear ownership
2. **Microservices** - Rejected for current scale: operational overhead outweighs benefits; single deployment unit sufficient
3. **Hexagonal/Ports-and-Adapters** - Partially adopted: repository pattern and persistence facade align with ports; full hexagonal refactor deferred

## 5. Consequences

**[SPEC]**

- **Positive**: Clear dependency direction (outer → inner); domain layer insulated from infrastructure; easier to test services in isolation
- **Negative**: Some services bypass persistence facade; domain models have occasional persistence concerns; requires discipline to maintain boundaries
- **Neutral**: Layered architecture is well-understood; onboarding developers familiar with Clean Architecture patterns

## 6. Related ADRs

**[SPEC]**

- ADR-002: ApplicationContainer for Dependency Injection
- ADR-003: Dual Event Systems (EventBus + NATS)
- ADR-005: Repository Pattern for Data Access

## 7. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Record provenance (post-hoc authorship) per the 2026-08 audit (#721) |
| 1.2.0 | 2026-08-30 | Clarify Domain Layer names `server/models/` + `server/events/`; note removal of the unrelated `server/domain/` scaffold (#757) |
