# Community 244

> 65 nodes

## Key Concepts

- **RealTimeEventHandler** (31 connections) — `server/realtime/event_handler.py`
- **phantom_visibility.py** (10 connections) — `server/services/phantom_visibility.py`
- **send_personalized_room_events()** (9 connections) — `server/realtime/room_viewer_fanout.py`
- **get_viewer_phantom_names()** (9 connections) — `server/services/phantom_visibility.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **send_personalized_occupants_update()** (8 connections) — `server/realtime/room_viewer_fanout.py`
- **room_has_hallucinating_viewer()** (8 connections) — `server/services/phantom_visibility.py`
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
- **test_get_viewer_phantom_names_matches_own_room()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_get_viewer_phantom_names_no_viewer_or_room()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- *... and 40 more nodes in this community*

## Relationships

- [Game Event Types](Game_Event_Types.md) (14 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (4 shared connections)
- [Community 500](Community_500.md) (2 shared connections)
- [Community 152](Community_152.md) (2 shared connections)
- [NPC Room Lifecycle](NPC_Room_Lifecycle.md) (2 shared connections)
- [Community 106](Community_106.md) (2 shared connections)
- [Player Name Extraction](Player_Name_Extraction.md) (1 shared connections)
- [Community 367](Community_367.md) (1 shared connections)
- [Community 75](Community_75.md) (1 shared connections)
- [Community 65](Community_65.md) (1 shared connections)
- [Community 904](Community_904.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/room_viewer_fanout.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/services/test_phantom_visibility.py`

## Audit Trail

- EXTRACTED: 107 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*