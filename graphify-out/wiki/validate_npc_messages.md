# .validate_npc_messages

> 12 nodes

## Key Concepts

- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **CombatMessages** (5 connections)
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **Any** (1 connections)
- **Generate combat start messages for all room occupants. Args: attacker_name:…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate combat end messages for all room occupants. Args: winner_name: Name of…** (1 connections) — `server/services/combat_messaging_service.py`
- **Validate NPC message templates against the schema. Args: messages_data: NPC…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate an attack message based on perspective and NPC configuration. Args:…** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate a death message for an NPC. Args: npc_name: Name of the NPC that died…** (1 connections) — `server/services/combat_messaging_service.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [test_combat_schema.py](test_combat_schema.py.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 18 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*