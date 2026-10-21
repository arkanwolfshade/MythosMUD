# test_npc_startup_service.py

> 143 nodes · cohesion 0.03

## Key Concepts

- **SecureBaseModel** (92 connections) — `server/schemas/shared/base.py`
- **test_player_requests.py** (36 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **api/player_effects.py** (35 connections) — `server/api/player_effects.py`
- **test_player_effects_endpoints.py** (31 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **player_requests.py** (19 connections) — `server/schemas/players/player_requests.py`
- **apply_lucidity_loss()** (14 connections) — `server/api/player_effects.py`
- **apply_corruption()** (13 connections) — `server/api/player_effects.py`
- **apply_fear()** (13 connections) — `server/api/player_effects.py`
- **damage_player()** (13 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (13 connections) — `server/api/player_effects.py`
- **heal_player()** (13 connections) — `server/api/player_effects.py`
- **EffectResponse** (13 connections) — `server/schemas/players/player_effects.py`
- **_request()** (13 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **test_integration_cleanup_gate.py** (10 connections) — `server/tests/unit/test_integration_cleanup_gate.py`
- **_test_touches_database()** (9 connections) — `server/tests/fixtures/integration/__init__.py`
- **test_apply_lucidity_loss_validation_maps_to_404()** (9 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_dialogue_tree.py** (9 connections) — `server/tests/unit/schemas/test_dialogue_tree.py`
- **dialogue_tree.py** (8 connections) — `server/schemas/dialogue/dialogue_tree.py`
- *... and 118 more nodes in this community*

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (29 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (25 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (22 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (14 shared connections)
- [NATSService](NATSService.md) (13 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (7 shared connections)
- [test_shutdown_sequence.py](test_shutdown_sequence.py.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [test_look_item.py](test_look_item.py.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/shared/base.py`
- `server/tests/fixtures/integration/__init__.py`
- `server/tests/unit/api/admin/test_dialogue_schemas.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_dialogue_tree.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/schemas/test_room_write.py`
- `server/tests/unit/test_integration_cleanup_gate.py`

## Audit Trail

- EXTRACTED: 419 (95%)
- INFERRED: 23 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*