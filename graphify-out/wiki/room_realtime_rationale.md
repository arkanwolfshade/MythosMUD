# room realtime rationale

> 156 nodes

## Key Concepts

- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (28 connections) — `server/models/spell.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (22 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_costs.py** (19 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **MagicServiceHealingMixin** (17 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (17 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **SpellCostsService** (16 connections) — `server/game/magic/spell_costs.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **SpellSchool** (15 connections) — `server/models/spell.py`
- **SpellEffectType** (15 connections) — `server/models/spell.py`
- **SpellTargetType** (14 connections) — `server/models/spell.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **SpellRangeType** (12 connections) — `server/models/spell.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **_spell()** (11 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **UUID** (6 connections)
- **._publish_or_send_dp_update()** (6 connections) — `server/game/magic/magic_healing_events.py`
- **_spell()** (6 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- *... and 131 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (46 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (26 shared connections)
- [player respawn event](player_respawn_event.md) (14 shared connections)
- [Error Conversion](Error_Conversion.md) (10 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (9 shared connections)
- [add used user](add_used_user.md) (6 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (5 shared connections)
- [magic completion game](magic_completion_game.md) (5 shared connections)
- [manager room npcs](manager_room_npcs.md) (5 shared connections)
- [subject nats manager](subject_nats_manager.md) (4 shared connections)
- [spell game magic](spell_game_magic.md) (4 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (4 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 632 (96%)
- INFERRED: 29 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*