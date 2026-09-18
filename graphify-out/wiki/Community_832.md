# Community 832

> 19 nodes

## Key Concepts

- **test_alias_expansion.py** (13 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (11 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (10 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **asyncio** (5 connections)
- **test_check_alias_safety_cycle_detected()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_delegates()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_depth_limit()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_invalid_content()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_ok()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_validate_expanded_command_too_long()** (2 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **Any** (1 connections)
- **CommandExecutionRequest** (1 connections)
- **Handle command processing with alias expansion and loop detection. This…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Check if an alias is safe to expand. Builds an alias dependency graph and…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Validate an expanded command for length and content. Args: expanded_command:…** (1 connections) — `server/command_handler/alias_expansion.py`
- **Unit tests for alias_expansion module.** (1 connections) — `server/tests/unit/commands/test_alias_expansion.py`

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (4 shared connections)
- [Community 256](Community_256.md) (3 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (3 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (3 shared connections)
- [Community 573](Community_573.md) (1 shared connections)
- [Community 432](Community_432.md) (1 shared connections)
- [Community 120](Community_120.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*