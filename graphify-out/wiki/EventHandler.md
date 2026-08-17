# EventHandler

> 68 nodes

## Key Concepts

- **EventHandler** (33 connections) — `server/realtime/event_handlers.py`
- **event_handlers.py** (24 connections) — `server/realtime/event_handlers.py`
- **test_event_handlers_combat.py** (23 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- **asyncio** (11 connections)
- **_send_combat_participant_updates()** (9 connections) — `server/realtime/event_handlers.py`
- **_as_event_data_dict()** (8 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- **.handle_event_message()** (5 connections) — `server/realtime/event_handlers.py`
- **_npc_died_ids_or_warn()** (5 connections) — `server/realtime/event_handlers.py`
- **_participant_key_strings()** (5 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (5 connections) — `server/realtime/event_handlers.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
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
- **test_handle_combat_started_event()** (3 connections) — `server/tests/unit/realtime/test_event_handlers_combat.py`
- *... and 43 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (2 shared connections)
- [NPCDied](NPCDied.md) (2 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/event_handlers.py`
- `server/tests/unit/realtime/test_event_handlers_combat.py`

## Audit Trail

- EXTRACTED: 119 (86%)
- INFERRED: 19 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*