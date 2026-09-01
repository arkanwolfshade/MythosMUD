# EventHandler

> 69 nodes

## Key Concepts

- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (10 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (6 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (6 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **ConnectionManager** (5 connections)
- **_EventBusPublishPort** (4 connections) — `server/realtime/event_handlers.py`
- **test_handle_npc_took_damage_flattens_event_data_for_websocket()** (4 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **.get_event_handler_map()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_ended_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_combat_started_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_died_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_npc_took_damage_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.handle_player_attacked_event()** (3 connections) — `server/realtime/event_handlers.py`
- **.__init__()** (3 connections) — `server/realtime/event_handlers.py`
- **.validate_event_message()** (3 connections) — `server/realtime/event_handlers.py`
- **test_handle_combat_ended_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- *... and 44 more nodes in this community*

## Relationships

- [CircuitBreaker](CircuitBreaker.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 125 (88%)
- INFERRED: 17 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*