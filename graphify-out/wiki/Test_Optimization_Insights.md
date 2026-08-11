# Test Optimization Insights

> 36 nodes

## Key Concepts

- **EventHandler** (22 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
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
- **Normalize NATS event_data payload to a string-keyed dict.** (1 connections) — `server/realtime/event_handlers.py`
- **Handler for NATS event messages.** (1 connections) — `server/realtime/event_handlers.py`
- **Initialize event handler.          Args:             connection_manager: Conn** (1 connections) — `server/realtime/event_handlers.py`
- **Get mapping of event types to their handler methods.          Returns:** (1 connections) — `server/realtime/event_handlers.py`
- **Validate that event message has required fields.          Args:             e** (1 connections) — `server/realtime/event_handlers.py`
- **Handle incoming event messages from NATS.          Args:             message_** (1 connections) — `server/realtime/event_handlers.py`
- **Handle player_entered event.          Args:             data: Event data cont** (1 connections) — `server/realtime/event_handlers.py`
- *... and 11 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (2 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (1 shared connections)
- [Circuit Breaker Core](Circuit_Breaker_Core.md) (1 shared connections)
- [Dead Letter Queue](Dead_Letter_Queue.md) (1 shared connections)
- [Chat Message Filtering](Chat_Message_Filtering.md) (1 shared connections)
- [Vim Editor Guidelines](Vim_Editor_Guidelines.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 95 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*