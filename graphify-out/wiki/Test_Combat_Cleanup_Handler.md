# Test Combat Cleanup Handler

> 121 nodes

## Key Concepts

- **models/combat.py** (60 connections) — `server/models/combat.py`
- **CombatParticipantType** (39 connections) — `server/models/combat.py`
- **CombatParticipantData** (31 connections) — `server/services/combat_types.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **combat_initialization.py** (15 connections) — `server/services/combat_initialization.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **CombatStatus** (10 connections) — `server/models/combat.py`
- **test_combat_initialization.py** (9 connections) — `server/tests/unit/services/test_combat_initialization.py`
- **CombatInitializer** (8 connections) — `server/services/combat_initialization.py`
- **clear_aggro_for_combat()** (6 connections) — `server/services/aggro_threat.py`
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **_build_participant()** (5 connections) — `server/services/combat_initialization.py`
- **_compute_turn_order()** (5 connections) — `server/services/combat_initialization.py`
- **.start_combat()** (5 connections) — `server/services/combat_service.py`
- **end_combat()** (5 connections) — `server/services/combat_service_end.py`
- **_build_combat_instance()** (4 connections) — `server/services/combat_initialization.py`
- **cleanup_handler()** (4 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.attacker_data()** (4 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 96 more nodes in this community*

## Relationships

- [Combat Events](Combat_Events.md) (16 shared connections)
- [Combat Turn Processing](Combat_Turn_Processing.md) (16 shared connections)
- [Test Combat Flee Handler](Test_Combat_Flee_Handler.md) (14 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (13 shared connections)
- [Test Aggro Threat](Test_Aggro_Threat.md) (11 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (11 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (10 shared connections)
- [Test Combat Attack](Test_Combat_Attack.md) (5 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (5 shared connections)
- [Combat Turn Participant Actions](Combat_Turn_Participant_Actions.md) (5 shared connections)
- [Test Combat Service Modules](Test_Combat_Service_Modules.md) (5 shared connections)
- [Combat Taunt](Combat_Taunt.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_end.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_initialization.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 318 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*