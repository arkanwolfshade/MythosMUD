# Realtime Event Handlers

> 34 nodes · cohesion 0.07

## Key Concepts

- **EventHandler** (24 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (6 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.handle_game_tick_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_player_entered_event()** (2 connections) — `server/realtime/event_handlers.py`
- **.handle_player_left_event()** (2 connections) — `server/realtime/event_handlers.py`
- **Handler for NATS event messages.** (1 connections) — `server/realtime/event_handlers.py`
- **Initialize event handler.          Args:             connection_manager: Conn** (1 connections) — `server/realtime/event_handlers.py`
- **Get mapping of event types to their handler methods.          Returns:** (1 connections) — `server/realtime/event_handlers.py`
- **Validate that event message has required fields.          Args:             e** (1 connections) — `server/realtime/event_handlers.py`
- **Handle incoming event messages from NATS.          Args:             message_** (1 connections) — `server/realtime/event_handlers.py`
- **Handle player_entered event.          Args:             data: Event data cont** (1 connections) — `server/realtime/event_handlers.py`
- **Handle player_left event.          Args:             data: Event data contain** (1 connections) — `server/realtime/event_handlers.py`
- **Handle game_tick event.          Args:             data: Event data containin** (1 connections) — `server/realtime/event_handlers.py`
- *... and 9 more nodes in this community*

## Relationships

- [[Combat Player Broadcasts]] (6 shared connections)
- [[NATS Chat Broadcasting]] (3 shared connections)
- [[NPC Death Lifecycle]] (1 shared connections)
- [[Room Occupant Events]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Circuit Breaker Core]] (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 86 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
