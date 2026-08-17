# server container bundles game gamebundle

> 32 nodes

## Key Concepts

- **SkillService** (38 connections) — `server/game/skill_service.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **UUID** (7 connections)
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **Wire player/room/user, container, skill, level, and quest services.** (1 connections) — `server/container/bundles/game.py`
- **Raise ValueError if any skill_id appears in both occupation and personal…** (1 connections) — `server/game/skill_service.py`
- **Build skill_key -> total modifier from profession skill_modifiers (supports…** (1 connections) — `server/game/skill_service.py`
- **Compute final skill_id -> value: base + profession mod, then occupation…** (1 connections) — `server/game/skill_service.py`
- **Validate skills allocation without persisting. Raises ValueError if invalid.…** (1 connections) — `server/game/skill_service.py`
- **Set all skills for a character at creation. Validates occupation_slots (9…** (1 connections) — `server/game/skill_service.py`
- **Return list of {skill_id, skill_key, skill_name, value} for the player. If the…** (1 connections) — `server/game/skill_service.py`
- **Record one successful use of a skill at the character's current level. Used for…** (1 connections) — `server/game/skill_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [server game skill service](server_game_skill_service.md) (9 shared connections)
- [server api character creation](server_api_character_creation.md) (5 shared connections)
- [server game skill service skillservice](server_game_skill_service_skillservice.md) (5 shared connections)
- [server commands skills commands](server_commands_skills_commands.md) (4 shared connections)
- [server api players](server_api_players.md) (3 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (3 shared connections)
- [leveluphook](leveluphook.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (2 shared connections)
- [maprooms](maprooms.md) (1 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 89 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*