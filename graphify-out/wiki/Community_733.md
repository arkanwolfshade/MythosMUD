# Community 733

> 23 nodes

## Key Concepts

- **Any** (13 connections)
- **._build_grid()** (6 connections) — `server/services/ascii_map_renderer.py`
- **._build_exit_lookup()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._determine_map_style()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._exit_is_bidirectional()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_exit_entries_for_room()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._resolve_exit_target()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_room_symbol()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._get_vertical_exit_char()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._get_reverse_direction()** (3 connections) — `server/services/ascii_map_renderer.py`
- **._horizontal_exit_char_between()** (3 connections) — `server/services/ascii_map_renderer.py`
- **._vertical_exit_char_between()** (3 connections) — `server/services/ascii_map_renderer.py`
- **Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return list of (direction, (target_x, target_y), is_bidirectional) for exits…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build exit lookup map from room data.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return the horizontal exit character (em dash, >, or <), or None.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return the vertical exit character (|, v, or ^), or None.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Exit character shown on the row below the room at (x, y), or None.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Determine map style from room data. Args: rooms: List of room dictionaries…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build a coordinate grid from room data. Args: rooms: List of room dictionaries…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get ASCII symbol for a room. Args: room: Room dictionary map_style: Current map…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Reverse of `direction`, for checking bidirectional exits.** (1 connections) — `server/services/ascii_map_renderer.py`
- **True if target room has a reverse exit back to from_room_id.** (1 connections) — `server/services/ascii_map_renderer.py`

## Relationships

- [Community 539](Community_539.md) (11 shared connections)
- [Community 732](Community_732.md) (7 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`

## Audit Trail

- EXTRACTED: 45 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*