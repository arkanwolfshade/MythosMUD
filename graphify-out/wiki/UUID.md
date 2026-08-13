# UUID

> 9 nodes

## Key Concepts

- **UUID** (5 connections)
- **.get_original_string_id()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **.get_player_by_id()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **.damage_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **.heal_player()** (3 connections) — `server/game/magic/spell_effect_types.py`
- **Apply healing to a player by id.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Apply typed damage to a player; returns damage result payload.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Load player by id; None if missing.** (1 connections) — `server/game/magic/spell_effect_types.py`
- **Return registry string id for npc_uuid, or None if unmapped.** (1 connections) — `server/game/magic/spell_effect_types.py`

## Relationships

- [PlayerService](PlayerService.md) (5 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*