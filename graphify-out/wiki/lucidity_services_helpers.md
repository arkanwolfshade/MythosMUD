# lucidity services helpers

> 150 nodes

## Key Concepts

- **LucidityService** (88 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (78 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (52 connections) — `server/services/lucidity_service.py`
- **lucidity_helpers.py** (24 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_service.py** (24 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **lucidity_trigger_handlers.py** (19 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_trigger_handlers.py** (17 connections) — `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- **UUID** (14 connections)
- **handle_catatonia_transitions()** (13 connections) — `server/services/lucidity_trigger_handlers.py`
- **encode_liabilities()** (12 connections) — `server/services/lucidity_helpers.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **LucidityUpdateResult** (10 connections) — `server/services/lucidity_helpers.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **UUID** (10 connections)
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **handle_delirium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **handle_sanitarium_trigger()** (9 connections) — `server/services/lucidity_trigger_handlers.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **test_lucidity_adjustment_round_trip()** (7 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- *... and 125 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (30 shared connections)
- [combat services persistence](combat_services_persistence.md) (17 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (16 shared connections)
- [aggro threat services](aggro_threat_services.md) (15 shared connections)
- [command helpers functions](command_helpers_functions.md) (11 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (11 shared connections)
- [rescue service services](rescue_service_services.md) (9 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (8 shared connections)
- [services service phantom](services_service_phantom.md) (8 shared connections)
- [combat models rationale](combat_models_rationale.md) (7 shared connections)
- [container schemas containers](container_schemas_containers.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_lucidity_trigger_handlers.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 700 (91%)
- INFERRED: 72 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*