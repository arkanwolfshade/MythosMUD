# test_item.py

> 77 nodes · cohesion 0.06

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **test_magic_service.py** (47 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **MagicService** (41 connections) — `server/game/magic/magic_service.py`
- **UUID** (26 connections)
- **CastingStateManager** (25 connections) — `server/game/magic/casting_state_manager.py`
- **asyncio** (19 connections)
- **casting_state_manager.py** (11 connections) — `server/game/magic/casting_state_manager.py`
- **test_casting_state_manager.py** (11 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **CastingState** (8 connections) — `server/game/magic/casting_state_manager.py`
- **UUID** (8 connections)
- **StartCastingTarget** (8 connections) — `server/game/magic/casting_state_manager.py`
- **_spell()** (8 connections) — `server/tests/unit/game/magic/test_casting_state_manager.py`
- **.start_casting()** (7 connections) — `server/game/magic/casting_state_manager.py`
- **test_start_delayed_cast_value_error()** (7 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_can_cast_spell_unknown_and_materials()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_material_consume_failure()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_check_casting_progress_completes()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_start_delayed_cast_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **fixture** (5 connections)
- **test_can_cast_spell_paths()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_cast_spell_delayed()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_complete_casting_via_combat_queue()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_fail()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **test_interrupt_casting_luck_pass()** (5 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **.complete_casting()** (4 connections) — `server/game/magic/casting_state_manager.py`
- *... and 52 more nodes in this community*

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (27 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (10 shared connections)
- [CORSConfig](CORSConfig.md) (9 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (6 shared connections)
- [RoomService](RoomService.md) (6 shared connections)
- [_str_id](_str_id.md) (5 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (5 shared connections)
- [Room](Room.md) (4 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (4 shared connections)
- [test_e2e_reset_players.py](test_e2e_reset_players.py.md) (4 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)

## Source Files

- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/tests/unit/game/magic/test_casting_state_manager.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 230 (83%)
- INFERRED: 48 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*