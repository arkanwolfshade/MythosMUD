# Game Magic Spell

> 21 nodes · cohesion 0.18

## Key Concepts

- **spell_effects_support.py** (14 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **Any** (7 connections) — `server/game/magic/spell_effects_support.py`
- **_create_object_for_room()** (6 connections) — `server/game/magic/spell_effects_support.py`
- **Spell** (6 connections) — `server/game/magic/spell_effects_support.py`
- **TargetMatch** (6 connections) — `server/game/magic/spell_effects_support.py`
- **_build_stat_modifications()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **_create_object_for_player()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **apply_stat_modifications()** (4 connections) — `server/game/magic/spell_effects_stats.py`
- **spell_effects_stats.py** (3 connections) — `server/game/magic/spell_effects_stats.py`
- **Stat modification helpers for spell effects.  This module contains utility fun** (1 connections) — `server/game/magic/spell_effects_stats.py`
- **Apply stat modification dict to stats.      Returns (updated stats, stat_chang** (1 connections) — `server/game/magic/spell_effects_stats.py`
- **Support helpers for spell effects that would otherwise bloat spell_effects.py.** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Process stat modification effect for a player target.      Delegated from SpellE** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Process object creation effect (delegated from SpellEffects).** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Create objects in a player's inventory.** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Handle object creation targeting a room.      Currently a placeholder until Item** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Build normalized stat_modifications dict from spell.effect_data.      Supports b** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Apply stat modifications (and optional BUFF status) to a player.** (1 connections) — `server/game/magic/spell_effects_support.py`

## Relationships

- [[Spell Registry Costs]] (4 shared connections)
- [[Spell Effect Protocols]] (4 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Status Effect Model]] (2 shared connections)
- [[Combat Command Handler]] (2 shared connections)
- [[Game Magic Spell]] (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
