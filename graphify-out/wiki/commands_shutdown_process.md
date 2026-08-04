# commands shutdown process

> 192 nodes

## Key Concepts

- **DatabaseError** (497 connections) — `server/exceptions.py`
- **log_and_raise()** (172 connections) — `server/utils/error_logging.py`
- **error_logging.py** (56 connections) — `server/utils/error_logging.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkillRepository** (25 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerSpell** (23 connections) — `server/models/player_spells.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **profession_repository.py** (18 connections) — `server/persistence/repositories/profession_repository.py`
- **skill_repository.py** (18 connections) — `server/persistence/repositories/skill_repository.py`
- **health_repository.py** (17 connections) — `server/persistence/repositories/health_repository.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **skill_use_log_repository.py** (14 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **spell_repository.py** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **test_skill_use_log_repository.py** (10 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- *... and 167 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (63 shared connections)
- [auth users rationale](auth_users_rationale.md) (36 shared connections)
- [persistence container item](persistence_container_item.md) (36 shared connections)
- [NPC Combat](NPC_Combat.md) (32 shared connections)
- [shutdown command commands](shutdown_command_commands.md) (32 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (30 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (26 shared connections)
- [Loot Generation](Loot_Generation.md) (24 shared connections)
- [Spell Validation](Spell_Validation.md) (24 shared connections)
- [persistence container extended](persistence_container_extended.md) (23 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (22 shared connections)
- [game models enums](game_models_enums.md) (20 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/dependencies.py`
- `server/exceptions.py`
- `server/models/player_spells.py`
- `server/persistence/container_query_helpers.py`
- `server/persistence/repositories/dialogue_definition_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/models/test_player_spells.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`

## Audit Trail

- EXTRACTED: 1138 (74%)
- INFERRED: 399 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*