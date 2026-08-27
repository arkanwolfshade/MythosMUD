# NPCCombatRewards

> 24 nodes

## Key Concepts

- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **asyncio** (8 connections)
- **test_respawn_player_from_delirium_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_validation_error()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_delirium_unexpected_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_no_session()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_success()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_unexpected_error()** (5 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **Request** (5 connections)
- **_respawn_payload()** (3 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **post** (2 connections)
- **Any** (1 connections)
- **Respawn a delirious player at the Sanitarium with restored lucidity. This…** (1 connections) — `server/api/player_respawn.py`
- **Respawn a dead player at their respawn location with full DP. This endpoint…** (1 connections) — `server/api/player_respawn.py`
- **Execute a respawn service call inside a DB session with shared error handling.** (1 connections) — `server/api/player_respawn.py`
- **Response model for player respawn endpoints.** (1 connections) — `server/schemas/players/player_respawn.py`
- **Unit tests for player_respawn API endpoints.** (1 connections) — `server/tests/unit/api/test_player_respawn_api.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (17 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (8 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (3 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [maps.py](maps.py.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_api.py`

## Audit Trail

- EXTRACTED: 76 (87%)
- INFERRED: 11 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*