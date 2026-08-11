# Cursor Plans Best

> 6 nodes

## Key Concepts

- **.validate_json_structure()** (7 connections) — `server/realtime/message_validator.py`
- **._validate_string_lengths()** (4 connections) — `server/realtime/message_validator.py`
- **._calculate_depth()** (3 connections) — `server/realtime/message_validator.py`
- **Validate JSON structure including depth limits.          Args:             me** (1 connections) — `server/realtime/message_validator.py`
- **Calculate the maximum nesting depth of a JSON structure.          Args:** (1 connections) — `server/realtime/message_validator.py`
- **Validate that strings in the JSON structure don't exceed length limits.** (1 connections) — `server/realtime/message_validator.py`

## Relationships

- [Database Helper Tests](Database_Helper_Tests.md) (3 shared connections)
- [Scenario Conversion Guide](Scenario_Conversion_Guide.md) (2 shared connections)
- [Security Issues And Fixes](Security_Issues_And_Fixes.md) (2 shared connections)

## Source Files

- `server/realtime/message_validator.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*