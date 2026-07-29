# test nats message handler subzone

> 10 nodes

## Key Concepts

- **test_nats_message_handler_subzone_events.py** (36 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_cleanup_empty_subzone_subscriptions_error()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_player_movement_different_subzone()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_npc_attacked_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Unit tests for NATS message handler subzone and event handling.  Tests subzone s** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone handles errors.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test handle_player_movement handles movement to different subzone.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test cleanup_empty_subzone_subscriptions handles NATSError.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_npc_attacked_event delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Relationships

- [Test handle player movement handles](Test_handle_player_movement_handles.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [Test get players in subzone](Test_get_players_in_subzone.md) (2 shared connections)
- [Test cleanup empty subzone subscriptions](Test_cleanup_empty_subzone_subscriptions.md) (1 shared connections)
- [Test get event handler map](Test_get_event_handler_map.md) (1 shared connections)
- [Test get event subscription count](Test_get_event_subscription_count.md) (1 shared connections)
- [Test get user manager falls](Test_get_user_manager_falls.md) (1 shared connections)
- [Test get user manager returns](Test_get_user_manager_returns.md) (1 shared connections)
- [Test handle combat ended event](Test_handle_combat_ended_event.md) (1 shared connections)
- [Test handle combat started event](Test_handle_combat_started_event.md) (1 shared connections)
- [Test handle event message delegates](Test_handle_event_message_delegates.md) (1 shared connections)
- [Test handle npc died event](Test_handle_npc_died_event.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*