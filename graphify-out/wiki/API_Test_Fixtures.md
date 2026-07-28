# API Test Fixtures

> 70 nodes · cohesion 0.02

## Key Concepts

- **test_player_service.py** (54 connections) — `server/tests/unit/game/test_player_service.py`
- **player_service()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_name_exists()** (4 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_corruption_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_fear_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_lucidity_loss_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_name_exists()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_with_stats_success()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_damage_player_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_delete_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_delete_player_persistence_fails()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_gain_occult_knowledge_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_heal_player_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_player_service_init()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_soft_delete_character_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_soft_delete_character_persistence_fails()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_soft_delete_character_wrong_user()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **test_update_player_location_player_not_found()** (3 connections) — `server/tests/unit/game/test_player_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_corruption()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_fear()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_apply_lucidity_loss()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_create_player_success()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_damage_player()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- **test_delete_player_success()** (2 connections) — `server/tests/unit/game/test_player_service.py`
- *... and 45 more nodes in this community*

## Relationships

- [Api Player Respawn](Api_Player_Respawn.md) (13 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (4 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (4 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (3 shared connections)
- [Commands Npc Admin](Commands_Npc_Admin.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_player_service.py`

## Audit Trail

- EXTRACTED: 174 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*