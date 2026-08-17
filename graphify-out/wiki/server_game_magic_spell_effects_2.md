# server game magic spell effects

> 20 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (5 connections)
- **.remove_status_effect()** (3 connections) — `server/models/game.py`
- **Status effect spell logic (apply/remove status, force-flee, grace-period…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Parse effect_data for status-effect type, duration, intensity, remove flag.…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a matching status effect from a player.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply a status effect, respecting login grace-period protection.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Apply or remove a status effect on a player, respecting grace-period rules.** (1 connections) — `server/game/magic/spell_effects_status.py`
- **True if target is in login grace period and effect is negative (should block).** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Load player, append status effect, save; return result dict or error if player…** (1 connections) — `server/game/magic/spell_effects_status.py`
- **Remove a status effect from the player. Args: effect_type: Type of effect to…** (1 connections) — `server/models/game.py`
- **Status effects that can be applied to characters.** (1 connections) — `server/models/game.py`

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (18 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (9 shared connections)
- [server game magic spell effect](server_game_magic_spell_effect.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server game skill service](server_game_skill_service.md) (1 shared connections)
- [server tests unit models test](server_tests_unit_models_test.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (1 shared connections)
- [computed field](computed_field.md) (1 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (1 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 73 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*