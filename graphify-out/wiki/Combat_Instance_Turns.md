# Combat Instance Turns

> 165 nodes

## Key Concepts

- **CombatInstance** (271 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (43 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (33 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (25 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (21 connections)
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **execute_flee_failed_free_hits()** (14 connections) — `server/services/combat_flee_handler.py`
- **UUID** (12 connections)
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (10 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **_FleeFreeHitsCombatService** (9 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **process_npc_turn()** (9 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_npc_participant()** (9 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_one_opponent()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_combat_ended()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_target_died()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_two_opponents_turn_order()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (8 connections)
- **_ordered_free_hit_attackers()** (7 connections) — `server/services/combat_flee_handler.py`
- **_alive_result()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_no_opponents_noop()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_acting_opponents()** (6 connections) — `server/services/combat_flee_handler.py`
- **_deliver_one_flee_free_hit()** (6 connections) — `server/services/combat_flee_handler.py`
- *... and 140 more nodes in this community*

## Relationships

- [Combat Participants](Combat_Participants.md) (60 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (48 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (32 shared connections)
- [Community 52](Community_52.md) (21 shared connections)
- [Community 121](Community_121.md) (20 shared connections)
- [Community 134](Community_134.md) (13 shared connections)
- [Community 126](Community_126.md) (10 shared connections)
- [Community 118](Community_118.md) (10 shared connections)
- [Community 217](Community_217.md) (8 shared connections)
- [Community 227](Community_227.md) (7 shared connections)
- [Community 398](Community_398.md) (7 shared connections)
- [Community 197](Community_197.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 599 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*