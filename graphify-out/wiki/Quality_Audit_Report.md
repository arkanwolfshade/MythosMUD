# Quality Audit Report

> 3 nodes

## Key Concepts

- **webhook()** (5 connections) — `monitoring/webhook-receiver.py`
- **Request** (1 connections)
- **Receive and log alert webhooks** (1 connections) — `monitoring/webhook-receiver.py`

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)

## Source Files

- `monitoring/webhook-receiver.py`

## Audit Trail

- EXTRACTED: 5 (71%)
- INFERRED: 2 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*