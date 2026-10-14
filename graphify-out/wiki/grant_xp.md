# .grant_xp

> 8 nodes

## Key Concepts

- **_XpAwardingPersistence** (4 connections) — `server/game/level_service.py`
- **.grant_xp()** (4 connections) — `server/game/level_service.py`
- **.award_player_xp()** (3 connections) — `server/game/level_service.py`
- **UUID** (3 connections)
- **Protocol** (1 connections)
- **Persistence surface LevelService actually calls (narrows the Any-typed…** (1 connections) — `server/game/level_service.py`
- **Atomically add XP and recompute level. Returns (new_xp, old_level, new_level).** (1 connections) — `server/game/level_service.py`
- **Grant experience points to a character and check for level-up. Delegates to…** (1 connections) — `server/game/level_service.py`

## Relationships

- [get_logger](get_logger.md) (2 shared connections)
- [LevelService](LevelService.md) (1 shared connections)
- [ValueError](ValueError.md) (1 shared connections)

## Source Files

- `server/game/level_service.py`

## Audit Trail

- EXTRACTED: 10 (91%)
- INFERRED: 1 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*