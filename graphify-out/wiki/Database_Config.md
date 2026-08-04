# Database Config

> 513 nodes

## Key Concepts

- **DatabaseError** (497 connections) — `server/exceptions.py`
- **log_and_raise()** (172 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **MovementService** (43 connections) — `server/game/movement_service.py`
- **DialogueDefinitionRepository** (32 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (30 connections) — `server/persistence/repositories/__init__.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **PlayerSkillRepository** (25 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_dialogue_definition_repository.py** (20 connections) — `server/tests/unit/persistence/repositories/test_dialogue_definition_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **QuestInstanceRepository** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **health_repository.py** (17 connections) — `server/persistence/repositories/health_repository.py`
- *... and 488 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (141 shared connections)
- [persistence container item](persistence_container_item.md) (87 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (64 shared connections)
- [combat models rationale](combat_models_rationale.md) (31 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (27 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (26 shared connections)
- [persistence container extended](persistence_container_extended.md) (22 shared connections)
- [world models rationale](world_models_rationale.md) (17 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (15 shared connections)
- [Exception Containers](Exception_Containers.md) (14 shared connections)
- [command commands service](command_commands_service.md) (13 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (13 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/populate_test_npc_databases.py`
- `server/async_persistence.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/dialogue/dialogue_service.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/game/skill_service.py`
- `server/models/dialogue.py`
- `server/models/player_effect.py`
- `server/models/player_spells.py`
- `server/models/quest.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`

## Audit Trail

- EXTRACTED: 2468 (83%)
- INFERRED: 517 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*