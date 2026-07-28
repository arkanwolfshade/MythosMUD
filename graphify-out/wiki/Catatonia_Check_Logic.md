# Catatonia Check Logic

> 76 nodes · cohesion 0.04

## Key Concepts

- **catatonia_check.py** (25 connections) — `server/command_handler/catatonia_check.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCatatoniaChecks** (21 connections) — `server/tests/unit/commands/test_command_validation.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **_load_player_for_catatonia_check()** (11 connections) — `server/command_handler/catatonia_check.py`
- **_is_catatonic()** (10 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_database()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_check_catatonia_registry()** (9 connections) — `server/command_handler/catatonia_check.py`
- **_query_lucidity_record()** (9 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (9 connections)
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **_fetch_lucidity_record()** (8 connections) — `server/command_handler/catatonia_check.py`
- **UUID** (8 connections)
- **_registry_player_id_value()** (7 connections) — `server/command_handler/catatonia_check.py`
- **_PersistenceGetPlayerByName** (6 connections) — `server/command_handler/catatonia_check.py`
- **_convert_player_id_to_uuid()** (4 connections) — `server/command_handler/catatonia_check.py`
- **CommandExecutionRequest** (3 connections)
- **.test_check_catatonia_block_allowed_command()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_no_app_state()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_block_uses_string_registry_key_when_player_id_not_uuid_or_str()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_database_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_catatonia_registry_not_catatonic()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 51 more nodes in this community*

## Relationships

- [Command Request App State](Command_Request_App_State.md) (14 shared connections)
- [Realtime Message Formatters](Realtime_Message_Formatters.md) (6 shared connections)
- [Player Cache](Player_Cache.md) (5 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (4 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (4 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (2 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Stats Planning Archive](Stats_Planning_Archive.md) (2 shared connections)
- [WebSocket Request Context](WebSocket_Request_Context.md) (1 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/catatonia_check.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 283 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*