# endpoints auth rationale

> 183 nodes

## Key Concepts

- **DatabaseError** (497 connections) — `server/exceptions.py`
- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **PlayerSkillRepository** (25 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_repository.py** (18 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **player_position_service.py** (17 connections) — `server/services/player_position_service.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_player_connection_setup.py** (16 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **skill.py** (12 connections) — `server/models/skill.py`
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **_manager()** (11 connections) — `server/tests/unit/realtime/test_player_connection_setup.py`
- **player_skill.py** (10 connections) — `server/models/player_skill.py`
- **test_skill_use_log_repository.py** (10 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_by_player_id()** (8 connections) — `server/persistence/repositories/player_skill_repository.py`
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **.get_all_skills()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- *... and 158 more nodes in this community*

## Relationships

- [commands party examples](commands_party_examples.md) (45 shared connections)
- [add used user](add_used_user.md) (42 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (41 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (33 shared connections)
- [position player service](position_player_service.md) (30 shared connections)
- [level curve game](level_curve_game.md) (23 shared connections)
- [player room realtime](player_room_realtime.md) (23 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (18 shared connections)
- [command combat models](command_combat_models.md) (15 shared connections)
- [movement service game](movement_service_game.md) (15 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (14 shared connections)
- [game weapon player](game_weapon_player.md) (11 shared connections)

## Source Files

- `scripts/populate_test_npc_databases.py`
- `server/exceptions.py`
- `server/game/skill_service.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/services/player_position_service.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/game/test_skill_service.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- `server/tests/unit/realtime/test_player_connection_setup.py`
- `server/tests/unit/services/test_player_position_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 829 (69%)
- INFERRED: 372 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*