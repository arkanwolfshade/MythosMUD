# Monitoring (2)

> 8 nodes

## Key Concepts

- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **webhook-receiver.py** (3 connections) — `monitoring/webhook-receiver.py`
- **health()** (2 connections) — `monitoring/webhook-receiver.py`
- **get_alerts()** (2 connections) — `monitoring/webhook-receiver.py`
- **Request** (1 connections)
- **Receive and log alert webhooks** (1 connections) — `monitoring/webhook-receiver.py`
- **Health check endpoint** (1 connections) — `monitoring/webhook-receiver.py`
- **Get recent alerts (for testing)** (1 connections) — `monitoring/webhook-receiver.py`

## Relationships

- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)
- [Server Persistence](Server_Persistence.md) (1 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`

## Audit Trail

- EXTRACTED: 14 (88%)
- INFERRED: 2 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*