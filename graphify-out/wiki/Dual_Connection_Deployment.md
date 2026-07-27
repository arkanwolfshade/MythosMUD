# Dual Connection Deployment

> 2 nodes · cohesion 0.12

## Key Concepts

- **Path** (9 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **Path** (7 connections) — `server/api/metrics.py`

## Relationships

- [NATS Metrics API](NATS_Metrics_API.md) (1 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/tests/unit/api/test_metrics_endpoints.py`

## Audit Trail

- EXTRACTED: 9 (56%)
- INFERRED: 7 (44%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*