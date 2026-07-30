# real time

> 387 nodes

## Key Concepts

- **DatabaseError** (432 connections) — `server/exceptions.py`
- **exceptions.py** (196 connections) — `server/exceptions.py`
- **log_and_raise()** (164 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **MovementService** (43 connections) — `server/game/movement_service.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **GameMechanicsService** (17 connections) — `server/game/mechanics.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **profession_repository.py** (17 connections) — `server/persistence/repositories/profession_repository.py`
- **skill_repository.py** (17 connections) — `server/persistence/repositories/skill_repository.py`
- **UUID** (16 connections)
- **ExperienceRepository** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **health_repository.py** (16 connections) — `server/persistence/repositories/health_repository.py`
- **exploration_service.py** (16 connections) — `server/services/exploration_service.py`
- **experience_repository.py** (15 connections) — `server/persistence/repositories/experience_repository.py`
- *... and 362 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (89 shared connections)
- [world](world.md) (74 shared connections)
- [close db()](close_db%28%29.md) (58 shared connections)
- [.initialize()](initialize%28%29.md) (53 shared connections)
- [bench cache npc](bench_cache_npc.md) (51 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (38 shared connections)
- [main()](main%28%29.md) (32 shared connections)
- [container persistence](container_persistence.md) (25 shared connections)
- [Player](Player.md) (25 shared connections)
- [spell registry](spell_registry.md) (22 shared connections)
- [datetime](datetime.md) (19 shared connections)
- [Any](Any.md) (19 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/populate_test_npc_databases.py`
- `server/api/skills.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/character_creation_service.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_skill_repository.py`

## Audit Trail

- EXTRACTED: 2134 (83%)
- INFERRED: 429 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*