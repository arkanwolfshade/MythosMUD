# NPC Spawn Validator

> 76 nodes

## Key Concepts

- **EventPublisher** (20 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher.py** (19 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_helpers.py** (9 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.initialize()** (8 connections) — `server/container/bundles/realtime.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **._setup_nats_dependent_services()** (6 connections) — `server/container/bundles/realtime.py`
- **Any** (6 connections)
- **._get_async_persistence()** (6 connections) — `server/realtime/event_publisher.py`
- **._connect_nats()** (5 connections) — `server/container/bundles/realtime.py`
- **.publish_player_entered_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (5 connections) — `server/realtime/event_publisher.py`
- **._require_core_services()** (4 connections) — `server/container/bundles/realtime.py`
- **.__init__()** (4 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init_with_initial_sequence()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **event_publisher()** (3 connections) — `server/tests/unit/realtime/test_event_publisher_helpers.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **mock_nats_service()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **mock_subject_manager()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_event_publisher_init()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_success()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **test_publish_player_entered_event_not_connected()** (2 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- *... and 51 more nodes in this community*

## Relationships

- [WebSocket Code Review](WebSocket_Code_Review.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Inventory Test Support](Inventory_Test_Support.md) (1 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (1 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (1 shared connections)

## Source Files

- `server/container/bundles/realtime.py`
- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher_helpers.py`

## Audit Trail

- EXTRACTED: 197 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*