# combatmessages

> 43 nodes

## Key Concepts

- **CombatMessagingService** (17 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (11 connections) — `server/services/combat_messaging/integration.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging/base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging_service.py** (9 connections) — `server/services/combat_messaging_service.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **.validate_npc_messages()** (6 connections) — `server/services/combat_messaging_service.py`
- **CombatMessages** (5 connections)
- **test_combat_messaging_service.py** (5 connections) — `server/tests/unit/services/test_combat_messaging_service.py`
- **.__init__()** (3 connections) — `server/services/combat_messaging/base.py`
- **.get_attack_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_end_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_combat_start_messages()** (3 connections) — `server/services/combat_messaging_service.py`
- **.get_death_message()** (3 connections) — `server/services/combat_messaging_service.py`
- **combat_messaging/__init__.py** (3 connections) — `server/services/combat_messaging/__init__.py`
- **.get_error_message()** (2 connections) — `server/services/combat_messaging_service.py`
- **.__init__()** (2 connections) — `server/services/combat_messaging_service.py`
- **Any** (1 connections)
- **Base integration with connection manager resolution.** (1 connections) — `server/services/combat_messaging/base.py`
- **Base for mixins that require connection_manager. Satisfies mypy attr-defined…** (1 connections) — `server/services/combat_messaging/base.py`
- *... and 18 more nodes in this community*

## Relationships

- [server realtime envelope build event](server_realtime_envelope_build_event.md) (18 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (11 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (6 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (3 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (3 shared connections)
- [draft7validator](draft7validator.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 104 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*