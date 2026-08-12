# Test Optimization Insights

> 30 nodes

## Key Concepts

- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.handle_player_entered_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_player_left_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_game_tick_event()** (2 connections) — `server/realtime/event_handlers.py`
- **Normalize NATS event_data payload to a string-keyed dict.** (1 connections) — `server/realtime/event_handlers.py`
- **Handler for NATS event messages.** (1 connections) — `server/realtime/event_handlers.py`
- **Get mapping of event types to their handler methods.          Returns:** (1 connections) — `server/realtime/event_handlers.py`
- **Validate that event message has required fields.          Args:             e** (1 connections) — `server/realtime/event_handlers.py`
- **Handle incoming event messages from NATS.          Args:             message_** (1 connections) — `server/realtime/event_handlers.py`
- **Handle player_entered event.          Args:             data: Event data cont** (1 connections) — `server/realtime/event_handlers.py`
- **Handle player_left event.          Args:             data: Event data contain** (1 connections) — `server/realtime/event_handlers.py`
- **Handle game_tick event.          Args:             data: Event data containin** (1 connections) — `server/realtime/event_handlers.py`
- **Handle combat_started event.** (1 connections) — `server/realtime/event_handlers.py`
- **Handle combat_ended event.** (1 connections) — `server/realtime/event_handlers.py`
- *... and 5 more nodes in this community*

## Relationships

- [Inventory Command Models](Inventory_Command_Models.md) (7 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (1 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 79 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*