# commands communication support

> 24 nodes

## Key Concepts

- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **combat_messaging_service.py** (9 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **CombatMessages** (6 connections)
- **test_combat_messaging_service.py** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **Base integration with connection manager resolution.** (1 connections) — `server/services/combat_messaging/base.py`
- **Base class with connection manager setup. Used by CombatMessagingIntegration.** (1 connections) — `server/services/combat_messaging/base.py`
- **Combat messaging service for thematic combat messages.  This service handles the** (1 connections) — `server/services/combat_messaging_service.py`
- **Service for generating combat messages.      This service creates thematic, pers** (1 connections) — `server/services/combat_messaging_service.py`
- **Initialize the combat messaging service.** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate an attack message based on perspective and NPC configuration.** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate a death message for an NPC.          Args:             npc_name: Name o** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate combat start messages for all room occupants.          Args:** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate combat end messages for all room occupants.          Args:** (1 connections) — `server/services/combat_messaging_service.py`
- **Generate thematic error messages for combat actions.          Args:** (1 connections) — `server/services/combat_messaging_service.py`
- **Unit tests for combat messaging service.  Tests the CombatMessagingService class** (1 connections) — `server/tests/unit/services/test_combat_messaging_service.py`

## Relationships

- [combat services messaging](combat_services_messaging.md) (11 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [tick game processing](tick_game_processing.md) (3 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 80 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*