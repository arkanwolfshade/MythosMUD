# test_combat_service_modules.py

> 123 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (36 connections)
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **check_attacker_grace_period()** (9 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **broadcast_aggro_target_switches()** (8 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (8 connections) — `server/services/combat_service_events.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **get_connection_manager_for_combat_check()** (7 connections) — `server/services/combat_service_start.py`
- **register_combat()** (7 connections) — `server/services/combat_service_start.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- *... and 98 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (41 shared connections)
- [get_logger](get_logger.md) (16 shared connections)
- [CombatParticipantType](CombatParticipantType.md) (14 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (12 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [NATSError](NATSError.md) (8 shared connections)
- [models/combat.py](models-combat.py.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (3 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)

## Source Files

- `server/services/aggro_threat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 333 (90%)
- INFERRED: 36 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*