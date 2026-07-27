# Game Magic Spell

> 11 nodes · cohesion 0.20

## Key Concepts

- **PlayerServiceHealPort** (5 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (5 connections) — `server/game/magic/spell_effect_types.py`
- **.get_original_string_id()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **.get_player_by_id()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **.damage_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **.heal_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **Apply healing to a player by id.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Apply typed damage to a player; returns damage result payload.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Load player by id; None if missing.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Return registry string id for npc_uuid, or None if unmapped.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Player service methods used by heal and steal-life spell paths.** (1 connections) — `server/game/magic/spell_effect_types.py`

## Relationships

- [[Spell Effect Protocols]] (4 shared connections)
- [[Player Combat XP]] (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
