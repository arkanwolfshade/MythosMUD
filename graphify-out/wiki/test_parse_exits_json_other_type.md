# test_parse_exits_json_other_type

> 152 nodes

## Key Concepts

- **LucidityService** (77 connections) — `server/services/lucidity_service.py`
- **PlayerLucidity** (74 connections) — `server/models/lucidity.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
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
- **LucidityUpdateResult** (9 connections) — `server/services/lucidity_helpers.py`
- **UUID** (9 connections)
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- *... and 127 more nodes in this community*

## Relationships

- [Combat Messaging Tests](Combat_Messaging_Tests.md) (29 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (17 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (15 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (14 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (11 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (10 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (7 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (6 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (6 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (6 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/active_lucidity_service.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`

## Audit Trail

- EXTRACTED: 687 (90%)
- INFERRED: 80 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*