# AGENTS Architecture Guidelines

> 16 nodes · cohesion 0.13

## Key Concepts

- **optimized_security_validator.py** (21 connections) — `server/validators/optimized_security_validator.py`
- **optimized_strip_ansi_codes()** (8 connections) — `server/validators/optimized_security_validator.py`
- **benchmark_validation_performance()** (5 connections) — `server/validators/optimized_security_validator.py`
- **test_benchmark_validation_performance()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_strip_ansi_codes_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_strip_ansi_codes_no_ansi()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_strip_ansi_codes_with_ansi()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **_cached_strip_ansi()** (3 connections) — `server/validators/optimized_security_validator.py`
- **Test benchmark function runs without errors.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test stripping ANSI codes from empty string.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test stripping ANSI codes from text without ANSI.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test stripping ANSI codes from text with ANSI.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Optimized security validation functions for MythosMUD.  This module provides per** (1 connections) — `server/validators/optimized_security_validator.py`
- **Benchmark the performance of optimized vs original validation functions.** (1 connections) — `server/validators/optimized_security_validator.py`
- **Cached version of strip_ansi for repeated inputs.** (1 connections) — `server/validators/optimized_security_validator.py`
- **Optimized ANSI code removal with caching.      Args:         text: Input text th** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [WebSocket Handler Tests](WebSocket_Handler_Tests.md) (9 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Archive Architecture Remediation](Archive_Architecture_Remediation.md) (2 shared connections)
- [Architecture Container System](Architecture_Container_System.md) (2 shared connections)
- [Command Factories Moderation](Command_Factories_Moderation.md) (1 shared connections)
- [Cursor Agents Performance](Cursor_Agents_Performance.md) (1 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (1 shared connections)
- [Logging Structured Setup](Logging_Structured_Setup.md) (1 shared connections)
- [Optimized Security Validator Tests](Optimized_Security_Validator_Tests.md) (1 shared connections)
- [Archive Connection Termination](Archive_Connection_Termination.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*