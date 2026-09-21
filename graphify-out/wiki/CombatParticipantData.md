# CombatParticipantData

> 87 nodes

## Key Concepts

- **CombatParticipantData** (39 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **.create_combat_instance()** (18 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (16 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **check_attacker_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **register_combat()** (7 connections) — `server/services/combat_service_start.py`
- **get_connection_manager_for_combat_check()** (6 connections) — `server/services/combat_service_start.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **.attacker_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.target_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **_AppStateWithConnectionManager** (3 connections) — `server/services/combat_service_start.py`
- **_AppWithState** (3 connections) — `server/services/combat_service_start.py`
- **.test_create_combat_instance_auto_progression_disabled()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_basic()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 62 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (25 shared connections)
- [CombatService](CombatService.md) (12 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (12 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)

## Source Files

- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 187 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*