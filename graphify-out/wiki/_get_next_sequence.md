# ._get_next_sequence

> 14 nodes

## Key Concepts

- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **Any** (6 connections)
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_occupants_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.__init__()** (3 connections) — `server/realtime/message_builders.py`
- **Build the room occupants update message. Args: room_id_str: Room ID as string…** (1 connections) — `server/realtime/message_builders.py`
- **Build a room update message. Args: room_id: The room ID room_data: The room…** (1 connections) — `server/realtime/message_builders.py`
- **Build a single authoritative room_state message (room metadata + occupants).…** (1 connections) — `server/realtime/message_builders.py`
- **Initialize the message builder. Args: sequence_counter: Callable that returns…** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number.** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number (public API). Returns: The next sequence number…** (1 connections) — `server/realtime/message_builders.py`
- **Create a real-time message for player entering a room. Args: event: The…** (1 connections) — `server/realtime/message_builders.py`

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (8 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (1 shared connections)

## Source Files

- `server/realtime/message_builders.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*