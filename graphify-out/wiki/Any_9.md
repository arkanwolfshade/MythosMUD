# Any

> 23 nodes

## Key Concepts

- **Any** (13 connections)
- **.render_map()** (11 connections) — `server/services/ascii_map_renderer.py`
- **._build_grid()** (6 connections) — `server/services/ascii_map_renderer.py`
- **._build_exit_lookup()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._determine_map_style()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_exit_entries_for_room()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_horizontal_exit_char()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._render_room_row()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._resolve_exit_target()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_room_symbol()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._horizontal_exit_char_between()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._auto_center_viewport()** (3 connections) — `server/services/ascii_map_renderer.py`
- **Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return list of (direction, (target_x, target_y), is_bidirectional) for exits…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build exit lookup map from room data.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Center viewport on the character's current room so the player is in the middle…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Render a single row of rooms with horizontal exits.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Render an ASCII map as HTML. Args: rooms: List of room dictionaries with…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return the horizontal exit character (—, >, or <) given east/west exit state,…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get exit character to display after a room for horizontal (east/west) exits.…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Determine map style from room data. Args: rooms: List of room dictionaries…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build a coordinate grid from room data. Args: rooms: List of room dictionaries…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get ASCII symbol for a room. Args: room: Room dictionary map_style: Current map…** (1 connections) — `server/services/ascii_map_renderer.py`

## Relationships

- [AsciiMapRenderer](AsciiMapRenderer.md) (11 shared connections)
- [._get_vertical_exit_char](_get_vertical_exit_char.md) (4 shared connections)
- [._exit_is_bidirectional](_exit_is_bidirectional.md) (2 shared connections)
- [._render_empty_map](_render_empty_map.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*