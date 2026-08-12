# Commands Look Item

> 246 nodes

## Key Concepts

- **event_types.py** (74 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (68 connections) — `server/events/event_types.py`
- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **PlayerLeftRoom** (51 connections) — `server/events/event_types.py`
- **NPCEnteredRoom** (51 connections) — `server/events/event_types.py`
- **NPCLeftRoom** (46 connections) — `server/events/event_types.py`
- **room.py** (31 connections) — `server/models/room.py`
- **event_reaction_system.py** (27 connections) — `server/npc/event_reaction_system.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **npc_event_handlers.py** (16 connections) — `server/realtime/npc_event_handlers.py`
- **test_player_event_handlers_room_left.py** (15 connections) — `server/tests/unit/realtime/test_player_event_handlers_room_left.py`
- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **._subscribe_to_events()** (14 connections) — `server/npc/event_reaction_system.py`
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **_PopulationLifecycleManager** (13 connections) — `server/npc/population_control.py`
- **subscribe_to_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **unsubscribe_from_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **test_connection_event_helpers.py** (13 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **room_event_handler.py** (12 connections) — `server/realtime/integration/room_event_handler.py`
- **__init__.py** (11 connections) — `server/events/__init__.py`
- **NPCSpoke** (11 connections) — `server/events/event_types.py`
- **NPCListened** (11 connections) — `server/events/event_types.py`
- **connection_event_helpers.py** (10 connections) — `server/realtime/connection_event_helpers.py`
- **RoomEventHandler** (10 connections) — `server/realtime/integration/room_event_handler.py`
- **ObjectAddedToRoom** (9 connections) — `server/events/event_types.py`
- *... and 221 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (116 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (57 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (21 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (18 shared connections)
- [Health Check Models](Health_Check_Models.md) (15 shared connections)
- [Archive Advanced Chat](Archive_Advanced_Chat.md) (14 shared connections)
- [Lucidity Database Models](Lucidity_Database_Models.md) (11 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (11 shared connections)
- [Game Chat Moderation](Game_Chat_Moderation.md) (9 shared connections)
- [Lucidity Recovery Commands](Lucidity_Recovery_Commands.md) (9 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (7 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)

## Source Files

- `server/events/__init__.py`
- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/models/room.py`
- `server/npc/event_reaction_system.py`
- `server/npc/lifecycle_manager.py`
- `server/npc/movement_integration.py`
- `server/npc/population_control.py`
- `server/npc/spawning_service.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_room_left.py`

## Audit Trail

- EXTRACTED: 930 (88%)
- INFERRED: 129 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*