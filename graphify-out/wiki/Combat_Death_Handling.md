# Combat Death Handling

> 97 nodes

## Key Concepts

- **CombatInstance** (169 connections) — `server/models/combat.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (8 connections) — `server/services/lucidity_command_disruption.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **UUID** (5 connections)
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (4 connections)
- **.validate_melee_location()** (4 connections) — `server/services/combat_service.py`
- **.check_involuntary_flee()** (4 connections) — `server/services/combat_service.py`
- *... and 72 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (53 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (21 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (21 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (14 shared connections)
- [Health Check Models](Health_Check_Models.md) (12 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (12 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (10 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (8 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (7 shared connections)
- [Game Client Container](Game_Client_Container.md) (6 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (5 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 451 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*