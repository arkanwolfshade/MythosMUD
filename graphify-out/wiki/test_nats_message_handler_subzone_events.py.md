# test_nats_message_handler_subzone_events.py

> 20 nodes

## Key Concepts

- **test_nats_message_handler_subzone_events.py** (36 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_get_event_handler_map()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_get_event_subscription_count()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_get_players_in_subzone()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_get_players_in_subzone_empty()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_get_user_manager_fallback()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_get_user_manager_injected()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_is_event_subscription_active()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_track_player_subzone_subscription_different_subzone()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_validate_event_message()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Unit tests for NATS message handler subzone and event handling. Tests subzone…** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test get_event_subscription_count returns count.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test is_event_subscription_active checks subscription.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _get_user_manager returns injected manager.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _get_user_manager falls back to global manager.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _get_event_handler_map delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _validate_event_message delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test track_player_subzone_subscription handles player moving to different…** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test get_players_in_subzone returns players in subzone.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test get_players_in_subzone returns empty list for empty subzone.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Relationships

- [asyncio](asyncio.md) (8 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_subscribe_to_subzone_no_subject_manager](test_subscribe_to_subzone_no_subject_manager.md) (1 shared connections)
- [test_subscribe_to_event_subjects_partial_failure](test_subscribe_to_event_subjects_partial_failure.md) (1 shared connections)
- [test_unsubscribe_from_subzone_decrease_count](test_unsubscribe_from_subzone_decrease_count.md) (1 shared connections)
- [test_handle_player_movement_old_subzone_none](test_handle_player_movement_old_subzone_none.md) (1 shared connections)
- [test_handle_player_movement_new_subzone_none](test_handle_player_movement_new_subzone_none.md) (1 shared connections)
- [test_handle_player_movement_error](test_handle_player_movement_error.md) (1 shared connections)
- [test_subscribe_to_subzone_subscribe_failure](test_subscribe_to_subzone_subscribe_failure.md) (1 shared connections)
- [test_unsubscribe_from_subzone_unsubscribe_failure](test_unsubscribe_from_subzone_unsubscribe_failure.md) (1 shared connections)
- [test_handle_combat_started_event](test_handle_combat_started_event.md) (1 shared connections)
- [test_handle_combat_ended_event](test_handle_combat_ended_event.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*