# Community 302

> 53 nodes

## Key Concepts

- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **get_session_maker()** (21 connections) — `server/database_helpers.py`
- **._validate_and_fix_player_room_with_persistence()** (11 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (6 connections)
- **.get_players_by_user_id()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.save_player()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **.update_player_last_active()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository()** (5 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **.delete_player()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **mock_player()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_player_repository_initialization_with_cache()** (4 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/player_repository.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/persistence/repositories/player_repository.py`
- **test_player_repository_initialization()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **test_player_repository_initialization_with_event_bus()** (3 connections) — `server/tests/unit/persistence/test_player_repository.py`
- **retry_with_backoff** (3 connections)
- *... and 28 more nodes in this community*

## Relationships

- [Player Creation Service](Player_Creation_Service.md) (14 shared connections)
- [Community 38](Community_38.md) (8 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (7 shared connections)
- [Community 161](Community_161.md) (4 shared connections)
- [Community 95](Community_95.md) (2 shared connections)
- [Community 543](Community_543.md) (1 shared connections)
- [Community 630](Community_630.md) (1 shared connections)
- [Database Manager](Database_Manager.md) (1 shared connections)
- [Community 892](Community_892.md) (1 shared connections)

## Source Files

- `server/database_helpers.py`
- `server/persistence/repositories/player_repository.py`
- `server/tests/unit/persistence/test_player_repository.py`

## Audit Trail

- EXTRACTED: 98 (84%)
- INFERRED: 18 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*