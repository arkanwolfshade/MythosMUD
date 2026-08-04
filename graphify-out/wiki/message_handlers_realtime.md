# message handlers realtime

> 20 nodes

## Key Concepts

- **test_lucidity_command_disruption.py** (14 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **lucidity_command_disruption.py** (9 connections) — `server/services/lucidity_command_disruption.py`
- **should_misfire_command()** (7 connections) — `server/services/lucidity_command_disruption.py`
- **should_involuntary_flee()** (7 connections) — `server/services/lucidity_command_disruption.py`
- **get_misfire_message()** (4 connections) — `server/services/lucidity_command_disruption.py`
- **can_perform_action()** (4 connections) — `server/services/lucidity_command_disruption.py`
- **test_should_misfire_ignores_simple_commands()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_should_misfire_catatonic_always()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_should_misfire_fractured_roll()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_should_misfire_fractured_miss()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_get_misfire_messages_by_tier()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_should_involuntary_flee_deranged_high_damage()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_should_involuntary_flee_wrong_tier_or_low_damage()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **test_can_perform_action()** (2 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`
- **Command disruption utilities for lucidity system.  Implements command misfires a** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if a command should misfire based on tier and command type.      Args:** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Get the misfire message for a failed command.      Args:         command_type: T** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if player should involuntarily flee.      Args:         tier: Current luci** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Check if player can perform actions (motor lock check).      Args:         tier:** (1 connections) — `server/services/lucidity_command_disruption.py`
- **Unit tests for lucidity command disruption.** (1 connections) — `server/tests/unit/services/test_lucidity_command_disruption.py`

## Relationships

- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/services/test_lucidity_command_disruption.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*