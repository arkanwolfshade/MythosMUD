# ASCII Map Renderer

> 23 nodes

## Key Concepts

- **Any** (13 connections)
- **.render_map()** (11 connections) — `server/services/ascii_map_renderer.py`
- **._build_grid()** (6 connections) — `server/services/ascii_map_renderer.py`
- **._resolve_exit_target()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_exit_entries_for_room()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._build_exit_lookup()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._render_room_row()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_horizontal_exit_char()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._determine_map_style()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._horizontal_exit_char_between()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._get_room_symbol()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._render_empty_map()** (3 connections) — `server/services/ascii_map_renderer.py`
- **Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if i** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return list of (direction, (target_x, target_y), is_bidirectional) for exits** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build exit lookup map from room data.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Render a single row of rooms with horizontal exits.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Render an ASCII map as HTML.          Args:             rooms: List of room dict** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return the horizontal exit character (—, >, or <) given east/west exit state, or** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get exit character to display after a room for horizontal (east/west) exits.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Determine map style from room data.          Args:             rooms: List of ro** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build a coordinate grid from room data.          Args:             rooms: List o** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get ASCII symbol for a room.          Args:             room: Room dictionary** (1 connections) — `server/services/ascii_map_renderer.py`
- **Render an empty map.          Args:             width: Viewport width** (1 connections) — `server/services/ascii_map_renderer.py`

## Relationships

- [Player Command Developer Guide](Player_Command_Developer_Guide.md) (11 shared connections)
- [Cursor Plans Best](Cursor_Plans_Best.md) (4 shared connections)
- [Command Processor](Command_Processor.md) (2 shared connections)
- [Command Commands Validation](Command_Commands_Validation.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*