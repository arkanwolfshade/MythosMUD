# test_command_registry_consistency.py

> 134 nodes · cohesion 0.03

## Key Concepts

- **lucidity.py** (37 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityCooldown** (27 connections) — `server/models/lucidity.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **test_lucidity_repository.py** (24 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **LucidityAdjustmentLog** (20 connections) — `server/models/lucidity.py`
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **lucidity_repository.py** (12 connections) — `server/services/lucidity_repository.py`
- **asyncio** (11 connections)
- **_scalar_result()** (11 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **UUID** (9 connections)
- **_utc_now()** (8 connections) — `server/models/lucidity.py`
- **_utc_now()** (7 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_utils.py** (7 connections) — `server/tests/unit/models/test_lucidity_utils.py`
- **test_get_cooldown()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_get_exposure_state()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_get_or_create_player_lucidity_existing()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_get_player_lucidity_returns_record()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_increment_exposure_state_existing()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_set_cooldown_update()** (7 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
- **.increment_exposure_state()** (6 connections) — `server/services/lucidity_repository.py`
- **.set_cooldown()** (6 connections) — `server/services/lucidity_repository.py`
- **test_get_or_create_player_lucidity_creates()** (6 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- *... and 109 more nodes in this community*

## Relationships

- [PopulationStats](PopulationStats.md) (30 shared connections)
- [.get_memory_status_report](get_memory_status_report.md) (6 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (5 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (4 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (4 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [scripts](scripts.md) (2 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (2 shared connections)
- [FollowService](FollowService.md) (2 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_repository.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/models/test_lucidity_utils.py`
- `server/tests/unit/services/test_lucidity_repository.py`

## Audit Trail

- EXTRACTED: 284 (90%)
- INFERRED: 30 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*