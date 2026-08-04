# services combat sync

> 78 nodes

## Key Concepts

- **test_combat_service_modules.py** (62 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (8 connections) — `server/services/combat_service_events.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **broadcast_aggro_target_switches()** (7 connections) — `server/services/combat_service_events.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **test_register_combat_delegates_to_service()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **UUID** (4 connections)
- **test_validate_combat_can_start_raises_when_in_combat()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_ok()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_success()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_handle_combat_completion_end_error_swallowed()** (4 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 53 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (45 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [commands communication say](commands_communication_say.md) (5 shared connections)
- [Item Instances](Item_Instances.md) (4 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (3 shared connections)
- [player look commands](player_look_commands.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [dead letter queue](dead_letter_queue.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 323 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*