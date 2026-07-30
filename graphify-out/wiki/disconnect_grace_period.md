# disconnect grace period

> 85 nodes

## Key Concepts

- **container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **ContainerData** (34 connections) — `server/persistence/container_data.py`
- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **test_container_persistence_extended_parse.py** (26 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **container_data.py** (12 connections) — `server/persistence/container_data.py`
- **_InsertBindSource** (11 connections) — `server/persistence/container_persistence.py`
- **_insert_container_row()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **_seed_new_container_items()** (11 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **_CreateOutcome** (10 connections) — `server/persistence/container_persistence.py`
- **_after_container_insert()** (10 connections) — `server/persistence/container_persistence.py`
- **_run_container_update_execute()** (9 connections) — `server/persistence/container_persistence.py`
- **container_create_params.py** (6 connections) — `server/persistence/container_create_params.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- *... and 60 more nodes in this community*

## Relationships

- [spell registry](spell_registry.md) (36 shared connections)
- [datetime](datetime.md) (34 shared connections)
- [real time](real_time.md) (30 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (17 shared connections)
- [rescue commands](rescue_commands.md) (10 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (5 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [test player death service](test_player_death_service.md) (2 shared connections)
- [HealthRepository](HealthRepository.md) (1 shared connections)
- [PlayerChannelPreferences](PlayerChannelPreferences.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/container_data.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 570 (94%)
- INFERRED: 36 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*