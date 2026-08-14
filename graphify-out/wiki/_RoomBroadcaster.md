# _RoomBroadcaster

> 7 nodes

## Key Concepts

- **_RoomBroadcaster** (4 connections) — `server/commands/position_commands.py`
- **_EventSequence** (3 connections) — `server/commands/position_commands.py`
- **.broadcast_to_room()** (3 connections) — `server/commands/position_commands.py`
- **Protocol** (2 connections)
- **Sequence counter surface used by build_event.** (1 connections) — `server/commands/position_commands.py`
- **Connection manager surface used to fan out posture events.** (1 connections) — `server/commands/position_commands.py`
- **Send event to occupants of room_id.** (1 connections) — `server/commands/position_commands.py`

## Relationships

- [AliasStorage](AliasStorage.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*