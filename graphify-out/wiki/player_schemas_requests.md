# player schemas requests

> 12 nodes

## Key Concepts

- **test_player_effects_endpoints.py** (28 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **apply_lucidity_loss()** (12 connections) — `server/api/player_effects.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_lucidity_loss_validation_maps_to_404()** (6 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_lucidity_loss_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_fear_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_apply_corruption_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_damage_player_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **Apply lucidity loss to a player.** (1 connections) — `server/api/player_effects.py`
- **Request model for applying lucidity loss.** (1 connections) — `server/schemas/players/player_requests.py`
- **Unit tests for server.api.player_effects route handlers.** (1 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`

## Relationships

- [player effects endpoints](player_effects_endpoints.md) (12 shared connections)
- [player requests schemas](player_requests_schemas.md) (8 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (4 shared connections)
- [combat messaging service](combat_messaging_service.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`

## Audit Trail

- EXTRACTED: 84 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*