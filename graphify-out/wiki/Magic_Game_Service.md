# Magic Game Service

> 24 nodes · cohesion 0.17

## Key Concepts

- **UUID** (19 connections) — `server/game/magic/magic_service_completion.py`
- **Any** (18 connections) — `server/game/magic/magic_service_completion.py`
- **magic_service_completion.py** (16 connections) — `server/game/magic/magic_service_completion.py`
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **TargetMatch** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **Casting completion flow for spellcasting.  Mixin that handles completing a casti** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs and process effects.          Args:             player_id: Pla** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Parse target_id from casting state. Returns None if missing or invalid.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply costs and queue spell for next combat round. Returns True if queued, False** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Apply spell costs/effects, send completion message and healing event.** (1 connections) — `server/game/magic/magic_service_completion.py`
- **If in combat, try to queue spell for next round. Return True if queued, False ot** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Complete a casting and apply spell effects.          In combat, spells are queue** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Get player and room_id for casting completion.          Returns:             Tup** (1 connections) — `server/game/magic/magic_service_completion.py`
- **Recreate target from stored casting state.          Args:             casting_st** (1 connections) — `server/game/magic/magic_service_completion.py`

## Relationships

- [[Magic Service Bundle]] (25 shared connections)
- [[Combat Command Handler]] (7 shared connections)
- [[Spell Effect Protocols]] (4 shared connections)
- [[Combat Service Bundle]] (4 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Database Manager Tests]] (1 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`

## Audit Trail

- EXTRACTED: 112 (84%)
- INFERRED: 22 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
