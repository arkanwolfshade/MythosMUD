# CacheManager

> 22 nodes

## Key Concepts

- **handle_skills_command()** (12 connections) — `server/commands/skills_commands.py`
- **test_skills_commands.py** (12 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **_get_container_services()** (8 connections) — `server/commands/skills_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/skills_commands.py`
- **_format_skills_output()** (5 connections) — `server/commands/skills_commands.py`
- **_resolve_user_id()** (5 connections) — `server/commands/skills_commands.py`
- **Any** (5 connections)
- **test_get_container_services_ok()** (3 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **test_handle_skills_command_no_services()** (3 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **test_handle_skills_command_success()** (3 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **test_format_skills_output()** (2 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **test_get_container_services_missing()** (2 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **test_resolve_player_id_from_string()** (2 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **test_resolve_user_id_from_dict()** (2 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **UUID** (2 connections)
- **asyncio** (2 connections)
- **Get container, persistence, and skill_service from request, or None if…** (1 connections) — `server/commands/skills_commands.py`
- **Extract and validate player_id from player object, returning UUID or None.** (1 connections) — `server/commands/skills_commands.py`
- **Resolve user_id from current_user (auth user) or fallback to player.user_id.** (1 connections) — `server/commands/skills_commands.py`
- **Format skills list as text output lines.** (1 connections) — `server/commands/skills_commands.py`
- **Handle the /skills command: return the active character's skills as text.…** (1 connections) — `server/commands/skills_commands.py`
- **Unit tests for skills command helpers.** (1 connections) — `server/tests/unit/commands/test_skills_commands.py`

## Relationships

- [TargetResolutionService](TargetResolutionService.md) (11 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [main](main.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/tests/unit/commands/test_skills_commands.py`

## Audit Trail

- EXTRACTED: 44 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*