# ADR-007: FastAPI with Async/Await

**Status:** Accepted
**Date:** 2026-02-02

## Context

MythosMUD's backend must handle concurrent HTTP and WebSocket connections, database I/O, NATS messaging, and game logic. Blocking I/O under load would limit throughput and responsiveness. The Python ecosystem offers sync (Flask, Django) and async (FastAPI, Starlette) frameworks. Async enables non-blocking I/O and scales better for I/O-bound workloads like a MUD server.

## Decision

Use **FastAPI** with **async/await** throughout the backend:

- FastAPI for HTTP and WebSocket routing
- Async route handlers and dependency injection
- SQLAlchemy async engine for database access
- Async NATS client for messaging
- Pydantic for request/response validation and serialization

All I/O-bound operations use `async def` and `await`. Synchronous code is wrapped with `asyncio.to_thread()` only where necessary (e.g., legacy sync libraries during migration).

## Alternatives Considered

1. **Flask (sync)** - Rejected: blocking I/O; lower concurrency under load
2. **Django + ASGI** - Rejected: FastAPI lighter; better fit for API + WebSocket focus; Pydantic native
3. **Starlette alone** - Rejected: FastAPI adds validation, OpenAPI, dependency injection; preferred over bare Starlette
4. **Tornado / aiohttp** - Rejected: FastAPI provides modern DX, automatic docs, Pydantic integration

## Consequences

- **Positive**: High concurrency for I/O-bound work; native async/await; automatic OpenAPI docs; Pydantic validation; WebSocket support
- **Negative**: Sync code must be migrated or run in thread pool; blocking calls in async context can stall event loop
- **Neutral**: Team must follow async patterns; avoid sync libraries in hot paths

## Related ADRs

- ADR-005: Repository Pattern for Data Access
- ADR-006: PostgreSQL as Primary Datastore
- ADR-004: WebSocket-Only Real-Time Architecture

## References

- [Async Persistence Migration Plan](../../ASYNC_PERSISTENCE_MIGRATION_PLAN.md)
- [SQLAlchemy Async Best Practices](../../SQLALCHEMY_ASYNC_BEST_PRACTICES.md)
