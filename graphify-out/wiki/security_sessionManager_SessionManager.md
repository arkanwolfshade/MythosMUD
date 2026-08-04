# security sessionManager SessionManager

> 9 nodes

## Key Concepts

- **UUID** (14 connections)
- **.delete_player()** (9 connections) — `server/game/player_service.py`
- **.get_player_by_id()** (8 connections) — `server/game/player_service.py`
- **.soft_delete_character()** (7 connections) — `server/game/player_service.py`
- **.validate_character_access()** (5 connections) — `server/game/player_service.py`
- **Get a player by their ID.          Args:             player_id: The player's ID** (1 connections) — `server/game/player_service.py`
- **Delete a player character.          Args:             player_id: The player's ID** (1 connections) — `server/game/player_service.py`
- **Validate that a character exists, belongs to the user, and is not deleted.** (1 connections) — `server/game/player_service.py`
- **Soft delete a character (sets is_deleted=True, deleted_at=timestamp).          M** (1 connections) — `server/game/player_service.py`

## Relationships

- [coercion int inventory](coercion_int_inventory.md) (14 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [commands party examples](commands_party_examples.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 43 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*