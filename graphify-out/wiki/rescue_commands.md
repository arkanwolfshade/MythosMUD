# rescue commands

> 58 nodes

## Key Concepts

- **handle_ground_command()** (32 connections) — `server/commands/rescue_commands.py`
- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **Any** (7 connections)
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (5 connections)
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_rescue_command()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_state()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 33 more nodes in this community*

## Relationships

- [Any](Any.md) (13 shared connections)
- [. init ()](_init_%28%29.md) (10 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [UUID](UUID.md) (4 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (3 shared connections)
- [LiabilityStackEntry](LiabilityStackEntry.md) (2 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [.state()](state%28%29.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 229 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*