# ✅ Phase 2 Async Persistence Migration - COMPLETE

> 10 nodes

## Key Concepts

- **test_event_publisher_helpers.py** (10 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_create_event_message()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_get_next_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **test_reset_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Unit tests for event publisher helper functions. Tests the helper functions in…** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test _create_event_message() creates event message.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test get_next_sequence_number() increments sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test reset_sequence_number() resets to 0.** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **Test _get_async_persistence() returns the injected persistence layer (#679:…** (1 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Relationships

- [Shared JSON schemas](Shared_JSON_schemas.md) (2 shared connections)
- [.load_container_from_room_json](load_container_from_room_json.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*