# CombatParticipantData

> 85 nodes

## Key Concepts

- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **.connection_manager()** (16 connections) — `server/services/combat_messaging/base.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **check_attacker_grace_period()** (9 connections) — `server/services/combat_service_start.py`
- **test_combat_initialization.py** (9 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **get_connection_manager_for_combat_check()** (7 connections) — `server/services/combat_service_start.py`
- **register_combat()** (7 connections) — `server/services/combat_service_start.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **.attacker_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.target_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_auto_progression_disabled()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_basic()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **.test_create_combat_instance_damaged_participants()** (3 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 60 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (21 shared connections)
- [CombatParticipant](CombatParticipant.md) (12 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (10 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (6 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (5 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)

## Source Files

- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 182 (86%)
- INFERRED: 29 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*