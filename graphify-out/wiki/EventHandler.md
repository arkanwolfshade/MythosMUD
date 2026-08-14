# EventHandler

> 17 nodes

## Key Concepts

- **EventHandler** (34 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_combat_ended_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_combat_started_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_event_message_dispatches_handler()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_event_message_invalid_skips()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_game_tick_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_npc_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_npc_died_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_player_entered_missing_room_id()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_player_left_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_validate_event_message()** (2 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **Handler for NATS event messages.** (1 connections) — `server/realtime/event_handlers.py`
- **Tests for NATS EventHandler combat-related broadcasts (WebSocket shape).** (1 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **NATS uses EventMessageSchema; clients expect flat npc_id, current_dp in…** (1 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`

## Relationships

- [_send_combat_participant_updates](_send_combat_participant_updates.md) (7 shared connections)
- [event_handlers.py](event_handlers.py.md) (5 shared connections)
- [_as_event_data_dict](_as_event_data_dict.md) (5 shared connections)
- [.handle_event_message](handle_event_message.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [.handle_player_entered_event](handle_player_entered_event.md) (1 shared connections)
- [.handle_player_left_event](handle_player_left_event.md) (1 shared connections)
- [.handle_game_tick_event](handle_game_tick_event.md) (1 shared connections)
- [lifecycle_manager.py](lifecycle_manager.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 63 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*