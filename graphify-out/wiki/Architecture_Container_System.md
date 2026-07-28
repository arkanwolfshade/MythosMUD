# Architecture Container System

> 8 nodes · cohesion 0.25

## Key Concepts

- **optimized_comprehensive_sanitize_input()** (14 connections) — `server/validators/optimized_security_validator.py`
- **test_optimized_comprehensive_sanitize_input_empty()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_comprehensive_sanitize_input_normal()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **test_optimized_comprehensive_sanitize_input_normalizes_newlines()** (3 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive sanitization of empty string.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test comprehensive sanitization of normal text.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Test that optimized comprehensive sanitization normalizes newlines to spaces.** (1 connections) — `server/tests/unit/validators/test_optimized_security_validator.py`
- **Optimized comprehensive input sanitization.      Args:         text: Raw input t** (1 connections) — `server/validators/optimized_security_validator.py`

## Relationships

- [WebSocket Handler Tests](WebSocket_Handler_Tests.md) (5 shared connections)
- [AGENTS Architecture Guidelines](AGENTS_Architecture_Guidelines.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Archive Architecture Remediation](Archive_Architecture_Remediation.md) (1 shared connections)
- [Command Factories Moderation](Command_Factories_Moderation.md) (1 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (1 shared connections)
- [Archive Connection Termination](Archive_Connection_Termination.md) (1 shared connections)

## Source Files

- `server/tests/unit/validators/test_optimized_security_validator.py`
- `server/validators/optimized_security_validator.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*