# Any

> 223 nodes

## Key Concepts

- **NATSError** (101 connections) — `server/services/nats_exceptions.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **NPCAttackedEvent** (10 connections) — `server/events/combat_events.py`
- *... and 198 more nodes in this community*

## Relationships

- [. initialize handlers()](_initialize_handlers%28%29.md) (38 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (37 shared connections)
- [test combat persistence handler events](test_combat_persistence_handler_events.md) (30 shared connections)
- [Any](Any.md) (28 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (25 shared connections)
- [Player](Player.md) (22 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (21 shared connections)
- [Room](Room.md) (13 shared connections)
- [test combat persistence handler persistence](test_combat_persistence_handler_persistence.md) (10 shared connections)
- [test exploration service](test_exploration_service.md) (9 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)

## Source Files

- `server/container/main.py`
- `server/events/combat_events.py`
- `server/realtime/message_filtering.py`
- `server/realtime/nats_message_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/nats_exceptions.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 990 (87%)
- INFERRED: 147 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*