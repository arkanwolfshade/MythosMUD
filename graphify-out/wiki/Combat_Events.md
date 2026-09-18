# Combat Events

> 180 nodes

## Key Concepts

- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **PlayerDiedEvent** (22 connections) — `server/events/event_types.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **PlayerDPDecayEvent** (18 connections) — `server/events/event_types.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- *... and 155 more nodes in this community*

## Relationships

- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (38 shared connections)
- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (20 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (12 shared connections)
- [Event Bus](Event_Bus.md) (11 shared connections)
- [Community 519](Community_519.md) (10 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (9 shared connections)
- [NPC Event Types](NPC_Event_Types.md) (8 shared connections)
- [Community 46](Community_46.md) (5 shared connections)
- [Community 1043](Community_1043.md) (5 shared connections)
- [Community 184](Community_184.md) (5 shared connections)
- [Community 257](Community_257.md) (3 shared connections)
- [Community 503](Community_503.md) (3 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 436 (90%)
- INFERRED: 49 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*