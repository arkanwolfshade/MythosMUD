# Game Magic Spell

> 7 nodes

## Key Concepts

- **_deep_dict()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_parse_and_validate_inner_json_depth_exceeded()** (5 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_depth_exceeded()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **test_validate_json_structure_accepts_depth_equal_to_limit()** (4 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **Build {\"k\": {\"k\": ... \"leaf\": 1}} with `levels` nesting below root.** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **Inner JSON string is validated with the same depth limits as the outer object.** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`
- **Depth equal to max_json_depth is allowed (failure is strict `>`).** (1 connections) — `server/tests/unit/realtime/test_message_validator.py`

## Relationships

- [Database Helper Tests](Database_Helper_Tests.md) (7 shared connections)
- [Scenario Conversion Guide](Scenario_Conversion_Guide.md) (2 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_validator.py`

## Audit Trail

- EXTRACTED: 19 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*