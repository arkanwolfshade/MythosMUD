# test_nats_message_handler.py

> 149 nodes · cohesion 0.03

## Key Concepts

- **Spell** (141 connections) — `server/models/spell.py`
- **SpellEffectType** (47 connections) — `server/models/spell.py`
- **SpellSchool** (37 connections) — `server/models/spell.py`
- **SpellTargetType** (34 connections) — `server/models/spell.py`
- **SpellRangeType** (32 connections) — `server/models/spell.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell.py** (29 connections) — `server/models/spell.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_magic_healing_events.py** (20 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **test_spell_costs.py** (20 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_spell_registry.py** (18 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **spell_costs.py** (16 connections) — `server/game/magic/spell_costs.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **MagicServiceHealingMixin** (14 connections) — `server/game/magic/magic_healing_events.py`
- **_HealingService** (12 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **_spell()** (10 connections) — `server/tests/unit/game/magic/test_spell_costs.py`
- **test_get_combat_target_auto_selects_opponent()** (10 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_spell()** (9 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_magic_healing_events.py`
- **self_spell()** (8 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **test_spell_with_materials()** (8 connections) — `server/tests/unit/models/test_spell.py`
- **._publish_dp_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- **._send_healing_update_event()** (7 connections) — `server/game/magic/magic_healing_events.py`
- *... and 124 more nodes in this community*

## Relationships

- [RoomService](RoomService.md) (38 shared connections)
- [test_item.py](test_item.py.md) (27 shared connections)
- [test_e2e_reset_players.py](test_e2e_reset_players.py.md) (26 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (19 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (17 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (16 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (14 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (12 shared connections)
- [_str_id](_str_id.md) (10 shared connections)
- [Room](Room.md) (8 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (8 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (7 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_magic_healing_events.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_costs.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 423 (72%)
- INFERRED: 161 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*