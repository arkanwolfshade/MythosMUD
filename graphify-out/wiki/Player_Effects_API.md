# Player Effects API

> 100 nodes · cohesion 0.04

## Key Concepts

- **player_effects.py** (29 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (26 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **RollStatsRequest** (16 connections) — `server/schemas/players/player_requests.py`
- **CreateCharacterRequest** (15 connections) — `server/schemas/players/player_requests.py`
- **player_requests.py** (13 connections) — `server/schemas/players/player_requests.py`
- **apply_lucidity_loss()** (12 connections) — `server/api/player_effects.py`
- **apply_corruption()** (11 connections) — `server/api/player_effects.py`
- **apply_fear()** (11 connections) — `server/api/player_effects.py`
- **damage_player()** (11 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (11 connections) — `server/api/player_effects.py`
- **heal_player()** (11 connections) — `server/api/player_effects.py`
- **DamageRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **LucidityLossRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **FearRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **SelectCharacterRequest** (7 connections) — `server/schemas/players/player_requests.py`
- **UUID** (7 connections) — `server/api/player_effects.py`
- **EffectResponse** (6 connections) — `server/api/player_effects.py`
- **FastAPIRequest** (6 connections) — `server/api/player_effects.py`
- **PlayerService** (6 connections) — `server/api/player_effects.py`
- **User** (6 connections) — `server/api/player_effects.py`
- *... and 75 more nodes in this community*

## Relationships

- [[Admin NPC Schemas]] (23 shared connections)
- [[Character Creation API]] (16 shared connections)
- [[NPC Admin API]] (11 shared connections)
- [[Container Exception Handlers]] (8 shared connections)
- [[Players API Endpoints]] (2 shared connections)
- [[Pydantic Error Handlers]] (2 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[API Test Fixtures]] (1 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 450 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
