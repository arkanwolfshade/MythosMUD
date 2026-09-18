# Community 831

> 19 nodes

## Key Concepts

- **game_tick_status_effects.py** (28 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **process_player_effects_expiration()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_handle_login_warded_expirations()** (4 connections) — `server/app/game_tick_status_effects.py`
- **UUID** (2 connections)
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process status effects for a single player. Returns: True if player was…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Clear in-memory grace state for each expired LOGIN_WARDED effect.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_status_effects.py`

## Relationships

- [Community 385](Community_385.md) (12 shared connections)
- [Community 370](Community_370.md) (11 shared connections)
- [Community 386](Community_386.md) (10 shared connections)
- [Community 883](Community_883.md) (8 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (4 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 542](Community_542.md) (2 shared connections)
- [Community 884](Community_884.md) (1 shared connections)
- [Community 183](Community_183.md) (1 shared connections)
- [Community 60](Community_60.md) (1 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 71 (86%)
- INFERRED: 12 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*