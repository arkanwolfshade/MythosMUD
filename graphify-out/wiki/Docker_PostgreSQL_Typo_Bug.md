# Docker PostgreSQL Typo Bug

> 2 nodes

## Key Concepts

- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **Initialize metrics collection.** (1 connections) — `server/services/nats_subject_manager/metrics.py`

## Relationships

- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (1 shared connections)
- [Manager Services Nats](Manager_Services_Nats.md) (1 shared connections)

## Source Files

- `server/services/nats_subject_manager/metrics.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*