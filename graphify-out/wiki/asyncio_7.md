# asyncio

> 21 nodes

## Key Concepts

- **asyncio** (13 connections)
- **test_publish_game_tick_uses_metadata_tick_number()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_returns_false_when_nats_publish_fails()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_uses_legacy_subjects_without_subject_manager()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_nats_error()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_game_tick_event() when NATS is not connected.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Persistence lookup should replace Player_/Room_ fallbacks in event data.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Legacy subject strings when subject_manager is unset.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **tick_number from additional_metadata should win over sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **publish() returning False should surface as False from EventPublisher.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_entered_event() successfully publishes.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_entered_event() when NATS is not connected.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_left_event() successfully publishes.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_game_tick_event() successfully publishes.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_player_entered_event() handles NATS errors.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [test_event_publisher.py](test_event_publisher.py.md) (13 shared connections)
- [EventPublisher](EventPublisher.md) (4 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 33 (89%)
- INFERRED: 4 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*