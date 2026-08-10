# Message Queue Cleanup

> 80 nodes

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service.py** (19 connections) — `server/services/rescue_service.py`
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **.rescue()** (9 connections) — `server/services/rescue_service.py`
- **Any** (7 connections)
- **factory()** (7 connections) — `server/tests/unit/utils/test_command_factories.py`
- **_load_rescue_participants()** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **._apply_rescue_adjustment()** (5 connections) — `server/services/rescue_service.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **_dispatch_rescue_events()** (4 connections) — `server/services/rescue_service.py`
- **UUID** (3 connections)
- **_rescue_success_payload()** (3 connections) — `server/services/rescue_service.py`
- **async_session_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **EventDispatcher** (2 connections)
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_event_dispatcher()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 55 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Follow Service Tests](Follow_Service_Tests.md) (4 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (1 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [NATS Message Handler Tests](NATS_Message_Handler_Tests.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 210 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*