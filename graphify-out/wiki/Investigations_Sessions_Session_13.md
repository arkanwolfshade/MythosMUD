# Investigations Sessions Session

> 17 nodes

## Key Concepts

- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **Any** (6 connections)
- **_create_object_for_room()** (6 connections) — `server/game/magic/spell_effects_support.py`
- **_build_stat_modifications()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **_create_object_for_player()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **apply_stat_modifications()** (4 connections) — `server/game/magic/spell_effects_stats.py`
- **Apply stat modification dict to stats.      Returns (updated stats, stat_chang** (1 connections) — `server/game/magic/spell_effects_stats.py`
- **Support helpers for spell effects that would otherwise bloat spell_effects.py.** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Build normalized stat_modifications dict from spell.effect_data.      Supports b** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Apply stat modifications (and optional BUFF status) to a player.** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Process stat modification effect for a player target.      Delegated from SpellE** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Process object creation effect (delegated from SpellEffects).** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Create objects in a player's inventory.** (1 connections) — `server/game/magic/spell_effects_support.py`
- **Handle object creation targeting a room.      Currently a placeholder until Item** (1 connections) — `server/game/magic/spell_effects_support.py`

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (7 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (7 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (2 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (1 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*