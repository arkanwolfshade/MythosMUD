# Any

> 16 nodes

## Key Concepts

- **Any** (7 connections)
- **UUID** (7 connections)
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **.__init__()** (3 connections) — `server/game/player_state_service.py`
- **Gain occult knowledge (with lucidity loss). Args: player_id: The player's ID…** (1 connections) — `server/game/player_state_service.py`
- **Heal a player's health. Args: player_id: The player's ID (UUID) amount: Amount…** (1 connections) — `server/game/player_state_service.py`
- **Damage a player's health. Args: player_id: The player's ID (UUID) amount:…** (1 connections) — `server/game/player_state_service.py`
- **Initialize with a persistence layer.** (1 connections) — `server/game/player_state_service.py`
- **Apply lucidity loss to a player. Args: player_id: The player's ID (UUID)…** (1 connections) — `server/game/player_state_service.py`
- **Apply fear to a player. Args: player_id: The player's ID (UUID) amount: Amount…** (1 connections) — `server/game/player_state_service.py`
- **Apply corruption to a player. Args: player_id: The player's ID (UUID) amount:…** (1 connections) — `server/game/player_state_service.py`

## Relationships

- [PlayerService](PlayerService.md) (7 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (6 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/player_state_service.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*