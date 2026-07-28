# Room Service Tests

> 100 nodes · cohesion 0.04

## Key Concepts

- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **player_requests.py** (14 connections) — `server/schemas/players/player_requests.py`
- **apply_lucidity_loss()** (12 connections) — `server/api/player_effects.py`
- **EffectResponse** (12 connections) — `server/schemas/players/player_effects.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **apply_corruption()** (11 connections) — `server/api/player_effects.py`
- **apply_fear()** (11 connections) — `server/api/player_effects.py`
- **damage_player()** (11 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (11 connections) — `server/api/player_effects.py`
- **heal_player()** (11 connections) — `server/api/player_effects.py`
- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **BaseModel** (11 connections)
- **SelectCharacterRequest** (8 connections) — `server/schemas/players/player_requests.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **UUID** (7 connections)
- **FastAPIRequest** (6 connections)
- *... and 75 more nodes in this community*

## Relationships

- [Player Effects API](Player_Effects_API.md) (23 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (14 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (11 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (11 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (9 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (9 shared connections)
- [Cursor Agents Analyzer](Cursor_Agents_Analyzer.md) (6 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (2 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (2 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 505 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*