# Game

> 23 nodes

## Key Concepts

- **server/models/game.py** (43 connections) — `server/models/game.py`
- **CoreStatValues** (7 connections) — `server/models/stats_random.py`
- **roll_random_core_stat_values()** (7 connections) — `server/models/stats_random.py`
- **._ensure_core_stats()** (6 connections) — `server/models/game.py`
- **stats_random.py** (5 connections) — `server/models/stats_random.py`
- **_merge_random_core_stats()** (4 connections) — `server/models/game.py`
- **._compute_max_dp_if_missing()** (4 connections) — `server/models/game.py`
- **_coerce_stat_int()** (3 connections) — `server/models/game.py`
- **_needs_random_core_stats()** (3 connections) — `server/models/game.py`
- **model_validator** (3 connections)
- **_utc_now_naive()** (2 connections) — `server/models/game.py`
- **datetime** (2 connections)
- **_new_player_id()** (1 connections) — `server/models/game.py`
- **TypedDict** (1 connections)
- **Game-related models for MythosMUD. This module contains models specific to the…** (1 connections) — `server/models/game.py`
- **Generate random core stats when missing or None. Callers may pass…** (1 connections) — `server/models/game.py`
- **Convert persisted stat values to int with a safe fallback.** (1 connections) — `server/models/game.py`
- **Populate max_dp from (CON+SIZ)/5 when not provided (stored value takes…** (1 connections) — `server/models/game.py`
- **True when any core stat key is missing or explicitly None.** (1 connections) — `server/models/game.py`
- **Fill missing or None core stat keys from rolled values.** (1 connections) — `server/models/game.py`
- **Random core stat rolls for character creation (no Stats import — breaks…** (1 connections) — `server/models/stats_random.py`
- **Core attribute ints rolled for a new character (keys match Stats core fields…** (1 connections) — `server/models/stats_random.py`
- **Roll core attribute values for a new character. Returns a plain dict so…** (1 connections) — `server/models/stats_random.py`

## Relationships

- [Stats Generator](Stats_Generator.md) (9 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (5 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (4 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Test Game Player](Test_Game_Player.md) (4 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (2 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (2 shared connections)
- [Test Game Enums](Test_Game_Enums.md) (2 shared connections)
- [Test Game Status Effect](Test_Game_Status_Effect.md) (2 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)
- [Combat Flee](Combat_Flee.md) (1 shared connections)
- [Test Flee Command](Test_Flee_Command.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/stats_random.py`

## Audit Trail

- EXTRACTED: 69 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*