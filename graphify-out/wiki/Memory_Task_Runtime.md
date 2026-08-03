# Memory Task Runtime

> 161 nodes

## Key Concepts

- **test_combat_event_publisher.py** (48 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (29 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (19 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **test_combat_event_handler.py** (16 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_paths_nats_publish_error()** (10 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (9 connections) — `server/services/combat_death_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- *... and 136 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (27 shared connections)
- [NPC Combat](NPC_Combat.md) (23 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (12 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (12 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (8 shared connections)
- [combat commands handler](combat_commands_handler.md) (7 shared connections)
- [services passive lucidity](services_passive_lucidity.md) (6 shared connections)
- [services combat sync](services_combat_sync.md) (6 shared connections)
- [command factories exploration](command_factories_exploration.md) (5 shared connections)
- [rate limiter services](rate_limiter_services.md) (4 shared connections)
- [npc combat base](npc_combat_base.md) (3 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 662 (93%)
- INFERRED: 51 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*