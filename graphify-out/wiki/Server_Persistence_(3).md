# Server Persistence (3)

> 86 nodes

## Key Concepts

- **get_session_maker()** (91 connections) — `server/database.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (13 connections)
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **_row_to_player_spell()** (9 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.list_players()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_spells()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.get_player_spell()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.learn_spell()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.update_mastery()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **.record_spell_cast()** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **UUID** (7 connections)
- **.update_player_last_active()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (7 connections)
- **.get_all_spells()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_spell_by_id()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **.save_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.save_players()** (6 connections) — `server/persistence/repositories/player_repository.py`
- **.soft_delete_player()** (6 connections) — `server/persistence/repositories/player_repository.py`
- *... and 61 more nodes in this community*

## Relationships

- [Server Persistence](Server_Persistence.md) (46 shared connections)
- [Server Api](Server_Api.md) (21 shared connections)
- [Server Admin](Server_Admin.md) (16 shared connections)
- [Server Utils (9)](Server_Utils_%289%29.md) (12 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (10 shared connections)
- [Server Persistence (7)](Server_Persistence_%287%29.md) (8 shared connections)
- [Server Persistence (8)](Server_Persistence_%288%29.md) (6 shared connections)
- [Server Models (26)](Server_Models_%2826%29.md) (6 shared connections)
- [Server Tools](Server_Tools.md) (5 shared connections)
- [Server Game (9)](Server_Game_%289%29.md) (5 shared connections)
- [Server Persistence (4)](Server_Persistence_%284%29.md) (5 shared connections)
- [Server Persistence (14)](Server_Persistence_%2814%29.md) (4 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 409 (93%)
- INFERRED: 33 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*