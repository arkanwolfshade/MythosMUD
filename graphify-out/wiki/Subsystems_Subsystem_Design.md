# Subsystems Subsystem Design

> 12 nodes · cohesion 0.12

## Key Concepts

- **PostgreSQL Procedures Migration - Audit Spreadsheet** (5 connections) — `docs/postgresql_procedures_audit.md`
- **Disconnect Grace Period (linkdead)** (3 connections) — `docs/realtime.md`
- **Gunicorn + Uvicorn Production** (2 connections) — `docs/deployment.md`
- **HTTPS and WSS Requirement** (2 connections) — `docs/deployment.md`
- **postgresql_procedures_audit.md** (2 connections) — `docs/postgresql_procedures_audit.md`
- **Login Grace Period (warded)** (2 connections) — `docs/realtime.md`
- **WebSocket JWT in URL Query String** (2 connections) — `docs/realtime.md`
- **Linkdead Grace Period** (1 connections) — `docs/debugging-mid-run-drops.md`
- **Audit Table** (1 connections) — `docs/postgresql_procedures_audit.md`
- **Domain Grouping Summary** (1 connections) — `docs/postgresql_procedures_audit.md`
- **Existing PostgreSQL Functions (Already in DDL)** (1 connections) — `docs/postgresql_procedures_audit.md`
- **Scope** (1 connections) — `docs/postgresql_procedures_audit.md`

## Relationships

- No strong cross-community connections detected

## Source Files

- `docs/debugging-mid-run-drops.md`
- `docs/deployment.md`
- `docs/postgresql_procedures_audit.md`
- `docs/realtime.md`

## Audit Trail

- EXTRACTED: 17 (74%)
- INFERRED: 6 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*