# LucidityService

> 371 nodes

## Key Concepts

- **LucidityService** (79 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (69 connections) — `server/models/lucidity.py`
- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **lucidity.py** (35 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **asyncio** (27 connections)
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **test_lucidity_service.py** (25 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **LucidityAdjustmentLog** (20 connections) — `server/models/lucidity.py`
- **rescue_service.py** (20 connections) — `server/services/rescue_service.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **PositionState** (17 connections) — `server/models/game.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **int_coercion.py** (17 connections) — `server/utils/int_coercion.py`
- **_MockAsyncSession** (16 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **player_respawn_wrapper.py** (16 connections) — `server/game/player_respawn_wrapper.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **lucidity_repository.py** (13 connections) — `server/services/lucidity_repository.py`
- **asyncio** (13 connections)
- *... and 346 more nodes in this community*

## Relationships

- [command_service.py](command_service.py.md) (28 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [models/player.py](models-player.py.md) (22 shared connections)
- [Player](Player.md) (21 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (21 shared connections)
- [DatabaseError](DatabaseError.md) (16 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (16 shared connections)
- [test_lucidity_trigger_handlers.py](test_lucidity_trigger_handlers.py.md) (13 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (9 shared connections)
- [coerce_int](coerce_int.md) (9 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (7 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (7 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/game/player_respawn_wrapper.py`
- `server/models/game.py`
- `server/models/lucidity.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/player_respawn_service.py`
- `server/services/rescue_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_repository.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/int_coercion.py`

## Audit Trail

- EXTRACTED: 878 (89%)
- INFERRED: 110 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*