# CommandHandler

> 146 nodes

## Key Concepts

- **test_lucidity_recovery_commands.py** (34 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_active_lucidity_service.py** (34 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **lucidity_recovery_commands.py** (25 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (22 connections) — `server/commands/lucidity_recovery_commands.py`
- **ActiveLucidityService** (20 connections) — `server/services/active_lucidity_service.py`
- **LucidityActionOnCooldownError** (16 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **handle_meditate_command()** (11 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections)
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_restore_mp_for_action()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **UUID** (4 connections)
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **test_handle_pray_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 121 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (17 shared connections)
- [Player Position Service](Player_Position_Service.md) (12 shared connections)
- [Any](Any.md) (8 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [Lock](Lock.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [test_get_valid_exits_empty_room](test_get_valid_exits_empty_room.md) (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 460 (97%)
- INFERRED: 16 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*