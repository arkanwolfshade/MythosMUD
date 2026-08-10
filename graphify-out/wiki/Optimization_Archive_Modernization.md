# Optimization Archive Modernization

> 487 nodes

## Key Concepts

- **DatabaseError** (434 connections) — `server/exceptions.py`
- **log_and_raise()** (174 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **__init__.py** (71 connections) — `server/models/__init__.py`
- **Base** (58 connections) — `server/models/base.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **base.py** (21 connections) — `server/models/base.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_item.py** (19 connections) — `server/tests/unit/models/test_item.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 462 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (207 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (28 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (22 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (19 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (19 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (19 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (17 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (17 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (15 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (14 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (13 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (13 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `monitoring/webhook-receiver.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/models/__init__.py`
- `server/models/alias.py`
- `server/models/base.py`
- `server/models/calendar.py`
- `server/models/emote.py`
- `server/models/invite.py`
- `server/models/item.py`
- `server/models/player_effect.py`
- `server/models/player_skill.py`
- `server/models/player_spells.py`
- `server/models/quest.py`
- `server/models/skill.py`
- `server/models/skill_use_log.py`
- `server/models/spell_db.py`

## Audit Trail

- EXTRACTED: 2255 (82%)
- INFERRED: 496 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*