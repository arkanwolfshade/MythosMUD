# combat npc mixin

> 45 nodes

## Key Concepts

- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_json_dumps()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_is_utc()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_basic()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_room_id()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_player_id_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_player_id_string()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_sequence_number()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_uses_global_sequence_when_no_manager()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_empty_data()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_no_data_parameter()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_timestamp_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_all_parameters()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_optional_parameters_none()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **.default()** (2 connections) — `server/realtime/envelope.py`
- **test_get_next_global_sequence_thread_safe()** (2 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Custom JSON encoder that handles UUID objects.** (1 connections) — `server/realtime/envelope.py`
- **Unit tests for envelope utilities.  Tests the build_event function, UUIDEncoder,** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 20 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (21 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (1 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 115 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*