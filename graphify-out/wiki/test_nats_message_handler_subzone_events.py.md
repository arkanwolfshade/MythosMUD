# test_nats_message_handler_subzone_events.py

> 10 nodes · cohesion 0.20

## Key Concepts

- **test_nats_message_handler_subzone_events.py** (36 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_event_message()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_handle_npc_attacked_event()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_not_subscribed()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **test_unsubscribe_from_subzone_unsubscribe_failure()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Unit tests for NATS message handler subzone and event handling.  Tests subzone s** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone returns False when unsubscription fails.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_npc_attacked_event delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test unsubscribe_from_subzone handles not subscribed case.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`
- **Test _handle_event_message delegates to event handler.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Relationships

- [CombatService](CombatService.md) (2 shared connections)
- [.test_extract_player_name_from_player](test_extract_player_name_from_player.md) (1 shared connections)
- [test_broadcast_combat_ended](test_broadcast_combat_ended.md) (1 shared connections)
- [test_broadcast_player_respawn_personal_message_error](test_broadcast_player_respawn_personal_message_error.md) (1 shared connections)
- [.test_is_valid_name_valid_string](test_is_valid_name_valid_string.md) (1 shared connections)
- [test_broadcast_combat_attack_no_attacker_id](test_broadcast_combat_attack_no_attacker_id.md) (1 shared connections)
- [test_broadcast_player_mortally_wounded_personal_message_error](test_broadcast_player_mortally_wounded_personal_message_error.md) (1 shared connections)
- [.test_is_valid_name_uuid_string](test_is_valid_name_uuid_string.md) (1 shared connections)
- [.test_is_valid_name_not_string](test_is_valid_name_not_string.md) (1 shared connections)
- [test_broadcast_player_died](test_broadcast_player_died.md) (1 shared connections)
- [test_broadcast_combat_error](test_broadcast_combat_error.md) (1 shared connections)
- [test_broadcast_player_respawn](test_broadcast_player_respawn.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_subzone_events.py`

## Audit Trail

- EXTRACTED: 49 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*