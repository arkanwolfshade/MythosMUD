# RoomDataValidator

> 32 nodes · cohesion 0.09

## Key Concepts

- **AsciiMapRenderer** (81 connections) — `server/services/ascii_map_renderer.py`
- **TestVerticalExitCharBetween** (9 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **TestRendererDelegation** (7 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **TestBridgeComputation** (6 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_a_diagonal_target_is_ignored()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_only_interior_cells_are_bridged()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_westward_and_northward_spans_are_bridged_too()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **.test_bidirectional_returns_pipe()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_no_exit_returns_none()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_and_one_way_south_assign_caret_and_v_by_target()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_returns_caret()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_north_uses_caret_bidirectional_uses_pipe()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.test_one_way_south_returns_v()** (3 connections) — `server/tests/unit/services/test_ascii_map_renderer_exits.py`
- **.__init__()** (2 connections) — `server/services/ascii_map_renderer.py`
- **.test_bridges_delegate()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_horizontal_char_delegates()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_reverse_direction_delegates()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_vertical_char_delegates()** (2 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **.test_adjacent_rooms_produce_no_bridge_cells()** (2 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **Renders ASCII maps from room coordinate data. Supports multiple map styles…** (1 connections) — `server/services/ascii_map_renderer.py`
- **Initialize the ASCII map renderer.** (1 connections) — `server/services/ascii_map_renderer.py`
- **The renderer's methods must stay equivalent to the functions they delegate to.** (1 connections) — `server/tests/unit/services/test_ascii_map_exits.py`
- **The endpoints are rooms; only the cells strictly between them are filled.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **Only axis-aligned spans can be drawn; a diagonal would fill the wrong cells.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- **Spans are directional; the lower endpoint is not always the source.** (1 connections) — `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- *... and 7 more nodes in this community*

## Relationships

- [ItemCatalogService](ItemCatalogService.md) (20 shared connections)
- [Migration Strategy](Migration_Strategy.md) (11 shared connections)
- [ClientLogger](ClientLogger.md) (8 shared connections)
- [field_validator](field_validator.md) (6 shared connections)
- [POSTGRESQL_AUDIT_REPORT_2026.md](POSTGRESQL_AUDIT_REPORT_2026.md.md) (5 shared connections)
- [client/package.json](client-package.json.md) (5 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (4 shared connections)
- [mock_container](mock_container.md) (4 shared connections)
- [NATS Complete Remediation Summary](NATS_Complete_Remediation_Summary.md) (2 shared connections)

## Source Files

- `server/services/ascii_map_renderer.py`
- `server/tests/unit/services/test_ascii_map_exits.py`
- `server/tests/unit/services/test_ascii_map_renderer_bridges.py`
- `server/tests/unit/services/test_ascii_map_renderer_exits.py`

## Audit Trail

- EXTRACTED: 96 (87%)
- INFERRED: 14 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*