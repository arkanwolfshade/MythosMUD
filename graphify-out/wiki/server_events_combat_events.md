# server events combat events

> 143 nodes

## Key Concepts

- **test_combat_event_publisher.py** (49 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (31 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **asyncio** (18 connections)
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **._publish_combat_payload()** (14 connections) — `server/services/combat_event_publisher.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (11 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_no_nats_service()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (9 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **publish_npc_damage_event()** (7 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (7 connections) — `server/services/combat_service_events.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- *... and 118 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (20 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (12 shared connections)
- [server services combat event handler](server_services_combat_event_handler.md) (11 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (11 shared connections)
- [moduletype](moduletype.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server events event bus](server_events_event_bus.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (4 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (3 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (2 shared connections)
- [server services combat event publisher](server_services_combat_event_publisher.md) (2 shared connections)
- [baseexception](baseexception.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 304 (83%)
- INFERRED: 61 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*