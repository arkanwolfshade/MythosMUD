# GameClientV2ContainerView.tsx

> 88 nodes · cohesion 0.04

## Key Concepts

- **SpellEffects** (63 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (50 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **asyncio** (30 connections)
- **SpellEffectsDeps** (22 connections) — `server/game/magic/spell_effects.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **test_process_teleport_into_instance_template_fails_cleanly()** (7 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_process_effect_flee_not_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_publish_npc_spell_damage_syncs_participant_when_npc_room_missing()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_effects.py`
- **spell_effects()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_to_npc_success()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_to_npc_unavailable()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_spell_effects_init_with_repository()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **mock_target_match()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **fixture** (4 connections)
- **test_process_corruption_adjust_invalid_target()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_create_object_invalid_target()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_invalid_target()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_corruption_adjust()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_create_object()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_effect_damage()** (4 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- *... and 63 more nodes in this community*

## Relationships

- [RoomService](RoomService.md) (45 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (17 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (14 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (10 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (6 shared connections)
- [endpoints.py](endpoints.py.md) (6 shared connections)
- [test_item.py](test_item.py.md) (5 shared connections)
- [_str_id](_str_id.md) (4 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (4 shared connections)
- [test_container_persistence_extended_row_helpers.py](test_container_persistence_extended_row_helpers.py.md) (4 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (3 shared connections)

## Source Files

- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 236 (81%)
- INFERRED: 55 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*