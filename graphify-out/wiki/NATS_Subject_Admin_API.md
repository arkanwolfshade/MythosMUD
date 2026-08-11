# NATS Subject Admin API

> 16 nodes

## Key Concepts

- **skills_commands.py** (15 connections) — `server/commands/skills_commands.py`
- **handle_skills_command()** (11 connections) — `server/commands/skills_commands.py`
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

- [Chat NATS Publisher](Chat_NATS_Publisher.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 59 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*