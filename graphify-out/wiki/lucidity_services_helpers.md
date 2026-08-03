# lucidity services helpers

> 201 nodes

## Key Concepts

- **LucidityService** (78 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (73 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **lucidity.py** (33 connections) — `server/models/lucidity.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityExposureState** (23 connections) — `server/models/lucidity.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **LucidityCooldown** (22 connections) — `server/models/lucidity.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **UUID** (14 connections)
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **lucidity_repository.py** (11 connections) — `server/services/lucidity_repository.py`
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **UUID** (9 connections)
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- *... and 176 more nodes in this community*

## Relationships

- [Async Query Helpers](Async_Query_Helpers.md) (38 shared connections)
- [world models rationale](world_models_rationale.md) (34 shared connections)
- [commands rescue rationale](commands_rescue_rationale.md) (21 shared connections)
- [lucidity event services](lucidity_event_services.md) (15 shared connections)
- [lucidity active service](lucidity_active_service.md) (13 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (7 shared connections)
- [services service phantom](services_service_phantom.md) (7 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (6 shared connections)
- [models player rationale](models_player_rationale.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [command validation commands](command_validation_commands.md) (5 shared connections)
- [services passive lucidity](services_passive_lucidity.md) (5 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 858 (91%)
- INFERRED: 82 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*