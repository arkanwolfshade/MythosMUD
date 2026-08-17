# server tests unit validators test

> 22 nodes

## Key Concepts

- **command_validator.py** (17 connections) — `server/validators/command_validator.py`
- **clean_command_input()** (9 connections) — `server/validators/command_validator.py`
- **server/validators/__init__.py** (9 connections) — `server/validators/__init__.py`
- **is_suspicious_input()** (8 connections) — `server/validators/command_validator.py`
- **test_clean_command_input_basic()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_empty()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_unicode()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_clean_command_input_whitespace()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_safe()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_sql_injection()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **test_is_suspicious_input_xss()** (3 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that safe commands are not flagged as suspicious.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that SQL injection patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test that XSS patterns are detected.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning basic command input.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning command with extra whitespace.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning empty command.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Test cleaning command with unicode characters.** (1 connections) — `server/tests/unit/validators/test_command_validator.py`
- **Command input validation utilities for MythosMUD. This module provides…** (1 connections) — `server/validators/command_validator.py`
- **Check if command contains suspicious patterns that might indicate injection…** (1 connections) — `server/validators/command_validator.py`
- **Clean and normalize command input with comprehensive sanitization. This…** (1 connections) — `server/validators/command_validator.py`
- **Input validation utilities for MythosMUD. This package provides validation…** (1 connections) — `server/validators/__init__.py`

## Relationships

- [server tests unit validators test](server_tests_unit_validators_test.md) (16 shared connections)
- [server models command alias aliascommand](server_models_command_alias_aliascommand.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server models command](server_models_command.md) (2 shared connections)
- [server command handler alias expansion](server_command_handler_alias_expansion.md) (1 shared connections)
- [server command handler command input](server_command_handler_command_input.md) (1 shared connections)
- [server command handler processing](server_command_handler_processing.md) (1 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_command_validator.py`
- `server/validators/__init__.py`
- `server/validators/command_validator.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*