# Rest Command Flow

> 125 nodes · cohesion 0.03

## Key Concepts

- **test_rest_command.py** (37 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (23 connections) — `server/commands/rest_command.py`
- **test_rest_and_grace_period.py** (23 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **handle_rest_command()** (21 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (17 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (11 connections) — `server/commands/rest_command.py`
- **Any** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_rest_interrupt_payload_if_moving()** (7 connections) — `server/commands/go_command.py`
- **_disconnect_player_intentionally()** (7 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_intentional_disconnect_no_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 100 more nodes in this community*

## Relationships

- [[Alias Expansion Logic]] (9 shared connections)
- [[Look Command Helpers]] (5 shared connections)
- [[Disconnect Grace Period]] (5 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Magic Command Handlers]] (4 shared connections)
- [[Combat Service Bundle]] (4 shared connections)
- [[Commands Go Command]] (3 shared connections)
- [[Commands Rest Countdown]] (3 shared connections)
- [[Player Position Service]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Commands Rest Command]] (2 shared connections)
- [[Ground and Rescue Commands]] (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/go_command.py`
- `server/commands/rest_command.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 449 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
