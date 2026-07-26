# webhook

> 8 nodes · cohesion 0.25

## Key Concepts

- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **webhook-receiver.py** (3 connections) — `monitoring/webhook-receiver.py`
- **get_alerts()** (2 connections) — `monitoring/webhook-receiver.py`
- **health()** (2 connections) — `monitoring/webhook-receiver.py`
- **Request** (1 connections)
- **Receive and log alert webhooks** (1 connections) — `monitoring/webhook-receiver.py`
- **Health check endpoint** (1 connections) — `monitoring/webhook-receiver.py`
- **Get recent alerts (for testing)** (1 connections) — `monitoring/webhook-receiver.py`

## Relationships

- [error_types.py](error_types.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`

## Audit Trail

- EXTRACTED: 14 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*