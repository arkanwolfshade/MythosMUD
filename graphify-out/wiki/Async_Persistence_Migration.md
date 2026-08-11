# Async Persistence Migration

> 39 nodes

## Key Concepts

- **UUID** (14 connections)
- **Any** (11 connections)
- **.delete_player()** (9 connections) — `server/game/player_service.py`
- **.get_player_by_id()** (8 connections) — `server/game/player_service.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_service.py`
- **.soft_delete_character()** (7 connections) — `server/game/player_service.py`
- **.create_player_with_stats()** (5 connections) — `server/game/player_service.py`
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
- **Get a player by their ID.          Args:             player_id: The player's ID** (1 connections) — `server/game/player_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (20 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (7 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (3 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 128 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*