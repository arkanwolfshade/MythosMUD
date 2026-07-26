# test_rescue_service.py

> 58 nodes · cohesion 0.04

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
- **factory()** (7 connections) — `server/tests/unit/utils/test_command_factories.py`
- **async_session_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **lucidity_service_factory()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **rescue_service()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_lucidity_record()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_no_persistence()** (3 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_event_dispatcher()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_lucidity_service()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_rescuer()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **sample_target()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_apply_lucidity_error()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_delta_calculation()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_delta_zero_or_negative()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_different_rooms()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_dispatches_events_for_both_players()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_event_dispatcher_error()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_handles_uuid_objects()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_handles_uuid_strings()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_lucidity_record_not_found()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_metadata_includes_location()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_metadata_includes_rescuer()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- **test_rescue_not_catatonic()** (2 connections) — `server/tests/unit/services/test_rescue_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [PlayerLucidity](PlayerLucidity.md) (6 shared connections)
- [lucidity.py](lucidity.py.md) (1 shared connections)
- [LRUCache](LRUCache.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_command_factories.py](test_command_factories.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_rescue_service.py`
- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 120 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*