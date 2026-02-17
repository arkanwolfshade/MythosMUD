# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) documenting major architectural decisions for MythosMUD. Each ADR captures the context, decision, rationale, and consequences of a significant architectural choice.

## Format

Each ADR follows this structure:

- **Status**: Proposed | Accepted | Deprecated | Superseded
- **Context**: The situation and forces driving the decision
- **Decision**: The chosen approach
- **Alternatives Considered**: Other options evaluated
- **Consequences**: Positive, negative, and neutral outcomes

## Index

| ADR                                                              | Title                                             | Status   | Date       |
| ---------------------------------------------------------------- | ------------------------------------------------- | -------- | ---------- |
| [ADR-001](ADR-001-layered-architecture-event-driven.md)          | Layered Architecture with Event-Driven Components | Accepted | 2026-02-02 |
| [ADR-002](ADR-002-application-container-dependency-injection.md) | ApplicationContainer for Dependency Injection     | Accepted | 2026-02-02 |
| [ADR-003](ADR-003-dual-event-systems-eventbus-nats.md)           | Dual Event Systems (EventBus + NATS)              | Accepted | 2026-02-02 |
| [ADR-004](ADR-004-websocket-only-realtime.md)                    | WebSocket-Only Real-Time Architecture             | Accepted | 2026-02-02 |
| [ADR-005](ADR-005-repository-pattern-data-access.md)             | Repository Pattern for Data Access                | Accepted | 2026-02-02 |
| [ADR-006](ADR-006-postgresql-primary-datastore.md)               | PostgreSQL as Primary Datastore                   | Accepted | 2026-02-02 |
| [ADR-007](ADR-007-fastapi-async-await.md)                        | FastAPI with Async/Await                          | Accepted | 2026-02-02 |
| [ADR-008](ADR-008-react-typescript-client.md)                    | React 18+ with TypeScript for Client              | Accepted | 2026-02-02 |
| [ADR-009](ADR-009-instanced-rooms.md)                            | Instanced Rooms for Tutorial and Future Content   | Accepted | 2026-02-17 |

## Related Documentation

- [Architecture Review Plan](../../.cursor/plans/architecture_review_plan_7bcbc812.plan.md)
- [Bounded Contexts and Service Boundaries](../../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
- [ApplicationContainer Analysis](../../APPLICATION_CONTAINER_ANALYSIS.md)
- [Event Ownership Matrix](../../EVENT_OWNERSHIP_MATRIX.md)
- [Real-Time Architecture](../../REAL_TIME_ARCHITECTURE.md)
