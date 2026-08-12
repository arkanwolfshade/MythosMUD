# Rate Limiter Utilities

> 27 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **command_helpers.py** (15 connections) — `server/utils/command_helpers.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_empty_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Any** (2 connections)
- **Unit tests for command helper utilities.  Tests helper functions for command par** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user with Player object.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user with username attribute.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user with name attribute.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user with dict containing username.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user with dict containing name.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user raises error with invalid user object.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user raises error with empty dict.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user raises error with None.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_username_from_user prioritizes player name over username.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Helper functions for command parsing and validation.  This module contains utili** (1 connections) — `server/utils/command_helpers.py`
- *... and 2 more nodes in this community*

## Relationships

- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (13 shared connections)
- [Archive Circuit Breaker](Archive_Circuit_Breaker.md) (6 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (4 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (3 shared connections)
- [Player Event Handler Tests](Player_Event_Handler_Tests.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (2 shared connections)
- [Player GUID Formatter](Player_GUID_Formatter.md) (2 shared connections)
- [Game Client Container](Game_Client_Container.md) (2 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 108 (78%)
- INFERRED: 30 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*