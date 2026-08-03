# calendar models rationale

> 18 nodes

## Key Concepts

- **test_level_service.py** (16 connections) — `server/tests/unit/game/test_level_service.py`
- **level_service()** (3 connections) — `server/tests/unit/game/test_level_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **sample_player()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_zero_no_op()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_negative_raises()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_player_not_found_raises()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **test_grant_xp_increases_xp_and_persists()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **test_check_level_up_player_not_found_raises()** (2 connections) — `server/tests/unit/game/test_level_service.py`
- **Unit tests for LevelService: grant_xp, check_level_up, level-up hook.  Character** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **Mock async persistence with get_player_by_id and save_player.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **LevelService with mocked persistence.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **Player-like object with experience_points and level.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp(amount=0) does not load or save.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp(amount < 0) raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp when player not found raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **grant_xp adds amount to experience_points and saves (level unchanged).** (1 connections) — `server/tests/unit/game/test_level_service.py`
- **check_level_up when player not found raises ValueError.** (1 connections) — `server/tests/unit/game/test_level_service.py`

## Relationships

- [message formatters realtime](message_formatters_realtime.md) (3 shared connections)
- [quests players rationale](quests_players_rationale.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_level_service.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*