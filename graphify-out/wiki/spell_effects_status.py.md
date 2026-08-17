# spell_effects_status.py

> 22 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (5 connections)
- **Status effect spell logic (apply/remove status, force-flee, grace-period…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag.…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a matching status effect from a player.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply a status effect, respecting login grace-period protection.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply or remove a status effect on a player, respecting grace-period rules.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Process status effect: apply/remove on player, or apply to NPC (no persistence).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **True if target is in login grace period and effect is negative (should block).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Load player, append status effect, save; return result dict or error if player…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Run flee effect when effect_data.force_flee is set; otherwise return None.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Status effects that can be applied to characters.** (1 connections) — `server/models/game.py`

## Relationships

- [TargetMatch](TargetMatch.md) (9 shared connections)
- [Spell](Spell.md) (7 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (4 shared connections)
- [StatusEffect](StatusEffect.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 79 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*