# Item Instances

> 1010 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **CombatParticipant** (168 connections) — `server/models/combat.py`
- **CombatInstance** (167 connections) — `server/models/combat.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **NATSError** (101 connections) — `server/services/nats_exceptions.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (51 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **test_combat_attack_handler.py** (37 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **CombatParticipantType** (36 connections) — `server/models/combat.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **nats_exceptions.py** (33 connections) — `server/services/nats_exceptions.py`
- **combat_taunt.py** (32 connections) — `server/commands/combat_taunt.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **TauntCommandHandler** (29 connections) — `server/commands/combat_taunt.py`
- **test_aggro_threat.py** (29 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **aggro_threat.py** (28 connections) — `server/services/aggro_threat.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **test_damage_grace_period.py** (26 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **update_aggro()** (24 connections) — `server/services/aggro_threat.py`
- *... and 985 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (101 shared connections)
- [NPC Combat](NPC_Combat.md) (59 shared connections)
- [spell game magic](spell_game_magic.md) (47 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (41 shared connections)
- [combat services rationale](combat_services_rationale.md) (23 shared connections)
- [command factories exploration](command_factories_exploration.md) (22 shared connections)
- [spell models rationale](spell_models_rationale.md) (21 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (20 shared connections)
- [combat flee commands](combat_flee_commands.md) (17 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (14 shared connections)
- [combat services persistence](combat_services_persistence.md) (14 shared connections)
- [combat npc mixin](combat_npc_mixin.md) (13 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/commands/combat_taunt.py`
- `server/config/__init__.py`
- `server/events/combat_events.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_configuration_service.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`

## Audit Trail

- EXTRACTED: 4514 (94%)
- INFERRED: 273 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*