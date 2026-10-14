# CombatInstance

> 174 nodes

## Key Concepts

- **CombatInstance** (271 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (43 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (36 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (25 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (21 connections)
- **execute_voluntary_flee()** (19 connections) — `server/services/combat_flee_handler.py`
- **execute_flee_failed_free_hits()** (14 connections) — `server/services/combat_flee_handler.py`
- **UUID** (12 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **_FleeFreeHitsCombatService** (9 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **_make_npc_participant()** (9 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **_resolve_free_hit_damage()** (8 connections) — `server/services/combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_one_opponent()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_combat_ended()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_stops_on_target_died()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_two_opponents_turn_order()** (8 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (8 connections)
- **._publish_npc_death_event()** (7 connections) — `server/services/combat_death_handler.py`
- **_ordered_free_hit_attackers()** (7 connections) — `server/services/combat_flee_handler.py`
- **_alive_result()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_flee_failed_free_hits_no_opponents_noop()** (7 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 149 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (74 shared connections)
- [CombatParticipant](CombatParticipant.md) (61 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (21 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (20 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (19 shared connections)
- [SuccessLevel](SuccessLevel.md) (12 shared connections)
- [combat_assist.py](combat_assist.py.md) (9 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (7 shared connections)
- [test_n_player_combat.py](test_n_player_combat.py.md) (7 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 612 (100%)
- INFERRED: 3 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*