# ADR-005: Repository Pattern for Data Access

**Version 1.1.0** · MythosMUD · 2026-08-28

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
MythosMUD persists player data, room state, health, inventory, and other game entities. Direct database access from services leads to scattered SQL, duplicated query logic, and difficulty testing business logic in isolation. The system needs a consistent abstraction for data access that supports async operations, atomic updates (e.g., for race conditions), and clear ownership of queries.

## 3. Decision

**[SPEC]**
Adopt the **Repository Pattern** for all data access:

- **AsyncPersistenceLayer** - Facade providing access to repositories
- **Specialized repositories** - PlayerRepository, HealthRepository, RoomRepository, ContainerRepository, ItemRepository, etc.
- **Atomic operations** - Repositories use atomic JSONB updates, transactions, and async/await
- **Clear ownership** - Each repository owns queries for its domain entity

Services depend on AsyncPersistenceLayer or specific repositories via ApplicationContainer. Repositories encapsulate SQL/SQLAlchemy; services never construct raw queries. RoomRepository uses cache-based reads where appropriate; HealthRepository and ExperienceRepository use atomic updates to prevent race conditions.

## 4. Alternatives Considered

**[SPEC]**

1. **Active Record** - Rejected: mixes persistence with domain models; harder to test and optimize
2. **Direct SQLAlchemy in services** - Rejected: duplicates query logic; makes testing difficult
3. **Unit of Work pattern** - Deferred: current repository pattern sufficient; Unit of Work could be added for complex multi-repository transactions
4. **CQRS (Command Query Responsibility Segregation)** - Deferred: read/write separation could optimize queries; not yet required for scale

## 5. Consequences

**[SPEC]**

- **Positive**: Clear separation of data access; testable services via repository mocks; atomic operations prevent race conditions; async-first design
- **Negative**: Some repositories use `asyncio.to_thread()` wrappers (ContainerRepository, ItemRepository) for sync legacy code; full async migration planned
- **Neutral**: Repository interfaces could be more explicit (protocols); current implementation relies on concrete classes

## 6. Related ADRs

**[SPEC]**

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-002: ApplicationContainer for Dependency Injection
- ADR-006: PostgreSQL as Primary Datastore

## 7. References

**[SPEC]**

- [Persistence Repository Architecture](../../PERSISTENCE_REPOSITORY_ARCHITECTURE.md)
- [Container Item Repository Async Migration Plan](../../archive/CONTAINER_ITEM_REPOSITORY_ASYNC_MIGRATION_PLAN.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 1.1.0 | 2026-08-28 | Record provenance (post-hoc authorship); fix broken migration-plan link, now in `docs/archive/` (#721) |
