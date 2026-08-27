# MythosMUDError

> 157 nodes

## Key Concepts

- **CombatService** (165 connections) — `server/services/combat_service.py`
- **combat_service.py** (74 connections) — `server/services/combat_service.py`
- **combat_service_attack.py** (25 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **UUID** (20 connections)
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **finalize_attack_result()** (10 connections) — `server/services/combat_service_attack.py`
- **.__init__()** (10 connections) — `server/services/combat_service.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **test_combat_service_npc_in_combat.py** (9 connections) — `server/tests/unit/services/test_combat_service_npc_in_combat.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **get_combat_service()** (7 connections) — `server/services/combat_service_state.py`
- **._handle_player_death_events()** (6 connections) — `server/services/combat_death_handler.py`
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **.finalize_attack_result()** (6 connections) — `server/services/combat_service.py`
- **.validate_melee_or_end_combat()** (6 connections) — `server/services/combat_service.py`
- **UUID** (6 connections)
- **combat_service_state.py** (6 connections) — `server/services/combat_service_state.py`
- **.handle_target_state_changes()** (5 connections) — `server/services/combat_death_handler.py`
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **.apply_attack_damage()** (5 connections) — `server/services/combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- *... and 132 more nodes in this community*

## Relationships

- [User](User.md) (31 shared connections)
- [NATSService](NATSService.md) (27 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (25 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (22 shared connections)
- [.get_instance](get_instance.md) (19 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (19 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (15 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (13 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (13 shared connections)
- [ChatMessage](ChatMessage.md) (9 shared connections)
- [PydanticErrorHandler](PydanticErrorHandler.md) (6 shared connections)
- [Any](Any.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 406 (84%)
- INFERRED: 76 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*