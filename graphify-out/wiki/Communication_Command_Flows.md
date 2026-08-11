# Communication Command Flows

> 187 nodes

## Key Concepts

- **EventBus** (129 connections) — `server/events/event_bus.py`
- **NPCBase** (82 connections) — `server/npc/npc_base.py`
- **spawning_service.py** (37 connections) — `server/npc/spawning_service.py`
- **spawning_instance_factory.py** (24 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_request_execution.py** (19 connections) — `server/npc/spawning_request_execution.py`
- **NPCSpawnStatistics** (16 connections) — `server/npc/spawning_service.py`
- **SimpleNPCDefinition** (15 connections) — `server/npc/spawning_models.py`
- **NPCSpawnResult** (14 connections) — `server/npc/spawning_models.py`
- **create_npc_instance()** (13 connections) — `server/npc/spawning_instance_factory.py`
- **spawning_models.py** (12 connections) — `server/npc/spawning_models.py`
- **spawn_npc_from_request()** (12 connections) — `server/npc/spawning_request_execution.py`
- **Any** (10 connections)
- **_instantiate_by_type()** (10 connections) — `server/npc/spawning_instance_factory.py`
- **_build_aggressive()** (9 connections) — `server/npc/spawning_instance_factory.py`
- **NPCSpawnRequest** (9 connections) — `server/npc/spawning_models.py`
- **._handle_event_async()** (8 connections) — `server/events/event_bus.py`
- **generate_npc_id()** (8 connections) — `server/npc/spawning_instance_factory.py`
- **._stop_processing()** (7 connections) — `server/events/event_bus.py`
- **._ensure_async_processing()** (6 connections) — `server/events/event_bus.py`
- **._create_async_subscriber_tasks()** (6 connections) — `server/events/event_bus.py`
- **.unsubscribe()** (6 connections) — `server/events/event_bus.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **._move_with_integration()** (6 connections) — `server/npc/npc_base.py`
- **_build_shopkeeper()** (6 connections) — `server/npc/spawning_instance_factory.py`
- **_build_passive()** (6 connections) — `server/npc/spawning_instance_factory.py`
- *... and 162 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (42 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (41 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (28 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (13 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (11 shared connections)
- [Command Alias Model](Command_Alias_Model.md) (8 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (7 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (7 shared connections)
- [Command Parser Tests](Command_Parser_Tests.md) (7 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (5 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (5 shared connections)

## Source Files

- `server/events/event_bus.py`
- `server/npc/event_reaction_system.py`
- `server/npc/npc_base.py`
- `server/npc/spawning_instance_factory.py`
- `server/npc/spawning_models.py`
- `server/npc/spawning_request_execution.py`
- `server/npc/spawning_service.py`
- `server/tests/integration/test_follow_flow.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/events/test_event_bus.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 739 (91%)
- INFERRED: 72 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*