# Lucidity Recovery Commands

> 74 nodes · cohesion 0.05

## Key Concepts

- **test_lucidity_recovery_commands.py** (32 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **lucidity_recovery_commands.py** (24 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_pray_command()** (21 connections) — `server/commands/lucidity_recovery_commands.py`
- **LucidityActionOnCooldownError** (16 connections) — `server/services/active_lucidity_service.py`
- **_perform_recovery_action()** (15 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_meditate_command()** (10 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_group_solace_command()** (9 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_folk_tonic_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **handle_therapy_command()** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **Any** (8 connections) — `server/commands/lucidity_recovery_commands.py`
- **AliasStorage** (6 connections) — `server/commands/lucidity_recovery_commands.py`
- **_validate_recovery_context()** (5 connections) — `server/commands/lucidity_recovery_commands.py`
- **_format_cooldown_message()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **_restore_mp_for_action()** (4 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_group_solace_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_naive_datetime()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_cooldown_object()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_cooldown_no_expiry()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_pray_command_unknown_action()** (4 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **_format_recovery_success_message()** (3 connections) — `server/commands/lucidity_recovery_commands.py`
- **test_handle_folk_tonic_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_group_solace_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- **test_handle_meditate_command_delegates()** (3 connections) — `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- *... and 49 more nodes in this community*

## Relationships

- [[Active Lucidity Service]] (12 shared connections)
- [[Alias Expansion Logic]] (10 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Command Helper Utilities]] (1 shared connections)
- [[Communication Command Handlers]] (1 shared connections)
- [[Spellbook Read Command]] (1 shared connections)
- [[Admin Status Commands]] (1 shared connections)
- [[NPC Population Control]] (1 shared connections)
- [[Inventory Service Helpers]] (1 shared connections)
- [[Lucidity State Models]] (1 shared connections)

## Source Files

- `server/commands/lucidity_recovery_commands.py`
- `server/services/active_lucidity_service.py`
- `server/tests/unit/commands/test_lucidity_recovery_commands.py`
- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 285 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
