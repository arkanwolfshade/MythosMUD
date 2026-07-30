# ADR-006: PostgreSQL as Primary Datastore
**Version 1.0.0** · MythosMUD · 2026-07-30

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

## 2. Context

**[NOTE]**
MythosMUD requires a relational datastore for players, rooms, inventory, combat state, and other structured game data. Historically, the project used SQLite for simplicity. As the system evolved, requirements for concurrent access, connection pooling, horizontal scalability, and robustness in multi-player scenarios grew. SQLite's limitations (single-writer, file-based, no native connection pooling across processes) became constraints.

## 3. Decision

**[SPEC]**
Use **PostgreSQL** as the primary datastore:

- All persistent game data stored in PostgreSQL
- SQLAlchemy async ORM for data access
- Connection pooling via SQLAlchemy engine
- No SQLite; migration from SQLite to PostgreSQL completed
- Alembic for schema migrations

Player data, room state, health, experience, inventory, and related entities reside in PostgreSQL. Repositories use async SQLAlchemy sessions.

## 4. Alternatives Considered

**[SPEC]**
1. **SQLite** - Rejected: single-writer limitation; file-based; unsuitable for multi-instance deployment
2. **MySQL/MariaDB** - Rejected: PostgreSQL chosen for JSON/JSONB support, robustness, and team familiarity
3. **MongoDB/NoSQL** - Rejected: relational model fits game entities (players, rooms, inventory); ACID transactions important for combat and economy
4. **Hybrid (PostgreSQL + Redis for cache)** - Partial: RoomRepository uses in-memory cache; Redis for distributed cache deferred

## 5. Consequences

**[SPEC]**
- **Positive**: ACID transactions; connection pooling; supports horizontal scaling (read replicas); JSONB for flexible schemas (e.g., health stats); mature ecosystem
- **Negative**: Operational overhead (PostgreSQL server); migration from SQLite required effort
- **Neutral**: Database hosted externally or in same deployment; environment variables for connection string

## 6. Related ADRs

**[SPEC]**
- ADR-005: Repository Pattern for Data Access
- ADR-007: FastAPI with Async/Await

## 7. References

**[SPEC]**
- [Database Access Patterns](../../DATABASE_ACCESS_PATTERNS.md)
- [Database Pool Configuration](../../DATABASE_POOL_CONFIGURATION.md)

## 8. Changelog

**[SPEC]**
| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
