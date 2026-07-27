# Game Magic Spell

> 25 nodes · cohesion 0.20

## Key Concepts

- **spell_effects_status.py** (18 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (13 connections) — `server/models/game.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **Spell** (7 connections) — `server/game/magic/spell_effects_status.py`
- **TargetMatch** (7 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (7 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (7 connections) — `server/game/magic/spell_effects_status.py`
- **Status effect spell logic (apply/remove status, force-flee, grace-period checks)** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag. Retu** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a matching status effect from a player.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply a status effect, respecting login grace-period protection.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply or remove a status effect on a player, respecting grace-period rules.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Process status effect: apply/remove on player, or apply to NPC (no persistence).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **True if target is in login grace period and effect is negative (should block).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Load player, append status effect, save; return result dict or error if player n** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Run flee effect when effect_data.force_flee is set; otherwise return None.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Status effects that can be applied to characters.** (1 connections) — `server/models/game.py`

## Relationships

- [[Spell Registry Costs]] (7 shared connections)
- [[Game Magic Spell]] (3 shared connections)
- [[Status Effect Model]] (3 shared connections)
- [[Look Command Helpers]] (2 shared connections)
- [[Combat Command Handler]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Spell Effect Protocols]] (2 shared connections)
- [[Player Model Inventory]] (2 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Game Enums]] (1 shared connections)
- [[Services Damage Grace]] (1 shared connections)
- [[Memory Profiler Tools]] (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 140 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
