# Container Component Capacity

> 148 nodes

## Key Concepts

- **CombatInstance** (169 connections) — `server/models/combat.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **UUID** (20 connections)
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (8 connections) — `server/services/lucidity_command_disruption.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.is_dead()** (5 connections) — `server/models/combat.py`
- **.get_alive_participants()** (5 connections) — `server/models/combat.py`
- **UUID** (5 connections)
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **.validate_and_get_combat_participants()** (5 connections) — `server/services/combat_service.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **.handle_attack_events_and_xp()** (5 connections) — `server/services/combat_service.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 123 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (68 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (32 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (28 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (22 shared connections)
- [Health Check Models](Health_Check_Models.md) (11 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (10 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (7 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (5 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (5 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (4 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 585 (97%)
- INFERRED: 19 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*