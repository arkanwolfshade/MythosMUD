# Disconnect Grace Period

> 105 nodes

## Key Concepts

- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **player_requests.py** (14 connections) — `server/schemas/players/player_requests.py`
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
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **SelectCharacterRequest** (8 connections) — `server/schemas/players/player_requests.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **UUID** (7 connections)
- **profession.py** (7 connections) — `server/schemas/players/profession.py`
- **ProfessionResponse** (7 connections) — `server/schemas/players/profession.py`
- **FastAPIRequest** (6 connections)
- *... and 80 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (44 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (16 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (10 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (7 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (6 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (1 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 499 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*