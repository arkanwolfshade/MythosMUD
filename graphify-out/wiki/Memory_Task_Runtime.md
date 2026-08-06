# Memory Task Runtime

> 162 nodes

## Key Concepts

- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (48 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **nats_exceptions.py** (36 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (35 connections) — `server/services/nats_exceptions.py`
- **CombatEventPublisher** (29 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (19 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **test_publish_paths_nats_publish_error()** (10 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (9 connections) — `server/services/combat_death_handler.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- *... and 137 more nodes in this community*

## Relationships

- [game chat service](game_chat_service.md) (36 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (31 shared connections)
- [subject admin controller](subject_admin_controller.md) (28 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (22 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (16 shared connections)
- [message nats handler](message_nats_handler.md) (13 shared connections)
- [Item Instances](Item_Instances.md) (13 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (11 shared connections)
- [command factories exploration](command_factories_exploration.md) (11 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (11 shared connections)
- [combat validator validators](combat_validator_validators.md) (10 shared connections)
- [models player rationale](models_player_rationale.md) (7 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 830 (94%)
- INFERRED: 57 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*