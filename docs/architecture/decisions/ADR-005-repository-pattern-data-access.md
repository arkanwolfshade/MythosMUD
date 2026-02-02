# ADR-005: Repository Pattern for Data Access

**Status:** Accepted
**Date:** 2026-02-02

## Context

MythosMUD persists player data, room state, health, inventory, and other game entities. Direct database access from services leads to scattered SQL, duplicated query logic, and difficulty testing business logic in isolation. The system needs a consistent abstraction for data access that supports async operations, atomic updates (e.g., for race conditions), and clear ownership of queries.

## Decision

Adopt the **Repository Pattern** for all data access:

- **AsyncPersistenceLayer** - Facade providing access to repositories
- **Specialized repositories** - PlayerRepository, HealthRepository, RoomRepository, ContainerRepository, ItemRepository, etc.
- **Atomic operations** - Repositories use atomic JSONB updates, transactions, and async/await
- **Clear ownership** - Each repository owns queries for its domain entity

Services depend on AsyncPersistenceLayer or specific repositories via ApplicationContainer. Repositories encapsulate SQL/SQLAlchemy; services never construct raw queries. RoomRepository uses cache-based reads where appropriate; HealthRepository and ExperienceRepository use atomic updates to prevent race conditions.

## Alternatives Considered

1. **Active Record** - Rejected: mixes persistence with domain models; harder to test and optimize
2. **Direct SQLAlchemy in services** - Rejected: duplicates query logic; makes testing difficult
3. **Unit of Work pattern** - Deferred: current repository pattern sufficient; Unit of Work could be added for complex multi-repository transactions
4. **CQRS (Command Query Responsibility Segregation)** - Deferred: read/write separation could optimize queries; not yet required for scale

## Consequences

- **Positive**: Clear separation of data access; testable services via repository mocks; atomic operations prevent race conditions; async-first design
- **Negative**: Some repositories use `asyncio.to_thread()` wrappers (ContainerRepository, ItemRepository) for sync legacy code; full async migration planned
- **Neutral**: Repository interfaces could be more explicit (protocols); current implementation relies on concrete classes

## Related ADRs

- ADR-001: Layered Architecture with Event-Driven Components
- ADR-002: ApplicationContainer for Dependency Injection
- ADR-006: PostgreSQL as Primary Datastore

## References

- [Persistence Repository Architecture](../../PERSISTENCE_REPOSITORY_ARCHITECTURE.md)
- [Container Item Repository Async Migration Plan](../../CONTAINER_ITEM_REPOSITORY_ASYNC_MIGRATION_PLAN.md)
