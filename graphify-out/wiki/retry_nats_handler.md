# retry nats handler

> 90 nodes

## Key Concepts

- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_internal.py** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_internal.py`
- **Protocol** (7 connections)
- **_add_healing_threat_if_in_combat()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_lookup_npc_by_id_or_uuid()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **_is_heal_other_self_target()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_player_damage()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_resolve_npc_id_for_event()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 65 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (42 shared connections)
- [models npc rationale](models_npc_rationale.md) (17 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (11 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [game models player](game_models_player.md) (3 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (3 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (2 shared connections)
- [command factories communication](command_factories_communication.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (2 shared connections)
- [logging setup structured](logging_setup_structured.md) (2 shared connections)
- [quest game service](quest_game_service.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`

## Audit Trail

- EXTRACTED: 411 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*