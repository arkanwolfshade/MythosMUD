# AsciiMapRenderer

> 52 nodes

## Key Concepts

- **AsciiMapRenderer** (81 connections) — `server/services/ascii_map_renderer.py`
- **_room()** (11 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **TestDepartureMarkers** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **test_ascii_map_renderer_bridges.py** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **_plain()** (8 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **._rendered()** (8 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **TestRendererDelegation** (7 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **TestResolveExitTarget** (7 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
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
- **.test_returns_coords_and_bidirectional_when_target_has_reverse_exit()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- *... and 27 more nodes in this community*

## Relationships

- [.render_map](render_map.md) (20 shared connections)
- [test_ascii_map_renderer_exits.py](test_ascii_map_renderer_exits.py.md) (13 shared connections)
- [ascii_map_renderer.py](ascii_map_renderer.py.md) (11 shared connections)
- [TestVerticalExitCharBetween](TestVerticalExitCharBetween.md) (7 shared connections)
- [map_minimap.py](map_minimap.py.md) (2 shared connections)
- [ExplorationService](ExplorationService.md) (2 shared connections)
- [TestDepartures](TestDepartures.md) (2 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/tests/unit/services/test_ascii_map_exits.py`
- `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Audit Trail

- EXTRACTED: 137 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*