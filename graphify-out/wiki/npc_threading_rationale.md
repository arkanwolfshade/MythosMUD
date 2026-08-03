# npc threading rationale

> 14 nodes

## Key Concepts

- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **handle_skills_command()** (10 connections) — `server/commands/skills_commands.py`
- **_get_container_services()** (6 connections) — `server/commands/skills_commands.py`
- **Any** (5 connections)
- **_resolve_player_id()** (5 connections) — `server/commands/skills_commands.py`
- **_resolve_user_id()** (4 connections) — `server/commands/skills_commands.py`
- **_format_skills_output()** (4 connections) — `server/commands/skills_commands.py`
- **UUID** (2 connections)
- **Skills command handler (plan 10.7 V4).  Returns the active character's skills as** (1 connections) — `server/commands/skills_commands.py`
- **Get container, persistence, and skill_service from request, or None if unavailab** (1 connections) — `server/commands/skills_commands.py`
- **Extract and validate player_id from player object, returning UUID or None.** (1 connections) — `server/commands/skills_commands.py`
- **Resolve user_id from current_user (auth user) or fallback to player.user_id.** (1 connections) — `server/commands/skills_commands.py`
- **Format skills list as text output lines.** (1 connections) — `server/commands/skills_commands.py`
- **Handle the /skills command: return the active character's skills as text.      R** (1 connections) — `server/commands/skills_commands.py`

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (5 shared connections)
- [commands position system](commands_position_system.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [command factories create](command_factories_create.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`

## Audit Trail

- EXTRACTED: 56 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*