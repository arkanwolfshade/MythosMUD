# Player Respawn Service

> 183 nodes

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **SpellEffectPlayer** (15 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **UUID** (12 connections)
- **TargetMetadata** (12 connections) — `server/schemas/shared/target_metadata.py`
- **PlayerPersistenceSpellPort** (11 connections) — `server/game/magic/spell_effect_types.py`
- **Any** (10 connections)
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- *... and 158 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (74 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (50 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (27 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (21 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (8 shared connections)
- [Test Refactoring Complete](Test_Refactoring_Complete.md) (5 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (5 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (4 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (3 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/game.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 827 (95%)
- INFERRED: 47 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*