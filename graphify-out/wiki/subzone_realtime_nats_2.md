# subzone realtime nats

> 10 nodes

## Key Concepts

- **test_nats_message_handler_subzone_events.py** (36 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_not_subscribed()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_unsubscribe_failure()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_npc_attacked_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_event_message()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Unit tests for NATS message handler subzone and event handling.  Tests subzone s** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone handles not subscribed case.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone returns False when unsubscription fails.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_npc_attacked_event delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_event_message delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Relationships

- [npc behavior engine](npc_behavior_engine.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [commands communication say](commands_communication_say.md) (1 shared connections)
- [test_cleanup_empty_subzone_subscriptions_error](test_cleanup_empty_subzone_subscriptions_error.md) (1 shared connections)
- [test_get_event_handler_map](test_get_event_handler_map.md) (1 shared connections)
- [test_get_event_subscription_count](test_get_event_subscription_count.md) (1 shared connections)
- [test_get_players_in_subzone](test_get_players_in_subzone.md) (1 shared connections)
- [test_get_players_in_subzone_empty](test_get_players_in_subzone_empty.md) (1 shared connections)
- [test_get_user_manager_fallback](test_get_user_manager_fallback.md) (1 shared connections)
- [test_get_user_manager_injected](test_get_user_manager_injected.md) (1 shared connections)
- [test_handle_combat_ended_event](test_handle_combat_ended_event.md) (1 shared connections)
- [test_handle_combat_started_event](test_handle_combat_started_event.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*