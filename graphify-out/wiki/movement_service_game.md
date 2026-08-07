# movement service game

> 55 nodes

## Key Concepts

- **SkillService** (37 connections) — `server/game/skill_service.py`
- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **test_skills_commands.py** (11 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **handle_skills_command()** (10 connections) — `server/commands/skills_commands.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
- **_get_container_services()** (6 connections) — `server/commands/skills_commands.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **Any** (5 connections)
- **_resolve_player_id()** (5 connections) — `server/commands/skills_commands.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **_resolve_user_id()** (4 connections) — `server/commands/skills_commands.py`
- **_format_skills_output()** (4 connections) — `server/commands/skills_commands.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **skill_service()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (15 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [combat npc service](combat_npc_service.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/game/skill_service.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 204 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*