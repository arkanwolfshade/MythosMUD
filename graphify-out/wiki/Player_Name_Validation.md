# Player Name Validation

> 279 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **npc_event_handlers.py** (16 connections) — `server/realtime/npc_event_handlers.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **Any** (14 connections)
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **message_builders.py** (9 connections) — `server/realtime/message_builders.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **UUID** (8 connections)
- **._validate_name_not_uuid()** (8 connections) — `server/realtime/player_name_utils.py`
- **.extract_and_validate_player_name()** (8 connections) — `server/realtime/player_name_utils.py`
- **get_room_sync_service()** (8 connections) — `server/services/room_sync_service.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **._try_fallback_name_sources()** (7 connections) — `server/realtime/player_name_utils.py`
- **Any** (6 connections)
- *... and 254 more nodes in this community*

## Relationships

- [item models rationale](item_models_rationale.md) (53 shared connections)
- [NATS Messaging](NATS_Messaging.md) (23 shared connections)
- [player occupant processor](player_occupant_processor.md) (22 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (9 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (9 shared connections)
- [npc event handlers](npc_event_handlers.md) (6 shared connections)
- [time service rationale](time_service_rationale.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [room fixer services](room_fixer_services.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 1006 (97%)
- INFERRED: 34 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*