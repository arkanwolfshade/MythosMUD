# get_logger

> 342 nodes

## Key Concepts

- **log_and_raise()** (157 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (93 connections) — `server/database.py`
- **test_quest_instance_repository.py** (23 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **player_effect_repository.py** (22 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_spell_repository.py** (22 connections) — `server/persistence/repositories/player_spell_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **test_quest_definition_repository.py** (21 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **ContainerTransferToMixin** (20 connections) — `server/services/container_service_transfer_to.py`
- **quest_instance_repository.py** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **PlayerSpell** (19 connections) — `server/models/player_spells.py`
- **profession_repository.py** (19 connections) — `server/persistence/repositories/profession_repository.py`
- **test_profession_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **ContainerSessionMixin** (18 connections) — `server/services/container_service_session.py`
- **QuestInstanceRepository** (17 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **quest_definition_repository.py** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **test_quest_flow.py** (17 connections) — `server/tests/integration/test_quest_flow.py`
- **PlayerEffectRepository** (16 connections) — `server/persistence/repositories/player_effect_repository.py`
- **QuestDefinitionRepository** (14 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **ContainerLockMixin** (14 connections) — `server/services/container_service_lock.py`
- **models/quest.py** (14 connections) — `server/models/quest.py`
- **QuestDefinition** (13 connections) — `server/models/quest.py`
- **_make_session_context()** (13 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **._execute_transfer_to_container()** (12 connections) — `server/services/container_service_transfer_to.py`
- **ProfessionRepository** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- *... and 317 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (144 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (38 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (23 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (17 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (11 shared connections)
- [Any](Any.md) (10 shared connections)
- [useGameTerminal.ts](useGameTerminal.ts.md) (10 shared connections)
- [Room](Room.md) (9 shared connections)
- [testing_examples.py](testing_examples.py.md) (9 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (8 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (8 shared connections)
- [Dependency Upgrade](Dependency_Upgrade.md) (7 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/async_persistence_direct_queries.py`
- `server/database.py`
- `server/models/player_spells.py`
- `server/models/quest.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/quest_definition_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/services/container_service_access.py`
- `server/services/container_service_lock.py`

## Audit Trail

- EXTRACTED: 969 (95%)
- INFERRED: 50 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*