# Communication Command Flows

> 436 nodes

## Key Concepts

- **BaseEvent** (75 connections) — `server/events/event_types.py`
- **PlayerEnteredRoom** (68 connections) — `server/events/event_types.py`
- **PlayerLeftRoom** (51 connections) — `server/events/event_types.py`
- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_room_sync_service.py** (40 connections) — `server/tests/unit/services/test_room_sync_service.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **room_occupant_manager.py** (19 connections) — `server/realtime/room_occupant_manager.py`
- **RoomSyncService** (19 connections) — `server/services/room_sync_service.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **NATSEventBusBridge** (16 connections) — `server/events/nats_event_bridge.py`
- **room_sync_service.py** (16 connections) — `server/services/room_sync_service.py`
- **event_serialization.py** (15 connections) — `server/events/event_serialization.py`
- **test_event_serialization.py** (15 connections) — `server/tests/unit/events/test_event_serialization.py`
- **serialize_event()** (14 connections) — `server/events/event_serialization.py`
- *... and 411 more nodes in this community*

## Relationships

- [Level and XP Curve](Level_and_XP_Curve.md) (84 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (37 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (36 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (15 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (13 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (12 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (11 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (11 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (11 shared connections)
- [Test Value Distribution](Test_Value_Distribution.md) (11 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (9 shared connections)

## Source Files

- `server/events/distributed_event_bus.py`
- `server/events/event_bus.py`
- `server/events/event_serialization.py`
- `server/events/event_types.py`
- `server/events/nats_event_bridge.py`
- `server/npc/population_control.py`
- `server/realtime/connection_event_helpers.py`
- `server/realtime/event_handler.py`
- `server/realtime/integration/room_event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/services/player_combat_service.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/events/test_event_serialization.py`
- `server/tests/unit/events/test_nats_event_bridge.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`

## Audit Trail

- EXTRACTED: 1550 (90%)
- INFERRED: 164 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*