# PlayerService

> 268 nodes

## Key Concepts

- **PlayerService** (113 connections) — `server/game/player_service.py`
- **test_player_service_mutations.py** (46 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_player_requests.py** (36 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **api/player_effects.py** (35 connections) — `server/api/player_effects.py`
- **test_player_effects_endpoints.py** (31 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **asyncio** (31 connections)
- **player_requests.py** (19 connections) — `server/schemas/players/player_requests.py`
- **apply_lucidity_loss()** (14 connections) — `server/api/player_effects.py`
- **UUID** (14 connections)
- **EffectResponse** (13 connections) — `server/schemas/players/player_effects.py`
- **apply_corruption()** (13 connections) — `server/api/player_effects.py`
- **apply_fear()** (13 connections) — `server/api/player_effects.py`
- **damage_player()** (13 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (13 connections) — `server/api/player_effects.py`
- **heal_player()** (13 connections) — `server/api/player_effects.py`
- **_request()** (13 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **Any** (11 connections)
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **test_apply_lucidity_loss_validation_maps_to_404()** (9 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- *... and 243 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (106 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [ValidationError](ValidationError.md) (14 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (13 shared connections)
- [magic_service.py](magic_service.py.md) (5 shared connections)
- [ErrorType](ErrorType.md) (5 shared connections)
- [SpellEffects](SpellEffects.md) (4 shared connections)
- [test_integration_cleanup_gate.py](test_integration_cleanup_gate.py.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (3 shared connections)
- [SpellMaterialsService](SpellMaterialsService.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [Stats](Stats.md) (3 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 596 (91%)
- INFERRED: 61 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*