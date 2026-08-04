# Memory Task Runtime

> 148 nodes

## Key Concepts

- **test_combat_event_publisher.py** (48 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (29 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (19 connections) — `server/events/combat_events.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **test_combat_event_handler.py** (16 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_paths_nats_publish_error()** (10 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- **.handle_attack_events_and_xp()** (8 connections) — `server/services/combat_event_handler.py`
- **test_publish_paths_not_connected()** (8 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_no_nats_service()** (8 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **.award_xp_to_player()** (5 connections) — `server/services/combat_event_handler.py`
- **.publish_combat_ended_event()** (5 connections) — `server/services/combat_event_handler.py`
- **_npc_attacked_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 123 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (37 shared connections)
- [item models rationale](item_models_rationale.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [Item Instances](Item_Instances.md) (7 shared connections)
- [services combat sync](services_combat_sync.md) (5 shared connections)
- [commands communication say](commands_communication_say.md) (5 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (5 shared connections)
- [services nats service](services_nats_service.md) (3 shared connections)
- [npc combat base](npc_combat_base.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 585 (95%)
- INFERRED: 32 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*