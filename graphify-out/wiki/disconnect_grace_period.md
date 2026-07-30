# disconnect grace period

> 64 nodes

## Key Concepts

- **container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
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
- **_validate_new_container_params()** (6 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (6 connections)
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **datetime** (5 connections)
- *... and 39 more nodes in this community*

## Relationships

- [spell registry](spell_registry.md) (35 shared connections)
- [real time](real_time.md) (18 shared connections)
- [test player death service](test_player_death_service.md) (14 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (9 shared connections)
- [datetime](datetime.md) (8 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (6 shared connections)
- [.initialize()](initialize%28%29.md) (5 shared connections)
- [.calculate xp reward()](calculate_xp_reward%28%29.md) (5 shared connections)
- [test player repository](test_player_repository.md) (4 shared connections)
- [rescue commands](rescue_commands.md) (3 shared connections)
- [test quest service collect](test_quest_service_collect.md) (2 shared connections)
- [world](world.md) (2 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 426 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*