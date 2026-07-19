# Architecture Decisions Adr

> 26 nodes · cohesion 0.08

## Key Concepts

- **ADR-014: Circuit Breaker + Dead Letter Queue for NATS Error Boundaries** (11 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Implementation Details** (6 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Consequences** (4 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Considered Options** (4 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Operational Considerations** (4 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Integration** (2 connections) — `.cursor/agents/bug-investigator.md`
- **ADR-014-nats-error-boundaries.md** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **1. Retry Handler with Exponential Backoff** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **2. Circuit Breaker (Three-State FSM)** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **3. Dead Letter Queue (File-Based)** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **4. Metrics Collector (Thread-Safe)** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Alerting** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Context and Problem Statement** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Decision Drivers** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Decision Outcome** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **DLQ Management** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Monitoring** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Negative** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Neutral** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Option 1: Circuit Breaker + DLQ + Retry (Custom Implementation)** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Option 2: resilience4j + External Message Queue** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Option 3: Python retry libraries (tenacity, backoff)** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Positive** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **References** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- **Related ADRs** (1 connections) — `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`
- *... and 1 more nodes in this community*

## Relationships

- [[Cursor Bug Agents]] (1 shared connections)

## Source Files

- `.cursor/agents/bug-investigator.md`
- `docs/architecture/decisions/ADR-014-nats-error-boundaries.md`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
