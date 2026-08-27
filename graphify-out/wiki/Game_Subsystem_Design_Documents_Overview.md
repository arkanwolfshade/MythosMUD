# Game Subsystem Design Documents Overview

> 27 nodes

## Key Concepts

- **persistence/container_helpers.py** (20 connections) — `server/persistence/container_helpers.py`
- **container_query_helpers.py** (16 connections) — `server/persistence/container_query_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **_build_container_data_from_row()** (9 connections) — `server/persistence/container_query_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **get_containers_by_entity_id()** (7 connections) — `server/persistence/container_query_helpers.py`
- **get_decayed_containers()** (7 connections) — `server/persistence/container_query_helpers.py`
- **_coerce_row_quantity()** (6 connections) — `server/persistence/container_helpers.py`
- **get_containers_by_room_id()** (6 connections) — `server/persistence/container_query_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **UUID** (3 connections)
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **PsycopgConnection** (2 connections)
- **datetime** (2 connections)
- **UUID** (2 connections)
- **PsycopgCursor** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures. Args: cursor: Database cursor…** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not…** (1 connections) — `server/persistence/container_helpers.py`
- **Query helper functions for container persistence operations.** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers that have decayed (decay_at < current_time). Args: conn:…** (1 connections) — `server/persistence/container_query_helpers.py`
- **Build ContainerData object from database row. Args: conn: Database connection…** (1 connections) — `server/persistence/container_query_helpers.py`
- *... and 2 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (11 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [TaskRegistry](TaskRegistry.md) (6 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_query_helpers.py`

## Audit Trail

- EXTRACTED: 75 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*