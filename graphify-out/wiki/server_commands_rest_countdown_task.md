# server commands rest countdown task

> 15 nodes

## Key Concepts

- **rest_countdown_task.py** (13 connections) — `server/commands/rest_countdown_task.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **UUID** (6 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **Task** (1 connections)
- **Rest countdown task implementation. This module contains the async task that…** (1 connections) — `server/commands/rest_countdown_task.py`
- **Create and return a rest countdown task. Args: player_id: The player's ID…** (1 connections) — `server/commands/rest_countdown_task.py`
- **Check if rest countdown was interrupted. Args: player_id: Player UUID…** (1 connections) — `server/commands/rest_countdown_task.py`
- **Send countdown message to player. Args: player_id: Player UUID remaining:…** (1 connections) — `server/commands/rest_countdown_task.py`
- **Execute countdown loop, sending messages every second. Args: player_id: Player…** (1 connections) — `server/commands/rest_countdown_task.py`
- **Disconnect player after rest countdown completes. Args: player_id: Player UUID…** (1 connections) — `server/commands/rest_countdown_task.py`

## Relationships

- [server container main get container](server_container_main_get_container.md) (4 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*