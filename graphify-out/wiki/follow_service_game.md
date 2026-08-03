# follow service game

> 23 nodes

## Key Concepts

- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **PsycopgConnection** (2 connections)
- **UUID** (2 connections)
- **datetime** (2 connections)
- **Persistence package for MythosMUD.  This package contains persistence utilities** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: PersistenceLayer and get_persistence removed - all code now uses AsyncPe** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from __** (1 connections) — `server/persistence/__init__.py`
- **Parse a JSONB column value from database.      JSONB columns may be returned a** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables.      Queries container_** (1 connections) — `server/persistence/container_helpers.py`
- **Query helper functions for container persistence operations.** (1 connections) — `server/persistence/container_query_helpers.py`
- **Build ContainerData object from database row.      Args:         conn: Database** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers in a room.      Args:         conn: Database connection** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers owned by an entity (player/NPC).      Args:         conn: Dat** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers that have decayed (decay_at < current_time).      Args:** (1 connections) — `server/persistence/container_query_helpers.py`

## Relationships

- [Database Config](Database_Config.md) (32 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (11 shared connections)
- [container sql injection](container_sql_injection.md) (11 shared connections)
- [persistence container item](persistence_container_item.md) (8 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (1 shared connections)
- [config models game](config_models_game.md) (1 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (1 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_query_helpers.py`

## Audit Trail

- EXTRACTED: 143 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*