# commands communication channels

> 48 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **event_handler()** (6 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **Any** (4 connections)
- **._create_player_entered_message()** (4 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (4 connections) — `server/realtime/event_handler.py`
- **._handle_player_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._send_room_occupants_update_internal()** (3 connections) — `server/realtime/event_handler.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **._get_room_occupants()** (3 connections) — `server/realtime/event_handler.py`
- **._send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/event_handler.py`
- **test_event_handler_init()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_init_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **._get_next_sequence()** (2 connections) — `server/realtime/event_handler.py`
- **UUID** (2 connections)
- **.shutdown()** (2 connections) — `server/realtime/event_handler.py`
- *... and 23 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (17 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (8 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (2 shared connections)
- [npc event handlers](npc_event_handlers.md) (2 shared connections)
- [schedule services service](schedule_services_service.md) (2 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (2 shared connections)
- [event bus events](event_bus_events.md) (2 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 135 (88%)
- INFERRED: 18 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*