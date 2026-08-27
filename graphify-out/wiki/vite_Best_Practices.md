# vite Best Practices

> 20 nodes

## Key Concepts

- **DatabaseComponent** (9 connections)
- **HealthComponents** (9 connections)
- **ConnectionsComponent** (8 connections)
- **ServerComponent** (8 connections)
- **test_determine_overall_status_degraded()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_healthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_determine_overall_status_unhealthy()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_no_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_generate_alerts_with_alerts()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **test_get_health_status_version_fallback()** (6 connections) — `server/tests/unit/services/test_health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **Get database component health status (async version with actual validation).** (1 connections) — `server/services/health_service.py`
- **Generate alerts based on component health.** (1 connections) — `server/services/health_service.py`
- **Test generate_alerts returns empty list when all healthy.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Test generate_alerts returns alerts when components are unhealthy.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Test determine_overall_status returns healthy when all components healthy.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Test determine_overall_status returns degraded when any component degraded.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Test determine_overall_status returns unhealthy when any component unhealthy.** (1 connections) — `server/tests/unit/services/test_health_service.py`
- **Test get_health_status handles version lookup failure.** (1 connections) — `server/tests/unit/services/test_health_service.py`

## Relationships

- [NPCStartupService](NPCStartupService.md) (9 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (7 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (3 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 26 (49%)
- INFERRED: 27 (51%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*