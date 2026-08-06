# profession game service

> 88 nodes

## Key Concepts

- **player_effects.py** (30 connections) — `server/api/player_effects.py`
- **test_player_requests.py** (29 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **player_requests.py** (15 connections) — `server/schemas/players/player_requests.py`
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
- **_user()** (8 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **UUID** (7 connections)
- **FastAPIRequest** (6 connections)
- **test_apply_lucidity_loss_validation_maps_to_404()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_lucidity_loss_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_fear_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_corruption_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- *... and 63 more nodes in this community*

## Relationships

- [add used user](add_used_user.md) (11 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (11 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (9 shared connections)
- [player service game](player_service_game.md) (9 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (7 shared connections)
- [player requests schemas](player_requests_schemas.md) (7 shared connections)
- [Player Stats](Player_Stats.md) (6 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 412 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*