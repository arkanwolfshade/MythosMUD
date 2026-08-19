# ADR-007: FastAPI with Async/Await

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
**Provenance:** Recorded by the 2026-08 design/implementation audit. This ADR set was authored after the
systems it describes: the structural architecture documents it draws on predate it by months, and
`DOCUMENTATION_AUDIT.md` records that the design documentation was reverse-engineered with code treated as
the source of truth. Read it as a description of a decision already in force, not a record made at decision
time.

## 2. Context

**[NOTE]**
MythosMUD's backend must handle concurrent HTTP and WebSocket connections, database I/O, NATS messaging, and game logic. Blocking I/O under load would limit throughput and responsiveness. The Python ecosystem offers sync (Flask, Django) and async (FastAPI, Starlette) frameworks. Async enables non-blocking I/O and scales better for I/O-bound workloads like a MUD server.

## 3. Decision

**[SPEC]**
Use **FastAPI** with **async/await** throughout the backend:

- FastAPI for HTTP and WebSocket routing
- Async route handlers and dependency injection
- SQLAlchemy async engine for database access
- Async NATS client for messaging
- Pydantic for request/response validation and serialization

All I/O-bound operations use `async def` and `await`. Synchronous code is wrapped with `asyncio.to_thread()` only where necessary (e.g., legacy sync libraries during migration).

## 4. Alternatives Considered

**[SPEC]**

1. **Flask (sync)** - Rejected: blocking I/O; lower concurrency under load
2. **Django + ASGI** - Rejected: FastAPI lighter; better fit for API + WebSocket focus; Pydantic native
3. **Starlette alone** - Rejected: FastAPI adds validation, OpenAPI, dependency injection; preferred over bare Starlette
4. **Tornado / aiohttp** - Rejected: FastAPI provides modern DX, automatic docs, Pydantic integration

## 5. Consequences

**[SPEC]**

- **Positive**: High concurrency for I/O-bound work; native async/await; automatic OpenAPI docs; Pydantic validation; WebSocket support
- **Negative**: Sync code must be migrated or run in thread pool; blocking calls in async context can stall event loop
- **Neutral**: Team must follow async patterns; avoid sync libraries in hot paths

## 6. Related ADRs

**[SPEC]**

- ADR-005: Repository Pattern for Data Access
- ADR-006: PostgreSQL as Primary Datastore
- ADR-004: WebSocket-Only Real-Time Architecture

## 7. References

**[SPEC]**

- [Async Persistence Migration Plan](../../archive/ASYNC_PERSISTENCE_MIGRATION_PLAN.md)
- [SQLAlchemy Async Best Practices](../../SQLALCHEMY_ASYNC_BEST_PRACTICES.md)

## 8. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
