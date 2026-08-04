# profession game service

> 199 nodes

## Key Concepts

- **character_creation.py** (47 connections) — `server/api/character_creation.py`
- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **roll_character_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **_roll_stats_with_profession_preview()** (14 connections) — `server/api/character_creation.py`
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **validate_character_stats()** (13 connections) — `server/api/character_creation.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **TestRollCharacterStats** (13 connections) — `server/tests/unit/api/test_character_creation.py`
- **apply_lucidity_loss()** (12 connections) — `server/api/player_effects.py`
- **EffectResponse** (12 connections) — `server/schemas/players/player_effects.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **apply_fear()** (11 connections) — `server/api/player_effects.py`
- **apply_corruption()** (11 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (11 connections) — `server/api/player_effects.py`
- **heal_player()** (11 connections) — `server/api/player_effects.py`
- **damage_player()** (11 connections) — `server/api/player_effects.py`
- **BaseModel** (11 connections)
- *... and 174 more nodes in this community*

## Relationships

- [Player Stats](Player_Stats.md) (43 shared connections)
- [Exception Containers](Exception_Containers.md) (31 shared connections)
- [player requests schemas](player_requests_schemas.md) (28 shared connections)
- [Loot Generation](Loot_Generation.md) (21 shared connections)
- [NPC Combat](NPC_Combat.md) (16 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (7 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (7 shared connections)
- [event connection helpers](event_connection_helpers.md) (7 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [player service game](player_service_game.md) (5 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (4 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (4 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/player_effects.py`
- `server/commands/admin_shutdown_command.py`
- `server/game/profession_service.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 901 (96%)
- INFERRED: 41 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*