# SkillUseLogRepository

> 9 nodes

## Key Concepts

- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **.__init__()** (5 connections) — `server/game/skill_service.py`
- **.get_skill_ids_used_at_level()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **.record_use()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **UUID** (3 connections)
- **.__init__()** (2 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **Repository for skill_use_log: insert, get distinct skills used at a level.** (1 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **Insert one skill_use_log row.** (1 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **Return distinct skill_ids that the player used at the given character level.…** (1 connections) — `server/persistence/repositories/skill_use_log_repository.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [test_skill_use_log_repository.py](test_skill_use_log_repository.py.md) (2 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [._init_player_quest_layer](_init_player_quest_layer.md) (1 shared connections)
- [bundles/game.py](bundles-game.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [PlayerSkillRepository](PlayerSkillRepository.md) (1 shared connections)
- [SkillRepository](SkillRepository.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/persistence/repositories/skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 25 (86%)
- INFERRED: 4 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*