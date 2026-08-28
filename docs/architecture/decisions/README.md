# Architecture Decision Records (ADRs)

**Version 1.1.0** · MythosMUD · 2026-08-28

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
This directory contains Architecture Decision Records (ADRs) documenting major architectural decisions for MythosMUD. Each ADR captures the context, decision, rationale, and consequences of a significant architectural choice.

## 2. Format

**[SPEC]**
Each ADR follows this structure:

- **Status**: Proposed | Accepted | Deprecated | Superseded
- **Context**: The situation and forces driving the decision
- **Decision**: The chosen approach
- **Alternatives Considered**: Other options evaluated
- **Consequences**: Positive, negative, and neutral outcomes
- **Provenance** *(ADR-001–017 only)*: Whether the ADR was written to describe a system already in
  place ("post-hoc") or ahead of implementation ("contemporaneous"). Recorded by the 2026-08
  design/implementation audit, which found that ADR-001–017's structural source documents predate
  them by months and that `DOCUMENTATION_AUDIT.md` records the design documentation as
  reverse-engineered with code treated as the source of truth — so a post-hoc ADR "conforming" to
  its own code is weak evidence, while a contemporaneous one deviating is a real finding
  (`AUDIT_COVERAGE_BOUNDARY_2026-08.md` §4.1 weights `CONFORMS` verdicts on exactly this
  distinction). **Absence of this field on ADR-018 and later means the audit never assessed that
  ADR — not that it is contemporaneous.**

## 3. Index

**[SPEC]**

| ADR                                                              | Title                                                | Status   | Date       |
| ---------------------------------------------------------------- | ---------------------------------------------------- | -------- | ---------- |
| [ADR-001](ADR-001-layered-architecture-event-driven.md)          | Layered Architecture with Event-Driven Components    | Accepted | 2026-02-02 |
| [ADR-002](ADR-002-application-container-dependency-injection.md) | ApplicationContainer for Dependency Injection        | Accepted | 2026-02-02 |
| [ADR-003](ADR-003-dual-event-systems-eventbus-nats.md)           | Dual Event Systems (EventBus + NATS)                 | Accepted | 2026-02-02 |
| [ADR-004](ADR-004-websocket-only-realtime.md)                    | WebSocket-Only Real-Time Architecture                | Accepted | 2026-02-02 |
| [ADR-005](ADR-005-repository-pattern-data-access.md)             | Repository Pattern for Data Access                   | Accepted | 2026-02-02 |
| [ADR-006](ADR-006-postgresql-primary-datastore.md)               | PostgreSQL as Primary Datastore                      | Accepted | 2026-02-02 |
| [ADR-007](ADR-007-fastapi-async-await.md)                        | FastAPI with Async/Await                             | Accepted | 2026-02-02 |
| [ADR-008](ADR-008-react-typescript-client.md)                    | React 18+ with TypeScript for Client                 | Accepted | 2026-02-02 |
| [ADR-009](ADR-009-instanced-rooms.md)                            | Instanced Rooms for Tutorial and Future Content      | Accepted | 2026-02-17 |
| [ADR-010](ADR-010-quest-subsystem.md)                            | Quest Subsystem Architecture                         | Accepted | 2026-02-19 |
| [ADR-011](ADR-011-xstate-frontend-fsm.md)                        | XState for Frontend Connection State Machine         | Accepted | 2025-10-11 |
| [ADR-012](ADR-012-python-statemachine-backend.md)                | python-statemachine for Backend Connection FSM       | Accepted | 2025-10-11 |
| [ADR-013](ADR-013-pydantic-configuration.md)                     | Pydantic BaseSettings for Configuration              | Accepted | 2025-10-11 |
| [ADR-014](ADR-014-nats-error-boundaries.md)                      | Circuit Breaker + DLQ for NATS Error Boundaries      | Accepted | 2025-10-11 |
| [ADR-015](ADR-015-postgresql-procedures-migration.md)            | PostgreSQL Procedures and Functions for Data Access  | Accepted | 2026-02-26 |
| [ADR-016](ADR-016-aggro-threat-management.md)                    | Aggro and Threat Management System                   | Accepted | 2026-02-26 |
| [ADR-017](ADR-017-ast-console-pruning-client-build.md)           | AST-Based Console Pruning in Client Production Build | Proposed | 2026-03-25 |
| [ADR-018](ADR-018-new-game-session-replacement.md)               | New Game Session vs Grace Reconnect                  | Accepted | 2026-08-14 |
| [ADR-019](ADR-019-player-effects-system.md)                      | Player Effects System                                | Accepted | 2026-08-19 |
| [ADR-020](ADR-020-websocket-authentication-and-csrf.md)          | WebSocket Authentication and CSRF                    | Accepted | 2026-08-19 |
| [ADR-021](ADR-021-character-display-name-validation.md)          | Character Display Name Validation                    | Accepted | 2026-08-23 |
| [ADR-022](ADR-022-ui-v2-client-transition.md)                    | ui-v2 Client Transition and Legacy Retirement         | Accepted | 2026-08-26 |

## 4. Related Documentation

**[SPEC]**

- [Architecture Review Plan](../../.cursor/plans/architecture_review_plan_7bcbc812.plan.md)
- [Bounded Contexts and Service Boundaries](../../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md)
- [ApplicationContainer Analysis](../../archive/APPLICATION_CONTAINER_ANALYSIS.md)
- [Event Ownership Matrix](../../EVENT_OWNERSHIP_MATRIX.md)
- [Real-Time Architecture](../../REAL_TIME_ARCHITECTURE.md)
- [Aggro and Threat System Design](../aggro-threat-system.md)

## 5. Changelog

**[SPEC]**

| Version | Date       | Change                                                                       |
| ------- | ---------- | ----------------------------------------------------------------------------- |
| 1.0.0   | 2026-07-30 | Initial HADS structural conversion                                            |
| 1.1.0   | 2026-08-28 | Document the Provenance field; fix broken `APPLICATION_CONTAINER_ANALYSIS.md` link (ADR-001–017 backfill, #721) |
