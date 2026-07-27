# Realtime Connection Impl

> 29 nodes · cohesion 0.02

## Key Concepts

- **DatabaseError** (247 connections) — `server/exceptions.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **Player** (16 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (10 connections) — `server/persistence/repositories/player_repository.py`
- **UUID** (9 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (8 connections) — `server/persistence/repositories/player_skill_repository.py`
- **UUID** (8 connections) — `server/persistence/repositories/player_spell_repository.py`
- **UUID** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **.get_session_maker()** (6 connections) — `server/database.py`
- **datetime** (6 connections) — `server/persistence/repositories/player_repository.py`
- **Any** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **async_sessionmaker** (5 connections) — `server/database.py`
- **AsyncSession** (5 connections) — `server/database.py`
- **Any** (5 connections) — `server/persistence/repositories/player_repository.py`
- **Profession** (5 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (5 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **Any** (4 connections) — `server/persistence/item_instance_persistence.py`
- **Player** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **datetime** (4 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **UUID** (4 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **Any** (4 connections) — `server/persistence/repositories/spell_repository.py`
- **Profession** (3 connections) — `server/async_persistence_direct_queries.py`
- **Player** (3 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Any** (3 connections) — `server/persistence/repositories/player_spell_repository.py`
- **Any** (3 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 4 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (12 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (9 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (5 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (3 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (3 shared connections)
- [Health Cold Resistance](Health_Cold_Resistance.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (2 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (2 shared connections)

## Source Files

- `server/async_persistence_direct_queries.py`
- `server/database.py`
- `server/exceptions.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 309 (65%)
- INFERRED: 166 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*