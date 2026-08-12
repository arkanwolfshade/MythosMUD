# Archive Planning Aliases

> 16 nodes

## Key Concepts

- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.__init__()** (3 connections) — `server/realtime/message_builders.py`
- **Initialize the message builder.          Args:             sequence_counter: Cal** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number.** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number (public API).          Returns:             The nex** (1 connections) — `server/realtime/message_builders.py`
- **Create a real-time message for player entering a room.          Args:** (1 connections) — `server/realtime/message_builders.py`
- **Create a real-time message for player leaving a room.          Args:** (1 connections) — `server/realtime/message_builders.py`
- **Build the room occupants update message.          Args:             room_id_str:** (1 connections) — `server/realtime/message_builders.py`
- **Build a room update message.          Args:             room_id: The room ID** (1 connections) — `server/realtime/message_builders.py`
- **Build a single authoritative room_state message (room metadata + occupants).** (1 connections) — `server/realtime/message_builders.py`

## Relationships

- [Character Creation E2E](Character_Creation_E2E.md) (7 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (2 shared connections)

## Source Files

- `server/realtime/message_builders.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*