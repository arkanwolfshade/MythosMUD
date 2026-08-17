# server realtime event handler py

> 88 nodes

## Key Concepts

- **RealTimeEventHandler** (35 connections) — `server/realtime/event_handler.py`
- **NPCEventHandler** (26 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (20 connections) — `server/realtime/message_builders.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._create_player_entered_message()** (4 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (4 connections) — `server/realtime/event_handler.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- *... and 63 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (9 shared connections)
- [server events event types playerleftroom](server_events_event_types_playerleftroom.md) (7 shared connections)
- [server events event bus](server_events_event_bus.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server events event types playerenteredroom](server_events_event_types_playerenteredroom.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [moduletype](moduletype.md) (2 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (2 shared connections)
- [server realtime npc occupant processor](server_realtime_npc_occupant_processor.md) (2 shared connections)
- [chatlogger](chatlogger.md) (2 shared connections)
- [server realtime player name utils](server_realtime_player_name_utils.md) (2 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`

## Audit Trail

- EXTRACTED: 169 (91%)
- INFERRED: 17 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*