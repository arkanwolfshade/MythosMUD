# handle_whisper_command

> 62 nodes · cohesion 0.06

## Key Concepts

- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **UUID** (21 connections)
- **JsonMap** (12 connections)
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **._casting_roll()** (7 connections) — `server/game/magic/magic_service.py`
- **._casting_roll_or_fail_result()** (7 connections) — `server/game/magic/magic_service.py`
- **._get_player_and_normalized_stats()** (7 connections) — `server/game/magic/magic_service.py`
- **._handle_instant_cast()** (7 connections) — `server/game/magic/magic_service.py`
- **._validate_spell_casting()** (7 connections) — `server/game/magic/magic_service.py`
- **_stat_int()** (7 connections) — `server/game/magic/magic_service.py`
- **._consume_materials_if_required()** (6 connections) — `server/game/magic/magic_service.py`
- **._perform_luck_check()** (6 connections) — `server/game/magic/magic_service.py`
- **._send_spell_completion_message()** (6 connections) — `server/game/magic/magic_service.py`
- **._check_already_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_lucidity_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_materials_available()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_mp_sufficient()** (5 connections) — `server/game/magic/magic_service.py`
- **._check_player_knows_spell()** (5 connections) — `server/game/magic/magic_service.py`
- **.interrupt_casting()** (5 connections) — `server/game/magic/magic_service.py`
- **._player_persistence()** (5 connections) — `server/game/magic/magic_service.py`
- **.send_spell_execution_notifications()** (5 connections) — `server/game/magic/magic_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (16 shared connections)
- [test_item.py](test_item.py.md) (10 shared connections)
- [RoomService](RoomService.md) (5 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (3 shared connections)
- [_str_id](_str_id.md) (2 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (1 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [test_e2e_reset_players.py](test_e2e_reset_players.py.md) (1 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (1 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (1 shared connections)

## Source Files

- `server/game/magic/magic_service.py`

## Audit Trail

- EXTRACTED: 154 (93%)
- INFERRED: 12 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*