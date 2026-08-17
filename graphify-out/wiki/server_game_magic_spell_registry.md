# server game magic spell registry

> 131 nodes

## Key Concepts

- **SpellEffectType** (45 connections) — `server/models/spell.py`
- **SpellSchool** (37 connections) — `server/models/spell.py`
- **SpellTargetType** (34 connections) — `server/models/spell.py`
- **SpellRangeType** (32 connections) — `server/models/spell.py`
- **test_spell.py** (32 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (29 connections) — `server/models/spell.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (23 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_magic_healing_events.py** (21 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_costs.py** (20 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (19 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **_spell()** (15 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **_HealingService** (12 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **_spell()** (10 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_get_combat_target_auto_selects_opponent()** (10 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_spell()** (9 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **self_spell()** (8 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_with_materials()** (8 connections) — `server/tests/unit/models/test_spell.py`
- **asyncio** (8 connections)
- **base_spell()** (7 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **area_spell()** (7 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **entity_spell()** (7 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_default_values()** (7 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_false()** (7 connections) — `server/tests/unit/models/test_spell.py`
- *... and 106 more nodes in this community*

## Relationships

- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (31 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (14 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (12 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (11 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (10 shared connections)
- [server game skill service](server_game_skill_service.md) (6 shared connections)
- [characterinfo](characterinfo.md) (5 shared connections)
- [server game magic magic healing](server_game_magic_magic_healing.md) (4 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (2 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (2 shared connections)
- [server game magic spell materials](server_game_magic_spell_materials.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 276 (66%)
- INFERRED: 140 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*