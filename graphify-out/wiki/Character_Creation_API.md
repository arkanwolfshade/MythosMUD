# Character Creation API

> 83 nodes · cohesion 0.04

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (21 connections) — `server/tests/unit/api/test_character_creation.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (14 connections) — `server/api/character_creation.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **TestRollCharacterStats** (14 connections) — `server/tests/unit/api/test_character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **TestCreateCharacterWithStats** (11 connections) — `server/tests/unit/api/test_character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (10 connections) — `server/api/character_creation.py`
- **TestValidateCharacterStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **_stats_to_rolled_stats()** (8 connections) — `server/api/character_creation.py`
- **User** (8 connections) — `server/api/character_creation.py`
- **Any** (6 connections) — `server/api/character_creation.py`
- **_apply_rate_limiting_for_stats_roll()** (5 connections) — `server/api/character_creation.py`
- **_apply_stat_modifiers()** (5 connections) — `server/api/character_creation.py`
- **_validate_user_for_stats_roll()** (5 connections) — `server/api/character_creation.py`
- **.test_create_character_rate_limit()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_profession_not_found()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_rate_limit()** (5 connections) — `server/tests/unit/api/test_character_creation.py`
- **Stats** (5 connections) — `server/api/character_creation.py`
- *... and 58 more nodes in this community*

## Relationships

- [[NPC Admin API]] (16 shared connections)
- [[Player Effects API]] (16 shared connections)
- [[Container Exception Handlers]] (13 shared connections)
- [[Admin NPC Schemas]] (10 shared connections)
- [[Standardized Error Responses]] (8 shared connections)
- [[Admin Shutdown Command]] (7 shared connections)
- [[API Test Fixtures]] (6 shared connections)
- [[Character Stats Model]] (5 shared connections)
- [[Players API Endpoints]] (4 shared connections)
- [[Game Service Bundle]] (2 shared connections)
- [[Argon2 Password Hashing]] (2 shared connections)
- [[WebSocket Player Helpers]] (2 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 381 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
