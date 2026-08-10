# Player Save Preparer

> 37 nodes

## Key Concepts

- **container_persistence_async.py** (34 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **Any** (12 connections)
- **get_container_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **_container_data_from_row()** (11 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (9 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (9 connections)
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **delete_container_async()** (8 connections) — `server/persistence/container_persistence_async.py`
- **_call_create_container_procedure()** (7 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (6 connections)
- **_parse_jsonb()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_validate_container_create_params()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_build_item_dict()** (5 connections) — `server/persistence/container_persistence_async.py`
- **ContainerData** (5 connections)
- **_prepare_container_create_params()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_mapping()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_parse_item_metadata()** (4 connections) — `server/persistence/container_persistence_async.py`
- **Validate lock_state parameter.      Args:         lock_state: Lock state to v** (1 connections) — `server/persistence/container_helpers.py`
- **Async container persistence operations.  Provides async implementations using SQ** (1 connections) — `server/persistence/container_persistence_async.py`
- **Parse JSONB value (same as container_helpers.parse_jsonb_column).** (1 connections) — `server/persistence/container_persistence_async.py`
- **Prepare params dict for create_container procedure call.** (1 connections) — `server/persistence/container_persistence_async.py`
- *... and 12 more nodes in this community*

## Relationships

- [JSONB Column Parsing](JSONB_Column_Parsing.md) (18 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (13 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (4 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (4 shared connections)
- [Feature Implementation Phases](Feature_Implementation_Phases.md) (2 shared connections)
- [Persistence Item Instance](Persistence_Item_Instance.md) (2 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`

## Audit Trail

- EXTRACTED: 201 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*