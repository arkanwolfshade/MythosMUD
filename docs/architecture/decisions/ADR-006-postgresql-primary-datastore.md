# ADR-006: PostgreSQL as Primary Datastore

**Status:** Accepted
**Date:** 2026-02-02

## Context

MythosMUD requires a relational datastore for players, rooms, inventory, combat state, and other structured game data. Historically, the project used SQLite for simplicity. As the system evolved, requirements for concurrent access, connection pooling, horizontal scalability, and robustness in multi-player scenarios grew. SQLite's limitations (single-writer, file-based, no native connection pooling across processes) became constraints.

## Decision

Use **PostgreSQL** as the primary datastore:

- All persistent game data stored in PostgreSQL
- SQLAlchemy async ORM for data access
- Connection pooling via SQLAlchemy engine
- No SQLite; migration from SQLite to PostgreSQL completed
- Alembic for schema migrations

Player data, room state, health, experience, inventory, and related entities reside in PostgreSQL. Repositories use async SQLAlchemy sessions.

## Alternatives Considered

1. **SQLite** - Rejected: single-writer limitation; file-based; unsuitable for multi-instance deployment
2. **MySQL/MariaDB** - Rejected: PostgreSQL chosen for JSON/JSONB support, robustness, and team familiarity
3. **MongoDB/NoSQL** - Rejected: relational model fits game entities (players, rooms, inventory); ACID transactions important for combat and economy
4. **Hybrid (PostgreSQL + Redis for cache)** - Partial: RoomRepository uses in-memory cache; Redis for distributed cache deferred

## Consequences

- **Positive**: ACID transactions; connection pooling; supports horizontal scaling (read replicas); JSONB for flexible schemas (e.g., health stats); mature ecosystem
- **Negative**: Operational overhead (PostgreSQL server); migration from SQLite required effort
- **Neutral**: Database hosted externally or in same deployment; environment variables for connection string

## Related ADRs

- ADR-005: Repository Pattern for Data Access
- ADR-007: FastAPI with Async/Await

## References

- [Database Access Patterns](../../DATABASE_ACCESS_PATTERNS.md)
- [Database Pool Configuration](../../DATABASE_POOL_CONFIGURATION.md)
