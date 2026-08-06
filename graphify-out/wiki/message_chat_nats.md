# message chat nats

> 10 nodes

## Key Concepts

- **test_nats_message_handler_chat.py** (40 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_validate_chat_message_fields_missing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_convert_ids_to_uuids()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_apply_dampening_and_send_message_no_original_content()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **test_get_player_lucidity_tier_exception_in_processing()** (2 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Unit tests for NATS message handler chat and messaging.  Tests chat field extrac** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _validate_chat_message_fields raises error when fields missing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _convert_ids_to_uuids converts IDs.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _apply_dampening_and_send_message handles missing original_content.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`
- **Test _get_player_lucidity_tier handles exceptions during processing.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Relationships

- [npc behavior engine](npc_behavior_engine.md) (3 shared connections)
- [commands communication say](commands_communication_say.md) (1 shared connections)
- [game chat service](game_chat_service.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)
- [test_get_combat_death_message](test_get_combat_death_message.md) (1 shared connections)
- [test_handle_player_movement_error](test_handle_player_movement_error.md) (1 shared connections)
- [test_get_combat_result_message_success_with_damage](test_get_combat_result_message_success_with_damage.md) (1 shared connections)
- [test_validate_combat_command_suspicious_patterns_with_mock](test_validate_combat_command_suspicious_patterns_with_mock.md) (1 shared connections)
- [test_build_chat_event_includes_speaker_kind](test_build_chat_event_includes_speaker_kind.md) (1 shared connections)
- [test_validate_can_attack_target_no_party_service_allows](test_validate_can_attack_target_no_party_service_allows.md) (1 shared connections)
- [test_handle_player_movement_old_subzone_none](test_handle_player_movement_old_subzone_none.md) (1 shared connections)
- [test_get_combat_status_message_not_in_combat](test_get_combat_status_message_not_in_combat.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler_chat.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*