# .clear_player_combat_state

> 6 nodes

## Key Concepts

- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.handle_combat_end()** (4 connections) — `server/services/player_combat_service.py`
- **.cleanup_stale_combat_states()** (3 connections) — `server/services/player_combat_service.py`
- **Clear a player's combat state. Args: player_id: ID of the player** (1 connections) — `server/services/player_combat_service.py`
- **Handle combat end by clearing all players in the combat. Args: combat_id: ID of…** (1 connections) — `server/services/player_combat_service.py`
- **Clean up stale combat states. Returns: Number of stale states cleaned up** (1 connections) — `server/services/player_combat_service.py`

## Relationships

- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/services/player_combat_service.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*