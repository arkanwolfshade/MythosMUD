# Test Event Handler

> 99 nodes

## Key Concepts

- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **RealTimeEventHandler** (31 connections) — `server/realtime/event_handler.py`
- **event_handler.py** (27 connections) — `server/realtime/event_handler.py`
- **PlayerRespawnedEvent** (21 connections) — `server/events/event_types.py`
- **PlayerDeliriumRespawnedEvent** (16 connections) — `server/events/event_types.py`
- **asyncio** (15 connections)
- **Test RealTimeEventHandler._handle_player_entered() delegates to player_handler.** (8 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **event_handler()** (7 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **.__init__()** (6 connections) — `server/realtime/event_handler.py`
- **test_event_handler_handle_npc_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_npc_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_delirium_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_died()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_decay()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_updated()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_entered()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_left()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_respawned()** (4 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **fixture** (4 connections)
- **._create_player_entered_message()** (3 connections) — `server/realtime/event_handler.py`
- **._create_player_left_message()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_entered()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_npc_left()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_delirium_respawned()** (3 connections) — `server/realtime/event_handler.py`
- **._handle_player_died()** (3 connections) — `server/realtime/event_handler.py`
- *... and 74 more nodes in this community*

## Relationships

- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (22 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (10 shared connections)
- [Combat Events](Combat_Events.md) (8 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (7 shared connections)
- [Player Event Handlers](Player_Event_Handlers.md) (6 shared connections)
- [Test Player Event Handlers Respawn](Test_Player_Event_Handlers_Respawn.md) (6 shared connections)
- [Test Player Event Handlers Room](Test_Player_Event_Handlers_Room.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (5 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (2 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (2 shared connections)
- [Event Types](Event_Types.md) (2 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (2 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/event_handler.py`
- `server/tests/unit/realtime/test_event_handler.py`

## Audit Trail

- EXTRACTED: 202 (91%)
- INFERRED: 20 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*