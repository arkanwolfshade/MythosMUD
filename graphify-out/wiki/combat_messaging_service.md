# combat messaging service

> 9 nodes

## Key Concepts

- **heal_player()** (11 connections) — `server/api/player_effects.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **test_heal_player_success()** (4 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **test_heal_request_validation()** (4 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_heal_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Heal a player's health.** (1 connections) — `server/api/player_effects.py`
- **Request model for healing a player.** (1 connections) — `server/schemas/players/player_requests.py`
- **Test HealRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test HealRequest validates amount range.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`

## Relationships

- [player effects endpoints](player_effects_endpoints.md) (5 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [player schemas requests](player_schemas_requests.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [magic healing game](magic_healing_game.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 36 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*