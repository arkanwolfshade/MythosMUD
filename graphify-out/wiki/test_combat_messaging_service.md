# test combat messaging service

> 59 nodes

## Key Concepts

- **TestCombatMessagingService** (21 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatMessages** (6 connections)
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **test_combat_messaging_service.py** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.service()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **Any** (2 connections)
- **.test_get_attack_message_attacker_perspective()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_defender_perspective()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_other_perspective()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_custom_action_type()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_custom_npc_messages()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_attack_message_fallback_to_default()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_death_message_default()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_death_message_custom()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_start_messages()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.test_get_combat_start_messages_single_occupant()** (2 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [Any](Any.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 135 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*