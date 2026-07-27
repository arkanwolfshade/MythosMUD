# .test_get_attack_message_defender_perspective

> 12 nodes · cohesion 0.17

## Key Concepts

- **CombatMessages** (6 connections)
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **Any** (2 connections)
- **Generate combat start messages for all room occupants.          Args:** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate combat end messages for all room occupants.          Args:** (1 connections) — `server/services/combat_messaging_service.py`
- **Validate NPC message templates against the schema.          Args:             me** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate an attack message based on perspective and NPC configuration.** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate a death message for an NPC.          Args:             npc_name: Name o** (1 connections) — `server/services/combat_messaging_service.py`

## Relationships

- [ConnectionManager](ConnectionManager.md) (5 shared connections)
- [MythosMUDError](MythosMUDError.md) (3 shared connections)
- [test_combat_schema.py](test_combat_schema.py.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 29 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*