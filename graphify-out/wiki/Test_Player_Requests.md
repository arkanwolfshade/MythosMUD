# Test Player Requests

> 80 nodes

## Key Concepts

- **test_player_effects_endpoints.py** (29 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **api/player_effects.py** (23 connections) — `server/api/player_effects.py`
- **player_requests.py** (19 connections) — `server/schemas/players/player_requests.py`
- **apply_lucidity_loss()** (14 connections) — `server/api/player_effects.py`
- **apply_corruption()** (13 connections) — `server/api/player_effects.py`
- **apply_fear()** (13 connections) — `server/api/player_effects.py`
- **damage_player()** (13 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (13 connections) — `server/api/player_effects.py`
- **heal_player()** (13 connections) — `server/api/player_effects.py`
- **DamageRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **LucidityLossRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (9 connections) — `server/schemas/players/player_requests.py`
- **FearRequest** (9 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (9 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (9 connections) — `server/schemas/players/player_requests.py`
- **_request()** (9 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **asyncio** (8 connections)
- **test_effect_endpoint_rejects_non_superuser()** (7 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **UUID** (7 connections)
- **test_apply_corruption_success()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_fear_success()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_lucidity_loss_success()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_lucidity_loss_validation_maps_to_404()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_damage_player_success()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- *... and 55 more nodes in this community*

## Relationships

- [NPC Definitions API](NPC_Definitions_API.md) (24 shared connections)
- [Character Creation API](Character_Creation_API.md) (12 shared connections)
- [Npc Admin](Npc_Admin.md) (8 shared connections)
- [Players](Players.md) (7 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (2 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Command Aliases](Command_Aliases.md) (2 shared connections)
- [Test Admin Auth Service](Test_Admin_Auth_Service.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Test Players Api Coverage](Test_Players_Api_Coverage.md) (1 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 199 (86%)
- INFERRED: 32 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*