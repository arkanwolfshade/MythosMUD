# combat_service.py

> 390 nodes

## Key Concepts

- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **models/combat.py** (50 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **NATSPublishError** (30 connections) — `server/services/nats_exceptions.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **asyncio** (14 connections)
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- *... and 365 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (134 shared connections)
- [get_logger](get_logger.md) (73 shared connections)
- [CombatService](CombatService.md) (40 shared connections)
- [NATSService](NATSService.md) (28 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (20 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (15 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (11 shared connections)
- [BaseEvent](BaseEvent.md) (10 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (9 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (8 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (5 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/models/combat.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/nats_exceptions.py`
- `server/services/npc_combat_data_provider.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`

## Audit Trail

- EXTRACTED: 931 (95%)
- INFERRED: 44 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*