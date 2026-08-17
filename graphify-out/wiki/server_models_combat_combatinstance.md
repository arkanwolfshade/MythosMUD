# server models combat combatinstance

> 126 nodes

## Key Concepts

- **CombatInstance** (162 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (34 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **asyncio** (15 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **check_involuntary_flee()** (9 connections) — `server/services/combat_flee_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._log_room_subscribers_before_npc_death()** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_roll_fail_consumes_action()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_success_moves_player()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **._handle_player_dp_update()** (5 connections) — `server/services/combat_service.py`
- **test_check_involuntary_flee_session_path()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_check_involuntary_flee_with_session_sets_cooldown()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- *... and 101 more nodes in this community*

## Relationships

- [server models combat combataction](server_models_combat_combataction.md) (50 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (35 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (25 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (19 shared connections)
- [server commands combat flee](server_commands_combat_flee.md) (8 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (6 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (4 shared connections)
- [server services combat initialization](server_services_combat_initialization.md) (4 shared connections)
- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (4 shared connections)
- [server models combat combatresult](server_models_combat_combatresult.md) (3 shared connections)
- [server services combat event handler](server_services_combat_event_handler.md) (3 shared connections)
- [server services lucidity command disruption](server_services_lucidity_command_disruption.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_service.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 391 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*