# Game Magic Spell

> 17 nodes · cohesion 0.27

## Key Concepts

- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effect_flee.py** (14 connections) — `server/game/magic/spell_effect_flee.py`
- **Any** (10 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_failure_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_not_in_combat_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_available()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_success_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_validate_room_exits()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **TargetMatch** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_type_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_room_error_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_unavailable_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **Flee spell effect: voluntary flee mechanics (success roll, lose-attack-on-fail,** (1 connections) — `server/game/magic/spell_effect_flee.py`
- **True if combat, movement, and get_room_by_id are all configured for flee effect.** (1 connections) — `server/game/magic/spell_effect_flee.py`
- **Return (room_id, None) if combat room has exits; else (None, error_message).** (1 connections) — `server/game/magic/spell_effect_flee.py`
- **Apply flee effect: same mechanics as /flee (success roll, lose-attack-on-fail, e** (1 connections) — `server/game/magic/spell_effect_flee.py`

## Relationships

- [[Combat Taunt Tests]] (2 shared connections)
- [[Combat Command Handler]] (2 shared connections)
- [[Spell Effect Protocols]] (2 shared connections)
- [[Game Magic Spell]] (2 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
