# Message Builders

> 39 nodes

## Key Concepts

- **MessageBuilder** (20 connections) — `server/realtime/message_builders.py`
- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **test_create_player_entered_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_left_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.__init__()** (3 connections) — `server/realtime/message_builders.py`
- **test_build_occupants_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_state_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_npc_movement_message_variants()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_non_callable_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_uses_callable()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **.create_npc_movement_message()** (2 connections) — `server/realtime/message_builders.py`
- **Create an NPC movement message with direction. Args: npc_name: Name of the NPC…** (1 connections) — `server/realtime/message_builders.py`
- **Build the room occupants update message. Args: room_id_str: Room ID as string…** (1 connections) — `server/realtime/message_builders.py`
- **Build a room update message. Args: room_id: The room ID room_data: The room…** (1 connections) — `server/realtime/message_builders.py`
- **Build a single authoritative room_state message (room metadata + occupants).…** (1 connections) — `server/realtime/message_builders.py`
- **Utility class for building real-time event messages.** (1 connections) — `server/realtime/message_builders.py`
- *... and 14 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (6 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (3 shared connections)
- [Player Event Handlers Room](Player_Event_Handlers_Room.md) (2 shared connections)
- [Npc Event Handlers](Npc_Event_Handlers.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Conftest](Conftest.md) (1 shared connections)

## Source Files

- `server/realtime/message_builders.py`
- `server/tests/unit/realtime/test_message_builders.py`

## Audit Trail

- EXTRACTED: 69 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*