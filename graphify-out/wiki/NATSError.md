# NATSError

> 102 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **test_message_filtering.py** (37 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **MessageFilteringHelper** (25 connections) — `server/realtime/message_filtering.py`
- **asyncio** (13 connections)
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **.check_player_mute_status()** (6 connections) — `server/realtime/message_filtering.py`
- **.filter_target_players()** (6 connections) — `server/realtime/message_filtering.py`
- **.is_player_in_room()** (6 connections) — `server/realtime/message_filtering.py`
- **TestNATSError** (5 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **message_filtering_helper()** (4 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Any** (4 connections)
- **.compare_canonical_rooms()** (3 connections) — `server/realtime/message_filtering.py`
- **.extract_chat_event_info()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_online_players()** (3 connections) — `server/realtime/message_filtering.py`
- **.get_player_room_from_persistence()** (3 connections) — `server/realtime/message_filtering.py`
- **._get_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.__init__()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver()** (3 connections) — `server/realtime/message_filtering.py`
- **.is_player_muted_by_receiver_with_user_manager()** (3 connections) — `server/realtime/message_filtering.py`
- **.should_apply_mute_check()** (3 connections) — `server/realtime/message_filtering.py`
- **._is_player_muted_by_receiver()** (3 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_get_player_room_from_persistence_not_found()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_in_room_error_returns_false()** (3 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- *... and 77 more nodes in this community*

## Relationships

- [NATSRetryHandler](NATSRetryHandler.md) (16 shared connections)
- [NATSPublishError](NATSPublishError.md) (10 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (9 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (8 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (7 shared connections)
- [NATSService](NATSService.md) (6 shared connections)
- [test_message_filtering_helpers.py](test_message_filtering_helpers.py.md) (3 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [test_nats_message_handler_chat.py](test_nats_message_handler_chat.py.md) (3 shared connections)
- [models/combat.py](models-combat.py.md) (2 shared connections)
- [CombatPersistenceHandler](CombatPersistenceHandler.md) (2 shared connections)

## Source Files

- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_filtering.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 172 (81%)
- INFERRED: 40 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*