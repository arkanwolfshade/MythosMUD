# AsciiMapRenderer

> 36 nodes

## Key Concepts

- **AsciiMapRenderer** (81 connections) — `server/services/ascii_map_renderer.py`
- **_room()** (11 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **TestDepartureMarkers** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **test_ascii_map_renderer_bridges.py** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **_plain()** (8 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **._rendered()** (8 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **TestBridgeComputation** (6 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **TestHorizontalBridging** (5 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_adjacent_rooms_still_render_unchanged()** (5 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_an_unconnected_gap_stays_blank()** (5 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **TestVerticalBridging** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_a_west_exit_out_of_the_area_marks_the_empty_cell_beside_it()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_an_exit_to_a_loaded_room_is_not_marked()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_an_east_west_exit_spanning_three_cells_is_drawn()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_a_north_south_exit_spanning_three_cells_is_drawn()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_an_unconnected_vertical_gap_stays_blank()** (4 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_a_diagonal_target_is_ignored()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_only_interior_cells_are_bridged()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_westward_and_northward_spans_are_bridged_too()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_a_north_exit_out_of_the_area_is_marked()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_a_room_with_no_exits_is_not_marked()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_an_east_exit_out_of_the_area_is_marked()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.__init__()** (2 connections) — `server/services/ascii_map_renderer.py`
- **.test_adjacent_rooms_produce_no_bridge_cells()** (2 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **Renders ASCII maps from room coordinate data. Supports multiple map styles…** (1 connections) — `server/services/ascii_map_renderer.py`
- *... and 11 more nodes in this community*

## Relationships

- [.render_map](render_map.md) (20 shared connections)
- [test_ascii_map_renderer_exits.py](test_ascii_map_renderer_exits.py.md) (7 shared connections)
- [TestVerticalExitCharBetween](TestVerticalExitCharBetween.md) (7 shared connections)
- [RoomService](RoomService.md) (6 shared connections)
- [test_ascii_map_exits.py](test_ascii_map_exits.py.md) (6 shared connections)
- [test_ascii_map_renderer_grid.py](test_ascii_map_renderer_grid.py.md) (6 shared connections)
- [TestHorizontalExitCharBetween](TestHorizontalExitCharBetween.md) (5 shared connections)
- [TestResolveExitTarget](TestResolveExitTarget.md) (5 shared connections)
- [TestSymbolTables](TestSymbolTables.md) (3 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/tests/unit/services/test_ascii_map_renderer_bridges.py`

## Audit Trail

- EXTRACTED: 121 (90%)
- INFERRED: 14 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*