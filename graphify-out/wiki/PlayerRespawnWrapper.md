# PlayerRespawnWrapper

> 44 nodes · cohesion 0.05

## Key Concepts

- **RealTimeEventHandler** (35 connections) — `server/realtime/event_handler.py`
- **._send_room_occupants_update_internal()** (5 connections) — `server/realtime/event_handler.py`
- **._create_player_entered_message()** (3 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_decay()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_dp_updated()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_xp_awarded()** (3 connections) — `server/realtime/event_handler.py`
- **._send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/event_handler.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **._subscribe_to_events()** (3 connections) — `server/realtime/event_handler.py`
- **test_event_handler_init()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_init_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **UUID** (2 connections)
- **._get_next_sequence()** (2 connections) — `server/realtime/event_handler.py`
- **._get_room_occupants()** (2 connections) — `server/realtime/event_handler.py`
- **.shutdown()** (2 connections) — `server/realtime/event_handler.py`
- **Get the next sequence number for events.** (1 connections) — `server/realtime/event_handler.py`
- **Subscribe to relevant game events.** (1 connections) — `server/realtime/event_handler.py`
- *... and 19 more nodes in this community*

## Relationships

- [._bind_event_type](_bind_event_type.md) (4 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (4 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [HolidayEntry](HolidayEntry.md) (2 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [Communities (355 total, 223 thin omitted)](Communities_355_total,_223_thin_omitted.md) (1 shared connections)
- [ChatHistoryPanel.tsx](ChatHistoryPanel.tsx.md) (1 shared connections)
- [ZoneConfiguration](ZoneConfiguration.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 69 (91%)
- INFERRED: 7 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*