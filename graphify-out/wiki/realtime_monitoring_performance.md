# realtime monitoring performance

> 39 nodes

## Key Concepts

- **MessageBuilder** (26 connections) — `server/realtime/message_builders.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **test_create_player_entered_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_left_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.__init__()** (3 connections) — `server/realtime/message_builders.py`
- **test_get_next_sequence_uses_callable()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_non_callable_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_npc_movement_message_variants()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_occupants_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_state_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.create_npc_movement_message()** (2 connections) — `server/realtime/message_builders.py`
- **Utility class for building real-time event messages.** (1 connections) — `server/realtime/message_builders.py`
- **Initialize the message builder.          Args:             sequence_counter: Cal** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number.** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number (public API).          Returns:             The nex** (1 connections) — `server/realtime/message_builders.py`
- **Create a real-time message for player entering a room.          Args:** (1 connections) — `server/realtime/message_builders.py`
- *... and 14 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (11 shared connections)
- [commands communication channels](commands_communication_channels.md) (2 shared connections)
- [npc event handlers](npc_event_handlers.md) (2 shared connections)
- [event bus events](event_bus_events.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)

## Source Files

- `server/realtime/message_builders.py`
- `server/tests/unit/realtime/test_message_builders.py`

## Audit Trail

- EXTRACTED: 131 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*