# Database Config

> 350 nodes

## Key Concepts

- **DatabaseError** (495 connections) — `server/exceptions.py`
- **log_and_raise()** (172 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **DialogueDefinitionRepository** (32 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **PlayerSkillRepository** (25 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **profession_repository.py** (18 connections) — `server/persistence/repositories/profession_repository.py`
- **skill_repository.py** (18 connections) — `server/persistence/repositories/skill_repository.py`
- **test_profession_repository.py** (18 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **quest_definition_repository.py** (16 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- *... and 325 more nodes in this community*

## Relationships

- [persistence container item](persistence_container_item.md) (65 shared connections)
- [world models rationale](world_models_rationale.md) (65 shared connections)
- [models npc rationale](models_npc_rationale.md) (45 shared connections)
- [command inventory factories](command_inventory_factories.md) (39 shared connections)
- [combat npc services](combat_npc_services.md) (34 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (33 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (22 shared connections)
- [persistence container extended](persistence_container_extended.md) (22 shared connections)
- [effect player repository](effect_player_repository.md) (20 shared connections)
- [schedule services service](schedule_services_service.md) (18 shared connections)
- [nats services metrics](nats_services_metrics.md) (16 shared connections)
- [Room Broadcast](Room_Broadcast.md) (15 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/dependencies.py`
- `server/exceptions.py`
- `server/game/dialogue/dialogue_service.py`
- `server/game/skill_service.py`
- `server/models/dialogue.py`
- `server/models/quest.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 1882 (81%)
- INFERRED: 454 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*