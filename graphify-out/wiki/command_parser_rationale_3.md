# command parser rationale

> 56 nodes

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
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
- **test_rescue_success()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_with_player_name()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_delta_calculation()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_delta_zero_or_negative()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_apply_lucidity_error()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_event_dispatcher_error()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_metadata_includes_rescuer()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_metadata_includes_location()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (3 shared connections)

## Source Files

- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 116 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*