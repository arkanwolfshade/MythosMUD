# LucidityService

> 198 nodes

## Key Concepts

- **LucidityService** (84 connections) — `server/services/lucidity_service.py`
- **lucidity_service.py** (54 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_helpers.py** (27 connections) — `server/services/lucidity_helpers.py`
- **asyncio** (24 connections)
- **CatatoniaObserverProtocol** (21 connections) — `server/services/lucidity_helpers.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **test_lucidity_trigger_handlers.py** (17 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **UUID** (12 connections)
- **test_lucidity_round_trip.py** (12 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_adjustment_round_trip()** (11 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (10 connections) — `server/services/lucidity_event_dispatcher.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **UUID** (10 connections)
- *... and 173 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (56 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [Player](Player.md) (9 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (8 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (8 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (8 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (7 shared connections)
- [admin_setstat_command.py](admin_setstat_command.py.md) (6 shared connections)
- [debrief_command.py](debrief_command.py.md) (6 shared connections)
- [rescue_service.py](rescue_service.py.md) (6 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (4 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 507 (91%)
- INFERRED: 48 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*