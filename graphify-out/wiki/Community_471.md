# Community 471

> 38 nodes

## Key Concepts

- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Player** (12 connections)
- **._validate_and_fix_player_room_with_persistence()** (11 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (5 connections) — `server/persistence/repositories/player_repository.py`
- **Any** (5 connections)
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_strings()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_parse_equipped_safely()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **.get_player_by_user_id()** (4 connections) — `server/persistence/repositories/player_repository.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (1 connections)
- **Any** (1 connections)
- **Extract and coerce stats from row. Returns empty dict if not a dict.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Parse equipped_json to dict. Returns empty dict on parse error or invalid type.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Extract string fields with defaults: inventory_json, equipped_json,…** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Extract numeric/bool fields with defaults: experience_points, level, is_admin,…** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- *... and 13 more nodes in this community*

## Relationships

- [Community 93](Community_93.md) (14 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (9 shared connections)
- [Community 384](Community_384.md) (9 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 333](Community_333.md) (3 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`

## Audit Trail

- EXTRACTED: 89 (91%)
- INFERRED: 9 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*