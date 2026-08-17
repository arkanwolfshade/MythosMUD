# server realtime envelope rationale 33

> 17 nodes

## Key Concepts

- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **test_utc_now_z_format()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_utc_now_z_is_utc()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_uuid()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_json_dumps()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **.default()** (2 connections) — `server/realtime/envelope.py`
- **test_get_next_global_sequence_thread_safe()** (2 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Custom JSON encoder that handles UUID objects.** (1 connections) — `server/realtime/envelope.py`
- **Return current UTC time in ISO 8601 format with 'Z' suffix.** (1 connections) — `server/realtime/envelope.py`
- **Unit tests for envelope utilities. Tests the build_event function, UUIDEncoder,…** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test _get_next_global_sequence() is thread-safe.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test UUIDEncoder handles UUID objects.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test UUIDEncoder works with json.dumps().** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test utc_now_z() returns ISO 8601 format with Z suffix.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`
- **Test utc_now_z() returns UTC time.** (1 connections) — `server/tests/unit/realtime/test_envelope.py`

## Relationships

- [server realtime envelope build event](server_realtime_envelope_build_event.md) (17 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [object](object.md) (2 shared connections)
- [server middleware comprehensive logging](server_middleware_comprehensive_logging.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [playercombatservice](playercombatservice.md) (1 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 42 (89%)
- INFERRED: 5 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*