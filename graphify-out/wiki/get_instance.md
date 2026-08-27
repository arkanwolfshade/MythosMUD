# .get_instance

> 135 nodes

## Key Concepts

- **test_combat_event_publisher.py** (51 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (33 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (20 connections) — `server/services/combat_event_publisher.py`
- **asyncio** (20 connections)
- **combat_events.py** (19 connections) — `server/events/combat_events.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (12 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **BaseEvent** (7 connections)
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_started()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_combat_target_switch()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_attacked()** (5 connections) — `server/services/combat_event_publisher.py`
- **.publish_npc_died()** (5 connections) — `server/services/combat_event_publisher.py`
- *... and 110 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (19 shared connections)
- [properties](properties.md) (11 shared connections)
- [NATSService](NATSService.md) (9 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (7 shared connections)
- [NPCDefinition](NPCDefinition.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (3 shared connections)
- [🔴 CRITICAL ISSUES](🔴_CRITICAL_ISSUES.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [TestGracefulDegradation](TestGracefulDegradation.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 310 (91%)
- INFERRED: 31 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*