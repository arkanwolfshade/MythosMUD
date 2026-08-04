# services combat sync

> 77 nodes

## Key Concepts

- **test_combat_service_modules.py** (62 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **handle_combat_completion()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (10 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (10 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (8 connections) — `server/services/combat_service_events.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **broadcast_aggro_target_switches()** (7 connections) — `server/services/combat_service_events.py`
- **UUID** (6 connections)
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **test_finalize_attack_result_and_process_attack()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **UUID** (4 connections)
- **test_publish_combat_started_event_success()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_handle_combat_completion_end_error_swallowed()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 52 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (35 shared connections)
- [Item Instances](Item_Instances.md) (12 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (12 shared connections)
- [command factories exploration](command_factories_exploration.md) (10 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (7 shared connections)
- [movement monitor game](movement_monitor_game.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)

## Source Files

- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 373 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*