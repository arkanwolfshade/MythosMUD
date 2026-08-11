# NPC Service Tests

> 121 nodes

## Key Concepts

- **lifespan_startup.py** (59 connections) — `server/app/lifespan_startup.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **quest_events.py** (14 connections) — `server/game/quest/quest_events.py`
- **FastAPI** (13 connections)
- **subscribe_quest_events()** (13 connections) — `server/game/quest/quest_events.py`
- **.event_bus()** (12 connections) — `server/realtime/connection_manager.py`
- **lifespan_event_subscriptions.py** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_combat_services()** (11 connections) — `server/app/lifespan_startup.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **subscribe_quest_events()** (9 connections) — `server/app/lifespan_event_subscriptions.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **QuestCompleted** (9 connections) — `server/events/event_types.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **initialize_mythos_time_consumer()** (8 connections) — `server/app/lifespan_startup.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **_EventBusPublishPort** (7 connections) — `server/realtime/event_handlers.py`
- **_publish_npc_died_to_event_bus()** (7 connections) — `server/realtime/event_handlers.py`
- **_npc_died_broadcast_and_bridge()** (7 connections) — `server/realtime/event_handlers.py`
- *... and 96 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (31 shared connections)
- [Client Event Store](Client_Event_Store.md) (27 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (25 shared connections)
- [Container Data Models](Container_Data_Models.md) (22 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (7 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (6 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Combat Schema Validation](Combat_Schema_Validation.md) (3 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (3 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (3 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/events/event_types.py`
- `server/game/quest/quest_events.py`
- `server/npc/npc_base.py`
- `server/realtime/connection_manager.py`
- `server/realtime/event_handlers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/npc_startup_service.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 492 (94%)
- INFERRED: 32 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*