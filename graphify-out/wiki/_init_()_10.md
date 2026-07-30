# . init ()

> 148 nodes

## Key Concepts

- **Spell** (84 connections) — `server/models/spell.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **SpellMaterialsService** (15 connections) — `server/game/magic/spell_materials.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **spell_materials.py** (10 connections) — `server/game/magic/spell_materials.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **SpellEffectType** (9 connections) — `server/models/spell.py`
- **Any** (8 connections)
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **SpellSchool** (8 connections) — `server/models/spell.py`
- **SpellTargetType** (8 connections) — `server/models/spell.py`
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- *... and 123 more nodes in this community*

## Relationships

- [.end combat()](end_combat%28%29.md) (50 shared connections)
- [message handler factory](message_handler_factory.md) (38 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (13 shared connections)
- [Player](Player.md) (12 shared connections)
- [command execution request](command_execution_request.md) (8 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [test command service](test_command_service.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [login grace period](login_grace_period.md) (3 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 626 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*