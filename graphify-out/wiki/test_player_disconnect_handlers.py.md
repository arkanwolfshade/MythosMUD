# test_player_disconnect_handlers.py

> 97 nodes

## Key Concepts

- **test_combat_service_modules.py** (62 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (36 connections)
- **combat_service_events.py** (15 connections) — `server/services/combat_service_events.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (8 connections) — `server/services/combat_service_attack.py`
- **broadcast_aggro_target_switches()** (8 connections) — `server/services/combat_service_events.py`
- **publish_npc_damage_event()** (8 connections) — `server/services/combat_service_events.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **publish_npc_died_event()** (7 connections) — `server/services/combat_service_events.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._get_persistence()** (5 connections) — `server/services/combat_hp_sync.py`
- **._update_and_save_player_dp()** (5 connections) — `server/services/combat_hp_sync.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_melee_location_paths()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_melee_or_end_combat_ends()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **._log_death_threshold_events()** (4 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (4 connections) — `server/services/combat_hp_sync.py`
- *... and 72 more nodes in this community*

## Relationships

- [MythosMUDError](MythosMUDError.md) (22 shared connections)
- [NATSService](NATSService.md) (11 shared connections)
- [.get_instance](get_instance.md) (7 shared connections)
- [User](User.md) (6 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [ChatMessage](ChatMessage.md) (1 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 245 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*