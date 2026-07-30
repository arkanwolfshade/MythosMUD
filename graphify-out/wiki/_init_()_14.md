# . init ()

> 55 nodes

## Key Concepts

- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging_service.py** (9 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **CombatMessages** (6 connections)
- **Any** (5 connections)
- **._send_mortally_wounded_personal_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_death()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.broadcast_player_respawn()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.send_dp_decay_message()** (4 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **test_combat_messaging_service.py** (4 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **__init__.py** (3 connections) — `server/services/combat_messaging/__init__.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **._build_mortally_wounded_messages()** (3 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [time commands](time_commands.md) (10 shared connections)
- [world](world.md) (8 shared connections)
- [circuit breaker](circuit_breaker.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [test combat messaging service](test_combat_messaging_service.md) (4 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (3 shared connections)
- [combat](combat.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (1 shared connections)
- [get health service()](get_health_service%28%29.md) (1 shared connections)
- [test_parse_command_empty_string](test_parse_command_empty_string.md) (1 shared connections)
- [test combat messaging integration](test_combat_messaging_integration.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 195 (94%)
- INFERRED: 13 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*