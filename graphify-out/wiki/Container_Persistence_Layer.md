# Container Persistence Layer

> 63 nodes · cohesion 0.09

## Key Concepts

- **test_container_persistence_extended_row_helpers.py** (51 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **container_persistence.py** (49 connections) — `server/persistence/container_persistence.py`
- **update_container()** (25 connections) — `server/persistence/container_persistence.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (18 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (15 connections) — `server/persistence/container_persistence.py`
- **UUID** (14 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (13 connections) — `server/persistence/container_persistence.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_InsertBindSource** (11 connections) — `server/persistence/container_persistence.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **_after_container_insert()** (10 connections) — `server/persistence/container_persistence.py`
- **_CreateOutcome** (10 connections) — `server/persistence/container_persistence.py`
- **_insert_container_row()** (10 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (10 connections) — `server/persistence/container_persistence.py`
- **_run_container_update_execute()** (9 connections) — `server/persistence/container_persistence.py`
- **_seed_new_container_items()** (9 connections) — `server/persistence/container_persistence.py`
- **datetime** (9 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- **_allowed_roles_from_row()** (5 connections) — `server/persistence/container_persistence.py`
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **_fetch_container_row_dict()** (5 connections) — `server/persistence/container_persistence.py`
- *... and 38 more nodes in this community*

## Relationships

- [[Container Data Models]] (41 shared connections)
- [[NPC Admin API]] (18 shared connections)
- [[Container Persistence Queries]] (17 shared connections)
- [[Container Repository CRUD]] (11 shared connections)
- [[Persistence Container Extended]] (10 shared connections)
- [[Persistence Item Instance]] (8 shared connections)
- [[Container Persistence Sql]] (5 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 422 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
