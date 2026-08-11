# E2E Suite Overview

> 19 nodes

## Key Concepts

- **container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (10 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **UUID** (3 connections)
- **test_coerce_row_quantity()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **PsycopgConnection** (2 connections)
- **datetime** (2 connections)
- **PsycopgCursor** (1 connections)
- **Composed** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not coerce_int(False)=** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables.      Queries container_** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures.      Args:         cursor: Da** (1 connections) — `server/persistence/container_helpers.py`
- **Build SQL update query for container.      Args:         updates: List of upd** (1 connections) — `server/persistence/container_helpers.py`
- **Row quantity/position coercion matches item quantity rules (PR #461 / int_coerci** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Relationships

- [Maps API Endpoints](Maps_API_Endpoints.md) (10 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (3 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (3 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (2 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 81 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*