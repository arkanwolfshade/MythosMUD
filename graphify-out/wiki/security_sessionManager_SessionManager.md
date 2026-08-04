# security sessionManager SessionManager

> 41 nodes

## Key Concepts

- **UUID** (14 connections)
- **Any** (11 connections)
- **.delete_player()** (9 connections) — `server/game/player_service.py`
- **.get_player_by_id()** (8 connections) — `server/game/player_service.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_service.py`
- **.soft_delete_character()** (7 connections) — `server/game/player_service.py`
- **.create_player_with_stats()** (5 connections) — `server/game/player_service.py`
- **.get_player_by_name()** (5 connections) — `server/game/player_service.py`
- **.get_user_characters()** (5 connections) — `server/game/player_service.py`
- **.validate_character_access()** (5 connections) — `server/game/player_service.py`
- **.create_player()** (4 connections) — `server/game/player_service.py`
- **.list_players()** (4 connections) — `server/game/player_service.py`
- **.apply_lucidity_loss()** (4 connections) — `server/game/player_service.py`
- **.apply_fear()** (4 connections) — `server/game/player_service.py`
- **.apply_corruption()** (4 connections) — `server/game/player_service.py`
- **.gain_occult_knowledge()** (4 connections) — `server/game/player_service.py`
- **.heal_player()** (4 connections) — `server/game/player_service.py`
- **.damage_player()** (4 connections) — `server/game/player_service.py`
- **.set_item_prototype_registry()** (3 connections) — `server/game/player_service.py`
- **.respawn_player_by_user_id()** (3 connections) — `server/game/player_service.py`
- **.respawn_player_from_delirium_by_user_id()** (3 connections) — `server/game/player_service.py`
- **Stats** (1 connections)
- **Set the item prototype registry on the schema converter (e.g. after item service** (1 connections) — `server/game/player_service.py`
- **Create a new player character.          Args:             name: The player's nam** (1 connections) — `server/game/player_service.py`
- **Create a new player character with specific stats.          Args:             na** (1 connections) — `server/game/player_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (21 shared connections)
- [Player Stats](Player_Stats.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 134 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*