# Invite & NPC DB Scripts

> 371 nodes

## Key Concepts

- **DatabaseError** (297 connections) — `server/exceptions.py`
- **server/exceptions.py** (271 connections) — `server/exceptions.py`
- **get_session_maker()** (111 connections) — `server/database.py`
- **database.py** (88 connections) — `server/database.py`
- **log_and_raise()** (79 connections) — `server/utils/error_logging.py`
- **error_logging.py** (62 connections) — `server/utils/error_logging.py`
- **repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **async_persistence_room_loader.py** (22 connections) — `server/async_persistence_room_loader.py`
- **persistence/container_helpers.py** (22 connections) — `server/persistence/container_helpers.py`
- **npc_service/__init__.py** (22 connections) — `server/services/npc_service/__init__.py`
- **SkillRepository** (21 connections) — `server/persistence/repositories/skill_repository.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **Skill** (20 connections) — `server/models/skill.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **item_catalog_repository.py** (20 connections) — `server/persistence/repositories/item_catalog_repository.py`
- **player_effect_repository.py** (20 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_mute_repository.py** (20 connections) — `server/persistence/repositories/player_mute_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **PlayerSkillRepository** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **profession_repository.py** (18 connections) — `server/persistence/repositories/profession_repository.py`
- **skill_repository.py** (18 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSpell** (17 connections) — `server/models/player_spells.py`
- **PlayerEffectRepository** (16 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 346 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (190 shared connections)
- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (49 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (35 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (35 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (28 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (27 shared connections)
- [Community 492](Community_492.md) (27 shared connections)
- [Community 158](Community_158.md) (21 shared connections)
- [Community 189](Community_189.md) (21 shared connections)
- [Community 312](Community_312.md) (20 shared connections)
- [NPC Behavior Engine](NPC_Behavior_Engine.md) (18 shared connections)
- [Community 51](Community_51.md) (18 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/populate_test_npc_databases.py`
- `server/alias_storage.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_facade.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/movement_room_occupancy.py`
- `server/models/dialogue.py`
- `server/models/player_skill.py`
- `server/models/player_spells.py`
- `server/models/quest.py`
- `server/models/skill.py`
- `server/persistence/container_helpers.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/emote_repository.py`
- `server/persistence/repositories/experience_repository.py`

## Audit Trail

- EXTRACTED: 1578 (90%)
- INFERRED: 171 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*