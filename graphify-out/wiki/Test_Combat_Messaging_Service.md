# Test Combat Messaging Service

> 60 nodes

## Key Concepts

- **TestCombatMessagingService** (21 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **asyncio** (16 connections)
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **CombatMessages** (5 connections)
- **test_combat_messaging_service.py** (5 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.service()** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.test_get_attack_message_attacker_perspective()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_custom_action_type()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_custom_npc_messages()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_defender_perspective()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_fallback_to_default()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_high_damage()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_other_perspective()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_zero_damage()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_end_messages()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_end_messages_empty_occupants()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_end_messages_loser_perspective()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_end_messages_winner_perspective()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_start_messages()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_start_messages_single_occupant()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- *... and 35 more nodes in this community*

## Relationships

- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)
- [Migrate Combat Data](Migrate_Combat_Data.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 87 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*