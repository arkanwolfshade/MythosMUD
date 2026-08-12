# combat_flee_handler.py

> 16 nodes

## Key Concepts

- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (8 connections) — `server/services/lucidity_command_disruption.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **should_involuntary_flee()** (4 connections) — `server/services/lucidity_command_disruption.py`
- **can_perform_action()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **get_misfire_message()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **should_misfire_command()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **Combat flee handler for involuntary and voluntary flee logic. Handles checking…** (1 connections) — `server/services/combat_flee_handler.py`
- **True if the involuntary-flee cooldown is still active.** (1 connections) — `server/services/combat_flee_handler.py`
- **Check tier, damage threshold, and cooldown; set cooldown and commit if flee…** (1 connections) — `server/services/combat_flee_handler.py`
- **Command disruption utilities for lucidity system. Implements command misfires…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if a command should misfire based on tier and command type. Args:…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Get the misfire message for a failed command. Args: command_type: Type of…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if player should involuntarily flee. Args: tier: Current lucidity tier…** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if player can perform actions (motor lock check). Args: tier: Current…** (1 connections) — `server/services/lucidity_command_disruption.py`

## Relationships

- [CombatInstance](CombatInstance.md) (8 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [LucidityService](LucidityService.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [database.py](database.py.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [run_flee_effect](run_flee_effect.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/services/lucidity_command_disruption.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*