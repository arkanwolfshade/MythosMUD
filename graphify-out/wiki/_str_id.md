# _str_id

> 41 nodes · cohesion 0.10

## Key Concepts

- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (19 connections) — `server/game/magic/spell_costs.py`
- **MagicServiceCompletionMixin** (12 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (12 connections)
- **Any** (11 connections)
- **._execute_casting_immediately()** (9 connections) — `server/game/magic/magic_service_completion.py`
- **._complete_casting()** (8 connections) — `server/game/magic/magic_service_completion.py`
- **._recreate_target_from_state()** (7 connections) — `server/game/magic/magic_service_completion.py`
- **.apply_costs()** (7 connections) — `server/game/magic/spell_costs.py`
- **._notify_mp_update()** (7 connections) — `server/game/magic/spell_costs.py`
- **._try_complete_casting_via_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **._try_queue_spell_for_combat()** (6 connections) — `server/game/magic/magic_service_completion.py`
- **UUID** (6 connections)
- **._apply_corruption_if_mythos()** (6 connections) — `server/game/magic/spell_costs.py`
- **._spend_lucidity_if_required()** (6 connections) — `server/game/magic/spell_costs.py`
- **._apply_spell_costs_and_effects()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._get_player_and_room()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **._parse_casting_target_id()** (5 connections) — `server/game/magic/magic_service_completion.py`
- **_is_heal_other_target()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_healing_update_event()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **_send_spell_completion_message()** (4 connections) — `server/game/magic/magic_service_completion.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **Any** (3 connections)
- **.__init__()** (3 connections) — `server/game/magic/spell_costs.py`
- **Casting completion flow for spellcasting. Mixin that handles completing a…** (1 connections) — `server/game/magic/magic_service_completion.py`
- *... and 16 more nodes in this community*

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (10 shared connections)
- [test_item.py](test_item.py.md) (5 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (4 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [reset_database](reset_database.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (2 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`

## Audit Trail

- EXTRACTED: 114 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*