# combat_service.py

> 210 nodes

## Key Concepts

- **combat_service.py** (105 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **PlayerDiedEvent** (31 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (31 connections) — `server/events/event_types.py`
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **player_death_service.py** (18 connections) — `server/services/player_death_service.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- *... and 185 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (41 shared connections)
- [get_logger](get_logger.md) (30 shared connections)
- [get_config](get_config.md) (25 shared connections)
- [NATSError](NATSError.md) (20 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (18 shared connections)
- [CombatInstance](CombatInstance.md) (16 shared connections)
- [EventBus](EventBus.md) (15 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (14 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (12 shared connections)
- [CombatParticipant](CombatParticipant.md) (10 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (7 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 637 (90%)
- INFERRED: 74 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*