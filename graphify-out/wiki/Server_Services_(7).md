# Server Services (7)

> 139 nodes

## Key Concepts

- **combat.py** (50 connections) — `server/models/combat.py`
- **CombatParticipantData** (38 connections) — `server/services/combat_types.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **test_npc_combat_data_provider.py** (14 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **CombatStatus** (11 connections) — `server/models/combat.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **check_attacker_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **test_combat_initialization.py** (8 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **get_connection_manager_for_combat_check()** (7 connections) — `server/services/combat_service_start.py`
- **check_target_rest_and_grace_period()** (7 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (7 connections) — `server/services/combat_service_start.py`
- **register_combat()** (6 connections) — `server/services/combat_service_start.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- *... and 114 more nodes in this community*

## Relationships

- [Server Services (28)](Server_Services_%2828%29.md) (21 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (21 shared connections)
- [Server Models (2)](Server_Models_%282%29.md) (18 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (14 shared connections)
- [Server Commands](Server_Commands.md) (12 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (12 shared connections)
- [Server Services (5)](Server_Services_%285%29.md) (11 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (10 shared connections)
- [Server Services (36)](Server_Services_%2836%29.md) (10 shared connections)
- [Server Services (26)](Server_Services_%2826%29.md) (7 shared connections)
- [Server Commands (15)](Server_Commands_%2815%29.md) (7 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (6 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 575 (96%)
- INFERRED: 24 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*