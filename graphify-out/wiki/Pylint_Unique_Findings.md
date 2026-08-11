# Pylint Unique Findings

> 134 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **envelope.py** (28 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **get_next_sequence_impl()** (7 connections) — `server/realtime/connection_manager_methods.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- **UUID** (6 connections)
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- *... and 109 more nodes in this community*

## Relationships

- [Playwright E2E Specs](Playwright_E2E_Specs.md) (10 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (8 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (8 shared connections)
- [UI Player Event Handlers](UI_Player_Event_Handlers.md) (7 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (6 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (5 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (5 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (5 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (4 shared connections)
- [E2E Playwright Conversion Plan](E2E_Playwright_Conversion_Plan.md) (4 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (4 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (4 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/envelope.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 553 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*