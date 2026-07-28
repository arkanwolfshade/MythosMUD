# Player Effects API

> 94 nodes · cohesion 0.04

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **StatsGenerator** (35 connections) — `server/game/stats_generator.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **ProfessionService** (17 connections) — `server/game/profession_service.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- **CreateCharacterResponse** (10 connections) — `server/schemas/players/character_creation.py`
- **RolledStats** (10 connections) — `server/schemas/players/stat_values.py`
- **_convert_stat_summary_to_stat_summary_model()** (9 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **ValidateStatsResponse** (9 connections) — `server/schemas/players/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_raw()** (8 connections) — `server/api/character_creation.py`
- **_roll_stats_with_class()** (8 connections) — `server/api/character_creation.py`
- **StatSummary** (8 connections) — `server/schemas/players/character_creation.py`
- **_stats_to_rolled_stats()** (7 connections) — `server/api/character_creation.py`
- **Any** (6 connections)
- **.test_roll_character_stats_profession_not_found()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **.test_roll_character_stats_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- *... and 69 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (23 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (17 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (15 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (15 shared connections)
- [Cursor Commands Remediation](Cursor_Commands_Remediation.md) (11 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (10 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (8 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (5 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (5 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (5 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/game/character_creation_service.py`
- `server/game/profession_service.py`
- `server/game/stats_generator.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`

## Audit Trail

- EXTRACTED: 446 (94%)
- INFERRED: 31 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*