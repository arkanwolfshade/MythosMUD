# Community 836

> 19 nodes

## Key Concepts

- **test_alias_expansion.py** (17 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **handle_expanded_command()** (10 connections) — `server/command_handler/alias_expansion.py`
- **check_alias_safety()** (9 connections) — `server/command_handler/alias_expansion.py`
- **validate_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **asyncio** (5 connections)
- **test_check_alias_safety_cycle_detected()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_depth_too_deep()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_check_alias_safety_ok()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_depth_limit()** (4 connections) — `server/tests/unit/commands/test_alias_expansion.py`
- **test_handle_expanded_command_delegates()** (3 connections) — `server/tests/unit/commands/test_alias_expansion.py`
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

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (10 shared connections)
- [Community 262](Community_262.md) (3 shared connections)
- [Community 483](Community_483.md) (3 shared connections)
- [Community 98](Community_98.md) (2 shared connections)
- [Community 566](Community_566.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/tests/unit/commands/test_alias_expansion.py`

## Audit Trail

- EXTRACTED: 43 (86%)
- INFERRED: 7 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*