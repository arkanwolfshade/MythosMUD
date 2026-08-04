# npc threading rationale

> 16 nodes

## Key Concepts

- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **handle_skills_command()** (10 connections) — `server/commands/skills_commands.py`
- **_get_container_services()** (6 connections) — `server/commands/skills_commands.py`
- **Any** (5 connections)
- **_resolve_player_id()** (5 connections) — `server/commands/skills_commands.py`
- **_resolve_user_id()** (4 connections) — `server/commands/skills_commands.py`
- **_format_skills_output()** (4 connections) — `server/commands/skills_commands.py`
- **skill_service()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **UUID** (2 connections)
- **Skills command handler (plan 10.7 V4).  Returns the active character's skills as** (1 connections) — `server/commands/skills_commands.py`
- **Get container, persistence, and skill_service from request, or None if unavailab** (1 connections) — `server/commands/skills_commands.py`
- **Extract and validate player_id from player object, returning UUID or None.** (1 connections) — `server/commands/skills_commands.py`
- **Resolve user_id from current_user (auth user) or fallback to player.user_id.** (1 connections) — `server/commands/skills_commands.py`
- **Format skills list as text output lines.** (1 connections) — `server/commands/skills_commands.py`
- **Handle the /skills command: return the active character's skills as text.      R** (1 connections) — `server/commands/skills_commands.py`
- **SkillService with mocks.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [status game spell](status_game_spell.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 60 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*