# NATS Complete Remediation Summary

> 21 nodes · cohesion 0.10

## Key Concepts

- **test_ascii_map_exits.py** (9 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **TestReverseDirections** (5 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **TestExitBridges** (4 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **TestExitCharacters** (4 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **parametrize** (2 connections)
- **.test_a_misaligned_vertical_target_is_ignored()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_a_non_tuple_target_is_ignored()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_an_exit_pointing_somewhere_else_is_not_drawn()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_horizontal_characters()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_vertical_characters()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_all_engine_directions_are_covered()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_every_direction_is_its_own_inverse()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **Direct tests for `server/services/ascii_map_exits.py`. The exit-geometry…** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **Guard branches in `build_exit_bridges` and its per-axis helpers.** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **`exit_from` values normally carry a `(x, y)` target; malformed data (a bare…** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **A `south`/`north` exit is expected to keep x fixed; `_vertical_bridge_cells`…** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **reverse(reverse(d)) == d for every entry - catches a transposed pair.** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **Every direction the command parser accepts needs an opposite, or exits in that…** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **The target must be the neighbouring cell; an exit to a third room draws nothing.** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_direction_lookup_is_case_insensitive()** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_unknown_direction_yields_empty_string()** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`

## Relationships

- [RoomDataValidator](RoomDataValidator.md) (2 shared connections)
- [mock_container](mock_container.md) (1 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (1 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Mansions of Madness_ Vol 1 - Behind Closed Doors  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Mansions_of_Madness__Vol_1_-_Behind_Closed_Doors__2026-08-12.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_ascii_map_exits.py`

## Audit Trail

- EXTRACTED: 26 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*