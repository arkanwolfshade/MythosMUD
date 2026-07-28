# Lucidity State Models

> 138 nodes · cohesion 0.03

## Key Concepts

- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **test_lucidity_event_dispatcher.py** (34 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **lucidity_event_dispatcher.py** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **lucidity_trigger_handlers.py** (18 connections) — `server/services/lucidity_trigger_handlers.py`
- **send_lucidity_change_event()** (17 connections) — `server/services/lucidity_event_dispatcher.py`
- **CatatoniaObserverProtocol** (17 connections) — `server/services/lucidity_helpers.py`
- **LucidityChangeEventExtras** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **send_catatonia_event()** (12 connections) — `server/services/lucidity_event_dispatcher.py`
- **_dispatch_player_event()** (11 connections) — `server/services/lucidity_event_dispatcher.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **_lucidity_change_payload_with_liabilities()** (11 connections) — `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **handle_catatonia_transitions()** (10 connections) — `server/services/lucidity_trigger_handlers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- **encode_liabilities()** (8 connections) — `server/services/lucidity_helpers.py`
- **resolve_tier()** (8 connections) — `server/services/lucidity_helpers.py`
- **._apply_delta_to_record()** (8 connections) — `server/services/lucidity_service.py`
- **handle_delirium_and_sanitarium_triggers()** (8 connections) — `server/services/lucidity_trigger_handlers.py`
- **liability_types.py** (8 connections) — `server/utils/liability_types.py`
- **LucidityUpdateResult** (7 connections) — `server/services/lucidity_helpers.py`
- **utc_now()** (7 connections) — `server/services/lucidity_helpers.py`
- **UUID** (6 connections)
- *... and 113 more nodes in this community*

## Relationships

- [Player Death Service Tests](Player_Death_Service_Tests.md) (28 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (14 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (8 shared connections)
- [Services Lucidity Repository](Services_Lucidity_Repository.md) (8 shared connections)
- [Lucidity Event Dispatcher](Lucidity_Event_Dispatcher.md) (8 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (6 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (5 shared connections)
- [Hallucination Trigger Service](Hallucination_Trigger_Service.md) (3 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (2 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (2 shared connections)

## Source Files

- `server/services/lucidity_event_dispatcher.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/lucidity_trigger_handlers.py`
- `server/tests/unit/services/test_lucidity_event_dispatcher.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 570 (97%)
- INFERRED: 18 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*