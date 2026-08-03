# persistence container item

> 68 nodes

## Key Concepts

- **container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **_InsertBindSource** (11 connections) — `server/persistence/container_persistence.py`
- **_insert_container_row()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **_seed_new_container_items()** (11 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **_CreateOutcome** (10 connections) — `server/persistence/container_persistence.py`
- **_after_container_insert()** (10 connections) — `server/persistence/container_persistence.py`
- **_run_container_update_execute()** (9 connections) — `server/persistence/container_persistence.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- **_validate_new_container_params()** (6 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (6 connections)
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **datetime** (5 connections)
- **_allowed_roles_from_row()** (5 connections) — `server/persistence/container_persistence.py`
- **_insert_bind_tuple()** (5 connections) — `server/persistence/container_persistence.py`
- *... and 43 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (33 shared connections)
- [container sql injection](container_sql_injection.md) (21 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (19 shared connections)
- [follow service game](follow_service_game.md) (8 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (8 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [schemas invite user](schemas_invite_user.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [persistence container extended](persistence_container_extended.md) (1 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (1 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 402 (95%)
- INFERRED: 22 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*