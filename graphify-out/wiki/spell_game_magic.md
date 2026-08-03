# spell game magic

> 106 nodes

## Key Concepts

- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **UUID** (12 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- **._process_teleport()** (8 connections) — `server/game/magic/spell_effects.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **Protocol** (7 connections)
- **._process_damage_to_npc()** (7 connections) — `server/game/magic/spell_effects.py`
- **_add_healing_threat_if_in_combat()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 81 more nodes in this community*

## Relationships

- [game models player](game_models_player.md) (43 shared connections)
- [target resolution service](target_resolution_service.md) (21 shared connections)
- [NPC Combat](NPC_Combat.md) (14 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (6 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)
- [command factories exploration](command_factories_exploration.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`

## Audit Trail

- EXTRACTED: 453 (97%)
- INFERRED: 16 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*