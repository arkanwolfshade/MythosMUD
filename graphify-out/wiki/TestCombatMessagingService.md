# TestCombatMessagingService

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

- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (2 shared connections)
- [combat_schema.py](combat_schema.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 87 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*