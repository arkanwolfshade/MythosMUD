# server services ascii map renderer

> 21 nodes

## Key Concepts

- **Any** (13 connections)
- **._build_exit_lookup()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._exit_is_bidirectional()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_exit_entries_for_room()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_horizontal_exit_char()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._get_vertical_exit_char()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._render_room_row()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._resolve_exit_target()** (5 connections) — `server/services/ascii_map_renderer.py`
- **._horizontal_exit_char_between()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._vertical_exit_char_between()** (4 connections) — `server/services/ascii_map_renderer.py`
- **._get_reverse_direction()** (3 connections) — `server/services/ascii_map_renderer.py`
- **True if target room has a reverse exit back to from_room_id.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Resolve one exit to (target_x, target_y) and is_bidirectional. Returns None if…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return list of (direction, (target_x, target_y), is_bidirectional) for exits…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Build exit lookup map from room data.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Render a single row of rooms with horizontal exits.** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return the horizontal exit character (—, >, or <) given east/west exit state,…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get exit character to display after a room for horizontal (east/west) exits.…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Return the vertical exit character (|, v, or ^) given south/north exit state,…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get exit character to display between rows for vertical (north/south) exits.…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Get reverse direction for checking bidirectional exits. Args: direction: Exit…** (1 connections) — `server/services/ascii_map_renderer.py`

## Relationships

- [server services ascii map renderer](server_services_ascii_map_renderer.md) (17 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`

## Audit Trail

- EXTRACTED: 43 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*