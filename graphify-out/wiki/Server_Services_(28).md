# Server Services (28)

> 68 nodes

## Key Concepts

- **CombatInstance** (167 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **.publish_combat_ended_event()** (5 connections) — `server/services/combat_event_handler.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (4 connections)
- **.get_participants_by_initiative()** (4 connections) — `server/models/combat.py`
- **UUID** (4 connections)
- **.validate_melee_location()** (4 connections) — `server/services/combat_service.py`
- **.check_involuntary_flee()** (4 connections) — `server/services/combat_service.py`
- **.handle_target_state_changes()** (4 connections) — `server/services/combat_service.py`
- **.apply_damage()** (3 connections) — `server/models/combat.py`
- **.get_current_turn_participant()** (3 connections) — `server/models/combat.py`
- *... and 43 more nodes in this community*

## Relationships

- [Server Models (2)](Server_Models_%282%29.md) (49 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (21 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (20 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (18 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (14 shared connections)
- [Server Services (36)](Server_Services_%2836%29.md) (12 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (9 shared connections)
- [Server Commands (20)](Server_Commands_%2820%29.md) (8 shared connections)
- [Server Services (26)](Server_Services_%2826%29.md) (8 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (6 shared connections)
- [Server Commands (37)](Server_Commands_%2837%29.md) (4 shared connections)
- [Server Services (68)](Server_Services_%2868%29.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 356 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*