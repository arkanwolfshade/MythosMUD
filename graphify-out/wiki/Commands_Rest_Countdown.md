# Commands Rest Countdown

> 15 nodes · cohesion 0.24

## Key Concepts

- **rest_countdown_task.py** (12 connections) — `server/commands/rest_countdown_task.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **UUID** (6 connections) — `server/commands/rest_countdown_task.py`
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections) — `server/commands/rest_countdown_task.py`
- **Rest countdown task implementation.  This module contains the async task that ha** (1 connections) — `server/commands/rest_countdown_task.py`
- **Create and return a rest countdown task.      Args:         player_id: The playe** (1 connections) — `server/commands/rest_countdown_task.py`
- **Check if rest countdown was interrupted.      Args:         player_id: Player UU** (1 connections) — `server/commands/rest_countdown_task.py`
- **Send countdown message to player.      Args:         player_id: Player UUID** (1 connections) — `server/commands/rest_countdown_task.py`
- **Execute countdown loop, sending messages every second.      Args:         player** (1 connections) — `server/commands/rest_countdown_task.py`
- **Disconnect player after rest countdown completes.      Args:         player_id:** (1 connections) — `server/commands/rest_countdown_task.py`
- **Task** (1 connections) — `server/commands/rest_countdown_task.py`

## Relationships

- [[Combat Player Broadcasts]] (4 shared connections)
- [[Rest Command Flow]] (3 shared connections)
- [[NPC Admin API]] (2 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
