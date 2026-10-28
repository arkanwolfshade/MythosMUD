# MythosMUD Code Quality Targets for AI

> 22 nodes · cohesion 0.16

## Key Concepts

- **EventPublisher** (32 connections) — `server/realtime/event_publisher.py`
- **._create_event_message()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_entered_event()** (7 connections) — `server/realtime/event_publisher.py`
- **.publish_player_left_event()** (7 connections) — `server/realtime/event_publisher.py`
- **._publish_event()** (5 connections) — `server/realtime/event_publisher.py`
- **.publish_game_tick_event()** (5 connections) — `server/realtime/event_publisher.py`
- **JsonMap** (5 connections)
- **._get_async_persistence()** (4 connections) — `server/realtime/event_publisher.py`
- **._resolve_player_and_room_names()** (4 connections) — `server/realtime/event_publisher.py`
- **.get_next_sequence_number()** (3 connections) — `server/realtime/event_publisher.py`
- **._player_event_subject()** (3 connections) — `server/realtime/event_publisher.py`
- **test_event_publisher_init_without_subject_manager()** (3 connections) — `server/tests/unit/realtime/test_event_publisher.py`
- **.reset_sequence_number()** (2 connections) — `server/realtime/event_publisher.py`
- **Publish a player_entered event to NATS. Args: player_id: ID of the player who…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a player_left event to NATS. Args: player_id: ID of the player who left…** (1 connections) — `server/realtime/event_publisher.py`
- **Publish a game_tick event to NATS. Args: timestamp: Optional custom timestamp…** (1 connections) — `server/realtime/event_publisher.py`
- **Create a standardized event message structure. Args: event_type: Type of event…** (1 connections) — `server/realtime/event_publisher.py`
- **Get the next sequence number for event ordering. Returns: Next sequence number** (1 connections) — `server/realtime/event_publisher.py`
- **Reset the sequence number to 0.** (1 connections) — `server/realtime/event_publisher.py`
- **Get async_persistence (#679: injected at construction by RealtimeBundle).** (1 connections) — `server/realtime/event_publisher.py`
- **Service for publishing real-time game events to NATS subjects. This service…** (1 connections) — `server/realtime/event_publisher.py`
- **Test EventPublisher initialization without subject manager.** (1 connections) — `server/tests/unit/realtime/test_event_publisher.py`

## Relationships

- [Frontend Design Skill](Frontend_Design_Skill.md) (7 shared connections)
- [day](day.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\Call of Cthulhu 7th Edition - Keeper's Rulebook  (2026-08-11)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_Call_of_Cthulhu_7th_Edition_-_Keeper's_Rulebook__2026-08-11.md) (2 shared connections)
- [Amplify the Design](Amplify_the_Design.md) (2 shared connections)
- [main](main.md) (1 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (1 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [test_websocket_handler_disconnect.py](test_websocket_handler_disconnect.py.md) (1 shared connections)

## Source Files

- `server/realtime/event_publisher.py`
- `server/tests/unit/realtime/test_event_publisher.py`

## Audit Trail

- EXTRACTED: 50 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*