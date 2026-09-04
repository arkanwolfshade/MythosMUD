# Test Combat Service Modules

> 97 nodes

## Key Concepts

- **test_combat_service_modules.py** (57 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **combat_service_start.py** (21 connections) — `server/services/combat_service_start.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **check_attacker_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (7 connections) — `server/services/combat_service_start.py`
- **register_combat()** (7 connections) — `server/services/combat_service_start.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- **CombatService** (7 connections)
- **test_publish_combat_started_event_handles_errors()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **get_connection_manager_for_combat_check()** (5 connections) — `server/services/combat_service_start.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_allows_disconnect_grace_target()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_success()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 72 more nodes in this community*

## Relationships

- [Combat Events](Combat_Events.md) (8 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (5 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (4 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (4 shared connections)
- [Game State Provider](Game_State_Provider.md) (3 shared connections)
- [NATS Messaging Config](NATS_Messaging_Config.md) (2 shared connections)
- [Test Login Grace Period](Test_Login_Grace_Period.md) (1 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)

## Source Files

- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 228 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*