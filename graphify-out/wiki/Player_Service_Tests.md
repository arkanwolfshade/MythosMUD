# Player Service Tests

> 92 nodes · cohesion 0.02

## Key Concepts

- **test_player_service.py** (53 connections) — `server/tests/unit/game/test_player_service.py`
- **Test get_player_by_name() when player is found.** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_character_limit()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_name_exists()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_success()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **Test validate_player_name() with name too short.** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **Test get_player_by_id() when player is found.** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_corruption()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_corruption_player_not_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_fear()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_fear_player_not_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_lucidity_loss()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_lucidity_loss_player_not_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_name_exists()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_success()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_damage_player()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_damage_player_player_not_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_delete_player_not_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_delete_player_persistence_fails()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_delete_player_success()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_gain_occult_knowledge()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_gain_occult_knowledge_player_not_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_get_online_players()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_get_player_by_id_found()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- *... and 67 more nodes in this community*

## Relationships

- [[Character Stats Model]] (4 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[Player Respawn Service]] (1 shared connections)
- [[Player Death Service Tests]] (1 shared connections)
- [[Async Persistence Core]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`

## Audit Trail

- EXTRACTED: 198 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
