# LucidityService

> 180 nodes

## Key Concepts

- **LucidityService** (86 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (76 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (56 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (28 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (27 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **CatatoniaObserverProtocol** (24 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_trigger_handlers.py** (18 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **LucidityUpdateResult** (17 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (16 connections)
- **handle_catatonia_transitions()** (14 connections) — `server/services/lucidity_trigger_handlers.py`
- **._prepare_sanitarium_respawn()** (13 connections) — `server/services/player_respawn_service.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_adjustment_round_trip()** (12 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **UUID** (12 connections)
- **test_lucidity_round_trip.py** (12 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **._apply_sanitarium_liability_update()** (11 connections) — `server/services/player_respawn_service.py`
- **UUID** (11 connections)
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **resolve_tier()** (9 connections) — `server/services/lucidity_helpers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- *... and 155 more nodes in this community*

## Relationships

- [lucidity.py](lucidity.py.md) (22 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (17 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (17 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (17 shared connections)
- [LucidityRepository](LucidityRepository.md) (12 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (10 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (10 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (9 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [debrief_command.py](debrief_command.py.md) (6 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/services/player_respawn_service.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 496 (87%)
- INFERRED: 73 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*