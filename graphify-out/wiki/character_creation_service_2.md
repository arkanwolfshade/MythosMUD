# character creation service

> 24 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (6 connections)
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- **Status effect spell logic (apply/remove status, force-flee, grace-period checks)** (1 connections) — `server/game/magic/spell_effects_status.py`
- **True if target is in login grace period and effect is negative (should block).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Load player, append status effect, save; return result dict or error if player n** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Run flee effect when effect_data.force_flee is set; otherwise return None.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag. Retu** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a matching status effect from a player.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply a status effect, respecting login grace-period protection.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply or remove a status effect on a player, respecting grace-period rules.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Process status effect: apply/remove on player, or apply to NPC (no persistence).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Status effects that can be applied to characters.** (1 connections) — `server/models/game.py`
- **Remove a status effect from the player.          Args:             effect_type:** (1 connections) — `server/models/game.py`

## Relationships

- [spell game magic](spell_game_magic.md) (18 shared connections)
- [combat models rationale](combat_models_rationale.md) (4 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (3 shared connections)
- [models invite Any](models_invite_Any.md) (3 shared connections)
- [command utility models](command_utility_models.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [game models player](game_models_player.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 136 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*