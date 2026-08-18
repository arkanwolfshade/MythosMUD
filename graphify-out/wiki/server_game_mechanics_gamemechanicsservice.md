# server game mechanics gamemechanicsservice

> 57 nodes

## Key Concepts

- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **GameMechanicsService** (27 connections) — `server/game/mechanics.py`
- **test_mechanics.py** (17 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **asyncio** (10 connections)
- **_player()** (8 connections) — `server/tests/unit/game/test_mechanics.py`
- **asyncio** (8 connections)
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.gain_occult_knowledge()** (4 connections) — `server/game/mechanics.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_apply_corruption_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_fear_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_player_not_found()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_apply_lucidity_loss_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_damage_player_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_experience_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_gain_occult_knowledge_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_heal_player_success()** (4 connections) — `server/tests/unit/game/test_mechanics.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_player_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **.apply_corruption()** (3 connections) — `server/game/mechanics.py`
- **.apply_fear()** (3 connections) — `server/game/mechanics.py`
- **.apply_lucidity_loss()** (3 connections) — `server/game/mechanics.py`
- **.damage_player()** (3 connections) — `server/game/mechanics.py`
- **.gain_experience()** (3 connections) — `server/game/mechanics.py`
- *... and 32 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (19 shared connections)
- [server game mechanics](server_game_mechanics.md) (7 shared connections)
- [server config init](server_config_init.md) (2 shared connections)
- [server async persistence](server_async_persistence.md) (2 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (2 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server async persistence asyncpersistencelayer init](server_async_persistence_asyncpersistencelayer_init.md) (1 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/game/mechanics.py`
- `server/persistence/repositories/experience_repository.py`
- `server/tests/unit/game/test_mechanics.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`

## Audit Trail

- EXTRACTED: 116 (83%)
- INFERRED: 24 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*