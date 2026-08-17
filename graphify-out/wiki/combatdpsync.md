# combatdpsync

> 95 nodes

## Key Concepts

- **test_combat_service_modules.py** (57 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **combat_service_attack.py** (19 connections) — `server/services/combat_service_attack.py`
- **_dp_sync()** (17 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_combat_instance()** (13 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **finalize_attack_result()** (9 connections) — `server/services/combat_service_attack.py`
- **handle_combat_completion()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **apply_damage_and_check_involuntary_flee()** (8 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (8 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **CombatService** (7 connections)
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (6 connections) — `server/services/combat_service_attack.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatParticipant** (6 connections)
- **UUID** (6 connections)
- **_melee_location_fail_reason()** (5 connections) — `server/services/combat_service_attack.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_melee_location_paths()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_melee_or_end_combat_ends()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatInstance** (5 connections)
- *... and 70 more nodes in this community*

## Relationships

- [server app game tick counter](server_app_game_tick_counter.md) (16 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (2 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [server events combat events](server_events_combat_events.md) (1 shared connections)

## Source Files

- `server/services/combat_service_attack.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 231 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*