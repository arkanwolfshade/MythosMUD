# services combat sync

> 85 nodes

## Key Concepts

- **test_combat_service_modules.py** (62 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_attack.py** (27 connections) — `server/services/combat_service_attack.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (13 connections) — `server/services/combat_hp_sync.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **handle_combat_completion()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (11 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (10 connections) — `server/services/combat_service_attack.py`
- **process_attack()** (10 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **._persist_player_dp_sync()** (8 connections) — `server/services/combat_hp_sync.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **UUID** (6 connections)
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **test_finalize_attack_result_and_process_attack()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._verify_player_save()** (4 connections) — `server/services/combat_hp_sync.py`
- **._log_death_threshold_events()** (4 connections) — `server/services/combat_hp_sync.py`
- **test_publish_combat_started_event_success()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 60 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (15 shared connections)
- [Item Instances](Item_Instances.md) (12 shared connections)
- [command factories exploration](command_factories_exploration.md) (10 shared connections)
- [combat commands handler](combat_commands_handler.md) (9 shared connections)
- [rest grace period](rest_grace_period.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [NPC Combat](NPC_Combat.md) (8 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (6 shared connections)
- [movement monitor game](movement_monitor_game.md) (5 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (4 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (3 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 382 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*