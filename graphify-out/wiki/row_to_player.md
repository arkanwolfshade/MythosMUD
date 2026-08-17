# row_to_player

> 40 nodes

## Key Concepts

- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **player_repository_mappers.py** (11 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **Any** (5 connections)
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_strings()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_parse_equipped_safely()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/persistence/repositories/player_repository.py`
- **InventoryPayload** (2 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Player** (1 connections)
- **Any** (1 connections)
- **Row-to-player mapping utilities for PlayerRepository. Maps procedure result…** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Type hint for inventory payload structure.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Extract and coerce stats from row. Returns empty dict if not a dict.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- *... and 15 more nodes in this community*

## Relationships

- [pytest.md](pytest.md.md) (17 shared connections)
- [get_session_maker](get_session_maker.md) (8 shared connections)
- [log_and_raise](log_and_raise.md) (8 shared connections)
- [test_retry.py](test_retry.py.md) (5 shared connections)
- [test_player_related_models.py](test_player_related_models.py.md) (2 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`

## Audit Trail

- EXTRACTED: 98 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*