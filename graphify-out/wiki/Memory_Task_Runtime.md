# Memory Task Runtime

> 125 nodes

## Key Concepts

- **test_combat_event_publisher.py** (48 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (29 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (19 connections) — `server/events/combat_events.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (10 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatTurnAdvancedEvent** (8 connections) — `server/events/combat_events.py`
- **CombatTimeoutEvent** (8 connections) — `server/events/combat_events.py`
- **test_publish_paths_not_connected()** (8 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_no_nats_service()** (8 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **combat_integration_protocols.py** (7 connections) — `server/npc/combat_integration_protocols.py`
- **CombatEventPublisherProtocol** (7 connections) — `server/npc/combat_integration_protocols.py`
- **NpcCombatServiceProtocol** (6 connections) — `server/npc/combat_integration_protocols.py`
- **_npc_attacked_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_took_damage_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_npc_died_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_turn_advanced_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **_timeout_event()** (5 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **.publish_combat_started()** (4 connections) — `server/services/combat_event_publisher.py`
- *... and 100 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (18 shared connections)
- [models npc rationale](models_npc_rationale.md) (15 shared connections)
- [subject admin controller](subject_admin_controller.md) (14 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (7 shared connections)
- [commands communication say](commands_communication_say.md) (6 shared connections)
- [tick game processing](tick_game_processing.md) (5 shared connections)
- [player event realtime](player_event_realtime.md) (4 shared connections)
- [game weapon player](game_weapon_player.md) (2 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [game chat service](game_chat_service.md) (1 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 471 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*