# test_combat_flee_handler.py

> 94 nodes

## Key Concepts

- **test_combat_flee_handler.py** (43 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (36 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (25 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (21 connections)
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **execute_flee_failed_free_hits()** (14 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **UUID** (11 connections)
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **_make_npc_participant()** (9 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_FleeFreeHitsCombatService** (8 connections) — `server/services/combat_flee_handler.py`
- **_resolve_free_hit_damage()** (8 connections) — `server/services/combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_one_opponent()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_combat_ended()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_target_died()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_two_opponents_turn_order()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_ordered_free_hit_attackers()** (7 connections) — `server/services/combat_flee_handler.py`
- **_alive_result()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_no_opponents_noop()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_acting_opponents()** (6 connections) — `server/services/combat_flee_handler.py`
- **_deliver_one_flee_free_hit()** (6 connections) — `server/services/combat_flee_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 69 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (25 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [CombatParticipant](CombatParticipant.md) (11 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [test_lucidity_command_disruption.py](test_lucidity_command_disruption.py.md) (3 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (2 shared connections)
- [resolve_npc_attack_damage](resolve_npc_attack_damage.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 271 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*