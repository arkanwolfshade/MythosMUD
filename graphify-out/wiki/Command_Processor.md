# Command Processor

> 4 nodes

## Key Concepts

- **._exit_is_bidirectional()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_reverse_direction()** (3 connections) — `server/services/ascii_map_renderer.py`
- **True if target room has a reverse exit back to from_room_id.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get reverse direction for checking bidirectional exits.          Args:** (1 connections) — `server/services/ascii_map_renderer.py`

## Relationships

- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (2 shared connections)
- [ASCII Map Renderer](ASCII_Map_Renderer.md) (2 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*