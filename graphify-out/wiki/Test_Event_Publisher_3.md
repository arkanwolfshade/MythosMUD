# Test Event Publisher

> 33 nodes

## Key Concepts

- **test_event_publisher.py** (26 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **asyncio** (13 connections)
- **test_publish_game_tick_uses_metadata_tick_number()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_resolves_names_from_persistence()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_returns_false_when_nats_publish_fails()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_uses_legacy_subjects_without_subject_manager()** (4 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_game_tick_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_nats_error()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_with_metadata()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_event_not_connected()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_left_event_success()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_get_next_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_reset_sequence_number()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Unit tests for event publisher. Tests the EventPublisher class.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test publish_game_tick_event() when NATS is not connected.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test get_next_sequence_number() returns and increments sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Test reset_sequence_number() resets sequence to 0.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Persistence lookup should replace Player_/Room_ fallbacks in event data.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Same persistence name resolution path for player_left.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **Legacy subject strings when subject_manager is unset.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **tick_number from additional_metadata should win over sequence.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 8 more nodes in this community*

## Relationships

- [Event Publisher](Event_Publisher.md) (7 shared connections)
- [Test Event Publisher](Test_Event_Publisher.md) (6 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 54 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*