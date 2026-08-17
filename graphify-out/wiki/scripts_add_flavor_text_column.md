# scripts add flavor text column

> 150 nodes

## Key Concepts

- **get_async_session()** (51 connections) — `server/database.py`
- **test_active_lucidity_service.py** (35 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (27 connections) — `server/commands/rescue_commands.py`
- **asyncio** (25 connections)
- **test_rescue_commands.py** (24 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **ActiveLucidityService** (23 connections) — `server/services/active_lucidity_service.py`
- **asyncio** (17 connections)
- **handle_rescue_command()** (15 connections) — `server/commands/rescue_commands.py`
- **npc_combat_lucidity.py** (13 connections) — `server/services/npc_combat_lucidity.py`
- **UnknownEncounterCategoryError** (9 connections) — `server/services/active_lucidity_service.py`
- **Any** (9 connections)
- **_run_ground_session()** (8 connections) — `server/commands/rescue_commands.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **patch** (7 connections)
- **_get_ground_services()** (6 connections) — `server/commands/rescue_commands.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **UUID** (6 connections)
- **_complete_ground_command()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- *... and 125 more nodes in this community*

## Relationships

- [server commands admin setlucidity command](server_commands_admin_setlucidity_command.md) (27 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (19 shared connections)
- [server services npc combat integration](server_services_npc_combat_integration.md) (10 shared connections)
- [server commands lucidity recovery commands](server_commands_lucidity_recovery_commands.md) (7 shared connections)
- [server services lucidity event dispatcher](server_services_lucidity_event_dispatcher.md) (5 shared connections)
- [server database close db](server_database_close_db.md) (5 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (4 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [server commands position commands](server_commands_position_commands.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [asyncsessionfactory](asyncsessionfactory.md) (3 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/commands/rescue_commands.py`
- `server/database.py`
- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/commands/test_rescue_commands.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 358 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*