# ._create_grid_map

> 23 nodes

## Key Concepts

- **._create_grid_map()** (6 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **._assign_coordinates()** (5 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **.render_ascii_map()** (5 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **._generate_color_legend()** (4 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **.get_street_color()** (4 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **.get_street_name()** (4 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **._draw_connection()** (3 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **._get_next_coordinates()** (3 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **.render_connectivity_stats()** (3 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **.render_json_summary()** (3 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **._reverse_direction()** (3 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Any** (3 connections)
- **Extract street name from room ID. Args: room_id: Full room ID Returns: Street…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Get color code for a street. Args: room_id: Full room ID Returns: ANSI color…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Render the mini-map as ASCII art with grid-based visualization. Args:…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Create a grid-based map visualization. Args: nodes: List of room nodes edges:…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Assign grid coordinates to rooms based on connectivity. Args: nodes: List of…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Get coordinates for the next room based on direction. Args: x: Current x…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Reverse a direction. Args: direction: Original direction Returns: Reversed…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Draw a connection line between two rooms. Args: grid: The grid to draw on x1,…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Generate a color-coded legend for the streets and special symbols. Args: nodes:…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Render a JSON summary of the mini-map data. Args: minimap_data: Mini-map graph…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`
- **Render connectivity statistics for the mini-map. Args: minimap_data: Mini-map…** (1 connections) — `tools/room_toolkit/room_validator/core/minimap_renderer.py`

## Relationships

- [PathValidator](PathValidator.md) (11 shared connections)

## Source Files

- `tools/room_toolkit/room_validator/core/minimap_renderer.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*