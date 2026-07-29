# combat

> 398 nodes

## Key Concepts

- **CombatInstance** (167 connections) — `server/models/combat.py`
- **CombatParticipant** (166 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **combat.py** (51 connections) — `server/models/combat.py`
- **CombatTurnProcessor** (48 connections) — `server/services/combat_turn_processor.py`
- **combat_turn_participant_actions.py** (46 connections) — `server/services/combat_turn_participant_actions.py`
- **test_combat_turn_processor.py** (36 connections) — `server/tests/unit/services/test_combat_turn_processor.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **CombatAction** (21 connections) — `server/models/combat.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **combat_service_end.py** (11 connections) — `server/services/combat_service_end.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **._execute_spell_action()** (11 connections) — `server/services/combat_turn_processor.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 373 more nodes in this community*

## Relationships

- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (102 shared connections)
- [combat taunt](combat_taunt.md) (58 shared connections)
- [get current tick()](get_current_tick%28%29.md) (39 shared connections)
- [main()](main%28%29.md) (21 shared connections)
- [combat flee](combat_flee.md) (13 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (12 shared connections)
- [combat initialization](combat_initialization.md) (11 shared connections)
- [.end combat()](end_combat%28%29.md) (11 shared connections)
- [Spell Targeting](Spell_Targeting.md) (11 shared connections)
- [Any](Any.md) (9 shared connections)
- [. init ()](_init_%28%29.md) (8 shared connections)
- [test flee command](test_flee_command.md) (8 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_processor.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 1717 (98%)
- INFERRED: 36 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*