# game models player

> 135 nodes

## Key Concepts

- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (28 connections) — `server/models/spell.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (22 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_costs.py** (19 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **_HealingService** (17 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellSchool** (15 connections) — `server/models/spell.py`
- **SpellEffectType** (15 connections) — `server/models/spell.py`
- **SpellTargetType** (14 connections) — `server/models/spell.py`
- **SpellRangeType** (12 connections) — `server/models/spell.py`
- **_spell()** (11 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **_spell()** (6 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **_spell()** (6 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **StrEnum** (4 connections)
- **_spell()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_is_heal_other_target()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_send_instant_heal_event_if_applied()** (4 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_mp_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_lucidity_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_with_materials()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_effect_result_has_healing()** (3 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- *... and 110 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (35 shared connections)
- [NPC Combat](NPC_Combat.md) (17 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (11 shared connections)
- [player respawn event](player_respawn_event.md) (8 shared connections)
- [world models rationale](world_models_rationale.md) (6 shared connections)
- [target resolution service](target_resolution_service.md) (5 shared connections)
- [retry nats handler](retry_nats_handler.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (2 shared connections)
- [manager room npcs](manager_room_npcs.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 503 (97%)
- INFERRED: 16 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*