# coercion int inventory

> 6 nodes

## Key Concepts

- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **test_corruption_request_validation()** (4 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **test_corruption_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Request model for applying corruption.** (1 connections) — `server/schemas/players/player_requests.py`
- **Test CorruptionRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Test CorruptionRequest validates amount range.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`

## Relationships

- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (2 shared connections)
- [player schemas requests](player_schemas_requests.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/schemas/players/player_requests.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*