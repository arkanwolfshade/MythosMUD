# webhook

> 4 nodes

## Key Concepts

- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **post** (1 connections)
- **Request** (1 connections)
- **Receive and log alert webhooks** (1 connections) — `monitoring/webhook-receiver.py`

## Relationships

- [get_logger](get_logger.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`

## Audit Trail

- EXTRACTED: 4 (80%)
- INFERRED: 1 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*