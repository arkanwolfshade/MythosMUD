# Combat Taunt Tests

> 375 nodes · cohesion 0.01

## Key Concepts

- **CombatParticipant** (86 connections) — `server/models/combat.py`
- **CombatInstance** (74 connections) — `server/models/combat.py`
- **test_combat.py** (59 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_turn_processor.py** (34 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatParticipantType** (32 connections) — `server/models/combat.py`
- **test_aggro_threat.py** (28 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **_make_combat()** (24 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **CombatTurnProcessor** (22 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **test_combat_taunt.py** (18 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **combat.py** (16 connections) — `server/models/combat.py`
- **combat_death_handler.py** (16 connections) — `server/services/combat_death_handler.py`
- **test_combat_service.py** (16 connections) — `server/tests/unit/services/test_combat_service.py`
- **combat_flee_handler.py** (15 connections) — `server/services/combat_flee_handler.py`
- **combat_turn_processor.py** (15 connections) — `server/services/combat_turn_processor.py`
- **test_combat_flee_handler.py** (15 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **CombatAction** (14 connections) — `server/models/combat.py`
- **execute_voluntary_flee()** (14 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (14 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_aggro_flow.py** (13 connections) — `server/tests/integration/test_aggro_flow.py`
- **_make_participant()** (12 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **CombatParticipant** (11 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **combat_attack_handler.py** (11 connections) — `server/services/combat_attack_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_service.py`
- *... and 350 more nodes in this community*

## Relationships

- [[Combat Service Bundle]] (21 shared connections)
- [[Combat Command Handler]] (18 shared connections)
- [[NPC Admin API]] (17 shared connections)
- [[Combat Aggro Threat]] (11 shared connections)
- [[Combat Attack Service]] (9 shared connections)
- [[Combat Flee Command]] (9 shared connections)
- [[Combat Turn Processor]] (8 shared connections)
- [[Flee Command Tests]] (7 shared connections)
- [[Combat Attack Handler]] (7 shared connections)
- [[Lucidity State Models]] (7 shared connections)
- [[NPC Combat Lifecycle]] (6 shared connections)
- [[Combat Death Handling]] (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_turn_processor.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/commands/test_combat_taunt.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_service.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`

## Audit Trail

- EXTRACTED: 1414 (99%)
- INFERRED: 18 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
