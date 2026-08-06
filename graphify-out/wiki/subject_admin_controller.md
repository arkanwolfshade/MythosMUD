# subject admin controller

> 90 nodes

## Key Concepts

- **test_combat_service_modules.py** (62 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **handle_combat_completion()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (10 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (10 connections) — `server/services/combat_service_attack.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **UUID** (6 connections)
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **test_register_combat_delegates_to_service()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_raises_when_in_combat()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_ok()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_success()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 65 more nodes in this community*

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (28 shared connections)
- [Item Instances](Item_Instances.md) (17 shared connections)
- [command factories exploration](command_factories_exploration.md) (11 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (9 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (6 shared connections)
- [player look commands](player_look_commands.md) (5 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (4 shared connections)
- [game chat service](game_chat_service.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (3 shared connections)
- [models player rationale](models_player_rationale.md) (2 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (2 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 404 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*