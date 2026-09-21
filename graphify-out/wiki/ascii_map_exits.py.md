# ascii_map_exits.py

> 29 nodes

## Key Concepts

- **ascii_map_exits.py** (15 connections) — `server/services/ascii_map_exits.py`
- **build_departures()** (5 connections) — `server/services/ascii_map_exits.py`
- **build_exit_bridges()** (5 connections) — `server/services/ascii_map_exits.py`
- **get_horizontal_exit_char()** (5 connections) — `server/services/ascii_map_exits.py`
- **get_vertical_exit_char()** (5 connections) — `server/services/ascii_map_exits.py`
- **horizontal_exit_char_between()** (4 connections) — `server/services/ascii_map_exits.py`
- **_index_room_positions()** (4 connections) — `server/services/ascii_map_exits.py`
- **_room_id()** (4 connections) — `server/services/ascii_map_exits.py`
- **vertical_exit_char_between()** (4 connections) — `server/services/ascii_map_exits.py`
- **_departing_directions()** (3 connections) — `server/services/ascii_map_exits.py`
- **_horizontal_bridge_cells()** (3 connections) — `server/services/ascii_map_exits.py`
- **_vertical_bridge_cells()** (3 connections) — `server/services/ascii_map_exits.py`
- **ExitLookup** (3 connections)
- **reverse_direction()** (2 connections) — `server/services/ascii_map_exits.py`
- **ExitInfo** (2 connections)
- **Grid** (2 connections)
- **Exit geometry for the ASCII map. Extracted from `ascii_map_renderer.py` to…** (1 connections) — `server/services/ascii_map_exits.py`
- **Exit character shown on the row between (x, y) and the room below it, or None.** (1 connections) — `server/services/ascii_map_exits.py`
- **Stable identifier for `room`, or "" when it has none.** (1 connections) — `server/services/ascii_map_exits.py`
- **Room ids present in this view, and the map cell each positioned one occupies.** (1 connections) — `server/services/ascii_map_exits.py`
- **Directions of `room`'s exits whose target is not part of this view.** (1 connections) — `server/services/ascii_map_exits.py`
- **Directions in which each room has an exit leading OUT of the loaded area. A map…** (1 connections) — `server/services/ascii_map_exits.py`
- **Cells strictly between (x, y) and an east/west target more than one column away.** (1 connections) — `server/services/ascii_map_exits.py`
- **Cells strictly between (x, y) and a north/south target more than one row away.** (1 connections) — `server/services/ascii_map_exits.py`
- **Cells lying strictly between two rooms joined by a single exit. A grid cell is…** (1 connections) — `server/services/ascii_map_exits.py`
- *... and 4 more nodes in this community*

## Relationships

- [ascii_map_renderer.py](ascii_map_renderer.py.md) (1 shared connections)
- [TestDepartures](TestDepartures.md) (1 shared connections)

## Source Files

- `server/services/ascii_map_exits.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*