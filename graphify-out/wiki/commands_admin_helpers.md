# commands admin helpers

> 119 nodes

## Key Concepts

- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **RollStatsRequest** (20 connections) — `server/schemas/players/player_requests.py`
- **CreateCharacterRequest** (17 connections) — `server/schemas/players/player_requests.py`
- **player_requests.py** (15 connections) — `server/schemas/players/player_requests.py`
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
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **SelectCharacterRequest** (10 connections) — `server/schemas/players/player_requests.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **UUID** (7 connections)
- *... and 94 more nodes in this community*

## Relationships

- [combat npc service](combat_npc_service.md) (24 shared connections)
- [Player Stats](Player_Stats.md) (22 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (15 shared connections)
- [command inventory models](command_inventory_models.md) (12 shared connections)
- [player requests schemas](player_requests_schemas.md) (8 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [invite models rationale](invite_models_rationale.md) (6 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (3 shared connections)
- [error websocket handler](error_websocket_handler.md) (3 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (2 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 562 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*