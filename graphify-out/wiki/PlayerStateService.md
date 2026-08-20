# PlayerStateService

> 33 nodes

## Key Concepts

- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **.__init__()** (3 connections) — `server/game/player_state_service.py`
- **Any** (1 connections)
- **Stats** (1 connections)
- **Create a new player character with specific stats. Args: name: The player's…** (1 connections) — `server/game/player_creation_service.py`
- **Service for player creation operations.** (1 connections) — `server/game/player_creation_service.py`
- **Initialize with persistence layer, schema converter, and optional instance…** (1 connections) — `server/game/player_creation_service.py`
- **Resolve starting room and tutorial instance ID. For tutorial players, returns…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character. Args: name: The player's name profession_id: The…** (1 connections) — `server/game/player_creation_service.py`
- **Initialize the player service with a persistence layer and optional combat…** (1 connections) — `server/game/player_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [User](User.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [PlayerSchemaConverter](PlayerSchemaConverter.md) (1 shared connections)
- [test_player_service_mutations.py](test_player_service_mutations.py.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`

## Audit Trail

- EXTRACTED: 70 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*