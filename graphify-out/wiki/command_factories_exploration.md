# command factories exploration

> 77 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **Any** (10 connections)
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (6 connections)
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **_flee_effect_validate_room_exits()** (5 connections) — `server/game/magic/spell_effect_flee.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 52 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (22 shared connections)
- [target resolution service](target_resolution_service.md) (15 shared connections)
- [game models player](game_models_player.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (4 shared connections)
- [command utility models](command_utility_models.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [movement monitor game](movement_monitor_game.md) (2 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [combat flee commands](combat_flee_commands.md) (2 shared connections)
- [spell game magic](spell_game_magic.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`
- `server/services/combat_flee_handler.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 377 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*