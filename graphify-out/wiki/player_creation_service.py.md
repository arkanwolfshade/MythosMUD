# player_creation_service.py

> 34 nodes

## Key Concepts

- **player_creation_service.py** (16 connections) — `server/game/player_creation_service.py`
- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **asyncio** (6 connections)
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.respawn_player_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **.respawn_player_from_delirium_by_user_id()** (4 connections) — `server/game/player_respawn_wrapper.py`
- **test_respawn_from_delirium_not_delirious()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_player_not_found()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_from_delirium_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_no_players()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_not_dead()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **test_respawn_player_by_user_id_success()** (4 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **_dead_player()** (3 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **Any** (3 connections)
- **Any** (1 connections)
- **Stats** (1 connections)
- **Player creation service. This module handles player character creation…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character with specific stats. Args: name: The player's…** (1 connections) — `server/game/player_creation_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (11 shared connections)
- [PlayerService](PlayerService.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [Stats](Stats.md) (1 shared connections)
- [get_session_maker](get_session_maker.md) (1 shared connections)
- [players/__init__.py](players-__init__.py.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 77 (87%)
- INFERRED: 12 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*