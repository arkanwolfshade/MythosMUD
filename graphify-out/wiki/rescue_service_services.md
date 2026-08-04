# rescue service services

> 72 nodes

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service.py** (16 connections) — `server/services/rescue_service.py`
- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **.rescue()** (7 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **Any** (4 connections)
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **UUID** (2 connections)
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **async_session_factory()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_event_dispatcher()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_target()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_rescuer_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_target_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_different_rooms()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_lucidity_record_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_not_catatonic()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 47 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (9 shared connections)
- [command helpers functions](command_helpers_functions.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/services/rescue_service.py`
- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 175 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*