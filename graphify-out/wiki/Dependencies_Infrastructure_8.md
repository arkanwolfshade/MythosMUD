# Dependencies Infrastructure

> 8 nodes · cohesion 0.29

## Key Concepts

- **get_passive_lucidity_flux_service()** (8 connections) — `server/dependencies.py`
- **TestGetPassiveLucidityFluxService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_passive_lucidity_flux_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_passive_lucidity_flux_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_passive_lucidity_flux_service dependency function.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_passive_lucidity_flux_service returns service when present.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_passive_lucidity_flux_service raises RuntimeError when service is None.** (1 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get a PassiveLucidityFluxService instance with dependency injection.      Args:** (1 connections) — `server/dependencies.py`

## Relationships

- [[Dependency Injection Tests]] (4 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
