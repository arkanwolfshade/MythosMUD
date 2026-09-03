# Combat Events

> 190 nodes

## Key Concepts

- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (55 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **PlayerDiedEvent** (31 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (31 connections) — `server/events/event_types.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatStartedEvent** (14 connections) — `server/events/combat_events.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 165 more nodes in this community*

## Relationships

- [Combat Service Attack](Combat_Service_Attack.md) (43 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (17 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (16 shared connections)
- [Test Combat Event Handler](Test_Combat_Event_Handler.md) (13 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (13 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (13 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (12 shared connections)
- [Test Player Death Service](Test_Player_Death_Service.md) (10 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (10 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (9 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (9 shared connections)
- [Test Event Handler](Test_Event_Handler.md) (8 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 580 (90%)
- INFERRED: 62 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*