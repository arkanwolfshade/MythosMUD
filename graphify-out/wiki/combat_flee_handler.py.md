# combat_flee_handler.py

> 23 nodes

## Key Concepts

- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (8 connections) — `server/services/lucidity_command_disruption.py`
- **check_involuntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **_handle_failed_voluntary_flee()** (6 connections) — `server/services/combat_flee_handler.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **UUID** (5 connections)
- **should_involuntary_flee()** (4 connections) — `server/services/lucidity_command_disruption.py`
- **Any** (3 connections)
- **can_perform_action()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **get_misfire_message()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **should_misfire_command()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **Combat flee handler for involuntary and voluntary flee logic. Handles checking…** (1 connections) — `server/services/combat_flee_handler.py`
- **Execute voluntary flee for a combat participant (shared by /flee command and…** (1 connections) — `server/services/combat_flee_handler.py`
- **True if the involuntary-flee cooldown is still active.** (1 connections) — `server/services/combat_flee_handler.py`
- **Check tier, damage threshold, and cooldown; set cooldown and commit if flee…** (1 connections) — `server/services/combat_flee_handler.py`
- **Check if player should involuntarily flee due to lucidity effects. Deranged…** (1 connections) — `server/services/combat_flee_handler.py`
- **Command disruption utilities for lucidity system. Implements command misfires…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if a command should misfire based on tier and command type. Args:…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Get the misfire message for a failed command. Args: command_type: Type of…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if player should involuntarily flee. Args: tier: Current lucidity tier…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if player can perform actions (motor lock check). Args: tier: Current…** (1 connections) — `server/services/lucidity_command_disruption.py`

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (7 shared connections)
- [Player](Player.md) (4 shared connections)
- [run_flee_effect](run_flee_effect.md) (3 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [combat_flee.py](combat_flee.py.md) (2 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/services/lucidity_command_disruption.py`

## Audit Trail

- EXTRACTED: 66 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*