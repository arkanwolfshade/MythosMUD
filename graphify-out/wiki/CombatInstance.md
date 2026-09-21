# CombatInstance

> 139 nodes

## Key Concepts

- **CombatInstance** (201 connections) — `server/models/combat.py`
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
- *... and 114 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (49 shared connections)
- [get_config](get_config.md) (41 shared connections)
- [CombatService](CombatService.md) (26 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (19 shared connections)
- [combat_service.py](combat_service.py.md) (16 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (7 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (7 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (7 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (6 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (4 shared connections)
- [test_flee_command.py](test_flee_command.py.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 491 (100%)
- INFERRED: 2 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*