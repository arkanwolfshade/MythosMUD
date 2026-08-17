# CombatService

> 291 nodes

## Key Concepts

- **CombatService** (165 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **models/combat.py** (58 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **CombatEventHandler** (27 connections) — `server/services/combat_event_handler.py`
- **combat_event_publisher.py** (23 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **test_combat_event_handler.py** (17 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- *... and 266 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (50 shared connections)
- [CombatParticipant](CombatParticipant.md) (48 shared connections)
- [CombatInstance](CombatInstance.md) (41 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (39 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (31 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (27 shared connections)
- [TargetMatch](TargetMatch.md) (26 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (25 shared connections)
- [NATSError](NATSError.md) (24 shared connections)
- [UUID](UUID.md) (20 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (17 shared connections)
- [.connection_manager](connection_manager.md) (16 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/events/combat_events.py`
- `server/game/player_service.py`
- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/config/test_config.py`

## Audit Trail

- EXTRACTED: 1039 (87%)
- INFERRED: 151 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*