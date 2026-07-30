# F

> 61 nodes

## Key Concepts

- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **retry.py** (16 connections) — `server/utils/retry.py`
- **test_retry.py** (10 connections) — `server/tests/unit/utils/test_retry.py`
- **retry_with_backoff()** (10 connections) — `server/utils/retry.py`
- **is_transient_error()** (9 connections) — `server/utils/retry.py`
- **Exception** (8 connections)
- **player_repository_room.py** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **validate_and_fix_player_room_with_persistence()** (7 connections) — `server/persistence/repositories/player_repository_room.py`
- **Any** (5 connections)
- **should_skip_room_validation()** (5 connections) — `server/persistence/repositories/player_repository_room.py`
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_parse_equipped_safely()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_strings()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- *... and 36 more nodes in this community*

## Relationships

- [real time](real_time.md) (17 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [world](world.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (1 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (1 shared connections)
- [spawn defaults](spawn_defaults.md) (1 shared connections)
- [test room subscription manager helpers](test_room_subscription_manager_helpers.md) (1 shared connections)
- [make mock row()](make_mock_row%28%29.md) (1 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_repository_room.py`
- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 225 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*