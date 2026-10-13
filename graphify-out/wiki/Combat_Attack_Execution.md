# Combat Attack Execution

> 291 nodes

## Key Concepts

- **combat_service.py** (97 connections) — `server/services/combat_service.py`
- **CombatParticipantType** (80 connections) — `server/models/combat.py`
- **models/combat.py** (80 connections) — `server/models/combat.py`
- **npc_combat_integration_service.py** (48 connections) — `server/services/npc_combat_integration_service.py`
- **CombatParticipantData** (46 connections) — `server/services/combat_types.py`
- **combat_turn_participant_actions.py** (44 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatResult** (30 connections) — `server/models/combat.py`
- **combat_service_attack.py** (30 connections) — `server/services/combat_service_attack.py`
- **combat_service_start.py** (30 connections) — `server/services/combat_service_start.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **combat_attack.py** (26 connections) — `server/commands/combat_attack.py`
- **combat_turn_processor.py** (23 connections) — `server/services/combat_turn_processor.py`
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **npc_combat_data_provider.py** (22 connections) — `server/services/npc_combat_data_provider.py`
- **test_combat_attack.py** (22 connections) — `server/tests/unit/commands/test_combat_attack.py`
- **test_npc_combat_integration_join.py** (22 connections) — `server/tests/unit/services/test_npc_combat_integration_join.py`
- **npc_combat_integration_validation_mixin.py** (20 connections) — `server/services/npc_combat_integration_validation_mixin.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_types.py** (17 connections) — `server/services/combat_types.py`
- **npc_combat_integration_combat_mixin.py** (17 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **combat_initialization.py** (16 connections) — `server/services/combat_initialization.py`
- **combat_service_end.py** (16 connections) — `server/services/combat_service_end.py`
- **CombatStatus** (15 connections) — `server/models/combat.py`
- **combat_event_handler.py** (14 connections) — `server/services/combat_event_handler.py`
- *... and 266 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (82 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (49 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (48 shared connections)
- [Combat Participants](Combat_Participants.md) (46 shared connections)
- [Community 197](Community_197.md) (35 shared connections)
- [Community 398](Community_398.md) (27 shared connections)
- [Community 52](Community_52.md) (26 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (18 shared connections)
- [Community 126](Community_126.md) (17 shared connections)
- [Community 134](Community_134.md) (15 shared connections)
- [Community 369](Community_369.md) (15 shared connections)
- [Community 121](Community_121.md) (14 shared connections)

## Source Files

- `server/commands/combat_attack.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_handlers.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_integration_validation_mixin.py`

## Audit Trail

- EXTRACTED: 1056 (95%)
- INFERRED: 51 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*