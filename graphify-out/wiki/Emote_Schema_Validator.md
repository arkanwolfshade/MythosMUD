# Emote Schema Validator

> 93 nodes

## Key Concepts

- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (30 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (10 connections) — `server/events/combat_events.py`
- **CombatTurnAdvancedEvent** (7 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (7 connections) — `server/events/combat_events.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_player_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_took_damage()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_turn_advanced()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_timeout()** (5 connections) — `server/services/combat_event_publisher.py`
- **._create_event_message()** (4 connections) — `server/services/combat_event_publisher.py`
- **test_publish_combat_started_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_started_nats_error()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_combat_ended_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_player_attacked_no_nats_service()** (4 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **._nats_ready()** (3 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started_event()** (3 connections) — `server/services/combat_service.py`
- *... and 68 more nodes in this community*

## Relationships

- [Health Check Models](Health_Check_Models.md) (17 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (7 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (5 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (5 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (4 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (3 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (2 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 323 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*