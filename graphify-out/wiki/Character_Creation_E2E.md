# Character Creation E2E

> 337 nodes

## Key Concepts

- **RealTimeEventHandler** (44 connections) — `server/realtime/event_handler.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **event_handler.py** (35 connections) — `server/realtime/event_handler.py`
- **player_combat_service.py** (35 connections) — `server/services/player_combat_service.py`
- **PlayerXPAwardEvent** (35 connections) — `server/services/player_combat_service.py`
- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **player_event_handlers_state.py** (23 connections) — `server/realtime/player_event_handlers_state.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **PlayerDiedEvent** (19 connections) — `server/events/event_types.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **PlayerDPDecayEvent** (16 connections) — `server/events/event_types.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerDeliriumRespawnedEvent** (15 connections) — `server/events/event_types.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **._subscribe_to_events()** (13 connections) — `server/realtime/event_handler.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- *... and 312 more nodes in this community*

## Relationships

- [Commands Look Item](Commands_Look_Item.md) (57 shared connections)
- [Client Event Store](Client_Event_Store.md) (34 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (21 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (21 shared connections)
- [Who Command Helpers](Who_Command_Helpers.md) (20 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (14 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (13 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (10 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (8 shared connections)
- [Archive Planning Aliases](Archive_Planning_Aliases.md) (7 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (5 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/realtime/websocket_initial_state.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/services/room_sync_service.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/realtime/test_player_event_handlers.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 1198 (92%)
- INFERRED: 100 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*