# Game Magic Spell

> 125 nodes · cohesion 0.04

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (84 connections) — `server/models/spell.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (8 connections) — `server/game/magic/spell_effects.py`
- *... and 100 more nodes in this community*

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (41 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (39 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (39 shared connections)
- [Command Service Tests](Command_Service_Tests.md) (20 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (17 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (15 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (12 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (8 shared connections)
- [Commands Go Command](Commands_Go_Command.md) (7 shared connections)
- [Cursor Plans Uvicorn](Cursor_Plans_Uvicorn.md) (7 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (6 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 785 (95%)
- INFERRED: 43 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*