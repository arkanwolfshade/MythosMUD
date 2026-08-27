# Alone Against the Dark (source summary)

> 6 nodes

## Key Concepts

- **.get_room_state_event()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/player_event_handlers.py`
- **UUID** (3 connections)
- **JsonMap** (1 connections)
- **Send occupants snapshot to a player. CRITICAL: This method MUST include NPCs…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Build authoritative room_state event for a room (for request/response enter-…** (1 connections) — `server/realtime/player_event_handlers.py`

## Relationships

- [InventoryCommandFactory](InventoryCommandFactory.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`

## Audit Trail

- EXTRACTED: 8 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*