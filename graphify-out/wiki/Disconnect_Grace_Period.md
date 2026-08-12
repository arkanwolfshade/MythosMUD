# Disconnect Grace Period

> 97 nodes

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
- **FastAPIRequest** (6 connections)
- **test_apply_lucidity_loss_validation_maps_to_404()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **RespawnPlayerData** (4 connections) — `server/schemas/players/player_respawn.py`
- *... and 72 more nodes in this community*

## Relationships

- [Game Mechanics Service](Game_Mechanics_Service.md) (18 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (13 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (10 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (9 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (9 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (7 shared connections)
- [Test Refactoring Deliverables](Test_Refactoring_Deliverables.md) (6 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (4 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (4 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Lucidity Flux Performance Bug](Lucidity_Flux_Performance_Bug.md) (2 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 470 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*