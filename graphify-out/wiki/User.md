# User

> 128 nodes

## Key Concepts

- **CombatInstance** (176 connections) — `server/models/combat.py`
- **test_combat_flee_handler.py** (34 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (20 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (20 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_attack_handler.py** (15 connections) — `server/services/combat_attack_handler.py`
- **asyncio** (15 connections)
- **_check_involuntary_flee_with_session()** (11 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (10 connections) — `server/services/combat_flee_handler.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **.validate_and_get_combat_participants()** (8 connections) — `server/services/combat_attack_handler.py`
- **check_involuntary_flee()** (8 connections) — `server/services/combat_flee_handler.py`
- **._apply_damage()** (7 connections) — `server/services/combat_attack_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **_execute_npc_attack()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **test_execute_voluntary_flee_free_hits_error_logged()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_missing_participant_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_move_fails_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_roll_fail_consumes_action()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_success_moves_player()** (6 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_attack_handler.py`
- *... and 103 more nodes in this community*

## Relationships

- [test_combat_service.py](test_combat_service.py.md) (53 shared connections)
- [MythosMUDError](MythosMUDError.md) (31 shared connections)
- [NATSService](NATSService.md) (25 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (14 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (10 shared connections)
- [waitForMessage](waitForMessage.md) (8 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (7 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (6 shared connections)
- [ChatMessage](ChatMessage.md) (6 shared connections)
- [Any](Any.md) (5 shared connections)
- [test_container_query_helpers_async.py](test_container_query_helpers_async.py.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_flee_handler.py`
- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 434 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*