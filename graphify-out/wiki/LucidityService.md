# LucidityService

> 255 nodes

## Key Concepts

- **LucidityService** (79 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (69 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_lucidity_service.py** (25 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (20 connections) — `server/models/lucidity.py`
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **lucidity_repository.py** (13 connections) — `server/services/lucidity_repository.py`
- **asyncio** (13 connections)
- **LucidityUpdateResult** (12 connections) — `server/services/lucidity_helpers.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **_scalar_result()** (11 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_lucidity_round_trip.py** (11 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **asyncio** (11 connections)
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- *... and 230 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (29 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (26 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (17 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (15 shared connections)
- [.state](state.md) (12 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (9 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (7 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (7 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (7 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 581 (84%)
- INFERRED: 108 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*