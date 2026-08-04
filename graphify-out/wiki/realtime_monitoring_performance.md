# realtime monitoring performance

> 106 nodes

## Key Concepts

- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **message_builders.py** (10 connections) — `server/realtime/message_builders.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (6 connections)
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- *... and 81 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (30 shared connections)
- [schedule services service](schedule_services_service.md) (5 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (5 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (5 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (4 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [player occupant processor](player_occupant_processor.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [schemas player rationale](schemas_player_rationale.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [npc event handlers](npc_event_handlers.md) (2 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/test_message_builders.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 371 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*