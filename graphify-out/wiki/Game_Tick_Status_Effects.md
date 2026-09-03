# Game Tick Status Effects

> 17 nodes

## Key Concepts

- **game_tick_status_effects.py** (30 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_handle_login_warded_expirations()** (5 connections) — `server/app/game_tick_status_effects.py`
- **UUID** (2 connections)
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process status effects for a single player. Returns: True if player was…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Clear in-memory grace state for each expired LOGIN_WARDED effect.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_status_effects.py`

## Relationships

- [Test Game Tick Processing Async](Test_Game_Tick_Processing_Async.md) (12 shared connections)
- [Test Game Tick Processing](Test_Game_Tick_Processing.md) (10 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (8 shared connections)
- [Game Tick Death](Game_Tick_Death.md) (6 shared connections)
- [Game Tick Protocols](Game_Tick_Protocols.md) (4 shared connections)
- [Test Login Grace Period](Test_Login_Grace_Period.md) (3 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 70 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*