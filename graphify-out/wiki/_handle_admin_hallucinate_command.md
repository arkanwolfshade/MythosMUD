# _handle_admin_hallucinate_command

> 57 nodes · cohesion 0.06

## Key Concepts

- **EventHandler** (37 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.handle_event_message()** (6 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **test_handle_combat_ended_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_combat_started_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_event_message_dispatches_handler()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_event_message_invalid_skips()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_game_tick_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_npc_attacked_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- *... and 32 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (11 shared connections)
- [Room](Room.md) (3 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [deque](deque.md) (2 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)
- [WebSocketManager](WebSocketManager.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 101 (86%)
- INFERRED: 16 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*