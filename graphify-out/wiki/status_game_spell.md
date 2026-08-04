# status game spell

> 19 nodes

## Key Concepts

- **SkillService** (37 connections) — `server/game/skill_service.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **Service for skills catalog, per-character skills, use logging, and improvement r** (1 connections) — `server/game/skill_service.py`
- **Return list of skill dicts (id, key, name, base_value, allow_at_creation, catego** (1 connections) — `server/game/skill_service.py`
- **Raise ValueError if occupation_slots are not exactly one 70, two 60, three 50, t** (1 connections) — `server/game/skill_service.py`
- **Require exactly 4 skill_ids; Cthulhu Mythos not allowed; all skill_ids unique.** (1 connections) — `server/game/skill_service.py`
- **Raise ValueError if any skill_id appears in both occupation and personal interes** (1 connections) — `server/game/skill_service.py`
- **Build skill_key -> total modifier from profession skill_modifiers (supports skil** (1 connections) — `server/game/skill_service.py`
- **Compute final skill_id -> value: base + profession mod, then occupation overlay,** (1 connections) — `server/game/skill_service.py`
- **Validate skills allocation without persisting. Raises ValueError if invalid.** (1 connections) — `server/game/skill_service.py`
- **Set all skills for a character at creation.          Validates occupation_slots** (1 connections) — `server/game/skill_service.py`

## Relationships

- [skill service game](skill_service_game.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [profession game service](profession_game_service.md) (3 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [shutdown commands admin](shutdown_commands_admin.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 93 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*