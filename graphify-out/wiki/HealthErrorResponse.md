# HealthErrorResponse

> 8 nodes

## Key Concepts

- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- **test_health_error_response_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_health_error_response_frozen()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_health_error_response_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_health.py`
- **Error response for health check failures.** (1 connections) — `server/models/health.py`
- **Test HealthErrorResponse can be created with required fields.** (1 connections) — `server/tests/unit/models/test_health.py`
- **Test HealthErrorResponse rejects unknown fields.** (1 connections) — `server/tests/unit/models/test_health.py`
- **Test HealthErrorResponse is frozen (immutable).** (1 connections) — `server/tests/unit/models/test_health.py`

## Relationships

- [HealthStatus](HealthStatus.md) (6 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [models/player.py](models-player.py.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/tests/unit/models/test_health.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*