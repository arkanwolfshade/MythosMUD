# Test Skill Service

> 120 nodes

## Key Concepts

- **test_skill_service.py** (37 connections) — `server/tests/unit/game/test_skill_service.py`
- **SkillService** (36 connections) — `server/game/skill_service.py`
- **asyncio** (23 connections)
- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **test_skills_commands.py** (12 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **handle_skills_command()** (11 connections) — `server/commands/skills_commands.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **_get_container_services()** (8 connections) — `server/commands/skills_commands.py`
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **UUID** (7 connections)
- **_resolve_player_id()** (6 connections) — `server/commands/skills_commands.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **fixture** (6 connections)
- **_format_skills_output()** (5 connections) — `server/commands/skills_commands.py`
- **_resolve_user_id()** (5 connections) — `server/commands/skills_commands.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **skill_service()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_occupation_rejected()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_occupation_skill_ids_raises()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 95 more nodes in this community*

## Relationships

- [Player Skill Repository](Player_Skill_Repository.md) (18 shared connections)
- [Character Creation API](Character_Creation_API.md) (5 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (1 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Test Command Parser](Test_Command_Parser.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/game/skill_service.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 233 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*