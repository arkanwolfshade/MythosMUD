# Logging MDC Code Review

> 14 nodes · cohesion 0.24

## Key Concepts

- **skills_commands.py** (15 connections) — `server/commands/skills_commands.py`
- **handle_skills_command()** (11 connections) — `server/commands/skills_commands.py`
- **_get_container_services()** (6 connections) — `server/commands/skills_commands.py`
- **Any** (5 connections)
- **_resolve_player_id()** (5 connections) — `server/commands/skills_commands.py`
- **_format_skills_output()** (4 connections) — `server/commands/skills_commands.py`
- **_resolve_user_id()** (4 connections) — `server/commands/skills_commands.py`
- **UUID** (2 connections)
- **Skills command handler (plan 10.7 V4).  Returns the active character's skills as** (1 connections) — `server/commands/skills_commands.py`
- **Get container, persistence, and skill_service from request, or None if unavailab** (1 connections) — `server/commands/skills_commands.py`
- **Extract and validate player_id from player object, returning UUID or None.** (1 connections) — `server/commands/skills_commands.py`
- **Resolve user_id from current_user (auth user) or fallback to player.user_id.** (1 connections) — `server/commands/skills_commands.py`
- **Format skills list as text output lines.** (1 connections) — `server/commands/skills_commands.py`
- **Handle the /skills command: return the active character's skills as text.      R** (1 connections) — `server/commands/skills_commands.py`

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (6 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [NPC Event Handler Tests](NPC_Event_Handler_Tests.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`

## Audit Trail

- EXTRACTED: 55 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*