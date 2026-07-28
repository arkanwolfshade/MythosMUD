# Architecture Api Openapi

> 3 nodes · cohesion 0.67

## Key Concepts

- **test_logger()** (4 connections) — `server/tests/conftest.py`
- **BoundLogger** (1 connections)
- **Provide a logger for tests.** (1 connections) — `server/tests/conftest.py`

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)
- [Common Troubleshooting Guide](Common_Troubleshooting_Guide.md) (1 shared connections)

## Source Files

- `server/tests/conftest.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*