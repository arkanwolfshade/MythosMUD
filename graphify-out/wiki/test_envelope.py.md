# test_envelope.py

> 19 nodes

## Key Concepts

- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_json_dumps()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **.default()** (2 connections) — `server/realtime/envelope.py`
- **test_get_next_global_sequence_thread_safe()** (2 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Custom JSON encoder that handles UUID objects.** (1 connections) — `server/realtime/envelope.py`
- **Unit tests for envelope utilities. Tests the build_event function, UUIDEncoder,…** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test build_event() uses connection_manager for sequence.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test build_event() prioritizes explicit sequence_number over connection_manager.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test _get_next_global_sequence() is thread-safe.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test build_event() produces JSON-serializable output.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test UUIDEncoder handles UUID objects.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test UUIDEncoder falls back to default for non-UUID types.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test UUIDEncoder works with json.dumps().** (1 connections) — `server/tests/unit/realtime/test_envelope.py`

## Relationships

- [build_event](build_event.md) (20 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [ComprehensiveLoggingMiddleware](ComprehensiveLoggingMiddleware.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 42 (84%)
- INFERRED: 8 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*