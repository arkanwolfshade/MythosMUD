# Migration Testing Guide

> 2 nodes

## Key Concepts

- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **Clean up large data structures to prevent memory bloat.          Args:** (1 connections) — `server/realtime/message_queue.py`

## Relationships

- [Architecture Decisions Adr](Architecture_Decisions_Adr.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/realtime/message_queue.py`

## Audit Trail

- EXTRACTED: 3 (75%)
- INFERRED: 1 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*