# follow game service

> 63 nodes

## Key Concepts

- **EventHandler** (34 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (22 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **.publish()** (3 connections) — `server/realtime/event_handlers.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.handle_player_entered_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_player_left_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_game_tick_event()** (2 connections) — `server/realtime/event_handlers.py`
- **test_as_event_data_dict_normalizes_mapping()** (2 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- *... and 38 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (14 shared connections)
- [Room Broadcast](Room_Broadcast.md) (7 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (3 shared connections)
- [command parser helpers](command_parser_helpers.md) (2 shared connections)
- [game chat service](game_chat_service.md) (1 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 195 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*