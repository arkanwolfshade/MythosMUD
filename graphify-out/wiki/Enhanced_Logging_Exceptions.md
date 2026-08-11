# Enhanced Logging Exceptions

> 192 nodes

## Key Concepts

- **LucidityService** (77 connections) — `server/services/lucidity_service.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **LucidityRepository** (14 connections) — `server/services/lucidity_repository.py`
- **UUID** (14 connections)
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **test_lucidity_round_trip.py** (10 connections) — `server/tests/integration/test_lucidity_round_trip.py`
- **LucidityUpdateResult** (9 connections) — `server/services/lucidity_helpers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **._calculate_max_lcd()** (8 connections) — `server/services/lucidity_service.py`
- *... and 167 more nodes in this community*

## Relationships

- [Message Queue Cleanup](Message_Queue_Cleanup.md) (21 shared connections)
- [Alias Storage Layer](Alias_Storage_Layer.md) (14 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (14 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (10 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (9 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (8 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (7 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (6 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (4 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (3 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_repository.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/integration/test_lucidity_round_trip.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 794 (95%)
- INFERRED: 42 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*