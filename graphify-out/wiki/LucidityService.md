# LucidityService

> 396 nodes

## Key Concepts

- **LucidityService** (81 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (71 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **test_lucidity_event_dispatcher.py** (35 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_rescue_service.py** (33 connections) — `server/tests/unit/services/test_rescue_service.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_service.py** (27 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (24 connections)
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **rescue_service.py** (20 connections) — `server/services/rescue_service.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **asyncio** (17 connections)
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **asyncio** (15 connections)
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **lucidity_repository.py** (13 connections) — `server/services/lucidity_repository.py`
- *... and 371 more nodes in this community*

## Relationships

- [Player](Player.md) (27 shared connections)
- [.state](state.md) (20 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [test_lucidity_models.py](test_lucidity_models.py.md) (19 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (15 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (13 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (12 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (10 shared connections)
- [coerce_int](coerce_int.md) (9 shared connections)
- [debrief_command.py](debrief_command.py.md) (8 shared connections)
- [pytest.md](pytest.md.md) (8 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (7 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/player_respawn_service.py`
- `server/services/rescue_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 926 (90%)
- INFERRED: 98 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*