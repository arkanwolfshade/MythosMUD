# Message Queue Cleanup

> 94 nodes

## Key Concepts

- **PlayerLucidity** (74 connections) — `server/models/lucidity.py`
- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service.py** (19 connections) — `server/services/rescue_service.py`
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **.rescue()** (9 connections) — `server/services/rescue_service.py`
- **.respawn_player_from_delirium_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **Any** (7 connections)
- **factory()** (7 connections) — `server/tests/unit/utils/test_command_factories.py`
- **_load_rescue_participants()** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (5 connections) — `server/models/lucidity.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **._apply_rescue_adjustment()** (5 connections) — `server/services/rescue_service.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **.__init__()** (4 connections) — `server/models/lucidity.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **_dispatch_rescue_events()** (4 connections) — `server/services/rescue_service.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **UUID** (3 connections)
- **_rescue_success_payload()** (3 connections) — `server/services/rescue_service.py`
- **async_session_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 69 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (21 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (11 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (6 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (6 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (4 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (4 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (3 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (3 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (3 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`
- `server/models/lucidity.py`
- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 291 (88%)
- INFERRED: 39 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*