# Player Save Preparer

> 37 nodes

## Key Concepts

- **container_persistence_async.py** (34 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **Any** (12 connections)
- **get_container_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **_container_data_from_row()** (11 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (9 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (9 connections)
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **_call_create_container_procedure()** (7 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (6 connections)
- **_parse_jsonb()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_validate_container_create_params()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_build_item_dict()** (5 connections) — `server/persistence/container_persistence_async.py`
- **ContainerData** (5 connections)
- **_prepare_container_create_params()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_mapping()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_parse_item_metadata()** (4 connections) — `server/persistence/container_persistence_async.py`
- **Parse a JSONB column value from database.      JSONB columns may be returned a** (1 connections) — `server/persistence/container_helpers.py`
- **Validate lock_state parameter.      Args:         lock_state: Lock state to v** (1 connections) — `server/persistence/container_helpers.py`
- **Async container persistence operations.  Provides async implementations using SQ** (1 connections) — `server/persistence/container_persistence_async.py`
- **Parse JSONB value (same as container_helpers.parse_jsonb_column).** (1 connections) — `server/persistence/container_persistence_async.py`
- *... and 12 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (28 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (12 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (4 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (4 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`

## Audit Trail

- EXTRACTED: 205 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*