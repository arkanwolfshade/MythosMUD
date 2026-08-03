# event realtime publisher

> 5 nodes

## Key Concepts

- **.respawn_player_from_delirium_by_user_id()** (7 connections) — `server/game/player_respawn_wrapper.py`
- **.__init__()** (3 connections) — `server/game/player_respawn_wrapper.py`
- **Any** (3 connections)
- **Initialize with a persistence layer.** (1 connections) — `server/game/player_respawn_wrapper.py`
- **Respawn a delirious player by user ID.          This method handles the complete** (1 connections) — `server/game/player_respawn_wrapper.py`

## Relationships

- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [magic healing game](magic_healing_game.md) (2 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/game/player_respawn_wrapper.py`

## Audit Trail

- EXTRACTED: 12 (80%)
- INFERRED: 3 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*