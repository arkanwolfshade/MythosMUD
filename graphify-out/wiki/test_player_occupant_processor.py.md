# test_player_occupant_processor.py

> 45 nodes

## Key Concepts

- **test_event_handler.py** (42 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **asyncio** (15 connections)
- **Test RealTimeEventHandler._handle_player_entered() delegates to player_handler.** (8 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **event_handler()** (6 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_delirium_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_died()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_decay()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_updated()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_xp_awarded()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **fixture** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **mock_task_registry()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_entered_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_create_player_left_message()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_get_room_occupants()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_occupants_snapshot_to_player()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_error()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_send_room_occupants_update_internal_success()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- *... and 20 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (19 shared connections)
- [ChatLogger](ChatLogger.md) (4 shared connections)
- [npc_database.py](npc_database.py.md) (4 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (2 shared connections)
- [factory](factory.md) (1 shared connections)
- [utils/layout.ts](utils-layout.ts.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 85 (85%)
- INFERRED: 15 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*