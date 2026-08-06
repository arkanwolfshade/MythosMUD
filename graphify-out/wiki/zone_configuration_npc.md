# zone configuration npc

> 30 nodes

## Key Concepts

- **SkillService** (37 connections) — `server/game/skill_service.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
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
- *... and 5 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (3 shared connections)
- [player event handlers](player_event_handlers.md) (3 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [archive QUALITY AUDIT](archive_QUALITY_AUDIT.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`

## Audit Trail

- EXTRACTED: 125 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*