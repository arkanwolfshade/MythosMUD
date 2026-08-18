# server tests unit services test

> 5 nodes

## Key Concepts

- **health_service()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **fixture** (2 connections)
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Create a HealthService instance.** (1 connections) — `server/tests/unit/services/test_health_service.py`

## Relationships

- [server models health](server_models_health.md) (2 shared connections)
- [healthstatus](healthstatus.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 6 (86%)
- INFERRED: 1 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*