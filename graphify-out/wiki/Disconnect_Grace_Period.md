# Disconnect Grace Period

> 112 nodes

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
- **ProfessionListResponse** (7 connections) — `server/schemas/players/profession.py`
- **ProfessionResponse** (7 connections) — `server/schemas/players/profession.py`
- *... and 87 more nodes in this community*

## Relationships

- [Game Mechanics Service](Game_Mechanics_Service.md) (18 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (9 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (8 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (7 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (6 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (4 shared connections)
- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (3 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/player_respawn.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 521 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*