# NPCEventHandler

> 83 nodes

## Key Concepts

- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
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
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- *... and 58 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (13 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [world](world.md) (5 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (4 shared connections)
- [.get instance()](get_instance%28%29.md) (4 shared connections)
- [get current tick()](get_current_tick%28%29.md) (3 shared connections)
- [test npc event handlers](test_npc_event_handlers.md) (2 shared connections)
- [combat taunt](combat_taunt.md) (1 shared connections)
- [CorpseNotFoundError](CorpseNotFoundError.md) (1 shared connections)
- [connection statistics](connection_statistics.md) (1 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (1 shared connections)
- [circuit breaker](circuit_breaker.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 262 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*